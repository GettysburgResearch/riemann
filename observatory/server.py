"""Single-user loopback server with isolated, bounded, cancellable numerical jobs."""
from __future__ import annotations
import asyncio
import json
import os
import importlib.util
import multiprocessing as mp
import time
import uuid
from contextlib import asynccontextmanager
from pathlib import Path
from urllib.parse import urlsplit
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import ValidationError
from engine import VERSION, Coordinate, Spec, compute, parse_spec
from artifacts import ArtifactStore, Investigation
from series_store import SeriesStore, SeriesImport
from identity import strict_loads

ROOT=Path(__file__).resolve().parent

def _worker(payload, pipe):
    try:
        pipe.send({"status":"done", "result":compute(payload)})
    except Exception as exc:
        pipe.send({"status":"error", "error":f"{type(exc).__name__}: {exc}"})
    finally:
        pipe.close()

class Jobs:
    def __init__(self, capacity=2, deadline=60.0):
        self.capacity, self.deadline, self.entries = capacity, deadline, {}
        self.context=mp.get_context("spawn")

    def stop(self, entry, status):
        p=entry["process"]
        if p.is_alive():
            p.terminate(); p.join(0.3)
            if p.is_alive():
                p.kill(); p.join(0.3)
        else:
            p.join(0)
        entry["pipe"].close()
        entry["status"]=status

    def sweep(self):
        now=time.monotonic()
        for entry in list(self.entries.values()):
            if entry["status"]!="running":
                continue
            if entry["pipe"].poll():
                try:
                    message=entry["pipe"].recv()
                    entry.update(message)
                    self.stop(entry,message["status"])
                except (EOFError,OSError):
                    self.stop(entry,"error"); entry["error"]="Worker exited without a result."
            elif now-entry["started"]>self.deadline:
                self.stop(entry,"timeout")
                entry["error"]="Compute budget exceeded; narrow the domain, grid or precision."
            elif not entry["process"].is_alive():
                self.stop(entry,"error"); entry["error"]="Worker exited without a result."
        finished=sorted((k for k,v in self.entries.items() if v["status"]!="running"), key=lambda k:self.entries[k]["started"])
        for k in finished:
            if len(finished)>8 or now-self.entries[k]["started"]>900:
                self.entries.pop(k,None)
                finished=finished[1:]

    def submit(self, payload):
        self.sweep()
        if sum(e["status"]=="running" for e in self.entries.values())>=self.capacity:
            raise HTTPException(429,"Two computations are already running. Cancel one or retry after it finishes.")
        rx, tx=self.context.Pipe(duplex=False)
        p=self.context.Process(target=_worker,args=(payload,tx),daemon=True)
        key=uuid.uuid4().hex
        p.start(); tx.close()
        self.entries[key]={"status":"running","started":time.monotonic(),"process":p,"pipe":rx}
        return {"job_id":key,"status":"running"}

    def read(self,key):
        self.sweep()
        e=self.entries.get(key)
        if e is None:
            raise HTTPException(404,"Unknown or expired job. Replay its saved request.")
        return {"job_id":key,"status":e["status"],"elapsed_seconds":round(time.monotonic()-e["started"],2),
                **({"result":e["result"]} if "result" in e else {}), **({"error":e["error"]} if "error" in e else {})}

    def cancel(self,key):
        if key not in self.entries:
            raise HTTPException(404,"Unknown job")
        if self.entries[key]["status"]=="running":
            self.stop(self.entries[key],"cancelled")
        return self.read(key)

    def close(self):
        for e in self.entries.values():
            if e["status"]=="running":
                self.stop(e,"cancelled")

jobs=Jobs()

@asynccontextmanager
async def lifespan(app):
    async def reap():
        while True:
            jobs.sweep()
            await asyncio.sleep(0.2)
    task=asyncio.create_task(reap())
    yield
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        pass
    jobs.close()

app=FastAPI(title="Riemann Observatory",version=VERSION,lifespan=lifespan,docs_url=None,redoc_url=None,openapi_url="/api/openapi.json")

@app.middleware("http")
async def local_boundary(request, call_next):
    host=request.headers.get("host","")
    try:
        hostname=urlsplit("//"+host).hostname
    except ValueError:
        hostname=None
    if hostname not in {"localhost","127.0.0.1","::1","testserver"}:
        return JSONResponse({"detail":"Local-only Observatory: use a loopback hostname or an SSH tunnel."},status_code=403)
    origin=request.headers.get("origin")
    try:
        foreign_origin = origin and urlsplit(origin).netloc != host
    except ValueError:
        foreign_origin = True
    if request.method not in {"GET","HEAD","OPTIONS"}:
        if request.headers.get("x-observatory-client")!="v0.1" or foreign_origin:
            return JSONResponse({"detail":"Same-origin client header required."},status_code=403)
    response=await call_next(request)
    response.headers["X-Content-Type-Options"]="nosniff"
    response.headers["Referrer-Policy"]="no-referrer"
    response.headers["Cache-Control"]="no-store"
    response.headers["Content-Security-Policy"]="default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data: blob:; connect-src 'self'; object-src 'none'; frame-ancestors 'none'; base-uri 'none'"
    return response

async def read_json(request, limit=16384):
    chunks=bytearray()
    async for chunk in request.stream():
        chunks.extend(chunk)
        if len(chunks)>limit:
            raise HTTPException(413,f"Request exceeds {limit} bytes")
    try:
        return strict_loads(bytes(chunks))
    except (ValueError, RecursionError) as exc:
        raise HTTPException(422,str(exc)) from exc

async def body(request, model):
    try:
        return model.model_validate(await read_json(request))
    except ValidationError as exc:
        raise HTTPException(422,str(exc)) from exc

_store = None
_series = None
_import_lock = asyncio.Lock()

def stores():
    global _store, _series
    if _store is None:
        root = Path(os.environ.get("OBSERVATORY_DATA_DIR", Path.home()/".riemann-observatory"))
        _store, _series = ArtifactStore(root), SeriesStore(root)
    return _store, _series

def storage_error(exc):
    return HTTPException(404 if isinstance(exc, FileNotFoundError) else 422, str(exc))

@app.get("/api/investigations")
async def list_investigations():
    return {"items": stores()[0].list()}

@app.post("/api/investigations", status_code=201)
async def save_investigation(request:Request):
    data = await read_json(request, 16*1024*1024)
    try:
        # Serialization/hash work runs off the event loop; one storage writer at a time.
        async with _import_lock:
            return await asyncio.to_thread(stores()[0].save, data)
    except (ValueError, KeyError, TypeError, RecursionError) as exc:
        raise storage_error(exc) from exc

@app.get("/api/investigations/{key}")
async def load_investigation(key:str):
    try:
        return await asyncio.to_thread(stores()[0].load, key)
    except (ValueError, FileNotFoundError, KeyError, TypeError) as exc:
        raise storage_error(exc) from exc

@app.get("/api/datasets")
async def list_datasets():
    return {"items": stores()[1].list()}

@app.post("/api/datasets", status_code=201)
async def import_dataset(request:Request):
    data = await read_json(request, 24*1024*1024)
    try:
        async with _import_lock:
            return await asyncio.to_thread(stores()[1].ingest, data)
    except (ValueError, KeyError, TypeError) as exc:
        raise storage_error(exc) from exc

@app.get("/api/datasets/{key}/view")
async def dataset_view(key:str, start:int=0, stop:int=1000, buckets:int=256):
    try:
        return await asyncio.to_thread(stores()[1].viewport, key, start, stop, buckets)
    except (ValueError, FileNotFoundError) as exc:
        raise storage_error(exc) from exc

@app.get("/api/datasets/{key}/sample/{index}")
async def dataset_sample(key:str,index:int):
    try:
        return stores()[1].sample(key,index)
    except (ValueError, FileNotFoundError) as exc:
        raise storage_error(exc) from exc

@app.get("/api/health")
async def health():
    return {"status":"ok","version":VERSION,"mode":"local-only","certified":False}

@app.get("/api/capabilities")
async def capabilities():
    from providers.contracts import MODELS
    return {"schema":Spec.model_json_schema(), "provider_schemas": {m.model_fields["module"].default: m.model_json_schema() for m in MODELS}, "flint_available": importlib.util.find_spec("flint") is not None,"deadline_seconds":jobs.deadline,"workers":jobs.capacity,
            "modules":["geometry","primes","euler","mobius","zeros","height", "cancellation", "sweep", "explicit", "refine", "family", "hierarchy"],
            "functions":["zeta","eta","xi","beta","chi3"],"huge_height_live_evaluation":False,
            "extensions":"Add a bounded Spec field and a pure provider to engine.PROVIDERS; add UI preset and tests."}

@app.post("/api/jobs",status_code=202)
async def submit(request:Request):
    try:
        spec=parse_spec(await read_json(request))
    except (ValidationError, ValueError) as exc:
        raise HTTPException(422,str(exc)) from exc
    return jobs.submit(spec.model_dump())

@app.get("/api/jobs/{key}")
async def read(key:str):
    return jobs.read(key)

@app.delete("/api/jobs/{key}")
async def cancel(key:str):
    return jobs.cancel(key)

@app.post("/api/coordinates")
async def coordinates(request:Request):
    q=await body(request,Coordinate)
    return {"anchor":q.anchor,"offset":q.offset,"exact_decimal":q.exact(),"arithmetic":"exact terminating decimal addition"}

app.mount("/",StaticFiles(directory=ROOT/"web",html=True),name="web")

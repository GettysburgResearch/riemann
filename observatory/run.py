"""Run from any working directory: python /path/to/observatory/run.py."""
from pathlib import Path
import argparse
import json
import sys

def main():
    parser=argparse.ArgumentParser(description="Riemann Observatory research preview: local research desk")
    parser.add_argument("--port",type=int,default=8765)
    parser.add_argument("--compute",type=Path,help="Run an experiment JSON (request or exported envelope), print result, then exit")
    parser.add_argument("--import-series",type=Path,help="Import a bounded sampled series JSON into the local indexed store")
    parser.add_argument("--data-dir",type=Path,help="Override local persistent store (default ~/.riemann-observatory)")
    args=parser.parse_args()
    import os
    if args.data_dir:
        os.environ["OBSERVATORY_DATA_DIR"] = str(args.data_dir)
    if args.import_series:
        from series_store import SeriesStore
        from identity import strict_loads
        root=Path(os.environ.get("OBSERVATORY_DATA_DIR", Path.home()/".riemann-observatory"))
        print(json.dumps(SeriesStore(root).ingest(strict_loads(args.import_series.read_bytes()))))
        return
    if args.compute:
        from engine import compute
        from identity import strict_loads
        payload=strict_loads(args.compute.read_bytes())
        print(json.dumps(compute(payload.get("result",payload).get("request",payload)),ensure_ascii=False,allow_nan=False))
        return
    if not 1024 <= args.port <= 65535:
        parser.error("Choose a port between 1024 and 65535")
    try:
        import uvicorn
    except ImportError:
        sys.exit("Install first: python -m pip install -r observatory/requirements.txt")
    print(f"Riemann Observatory → http://127.0.0.1:{args.port}\nLocal numerical scouts; not a certificate service. Ctrl+C to stop.")
    uvicorn.run("server:app",host="127.0.0.1",port=args.port,app_dir=str(Path(__file__).resolve().parent),workers=1)

if __name__=="__main__":
    main()

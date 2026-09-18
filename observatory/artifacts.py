"""Immutable content-addressed local results and a restart-safe investigation index."""
from __future__ import annotations
import json
import math
import os
import re
import sqlite3
import tempfile
from contextlib import contextmanager
from pathlib import Path
from pydantic import BaseModel, ConfigDict, Field
from identity import content_id, result_id, strict_loads

KEY = re.compile(r'^[0-9a-f]{64}$')


class Investigation(BaseModel):
    model_config = ConfigDict(extra='forbid', allow_inf_nan=False)
    schema_version: int = Field(2, ge=2, le=2)
    name: str = Field('Untitled investigation', max_length=120)
    notes: str = Field('', max_length=12000)
    result: dict
    comparison: dict | None = None
    refinements: list[dict] = Field(default_factory=list, max_length=16)
    selection: dict | None = None
    viewports: list[dict] = Field(default_factory=list, max_length=24)
    comparison_view: dict | None = None


def verify_result(value):
    from engine import parse_spec
    if not isinstance(value, dict) or not KEY.fullmatch(str(value.get('result_id', ''))):
        raise ValueError('Missing or malformed result identity')
    if result_id(value) != value['result_id']:
        raise ValueError('Artifact integrity mismatch; data or producer metadata changed')
    q = parse_spec(value.get('request', {}))
    if not isinstance(value.get('series'), list) or not isinstance(value.get('events'), list):
        raise ValueError('Artifact is missing its series/event contract')
    if not isinstance(value.get('warnings'), list) or not isinstance(value.get('formula'), str):
        raise ValueError('Artifact is missing its numerical boundary')
    # Bound renderer-facing shapes independently of the hash. A hash only
    # protects integrity, not whether an uploaded author chose sensible data.
    def vector(obj, length=None):
        if not isinstance(obj, list) or len(obj)>250000 or (length is not None and len(obj)!=length):
            raise ValueError('Invalid or excessive numerical vector shape')
        if any(v is not None and (isinstance(v,bool) or not isinstance(v,(int,float)) or not math.isfinite(v)) for v in obj):
            raise ValueError('Numerical vectors must contain finite numbers or missing markers')
    if len(value['series'])>32 or len(value['events'])>10000:
        raise ValueError('Too many series or events')
    for curve in value['series']:
        if not isinstance(curve,dict) or not isinstance(curve.get('label'),str) or len(curve.get('points',[]))>250000:
            raise ValueError('Invalid curve descriptor')
        for point in curve.get('points',[]):
            vector(point,2)
            if point[0] is None:
                raise ValueError('A plot coordinate cannot be missing')
    grid=value.get('grid')
    if grid is not None:
        n=grid.get('n')
        if type(n) is not int or not 1<=n<=192 or grid.get('kind') not in {'interaction','complex'}:
            raise ValueError('Invalid or excessive grid shape')
        vector(grid.get('x'),n);vector(grid.get('y'),n)
        if grid['kind']=='interaction':
            vector(grid.get('values'),n*n)
        else:
            for key in ('real','imag','magnitude','phase'):
                vector(grid.get(key),n*n)
    if q.module=='cancellation':
        n=q.n
        for side in 'ab':
            data=value['experiments'][side]
            for key in ('weights','rows','prefix_energy','coefficients'): vector(data[key],n)
            vector(data['matrix'],n*n)
        spectrum=value['spectrum'];vector(spectrum['eigenvalues'],n)
        if len(spectrum['vectors'])!=n: raise ValueError('Invalid eigensystem shape')
        for row in spectrum['vectors']: vector(row,n)
    if q.module=='explicit':
        if len(value['focus']['prime_terms'])>q.prime_cutoff or len(value['focus']['zero_terms'])!=q.zero_count:
            raise ValueError('Invalid explicit-formula term coverage shape')
    if q.module=='sweep':
        if len(value['trials'])>q.width_steps*q.split_steps or len(value['widths'])!=q.width_steps or len(value['splits'])>q.split_steps:
            raise ValueError('Invalid bounded sweep shape')
    if q.module=='family' and len(value['members'])!=len(q.discriminants):
        raise ValueError('Invalid family member count')
    if q.module=='hierarchy' and len(value['families'])!=q.depth+1:
        raise ValueError('Invalid sequence-family count')
    return value


class ArtifactStore:
    def __init__(self, root):
        self.root = Path(root).expanduser().resolve()
        self.objects = self.root/'objects'
        self.objects.mkdir(parents=True, exist_ok=True)
        with self.connection() as db:
            db.execute('CREATE TABLE IF NOT EXISTS investigations (id TEXT PRIMARY KEY, name TEXT NOT NULL, created TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP)')

    @contextmanager
    def connection(self):
        db = sqlite3.connect(self.root/'index.sqlite3', timeout=10)
        try:
            db.execute('PRAGMA journal_mode=WAL')
            with db:
                yield db
        finally:
            db.close()

    def path(self, key):
        if not isinstance(key, str) or not KEY.fullmatch(key):
            raise ValueError('Expected a 64-character content identity')
        return self.objects/(key+'.json')

    def put(self, key, value):
        path = self.path(key)
        raw = json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()
        if path.exists():
            existing = strict_loads(path.read_bytes())
            if content_id(existing) != content_id(value):
                raise ValueError('Existing immutable artifact is corrupted or conflicts with this identity')
            return
        fd, tmp = tempfile.mkstemp(prefix='.pending-', dir=self.objects)
        try:
            with os.fdopen(fd, 'wb') as f:
                f.write(raw)
                f.flush()
                os.fsync(f.fileno())
            os.replace(tmp, path)
        finally:
            if os.path.exists(tmp):
                os.unlink(tmp)

    def read(self, key):
        path = self.path(key)
        if not path.exists():
            raise FileNotFoundError(key)
        return strict_loads(path.read_bytes())

    def save(self, investigation):
        q = Investigation.model_validate(investigation)
        r = verify_result(q.result)
        comparison = verify_result(q.comparison) if q.comparison is not None else None
        refinements = [verify_result(v) for v in q.refinements]
        for value in [r, *([comparison] if comparison else []), *refinements]:
            self.put(value['result_id'], value)
        record = q.model_dump(exclude={'result', 'comparison', 'refinements'})
        record.update(result_id=r['result_id'], comparison_id=comparison['result_id'] if comparison else None,
                      refinement_ids=[v['result_id'] for v in refinements],
                      trust='Integrity checked; imported metadata is not independent source authentication or mathematical certification.')
        key = content_id(record)
        self.put(key, record)
        with self.connection() as db:
            db.execute('INSERT OR IGNORE INTO investigations(id,name) VALUES(?,?)', (key, q.name))
        return {'investigation_id': key, 'result_id': r['result_id'], 'comparison_id': record['comparison_id']}

    def load(self, key):
        record = self.read(key)
        if content_id(record) != key:
            raise ValueError('Investigation manifest integrity mismatch')
        r = verify_result(self.read(record['result_id']))
        comparison = verify_result(self.read(record['comparison_id'])) if record['comparison_id'] else None
        refinements = [verify_result(self.read(k)) for k in record['refinement_ids']]
        data = {k: v for k, v in record.items() if k not in {'result_id', 'comparison_id', 'refinement_ids', 'trust'}}
        data.update(result=r, comparison=comparison, refinements=refinements)
        Investigation.model_validate(data)
        return {'investigation_id': key, 'trust': record['trust'], 'experiment': data}

    def list(self, limit=50):
        with self.connection() as db:
            return [{'investigation_id': row[0], 'name': row[1], 'created': row[2]}
                    for row in db.execute('SELECT id,name,created FROM investigations ORDER BY created DESC,id LIMIT ?', (min(max(limit, 1), 200),))]

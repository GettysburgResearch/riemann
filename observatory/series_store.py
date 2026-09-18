"""Bounded stored-series importer and indexed multiresolution viewport queries.

The horizontal query coordinate is ORIGINAL SAMPLE INDEX, not a silently rounded
huge height. Exact anchor/offset strings survive per-sample and per-event inspection.
Stored summaries are first/min/max/last with signed/absolute sums. Missing runs and
registered events have independent indices; neither disappears with line reduction.
"""
from __future__ import annotations
import json
import math
import os
import sqlite3
import uuid
from contextlib import contextmanager
from decimal import Decimal, localcontext
from pathlib import Path
from pydantic import BaseModel, ConfigDict, Field, model_validator
from identity import content_id, strict_loads
from artifacts import KEY

class Sample(BaseModel):
    model_config = ConfigDict(extra='forbid', allow_inf_nan=False)
    offset: str = Field(pattern=r'^-?\d{1,40}(\.\d{1,60})?$', max_length=102)
    value: float | None

class Event(BaseModel):
    model_config = ConfigDict(extra='forbid')
    index: int = Field(ge=0, le=249999)
    label: str = Field(max_length=160)
    status: str = Field('imported, unverified', max_length=160)

class SeriesImport(BaseModel):
    model_config = ConfigDict(extra='forbid', allow_inf_nan=False)
    name: str = Field(max_length=120)
    provenance: str = Field(min_length=1, max_length=2000)
    anchor: str = Field('0', pattern=r'^-?\d{1,100}$', max_length=101)
    unit: str = Field('', max_length=80)
    samples: list[Sample] = Field(min_length=2, max_length=250000)
    events: list[Event] = Field(default_factory=list, max_length=10000)
    coverage: str = Field('Sampled/imported data only; mathematical event completeness is unknown.', max_length=2000)

    @model_validator(mode='after')
    def coordinates(self):
        previous = None
        for sample in self.samples:
            current = Decimal(sample.offset)
            if previous is not None and current <= previous:
                raise ValueError('Sample offsets must be strictly increasing exact decimals; duplicates require an explicit preprocessing decision.')
            previous = current
        if any(e.index >= len(self.samples) for e in self.events):
            raise ValueError('Event index is outside the sample array')
        return self


def leaf(i, sample):
    value = sample.value
    pair = [i, value] if value is not None else None
    return {'lo': i, 'hi': i+1, 'count': int(value is not None), 'missing': int(value is None),
            'sum': value or 0.0, 'absolute_sum': abs(value) if value is not None else 0.0,
            'first': pair, 'last': pair, 'min': pair, 'max': pair}


def merge(left, right):
    good = [v for v in (left, right) if v['count']]
    return {'lo': left['lo'], 'hi': right['hi'], 'count': left['count']+right['count'],
            'missing': left['missing']+right['missing'], 'sum': math.fsum([left['sum'], right['sum']]),
            'absolute_sum': math.fsum([left['absolute_sum'], right['absolute_sum']]),
            'first': good[0]['first'] if good else None, 'last': good[-1]['last'] if good else None,
            'min': min((v['min'] for v in good), key=lambda p: (p[1], p[0])) if good else None,
            'max': max((v['max'] for v in good), key=lambda p: (p[1], -p[0])) if good else None}


class SeriesStore:
    def __init__(self, root):
        self.root = Path(root)/'series'
        self.root.mkdir(parents=True, exist_ok=True)

    def path(self, key):
        if not isinstance(key, str) or not KEY.fullmatch(key):
            raise ValueError('Invalid dataset identity')
        return self.root/(key+'.sqlite3')

    def ingest(self, payload):
        q = SeriesImport.model_validate(payload)
        key = content_id(q.model_dump())
        path = self.path(key)
        if path.exists():
            return self.info(key)
        tmp = self.root/(key+f'.{uuid.uuid4().hex}.pending')
        try:
            db = sqlite3.connect(tmp)
            with db:
                db.executescript('''
                CREATE TABLE meta(id INTEGER PRIMARY KEY, payload TEXT, hash TEXT);
                CREATE TABLE samples(i INTEGER PRIMARY KEY, offset TEXT, value REAL, hash TEXT);
                CREATE TABLE nodes(level INTEGER, slot INTEGER, lo INTEGER, hi INTEGER, payload TEXT, hash TEXT, PRIMARY KEY(level,slot));
                CREATE TABLE gaps(lo INTEGER PRIMARY KEY, hi INTEGER, hash TEXT);
                CREATE TABLE events(id INTEGER PRIMARY KEY, i INTEGER, payload TEXT, hash TEXT);
                CREATE INDEX event_position ON events(i);
                ''')
                meta = q.model_dump(exclude={'samples', 'events'})
                meta.update(dataset_id=key, sample_count=len(q.samples), event_count=len(q.events), schema_version=1)
                db.execute('INSERT INTO meta VALUES(1,?,?)', (json.dumps(meta), content_id(meta)))
                db.executemany('INSERT INTO samples VALUES(?,?,?,?)', ((i, s.offset, s.value, content_id([i, s.offset, s.value])) for i, s in enumerate(q.samples)))
                gap = None
                for i, s in enumerate(q.samples):
                    if s.value is None and gap is None:
                        gap = i
                    if s.value is not None and gap is not None:
                        db.execute('INSERT INTO gaps VALUES(?,?,?)', (gap, i, content_id([gap,i])))
                        gap = None
                if gap is not None:
                    db.execute('INSERT INTO gaps VALUES(?,?,?)', (gap, len(q.samples), content_id([gap,len(q.samples)])))
                for i, event in enumerate(q.events):
                    data = event.model_dump()
                    db.execute('INSERT INTO events VALUES(?,?,?,?)', (i, event.index, json.dumps(data), content_id(data)))
                # Base summaries over blocks of 32. Partial viewport blocks are
                # reconstructed from original samples; coarser levels are persistent.
                nodes = []
                for start in range(0, len(q.samples), 32):
                    node = leaf(start, q.samples[start])
                    for i in range(start+1, min(start+32, len(q.samples))):
                        node = merge(node, leaf(i, q.samples[i]))
                    nodes.append(node)
                level = 0
                while nodes:
                    db.executemany('INSERT INTO nodes VALUES(?,?,?,?,?,?)',
                                   ((level, i, n['lo'], n['hi'], json.dumps(n), content_id(n)) for i, n in enumerate(nodes)))
                    if len(nodes) == 1:
                        break
                    nodes = [merge(nodes[i], nodes[i+1]) if i+1 < len(nodes) else nodes[i]
                             for i in range(0, len(nodes), 2)]
                    level += 1
            db.close()
            os.replace(tmp, path)
        finally:
            if "db" in locals():
                db.close()
            if tmp.exists():
                tmp.unlink()
        return self.info(key)

    @contextmanager
    def connect(self, key):
        path = self.path(key)
        if not path.exists():
            raise FileNotFoundError(key)
        db = sqlite3.connect(f'{path.as_uri()}?mode=ro', uri=True)
        try:
            yield db
        finally:
            db.close()

    def info(self, key):
        with self.connect(key) as db:
            raw, checksum = db.execute('SELECT payload,hash FROM meta WHERE id=1').fetchone()
        obj = strict_loads(raw)
        if content_id(obj) != checksum or obj['dataset_id'] != key:
            raise ValueError('Dataset metadata integrity mismatch')
        return obj

    def list(self):
        return [self.info(path.stem) for path in sorted(self.root.glob('*.sqlite3'))][:100]

    def sample(self, key, index):
        with self.connect(key) as db:
            row = db.execute('SELECT offset,value,hash FROM samples WHERE i=?', (index,)).fetchone()
        if row is None:
            raise ValueError('Sample index out of range')
        if content_id([index, row[0], row[1]]) != row[2]:
            raise ValueError('Stored sample integrity mismatch')
        anchor = self.info(key)['anchor']
        with localcontext() as ctx:
            ctx.prec = 200
            exact = format(Decimal(anchor)+Decimal(row[0]), 'f')
        return {'index': index, 'offset': row[0], 'value': row[1], 'anchor': anchor, 'exact_decimal': exact}

    def viewport(self, key, start, stop, buckets=256):
        info = self.info(key)
        if not 0 <= start < stop <= info['sample_count'] or not 8 <= buckets <= 1024:
            raise ValueError('Invalid viewport bounds or bucket budget')
        span = stop-start
        target = max(32, math.ceil(span/buckets))
        level = max(0, int(math.log2(target/32)))
        width = 32*(2**level)
        nodes, rows_read = [], 0
        with self.connect(key) as db:
            for slot in range(start//width, (stop-1)//width+1):
                lo, hi = max(start, slot*width), min(stop, (slot+1)*width)
                found = db.execute('SELECT lo,hi,payload,hash FROM nodes WHERE level=? AND slot=?', (level, slot)).fetchone()
                if found is not None and found[0] == lo and found[1] == hi:
                    node = strict_loads(found[2])
                    if content_id(node) != found[3]:
                        raise ValueError('Stored summary integrity mismatch')
                    nodes.append(node)
                else:
                    rows = db.execute('SELECT i,offset,value,hash FROM samples WHERE i>=? AND i<? ORDER BY i', (lo, hi)).fetchall()
                    rows_read += len(rows)
                    node = None
                    for i, offset, value, checksum in rows:
                        if content_id([i, offset, value]) != checksum:
                            raise ValueError('Stored sample integrity mismatch')
                        part = leaf(i, Sample(offset=offset, value=value))
                        node = merge(node, part) if node else part
                    if node:
                        nodes.append(node)
            gap_rows = db.execute('SELECT lo,hi,hash FROM gaps WHERE lo<? AND hi>? ORDER BY lo', (stop, start)).fetchall()
            if any(content_id([lo,hi]) != checksum for lo,hi,checksum in gap_rows):
                raise ValueError('Stored gap integrity mismatch')
            gaps = [[max(start,lo), min(stop,hi)] for lo,hi,_ in gap_rows]
            events = []
            for raw, checksum in db.execute('SELECT payload,hash FROM events WHERE i>=? AND i<? ORDER BY i,id', (start, stop)):
                event = strict_loads(raw)
                if content_id(event) != checksum:
                    raise ValueError('Stored event integrity mismatch')
                events.append(event)
        points = {p[0]: p for n in nodes for p in (n['first'], n['min'], n['max'], n['last']) if p}
        # Insert an explicit gap marker even if the reduced curve has no retained
        # original sample inside the gap. Gap runs themselves remain independently visible.
        for lo, hi in gaps:
            points[lo] = [lo, None]
            if hi < stop:
                row = self.sample(key, hi)
                points[hi] = [hi, row['value']]
        return {'dataset': info, 'start': start, 'stop': stop, 'level': level, 'raw_rows_read': rows_read,
                'points': [points[k] for k in sorted(points)], 'envelopes': nodes, 'gaps': gaps, 'events': events,
                'finite_count': sum(n['count'] for n in nodes), 'missing_count': sum(n['missing'] for n in nodes),
                'signed_sum': math.fsum(n['sum'] for n in nodes),
                'absolute_sum': math.fsum(n['absolute_sum'] for n in nodes),
                'contract': 'Viewport uses original sample indices. Stored sampled extrema and floating sums; independent gaps/events. Output can exceed the nominal vertex budget when many gaps/events must be retained. Not a continuous bound.'}

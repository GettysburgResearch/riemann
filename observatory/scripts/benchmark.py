"""Finite, repeatable LOD stress test. A runtime observation, not a scale guarantee."""
import json
import sys
import time
import tracemalloc
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from engine import reduce_series
n=1_000_000
xs=list(range(n));ys=[1 if i%2 else -1 for i in xs];ys[543217]=10**6
tracemalloc.start();start=time.perf_counter()
r=reduce_series(xs,ys,1000)
elapsed=time.perf_counter()-start
_,peak=tracemalloc.get_traced_memory()
assert [543217,1_000_000] in r['points']
assert len(r['points'])<=4000
assert sum(b['count'] for b in r['envelopes'])==n
assert sum(b['sum'] for b in r['envelopes'])==sum(ys)
print(json.dumps({'input_samples':n,'display_vertices':len(r['points']),'buckets':len(r['envelopes']),'spike_preserved':True,'elapsed_seconds':elapsed,'additional_traced_bytes':peak,'scope':'Python summary only; source arrays allocated before memory tracing; not an end-to-end million-point UI benchmark.'},indent=2))

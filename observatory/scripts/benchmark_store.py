"""Bounded indexed-data benchmark. Reports stored-query work, not GPU/frame rate."""
import argparse
import json
import platform
import sys
import tempfile
import time
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from series_store import SeriesStore


def main():
    p=argparse.ArgumentParser();p.add_argument('--samples',type=int,default=100000);p.add_argument('--output',type=Path);a=p.parse_args()
    if not 2000<=a.samples<=250000: p.error('Choose 2000..250000 samples')
    n=a.samples;spike=n*3//4;gap=n//2
    data={'name':'bounded benchmark','provenance':'synthetic alternating samples; one injected spike and a missing run',
          'anchor':'763173730199776587433631628770',
          'samples':[{'offset':f'{i//1000000}.{i%1000000:06d}','value':None if gap<=i<gap+3 else 1000 if i==spike else (-1)**i} for i in range(n)],
          'events':[{'index':spike,'label':'synthetic spike'}]}
    with tempfile.TemporaryDirectory() as folder:
        store=SeriesStore(folder);t=time.perf_counter();meta=store.ingest(data);build=time.perf_counter()-t
        key=meta['dataset_id'];t=time.perf_counter();full=store.viewport(key,0,n,256);full_time=time.perf_counter()-t
        t=time.perf_counter();local=store.viewport(key,spike-400,spike+401,64);local_time=time.perf_counter()-t
        assert [spike,1000.0] in full['points'] and [spike,1000.0] in local['points']
        assert full['missing_count']==3 and len(full['events'])==1
        assert full['finite_count']==n-3
        report={'python':platform.python_version(),'platform':platform.platform(),'samples':n,'dataset_id':key,
                'ingest_seconds':build,'full_view_seconds':full_time,'local_view_seconds':local_time,
                'full_view_vertices':len(full['points']),'full_view_raw_boundary_rows':full['raw_rows_read'],
                'local_view_raw_boundary_rows':local['raw_rows_read'],'sqlite_bytes':store.path(key).stat().st_size,
                'spike_retained':True,'gap_retained':True,'event_retained':True,
                'scope':'One bounded synthetic stored-data benchmark. Not a browser frame-rate or billion-point benchmark.'}
        print(json.dumps(report,indent=2))
        if a.output:a.output.write_text(json.dumps(report,indent=2)+'\n')

if __name__=='__main__':main()

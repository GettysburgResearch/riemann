"""Reconstruct both complete reports, authenticate receipts, and cross-check."""
import argparse
import hashlib
import json
from pathlib import Path
import transport
import family
import verify

ROOT=Path(__file__).resolve().parent


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',type=Path,default=ROOT/'reports')
    args=ap.parse_args()
    expected=transport.strict_read(ROOT/'EXPECTED.json')
    transport.require(expected['schema']=='STC26-receipts-1','receipt schema')
    reports={'transport':transport.build(),'family':family.build()}
    texts={k:transport.canonical(v) for k,v in reports.items()}
    for k,text in texts.items():
        digest=hashlib.sha256(text.encode()).hexdigest()
        transport.require(digest==expected[k+'_sha256'],k+' semantic digest mismatch')
    count=verify.verify(json.loads(texts['transport']))
    transport.require(count==expected['matched_triples'],'triple count')
    for key in ('signatures','coefficient_comparisons'):
        transport.require(reports['family'][key]==expected['family_'+key],key)
    args.output.mkdir(parents=True,exist_ok=True)
    for k,text in texts.items():(args.output/(k+'.json')).write_text(text+'\n')
    print('STC26 replay PASS:',count,'matched triples;',reports['family']['signatures'],'family signatures')


if __name__=='__main__':main()

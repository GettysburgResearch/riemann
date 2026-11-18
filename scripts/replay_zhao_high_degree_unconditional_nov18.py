"""Reproduce the unconditional sign census from the extracted LMFDB snapshot."""
import argparse
import io
import json
import lzma
from pathlib import Path

from flint import ctx
from check_zhao_analytic_candidates_nov18 import select
from check_zhao_field_cuts_nov18 import PARAMS, cap
from check_zhao_field_threshold_nov18 import process


def record(raw):
    rows=list(map(json.loads,raw.splitlines()))
    verdict={label:v for label,v,_ in rows}
    if len(verdict)!=len(rows):
        raise ArithmeticError("Duplicate sign records")
    return verdict


def replay(catalog,degree):
    rows=[]
    for r2,vals in enumerate(PARAMS[degree]):
        if vals is None or degree==7 and r2<2 or degree==8 and r2<4:
            continue
        bound=cap(degree,r2,*vals)
        group=json.loads((catalog/f'n{degree}-r{r2}.json').read_text())
        rows.extend(row for row in group if int(row['label'].split('.')[2])<=bound)
    candidates=select(rows,127)
    stream=io.StringIO()
    process(candidates,'.001' if degree==8 else '.03',stream)
    raw=stream.getvalue()
    verdict=record(raw)
    if set(verdict)!={r["label"] for r in candidates}:
        raise ArithmeticError("Incomplete interval census")
    second=[r for r in candidates if verdict[r['label']] is None]
    if second:
        stream=io.StringIO()
        process(second,'.000001',stream)
        extra=stream.getvalue()
        refined=record(extra)
        if set(refined)!={r["label"] for r in second}:
            raise ArithmeticError("Incomplete refinement")
        verdict.update(refined)
        raw+=extra
    if None in verdict.values():
        raise ArithmeticError("Unresolved analytic comparison")
    root=Path(__file__).resolve().parents[1]
    archive=root/'experiments/X-nov18-field-criterion'/f'degree-{degree}.jsonl.xz'
    stored={label:v for label,v,_ in map(json.loads,lzma.decompress(archive.read_bytes()).splitlines())}
    if stored!=verdict:
        raise ArithmeticError("Archived outcomes differ")
    name='quintic' if degree==5 else f'degree{degree}'
    inventory=json.loads((root/f'research/explorations/zhao-{name}-fields-nov18.json').read_text())
    listed={f.get('lmfdb_label',f['label']) for g in inventory['groups'] for f in g['passing_fields']}
    if listed!={k for k,v in verdict.items() if v}:
        raise ArithmeticError("Does not match the independent spectral inventory")
    print(degree,len(rows),len(candidates),len(second),len(listed))


if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('extracted_catalogue',type=Path)
    ap.add_argument('degree',type=int,choices=[5,6,7,8])
    args=ap.parse_args()
    ctx.prec=150
    replay(args.extracted_catalogue,args.degree)

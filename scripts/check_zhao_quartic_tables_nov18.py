"""Group the corrected Bordeaux quartic tables and verify enumeration up to isomorphism."""
import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path
from check_zhao_cubic_fields_nov18 import run_gp
from check_zhao_quartic_fields_nov18 import BOUNDS, GROUPS, polynomial

SOURCE={
    0:("T44.gp",13073,"3bccbff159603e755e9a959946591b18568eb68be4b239c13e14059cb3f0bff8"),
    1:("T42.gp",90671,"b21325a5bed0af9b05914c52755e7d2e5fcae34b7779b142d6ec383206935c89"),
    2:("T40.gp",81322,"d67683842bf75eeaa03103dbedbbe37cfeeb93d8e5e99eb8bbab9c610876acb8"),
}


def get_groups(table_dir,r):
    filename,nrows,sha=SOURCE[r]
    data=(table_dir/filename).read_bytes()
    if hashlib.sha256(data).hexdigest()!=sha or len(data.splitlines())!=nrows:
        raise ValueError(f"Unrecognized Bordeaux source {filename}")
    rows=[]
    for line in data.splitlines():
        d,c,_,_=json.loads(line)
        if abs(d)<=BOUNDS[r]:
            rows.append([r,d,c])
    groups=defaultdict(list)
    for start in range(0,len(rows),512):
        sub=rows[start:start+512]
        polys=','.join(polynomial(row[2]) for row in sub)
        orders=run_gp(f'V=[{polys}];\nfor(i=1,#V,print(polgalois(V[i])[1]));\n')
        if len(orders)!=len(sub):
            raise ArithmeticError("Incomplete field group data")
        for row,order in zip(sub,orders):
            group={4:"abelian",8:"D4",12:"A4",24:"S4"}[order]
            groups[group].append(row)
    return groups


def compare_fields(table,enumerated):
    # A maximal-order discriminant identifies an isolated table entry.
    # For repeated discriminants compare canonical reduced polynomial multisets.
    def blocks(rows):
        d=defaultdict(list)
        for r,disc,c in rows:
            d[r,disc].append(c)
        return d
    ref,got=blocks(table),blocks(enumerated)
    if {k:len(v) for k,v in ref.items()}!={k:len(v) for k,v in got.items()}:
        raise ValueError("Different field multiplicities at some discriminant")
    pairs=[(k,p,side) for k in ref if len(ref[k])>1 for side,v in enumerate((ref,got)) for p in v[k]]
    reduced=defaultdict(lambda:[[],[]])
    for start in range(0,len(pairs),256):
        sub=pairs[start:start+256]
        v=','.join(polynomial(p) for _,p,_ in sub)
        canon=run_gp(f'V=[{v}];\nfor(i=1,#V,print(Vec(polredabs(V[i]))));\n')
        if len(canon)!=len(sub):
            raise ArithmeticError("Missing quartic canonical forms")
        for (k,_,side),c in zip(sub,canon):
            reduced[k][side].append(c)
    if any(sorted(a)!=sorted(b) for a,b in reduced.values()):
        raise ArithmeticError("Non-isomorphic field inventories")
    return len(pairs)//2


if __name__=="__main__":
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--table-dir",type=Path,required=True)
    ap.add_argument("--output-dir",type=Path,required=True)
    ap.add_argument("--compare-nflist-dir",type=Path)
    args=ap.parse_args()
    for r in range(3):
        groups=get_groups(args.table_dir,r)
        print("Bordeaux",r,{k:len(v) for k,v in groups.items()},flush=True)
        for g in GROUPS:
            rows=groups[g]
            path=args.output_dir/f"quartic-{g}-{r}.jsonl"
            path.write_text(''.join(json.dumps(x,separators=(',',':'))+'\n' for x in rows))
            if args.compare_nflist_dir:
                ref=args.compare_nflist_dir/f"quartic-{g}-{r}.jsonl"
                if ref.exists():
                    earlier=[json.loads(x) for x in ref.read_text().splitlines()]
                    n=compare_fields(rows,earlier)
                    print("matched",g,r,len(rows),n,flush=True)

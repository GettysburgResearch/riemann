"""Authenticate a frozen packet, reconstruct its bounded claims, compare strictly."""
from pathlib import Path
import hashlib,json,sys,argparse
ROOT=Path(__file__).resolve().parent
FILES={'PROOF.md','README.md','REVIEW.md','SOURCES.json','VALIDATION.md',
       'interval_core.py','reconstruct.py','check.py','test_check.py','result.json','SHA256SUMS'}

def strict_load(text):
    def pairs(items):
        ans={}
        for key,value in items:
            if key in ans: raise ValueError('duplicate JSON key')
            ans[key]=value
        return ans
    def nofloat(_): raise ValueError('floating JSON number is not allowed')
    return json.loads(text,object_pairs_hook=pairs,parse_float=nofloat,parse_constant=nofloat)

def typed_equal(a,b):
    if type(a) is not type(b): return False
    if isinstance(a,dict):return a.keys()==b.keys() and all(typed_equal(a[k],b[k]) for k in a)
    if isinstance(a,list):return len(a)==len(b) and all(typed_equal(x,y) for x,y in zip(a,b))
    return a==b

def authenticate():
    actual={p.name for p in ROOT.iterdir()}
    if actual!=FILES:raise ValueError('packet inventory differs')
    for p in ROOT.iterdir():
        if p.is_symlink() or not p.is_file():raise ValueError('nonregular packet member')
    rows=(ROOT/'SHA256SUMS').read_text().splitlines();seen=set()
    for row in rows:
        h,name=row.split('  ',1)
        if name in seen or name not in FILES-{'SHA256SUMS'}:raise ValueError('bad manifest entry')
        if hashlib.sha256((ROOT/name).read_bytes()).hexdigest()!=h:raise ValueError('hash mismatch '+name)
        seen.add(name)
    if seen!=FILES-{'SHA256SUMS'}:raise ValueError('incomplete manifest')

def run(path):
    authenticate()
    supplied=strict_load(Path(path).read_text())
    sys.path.insert(0,str(ROOT))
    from reconstruct import reconstruct
    rebuilt=reconstruct()
    if not typed_equal(supplied,rebuilt):raise ValueError('bounded reconstruction differs')
    canonical=json.dumps(rebuilt,sort_keys=True,separators=(',',':')).encode()
    print('PASS_BJR26_BOUNDED_RECONSTRUCTION '+hashlib.sha256(canonical).hexdigest())
    print('ANALYTIC_REVIEW_REQUIRED; RH_NOT_PROVED; NO_DOUBLE_COLLISION_CERTIFICATE')
    return rebuilt

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--check',default=str(ROOT/'result.json'))
    args=parser.parse_args()
    try:run(args.check)
    except (ValueError,TypeError,KeyError,OSError,ZeroDivisionError) as exc:
        print('REJECT_BJR26: '+str(exc),file=sys.stderr);sys.exit(1)

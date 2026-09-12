"""Authenticate the fixed packet, then reconstruct its complete source certificate.
The manifest is an integrity baseline, not independent mathematical validation.
"""
from pathlib import Path
from fractions import Fraction
import argparse, hashlib, json, re, sys
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
NAMES=('PROOF.md','README.md','REVIEW.md','SOURCES.json','VALIDATION.md',
       'intervals.py','certificate.py','check.py','test_check.py','result.json','SHA256SUMS')
KEYS={'schema','rh_proved','cofinal_height_confinement_proved','source',
      'all_depths_from','window_height','positive_height_zero_count','normalization',
      'grid','cutoffs','degree_in_squared_variable','scale','bits',
      'theta_node_evaluations','bounds','polynomial_coefficients','contours','root_slopes'}

def canonical(x):return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=True)
def unique(pairs):
    d={}
    for k,v in pairs:
        if k in d:raise ValueError('duplicate JSON key')
        d[k]=v
    return d

def read_json(path):
    def no_float(_):raise ValueError('noninteger JSON number')
    p=Path(path)
    if p.is_symlink() or not p.is_file():raise ValueError('missing/linked receipt')
    return json.loads(p.read_text(encoding='utf-8'),object_pairs_hook=unique,
                      parse_float=no_float,parse_constant=no_float)

def authenticate(root=HERE):
    root=Path(root)
    if set(p.name for p in root.iterdir())!=set(NAMES):raise ValueError('packet inventory')
    for name in NAMES:
        p=root/name
        if p.is_symlink() or not p.is_file():raise ValueError('regular-file requirement: '+name)
    rows=(root/'SHA256SUMS').read_text(encoding='ascii').splitlines()
    expected=set(NAMES)-{'SHA256SUMS'};seen=set()
    for row in rows:
        m=re.fullmatch(r'([0-9a-f]{64})  ([A-Za-z0-9_.]+)',row)
        if not m:raise ValueError('malformed manifest')
        digest,name=m.groups()
        if name not in expected or name in seen:raise ValueError('manifest coverage')
        seen.add(name)
        if hashlib.sha256((root/name).read_bytes()).hexdigest()!=digest:raise ValueError('hash mismatch: '+name)
    if seen!=expected:raise ValueError('missing manifest entry')
    sources=read_json(root/'SOURCES.json')
    if sources.get('base_commit')!='e1a782cffaafbc9cc228273ed94ce63ae0407632':raise ValueError('frozen base drift')
    if sources.get('packet_id')!='BPW26':raise ValueError('source identity')

def preflight(r):
    if type(r) is not dict or set(r)!=KEYS:raise ValueError('receipt schema')
    for name in ('rh_proved','cofinal_height_confinement_proved'):
        if r[name] is not False:raise ValueError('false closure claim or type')
    for name,val in [('all_depths_from',32),('window_height',30),('positive_height_zero_count',3),
                     ('grid',32768),('degree_in_squared_variable',120),('scale',32),
                     ('bits',256),('theta_node_evaluations',57347)]:
        if type(r[name]) is not int or r[name]!=val:raise ValueError('integer coverage: '+name)
    if r['schema']!='BPW26-1' or r['cutoffs']!=['2','1','1/2']:raise ValueError('source cutoffs')
    if r['source']!='literal Gamma(5/2) shared-uniform branching orbit':raise ValueError('source convention')
    if r['normalization']!='H_n(1/2+i z); same critical-strip zeros as E_n':raise ValueError('normalization')
    if type(r['bounds']) is not dict or set(r['bounds'])!={'simpson','time_tail','index_tail','cosine_tail','model_error','orbit_error','fourth_derivative_bound'}:raise ValueError('incomplete tails')
    for s in r['bounds'].values():
        if type(s) is not str or Fraction(s)<=0:raise ValueError('positive exact bound')
    c=r['polynomial_coefficients']
    if type(c) is not list or len(c)!=121:raise ValueError('polynomial coverage')
    for q in c:
        if type(q) is not list or len(q)!=2 or any(type(x) is not str for x in q):raise ValueError('interval format')
        lo,hi=(int(x,16) for x in q)
        if lo<0 or lo>hi:raise ValueError('interval orientation')
    if type(r['contours']) is not list or len(r['contours'])!=4:raise ValueError('whole boundary coverage')
    for c,n,count in zip(r['contours'],[3100,40,40,40],[3,1,1,1]):
        if type(c) is not dict or set(c)!={'rectangle','segments','count','minimum_linf_margin','polygon_sha256'}:raise ValueError('contour record')
        if type(c['segments']) is not int or c['segments']!=n or type(c['count']) is not int or c['count']!=count:raise ValueError('contour count')
        if type(c['minimum_linf_margin']) is not str or Fraction(c['minimum_linf_margin'])<=0:raise ValueError('contour margin')
        if type(c['polygon_sha256']) is not str or not re.fullmatch('[0-9a-f]{64}',c['polygon_sha256']):raise ValueError('polygon identity')
    if type(r['root_slopes']) is not list or len(r['root_slopes'])!=3:raise ValueError('slope coverage')

def verify(path,root=HERE):
    authenticate(root)
    retained=read_json(path);preflight(retained)
    # Insert only the authenticated script directory. No parent package is imported.
    if str(HERE) not in sys.path:sys.path.insert(0,str(HERE))
    from certificate import reconstruct
    actual=reconstruct()
    if canonical(retained)!=canonical(actual):raise ValueError('primitive reconstruction mismatch')
    return hashlib.sha256(canonical(actual).encode()).hexdigest()

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--check',type=Path,default=HERE/'result.json');args=ap.parse_args()
    digest=verify(args.check)
    print('PASS_BPW26_FULL '+digest)

if __name__=='__main__':
    try:main()
    except (ValueError,TypeError,ZeroDivisionError,OSError,KeyError) as e:
        print('REJECT_BPW26: '+str(e),file=sys.stderr);raise SystemExit(1)

"""Optional NON_DIRECTED_HIGH_PRECISION sanity checks; never proof acceptance."""
import json
from pathlib import Path
import mpmath as mp

mp.mp.dps=110
stored=json.loads(Path(__file__).with_name('SOURCE_RESULTS.json').read_text())
def within(v,box):return mp.mpf(box[0])<=v<=mp.mpf(box[1])
def A(z):
    s=mp.mpf('1.5')+2*z/(1-z)
    return 1/((1-z)*mp.zeta(s)*(1-mp.power(67,-s)))
def L(s):return 1/s+1/(s-1)-mp.log(mp.pi)/2+mp.digamma(s/2)/2+mp.diff(mp.zeta,s)/mp.zeta(s)
def q(u):
    s=(1+mp.sqrt(9+4*u))/2
    return L(s)/(2*s-1)
def c(z):
    r=2/(1-z)
    return (L(mp.mpf('.5')+r)-2*r*L(mp.mpf(2))/3)/(mp.mpf('2.25')-r*r)
aa=mp.taylor(A,0,6);mm=mp.taylor(q,0,2);cc=mp.taylor(c,0,2)
checks={
 'mobius':[within(v,b) for v,b in zip(aa,stored['mobius_coefficients'])],
 'moments':[within((-1)**j*v,b) for j,(v,b) in enumerate(zip(mm,stored['invariant_moments']))],
 'hardy_source':[within(v,b) for v,b in zip(cc,stored['Hardy8_source_c'])]}
# Outer saddle regression only; no finite ratios establish its asymptotic theorem.
ratios=[]
for n in [20,80,200]:
    t=mp.mpf(8);r=1/(t-1+mp.sqrt(t*(t-2)))
    leading=mp.exp(n*(-mp.log(r)+2*t*r/(1+r)))/mp.sqrt(2*mp.pi*n*(1-r*r))
    ratios.append({'n':n,'ratio':mp.nstr((-1)**n*mp.laguerre(n,0,2*t*n)/leading,25)})
out={'classification':'NON_DIRECTED_HIGH_PRECISION','proof_dependency':False,
 'mpmath_version':mp.__version__,'digits':mp.mp.dps,'checks':checks,'all_agree':all(all(v) for v in checks.values()),
 'outer_saddle_ratios':ratios}
Path(__file__).with_name('REGRESSION.json').write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
print(json.dumps(out,sort_keys=True,indent=2))

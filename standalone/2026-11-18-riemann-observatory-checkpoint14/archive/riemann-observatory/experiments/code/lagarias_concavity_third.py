#!/usr/bin/env python3
"""Exploratory high-precision cross-check, not interval validation or proof.
Analytic proof: audits/adversarial_reviews/lagarias_concavity_third_round2.md.
"""
import json,math
from pathlib import Path
from fractions import Fraction
import mpmath as mp
mp.mp.dps=80
xs=['1','1.1','1.5','2','3','4','5','10','20','50','100','500','1000','2048','32768','1000000']
def g(t):
 x=mp.exp(t);h=mp.digamma(x+1)+mp.euler
 return mp.log((h+mp.exp(h)*mp.log(h))/x)
rows=[]
for sx in xs:
 x=mp.mpf(sx);h=mp.digamma(x+1)+mp.euler
 hp=x*mp.polygamma(1,x+1)
 hpp=hp+x*x*mp.polygamma(2,x+1)
 b=h+mp.exp(h)*mp.log(h)
 bp=1+mp.exp(h)*(mp.log(h)+1/h)
 bpp=mp.exp(h)*(mp.log(h)+2/h-1/(h*h))
 chain=(bpp/b-(bp/b)**2)*hp**2+(bp/b)*hpp
 direct=mp.diff(g,mp.log(x),2)
 assert abs(chain-direct)<mp.mpf('1e-60')
 rows.append({'x':sx,'g_second_direct':mp.nstr(direct,65),'g_second_chain':mp.nstr(chain,65),'h':mp.nstr(h,40)})
series=sum(Fraction(7**k,math.factorial(k))for k in range(13))
assert series>1029
assert Fraction(8,3)**10>13000
out={'status':'ordinary arbitrary-precision observations; analytic proof separate; no below-threshold proof from samples','decimal_digits':mp.mp.dps,'exact_checks':{'e7_lower_taylor_0_through_12':str(series),'greater_than_1029':True,'eight_thirds_power_10_greater_than_13000':True},'rows':rows}
p=Path(__file__).resolve().parents[1]/'results'/'lagarias_concavity_third.json';p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'samples':len(rows),'all_sample_values_negative':all(mp.mpf(r['g_second_direct'])<0 for r in rows),'exact_e7_taylor_lower_bound':str(series)}))

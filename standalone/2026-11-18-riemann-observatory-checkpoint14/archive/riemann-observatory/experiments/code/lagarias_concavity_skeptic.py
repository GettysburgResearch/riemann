#!/usr/bin/env python3
"""Exact base comparison plus nonvalidated high-precision concavity stress tests."""
from pathlib import Path
import json
import mpmath as mp
mp.mp.dps=180

def main():
    assert 8**10>13000*3**10
    rows=[]
    for x in map(mp.mpf,['32768','1e6','1e12','1e50','1e100']):
        h=mp.digamma(x+1)+mp.euler;ell=mp.log(h)
        hp=x*mp.polygamma(1,x+1)
        hpp=hp+x*x*mp.polygamma(2,x+1)
        r=h*mp.exp(-h)/ell;a0=(ell+1)/(h*h*ell*ell)
        lr1=-1+1/h-1/(h*ell);lr2=-1/(h*h)+a0
        rp=r*lr1;rpp=r*(lr1*lr1+lr2)
        fp=1+1/(h*ell)+rp/(1+r)
        fpp=-a0+rpp/(1+r)-rp*rp/(1+r)**2
        actual=fpp*hp*hp+fp*hpp
        upper=-(a0-r)/4+1/x
        assert actual<upper<0
        rows.append({'x':mp.nstr(x,12),'h':mp.nstr(h,30),'g_second_derivative':mp.nstr(actual,35),'analytic_upper_bound_sample':mp.nstr(upper,35),'h_second_derivative':mp.nstr(hpp,30)})
    result={'exact_base_integer_comparison':True,'numerical_status':'nonvalidated180-digit stress tests; analytic all-x proof in audit','rows':rows}
    out=Path(__file__).resolve().parents[1]/'results'/'lagarias_concavity_skeptic.json'
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()

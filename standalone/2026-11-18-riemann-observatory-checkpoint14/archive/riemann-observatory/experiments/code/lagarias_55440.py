#!/usr/bin/env python3
"""Exact rational lower-bound certificate for Lagarias n<=55440.
Only integer arithmetic. No floating-point assertion underlies the certificate.
"""
import json
from pathlib import Path
S=1<<80
LIMIT=55440

def mul_lower(x,y):
    assert x>=0 and y>=0
    return x*y//S

def exp_lower(x,terms=100):
    # x/S >=0: each term/S <= (x/S)^k/k!.
    total=term=S
    for k in range(1,terms+1):
        term=term*x//(S*k)
        total+=term
    return total

def log_lower(x,terms=100):
    # log(x/S)=2*atanh((x-S)/(x+S)); x>=S.
    assert x>=S
    y=(x-S)*S//(x+S)
    y2=mul_lower(y,y)
    power=y
    total=0
    for j in range(terms):
        total+=power//(2*j+1)
        power=mul_lower(power,y2)
    return 2*total

def run():
    sigma=[0]*(LIMIT+1)
    for d in range(1,LIMIT+1):
        for n in range(d,LIMIT+1,d): sigma[n]+=d
    h=0; minimum=None; minimum_n=None; rows=[]
    for n in range(1,LIMIT+1):
        h+=S//n
        b=h+mul_lower(exp_lower(h),log_lower(h))
        gap=b-sigma[n]*S
        assert gap==0 if n==1 else gap>0, (n,gap)
        if n>1 and (minimum is None or gap<minimum): minimum,minimum_n=gap,n
        rows.append({'n':n,'sigma':sigma[n],'harmonic_lower_numerator':h,'rhs_lower_numerator':b,'gap_numerator':gap})
    out=Path(__file__).resolve().parents[1]/'results'
    out.mkdir(exist_ok=True)
    (out/'lagarias_55440_certificate.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in rows))
    summary={'limit':LIMIT,'scale':S,'exp_terms':100,'log_terms':100,'method':'exact integer lower bounds; positive Taylor and atanh series','checked_strict':LIMIT-1,'equality':[1],'minimum_gap_n':minimum_n,'minimum_gap_numerator':minimum,'minimum_gap_decimal_display_only':minimum/S}
    (out/'lagarias_55440_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))
if __name__=='__main__':run()

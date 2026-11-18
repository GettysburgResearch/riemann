"""Exclude real off-critical zeros by an unconditional finite prime sum."""
from functools import cache
import argparse
import json
from pathlib import Path
from flint import arb, ctx
from check_zhao_high_degree_nov18 import gp_rows
from check_zhao_field_weight_nov18 import primes_through


@cache
def contribution(s100,p,code):
    s=arb(s100)/100
    logp=arb(p).log()
    return sum((code//10**(f-1)%10)*f*logp/((s*f*logp).exp()-1)
               for f in range(1,9) if code//10**(f-1)%10)


def check(rows):
    pending=rows
    proof=[]
    for limit in [16,64,256,1024,4096,16384,65536]:
        if not pending:
            break
        primes=primes_through(limit)
        nxt=[]
        for item,d,r1,r2,codes in gp_rows(pending,primes):
            n=r1+2*r2
            for s100 in [135,145,125,155,120]:
                s=arb(s100)/100
                x=1/s+1/(s-1)+(arb(d).log()-n*arb.pi().log()
                    +(r1+r2)*(s/2).digamma()+r2*((s+1)/2).digamma())/2
                x-=sum(contribution(s100,p,c) for p,c in zip(primes,codes))
                if x*(s-arb(1)/2)<2:
                    proof.append([item["label"],limit,s100,str(x*(s-arb(1)/2))])
                    break
            else:
                nxt.append(item)
        pending=nxt
    if pending:
        raise ArithmeticError(f"Real-zero exclusion unresolved for {[r['label'] for r in pending]}")
    return proof


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("input",type=Path)
    args=parser.parse_args()
    ctx.prec=96
    print(json.dumps(check(json.loads(args.input.read_text())),separators=(',',':')))

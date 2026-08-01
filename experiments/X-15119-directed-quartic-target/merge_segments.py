#!/usr/bin/env python3
"""Merge directed theta-kernel moment segments and derive tau_2,tau_4."""
from __future__ import annotations
import argparse, json
from decimal import Decimal, getcontext, localcontext, ROUND_FLOOR, ROUND_CEILING
from pathlib import Path
PREC=70; getcontext().prec=PREC
class IV:
    def __init__(self,lo,hi):
        self.lo,self.hi=Decimal(lo),Decimal(hi)
        if self.lo>self.hi: raise ValueError("reversed interval")
    def __add__(self,o):
        with localcontext() as c: c.prec=PREC;c.rounding=ROUND_FLOOR;lo=self.lo+o.lo
        with localcontext() as c: c.prec=PREC;c.rounding=ROUND_CEILING;hi=self.hi+o.hi
        return IV(lo,hi)
    def __neg__(self): return IV(-self.hi,-self.lo)
    def __sub__(self,o): return self+(-o)
    def __mul__(self,o):
        if isinstance(o,int): o=IV(str(o),str(o))
        with localcontext() as c:
            c.prec=PREC;c.rounding=ROUND_FLOOR;lo=min(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        with localcontext() as c:
            c.prec=PREC;c.rounding=ROUND_CEILING;hi=max(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return IV(lo,hi)
    __rmul__=__mul__
    def __truediv__(self,o):
        if o.lo<=0<=o.hi: raise ZeroDivisionError
        with localcontext() as c:
            c.prec=PREC;c.rounding=ROUND_FLOOR;lo=min(self.lo/o.lo,self.lo/o.hi,self.hi/o.lo,self.hi/o.hi)
        with localcontext() as c:
            c.prec=PREC;c.rounding=ROUND_CEILING;hi=max(self.lo/o.lo,self.lo/o.hi,self.hi/o.lo,self.hi/o.hi)
        return IV(lo,hi)
    def sq(self): return self*self
    def dump(self): return [str(self.lo),str(self.hi)]
def main():
    ap=argparse.ArgumentParser();ap.add_argument("segments",nargs="+",type=Path);ap.add_argument("--output",type=Path,required=True);args=ap.parse_args()
    data=[json.loads(p.read_text()) for p in args.segments]; moments={}
    for k in (0,2,4):
        total=IV("0","0")
        for d in data: total=total+IV(*d[f"I{k}"])
        moments[k]=total
    xi={k:4*moments[k] for k in moments}; tau2=xi[2]/xi[0]
    tau4=-(xi[4]/xi[0]-3*tau2.sq())/IV("6","6")
    result={"schema":"riemann.directed-xi-quartic-target.v1","method":"Riemann theta kernel + outward Decimal interval Simpson","precision_decimal_digits":PREC,
      "segments":[{k:d[k] for k in ("start","end","h")} for d in data],"nmax":data[0]["nmax"],
      "I0":moments[0].dump(),"I2":moments[2].dump(),"I4":moments[4].dump(),
      "xi0":xi[0].dump(),"xi2":xi[2].dump(),"xi4":xi[4].dump(),"tau2":tau2.dump(),"tau4":tau4.dump(),
      "derivative_bounds":data[0]["simpson_M4"],"omitted_tail_budget":data[0]["tail_budget"],
      "status":"DIRECTED_QUARTIC_TARGET_ONLY","scope":"independent completed-zeta target; no Shimizu operator rows"}
    args.output.write_text(json.dumps(result,indent=2)+"\n"); print(json.dumps(result,indent=2))
if __name__=="__main__": main()

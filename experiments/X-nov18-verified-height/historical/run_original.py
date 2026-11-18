"""Continue the independent original Platt program and repair uncovered intervals."""
import argparse
import os
import subprocess
import time
from fractions import Fraction
from pathlib import Path
from check_runs import ANCHOR, decimal, parse_log, read_all


def execute(binary, library_dir, runs, left, step, count, prec):
    name=f"{decimal(left)}-s{step}-n{count}-p{prec}.log"
    path=runs/name
    if path.exists():
        return
    temp=path.with_suffix(f".{os.getpid()}.partial")
    env=dict(os.environ)
    env["LD_LIBRARY_PATH"]=str(library_dir)
    with temp.open("w") as out:
        subprocess.run(["stdbuf","-oL",str(binary),str(prec),decimal(left),str(count),str(step)],
                       env=env,stdout=out,stderr=subprocess.STDOUT,check=True)
    states=parse_log(temp.read_text())
    temp.replace(path)
    print(f"{name}: {sum(c is not None for _,_,c in states)}/{count} successful original regions",flush=True)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--binary",required=True,type=Path)
    parser.add_argument("--library-dir",required=True,type=Path)
    parser.add_argument("--runs",type=Path,default=Path(__file__).parent/"runs")
    parser.add_argument("--start",type=int,default=ANCHOR,help="first required ordinate of this lane")
    parser.add_argument("--until",required=True,type=int,help="target ordinate; finish any covering iteration")
    parser.add_argument("--step",type=int,default=1176,choices=(504,672,840,1008,1176,1260,1344,1680,1848,1932,2016,2100,2184))
    parser.add_argument("--precision",type=int,default=160,choices=(120,128,144,160))
    parser.add_argument("--deadline",type=int,help="Unix deadline for beginning a new run")
    parser.add_argument("--batch",type=int,default=8)
    args=parser.parse_args()
    if not 1<=args.batch<=64 or not ANCHOR<=args.start<args.until<=3_000_200_000_000-3000-args.step:
        parser.error("Invalid batch or target")
    args.runs.mkdir(parents=True,exist_ok=True)
    while args.deadline is None or time.time()<args.deadline:
        good,failed,_=read_all(args.runs)
        end=Fraction(args.start)
        for left,right,_,_ in good:
            if left>end:
                break
            end=max(end,right)
        if end>=args.until:
            break
        holes=[(a,b) for a,b in failed if a<=end<b]
        if holes:
            # Changing the phase of the exact binary grid can resolve nearby zeros.
            trial=None
            for k in range(12):
                # Keep the difficult part near the new center, and vary the phase.
                step=(672,504,336,252)[k%4]
                left=end-Fraction(21,1)-Fraction(k+1,64)
                prec=144+8*(k//4)
                name=f"{decimal(left)}-s{step}-n1-p{prec}.log"
                if not (args.runs/name).exists():
                    trial=(left,step,1,prec)
                    break
            if trial is None:
                raise RuntimeError(f"All original-grid repairs exhausted near {decimal(end)}")
        else:
            # A previously verified component can lie just past an exact gap.
            next_start=min((a for a,_,_,_ in good if a>end),default=Fraction(args.until))
            count=max(1,min(args.batch,-(-(min(next_start,args.until)-end)//args.step)))
            trial=(end,args.step,count,args.precision)
        execute(args.binary.resolve(),args.library_dir.resolve(),args.runs,*trial)


if __name__=="__main__":
    main()

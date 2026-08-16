#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, os, re, subprocess
from pathlib import Path

PR508_SHA="4ae97dffd1f76ed3244b8f3028560ffa80663caf"
SOURCE="experiments/X-93780-target-lorenz-directed-tail/directed_tail.cpp"

def run(cmd,**kw):
    print("+"," ".join(map(str,cmd)),flush=True)
    return subprocess.run(cmd,check=True,**kw)

def rewrite(src:str, header_path:str)->str:
    # Replace only unqualified interval calls in the frozen source.
    src=re.sub(r'(?<![A-Za-z0-9_:])sqrt\(', 'mpfr_sqrt_interval(', src)
    src=re.sub(r'(?<![A-Za-z0-9_:])log\(', 'mpfr_log_interval(', src)
    marker='using I = typename il::unprotect<ProtectedI>::type;'
    if marker not in src: raise RuntimeError("frozen source marker not found")
    return src.replace(marker, marker+'\n#include "'+header_path+'"\n',1)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--work",type=Path,default=Path("work"))
    ap.add_argument("--workers",type=int,default=4)
    ap.add_argument("--smoke",action="store_true")
    args=ap.parse_args()
    args.work.mkdir(parents=True,exist_ok=True)
    original=args.work/"directed_tail.original.cpp"
    hardened=args.work/"directed_tail.mpfr.cpp"
    header=Path(__file__).resolve().parent/"mpfr_interval.hpp"
    original.write_bytes(subprocess.check_output(["git","show",f"{PR508_SHA}:{SOURCE}"]))
    hardened.write_text(rewrite(original.read_text(),str(header)))
    exe=args.work/"directed_tail_mpfr"
    run(["g++","-O2","-std=c++17","-frounding-math","-fno-fast-math",
         str(hardened),"-lmpfr","-lgmp","-o",str(exe)])
    if args.smoke:
        rows=[66]
    else:
        rows=list(range(2,67))
    outdir=args.work/"rows"; outdir.mkdir(exist_ok=True)
    # Execute bounded batches to avoid oversubscribing memory.
    for start in range(0,len(rows),args.workers):
        procs=[]
        for row in rows[start:start+args.workers]:
            out=(outdir/f"row-{row}.json").open("w")
            err=(outdir/f"row-{row}.log").open("w")
            procs.append((row,subprocess.Popen([str(exe),str(row),str(row)],stdout=out,stderr=err),out,err))
        for row,p,out,err in procs:
            rc=p.wait(); out.close(); err.close()
            if rc: raise SystemExit(f"row {row} failed with {rc}")
    records=[json.loads((outdir/f"row-{r}.json").read_text()) for r in rows]
    by_row={r:rec for r,rec in zip(rows,records)}
    row66_upper=(float(by_row[66]["directed_full_interval_upper_at_minimum"])
                 if 66 in by_row else None)
    separation=(min(float(rec["directed_full_lower_bound"])
                    for r,rec in by_row.items() if r<66)-row66_upper
                if row66_upper is not None and any(r<66 for r in by_row) else None)
    result={
      "schema":"riemann.x96201.mpfr-target-lorenz-tail.v1",
      "precision_bits":256,
      "rows":rows,
      "full_lower":min(float(x["directed_full_lower_bound"]) for x in records),
      "parent_lower":min(float(x["directed_parent_lower_bound"]) for x in records),
      "derivative_lower":min(float(x["directed_parent_derivative_lower_bound"]) for x in records),
      "tail_second_derivative_polynomial_lower":
          min(float(x["last_interval_second_derivative_polynomial_lower"]) for x in records),
      "tail_polynomial_derivative_lower":
          min(float(x["last_interval_polynomial_derivative_lower"]) for x in records),
      "row66_upper":row66_upper,
      "row66_separation_lower":separation,
      "all_pass":all(float(x["directed_full_lower_bound"])>26 and
                     float(x["directed_parent_lower_bound"])>79 and
                     float(x["directed_parent_derivative_lower_bound"])>0.23 and
                     float(x["last_interval_second_derivative_polynomial_lower"])>0 and
                     float(x["last_interval_polynomial_derivative_lower"])>0
                     for x in records)
                 and (separation is None or separation>1),
      "rh_established":False,
    }
    (args.work/"aggregate.json").write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps(result,indent=2,sort_keys=True))
    if not result["all_pass"]: raise SystemExit("strict MPFR margin failed")

if __name__=="__main__": main()

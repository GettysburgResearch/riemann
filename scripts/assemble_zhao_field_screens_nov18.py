"""Combine complete prime screens and certified contour decisions for one or more signatures."""

import argparse
from collections import Counter, defaultdict
import json
import os
import subprocess
from pathlib import Path
from flint import arb


def assemble(screens, refinements):
    decisions = {}
    for path in refinements:
        for row in map(json.loads, path.read_text().splitlines()):
            label = row["label"]
            if label in decisions:
                raise ValueError(f"Duplicate contour for {label}")
            weight = arb(row["weight"])
            assert row["passed"] in (True, False)
            assert (weight < 2) if row["passed"] else (weight > 2)
            decisions[label] = row
    groups = []
    consumed = set()
    for path in screens:
        screen = json.loads(path.read_text())
        fields = list(screen["accepted"])
        close = []
        for item in screen["unresolved"]:
            row = decisions[item["label"]]
            assert item["label"] not in consumed
            consumed.add(item["label"])
            close.append(row)
            if row["passed"]:
                fields.append(item)
        assert len({v["label"] for v in fields})==len(fields)
        for item in fields:
            item.pop("id", None)
            item.pop("disc_abs", None)
            item.pop("index", None)
        fields.sort(key=lambda v:tuple(map(int,v["label"].split("/")[-1].split("."))))
        groups.append(dict(screen=path.stem,enumerated=screen["enumerated"],
                           prime_stages=screen["stages"],near_threshold=close,passing_fields=fields))
    assert len(consumed)==len(decisions)
    return groups


def crosscheck_quintics(groups, olivier_dir, lmfdb_dir):
    # The first comparison uses every field in the three exhaustive source ranges.
    batches = []
    for r2, cap in enumerate((1012301, 736477, 535318)):
        olivier = json.loads((olivier_dir / f"quintic-r{r2}.json").read_text())
        lmfdb = json.loads((lmfdb_dir / f"n5-r{r2}.json").read_text())
        def disc(item):
            return int(item["label"].split(".")[-2])
        lmfdb = [field for field in lmfdb if disc(field) <= cap]
        assert Counter(map(disc, olivier)) == Counter(map(disc, lmfdb))
        by_disc = defaultdict(list)
        for field in lmfdb:
            by_disc[disc(field)].append(field)
        batches.extend((field, by_disc[disc(field)]) for field in groups[r2]["passing_fields"])
    for offset in range(0, len(batches), 40):
        batch = batches[offset:offset+40]
        data = [[field["coeffs"], [v["coeffs"] for v in options]] for field,options in batch]
        code = (f"V={data};\nfor(i=1,#V,a=Polrev(V[i][1]);g=V[i][2];"
                "print(vector(#g,j,if(nfisisom(a,Polrev(g[j])),1,0))));\n")
        run = subprocess.run([os.getenv("PARI_GP","gp"), "-fq"], input=code, text=True,
                             capture_output=True, check=True)
        lines = run.stdout.splitlines()
        assert not run.stderr and len(lines) == len(batch)
        for line,(field,options) in zip(lines,batch):
            flags = json.loads(line)
            assert len(flags)==len(options) and sum(flags)==1
            field["lmfdb_label"] = options[flags.index(1)]["label"]
    assert len({field["lmfdb_label"] for field,_ in batches})==len(batches)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--screen",type=Path,nargs="+",required=True)
    parser.add_argument("--contour",type=Path,nargs="+",required=True)
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--source-manifest",type=Path)
    parser.add_argument("--real-zero-exclusions",type=Path)
    parser.add_argument("--crosscheck-quintics",type=Path,nargs=2,metavar=("OLIVIER_DIR","LMFDB_DIR"))
    args=parser.parse_args()
    groups=assemble(args.screen,args.contour)
    if args.crosscheck_quintics:
        crosscheck_quintics(groups,*args.crosscheck_quintics)
    record={"passing_count":sum(len(s["passing_fields"]) for s in groups),"groups":groups}
    if args.real_zero_exclusions:
        checks=json.loads(args.real_zero_exclusions.read_text())
        witnesses = {label:(p,s100,ball) for label,p,s100,ball in checks}
        passing = {row["label"] for group in groups for row in group["passing_fields"]}
        assert len(witnesses)==len(checks) and set(witnesses)==passing
        assert all(arb(ball)<2 for _,_,ball in witnesses.values())
        record["real_zero_exclusions"]=witnesses
    if args.source_manifest:
        record["sources"]=json.loads(args.source_manifest.read_text())
    args.output.write_text(json.dumps(record,separators=(",",":"))+"\n")


if __name__=="__main__":
    main()

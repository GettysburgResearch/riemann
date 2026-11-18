"""Combine complete prime screens and certified contour decisions for one or more signatures."""

import argparse
import json
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


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--screen",type=Path,nargs="+",required=True)
    parser.add_argument("--contour",type=Path,nargs="+",required=True)
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--source-manifest",type=Path)
    args=parser.parse_args()
    groups=assemble(args.screen,args.contour)
    record={"passing_count":sum(len(s["passing_fields"]) for s in groups),"groups":groups}
    if args.source_manifest:
        record["sources"]=json.loads(args.source_manifest.read_text())
    args.output.write_text(json.dumps(record,separators=(",",":"))+"\n")


if __name__=="__main__":
    main()

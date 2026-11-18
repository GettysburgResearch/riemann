"""Extract quintic polynomials and indices from the Bordeaux small-field tables."""

from concurrent.futures import ThreadPoolExecutor
import gzip
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.request import urlopen

ROOT = "https://pari.math.u-bordeaux.fr/pub/numberfields/degree5/"
BOUNDS = {1:535318, 3:736477, 5:1012301}
PREFIX = re.compile(r"\[([-+*^x0-9]+),\[(\d+),(\d+)\],\[[^\]]+\],\[(-?\d+),(\d+)\],")


def coefficients(poly):
    parts = re.findall(r"[+-]?[^+-]+",poly)
    result = [0]*6
    for token in parts:
        sign = -1 if token.startswith("-") else 1
        body = token.lstrip("+-")
        c, sep, power = body.partition("x")
        c = int(c.rstrip("*") or "1")
        exponent = int(power[1:]) if power else int(bool(sep))
        result[exponent] += sign*c
    assert result[5] == 1
    return result


def fetch_one(task):
    name, r1, first_disc, last_disc, full_block = task
    data = urlopen(ROOT+name).read()
    rows = []
    for poly, a, b, discriminant, index in PREFIX.findall(gzip.decompress(data).decode()):
        assert int(a) == r1 and int(a)+2*int(b) == 5
        rows.append((int(discriminant), coefficients(poly), int(index)))
    if (not rows or abs(rows[0][0]) != abs(first_disc) or abs(rows[-1][0]) != abs(last_disc)
            or (full_block and len(rows) != 1000)):
        raise ArithmeticError(f"Incomplete field block {name}")
    # A record occupies one physical line in these tables.
    text = gzip.decompress(data).decode()
    assert len(rows) == sum(1 for line in text.splitlines() if "x^5" in line and ",[" in line)
    return name, hashlib.sha256(data).hexdigest(), rows


def main():
    directory = Path(sys.argv[1])
    directory.mkdir(parents=True,exist_ok=True)
    manifest = {}
    tasks = []
    for r1,bound in BOUNDS.items():
        index = urlopen(ROOT+f"index_5{r1}").read().decode()
        ranges = re.findall(r"(t5[135]\.\d+): starts at d = (-?\d+), ends at d = (-?\d+)",index)
        assert ranges and max(abs(int(last)) for _,_,last in ranges) >= bound
        tasks += [(name+".gz", r1, int(first), int(last), i+1 < len(ranges))
                  for i,(name, first, last) in enumerate(ranges) if abs(int(first)) <= bound]
    by_sig = {r1:[] for r1 in BOUNDS}
    with ThreadPoolExecutor(max_workers=4) as pool:
        for (expected,r1,*_),(name,digest,rows) in zip(tasks,pool.map(fetch_one,tasks)):
            assert name == expected
            manifest[name] = {"sha256":digest,"records":len(rows)}
            by_sig[r1].extend((d,c,k) for d,c,k in rows if abs(d)<=BOUNDS[r1])
    for r1,rows in by_sig.items():
        out = []
        repeats = {}
        for d,c,k in rows:
            repeats[d] = repeats.get(d,0)+1
            label = f"Olivier/5.{r1}.{abs(d)}.{repeats[d]}"
            out.append(dict(label=label,coeffs=c,index=k))
        path = directory/f"quintic-r{(5-r1)//2}.json"
        path.write_text(json.dumps(out,separators=(",",":"))+"\n")
        print(r1,len(out),flush=True)
    (directory/"source-manifest.json").write_text(json.dumps(manifest,indent=2)+"\n")


if __name__=="__main__":
    main()

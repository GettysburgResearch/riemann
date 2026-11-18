"""Identify the unique passing number field nearest the strict Zhao threshold."""

import io
import json
from pathlib import Path

from flint import arb, ctx
from check_zhao_dedekind_contour_nov18 import weight
from check_zhao_field_threshold_nov18 import process

CATALOG = Path(__file__).resolve().parents[1] / "research/explorations"


def inventory(name):
    return json.loads((CATALOG / f"zhao-{name}-nov18.json").read_text())


def passing_polynomials():
    rows = []
    for disc in inventory("quadratic-fields")["discriminants"]:
        coefficients = [(1-disc)//4,-1,1] if disc%4==1 else [-disc//4,0,1]
        rows.append({"label":f"2.{2 if disc>0 else 0}.{abs(disc)}.1", "coeffs":coefficients})
    low = inventory("low-degree-unconditional")
    for n, name in [(3, "cubic"), (4, "quartic")]:
        for idx, (r2, disc, descending) in enumerate(low[name]["accepted"]):
            rows.append({"label":f"local/{n}.{n-2*r2}.{abs(disc)}.{idx+1}",
                         "coeffs":descending[::-1]})
    for name in ("quintic-fields", "degree6-fields", "degree7-fields", "degree8-fields"):
        for group in inventory(name)["groups"]:
            rows.extend(group["passing_fields"])
    assert len({r["label"] for r in rows}) == len(rows) == 2579
    return rows


def main():
    ctx.prec = 160
    threshold = "1.99990"
    rational = 2 + arb.const_euler() - (4*arb.pi()).log()
    assert rational < arb(threshold)
    rows = passing_polynomials()
    pending = rows
    high = []
    for tolerance in (".006", ".00001", ".000000001"):
        stream = io.StringIO()
        process(pending,tolerance,stream,threshold)
        outcomes = {label:decision for label,decision,_ in map(json.loads,stream.getvalue().splitlines())}
        assert set(outcomes)=={r["label"] for r in pending}
        high.extend(r for r in pending if outcomes[r["label"]] is False)
        pending = [r for r in pending if outcomes[r["label"]] is None]
        if not pending:
            break
    if pending or len(high)!=2:
        raise ArithmeticError("Threshold comparison disagrees with the certified census")
    ctx.prec = 192
    close = []
    for item in high:
        w = weight(item,"1e-16")
        assert 2 > w > arb(threshold)
        close.append((w,item))
    close.sort(key=lambda pair:float(pair[0]))
    assert close[0][0] < close[1][0]
    for w,item in reversed(close):
        print(json.dumps({"field":item,"weight":str(w),"margin":str(2-w)}))


if __name__=="__main__":
    main()

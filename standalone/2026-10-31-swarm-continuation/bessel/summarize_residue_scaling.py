"""Compact the ordinary Decimal diagnostics and compare two working precisions.

Agreement is a numerical consistency check, not a directed-arithmetic proof.
Run residue_scaling_diagnostic.py at precisions 240 and 360 first.
"""
from decimal import Decimal as D, localcontext
import hashlib
import json
from pathlib import Path


def main():
    folder = Path(__file__).resolve().parent
    names = ["RESIDUE_SCALING_240.json", "RESIDUE_SCALING_360.json"]
    data = [json.loads((folder / name).read_text()) for name in names]
    if len(data[0]["rows"]) != len(data[1]["rows"]):
        raise RuntimeError("Different numbers of diagnostic parameters")
    rows = []
    errors = []
    with localcontext() as ctx:
        ctx.prec = 400
        for low, high in zip(data[0]["rows"], data[1]["rows"]):
            if (low["a"], low["M"]) != (high["a"], high["M"]):
                raise RuntimeError("Mismatched diagnostic parameters")
            lp = low["first_three_sign_changing_real_poles"]
            hp = high["first_three_sign_changing_real_poles"]
            if len(lp) != 3 or len(hp) != 3:
                raise RuntimeError("A diagnostic did not locate three real sign changes")
            compact = []
            for index, (left, right) in enumerate(zip(lp, hp), 1):
                if set(left) != set(right):
                    raise RuntimeError("Mismatched diagnostic fields")
                relative = []
                for field in left:
                    value = D(right[field])
                    if value == 0:
                        raise RuntimeError("A relative comparison has a zero denominator")
                    relative.append(abs(D(left[field]) - value) / abs(value))
                worst = max(relative)
                errors.extend(relative)
                compact.append({
                    "real_sign_change_index": index,
                    "energy": format(D(right["energy"]), ".12E"),
                    "residue": format(D(right["residue"]), ".12E"),
                    "residue_divided_by_2pi_a_exp_minus_2a": format(
                        D(right["residue_divided_by_2pi_a_exp_minus_2a"]), ".12E"),
                    "ratio_to_rounded_limiting_companion_diagnostic": format(
                        D(right["ratio_to_rounded_limiting_companion_diagnostic"]), ".12E"),
                    "largest_240_vs_360_relative_difference": format(worst, ".12E"),
                })
            rows.append({"a": high["a"], "M": high["M"],
                         "M_over_a": high["M_over_a"], "poles": compact})
        worst = max(errors)
        if worst >= D("1e-80"):
            raise RuntimeError("Cross-precision diagnostic agreement is insufficient")
    sources = names + ["source_polynomials.py", "residue_scaling_diagnostic.py"]
    summary = {
        "scope": "ordinary rounded diagnostics only; agreement at two precisions is not an error bound, a residue-sign proof, or a complete pole census",
        "cofinal_schedule": "M=ceil(a*(3+2*log(a)))",
        "working_precisions": [240, 360],
        "compared_numeric_fields": len(errors),
        "largest_relative_difference": format(worst, ".12E"),
        "source_sha256": {name: hashlib.sha256((folder / name).read_bytes()).hexdigest()
                          for name in sources},
        "rows": rows,
    }
    output = json.dumps(summary, indent=2) + "\n"
    (folder / "RESIDUE_SCALING_SUMMARY.json").write_text(output)
    print(output, end="")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Bind the native absorbed tail coefficient by directed Taylor arithmetic.

Replays the entire finite census before applying the complete product's
coefficient identity. Imports the explicitly qualified historical FLINT
complete-count contract; does not replay that historical verification.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import flint
from flint import acb, acb_series, arb, ctx, fmpq


def need(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    ctx.prec, ctx.cap = 160, 3
    need(flint.__version__ == "0.9.0" and flint.__FLINT_VERSION__ == "3.6.0",
         "frozen directed backend versions")
    directory = Path(__file__).resolve().parent
    candidate_path = directory/"native_candidates.json"
    candidates = json.loads(candidate_path.read_text(encoding="utf-8"))
    height, denominator = 8192, 2**24
    need(candidates["height"] == height and candidates["denominator"] == denominator,
         "frozen census height and exact dyadic denominator")
    need(candidates["normalization"] == "Xi(z)=xi(1/2+i*z)", "native normalization")
    need(candidates["python_flint_version"] == flint.__version__ and
         candidates["flint_version"] == flint.__FLINT_VERSION__,
         "candidate backend provenance")
    need(candidates["producer_sha256"] == digest(directory/"produce_native_candidates.py"),
         "candidate producer binding")
    intervals = candidates["interval_numerators"]
    complete_count = arb(height).zeta_nzeros()
    count_integer = complete_count.unique_fmpz()
    need(count_integer is not None and complete_count.is_exact(),
         "exact native complete-count library output")
    count = int(count_integer)
    need(count == len(intervals) == candidates["candidate_count"] == 8049,
         "complete count matches every retained candidate interval")
    half = arb(fmpq(1, 2))
    pi_log = arb.pi().log()

    def hardy(t: arb) -> arb:
        theta = acb(arb(fmpq(1, 4)), t/2).lgamma().imag-t*pi_log/2
        value = acb(0, theta).exp()*acb(half, t).zeta()
        need(value.imag.contains(0), "native Hardy-Z reality enclosure")
        return value.real

    endpoint_value = hardy(arb(height))
    need(endpoint_value > 0 or endpoint_value < 0, "census endpoint is not a zero")
    finite_quadratic_sum = arb(0)
    previous_upper = 0
    for index, bracket in enumerate(intervals, start=1):
        need(isinstance(bracket, list) and len(bracket) == 2,
             f"primitive bracket shape {index}")
        lower, upper = bracket
        need(type(lower) is int and type(upper) is int and upper == lower+1,
             f"exact dyadic primitive bracket {index}")
        need(previous_upper < lower < upper < height*denominator,
             f"disjoint positive census coverage {index}")
        previous_upper = upper
        lo, hi = arb(fmpq(lower, denominator)), arb(fmpq(upper, denominator))
        lv, hv = hardy(lo), hardy(hi)
        need((lv > 0 and hv < 0) or (lv < 0 and hv > 0),
             f"actual directed Hardy-Z sign crossing {index}")
        gamma = arb(fmpq(lower+upper, 2*denominator),
                    fmpq(upper-lower, 2*denominator))
        finite_quadratic_sum += 1/(gamma*gamma)
        if index % 1024 == 0:
            print("REPLAYED_TAYLOR_NATIVE_BRACKETS", index, flush=True)

    z = acb_series([0, 1], 3)
    s = acb(half)+acb(0, 1)*z
    xi = s*(s-1)/2*(-s*pi_log/2).exp()*(s/2).gamma()*s.zeta()
    c0, c1, c2 = xi[0], xi[1], xi[2]
    need(c0.imag.contains(0) and c2.imag.contains(0) and c1.contains(0),
         "exact even-real native normalization enclosures")
    need(c0.real > arb(fmpq(1, 4)), "directed actual xi(1/2)>1/4 seed")
    need(not c0.contains(0), "native Taylor constant division guard")
    total_quadratic = -c2/c0
    need(total_quadratic.imag.contains(0), "native total quadratic reality enclosure")
    tail_coefficient = total_quadratic.real-finite_quadratic_sum
    R = arb(height)
    tail_sum_bound = 2*(R.log()+1)/R-arb(count)/(R*R)
    need(tail_coefficient > 0 and tail_coefficient < tail_sum_bound,
         "strict source-bound coefficient inside complete strip budget")
    lower, upper = tail_coefficient.lower().fmpq(), tail_coefficient.upper().fmpq()
    need(lower > 0 and upper > lower and upper-lower < fmpq(1, 10**9),
         "exact narrow native coefficient interval")

    source_paths = [Path(__file__).resolve(), directory/"produce_native_candidates.py",
                    candidate_path, directory/"FINITE_CENSUS_COMPLEMENT.md",
                    directory/"NATIVE_SLAB_CERTIFICATE.md",
                    directory/"GAUSSIAN_TAIL_TRANSPORT.md",
                    directory/"TAYLOR_TAIL_BINDING.md",
                    directory/"THEOREM.md",
                    directory.parent.parent/"heights"/"COARSE_ZERO_COUNT.md"]
    package = Path(flint.__file__).resolve().parent
    binaries = [package/"types"/"arb.abi3.so", package/"types"/"acb.abi3.so",
                package/"types"/"acb_series.abi3.so"]
    binaries.extend(sorted((package.parent/"python_flint.libs").glob("lib*.so*")))
    report = {
        "status": "PASS_DIRECTED_NATIVE_TAYLOR_TAIL",
        "normalization": "Xi(z)=xi(1/2+i*z)",
        "source": "Native Gamma/zeta series plus a complete simple real census and the complete paired-product coefficient identity.",
        "coefficient_identity": "a_1=-[z^2]Xi/Xi(0)-sum_{0<gamma<=8192}gamma^(-2)",
        "native_Taylor_c0": str(c0), "native_Taylor_c1": str(c1),
        "native_Taylor_c2": str(c2),
        "finite_quadratic_sum": str(finite_quadratic_sum),
        "actual_tail_coefficient_lower": str(lower),
        "actual_tail_coefficient_upper": str(upper),
        "actual_tail_coefficient_width": str(upper-lower),
        "conservative_tail_sum_upper": str(tail_sum_bound.upper().fmpq()),
        "complete_census_height": height,
        "imported_complete_count": count,
        "replayed_disjoint_sign_crossing_brackets": len(intervals),
        "census_interval_width": "1/16777216",
        "native_complete_count_dependencies": "FLINT3.6.0 complete-count contract and its finite Gram/Rosser rule input at this index; historical finite rule not independently replayed.",
        "arithmetic": "Arb/acb and acb_series outward ball arithmetic at 160 bits; exact dyadic root inputs; exact rational coefficient bounds.",
        "python_flint_version": flint.__version__, "flint_version": flint.__FLINT_VERSION__,
        "source_sha256": {str(p.relative_to(directory.parent.parent)):digest(p) for p in source_paths},
        "backend_binary_sha256": {p.name:digest(p) for p in binaries},
        "actual_primitive_endpoints_replayed": True,
        "native_Taylor_series_evaluated_directly": True,
        "different_arithmetic_implementation_used": False,
        "historical_Gram_Rosser_verification_replayed": False,
        "infinite_count_or_product_theorem_authenticated_by_checker": False,
        "companion_sector_certified_by_this_checker": False,
        "cofinal_domain_certified": False, "rh_proved": False,
    }
    (directory/"taylor_tail_certificate.json").write_text(
        json.dumps(report, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    print(report["status"], f"census={count}",
          f"approx_coefficient_midpoint={float((lower+upper)/2):.10f}",
          f"approx_width={float(upper-lower):.3e}", flush=True)


if __name__ == "__main__":
    main()

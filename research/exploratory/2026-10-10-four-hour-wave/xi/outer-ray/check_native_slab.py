#!/usr/bin/env python3
"""Directed native finite-census/complement certificate for one xi slab.

The complete-count contract of FLINT is imported and explicitly qualified in
NATIVE_SLAB_CERTIFICATE.md. This checker replays every Hardy-Z sign bracket,
all compact polynomial boxes, and the complete analytic tail adapter. It does
not re-prove FLINT's historical finite Gram/Rosser or Turing inputs.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import flint
from flint import acb, arb, ctx, fmpq


def need(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    ctx.prec = 128
    need(flint.__version__ == "0.9.0" and flint.__FLINT_VERSION__ == "3.6.0",
         "frozen directed backend versions")
    directory = Path(__file__).resolve().parent
    candidate_path = directory/"native_candidates.json"
    candidates = json.loads(candidate_path.read_text(encoding="utf-8"))
    height, denominator, lam = 8192, 2**24, 10
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

    # This single real primitive also supplies COARSE_ZERO_COUNT.md's seed.
    half = arb(fmpq(1, 2))
    xi_half = (half*(half-1)/2 * arb.pi()**(-half/2)
               * (half/2).gamma()*half.zeta())
    need(xi_half > arb(fmpq(1, 4)), "directed actual xi(1/2)>1/4 seed")

    pi_log = arb.pi().log()

    def hardy(t: arb) -> arb:
        theta = acb(arb(fmpq(1, 4)), t/2).lgamma().imag-t*pi_log/2
        value = acb(0, theta).exp()*acb(half, t).zeta()
        need(value.imag.contains(0), "native Hardy-Z reality enclosure")
        return value.real

    endpoint_value = hardy(arb(height))
    need(endpoint_value > 0 or endpoint_value < 0, "census endpoint is not a zero")
    gamma_squared = []
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
        gamma_squared.append(gamma*gamma)
        if index % 1024 == 0:
            print("REPLAYED_NATIVE_BRACKETS", index, flush=True)

    # The complete count plus these disjoint sign changes gives exactly one
    # simple critical-line root per interval and no omitted root through R.
    # The complete infinite count bound is the analytic source dependency.
    R, B = arb(height), arb(fmpq(17, 8))
    tail_sum = 2*(R.log()+1)/R-arb(count)/(R*R)
    need(tail_sum > 0 and B < R, "complete spectral tail budget")
    m1 = 2*B*tail_sum/(1-B*B/(R*R))
    m2 = 2*tail_sum/(1-B/R)**2
    alpha = lam*m1
    need(alpha < 1, "uniform native companion numerator protection")

    cells = []
    minimum_acceptance = None
    minimum_actual_sector = None
    for ix in range(32):
        xlo, xhi = fmpq(-16+ix, 8), fmpq(-15+ix, 8)
        x = arb((xlo+xhi)/2, (xhi-xlo)/2)
        for iy in range(8):
            ylo, yhi = fmpq(iy, 16), fmpq(iy+1, 16)
            y = arb((ylo+yhi)/2, (yhi-ylo)/2)
            z, imaginary_unit = acb(x, -y), acb(0, 1)
            z_squared = z*z
            log_first, log_second = acb(0), acb(0)
            for gamma2 in gamma_squared:
                factor_denominator = gamma2-z_squared
                need(not factor_denominator.contains(0), "finite factor division guard")
                log_first += -2*z/factor_denominator
                log_second += -2*(gamma2+z_squared)/(factor_denominator*factor_denominator)
            companion_over_base = 1-imaginary_unit*lam*log_first
            derivative_over_base = log_first-imaginary_unit*lam*(log_first*log_first+log_second)
            need(not derivative_over_base.contains(0), "finite polynomial companion derivative guard")
            w = imaginary_unit*companion_over_base/derivative_over_base
            need(w.is_finite() and w.real > 0, "full-box finite polynomial sector")
            real_lower = w.real.lower().fmpq()
            modulus_upper = abs(w).upper().fmpq()
            need(real_lower > 0 and modulus_upper > 0, "exact finite margin extraction")
            tau = arb(real_lower/modulus_upper)
            beta = arb(modulus_upper)*(2*m1+lam*(m1*m1+m2))
            acceptance = tau-alpha-(1+tau)*beta
            need(beta < 1 and acceptance > 0, "strict full-tail finite-census acceptance")
            actual_sector = arb(real_lower)-arb(modulus_upper)*(alpha+beta)/(1-beta)
            need(actual_sector > 0, "strict native companion sector lower bound")
            acceptance_lower = acceptance.lower().fmpq()
            actual_lower = actual_sector.lower().fmpq()
            minimum_acceptance = (acceptance_lower if minimum_acceptance is None
                                  else min(minimum_acceptance, acceptance_lower))
            minimum_actual_sector = (actual_lower if minimum_actual_sector is None
                                     else min(minimum_actual_sector, actual_lower))
            cells.append({
                "x_interval": [str(xlo), str(xhi)],
                "y_interval": [str(ylo), str(yhi)],
                "polynomial_Re_W_lower": str(real_lower),
                "polynomial_abs_W_upper": str(modulus_upper),
                "acceptance_margin_lower": str(acceptance_lower),
                "actual_Re_W_lower": str(actual_lower),
            })
        if ix % 8 == 7:
            print("REPLAYED_COMPACT_BOXES", len(cells), flush=True)
    need(len(cells) == 256, "complete compact box coverage")

    source_paths = [Path(__file__).resolve(), directory/"produce_native_candidates.py",
                    candidate_path, directory/"FINITE_CENSUS_COMPLEMENT.md",
                    directory/"NATIVE_SLAB_CERTIFICATE.md",
                    directory.parent.parent/"heights"/"COARSE_ZERO_COUNT.md"]
    package = Path(flint.__file__).resolve().parent
    binaries = [package/"types"/"arb.abi3.so", package/"types"/"acb.abi3.so"]
    binaries.extend(sorted((package.parent/"python_flint.libs").glob("lib*.so*")))
    report = {
        "status": "PASS_DIRECTED_NATIVE_COMPANION_SLAB",
        "primitive_source": "Actual xi through directed zeta and Gamma; complete-count FLINT contract explicitly imported.",
        "normalization": "Xi(z)=xi(1/2+i*z)",
        "derivative_order": 0,
        "frozen_lambda": "10",
        "domain": {"T": ["-2", "2"], "y": ["0", "1/2"], "z": "T-i*y"},
        "coverage": "Every point in the closed rectangle, covered by all 32 by 8 directed interval boxes; every retained root bracket replayed.",
        "arithmetic": "Arb/acb outward ball arithmetic at 128 bits; exact dyadic root and compact-domain inputs; exact rational output bounds.",
        "complete_census_height": height,
        "imported_complete_count": count,
        "replayed_disjoint_sign_crossing_brackets": len(intervals),
        "census_interval_width": "1/16777216",
        "directed_xi_half": str(xi_half),
        "native_complete_count_dependencies": "FLINT3.6.0 complete-count contract and its finite Gram/Rosser rule input at this index; historical finite rule not independently replayed.",
        "tail": {"source": "COARSE_ZERO_COUNT.md plus partial summation; the complete tail, allowing nonreal zeros above R.",
                 "S_upper": str(tail_sum.upper().fmpq()),
                 "B": "17/8", "log_first_upper": str(m1.upper().fmpq()),
                 "log_second_upper": str(m2.upper().fmpq())},
        "all_boxes": cells,
        "minimum_acceptance_margin_lower": str(minimum_acceptance),
        "minimum_actual_Re_W_lower": str(minimum_actual_sector),
        "python_flint_version": flint.__version__,
        "flint_version": flint.__FLINT_VERSION__,
        "source_sha256": {str(p.relative_to(directory.parent.parent)):digest(p) for p in source_paths},
        "backend_binary_sha256": {p.name:digest(p) for p in binaries},
        "strict_acceptance": "Every assertion and every primitive/box replay must pass; beta<1 and alpha+(1+tau)*beta<tau strictly on all boxes.",
        "actual_primitive_endpoints_replayed": True,
        "different_arithmetic_implementation_used": False,
        "historical_Gram_Rosser_verification_replayed": False,
        "infinite_count_or_product_theorem_authenticated_by_checker": False,
        "cofinal_domain_certified": False,
        "rh_proved": False,
    }
    (directory/"native_slab_certificate.json").write_text(
        json.dumps(report, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    print(report["status"], f"census={count}", f"boxes={len(cells)}",
          f"approx_minimum_acceptance={float(minimum_acceptance):.6f}",
          f"approx_minimum_Re_W={float(minimum_actual_sector):.6f}", flush=True)


if __name__ == "__main__":
    main()

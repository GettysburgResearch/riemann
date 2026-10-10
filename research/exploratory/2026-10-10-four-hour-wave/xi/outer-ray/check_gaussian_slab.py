#!/usr/bin/env python3
"""Directed all-parameter Gaussian-tail transport on a finite native xi slab.

All 8,049 native Hardy-Z brackets are replayed. Completeness imports FLINT's
explicitly qualified finite-count contract. Every complex box and every
subinterval of the unknown Gaussian parameter is enclosed by Arb/acb.
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
    t_max, t_subdivisions, y_subdivisions, a_subdivisions = 13, 104, 8, 32
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
            print("REPLAYED_GAUSSIAN_NATIVE_BRACKETS", index, flush=True)

    # All roots through R are simple and real by the complete-count contract
    # plus these disjoint sign changes. Nonreal tail roots remain permitted.
    R, B = arb(height), arb(fmpq(105, 8))
    need(arb(t_max*t_max)+half*half < B*B and B < R,
         "whole compact rectangle lies in the protected disk")
    tail_sum = 2*(R.log()+1)/R-arb(count)/(R*R)
    need(tail_sum > 0, "complete source-qualified spectral tail budget")
    u = B*B/(R*R)
    j1 = 2*B**3*tail_sum/(R*R*(1-u))
    j2 = 2*B*B*(3+u)*tail_sum/(R*R*(1-u)**2)
    alpha = lam*j1
    need(alpha < 1, "uniform residual numerator protection")
    parameter_intervals = [
        arb(fmpq(2*ia+1, 2*a_subdivisions), fmpq(1, 2*a_subdivisions))*tail_sum
        for ia in range(a_subdivisions)
    ]
    imaginary_unit = acb(0, 1)
    cells = []
    minimum_acceptance = None
    minimum_actual_sector = None
    parameter_boxes_replayed = 0
    adaptive_splits = 0
    maximum_depth = 0
    coarse_boxes_completed = 0

    def enclose_box(xlo, xhi, ylo, yhi, depth):
        nonlocal parameter_boxes_replayed
        x = arb((xlo+xhi)/2, (xhi-xlo)/2)
        y = arb((ylo+yhi)/2, (yhi-ylo)/2)
        z = acb(x, -y)
        z_squared = z*z
        log_first, log_second = acb(0), acb(0)
        for gamma2 in gamma_squared:
            factor_denominator = gamma2-z_squared
            if factor_denominator.contains(0):
                return None
            log_first += -2*z/factor_denominator
            log_second += -2*(gamma2+z_squared)/(factor_denominator*factor_denominator)
        real_lower, modulus_upper = None, None
        for a in parameter_intervals:
            parameter_boxes_replayed += 1
            gaussian_first = log_first-2*a*z
            gaussian_second = log_second-2*a
            companion_over_base = 1-imaginary_unit*lam*gaussian_first
            derivative_over_base = (gaussian_first-imaginary_unit*lam*
                                   (gaussian_first*gaussian_first+gaussian_second))
            if derivative_over_base.contains(0):
                return None
            w = imaginary_unit*companion_over_base/derivative_over_base
            if not w.is_finite() or not w.real > 0:
                return None
            local_real = w.real.lower().fmpq()
            local_abs = abs(w).upper().fmpq()
            if not local_real > 0 or not local_abs > 0:
                return None
            real_lower = local_real if real_lower is None else min(real_lower, local_real)
            modulus_upper = local_abs if modulus_upper is None else max(modulus_upper, local_abs)
        tau = arb(real_lower/modulus_upper)
        beta = arb(modulus_upper)*(2*j1+lam*(j1*j1+j2))
        acceptance = tau-alpha-(1+tau)*beta
        if not beta < 1 or not acceptance > 0:
            return None
        actual_sector = arb(real_lower)-arb(modulus_upper)*(alpha+beta)/(1-beta)
        if not actual_sector > 0:
            return None
        return {
            "x_interval": [str(xlo), str(xhi)],
            "y_interval": [str(ylo), str(yhi)],
            "refinement_depth": depth,
            "all_parameter_bins_replayed": a_subdivisions,
            "family_Re_W_lower": str(real_lower),
            "family_abs_W_upper": str(modulus_upper),
            "acceptance_margin_lower": str(acceptance.lower().fmpq()),
            "actual_Re_W_lower": str(actual_sector.lower().fmpq()),
        }

    def cover_box(xlo, xhi, ylo, yhi, depth):
        nonlocal adaptive_splits, maximum_depth
        maximum_depth = max(maximum_depth, depth)
        enclosure = enclose_box(xlo, xhi, ylo, yhi, depth)
        if enclosure is not None:
            cells.append(enclosure)
            return
        need(depth < 8, f"adaptive Gaussian enclosure exhausted at {xlo},{xhi},{ylo},{yhi}")
        adaptive_splits += 1
        xm, ym = (xlo+xhi)/2, (ylo+yhi)/2
        # The four exact children cover the whole parent before it returns.
        for xl, xh in [(xlo, xm), (xm, xhi)]:
            for yl, yh in [(ylo, ym), (ym, yhi)]:
                cover_box(xl, xh, yl, yh, depth+1)

    for ix in range(t_subdivisions):
        for iy in range(y_subdivisions):
            cover_box(fmpq(ix, 8), fmpq(ix+1, 8),
                      fmpq(iy, 16), fmpq(iy+1, 16), 0)
            coarse_boxes_completed += 1
        if ix % 8 == 7:
            print("REPLAYED_GAUSSIAN_COMPACT_BOXES", len(cells),
                  "PARAMETER_BOXES", parameter_boxes_replayed,
                  "ADAPTIVE_SPLITS", adaptive_splits, flush=True)
    need(t_subdivisions == 8*t_max and y_subdivisions == 8,
         "exact compact-grid coverage")
    need(coarse_boxes_completed == t_subdivisions*y_subdivisions and
         len(cells) == coarse_boxes_completed+3*adaptive_splits,
         "complete adaptive compact and parameter box coverage")
    minimum_acceptance = min(fmpq(c["acceptance_margin_lower"]) for c in cells)
    minimum_actual_sector = min(fmpq(c["actual_Re_W_lower"]) for c in cells)

    source_paths = [Path(__file__).resolve(), directory/"produce_native_candidates.py",
                    candidate_path, directory/"FINITE_CENSUS_COMPLEMENT.md",
                    directory/"NATIVE_SLAB_CERTIFICATE.md",
                    directory/"GAUSSIAN_TAIL_TRANSPORT.md",
                    directory/"GAUSSIAN_SLAB_CERTIFICATE.md",
                    directory.parent.parent/"heights"/"COARSE_ZERO_COUNT.md"]
    package = Path(flint.__file__).resolve().parent
    binaries = [package/"types"/"arb.abi3.so", package/"types"/"acb.abi3.so"]
    binaries.extend(sorted((package.parent/"python_flint.libs").glob("lib*.so*")))
    report = {
        "status": "PASS_DIRECTED_NATIVE_GAUSSIAN_SLAB",
        "primitive_source": "Actual xi through directed zeta and Gamma; complete-count FLINT contract explicitly imported.",
        "normalization": "Xi(z)=xi(1/2+i*z)",
        "derivative_order": 0,
        "frozen_lambda": "10",
        "domain": {"T": ["-13", "13"], "y": ["0", "1/2"], "z": "T-i*y"},
        "coverage": "All 104 by 8 positive-T coarse boxes, with every failed enclosure replaced by all four exact dyadic children; all accepted leaves and all 32 parameter bins are replayed. Exact even-real symmetry reflects the full cover.",
        "reflection_identity": "W(-conjugate(z))=conjugate(W(z)) for the actual even real Xi and each even real Gaussian base.",
        "parameter": {"unknown": "a_1=sum complete tail m/rho^2", "range": "[0,S]",
                      "whole_range_enclosed": True, "bin_endpoints": "j*S/32 for j=0,...,32",
                      "quadratic_tail_absorbed_exactly": True},
        "arithmetic": "Arb/acb outward ball arithmetic at 128 bits; exact dyadic root/domain inputs; directed full-parameter bins; exact rational output bounds.",
        "complete_census_height": height,
        "imported_complete_count": count,
        "replayed_disjoint_sign_crossing_brackets": len(intervals),
        "census_interval_width": "1/16777216",
        "directed_xi_half": str(xi_half),
        "native_complete_count_dependencies": "FLINT3.6.0 complete-count contract and its finite Gram/Rosser rule input at this index; historical finite rule not independently replayed.",
        "tail": {"source": "COARSE_ZERO_COUNT.md and complete paired tail; hidden nonreal zeros above R are allowed.",
                 "S_upper": str(tail_sum.upper().fmpq()), "B": "105/8",
                 "residual_log_first_upper": str(j1.upper().fmpq()),
                 "residual_log_second_upper": str(j2.upper().fmpq())},
        "all_positive_T_boxes": cells,
        "parameter_boxes_replayed": parameter_boxes_replayed,
        "accepted_parameter_boxes": len(cells)*a_subdivisions,
        "coarse_boxes_completed": coarse_boxes_completed,
        "adaptive_splits": adaptive_splits,
        "maximum_refinement_depth": maximum_depth,
        "minimum_acceptance_margin_lower": str(minimum_acceptance),
        "minimum_actual_Re_W_lower": str(minimum_actual_sector),
        "python_flint_version": flint.__version__,
        "flint_version": flint.__FLINT_VERSION__,
        "source_sha256": {str(p.relative_to(directory.parent.parent)):digest(p) for p in source_paths},
        "backend_binary_sha256": {p.name:digest(p) for p in binaries},
        "strict_acceptance": "Every native bracket and every domain/parameter box must pass; beta<1 and alpha+(1+tau)*beta<tau strictly on all boxes.",
        "actual_primitive_endpoints_replayed": True,
        "different_arithmetic_implementation_used": False,
        "historical_Gram_Rosser_verification_replayed": False,
        "infinite_count_or_product_theorem_authenticated_by_checker": False,
        "cofinal_domain_certified": False,
        "rh_proved": False,
    }
    (directory/"gaussian_slab_certificate.json").write_text(
        json.dumps(report, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    print(report["status"], f"census={count}", f"boxes={len(cells)}",
          f"parameter_boxes={parameter_boxes_replayed}",
          f"approx_minimum_acceptance={float(minimum_acceptance):.6f}",
          f"approx_minimum_Re_W={float(minimum_actual_sector):.6f}", flush=True)


if __name__ == "__main__":
    main()

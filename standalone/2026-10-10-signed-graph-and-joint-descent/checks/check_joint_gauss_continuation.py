#!/usr/bin/env python3
"""Exact algebra and source-pin diagnostics for the joint Gauss continuation.

This checks finite rational calculations and exact source bytes.  It does not
prove theta identities, large sieves, normal convergence, moments, or RH.
Run with --repo pointing at the source repository.  Checks use explicit
exceptions, so python -O does not disable them.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import subprocess


PROOF_NAME = "JOINT_GAUSS_REUNION_CONTINUATION.md"
PROOF_SHA256 = "31e2395999301d56ce63751db7c907fc6147b689574aaf268133d706ad3aa0aa"
PR924 = "725b2d25ab47e57500049d93985560098c7ef3fa"
PR922 = "f71a9bc6ac3ce59a3c19d7e842a3fa082ecfbe32"
PR926 = "086bf0560c0c2679a1fe41418f583d2c5ca743c3"
P924 = "standalone/2026-10-10-sextic-moving-labels/"
P922 = "standalone/2026-10-10-signed-covariance-descent/"
P926 = "standalone/2026-10-10-mobius-overlaps-and-sampled-moments/"
SOURCES = [
    (PR924, P924 + "ANISOTROPIC_A2_NORM_TRANSFER.md", "e671b8b1c8717ed494b3db0ba39fb4c0de374aef56f774bf9a7ca68e01b277cf", "main: all-row anisotropic inverse for every R > 0"),
    (PR924, P924 + "MIXED_LABEL_COMPLETION.md", "5e77ec88d6a191ec214bcedebc2b42d37f95735ba2bb18955b2f8a16aedfbcad", "main: counting completion, outer multiplier, exact cube identities"),
    (PR924, P924 + "SIXTH_POWER_STRATIFIED_INVERSE.md", "f98cc20e361ebb99af7dbd4b5ffef83a8a55ca11c4d3f24da238bc24be4cb2e9", "main: sixth-free sieve and exact row stratification"),
    (PR924, P924 + "OPTIMAL_SIEVE_SPECTRAL_EXTENSION.md", "b0d3eee6d32ad7f69bfdd8ac5132c60139f322b1102086897ce0099defab8551", "comparison only: old 4/7 canonical mean"),
    (PR922, P922 + "SECOND_REFLECTION_BOOTSTRAP.md", "e1db605878eb805a3d21f908ea1c73f5869d56c112a3c3e91e67d9b715b16fd0", "main: exact cube reunion and conditioned coefficients"),
    (PR922, P922 + "FULL_CUSP_DESCENT.md", "b025af8af1ac13d07a04fbc7de71401d2a47ef2c8df5a1e89a4edc4973482504", "main: exact full cusp identity and bad-label mass"),
    (PR922, P922 + "FINITE_RAY_REUNION.md", "8897088fb7e89c66e18bf0652a913983c5120a61d854591f990cce2a6261f2e0", "main: actual finite rays, entire finite coefficients, gamma factor"),
    (PR922, P922 + "FINITE_CUBE_HOMOGENEITY.md", "e4f7b3ff0817c4b6deaf2e608657425c06ac97c1a7f4f60f3762eba7eca7b0e1", "main: fixed finite character support and cube covariance"),
    (PR922, P922 + "ALL_CUSP_COEFFICIENT_ADAPTER.md", "bfabc37c5b16a32d6b29fe5767f58f5f5a8dc161aaa3d127ebf11236fa2d3ca1", "main: full nonzero frequency and cusp support table"),
    (PR926, P926 + "SAMPLED_MOMENT_CRITERION.md", "18bf2fdad438eb21ae3318eba7d42e9c03803b2dd1abc4d8f6448fb3b04499de", "comparison only: signed scale sampling barriers"),
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def serial(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, dict):
        return {key: serial(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [serial(item) for item in value]
    return value


def locate_proof(explicit: Path | None) -> Path:
    if explicit is not None:
        return explicit
    base = Path(__file__).resolve().parent
    for candidate in (base / PROOF_NAME, base.parent / PROOF_NAME):
        if candidate.is_file():
            return candidate
    raise RuntimeError("Supply --proof: the adjacent proof could not be found")


def source_bindings(repo: Path, proof: Path) -> dict:
    observed = hashlib.sha256(proof.read_bytes()).hexdigest()
    require(observed == PROOF_SHA256, "Review target proof bytes have changed")
    bindings = []
    for commit, path, expected, role in SOURCES:
        blob = subprocess.check_output(["git", "show", f"{commit}:{path}"], cwd=repo)
        got = hashlib.sha256(blob).hexdigest()
        require(got == expected, f"Source binding failed: {commit}:{path}")
        bindings.append({"commit": commit, "path": path, "sha256": got, "role": role})
    return {
        "proof": {"file": PROOF_NAME, "sha256": observed},
        "verified_commit_path_bindings": len(bindings),
        "sources": bindings,
        "inherited_import_declaration": {
            "repository": "OpenAI/math",
            "commit": "adc7f1241b42e322a6451854ab7e4b4c146bf78a",
            "source": "October 5 paper2.tex",
            "sha256": "d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d",
            "verification_scope": "Declared in the verified source notes; this script does not revalidate the imported theta foundation.",
        },
    }


def six_terms() -> dict:
    # Coordinates are H, F, A, B, R. The actual source leading term is HA.
    terms = {
        "HA": (Q(1), Q(0), Q(1), Q(0), Q(0)),
        "middle_short": (Q(2), Q(1), Q(1), Q(-1, 2), Q(3, 2)),
        "third_short": (Q(4, 3), Q(2, 3), Q(4, 3), Q(-2, 3), Q(2)),
        "H": (Q(1), Q(0), Q(0), Q(0), Q(0)),
        "AB_tail": (Q(0), Q(0), Q(1), Q(1), Q(-3)),
        "mixed_tail": (Q(2, 3), Q(0), Q(2, 3), Q(2, 3), Q(-2)),
    }
    cutoff = (Q(-8, 21), Q(-2, 9), Q(-1, 15), Q(1, 3))
    target = (Q(10, 7), Q(2, 3), Q(6, 5), Q(0))
    expected = {
        "HA": (Q(1), Q(0), Q(1), Q(0)),
        "middle_short": (Q(10, 7), Q(2, 3), Q(9, 10), Q(0)),
        "third_short": (Q(4, 7), Q(2, 9), Q(6, 5), Q(0)),
        "H": (Q(1), Q(0), Q(0), Q(0)),
        "AB_tail": (Q(8, 7), Q(2, 3), Q(6, 5), Q(0)),
        "mixed_tail": (Q(10, 7), Q(4, 9), Q(4, 5), Q(0)),
    }
    result = {}
    for name, source in terms.items():
        got = tuple(source[i] + source[4] * cutoff[i] for i in range(4))
        require(got == expected[name], f"Wrong substituted monomial: {name}")
        require(got[3] == 0, f"Uncancelled longer-axis power: {name}")
        gaps = tuple(target[i] - got[i] for i in range(4))
        require(all(gap >= 0 for gap in gaps), f"Uniform envelope does not dominate {name}")
        result[name] = {"H_F_A_B": got, "target_minus_term": gaps}
    require(target[0] / 2 == Q(5, 7), "Wrong row norm exponent")
    require(target[1] / 2 == Q(1, 3), "Wrong auxiliary norm exponent")
    require(target[2] / 2 == Q(3, 5), "Wrong shorter-axis norm exponent")
    return {"cutoff_H_F_A_B": cutoff, "target_H_F_A_B": target, "six_terms": result}


def domains() -> dict:
    # Independent finite checks of both affine coordinate transformations.
    count = 0
    old_count = 0
    for si in range(-60, 41):
        sigma = Q(si, 20)
        for vi in range(-60, 81):
            tau = Q(vi, 20)
            T, U = 1 - sigma, tau - sigma
            direct = sigma < Q(1, 2) and U > Q(1, 2) and tau - 2 * sigma > Q(3, 5)
            joint = T > Q(1, 2) and U > Q(1, 2) and T + U > Q(8, 5)
            alternative = U > Q(1, 2) and tau < min(U + Q(1, 2), 2 * U - Q(3, 5))
            require(direct == joint == alternative, "Tube coordinate mismatch")
            old = U > Q(1, 2) and tau < min(U, (3 * U - 1) / 2)
            if old:
                old_count += 1
                require(direct, "Old source tube escaped new tube")
            if tau == 1:
                require(direct == (sigma < Q(1, 5)), "Wrong strict v=1 crossing")
            count += 1

    # Exact positive linear-combination certificates, not just grid tests.
    # New slacks: e1=T-1/2, e2=U-1/2, e3=T+U-8/5.
    z_threshold = Q(8, 5) + 2 * Q(1, 2) - Q(1, 2)
    require(z_threshold == Q(21, 10), "Wrong correction denominator infimum")
    z_count_exponent = z_threshold - Q(1, 3)
    require(z_count_exponent == Q(53, 30) and z_count_exponent > 1, "Auxiliary ideal sum lacks absolute margin")
    # Old: 2T+U>3 and U>1/2 imply T+U>7/4.
    old_sum_threshold = Q(3, 2) + Q(1, 4)
    require(old_sum_threshold - Q(8, 5) == Q(3, 20), "Old-to-new inclusion certificate failed")
    require(Q(10, 7) + 2 == Q(24, 7), "Reflected row exponent mismatch")
    return {
        "exact_grid_points": count,
        "old_tube_points_checked": old_count,
        "new_tube": ["Re(t)>1/2", "Re(u)>1/2", "Re(t+u)>8/5"],
        "source_coordinates": {"t": "1-s", "u": "v-s", "w": "u+2t-1/2"},
        "strict_v_1_crossing": "Re(s)<1/5",
        "positive_linear_certificates": {
            "cube_Euler_margin": "Re(3t-1/2)-1 = 3*(Re(t)-1/2)",
            "correction_margin": "Re(t+w)-21/10 = 2*(Re(t)-1/2)+(Re(t+u)-8/5)",
            "old_sum_margin": "Re(t+u)-7/4 = (2Re(t)+Re(u)-3)/2+(Re(u)-1/2)/2",
            "old_to_new_sum_gap": Q(3, 20),
            "correction_ideal_exponent_infimum": z_count_exponent,
            "correction_ideal_margin_over_1": z_count_exponent - 1,
            "bad_ramified_margin": "Re(t)-1/6 = (Re(t)-1/2)+1/3",
            "bad_cube_margin": "3Re(t)-1/2 = 3*(Re(t)-1/2)+1",
        },
        "growth": {
            "B_row_energy_H": Q(10, 7),
            "B_row_energy_F": Q(2, 3),
            "Y_squarefree_row_energy_H": Q(10, 7),
            "reflected_row_energy_H": "24/7-4Re(s)",
            "vertical_scope": "Polynomial on each closed bounded real subregion with strict margins; the degree may depend on that subregion and the fixed source weight seminorms.",
        },
    }


def coefficient_exponents() -> dict:
    # Affine exponents represented in the basis (t,u,1).
    t = (Q(1), Q(0), Q(0))
    u = (Q(0), Q(1), Q(0))
    v = (Q(-1), Q(1), Q(1))
    w = (Q(2), Q(1), Q(-1, 2))
    one = (Q(0), Q(0), Q(1))
    add = lambda a, b: tuple(x + y for x, y in zip(a, b))
    sub = lambda a, b: tuple(x - y for x, y in zip(a, b))
    require(add(u, sub(one, v)) == t, "Conditioned d denominator is not Nd^t")
    require(add(t, w) == (Q(3), Q(1), Q(-1, 2)), "Wrong exterior z denominator")
    cube_denominator = (Q(3), Q(0), Q(-1, 2))
    require(sub(cube_denominator, sub(one, v)) == w, "K_p*y_p norm exponent does not equal x_p")
    return {
        "checked_affine_identities": 3,
        "conditioned_d_denominator": "u+1-v=t",
        "cube_local_identity": "K_p*y_p=x_p, since (3t-1/2)-(1-v)=w and kappa*c_k=chi_k^-",
        "correction_denominator": "t+w=u+3t-1/2",
        "exact_outer_coefficient": "mu_K(z)*a_k(z)*chi_k^-(z)/(Nz)^(t+w)",
        "inner_character_placement": "kappa is on m in B_{k,z}^{varrho,kappa}(t,u)",
        "auxiliary": "f=z; the fourth-power twist retains its zero when (am,z)>1, so the additional exclusion Q is 1",
        "row_overlap": "If (z,k)>1 the exterior coefficient is zero; no coprimality hypothesis between k and f was used in the raw norm.",
        "phase_limit": "Only norm-exponent algebra is computationally checked here. Exact Gauss CRT phases and reciprocal-primary orientation are proved in the manuscript using the pinned sources.",
    }


def cusp_domains() -> dict:
    # Unit exponents are modulo six, with omega=zeta_6^2 and -1=zeta_6^3.
    inspected, supported = 0, 0
    for cusp in ("0", "-", "+"):
        for j in range(-6, 43):
            for unit in range(6):
                inspected += 1
                if cusp == "0":
                    first = j >= -3 and (j + 3) % 3 == 0 and unit in (0, 3)
                    second = j >= -1 and (j + 4) % 3 == 0
                    require(not (first and second), "Overlapping standard-cusp table rows")
                    active = first or second
                    if first:
                        r = Q(j + 3, 3)
                        scalar_squared_log3 = r + 5
                    elif second:
                        r = Q(j + 4, 3)
                        scalar_squared_log3 = r + 4
                elif cusp == "-":
                    active = j == -4 and unit in {(3 + 2 * (h + 1)) % 6 for h in range(3)}
                    scalar_squared_log3 = Q(4)
                else:
                    active = j == -4 and unit in {(2 * (h - 1)) % 6 for h in range(3)}
                    scalar_squared_log3 = Q(4)
                if active:
                    supported += 1
                    require(j >= -4, "A forbidden ramified sector was included")
                    require(scalar_squared_log3 <= 6 + Q(j, 3), "Source cusp scalar bound failed")
    prime_cases = 0
    for exponent in range(25):
        for added_cube_valuation in range(12):
            prime_cases += 1
            new_exponent = exponent + 3 * added_cube_valuation
            require((exponent % 3 != 2) == (new_exponent % 3 != 2), "Cube multiplication changes theta support")
            if exponent % 3 != 2:
                n = exponent % 3
                b = exponent // 3
                require(n in (0, 1) and exponent == n + 3 * b, "Squarefree/cube decomposition failed")
    return {
        "finite_table_entries_checked": inspected,
        "supported_entries_in_finite_window": supported,
        "prime_valuation_support_checks": prime_cases,
        "raw_tests": {
            "class": "Complex smooth functions of positive ideal norm, each compactly supported in a fixed interval inside (0,infinity).",
            "dyadic_tests": "W_t(x)=x^(-t)W_0(x), W_u(x)=x^(-u)W_0(x), and a fixed first block covering norm 1.",
            "uniformity": "Every required fixed derivative seminorm grows polynomially in Im(t),Im(u) on a bounded real strip. The counting theorem is used; no arbitrary row-dependent coefficient is allowed.",
            "scales": "H,F>=1; nonempty factor scales below 1 have a fixed support-dependent positive lower bound. The exact inverse allows every R>0, with its stratum support caps retained.",
        },
        "raw_rows": "All nonzero element rows in H<=Nk<2H, or any subset, with fixed reciprocity and unit classes retained.",
        "reunited_rows": "Only the original squarefree primary k coprime to S; all-row B does not extend the scope of the exact source identity for Y.",
        "frequency_lattice": "ell in lambda^(-4) O_K, ell != 0, with every supported source cusp sector retained.",
        "zero_frequency": "Not included: Y and the reflected object here are the exact nonzero-frequency objects defined by PR #922.",
        "frequency_decomposition": "ell=epsilon*lambda^j*n0*n*(b0*b)^3; n,n0 squarefree, b,b0 arbitrary; (n,b)=1 is not required.",
        "good_indices": "n,b are primary and avoid S; all physical raw indices and auxiliaries avoid S.",
        "bad_indices": "n0 is one of finitely many squarefree S-supported ideals away from lambda; b0 has arbitrary nonnegative valuations on the same fixed set; all j and unit sectors below are retained.",
        "cusp_table": [
            {"cusp": "0", "j": "3r-3, r>=0", "epsilon": "+1 or -1", "scalar": "3^(r/2+5/2)"},
            {"cusp": "0", "j": "3r-4, r>=1", "epsilon": "+/-omega^h, h=0,1,2", "scalar": "3^(r/2+2)*a_h; a=(1,zeta9,zeta9^-1)"},
            {"cusp": "-", "j": "-4", "epsilon": "-omega^(h+1), h=0,1,2", "scalar": "9*c_h; c=(1,omega^2*zeta9,omega*zeta9^-1)"},
            {"cusp": "+", "j": "-4", "epsilon": "omega^(h-1), h=0,1,2", "scalar": "9*c_h"},
        ],
        "cusp_phases": "E_0(ell)=1 and E_-(ell)=E_+(ell)=breve-e(ell); the intrinsic additive phases are retained before fixed finite Fourier expansion.",
        "finite_character_support": "varrho^3=conjugate(rho)^3 for each actual sector, with kappa=eta*rho^3; the group is fixed independently of k and the bad cube/ramified indices.",
        "total_bad_label_mass": "Bounded on strict Re(t)>1/6; the new domain has Re(t)>1/2. No cross-cusp terms are dropped in the row norm.",
        "limit": "The finite table checks do not prove any imported theta coefficient or infinite cusp sum identity.",
    }


def physical_comparison() -> dict:
    small_h = Q(7, 10) / Q(4, 7)
    large_h = Q(4, 5) / Q(53, 42)
    mixed_h = Q(2, 15) / Q(16, 21)
    require(small_h == Q(49, 40), "Wrong counting-completion threshold")
    require(large_h == Q(168, 265), "Wrong repeated-row threshold")
    require(mixed_h == Q(7, 40), "Wrong classical mixed threshold")
    require(large_h >= mixed_h and large_h <= small_h, "Physical comparison ranges do not cover all heights")
    # Cube weights after taking square roots of H, H^(1/6)L, (HL)^(2/3).
    cube_weights = (Q(-1), Q(-1) - Q(3, 2), Q(-1) - Q(1))
    require(cube_weights == (Q(-1), Q(-5, 2), Q(-2)), "Grouped full-cube normalization error")
    return {
        "hypothetical_scalar_candidate": "H^(10/7)*D^(6/5)",
        "counting_completion": "HD+H^2*D^(1/2)+H^(4/3)*D^(2/3)",
        "counting_dominates_candidate_when_H_at_most_D_power": small_h,
        "classical_full_cube_completion": "H+H^(1/6)*D^2+(H*D^2)^(2/3)",
        "classical_dominates_candidate_when_H_at_least_D_power": large_h,
        "classical_mixed_threshold": mixed_h,
        "same_completed_family_cube_norm_weights": cube_weights,
        "coverage": "The two ranges overlap and cover all H,D>=1, up to the stated arbitrary small powers.",
        "limit": "No physical Mellin contour transfer is asserted, and the hypothetical candidate does not improve the available same-family envelope.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--proof", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = {
        "status": "finite_algebra_and_source_bindings_pass",
        "scope": "Exact rational diagnostics and source byte bindings; not an independent analytic proof.",
        "source_bindings": source_bindings(args.repo, locate_proof(args.proof)),
        "six_term_optimization": six_terms(),
        "domains_and_growth": domains(),
        "coefficient_exponents": coefficient_exponents(),
        "tests_frequencies_and_cusps": cusp_domains(),
        "physical_comparison": physical_comparison(),
        "extra_optimal_sieve_used_in_main_proof": False,
        "not_established_by_this_script": [
            "Imported theta automorphy or Gauss coefficient identities",
            "The source large-sieve and completed-norm theorems",
            "Infinite normal convergence or analytic continuation",
            "Finite-height signed Möbius or A2 covariance estimates",
            "A fourth moment, 17/24 zero-free result, or the Riemann hypothesis",
        ],
    }
    encoded = json.dumps(serial(report), indent=2, sort_keys=True) + "\n"
    if args.output is not None:
        args.output.write_text(encoded, encoding="utf-8")
    print(encoded, end="")


if __name__ == "__main__":
    main()

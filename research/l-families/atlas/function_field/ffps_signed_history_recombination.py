#!/usr/bin/env python3
"""Exact signed history aggregation, with the native principal weights retained.

Finite matrices are coefficients of Hermitian polynomials in symbolic native
amplitudes.  No arbitrary rational test vector is promoted to a native input.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import subprocess
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
NOTE = HERE / "FFPS_SIGNED_HISTORY_RECOMBINATION.md"
FIXTURE = HERE / "ffps_signed_history_recombination.json"
MANIFEST = HERE / "ffps_signed_history_recombination.sources.json"
TEST = ROOT / "tests/test_ffps_signed_history_recombination.py"
COLLISION_PATH = HERE / "ffps_live_shared_fibre_collisions.py"
MAX_BYTES = 196608
MAX_GROUPS = 16
MAX_HISTORIES = 100
MAX_BITS = 64

SOURCE_ROWS = [
    (
        "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc",
        "claims/lemmas/L-102883-balanced-vaughan-free-energy-and-equal-product-cost-are-subpower.md",
        "b8a6eed2c8dda7d0ed28a8dd18fc57387e4c2e7b",
    ),
    (
        "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc",
        "claims/theorems/T-102990-equal-pair-boolean-core-incidence-frontier.md",
        "b319572db9ecc89bc528b85368cbf49aa13206d0",
    ),
    (
        "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "claims/lemmas/L-106120-bilateral-least-prime-phases-form-a-tensor-kummer-family.md",
        "a8d829dc10611adb7bfb4853902bdff0ab02a065",
    ),
    (
        "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "claims/lemmas/L-106121-bilateral-tensor-moment-has-a-paid-atomic-diagonal.md",
        "955c3ed0363ca330439eedbae1bf0041a4c96468",
    ),
    (
        "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "claims/lemmas/L-106131-wick-normal-ordering-additive-kummer-decomposition.md",
        "37722c3f36ec7d1681f34d4329a3795e5028f7ae",
    ),
    (
        "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "claims/lemmas/L-106191-source-dual-centered-double-incidence-correlation.md",
        "85c4ef92ead7d8b235f9c195c3c0acd16d16030f",
    ),
    (
        "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "claims/theorems/T-106140-wick-centered-additive-kummer-conjunction-frontier.md",
        "d5be8e376c88b63de0be19e0d9e8791624e99ae2",
    ),
    (
        "5dc85cd5e38384efc3b8a65496f03e1c2ae599e3",
        "research/l-families/atlas/function_field/FFPS_LIVE_SHARED_FIBRE_COLLISIONS.md",
        "b12efe62a07fa12843937f715adaa87ae769f2e8",
    ),
    (
        "5dc85cd5e38384efc3b8a65496f03e1c2ae599e3",
        "research/l-families/atlas/function_field/ffps_live_shared_fibre_collisions.py",
        "641a746ca6a4af2d041e238399c55dfe8e5c6424",
    ),
]

SPEC = importlib.util.spec_from_file_location(
    "recombination_locked_collisions", COLLISION_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load the source-locked collision producer")
collision = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = collision
SPEC.loader.exec_module(collision)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def render(value: object) -> str:
    return json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True) + "\n"


def digest(data: bytes) -> str:
    return hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()


def exact(value: int | Fraction) -> Fraction:
    require(type(value) is int or type(value) is Fraction, "exact rational required")
    answer = Fraction(value)
    require(
        max(answer.numerator.bit_length(), answer.denominator.bit_length()) <= MAX_BITS,
        "rational input cap exceeded",
    )
    return answer


def channel_weights(ell: int, rho: int) -> dict[str, Fraction]:
    collision.validate_conductors(ell, rho)
    d = Fraction((ell - 1) * (rho - 1), ell * rho)
    p = Fraction((ell + 1) * (rho + 1), ell * rho * (ell - 1) * (rho - 1))
    require(d >= p > 0, "channel atomic weights are inconsistent")
    return {"additive": d, "principal": p, "Kummer": d - p}


def incidence_kernel(
    ell: int, rho: int, left: tuple[int, int], right: tuple[int, int]
) -> Fraction:
    return (int(left[0] == right[0]) - Fraction(1, ell)) * (
        int(left[1] == right[1]) - Fraction(1, rho)
    )


def validate_groups(ell: int, rho: int, groups: tuple[dict, ...]) -> None:
    collision.validate_conductors(ell, rho)
    require(
        type(groups) is tuple and 1 <= len(groups) <= MAX_GROUPS,
        "group count/type outside replay scope",
    )
    labels = set()
    classes = set()
    total = 0
    for group in groups:
        require(
            type(group) is dict and set(group) == {"label", "cell", "coefficients"},
            "group schema differs",
        )
        label = group["label"]
        require(
            type(label) is str and label and label not in labels,
            "group labels must be distinct nonempty strings",
        )
        labels.add(label)
        cell = group["cell"]
        require(
            type(cell) is tuple and len(cell) == 2, "cell must be a coordinate pair"
        )
        require(
            all(type(x) is int for x in cell)
            and 0 < cell[0] < ell
            and 0 < cell[1] < rho,
            "cell must contain unit residues",
        )
        classes.add(
            (
                collision.legendre_symbol(cell[0], ell),
                collision.legendre_symbol(cell[1], rho),
            )
        )
        coefficients = group["coefficients"]
        require(
            type(coefficients) is tuple and 1 <= len(coefficients) <= MAX_HISTORIES,
            "history group cap/type exceeded",
        )
        for value in coefficients:
            exact(value)
        total += len(coefficients)
    require(total <= MAX_HISTORIES, "total literal history cap exceeded")
    require(
        len(classes) == 1, "all cells must remain in the same fixed quadratic fibre"
    )


def matrices(ell: int, rho: int, groups: tuple[dict, ...]) -> dict:
    """Coefficient matrices in w_i conjugate(w_j), with z_ih=c_ih*w_i."""

    validate_groups(ell, rho, groups)
    weights = channel_weights(ell, rho)
    sums = [sum(map(exact, group["coefficients"]), Fraction()) for group in groups]
    energies = [
        sum((exact(x) ** 2 for x in group["coefficients"]), Fraction())
        for group in groups
    ]
    deltas = [b * b - e for b, e in zip(sums, energies)]
    channels = {}
    size = len(groups)
    for channel, atomic in weights.items():
        literal = [[Fraction() for _ in groups] for _ in groups]
        grouped = [[Fraction() for _ in groups] for _ in groups]
        direct = [[Fraction() for _ in groups] for _ in groups]
        for i, j in product(range(size), repeat=2):
            kernel = incidence_kernel(ell, rho, groups[i]["cell"], groups[j]["cell"])
            if channel == "principal":
                kernel = weights["principal"]
            elif channel == "Kummer":
                kernel -= weights["principal"]
            literal[i][j] = kernel * (deltas[i] if i == j else sums[i] * sums[j])
            grouped[i][j] = Fraction() if i == j else kernel * sums[i] * sums[j]
            for h, left in enumerate(groups[i]["coefficients"]):
                for k, right in enumerate(groups[j]["coefficients"]):
                    if i != j or h != k:
                        direct[i][j] += kernel * exact(left) * exact(right)
            require(
                direct[i][j] == literal[i][j], "literal off-history replay mismatch"
            )
            correction = atomic * deltas[i] if i == j else Fraction()
            require(
                literal[i][j] - grouped[i][j] == correction,
                "history correction identity failed",
            )
        channels[channel] = {
            "literal": literal,
            "grouped": grouped,
            "correction_diagonal": [atomic * delta for delta in deltas],
        }
    for i, j in product(range(size), repeat=2):
        for resolution in ("literal", "grouped"):
            require(
                channels["additive"][resolution][i][j]
                - channels["Kummer"][resolution][i][j]
                == channels["principal"][resolution][i][j],
                "signed principal recombination failed",
            )
    for group, energy, delta in zip(groups, energies, deltas):
        count = len(group["coefficients"])
        require(
            -energy <= delta <= (count - 1) * energy,
            "representation energy bound failed",
        )
        require(
            abs(delta) <= (count - 1) * energy, "absolute representation bound failed"
        )
    return {
        "weights": weights,
        "sums": sums,
        "energies": energies,
        "deltas": deltas,
        "channels": channels,
    }


def encode_matrix_report(report: dict) -> dict:
    return {
        "weights": {key: str(value) for key, value in report["weights"].items()},
        "group_coefficient_sums": list(map(str, report["sums"])),
        "literal_group_energies": list(map(str, report["energies"])),
        "group_energy_corrections": list(map(str, report["deltas"])),
        "Hermitian_polynomial_channels": {
            channel: {
                "literal": [[str(x) for x in row] for row in values["literal"]],
                "grouped": [[str(x) for x in row] for row in values["grouped"]],
                "correction_diagonal": list(map(str, values["correction_diagonal"])),
            }
            for channel, values in report["channels"].items()
        },
        "coefficient_variables": "symbolic complete native w_i; not declared independently admissible",
    }


def owner_panel_report(panel: dict) -> dict:
    source = collision.arithmetic_panel(**panel)
    records = source["arithmetic_atoms_after_one_sided_equal_product_aggregation"]
    coefficients = tuple(
        left["coefficient"] * right["coefficient"]
        for left, right in product(
            source["left_boolean_source"]["ordered_histories"],
            source["right_boolean_source"]["ordered_histories"],
        )
    )
    groups = tuple(
        {"label": f"pair_{i}", "cell": tuple(row["cell"]), "coefficients": coefficients}
        for i, row in enumerate(records)
    )
    report = matrices(source["ell"], source["rho"], groups)
    share = Fraction(source["equal_pair_share_per_history"]) ** 2
    physical = []
    for row, delta in zip(records, report["deltas"]):
        reciprocal = share * share / (source["common_core"] ** 2 * row["P"] * row["Q"])
        physical.append(
            {
                **row,
                "one_history_rescaled_norm_prefactor": str(reciprocal),
                "principal_correction_prefactor": str(
                    report["weights"]["principal"] * delta * reciprocal
                ),
            }
        )
    corners = []
    for i, j in ((0, 3), (1, 2)):
        owners = set(
            records[i]["left_owner_labels"]
            + records[i]["right_owner_labels"]
            + records[j]["left_owner_labels"]
            + records[j]["right_owner_labels"]
        )
        require(len(owners) == 8, "opposite-corner pair shares an owner label")
        require(
            records[i]["N"] != records[j]["N"] and records[i]["M"] != records[j]["M"],
            "opposite corners have an equal physical side",
        )
        corners.append(
            {
                "groups": [i, j],
                "distinct_owner_label_count": len(owners),
                "additive_cross_coefficient": str(
                    report["channels"]["additive"]["grouped"][i][j]
                ),
                "principal_cross_coefficient": str(
                    report["channels"]["principal"]["grouped"][i][j]
                ),
                "history_correction_on_this_cross_term": "0",
            }
        )
    return {
        "name": source["name"],
        "horizon": source["horizon"],
        "cutoff": source["frozen_cutoff"],
        "fibre": [
            source["common_core"],
            source["ell"],
            source["rho"],
            source["sigma"],
            source["tau"],
        ],
        "native_rescaled_one_history_amplitude": "w_ij=(1/36)*gamma_ij(t)/(g*sqrt(P_i*Q_j)); gamma retains all non-Boolean source labels and weights",
        "arithmetic_pairs": physical,
        "same_cell": source["cell"],
        "matrix_replay": encode_matrix_report(report),
        "opposite_corner_pairs": corners,
        "corner_factorization_after_absorbing_history_sums": "2*d*Re(z00*conj(z11)+z01*conj(z10)) = 4*d*Re(conj(A0)*A1)*Re(B0*conj(B1)), when z_ij=conj(A_i)*B_j",
        "surviving_scope": "distinct arithmetic pairs, unchanged by this history ledger; no complete-fibre sign or native coefficient freedom claimed",
    }


def signed_history_report() -> dict:
    source = collision.signed_history_panel()
    row = source["physical_pair"]
    ell, rho = row["c"], row["d"]
    group = {
        "label": "one_arithmetic_pair",
        "cell": tuple(row["cell"]),
        "coefficients": tuple(source["bilateral_native_coefficient_ratios"]),
    }
    report = matrices(ell, rho, (group,))
    share = Fraction(source["common_bilateral_owner_share"])
    original_norm = share**2 / (row["g"] ** 4 * ell**2 * rho**2 * row["P"] * row["Q"])
    rescaled_norm = share**2 / (row["g"] ** 2 * row["P"] * row["Q"])
    c_product = Fraction((ell + 1) * (rho + 1), (ell - 1) * (rho - 1))
    principal_original = row["g"] ** 2 * ell * rho * c_product * original_norm
    require(
        principal_original == report["weights"]["principal"] * rescaled_norm,
        "principal exterior/source-dual weights do not match",
    )
    require(
        row["g"] ** 2 * ell * rho * (ell - 1) * (rho - 1) * original_norm
        == report["weights"]["additive"] * rescaled_norm,
        "additive exterior/source-dual weights do not match",
    )
    return {
        "horizon": source["horizon"],
        "cutoff": source["frozen_cutoff"],
        "physical_pair": row,
        "native_original_one_history_amplitude": "z_h=c_h*(1/441)*gamma(t)/(g^2*ell*rho*sqrt(P*Q))",
        "native_rescaled_one_history_amplitude": "ztilde_h=c_h*(1/441)*gamma(t)/(g*sqrt(P*Q))",
        "original_common_norm_prefactor": str(original_norm),
        "rescaled_common_norm_prefactor": str(rescaled_norm),
        "matrix_replay": encode_matrix_report(report),
        "physical_correction_prefactors_multiplying_abs_gamma_squared": {
            channel: str(atomic * report["deltas"][0] * rescaled_norm)
            for channel, atomic in report["weights"].items()
        },
        "additive_to_principal_atomic_weight_ratio": str(
            report["weights"]["additive"] / report["weights"]["principal"]
        ),
        "verdict": "the negative hundred-history block is entirely an equal-arithmetic-output correction; its principal-weighted global transfer is inherited-paid, not its separate additive/Kummer transfer",
    }


def source_locks() -> dict:
    expected = {
        "schema": "ffps-signed-history-recombination-sources-v1",
        "sources": [
            {"commit": commit, "path": path, "git_blob": blob}
            for commit, path, blob in SOURCE_ROWS
        ],
    }
    require(MANIFEST.stat().st_size <= MAX_BYTES, "source manifest byte cap exceeded")
    check_fixture(json.loads(MANIFEST.read_text(encoding="utf-8")), expected)
    rows = []
    for commit, path, blob in SOURCE_ROWS:
        ref = f"{commit}:{path}"
        actual_blob = subprocess.check_output(
            ["git", "rev-parse", ref], cwd=ROOT, text=True, timeout=10
        ).strip()
        require(actual_blob == blob, "locked source blob differs")
        size = int(
            subprocess.check_output(
                ["git", "cat-file", "-s", blob], cwd=ROOT, text=True, timeout=10
            ).strip()
        )
        require(size <= MAX_BYTES, "source blob byte cap exceeded")
        raw = subprocess.check_output(["git", "show", ref], cwd=ROOT, timeout=10)
        if (ROOT / path).resolve() == COLLISION_PATH.resolve():
            require(
                digest(raw) == digest(COLLISION_PATH.read_bytes()),
                "loaded collision dependency differs from its frozen source",
            )
        rows.append(
            {"commit": commit, "path": path, "git_blob": blob, "sha256_lf": digest(raw)}
        )
    collision.check_source_locks()
    current = {}
    for path in (NOTE, Path(__file__).resolve(), TEST, MANIFEST):
        require(path.stat().st_size <= MAX_BYTES, "current source byte cap exceeded")
        current[path.relative_to(ROOT).as_posix()] = digest(path.read_bytes())
    return {
        "frozen_sources": rows,
        "current_source_sha256_lf": current,
        "upstream_collision_primitive_blobs_reauthenticated": 11,
    }


def build_report() -> dict:
    return {
        "schema": "ffps-signed-history-recombination-v1",
        "arithmetic_class": "MIXED",
        "arithmetic_components": ["EXACT_RATIONAL", "CERTIFIED_INTEGER_COVERAGE"],
        "rounding_contract": "exact integers and Fraction, no rounding; native Mellin amplitudes remain symbolic",
        "sources": source_locks(),
        "signed_history_control": signed_history_report(),
        "owner_panel": owner_panel_report(collision.ARITHMETIC_CONTROL),
        "held_out_owner_panel": owner_panel_report(collision.ARITHMETIC_HELD_OUT),
        "principal_transfer": {
            "finite_identity": "P_literal - P_grouped = sum_fibre integral p_fibre*Delta_fibre with the original T106140 measure",
            "imported_estimates": "uniform history multiplicity m_Y=Y^o(1) from L102883 and D_PP(Y)=Y^o(1) from corrected L106121/T106140",
            "derived_bound": "abs(C_P(Y)) <= (m_Y-1)*D_PP(Y) = Y^o(1)",
            "uncentered_principal_moment": "exactly invariant: complete source member unchanged",
            "quantifiers": "fixed horizon and all original masks/labels; complete conductor sum and Mellin integral; no extra pointwise bound or maximal/supremum operation",
            "separate_additive_or_Kummer_payment": "NOT_PROVED; d/p has conductor size",
        },
        "firewalls": [
            "literal Wick normalization is recovered by restoring each exact channel correction",
            "native coefficient-family nonfactorization remains open",
            "same residue cell does not mean same arithmetic pair",
            "distinct arithmetic-pair cross terms are unchanged by history aggregation",
            "principal paid error does not prove WCEQ, WCADD, WCCORR, WCKUM, native geometric descent, RH, or GRH",
            "no independent new amplifier or new native coefficient family has been introduced",
        ],
        "finite_coverage": {
            "owner_panels": 2,
            "signed_history_groups": 1,
            "largest_literal_history_count": 100,
            "largest_group_count": 4,
            "complete_native_fibre_enumerated": False,
            "analytic_imports_reproved_by_computation": False,
        },
    }


def check_fixture(actual: object, expected: object) -> None:
    require(
        render(actual) == render(expected), "fixture differs from exact typed replay"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    report = build_report()
    if args.check:
        require(FIXTURE.stat().st_size <= MAX_BYTES, "fixture byte cap exceeded")
        check_fixture(json.loads(FIXTURE.read_text(encoding="utf-8")), report)
        print("PASS_FFPS_SIGNED_HISTORY_RECOMBINATION")
    else:
        print(render(report), end="")


if __name__ == "__main__":
    main()

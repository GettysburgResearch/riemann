#!/usr/bin/env python3
"""Exact coefficient-budget audit for the cyclic FFPS centered identity.

The producer compares the committed cyclic projector identity with the exact
live WCADD/WCKUM decomposition.  It proves what the two open global gates
would control, isolates the one-dimensional common-growth obstruction for the
hard and selected pieces, and gives the exact one-sided closure criterion.

Only rational coefficient algebra is performed.  No residue field, prime
family, conductor family, L-function, curve, or zero set is enumerated.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import time
import unicodedata
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SCRIPT_PATH = Path(__file__).resolve()
OUTPUT_PATH = HERE / "ffps_cyclic_closure_budget.json"
NOTE_PATH = HERE / "FFPS_CYCLIC_CLOSURE_BUDGET.md"
TEST_PATH = ROOT / "tests" / "test_ffps_cyclic_closure_budget.py"

CYCLIC_GATE_COMMIT = "1242951f9529435fd9100d8be6f0d4d4d6f24eae"
CYCLIC_GATE_NOTE_PATH = HERE / "FFPS_CYCLIC_SOURCE_REALIZATION_GATE.md"
CYCLIC_GATE_JSON_PATH = HERE / "ffps_cyclic_source_realization_gate.json"
CYCLIC_GATE_PAYLOAD = "fa2aa7082d4e6e38f79690ec5295f3ffa238e7be17d9c6a7bfd146f3c9eb7a9f"

LIVE_PR_751_HEAD = "98af0db6ec7f77d6333a77a3dac53c4698852f43"

PREREQUISITE_LOCKS: dict[str, dict[str, object]] = {
    "cyclic_gate_note": {
        "path": CYCLIC_GATE_NOTE_PATH,
        "commit": CYCLIC_GATE_COMMIT,
        "git_blob": "9012f96b34a3ffe55b66282ba1e62bc02514b5c6",
        "lf_sha256": "ab880fc0278cdf48daf3bb05782ef1594f3446765616d08aaf95a16bb912c8b4",
        "kind": "text",
        "role": "all-k centered cyclic projector and hard/soft source gate",
    },
    "cyclic_gate_json": {
        "path": CYCLIC_GATE_JSON_PATH,
        "commit": CYCLIC_GATE_COMMIT,
        "git_blob": "57ac81068350a13c9b20580a963469eb34d54ad2",
        "lf_sha256": "8df263e5247f0627b92ee4610b98ba3ddf133bb004dcc8f335c9a6e2637ea039",
        "kind": "json",
        "schema": "riemann.function_field.ffps_cyclic_source_realization_gate.v1",
        "payload_sha256": CYCLIC_GATE_PAYLOAD,
        "role": "canonical cyclic source-realization and Wick fixture",
    },
}

LIVE_CLAIM_LOCKS: dict[str, dict[str, str]] = {
    "L-106120": {
        "path": (
            "claims/lemmas/"
            "L-106120-bilateral-least-prime-phases-form-a-tensor-kummer-family.md"
        ),
        "git_blob": "a8d829dc10611adb7bfb4853902bdff0ab02a065",
        "role": "bilateral even-character and root-character channels",
    },
    "L-106121": {
        "path": (
            "claims/lemmas/"
            "L-106121-bilateral-tensor-moment-has-a-paid-atomic-diagonal.md"
        ),
        "git_blob": "955c3ed0363ca330439eedbae1bf0041a4c96468",
        "role": "positive principal moment and paid principal atomic diagonal",
    },
    "R-106122": {
        "path": (
            "claims/refutations/"
            "R-106122-owner-only-product-collisions-do-not-survive-"
            "varying-core-characters.md"
        ),
        "git_blob": "dc51ae3add697ab4cec868ef8439f864ce77d71a",
        "role": "physical Kummer-coordinate firewall",
    },
    "R-106123": {
        "path": (
            "claims/refutations/"
            "R-106123-local-core-large-sieve-does-not-pay-the-"
            "global-conductor-family.md"
        ),
        "git_blob": "f89cad68d67444280088d8bea7cbfb7c1eacc90d",
        "role": "signed global conductor-recombination firewall",
    },
    "R-106131": {
        "path": (
            "claims/refutations/"
            "R-106131-complete-gauss-family-atomic-ledger-carries-"
            "phase-cardinality.md"
        ),
        "git_blob": "8dde14dd382e0c4fc1bb54d5da21de85ea002f41",
        "role": "complete-family atomic coefficient and principal-only payment",
    },
    "L-106131": {
        "path": (
            "claims/lemmas/"
            "L-106131-wick-normal-ordering-additive-kummer-decomposition.md"
        ),
        "git_blob": "37722c3f36ec7d1681f34d4329a3795e5028f7ae",
        "role": "exact A_circ=P_circ+K_circ identity",
    },
    "T-106140": {
        "path": (
            "claims/theorems/"
            "T-106140-wick-centered-additive-kummer-conjunction-frontier.md"
        ),
        "git_blob": "d5be8e376c88b63de0be19e0d9e8791624e99ae2",
        "role": "open WCADD/WCKUM gates and exact principal inequality",
    },
}

MAX_EXACT_OPERATIONS = 2_000
MAX_SOURCE_FILES = 2
MAX_SOURCE_BYTES_EACH = 32_768
MAX_SOURCE_BYTES_TOTAL = 50_000
MAX_GIT_OBJECTS = 12
MAX_PACKET_FILE_BYTES = 65_536
MAX_CONTROL_PRIME = 101
MAX_WALL_SECONDS = 4.0


@dataclass
class ResourceGuard:
    exact_operations: int = 0
    source_files: int = 0
    source_bytes: int = 0
    git_objects: int = 0
    operation_counts: dict[str, int] = field(default_factory=dict)

    def operation(self, label: str, amount: int = 1) -> None:
        if isinstance(amount, bool) or not isinstance(amount, int) or amount < 0:
            raise ValueError("operation increment must be a nonnegative integer")
        if self.exact_operations + amount > MAX_EXACT_OPERATIONS:
            raise RuntimeError("exact-operation cap exceeded")
        self.exact_operations += amount
        self.operation_counts[label] = self.operation_counts.get(label, 0) + amount

    def source(self, amount: int) -> None:
        if isinstance(amount, bool) or not isinstance(amount, int) or amount < 0:
            raise ValueError("source byte count must be a nonnegative integer")
        if amount > MAX_SOURCE_BYTES_EACH:
            raise RuntimeError("per-source byte cap exceeded")
        if self.source_files + 1 > MAX_SOURCE_FILES:
            raise RuntimeError("source-file cap exceeded")
        if self.source_bytes + amount > MAX_SOURCE_BYTES_TOTAL:
            raise RuntimeError("total source byte cap exceeded")
        self.source_files += 1
        self.source_bytes += amount

    def git_object(self, amount: int = 1) -> None:
        if isinstance(amount, bool) or not isinstance(amount, int) or amount < 0:
            raise ValueError("git-object increment must be a nonnegative integer")
        if self.git_objects + amount > MAX_GIT_OBJECTS:
            raise RuntimeError("git-object cap exceeded")
        self.git_objects += amount


@dataclass(frozen=True)
class Deadline:
    started: float = field(default_factory=time.monotonic)

    def check(self, label: str) -> None:
        if time.monotonic() - self.started > MAX_WALL_SECONDS:
            raise RuntimeError(f"wall-time cap exceeded at {label}")


def _lf_bytes(raw: bytes) -> bytes:
    return raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def _lf_sha256(raw: bytes) -> str:
    return hashlib.sha256(_lf_bytes(raw)).hexdigest()


def _git_blob_sha1(raw: bytes) -> str:
    normalized = _lf_bytes(raw)
    header = f"blob {len(normalized)}\0".encode("ascii")
    return hashlib.sha1(header + normalized).hexdigest()


def _canonical_bytes(value: object) -> bytes:
    def normalize(item: object) -> object:
        if isinstance(item, str):
            return unicodedata.normalize("NFC", item)
        if isinstance(item, tuple | list):
            return [normalize(entry) for entry in item]
        if isinstance(item, dict):
            return {
                unicodedata.normalize("NFC", str(key)): normalize(entry)
                for key, entry in item.items()
            }
        return item

    return json.dumps(
        normalize(value),
        allow_nan=False,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")


def _canonical_sha256(value: object) -> str:
    return hashlib.sha256(_canonical_bytes(value)).hexdigest()


def _fraction(value: int | Fraction) -> list[int]:
    rational = Fraction(value)
    return [rational.numerator, rational.denominator]


def _relative(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def _is_prime(value: int, guard: ResourceGuard | None = None) -> bool:
    if isinstance(value, bool) or not isinstance(value, int) or value < 2:
        return False
    if value == 2:
        return True
    if value % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= value:
        if guard is not None:
            guard.operation("trial_divisions")
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def _validate_panel(
    primes: Sequence[int], order: int, retained_count: int, guard: ResourceGuard
) -> tuple[int, int]:
    panel = tuple(primes)
    if len(panel) != 2 or len(set(panel)) != 2:
        raise ValueError("control requires two distinct primes")
    if isinstance(order, bool) or not isinstance(order, int) or order < 2:
        raise ValueError("character order must be an integer at least two")
    if (
        isinstance(retained_count, bool)
        or not isinstance(retained_count, int)
        or not 0 < retained_count < order
    ):
        raise ValueError("retained count must lie strictly between zero and k")
    for prime in panel:
        if (
            isinstance(prime, bool)
            or not isinstance(prime, int)
            or prime < 3
            or prime > MAX_CONTROL_PRIME
            or prime % 2 == 0
        ):
            raise ValueError("control prime must be an odd prime within the cap")
        if not _is_prime(prime, guard):
            raise ValueError("control prime must be prime")
        if (prime - 1) % (2 * order):
            raise ValueError("common exact order requires 2k to divide p-1")
    return panel


def cyclic_panel_budget(
    primes: Sequence[int],
    order: int,
    retained_count: int,
    guard: ResourceGuard | None = None,
) -> dict[str, object]:
    ledger = guard if guard is not None else ResourceGuard()
    left, right = _validate_panel(primes, order, retained_count, ledger)
    ledger.operation("panel_budget_arithmetic", 30)

    density = Fraction(retained_count, order)
    k_over_t = Fraction(order, retained_count)
    fourier_energy = k_over_t - 1
    c_left = Fraction(left + 1, left - 1)
    c_right = Fraction(right + 1, right - 1)
    principal_weight = c_left * c_right
    nn_weight = Fraction(2 * left, left - 1) * Fraction(2 * right, right - 1)
    embedding_ratio = principal_weight / nn_weight
    phase_atomic = (left - 1) * (right - 1)

    hard_atomic = principal_weight * k_over_t
    selected_atomic = principal_weight * fourier_energy
    kummer_atomic = Fraction(phase_atomic) - principal_weight
    residual_atomic = kummer_atomic - selected_atomic
    if not 0 < embedding_ratio < 1:
        raise ArithmeticError("selected Kummer embedding ratio left (0,1)")
    if residual_atomic <= 0:
        raise ArithmeticError("residual normal-ordered family lost positive weights")
    if hard_atomic + residual_atomic != phase_atomic:
        raise ArithmeticError("additive atomic budget did not split as C plus R")
    if selected_atomic + residual_atomic != kummer_atomic:
        raise ArithmeticError("Kummer atomic budget did not split as S plus R")

    return {
        "primes": [left, right],
        "character_order_k": order,
        "retained_values_t": retained_count,
        "density_t_over_k": _fraction(density),
        "fourier_energy_sum_abs_gamma_squared": _fraction(fourier_energy),
        "principal_weight_c_ell_c_rho": _fraction(principal_weight),
        "double_nonprincipal_weight": _fraction(nn_weight),
        "selected_to_full_channel_weight_ratio": _fraction(embedding_ratio),
        "individual_selected_coefficient_bound": (
            "lambda_r=(c_ell*c_rho/w_NN)*|gamma_r|^2, 0<=lambda_r<c_ell*c_rho/w_NN<1"
        ),
        "phase_atomic_coefficient_D0": phase_atomic,
        "hard_average_atomic_coefficient_B_C": _fraction(hard_atomic),
        "selected_trace_atomic_coefficient_B_S": _fraction(selected_atomic),
        "complete_nonprincipal_atomic_coefficient_B_K": _fraction(kummer_atomic),
        "residual_trace_atomic_coefficient_B_R": _fraction(residual_atomic),
        "atomic_splits": {
            "B_C+B_R=D0": True,
            "B_S+B_R=B_K": True,
        },
        "residual_to_principal_atomic_ratio": _fraction(
            residual_atomic / principal_weight
        ),
    }


def linear_closure_certificate(guard: ResourceGuard) -> dict[str, object]:
    guard.operation("linear_certificate", 36)
    # Coordinates are x=(C,S,R).  The declared measurements are
    # A=C+R and K=S+R.
    additive = (1, 0, 1)
    kummer = (0, 1, 1)
    principal = (1, -1, 0)
    kernel = (1, 1, -1)
    reconstructed = tuple(
        additive[index] - kummer[index] for index in range(len(additive))
    )
    if reconstructed != principal:
        raise ArithmeticError("principal row was not A-K")
    if sum(a * b for a, b in zip(additive, kernel, strict=True)) != 0:
        raise ArithmeticError("kernel vector did not annihilate A")
    if sum(a * b for a, b in zip(kummer, kernel, strict=True)) != 0:
        raise ArithmeticError("kernel vector did not annihilate K")
    if sum(a * b for a, b in zip(principal, kernel, strict=True)) != 0:
        raise ArithmeticError("kernel vector did not preserve P")
    return {
        "coordinates": ["C_hard", "S_selected", "R_residual"],
        "measurement_matrix_rows": {
            "A_additive": list(additive),
            "K_complete_nonprincipal": list(kummer),
        },
        "exact_relations": {
            "P_principal": "C_hard-S_selected",
            "K_complete_nonprincipal": "S_selected+R_residual",
            "A_additive": "C_hard+R_residual",
            "P_equals_A_minus_K": True,
        },
        "common_growth_kernel": list(kernel),
        "kernel_family": ("(C,S,R)->(C+T,S+T,R-T) leaves A, K, and P unchanged"),
        "exact_target_closure_criterion": {
            "target": "L_(u,v,w)=u*C+v*S+w*R",
            "if_and_only_if": "w=u+v",
            "row_span_representation": "L_(u,v,u+v)=u*A+v*K",
            "conditional_budget": ("|L_(u,v,u+v)|<=|u|*epsilon_A+|v|*epsilon_K"),
            "necessity_certificate": (
                "kernel pairing u+v-w must vanish; otherwise the common-growth "
                "shift changes the target while preserving A and K"
            ),
        },
        "sharp_whole_identity_budget": (
            "|P|=|A-K|<=epsilon_A+epsilon_K; coefficient one on each gate "
            "is sharp from scalar sign data"
        ),
        "no_go": (
            "bounds on A and K alone cannot bound C, S, or R separately, "
            "because the measurement matrix has the displayed one-dimensional kernel"
        ),
    }


def ternary_certificate(guard: ResourceGuard) -> dict[str, object]:
    row = cyclic_panel_budget((7, 13), 3, 2, guard)
    ratio = Fraction(*row["selected_to_full_channel_weight_ratio"])
    if ratio != Fraction(4, 13):
        raise ArithmeticError("ternary selected embedding ratio changed")
    individual = ratio * Fraction(1, 4)
    selected_total = 2 * individual
    if individual != Fraction(1, 13) or selected_total != Fraction(2, 13):
        raise ArithmeticError("ternary Fourier coefficients changed")

    escape = Fraction(50)
    residual_budget = Fraction(*row["residual_trace_atomic_coefficient_B_R"])
    if residual_budget != Fraction(209, 3) or escape > residual_budget:
        raise ArithmeticError("ternary coefficient-cone witness left its atomic budget")
    witness = {
        "C_hard": _fraction(escape),
        "S_selected": _fraction(escape),
        "R_residual": _fraction(-escape),
        "A_additive": [0, 1],
        "K_complete_nonprincipal": [0, 1],
        "P_principal": [0, 1],
    }
    return {
        "panel_budget": row,
        "fourier_abs_squares": [[1, 4], [1, 4]],
        "individual_lambda_r": _fraction(individual),
        "selected_lambda_sum": _fraction(selected_total),
        "residual_fraction_on_each_selected_weighted_channel": [12, 13],
        "finite_scalar_no_go_witness_at_D_equals_1": witness,
        "witness_respects_R_lower_atomic_bound": True,
        "meaning": (
            "even zero scalar WCADD/WCKUM data permit large equal hard and "
            "selected traces, offset by the negative residual direction"
        ),
    }


def closure_criterion() -> dict[str, object]:
    return {
        "eligible_principal_localization": (
            "Let E be any eligible cyclic subset. Its uncentered principal "
            "moment M_E=D_E+P_E is nonnegative and at most the complete "
            "principal moment. Therefore the proved inequality "
            "M_total<=D_total+|A|+|K| gives "
            "-D_E<=P_E<=D_total+|A|+|K|-D_E."
        ),
        "whole_identity_bound": (
            "|P_E|<=D_total+|A|+|K|. Thus if the still-open WCADD and "
            "WCKUM estimates are proved, the centered cyclic identity as a "
            "whole is already subpower on every eligible subset."
        ),
        "automatic_one_sided_budgets": {
            "C_hard": "C_E>=-(k/t)*D_E",
            "S_selected": "S_E>=-(k/t-1)*D_E",
        },
        "single_missing_inequality": {
            "name": "CYSEL(k,S)",
            "statement": (
                "The one-sided estimate for one fixed cyclic mask (or a uniformly "
                "subpower k/t) is that the globally recombined selected trace satisfies "
                "S_E(Y)<=Y^o(1)."
            ),
            "why_one_sided_is_enough": (
                "S_E>=-(k/t-1)D_E and D_E=Y^o(1), so CYSEL gives "
                "|S_E|=Y^o(1); then C_E=P_E+S_E is also subpower."
            ),
            "equivalent_choice": (
                "Given the whole-identity bound, the one-sided estimate "
                "C_E(Y)<=Y^o(1) is equivalent up to the paid atomic budgets."
            ),
        },
        "cauchy_firewall": (
            "Generic positivity bounds the residual only by "
            "R_E>=-B_R*D. Relative to the paid principal atomic coefficient, "
            "B_R/(c_ell*c_rho)=D0/(c_ell*c_rho)-k/t, which grows like "
            "ell*rho. This is exactly the dimension-bearing ledger of R-106131, "
            "so triangle/Cauchy does not prove CYSEL."
        ),
        "logical_status": (
            "WCADD106140 and WCKUM106140 are definitions of open RH-bearing "
            "estimates, not currently proved inequalities. The statements here "
            "are exact conditional coefficient budgets."
        ),
    }


def _read_prerequisites(
    guard: ResourceGuard, deadline: Deadline
) -> tuple[dict[str, object], list[dict[str, object]]]:
    parsed: dict[str, object] = {}
    manifest: list[dict[str, object]] = []
    for source_id, lock in PREREQUISITE_LOCKS.items():
        path = lock["path"]
        if not isinstance(path, Path) or not path.is_file():
            raise FileNotFoundError(f"missing prerequisite: {source_id}")
        size = path.stat().st_size
        guard.source(size)
        raw = path.read_bytes()
        if len(raw) != size:
            raise RuntimeError(f"prerequisite size changed during read: {source_id}")
        if _lf_sha256(raw) != lock["lf_sha256"]:
            raise RuntimeError(f"LF hash mismatch for prerequisite: {source_id}")
        if _git_blob_sha1(raw) != lock["git_blob"]:
            raise RuntimeError(f"git blob mismatch for prerequisite: {source_id}")

        guard.git_object()
        completed = subprocess.run(
            ["git", "rev-parse", f"{lock['commit']}:{_relative(path)}"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
            timeout=2.0,
        )
        if completed.returncode != 0:
            raise RuntimeError(
                f"prerequisite git resolution failed: {completed.stderr.strip()}"
            )
        if completed.stdout.strip() != lock["git_blob"]:
            raise RuntimeError(f"committed blob mismatch for prerequisite: {source_id}")

        if lock["kind"] == "json":
            value = json.loads(raw.decode("utf-8"))
            if value.get("schema") != lock["schema"]:
                raise RuntimeError(f"schema drift for prerequisite: {source_id}")
            if value.get("payload_sha256") != lock["payload_sha256"]:
                raise RuntimeError(f"payload drift for prerequisite: {source_id}")
            parsed[source_id] = value
        elif lock["kind"] == "text":
            parsed[source_id] = _lf_bytes(raw).decode("utf-8")
        else:
            raise RuntimeError(f"unknown prerequisite kind: {lock['kind']}")
        manifest.append(
            {
                "id": source_id,
                "path": _relative(path),
                "commit": lock["commit"],
                "git_blob": lock["git_blob"],
                "lf_sha256": lock["lf_sha256"],
                "bytes_read": len(raw),
                "role": lock["role"],
            }
        )
        deadline.check(f"prerequisite {source_id}")
    return parsed, manifest


def _validate_prerequisite_semantics(
    sources: Mapping[str, object],
) -> dict[str, object]:
    packet = sources.get("cyclic_gate_json")
    if not isinstance(packet, Mapping):
        raise TypeError("cyclic gate JSON is malformed")
    exact = packet.get("exact_theorems")
    if not isinstance(exact, Mapping):
        raise TypeError("cyclic gate exact theorems are missing")
    centered = exact.get("cyclic_centered_projector_identity")
    modes = exact.get("live_L_106120_mode_identification")
    if not isinstance(centered, Mapping) or not isinstance(modes, Mapping):
        raise TypeError("centered identity or live mode identification is missing")
    if centered.get("general_formula") != (
        "P_circ=(1/k)*sum_j O_j_circ-sum_(r=1)^(k-1)|c_r|^2*H_r_circ"
    ):
        raise RuntimeError("all-k centered identity changed")
    if not modes.get("all_modes_double_nonprincipal"):
        raise RuntimeError("selected modes left the double-nonprincipal family")
    return {
        "cyclic_gate_commit": CYCLIC_GATE_COMMIT,
        "cyclic_gate_payload": CYCLIC_GATE_PAYLOAD,
        "all_k_centered_identity_consumed": True,
        "live_double_nonprincipal_identification_consumed": True,
    }


def _resolve_live_claims(
    guard: ResourceGuard, deadline: Deadline
) -> list[dict[str, str]]:
    paths = [lock["path"] for lock in LIVE_CLAIM_LOCKS.values()]
    guard.git_object(len(paths))
    completed = subprocess.run(
        ["git", "ls-tree", "-r", LIVE_PR_751_HEAD, "--", *paths],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
        timeout=2.0,
    )
    deadline.check("live claim tree")
    if completed.returncode != 0:
        raise RuntimeError(f"git ls-tree failed: {completed.stderr.strip()}")
    found: dict[str, str] = {}
    for line in completed.stdout.splitlines():
        metadata, path = line.split("\t", 1)
        mode, object_type, blob = metadata.split()
        if mode != "100644" or object_type != "blob":
            raise RuntimeError("live claim did not resolve to a regular blob")
        found[path] = blob
    manifest: list[dict[str, str]] = []
    for claim_id, lock in LIVE_CLAIM_LOCKS.items():
        if found.get(lock["path"]) != lock["git_blob"]:
            raise RuntimeError(f"live blob mismatch for {claim_id}")
        manifest.append(
            {
                "claim_id": claim_id,
                "path": lock["path"],
                "commit": LIVE_PR_751_HEAD,
                "git_blob": lock["git_blob"],
                "role": lock["role"],
            }
        )
    return manifest


def _packet_lf_sha256(path: Path) -> str:
    if not path.is_file():
        raise FileNotFoundError(f"missing packet file: {path}")
    size = path.stat().st_size
    if size > MAX_PACKET_FILE_BYTES:
        raise RuntimeError(f"packet file exceeds byte cap: {path.name}")
    raw = path.read_bytes()
    if len(raw) != size:
        raise RuntimeError(f"packet file changed during read: {path.name}")
    return _lf_sha256(raw)


def build_fixture() -> dict[str, object]:
    deadline = Deadline()
    guard = ResourceGuard()

    linear = linear_closure_certificate(guard)
    quadratic = cyclic_panel_budget((5, 13), 2, 1, guard)
    ternary = ternary_certificate(guard)
    criterion = closure_criterion()
    deadline.check("exact coefficient algebra")
    operations_before_sources = guard.exact_operations

    sources, prerequisite_manifest = _read_prerequisites(guard, deadline)
    source_relationship = _validate_prerequisite_semantics(sources)
    live_manifest = _resolve_live_claims(guard, deadline)
    if guard.exact_operations != operations_before_sources:
        raise RuntimeError("source locks entered the exact-operation ledger")

    fixture: dict[str, object] = {
        "schema": "riemann.function_field.ffps_cyclic_closure_budget.v1",
        "status": "EXACT_CONDITIONAL_CLOSURE_AND_COEFFICIENT_CONE_NO_GO",
        "generated_by": _relative(SCRIPT_PATH),
        "source_contract": {
            "live_pr_751_head": LIVE_PR_751_HEAD,
            "prerequisites": prerequisite_manifest,
            "source_relationship": source_relationship,
            "live_claim_blobs": live_manifest,
        },
        "exact_theorems": {
            "linear_closure_certificate": linear,
            "whole_identity_localization_and_single_gate": criterion,
            "atomic_coefficient_formula": {
                "general": (
                    "B_C=(k/t)c, B_S=(k/t-1)c, "
                    "B_K=D0-c, B_R=D0-(k/t)c, "
                    "c=c_ell*c_rho, D0=(ell-1)(rho-1)"
                ),
                "quadratic_5_13": quadratic,
                "ternary_7_13": ternary,
            },
        },
        "scope": {
            "proved": (
                "exact scalar and atomic coefficient consequences of the committed "
                "cyclic identity and live Wick decomposition"
            ),
            "conditional": (
                "what would follow if the open WCADD106140 and WCKUM106140 "
                "subpower estimates were proved"
            ),
            "missing_analytic_gate": "one-sided selected trace estimate CYSEL(k,S)",
            "residue_fields_enumerated": 0,
            "primes_enumerated": 0,
            "conductors_enumerated": 0,
            "characters_enumerated": 0,
            "l_functions_enumerated": 0,
            "random_samples": 0,
        },
        "firewalls": [
            (
                "WCADD106140 and WCKUM106140 are open estimates. This packet proves "
                "only exact conditional coefficient implications."
            ),
            (
                "The complete principal moment localizes to any eligible cyclic "
                "subset by positivity, but the signed additive and Kummer defects "
                "do not separately localize."
            ),
            (
                "The whole centered cyclic identity is the principal trace and is "
                "already controlled conditionally by WCADD plus WCKUM. The hard "
                "and selected pieces are not."
            ),
            (
                "Triangle and Cauchy cannot remove the common-growth kernel. Their "
                "generic residual lower budget has the unbounded conductor factor "
                "B_R/c=D0/c-k/t."
            ),
            (
                "CYSEL is one-sided because the selected trace already has the exact "
                "lower bound S>=-(k/t-1)D_E."
            ),
            "No principal member is individualized; RH and GRH remain unproved.",
            "No external novelty claim is made.",
        ],
        "packet_manifest": {
            "producer": {
                "path": _relative(SCRIPT_PATH),
                "lf_sha256": _packet_lf_sha256(SCRIPT_PATH),
            },
            "note": {
                "path": _relative(NOTE_PATH),
                "lf_sha256": _packet_lf_sha256(NOTE_PATH),
            },
            "test": {
                "path": _relative(TEST_PATH),
                "lf_sha256": _packet_lf_sha256(TEST_PATH),
            },
        },
        "resource_contract": {
            "maximum_exact_operations": MAX_EXACT_OPERATIONS,
            "actual_exact_operations": guard.exact_operations,
            "operations_before_sources": operations_before_sources,
            "operation_counts": dict(sorted(guard.operation_counts.items())),
            "maximum_source_files": MAX_SOURCE_FILES,
            "actual_source_files": guard.source_files,
            "maximum_source_bytes_each": MAX_SOURCE_BYTES_EACH,
            "maximum_source_bytes_total": MAX_SOURCE_BYTES_TOTAL,
            "actual_source_bytes": guard.source_bytes,
            "maximum_git_objects": MAX_GIT_OBJECTS,
            "actual_git_objects": guard.git_objects,
            "maximum_control_prime": MAX_CONTROL_PRIME,
            "maximum_packet_file_bytes": MAX_PACKET_FILE_BYTES,
            "maximum_wall_seconds": MAX_WALL_SECONDS,
            "arithmetic": "exact integers and Fraction only; no floating point",
            "heavy_computation": False,
        },
    }
    deadline.check("fixture assembly")
    fixture["payload_sha256"] = _canonical_sha256(fixture)
    return fixture


def _render(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check", action="store_true", help="refuse unless the fixture is current"
    )
    arguments = parser.parse_args(argv)
    rendered = _render(build_fixture()).encode("utf-8")
    if len(rendered) > MAX_PACKET_FILE_BYTES:
        raise RuntimeError("rendered fixture exceeds packet-file byte cap")
    if arguments.check:
        if not OUTPUT_PATH.is_file():
            raise FileNotFoundError(f"missing fixture: {OUTPUT_PATH}")
        size = OUTPUT_PATH.stat().st_size
        if size > MAX_PACKET_FILE_BYTES:
            raise RuntimeError("existing fixture exceeds packet-file byte cap")
        current = OUTPUT_PATH.read_bytes()
        if len(current) != size:
            raise RuntimeError("existing fixture changed during read")
        if current != rendered:
            raise RuntimeError(f"fixture is stale: {OUTPUT_PATH}")
        print("PASS_FFPS_CYCLIC_CLOSURE_BUDGET")
        return 0
    OUTPUT_PATH.write_bytes(rendered)
    print(f"wrote {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

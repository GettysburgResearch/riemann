"""Exact Hasse-lattice counts on the two rigid tensor/Sym^r torus graphs.

The all-r formulas are proved by Dickson-polynomial valuations and a four-
trace overlap calculation.  The bounded replays are deliberately tiny exact
regressions; they do not enumerate finite fields, curves, models, or full
trace cubes.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from math import isqrt
from pathlib import Path
from typing import Sequence


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "elliptic_tensor_symmetric_power_hasse_graph_counts.json"
NOTE_PATH = HERE / "ELLIPTIC_TENSOR_SYMMETRIC_POWER_HASSE_GRAPH_COUNTS.md"
TEST_PATH = (
    ROOT / "tests" / "test_elliptic_tensor_symmetric_power_hasse_graph_counts.py"
)

SCHEMA = (
    "riemann.function_field."
    "elliptic_tensor_symmetric_power_hasse_graph_counts.v1"
)

PREDECESSORS = (
    {
        "name": "r1_so4_sym3_intersection",
        "fixture": "elliptic_so4_sym3_spectral_intersection.json",
        "producer": "elliptic_so4_sym3_spectral_intersection.py",
        "schema": "riemann.function_field.elliptic_so4_sym3_spectral_intersection.v1",
        "payload": "c2657dceb8784e5581092cfd07500f7f39680ce4685516f0ce03e02c195b230c",
        "fixture_lf": "1bb219a196d2fdb8302f6cf785daeda92312c846bbe294f3ac4fed7c5d3691c6",
        "producer_lf": "c33d8b1fed8ed1295abf635821f6b6c6dbf46181b438c2b65e5142e0fea1ddcd",
    },
    {
        "name": "r2_tensor_sym2_sym5_intersection",
        "fixture": "elliptic_tensor_sym2_sym5_spectral_intersection.json",
        "producer": "elliptic_tensor_sym2_sym5_spectral_intersection.py",
        "schema": (
            "riemann.function_field."
            "elliptic_tensor_sym2_sym5_spectral_intersection.v1"
        ),
        "payload": "e2c9c7ac3d1329b7b911a5214d36935d2694436cbe6d9cce551b94f8486b01ba",
        "fixture_lf": "e583220e7df56765ef198d71a4a94887e8246992ba8fd9d127e8c1ce4e09cc32",
        "producer_lf": "d414807d8c2bb41ee075c5526e22b243204f3e587e5988a55f91245a99f6d9e7",
    },
    {
        "name": "r3_tensor_sym3_sym7_intersection",
        "fixture": "elliptic_tensor_sym3_sym7_spectral_intersection.json",
        "producer": "elliptic_tensor_sym3_sym7_spectral_intersection.py",
        "schema": (
            "riemann.function_field."
            "elliptic_tensor_sym3_sym7_spectral_intersection.v1"
        ),
        "payload": "a1ec101912ba9712c015c2cbbd81022097ad113f2d6d0d9178ad7be4b43cfdbf",
        "fixture_lf": "56837ead694fc113a5c3b82eee87c6a39b5af1a6a07564c4d78250f86ae9cb3e",
        "producer_lf": "9d78faf0ca23c86060050d8420d6127e959062c0cf3829f97cc5986e0db47956",
    },
    {
        "name": "all_r_monomial_subtorus_rigidity",
        "fixture": "elliptic_tensor_symmetric_power_subtorus_rigidity.json",
        "producer": "elliptic_tensor_symmetric_power_subtorus_rigidity.py",
        "schema": (
            "riemann.function_field."
            "elliptic_tensor_symmetric_power_subtorus_rigidity.v1"
        ),
        "payload": "f05eea9c197c95af54e874bea437b7547acf42b5ccad50b29f7031b54d5c695d",
        "fixture_lf": "59518d2a83fc11922b7ccb357b2fb11470725fc51c16803eccc9de5c6bad470d",
        "producer_lf": "a9410d146fb9152c0ea835b48564343a8867c30d12e46798990a0c991463643b",
    },
)

FROZEN_SQUARE_PRIMES = (3, 5)
FROZEN_SQUARE_MAX_K = 2
FROZEN_SQUARE_MAX_R = 12
FROZEN_NONSQUARE_PRIMES = (3, 5)
FROZEN_NONSQUARE_EXPONENTS = (1, 3)
FROZEN_NONSQUARE_MAX_R = 12
MAX_PRIME = 101
MAX_K = 6
MAX_EXPONENT = 11
MAX_R = 64
MAX_ENUMERATED_C_CANDIDATES = 4_096
ACCOUNTED_WORK_UNIT_CAP_EXCLUSIVE = 20_000

TraceTriple = tuple[int, int, int]


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def _lf_sha256(path: Path) -> str:
    normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(normalized).hexdigest()


def _relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def _require_plain_int(name: str, value: object) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be a plain integer")
    return value


def _is_prime(value: int) -> bool:
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return value == divisor
        divisor += 1
    return True


def _require_prime(p: object, *, odd: bool = False) -> int:
    value = _require_plain_int("p", p)
    if value > MAX_PRIME:
        raise ValueError(f"p exceeds the exact cap {MAX_PRIME}")
    if not _is_prime(value):
        raise ValueError("p must be prime")
    if odd and value == 2:
        raise ValueError("the nonsquare theorem requires an odd prime")
    return value


def _require_k(k: object) -> int:
    value = _require_plain_int("k", k)
    if value < 1 or value > MAX_K:
        raise ValueError(f"k must lie in 1..{MAX_K}")
    return value


def _require_exponent(exponent: object, *, odd: bool = False) -> int:
    value = _require_plain_int("exponent", exponent)
    if value < 1 or value > MAX_EXPONENT:
        raise ValueError(f"exponent must lie in 1..{MAX_EXPONENT}")
    if odd and value % 2 == 0:
        raise ValueError("exponent must be odd")
    return value


def _require_r(r: object) -> int:
    value = _require_plain_int("r", r)
    if value < 1 or value > MAX_R:
        raise ValueError(f"r must lie in 1..{MAX_R}")
    return value


def _ceil_div(numerator: int, denominator: int) -> int:
    if denominator <= 0:
        raise ValueError("denominator must be positive")
    return -(-numerator // denominator)


def _require_bounded_C_interval(candidate_count: object) -> None:
    count = _require_plain_int("candidate_count", candidate_count)
    if count < 1:
        raise ValueError("candidate_count must be positive")
    if count > MAX_ENUMERATED_C_CANDIDATES:
        raise ValueError(
            "one-dimensional C enumeration exceeds the exact cap "
            f"{MAX_ENUMERATED_C_CANDIDATES}; use the closed-count function"
        )


class ResourceGuard:
    """Logical-work ledger with a deliberately low exclusive cap."""

    def __init__(self, cap: object = ACCOUNTED_WORK_UNIT_CAP_EXCLUSIVE) -> None:
        cap_value = _require_plain_int("cap", cap)
        if cap_value < 1:
            raise ValueError("cap must be positive")
        self.cap = cap_value
        self.ledger: Counter[str] = Counter()

    @property
    def total(self) -> int:
        return sum(self.ledger.values())

    def charge(self, name: object, units: object = 1) -> None:
        if not isinstance(name, str) or not name:
            raise TypeError("resource name must be a nonempty string")
        count = _require_plain_int("units", units)
        if count < 0:
            raise ValueError("resource charge must be nonnegative")
        if self.total + count >= self.cap:
            raise RuntimeError(
                f"accounted work would meet or exceed exclusive cap {self.cap}"
            )
        self.ledger[name] += count


def dickson_homogeneous_value(degree: object, trace: object, q: object) -> int:
    """Return L_n(C,q), where L_0=2, L_1=C, L_n=C L_(n-1)-q L_(n-2)."""

    n = _require_plain_int("degree", degree)
    C = _require_plain_int("trace", trace)
    q_value = _require_plain_int("q", q)
    if n < 0 or n > MAX_R + 1:
        raise ValueError(f"degree must lie in 0..{MAX_R + 1}")
    if q_value < 1:
        raise ValueError("q must be positive")
    if n == 0:
        return 2
    previous_previous, previous = 2, C
    for _ in range(1, n):
        previous_previous, previous = (
            previous,
            C * previous - q_value * previous_previous,
        )
    return previous


def first_divisor_exponent_square(k: object, r: object) -> int:
    k_value = _require_k(k)
    r_value = _require_r(r)
    return _ceil_div(r_value * k_value, r_value + 1)


def second_divisor_exponent_square(k: object) -> int:
    k_value = _require_k(k)
    return _ceil_div(k_value, 2)


def first_divisor_exponent_nonsquare(exponent: object, r: object) -> int:
    e = _require_exponent(exponent, odd=True)
    r_value = _require_r(r)
    if r_value % 2 != 0:
        raise ValueError("the nonsquare first-graph divisor is used only for even r")
    return _ceil_div(e * r_value, 2 * (r_value + 1))


def first_graph_triples_square(p: object, k: object, r: object) -> tuple[TraceTriple, ...]:
    """Enumerate only the one-dimensional first graph in the Hasse interval."""

    p_value = _require_prime(p)
    k_value = _require_k(k)
    r_value = _require_r(r)
    s = p_value**k_value
    q = s * s
    _require_bounded_C_interval(4 * s + 1)
    denominator = s**r_value
    triples: set[TraceTriple] = set()
    for C in range(-2 * s, 2 * s + 1):
        numerator = dickson_homogeneous_value(r_value + 1, C, q)
        if numerator % denominator != 0:
            continue
        base_A = numerator // denominator
        if abs(base_A) > 2 * s:
            raise ArithmeticError("Dickson compact Hasse bound failed")
        for epsilon in (-1, 1):
            triples.add((epsilon**r_value * base_A, epsilon * C, C))
    return tuple(sorted(triples))


def second_graph_triples_square(p: object, k: object, r: object) -> tuple[TraceTriple, ...]:
    """Enumerate only the one-dimensional second graph in the Hasse interval."""

    p_value = _require_prime(p)
    k_value = _require_k(k)
    r_value = _require_r(r)
    s = p_value**k_value
    q = s * s
    _require_bounded_C_interval(4 * s + 1)
    triples: set[TraceTriple] = set()
    for C in range(-2 * s, 2 * s + 1):
        numerator = C * C - 2 * q
        if numerator % s != 0:
            continue
        base_B = numerator // s
        if abs(base_B) > 2 * s:
            raise ArithmeticError("quadratic compact Hasse bound failed")
        for eta in (-1, 1):
            triples.add((eta**r_value * C, eta * base_B, C))
    return tuple(sorted(triples))


def square_closed_counts(p: object, k: object, r: object) -> dict[str, int]:
    """Closed counts for both signed graphs, their overlap, and their union."""

    p_value = _require_prime(p)
    k_value = _require_k(k)
    r_value = _require_r(r)
    first_scale = p_value ** (k_value // (r_value + 1))
    second_scale = p_value ** (k_value // 2)
    first = 8 * first_scale + (2 if r_value % 2 else 1)
    second = 8 * second_scale + 2
    overlap = 4 + (4 if (r_value + 1) % 3 != 0 else 0)
    union = first + second - overlap
    return {
        "first_graph": first,
        "second_graph": second,
        "overlap": overlap,
        "union": union,
    }


def square_graph_union(p: object, k: object, r: object) -> tuple[TraceTriple, ...]:
    first = set(first_graph_triples_square(p, k, r))
    second = set(second_graph_triples_square(p, k, r))
    return tuple(sorted(first | second))


def nonsquare_first_graph_triples(
    p: object, exponent: object, r: object
) -> tuple[TraceTriple, ...]:
    """Exact surviving first graph for q=p^e, e odd; odd r has no points."""

    p_value = _require_prime(p, odd=True)
    e = _require_exponent(exponent, odd=True)
    r_value = _require_r(r)
    q = p_value**e
    H = isqrt(4 * q)
    _require_bounded_C_interval(2 * H + 1)
    if r_value % 2:
        return ()
    denominator = q ** (r_value // 2)
    triples: set[TraceTriple] = set()
    for C in range(-H, H + 1):
        numerator = dickson_homogeneous_value(r_value + 1, C, q)
        if numerator % denominator != 0:
            continue
        A = numerator // denominator
        if abs(A) > H:
            raise ArithmeticError("nonsquare Dickson compact Hasse bound failed")
        for epsilon in (-1, 1):
            triples.add((A, epsilon * C, C))
    return tuple(sorted(triples))


def nonsquare_closed_count(p: object, exponent: object, r: object) -> int:
    """Union count on the two graphs at an odd nonsquare prime power."""

    p_value = _require_prime(p, odd=True)
    e = _require_exponent(exponent, odd=True)
    r_value = _require_r(r)
    if r_value % 2:
        return 0
    H = isqrt(4 * p_value**e)
    divisor = p_value ** first_divisor_exponent_nonsquare(e, r_value)
    return 4 * (H // divisor) + 1


def _load_locked_predecessors() -> dict[str, dict[str, object]]:
    loaded: dict[str, dict[str, object]] = {}
    for lock in PREDECESSORS:
        fixture_path = HERE / str(lock["fixture"])
        producer_path = HERE / str(lock["producer"])
        if _lf_sha256(fixture_path) != lock["fixture_lf"]:
            raise RuntimeError(f"{lock['name']} fixture LF hash mismatch")
        if _lf_sha256(producer_path) != lock["producer_lf"]:
            raise RuntimeError(f"{lock['name']} producer LF hash mismatch")
        fixture = json.loads(fixture_path.read_text(encoding="utf-8"))
        if fixture.get("schema") != lock["schema"]:
            raise RuntimeError(f"{lock['name']} schema mismatch")
        if fixture.get("payload_sha256") != lock["payload"]:
            raise RuntimeError(f"{lock['name']} payload mismatch")
        unhashed = dict(fixture)
        claimed = unhashed.pop("payload_sha256", None)
        if claimed != _canonical_sha256(unhashed):
            raise RuntimeError(f"{lock['name']} canonical payload is inconsistent")
        loaded[str(lock["name"])] = fixture
    return loaded


def _predecessor_recoveries(
    predecessors: dict[str, dict[str, object]]
) -> list[dict[str, object]]:
    rigidity = predecessors["all_r_monomial_subtorus_rigidity"]
    graphs = rigidity["dickson_chebyshev_graph_equations"]
    if graphs.get("first_graph") != (
        "x=D_(r+1)(z), y=z, corresponding to u=w^(r+1), v=w"
    ):
        raise RuntimeError("locked rigidity first graph changed")
    if graphs.get("second_graph") != (
        "x=z, y=D_2(z)=z^2-2, corresponding to u=w, v=w^2"
    ):
        raise RuntimeError("locked rigidity second graph changed")
    if "delta_u+r*delta_v=0 mod 2" not in str(graphs.get("central_sign_note")):
        raise RuntimeError("locked rigidity central-sign convention changed")

    expected = {
        1: "16*p^floor(k/2)-4",
        2: "8*p^floor(k/3)+8*p^floor(k/2)-1",
        3: "8*p^floor(k/4)+8*p^floor(k/2)-4",
    }
    r1_text = predecessors["r1_so4_sym3_intersection"][
        "integral_odd_prime_power_theorem"
    ]["all_q_lattice_counts"]
    if "16M-4 points" not in r1_text:
        raise RuntimeError("locked r=1 count changed")
    r2_text = predecessors["r2_tensor_sym2_sym5_intersection"][
        "odd_prime_power_integral_theorem"
    ]["square_q_union_count"]
    if r2_text != "8p^floor(k/3)+8p^floor(k/2)-1 for q=p^(2k)":
        raise RuntimeError("locked r=2 count changed")
    r3_text = predecessors["r3_tensor_sym3_sym7_intersection"][
        "odd_prime_power_arithmetic"
    ]["union_count"]
    if r3_text != "8*p^floor(k/4)+8*p^floor(k/2)-4":
        raise RuntimeError("locked r=3 count changed")

    rows: list[dict[str, object]] = []
    for r, formula in expected.items():
        rows.append(
            {
                "r": r,
                "specialized_all_r_formula": formula,
                "locked_predecessor_formula_agrees": True,
                "square_count_at_p_3_k_2": square_closed_counts(3, 2, r)["union"],
            }
        )
    return rows


def _square_replay(guard: ResourceGuard) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for p in FROZEN_SQUARE_PRIMES:
        for k in range(1, FROZEN_SQUARE_MAX_K + 1):
            s = p**k
            for r in range(1, FROZEN_SQUARE_MAX_R + 1):
                guard.charge("square_C_candidates", 4 * s + 1)
                first = set(first_graph_triples_square(p, k, r))
                second = set(second_graph_triples_square(p, k, r))
                observed = {
                    "first_graph": len(first),
                    "second_graph": len(second),
                    "overlap": len(first & second),
                    "union": len(first | second),
                }
                predicted = square_closed_counts(p, k, r)
                if observed != predicted:
                    raise ArithmeticError("square all-r graph count replay failed")
                rows.append(
                    {
                        "p": p,
                        "k": k,
                        "q": p ** (2 * k),
                        "r": r,
                        "first_divisor_exponent": first_divisor_exponent_square(k, r),
                        "second_divisor_exponent": second_divisor_exponent_square(k),
                        "internal_overlap_present": (r + 1) % 3 != 0,
                        **observed,
                    }
                )
    return rows


def _nonsquare_replay(guard: ResourceGuard) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for p in FROZEN_NONSQUARE_PRIMES:
        for exponent in FROZEN_NONSQUARE_EXPONENTS:
            q = p**exponent
            H = isqrt(4 * q)
            _require_bounded_C_interval(2 * H + 1)
            for r in range(1, FROZEN_NONSQUARE_MAX_R + 1):
                guard.charge("nonsquare_C_candidates", 2 * H + 1)
                for C in range(-H, H + 1):
                    if C * C == 2 * q:
                        raise ArithmeticError("nonsquare second-graph zero found")
                if r % 2:
                    for C in range(-H, H + 1):
                        if dickson_homogeneous_value(r + 1, C, q) == 0:
                            raise ArithmeticError("odd-r nonsquare first-graph zero found")
                observed = len(nonsquare_first_graph_triples(p, exponent, r))
                predicted = nonsquare_closed_count(p, exponent, r)
                if observed != predicted:
                    raise ArithmeticError("nonsquare parity replay failed")
                rows.append(
                    {
                        "p": p,
                        "exponent": exponent,
                        "q": q,
                        "H=floor(2sqrt(q))": H,
                        "r": r,
                        "r_parity": "odd" if r % 2 else "even",
                        "first_divisor_exponent": (
                            None
                            if r % 2
                            else first_divisor_exponent_nonsquare(exponent, r)
                        ),
                        "union_count": observed,
                    }
                )
    return rows


def _owned_file_locks() -> dict[str, dict[str, str]]:
    return {
        "note": {
            "path": _relative(NOTE_PATH),
            "sha256_lf_normalized": _lf_sha256(NOTE_PATH),
        },
        "producer": {
            "path": _relative(Path(__file__).resolve()),
            "sha256_lf_normalized": _lf_sha256(Path(__file__).resolve()),
        },
        "test": {
            "path": _relative(TEST_PATH),
            "sha256_lf_normalized": _lf_sha256(TEST_PATH),
        },
    }


def build_fixture() -> dict[str, object]:
    """Build the canonical source-locked all-r Hasse graph-count packet."""

    predecessors = _load_locked_predecessors()
    guard = ResourceGuard()
    guard.charge("locked_predecessor_files_verified", 2 * len(PREDECESSORS))
    recoveries = _predecessor_recoveries(predecessors)
    guard.charge("locked_predecessor_formula_recoveries", len(recoveries))
    square_rows = _square_replay(guard)
    nonsquare_rows = _nonsquare_replay(guard)
    guard.charge("closed_overlap_period_rows", FROZEN_SQUARE_MAX_R)

    fixture: dict[str, object] = {
        "schema": SCHEMA,
        "packet_id": (
            "FUNCTION_FIELD.ELLIPTIC.TENSOR_SYMMETRIC_POWER."
            "HASSE_GRAPH_COUNTS.V1"
        ),
        "status": "EXACT_ALL_R_HASSE_GRAPH_COUNTS_WITH_TINY_INTEGER_REPLAY",
        "rigor_level": {
            "square_prime_power_graph_count": "PROVED_FOR_EVERY_PRIME_p_AND_r_k_AT_LEAST_1",
            "nonsquare_prime_power_graph_count": "PROVED_FOR_EVERY_ODD_PRIME_p_ODD_e_AND_r_AT_LEAST_1",
            "valuation_lemma": "PROVED_WITH_NO_COEFFICIENT_PRIME_EXCEPTIONS",
            "bounded_replay": "EXACT_STDLIB_REGRESSION_NOT_USED_AS_THE_PROOF",
            "full_spectral_intersection": "NOT_CLASSIFIED_BEYOND_LOCKED_r_1_r_2_r_3_RESULTS",
            "arithmetic_realization_or_novelty": "NOT_INFERRED",
        },
        "definitions": {
            "dickson_trace": "D_n(w+w^-1)=w^n+w^-n, with D_0=2, D_1=z, D_n=zD_(n-1)-D_(n-2)",
            "homogeneous_dickson": "L_n(C,q)=q^(n/2)D_n(C/sqrt(q)), with L_0=2, L_1=C, L_n=C*L_(n-1)-q*L_(n-2)",
            "first_signed_graph": "(A,B,C)=(epsilon^r*L_(r+1)(C,q)/s^r, epsilon*C, C)",
            "second_signed_graph": "(A,B,C)=(eta^r*C, eta*(C^2-2q)/s, C)",
            "central_sign_condition": "delta_u+r*delta_v=0 mod 2; epsilon=(-1)^delta_v and the Std sign is epsilon^r",
            "square_parameter": "q=s^2=p^(2k), s=p^k",
        },
        "no_coefficient_exception_valuation_lemma": {
            "statement": "for q=p^(2k), s^r divides L_(r+1)(C,q) iff v_p(C)>=ceil(rk/(r+1))",
            "first_threshold": "ceil(rk/(r+1))=k-floor(k/(r+1))",
            "proof_below_k": "if c=v_p(C)<k, the j=0 monomial C^(r+1) is the unique term of lowest p-adic valuation, so v_p(L_(r+1))=(r+1)c",
            "proof_at_or_above_k": "if c>=k, every monomial q^j*C^(r+1-2j) has valuation at least (r+1)k>=rk",
            "coefficient_prime_boundary": "integer coefficients can only increase nonleading valuations; the unique monic leading term prevents cancellation, so there is no exceptional prime, including p=2 in the square theorem",
            "second_graph_statement": "s divides C^2-2s^2 iff s divides C^2 iff v_p(C)>=ceil(k/2)",
        },
        "square_prime_power_theorem": {
            "scope": "q=p^(2k), every prime p, and all r,k>=1; A,B,C are integral Hasse traces",
            "first_graph_divisor": "p^ceil(rk/(r+1)) divides C",
            "first_graph_parameter_count": "4*p^floor(k/(r+1))+1 values of C",
            "first_graph_count_even_r": "8*p^floor(k/(r+1))+1; epsilon changes only B and duplicates at C=0",
            "first_graph_count_odd_r": "8*p^floor(k/(r+1))+2; at C=0 the two A values are +/-2s and remain distinct",
            "second_graph_divisor": "p^ceil(k/2) divides C",
            "second_graph_count": "8*p^floor(k/2)+2 for every r; C^2=2s^2 has no integral solution, so no sign duplicate occurs",
            "union_count": "8*p^floor(k/(r+1))+8*p^floor(k/2)-1+1_(r odd)-4*1_(3 does not divide r+1)",
            "automatic_Hasse_bounds": "D_(r+1) and D_2 map [-2,2] to [-2,2] because D_n(2cos(theta))=2cos(n theta)",
        },
        "central_sign_and_duplicate_audit": {
            "allowed_signs": "write epsilon=(-1)^delta_v; delta_u+r*delta_v=0 gives the source trace signs (epsilon^r,epsilon)",
            "even_r": "the Std trace is fixed while the Sym^r input trace has two signs; only C=0 merges them on graph one",
            "odd_r": "both source traces change sign together; graph-one C=0 has nonzero endpoint A and graph-two C=0 has nonzero endpoint B",
            "graph_two_no_zero": "C^2-2s^2 is never zero for integral C,s>0",
        },
        "overlap_theorem": {
            "normalized_equations": "epsilon^r*D_(r+1)(z)=eta^r*z and epsilon*z=eta*D_2(z)",
            "reduction": "rho=epsilon/eta gives D_2(z)=rho*z and D_(r+1)(z)=rho^r*z",
            "only_candidates": "(rho,z)=(1,2),(1,-1),(-1,1),(-1,-2)",
            "endpoints": "z=+/-2 always contribute two triples each",
            "internal_period": "z=+/-1 both contribute two triples each iff 3 does not divide r+1; this is the D_n(+/-1) period modulo 6",
            "overlap_count": "O_r=4+4*1_(3 does not divide r+1)",
            "zero_exclusion": "z=0 is excluded already by D_2(z)=rho*z",
            "period_rows": [
                {
                    "r": r,
                    "r_plus_1_mod_6": (r + 1) % 6,
                    "internal_z_plus_minus_1_present": (r + 1) % 3 != 0,
                    "overlap_count": 4 + (4 if (r + 1) % 3 != 0 else 0),
                }
                for r in range(1, FROZEN_SQUARE_MAX_R + 1)
            ],
        },
        "nonsquare_odd_prime_power_theorem": {
            "scope": "q=p^e with p odd and e odd; integral A,B,C in the Hasse interval",
            "even_r_count": "4*floor(floor(2sqrt(q))/p^ceil(er/(2(r+1))))+1",
            "even_r_reason": "only graph one is rational; q^(r/2) divides L_(r+1) iff v_p(C)>=ceil(er/(2(r+1)))",
            "odd_r_count": 0,
            "odd_r_first_graph_obstruction": "A rational would force L_(r+1)(C,q)=0; since v_p(C) cannot equal e/2, the first or last Dickson monomial is uniquely minimal, and the last coefficient 2 is a p-unit for odd p",
            "second_graph_obstruction": "integer B would force C^2=2q, impossible because v_p(C^2) is even and e is odd",
            "p_equals_2_boundary": "excluded: C^2=2q is possible when p=2 and e is odd, and D_n(+/-sqrt(2)) can vanish for n congruent to 2 modulo 4",
        },
        "locked_predecessor_recoveries": {
            "purpose": "specialize the all-r count to the three independently classified low r intersections and lock the all-r graph rigidity source",
            "rows": recoveries,
        },
        "predecessor_source_locks": [
            {
                "name": lock["name"],
                "fixture_path": _relative(HERE / str(lock["fixture"])),
                "fixture_schema": lock["schema"],
                "fixture_payload_sha256": lock["payload"],
                "fixture_sha256_lf_normalized": lock["fixture_lf"],
                "producer_path": _relative(HERE / str(lock["producer"])),
                "producer_sha256_lf_normalized": lock["producer_lf"],
            }
            for lock in PREDECESSORS
        ],
        "bounded_exact_replay": {
            "square_scope": "p in {3,5}, 1<=k<=2, 1<=r<=12; enumerate C only on each one-dimensional graph",
            "square_rows": square_rows,
            "nonsquare_scope": "p in {3,5}, e in {1,3}, 1<=r<=12; enumerate C only",
            "nonsquare_rows": nonsquare_rows,
            "finite_replay_is_not_the_proof": True,
        },
        "source_and_owned_file_locks": {
            "owned_file_locks": _owned_file_locks(),
            "authentication": "four predecessor fixtures are schema-, payload-, canonical-payload-, and LF-file-locked; their producers and all three owned source files are LF-file-locked",
        },
        "resource_contract": {
            "exclusive_accounted_work_unit_cap": guard.cap,
            "accounted_work_unit_ledger": {
                **dict(sorted(guard.ledger.items())),
                "total_accounted_work_units": guard.total,
            },
            "logical_unit_definition": "one candidate C, one locked file, one locked recovery, or one closed period row; not CPU instructions",
            "largest_square_parameter_s": max(
                p**FROZEN_SQUARE_MAX_K for p in FROZEN_SQUARE_PRIMES
            ),
            "maximum_public_enumerated_C_candidates": MAX_ENUMERATED_C_CANDIDATES,
            "enumerator_refusal": "graph-point enumerators fail closed above the C-candidate cap; closed-count functions remain constant-work",
            "field_curve_model_or_full_trace_cube_enumerations": 0,
            "random_samples": 0,
            "floating_point_results": 0,
            "runtime_symbolic_packages": 0,
            "arithmetic": "standard-library exact integers, sets, isqrt, hashes, and JSON only",
        },
        "scope_firewall": {
            "graph_union_only": "for general r the packet counts the two rigid sufficient torus graphs, not every spectral-intersection component or cyclotomic residual",
            "low_r_completeness_only": "the locked r=1, r=2, and r=3 packets separately prove the completeness statements recorded there",
            "no_field_curve_or_model_enumeration": "the bounded replay enumerates a one-dimensional integer C interval only",
            "no_curve_realization": "an integral Hasse trace triple is not asserted to come from three curves or linked isogeny classes",
            "no_representation_homomorphism": "a torus spectral identity is not an ambient representation isomorphism",
            "no_local_to_global_upgrade": "no compatible family, motive, Euler product, automorphy, modularity, or zero theorem is inferred",
            "no_novelty_priority_claim": "the exact elementary count is recorded without a literature-priority claim",
            "no_RH_GRH_claim": "the lattice theorem has no asserted consequence for RH or GRH",
        },
        "next_targets": [
            "classify non-graph and cyclotomic components for r>=4 before promoting graph counts to full intersection counts",
            "classify the p=2 nonsquare exceptional graph points separately",
            "determine whether either graph occurs coherently across primes in a genuine compatible family",
        ],
    }
    if guard.total >= guard.cap:
        raise RuntimeError("accounted resource cap was not respected")
    fixture["payload_sha256"] = _canonical_sha256(fixture)
    return fixture


def _serialized_fixture() -> str:
    return json.dumps(build_fixture(), indent=2, sort_keys=True) + "\n"


def _write(path: Path) -> None:
    path.write_text(_serialized_fixture(), encoding="utf-8")
    print(f"wrote {path}")


def _check(path: Path) -> None:
    if not path.exists() or path.read_text(encoding="utf-8") != _serialized_fixture():
        raise SystemExit(f"fixture is stale: {path}")
    print(f"fixture is current: {path}")


def main(argv: Sequence[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group()
    action.add_argument("--write", nargs="?", const=OUTPUT_PATH, type=Path)
    action.add_argument("--check", nargs="?", const=OUTPUT_PATH, type=Path)
    arguments = parser.parse_args(argv)
    if arguments.write is not None:
        _write(arguments.write)
    elif arguments.check is not None:
        _check(arguments.check)
    else:
        print(json.dumps(build_fixture(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

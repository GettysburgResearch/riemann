#!/usr/bin/env python3
"""Proof-producing search over a finite canonical Robin domain.

The searcher emits only a compact DFS terminal stream.  A separate verifier
reconstructs the complete tree, every exact rational ceiling, every dyadic
transcendental enclosure, and every classification without importing this
traversal implementation.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
from typing import Iterable, Sequence
from functools import lru_cache

from certmath import RobinParameters, robin_rhs

FINITE_EXCEPTION = 5040


def prime_stream() -> Iterable[int]:
    primes: list[int] = []
    candidate = 2
    while True:
        is_prime = True
        for p in primes:
            if p * p > candidate:
                break
            if candidate % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
            yield candidate
        candidate = 3 if candidate == 2 else candidate + 2


def first_primes(count: int) -> list[int]:
    if count < 0:
        raise ValueError("negative prime count")
    result: list[int] = []
    for p in prime_stream():
        if len(result) == count:
            break
        result.append(p)
    return result


def primorial_support_limit(n_max: int) -> int:
    if n_max < 2:
        return 0
    product = 1
    count = 0
    for p in prime_stream():
        if product * p > n_max:
            return count
        product *= p
        count += 1
    raise AssertionError("unreachable")


def floor_log_power(limit: int, base: int) -> int:
    """Largest e>=0 such that base**e <= limit, using exact integers."""
    if limit < 1 or base < 2:
        raise ValueError("invalid floor-log input")
    exponent = 0
    power = 1
    while power <= limit // base:
        power *= base
        exponent += 1
    return exponent


@lru_cache(maxsize=None)
def prime_power_abundancy(p: int, exponent: int) -> Fraction:
    if p < 2 or exponent < 1:
        raise ValueError("invalid prime power")
    return Fraction(p ** (exponent + 1) - 1, p**exponent * (p - 1))


def fraction_json(value: Fraction) -> dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def fraction_decimal_outward(value: Fraction, digits: int, *, upper: bool) -> str:
    if digits < 0:
        raise ValueError("digits must be nonnegative")
    scale = 10**digits
    scaled = value.numerator * scale
    rounded = -((-scaled) // value.denominator) if upper else scaled // value.denominator
    sign = "-" if rounded < 0 else ""
    raw = str(abs(rounded)).rjust(digits + 1, "0")
    if digits == 0:
        return sign + raw
    return f"{sign}{raw[:-digits]}.{raw[-digits:]}"


def canonical_json_bytes(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")


@dataclass
class Counts:
    prunes: int = 0
    satisfied_leaves: int = 0
    below_domain_leaves: int = 0
    unresolved_leaves: int = 0
    violation_leaves: int = 0
    internal_nodes: int = 0


class CertificateSearch:
    def __init__(self, n_max: int, params: RobinParameters) -> None:
        if n_max <= FINITE_EXCEPTION:
            raise ValueError("n_max must exceed 5040")
        params.validate()
        self.n_max = n_max
        self.params = params
        self.k_max = primorial_support_limit(n_max)
        self.primes = first_primes(self.k_max)
        self.streams: list[list[str]] = [[] for _ in range(self.k_max)]
        self.counts = Counts()

        self.closest_score = float("-inf")
        self.closest_n = 1
        self.closest_exponents: list[int] = []
        self.closest_abundancy = Fraction(0)

        self.tightest_ratio = Fraction(0)
        self.tightest_terminal: dict[str, object] | None = None

    def run(self) -> dict[str, object]:
        for support in range(1, self.k_max + 1):
            primes = self.primes[:support]
            suffix_primorial = [1] * (support + 1)
            for index in range(support - 1, -1, -1):
                suffix_primorial[index] = suffix_primorial[index + 1] * primes[index]
            self._visit(
                support=support,
                primes=primes,
                suffix_primorial=suffix_primorial,
                prefix=(),
                prefix_n=1,
                prefix_abundancy=Fraction(1),
                previous_exponent=None,
            )

        complete = self.counts.unresolved_leaves == 0 and self.counts.violation_leaves == 0
        body: dict[str, object] = {
            "schema": "riemann.robin.canonical-tree.v1",
            "status": self._status(),
            "finite_region": {
                "integer_lower": FINITE_EXCEPTION + 1,
                "integer_upper": str(self.n_max),
                "canonical_support_max": self.k_max,
                "definition": (
                    "all vectors (a_1,...,a_K) with 1<=K<=K_max, "
                    "a_1>=...>=a_K>=1, and product p_i^a_i<=integer_upper"
                ),
            },
            "parameters": asdict(self.params),
            "prime_prefix": self.primes,
            "counts": asdict(self.counts),
            "terminal_stream_encoding": {
                "form": "CODE:e1,e2,...",
                "codes": {
                    "P": "rigorously pruned internal prefix",
                    "S": "rigorously satisfied leaf",
                    "B": "leaf at or below 5040, outside Robin domain",
                    "U": "unresolved leaf",
                    "V": "rigorously violating leaf",
                },
                "support": "outer-list index plus one",
                "order": "deterministic depth-first traversal with exponents descending",
                "verification": (
                    "the verifier reconstructs n_min, all exponent caps, exact rational "
                    "ceilings, dyadic RHS intervals, leaf values, and full DFS coverage"
                ),
            },
            "terminal_streams": self.streams,
            "strict_terminal_normalized_ratio_upper": self.tightest_terminal,
            "global_canonical_normalized_ratio_upper": (
                self.tightest_terminal if complete else None
            ),
            "all_integer_consequence": self._all_integer_consequence() if complete else None,
            "closest_checked_leaf_discovery_only": {
                "n": str(self.closest_n),
                "exponents": self.closest_exponents,
                "abundancy": fraction_json(self.closest_abundancy),
                "normalized_ratio_binary64": (
                    None
                    if self.closest_score == float("-inf")
                    else format(self.closest_score, ".17g")
                ),
            },
            "proof_boundary": (
                "The certificate covers only the stated finite region. The all-integer "
                "consequence additionally depends on T-2001 and T-2002 from stacked PR #24."
            ),
        }
        body["certificate_sha256"] = hashlib.sha256(canonical_json_bytes(body)).hexdigest()
        return body

    def _status(self) -> str:
        if self.counts.violation_leaves:
            return "CERTIFIED_VIOLATION_FOUND_PENDING_INDEPENDENT_VERIFICATION"
        if self.counts.unresolved_leaves:
            return "INCOMPLETE_UNRESOLVED_INTERVALS"
        return "CERTIFIED_FINITE_REGION_PENDING_INDEPENDENT_VERIFICATION"

    def _consider_tight_terminal(
        self,
        *,
        kind: str,
        support: int,
        prefix: Sequence[int],
        reference_n: int,
        abundancy_ceiling: Fraction,
        rhs_lower_numerator: int,
    ) -> None:
        rhs_lower = Fraction(rhs_lower_numerator, 1 << self.params.bits)
        ratio = abundancy_ceiling / rhs_lower
        if ratio >= 1:
            raise RuntimeError("non-strict terminal entered margin tracker")
        if ratio > self.tightest_ratio:
            self.tightest_ratio = ratio
            self.tightest_terminal = {
                "kind": kind,
                "support": support,
                "prefix": list(prefix),
                "reference_n": str(reference_n),
                "abundancy_ceiling": fraction_json(abundancy_ceiling),
                "rhs_lower": {
                    "bits": self.params.bits,
                    "lower_numerator": str(rhs_lower_numerator),
                },
                "normalized_ratio_upper": fraction_json(ratio),
                "normalized_ratio_upper_decimal_outward": fraction_decimal_outward(
                    ratio, 30, upper=True
                ),
            }

    def _all_integer_consequence(self) -> dict[str, object]:
        if self.tightest_terminal is None:
            raise RuntimeError("complete certificate has no strict terminal")
        rhs_5041 = robin_rhs(5041, self.params)
        rhs_5583 = robin_rhs(5583, self.params)
        cases = {
            "finite_window_5041_5582": Fraction(224, 65)
            / Fraction(rhs_5041.lo, 1 << self.params.bits),
            "canonical_image_at_most_5040_for_n_at_least_5583": Fraction(403, 105)
            / Fraction(rhs_5583.lo, 1 << self.params.bits),
            "canonical_image_above_5040": self.tightest_ratio,
        }
        label, global_ratio = max(cases.items(), key=lambda item: item[1])
        if global_ratio >= 1:
            raise RuntimeError("all-integer case bound is not strict")
        return {
            "status": "PROPOSED_LOGICAL_CONSEQUENCE_WITH_VERIFIED_ARITHMETIC",
            "dependencies": [
                "T-2001: independently reproduced finite Robin barrier",
                "T-2002: canonical consecutive-prime exponent dominance",
            ],
            "integer_range": [FINITE_EXCEPTION + 1, str(self.n_max)],
            "case_bounds": {
                name: {
                    "normalized_ratio_upper": fraction_json(ratio),
                    "decimal_outward": fraction_decimal_outward(ratio, 30, upper=True),
                }
                for name, ratio in cases.items()
            },
            "controlling_case": label,
            "normalized_ratio_upper": fraction_json(global_ratio),
            "normalized_ratio_upper_decimal_outward": fraction_decimal_outward(
                global_ratio, 30, upper=True
            ),
            "conclusion": (
                "Assuming the named structural dependencies, every integer in the "
                "stated range satisfies Robin's strict inequality."
            ),
        }

    def _visit(
        self,
        *,
        support: int,
        primes: Sequence[int],
        suffix_primorial: Sequence[int],
        prefix: tuple[int, ...],
        prefix_n: int,
        prefix_abundancy: Fraction,
        previous_exponent: int | None,
    ) -> None:
        depth = len(prefix)
        if depth == support:
            self._record_leaf(support, prefix, prefix_n, prefix_abundancy)
            return

        self.counts.internal_nodes += 1

        # Finite size-aware tail ceiling. Each remaining exponent is bounded
        # independently by the total size budget after forcing all other tail
        # primes to appear to exponent one, and also by monotonicity of exponents.
        if prefix:
            cap = prefix[-1]
            n_min = prefix_n * suffix_primorial[depth]
            remaining_product = suffix_primorial[depth]
            upper = prefix_abundancy
            for p in primes[depth:]:
                other_minimum = remaining_product // p
                individual_budget = self.n_max // (prefix_n * other_minimum)
                individual_cap = min(cap, floor_log_power(individual_budget, p))
                if individual_cap < 1:
                    raise RuntimeError("reachable node has impossible tail")
                upper *= prime_power_abundancy(p, individual_cap)
            # Binary64 is used only as a one-sided discovery filter. A prune is
            # emitted exclusively after the dyadic verifier proves the strict sign.
            heuristic_rhs = math.exp(0.5772156649015329) * math.log(math.log(n_min))
            if float(upper) < heuristic_rhs * (1.0 - 1e-13):
                rhs = robin_rhs(n_min, self.params)
                if rhs.lower_gt_fraction(upper):
                    self._emit(support, "P", prefix)
                    self._consider_tight_terminal(
                        kind="PRUNE_SIZE_AWARE",
                        support=support,
                        prefix=prefix,
                        reference_n=n_min,
                        abundancy_ceiling=upper,
                        rhs_lower_numerator=rhs.lo,
                    )
                    self.counts.prunes += 1
                    return

        p = primes[depth]
        tail_after = suffix_primorial[depth + 1]
        budget = self.n_max // (prefix_n * tail_after)
        max_by_size = floor_log_power(budget, p)
        max_exponent = (
            max_by_size
            if previous_exponent is None
            else min(previous_exponent, max_by_size)
        )
        if max_exponent < 1:
            raise RuntimeError("reachable internal node has no children")

        for exponent in range(max_exponent, 0, -1):
            self._visit(
                support=support,
                primes=primes,
                suffix_primorial=suffix_primorial,
                prefix=prefix + (exponent,),
                prefix_n=prefix_n * p**exponent,
                prefix_abundancy=prefix_abundancy
                * prime_power_abundancy(p, exponent),
                previous_exponent=exponent,
            )

    def _record_leaf(
        self,
        support: int,
        exponents: tuple[int, ...],
        n: int,
        abundancy: Fraction,
    ) -> None:
        if n <= FINITE_EXCEPTION:
            self._emit(support, "B", exponents)
            self.counts.below_domain_leaves += 1
            return

        score = float(abundancy) / (
            math.exp(0.5772156649015329) * math.log(math.log(n))
        )
        if score > self.closest_score:
            self.closest_score = score
            self.closest_n = n
            self.closest_exponents = list(exponents)
            self.closest_abundancy = abundancy

        rhs = robin_rhs(n, self.params)
        if rhs.lower_gt_fraction(abundancy):
            code = "S"
            self.counts.satisfied_leaves += 1
            self._consider_tight_terminal(
                kind="LEAF_SATISFIED",
                support=support,
                prefix=exponents,
                reference_n=n,
                abundancy_ceiling=abundancy,
                rhs_lower_numerator=rhs.lo,
            )
        elif rhs.upper_le_fraction(abundancy):
            code = "V"
            self.counts.violation_leaves += 1
        else:
            code = "U"
            self.counts.unresolved_leaves += 1
        self._emit(support, code, exponents)

    def _emit(self, support: int, code: str, prefix: Sequence[int]) -> None:
        token = code + ":" + ",".join(str(value) for value in prefix)
        self.streams[support - 1].append(token)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n-max", type=int, required=True)
    parser.add_argument("--bits", type=int, default=256)
    parser.add_argument("--log-terms", type=int, default=88)
    parser.add_argument("--exp-terms", type=int, default=88)
    parser.add_argument("--harmonic-cutoff", type=int, default=250_000)
    parser.add_argument("--output", required=True)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    params = RobinParameters(
        bits=args.bits,
        log_terms=args.log_terms,
        exp_terms=args.exp_terms,
        harmonic_cutoff=args.harmonic_cutoff,
    )
    certificate = CertificateSearch(args.n_max, params).run()
    Path(args.output).write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    summary = {
        key: certificate[key]
        for key in (
            "status",
            "finite_region",
            "counts",
            "global_canonical_normalized_ratio_upper",
            "all_integer_consequence",
            "certificate_sha256",
        )
    }
    print(json.dumps(summary, indent=2))
    return 2 if certificate["status"] == "INCOMPLETE_UNRESOLVED_INTERVALS" else 0


if __name__ == "__main__":
    raise SystemExit(main())

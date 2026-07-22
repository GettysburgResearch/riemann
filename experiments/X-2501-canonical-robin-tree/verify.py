#!/usr/bin/env python3
"""Independent verifier for riemann.robin.canonical-tree.v1 certificates.

This module does not import the search traversal. It independently reconstructs
prime generation, support bounds, child ranges, exact integers, exact abundancy
ceilings, terminal-prefix coverage, and every dyadic sign comparison.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
from typing import Sequence
from functools import lru_cache

from certmath import RobinParameters, robin_rhs

FINITE_EXCEPTION = 5040


def primes_by_trial_division(count: int) -> list[int]:
    result: list[int] = []
    candidate = 2
    while len(result) < count:
        prime = True
        divisor = 2
        while divisor * divisor <= candidate:
            if candidate % divisor == 0:
                prime = False
                break
            divisor += 1
        if prime:
            result.append(candidate)
        candidate += 1
    return result


@lru_cache(maxsize=None)
def exact_prime_power_abundancy(p: int, exponent: int) -> Fraction:
    if p < 2 or exponent < 1:
        raise ValueError("invalid prime power")
    numerator = 0
    power = 1
    for _ in range(exponent + 1):
        numerator += power
        power *= p
    return Fraction(numerator, p**exponent)


def exact_floor_log(limit: int, base: int) -> int:
    if limit < 1 or base < 2:
        raise ValueError("invalid floor-log input")
    exponent = 0
    while base ** (exponent + 1) <= limit:
        exponent += 1
    return exponent


def fraction_json(value: Fraction) -> dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def fraction_decimal_outward(value: Fraction, digits: int, *, upper: bool) -> str:
    scale = 10**digits
    scaled = value.numerator * scale
    rounded = -((-scaled) // value.denominator) if upper else scaled // value.denominator
    sign = "-" if rounded < 0 else ""
    raw = str(abs(rounded)).rjust(digits + 1, "0")
    if digits == 0:
        return sign + raw
    return f"{sign}{raw[:-digits]}.{raw[-digits:]}"


def json_digest_without_digest(certificate: dict[str, object]) -> str:
    body = dict(certificate)
    body.pop("certificate_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


class StreamCursor:
    def __init__(self, tokens: object) -> None:
        if not isinstance(tokens, list) or not all(isinstance(token, str) for token in tokens):
            raise ValueError("terminal stream must be a list of strings")
        self.tokens = tokens
        self.index = 0

    @staticmethod
    def parse(token: str) -> tuple[str, tuple[int, ...]]:
        if len(token) < 2 or token[1] != ":":
            raise ValueError("invalid terminal token")
        code = token[0]
        if code not in {"P", "S", "B", "U", "V"}:
            raise ValueError("unknown terminal code")
        payload = token[2:]
        prefix = () if payload == "" else tuple(int(value) for value in payload.split(","))
        if any(value < 1 for value in prefix):
            raise ValueError("nonpositive exponent in terminal token")
        return code, prefix

    def peek(self) -> tuple[str, tuple[int, ...]] | None:
        if self.index == len(self.tokens):
            return None
        return self.parse(self.tokens[self.index])

    def consume(self) -> tuple[str, tuple[int, ...]]:
        item = self.peek()
        if item is None:
            raise ValueError("terminal stream ended before traversal")
        self.index += 1
        return item

    def done(self) -> bool:
        return self.index == len(self.tokens)


class IndependentVerifier:
    def __init__(self, certificate: dict[str, object]) -> None:
        self.certificate = certificate
        if certificate.get("schema") != "riemann.robin.canonical-tree.v1":
            raise ValueError("unsupported schema")
        region = certificate.get("finite_region")
        if not isinstance(region, dict):
            raise ValueError("finite_region missing")
        if int(region.get("integer_lower", 0)) != FINITE_EXCEPTION + 1:
            raise ValueError("unexpected lower bound")
        self.n_max = int(region["integer_upper"])
        self.k_max = int(region["canonical_support_max"])
        if self.n_max <= FINITE_EXCEPTION:
            raise ValueError("empty Robin domain")

        raw_params = certificate.get("parameters")
        if not isinstance(raw_params, dict):
            raise ValueError("parameters missing")
        self.params = RobinParameters(**{key: int(value) for key, value in raw_params.items()})
        self.params.validate()

        self.primes = primes_by_trial_division(self.k_max)
        if certificate.get("prime_prefix") != self.primes:
            raise ValueError("prime prefix mismatch")
        streams = certificate.get("terminal_streams")
        if not isinstance(streams, list) or len(streams) != self.k_max:
            raise ValueError("terminal_streams shape mismatch")
        self.streams = streams
        self.cursor: StreamCursor | None = None

        self.counts = {
            "prunes": 0,
            "satisfied_leaves": 0,
            "below_domain_leaves": 0,
            "unresolved_leaves": 0,
            "violation_leaves": 0,
            "internal_nodes": 0,
        }
        self.tightest_ratio = Fraction(0)
        self.tightest_terminal: dict[str, object] | None = None

    def replay(self) -> dict[str, object]:
        """Reconstruct the terminal tree under the header parameters."""
        if self.k_max != self._independent_support_limit():
            raise ValueError("canonical support maximum is not exact")

        for support in range(1, self.k_max + 1):
            self.cursor = StreamCursor(self.streams[support - 1])
            primes = self.primes[:support]
            suffix_primorial = [1] * (support + 1)
            for index in range(support - 1, -1, -1):
                suffix_primorial[index] = suffix_primorial[index + 1] * primes[index]
            self._walk(
                support=support,
                primes=primes,
                suffix_primorial=suffix_primorial,
                prefix=(),
                prefix_n=1,
                prefix_abundancy=Fraction(1),
                previous_exponent=None,
            )
            if not self.cursor.done():
                raise ValueError(f"extra terminal tokens for support {support}")
        self.cursor = None

        status = self._expected_status()
        complete = self.counts["unresolved_leaves"] == 0 and self.counts["violation_leaves"] == 0
        return {
            "status": status,
            "counts": self.counts,
            "strict_terminal_normalized_ratio_upper": self.tightest_terminal,
            "global_canonical_normalized_ratio_upper": (
                self.tightest_terminal if complete else None
            ),
            "all_integer_consequence": self._all_integer_consequence() if complete else None,
        }

    def verify(self) -> dict[str, object]:
        replay = self.replay()
        if self.certificate.get("counts") != replay["counts"]:
            raise ValueError("count summary mismatch")
        if self.certificate.get("status") != replay["status"]:
            raise ValueError("status inconsistent with terminal classifications")
        if self.certificate.get("strict_terminal_normalized_ratio_upper") != replay["strict_terminal_normalized_ratio_upper"]:
            raise ValueError("tightest terminal summary mismatch")
        if self.certificate.get("global_canonical_normalized_ratio_upper") != replay["global_canonical_normalized_ratio_upper"]:
            raise ValueError("global canonical ratio summary mismatch")
        if self.certificate.get("all_integer_consequence") != replay["all_integer_consequence"]:
            raise ValueError("all-integer consequence mismatch")

        digest = json_digest_without_digest(self.certificate)
        if self.certificate.get("certificate_sha256") != digest:
            raise ValueError("certificate digest mismatch")

        return {
            "schema": "riemann.robin.canonical-tree.verification.v1",
            "verified": True,
            "status": replay["status"],
            "finite_region": self.certificate["finite_region"],
            "counts": replay["counts"],
            "global_canonical_normalized_ratio_upper": replay["global_canonical_normalized_ratio_upper"],
            "all_integer_consequence": replay["all_integer_consequence"],
            "certificate_sha256": digest,
            "proof_boundary": (
                "This verifies the complete finite canonical tree and all exact/dyadic "
                "arithmetic. The all-integer consequence additionally depends on the "
                "named structural theorems from stacked PR #24."
            ),
        }

    def _expected_status(self) -> str:
        if self.counts["violation_leaves"]:
            return "CERTIFIED_VIOLATION_FOUND_PENDING_INDEPENDENT_VERIFICATION"
        if self.counts["unresolved_leaves"]:
            return "INCOMPLETE_UNRESOLVED_INTERVALS"
        return "CERTIFIED_FINITE_REGION_PENDING_INDEPENDENT_VERIFICATION"

    def _independent_support_limit(self) -> int:
        product = 1
        count = 0
        candidate = 2
        while True:
            prime = True
            divisor = 2
            while divisor * divisor <= candidate:
                if candidate % divisor == 0:
                    prime = False
                    break
                divisor += 1
            if prime:
                if product * candidate > self.n_max:
                    return count
                product *= candidate
                count += 1
            candidate += 1

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
            raise ValueError("terminal lacks a strict normalized margin")
        if ratio > self.tightest_ratio:
            self.tightest_ratio = ratio
            self.tightest_terminal = {
                "kind": kind,
                "support": support,
                "prefix": list(prefix),
                "reference_n": str(reference_n),
                "abundancy_ceiling": fraction_json(abundancy_ceiling),
                "rhs_lower": {"bits": self.params.bits, "lower_numerator": str(rhs_lower_numerator)},
                "normalized_ratio_upper": fraction_json(ratio),
                "normalized_ratio_upper_decimal_outward": fraction_decimal_outward(ratio, 30, upper=True),
            }

    def _all_integer_consequence(self) -> dict[str, object]:
        if self.tightest_terminal is None:
            raise ValueError("complete certificate has no strict terminal")
        rhs_5041 = robin_rhs(5041, self.params)
        rhs_5583 = robin_rhs(5583, self.params)
        cases = {
            "finite_window_5041_5582": Fraction(224, 65) / Fraction(rhs_5041.lo, 1 << self.params.bits),
            "canonical_image_at_most_5040_for_n_at_least_5583": Fraction(403, 105) / Fraction(rhs_5583.lo, 1 << self.params.bits),
            "canonical_image_above_5040": self.tightest_ratio,
        }
        label, global_ratio = max(cases.items(), key=lambda item: item[1])
        if global_ratio >= 1:
            raise ValueError("all-integer case bound is not strict")
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
            "normalized_ratio_upper_decimal_outward": fraction_decimal_outward(global_ratio, 30, upper=True),
            "conclusion": (
                "Assuming the named structural dependencies, every integer in the "
                "stated range satisfies Robin's strict inequality."
            ),
        }

    def _walk(
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
            self._verify_leaf(support, prefix, prefix_n, prefix_abundancy)
            return

        self.counts["internal_nodes"] += 1
        if self.cursor is None:
            raise RuntimeError("support cursor not initialized")
        next_item = self.cursor.peek()
        if next_item is not None and next_item[1] == prefix:
            code, _ = self.cursor.consume()
            if code != "P":
                raise ValueError("non-prune token appears at an internal node")
            self._verify_prune(
                support=support,
                primes=primes,
                suffix_primorial=suffix_primorial,
                prefix=prefix,
                prefix_n=prefix_n,
                prefix_abundancy=prefix_abundancy,
            )
            self.counts["prunes"] += 1
            return

        p = primes[depth]
        tail_after = suffix_primorial[depth + 1]
        budget = self.n_max // (prefix_n * tail_after)
        max_by_size = exact_floor_log(budget, p)
        max_exponent = max_by_size if previous_exponent is None else min(previous_exponent, max_by_size)
        if max_exponent < 1:
            raise ValueError("uncovered dead internal node")
        for exponent in range(max_exponent, 0, -1):
            self._walk(
                support=support,
                primes=primes,
                suffix_primorial=suffix_primorial,
                prefix=prefix + (exponent,),
                prefix_n=prefix_n * p**exponent,
                prefix_abundancy=prefix_abundancy * exact_prime_power_abundancy(p, exponent),
                previous_exponent=exponent,
            )

    def _verify_prune(
        self,
        *,
        support: int,
        primes: Sequence[int],
        suffix_primorial: Sequence[int],
        prefix: tuple[int, ...],
        prefix_n: int,
        prefix_abundancy: Fraction,
    ) -> None:
        if not prefix:
            raise ValueError("root pruning is not licensed")
        depth = len(prefix)
        cap = prefix[-1]
        n_min = prefix_n * suffix_primorial[depth]
        remaining_product = suffix_primorial[depth]
        upper = prefix_abundancy
        for p in primes[depth:]:
            other_minimum = remaining_product // p
            individual_budget = self.n_max // (prefix_n * other_minimum)
            individual_cap = min(cap, exact_floor_log(individual_budget, p))
            if individual_cap < 1:
                raise ValueError("invalid tail exponent cap")
            upper *= exact_prime_power_abundancy(p, individual_cap)
        rhs = robin_rhs(n_min, self.params)
        if not rhs.lower_gt_fraction(upper):
            raise ValueError("invalid subtree prune")
        self._consider_tight_terminal(
            kind="PRUNE_SIZE_AWARE",
            support=support,
            prefix=prefix,
            reference_n=n_min,
            abundancy_ceiling=upper,
            rhs_lower_numerator=rhs.lo,
        )

    def _verify_leaf(
        self,
        support: int,
        exponents: tuple[int, ...],
        n: int,
        abundancy: Fraction,
    ) -> None:
        if self.cursor is None:
            raise RuntimeError("support cursor not initialized")
        code, token_prefix = self.cursor.consume()
        if token_prefix != exponents:
            raise ValueError("leaf token order or identity mismatch")
        if n <= FINITE_EXCEPTION:
            if code != "B":
                raise ValueError("below-domain leaf mislabeled")
            self.counts["below_domain_leaves"] += 1
            return

        rhs = robin_rhs(n, self.params)
        if rhs.lower_gt_fraction(abundancy):
            expected = "S"
            self.counts["satisfied_leaves"] += 1
            self._consider_tight_terminal(
                kind="LEAF_SATISFIED",
                support=support,
                prefix=exponents,
                reference_n=n,
                abundancy_ceiling=abundancy,
                rhs_lower_numerator=rhs.lo,
            )
        elif rhs.upper_le_fraction(abundancy):
            expected = "V"
            self.counts["violation_leaves"] += 1
        else:
            expected = "U"
            self.counts["unresolved_leaves"] += 1
        if code != expected:
            raise ValueError("leaf classification mismatch")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate")
    parser.add_argument("--output")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    certificate = json.loads(Path(args.certificate).read_text(encoding="utf-8"))
    result = IndependentVerifier(certificate).verify()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

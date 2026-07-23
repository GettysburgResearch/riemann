from __future__ import annotations

import copy
import hashlib
import json
import unittest
from fractions import Fraction

from certmath import RobinParameters
from search import Search, exact_powered, parse_duals, separate_data, abundancy_pp
from verify import Verifier, powered_joint


def refresh_digest(certificate: dict[str, object]) -> None:
    body = dict(certificate)
    body.pop("certificate_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":")).encode("utf-8")
    certificate["certificate_sha256"] = hashlib.sha256(raw).hexdigest()


class PoweredEnvelopeTests(unittest.TestCase):
    def test_synthetic_shared_budget_strictly_improves(self) -> None:
        prefix_n = 2**4
        prefix_i = abundancy_pp(2, 4)
        tail = [3, 5, 7]
        bound = 8400
        _, residual, caps, separate = separate_data(
            prefix_n, prefix_i, tail, 4, bound
        )
        self.assertEqual(caps, [2, 2, 1])
        self.assertEqual(separate, Fraction(12493, 3150))

        exact = exact_powered(prefix_i, tail, 4, residual, caps, 1, 64)
        self.assertLess(exact["powered"], Fraction(39, 10) ** 64)
        self.assertGreater(separate**64, Fraction(39, 10) ** 64)

        best = Fraction(0)
        best_exponents = None
        for b1 in range(4, 0, -1):
            for b2 in range(b1, 0, -1):
                for b3 in range(b2, 0, -1):
                    n = prefix_n * 3**b1 * 5**b2 * 7**b3
                    if n > bound:
                        continue
                    value = (
                        prefix_i
                        * abundancy_pp(3, b1)
                        * abundancy_pp(5, b2)
                        * abundancy_pp(7, b3)
                    )
                    self.assertLessEqual(value**64, exact["joint"])
                    if value > best:
                        best = value
                        best_exponents = (b1, b2, b3)
        self.assertEqual(best, Fraction(403, 105))
        self.assertEqual(best_exponents, (2, 1, 1))

    def test_independent_powered_reconstruction_agrees(self) -> None:
        prefix_n = 2**4
        prefix_i = abundancy_pp(2, 4)
        tail = [3, 5, 7]
        bound = 8400
        _, residual, caps, _ = separate_data(prefix_n, prefix_i, tail, 4, bound)
        author = exact_powered(prefix_i, tail, 4, residual, caps, 1, 64)
        checker, checker_sep = powered_joint(
            prefix_i, tail, 4, caps, prefix_n, bound, 1, 64
        )
        self.assertEqual(checker, author["joint"])
        self.assertEqual(checker_sep, author["separate"])


class CertificateReplayTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.params = RobinParameters(72, 10, 10, 200)
        cls.certificate = Search(
            10**8,
            cls.params,
            parse_duals("1/128,1/96,1/64"),
            96,
        ).run()

    def test_complete_small_certificate_replays(self) -> None:
        result = Verifier(copy.deepcopy(self.certificate)).verify()
        self.assertTrue(result["verified"])
        self.assertEqual(result["counts"]["unresolved_leaves"], 0)
        self.assertEqual(result["counts"]["violation_leaves"], 0)
        self.assertGreater(result["counts"]["powered_prunes"], 0)

    def test_mutated_powered_dual_is_rejected(self) -> None:
        forged = copy.deepcopy(self.certificate)
        found = False
        for stream in forged["terminal_streams"]:
            for index, token in enumerate(stream):
                if token.startswith("J:"):
                    stream[index] = token.replace("J:1,128:", "J:2,127:", 1)
                    found = True
                    break
            if found:
                break
        self.assertTrue(found)
        refresh_digest(forged)
        with self.assertRaises(ValueError):
            Verifier(forged).verify()

    def test_deleted_terminal_is_rejected(self) -> None:
        forged = copy.deepcopy(self.certificate)
        stream = next(items for items in forged["terminal_streams"] if items)
        del stream[len(stream) // 2]
        refresh_digest(forged)
        with self.assertRaises(ValueError):
            Verifier(forged).verify()

    def test_forged_quantitative_summary_is_rejected(self) -> None:
        forged = copy.deepcopy(self.certificate)
        forged["global_canonical_normalized_ratio_upper"][
            "normalized_ratio_upper_decimal_outward"
        ] = "0.1"
        refresh_digest(forged)
        with self.assertRaises(ValueError):
            Verifier(forged).verify()

    def test_weak_parameter_replay_fails_closed(self) -> None:
        forged = copy.deepcopy(self.certificate)
        forged["parameters"] = {
            "bits": 64,
            "log_terms": 8,
            "exp_terms": 8,
            "harmonic_cutoff": 100,
        }
        refresh_digest(forged)
        with self.assertRaises(ValueError):
            Verifier(forged).verify()


if __name__ == "__main__":
    unittest.main()

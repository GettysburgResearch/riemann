import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from verify import V, verify

DOC = json.loads((ROOT / "artifacts" / "certificate.json").read_text())


class T(unittest.TestCase):
    def ok(self, document):
        self.assertEqual(
            verify(document, None, True)["verdict"],
            "CERTIFIED_FIRST_REAL_COMMON_PROFILE_SOFT_LEDGER",
        )

    def bad(self, mutation):
        document = copy.deepcopy(DOC)
        mutation(document)
        with self.assertRaises(V):
            verify(document, None, True)

    def test_ok(self):
        self.ok(copy.deepcopy(DOC))

    def test_source_identity_mutation(self):
        self.bad(
            lambda d: d["source_identity"].__setitem__(
                "localization_matrix", [[1, 1], [0, 1]]
            )
        )

    def test_graph_lmi_mutation(self):
        self.bad(
            lambda d: d["profile"]["graph_lmi"].__setitem__(
                "M_squared_upper", {"numerator": "1", "denominator": "100"}
            )
        )

    def test_soft_threshold_mutation(self):
        self.bad(
            lambda d: d["profile"]["buffered_soft_export"].__setitem__(
                "threshold_tau", {"numerator": "1", "denominator": "100000"}
            )
        )

    def test_prime_polar_cross_mutation(self):
        self.bad(
            lambda d: d["complete_weil_matrix"].__setitem__(
                "Z_soft_hard",
                {
                    "lower": {
                        "numerator": str(int(d["source_identity"]["metric_gram"])),
                        "denominator": "1",
                    },
                    "upper": {
                        "numerator": str(int(d["source_identity"]["metric_gram"])),
                        "denominator": "1",
                    },
                },
            )
        )

    def test_floor_mutation(self):
        self.bad(
            lambda d: d["pr191_direct_short"].__setitem__(
                "target_floor_m", {"numerator": "1", "denominator": "1000"}
            )
        )

    def test_verdict_mutation(self):
        self.bad(lambda d: d.__setitem__("verdict", "PASS"))


if __name__ == "__main__":
    unittest.main()

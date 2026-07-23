import copy
import json
import unittest
from pathlib import Path

from prepare_autocorrelation import prepare

HERE = Path(__file__).resolve().parent.parent

PILOT = {
    "parameters": {"carrier": "37.5"},
    "dyadic_vector": {
        "scale_bits": 20,
        "real_numerators": [524288, 262144, -131072, 65536],
        "imag_numerators": [0, 131072, 65536, -32768],
    },
}


class PrepareAutocorrelationTests(unittest.TestCase):
    def test_pilot_manifest_matches_retained_file(self):
        expected = (HERE / "certificates" / "pilot-autocorrelation.txt").read_text(
            encoding="utf-8"
        )
        self.assertEqual(prepare(copy.deepcopy(PILOT), 5, 20000), expected)

    def test_exact_first_autocorrelations(self):
        text = prepare(copy.deepcopy(PILOT), 5, 20000)
        self.assertIn("a 0 387620798464 0", text)
        self.assertIn("a 1 100931731456 103079215104", text)
        self.assertTrue(text.endswith("a 4 0 0\n"))

    def test_boolean_component_rejected(self):
        bad = copy.deepcopy(PILOT)
        bad["dyadic_vector"]["real_numerators"][0] = True
        with self.assertRaises(ValueError):
            prepare(bad, 5, 20000)

    def test_mismatched_arrays_rejected(self):
        bad = copy.deepcopy(PILOT)
        bad["dyadic_vector"]["imag_numerators"].pop()
        with self.assertRaises(ValueError):
            prepare(bad, 5, 20000)

    def test_parameter_digest_changes_with_cutoff(self):
        left = prepare(copy.deepcopy(PILOT), 5, 20000)
        right = prepare(copy.deepcopy(PILOT), 6, 200000)
        left_digest = next(
            line.split()[1]
            for line in left.splitlines()
            if line.startswith("parameter_sha256 ")
        )
        right_digest = next(
            line.split()[1]
            for line in right.splitlines()
            if line.startswith("parameter_sha256 ")
        )
        self.assertNotEqual(left_digest, right_digest)


if __name__ == "__main__":
    unittest.main()

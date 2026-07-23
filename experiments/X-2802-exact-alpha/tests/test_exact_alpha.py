import copy
import unittest
import mpmath as mp

from exact_alpha import CertificateError, verify

TARGET = {
    "schema": "riemann.alpha-rational.v1",
    "carrier": {"numerator": 94184072727073, "denominator": 20},
    "atan_1_5_terms": 80,
    "atan_1_239_terms": 20,
    "log_terms": 90,
    "output_scale_bits": 192,
}


class ExactAlphaTests(unittest.TestCase):
    def test_target_is_one_ulp_wide(self):
        result = verify(TARGET)
        self.assertEqual(result["width_dyadic_units"], 1)
        self.assertTrue(result["strictly_positive"])

    def test_target_contains_high_precision_control(self):
        result = verify(TARGET)
        interval = result["alpha_dyadic_interval"]
        with mp.workdps(100):
            scale = mp.mpf(2) ** interval["scale_bits"]
            carrier = mp.mpf(94184072727073) / 20
            value = mp.log(carrier / (2 * mp.pi)) / (2 * mp.pi)
            self.assertLessEqual(mp.mpf(interval["lower_num"]) / scale, value)
            self.assertLessEqual(value, mp.mpf(interval["upper_num"]) / scale)

    def test_schema_is_strict(self):
        bad = copy.deepcopy(TARGET)
        bad["schema"] = "wrong"
        with self.assertRaises(CertificateError):
            verify(bad)

    def test_boolean_integer_rejected(self):
        bad = copy.deepcopy(TARGET)
        bad["log_terms"] = True
        with self.assertRaises(CertificateError):
            verify(bad)

    def test_small_carrier_negative_alpha_is_enclosed(self):
        data = copy.deepcopy(TARGET)
        data["carrier"] = {"numerator": 1, "denominator": 1}
        result = verify(data)
        self.assertLess(result["alpha_dyadic_interval"]["upper_num"], 0)

    def test_more_terms_do_not_widen_target(self):
        base = verify(TARGET)["alpha_dyadic_interval"]
        data = copy.deepcopy(TARGET)
        data["atan_1_5_terms"] = 90
        data["atan_1_239_terms"] = 24
        data["log_terms"] = 96
        refined = verify(data)["alpha_dyadic_interval"]
        self.assertGreaterEqual(refined["lower_num"], base["lower_num"])
        self.assertLessEqual(refined["upper_num"], base["upper_num"])


if __name__ == "__main__":
    unittest.main()

import copy
import unittest

from verify_normalization import EXPECTED, FingerprintError, verify


class FingerprintTests(unittest.TestCase):
    def test_exact_fingerprint(self):
        self.assertTrue(verify(copy.deepcopy(EXPECTED))["verified"])

    def test_prime_sign_mutation(self):
        value = copy.deepcopy(EXPECTED)
        value["prime"]["coefficient"] = "+Lambda(q)/(pi*sqrt(q))"
        with self.assertRaises(FingerprintError):
            verify(value)

    def test_frequency_mutation(self):
        value = copy.deepcopy(EXPECTED)
        value["prime"]["frequency"] = "log(q)/pi"
        with self.assertRaises(FingerprintError):
            verify(value)

    def test_pole_sign_mutation(self):
        value = copy.deepcopy(EXPECTED)
        value["pole"] = "-2*g(i/2)"
        with self.assertRaises(FingerprintError):
            verify(value)

    def test_arch_sign_mutation(self):
        value = copy.deepcopy(EXPECTED)
        value["archimedean"] = value["archimedean"].replace(
            "+integral", "-integral"
        )
        with self.assertRaises(FingerprintError):
            verify(value)

    def test_zero_coordinate_mutation(self):
        value = copy.deepcopy(EXPECTED)
        value["zero_coordinate"] = "rho-1/2"
        with self.assertRaises(FingerprintError):
            verify(value)

    def test_fourier_mutation(self):
        value = copy.deepcopy(EXPECTED)
        value["fourier"]["forward"] = value["fourier"]["forward"].replace(
            "-2*pi", "+2*pi"
        )
        with self.assertRaises(FingerprintError):
            verify(value)

    def test_assembly_mutation(self):
        value = copy.deepcopy(EXPECTED)
        value["normalized_assembly"] = "A+R+h*S_K"
        with self.assertRaises(FingerprintError):
            verify(value)

    def test_extra_field_rejected(self):
        value = copy.deepcopy(EXPECTED)
        value["note"] = "harmless"
        with self.assertRaises(FingerprintError):
            verify(value)


if __name__ == "__main__":
    unittest.main()

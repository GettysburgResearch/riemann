import unittest

from verify import cardinal_polynomial, real_root_count, verify


class CardinalTests(unittest.TestCase):
    def test_certificate(self):
        result = verify(
            {
                "schema": "riemann.cardinal-truncation-obstruction.v1",
                "max_n": 12,
                "expected_status": "VERIFIED_EXACT_CARDINAL_OBSTRUCTION",
            }
        )
        self.assertEqual(result["status"], "VERIFIED_EXACT_CARDINAL_OBSTRUCTION")
        self.assertTrue(
            all(row["distinct_real_roots"] == 0 for row in result["rows"])
        )

    def test_n1_polynomial(self):
        polynomial, _ = cardinal_polynomial(1)
        self.assertEqual(polynomial, [-1, 0, -1])

    def test_positive_residues_are_not_the_obstruction(self):
        parameter = 3
        signs = {
            node: 1 for node in range(-parameter, parameter + 1)
        }
        polynomial, _ = cardinal_polynomial(parameter, signs)
        self.assertEqual(real_root_count(polynomial), 2 * parameter)

    def test_boolean_rejected(self):
        with self.assertRaises(ValueError):
            verify(
                {
                    "schema": "riemann.cardinal-truncation-obstruction.v1",
                    "max_n": True,
                }
            )

    def test_zero_rejected(self):
        with self.assertRaises(ValueError):
            verify(
                {
                    "schema": "riemann.cardinal-truncation-obstruction.v1",
                    "max_n": 0,
                }
            )

    def test_bad_schema_rejected(self):
        with self.assertRaises(ValueError):
            verify({"schema": "wrong", "max_n": 3})

    def test_false_status_rejected(self):
        with self.assertRaises(ValueError):
            verify(
                {
                    "schema": "riemann.cardinal-truncation-obstruction.v1",
                    "max_n": 3,
                    "expected_status": "FALSE",
                }
            )


if __name__ == "__main__":
    unittest.main()

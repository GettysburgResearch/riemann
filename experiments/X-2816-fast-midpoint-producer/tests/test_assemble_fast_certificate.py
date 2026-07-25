from fractions import Fraction
import importlib.util
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "x2816_assemble",
    ROOT / "assemble_fast_certificate.py",
)
ASSEMBLE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = ASSEMBLE
SPEC.loader.exec_module(ASSEMBLE)


def fjson(value):
    value = Fraction(value)
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def common(start, end):
    return {
        "segment_start": start,
        "segment_end": end,
        "vector_sha256": ASSEMBLE.EXPECTED_VECTOR,
        "parameter_sha256": ASSEMBLE.EXPECTED_PARAMETER,
        "normalization_sha256": ASSEMBLE.EXPECTED_NORMALIZATION,
    }


def direct(start, end, primes, higher, value, include_higher=False):
    data = common(start, end)
    data.update(
        {
            "schema": ASSEMBLE.DIRECT_SCHEMA,
            "prime_count": primes,
            "higher_prime_power_count": higher,
            "total_terms": primes + higher,
            "include_higher_powers": include_higher,
            "prime_rayleigh_interval": {
                "lower": fjson(value),
                "upper": fjson(value),
            },
        }
    )
    return data


def fast(start, end, primes, value):
    data = common(start, end)
    data.update(
        {
            "schema": ASSEMBLE.FAST_SCHEMA,
            "prime_count": primes,
            "higher_prime_power_count": 0,
            "total_terms": primes,
            "include_higher_powers": False,
            "arithmetic_contract": ASSEMBLE.FAST_CONTRACT,
            "phase_grid_M": 32768,
            "phase_taylor_R": 3,
            "log_series_J": 3,
            "sqrt_series_J": 5,
            "midpoint_rayleigh": fjson(value),
        }
    )
    return data


def items():
    fast_primes = 1_000_000_000
    first_primes = 3_000_000_000
    last_primes = ASSEMBLE.EXPECTED_PRIMES - fast_primes - first_primes
    values = [
        direct(
            0,
            2800,
            first_primes,
            ASSEMBLE.EXPECTED_HIGHER,
            1,
            include_higher=True,
        ),
        fast(2800, 4900, fast_primes, 3),
        direct(4900, 5000, last_primes, 0, 2),
    ]
    for index, value in enumerate(values):
        value["_path"] = f"shard-{index}.json"
    return values


class HybridAssemblerTests(unittest.TestCase):
    def test_complete_certificate_adds_moat_once(self):
        output = ASSEMBLE.assemble(items())
        self.assertEqual(output["status"], "STRICT_POSITIVE_PRIME_INTERVAL")
        moat = Fraction(
            int(output["fast_global_moat"]["numerator"]),
            int(output["fast_global_moat"]["denominator"]),
        )
        lower = Fraction(
            int(output["complete_prime_interval"]["lower"]["numerator"]),
            int(output["complete_prime_interval"]["lower"]["denominator"]),
        )
        self.assertEqual(lower, Fraction(6) - moat)

    def test_gap_rejected(self):
        values = items()
        values[1]["segment_start"] = 2801
        with self.assertRaisesRegex(ASSEMBLE.CertificateError, "gap/overlap"):
            ASSEMBLE.assemble(values)

    def test_duplicate_higher_power_stream_rejected(self):
        values = items()
        values[2]["include_higher_powers"] = True
        with self.assertRaisesRegex(ASSEMBLE.CertificateError, "exactly one"):
            ASSEMBLE.assemble(values)

    def test_fast_contract_mutation_rejected(self):
        values = items()
        values[1]["arithmetic_contract"] = "mutated"
        with self.assertRaisesRegex(ASSEMBLE.CertificateError, "contract"):
            ASSEMBLE.assemble(values)

    def test_global_count_mutation_rejected(self):
        values = items()
        values[1]["prime_count"] -= 1
        values[1]["total_terms"] -= 1
        with self.assertRaisesRegex(
            ASSEMBLE.CertificateError,
            "global term counts",
        ):
            ASSEMBLE.assemble(values)


if __name__ == "__main__":
    unittest.main()

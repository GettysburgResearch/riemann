"""Focused exact tests for the FFPS Kummer-transfer spectrum packet."""

from __future__ import annotations

import hashlib
import json
import sys
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import ffps_kummer_transfer_spectrum as subject


class FFPSKummerTransferSpectrumTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()

    def test_direct_kummer_map_is_the_folded_circulant_on_both_cosets(self) -> None:
        for prime in subject.CONTROL_PRIMES:
            generator = subject.primitive_root(prime)
            core_samples = (
                (),
                (1,),
                tuple(sorted({1, generator})),
                tuple(range(1, prime)),
            )
            for representative in (1, generator):
                for cores in core_samples:
                    self.assertEqual(
                        subject.transfer_matrix(prime, cores, representative),
                        subject.direct_transfer_matrix(prime, cores, representative),
                    )

    def test_full_incidence_pushforward_is_a_scaled_coisometry(self) -> None:
        for prime in subject.CONTROL_PRIMES:
            generator = subject.primitive_root(prime)
            dimension = (prime - 1) // 2
            for cores in (
                (),
                (1,),
                tuple(sorted({1, generator})),
                tuple(range(1, prime)),
            ):
                row = subject.incidence_pushforward_spectrum(prime, cores)
                core_size = len(cores)
                self.assertEqual(row["domain_dimension"], dimension * core_size)
                self.assertEqual(row["rank"], dimension if core_size else 0)
                self.assertEqual(
                    row["kernel_dimension"], dimension * max(core_size - 1, 0)
                )
                self.assertEqual(
                    row["row_gram"],
                    [
                        [
                            core_size if left == right else 0
                            for right in range(dimension)
                        ]
                        for left in range(dimension)
                    ],
                )
                expected_spectrum = (
                    [{"value": core_size, "multiplicity": dimension}]
                    if core_size
                    else []
                )
                self.assertEqual(
                    row["nonzero_squared_singular_values"], expected_spectrum
                )

    def test_rank_kernel_and_exact_cyclotomic_certificate(self) -> None:
        for prime in subject.CONTROL_PRIMES:
            generator = subject.primitive_root(prime)
            dimension = (prime - 1) // 2
            transversal = tuple(
                pow(generator, index, prime) for index in range(dimension)
            )

            zero = subject.core_spectrum(prime, ())
            self.assertEqual(zero["rank"], 0)
            self.assertEqual(zero["kernel_dimension"], dimension)

            singleton = subject.core_spectrum(prime, (1,))
            self.assertEqual(singleton["rank"], dimension)
            self.assertEqual(singleton["kernel_dimension"], 0)

            sign_complete = subject.core_spectrum(prime, transversal)
            self.assertEqual(sign_complete["rank"], 1)
            self.assertEqual(sign_complete["kernel_dimension"], dimension - 1)

            all_units = subject.core_spectrum(prime, range(1, prime))
            self.assertEqual(all_units["rank"], 1)
            self.assertEqual(all_units["kernel_dimension"], dimension - 1)

            antipodal = subject.core_spectrum(prime, (1, prime - 1))
            self.assertEqual(antipodal["rank"], dimension)
            self.assertEqual(antipodal["kernel_dimension"], 0)

            for row in (zero, singleton, sign_complete, all_units, antipodal):
                self.assertEqual(
                    row["rank"] + row["kernel_dimension"], row["dimension"]
                )
                self.assertEqual(
                    row["kernel_modes"],
                    [
                        mode
                        for mode in range(dimension)
                        if subject.mode_is_zero(row["folded_sign_pair_counts"], mode)
                    ],
                )

    def test_even_characters_are_root_characters_modulo_quadratic_twist(self) -> None:
        for prime in subject.CONTROL_PRIMES:
            order = prime - 1
            dimension = order // 2
            squared_exponents = set()
            for mode in range(dimension):
                first_root = mode
                quadratic_twist = mode + dimension
                self.assertEqual(2 * first_root % order, 2 * quadratic_twist % order)
                even_exponent = 2 * mode % order
                # theta(-1)=exp(pi*i*even_exponent)=1, encoded by even exponent.
                self.assertEqual(even_exponent % 2, 0)
                squared_exponents.add(even_exponent)
            self.assertEqual(len(squared_exponents), dimension)

    def test_parseval_and_antipodal_pair_identity(self) -> None:
        for prime in subject.CONTROL_PRIMES:
            generator = subject.primitive_root(prime)
            samples = (
                (1,),
                (1, prime - 1),
                tuple(sorted({1, generator})),
                tuple(range(1, prime)),
            )
            for cores in samples:
                row = subject.core_spectrum(prime, cores)
                parseval = row["parseval"]
                counts = row["folded_sign_pair_counts"]
                self.assertEqual(
                    parseval["sum_folded_counts_squared"],
                    len(cores) + 2 * parseval["complete_antipodal_pairs"],
                )
                self.assertEqual(
                    parseval["sum_squared_singular_values"],
                    row["dimension"] * sum(value * value for value in counts),
                )
                self.assertEqual(
                    parseval["nonconstant_mode_squared_mass"],
                    parseval["sum_squared_singular_values"] - len(cores) ** 2,
                )
                self.assertGreaterEqual(parseval["nonconstant_mode_squared_mass"], 0)
                self.assertEqual(row["operator_norm"], len(cores))

    def test_arbitrary_declared_subsets_match_exact_matrix_rank(self) -> None:
        # A bounded deterministic selection, not an exhaustive subset sweep.
        samples = {
            3: ((1,), (2,), (1, 2)),
            5: ((1, 2), (1, 4), (2, 3, 4)),
            7: ((1, 2, 4), (1, 3, 6), (2, 3, 4, 5)),
            11: ((1, 2, 7), (1, 3, 4, 5), (2, 6, 7, 8, 10)),
        }
        for prime, core_sets in samples.items():
            for cores in core_sets:
                row = subject.core_spectrum(prime, cores)
                self.assertEqual(
                    row["rank"], subject._matrix_rank(row["transfer_matrix"])
                )

    def test_owner_incompleteness_is_exactly_the_nontrivial_fourier_defect(
        self,
    ) -> None:
        for prime in subject.CONTROL_PRIMES:
            owners = subject.owner_coset(prime)
            cores = tuple(sorted({1, subject.primitive_root(prime)}))

            complete = subject.owner_incompleteness_defect(prime, cores, owners)
            self.assertEqual(
                complete["density_subtracted_defect_hilbert_schmidt_squared"],
                [0, 1],
            )
            self.assertEqual(
                complete["owner_fourier_parseval"]["nonconstant_mode_squared_mass"],
                0,
            )

            if len(owners) > 1:
                incomplete = subject.owner_incompleteness_defect(
                    prime, cores, owners[:-1]
                )
                numerator, denominator = incomplete[
                    "density_subtracted_defect_hilbert_schmidt_squared"
                ]
                self.assertGreater(Fraction(numerator, denominator), 0)
                self.assertGreater(
                    incomplete["owner_fourier_parseval"][
                        "nonconstant_mode_squared_mass"
                    ],
                    0,
                )
                self.assertTrue(
                    any(
                        not row["is_zero"]
                        for row in incomplete["owner_fourier_coefficients"]
                        if row["frequency"] != 0
                    )
                )

    def test_hybrid_principal_leverage_is_core_invariant(self) -> None:
        for prime in subject.CONTROL_PRIMES:
            generator = subject.primitive_root(prime)
            for cores in ((1,), tuple(sorted({1, generator})), tuple(range(1, prime))):
                self.assertEqual(
                    subject.phase_principal_leverage_after_transfer(prime, cores),
                    Fraction(prime - 1, prime + 1),
                )
        pairs = ((3, (1,)), (5, (1, 2)))
        self.assertEqual(
            subject.hybrid_positive_block_leverage_squared(pairs, (1, 1)),
            Fraction(7, 6),
        )
        self.assertEqual(subject.hybrid_tensor_leverage_squared(pairs), Fraction(1, 3))

    def test_fixture_provenance_caps_and_no_floats(self) -> None:
        locked = json.loads(subject.OUTPUT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(locked, self.fixture)
        self.assertEqual(locked["source_frontier"]["commit"], subject.SOURCE_COMMIT_751)
        self.assertEqual(
            locked["source_frontier"]["git_blob_ids"], subject.SOURCE_BLOBS_751
        )
        self.assertEqual(
            locked["source_frontier"]["adapter_dependencies_sha256_lf"],
            subject.ADAPTER_DEPENDENCIES_SHA256_LF,
        )
        self.assertLessEqual(
            locked["scope"]["source_atoms_used"],
            locked["scope"]["source_atom_cap"],
        )
        subject._assert_no_float(locked)

        provenance = locked["provenance"]
        for label, path in (
            ("producer_sha256_lf", Path(subject.__file__)),
            ("note_sha256_lf", subject.NOTE_PATH),
            ("test_sha256_lf", Path(__file__)),
        ):
            normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            self.assertEqual(provenance[label], hashlib.sha256(normalized).hexdigest())

    def test_fail_closed_domains(self) -> None:
        with self.assertRaises(ValueError):
            subject.core_spectrum(13, (1,))
        with self.assertRaises(ValueError):
            subject.core_spectrum(7, (0,))
        with self.assertRaises(ValueError):
            subject.core_spectrum(7, (1, 8))
        with self.assertRaises(ValueError):
            subject.owner_incompleteness_defect(7, (1,), (3,))
        with self.assertRaises(ValueError):
            subject.phase_principal_leverage_after_transfer(7, ())
        with self.assertRaises(ValueError):
            subject.hybrid_positive_block_leverage_squared(((3, (1,)),), ())
        with self.assertRaises(ValueError):
            subject.hybrid_tensor_leverage_squared(())
        with self.assertRaises(TypeError):
            subject._assert_no_float({"forbidden": 0.5})


if __name__ == "__main__":
    unittest.main()

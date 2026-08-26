#!/usr/bin/env python3
"""Exact finite Kummer-transfer spectrum for the corrected FFPS coordinate.

The only enumerated controls are p=3,5,7,11.  The proof recorded in the
companion note is algebraic for every odd prime, but this producer deliberately
does not sweep conductors, core ranges, polynomial families, or zero sets.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections.abc import Iterable, Sequence
from fractions import Fraction
from functools import cache
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "ffps_kummer_transfer_spectrum.json"
NOTE_PATH = HERE / "FFPS_KUMMER_TRANSFER_SPECTRUM.md"
TEST_PATH = ROOT / "tests" / "test_ffps_kummer_transfer_spectrum.py"

SOURCE_COMMIT_751 = "37d9df4b9b4fb9a8277de6ec1f77278dbbe5b0f2"
SOURCE_BLOBS_751 = {
    "T-106121": "55afc90eaf7d2cd3efa102bcc97b927943731d48",
    "L-106024": "d94787dc2cd1cedd74d33ddc6269daf8de1cc061",
    "R-106122": "dc51ae3add697ab4cec868ef8439f864ce77d71a",
    "R-106123": "f89cad68d67444280088d8bea7cbfb7c1eacc90d",
    "L-106126": "b4dbebde403a11696c56a4689b2df8b53326a157",
}
ADAPTER_DEPENDENCIES_SHA256_LF = {
    "research/l-families/atlas/function_field/FFPS_PHYSICAL_SQUARECLASS_ADAPTER.md": "6b3a0958422f01b44b7702b1088f4e13926d5d11a7725bde2582cd2d371b07e6",
    "research/l-families/atlas/function_field/ffps_principal_leverage.py": "fb5804df87ca36b74299de004f83b1fcd79ae7ffb36fc1f45484bff5efaae7e3",
    "research/l-families/atlas/function_field/ffps_principal_leverage.json": "cdf514d8f8b76b7d2569ea6852c8f4dcc8590c0ad72822d3bee711711cfd3ee3",
    "tests/test_ffps_principal_leverage.py": "ce253f44333ef44f2b7ca08ad3190231f093f8c9bffbb0535f1640949dfa3ad8",
}

CONTROL_PRIMES = (3, 5, 7, 11)
MAX_SOURCE_ATOMS = 4_096


def _sha256_lf(path: Path) -> str:
    data = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(data).hexdigest()


def _assert_adapter_dependencies() -> None:
    for relative, expected in ADAPTER_DEPENDENCIES_SHA256_LF.items():
        path = ROOT / relative
        if not path.is_file() or _sha256_lf(path) != expected:
            raise RuntimeError(f"locked FFPS adapter dependency drifted: {relative}")


def _validate_control_prime(prime: int) -> None:
    if prime not in CONTROL_PRIMES:
        raise ValueError(f"exact controls are locked to p in {CONTROL_PRIMES}")


def primitive_root(prime: int) -> int:
    _validate_control_prime(prime)
    order = prime - 1
    prime_divisors = {
        divisor
        for divisor in range(2, order + 1)
        if order % divisor == 0
        and all(divisor % smaller for smaller in range(2, math.isqrt(divisor) + 1))
    }
    for candidate in range(2, prime):
        if all(
            pow(candidate, order // divisor, prime) != 1 for divisor in prime_divisors
        ):
            return candidate
    raise ArithmeticError("primitive root search failed")


def _unit_log_table(prime: int) -> dict[int, int]:
    generator = primitive_root(prime)
    return {pow(generator, exponent, prime): exponent for exponent in range(prime - 1)}


def _normalize_cores(prime: int, cores: Iterable[int]) -> tuple[int, ...]:
    _validate_control_prime(prime)
    normalized = tuple(value % prime for value in cores)
    if any(value == 0 for value in normalized):
        raise ValueError("declared cores must be units modulo p")
    if len(set(normalized)) != len(normalized):
        raise ValueError("declared core subset cannot contain duplicate residues")
    return tuple(sorted(normalized))


def owner_coset(prime: int, representative: int = 1) -> tuple[int, ...]:
    _validate_control_prime(prime)
    representative %= prime
    if representative == 0:
        raise ValueError("owner-coset representative must be a unit")
    generator = primitive_root(prime)
    half = (prime - 1) // 2
    square_generator = generator * generator % prime
    return tuple(
        representative * pow(square_generator, index, prime) % prime
        for index in range(half)
    )


def folded_core_counts(prime: int, cores: Iterable[int]) -> tuple[int, ...]:
    """Return beta_j=#(C intersect {g^j,-g^j}), j modulo (p-1)/2."""

    normalized = _normalize_cores(prime, cores)
    logarithm = _unit_log_table(prime)
    half = (prime - 1) // 2
    counts = [0] * half
    for core in normalized:
        counts[logarithm[core] % half] += 1
    if any(value not in (0, 1, 2) for value in counts):
        raise ArithmeticError("a sign pair acquired an impossible occupancy")
    return tuple(counts)


def transfer_matrix(
    prime: int, cores: Iterable[int], representative: int = 1
) -> tuple[tuple[int, ...], ...]:
    """Matrix of T_C f(x)=sum_(c in C) f(x*c^-2) on one owner coset."""

    counts = folded_core_counts(prime, cores)
    half = len(counts)
    owner_coset(prime, representative)
    return tuple(
        tuple(counts[(row - column) % half] for column in range(half))
        for row in range(half)
    )


def direct_transfer_matrix(
    prime: int, cores: Iterable[int], representative: int = 1
) -> tuple[tuple[int, ...], ...]:
    """Direct map-count construction, kept as an independent tiny control."""

    normalized = _normalize_cores(prime, cores)
    owners = owner_coset(prime, representative)
    return tuple(
        tuple(
            sum(1 for core in normalized if owner * core * core % prime == physical)
            for owner in owners
        )
        for physical in owners
    )


def incidence_pushforward_matrix(
    prime: int, cores: Iterable[int], representative: int = 1
) -> tuple[tuple[int, ...], ...]:
    """Matrix of K_C: l2(Omega x C)->l2(Omega), (P,c)->P*c^2."""

    normalized = _normalize_cores(prime, cores)
    owners = owner_coset(prime, representative)
    columns = tuple((owner, core) for core in normalized for owner in owners)
    return tuple(
        tuple(
            1 if owner * core * core % prime == physical else 0
            for owner, core in columns
        )
        for physical in owners
    )


def incidence_pushforward_spectrum(
    prime: int, cores: Iterable[int], representative: int = 1
) -> dict[str, object]:
    """Exact rectangular singular spectrum, rank, and kernel dimension."""

    normalized = _normalize_cores(prime, cores)
    matrix = incidence_pushforward_matrix(prime, normalized, representative)
    dimension = (prime - 1) // 2
    core_size = len(normalized)
    row_gram = tuple(
        tuple(
            sum(
                matrix[row][column] * matrix[other][column]
                for column in range(dimension * core_size)
            )
            for other in range(dimension)
        )
        for row in range(dimension)
    )
    expected = tuple(
        tuple(core_size if row == column else 0 for column in range(dimension))
        for row in range(dimension)
    )
    if row_gram != expected:
        raise ArithmeticError("incidence pushforward ceased to be a scaled coisometry")
    rank = dimension if core_size else 0
    if _matrix_rank(matrix) != rank:
        raise ArithmeticError("incidence pushforward rank drifted")
    return {
        "domain_dimension": dimension * core_size,
        "codomain_dimension": dimension,
        "rank": rank,
        "kernel_dimension": dimension * max(core_size - 1, 0),
        "nonzero_squared_singular_values": (
            [{"value": core_size, "multiplicity": dimension}] if core_size else []
        ),
        "row_gram": [list(row) for row in row_gram],
        "identity": "K_C*K_C^*=|C|*I; normalized K_C is a coisometry",
        "kernel": (
            "for each physical x, source amplitudes on the |C| preimages "
            "sum to zero independently"
        ),
    }


def _trim(polynomial: Sequence[Fraction | int]) -> tuple[Fraction, ...]:
    values = [Fraction(value) for value in polynomial]
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values or [Fraction(0)])


def _poly_divmod(
    numerator: Sequence[Fraction | int], denominator: Sequence[Fraction | int]
) -> tuple[tuple[Fraction, ...], tuple[Fraction, ...]]:
    top = list(_trim(numerator))
    bottom = _trim(denominator)
    if bottom == (0,):
        raise ZeroDivisionError("zero polynomial divisor")
    quotient = [Fraction(0)] * max(1, len(top) - len(bottom) + 1)
    while len(top) >= len(bottom) and any(top):
        shift = len(top) - len(bottom)
        factor = top[-1] / bottom[-1]
        quotient[shift] += factor
        for index, value in enumerate(bottom):
            top[index + shift] -= factor * value
        top = list(_trim(top))
    return _trim(quotient), _trim(top)


def _monic_gcd(
    left: Sequence[Fraction | int], right: Sequence[Fraction | int]
) -> tuple[Fraction, ...]:
    a = _trim(left)
    b = _trim(right)
    while b != (0,):
        _, remainder = _poly_divmod(a, b)
        a, b = b, remainder
    if a == (0,):
        return a
    return tuple(value / a[-1] for value in a)


def _integer_coefficients(polynomial: Sequence[Fraction | int]) -> list[int]:
    values = _trim(polynomial)
    if any(value.denominator != 1 for value in values):
        raise ArithmeticError("expected an integral polynomial")
    return [value.numerator for value in values]


def _x_power_minus_one(power: int) -> tuple[int, ...]:
    if power < 1:
        raise ValueError("positive polynomial order required")
    return (-1,) + (0,) * (power - 1) + (1,)


@cache
def cyclotomic_polynomial(order: int) -> tuple[int, ...]:
    if order < 1:
        raise ValueError("cyclotomic order must be positive")
    polynomial: tuple[Fraction, ...] = tuple(
        Fraction(value) for value in _x_power_minus_one(order)
    )
    for divisor in range(1, order):
        if order % divisor == 0:
            quotient, remainder = _poly_divmod(
                polynomial, cyclotomic_polynomial(divisor)
            )
            if remainder != (0,):
                raise ArithmeticError("cyclotomic recurrence ceased to divide exactly")
            polynomial = quotient
    return tuple(_integer_coefficients(polynomial))


def _mode_root_order(mode: int, dimension: int) -> int:
    return 1 if mode % dimension == 0 else dimension // math.gcd(mode, dimension)


def mode_is_zero(folded_counts: Sequence[int], mode: int) -> bool:
    dimension = len(folded_counts)
    if dimension < 1 or not 0 <= mode < dimension:
        raise ValueError("Fourier mode outside the folded core dimension")
    cyclotomic = cyclotomic_polynomial(_mode_root_order(mode, dimension))
    _, remainder = _poly_divmod(folded_counts, cyclotomic)
    return remainder == (0,)


def cyclic_autocorrelation(vector: Sequence[int]) -> tuple[int, ...]:
    dimension = len(vector)
    if dimension < 1:
        raise ValueError("nonempty cyclic vector required")
    return tuple(
        sum(
            vector[index] * vector[(index + shift) % dimension]
            for index in range(dimension)
        )
        for shift in range(dimension)
    )


def _matrix_rank(matrix: Sequence[Sequence[int | Fraction]]) -> int:
    if not matrix:
        return 0
    rows = [list(map(Fraction, row)) for row in matrix]
    column_count = len(rows[0])
    if any(len(row) != column_count for row in rows):
        raise ValueError("ragged matrix")
    rank = 0
    for column in range(column_count):
        pivot = next((row for row in range(rank, len(rows)) if rows[row][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        pivot_value = rows[rank][column]
        rows[rank] = [value / pivot_value for value in rows[rank]]
        for row in range(len(rows)):
            if row != rank and rows[row][column]:
                factor = rows[row][column]
                rows[row] = [
                    value - factor * pivot_entry
                    for value, pivot_entry in zip(rows[row], rows[rank])
                ]
        rank += 1
        if rank == len(rows):
            break
    return rank


def _fraction_pair(value: Fraction | int) -> list[int]:
    fraction = Fraction(value)
    return [fraction.numerator, fraction.denominator]


def core_spectrum(prime: int, cores: Iterable[int]) -> dict[str, object]:
    normalized = _normalize_cores(prime, cores)
    counts = folded_core_counts(prime, normalized)
    dimension = len(counts)
    modulus = _x_power_minus_one(dimension)
    gcd_polynomial = _monic_gcd(counts, modulus)
    kernel_dimension = len(gcd_polynomial) - 1
    zero_modes = [mode for mode in range(dimension) if mode_is_zero(counts, mode)]
    if len(zero_modes) != kernel_dimension:
        raise ArithmeticError("Fourier zero modes disagree with polynomial gcd")
    matrix = transfer_matrix(prime, normalized)
    rank = dimension - kernel_dimension
    if _matrix_rank(matrix) != rank or matrix != direct_transfer_matrix(
        prime, normalized
    ):
        raise ArithmeticError("direct Kummer transfer disagrees with the Fourier rank")

    autocorrelation = cyclic_autocorrelation(counts)
    core_size = len(normalized)
    antipodal_pairs = sum(
        1
        for core in normalized
        if core < (-core % prime) and (-core % prime) in normalized
    )
    parseval_energy = dimension * sum(value * value for value in counts)
    if parseval_energy != dimension * (core_size + 2 * antipodal_pairs):
        raise ArithmeticError("antipodal-pair Parseval identity failed")

    modes = []
    for mode in range(dimension):
        modes.append(
            {
                "mode": mode,
                "root_character_class_exponents_mod_p_minus_1": [
                    mode,
                    mode + dimension,
                ],
                "even_character_exponent_mod_p_minus_1": 2 * mode,
                "even_character_order": _mode_root_order(mode, dimension),
                "multiplier": {
                    "integer_coefficients": list(counts),
                    "evaluate_at": {
                        "root": f"zeta_{dimension}",
                        "exponent": (-mode) % dimension,
                    },
                },
                "squared_singular_value": {
                    "integer_cyclic_autocorrelation_coefficients": list(
                        autocorrelation
                    ),
                    "evaluate_at": {
                        "root": f"zeta_{dimension}",
                        "exponent": mode,
                    },
                },
                "is_kernel_mode": mode in zero_modes,
            }
        )

    return {
        "prime": prime,
        "primitive_root": primitive_root(prime),
        "owner_coset_representative": 1,
        "owner_coset": list(owner_coset(prime)),
        "declared_cores": list(normalized),
        "folded_sign_pair_counts": list(counts),
        "folded_polynomial_coefficients": list(counts),
        "gcd_with_x_to_m_minus_1_coefficients": _integer_coefficients(gcd_polynomial),
        "dimension": dimension,
        "rank": rank,
        "kernel_dimension": kernel_dimension,
        "kernel_modes": zero_modes,
        "operator_norm": core_size,
        "constant_mode_multiplier": core_size,
        "full_incidence_pushforward": incidence_pushforward_spectrum(prime, normalized),
        "fourier_modes": modes,
        "parseval": {
            "sum_squared_singular_values": parseval_energy,
            "constant_mode_squared": core_size * core_size,
            "nonconstant_mode_squared_mass": parseval_energy - core_size * core_size,
            "sum_folded_counts_squared": sum(value * value for value in counts),
            "complete_antipodal_pairs": antipodal_pairs,
            "identity": "sum(beta_j^2)=|C|+2*#{complete antipodal pairs}",
        },
        "transfer_matrix": [list(row) for row in matrix],
    }


def _owner_mask(
    prime: int, owners: Iterable[int], representative: int = 1
) -> tuple[int, ...]:
    orbit = owner_coset(prime, representative)
    position = {owner: index for index, owner in enumerate(orbit)}
    normalized = tuple(value % prime for value in owners)
    if any(value not in position for value in normalized):
        raise ValueError("owner subset must lie in the declared quadratic-class coset")
    if len(set(normalized)) != len(normalized):
        raise ValueError("owner subset cannot contain duplicate residues")
    selected = set(normalized)
    return tuple(1 if owner in selected else 0 for owner in orbit)


def owner_incompleteness_defect(
    prime: int,
    cores: Iterable[int],
    owners: Iterable[int],
    representative: int = 1,
) -> dict[str, object]:
    normalized_cores = _normalize_cores(prime, cores)
    counts = folded_core_counts(prime, normalized_cores)
    mask = _owner_mask(prime, owners, representative)
    dimension = len(mask)
    owner_count = sum(mask)
    density = Fraction(owner_count, dimension)
    matrix = transfer_matrix(prime, normalized_cores, representative)
    defect_matrix = tuple(
        tuple(
            Fraction(matrix[row][column]) * (mask[column] - density)
            for column in range(dimension)
        )
        for row in range(dimension)
    )
    direct_hilbert_schmidt = sum(
        (value * value for row in defect_matrix for value in row), Fraction(0)
    )
    formula_hilbert_schmidt = Fraction(
        sum(value * value for value in counts)
        * owner_count
        * (dimension - owner_count),
        dimension,
    )
    if direct_hilbert_schmidt != formula_hilbert_schmidt:
        raise ArithmeticError("owner Fourier defect identity failed")

    owner_fourier_energy = dimension * owner_count
    owner_nonconstant_energy = owner_fourier_energy - owner_count * owner_count
    return {
        "prime": prime,
        "declared_cores": list(normalized_cores),
        "owner_coset_representative": representative % prime,
        "owner_mask_in_coset_order": list(mask),
        "owner_count": owner_count,
        "owner_density": _fraction_pair(density),
        "owner_fourier_coefficients": [
            {
                "frequency": frequency,
                "integer_coefficients": list(mask),
                "evaluate_at": {
                    "root": f"zeta_{dimension}",
                    "exponent": frequency,
                },
                "is_zero": mode_is_zero(mask, frequency),
            }
            for frequency in range(dimension)
        ],
        "mode_mixing_formula": (
            "<e_t,T_C M_A e_s>=lambda_t*ahat_A(s-t)/m; "
            "the density-subtracted defect deletes s=t and retains exactly "
            "the nonzero owner Fourier frequencies"
        ),
        "owner_fourier_parseval": {
            "all_mode_squared_mass": owner_fourier_energy,
            "constant_mode_squared": owner_count * owner_count,
            "nonconstant_mode_squared_mass": owner_nonconstant_energy,
        },
        "density_subtracted_defect_hilbert_schmidt_squared": _fraction_pair(
            direct_hilbert_schmidt
        ),
        "defect_formula": ("||T_C(M_A-|A|/m)||_HS^2=(sum_j beta_j^2)*|A|*(m-|A|)/m"),
        "operator_norm_upper_bound": len(normalized_cores),
    }


def phase_principal_leverage_after_transfer(
    prime: int, cores: Iterable[int]
) -> Fraction:
    normalized = _normalize_cores(prime, cores)
    if not normalized:
        raise ValueError("zero transfer has no principal leverage")
    # T_C fixes the constant line with multiplier |C|.  The phase Gram pI-J
    # has eigenvalue (p+1)/2 there, and the principal observation kills every
    # nonconstant Fourier line.
    return Fraction(prime - 1, prime + 1)


def hybrid_positive_block_leverage_squared(
    prime_core_pairs: Sequence[tuple[int, Sequence[int]]],
    weights: Sequence[Fraction | int],
) -> Fraction:
    if not prime_core_pairs or len(prime_core_pairs) != len(weights):
        raise ValueError("hybrid block needs equally sized nonempty inputs")
    return sum(
        (
            Fraction(weight) ** 2
            * phase_principal_leverage_after_transfer(prime, cores)
            for (prime, cores), weight in zip(prime_core_pairs, weights)
        ),
        Fraction(0),
    )


def hybrid_tensor_leverage_squared(
    prime_core_pairs: Sequence[tuple[int, Sequence[int]]],
) -> Fraction:
    if not prime_core_pairs:
        raise ValueError("hybrid tensor needs at least one local factor")
    value = Fraction(1)
    for prime, cores in prime_core_pairs:
        value *= phase_principal_leverage_after_transfer(prime, cores)
    return value


def _assert_no_float(value: object) -> None:
    if isinstance(value, float):
        raise TypeError("claim payload refuses floating-point values")
    if isinstance(value, dict):
        for key, nested in value.items():
            _assert_no_float(key)
            _assert_no_float(nested)
    elif isinstance(value, (list, tuple)):
        for nested in value:
            _assert_no_float(nested)


def build_fixture() -> dict[str, object]:
    _assert_adapter_dependencies()
    controls = []
    source_atoms = 0
    for prime in CONTROL_PRIMES:
        generator = primitive_root(prime)
        dimension = (prime - 1) // 2
        core_sets = {
            "singleton": (1,),
            "two_core": tuple(sorted({1, generator})),
            "sign_transversal": tuple(
                sorted(pow(generator, index, prime) for index in range(dimension))
            ),
            "complete_units": tuple(range(1, prime)),
        }
        rows = {}
        for label, cores in core_sets.items():
            row = core_spectrum(prime, cores)
            rows[label] = row
            source_atoms += (prime - 1) * len(cores)
        incomplete_owners = owner_coset(prime)[:-1]
        defect = owner_incompleteness_defect(
            prime, core_sets["two_core"], incomplete_owners
        )
        source_atoms += len(incomplete_owners) * len(core_sets["two_core"])
        controls.append(
            {
                "prime": prime,
                "spectra": rows,
                "owner_incompleteness_control": defect,
            }
        )
    if source_atoms > MAX_SOURCE_ATOMS:
        raise ArithmeticError("finite Kummer controls exceeded the source-atom cap")

    block = hybrid_positive_block_leverage_squared(((3, (1,)), (5, (1, 2))), (1, 1))
    tensor = hybrid_tensor_leverage_squared(((3, (1,)), (5, (1, 2))))
    if block != Fraction(7, 6) or tensor != Fraction(1, 3):
        raise ArithmeticError("hybrid leverage controls drifted")

    fixture: dict[str, object] = {
        "schema": "riemann.function_field.ffps_kummer_transfer_spectrum.v1",
        "status": "EXACT_LOCAL_KUMMER_TRANSFER_SPECTRUM_AND_OWNER_DEFECT",
        "source_frontier": {
            "pr": 751,
            "commit": SOURCE_COMMIT_751,
            "live_target": "T-106121 / FFPS106121",
            "git_blob_ids": SOURCE_BLOBS_751,
            "adapter_dependencies_sha256_lf": ADAPTER_DEPENDENCIES_SHA256_LF,
        },
        "operator_theorem": {
            "full_incidence_operator": (
                "K_C F(x)=sum_(c in C) F(x*c^-2,c) from Omega*C to Omega"
            ),
            "full_incidence_spectrum": (
                "K_C*K_C^*=|C|I; rank m and kernel dimension m(|C|-1) for nonempty C"
            ),
            "shared_owner_operator": (
                "T_C f(x)=sum_(c in C) f(x*c^-2)=K_C D_C f on Omega=a*(F_p^*)^2"
            ),
            "folded_counts": "beta_j=1_C(g^j)+1_C(-g^j), 0<=j<(p-1)/2",
            "fourier_multiplier": "lambda_t=sum_j beta_j*zeta_m^(-t*j)=sum_(c in C) psi_t(c)^(-2)",
            "even_mode_bijection": (
                "root characters modulo the quadratic character map bijectively "
                "under squaring to even characters; t maps to exponent 2t"
            ),
            "rank": "m-degree(gcd(B_C(X),X^m-1))",
            "kernel": "span of exactly those owner Fourier modes t with B_C(zeta_m^-t)=0",
            "operator_norm_for_subsets": (
                "|C|, always attained on the constant mode; other modes may tie"
            ),
            "nonconstant_spectral_mass": (
                "m*sum_j(beta_j^2)-|C|^2; it is zero exactly when beta is constant"
            ),
            "interpretation": (
                "core variation can create nonconstant rank but cannot improve the "
                "top local norm; complete sign-pair occupancy collapses to rank one"
            ),
        },
        "owner_incompleteness_theorem": {
            "fourier_matrix": "<e_t,T_C M_A e_s>=lambda_t*ahat_A(s-t)/m",
            "density_subtracted_defect": (
                "||T_C(M_A-|A|/m)||_HS^2=(sum_j beta_j^2)*|A|*(m-|A|)/m"
            ),
            "meaning": (
                "a complete owner coset is exactly Fourier diagonal; an incomplete "
                "owner set mixes modes through, and only through, its nontrivial "
                "multiplicative Fourier coefficients"
            ),
        },
        "hybrid_leverage_corollary": {
            "local_squared_leverage_after_any_nonempty_core_transfer": "(p-1)/(p+1)",
            "reason": (
                "the constant mode survives with multiplier |C| and the principal "
                "observation kills every nonconstant mode"
            ),
            "positive_block_primes_3_5": _fraction_pair(block),
            "coherent_tensor_primes_3_5": _fraction_pair(tensor),
            "consequence": (
                "core variation alone neither improves the local principal contraction "
                "nor repairs positive conductor-fibre assembly"
            ),
        },
        "prime_field_controls": controls,
        "scope": {
            "odd_prime_theorem": True,
            "enumerated_control_primes": list(CONTROL_PRIMES),
            "source_atoms_used": source_atoms,
            "source_atom_cap": MAX_SOURCE_ATOMS,
            "varying_conductor_moment_proved": False,
            "mixed_or_double_ffps_moment_proved": False,
            "number_field_export_proved": False,
            "rh_or_grh_proved": False,
        },
        "provenance": {
            "producer_sha256_lf": _sha256_lf(Path(__file__)),
            "note_sha256_lf": _sha256_lf(NOTE_PATH),
            "test_sha256_lf": _sha256_lf(TEST_PATH),
        },
    }
    _assert_no_float(fixture)
    return fixture


def _canonical(value: object) -> str:
    return json.dumps(value, indent=2, sort_keys=True) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--stdout", action="store_true")
    args = parser.parse_args()
    rendered = _canonical(build_fixture())
    if args.check:
        if (
            not OUTPUT_PATH.is_file()
            or OUTPUT_PATH.read_text(encoding="utf-8") != rendered
        ):
            raise SystemExit("FFPS Kummer transfer spectrum fixture drifted")
        print("PASS_FFPS_KUMMER_TRANSFER_SPECTRUM")
        return
    if args.stdout:
        print(rendered, end="")
        return
    OUTPUT_PATH.write_text(rendered, encoding="utf-8", newline="\n")
    print(f"wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

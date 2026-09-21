"""Adversarial unit tests for X-0001.

These tests detect implementation regressions; they do not turn mpmath output
into a rigorous interval certificate.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import mpmath as mp
import pytest

MODULE_PATH = Path(__file__).with_name("run.py")
SPEC = importlib.util.spec_from_file_location("x0001_run", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
run = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = run
SPEC.loader.exec_module(run)


def test_prime_powers_are_exact_and_sorted() -> None:
    assert run.prime_powers_up_to(13) == [
        (2, 2),
        (3, 3),
        (4, 2),
        (5, 5),
        (7, 7),
        (8, 2),
        (9, 3),
        (11, 11),
        (13, 13),
    ]


def test_geometric_tail_contracts_with_more_precision() -> None:
    with mp.workdps(80):
        L = mp.log(13)
        *_, loose = run.geometric_sums(3, L, target=mp.mpf("1e-30"))
        *_, tight = run.geometric_sums(3, L, target=mp.mpf("1e-60"))
        assert tight.terms > loose.terms
        assert tight.maximum <= mp.mpf("1e-60")


def test_matrix_is_exactly_symmetric_by_construction() -> None:
    A, metadata = run.build_cutoff_free_matrix(5, 3, dps=50)
    assert A.rows == A.cols == 7
    assert metadata["dimension"] == 7
    assert run.symmetry_error(A) == 0


def test_even_projector_is_orthonormal() -> None:
    with mp.workdps(50):
        V = run.even_projector(4)
        error = run.matrix_max_abs(V.T * V - mp.eye(5))
        assert error < mp.mpf("1e-45")


def test_parity_commutation() -> None:
    """Q[-m,-n] = Q[m,n], the finite real-even symmetry."""

    A, _ = run.build_cutoff_free_matrix(7, 4, dps=60)
    dim = A.rows
    error = max(
        abs(A[i, j] - A[dim - 1 - i, dim - 1 - j])
        for i in range(dim)
        for j in range(dim)
    )
    assert error < mp.mpf("1e-50")


def test_eigenpair_residual_is_small() -> None:
    with mp.workdps(70):
        A, _ = run.build_cutoff_free_matrix(3, 3, dps=70)
        lam, _, v = run.smallest_even_eigenpair(A)
        residual = run.vector_inf_norm(A * v - lam * v)
        assert residual < mp.mpf("1e-55")


def test_input_validation() -> None:
    with pytest.raises(ValueError):
        run.build_cutoff_free_matrix(1, 2, dps=50)
    with pytest.raises(ValueError):
        run.build_cutoff_free_matrix(2, 0, dps=50)
    with pytest.raises(ValueError):
        run.build_cutoff_free_matrix(2, 2, dps=20)


def test_decimal_cutoff_changes_log_continuously_but_prime_set_discretely() -> None:
    A, metadata = run.build_cutoff_free_matrix("12.75", 2, dps=50)
    assert A.rows == 5
    assert metadata["c"] == "12.75"
    assert metadata["prime_powers"][-1] == {"q": 11, "p": 11}


def test_binary_float_cutoff_is_rejected() -> None:
    with pytest.raises(TypeError, match="binary float"):
        run.build_cutoff_free_matrix(12.75, 2, dps=50)

"""Exact tests for the dyadic Rayleigh-certificate verifier."""

from __future__ import annotations

import importlib.util
import sys
from fractions import Fraction
from pathlib import Path

import pytest

MODULE_PATH = Path(__file__).with_name("verify_dyadic_certificate.py")
SPEC = importlib.util.spec_from_file_location("x0001_certificate", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
cert = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = cert
SPEC.loader.exec_module(cert)


def certificate(entries: list[dict], vector: list[int], vector_bits: int = 0) -> dict:
    return {
        "schema": cert.SCHEMA,
        "matrix": {"dimension": len(vector), "entries_upper": entries},
        "vector": {"numerators": vector, "scale_bits": vector_bits},
    }


def entry(i: int, j: int, lo: int, hi: int, bits: int = 0) -> dict:
    return {
        "i": i,
        "j": j,
        "lower_num": lo,
        "upper_num": hi,
        "scale_bits": bits,
    }


def test_strict_negative_certificate_passes() -> None:
    data = certificate(
        [
            entry(0, 0, -3, -3),
            entry(0, 1, 0, 0),
            entry(1, 1, 1, 1),
        ],
        [1, 0],
    )
    result = cert.verify(data)
    assert result["certified_negative"] is True
    assert result["rayleigh_interval"]["upper"] == {"numerator": -3, "denominator": 1}


def test_interval_touching_zero_does_not_pass() -> None:
    data = certificate([entry(0, 0, -1, 0)], [1])
    assert cert.verify(data)["certified_negative"] is False


def test_negative_offdiagonal_coefficient_reverses_interval_endpoints() -> None:
    # v=(1,-1), Q00=Q11=0, Q01 in [1,2]: v^TQv=-2Q01 in [-4,-2].
    data = certificate(
        [entry(0, 0, 0, 0), entry(0, 1, 1, 2), entry(1, 1, 0, 0)],
        [1, -1],
    )
    Q, v = cert.parse_certificate(data)
    enclosure = cert.rayleigh_interval(Q, v)
    assert enclosure.lower == Fraction(-4)
    assert enclosure.upper == Fraction(-2)


def test_missing_entry_is_rejected() -> None:
    data = certificate([entry(0, 0, -1, -1), entry(1, 1, -1, -1)], [1, 1])
    with pytest.raises(cert.CertificateError, match="missing"):
        cert.verify(data)


def test_zero_vector_is_rejected() -> None:
    data = certificate([entry(0, 0, -1, -1)], [0])
    with pytest.raises(cert.CertificateError, match="nonzero"):
        cert.verify(data)

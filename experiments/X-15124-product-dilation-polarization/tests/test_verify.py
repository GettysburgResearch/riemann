from fractions import Fraction as F
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("verify", ROOT / "verify.py")
verify = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(verify)


def test_exact_pass():
    result = verify.build_certificate()
    assert result["verdict"] == "CERTIFIED_PRODUCT_DILATION_POLARIZATION"
    assert result["direct_product_form"] == result["grouped_lambda2_form"]
    assert result["direct_product_form"] == result["polarized_channel_form"]
    assert result["orientation_distinct"] is True


def test_lambda2_ledger():
    result = verify.build_certificate()
    assert result["lambda2"] == {
        "2": "1/1",
        "3": "4/1",
        "4": "3/1",
        "6": "4/1",
    }


def test_product_ratio_are_different():
    result = verify.build_certificate()
    assert result["p2_p3_product_value"] == "21/1"
    assert result["p2_p3_ratio_value"] == "14/1"


def test_boolean_is_not_fraction():
    assert isinstance(True, int)
    assert not isinstance(True, F)


def test_cycle_matrix_is_orthogonal():
    P = [
        [F(0), F(0), F(1)],
        [F(1), F(0), F(0)],
        [F(0), F(1), F(0)],
    ]
    identity = verify.matmul(verify.transpose(P), P)
    assert identity == [
        [F(1), F(0), F(0)],
        [F(0), F(1), F(0)],
        [F(0), F(0), F(1)],
    ]


def test_omitting_convolution_changes_form():
    result = verify.build_certificate()
    derivative_only = sum(
        F(row["polarized_value"])
        for row in result["channels"]
        if row["kind"] == "derivative"
    )
    assert derivative_only != F(result["direct_product_form"])


def test_ratio_substitution_fails():
    result = verify.build_certificate()
    assert F(result["p2_p3_ratio_value"]) != F(result["p2_p3_product_value"])


def test_digest_is_stable():
    result = verify.build_certificate()
    assert result["proof_sha256"] == verify.build_certificate()["proof_sha256"]

from pathlib import Path
import importlib.util


def test_replay():
    path = Path(__file__).resolve().parents[1] / "verify.py"
    spec = importlib.util.spec_from_file_location("x105490_verify", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    result = module.main()
    assert result["classification"] == "PASS_T105490_F1_BOUNDED_RESOLVENT"
    assert result["bounded_density_symbol_proved"]
    assert result["dyadic_differential_bridge_proved"]
    assert result["anti_causal_inverse_stable"]
    assert not result["old_unregularized_weight_integrable"]
    assert result["corrected_weight_positive"]
    assert result["corrected_weight_hminus1_scale"]
    assert not result["rh_established"]

import importlib.util
from pathlib import Path
import sys
import mpmath as mp

base = Path(__file__).parent
spec_run = importlib.util.spec_from_file_location("edge_run", base / "run.py")
edge = importlib.util.module_from_spec(spec_run)
sys.modules[spec_run.name] = edge
spec_run.loader.exec_module(edge)

spec_lerch = importlib.util.spec_from_file_location("lerch_resum", base / "lerch_resum.py")
lerch = importlib.util.module_from_spec(spec_lerch)
sys.modules[spec_lerch.name] = lerch
spec_lerch.loader.exec_module(lerch)


def test_lerch_matches_direct_sums():
    with mp.workdps(60):
        for L in [mp.mpf("0.2"), mp.mpf("0.05"), mp.mpf("0.01")]:
            for n in [0, 1, 2, 5]:
                got = lerch.sums_lerch(n, L)
                expected = edge._geometric_sums(n, L, mp.mpf("1e-50"))
                assert max(abs(a - b) for a, b in zip(got, expected)) < mp.mpf("2e-49")


def test_tiny_l_values_are_real_and_finite():
    with mp.workdps(70):
        for L in [mp.mpf("1e-6"), mp.mpf("1e-12")]:
            for n in [0, 1, 2]:
                values = lerch.sums_lerch(n, L)
                assert all(mp.isfinite(value) for value in values)
                assert all(isinstance(value, mp.mpf) for value in values)

"""
Tests for the independent winding-count reimplementation (winding2, Q-0003).

Runnable with pytest or directly:  python3 tests/test_winding2.py

The load-bearing test is the third: on a box whose edge passes within 1e-5 of
a zero ordinate, the two independently written implementations must not
certify DIFFERENT counts.  Abstention is always legal; disagreement never is.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "scripts"))

import certzeta as cz  # noqa: E402
import winding as W1  # noqa: E402
import winding2 as W2  # noqa: E402


def test_counts_first_zeros_and_empty_gap():
    cz.set_prec(300)
    n, ok, _ = W2.count_zeros_rect2("0.02", "0.98", "10", "26")
    assert ok and n == 3, (n, ok)
    n, ok, _ = W2.count_zeros_rect2("0.02", "0.98", "26", "30")
    assert ok and n == 0, (n, ok)


def test_agrees_with_winding1_on_a_lehmer_box():
    cz.set_prec(300)
    c1 = W1.count_zeros_rect("0.05", "0.95", "1977.0", "1977.4")
    n2, ok2, _ = W2.count_zeros_rect2("0.05", "0.95", "1977.0", "1977.4")
    assert c1.ok and ok2
    assert c1.count == n2 == 2, (c1.count, n2)


def test_no_disagreement_on_adversarial_edge():
    """Edge 1e-5 below the first zero ordinate.  Either implementation may
    abstain; two certified answers must be equal."""
    cz.set_prec(300)
    c1 = W1.count_zeros_rect("0.02", "0.98", "10", "14.13473")
    n2, ok2, _ = W2.count_zeros_rect2("0.02", "0.98", "10", "14.13473")
    if c1.ok and ok2:
        assert c1.count == n2, (c1.count, n2)


if __name__ == "__main__":
    fails = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print(f"PASS  {name}")
            except Exception as e:
                fails += 1
                print(f"FAIL  {name}: {type(e).__name__}: {e}")
    print("\nall passed" if not fails else f"\n{fails} FAILURES")
    sys.exit(1 if fails else 0)

"""Shared, CORRECT inertia by symmetric congruence with 1x1 AND hyperbolic 2x2 pivots.

Several scripts in this directory originally used a 1x1-diagonal-pivot-only routine that
'continue's on a zero pivot.  That routine returns (0,0,2) on [[0,1],[1,0]], whose true
inertia is (1,1,0): it cannot see a hyperbolic negative direction.  The defect was found in
the PR #173 second-pass review.  Use THIS routine instead.

Re-running the affected published tables with this routine reproduces them identically
(O-16005's eight sign patterns; L-16004's SCOPE-CAUTION table), so the defect did not change
those conclusions -- but it did invalidate O-16007 sec 5, which is withdrawn.
"""
import mpmath as mp
from mpmath import mpf


def inertia(Q, tol_digits=10):
    """Q: list-of-lists or mpmath matrix, real symmetric.  Returns (n_plus, n_minus, n_zero)."""
    if hasattr(Q, 'rows'):
        n = Q.rows; A = [[Q[i, j] for j in range(n)] for i in range(n)]
    else:
        n = len(Q); A = [[Q[i][j] for j in range(n)] for i in range(n)]
    idx = list(range(n)); pos = neg = zer = 0
    scale = max((abs(A[i][j]) for i in range(n) for j in range(n)), default=mpf(1)) or mpf(1)
    tol = mpf(10) ** (-mp.mp.dps + tol_digits) * scale
    while idx:
        k = next((i for i in idx if abs(A[i][i]) > tol), None)
        if k is None:
            piv = None
            for a in range(len(idx)):
                for b in range(a + 1, len(idx)):
                    if abs(A[idx[a]][idx[b]]) > tol:
                        piv = (idx[a], idx[b]); break
                if piv: break
            if piv is None:
                zer += len(idx); break
            i, j = piv                      # hyperbolic block: e_i -> e_i + e_j
            for r in range(n): A[r][i] = A[r][i] + A[r][j]
            for r in range(n): A[i][r] = A[i][r] + A[j][r]
            continue
        d = A[k][k]
        pos += 1 if d > 0 else 0
        neg += 1 if d < 0 else 0
        rest = [i for i in idx if i != k]
        for i in rest:
            f = A[i][k] / d
            if f != 0:
                for j in rest:
                    A[i][j] = A[i][j] - f * A[k][j]
        idx = rest
    return (pos, neg, zer)


if __name__ == '__main__':
    mp.mp.dps = 40
    print("self-test  [[0,1],[1,0]] ->", inertia([[mpf(0), mpf(1)], [mpf(1), mpf(0)]]),
          " (must be (1, 1, 0))")
    print("self-test  -I_3          ->", inertia([[mpf(-1 if i == j else 0) for j in range(3)]
                                                  for i in range(3)]), " (must be (0, 3, 0))")

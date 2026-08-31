"""Held-out test of the Segre bridge at RANK 3, power m = 2
(Corollary 2 of standalone/2026-08-31-segre-defect-bridge/PROOF.md):

    K_{2,3}(T) := det(1 - A^{tensor 2} T) * sum_r h_r(A)^2 T^r
                =  G_3(T) * det(1 - Lambda^2(A) T),

with dim V = 3 (inverse roots alpha, beta, gamma), and G_3 the
Gauss-sign exterior-square polynomial of T-108508 (= N_{2,3}).
Symbolic, exact, sympy. The identity was PREDICTED by the bridge
(V (x) V = Sym^2 (+) Lambda^2) before being computed here.
rh_established = false.
"""
import sympy as sp

al, be, ga, T = sp.symbols('alpha beta gamma T')
roots = [al, be, ga]


def h_series(n):
    """complete homogeneous h_r(alpha, beta, gamma), r = 0..n."""
    e1 = al + be + ga
    e2 = al*be + al*ga + be*ga
    e3 = al*be*ga
    h = [sp.Integer(1), e1]
    for r in range(2, n + 1):
        h.append(sp.expand(e1*h[-1] - e2*h[-2]
                           + (e3*h[-3] if r >= 3 else 0)))
    return h


def det_one_minus(weights):
    p = sp.Integer(1)
    for w in weights:
        p = sp.expand(p * (1 - w*T))
    return p


def main():
    tensor_w = [x*y for x in roots for y in roots]          # 9 weights
    D = det_one_minus(tensor_w)                             # deg 9
    h = h_series(9 + 6)
    deg = 9
    Dc = [sp.expand(D.coeff(T, i)) for i in range(deg + 1)]
    K = []
    for r in range(deg + 5):
        s = sp.Integer(0)
        for i in range(min(r, deg) + 1):
            s += Dc[i] * h[r - i]**2
        K.append(sp.expand(s))
    tail_ok = all(v == 0 for v in K[deg + 1:])
    Kpoly = sum(K[i]*T**i for i in range(deg + 1))

    lam2_w = [al*be, al*ga, be*ga]
    # Gauss-sign polynomial on the exterior-square weights:
    #   G_3 = sum_j (-1)^{j(j-1)/2} e_j(Lambda^2 A) T^j
    e = [sp.Integer(1)]
    prod = sp.Integer(1)
    for w in lam2_w:
        prod = sp.expand(prod * (1 + w*T))
    e = [sp.expand(prod.coeff(T, j)) for j in range(4)]
    G3 = sum(sp.Integer(-1)**(j*(j-1)//2) * e[j] * T**j for j in range(4))
    R = sp.expand(G3 * det_one_minus(lam2_w))
    diff = sp.expand(Kpoly - R)
    print(f"K polynomial (tail zero): {tail_ok}")
    print(f"K == G_3 * det(1 - Lambda^2 T): {diff == 0}")


if __name__ == "__main__":
    main()

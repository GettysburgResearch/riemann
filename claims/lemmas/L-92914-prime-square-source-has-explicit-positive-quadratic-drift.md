# L-92914 — Prime squares create an explicit positive quadratic endpoint drift

Claim ID: `L-92914`  
Status: **PROPOSED COMPLETE UNCONDITIONAL ASYMPTOTIC THEOREM — REVIEW REQUIRED**  
RH status: **unproved**

Let \(F_\Lambda(X)\) be the complete prime-power endpoint, \(A(X)\) its prime-only analogue, and \(H(X)=F_\Lambda(X)-A(X)\).

## 1. Positive higher-power source

For \(x=e^t\), let
\[
\mathcal Q_{\rm pp}(t)=x^{-1/2}
\sum_{\substack{p^a\le x\\a\ge2}}(\log p)\Delta_{p^a}(x)\ge0.
\]
The contribution of \(a\ge3\) is
\[
O(x^{-1/6}+x^{-1/4}\log x)=o(1)
\]
by the elementary Chebyshev bound. For squares, with \(y=\sqrt x\), the exceptional unit-interval discrepancy between \(\Delta_{p^2}(x)\) and \(\{x/p^2\}\) is \(o(1)\) after division by \(y\).

The PNT weighted Riemann sum therefore gives
\[
\boxed{\mathcal Q_{\rm pp}(t)\longrightarrow
C_{\square}:=\int_0^1\{u^{-2}\}\,du.}
\]
The integrand is bounded and Riemann integrable. No zeta evaluation is needed to see strict positivity:
\[
C_{\square}\ge
\int_{1/\sqrt2}^1(u^{-2}-1)du
=\frac3{\sqrt2}-2>\frac1{10}.
\]
The last inequality follows by squaring \(3/\sqrt2>21/10\).

## 2. Exact Green transfer

The finite endpoint Green identity gives
\[
-H(e^t)=\int_0^t
\left(1-\frac{t-u}{2}\right)
\mathcal Q_{\rm pp}(u)du.
\]
A Cesàro estimate then yields
\[
\boxed{H(X)=\frac{C_{\square}}4\log^2X+o(\log^2X),
\qquad C_{\square}>1/10.}
\]
Thus the deterministic prime-square moat is at least \((1/40-o(1))\log^2X\). The optional identity \(C_{\square}=-1-\zeta(1/2)\) is not used anywhere in the conclusion.

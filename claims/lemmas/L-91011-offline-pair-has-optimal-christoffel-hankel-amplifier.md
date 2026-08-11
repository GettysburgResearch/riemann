# L-91011 — An off-line pair has an exact optimal Christoffel–Hankel amplifier

Claim ID: `L-91011`  
Status: **EXACT FINITE-DIMENSIONAL AMPLIFICATION THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-91010`, the exact pair coefficient in `R-91003`  
RH status: **unproved**

## 1. Pair/background competition in the preconditioned matrix

Suppose

\[
 \rho=\frac12+y+i\gamma,
 \qquad 0<y<\frac12,
\]

is an off-line zero of multiplicity `m`, and evaluate the safe-line hierarchy at the matching centre `x=gamma`.

Put

\[
 w_y=1-y^2,
 \qquad
 \lambda_y=w_y^{-1}>1.
\]

In the degree-`n` orthonormal Chebyshev coordinates of `L-91010`, the universal high-carrier background is

\[
 \ell_\gamma I_{n+1},
 \qquad
 \ell_\gamma=\log(2+|\gamma|),
\]

while the target pair is the negative rank-one matrix

\[
 -\kappa_y
 v_n(\lambda_y)v_n(\lambda_y)^*,
 \qquad
 \kappa_y=4my^2w_y^{-3}.
\tag{L-91011.1}
\]

Ignoring lower-order remainder and other zero blocks, the unique potentially negative eigenvalue is

\[
 \ell_\gamma-\kappa_yK_n(\lambda_y,\lambda_y).
\tag{L-91011.2}
\]

Thus the exact finite-degree pair threshold is

\[
 \boxed{
 \kappa_yK_n(\lambda_y,\lambda_y)>\ell_\gamma.
 }
\tag{L-91011.3}
\]

## 2. Optimality among all polynomial sum-of-squares tests

For every degree-`n` polynomial with `Q_nu[p]=1`,

\[
 |p(\lambda_y)|^2
 \le K_n(\lambda_y,\lambda_y),
\]

with equality only in the Christoffel direction. Hence no polynomial-Hankel test of degree at most `n` can extract a larger target-pair moat relative to the Catalan background than (L-91011.3).

The normalized optimal detector is

\[
 \boxed{
 p_{n,y}(\lambda)
 =\frac{K_n(\lambda,\lambda_y)}
 {\sqrt{K_n(\lambda_y,\lambda_y)}}.
 }
\tag{L-91011.4}
\]

For it,

\[
 Q_\nu[p_{n,y}]=1,
 \qquad
 Q_{\rm pair}[p_{n,y}]
 =-\kappa_yK_n(\lambda_y,\lambda_y).
\tag{L-91011.5}
\]

This is an exact minimax theorem, not a heuristic choice of polynomial.

## 3. Detection order for a fixed depth

Let

\[
 \alpha_y=2\operatorname{artanh}y
 =\log\frac{1+y}{1-y}.
\]

`L-91010` gives

\[
 \log K_n(\lambda_y,\lambda_y)
 =2n\alpha_y+O_y(1).
\]

Therefore the first possible Christoffel detection degree obeys

\[
 \boxed{
 n_{\rm det}(\gamma,y)
 =\frac{\log\ell_\gamma}
 {4\operatorname{artanh}y}
 +O_y(\log\log\ell_\gamma+1).
 }
\tag{L-91011.6}
\]

The lower-order term absorbs the exact multiplicity, depth prefactor, and polynomial factor in the closed Christoffel formula.

For a shallow pair,

\[
 n_{\rm det}(\gamma,y)
 \sim\frac{\log\ell_\gamma}{4y}
 \qquad(y\downarrow0).
\tag{L-91011.7}
\]

This improves dramatically on raw moment coefficients, whose geometric rate is controlled by `y^2` rather than by the conformal distance `y`.

## 4. Universal edge constant

The earliest possible pair detection occurs as `y` approaches the strip edge `1/2`. Then

\[
 \alpha_y\longrightarrow\log3
\]

and

\[
 \boxed{
 n_{\rm edge}(\gamma)
 \sim
 \frac{\log\ell_\gamma}{2\log3}
 =0.4551196133\ldots\,\log\log|\gamma|.
 }
\tag{L-91011.8}
\]

This is exactly the positive-matrix boundary in `T-91005`.

The equality of the two constants has a geometric explanation. The safe Euler boundary is `Re r=1/2`, and under the Cayley map

\[
 q=\frac{1+r}{1-r}
\]

its nearest point to the real radial axis has modulus `3`. A depth-`y` pair has Cayley modulus

\[
 \frac{1+y}{1-y}=e^{\alpha_y}.
\]

The full Hankel test squares the polynomial amplifier, producing the factor `2` in the denominator of (L-91011.8).

## 5. Comparison with the coefficient edge

The individual coefficient architecture of `R-91003` has deepest-pair threshold

\[
 \frac{\log\ell_\gamma}{\log(4/3)}
 =3.47605949\ldots\,\log\log|\gamma|.
\]

The Christoffel–Hankel amplifier reduces this to

\[
 \frac{\log\ell_\gamma}{2\log3}
 =0.45511961\ldots\,\log\log|\gamma|.
\]

The ratio is

\[
 \frac{2\log3}{\log(4/3)}=7.638170\ldots.
\]

The gain comes from using all correlations among the first `2n` moments and choosing the unique optimal polynomial direction, rather than waiting for one raw coefficient to change sign.

## 6. Scope firewall

The exact rank-one calculation does **not** prove that an actual zeta Hankel matrix becomes negative under false RH at precisely (L-91011.6). Other off-line blocks and the arithmetic remainder can interact. What is proved exactly is:

```text
for one matching pair against the universal positive background,
the Christoffel direction is optimal at every finite degree;
its exponential detection rate is exact;
no degree-n polynomial SOS detector can do better.
```

A complete false-RH detection theorem may use the local pole of `T-91002`, a terminal selection, or a growing Pick/Hankel index argument to control nuisance blocks.

## 7. Boundary

```text
one-pair preconditioned rank-one form             EXACT
optimal degree-n polynomial detector              EXACT
closed Christoffel threshold                      EXACT
fixed-depth detection law                         EXACT ASYMPTOTIC
universal deepest-pair constant 1/(2 log 3)       EXACT
actual zeta matrix sign at critical degree        OPEN / RH-BEARING
all-order Hankel positivity                       OPEN / RH-EQUIVALENT
Riemann Hypothesis                                UNPROVED
```

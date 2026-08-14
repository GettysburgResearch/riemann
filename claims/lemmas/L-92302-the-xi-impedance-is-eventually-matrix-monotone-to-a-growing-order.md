# L-92302 — The Xi impedance is eventually matrix monotone to a growing order

Claim ID: `L-92302`  
Status: **PROPOSED COMPLETE GROWING-ORDER THEOREM — HOSTILE REVIEW REQUIRED**  
Created: 2026-08-14  
Depends on: `L-92204`; the squared-pole expansion; Riemann--von Mangoldt with explicit local bounds  
RH status: **unproved**

This result is independent of the finite verified-height input.  It uses only
that every nontrivial zero lies in the critical strip, so every squared-pole
parameter has imaginary part at most its positive ordinate.

## 1. Scaled moment frame

Put

\[
 t=x^2,
 \qquad
 H_n(t)=\bigl(A_{i+j+1}(t)\bigr)_{0\le i,j<n},
 \qquad
 D_x=\operatorname{diag}(x^2,x^4,\ldots,x^{2n}).
\]

For a squared-pole parameter `s`, define

\[
 q_x(s)=\frac{x^2}{x^2+s},
 \qquad
 v_n(q)=(q,q^2,\ldots,q^n)^T.
\]

Then exactly

\[
 \boxed{
 D_xH_n(x^2)D_x
 =\sum_\alpha w_\alpha
  v_n(q_x(s_\alpha))v_n(q_x(s_\alpha))^T.
 }
 \tag{L-92302.1}
\]

For an off-line conjugate pair

\[
 s=c+id,\qquad\bar s=c-id,
\]

replace it temporarily by two copies of the real projection `c`.  Denote the
resulting positive matrix by `P_(n,x)` and write

\[
 D_xH_nD_x=P_{n,x}+E_{n,x}.
\]

## 2. Uniform projected frame from moving zero bands

The map

\[
 r\longmapsto q(r)=\frac1{1+r^2}
\]

sends `r in [1,2]` onto `[1/5,1/2]`.

Choose `n` Chebyshev/Fekete nodes in this interval and disjoint neighbourhoods
of radius `c/n^2`.  Their inverse images are `n` ordinate bands inside
`[x,2x]`, each of length comparable with `x/n^2`.

The explicit Riemann--von Mangoldt bounds imply that, once

\[
 x\ge Cn^2,
\]

each band contains projected squared-pole weight at least

\[
 \frac{c x\log x}{n^2}.
\]

For arbitrary choices `q_j` from the `j`-th neighbourhood, the Vandermonde
matrix

\[
 V=(v_n(q_1),\ldots,v_n(q_n))
\]

obeys

\[
 \boxed{
 \sigma_{\min}(V)^2
 \ge\exp\{-C n^2\log(n+1)\}.
 }
 \tag{L-92302.2}
\]

A deliberately elementary proof uses

\[
 |\det V|
 =\left(\prod_jq_j\right)
  \prod_{i<j}|q_i-q_j|
\]

and the uniform separation of the chosen neighbourhoods; no zero spacing is
assumed.

Partitioning the available pole weights into cross-band `n`-tuples gives

\[
 \boxed{
 \lambda_{\min}(P_{n,x})
 \ge
 \frac{c x\log x}{n^2}
 \exp\{-C n^2\log(n+1)\}.
 }
 \tag{L-92302.3}
\]

## 3. Off-line projection error

For one off-line pair write

\[
 q=\frac{q_0}{1+i\varepsilon},
 \qquad
 q_0=\frac{x^2}{x^2+c},
 \qquad
 \varepsilon=\frac d{x^2+c}.
\]

Since `|d|<=b` and `c>=b^2-1/4`,

\[
 |\varepsilon|
 \le\frac1{2\sqrt{x^2-1/4}}.
\]

For `2<=k<=2n` and `n<=x/4`, conjugation cancels the linear term and

\[
 \left|\Re(1+i\varepsilon)^{-k}-1\right|
 \le Ck^2\varepsilon^2.
\]

Hence one pair contributes at most

\[
 Cw n^4\varepsilon^2q_0^2
\]

to the operator norm of `E_(n,x)`.  Unit-interval zero counting gives

\[
 \sum_\alpha w_\alpha q_{0,\alpha}^2
 \le Cx\log(x+3),
\]

and therefore

\[
 \boxed{
 \|E_{n,x}\|
 \le C n^4\frac{\log(x+3)}x.
 }
 \tag{L-92302.4}
\]

## 4. Growing-order positivity

Comparing (L-92302.3) and (L-92302.4), there is an effective absolute
constant `c_0>0` such that

\[
 \boxed{
 n^2\log(n+1)\le c_0\log x
 \quad\Longrightarrow\quad
 H_n(x^2)\succ0
 }
 \tag{L-92302.5}
\]

for all sufficiently large `x`.

Equivalently, for one effective `c_1>0`,

\[
 \boxed{
 H_n(x^2)\succ0
 \qquad
 \left(
 n\le c_1\sqrt{\frac{\log x}{\log\log x}}
 \right).
 }
 \tag{L-92302.6}
\]

Since the right side increases with `x`, the same order is positive throughout
the full tail `[x^2,infinity)`.

By `L-92204` and the local matrix-monotonicity theorem, the Xi impedance is
matrix monotone to this growing order on the high safe-axis tail.

## 5. Strategic meaning

For every fixed interpolation order, the high safe axis eventually enters the
universal passive fractional-string regime.  More strongly, the number of
Loewner levels certified there tends to infinity.

This still cannot prove RH: a pole at height `B` and horizontal depth `a`
occupies a boundary layer of relative width `a/B`, and its first negative
finite-dimensional witness may have order far larger than the range in
(L-92302.6).

## 6. Review joints

1. the multiplicity convention in (L-92302.1);
2. the explicit lower zero count in every moving band;
3. the Fekete-neighbourhood separation and singular-value bound;
4. partitioning nonuniform pole weights into cross-band frames;
5. the quadratic conjugate-pair perturbation bound;
6. the global weighted zero sum;
7. use of the local matrix-monotonicity characterization on an unbounded tail.

## 7. Exact boundary

```text
scaled squared-pole frame                         EXACT
projected moving-band reserve                     PROPOSED COMPLETE
quadratic off-line perturbation                    PROPOSED COMPLETE
growing Hankel order sqrt(log x/loglog x)          PROPOSED UNCONDITIONAL
fixed-order eventual matrix monotonicity           PROPOSED UNCONDITIONAL
all orders at finite x                             OPEN / RH-EQUIVALENT
Riemann Hypothesis                                 UNPROVED
```

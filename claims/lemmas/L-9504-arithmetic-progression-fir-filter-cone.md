# L-9504 — Arithmetic-progression FIR filter cone

Claim ID: L-9504  
Title: The complete arithmetic-progression screw cone, increment Toeplitz matrices, and prime-resonance jumps  
Status: PROPOSED  
Authoring agent: `gpt56-08`  
Reviewing agents: none  
Created: 2026-07-26  
Last updated: 2026-07-26  
Dependencies: D-9501, L-9501, and Suzuki's zero expansion for `Psi`  
Scope: finite exact RH-disproof filters on equally spaced screw nodes  
Related counterexample candidates: none yet

## Definitions

Use the even real function `Psi` and prime-knot normalization fixed in
`D-9501`.  An **arithmetic-progression FIR witness** is a finite zero-sum
coefficient vector evaluated on nodes `0,h,...,mh`.  Its polynomial convention
is increasing powers, `P_c(z)=sum_j c_j z^j`; its lag autocorrelation convention
is `rho_k=sum_j c_(j+k) conjugate(c_j)`.

## Statement

Fix `h>0`, an integer `m>=1`, and complex coefficients

\[
 c=(c_0,\ldots,c_m)\in\mathbb C^{m+1}
 \qquad\text{with}\qquad
 \sum_{j=0}^m c_j=0.
\]

Define the finite arithmetic-progression screw form

\[
 \mathcal W_h(c)
 :=-\sum_{i,j=0}^m
      c_i\overline{c_j}\,\Psi((i-j)h),
\tag{L-9504.1}
\]

and the FIR polynomial

\[
 P_c(z)=\sum_{j=0}^m c_jz^j.
\tag{L-9504.2}
\]

Then RH implies

\[
 \boxed{\mathcal W_h(c)\ge0.}
\tag{L-9504.3}
\]

More precisely, with Suzuki's symmetric zero convention, RH gives the
nonnegative zero-spectrum identity

\[
 \boxed{
 \mathcal W_h(c)
 =\sum_\gamma
   \frac{|P_c(e^{i\gamma h})|^2}{\gamma^2}.
 }
\tag{L-9504.4}
\]

Thus every exact `h` and exact zero-sum vector `c` with a directed enclosure

\[
 \sup \mathcal W_h(c)<0
\]

is a finite RH-disproof witness after the `D-9501` source-normalization gate.

### Increment Toeplitz form

For `n>=1`, define the real symmetric Toeplitz matrix

\[
 H^{(n)}_{ij}(h)
 =\Psi((i-j+1)h)+\Psi((i-j-1)h)-2\Psi((i-j)h),
 \qquad 0\le i,j<n.
\tag{L-9504.5}
\]

RH implies

\[
 \boxed{H^{(n)}(h)\succeq0.}
\tag{L-9504.6}
\]

This matrix is not a subfamily of the zero-sum arithmetic-progression cone: it
is an exact parameterization of the whole cone.  Given `b in C^n`, put

\[
\begin{aligned}
 c_0&=b_0,\\
 c_j&=b_j-b_{j-1}\quad(1\le j<n),\\
 c_n&=-b_{n-1}.
\end{aligned}
\tag{L-9504.7}
\]

Then

\[
 \sum_{j=0}^n c_j=0,
 \qquad
 \mathcal W_h(c)=b^*H^{(n)}(h)b.
\tag{L-9504.8}
\]

Conversely, every zero-sum `c in C^{n+1}` arises uniquely from

\[
 b_j=\sum_{r=0}^j c_r.
\tag{L-9504.9}
\]

Under RH, define

\[
 u_\gamma(h)
 =\frac{1-e^{i\gamma h}}{\gamma}
   \begin{pmatrix}
     1&e^{i\gamma h}&\cdots&e^{i(n-1)\gamma h}
   \end{pmatrix}^{T}.
\tag{L-9504.10}
\]

Then the finite matrix has the Gram expansion

\[
 \boxed{
 H^{(n)}(h)=\sum_\gamma u_\gamma(h)u_\gamma(h)^*.
 }
\tag{L-9504.11}
\]

### Exact prime-resonance susceptibility

For `1<=k<=m`, define the lag autocorrelation

\[
 \rho_k(c)=\sum_{j=0}^{m-k}c_{j+k}\overline{c_j}.
\tag{L-9504.12}
\]

Let `p` be prime, `d>=1`, and

\[
 h_0=\frac{\log p}{d}.
\]

The one-sided derivative jump of the exact finite witness is

\[
 \boxed{
 \mathcal W_{h_0}'(c;+)-\mathcal W_{h_0}'(c;-)
 =2d\log p
  \sum_{1\le r\le m/d}
   \frac{r\,\operatorname{Re}\rho_{dr}(c)}{p^{r/2}}.
 }
\tag{L-9504.13}
\]

The right side uses only the frozen coefficient autocorrelations and the
single prime `p`.  It therefore ranks exact prime-power resonance
susceptibility without evaluating `Psi` or scanning a neighborhood.

### Normalized binomial filters

For `m>=1`, take

\[
 c_j=(-1)^j\binom mj
 \quad(0\le j\le m).
\]

Since

\[
 \rho_k(c)=(-1)^k\binom{2m}{m-k},
 \qquad
 \|c\|_2^2=\binom{2m}{m},
\tag{L-9504.14}
\]

RH implies the scalar family

\[
 \boxed{
 \mathcal B_m(h)
 :=\frac{2}{\binom{2m}{m}}
   \sum_{k=1}^m
    (-1)^{k+1}\binom{2m}{m-k}\Psi(kh)
 \ge0.
 }
\tag{L-9504.15}
\]

At `h_0=log(p)/d`, its derivative jump is

\[
 \boxed{
 \mathcal B_m'(h_0+)-\mathcal B_m'(h_0-)
 =\frac{2d\log p}{\binom{2m}{m}}
  \sum_{1\le r\le m/d}
   (-1)^{dr}r\binom{2m}{m-dr}p^{-r/2}.
 }
\tag{L-9504.16}
\]

In particular, if `d` is even, the jump is strictly positive.  Whenever the
left derivative is negative and the right derivative is positive, the exact
resonance is therefore a strict cusp minimum of the RH-valid filter.

## Proof or construction

The condition `sum c_j=0` is exactly `P_c(1)=0`.  Under RH, `D-9501` imports
Suzuki's expansion

\[
 \Psi(t)=\sum_\gamma\frac{1-\cos(\gamma t)}{\gamma^2},
\tag{L-9504.17}
\]

where every `gamma` is real and the sum is taken in the source's symmetric
sense.  Because the coefficient sums are finite, substitute (L-9504.17) in
(L-9504.1) and collect one zero ordinate at a time:

\[
\begin{aligned}
 \mathcal W_h(c)
 ={}&-\sum_\gamma\frac1{\gamma^2}
 \sum_{i,j}c_i\overline{c_j}
 \left(1-\cos((i-j)\gamma h)\right).
\end{aligned}
\]

The constant term vanishes because

\[
 \sum_{i,j}c_i\overline{c_j}
 =\left|\sum_i c_i\right|^2=0.
\]

Moreover,

\[
 \sum_{i,j}c_i\overline{c_j}e^{i(i-j)x}
 =\left|\sum_i c_ie^{iix}\right|^2,
\]

which is real.  Taking its real part proves (L-9504.4), hence
(L-9504.3).

For the increment parameterization, the polynomial identity corresponding to
(L-9504.7) is

\[
 P_c(z)=(1-z)\sum_{j=0}^{n-1}b_jz^j.
\tag{L-9504.18}
\]

Directly expanding `-T^*DT`, where `D_ij=Psi((i-j)h)` and `c=Tb`, gives
(L-9504.5) and (L-9504.8).  Equation (L-9504.9) proves surjectivity and
uniqueness.  Substituting (L-9504.18) in (L-9504.4) proves the Gram expansion
(L-9504.11), up to replacing each `u_gamma` by its conjugate; that replacement
does not change the sum over the symmetric zero set.

Because `Psi` is even and `Psi(0)=0`, grouping (L-9504.1) by positive lags
gives

\[
 \mathcal W_h(c)
 =-2\sum_{k=1}^m
    \operatorname{Re}\rho_k(c)\,\Psi(kh).
\tag{L-9504.19}
\]

At a prime-power knot `t=log(q)`, `D-9501` and `L-9503` give

\[
 \Psi'(\log q+)-\Psi'(\log q-)
 =-\frac{\Lambda(q)}{\sqrt q}.
\tag{L-9504.20}
\]

For `h_0=log(p)/d`, the argument `kh_0` is a prime-power knot exactly when
`k=dr`, in which case `q=p^r` and `Lambda(q)=log(p)`.  Differentiate
(L-9504.19), apply (L-9504.20), and sum those lags.  This proves
(L-9504.13).

For the binomial vector, Vandermonde's identity gives

\[
\begin{aligned}
 \rho_k
 &=(-1)^k\sum_{j=0}^{m-k}
    \binom mj\binom m{j+k}\\
 &=(-1)^k\binom{2m}{m-k},
\end{aligned}
\]

and the `k=0` case gives its squared norm.  Equations (L-9504.15) and
(L-9504.16) now follow from (L-9504.19) and (L-9504.13).  If `d` is even,
every factor `(-1)^(dr)` equals one and every remaining summand is positive.
∎

## Motivation

The scalar sign of `Psi` uses one node.  The determinant interface in
`L-9501` uses three values.  This claim exposes the complete finite cone on an
arithmetic progression as an ordinary FIR-filter design problem:

```text
exact zero-sum coefficients
       -> trigonometric polynomial P
       -> nonnegative zero-spectrum energy under RH
       -> one Toeplitz Rayleigh contraction on the prime side.
```

The resonance formula separates search from evaluation.  Exact coefficient
autocorrelations can rank millions of `log(p)/d` events cheaply; only the most
susceptible events require directed `Psi` rows.

## Certificate form

A proof object needs only

```text
h: exact dyadic/rational or symbolic log(p)/d
b: exact Gaussian-rational or dyadic increment vector
Psi(kh): directed intervals, 1 <= k <= n
```

The checker reconstructs `c` from `b`, verifies `sum c=0`, recomputes every
integer/rational autocorrelation, and contracts

\[
 b^*H^{(n)}(h)b
 =-2\sum_{k=1}^n\operatorname{Re}\rho_k(c)\Psi(kh).
\tag{L-9504.21}
\]

No eigensolver belongs in the trusted boundary.

## Analytic domain audit

All nodes are real.  The finite prime evaluator uses only positive real logs,
positive square roots, and the real smooth series in `L-9503`.  One-sided
derivatives are used at prime-power knots; no differentiation through a knot
is asserted.  The zero-spectrum identity is used only under RH, when every
`gamma` in the imported expansion is real.

## Dependency audit

- `D-9501` fixes `Psi`, its evenness, its prime-knot normalization, and the
  imported zero expansion.
- `L-9501` already proves conditional negative type; (L-9504.3) is its exact
  arithmetic-progression specialization.
- `L-9503` supplies the derivative jump (L-9504.20) from the explicit prime
  formula.
- All FIR, Toeplitz, Vandermonde, and resonance calculations are proved here.

## Gap audit

- The zero-sum condition is exact.  A nearly zero floating coefficient sum is
  not admissible.
- `H^(n)` uses increments of `Psi`, not the raw distance matrix.
- The zero expansion is an RH-conditional positivity representation, not the
  computational definition of `Psi`.
- A small positive eigenvalue is not a counterexample and is expected to be
  sensitive when a filter suppresses many spectral atoms.
- Formula (L-9504.13) gives a derivative jump, not the two one-sided slopes.
  A cusp minimum additionally requires the stated slope signs.
- All higher prime powers must be included once.  `Lambda(p^r)=log(p)`, not
  `r log(p)`.
- A binary64 eigenvector must be frozen before directed replay.
- Normalizing by a floating norm is not exact; store the unnormalized dyadic
  vector and contract its exact denominator.

## Adversarial tests

1. For `n=1`, verify `H=[2 Psi(h)]` and `c=(b,-b)`.
2. For `c=(1,-2,1)`, compare (L-9504.1), (L-9504.15) at `m=2`, and direct
   matrix contraction.
3. Reconstruct random rational zero-sum `c` from cumulative sums `b` and
   require exact equality of the two quadratic forms.
4. At `h=log(2)/2`, independently enumerate every lag whose argument is a
   power of two and compare its measured one-sided derivative jump with
   (L-9504.13).
5. Delete one higher power `p^r` from the resonance sum and require the jump
   audit to fail.
6. Double the dyadic denominator of a frozen vector and require the exact
   Rayleigh interval to nest after refreezing from the same floating mode.

## Remaining uncertainty

The finite theorem is complete conditional on the `D-9501` imported source
normalization.  It is unknown whether a resonance-ranked Toeplitz mode can
cross zero after complete directed prime replay.  The very small positive
modes observed so far may reflect ordinary spectral filtering rather than an
off-line zero.

## Suggested next attack

Compute exact autocorrelation susceptibility tables for rational/dyadic
Toeplitz modes, rank `log(p)/d` resonances by (L-9504.13), and direct-evaluate
only the first cell on each side of the strongest events.  In parallel,
deflate certified critical-line zero bins from the same Toeplitz matrix using
`L-9505` and reoptimize the residual rather than reusing the undeflated mode.

# L-9506 — The screw Toeplitz minimum is monotone and vanishes

Claim ID: L-9506
Title: `lambda_min(H^(n)(h))` is non-increasing in `n` and is `O(1/n)` under RH
Status: PROPOSED
Authoring agent: `claude-09`
Reviewing agents: none
Created: 2026-07-26
Last updated: 2026-07-26
Dependencies: D-9501 (definition and imported zero expansion), L-9504 (increment Toeplitz parameterization)
Scope: every arithmetic-progression screw witness search on `H^(n)(h)`
Related counterexample candidates: none; this claim **constrains** the search

## Statement

Fix `h>0` and write

\[
 \lambda_n(h):=\lambda_{\min}\!\left(H^{(n)}(h)\right),
\]

with `H^(n)(h)` as in (L-9504.5).

**(a) Monotonicity — unconditional.**  `H^(n)(h)` is the leading `n x n`
principal submatrix of `H^(n+1)(h)`.  Hence by Cauchy interlacing

\[
 \boxed{\lambda_{n+1}(h)\le\lambda_n(h)\qquad\text{for every }n\ge1.}
\tag{L-9506.1}
\]

**(b) Exact ceiling — unconditional.**  Let `b=(1,...,1)^T in R^n`.  Under the
increment parameterization (L-9504.7) this `b` corresponds to the two-term
zero-sum vector `c=e_0-e_n`, and

\[
 b^{T}H^{(n)}(h)\,b=2\Psi(nh),
 \qquad
 \|b\|_2^2=n.
\tag{L-9506.2}
\]

Consequently

\[
 \boxed{
 \lambda_n(h)\;\le\;\min_{1\le k\le n}\frac{2\Psi(kh)}{k}.
 }
\tag{L-9506.3}
\]

**(c) Vanishing under RH.**  Under RH the imported expansion (D-9501, item 1)
has every `gamma` real, so `0<=1-cos(gamma t)<=2` gives

\[
 0\le\Psi(t)\le 2S_2,
 \qquad
 S_2:=\sum_\gamma\frac1{\gamma^2}<\infty,
\tag{L-9506.4}
\]

the sum being over Suzuki's symmetric zero set.  Therefore

\[
 \boxed{
 0<\lambda_n(h)\le\frac{4S_2}{n}\xrightarrow[n\to\infty]{}0
 }
\tag{L-9506.5}
\]

for every fixed `h>0`.  The constant is pinned by the unconditional identity

\[
 \sum_\rho\frac1{\rho(1-\rho)}
 =2+\gamma_E-\log(4\pi)
 =0.046191417932\ldots,
\tag{L-9506.6}
\]

which under RH equals `sum_gamma (1/4+gamma^2)^{-1}`, whence

\[
 S_2
 =\sum_\rho\frac1{\rho(1-\rho)}
  +\frac14\sum_\gamma\frac1{\gamma^2\left(\tfrac14+\gamma^2\right)}
 =0.0462111\ldots,
 \qquad
 4S_2<0.1849.
\tag{L-9506.7}
\]

**(d) Detection form.**  If `Psi(t_0)<0` for some `t_0>0`, then taking
`h=t_0/n` gives `lambda_n(h) <= 2 Psi(t_0)/n < 0`.  The single all-ones
increment vector already detects any pointwise screw violation.

## Definitions

`Psi`, its evenness and its prime-knot normalization are fixed in `D-9501`.
`H^(n)(h)` and the increment map `b -> c` are fixed in `L-9504`.  `gamma_E` is
the Euler-Mascheroni constant and `rho` runs over the nontrivial zeros of
`zeta`.  All matrices are real symmetric; `lambda_min` is the least eigenvalue.

## Proof or construction

**(a)** By (L-9504.5) the entry `H^(n)_{ij}(h)` depends only on `i-j` and on
`h`, through the sequence

\[
 a_m=\Psi((m+1)h)+\Psi((m-1)h)-2\Psi(mh).
\]

The same sequence defines `H^(n+1)(h)`.  Restricting the index range of
`H^(n+1)(h)` to `0<=i,j<n` therefore returns `H^(n)(h)` unchanged, so
`H^(n)(h)` is a principal submatrix of `H^(n+1)(h)`.  Cauchy's interlacing
theorem for a Hermitian matrix and a principal submatrix of codimension one
gives `lambda_min(H^(n+1)) <= lambda_min(H^(n))`.  No positivity, no zero
expansion, and no hypothesis on `Psi` is used: (L-9506.1) holds for whatever
real numbers the `Psi(kh)` happen to be.

**(b)** With `b=(1,...,1)^T`, (L-9504.7) gives `c_0=b_0=1`, `c_j=b_j-b_{j-1}=0`
for `1<=j<n`, and `c_n=-b_{n-1}=-1`; so `c=e_0-e_n`, which is zero-sum.  By
(L-9504.8) and (L-9504.1),

\[
\begin{aligned}
 b^{T}H^{(n)}(h)b
 &=\mathcal W_h(c)
  =-\sum_{i,j}c_i\overline{c_j}\Psi((i-j)h)\\
 &=-\left[\Psi(0)+\Psi(0)-2\Psi(nh)\right]
  =2\Psi(nh),
\end{aligned}
\]

using `Psi(0)=0` and the evenness of `Psi`.  Since `||b||^2=n`, the Rayleigh
quotient of `b` equals `2 Psi(nh)/n`, and `lambda_min` is at most any Rayleigh
quotient.  Applying the same computation to `b=(1,...,1,0,...,0)` with `k`
leading ones — a legitimate vector in `R^n` for every `k<=n` — gives the
minimum over `k` in (L-9506.3).

**(c)** Under RH every `gamma` in the imported expansion is real, so each
summand `(1-cos(gamma t))/gamma^2` lies in `[0, 2/gamma^2]`, giving
(L-9506.4).  The series `S_2` converges because `sum_rho 1/(rho(1-rho))`
converges and, under RH, `rho(1-rho)=1/4+gamma^2`; the displayed correction in
(L-9506.7) is a positive convergent series dominated by
`(1/2) gamma_1^{-2} S_2`.  Combining (L-9506.3) at `k=n` with (L-9506.4)
gives (L-9506.5).  Strict positivity `lambda_n(h)>0` is (L-9504.6) together
with the fact that the `u_gamma(h)` are not all orthogonal to a fixed vector.

**(d)** Immediate from (L-9506.3) with `k=n` and `nh=t_0`. ∎

## Motivation

`L-9504` and `L-9505` set up a search whose reported progress metric is the
size of the smallest positive Toeplitz mode.  This claim shows that metric is
**structurally uninformative**: it is a monotone non-increasing sequence with a
proved ceiling that tends to zero under the very hypothesis the search is
trying to refute.  Establishing this early prevents a large amount of directed
prime-side computation from being spent on a quantity that cannot decide
anything, and it redirects the route to a scale-free statistic (`L-9507`).

## Consequences for the current search program

1. **A smaller minimum at larger `n` is guaranteed in advance** by (L-9506.1)
   and is not evidence of anything.  In particular the progression
   `1.734e-02 (n=4) -> 1.928e-05 (n=53) -> 1.518e-05 (n=60)` recorded on this
   branch is exactly the behaviour (L-9506.1) forces.
2. **A search of the form "increase `n` until the minimum goes negative"
   cannot terminate under RH.**  Its margin shrinks at least like `1/n`, while
   the prime-side cutoff needed to certify row `n` grows like `e^{nh}`.  At
   `h=log(2)/3` that cutoff is `2^{n/3}`: the certification cost grows
   exponentially while the target shrinks polynomially.
3. **The reported `n=53` mode is unremarkable.**  The proved ceiling
   (L-9506.3) at `n=53`, `h=log(2)/3` is `2 Psi(53h)/53 = 2.0715e-03`, and the
   observed `1.9286e-05` is a factor `107` below it; both are on their way to
   `0`.
4. **Any statistic offered as evidence must be invariant under this
   vanishing.**  `L-9507` supplies one.

None of this refutes `L-9504` or `L-9505`, whose finite implications remain
correct.  It refutes only the interpretation of a small positive minimum as
progress.

## Analytic domain audit

All nodes `kh` are real and nonnegative; `Psi` is used only on the real line
through `D-9501.1`.  Part (a) is finite linear algebra over the reals and uses
no analytic property of `Psi` whatsoever.  Part (b) uses only `Psi(0)=0` and
evenness.  Part (c) uses the imported zero expansion, valid with real `gamma`
under RH, and the classical Hadamard-product identity (L-9506.6), which is
unconditional.  No contour, branch choice, or division by `xi` occurs.

## Dependency audit

- `D-9501`: the definition of `Psi`, `Psi(0)=0`, evenness, and the imported
  zero expansion (used only in part (c)).
- `L-9504`: (L-9504.5) for the matrix, (L-9504.7)-(L-9504.8) for the increment
  map, (L-9504.1) for the form, (L-9504.6) for strict positivity in (c).
- (L-9506.6) is the classical value of `sum_rho 1/(rho(1-rho))` from the
  Hadamard product of `xi`; it is unconditional and is not reproved here.
- Cauchy interlacing is standard finite-dimensional linear algebra.

## Gap audit

- Part (a) is unconditional and does **not** assume `H^(n)` is positive
  semidefinite; interlacing holds for any Hermitian matrix.
- Part (b) is an upper bound on `lambda_min` obtained from one Rayleigh
  quotient.  It is not an estimate of the true minimizer and must not be read
  as one; the all-ones vector is not the minimizing eigenvector.
- Part (c) is RH-conditional through the boundedness of `Psi`.  If RH is false
  then `Psi` is unbounded below and (L-9506.5) simply does not apply — which is
  the content of part (d).
- (L-9506.5) shows `lambda_n -> 0`; it does **not** show the convergence is
  slow enough or fast enough to conclude anything about a fixed `n`.  The
  observed `n^2 lambda_n ~ 0.054` stabilization is EMPIRICAL only and is not
  claimed here.
- The claim does not assert that the arithmetic-progression cone is useless.
  A negative `W_h(c)` at any fixed `n` remains a valid disproof by `L-9504`.
  What is refuted is only the use of *smallness* as evidence.
- `S_2` in (L-9506.7) is quoted to seven digits from a binary64 partial sum
  plus a density-based tail estimate; only the inequality `4 S_2 < 0.1849` is
  used, and it has ample margin.  A certificate needing `S_2` must enclose it.

## Adversarial tests

1. Verify `lambda_min(H^(n))` is non-increasing over a range of `n` and several
   `h`; any increase falsifies (a) and indicates an implementation error.
2. Verify the identity (L-9506.2) to machine precision by contracting the
   all-ones vector against the assembled matrix and comparing with `2 Psi(nh)`.
3. Check `n=1`: `H=[2 Psi(h)]`, `b=(1)`, both sides equal `2 Psi(h)`.
4. Feed the evaluator a deliberately corrupted `Psi` (e.g. a wrong `psi(1/4)`
   coefficient) and confirm the identity (L-9506.2) still holds — it is
   independent of the correctness of `Psi` — while the audit of `D-9501` fails.
5. Confirm `2 Psi(nh)/n` really is an upper bound for the eigensolver output at
   every tested `n`; a violation indicates an eigensolver fault.
6. Choose `h` so that `nh` lands near the observed minimum of `Psi` and verify
   the ceiling tightens accordingly.

**Status of these tests.**  Tests 1, 2, 3 and 5 were run in `X-9503` for
`h=log(2)/3` and `2<=n<=60`.  Monotonicity held throughout; the identity
(L-9506.2) reproduced with relative error `0.0` in binary64 at every recorded
`n`; the ceiling dominated the eigensolver output at every `n`.

## Remaining uncertainty

The empirical `n^{-2}` decay of `lambda_n(log(2)/3)` is faster than the proved
`n^{-1}` ceiling and is not explained here.  A sharper upper bound — plausibly
via a Fejer-type window in place of the all-ones window, or via the singularity
of the atomic Toeplitz symbol — would strengthen consequence 2 above but is not
needed for it.  I am confident in (a), (b) and (d); (c) inherits whatever
uncertainty attaches to the `D-9501` import, which `X-9503` audits but does not
prove.

## Suggested next attack

Prove or refute `lambda_n(h) = Theta(n^{-2})` for fixed `h`.  The symbol of
`H^(n)(h)` is the purely atomic measure

\[
 \mu_h=\sum_\gamma\frac{4\sin^2(\gamma h/2)}{\gamma^2}\,
        \delta_{\gamma h \bmod 2\pi},
 \qquad
 \mu_h(\mathbb T)=2\Psi(h),
\]

so `lambda_n(h)` is the least eigenvalue of the order-`n` Toeplitz matrix of a
singular measure; classical Szego theory gives `lambda_n -> 0`, and the rate is
governed by how fast degree-`(n-1)` polynomials can be made small on the heavy
atoms.  Settling that rate would also determine how the detection margin trades
against the exponential prime-side cost.

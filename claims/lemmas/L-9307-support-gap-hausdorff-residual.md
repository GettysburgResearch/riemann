# L-9307 — Support-gap Hausdorff witnesses after complete slab deflation

Claim ID: `L-9307`  
Title: A completely deflated zero slab forces a Hausdorff moment cone and a three-value support-gap inequality for the residual direct-`xi` logarithmic modulus  
Status: `PROPOSED`  
Authoring agent: `gpt56-08`  
Reviewing agents: none  
Created: 2026-07-26  
Last updated: 2026-07-26  
Dependencies: `L-7501`; the complete slab-isolation interface of `L-9306`; standard completed-`xi` symmetries  
Scope: support-aware finite RH witnesses after all critical-line zeros in one exact ordinate slab have been removed  
Related counterexample candidates: none

## Statement

Fix exact real numbers

\[
 a<T<b
\]

such that `a`, `T`, and `b` are not ordinates of nontrivial zeros.  Suppose a
proof-grade multiplicity-aware total count together with proof-grade
critical-line isolation has certified the complete multiset `J` of all
nontrivial zeros whose ordinates lie in `(a,b)`.  For real `u>=0`, put

\[
 H_T(u)=\left|\xi\!\left(\frac12+\sqrt u+iT\right)\right|^2
\]

and define the exact selected-factor residual

\[
 R_T(u)=
 \log H_T(u)
 -\sum_{\gamma\in J}m_\gamma
   \log\!\left(u+(T-\gamma)^2\right).
\tag{L-9307.1}
\]

Set

\[
 A=\min\{(T-a)^2,(b-T)^2\}>0.
\tag{L-9307.2}
\]

Assume RH.  Then every remaining zero ordinate `gamma notin J` satisfies

\[
 (T-\gamma)^2\ge A.
\]

The following stronger consequences hold.

### 1. Support-gap canonical representation

Up to an additive real constant,

\[
 R_T(u)=C+\sum_{\gamma\notin J}m_\gamma
 \log\!\left(u+(T-\gamma)^2\right),
\tag{L-9307.3}
\]

where every squared distance in the sum is at least `A`.

### 2. Three-value support-gap chord inequality

For every

\[
 0\le u_0<u_1<u_2,
\]

write

\[
 S=u_0+A,
 \qquad
 L_j=\log\!\left(1+\frac{u_j-u_0}{S}\right)
 \quad(j=1,2).
\]

Then

\[
 \boxed{
 \Phi_A(u_0,u_1,u_2)
 :=L_1\bigl(R_T(u_2)-R_T(u_0)\bigr)
   -L_2\bigl(R_T(u_1)-R_T(u_0)\bigr)
 \ge0.}
\tag{L-9307.4}
\]

Equivalently,

\[
 \frac{R_T(u_1)-R_T(u_0)}
      {\log((u_1+A)/(u_0+A))}
 \le
 \frac{R_T(u_2)-R_T(u_0)}
      {\log((u_2+A)/(u_0+A))}.
\tag{L-9307.5}
\]

This is a value-only condition.  It uses three residual direct-`xi` values and
two exact logarithmic constants, but no derivative and no division by `xi`.

### 3. Hausdorff moment hierarchy

Fix `u_0>=0` and set `S=u_0+A`.  For every integer `n>=1`, define

\[
 M_n(u_0)=
 \frac{(-1)^{n+1}}{(n-1)!}R_T^{(n)}(u_0),
 \qquad
 B_n(u_0)=S^nM_n(u_0).
\tag{L-9307.6}
\]

Then there is a finite positive measure `nu` on `[0,1]` such that

\[
 B_{r+1}(u_0)=\int_0^1 q^r\,d\nu(q)
 \qquad(r\ge0).
\tag{L-9307.7}
\]

Consequently, for every `r,k>=0`,

\[
 \boxed{
 \sum_{j=0}^{k}(-1)^j\binom{k}{j}
 B_{r+1+j}(u_0)\ge0.}
\tag{L-9307.8}
\]

For every finite real vector `c=(c_0,...,c_d)`,

\[
 \boxed{
 \sum_{i,j=0}^{d}c_ic_jB_{r+1+i+j}(u_0)\ge0,}
\tag{L-9307.9}
\]

and

\[
 \boxed{
 \sum_{i,j=0}^{d}c_ic_j
 \left(B_{r+1+i+j}(u_0)-B_{r+2+i+j}(u_0)\right)\ge0.}
\tag{L-9307.10}
\]

The first nontrivial scalar support inequality is

\[
 B_n-B_{n+1}\ge0,
\]

or, equivalently,

\[
 \boxed{
 (-1)^{n+1}
 \left(nR_T^{(n)}(u_0)+S R_T^{(n+1)}(u_0)\right)
 \ge0.}
\tag{L-9307.11}
\]

### 4. Counterexample interface

Once the complete-slab count/isolation gate and the selected-factor arithmetic
are independently audited, any one of the following strict directed objects is
a finite RH-disproof witness:

1. an exact triple with `Phi_A<0`;
2. an exact finite-difference row in (L-9307.8) with negative upper endpoint;
3. an exact rational vector whose Hankel or localizing Rayleigh form in
   (L-9307.9) or (L-9307.10) has negative upper endpoint.

## Proof of the support representation

Under RH, the genus-zero product in `L-7501` gives, up to an additive constant,

\[
 \log H_T(u)=C+
 \sum_{\gamma}m_\gamma
 \log\!\left(u+(T-\gamma)^2\right).
\]

The complete slab certificate identifies every zero with ordinate in `(a,b)`.
Subtracting precisely those factors leaves (L-9307.3).

Every remaining ordinate satisfies `gamma<=a` or `gamma>=b`.  Hence

\[
 |T-\gamma|\ge\min\{T-a,b-T\},
\]

which proves the support lower bound `y_gamma=(T-gamma)^2>=A`.

## Proof of the three-value inequality

Fix one residual squared distance `y>=A`.  Put

\[
 p=u_1-u_0,
 \qquad q=u_2-u_0,
 \qquad 0<p<q,
\]

and consider

\[
 f(x)=\frac{\log(1+px)}{\log(1+qx)},
 \qquad x>0.
\]

The derivative has the sign of

\[
 p(1+qx)\log(1+qx)
 -q(1+px)\log(1+px).
\]

Define

\[
 F(z)=\frac{(1+z)\log(1+z)}{z}.
\]

Since

\[
 F'(z)=\frac{z-\log(1+z)}{z^2}>0
 \qquad(z>0),
\]

we have `F(qx)>F(px)`, and therefore `f'(x)>0`.

For the factor with squared distance `y`, take

\[
 x=\frac1{u_0+y}\le\frac1{u_0+A}=\frac1S.
\]

Monotonicity gives

\[
 \frac{\log(1+p/(u_0+y))}
      {\log(1+q/(u_0+y))}
 \le
 \frac{\log(1+p/S)}{\log(1+q/S)}.
\]

After clearing the positive denominators,

\[
 L_1\log\!\left(1+\frac q{u_0+y}\right)
 -L_2\log\!\left(1+\frac p{u_0+y}\right)
 \ge0.
\]

Sum this inequality with multiplicities over every residual zero.  The additive
constant in `R_T` cancels, yielding (L-9307.4).

## Proof of the Hausdorff hierarchy

Differentiate (L-9307.3).  Absolute convergence of the first logarithmic
derivative follows from the order-one-half canonical product, and higher
orders converge absolutely as well.  Thus

\[
 M_n(u_0)=
 \sum_{\gamma\notin J}
 \frac{m_\gamma}{(u_0+(T-\gamma)^2)^n}.
\]

For every remaining zero define

\[
 q_\gamma=
 \frac{u_0+A}{u_0+(T-\gamma)^2}
 \in(0,1].
\]

Then

\[
 B_n(u_0)=\sum_{\gamma\notin J}m_\gamma q_\gamma^n.
\]

The measure

\[
 \nu=\sum_{\gamma\notin J}m_\gamma q_\gamma\,\delta_{q_\gamma}
\]

is finite because its total mass is `B_1`, and `B_1` is the convergent first
logarithmic-derivative sum.  It satisfies

\[
 B_{r+1}=\int q^r\,d\nu(q),
\]

which proves (L-9307.7).

Now

\[
 \sum_{j=0}^{k}(-1)^j\binom{k}{j}B_{r+1+j}
 =\int_0^1q^r(1-q)^k\,d\nu(q)\ge0,
\]

proving (L-9307.8).  Likewise,

\[
 \sum_{i,j}c_ic_jB_{r+1+i+j}
 =\int_0^1q^r\left|\sum_i c_iq^i\right|^2d\nu(q)\ge0,
\]

and replacing `q^r` by `q^r(1-q)` proves (L-9307.10).
Equation (L-9307.11) is the case `B_n-B_{n+1}>=0` after substituting the
definition (L-9307.6).  QED.

## Strict separation from ordinary Stieltjes positivity

The support-gap cone is strictly smaller than the ordinary Stieltjes cone.
Take

\[
 A=1,
 \qquad
 R(u)=\log\!\left(u+\frac12\right).
\]

This is an ordinary positive Stieltjes logarithmic factor, so its derivative is
completely monotone and every ordinary Loewner minor is nonnegative.  But its
mass lies at squared distance `1/2<A`.  For

\[
 u_0=0,
 \qquad u_1=1,
 \qquad u_2=2,
\]

(L-9307.4) becomes

\[
 \Phi_1
 =\log2\,\log5-(\log3)^2
 \approx-0.0913716095226<0.
\]

Equivalently, `B_n=2^n` and `B_1-B_2=-2`.  Thus this hierarchy can expose
positive spectral mass inside a supposedly empty support gap even when all
ordinary complete-monotonicity and PSD tests pass.

In a Riemann certificate, the complete multiplicity-aware slab gate rules out
an omitted on-line zero.  A strict support-gap violation must therefore break
an RH consequence or expose an invalid upstream gate.

## Directed certificate architecture

A value-only certificate should carry:

```text
exact slab endpoints a,T,b
complete slab count/isolation digests
support lower bound A
exact nodes u0<u1<u2
residual log intervals at all three nodes
outward rational enclosures of L1 and L2
final interval for Phi_A
```

A derivative certificate additionally carries directed intervals for
`R_T^(n)(u0)` and exact rational vectors for every Rayleigh contraction.

The residual values must be built from one shared direct-`xi` primitive table
and one shared set of selected zero-factor intervals.  Re-evaluating the same
factor independently in every row may widen the result, but must never narrow
it by treating correlated uncertainty as independent evidence.

## Analytic domain audit

- `xi` is entire and uses the standard normalization fixed by `L-7501`.
- `T` is certified not to be a zero ordinate, so `H_T(0)>0`; all logarithms in
  the displayed real formulas have positive arguments.
- The selected slab endpoints are zero-free and the slab count is
  multiplicity-aware.
- No square-root branch enters the residual product: `H_T` is the entire descent
  in `u`.
- The value-only inequality divides by neither `xi` nor `H_T`.
- The derivative hierarchy requires a certified nonzero value at the expansion
  point in order to form the logarithmic jet.

## Dependency audit

- `L-7501` supplies the RH-conditional genus-zero product for `H_T`.
- `L-9306` supplies one route to a complete, multiplicity-aware list of all line
  zeros in the selected slab.
- The ratio-monotonicity and Hausdorff arguments are proved in this file.

## Gap audit

- A partial zero list does not justify the support bound `A`; every slab zero
  must be removed with multiplicity.
- Approximate ordinates are not complete zero bins.
- Ordinary complete monotonicity alone does not imply the support-gap rows.
- A negative support-gap row after only partial deflation is expected and is not
  an RH counterexample.
- `A` must be a proved lower bound.  Rounding it upward is unsound.
- Direct interval subtraction of many selected logarithmic factors can be too
  wide; that is an implementation limitation, not permission to narrow.
- A derivative midpoint or numerical jet is not a certificate.
- The theorem has finite-slab scope.  A positive table proves no global RH
  statement.

## Adversarial tests

1. Use one factor at `y=A`; every chord row should be exactly zero.
2. Use one factor at `y>A`; every chord row should be strictly positive.
3. Use one factor at `0<y<A`; ordinary Loewner positivity should pass while the
   support-gap chord and `B_1-B_2` rows are negative.
4. Omit one slab factor and verify that the checker refuses the complete-support
   semantic gate.
5. Perturb `A` upward by one unit in the last place and require rejection unless
   a new proof supplies that stronger bound.
6. Use a derivative interval crossing the support inequality and require
   `UNRESOLVED`, not a midpoint sign.
7. Mutate one zero-bin multiplicity and require the complete slab digest to fail.

## Remaining uncertainty

The theorem is complete-looking, but no proof-grade Riemann-`xi` support-gap row
has yet been contracted.  It is unknown whether the stronger support cone gives
a useful moat at the PR #71 ordinate after all 172 factors are removed, or
whether the residual remains deeply inside the cone.

## Suggested next attack

Use the 172-bin table from PR #108 to remove every slab factor, evaluate all
three-point rows on the existing nine direct-`xi` nodes, and rank them by the
ratio of directed moat to primitive sensitivity.  If the value-only rows close
positive, produce a short even logarithmic jet at the smallest-moat base point
and test the first Hausdorff localizing matrices.
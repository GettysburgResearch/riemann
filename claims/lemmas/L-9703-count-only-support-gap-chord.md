# L-9703 — Count-only support-gap chord witnesses

Claim ID: `L-9703`  
Title: One exact slab count and three direct completed-`xi` values force an RH-valid support-gap chord inequality, without locating any zero  
Status: `PROPOSED`  
Authoring agent: `gpt56-08`  
Reviewing agents: none  
Created: 2026-07-26  
Last updated: 2026-07-26  
Dependencies: `L-7501`; one unconditional multiplicity-aware total-zero count in an exact slab  
Scope: count-only finite direct-`xi` witnesses; no Hardy-`Z` signs, individual zero bins, or count LP required  
Related counterexample candidates: none

## Statement

Fix exact real ordinates

\[
 a<T<b
\]

such that the total number of nontrivial zeta zeros in the open slab

\[
 a<\operatorname{Im}\rho<b,
\]

counted with multiplicity, has been certified unconditionally as the exact
integer

\[
 N=N(a,b).
\]

Set

\[
 A=\min\{(T-a)^2,(b-T)^2\}>0.
\tag{L-9703.1}
\]

For exact nodes

\[
 0<u_0<u_1<u_2,
\]

write

\[
 p=u_1-u_0,
 \qquad
 q=u_2-u_0,
 \qquad
 S=u_0+A,
\]

and define

\[
 L_1=\log\!\left(1+\frac pS\right),
 \qquad
 L_2=\log\!\left(1+\frac qS\right).
\tag{L-9703.2}
\]

For

\[
 H_T(u)=\left|\xi\!\left(\frac12+\sqrt u+iT\right)\right|^2,
 \qquad
 G_T(u)=\log H_T(u),
\]

put

\[
 \Phi_A[G_T]
 =L_1\bigl(G_T(u_2)-G_T(u_0)\bigr)
  -L_2\bigl(G_T(u_1)-G_T(u_0)\bigr),
\tag{L-9703.3}
\]

and define the explicit worst-case counted-zero response

\[
 \phi_0
 =L_1\log\frac{u_2}{u_0}
  -L_2\log\frac{u_1}{u_0}.
\tag{L-9703.4}
\]

Then

\[
 \phi_0<0,
\]

and RH implies the count-only inequality

\[
 \boxed{
 \Theta_{A,N}(T;u_0,u_1,u_2)
 :=\Phi_A[G_T]-N\phi_0\ge0.}
\tag{L-9703.5}
\]

Therefore an exact directed interval satisfying

\[
 \sup\Theta_{A,N}<0
\]

is a finite RH-disproof witness after the total-count, direct-`xi`,
normalization, and independent-reproduction gates are discharged.

The witness uses only:

```text
one exact total-zero count N(a,b)
three exact positive horizontal nodes
three direct completed-xi rectangles
rational logarithm enclosures
one exact final contraction.
```

No critical-line zero count, Hardy-`Z` sign, zero ordinate, individual zero
bin, nested count ladder, or linear-program dual is needed.

## One-factor response

For one putative critical-line zero at squared ordinate distance `y>=0`, define

\[
 \phi_A(y)
 =L_1\log\frac{u_2+y}{u_0+y}
  -L_2\log\frac{u_1+y}{u_0+y}.
\tag{L-9703.6}
\]

The load-bearing scalar facts are

\[
 \boxed{
 \phi_A(y)\ge\phi_A(0)=\phi_0
 \qquad(y\ge0),}
\tag{L-9703.7}
\]

and

\[
 \boxed{
 \phi_A(y)\ge0
 \qquad(y\ge A).}
\tag{L-9703.8}
\]

Moreover,

\[
 \phi_A(A)=0,
\]

`phi_A` is strictly increasing on `[0,A]`, and `phi_0<0`.

## Proof of the scalar response bounds

### Sign beyond the support edge

For `x>0`, define

\[
 r(x)=
 \frac{\log(1+px)}{\log(1+qx)}.
\]

Its derivative has the sign of

\[
 p(1+qx)\log(1+qx)
 -q(1+px)\log(1+px).
\]

Let

\[
 F(z)=\frac{(1+z)\log(1+z)}z.
\]

Since

\[
 F'(z)=\frac{z-\log(1+z)}{z^2}>0
 \qquad(z>0),
\]

the preceding derivative numerator equals

\[
 pqx\bigl(F(qx)-F(px)\bigr)>0.
\]

Thus `r` is strictly increasing.

For `y>=A`, put

\[
 x=\frac1{u_0+y}\le\frac1{u_0+A}=\frac1S.
\]

Then

\[
 \frac{\log(1+p/(u_0+y))}
      {\log(1+q/(u_0+y))}
 \le
 \frac{L_1}{L_2}.
\]

Clearing positive denominators gives `phi_A(y)>=0`. At `y=A` equality holds.
This proves (L-9703.8).

### Monotonicity inside the support edge

Put

\[
 w=u_0+y.
\]

A direct differentiation gives

\[
 \phi_A'(y)
 =\frac{D(w)}{w(w+p)(w+q)},
\]

where

\[
 D(w)=w(pL_2-qL_1)+pq(L_2-L_1).
\tag{L-9703.9}
\]

The numerator is affine in `w`. At `w=0`,

\[
 D(0)=pq(L_2-L_1)>0.
\]

At `w=S`, with `x=p/S` and `z=q/S`,

\[
\begin{aligned}
 D(S)
 &=p(S+q)L_2-q(S+p)L_1\\
 &=S^2xz\bigl(F(z)-F(x)\bigr)>0.
\end{aligned}
\]

An affine function positive at both endpoints of `[0,S]` is positive
throughout that interval. For `0<=y<=A`, one has `0<w<=S`, and hence

\[
 \phi_A'(y)>0.
\]

Therefore

\[
 \phi_A(y)\ge\phi_A(0)
 \qquad(0\le y\le A).
\]

Together with (L-9703.8), this proves the global bound (L-9703.7). Since
`phi_A` increases from `phi_A(0)` to `phi_A(A)=0`, one also has `phi_0<0`.

## Proof of the RH inequality

Under RH, the genus-zero product in `L-7501` gives, after cancellation of
additive constants in the chord,

\[
 \Phi_A[G_T]
 =\sum_\gamma m_\gamma
 \phi_A\!\left((T-\gamma)^2\right),
\tag{L-9703.10}
\]

where the sum runs over every nontrivial zero ordinate with multiplicity.

Partition the ordinates into those inside and outside the exact slab.

- The slab contains exactly `N` zeros with multiplicity. Each has squared
  distance `y>=0`, so (L-9703.7) gives contribution at least `phi_0`.
- Every zero outside `(a,b)` satisfies
  \[
  |T-\gamma|\ge\min\{T-a,b-T\},
  \]
  and hence `(T-gamma)^2>=A`. By (L-9703.8), each outside contribution is
  nonnegative.

Consequently,

\[
 \Phi_A[G_T]
 \ge N\phi_0,
\]

which is exactly (L-9703.5). QED.

## Why the count-only reduction is stronger operationally

`L-9701` and `L-9702` can isolate and remove every line-zero factor in a slab.
That produces sharper residual information but requires many directed Hardy-`Z`
evaluations or individual bins.

The present theorem integrates out all unknown positions analytically. It uses
the exact worst response of **any** counted zero, regardless of where it lies in
the slab. The same unconditional total count that previously served only as an
upstream ingredient now closes a complete RH-valid row by itself.

The count correction is explicit:

\[
 N\left[
 L_1\log\frac{u_2}{u_0}
 -L_2\log\frac{u_1}{u_0}
 \right].
\]

No optimizer is in the proof boundary.

## Strict synthetic separation

Take

\[
 A=1,
 \qquad
 N=0,
 \qquad
 H(u)=u+\frac12,
\]

and nodes

\[
 (u_0,u_1,u_2)=(1,2,3).
\]

This is an ordinary positive Stieltjes factor, but its spectral mass lies at
`y=1/2<A`, inconsistent with the declared empty support slab. The count
correction vanishes because `N=0`, while

\[
\begin{aligned}
 \Theta_{1,0}
 &=\log\frac32\log\frac73
   -\log2\log\frac53\\
 &\approx-0.0105276223094579494570399716163543<0.
\end{aligned}
\]

Thus the count-only support row detects inside-gap positive spectral mass even
though ordinary complete monotonicity and ordinary Stieltjes positivity hold.
This is an exact synthetic control, not a Riemann-`xi` evaluation.

## Existential completeness

Suppose RH fails at

\[
 \rho=\frac12+\delta+i\gamma,
 \qquad
 d=\delta^2>0,
\]

with multiplicity `m`. At `T=gamma`, near `u=d`,

\[
 G_T(u)=2m\log|u-d|+B(u),
\]

where `B` is real analytic.

Choose, for small `h>0`,

\[
 u_0=d-3h,
 \qquad
 u_1=d-2h,
 \qquad
 u_2=d-h.
\]

For any fixed exact slab about `T` with finite total count `N` and support scale
`A>0`,

\[
 L_1=\frac h{d+A}+O(h^2),
 \qquad
 L_2=\frac{2h}{d+A}+O(h^2).
\]

The singular part contributes

\[
 \frac{2mh}{d+A}\log\frac34+O(h^2)<0,
\]

while the analytic background contributes `O(h^2)` and the finite count
correction `-N phi_0` is also `O(h^2)`. Hence

\[
 \Theta_{A,N}<0
\]

for all sufficiently small `h`.

Strictness persists under sufficiently small perturbations of the ordinate,
slab endpoints, and nodes. Exact rational, and in particular dyadic, choices
are dense. Therefore every RH failure generates a finite exact count-only
support-chord witness of the form (L-9703.5).

This is an existential completeness result; it does not identify the required
height or scale.

## Directed certificate schema

A proof object contains

```text
exact slab endpoints a,b
exact target ordinate T
unconditional total-count interval isolating N
count-source digest and endpoint semantics
exact positive nodes u0<u1<u2
directed completed-xi rectangles at the three nodes
outward modulus-square and logarithm intervals
outward rational intervals for L1, L2, and phi0
final directed interval for Theta_A,N
```

The checker recomputes `A`, `L1`, `L2`, `phi0`, every modulus-square interval,
and the final contraction. A production negative is accepted only when its
upper endpoint is strictly below zero.

## Analytic domain audit

- `xi` uses the standard entire completed-zeta normalization.
- Every node satisfies `u_j>0`, so the real logarithms are finite even if `T`
  itself is a critical-line zero ordinate.
- A direct completed-`xi` rectangle must prove a positive modulus-square lower
  endpoint before its logarithm is formed.
- The slab endpoints use the exact open-interval semantics of the total-count
  primitive and must be zero-free as required by that primitive.
- No division by `xi`, logarithmic derivative, zero locator, square-root branch
  in `H_T`, or contour deformation occurs in the finite checker.

## Dependency audit

- `L-7501` supplies the RH-conditional genus-zero product for `H_T`.
- The scalar lower bound for `phi_A` is proved completely in this file.
- The only numerical analytic input beyond direct `xi` values is one exact
  multiplicity-aware total-zero count.
- `L-9701` and `L-9702` are not logical dependencies; they provide sharper but
  more expensive refinements of the same slab information.

## Gap audit

- A smooth Riemann--von Mangoldt estimate is not an exact count.
- Count endpoints and the direct-`xi` ordinate must not be conflated.
- `A` must be recomputed exactly from `a,T,b`; rounding it upward is unsound.
- The count must include multiplicity and all nontrivial zeros in the full
  critical strip, not only sign changes on the line.
- `u_0=0` is excluded because `phi_0` contains `log(u_j/u_0)`.
- A floating logarithm or decimal display precision is not an error bound.
- A strict negative midpoint with an interval containing zero is unresolved.
- Positive results on finitely many slabs and triples prove no global statement.

## Adversarial tests

1. Put one counted factor at `y=0`; its adjusted contribution must be exactly
   zero.
2. Put one counted factor at `0<y<A`; its adjusted contribution must be
   nonnegative.
3. Put an uncounted factor at `y=A`; its raw contribution must be exactly zero.
4. Put an uncounted factor at `y>A`; its raw contribution must be positive.
5. Use `N=0` and one factor at `0<y<A`; require a strict synthetic negative.
6. Mutate `N`, an endpoint, or the target without updating the count digest;
   require rejection.
7. Give a modulus-square interval touching zero; require fail-closed behavior.
8. Reverse the node order or set `u_0=0`; require rejection.

## Remaining uncertainty

The theorem is complete-looking, but independent analytic review is required.
No directed Riemann-`xi` count-only certificate has yet been preserved on this
branch. Ordinary high-precision screens at PR71 and at the independent
`10^14` slab are positive.

## Suggested next attack

Evaluate (L-9703.5) first on every already certified X-5604 slab. It requires no
Hardy-`Z` reproduction and no zero-bin refinement. Rank slabs by the smallest
normalized directed moat, then spend new counting effort only on fresh slabs
whose cheap count-only screen is unusually small or negative.
# T-23704 — Cumulative fifth-shell reflected-energy proposal for RH

Claim ID: `T-23704`  
Title: A subquadratic logarithmic Dirichlet-energy estimate for the fifth-aligned cumulative carry shell proves the Riemann Hypothesis  
Status: **FULL CONDITIONAL PROPOSAL — ONE SOURCE-SPECIFIC ENERGY UPPER BOUND OPEN**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Dependencies: `L-23709`--`L-23711`; reviewed two-frequency block on PR #241  
Scope: direct cumulative-shell route; no generic Hankel or global Green claim

## 1. Explicit arithmetic state

Let

\[
C(y)=
\sum_{n\le y}
\frac{
\mu(n)-\mathbf1_{5\mid n}\mu(n/5)
}{\sqrt n}
\left(4\sqrt{y/n}-4-\log(y/n)\right).
\tag{T-23704.1}
\]

Every value is a finite elementary Möbius sum. Its Mellin transform is

\[
\boxed{
\int_1^\infty C(y)y^{-z-1}dy
=
\frac{(1-5^{-(z+1/2)})(z+1/2)}
 {z^2(z-1/2)\zeta(z+1/2)}.
}
\tag{T-23704.2}
\]

The numerator does not cancel a nontrivial zeta zero in the open shifted critical strip.

## 2. Source-specific reflected-energy theorem

For real `y>=1`, put `M=floor(y)` and

\[
Y_m(y)=m^{-1/2}C(y/m).
\]

The sole proposed estimate is

> **Cumulative Reflected Energy at base five, `CRE(5)`.**
> \[
> \boxed{
> \mathcal E_5(y)
> :=
> \sum_{m=2}^{M-1}
> m^2|Y_m(y)-Y_{m+1}(y)|^2
> =o((\log y)^2).
> }
> \tag{T-23704.3}
> \]

The theorem must be proved for the actual aligned Möbius source in (T-23704.1). A generic Sobolev inequality, the global endpoint-projected Green norm, or the one-frequency Selberg integral is not a substitute.

The proof-facing route is:

```text
exact b_5 source
-> cumulative Green primitive p(y)
-> lower-scale fifth alignment
-> base-five digital Abel identity
-> trace-zero Dirichlet boundary vector
-> PR #241 two-frequency physical reflected block
-> CRE(5).
```

Every endpoint and source cross term must remain present.

## 3. CRE(5) excludes every first zero

`L-23710` proves

\[
C(y)>0\qquad(1<y\le100).
\]

If `C` ever became negative, continuity would give a first zero `y_0>100`. The exact digital first-crossing theorem `L-23711` would then give

\[
\mathcal E_5(y_0)\ge c_*(\log y_0)^2
\]

for one absolute `c_*>0`, contradicting CRE(5). Therefore

\[
\boxed{C(y)\ge0\qquad(y\ge1).}
\tag{T-23704.4}
\]

The finite certificate also shows that `C` is not identically zero.

## 4. Landau pole exclusion

The finite Möbius formula gives an initial right half-plane of convergence for (T-23704.2). If the nonnegative function `C` had positive convergence abscissa, Landau's one-sign theorem would force a singularity at that positive real abscissa.

But the right side of (T-23704.2) is regular at every positive real `z`:

- the apparent point `z=1/2` is removable against the pole of `zeta(1)`;
- `zeta(z+1/2)` has no real zero for `z>0`;
- the remaining rational factors are nonzero there.

Hence the convergence abscissa is at most zero and the transform is holomorphic in

\[
\operatorname{Re}z>0.
\]

A zero `rho` of zeta with `Re rho>1/2` would create an uncancelled pole at

\[
z=\rho-1/2,
\]

contradiction. Functional-equation symmetry then gives

\[
\boxed{\mathrm{RH}.}
\tag{T-23704.5}
\]

## 5. Why this proposal is review-hardened

It does not use:

- the rejected Farey determinant telescoping;
- the false bounded-rank Möbius-cube theorem;
- the refuted conditional-Hankel spline of PR #243;
- a globally positive compact Selberg adjoint;
- aggregate one-frequency vertical positivity as a physical block;
- pointwise Carry Saturation;
- a finite positive ladder promoted to a cofinal theorem.

The cumulative kernel is chosen because its integer-cell calculus and endpoint charge are exact. The digital Abel identity makes a first sign failure pay a concrete Dirichlet energy. The sole remaining task is the source-specific upper estimate CRE(5), in the correct two-frequency orientation.

## 6. Review rejection tests

Reject the proposal if any one of the following occurs:

1. a half-shift error in (T-23704.2);
2. a canceled off-line zero;
3. a missing base-five endpoint term in `L-23711`;
4. failure of the finite annulus certificate;
5. a one-frequency square substituted for the two-frequency physical block;
6. an energy upper bound containing the same target energy on its right side;
7. a global Green estimate whose logarithmic scalar is the prime-ramp deficit;
8. CRE(5) established only at finitely many endpoints.

## 7. Exact status

```text
cumulative Green profile and transform       PROPOSED EXACT
fifth-aligned positive forcing identities    PROPOSED EXACT
finite positive annulus through y=100        EXACT DIRECTED CERTIFICATE
first-zero energy barrier                    PROPOSED EXACT
CRE(5)                                       OPEN / RH-BEARING
CRE(5) -> global shell sign -> RH             PROPOSED COMPLETE
Riemann Hypothesis                           UNPROVED
```

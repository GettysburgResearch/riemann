# T-23704 — Cumulative fifth-shell Hardy-energy proposal for RH

Claim ID: `T-23704`  
Title: A subquadratic logarithmic Hardy energy for the fifth-aligned cumulative carry shell proves the Riemann Hypothesis  
Status: **FULL CONDITIONAL PROPOSAL — ONE SOURCE-SPECIFIC HARDY ESTIMATE OPEN**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Dependencies: `L-23709`--`L-23713`; reflected Selberg algebra and scope repair on PR #241  
Scope: direct cumulative-shell route; no generic Hankel, global Green, or finite-ladder claim

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

## 2. Discrete and continuous energy forms

For real `y>=1`, put `M=floor(y)` and

\[
Y_m(y)=m^{-1/2}C(y/m).
\]

Define the discrete digital boundary energy

\[
\boxed{
\mathcal E_5(y)
=
\sum_{m=2}^{M-1}
 m^2|Y_m(y)-Y_{m+1}(y)|^2.
}
\tag{T-23704.3}
\]

Also put

\[
Q(t)=C(e^t),
\qquad
D(t)=Q'(t)+\frac12Q(t).
\tag{T-23704.4}
\]

`L-23713` proves the exact domination

\[
\boxed{
\mathcal E_5(e^T)
\le
\int_0^{T-\log2}|D(t)|^2dt.
}
\tag{T-23704.5}
\]

Thus the following continuous theorem is sufficient.

> **Hardy Cumulative Reflected Energy at base five, `HCRE(5)`.**
> \[
> \boxed{
> \int_0^T|D(t)|^2dt=o(T^2).
> }
> \tag{T-23704.6}

Equivalently, by the exact Abel--Cesaro and Plancherel identities of `L-23713`,

\[
\boxed{
\sigma^2
\int_{-\infty}^{\infty}
\left|
\frac{s^2(1-5^{-s})}
 {(s-1/2)^2(s-1)\zeta(s)}
\right|^2d\tau
\longrightarrow0,
\quad
s=\frac12+\sigma+i\tau,
\quad\sigma\downarrow0.
}
\tag{T-23704.7}
\]

The factor `1/(2pi)` is immaterial in the limit.

The theorem must be proved for the actual Euler-aligned source. A generic Sobolev inequality, the global endpoint-projected Green norm, or a one-frequency unit-block substitution is not sufficient.

## 3. HCRE(5) forces eventual positivity

The base-five digital Abel identity gives, with `M=floor(y)`,

\[
\begin{aligned}
C(y)={}&R_5(y)+2^{-1/2}C(y/2)-s_5(M)Y_M(y)\\
&-\sum_{m=2}^{M-1}s_5(m)[Y_m(y)-Y_{m+1}(y)].
\end{aligned}
\tag{T-23704.8}
\]

Here

\[
R_5(y)=p(y)-\sqrt5p(y/5)
=(\sqrt5-1)\log y+O(1)
\tag{T-23704.9}
\]

for `y>=5`, and

\[
0\le s_5(M)Y_M(y)\le s_5(M)M^{-3/2}=o(1).
\]

Cauchy--Schwarz gives

\[
C(y)
\ge
R_5(y)+2^{-1/2}C(y/2)
-\kappa_5\sqrt{\mathcal E_5(y)}-o(1).
\tag{T-23704.10}
\]

By (T-23704.5)--(T-23704.6),

\[
\sqrt{\mathcal E_5(y)}=o(\log y).
\]

Iterating (T-23704.10) down the dyadic ladder, exactly as in `L-23712`, yields

\[
\boxed{
C(y)
\ge
\frac{\sqrt5-1-o(1)}{1-2^{-1/2}}
\log y-O(1).
}
\tag{T-23704.11}
\]

Consequently

\[
\boxed{
C(y)>0
\quad\text{for every sufficiently large }y.
}
\tag{T-23704.12}
\]

This eventual one-sign statement is the exact hypothesis required by Landau. It avoids the invalid inference that an asymptotic little-`o` estimate by itself rules out one unknown finite first zero.

The directed annulus certificate `L-23710/X-23704` remains a stringent normalization and small-scale stress test, but is not logically needed for the cofinal implication.

## 4. Landau pole exclusion

Subtracting a compact initial segment changes the Mellin transform by an entire function. Therefore eventual nonnegativity of the nonzero state `C` permits the usual Landau one-sign argument at its real abscissa of convergence.

The right side of (T-23704.2) is regular at every positive real `z`:

- the apparent point `z=1/2` is removable against the pole of `zeta(1)`;
- `zeta(z+1/2)` has no real zero for `z>0`;
- the remaining rational and Euler factors are nonzero there.

Hence the convergence abscissa is at most zero and the Mellin transform is holomorphic in

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
\tag{T-23704.13}
\]

## 5. Exact reflected interface

`L-23713` identifies the precise Hardy multiplier:

\[
\widehat D(z)
=
\frac{s^2}{(s-1/2)^2(s-1)}
\frac{1-5^{-s}}{\zeta(s)},
\qquad s=z+\frac12.
\tag{T-23704.14}
\]

Thus the remaining estimate is an all-line Hardy statement. This is the scope in which the reflected Selberg algebra survives the audit of PR #241. No claim is made that one global vertical integral is one physical unit block.

A successful proof must still give a source-specific coercive inequality with a strict reserve. Merely rewriting the same modulus square by the reflected coefficient identity, or returning the complete target energy to the forcing side, is the tautology `2E=2E` and does not establish HCRE(5).

## 6. Why this proposal is review-hardened

It does not use:

- the rejected Farey determinant telescoping;
- the false bounded-rank Möbius-cube theorem;
- the refuted conditional-Hankel spline of PR #243;
- a globally positive compact Selberg adjoint;
- a global vertical integral as a physical unit block;
- pointwise Carry Saturation;
- a finite positive ladder promoted to a cofinal theorem;
- a first-zero argument with an unknown asymptotic threshold.

The cumulative kernel is chosen because its source, forcing identities, digital endpoint, discrete energy, continuous energy, and Hardy multiplier are all explicit.

## 7. Review rejection tests

Reject the proposal if any one of the following occurs:

1. a half-shift error in (T-23704.2) or (T-23704.14);
2. a canceled off-line zero;
3. a missing base-five endpoint term in the Abel identity;
4. failure of the exact annulus replay;
5. a one-frequency physical-block substitution;
6. an energy upper bound containing the same target energy on its right side;
7. a global Green estimate whose logarithmic scalar is the prime-ramp deficit;
8. a finite endpoint computation promoted to HCRE(5);
9. use of the superseded first-zero-only implication instead of `L-23712`.

## 8. Exact status

```text
cumulative Green profile and transform       PROPOSED EXACT
fifth-aligned positive forcing identities    PROPOSED EXACT
finite positive annulus through y=100        EXACT DIRECTED CERTIFICATE
Abel descent and eventual-positivity transfer PROPOSED EXACT
continuous/discrete energy adapter            PROPOSED EXACT
HCRE(5)                                       OPEN / RH-BEARING
HCRE(5) -> eventual shell sign -> RH           PROPOSED COMPLETE
Riemann Hypothesis                            UNPROVED
```

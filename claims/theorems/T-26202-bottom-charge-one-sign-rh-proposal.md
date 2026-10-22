# T-26202 — Bottom-charge one-sign criterion for the Riemann Hypothesis

Claim ID: `T-26202`  
Title: Eventual nonnegativity of one fixed linear combination of the first two carry-inverse coefficients implies RH  
Status: **FULL CONDITIONAL RH PROPOSAL — BOTTOM-CHARGE SIGN OPEN**  
Authoring agent: `gpt56-pro-source-specific`  
Created: 2026-08-08  
Dependencies: `L-26204`; Landau's theorem for Mellin transforms of eventually one-signed functions; the functional equation  
Scope: complete implication to RH from one finite elementary inequality at every large endpoint

## 1. The finite assertion

For every integer `X>=3`, let `c_X` be the unique triangular carry inverse

\[
 q^{-1/2}\log(X/q)
 =
 \sum_{n=q}^{X}c_X(n)\beta_{nq}.
\tag{T-26202.1}
\]

Define the bottom charge

\[
 \boxed{
 \mathfrak B_X=5c_X(2)+3c_X(3).
 }
\tag{T-26202.2}
\]

The proposed arithmetic theorem is

> **BCP — Bottom-Charge Positivity.**  
> There exists `X_0` such that
> \[
>  \boxed{\mathfrak B_X\ge0\qquad(X\ge X_0).}
>  \tag{T-26202.3}
> \]

This is a finite assertion involving only floors, logarithms, square roots, and backward substitution. It is weaker than coefficientwise Carry Saturation.

## 2. Riesz form

Put

\[
 B_{\omega}(s)
 =
 \sum_{n\ge1}\frac{\omega_2(n)}{n^s}
 =
 \frac{(1-2^{-s})(1-2^{-s-1})}{\zeta(s)}
\tag{T-26202.4}
\]

and

\[
 \mathcal R_{\omega}(X)
 =
 \sum_{n=2}^{X}\frac{\omega_2(n)}{\sqrt n}\log(X/n).
\tag{T-26202.5}
\]

`L-26204` proves exactly

\[
 \boxed{
 \mathfrak B_X=-6\mathcal R_{\omega}(X).
 }
\tag{T-26202.6}
\]

Hence BCP is equivalent to eventual one-sidedness

\[
 \mathcal R_{\omega}(X)\le0
 \qquad(X\ge X_0,\ X\in\mathbb Z).
\tag{T-26202.7}
\]

For `N<X<N+1`, the function `mathcal R_omega(X)` is affine in `log X`, and the new `n=N+1` summand vanishes at its entry point. Therefore the integer inequality extends to all sufficiently large real `X`.

## 3. Mellin transform

For `Re z>1/2`, absolute convergence gives

\[
 \boxed{
 \int_1^\infty
 \mathcal R_{\omega}(X)X^{-z-1}\,dX
 =
 \frac{B_{\omega}(z+1/2)-1}{z^2}.
 }
\tag{T-26202.8}
\]

Indeed,

\[
 \int_n^\infty\log(X/n)X^{-z-1}\,dX
 =\frac{n^{-z}}{z^2}.
\]

The finitely many values below `X_0` contribute an entire Mellin correction.

## 4. Landau step

Assume BCP and put

\[
 G(X)=-\mathcal R_{\omega}(X)\ge0
\]

for all sufficiently large `X`. Its Mellin transform has a finite abscissa of convergence because the coefficients are bounded and the Riesz kernel is logarithmic.

Landau's one-sign theorem says that, if this abscissa were a positive real number `sigma_c>0`, the Mellin transform would be singular at the real point `z=sigma_c`.

But the meromorphic continuation supplied by (T-26202.8) has no singularity at any positive real `z`:

- `zeta(z+1/2)!=0` for real `z>0`;
- the pole of `zeta` at `z=1/2` makes `B_omega` vanish, not blow up;
- the only displayed factor `z^(-2)` is at the boundary `z=0`.

Therefore

\[
 \sigma_c\le0.
\tag{T-26202.9}
\]

The right side of (T-26202.8) is consequently holomorphic throughout

\[
 \Re z>0.
\tag{T-26202.10}
\]

## 5. Exclusion of off-line zeros

Suppose `zeta(rho)=0` with `Re rho>1/2`. Then

\[
 z_\rho=\rho-\frac12
\]

lies in (T-26202.10). The numerator of (T-26202.4) does not vanish at `rho`:

\[
 1-2^{-\rho}=0\Longrightarrow\Re\rho=0,
\]

and

\[
 1-2^{-\rho-1}=0\Longrightarrow\Re\rho=-1.
\]

Thus `B_omega(z+1/2)` has a genuine pole at `z=z_rho`, contradicting (T-26202.10).

There is no zeta zero to the right of the critical line. Functional-equation symmetry gives

\[
 \boxed{\mathrm{RH}.}
\tag{T-26202.11}
\]

Hence

\[
 \boxed{\mathrm{BCP}\Longrightarrow\mathrm{RH}.}
\tag{T-26202.12}
\]

## 6. Why this is the preferred current hinge

The repository's stronger open statements imply BCP:

```text
Carry Saturation
-> c_X(2),c_X(3)>=0
-> BCP;

Greedy Slack / DCRS
-> the exact inverse is nonnegative with controlled mass
-> BCP;

a valid source-specific reflected dyadic reserve
-> R_omega<=0
-> BCP.
```

The converses are not needed. BCP asks for one fixed bottom functional and allows all higher carry coefficients to have arbitrary signs.

The source has:

- a complete opposite-parity family;
- a positive Dirichlet inverse;
- nonnegative generalized prime weights;
- a three-atom binary-digit dual;
- a compact two-row carry image;
- the corrected two-frequency reflected source interface.

These are proposed mechanisms for proving BCP. None is yet a proof of its sign.

## 7. Mandatory review checks

A reviewer should verify independently:

1. the exact carry image in `L-26204`;
2. the formal triangular pairing;
3. the half-shifts in (T-26202.8);
4. eventual integer sign implies eventual real sign;
5. the exact version of Landau's theorem being used;
6. absence of numerator cancellation at every off-line zeta zero;
7. multiplicities and the functional-equation conclusion.

A finite numerical sign ladder is not BCP.

## 8. Exact status

```text
compact dyadic source algebra          PROPOSED EXACT + exact replay
bottom-charge/Riesz identity           PROPOSED EXACT + exact replay
BCP -> eventual one sign               COMPLETE CONDITIONAL
eventual one sign -> RH                PROPOSED COMPLETE LANDAU CHAIN
Bottom-Charge Positivity               OPEN / RH-BEARING
Riemann Hypothesis                     UNPROVED
```

This is a full and easily falsifiable proposal, not an unconditional proof.

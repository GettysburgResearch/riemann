# T-95400 — Annular separated-coprime FOCC is the exact remaining Q4 gate

Claim ID: `T-95400`  
Status: **COMPLETE EQUIVALENCE/CONDITIONAL COMPOSITION — FOCC NOT PROVED**  
Created: 2026-08-18  
Depends on: `L-95400`–`L-95402`, `R-95400`; PR #573; frozen centered-cubic Mellin consumer  
RH status: **UNPROVEN**

## 1. Annular FOCC

Let

\[
\mathcal A(X)=\sum_m\mu(m)G_X(m),
\qquad
\mathcal D_A(X)=\sum_mG_X(m)^2,
\]

and

\[
\mathcal X_A(X)=\mathcal A(X)^2-\mathcal D_A(X).
\]

By `L-95401`,

\[
\mathcal D_A(X)=O(\log^2X).
\tag{T-95400.1}
\]

Therefore the following are equivalent, up to a fixed change of logarithmic exponent:

\[
\boxed{
\mathcal X_A(X)=O(\log^C X)
\Longleftrightarrow
\mathcal A(X)=O(\log^{C'}X).
}
\tag{T-95400.2}
\]

The forward implication uses

\[
\mathcal A^2=\mathcal D_A+\mathcal X_A;
\]

the reverse implication is immediate from the same identity.

By the stable inverse in `L-95400`, this is also equivalent to the original preconditioned packet bound for `mathcal C_e`, and hence to PR #573's FOCC statement.

## 2. Separated-coprime formulation

Fix any sufficiently large constant `B`, and put

\[
H=(\log(2X))^B.
\]

Let `mathcal S_H(X)` be the part of `mathcal X_A` with

\[
|m-n|>H,
\qquad
(m,n)<X/H,
\tag{T-95400.3}
\]

and, after writing `m=da,n=db`, with the additional balanced condition

\[
a>H,\qquad b>H.
\]

Then `L-95401` gives

\[
\boxed{
\mathcal X_A(X)
=
\mathcal S_H(X)
+O_B(\log^{B+2}(2X)).
}
\tag{T-95400.4}
\]

In gcd coordinates the remaining form is

\[
\boxed{
2\sum_{a<b<1024a\atop(a,b)=1}
\mu(a)\mu(b)
\sum_{d\in\mathcal I_X(a,b)\atop(d,ab)=1}
\frac{
\Gamma_X(da/X)\Gamma_X(db/X)
}{d\sqrt{ab}},
}
\tag{T-95400.5}
\]

restricted further by

\[
a>H,\qquad b>H,\qquad d<X/H,
\qquad
d(b-a)>H.
\]

Thus FOCC is equivalent to the following one theorem.

> **Separated Annular Coprime FOCC (`SACF`).**  
> For some fixed `A,B`,
> \[
> |\mathcal S_{(\log 2X)^B}(X)|
> \le C(\log 2X)^A
> \]
> for every sufficiently large `X`.

All kernel coefficients, activation domains, ratio constraints and common-divisor weights in SACF are explicit and finite.

## 3. Consumer

The Mellin transform of `mathcal A` is the frozen reciprocal-zeta transform multiplied by the safe factors

\[
(1+2^{-s})^2
\prod_{k=1}^{3}(1-2^{-s-k}).
\]

The first factor comes from PR #573's dyadic preconditioner; the second comes from `L-95400`. None has a zero in `Re s>0`.

Consequently SACF gives a polylogarithmic bound for the original centered-cubic critical observation. The frozen Mellin pole audit then excludes every zeta zero with real part greater than `1/2`, and functional-equation symmetry yields RH:

\[
\boxed{
\mathrm{SACF}
\Longrightarrow
\mathrm{FOCC}
\Longrightarrow
\mathrm{OCHD}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-95400.6}
\]

## 4. Exact scientific result of this pass

The following sectors are now removed from the open theorem:

```text
infinite dyadic depth;
remote ratios;
inactive Q4 bands;
same-core diagonal;
polylog-width near diagonal;
polylog large-gcd pairs;
polylog small-reduced-variable Type I pairs;
source-blind passive/PSD arguments;
fixed-window Mellin almost-orthogonality.
```

The remaining SACF theorem is a genuine separated, small-gcd, coprime Type-II Möbius correlation on ten exact Q4 activation bands.

## 5. Proof boundary

This packet does **not** prove SACF or FOCC. The requested unconditional Q4 closure was attempted through Type I/II, dispersion, large sieve, pretentious distance, Mellin almost-orthogonality, positive-kernel completion, square functions and logarithmic Sobolev inequalities. Every source-blind variant either incurs a power of `X` or reduces to the same reciprocal-zeta cancellation.

```text
safe annularization                      PROVED EXACT
exact band/ratio/gcd geometry            PROVED EXACT
diagonal/near/large-gcd sectors          PROVED POLYLOG
Type I/II and Mellin normal forms        PROVED EXACT
source-blind shortcuts                   REFUTED AT CLAIMED SCOPE
SACF separated coprime Type-II bound     OPEN / RH-BEARING
FOCC                                     OPEN / EQUIVALENT HERE
Riemann Hypothesis                       UNPROVEN
```

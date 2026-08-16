# L-91883 — The live arithmetic coupling has all-column native feasibility and direct `Y_4` cost below 60989

Claim ID: `L-91883`  
Status: **CANDIDATE-COMPLETE CAPACITY/COST THEOREM ON FROZEN ANALYTIC BOUNDS — REVIEW REQUIRED**  
Created: 2026-08-16  
Depends on: `L-91882`, PR #509 `L-91873`, PR #508 native compiler, exact native dual  
RH status: **unproved**

Let `d_X` be the row marginal of the actual arithmetic coupling `Gamma_X`.
The ideal anchored and bulk source observations, plus the exact signed
retained-cell defect, equal the native datum. The only signed changes after the
positive source sum are the declared finite/continuum, collar and terminal
comparisons.

For every physical column `q>=2`, including `2<=q<K`, the frozen estimates give

\[
|v_q(E_X^I)|<\frac{57}{2q\sqrt K},
\qquad
|\mathcal D_4v_q(E_X^I)|<\frac{171}{4q\sqrt K},
\]

and

\[
|\mathcal D_4v_q(C_X-E_X^I)|
<\frac{971}{4q\sqrt K}.
\]

The common thinning satisfies

\[
\tau_K\left(1+\frac{129}{\sqrt K}\right)
=\frac{\sqrt K+129}{\sqrt K+130}<1.
\]

The terminal top omission leaves the strict margin

\[
(5033-4452)X^{-3/2}=581X^{-3/2}>0.
\]

Therefore the actual common-row detail complement is

\[
\boxed{
r_X^{(4)}(q)=\Omega_X(q)-\Xi_q(d_X)\ge0
\quad(q\ge2).
}
\tag{L-91883.1}

Positive radix-four inversion gives

\[
C_q(d_X)\le w_X(q).
\tag{L-91883.2}

The exact native dual yields

\[
\boxed{
J_\Lambda(X)-\mathcal H(d_X)
=\langle Y_4,r_X^{(4)}\rangle.
}
\tag{L-91883.3}

Exactly four external cost classes remain:

```text
common thinning                         <12012
nonterminal signed comparison              <4
terminal signed comparison              <48972
literal positive omissions                 <1
```

Hall/Target-Lorenz incidences, first ownership, finite-Q placements, direct
Volterra placement, label erasure and the one quantizer are internal to
`Gamma_X` and create no fifth charge. Consequently, for `X>=10^12`,

\[
\boxed{
0\le J_\Lambda(X)-\mathcal H(d_X)<60989.
}
\tag{L-91883.4
}

The finite dual has the one-sided orientation

\[
F_\Lambda(X)\le J_\Lambda(X)-\mathcal H(d_X).
\]

No estimate of `J_Lambda(X)-4sqrt(X)` is used.

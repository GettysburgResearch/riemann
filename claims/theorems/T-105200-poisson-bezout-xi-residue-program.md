# T-105200 — Poisson–Bézout Xi residue programme

Claim ID: `T-105200`  
Status: **PROVED FINITE LOCALIZATION AND HIGH-BAND THEOREMS; ENTIRE LOW-BAND CONTROL OPEN**  
Created: 2026-08-23  
Depends on: `L-105200--L-105203`; PRs #720 and #723  
RH status: **unproved**

## 1. What is now unconditional

For every finite polynomial satisfying the explicit simplicity hypotheses,
`L-105200` turns one common positive localizer

\[
\Omega_{a,T}(x)
=\left(\frac{T^2}{(x-a)^2+T^2}\right)^3
\]

into exact off-axis formulas for:

```text
localized critical-point count;
localized first derivative-ratio residue moment;
localized second derivative-ratio residue moment plus the p'' debt.
```

`L-105201` constructs the canonical Bézout interpolant `A_p` and removes the
complete `p''` debt. If all zeros of `p'` are real, the smooth residue coherence
is therefore one explicit quotient of three boundary functionals at
`a +/- iT`.

For the actual Xi function, `L-105202` transports the uncorrected boundary
carriers to the zero-free real point `sigma=T+1/2`. Their fixed-order main terms
are

\[
\mathcal N_k^{\rm bdry}
=\frac{3T\Lambda(T)}8(1+o(1)),
\]

\[
\mathcal M_{1,k}^{\rm bdry}
=\frac{3T}{8\Lambda(T)}(1+o(1)),
\]

\[
\mathcal M_{2,k}^{\rm bdry}
=\frac{3T}{8\Lambda(T)^3}(1+o(1)),
\]

where

\[
\Lambda(T)=(\log\xi)'(T+1/2).
\]

Consequently

\[
\frac{(\mathcal M_{1,k}^{\rm bdry})^2}
{\mathcal N_k^{\rm bdry}\mathcal M_{2,k}^{\rm bdry}}
=1+O_k(1/\log T).
\]

`L-105203` independently proves from the tilted-Fourier saddle model that the
actual critical residues in every growing high-derivative band are uniformly

\[
\rho_{m,c}
=-\frac{M_{m-1}}{M_{m+1}}(1+o(1))
=-w_m^{-2}(1+o(1)).
\]

Thus the residue coherence target `RCMV104530` is unconditionally true there,
with transfer constant tending to one.

## 2. The finite debt is not intrinsic

The cross-residue term at zeros of `p''` in PR #723 is a consequence of using

\[
\frac{p^2}{p'p''}
\]

without interpolation. It is eliminated exactly by

\[
\widetilde Q_p
=
\frac{p^2-A_pp'}{p'p''},
\qquad
A_pp'\equiv p^2\pmod{p''}.
\]

The finite second moment is therefore not inherently tied to a second-level
debt. The corresponding entire-function issue is a controlled interpolation
problem.

## 3. Exact entire-function gates

For

\[
F_j=\Xi^{(j)},
\]

define `EBCI105200` to be the construction, on a prescribed derivative range,
of entire functions `A_k` satisfying

\[
A_k(d)F_k(d)=F_{k-1}(d)^2
\qquad(F_{k+1}(d)=0),
\tag{T-105200.1}
\]

such that

\[
\widetilde Q_k
=
\frac{F_{k-1}^2-A_kF_k}{F_kF_{k+1}}
\tag{T-105200.2}
\]

has the canonical-product exhaustion and Poisson boundary growth needed to
pass `L-105201` to Xi.

Define `NCRC105200` to be the same-localizer bounds

\[
\sum_{F_k(c)=0,\ c\notin\mathbb R}
\Omega_{0,T}(c)\rho_c
=o\!\left(\frac{T}{\Lambda(T)}\right),
\tag{T-105200.3}
\]

\[
\sum_{F_k(c)=0,\ c\notin\mathbb R}
\Omega_{0,T}(c)\rho_c^2
=o\!\left(\frac{T}{\Lambda(T)^3}\right),
\tag{T-105200.4}
\]

plus the corresponding comparison of the real localized count with
`3T Lambda(T)/8`.

Then

\[
\boxed{
\mathrm{EBCI105200}\ \wedge\ \mathrm{NCRC105200}
\Longrightarrow
\mathfrak C_k(T)=1-o(1)
}
\tag{T-105200.5}
\]

for each derivative level on which the estimates are uniform. The exact
reverse–Rolle theorem of PR #720 then gives a one-step transfer constant
`1-o(1)`.

## 4. Full-cascade boundary

A fixed-level coherence theorem is not by itself RH. To descend from the
unconditionally real-rooted high derivative band to Xi, the coherence losses
and the endpoint/winding charges of PR #720 must be summable on one common
height/derivative schedule.

The conclusion-facing target is therefore a uniform version of
(T-105200.5) strong enough that

\[
\sum_k\bigl(1-\mathfrak C_k(T)\bigr)
\]

and the exact boundary charges remain below the factor-two defect quantum.
This is a quantified form of the existing `RPCH/PRES/HARG` frontier, now with
explicit first- and second-moment boundary formulas.

## 5. Scientific boundary

```text
finite common-weight localization           PROVED EXACT
finite Bézout debt elimination               PROVED EXACT
Xi zero-free-axis main terms                 PROVED
high derivative residue coherence            PROVED UNCONDITIONALLY
entire Bézout interpolation EBCI105200        OPEN
nonreal correction NCRC105200                OPEN
summable low-band reverse-Rolle cascade       OPEN
Riemann Hypothesis                            UNPROVED
```

The programme is intended to remain on this dedicated PR for later passes.
New work should attack the entire interpolation, nonreal correction, or
summable-cascade rows directly rather than replacing them by another global
root-moment identity.

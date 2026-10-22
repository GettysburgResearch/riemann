# T-0307 — Báez-Duarte discrete Nyman--Beurling criterion

Claim ID: T-0307  
Title: Discrete Nyman--Beurling closure criterion  
Status: PROPOSED  
Authoring agent: `gpt56-03`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: external theorem of Báez-Duarte (2003)  
Scope: imported Hilbert-space equivalence; not a one-sample finite witness  
Related counterexample candidates: none

## Statement

Let
\[
 \rho(x)=x-\lfloor x\rfloor,\qquad
 \chi(x)=\mathbf 1_{(0,1]}(x),
\]
and for every positive integer `a` define
\[
 \rho_a(x)=\rho\!\left(\frac{1}{a x}\right)
 \qquad(x>0).
\]
In the Hilbert space `L^2(0,infinity)`, RH is equivalent to
\[
 \chi\in
 \overline{\operatorname{span}}\{\rho_a:a=1,2,3,\ldots\}.
\]

## Source

Luis Báez-Duarte, *A strengthening of the Nyman--Beurling criterion for the
Riemann hypothesis*, Atti Accad. Naz. Lincei Rend. Lincei Mat. Appl. 14
(2003), 5--11; arXiv:math/0202141.

Inspection level: author PDF/arXiv text inspected.

## Motivation

The discrete basis is potentially useful for basis design, approximation
theory, and dual separating functionals.  It is also a cautionary example:
not every RH equivalent supplies a finite witness from one numerical value.

## Proof status

Imported theorem; proof not reproduced.

## Finite-witness audit

For
\[
 d_N=\inf_{c_1,\ldots,c_N}
 \left\|\chi-\sum_{a=1}^N c_a\rho_a\right\|_2,
\]
a computed positive `d_N` is compatible with both RH and `not RH`.  Even a
rigorous positive lower bound for one finite `N` says nothing about the closure
as `N->infinity`.

A finite disproof route would require, for example, an explicitly certified
bounded linear functional `L` such that
\[
 L(\rho_a)=0\quad\text{for every }a\ge1,
 \qquad
 L(\chi)\ne0.
\]
That universal annihilation is an infinite analytic theorem, not a finite
least-squares computation.

## Analytic/domain audit

- Functions are elements of `L^2(0,infinity)` modulo equality almost
  everywhere.
- The bar denotes norm closure.
- The parameter set is the positive integers in the strengthened criterion.
- Pointwise values at discontinuities do not affect the Hilbert-space element.

## Dependency audit

No other project claim proves this equivalence.

## Gap audit

- Finite-dimensional residuals cannot refute closure.
- Numerical Gram matrices may be ill-conditioned.
- Replacing the discrete set by arbitrary real parameters changes the theorem.
- A candidate separating functional must be continuous on `L^2`.

## Remaining uncertainty

No source uncertainty.  Repository proof reconstruction is pending.

## Suggested next attack

Treat this as a source of dual test functions for Weil/Li work, or open a
separate issue only after proposing a universal separating-functional ansatz.

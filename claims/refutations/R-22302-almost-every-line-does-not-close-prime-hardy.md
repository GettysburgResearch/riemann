# R-22302 — Almost-every-line estimates do not close the prime Hardy criterion

Claim ID: `R-22302`  
Title: Pointwise or almost-everywhere vertical estimates can miss every off-critical zero line; a locally uniform compact-strip bound is load-bearing  
Status: `PROPOSED — COMPLETE SCOPE REFUTATION`  
Authoring agent: `gpt56-pro-19`  
Created: 2026-08-07  
Dependencies: `T-22302`

## 1. The tempting but invalid shortcut

A natural analytic-number-theory target is to prove

\[
 I_H(\sigma)<\infty
 \]

for almost every `sigma`, or for every `sigma` outside a countable exceptional set. That does not imply RH.

If an off-critical zero

\[
 \rho=\frac12+\delta+i\gamma
 \]

exists, `T-22302` proves that the requested energy diverges at the single line

\[
 \sigma=\delta.
 \]

The set of real parts of zeta zeros is countable. An almost-everywhere theorem is therefore compatible with every off-critical zero lying in the omitted set.

## 2. Pointwise constants do not glue

Even a statement of the form

\[
 I_H(\sigma)\le C(\sigma)<\infty
 \]

on a dense set of `sigma` values is insufficient if the constants are allowed to blow up without control. Near an off-critical zero line,

\[
 I_{\rho,r}(\sigma)
 ={\pi m^2|\widehat H(z_\rho)|^2\over|\sigma-\delta|}
 +O\!\left(\log{1\over|\sigma-\delta|}\right).
 \]

Thus every punctured neighborhood can contain finite line values while their supremum is infinite.

This behavior is already present in the elementary model

\[
 F(z)={1\over z-z_0}.
 \]

Every vertical line not passing through `z_0` has finite weighted square integral, while the line through the pole has infinite energy.

## 3. Correct positive interface

For every compact interval

\[
 0<a<b<1/2,
 \]

the proof-facing target is

\[
 \boxed{
 \sup_{a\le\sigma\le b}
 \int_{\mathbb R}
 |\widehat H(\sigma+it)|^2
 \left|P_1\!\left(\frac12+\sigma+it\right)\right|^2dt
 <\infty.
 }
 \tag{R-22302.1}
\]

Any one such bound excludes every zeta zero in the corresponding closed vertical strip. A sequence of overlapping compact strips covering `(0,1/2)` proves RH.

The constants may depend arbitrarily on `(a,b)`; no limit as `a downarrow 0` is required. But uniformity in `sigma` inside each fixed interval is essential.

## 4. Consequences for proposed methods

The following are insufficient without a compact-strip upgrade:

- almost-everywhere boundary convergence of a Dirichlet series;
- Bohr mean or long-translation mean-square estimates;
- estimates on all rational vertical lines;
- a countable family of linewise estimates with uncontrolled constants;
- exclusion of poles only up to a finite ordinate;
- weak `L^p` bounds that permit a `1/(t-gamma)` singularity.

A valid proof must produce either (R-22302.1) or another theorem that directly excludes the local principal part in `T-22302.6`.

## 5. Proof boundary

This refutation does not make the compact-strip estimate easier. It prevents a measure-theoretic or density-one statement from being mistaken for the universal vertical criterion requested in `T-22301`.

# R-90416 — A fixed-endpoint carry Gram is not the periodized Jordan Gram

Claim ID: `R-90416`  
Title: Complete-residue coprime orthogonality fails at a fixed parent endpoint; the incomplete-period boundary is a load-bearing source of PIG correlations  
Status: **PROPOSED COMPLETE EXACT FINITE REFUTATION — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Dependencies: `L-90417`; elementary finite counting  
Scope: blocks a false transfer only; it does not refute the periodized theorem, PIG, or RH

## 1. Fixed-parent centered carries

For integers `N>=2` and `d>=2`, put

\[
 \chi_{N,d}(j)
 =\left\lfloor\frac Nd\right\rfloor
  -\left\lfloor\frac jd\right\rfloor
  -\left\lfloor\frac{N-j}{d}\right\rfloor,
 \qquad 0\le j<N.
 \tag{R-90416.1}
\]

Equivalently,

\[
 \chi_{N,d}(j)=\mathbf1_{\,j\bmod d>N\bmod d}.
 \tag{R-90416.2}
\]

Let

\[
 \overline\chi_{N,d}=\frac1N\sum_{j=0}^{N-1}\chi_{N,d}(j)
\]

and define the fixed-parent covariance

\[
 \operatorname{Cov}_N(d,e)
 =\frac1N\sum_{j=0}^{N-1}
 (\chi_{N,d}(j)-\overline\chi_{N,d})
 (\chi_{N,e}(j)-\overline\chi_{N,e}).
 \tag{R-90416.3}
\]

## 2. Exact coprime witness

Take

\[
 \boxed{N=100,\qquad d=49,\qquad e=47.}
 \tag{R-90416.4}
\]

The moduli are coprime. Direct exact counting gives

\[
 \boxed{
 \operatorname{Cov}_{100}(49,47)=\frac8{125}>0.
 }
 \tag{R-90416.5}
\]

By contrast, `L-90417` gives for the complete residue ensemble

\[
 \operatorname{Cov}_{\rm per}(49,47)
 =\frac{(49,47)^2-1}{4\cdot49\cdot47}=0.
 \tag{R-90416.6}
\]

Thus even exact coprime orthogonality does not survive freezing the parent endpoint.

A second witness with nontrivial gcd is

\[
 \boxed{
 \operatorname{Cov}_{100}(40,45)=\frac{76}{625},
 }
 \tag{R-90416.7}
\]

whereas the complete-residue covariance is only

\[
 \frac{5^2-1}{4\cdot40\cdot45}=\frac1{300}.
 \tag{R-90416.8}
\]

The discrepancy is not a small perturbation of the Jordan kernel.

## 3. Consequence

The periodized theorem may be used as:

- a complete-period benchmark;
- a source of positive Jordan squares;
- a model for the arithmetic bulk after a genuine transfer theorem.

It may not be substituted for the actual fixed-endpoint PIG Gram.

The missing quantity is precisely the incomplete-period/local-boundary correlation. In the Farey coordinate this is where noncoprime residue chains and the first Mertens cell live; in the fixed-prefix coordinate it is the reflection-Brownian source of `L-90416`.

## 4. Proof boundary

Refuted exactly:

\[
 \text{fixed endpoint covariance}
 =\text{complete residue covariance}.
\]

Not refuted:

1. `L-90417` in its declared periodized scope;
2. a source-specific cancellation of the boundary;
3. PIG or RH.

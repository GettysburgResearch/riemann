# L-91692 — Positive direct integrals preserve the strict one-eighth child-mass contraction

Claim ID: `L-91692`  
Status: **PROVED EXACT MASS-NORMALIZATION THEOREM**  
Created: 2026-08-14  
Frozen parent: PR #473 at `13ad1fdbf06edc931dc0c524327b701c5c8f86a3`  
Primary inputs: `L-91650`, `L-91674`, `L-91690`  
RH status: **unproved at this claim**

## 1. The normalization issue

The pointwise causal identity gives a strict child coefficient budget on one
positive packet. A root construction is a positive endpoint integral of many
such packets. The required global statement is about **target mass**, not the
unweighted number of fiberwise coefficients.

Let `(S,lambda)` be a positive finite measure space. For almost every `s`, let
`P_s` be a positive typed packet with target mass

\[
m_s=m(P_s)\ge0.
\]

Assume a one-use decomposition

\[
P_s=P_s^{\rm cur}+\sum_i a_i(s)A_{s,i}Q_{s,i}
\tag{L-91692.1}
\]

in every retained typed coordinate, where `a_i(s)>=0` and

\[
\boxed{
\sum_i a_i(s)m(A_{s,i}Q_{s,i})
\le \rho\,m_s,
\qquad
\rho<\frac18.
}
\tag{L-91692.2}
\]

The packets need not have unit mass and the index set may depend on `s`.

## 2. Positive integration

Put

\[
P=\int_S P_s\,d\lambda(s),
\qquad
P^{\rm cur}=\int_S P_s^{\rm cur}\,d\lambda(s).
\]

Tonelli gives the exact typed identity

\[
P=P^{\rm cur}
+\int_S\sum_i a_i(s)A_{s,i}Q_{s,i}\,d\lambda(s).
\tag{L-91692.3}
\]

Its total recursive target mass is

\[
\begin{aligned}
M_{\rm ch}
&=\int_S\sum_i a_i(s)m(A_{s,i}Q_{s,i})\,d\lambda(s)\\
&\le\rho\int_Sm_s\,d\lambda(s)
=\rho\,m(P).
\end{aligned}
\tag{L-91692.4}
\]

Therefore

\[
\boxed{M_{\rm ch}<\frac18\,m(P).}
\tag{L-91692.5}
\]

This remains true for monotone limits of positive simple endpoint measures.

## 3. Normalized hereditary form

Assume `m(P)>0`. Partition the integrated child field by any countable
source/provenance label `b`. Let `M_b` be the target mass of the resulting
aggregate child. For `M_b>0`, normalize it to a unit-mass packet

\[
\widehat P_b=M_b^{-1}P_b.
\]

Then

\[
P=P^{\rm cur}+\sum_b M_b A_b\widehat P_b,
\tag{L-91692.6}
\]

with

\[
\boxed{\sum_bM_b=M_{\rm ch}<\frac18\,m(P).}
\tag{L-91692.7}
\]

After normalizing the parent to unit target mass, the coefficients in the
Hereditary Typed Reset satisfy

\[
\boxed{\sum_b\alpha_b<\frac18.}
\tag{L-91692.8}
\]

Thus positive endpoint integration does not weaken the causal contraction.

## 4. Safety thinning and omission

If all retained source weights are multiplied by a common factor
`0<=sigma<=1`, then both parent and child target masses are multiplied by
`sigma`. If a positive top interval is omitted, both can only decrease. Hence

\[
M_{\rm ch}^{\rm corrected}
\le\rho\,m(P^{\rm corrected})
\]

whenever the correction is applied to the common positive parent packet before
the current/child split is forgotten.

This is exactly the one-use ordering in `L-91691`.

## 5. Application to factor 67

For one residual root fiber, `L-91650` has

\[
\sum_i\alpha_i<67^{-1/2}<\frac18.
\]

`L-91690` supplies a positive target-exact root residual and `L-91674`
integrates it without changing source ownership. Applying the present theorem
gives the global mass-weighted contraction required by `T-91312/T-91314`.

```text
fiberwise causal coefficient bound          EXACT / L-91650
positive endpoint direct integral           EXACT
global child target mass <1/8                EXACT
normalized hereditary coefficients <1/8     EXACT
safety thinning preserves contraction        EXACT
finite physical realization                  PR #473 / REVIEW
Riemann Hypothesis                           UNPROVEN AT THIS CLAIM
```

# T-30501 — Shift-terminalized critical eta variation criterion for RH

Claim ID: `T-30501`  
Title: A subpower variation bound for the explicit unshifted eta cascade gives a complete balanced flow, the sharp prime ramp, and RH  
Status: **EXACT CONDITIONAL CRITERION — CRITICAL VARIATION NOT PROVED HERE**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: `L-30501/L-30502`; PR #272 Cycle-Debt consumer  
RH status: **unproved**

## 1. Explicit propagated sequence

Let

\[
r_0(q)=q^{-1/2}\log(X/q)\mathbf1_{q\le X}.
\]

Put `N_0=X` and define

\[
\boxed{
 r_{j+1}(q)
 =\sum_{k\ge1}
 [r_j(2kq)-r_j((2k+1)q)],
 \qquad
 N_{j+1}=\left\lfloor\frac{N_j}{2}\right\rfloor.
}
\tag{T-30501.1}
\]

The sequence terminates after at most `ceil(log_2 X)` stages.

For each stage define

\[
G_j(n)=\sqrt n\,r_j(n)
\]

and

\[
\boxed{
\mathcal V_j
=\sum_{n=2}^{N_j-1}|G_j(n+1)-G_j(n)|
+2\sum_{n=2}^{N_j}\frac{|G_j(n)|}{n}.
}
\tag{T-30501.2}
\]

Every term is a finite explicit elementary expression.

## 2. Complete finite producer

At stage `j`, use:

1. the signed central first-difference flow for `r_j`;
2. the terminal adjacent-commutator flow for
   \[
   \sigma_j(m)=r_j(2m-1)-r_j(2m);
   \]
3. the unshifted residual `r_(j+1)` as the only propagated state.

`L-30502` proves that the resulting combined flow `d_X` exactly saturates every critical carry column and obeys

\[
\boxed{
\mathcal N_\omega(d_X)
\le50\sum_{j<\log_2X+1}\mathcal V_j.
}
\tag{T-30501.3]

The closing bracket in the tag is typographical only.

No finite Euler cutoff source, positive central-capacity manifest, or physical transference theorem enters this flow.

## 3. Critical Eta Variation (`CEV`)

Define the explicit theorem

\[
\boxed{
\mathrm{CEV}:
\qquad
\sum_j\mathcal V_j=X^{o(1)}.
}
\tag{T-30501.4}

This statement concerns the one frozen cascade (T-30501.1); it does not quantify over an unspecified producer.

Under CEV, (T-30501.3) gives subpower Cycle Debt. PR #272 then yields

\[
\sum_{p^a\le X}
\frac{\Lambda(p^a)}{\sqrt{p^a}}
\log\frac X{p^a}
=4\sqrt X+X^{o(1)}.
\tag{T-30501.5}

The source-pinned square-screw identity and one-sided Landau theorem exclude every zeta zero with real part greater than `1/2`; functional-equation symmetry gives RH.

Therefore

\[
\boxed{
\mathrm{CEV}\Longrightarrow\mathrm{RH}.
}
\tag{T-30501.6}

## 4. Exact analytic coordinate

For a causal logarithmic profile

\[
r_j(n)=n^{-1/2}F_j(\log(N_j/n)),
\]

one has exactly, up to the harmless endpoint translation from `N_j` to `floor(N_j/2)`,

\[
\boxed{
F_{j+1}=\beta*F_j,
}
\tag{T-30501.7}

where `beta` is the critical eta comb of `L-30501`.

That lemma proves the strict weighted-jet reserve

\[
\mathcal J_M(\beta*F)
\le\theta\mathcal J_M(F)
+c2^M\|F^{(M+1)}\|_1,
\qquad\theta<1.
\tag{T-30501.8}

This is the correct analytic attack on CEV. Endpoint causality and the eta signs remain inside the same convolution; they are not exported to a linearly large atomic source.

## 5. Why this is not presented as a proof of RH

`R-30501` invalidates the former PR #304 completion. Equations (T-30501.1)--(T-30501.8) completely specify the replacement producer and analytic coordinate, but the bound (T-30501.4) has not been proved.

Accordingly this file is an exact criterion and construction, not a request that a reviewer complete a missing argument. A future RH proposal may cite this theorem only after supplying a proof of CEV.

## 6. Exact status

```text
terminal atomic cutoff proof in PR #304      REJECTED
shift/divisor factorization                  PROPOSED COMPLETE EXACT
modified finite producer                     PROPOSED COMPLETE EXACT
critical eta weighted-jet contraction        PROPOSED COMPLETE
CEV                                          OPEN / RH-BEARING
CEV -> Cycle Debt -> RH                       COMPLETE CONDITIONAL CHAIN
Riemann Hypothesis                           UNPROVEN
```
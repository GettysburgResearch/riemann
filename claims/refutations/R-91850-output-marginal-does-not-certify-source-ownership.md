# R-91850 — An uncoloured output marginal does not certify source ownership

Claim ID: `R-91850`  
Status: **PROVED EXACT TYPE-SEPARATION COUNTERMODEL**  
Created: 2026-08-15  
Base: frozen PR #488 head `9acd381fa168db02a03646ab16851daebbf4d0fd`  
RH status: **unproved**

## 1. Countermodel

Let the positive source consist of two unit atoms `s1,s2`, and let the physical target consist of one atom `t`. The valid coupling

\[
 \Gamma_{\rm good}=\delta_{(s_1,t)}+\delta_{(s_2,t)}
\]

has output marginal `2 delta_t` and source marginal `delta_(s1)+delta_(s2)`.
The invalid source assignment

\[
 \Gamma_{\rm bad}=2\delta_{(s_1,t)}
\]

has the same output marginal `2 delta_t` but a different source marginal.
Every linear ordinary response, radix-four response, score and positive dual of the output row agrees for the two couplings.

Therefore

\[
 \boxed{\text{output marginal equality does not imply source-marginal equality}.}
\]

## 2. Hall version

A Hall producer has two input marginals, not one: odd demand must be exhausted and even capacity may be used at most once. The data which certify it are the edge coupling `pi`, its odd marginal, its even marginal, and the residual even measure. Erasing those marginals before verification loses the one-use theorem.

## 3. Consequence

The phrase “all children remain internal colours of one final row” is valid only after the internal colours have been constructed as marginals of one positive Hall–causal–physical coupling. A row identity alone cannot supply that fact.

```text
same output row / different source owner       exact countermodel
ordinary/detail/score tests distinguish them   no
source marginal required                       yes
Riemann Hypothesis                             unproved
```

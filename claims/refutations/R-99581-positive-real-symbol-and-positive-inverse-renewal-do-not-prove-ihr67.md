# R-99581 — Positive-real symbols and positive inverse renewals do not prove IHR67

Claim ID: `R-99581`  
Status: **SCOPE FIREWALL**  
Created: 2026-08-20

Two tempting implications are invalid.

1. Positivity of the continued Mellin transform on the positive real axis does
   not imply positivity of its inverse Mellin density. Complete monotonicity,
   not pointwise positivity, would be required; complete monotonicity here is
   equivalent to the unresolved stop-loss sign.
2. The positive inverse renewal

   \[
   T(x)=\sum_{d\le x}\frac{v_{67}(d)+1}{\sqrt d}\,h(x/d)
   \]

   is an exact identity, but a positive convolution can hide negative values of
   `h`. The overshoot identity of PR #653 is a source-specific debt equation,
   not a sign theorem.

Any successor must supply the missing owner-Carleson or stop-loss order rather
than infer it from either fact alone.

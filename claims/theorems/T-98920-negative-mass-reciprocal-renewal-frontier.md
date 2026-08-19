# T-98920 — Negative-mass reciprocal-renewal frontier

Claim ID: `T-98920`  
Status: **UNCONDITIONAL REDUCTION; FINAL NEGATIVE-MASS RENEWAL ESTIMATE OPEN**  
Created: 2026-08-19  
Depends on: `L-98920`; PR #615 `L-98072`; PR #613 correction `T-98900`  
RH status: **unproved**

The corrected proof graph is:

```text
fractional Julia/Hermite tunable heat proof   REFUTED as originally stated
compensated Weyl/heat formulation             EXACT / signed estimate open
reciprocal-Julia renewal identity             PROVED EXACT
subpower scalar negative mass -> RH           RETAINED
```

For

\[
P(T)=\int_1^T(\mathcal B(x)-1)_+\,\frac{dx}{x},
\qquad
N(T)=\int_1^T\mathcal B_-(x)\,\frac{dx}{x},
\]

`L-98920` gives after Tonelli/Fubini

\[
\boxed{
P(T)
\le
\sum_{2\le d\le T}\mathcal G(d)N(T/d).
}
\tag{T-98920.1}
\]

Thus upper reciprocal-Julia overshoot is paid only by negative mass on smaller quotient states, with a positive exact kernel.

The remaining theorem, `NRR98920`, is to prove a complementary source-faithful inequality of the form

\[
N(T)
\le
T^{o(1)}
+
\sum_{d\le T}k(d)P(T/d)
\]

with a two-step tilted kernel contracting at every fixed positive tilt. Such an inequality would imply

\[
P(T)+N(T)=T^{o(1)},
\]

hence the PR #615 one-sided negative-mass criterion and RH.

This packet does **not** claim `NRR98920` or RH.

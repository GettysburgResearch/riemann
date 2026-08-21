# O-91417 — Fixed discrete inner comparisons have a positive asymptotic gap

Claim ID: `O-91417`  
Status: **PROPOSED ANALYTIC TAIL THEOREM — EFFECTIVE REMAINDER PENDING REVIEW**  
Created: 2026-08-13  
Depends on: fixed-row expansion in `O-91414`  
RH status: **unproved**

Fix a row `2<=j<=66` and arithmetic source nodes

\[
1<=e<o<=67.
\]

For `y>=o`, put `z_e=y/e` and `z_o=y/o`.  The causal quotient is

\[
q_{p,j}(z)=
\frac{Q_{pz}(j)-p^{-1/2}Q_z(j)}
     {(5\sqrt{pz}-3)-p^{-1/2}(5\sqrt z-3)}.
\]

The fixed-row expansion

\[
Q_Y(j)=\alpha_j\sqrt Y+\lambda_j\log Y+\kappa_j
+O_j(Y^{-1/2}\log(2Y)),
\qquad \lambda_j<0,
\]

gives, uniformly for `1<=z<=67`,

\[
q_{p,j}(z)
=\frac{\alpha_j}{5}
 +\frac{\lambda_j\log p}{5\sqrt{pz}}
 +O_j(p^{-1/2}).
\]

Hence

\[
\boxed{
q_{p,j}(z_e)-q_{p,j}(z_o)
=
\frac{(-\lambda_j)\log p}{5\sqrt{py}}
 (\sqrt o-\sqrt e)
 +O_{j,e,o}(p^{-1/2}).
}
\]

The leading coefficient is strictly positive.  Since the row, source-pair and `y` domains are finite/compact, all arithmetic inner comparisons are correctly ordered for every sufficiently large `p`.

This does not restore the refuted continuous monotonicity between arithmetic nodes.  It proves that the Route-B discrete-order problem has no unbounded tail obstruction.  What remains is an explicit common remainder and a directed compact replay.

```text
fixed-pair leading gap              STRICTLY POSITIVE
uniform eventual discrete ordering PROPOSED ANALYTIC
continuous causal monotonicity      FALSE / NOT USED
effective transition height        OPEN
compact directed replay             OPEN
Riemann Hypothesis                  UNPROVEN
```

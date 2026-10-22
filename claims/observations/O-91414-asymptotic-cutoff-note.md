# O-91414 — The cutoff determinant has a positive asymptotic leading term

Claim ID: `O-91414`  
Status: **PROPOSED ANALYTIC TAIL THEOREM — EFFECTIVE REMAINDER PENDING REVIEW**  
Created: 2026-08-13  
Depends on: exact Green formula; `L-91359`; finite `P_61` source support  
RH status: **unproved**

Put

\[
A=\prod_{q\le61}(1-q^{-1}),
\qquad
B=\prod_{q\le61}(1-q^{-1/2}).
\]

Then `A>B>0`.  For each fixed row `2<=j<=66`, Euler summation in the exact Green formula gives

\[
Q_Y(j)=\alpha_j\sqrt Y+\lambda_j\log Y+\kappa_j
+O_j(Y^{-1/2}\log(2Y)),
\]

where

\[
\alpha_j=\frac8{j(j-1)}
\]

and

\[
\lambda_j=rac2{j(j-1)}[1+\zeta(1/2)]-\eta_j<0.
\]

Here `eta_j>0` is the directed constant of `L-91359`; the strict sign uses the elementary inequality `zeta(1/2)<-1`.

After the complete finite parent support activates, uniformly for `1<=y<=67`,

\[
S_{sig}=5A\sqrt{py}-3B+O(p^{-1/2}),
\]

\[
R_{sig}^{(j)}=\alpha_jA\sqrt{py}+\lambda_jB\log p+O_j(1).
\]

For any possible cutoff node `c<2000`, which is child-inactive because `c>y`,

\[
S_c=5\sqrt{py}/c-3/\sqrt c,
\]

\[
R_c^{(j)}=\alpha_j\sqrt{py}/c
 +(\lambda_j/\sqrt c)\log p+O_j(1).
\]

The order-`p` terms in

\[
\Delta_{j,c}=R_{sig}^{(j)}S_c-S_{sig}R_c^{(j)}
\]

cancel exactly.  The first surviving term is

\[
\boxed{
\Delta_{j,c}(p,y)
=5(-\lambda_j)\sqrt y
 \left(A/\sqrt c-B/c\right)
 \sqrt p\log p+O_{j,c}(\sqrt p).
}
\]

Its coefficient is strictly positive because

\[
\lambda_j<0,
\qquad
A/\sqrt c-B/c=(A\sqrt c-B)/c>0.
\]

Since the row and cutoff sets are finite, this proves positivity for all sufficiently large `p`, uniformly in `y`, once the displayed remainder is reconstructed with a common constant.

The proposal therefore divides Route A into two concrete obligations:

1. promote the Euler-summation remainder to one explicit uniform bound and obtain an effective transition `P_0`;
2. certify the compact domain `67<=p<P_0` by directed activation cells.

The asymptotic sign itself is not the remaining mystery: the positive `sqrt(p) log(p)` coefficient is explicit.

```text
leading square-root cancellation        EXACT ALGEBRA
first surviving coefficient             STRICTLY POSITIVE
uniform eventual sign                   PROPOSED ANALYTIC THEOREM
explicit remainder and transition       OPEN
compact directed replay                  OPEN
Riemann Hypothesis                       UNPROVEN
```

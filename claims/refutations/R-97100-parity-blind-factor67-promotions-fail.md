# R-97100 — The single-scalar and annular factor-67 promotions fail unless cumulative rough parity is realized

Claim ID: `R-97100`  
Status: **PROVED EXACT SCOPE REFUTATION**  
Created: 2026-08-17  
Frozen comparisons: PR #559 at `88d97adef8a42c5baf2f52c2c259a4ef536bdfdd`; PR #556 at `a4feca0457d310c72054f274040f93b0503f658b`; PR #561 at `db9bdc63c855c6ddf664b763d748f8155a6a2c67`  
RH status: **unproved**

Let `S(E,O)=(O,E)` and let signed observation be
\[
\mathcal O(E,O)=R(E)-R(O).
\]
For a rough history `h`,
\[
\boxed{\mathcal O(S^{|h|}P)=(-1)^{|h|}\mathcal O(P).}
\tag{R-97100.1}
\]
This is the exact parity cocycle proved in PR #561. Recording history parity in a label but replacing every terminal by the canonical even-oriented realization does not preserve the root marginal.

## 1. PR #559 single-scalar promotion

`L-97001` records rough history, but `L-97002` applies the canonical Target--Lorenz orientation to every terminal and then applies `5R_2+3R_3`. This omits the factor in (R-97100.1).

Take incoming history `(67)`, terminal prime `p=2521`, and `y=66`; then `py=166386`. The frozen MPFR theorem of PR #550 gives a strictly positive canonical row margin in every row `2<=j<=66` because its directed determinant is strictly positive on `py>=166000`. Hence
\[
K_{5:3}=5K_2+3K_3>0.
\]
The history is odd, so the root-oriented datum is `-K_(5:3)<0`. A positive scalar terminal row cannot realize it. Therefore `L-97002`, `L-97003`, and `T-97000` do not follow from `L-97001`.

## 2. PR #556 annular promotion

For the same odd history and terminal `(p,y)=(2521,66)`, `L-96601` gives
\[
E_2(py)>\frac75,
\qquad E_2(y)<\frac52,
\]
\[
E_3(py)>\frac12,
\qquad E_3(y)<1.
\]
Since `sqrt(2521)>50`, the canonical terminal currents obey
\[
E_2(py)-2521^{-1/2}E_2(y)>\frac75-\frac1{20}>0,
\]
\[
E_3(py)-2521^{-1/2}E_3(y)>\frac12-\frac1{50}>0.
\]
The odd history again requires both signs to be reversed. Thus the local reserve `L-96600--L-96601` survives, while `L-96603/T-96600/T-96601` are not valid global compositions.

## 3. Binding disposition

```text
PR #559 finite source identity                    retained with parity label
PR #559 parity-blind terminal scalar             refuted
PR #556 local quadrature and P61 reserve          retained
PR #556 parity-blind annular root promotion       refuted
PR #561 parity covariance and explicit no-go      retained
full scalar or annular positivity                 not refuted
Riemann Hypothesis                                unproved
```

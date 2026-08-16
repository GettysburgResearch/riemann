# L-92911 — Whole-cell endpoint realization is positive, measurable and source exact

Claim ID: `L-92911`  
Status: **PROPOSED COMPLETE EXPLICIT REALIZATION THEOREM — REVIEW REQUIRED**  
RH status: **unproved**

Let \(K=\lfloor X/67\rfloor+1\), \(W=10000\), and retain
\[
I_X=[K+2,X-W-2].
\]
Its endpoints are integers, so the retained region is a union of complete unit cells. No partial-cell defect or activation collar is present.

## 1. Positive endpoint measure

On \(1\le x<67\), set
\[
L(x)=2\sqrt x\sum_{n\le x}\frac{\mu(n)}n-
     \sum_{n\le x}\frac{\mu(n)}{\sqrt n}.
\]
The directed cell reconstruction gives \(L(x)>159/500\). Hence
\[
d\mu_X(s)=\frac{2L(X/s)}s\,ds
\]
is a finite positive atomless measure on \(I_X\).

## 2. Measurable Hall source

The left-greedy Hall coefficients are obtained on each activation cell by finitely many additions, divisions by positive target atoms, and `min`. They are Borel. Apply the one flow of `L-92910` fibrewise, retain all Hall and first-owner labels, and keep every causal child as an internal colour. Tonelli gives one positive labelled parent measure. Every source occurrence has exactly one owner.

## 3. Explicit martingale quantizer

For \(s\in[n,n+1]\), define
\[
q_n(s)=\frac{s^{-1/2}-(n+1)^{-1/2}}
             {n^{-1/2}-(n+1)^{-1/2}},
\qquad q_{n+1}(s)=1-q_n(s).
\]
Then \(q_n,q_{n+1}\in[0,1]\), their sum is one, and
\[
q_n(s)n^{-1/2}+q_{n+1}(s)(n+1)^{-1/2}=s^{-1/2}.
\]
Thus the cell map is a positive Markov pushforward preserving constants and the exact \(s^{-1/2}\) mode. Since the SHARP target and declared score are affine in \(s^{-1/2}\) for each fixed source label, both are transported exactly. Apply this quantizer once to the total labelled measure after all Hall/current/child colours are summed.

The resulting finite row \(d_X^0\) is coefficientwise nonnegative. There is no second Hall operation, child quantizer, correction, or matrix port.

## 4. The only approximation

Component/capacity coordinates not affine in \(s^{-1/2}\) produce one retained-cell quadrature defect. It is restricted to the complete retained cells before the carry response is taken. `L-92912` bounds this one defect on every physical column. No exact finite/continuum identification is assumed.

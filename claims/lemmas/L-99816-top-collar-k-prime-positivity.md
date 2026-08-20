# L-99816 — Every fully active top-collar rough Euler cube is positive

Claim ID: `L-99816`  
Status: **PROVED EXACT ALL-ORDER TOP-COLLAR THEOREM**  
Created: 2026-08-20  
Depends on: PR #658 `L-99703`; `L-99814`  
RH status: **not assumed**

Let `67<=p_1<...<p_k`, put

\[
P=\prod_{i=1}^k p_i,\qquad r_i=p_i^{-1/2},
\]

and let

\[
\mathcal E_P=\prod_{i=1}^k(I-r_iU_{p_i}).
\]

For the normalized SHARP box potential `Phi`, consider the top activation collar

\[
y=Pz,\qquad 1<=z<67.
\]

Every proper-subset argument `y/p_A=z P/p_A` is at least `67`, because the complement of a proper subset contains one rough prime. Thus all proper-subset terms use the deep formula

\[
\Phi_{\rm deep}(t)=A-Bt^{-1/2},
\quad A=8(1-67^{-1/2}),\quad B=3\log67,
\]

while only the full-subset term sees the collar value `Phi(z)`.

Since one weighted Euler factor annihilates the critical half-order mode, exact inclusion-exclusion gives

\[
\boxed{
\mathcal E_P\Phi(Pz)
=A\prod_{i=1}^k(1-r_i)
+\frac{(-1)^k}{\sqrt P}D(z),
}
\tag{L-99816.1}
\]

where

\[
D(z)=\Phi(z)-\Phi_{\rm deep}(z)
=\frac{8\sqrt{67z}-201\log z-536+201\log67}{67\sqrt z}.
\tag{L-99816.2}
\]

Elementary calculus gives a global bound on `1<=z<=67`:

\[
\boxed{-1/20<D(z)<28/5.}
\tag{L-99816.3}
\]

(The derivative has only finitely many elementary critical points after multiplication by `sqrt(z)`; outward rational radical/log bounds certify these coarse margins.)

For even `k`, the adverse correction is at worst `-1/(20 sqrt(P))`, while

\[
A\prod_i(1-r_i)
\ge A(1-67^{-1/2})(1-71^{-1/2})\prod_{i>=3}(1-r_i)>0,
\]

and the first two factors already dominate the tiny correction. For odd `k`, the adverse correction is at worst `-(28/5)/sqrt(P)`. The ratio

\[
\frac{1}{\sqrt P\prod_i(1-r_i)}
=\prod_i\frac1{\sqrt{p_i}-1}
\]

strictly decreases when another rough prime is added. Hence the worst odd case is `k=1,p_1=67`. There

\[
A(1-67^{-1/2})-\frac{28}{5\sqrt{67}}>0.
\]

Therefore

\[
\boxed{
\mathcal E_P\Phi(Pz)>0
\qquad(1<=z<67)
}
\tag{L-99816.4}
\]

for every number `k>=1` of rough primes.

This proves all-order positivity on the top collar, where every rough source atom is active. Together with full-deep positivity, any remaining sign issue must occur in intermediate activation patterns where only a proper suffix of the rough-prime set is active.

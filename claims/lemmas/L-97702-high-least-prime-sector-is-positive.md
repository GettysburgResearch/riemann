# L-97702 — The genuinely high-least-prime native sector is positive

Claim ID: `L-97702`  
Status: **PROVED UNCONDITIONAL ASYMPTOTIC THEOREM**  
Created: 2026-08-18  
Depends on: the nonnegative annular base and its square-root asymptotic on PR #587  
RH status: **not assumed**

For a least allowed rough prime `p_0`, define the exact native substate

\[
\mathcal F_{p_0}(Y)=
\sum_{\substack{m\in\mathcal R_{67}^{\rm sf}\\P^-(m)\ge p_0}}
 {\mu(m)\over\sqrt m}b(Y/m).
\tag{L-97702.1}
\]

Fix

\[
\theta>e^{-1}.
\]

Then, uniformly over states satisfying

\[
p_0\ge Y^\theta,
\]

one has

\[
\boxed{\mathcal F_{p_0}(Y)>0}
\tag{L-97702.2}
\]

for all sufficiently large `Y`.

## Proof

Since `3theta>1`, an active rough product contains at most two primes. Hence

\[
\mathcal F_{p_0}(Y)
=b(Y)
-\sum_{p\ge p_0}{1\over\sqrt p}b(Y/p)
+\sum_{p<q\atop p,q\ge p_0}{1\over\sqrt{pq}}b(Y/(pq)).
\tag{L-97702.3}
\]

The last term is nonnegative. Using

\[
b(u)=a\sqrt u+O(1),\qquad a>0,
\]

and partial summation,

\[
\sum_{Y^\theta\le p\le Y/2}{1\over\sqrt p}b(Y/p)
=a\sqrt Y\sum_{Y^\theta\le p\le Y/2}{1\over p}
+O\left(\sum_{p\le Y}p^{-1/2}\right).
\]

Mertens' theorem and the PNT give

\[
\sum_{Y^\theta\le p\le Y/2}{1\over p}
=\log(1/\theta)+o(1),
\]

\[
\sum_{p\le Y}p^{-1/2}=O(\sqrt Y/\log Y).
\]

Because `log(1/theta)<1`, the one-prime subtraction is strictly smaller than
`b(Y)=a sqrt(Y)+O(1)`, proving (L-97702.2).

This theorem closes a genuine terminal sector without parity-blind leafwise
Hall. The unresolved histories have least prime below `Y^theta` and lie near
the critical rough-depth saddle.

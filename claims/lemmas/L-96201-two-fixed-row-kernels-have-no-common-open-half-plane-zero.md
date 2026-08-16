# L-96201 — The two fixed row kernels have no common zero in the open right half-plane

Claim ID: `L-96201`  
Status: **PROVED EXACT ANALYTIC ALGEBRA**  
Created: 2026-08-17

For the fixed-row Mellin transform of PR #542, the finite numerators at rows two and three are

\[
P_2(z)=2^{1-z}-1-3^{-z},
\]

\[
3P_3(z)=5\,3^{-z}-2^{-z}-1-3\,4^{-z}.
\]

Suppose `Re z>0` and both vanish. Put

\[
a=2^{-z},\qquad b=3^{-z}.
\]

The first equation gives `b=2a-1`. The second becomes

\[
0=5(2a-1)-a-1-3a^2=-3(a-1)(a-2).
\]

Thus `a` is either one or two. But

\[
|a|=2^{-\Re z}<1,
\]

which is impossible. Therefore

\[
\boxed{P_2(z)\text{ and }P_3(z)\text{ never vanish simultaneously for }\Re z>0.}
\]

This removes the large-row asymptotic noncancellation step from PR #542: two fixed rows suffice for every hypothetical off-line zero.

# L-101101 — Every rough factor-eight prime interval has reciprocal mass below \(3/4\)

Claim ID: `L-101101`  
Status: **PROVED ELEMENTARY UNIFORM BUDGET**  
Created: 2026-08-20  
RH status: **not assumed**

For every real \(x\ge67\),
\[
 \boxed{
 \sum_{x<p\le8x}{1\over p}< {3\over4}.
 }                                                   \tag{L-101101.1}
\]
The same bound remains true if one extra labelled copy of \(67\) is allowed.

Every prime \(p>3\) lies in one of the two residue classes
\(1,5\pmod 6\).  Fix one such class and list its members in \((x,8x]\) as
\[
 n_1<n_2<\cdots<n_m,\qquad n_{j+1}-n_j=6.
\]
For \(j\ge2\), monotonicity of \(1/t\) gives
\[
 {1\over n_j}
 \le {1\over6}\int_{n_j-6}^{n_j}{dt\over t}.
\]
Therefore the contribution of one residue class is at most
\[
 {1\over x}+{1\over6}\log8.
\]
Both classes contribute at most
\[
 {2\over x}+{1\over3}\log8.
\]
Allowing one additional labelled \(67\) costs at most \(1/67\).  Since
\[
 {3\over67}+\log2
 < {3\over67}+0.693148
 < {3\over4},
\]
(L-101101.1) follows, including the decorated-\(67\) convention.

The constant is deliberately not optimized.  What matters is a uniform moat
below one on every multiplicative interval of ratio eight.

# O-18513 — Source-corrector Schur scaling reconnaissance

Claim ID: `O-18513`  
Status: `NON_DIRECTED MPMATH RECONNAISSANCE`  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-01

The exact source-canonical split of `X-18506` was evaluated in ordinary
100--140 digit arithmetic before the directed run.  Let

\[
s(c,N)=\lambda_{\min}
\left(B_W-Z_W^*C^{-1}Z_W,G_W\right)
\]

for the one-dimensional source-corrector quotient.  On the nine-level schedule,
all midpoints are positive and

\[
0.1717527528
<
(\log c)s(c,N)
<
0.2021656005.
\]

The raw values decrease from approximately

\[
0.08251754261
\quad(c=10,N=2)
\]

to

\[
0.02213524823
\quad(c=5000,N=10).
\]

This nominates the scaling law

\[
\boxed{s(c,N)\asymp (\log c)^{-1}}
\]

along slowly growing `N`.  The production target

\[
m(c)=\frac1{40(1+\lceil\log c\rceil)}
\]

lies well below every ordinary value.

The source-valid coercivity becomes much smaller:

\[
\lambda_{\min}(C,G_E)
\approx 7.14\times10^{-9}
\]

at `(10,2)` and approximately

\[
5.99\times10^{-49}
\]

at `(5000,10)`.  The frozen 240-bit dyadic solves reduce the ordinary residual
penalty below `2e-105` at the last level, so the directed difficulty is
coercivity/conditioning rather than solve accuracy.

These numbers schedule the directed emitter.  They do not prove positivity,
the asymptotic scaling law, or an unbounded sequence.

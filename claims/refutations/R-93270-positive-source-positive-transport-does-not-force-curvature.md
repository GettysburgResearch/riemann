# R-93270 - Positive source and positive Peano transport do not force curvature positivity

Claim ID: `R-93270`
Status: **EXACT REFUTATION**
Created: 2026-08-16
Refutes: any source-blind inference `positive source + positive scale transport => nonnegative second scale curvature`

Let

\[
\nu(v)=1+\frac12\cos v\ge\frac12.
\tag{R-93270.1}
\]

Let

\[
b(v)=8192\,(b_1*b_2*b_3)(v),
\tag{R-93270.2}
\]

with the nonnegative compact kernels `b_j` from `L-93270`. Put

\[
U=\nu*b.
\tag{R-93270.3}
\]

Because `nu>=1/2` and `b>=0`,

\[
U(v)\ge\frac12\int_\mathbb R b(u)\,du>0
\tag{R-93270.4}
\]

for every real `v`.

However

\[
U''=\nu''*b=-\frac12(\cos*b).
\tag{R-93270.5}
\]

The Fourier coefficient of `b` at frequency one is

\[
\widehat b(1)
=8192\prod_{j=1}^3
\frac{1-e^{-(j+i)\log4}}{j+i}.
\tag{R-93270.6}
\]

Every numerator is nonzero because its second term has modulus `4^{-j}<1`. Hence `widehat b(1) != 0`, and `U''` is a nonzero sinusoid. It takes both signs.

Therefore

\[
\boxed{
\nu\ge0,
\quad b\ge0,
\quad \nu*b>0
\quad\not\Longrightarrow\quad
(\nu*b)''\ge0.
}
\tag{R-93270.7}
\]

This countermodel is binding. The positive factor-64 bank is valuable as a source and transport architecture, but its RH-bearing curvature still requires signed arithmetic cancellation.

# L-100331 — GCD extraction leaves a positive common core and one primitive signed ratio

Claim ID: `L-100331`  
Status: **PROVED EXACT ARITHMETIC FACTORIZATION**  
Created: 2026-08-20  
Depends on: `L-100330`  
RH status: **not assumed**

In the off-diagonal term of `L-100330`, write

\[
m=da,\qquad n=db,\qquad (a,b)=1,\qquad 1<a^{-1}b\le8.
\]

If `mu(m)mu(n)` is nonzero, then `a,b,d` are squarefree and pairwise coprime.
Therefore

\[
\boxed{\mu(m)\mu(n)=\mu(a)\mu(b).}
\tag{L-100331.1}
\]

The common-core sign disappears completely.

For `sigma>1`, the full positive common-core sum is

\[
\begin{aligned}
\mathcal G_{a,b}(\sigma)
&=\sum_{\substack{d\ {m squarefree}\\(d,ab)=1}}d^{1-2\sigma}\\
&=\prod_{p\nmid ab}(1+p^{1-2\sigma})\\
&=\boxed{
\frac{\zeta(2\sigma-1)}{\zeta(4\sigma-2)}
\prod_{p\mid ab}(1+p^{1-2\sigma})^{-1}
}>0.
\end{aligned}
\tag{L-100331.2}
\]

Consequently the formal infinite off-diagonal energy becomes

\[
\boxed{
2\sum_{\substack{(a,b)=1\\1<b/a\le8}}
\mu(a)\mu(b)a^{1-2\sigma}
\kappa_\sigma(b/a)\mathcal G_{a,b}(\sigma).
}
\tag{L-100331.3}
\]

At the physical convergence frontier one first truncates in `m,n`, performs
this exact gcd decomposition, and only then passes to a limit.  No absolute
value may be taken over the primitive pair.

## Exact remaining theorem: PRBC100330

For every `sigma>1`, the finite primitive-pair expressions arising from the
physical wavelet energy are uniformly bounded as the endpoint tends to
infinity, with the top boundary layer treated in the same gcd coordinates.

This is a fixed-width, coprime, ordinary-Mobius Type-II statement.  It is not a
source-blind large sieve: the signs `mu(a)mu(b)`, the exact ratio kernel and the
positive common-core factor are all retained.

`PRBC100330` is not proved here.

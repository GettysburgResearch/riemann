# L-98073 — Exact source-faithful log-energy Type-II kernel

Claim ID: `L-98073`  
Status: **PROVED EXACT FINITE IDENTITY**  
RH status: **unproved**

Let
\[
\alpha_1=6,\quad \alpha_2=-9/\sqrt2,\quad \alpha_4=3/2,
\]
so
\[
\mathcal D(t)=\sum_{r\in\{1,2,4\}}\alpha_r B_{1/2}(t/r).
\]

For
\[
K_T(m,n)=\sum_{r,s\in\{1,2,4\}}\alpha_r\alpha_s
\log\!\frac{T}{\max(rm,sn)}_+,
\]
finite Fubini gives exactly
\[
\int_1^T\mathcal D(t)^2\,dt/t
=
\sum_{m,n\le T}\frac{\mu(m)\mu(n)}{\sqrt{mn}}K_T(m,n).
\]

The kernel is Gram-positive because it is the log-scale inner product of the
three-band step functions. Its diagonal is `O(log^2 T)`. Thus only the
one-sided off-diagonal upper bound
\[
\sum_{m\ne n}\frac{\mu(m)\mu(n)}{\sqrt{mn}}K_T(m,n)\le T^{o(1)}
\]
remains conclusion-producing.

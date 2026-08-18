# L-98702 — The reciprocal-Julia Hermite heat transform detects every off-line zero exponentially

Claim ID: `L-98702`  
Status: **PROVED ANALYTIC THEOREM**  
Created: 2026-08-18  
Depends on: `L-98700`; standard Mellin inversion and local meromorphic continuation of zeta  
RH status: **not assumed**

For `0<theta<=1`, let

\[
B_\theta(s)=B_\diamond(s)^\theta
\]

be the branch positive on the real line `s>1`. Write its safe-line Dirichlet series as

\[
B_\theta(s)=\sum_{n\ge1}b_\theta(n)n^{-s}.
\]

For `T>0` and real `tau`, define the First-Hermite heat packet

\[
\mathscr B_{\theta,T}(\tau)
=\sum_{n\ge1}\frac{b_\theta(n)}{\sqrt n}
 e^{-(\log n)^2/(4T)}e^{-i\tau\log n}.
\]

Gaussian Mellin inversion gives, for every `c>1`,

\[
\mathscr B_{\theta,T}(\tau)
=2\sqrt{\pi T}\,\frac1{2\pi i}
 \int_{c-i\infty}^{c+i\infty}
 B_\theta(s)e^{T(s-1/2-i\tau)^2}\,ds.
\]

The finite numerator of `B_diamond` is

\[
(1-2^{-s})(1-2^{-s-1}),
\]

whose zeros lie on `Re s=0` and `Re s=-1`. Thus it cannot cancel a nontrivial zeta zero in `0<Re s<1`.

Suppose `rho=beta+i gamma`, `beta>1/2`, is a zeta zero of multiplicity `m`. Then `B_theta` has a branch singularity of order `m theta` at `rho`. Shifting the contour to a line strictly between `1/2` and `beta`, taking a Hankel contour around `rho`, and setting `tau=gamma` gives

\[
\mathscr B_{\theta,T}(\gamma)
=c_{\rho,\theta}T^{m\theta-1/2}e^{(\beta-1/2)^2T}
(1+O_{\rho,\theta}(T^{-1/2}))+\mathcal R_T.
\]

A Gaussian `tau`-average over a window of width `T^{-1/2}` makes the squared contribution of distinct ordinates asymptotically orthogonal. Consequently no cancellation among poles can remove the exponential rate: for some bounded window centered at an ordinate of a rightmost off-line zero,

\[
\int |\mathscr B_{\theta,T}(\tau)|^2w_T(\tau-\gamma)\,d\tau
\gg_{\rho,\theta}T^{2m\theta-1}e^{2(\beta-1/2)^2T}.
\]

This pole-growth statement is independent of RH and remains valid for every fixed positive `theta`.

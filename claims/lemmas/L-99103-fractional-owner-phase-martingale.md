# L-99103 — Fractional reciprocal coefficients carry an exact phase-twisted logarithmic-owner martingale

Claim ID: `L-99103`  
Status: **PROVED EXACT SOURCE THEOREM**  
Created: 2026-08-19  
Depends on: `L-98700`, `L-98710`, `L-97101`  
RH status: **not assumed**

Write

\[
G_\diamond(s)^\theta
=\sum_{n\ge1}g_\theta(n)n^{-s},
\qquad
B_\diamond(s)^\theta
=\sum_{n\ge1}b_\theta(n)n^{-s}.
\]

All `g_theta(n)` are nonnegative, and for `n>1`

\[
g_\theta(n)\log n
=\theta\sum_{\substack{d\mid n\\d>1}}
 \Lambda_\diamond(d)g_\theta(n/d).
\]

Therefore

\[
\boxed{
P_{\theta,n}(d)
=\frac{\theta\Lambda_\diamond(d)g_\theta(n/d)}
 {g_\theta(n)\log n}
}
\tag{L-99103.1}
\]

is a probability distribution on generalized-prime-power divisors of `n`. The inverse logarithmic derivative gives

\[
b_\theta(n)\log n
=-\theta\sum_{\substack{d\mid n\\d>1}}
 \Lambda_\diamond(d)b_\theta(n/d).
\]

For real `tau`, put

\[
f_{\theta,\tau}(n)
=\frac{b_\theta(n)}{g_\theta(n)}n^{-i\tau}.
\]

Then

\[
\boxed{
f_{\theta,\tau}(n)
=-\sum_d P_{\theta,n}(d)d^{-i\tau}
 f_{\theta,\tau}(n/d).}
\tag{L-99103.2}
\]

Let `N_(t+1)=N_t/D_(t+1)` under these transition probabilities and let `R_t=D_1...D_t`. The process

\[
\boxed{
M_t=(-1)^tR_t^{-i\tau}f_{\theta,\tau}(N_t)
}
\tag{L-99103.3}
\]

is a bounded complex martingale.

At `tau=gamma`, this is the exact source-level phase which survives the optimal notch. Thus any successful annular estimate can and should eliminate cross terms by conditional martingale orthogonality before the integer-product source is collapsed. This is the source-specific mechanism absent from every magnitude-only estimate ruled out by `R-99100`.

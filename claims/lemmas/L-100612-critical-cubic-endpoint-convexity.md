# L-100612 — The critical cubic carrier has positive one- and two-ended differences

Claim ID: `L-100612`  
Status: **PROVED EXACT KERNEL THEOREM**  
Created: 2026-08-20  
Depends on: PR #676 `L-100001`; `L-100610`  
RH status: **not assumed**

Let

\[
\Psi(y)=64
\begin{cases}
3y-y^{3/2},&0<y\le1,\\
3\sqrt y-1,&y\ge1,
\end{cases}
\tag{L-100612.1}
\]

be the positive self-reciprocal cubic critical kernel. Put

\[
\phi(u)=\Psi(e^u),
\qquad u\in\mathbb R.
\]

Then `phi` is increasing and convex on the whole real line. More precisely,

\[
\phi'(u)=64
\begin{cases}
3e^u-\frac32e^{3u/2},&u\le0,\\
\frac32e^{u/2},&u\ge0,
\end{cases}
\tag{L-100612.2}
\]

and

\[
\phi''(u)=64
\begin{cases}
3e^u-\frac94e^{3u/2},&u\le0,\\
\frac34e^{u/2},&u\ge0.
\end{cases}
\tag{L-100612.3}
\]

Both expressions are strictly positive. Their values and first two derivatives
match at `u=0`, so no activation atom or derivative jump is hidden in the
claim.

For a prime label `p`, let

\[
(U_p f)(y)=f(y/p),
\qquad
\Delta_p=I-U_p.
\]

Monotonicity gives

\[
\boxed{
\Delta_p\Psi(y)\ge0
\qquad(y>0).
}
\tag{L-100612.4}
\]

For two labels `p,q`, convexity gives the exact Peano square

\[
\boxed{
\begin{aligned}
\Delta_p\Delta_q\Psi(e^u)
&=\int_0^{\log p}\int_0^{\log q}
 \phi''(u-s-t)\,dt\,ds\\
&\ge0.
\end{aligned}
}
\tag{L-100612.5}
\]

Thus every root term, every singleton term, and every double-ended term with
an empty interior interval in `L-100610` has the correct sign before any
arithmetic estimate.

## Exact localization of possible negativity

Apply the two-ended hazard identity to the finite cubic Euler source. Because
of (L-100612.4)--(L-100612.5), the negative part can only arise from

\[
\Delta_{p_i}\Delta_{p_j}
\prod_{p_i<p<p_j}(I-p^{-1/2}U_p)\Psi,
\qquad i<j,
\tag{L-100612.6}
\]

with a nonempty interior prime interval. Hence:

```text
root/survival channel                         nonnegative;
single-ended channels                         nonnegative;
adjacent-prime double-ended channels          nonnegative;
only a signed interior interval Euler product can be negative.
```

This is stronger than assigning diagonal and short blocks to later machinery:
the complete zero-interior region is closed unconditionally.

## Scope

Convexity does not imply that applying an arbitrary interior Euler product
preserves positivity. The critical deep mode still has prime-harmonic owner
cost. Long intervals require the finite-squaring/renewal mechanisms already
present in PR #691, while short intervals require a compact interval estimate.
No RH conclusion is claimed from kernel convexity alone.
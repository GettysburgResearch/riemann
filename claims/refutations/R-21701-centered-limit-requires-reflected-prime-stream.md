# R-21701 — The centered notch limit requires the reflected prime stream

Claim ID: `R-21701`  
Title: Centering destroys the causal support used by the compact one-sided prime formula  
Status: **PROVED SCOPE CORRECTION**  
Authoring agent: `gpt56-pro-global-01`  
Created: 2026-08-07  
Scope: correction to the prime-side interface in the first version of `T-21701`

## 1. The finite causal formula and the centered limit are different objects

For a compact causal window `G` supported in `[0,L]`, the translated
Guinand--Weil test

\[
 \phi_x(u)=G(x-u)
\]

satisfies

\[
 \phi_x(-\log n)=G(x+\log n)=0
\]

whenever `x>L`.  On that right half-line the full prime contribution therefore
reduces to the one-sided terminal stream

\[
 \sum_{n\ge2}{\Lambda(n)\over\sqrt n}G(x-\log n).
\]

This is the interface used legitimately by the compact-window criteria on
PRs #165 and #190.

For the finite notch cascade, however, centering replaces `G_M` by

\[
 \widetilde G_M(t)=G_M(t+S_M/2),
 \qquad S_M=\sum_{k\le M}r_k.
\]

Its support is

\[
 [-S_M/2,\,L+S_M/2].
\]

The limiting centered profile `G_infinity` has two-sided Gaussian tails.  Hence

\[
 G_\infty(x+\log n)
\]

is not identically zero for any fixed right half-line.

## 2. The completed Guinand--Weil prime term

For a real rapidly decreasing test `G`, put

\[
 H_x(z)=e^{zx}\widehat G_L(z),
 \qquad
 \widehat G_L(z)=\int_{\mathbb R}e^{-zu}G(u)\,du.
\]

In the centered Guinand--Weil convention, the prime term is

\[
 \boxed{
 \mathcal P_G(x)=
 \sum_{n\ge2}{\Lambda(n)\over\sqrt n}
 \bigl[G(x-\log n)+G(x+\log n)\bigr].}
 \tag{R-21701.1}
\]

Both streams are forced by the two Fourier values at `+log n` and `-log n`.
The reflected stream may be omitted only after a support argument proves it is
zero.

## 3. Exact correction

The first version of `T-21701` asserted the centered limiting identity using
only

\[
 Q_\infty(x)=
 \sum_n{\Lambda(n)\over\sqrt n}G_\infty(x-\log n).
\]

That assertion does not follow from the compact-window formula.  In particular,
the reflected prime stream cannot be hidden inside an ``endpoint'' or
``initial-segment'' term: it is an infinite arithmetic sum, absolutely
convergent because of the Gaussian tail, and depends nontrivially on `x`.

The probability-product construction, the entire zero geometry, and the
centered convergence of the notch kernels survive.  The one-sided equations in
the original Sections 5--9 do not.  The corrected theorem uses the completed
prime expression (R-21701.1), the exact archimedean functional, and the full
Guinand--Weil identity.

## 4. Process lesson

A translation that recenters an expanding causal support is not a harmless
coordinate change for an explicit formula.  It converts a terminal-prime
observable into a completed two-sided prime observable.  Every future centered
limit must transport both prime streams before passing to the limit.

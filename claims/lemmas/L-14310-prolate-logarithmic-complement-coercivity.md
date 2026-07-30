# L-14310 — Prolate concentration gives an explicit logarithmic complement floor

Claim ID: `L-14310`  
Title: A finite prolate packet captures every low mode of the logarithmic Weil head  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-09-b`  
Created: 2026-07-30  
Dependencies: Suzuki equation (4.5)–(4.6); Plancherel; the trace of the time–band concentration operator; Young's convolution inequality  
Scope: complete high-frequency complement for the scaled localized Weil form  
Related counterexample candidates: none

## Pure logarithmic form

Extend `w∈L^2(-1,1)` by zero to the real line and use the Fourier convention

\[
 \widehat w(z)=\int_{-1}^{1}w(x)e^{-izx}\,dx,
 \qquad
 \|w\|_2^2=\frac1{2\pi}\int_{\mathbb R}|\widehat w(z)|^2dz.
 \tag{L-14310.1}
\]

Let

\[
 \mathcal L(w)
 =\frac1{2\pi}\int_{\mathbb R}
   (\log|z|+C_0)|\widehat w(z)|^2dz,
 \tag{L-14310.2}
\]

with its closed form domain.  This is the universal logarithmic form in
Suzuki (4.4)–(4.6).

For `Omega>1`, define the time–band concentration operator

\[
 \langle K_\Omega w,w\rangle
 =\frac1{2\pi}\int_{-\Omega}^{\Omega}
   |\widehat w(z)|^2dz.
 \tag{L-14310.3}
\]

It is the positive trace-class integral operator with kernel

\[
 \frac{\sin(\Omega(x-y))}{\pi(x-y)},
\]

and

\[
 \operatorname{Tr}K_\Omega=\frac{2\Omega}{\pi}.
 \tag{L-14310.4}
\]

Fix `0<eta<1` and let `S_(Omega,eta)` be the span of all eigenvectors of
`K_Omega` whose eigenvalues exceed `eta`.

Then

\[
 \boxed{
 \dim S_{\Omega,\eta}
 \le \left\lceil\frac{2\Omega}{\pi\eta}\right\rceil.}
 \tag{L-14310.5}
\]

For every `w` in the form domain with

\[
 w\perp S_{\Omega,\eta},
\]

one has the complete complement bound

\[
 \boxed{
 \mathcal L(w)
 \ge
 \left(C_0-\frac2\pi+(1-\eta)\log\Omega\right)
 \|w\|_2^2.}
 \tag{L-14310.6}
\]

The subspace `S_(Omega,eta)` is precisely a finite packet of the most
concentrated prolate modes for time interval `[-1,1]` and frequency interval
`[-Omega,Omega]`.

## Proof

All eigenvalues of `K_Omega` lie in `[0,1]`.  If `d` of them exceed `eta`, then

\[
 d\eta<\operatorname{Tr}K_\Omega=2\Omega/\pi,
\]

which gives (L-14310.5).  On the orthogonal complement of their eigenspaces,

\[
 \frac1{2\pi}\int_{-\Omega}^{\Omega}|\widehat w(z)|^2dz
 =\langle K_\Omega w,w\rangle
 \le\eta\|w\|_2^2.
 \tag{L-14310.7}
\]

Hence at least `(1-eta)||w||^2` of the Fourier energy lies outside the band.

The only negative part of `log|z|` occurs for `|z|<1`.  Since the support has
length two,

\[
 |\widehat w(z)|\le\sqrt2\|w\|_2.
\]

Therefore

\[
 \begin{aligned}
 \frac1{2\pi}\int_{|z|<1}
   \log|z|\,|\widehat w(z)|^2dz
 &\ge-
 \frac{2\|w\|_2^2}{2\pi}
 \int_{-1}^{1}|\log|z||dz\\
 &=-\frac2\pi\|w\|_2^2.
 \end{aligned}
 \tag{L-14310.8}
\]

The contribution from `1<=|z|<Omega` is nonnegative, while on
`|z|>=Omega`,

\[
 \log|z|\ge\log\Omega.
\]

Combining this with (L-14310.7), Plancherel, and the constant `C_0` proves
(L-14310.6).  QED.

## Suzuki localized Weil form

Let `q_a` be Suzuki's scaled form on `(-1,1)` from equation (4.5):

\[
 \begin{aligned}
 q_a(w)={}&\mathcal L(w)
 -(\log a+2A_\zeta+1)\|w\|_2^2\\
 &-\sum_{n\le e^{2a}}\frac{\Lambda(n)}{\sqrt n}
   \bigl(\langle T_{\log n/a}w,w\rangle
        +\langle T_{-\log n/a}w,w\rangle\bigr)\\
 &-\left\langle
   \bigl[a\,r''(a\,\cdot)\bigr]*w,w\right\rangle,
 \end{aligned}
 \tag{L-14310.9}
\]

where every translation is understood with zero extension outside `(-1,1)`.
Define the explicit perturbation majorant

\[
 \boxed{
 \kappa(a)=
 |\log a+2A_\zeta+1|
 +2\sum_{n\le e^{2a}}\frac{\Lambda(n)}{\sqrt n}
 +\int_{-2a}^{2a}|r''(u)|du.}
 \tag{L-14310.10}
\]

Then, for every form-domain vector,

\[
 \boxed{q_a(w)\ge\mathcal L(w)-\kappa(a)\|w\|_2^2.}
 \tag{L-14310.11}
\]

Indeed, each truncated translation has operator norm at most one, and Young's
inequality gives

\[
 \left\|a\,r''(a\,\cdot)*w\right\|_2
 \le
 \left(\int_{-2a}^{2a}|r''(u)|du\right)\|w\|_2.
\]

Consequently, for `w perpendicular S_(Omega,eta)`,

\[
 \boxed{
 q_a(w)\ge
 \Gamma(a,\Omega,\eta)\|w\|_2^2,}
 \tag{L-14310.12}
\]

where

\[
 \boxed{
 \Gamma(a,\Omega,\eta)
 =C_0-\frac2\pi+(1-\eta)\log\Omega-\kappa(a).}
 \tag{L-14310.13}
\]

For any prescribed real complement floor `G`, choosing

\[
 \log\Omega
 \ge
 \frac{G+\kappa(a)-C_0+2/\pi}{1-\eta}
 \tag{L-14310.14}
\]

makes `Gamma>=G`.  Thus the infinite complement of a finite explicitly
rank-bounded prolate packet has a rigorous lower floor.

## Consequences

### 1. Constructive finite Morse-index bound

Every spectral direction of `q_a` below `G` lies in a space of dimension at
most

\[
 \left\lceil\frac{2\Omega}{\pi\eta}\right\rceil
\]

for any `Omega` satisfying (L-14310.14).  In particular, the negative spectral
subspace is finite and has an explicit, though very conservative, prolate rank
bound.

### 2. Complete complement packet for L-14308

Take the low space in `L-14308` to contain `S_(Omega,eta)`.  The remaining
infinite-dimensional complement already satisfies (L-14310.12); no unproved
Fourier-tail positivity assertion is needed.  A finite middle-space enlargement
may be added to improve the moat without weakening the theorem.

### 3. The prolate basis is structural, not merely empirical

The same prolate concentration operator used by CCM is forced here by a simple
minimax principle: a vector outside the finite high-concentration packet must
place a fixed proportion of its Fourier energy where the logarithmic head is
large.  This gives an operator-theoretic reason that the low Weil spectrum is
well approximated by prolate modes.

## Size and sharpness audit

The crude prime norm in (L-14310.10) ignores cancellation and is roughly
exponential in `a`; the resulting `Omega` can therefore be extremely large.
The theorem removes the **infinite-complement logical gap**, not the practical
finite-block size problem.

Sharper replacements for `kappa(a)` are admissible:

- a directed operator norm of the complete translation polynomial;
- parity-separated norms;
- a block norm after selected prime channels are placed into the low packet;
- an exact finite-rank pole correction rather than an absolute-value charge.

Every improvement decreases the required prolate rank exponentially.

## Proof-producing interface

A finite certificate needs:

1. directed rational bounds for `C_0`, `pi`, `log Omega`, and `kappa(a)`;
2. exact rationals `eta`, `G`, and the support `a`;
3. an integer rank cap exceeding `2 Omega/(pi eta)`;
4. a provenance-bound complete prime-power sum and remainder-integral bound;
5. the declaration that the low block contains every concentration eigenvector
   above `eta`.

The last item can be implemented by a separate prolate eigenvalue enclosure or
by choosing a packet dimension above the trace cap and verifying the residual
concentration norm directly.

## Gap audit

- The trace bound controls dimension but does not supply explicit basis
  coefficients by itself.
- Formula (L-14310.9) and the constants `A_zeta,C_0,r` must be independently
  matched to Suzuki's exact normalization.
- The perturbation majorant is sufficient, not sharp.
- This lemma proves only complement coercivity.  The finite prolate low block
  may still contain a negative direction.
- No cofinal lower envelope has yet been proved, so RH is not resolved.

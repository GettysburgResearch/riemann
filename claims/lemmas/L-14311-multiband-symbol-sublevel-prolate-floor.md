# L-14311 — Multiband symbol sublevels give a finite generalized-prolate floor

Claim ID: `L-14311`  
Title: Only finitely many time-limited modes can concentrate on the low-symbol frequency set  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-09-b`  
Created: 2026-07-30  
Dependencies: Plancherel; trace of a time–frequency concentration operator; Suzuki equation (4.5)–(4.6); `L-14310`  
Scope: cancellation-aware complete complement for the localized Weil symbol  
Related counterexample candidates: none

## Abstract multiband theorem

Extend `w∈L^2(-1,1)` by zero to the real line and use

\[
 \|w\|_2^2=\frac1{2\pi}
 \int_{\mathbb R}|\widehat w(\xi)|^2d\xi.
 \tag{L-14311.1}
\]

Let `B⊂R` be measurable with finite Lebesgue measure `|B|`.  Define the
multiband concentration operator

\[
 K_B=P_T\mathcal F^{-1}1_B\mathcal F P_T,
 \qquad T=[-1,1],
 \tag{L-14311.2}
\]

so that

\[
 \langle K_Bw,w\rangle
 =\frac1{2\pi}\int_B|\widehat w(\xi)|^2d\xi.
 \tag{L-14311.3}
\]

It is a positive trace-class contraction and

\[
 \boxed{\operatorname{Tr}K_B=\frac{|B|}{\pi}.}
 \tag{L-14311.4}
\]

Fix `0<eta<1`, and let `S_(B,eta)` be the span of the eigenspaces of `K_B`
with eigenvalue greater than `eta`.  Then

\[
 \boxed{
 \dim S_{B,\eta}
 \le\left\lceil\frac{|B|}{\pi\eta}\right\rceil.}
 \tag{L-14311.5}
\]

Let `s:R→R` be measurable and suppose there are real numbers `m<=G` such that

\[
 s(\xi)\ge m\quad\text{a.e. on }\mathbb R,
 \qquad
 s(\xi)\ge G\quad\text{a.e. on }\mathbb R\setminus B.
 \tag{L-14311.6}
\]

For every `w⊥S_(B,eta)`, one has

\[
 \boxed{
 \frac1{2\pi}\int_{\mathbb R}
 s(\xi)|\widehat w(\xi)|^2d\xi
 \ge\bigl((1-\eta)G+\eta m\bigr)\|w\|_2^2.}
 \tag{L-14311.7}
\]

## Proof

The kernel diagonal of `K_B` equals `|B|/(2pi)`.  Integrating it over the
time interval of length two proves (L-14311.4).  If `d` eigenvalues exceed
`eta`, then

\[
 d\eta<\operatorname{Tr}K_B=|B|/\pi,
\]

which gives (L-14311.5).

On the orthogonal complement of those eigenspaces,

\[
 e_B(w):=
 \frac1{2\pi}\int_B|\widehat w(\xi)|^2d\xi
 \le\eta\|w\|_2^2.
\]

Using (L-14311.6),

\[
\begin{aligned}
 \frac1{2\pi}\int s|\widehat w|^2
 &\ge m e_B(w)+G(\|w\|_2^2-e_B(w))\\
 &=G\|w\|_2^2-(G-m)e_B(w)\\
 &\ge\bigl((1-\eta)G+\eta m\bigr)\|w\|_2^2.
\end{aligned}
\]

QED.

## Exact Suzuki symbol

For Suzuki's scaled form `q_a` on `(-1,1)`, put

\[
 \delta_n=\frac{\log n}{a},
 \qquad
 c_n=\frac{\Lambda(n)}{\sqrt n},
 \tag{L-14311.8}
\]

and extend every vector by zero.  The two translation correlations in (4.5)
are exactly the Fourier multiplier

\[
 2c_n\cos(\delta_n\xi).
\]

Let

\[
 k_a(t)=a\,r''(at)1_{[-2,2]}(t).
 \tag{L-14311.9}
\]

Then the smooth remainder is the multiplier `hat(k_a)(xi)`.  Define the
bounded-below modified symbol

\[
\begin{aligned}
 s_a^+(\xi)={}&C_0-\log a-(2A_\zeta+1)
 +\log_+|\xi|\\
 &-2\sum_{n\le e^{2a}}c_n\cos(\delta_n\xi)
 -\widehat{k_a}(\xi),
\end{aligned}
 \tag{L-14311.10}
\]

where `log_+ x=max(log x,0)`.

The negative logarithmic part has the universal compact-support charge from
`L-14310`:

\[
 \frac1{2\pi}\int_{|\xi|<1}
 \log|\xi|\,|\widehat w(\xi)|^2d\xi
 \ge-\frac2\pi\|w\|_2^2.
 \tag{L-14311.11}
\]

Consequently,

\[
 \boxed{
 q_a(w)\ge
 -\frac2\pi\|w\|_2^2
 +\frac1{2\pi}\int_{\mathbb R}
 s_a^+(\xi)|\widehat w(\xi)|^2d\xi.}
 \tag{L-14311.12}
\]

Suppose a finite union of frequency intervals `B_a` and directed constants
`m_a<=G_a` certify

\[
 s_a^+(\xi)\ge m_a\quad(\xi\in\mathbb R),
 \qquad
 s_a^+(\xi)\ge G_a\quad(\xi\notin B_a).
 \tag{L-14311.13}
\]

Then, on the complete orthogonal complement of `S_(B_a,eta)`,

\[
 \boxed{
 q_a(w)\ge
 \left[-\frac2\pi+(1-\eta)G_a+\eta m_a\right]
 \|w\|_2^2.}
 \tag{L-14311.14}
\]

The low packet has dimension at most

\[
 \boxed{
 \left\lceil\frac{|B_a|}{\pi\eta}\right\rceil.}
 \tag{L-14311.15}
\]

## Why this improves L-14310

`L-14310` declares the whole interval `[-Omega,Omega]` potentially bad and
charges the prime translations by their absolute coefficient sum.  The exact
prime symbol, however, contains strong oscillatory cancellation.  `L-14311`
retains that cancellation rigorously:

- interval arithmetic identifies only the cells where the total symbol may
  fall below the chosen floor;
- their total frequency measure, not the outermost frequency, controls the low
  packet rank;
- all good cells contribute their full positive symbol floor.

The finite-frequency alignment phenomenon does not invalidate the theorem.
Even if the prime cosines nearly re-align at isolated large frequencies, only
the measure of neighborhoods where the **complete** symbol is low enters the
trace bound.

## Certifying the sublevel cover

A production cover may be built as follows.

1. Choose a rational target floor `G_a` and an exact rational cell partition of
   a finite frequency window.
2. Enclose every phase `delta_n xi`, every cosine, and the smooth multiplier by
   directed balls on each cell.
3. Mark a cell bad unless the lower symbol endpoint exceeds `G_a`.
4. Prove an analytic tail threshold beyond which the `log_+` term dominates the
   complete bounded perturbation.
5. Merge adjacent bad cells and sum their rational lengths exactly.
6. Supply a global lower bound `m_a`, for example the coarse `L-14310`
   perturbation bound without the logarithmic growth.
7. Run `X-14306` on the exact bad-set measure and floor data.

No midpoint sign or sampled minimum enters the trust boundary.

## Structural consequences

### Generalized prolate packet

For a disconnected `B_a`, the eigenvectors of `K_(B_a)` are multiband or
generalized prolate functions.  They are the unique finite packet selected by
the geometry of the **actual arithmetic low-symbol set**, rather than by a
single symmetric band chosen in advance.

### Cancellation-aware finite reduction

Every localized Weil direction below the floor in (L-14311.14) lies in a
finite-dimensional generalized-prolate packet with the explicit rank cap
(L-14311.15).  Combining that packet with `L-14308` reduces the ambient problem
to one exact finite Schur block.

### Candidate scheduler

The measure `|B_a|` is a proof-relevant objective for selecting supports.  A
support with a smaller bad-symbol measure requires fewer low modes even if its
raw lowest Ritz value is similar.  This gives a new scheduler for the positive
RH search.

## Proof-producing interface

A certificate must bind:

1. exact support and complete prime-power manifest;
2. the normalization of `s_a^+`;
3. a directed finite union cover `B_a` and exact total length;
4. a global symbol lower bound `m_a`;
5. a good-region lower bound `G_a`;
6. an analytic infinite-frequency tail gate;
7. `eta`, the declared generalized-prolate packet, and its containment proof;
8. the exact rank and floor calculation checked by `X-14306`.

## Gap audit

- The abstract theorem is exact; the Suzuki specialization still needs an
  independent sign and Fourier-convention audit.
- A cellwise midpoint scan is not a sublevel-set certificate.
- The packet eigenfunctions for a multiband set are not the ordinary one-band
  PSWFs and require their own directed construction or a rank-cap surrogate.
- Small bad-set measure does not prove the finite low packet positive.
- The theorem removes the crude absolute-prime rank explosion only to the extent
  that the total symbol's low set can be rigorously shown to have small measure.
- No cofinal bad-set measure/floor theorem is currently available, so RH remains
  unproved.

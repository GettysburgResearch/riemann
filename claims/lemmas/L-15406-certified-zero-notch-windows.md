# L-15406 — Certified critical-line zeros generate zero-free spectral-notch prime windows

Claim ID: `L-15406`  
Title: Uniform-convolution factors suppress known line-zero background without losing sensitivity to an off-line displacement  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-07-31  
Dependencies: `L-15405`; elementary sine and Laplace-product estimates  
Scope: proof-producing refinement of the one-window terminal-prime criterion  
Related counterexample candidates: none

## General convolution family

Let `r_j>0` satisfy

\[
 \sum_{j=1}^\infty r_j<\infty.
 \tag{L-15406.1}
\]

For every `j`, let

\[
 u_{r_j}(t)=r_j^{-1}\mathbf1_{[0,r_j]}(t).
 \tag{L-15406.2}
\]

Assume the tail of `(r_j)` is chosen so that the infinite convolution has a
smooth density; for example, after finitely many arbitrary lengths, append

\[
 r_{m+k}=\eta2^{-k},
 \qquad k\ge1,
 \tag{L-15406.3}
\]

with `eta>0`. The argument of `L-15405` then gives a nonnegative smooth compact
density whose Laplace transform is

\[
\boxed{
 M_{\mathbf r}(z)=
 \prod_{j=1}^\infty
 {1-e^{-r_jz}\over r_jz}.}
 \tag{L-15406.4}
\]

Every factor is nonzero for `Re z>0`, so

\[
\boxed{M_{\mathbf r}(z)\ne0
 \qquad(\operatorname{Re}z>0).}
 \tag{L-15406.5}
\]

After shifting away from the origin and convolving the density with itself, one
obtains a smooth nonnegative terminal window satisfying the one-window
criterion of `T-15403`.

## Exact notch

Fix `gamma_0>0` and choose one length

\[
 r={2\pi\over\gamma_0}.
 \tag{L-15406.6}
\]

On the imaginary axis,

\[
 {1-e^{-ir\gamma}\over ir\gamma}
 =e^{-ir\gamma/2}
 {2\sin(r\gamma/2)\over r\gamma}.
 \tag{L-15406.7}
\]

Therefore the factor vanishes exactly at

\[
 z=i\gamma_0.
 \tag{L-15406.8}
\]

It remains nonzero throughout the open right half-plane.

## Directed zero-ball attenuation

Suppose an actual certified critical-line ordinate lies in

\[
 \gamma\in[\widetilde\gamma-\varepsilon,
            \widetilde\gamma+\varepsilon],
 \qquad
 0<\varepsilon<\widetilde\gamma,
 \tag{L-15406.9}
\]

and choose the exact design length

\[
 r={2\pi\over\widetilde\gamma}.
 \tag{L-15406.10}
\]

Then

\[
\boxed{
 \left|{1-e^{-ir\gamma}\over ir\gamma}\right|
 \le{\varepsilon\over\widetilde\gamma-\varepsilon}.}
 \tag{L-15406.11}
\]

Indeed, `r gamma/2=pi gamma/tilde gamma`, so

\[
 |\sin(r\gamma/2)|
 \le{\pi|\gamma-\widetilde\gamma|\over\widetilde\gamma},
\]

and division by `r gamma/2` gives (L-15406.11).

All other uniform-convolution factors have modulus at most one on the imaginary
axis. Thus one certified zero ball contributes at most

\[
 \left({\varepsilon\over
              \widetilde\gamma-\varepsilon}\right)^2
 \tag{L-15406.12}
\]

to the transform magnitude of the convolution-square terminal window.

## Off-line displacement survives

At the same ordinate but horizontal displacement `delta>0`, put

\[
 z=\delta+i\widetilde\gamma.
\]

The notch factor is

\[
\boxed{
 {1-e^{-rz}\over rz}
 ={1-e^{-r\delta}\over r(\delta+i\widetilde\gamma)}
e0.}
 \tag{L-15406.13}
\]

For small `delta`, its magnitude is asymptotic to

\[
 {\delta\over\widetilde\gamma}.
 \tag{L-15406.14}
\]

Consequently the convolution-square response is quadratic in the horizontal
displacement near a notched ordinate, but the false-RH exponential factor

\[
 e^{2a\delta}
 \tag{L-15406.15}
\]

eventually dominates every fixed polynomial loss.

Thus a notch removes a known on-line contribution without canceling a possible
off-line collision at the same height.

## Multiple notches and support cost

For certified ordinates `gamma_1,...,gamma_m`, prepend lengths

\[
 r_j={2\pi\over\widetilde\gamma_j},
 \qquad1\le j\le m,
 \tag{L-15406.16}
\]

then append a smooth dyadic tail. The extra physical support is

\[
\boxed{
 R_{notch}=2\pi\sum_{j=1}^m{1\over\widetilde\gamma_j}.}
 \tag{L-15406.17}
\]

High-height notches are therefore almost free in support length. Low zeros cost
more and should be selected by proof-relevant gain per support cost.

The resulting transform remains zero-free in `Re z>0`, regardless of the
number of finite notches.

## RH-valid moat improvement

Under RH, the explicit bound `B_*` of `T-15403` is a weighted sum of transform
magnitudes at critical-line ordinates. A certified notch replaces the selected
zero contribution by the rigorous attenuation factor (L-15406.12). Hence the
same zero tables used for direct-xi deflation can reduce the terminal-prime RH
bound without entering the prime statistic itself.

This gives the scheduling objective

\[
 {\text{certified reduction in }B_*
  \over
  2\pi/\widetilde\gamma}.
 \tag{L-15406.18}
\]

The numerator includes the zero multiplicity and all previously installed
factors.

## Density limitation

The support cost is not cosmetic. The nontrivial zero density is too large to
notch every zero with a compactly supported uniform-convolution profile: the sum
of reciprocal ordinates diverges. The method is therefore a finite adaptive
background suppressor, not a way to annihilate the entire critical-line
spectrum.

This limitation is consistent with exponential-type zero-density constraints.

## Proof-producing schema

A certificate binds:

1. every exact rational design ordinate `tilde gamma_j` and corresponding
   length `2pi/tilde gamma_j` through directed pi intervals;
2. the source critical-line zero balls and multiplicities;
3. the attenuation comparisons (L-15406.11)--(L-15406.12);
4. the finite total support and terminal annulus;
5. the dyadic smooth tail and its transform bound;
6. the resulting explicit RH-valid moat `B_*`;
7. the prime-window value and strict final comparison.

For exact arithmetic implementations, one may replace `2pi/tilde gamma_j` by a
rational interval length and directly optimize the maximum sine factor over the
certified zero ball.

## Wider meaning

Certified-zero deflation and terminal-prime windows are dual descriptions of
the same spectral operation:

```text
zero side: subtract known line mass;
prime side: install transform notches at known line ordinates.
```

The prime-side form preserves sensitivity to horizontal displacement and uses a
single finite von Mangoldt window.

## Gap audit

- Exact notches involving `2pi/gamma` are analytic objects; numerical producers
  need outward intervals.
- A near-notch is not an exact zero and must use the complete attenuation bound.
- The convolution-square transform squares the attenuation factor.
- Notching finitely many known zeros does not prove RH.
- A false-RH response may remain extremely small at moderate support when the
  displacement is tiny; exponential dominance is only cofinal.

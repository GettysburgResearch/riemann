# L-23005 — Deep-contour closure for one complete lattice variable

Claim ID: `L-23005`  
Title: A pole-cancelled complete integer-lattice row may be shifted arbitrarily far left, so every genuinely free large variable is exponentially negligible relative to its logarithmic reserve  
Status: **PROPOSED — COMPLETE ANALYTIC LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-o`  
Created: 2026-08-07  
Dependencies: elementary Mellin inversion; analytic continuation and polynomial vertical growth of `zeta` and its derivatives; the terminal-row notation of `L-15449`  
Scope: rows containing one unrestricted complete positive-integer variable; no estimate for truncated Möbius boundary packets

## 1. Setup

Let `W` be compactly supported and `C^M`, and write its bilateral Laplace
transform as

\[
 \widehat W(z)=\int_{\mathbb R}e^{-zu}W(u)\,du.
\]

Let

\[
 P(y)=\sum_{k=0}^{d}p_k y^k
\]

be a polynomial of degree at most `d`. Assume that `widehat W` has a zero of
order at least `d+1` at

\[
 z=\frac12.
\tag{L-23005.1}
\]

For `A>=1`, define the complete lattice row

\[
 \boxed{
 \mathcal T_{A,P,W}(x)
 =\sum_{n\ge1}{P(\log n)\over\sqrt{An}}
  W\!\left(x-\log(An)\right).}
\tag{L-23005.2}
\]

The sum is finite at every `x` because `W` is compactly supported.

## 2. Exact transform

For `Re z>1/2`, Fubini gives

\[
 \int_{\mathbb R}\mathcal T_{A,P,W}(x)e^{-zx}\,dx
 =A^{-z-1/2}\widehat W(z)
   \sum_{n\ge1}P(\log n)n^{-z-1/2}.
\tag{L-23005.3}
\]

Put

\[
 \mathcal Z_P(s)
 =\sum_{n\ge1}P(\log n)n^{-s}
 =\sum_{k=0}^{d}p_k(-1)^k\zeta^{(k)}(s).
\tag{L-23005.4}
\]

The only pole of `mathcal Z_P` is at `s=1`, of order at most `d+1`.
By (L-23005.1), the product

\[
 \widehat W(z)\mathcal Z_P(z+1/2)
\]

is entire. In particular, nontrivial zeta zeros create no singularity because
only zeta and its derivatives, not reciprocal zeta, occur in this complete
lattice row.

## 3. Arbitrary left shift

Fix `sigma>0`. Suppose `M` is large enough that on the line

\[
 \operatorname{Re}z=-\frac12-\sigma
\]

the product in (L-23005.3) is absolutely integrable. This follows from the
standard polynomial vertical growth of `zeta^(k)` together with sufficiently
many integrations by parts in `widehat W`.

Mellin inversion and contour displacement then give

\[
 \boxed{
 \mathcal T_{A,P,W}(x)
 ={1\over2\pi i}
 \int_{(-1/2-\sigma)}
 e^{zx}A^{-z-1/2}\widehat W(z)
 \mathcal Z_P(z+1/2)\,dz.}
\tag{L-23005.5}
\]

No residue is crossed: the sole zeta pole was cancelled exactly by the window
moments.

Consequently there is a finite constant `C_(sigma,P,W)` such that

\[
 \boxed{
 |\mathcal T_{A,P,W}(x)|
 \le C_{\sigma,P,W}
 A^{\sigma}e^{-(1/2+\sigma)x}.}
\tag{L-23005.6}
\]

This sharpens the first-Euler-remainder estimate of `L-15449` whenever there is
a strict logarithmic gap between `A` and the output scale.

## 4. Source-family consequence

Let `J<=x<=J+1`, and consider a source-bound family

\[
 \mathcal T_J(x)=\sum_{A\in\mathcal A_J}c_A
 \mathcal T_{A,P_A,W}(x).
\tag{L-23005.7}
\]

Assume

\[
 \log A\le(1-\delta)J+C,
 \qquad \delta>0,
\tag{L-23005.8}
\]

and

\[
 \sum_{A\in\mathcal A_J}|c_A|C_{\sigma,P_A,W}
 \le \exp((\alpha+o(1))J).
\tag{L-23005.9}
\]

Then (L-23005.6) yields

\[
 \boxed{
 \sup_{J\le x\le J+1}|\mathcal T_J(x)|
 \le
 \exp\left[
  \left(\alpha-\frac12-\sigma\delta+o(1)\right)J
 \right].}
\tag{L-23005.10}
\]

For fixed `alpha` and `delta`, any sufficiently large fixed `sigma` gives a
strictly negative exponent, provided the common window has enough smoothness
for that contour.

Thus every packet row with one genuinely unrestricted complete large lattice
variable and a strict reserve in the complementary coefficient word is closed
without a prime theorem, a zero-free region, or RH.

## 5. Application to the high-order packet programme

In a Heath--Brown row, the logarithmic variable `q` and the auxiliary
`1`-convolution variables are unrestricted. If one such variable carries at
least `delta J` of logarithmic scale, freeze all other variables into `A` and
apply (L-23005.10). The same applies to the unrestricted residual variables in
the finite Möbius resolvent.

Therefore the balanced Type-II theorem need not include rows in which a complete
unrestricted variable remains macroscopically large. Those rows are analytic
lattice discrepancies and are removable by deep contour shift after exact pole
moment cancellation.

The surviving corner is the one in which every unrestricted variable is small
and the truncated Möbius variables carry essentially the complete output scale.
That corner is identified exactly in `L-23006` and `R-23003`.

## 6. Safe smoothing interface

The piecewise-linear windows of `L-15155` have only fixed `t^-2` vertical decay.
For a prescribed fixed `sigma`, convolve them with a compact B-spline factor
whose transform has zeros only on the imaginary boundary. This increases
smoothness, preserves the boundary zeros at `0` and `1/2`, introduces no zero in
`0<Re z<1/2`, and permits the contour shift in Section 3.

The smoothing order may depend on the fixed packet order and the chosen fixed
`sigma`; it is not allowed to grow with the output scale without the
pole-sensitivity audit of `R-23003`.

## 7. Proof boundary

Closed in this lemma, subject to routine contour-growth review:

- the exact complete-lattice transform;
- cancellation of its only pole;
- arbitrary fixed left displacement;
- exponential closure of every free-large-variable source family with a strict
  complementary reserve.

Not closed:

- rows whose large scale is carried entirely by truncated Möbius variables;
- signed cancellation between different Heath--Brown orders;
- the first-cell Mertens mutation;
- `BTP(K)` or RH.

# Full-problem continuation — Haar audit and the sharp prime-debt barrier

Author: `gpt56-pro-09-n`  
Date: 2026-08-07  
Branch: `agent/gpt56-pro-09-n/202-haar-renormalization`  
Status: **PROPOSED; RH remains unproved and undisproved**

## 1. Valid global core

The following branch results remain the active full-problem route:

1. `T-20201`: the dyadic Haar defect
   \[
   D_2(t)=4\Psi(t)-\Psi(2t)
   \]
   is RH-nonnegative, and proposed Landau/pole descent makes eventual sampled
   nonnegativity or subpower negative part equivalent to RH.
2. `T-20203`: for every fixed integer `r>=2`,
   \[
   D_r(t)=r^2\Psi(t)-\Psi(rt)
   \]
   has the same pole-descent completeness on its critical logarithmic mesh.
3. `L-20202/L-20203`: exact prime-power and Chebyshev--Riesz formulas. The
   negative prime prefix is `q<n^(2/(r+1))`, while the terminal band and Lerch
   channel have the favorable sign.
4. `L-20204`: each `r`-adic spectral multiplier is a finite positive Gram
   portfolio of four-tap FIR vectors.
5. `T-20202`: the real-axis dyadic logarithmic-derivative ratio is proposed to
   be completely monotone exactly under RH, giving a one-point all-order
   Stieltjes-Hankel hierarchy.

These statements remain proposed pending independent review of normalization,
Landau continuation, and the moment-determinacy converse.

## 2. Refuted continuation

The later terminal-flat draft used

\[
 F_{r,M}=D_r-M^{-2}D_{Mr}
\]

and claimed `F_(r,M)>=0` under RH. Exact algebra gives instead

\[
 \boxed{F_{r,M}(t)=-M^{-2}D_M(rt).}
\]

Thus RH gives `F_(r,M)<=0`. `R-20202` records the refutation, and
`T-20204/T-20205/L-20206/L-20207` have been corrected or narrowed.

This was not cosmetic: the false orientation was what made all new prime
coefficients appear favorable. The corrected statistic is only a rescaled old
`M`-adic defect.

## 3. Sharp finite-filter obstruction

For any nonzero degree-`N` positive screw filter

\[
 P(x)=\sum_{k=1}^N\lambda_k(1-\cos kx)\ge0,
\]

define

\[
 L_P(s)=\sum_{k=1}^N\lambda_k(k-s)_+.
\]

`L-20208` proves

\[
 \frac{L_P(1/2)}{L_P(0)}
 \ge
 \sin^2\!\frac{\pi}{2(N+1)}.
\]

The bound is sharp, with equality for the alternating-sine Fejer factor. At
base support `t=log 4`, the first prime lies at the normalized half-knot, so
**every** finite positive filter retains a strictly negative `q=2` prime
coefficient. The optimal debt decays only as `pi^2/(4N^2)`.

`L-20210` extends strict half-knot positivity to every fixed stable `H^2`
filter. A fixed infinite summable mixture cannot remove the debt either. Only a
growing-degree or singular cofinal limit can approach zero.

## 4. Exact autocorrelation bridge

`L-20209` identifies the ramp with one aperiodic autocorrelation sequence. If

\[
 P=|(1-z)Q(z)|^2,
 \qquad Q(z)=\sum_{j=0}^{N-1}q_jz^j,
\]

and

\[
 d_m=\operatorname{Re}\sum_jq_{j+m}\overline{q_j},
\]

then

\[
 L_P(m)=2d_m,
\]

and between knots `L_P` is their linear interpolation. The complete prime
contraction is therefore

\[
 -2t\sum_mW_m(t)d_m
\]

with explicit nonnegative prime-deposition weights `W_m(t)`.

This unifies the Haar/screw route with:

- Toeplitz carrier contractions;
- low-autocorrelation sequence design;
- the square-screw D-0001 coordinate;
- the prime-polygon and Chebyshev--Riesz formulations.

## 5. Correct global target

The new theorems rule out the tempting shortcut “choose one positive filter
with all prime coefficients favorable.” That is impossible.

The actual remaining theorem is a cofinal **bulk transport versus
 autocorrelation debt** inequality:

\[
 \text{positive terminal prime mass + exact archimedean/pole balance}
 \ge
 2t_N\sum_mW_m(t_N)(d_m^{(N)})_+ - o(1)
\]

for a growing, pole-descent-complete family.

Equivalent coordinates are:

1. the prime-polygon margin `B_j-F*(A_j)` of PR #219;
2. the Chebyshev--Riesz excess of PR #202;
3. the terminal prime-pair energy of PR #216;
4. the growing Toeplitz/autocorrelation matrix of the present branch.

A proof must preserve cancellation. Entrywise absolute values or a phase-blind
PNT remainder are too large.

## 6. Immediate attack

1. Use the equality Fejer factor as the canonical degree-`N` endpoint profile.
2. Emit its exact autocorrelations and prime-ramp deposition ledger.
3. Center the terminal prime/polar main term before taking norms.
4. Compare the remaining quadratic form with the Selberg log-convolution
   identity from PR #216.
5. Search for an exact positive square plus a remainder bounded by the sharp
   `O(N^-2)` half-knot debt.
6. Keep the prime-polygon recurrence as the independent scalar replay.

No finite positive ladder can replace the cofinal estimate. No RH claim is made.

# R-22102 — Resolution/diagonalization uncertainty barrier

Claim ID: `R-22102`  
Title: A safe window narrow enough to diagonalize log-prime translates necessarily creates an exponential diagonal that masks the whole counterexample strip  
Status: `PROPOSED — COMPLETE SCALING NO-GO`  
Authoring agent: `gpt56-pro-18`  
Created: 2026-08-07  
Issue: #221  
Dependencies: `L-21501`, `T-21502`; the prime number theorem

## 1. Narrow safe family

Let `phi` be the unit triangular spline of `L-21501`, with

\[
 \|\phi\|_2^2=\frac23.
\]

For `delta>0`, define its integral-normalized compression

\[
 \phi_\delta(u)=\delta^{-1}\phi(u/\delta).
 \tag{R-22102.1}
\]

Then

\[
 \operatorname{supp}\phi_\delta=[0,2\delta],
 \qquad
 \|\phi_\delta\|_2^2=\frac{2}{3\delta},
 \tag{R-22102.2}
\]

and

\[
 \widehat\phi_\delta(z)
 =\left(\frac{1-e^{-\delta z}}{\delta z}\right)^2.
\]

With `h=log 4`, define

\[
 G_\delta(u)=\phi_\delta(u-1)-2\phi_\delta(u-1-h)
 \tag{R-22102.3}
\]

and

\[
 H_\delta(u)=G_\delta(u)-G_\delta(u-1).
 \tag{R-22102.4}
\]

Its transform is

\[
 \boxed{
 \widehat H_\delta(z)
 =e^{-z}
  \left(\frac{1-e^{-\delta z}}{\delta z}\right)^2
  (1-2e^{-hz})(1-e^{-z}).
 }
 \tag{R-22102.5}
\]

For every fixed `z` with `0<Re z<1/2`,

\[
 \widehat H_\delta(z)
 \longrightarrow
 e^{-z}(1-2e^{-hz})(1-e^{-z})\ne0
 \tag{R-22102.6}
\]

as `delta->0`. Thus narrowing does not erase any fixed hypothetical off-line
zero.

## 2. Exact diagonal cost

If

\[
 0<2\delta<h-1,
\]

the four translated triangular pieces in (R-22102.4) are pairwise disjoint.
Their coefficients are `1,-2,-1,2`; hence

\[
 \boxed{
 \|H_\delta\|_2^2
 =10\|\phi_\delta\|_2^2
 =\frac{20}{3\delta}.
 }
 \tag{R-22102.7}
\]

For the ordinary-prime signal formed with `H_delta`, the fully interior diagonal
through logarithmic height `X` is therefore

\[
 \mathcal D_\delta(X)
 =\frac{20}{3\delta}
  \sum_{p\le e^{X-O(1)}}\frac{(\log p)^2}{p}.
 \tag{R-22102.8}
\]

The prime number theorem gives

\[
 \sum_{p\le e^X}\frac{(\log p)^2}{p}
 =\frac12X^2+O(X),
 \tag{R-22102.9}
\]

so

\[
 \boxed{
 \mathcal D_\delta(X)
 =\left(\frac{10}{3}+o(1)\right)\frac{X^2}{\delta}.
 }
 \tag{R-22102.10}
\]

If `delta=exp(-alpha X+o(X))`, its contribution to the Hardy-energy exponent is

\[
 \limsup\frac{\log\mathcal D_\delta(X)}{2X}=\frac\alpha2.
 \tag{R-22102.11}
\]

## 3. Diagonalization requires the fatal scale

For distinct integers `m<n<=e^X`,

\[
 \log n-\log m
 \ge\log(1+e^{-X})
 =e^{-X+o(X)}.
 \tag{R-22102.12}
\]

Consequently a deterministic window resolution that makes every distinct
log-prime translate disjoint through height `X` must satisfy

\[
 \delta_X\le e^{-X+o(X)}.
 \tag{R-22102.13}
\]

By (R-22102.11), the diagonal then has Hardy exponent `1/2`. This is the largest
possible rightmost-zero displacement:

\[
 0\le\Theta_\zeta\le\frac12.
\]

Thus complete diagonalization masks every possible off-line exponent instead of
excluding it.

Conversely, keeping the diagonal subexponential requires

\[
 \log(1/\delta_X)=o(X),
 \tag{R-22102.14}
\]

which leaves exponentially many neighboring primes inside one resolution cell.
The signed pair cancellation remains unavoidable.

## 4. Consequence

No proof can close the prime-energy route by:

1. shrinking the safe window until prime translates are disjoint;
2. retaining nonvanishing response at fixed off-line zeros;
3. and then bounding only the resulting diagonal.

These three requirements violate the exact scaling law (R-22102.10).

A successful proof must control the coherent signed semiprime form at a
subexponential-resolution window. This is an uncertainty-principle obstruction,
not a computational limitation.

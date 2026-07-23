# L-2805 — Exact rational enclosure of the carrier scalar

Claim ID: L-2805  
Title: Machin and atanh series give a self-contained rational enclosure of `alpha(T)`  
Status: PROPOSED  
Authoring agent: `gpt56-04-c`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: elementary power series only  
Scope: the scalar `alpha(T)=log(T/(2*pi))/(2*pi)` used by D-0801  
Related counterexample candidates: any carrier fixed-vector certificate

## Statement

Let `T>0` be rational. For positive integers `M_5`, `M_239`, and `M_log`,
there is a finite exact-rational algorithm producing an interval

\[
 [\alpha_-,\alpha_+]\ni
 \alpha(T)=\frac{\log(T/(2\pi))}{2\pi}.
\]

The algorithm uses:

1. Machin's identity
   \[
   \pi=16\arctan(1/5)-4\arctan(1/239);
   \]
2. the alternating arctangent series with its next-term remainder;
3. exact power-of-two range reduction for every logarithm;
4. the positive series
   \[
   \log y=2\sum_{j=0}^{\infty}
   \frac{z^{2j+1}}{2j+1},
   \qquad z=\frac{y-1}{y+1},\quad 1\le y\le2;
   \]
5. the explicit tail bound
   \[
   0\le
   \log y-2\sum_{j=0}^{M-1}\frac{z^{2j+1}}{2j+1}
   \le
   \frac{2z^{2M+1}}{(2M+1)(1-z^2)}.
   \]

All interval endpoints before final export are exact rational numbers. Rounding
outward to a chosen denominator `2^B` preserves containment.

At the optimized carrier

\[
 T=4709203636353.65=\frac{94184072727073}{20},
\]

using

```text
M_5=80, M_239=20, M_log=90, B=192
```

X-2802 proves

\[
 \boxed{
 \frac{27316188863170422972141786876274838781565257086415513364963}{2^{192}}
 \le \alpha(T)\le
 \frac{27316188863170422972141786876274838781565257086415513364964}{2^{192}}.}
\]

The interval is exactly one `2^-192` unit wide.

## Proof

### Machin identity

Put `A=arctan(1/5)` and `B=arctan(1/239)` in their principal real branches.
The double-angle formula gives

\[
 \tan(2A)=\frac{5}{12},
 \qquad
 \tan(4A)=\frac{120}{119}.
\]

Therefore

\[
 \tan(4A-B)
 =\frac{120/119-1/239}{1+(120/119)(1/239)}=1.
\]

Also `0<4A-B<pi/2`, so `4A-B=pi/4`, proving Machin's identity.

For `0<=x<=1`, the arctangent expansion is alternating with monotonically
decreasing term magnitudes:

\[
 \arctan x=\sum_{k=0}^{M-1}\frac{(-1)^k x^{2k+1}}{2k+1}+R_M,
 \qquad |R_M|\le\frac{x^{2M+1}}{2M+1},
\]

with the sign of `R_M` equal to the next term. Thus each arctangent, and hence
`pi`, receives an exact rational lower and upper endpoint.

### Logarithm enclosure

For any positive rational `x`, exact integer comparisons determine the unique
integer `k` such that

\[
 2^k\le x<2^{k+1}.
\]

Writing `x=2^k y` gives `1<=y<2` and

\[
 \log x=k\log2+\log y.
\]

For `z=(y-1)/(y+1)`, one has `0<=z<=1/3`, and integrating the geometric series
for `1/(1-t^2)` gives

\[
 \log y=2\operatorname{artanh}z
       =2\sum_{j=0}^{\infty}\frac{z^{2j+1}}{2j+1}.
\]

All terms are nonnegative. Bounding every omitted denominator by `2M+1` and
summing the remaining geometric series proves the displayed tail inequality.
The same formula with `y=2` encloses `log2`. If `k<0`, multiplication by `k`
reverses the appropriate interval endpoints; X-2802 handles this explicitly.

### Propagation to `alpha`

The positive `pi` interval first gives an interval for `T/(2*pi)`. Monotonicity
of the real logarithm gives a logarithm interval from its two rational endpoint
calculations. Division of that interval by the positive interval `2*pi` is
performed by taking the minimum and maximum of all four endpoint quotients.
Every operation is inclusion-preserving exact rational interval arithmetic.
Final floor/ceiling rounding to denominator `2^B` therefore proves the exported
dyadic enclosure.

## Analytic domain audit

- `T` is a positive rational number.
- Only the ordinary real logarithm on `(0,infinity)` is used.
- Both arctangent arguments lie in `(0,1)`.
- Every denominator in the series and interval operations is positive.
- No complex branch, prime computation, zeta value, or floating operation enters
  the proof backend.

## Dependency audit

The result is independent of D-0801 admissibility, the Guinand--Weil formula,
prime enumeration, phase reduction, and the carrier eigenvector. It supplies
only the exact scalar interval consumed by L-2804.

## Gap audit

1. The mpmath containment test in X-2802 is a regression control, not part of the
   proof.
2. A narrow `alpha` interval does not certify the prime Rayleigh value.
3. The carrier in a real certificate must match the exact rational encoded here.
4. Changing any series count changes the proof object and must change the
   parameter fingerprint.

## Adversarial tests

X-2802 rejects schema drift and Boolean values masquerading as integers, checks
a negative-`alpha` small carrier, verifies precision refinement does not widen
the target dyadic interval, and compares the target enclosure with an
independent 100-decimal control.

## Remaining uncertainty

No mathematical uncertainty is known in the finite interval construction. The
claim remains `PROPOSED` until independent code and proof review.

## Suggested next attack

Insert the committed target interval directly into the first real
`riemann.piecewise-carrier-fixed-vector.v1` certificate. No transcendental
`alpha` producer is needed beyond this exact artifact.

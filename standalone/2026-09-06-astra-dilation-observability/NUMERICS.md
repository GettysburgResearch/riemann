# Infinite Gram entries with finite, outward-rounded arithmetic

**Scope:** all 120 symmetric Gram entries for indices 2 through 16;
projections at N = 2, 3, 4, 8, 16; complete doubling gains at N = 2, 4, 8.
The first 1,024 summands are used only as a coarse cross-check. They are not
the definition of the computed Gram. No zero, prime, conductor, or large
parameter search is run.

The implementation uses Python's standard-library integers and `Fraction`.
`intervals.py` represents endpoints by integers divided by 2^224 and rounds
every arithmetic operation outwards. It is research code requiring review,
not a proof-kernel-verified arithmetic library. The analytic justification
for the enclosures is given here rather than inferred from agreement with a
high-precision floating-point library.

## 1. Periodic summation identity

For fixed j,k, let L=lcm(j,k) and

\[
a_r=\frac{(r\bmod j)(r\bmod k)}{jk}\quad(1\le r\le L).
\]

Since a_L=0, grouping the absolutely convergent positive series gives

\[
G_{jk}=\frac1L\sum_{r=1}^{L-1}a_r
\left[\psi\left(\frac{r+1}L\right)-\psi\left(\frac rL\right)\right].
\tag{N1}
\]

Indeed,

\[
\sum_{u\ge0}\frac1{(Lu+r)(Lu+r+1)}
=\frac1L\sum_{u\ge0}\left(\frac1{u+r/L}-\frac1{u+(r+1)/L}\right),
\]

which is the digamma difference in (N1). All weights a_r are exact rational
numbers taken directly from the fractional-part dictionary. In this frozen
domain L is at most 240.

## 2. Digamma remainder: an actual bound, not an asymptotic instruction

For x>0 define equivalently

\[
\psi(x)=\lim_{M\to\infty}\left(\log M-\sum_{j=0}^{M-1}\frac1{x+j}\right).
\]

Apply Euler–Maclaurin to t↦1/(x+t) on [0,M], including the Bernoulli terms
through degree 2m. Its derivative of order 2m is
(2m)!/(x+t)^(2m+1). Passing to the limit yields

\[
\psi(x)=\log x-\frac1{2x}
 -\sum_{k=1}^m\frac{B_{2k}}{2k x^{2k}}+R_m(x),
\quad
|R_m(x)|\le\frac{\sup_{0\le u\le1}|B_{2m}(u)|}{2m x^{2m}}.
\tag{N2}
\]

This deliberately conservative bound is enough; we do not need the sharper
first-omitted-term bound for positive x stated in DLMF §5.11(ii). The periodic
Bernoulli integral is absolutely convergent. The coefficient expansion

\[
B_d(u)=\sum_{j=0}^d\binom dj B_j u^{d-j}
\]

implies the rational bound

\[
\sup_{0\le u\le1}|B_d(u)|\le
A_d:=\sum_{j=0}^d\binom dj|B_j|.
\]

Bernoulli numbers are computed from B_0=1 and
sum_{j=0}^n binom(n+1,j) B_j=0 for n≥1. The source check includes
B_2=1/6 and B_32=-7709321041217/510.

We use m=16 and y=x+128. The exact recurrence gives

\[
\psi(x)=\psi(y)-\sum_{j=0}^{127}\frac1{x+j}.
\tag{N3}
\]

Evaluate the displayed terms of (N2) at y and add the interval
[-A_32/(32 y^32), A_32/(32 y^32)]. Then subtract the finite rational sum in
(N3). Formula (N1) now has a full analytic tail enclosure.

## 3. Elementary logarithm and independent low-dimensional formulas

For a positive rational x, write x=2^e y with 1≤y<2 and put
z=(y-1)/(y+1), so 0≤z<1/3. Use

\[
\log y=2\sum_{j=0}^{T-1}\frac{z^{2j+1}}{2j+1}+E_T,
\quad 0\le E_T\le
\frac{2z^{2T+1}}{(2T+1)(1-z^2)}.
\tag{N4}
\]

Use the same formula at z=1/3 for log 2. T=90 is fixed. All powers, endpoints
and remainders are rational or outward dyadic operations, with no float
conversion. `sqrt` uses integer square roots of scaled integer endpoints.

As an independent algebraic cross-check, integral summation gives

\[
G_{22}=\frac{\log2}{4},\qquad
G_{23}=\frac{\log2}{6}+\frac{\log3}{12}-\frac{\pi}{18\sqrt3},
\qquad G_{33}=\frac{2\log3}{9}-\frac{\pi}{27\sqrt3}.
\tag{N5}
\]

To verify (N5), use 1/[n(n+1)]=integral_0^1 (1-x)x^(n-1) dx. The integrands
for G_22 and G_33 reduce to 1/[4(1+x)] and
(1+4x)/[9(1+x+x²)]. For G_23 the rational integrand is

\[
\frac{1+2x^4}{6(1+x+x^2+x^3+x^4+x^5)}
=\frac{2x+1}{12(x^2+x+1)}-
 \frac1{12(x^2-x+1)}+\frac1{6(x+1)}.
\]

Integrating these expressions proves (N5). The π enclosure for this check
comes independently from Machin's identity
π=16 arctan(1/5)-4 arctan(1/239), using 100 terms of each alternating
rational series and its first-omitted-term bound. It is not used in the
main periodic Gram construction.

A second, coarse check encloses each Gram between its first 1,024 summands
and that partial sum plus 1/1,025. This tail bound follows simply from
0≤a_n≤1 and the telescoping weight sum. It checks the normalization but is
not responsible for the tight final bounds.

## 4. Linear algebra and strict acceptance

Gaussian elimination and back-substitution are performed using interval
operations. Every pivot must have a strictly positive lower endpoint;
a zero-containing pivot is refused. The exact positive definiteness of
the underlying matrix is also proved independently in PROOF.md using the
dual system. Positive interval pivots confirm the bounded implementation.

The output encloses the solution of the *exact* linear system, not just the
residual of a proposed solution. It gives delta_N, the first-cell value,
the full Schur gain, and the one-dilation innovation. The complete block
Schur calculation and the difference delta_N-delta_2N are computed by two
expressions and must have overlapping intervals. Scalar distance, first-cell
and full-gain enclosure widths must be below 10^-25.

The special rejections include N=3 first-cell overshoot and N=8 strictly
negative dilation leakage: the relevant interval must lie strictly on the
claimed side of zero. All JSON data are rebuilt from the source formulas.
Hashes additionally bind the proof, numerical justification, code and
stored output, but hashes alone do not certify mathematics.

## 5. Exact controls and interpretation

The bounded arithmetic controls cover dilation identities, weight
preservation on finite-support vectors, Möbius inversion by two finite
methods, dual biorthogonality and the support witness, elementary interval
arithmetic, recurrence checks, low-dimensional closed forms, and the coarse
Gram tail comparison. `test_replay.py` tests type, division, pivot, parser,
manifest and mutation rejection. Assertions in the unit-test framework are
not Python `assert` statements; the scientific replay uses explicit checks
and refuses under optimized Python as well.

The scientific meaning is narrow: full infinite sums in a fixed finite Gram
problem have directed enclosures, and the quoted finite counterexamples are
established subject to review of this code and its remainder proof. This
does not certify (G), cofinal overshoot, a convergence rate, the classical
RH equivalence, an external numerical campaign, or an RH proof.

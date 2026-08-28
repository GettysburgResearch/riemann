# Divisor-wave Fourier modes carry two shifted reciprocal-zeta factors

Status: **exact Fourier--hyperbola formula for every height prefix, exact
squarefree divisor-polynomial factorization, and exact shifted reciprocal-zeta
Euler factorization; no mode estimate, HIGHGCDWAVE estimate, RH, or GRH**

Architecture: **Architecture A only**.

Bounded replay:
[`ffps_divisor_wave_shifted_zeta_factorization.py`](ffps_divisor_wave_shifted_zeta_factorization.py).
Canonical fixture:
[`ffps_divisor_wave_shifted_zeta_factorization.json`](ffps_divisor_wave_shifted_zeta_factorization.json).

Frozen predecessor: the high balanced gcd-wave localization packet at
`cf5cf6876dce5c8a969ad4636055215f7cec395d`.

## 0. Outcome

The remaining `HIGHGCDWAVE` gate cannot be treated as a generic smooth
bilinear form whose Fourier modes have lost the zeta obstruction.  Each
untruncated Fourier mode has an exact Dirichlet series with **two shifted
reciprocal-zeta factors**.

Use the Fourier convention
\[
 \mathcal R(u)={1\over2\pi}\int_{\mathbb R}
 \widehat{\mathcal R}(\xi)e^{i\xi u}\,d\xi.
\tag{0.1}
\]
For a max-height prefix define
\[
 \mathcal W_{\le T}^\alpha(N)
 =
 \sum_{\substack{a\mid N\\
  \max(67^\alpha a,N/a)\le T}}
 \mathcal R\!\left(\log{67^\alpha a^2\over N}\right).
\tag{0.2}
\]
Then
\[
\boxed{
 \mathcal W_{\le T}^\alpha(N)
 ={1\over2\pi}\int_{\mathbb R}
 \widehat{\mathcal R}(\xi)\,
 67^{i\alpha\xi}N^{-i\xi}
 \sum_{\substack{a\mid N\\N/T\le a\le T/67^\alpha}}
 a^{2i\xi}\,d\xi.
}
\tag{0.3}
\]
Every dyadic height wavelet is a difference of two such prefixes.

Remove the hyperbola cutoff temporarily and put
\[
 D_\xi(N)=N^{-i\xi}\sum_{a\mid N}a^{2i\xi}.
\tag{0.4}
\]
For squarefree `N`,
\[
\boxed{
 D_\xi(N)=\prod_{p\mid N}
 (p^{i\xi}+p^{-i\xi})
 =\prod_{p\mid N}2\cos(\xi\log p).
}
\tag{0.5}
\]

Let
\[
 \zeta^{(67)}(w)
 =\prod_{p\ne67}(1-p^{-w})^{-1}
 =\zeta(w)(1-67^{-w}).
\tag{0.6}
\]
For `Re(s)>1`, absolute convergence gives
\[
 F_\xi(s)
 :=\sum_{\substack{N\ {\rm squarefree}\\67\nmid N}}
 {\mu(N)D_\xi(N)\over N^s}
 =\prod_{p\ne67}
 \left(1-(p^{i\xi}+p^{-i\xi})p^{-s}\right).
\tag{0.7}
\]
This has the exact factorization
\[
\boxed{
 F_\xi(s)
 ={E_\xi(s)\over
   \zeta^{(67)}(s-i\xi)\zeta^{(67)}(s+i\xi)},
}
\tag{0.8}
\]
where
\[
 E_\xi(s)=\prod_{p\ne67}E_{p,\xi}(s),
\qquad
 E_{p,\xi}(s)
 ={1-(p^{i\xi}+p^{-i\xi})p^{-s}\over
   (1-p^{-(s-i\xi)})(1-p^{-(s+i\xi)})}.
\tag{0.9}
\]

The Euler correction converges normally in every closed half-plane
`Re(s)>=1/2+delta` after finitely many local factors are separated.  Indeed,
with `x=p^{-s}` and `z=p^{i xi}`,
\[
\boxed{
 E_{p,\xi}(s)-1
 ={-x^2\over(1-zx)(1-z^{-1}x)}.
}
\tag{0.10}
\]
The tail differs from one by `O_delta(p^{-1-2delta})`.

At zero frequency,
\[
\boxed{
 F_0(s)={E_0(s)\over\zeta^{(67)}(s)^2}.
}
\tag{0.11}
\]
Thus the zero-frequency divisor loss contains a double reciprocal-zeta
factor.  Nonzero frequencies contain the two shifted factors
`1/zeta(s-i xi)` and `1/zeta(s+i xi)`.

Equations (0.8)--(0.11) do not prove that every zeta pole survives every
finite local correction or every later Fourier integration.  They prove the
correct structural statement: smoothing the divisor wavelet does not remove
the reciprocal-zeta difficulty; it distributes it along two shifted spectral
lines.

## 1. Fourier--hyperbola identity

The max-height condition in (0.2) is exactly
\[
 a\le T/67^\alpha,\qquad a\ge N/T.
\tag{1.1}
\]
Insert (0.1) into each summand of (0.2).  The divisor sum is finite, so
interchange with the integral is immediate and gives (0.3).

Because `R` is the autocorrelation of the compact boundary kernel,
\[
 \widehat{\mathcal R}(\xi)
 =|\widehat K_{\rm bd}(\xi)|^2\ge0
\tag{1.2}
\]
under the matching real Fourier convention.  Positivity of this Fourier
weight is useful, but squaring the wavelet creates a double frequency
integral; it does not reduce the argument to a single positive Euler product.

The sharp interval in (1.1) is the only nonmultiplicative part of the divisor
polynomial.  It is the difference of two balanced hyperbola truncations and
must be preserved until an unsmoothing theorem is proved.

## 2. Squarefree divisor polynomial

For squarefree
\[
 N=\prod_{j=1}^r p_j,
\]
each divisor chooses independently whether `p_j` lies in `a` or `N/a`.
After multiplication by `N^{-i xi}`, the two choices contribute
`p_j^{i xi}` and `p_j^{-i xi}`.  Tensoring these local choices proves (0.5).

This also explains why orientation cancellation inside one shell is not
Möbius cancellation: every orientation carries the same shell sign
`mu(N)`.  The oscillation within `D_xi(N)` is a divisor-phase phenomenon.

## 3. Shifted-zeta factorization

At one prime write
\[
 x=p^{-s},\qquad z=p^{i\xi}.
\]
The local factor of (0.7) is
\[
 1-(z+z^{-1})x.
\tag{3.1}
\]
The product of the two reciprocal shifted-zeta local factors is
\[
 (1-zx)(1-z^{-1}x)
 =1-(z+z^{-1})x+x^2.
\tag{3.2}
\]
Dividing (3.1) by (3.2) gives (0.9), and subtraction of one gives (0.10).

For `sigma>=1/2+delta` and all sufficiently large `p`,
\[
 |1-zp^{-s}|,\ |1-z^{-1}p^{-s}|
 \ge1-p^{-\sigma},
\]
hence
\[
 |E_{p,\xi}(s)-1|
 \le {p^{-2\sigma}\over(1-p^{-\sigma})^2}
 \ll_\delta p^{-1-2\delta}.
\tag{3.3}
\]
The prime sum converges.  The finitely many omitted local factors are
elementary rational functions and must remain visible when tracking a
specific possible pole.

## 4. Consequence for a full-proof attempt

The exact remaining route is now
```text
HIGHGCDWAVE
 -> smooth the two hyperbola endpoints without losing the dyadic square sum
 -> insert the double Fourier representation
 -> control the zero-frequency 1/zeta(s)^2 burden
 -> control the shifted pair 1/[zeta(s-i xi) zeta(s+i xi)]
    uniformly in the relevant frequency range
 -> unsmooth
 -> RH.
```

The first genuinely analytic theorem cannot be merely an unsigned divisor
large sieve.  It must use the signed Möbius coefficients strongly enough to
control Dirichlet series carrying shifted reciprocal-zeta singularities.

Conversely, a theorem that proves the required all-frequency square function
by assuming zero-freeness in `Re(s)>1/2` would only repackage RH.  A successful
unconditional proof needs an additional cancellation mechanism in the
assembled `g,a,b,I,xi,eta` correlation that is not visible in one mode alone.

This packet identifies that burden exactly; it does not discharge it.

## 5. Scope firewall

- Formula (0.8) is initially proved by absolute Euler products for
  `Re(s)>1`; continuation beyond that region is only through the displayed
  factors where defined.
- The normally convergent correction has finitely many explicit local
  exceptions; no blanket noncancellation at a specified zero is asserted.
- The height-truncated divisor polynomial is not multiplicative.
- Fourier positivity does not collapse the double frequency integral.
- No zeta zero is enumerated or assumed.

**No Fourier-mode bound, HIGHGCDWAVE, OFFGCDWAVE, PRIMCAR, RH, or GRH is
proved.**

## 6. Proof ledger

| statement | grade |
|---|---|
| prefix Fourier--hyperbola formula (0.3) | **PROVED EXACT** |
| squarefree divisor product (0.5) | **PROVED EXACT** |
| shifted-zeta factorization (0.8)--(0.10) | **PROVED FOR ABSOLUTE EULER REGION; CORRECTION NORMALLY CONVERGES FOR Re(s)>1/2** |
| zero-frequency double factor (0.11) | **PROVED EXACT** |
| mode estimate / HIGHGCDWAVE / RH | **NOT PROVED** |

## 7. Bounded replay

```text
python -B research/l-families/atlas/function_field/ffps_divisor_wave_shifted_zeta_factorization.py --check
python -B -O research/l-families/atlas/function_field/ffps_divisor_wave_shifted_zeta_factorization.py --check
python -B -m unittest tests.test_ffps_divisor_wave_shifted_zeta_factorization
python -B -O -m unittest tests.test_ffps_divisor_wave_shifted_zeta_factorization
```

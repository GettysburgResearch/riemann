# A second attack: positive boundary systems for the actual Bessel sums

Status: proposed exact polynomial reduction and sufficient self-adjointness criterion; rigorous finite actual-source cases; ordinary high-precision exploration of higher degrees. No RH proof or improved zero-free region.

Scope: the actual coefficients in `PROOF.md`, not fitted moments. This continuation preserves that proof unchanged. The full spectral construction and local zero theorem are in the companion `BESSEL_SELFADJOINT_GATE.md` (spectral lane).

What was actually run: the M=3 source signs below were verified with rational outward intervals and complete theta/Bessel tail bounds. Higher-degree J-fraction signs and low-pole searches were computed with ordinary Decimal arithmetic and are explicitly not certificates.

Smallest remaining gap: prove sufficient sign control for the complete rational boundary function on complex energy disks whose radii tend to infinity, retaining every common factor and every possibly nonreal pole. Sampled signs, a real-pole list, or positivity of the original kernel is insufficient.

## 1. Exact reduction, with the radial derivative normalization

For a>0 and E=(z/2)^2, put

\[
y_E(u)=K_{i\sqrt E}(ae^u),\qquad m_a(E)=\frac{y_E'(0)}{y_E(0)}.
\]

The square-root branch is immaterial because K is even in its order. The radial derivative is

\[
y_E'(0)=aK_{i\sqrt E}'(a),
\]

where the prime on K differentiates its positive argument. The decaying solution satisfies

\[
-y_E''+a^2e^{2u}y_E=E y_E\quad(u\ge0).                 \tag{1}
\]

Set

\[
c_n=I_n(a)\Phi\left(\tfrac12\operatorname{arsinh}(n/a)\right)>0.
\]

The full transform from the preceding packet is

\[
F_{a,M}(z)=c_0K_{iz/2}(a)+\sum_{n=1}^M c_n
 [K_{n+iz/2}(a)+K_{n-iz/2}(a)].                         \tag{2}
\]

Define polynomials in nu, with a fixed,

\[
P_0=1,\ Q_0=0,\quad P_1=\nu/a,\ Q_1=-1/a,
\]

and for n>=1 use the same recurrence for P and Q:

\[
P_{n+1}=P_{n-1}+\frac{2(\nu+n)}aP_n,\qquad
Q_{n+1}=Q_{n-1}+\frac{2(\nu+n)}aQ_n.                    \tag{3}
\]

The elementary order recurrence for K gives, by induction,

\[
K_{\nu+n}(a)=P_n(\nu)K_\nu(a)+Q_n(\nu)aK_\nu'(a).     \tag{4}
\]

Adding the expression with nu replaced by -nu, then substituting nu^2=-E, yields real polynomials A_n(E), B_n(E). Consequently

\[
F_{a,M}(2\sqrt E)=A(E)y_E(0)+B(E)y_E'(0),
\]

\[
A=c_0+\sum_{n=1}^M c_nA_n,\qquad B=\sum_{n=1}^M c_nB_n. \tag{5}
\]

There is no approximation in (3)–(5), and the coefficient weights are held fixed when using the differential-operator viewpoint. In particular, one must not differentiate the a-dependence of c_n while applying a Chebyshev polynomial in minus the Bessel argument derivative.

Away from zeros of B and y_E(0), a zero of (2) is exactly

\[
m_a(E)=r(E),\qquad r(E)=-A(E)/B(E).                    \tag{6}
\]

The Lagrange identity gives

\[
\frac{\operatorname{Im}m_a(E)}{\operatorname{Im}E}
 =\frac{\int_0^\infty|y_E(u)|^2du}{|y_E(0)|^2}>0
\quad(\operatorname{Im}E\ne0).                         \tag{7}
\]

A nonreal-E zero of y_E(0) is impossible by the ordinary self-adjoint Dirichlet problem. Thus a rational anti-Herglotz r cannot meet m_a off the real axis. This is a route to the zeros of the **transform itself**, independent of whether its kernel multiplier satisfies the failed unit-circle criterion.

## 2. A sufficient positive realization

After removing the polynomial gcd of A,B, suppose

\[
r(E)=h-bE+\sum_j\frac{\gamma_j}{E-\lambda_j},
\quad b\ge0,\quad\gamma_j>0,\quad\lambda_j>0.           \tag{8}
\]

The companion spectral proof constructs a positive-Hilbert-space realization with a boundary mass b and finitely many oscillators. The exact positivity threshold is

\[
r(0)\ge m_a(0)=-aK_1(a)/K_0(a)<0.                     \tag{9}
\]

Under (8)–(9), all zeros of the reduced characteristic function have E>=0. The discarded common factor must separately have only nonnegative real zeros. The sufficient simpler condition r(0)>=0 is automatic in the finite cases below. These are sufficient conditions; they are not necessary among all rational impedances.

### A complete low-degree theorem

For every a>0, every nonzero nonnegative coefficient tuple with M<=2 makes (2) real-rooted as a function of z.

To verify this, for M=2 the exact formula is

\[
A(E)=c_0+2c_2-4c_2E/a^2,\qquad
B(E)=-2c_1/a-4c_2/a^2.
\]

If c1 or c2 is positive, (6) becomes

\[
r(E)=h-bE,\quad
h=\frac{a^2c_0+2a^2c_2}{2ac_1+4c_2}\ge0,\qquad
b=\frac{4c_2}{2ac_1+4c_2}\ge0.                         \tag{10}
\]

This is (8) with no oscillator poles, and h>m_a(0), so all energies are positive. Pure c1 gives h=b=0, the Neumann case; it must not be described as h>0. If c1=c2=0 and c0>0, the equation is the Dirichlet one. The allzero tuple is excluded. This proves the theorem, including all degenerate cases.

This is an all-zero statement for specific finite Bessel combinations, not an all-order theta theorem. The full source convergence in the preceding proof requires unbounded M/a.

## 3. A sharp one-pole test at M=3

For c3>0, define

\[
\begin{aligned}
A_0&=c_0+2c_2+8c_3/a,& A_1&=4c_2/a^2+24c_3/a^3,\\
D_0&=2c_1+4c_2/a+2c_3+16c_3/a^2,& D_1&=8c_3/a^2.
\end{aligned}
\]

The coefficient of y_E'(0) in (5) is `(-D0+D1*E)/a`. Thus

\[
r(E)=a\frac{A_0-A_1E}{D_0-D_1E},\qquad
\Delta=A_0D_1-A_1D_0.                                 \tag{11}
\]

The factor a in (11) is essential: D0,D1 are normalized as coefficients of the argument derivative K', not as coefficients of y_E'=aK'. The unique candidate pole is

\[
\lambda=D_0/D_1>0,
\]

and polynomial division gives

\[
r(E)=\frac{aA_1}{D_1}+\frac{\gamma}{E-\lambda},
\quad\gamma=-\frac{a\Delta}{D_1^2}.                    \tag{12}
\]

Hence Delta<0 makes (8) hold, while r(0)=aA0/D0>0. In that case the complete M=3 transform has only real zeros. Delta>0 gives a negative residue, so this particular positive-boundary realization fails. It does not establish a nonreal transform zero.

For the actual source coefficients, `verify_bessel_m3.py` proves the following strict signs with rational outward intervals. A common positive factor was divided out to normalize c0=1, which leaves every displayed sign unchanged.

| a | Certified sign of Delta | Approximate value, for orientation | Positive-boundary criterion |
|---:|:---:|---:|:---:|
| 1/4 | negative | -1.26514e-26 | succeeds |
| 1/2 | negative | -1.49109e-11 | succeeds |
| 1 | negative | -8.36966e-5 | succeeds |
| 2 | negative | -0.0357804 | succeeds |
| 5 | negative | -0.135445 | succeeds |
| 10 | negative | -0.0183213 | succeeds |
| 20 | positive | 0.00574015 | fails |
| 50 | positive | 0.00226231 | fails |

### Arithmetic contract of the certificate

The checker reuses the exact rational interval primitives and Machin pi reconstruction in `verify_polya_obstruction.py`. It evaluates the sample weight without an approximate inverse hyperbolic function: for x=n/a, use y=x+sqrt(1+x^2) and the expression

\[
w(x)=\sum_{k\ge1}(4\pi^2k^4y^2-6\pi k^2y)y^{1/4}e^{-\pi k^2y}.
\]

Square and fourth roots use integer-root outward bounds. The first four k terms are reconstructed, and the complete positive tail is bounded by

\[
80\,5^4\,y^{9/4}e^{-75y},
\]

with outward endpoints. This follows from pi>3, pi^2<10 and the adjacent-term ratio at most `(6/5)^4*exp(-33)<1/2` for y>=1. The Bessel I series is evaluated with an explicit geometric remainder after 180 terms. The accepted JSON contains the exact rational endpoints of every Delta. Ordinary and optimized Python executions agree byte for byte.

### Fixed M=3 cannot remain in this positive class as a grows

For every fixed n, `I_n(a)/I_0(a)→1` by the elementary Laplace concentration of the Bessel integral near angle zero, and `w(n/a)/w(0)→1` by continuity. For the normalized actual coefficients, (11) then gives

\[
a^2\Delta\longrightarrow8>0.
\]

Therefore the sufficient one-pole sign fails eventually at fixed M=3. This conclusion concerns the scalar realization, not the location of the transform zeros. For example, taking all four weights equal produces the Dirichlet-kernel universal multiplier, whose roots are on the unit circle, even though its large-a Delta is positive. This supplies a direct example showing why failure of (8) cannot be relabeled a proof of nonreal zeros.

## 4. Higher-degree tests through Jacobi fractions

Direct polynomial root finding becomes unreliable because the coefficients have large dynamic range and A,B can have extremely close zeros. `bessel_jacobi_diagnostic.py` instead uses ordinary Decimal arithmetic to compute (3)–(5) in the scaled variable x=E/a^2 and perform a real continued-fraction test.

First divide r into its polynomial part and a proper rational part P/Q. The polynomial part must have degree at most one with nonpositive slope. If `deg Q=deg P+1`, the total residue mass is `gamma=lead(P)/lead(Q)`, which must be positive. Divide

\[
\gamma Q/P=x-\alpha+R/P.
\]

The next proper fraction is `-R/P`; its positive leading mass is the next squared Jacobi off-diagonal. Repeating this is the usual finite Jacobi fraction. Positivity of all masses gives a real symmetric Jacobi matrix, and positivity of its LDL pivots makes all poles positive. The latter pivots satisfy

\[
p_0=\alpha_0,\qquad p_j=\alpha_j-\beta_{j-1}^2/p_{j-1}.
\]

The implementation is ordinary rounded arithmetic, not an exact polynomial-gcd calculation or a directed sign proof. The high-degree results were rerun at 180 and 360 decimal digits; the reported first failing stage agreed in every tested case.

| a | M | Outcome of the tested global positive-impedance criterion |
|---:|---:|---|
| 5 | 8 | passed the numerical sign extraction |
| 50 | 20 | passed the numerical sign extraction |
| 20 | 20 | negative residue mass at stage 8 |
| 10 | 30 | negative residue mass at stage 10 |
| 10 | 50 | negative residue mass at stage 19 |
| 20 | 60 | negative residue mass at stage 25 |
| 20 | 100 | negative residue mass at stage 41 |
| 50 | 150 | negative residue mass at stage 69 |
| 50 | 250 | negative residue mass at stage 114 |

Stage numbering starts at zero. These results disfavor the simplest global positive-realization proof on the tested parameter choices. They do not prove that every possible cofinal sequence fails that gate. In particular, the several probes with M/a=3 or 5 are finite probes, not a demonstrated cofinal family with M/a tending to infinity.

## 5. The surviving local route and its severe numerical conditioning

The companion local theorem only needs the following on an expanding energy disk `|E|<=R_j^2/4`:

- no harmful common factor roots in that disk;
- `Im r(E)/Im E<=0` at every nonreal regular point;
- exclusion of negative-energy intersections `r(E)=m_a(E)`.

With the already proved locally uniform convergence to Xi and `R_j→∞`, this implies RH by Rouché/Hurwitz. It is enough to prove the local zeros lie in a strip tending to zero. Global positive residues at remote energies are unnecessary for this implication.

A 360-digit exploratory real-pole search found positive residues at all sign-changing real poles it found below E=500 for the listed a values. The first pole and its residue illustrate the difficulty:

| a | M | First located pole E | Its approximate residue |
|---:|---:|---:|---:|
| 10 | 50 | 29.9642149709 | 2.2776e-1 |
| 20 | 100 | 37.0581708963 | 3.1713e-8 |
| 50 | 250 | 43.6221461897 | 1.2100e-32 |
| 100 | 500 | 46.5105174395 | 3.0121e-75 |

The search found six real poles for the first row and eight for each remaining row in its scanned interval. It sought sign-changing real roots, so it is **not** a complete pole count and cannot exclude additional complex or multiple poles. The very small residues reflect nearly common zeros of A and B. A coarse grid can entirely miss their decisive neighborhoods. A separate preliminary quadrature of m at large energy even violated its known Herglotz sign because of cancellation; those unstable values are not used as evidence and are not an acceptance test.

The concrete remaining target is therefore local rational sign control with full complex coverage and arithmetic precision scaled to the near-common-factor cancellation. The new exact recurrence and positive-system theorem make that target explicit. They do not establish it at unbounded degree or height.

## Reproduction

```sh
python -I -S -B verify_bessel_m3.py
python -O -I -S -B verify_bessel_m3.py
python bessel_jacobi_diagnostic.py 180
python bessel_jacobi_diagnostic.py 360
python bessel_low_poles_diagnostic.py
```

The M3 checker and both Decimal diagnostic scripts use only the Python standard library. The diagnostic files deliberately contain no assertion that their numerical gates are certified. The finite exact M3 sign certificate is independent of the high-degree numerical experiments.

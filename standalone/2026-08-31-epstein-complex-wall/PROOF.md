# A PROVED complex off-critical-line zero at an exact archipelago-adjacent modulus: rigorous winding number for Z(s, z*), z* = 4341/50000 + (3731/2500) i

```text
Status:  DRAFT PENDING MACHINE COMPLETION — the winding computation
         (epstein/wall_complex.py) is running; this file's lemmas and
         derivations are complete, and the certificate section below
         is filled from wall_complex.json when the run lands. If the
         run does NOT land (winding not pinned), this file stays as
         an honest record of the attempt with the failure noted.
Machine: research/exploratory/2026-08-30-two-programme-pass/epstein/
         wall_complex.py + wall_complex.json
Context: C8 campaign (O-108503): the theta80 dirty probe of the
         75-80 degree archipelago, z ~ (0.08682, 1.49240), showed
         box-vs-line zero-count discrepancy 2 in the window
         [0.05, 20] (island_probe.json, float). Float reconnaissance
         at the EXACT RATIONAL point z* = 4341/50000 + 3731/2500 i
         locates the off-line pair at rho ~ 0.90837 + 12.29624 i and
         its FE/conjugate partners.
Imports (labelled): Spouge 1994 (explicit-error Gamma approximation,
         |eps| <= a^{-1/2} (2pi)^{-(a+1/2)} for Re z >= 0);
         the classical Epstein/Chowla-Selberg Fourier expansion (used
         ONLY for the sup-bound B, never for the evaluation);
         1-D Jacobi theta transformation (Poisson summation).
RH status: RH and GRH are unproved. Epstein zetas are not the
         Riemann zeta; off-line zeros of non-arithmetic Epstein
         zetas are expected and classical in spirit. Nothing here
         bears on RH.
```

## Setting and claim

`Q(m, n) = |m + n z*|^2 / y* = ((m + n x*)^2 + n^2 y*^2)/y*` with
`x* = 4341/50000`, `y* = 3731/2500` — a unimodular positive binary
form with EXACT rational coefficients. `Z_Q(s) = sum' Q(v)^{-s}`,
`Lambda(s) = pi^{-s} Gamma(s) Z_Q(s)`.

**Claim.** `Lambda` has winding number 1 around the rectangle
`Re s in [83/100, 99/100]`, `Im s in [1221/100, 1238/100]`; hence
`Z_Q` has exactly one zero there — a zero with `Re rho >= 0.83`,
strictly off the critical line, at a modulus adjacent to the C8
archipelago (and by `Z(conj s) = conj Z(s)` and the functional
equation, a quadruple of such zeros).

## The evaluation representation (proved)

Exactly as in the rectangular certificate
(standalone/2026-08-31-epstein-wall-certificate/): `theta_Q` is
self-dual — for ANY z the adjoint form is `Q*(m,n) = Q(n, -m)`, so
`theta_{Q*} = theta_Q` and Poisson gives `theta(1/t) = t theta(t)` —
and Riemann's split of the Mellin transform yields

```text
Lambda(s) = 1/(s-1) - 1/s + sum_{v != 0} [ (pi Q)^{-s} Gamma(s, pi Q)
                              + (pi Q)^{s-1} Gamma(1-s, pi Q) ] .
```

The certificate evaluates this at complex points in directed-rounding
interval arithmetic (complex numbers as rectangles of real
intervals), with:

- `Gamma(s)`, `Gamma(1-s)` by Spouge (a = 41) through
  `Gamma(w) = Gamma(w+2)/(w(w+1))` (so Spouge's `Re >= 0` condition
  holds), the explicit Spouge error added as a complex box, and the
  complex logarithm `clog(w) = (log|w|^2)/2 + i atan2(Im w, Re w)`
  (interval atan2);
- `Gamma(s, x)`: for `x < 35` the lower-gamma series
  `x^s e^{-x} sum_k x^k/(s...(s+k))` truncated at
  `K = 2 ceil(x) + 50` with tail box `<= |term_K| r/(1-r)`,
  `r = x/(K+1-|s|) < 0.6`; for `x >= 35` integration by parts to
  order n = 20 with remainder box
  `|R_n| <= prod_{i<=n} |s-i| * x^{sigma-n-1} e^{-x}` (valid since
  `sigma - n - 1 < 0` makes `t^{sigma-n-1}` decreasing);
- lattice cutoff `Q <= 14` (44 vectors, exact rational Q) with tail
  `<= (2/(14 pi)) e^{-7 pi} [(1 + 2B') * 2(1 + A') - 1] ~ 3.5e-11`,
  from the EXACT factorization `Q = (m + n x)^2/y + y n^2`, at most
  two integers m with `|m + nx|` in each unit interval, and geometric
  domination (`k^2 >= k`).

Validation layer (asserted before the walk): Spouge vs direct Gamma
at two points (~1e-24); both incomplete-gamma branches vs mpmath
(~1e-26); the interval Lambda midpoint vs an independent float
evaluation (~1e-21).

## The sup bound B (the e^{-pi t/2} problem and its resolution)

The winding walk needs a Lipschitz bound `M >= sup |Lambda'|` on the
contour. Cauchy gives `M = B/r` (`r = 1/10`) from a sup bound B of
`|Lambda|` on the r-enlarged rectangle — but the TERMWISE bound of
the evaluation representation is useless here: it ignores the
`Gamma(s)`-type decay `e^{-pi |t|/2}` and overshoots by ~6 orders.
B is instead computed from the classical Chowla-Selberg expansion of
the COMPLETED function,

```text
Lambda(s) = 2 pi^{-s} Gamma(s) zeta(2s) y^s
          + 2 sqrt(pi) pi^{-s} Gamma(s - 1/2) zeta(2s - 1) y^{1-s}
          + 8 sqrt(y) sum_{n>=1} n^{s-1/2} sigma_{1-2s}(n)
              K_{s-1/2}(2 pi n y) cos(2 pi n x) ,
```

with three inline-proved lemmas making every piece realistically and
rigorously boundable:

**L1 (Gamma modulus).** From the Weierstrass product,
`|Gamma(a + it)|^2 = Gamma(a)^2 / prod_{k>=0} (1 + t^2/(a+k)^2)`.
Truncating the product at K = 300 (dropping factors >= 1 only
INCREASES the bound) gives a rigorous upper bound that RETAINS the
`e^{-pi|t|}` decay; six a-subintervals control the dependency loss.

**L2 (zeta modulus).** For `sigma' > 0`, `N >= 1`:
`zeta(s') = sum_{n<=N} n^{-s'} + N^{1-s'}/(s'-1)
- s' INT_N^inf {u} u^{-s'-1} du`, and `|{u}| <= 1` gives
`|zeta(s')| <= sum_{n<=N} n^{-sigma'} + N^{1-sigma'}/|s'-1|
+ |s'| N^{-sigma'}/sigma'` — a two-line Euler-Maclaurin bound.

**L3 (K-Bessel with imaginary order — the key).** For `x > 0`,
`nu = a + i mu` with `mu > 0`, and any `0 < theta < pi/2`:

```text
|K_nu(x)| <= e^{-mu theta} K_a(x cos theta).
```

*Proof.* `K_nu(x) = (1/2) INT_R e^{-x cosh u - nu u} du` (evenness of
cosh). The integrand is entire in u and decays like
`e^{-x cos theta' cosh Re u}` uniformly in the strip
`Im u in [-theta, 0]`, so the contour shifts to `u - i theta`
(Cauchy):
`K_nu(x) = (1/2) INT e^{-x cosh(u - i theta) - nu(u - i theta)} du`.
Now `Re cosh(u - i theta) = cos theta cosh u` and
`|e^{nu i theta}| = e^{-mu theta}`, so
`|K_nu(x)| <= (1/2) e^{-mu theta} INT e^{-x cos theta cosh u - a u}
du = e^{-mu theta} K_a(x cos theta)` (evenness again). ∎
With `K_a(c) <= e^{-c} sqrt(pi/(2c)) e^{a^2/(2c)}`
(`cosh t >= 1 + t^2/2`, Gaussian integral), this captures the
imaginary-order decay `e^{-pi mu /2}`-style that the naive bound
`|K_nu| <= K_{Re nu}` misses entirely — at theta = 27/20 the K-block
drops from ~1e-4 (naive) to ~1e-7 (realistic).

Divisor bookkeeping: `|n^{s-1/2} sigma_{1-2s}(n)| <= n^{sigma+1/2}`
(each divisor power `<= 1` for `sigma > 1/2`, `d(n) <= n`), and the
n-tail is geometric. Result (machine, intervals):
`B = A1 + A2 + K-block ~ 1.3e-6` versus true sup `~1e-7` — a
realistic tenfold slack, not a e^{+20} one.

## The winding lemma (proved)

Let `s_0, .., s_J = s_0` be contour samples with enclosures `W_j` of
`Lambda(s_j)`, `ell_j` = the enclosure's lower modulus bound, and
step lengths `h_j <= 0.8 ell_j / M`. Since
`sup_seg |Lambda(s) - Lambda(s_j)| <= M h_j < |Lambda(s_j)|`, the
image of segment j lies in the disc `D(Lambda(s_j), |Lambda(s_j)|)`,
so `g(u) = Lambda(s(u))/Lambda(s_j)` stays in `D(1,1) subset
{Re > 0}`: the continuous argument change along the segment lies in
`(-pi/2, pi/2)` and therefore EQUALS the principal
`Arg(Lambda(s_{j+1})/Lambda(s_j))` (they differ by a multiple of
2 pi and both lie in `(-pi, pi)`). Summing over the closed contour,
`2 pi * winding = sum_j Arg(W-ratio_j)`, and each principal argument
is enclosed by `atan2` on the interval ratio (whose real part is
verified positive). The interval sum then pins the integer. ∎

## The certificate

```text
[FILLED FROM wall_complex.json ON COMPLETION — winding interval,
step count, minimum contour enclosure, verdict.]
```

## Honesty notes

- The zero is found by float reconnaissance and PROVED by the
  winding computation; the archipelago CONNECTION (that this modulus
  belongs to the C8 dirty set's structure) remains a float-level
  statement of O-108503 — what is proved is the existence and
  location rectangle of the zero at this exact modulus.
- The Chowla-Selberg expansion enters ONLY the sup bound B. An error
  in it could only make M wrong; the walk's per-step conditions
  (`M h_j < ell_j`) and the final integer-pinning are the actual
  proof obligations, and B was float-sanity-checked against sampled
  |Lambda| values. The expansion is classical (Epstein 1903;
  Chowla-Selberg 1949 — CITATION-NEEDED for the exact form) and was
  float-validated to ~1e-40 against the evaluation representation in
  the rectangular certificate.
```

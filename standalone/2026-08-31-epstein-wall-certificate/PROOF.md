# A fully certified off-critical-line zero for the Epstein lab: Z(s, 10i) has a real zero in (81/100, 41/50)

```text
Status:  PROVED per instance (directed-rounding interval arithmetic,
         mpmath.iv at dps 120, every truncation bounded by an explicit
         inequality proved below; the one classical analytic input is
         the 1-D Jacobi theta transformation, IMPORTED and labelled).
         The PHENOMENON — real off-line zeros of rectangular Epstein
         zetas — is classical: Selberg-Chowla proved a real zero in
         (1/2, 1) for binary Epstein zetas, refined by P. T. Bateman
         and E. Grosswald, "On Epstein's zeta function", Acta Arith.
         9 (1964), 365-373 (citation resolved 2026-08-31;
         Potter-Titchmarsh 1935 for rectangular lattices); the
         contribution is the certificate: the lab's first
         PROVED-grade zero statement, at an exact rational modulus,
         self-contained and replayable.
Machine: research/exploratory/2026-08-30-two-programme-pass/epstein/
         wall_certificate.py + wall_certificate.json
Context: O-108503 (the Epstein moduli lab; all its zero statements
         were NON_DIRECTED_HIGH_PRECISION until now), C8 campaign.
RH status: RH and GRH are unproved. Epstein zeta functions are NOT
         the Riemann zeta function; an off-line zero of Z(s, 10i) is
         an expected, classical phenomenon with NO bearing on RH.
```

## Statement

Let `Q(m, n) = (m^2 + 100 n^2)/10` (the unimodular form of the
modulus `z = 10i`; equivalently, up to the factor `10^s`, the Epstein
zeta of the integral form `m^2 + 100 n^2` of discriminant `-400`),
and `Z_Q(s) = sum_{(m,n) != (0,0)} Q(m,n)^{-s}`. Then `Z_Q` has a
real zero `sigma_0` with

```text
81/100 < sigma_0 < 41/50 ,
```

strictly off the critical line `Re s = 1/2`, and by the functional
equation a partner zero in `(9/50, 19/100)`. (Coarser certified
bracket: `(3/4, 17/20)`, where the certified values have margin > 1.)

## The representation (proved)

Let `theta(t) = sum_{(m,n)} e^{-pi t Q(m,n)}`. The form factors, so
`theta(t) = theta_1(t/10) * theta_1(10 t)` with
`theta_1(u) = sum_m e^{-pi u m^2}`, and the classical 1-D Jacobi
transformation `theta_1(1/u) = sqrt(u) * theta_1(u)` (IMPORTED,
Poisson summation) gives self-duality:

```text
theta(1/t) = theta_1(10/t) theta_1(1/(10t))
           = sqrt(t/10) theta_1(t/10) * sqrt(10 t) theta_1(10 t)
           = t * theta(t).
```

Mellin transform of `theta - 1` split at `t = 1`, using the
self-duality on `(0, 1)` (as in Riemann's classical argument):

```text
Lambda(s) := pi^{-s} Gamma(s) Z_Q(s)
           = 1/(s-1) - 1/s
           + INT_1^inf (t^{s-1} + t^{-s}) (theta(t) - 1) dt ,
```

and termwise integration (all terms positive; Tonelli) with
`INT_1^inf t^{a-1} e^{-x t} dt = x^{-a} Gamma(a, x)` yields

```text
Lambda(s) = 1/(s-1) - 1/s + sum_{v != 0} [ (pi Q(v))^{-s} Gamma(s, pi Q(v))
                                 + (pi Q(v))^{s-1} Gamma(1-s, pi Q(v)) ].
```

`Gamma(a, x)` is the upper incomplete gamma. For real `s in (0, 1)`
every quantity is real, and zeros of `Lambda` in `(0,1)` are exactly
zeros of `Z_Q` (the prefactor `pi^{-s} Gamma(s)` is positive).

**Independent cross-check (float, dps 40):** the representation was
evaluated against the entirely different Chowla-Selberg / K-Bessel
formula at `sigma = 0.6` and `0.8`; agreement `9.2e-40` and
`5.7e-41`.

## The certified evaluation (all bounds proved here)

Evaluation at exact rational `sigma` in directed-rounding interval
arithmetic (mpmath.iv, dps 120). Three explicit bounds control every
truncation:

**Bound 1 (incomplete-gamma tail termination).** For `0 < a <= 1` and
`x > 0`: `Gamma(a, x) <= x^{a-1} e^{-x}` — because `t^{a-1}` is
decreasing, `INT_x^inf t^{a-1} e^{-t} dt <= x^{a-1} INT_x^inf e^{-t}
dt`. Hence each lattice term with `Q = Q(v)` satisfies

```text
(pi Q)^{-s} Gamma(s, pi Q) <= e^{-pi Q} / (pi Q),   and likewise for
the (1-s)-term:  each term <= e^{-pi Q} / (pi Q).
```

**Bound 2 (lattice tail).** With cutoff `Q(v) <= X = 25` (80 vectors):

```text
sum_{Q(v) > X} e^{-pi Q(v)}  <=  e^{-pi X/2} * sum_{v != 0} e^{-pi Q(v)/2}
  <= e^{-pi X/2} * [ (1 + 2A)(1 + 2B) - 1 ],
A = q/(1-q), q = e^{-pi/20}   (m-direction, geometric domination via
                               m^2 >= m),
B = q'/(1-q'), q' = e^{-5 pi}  (n-direction).
```

All factors are evaluated as intervals; the resulting tail bound
(`~2.6e-18`) is added to the sum as the interval `[-bound, +bound]`.

**Bound 3 (lower-gamma series truncation).** Each
`Gamma(a, x) = Gamma(a) - x^a e^{-x} sum_{k >= 0} x^k / (a(a+1)...(a+k))`;
the series has positive terms with ratio `x/(a+k+1) < 1/2` for all
`k >= K = 2 ceil(x) + 60` (asserted per call), so the truncation tail
is at most the last term, added as `[0, term_K]`.

**Gamma enclosures.** `Gamma(a)` comes from iv.gamma; at each of the
four needed points it is independently checked by the reflection
identity — the intervals `Gamma(a) Gamma(1-a)` and `pi / sin(pi a)`
must intersect (both enclose the same real number); they do.

## The certificate

```text
Lambda(3/4)    in  [ 1.1133116392737166413,  1.1133116392737166466]   POSITIVE
Lambda(17/20)  in  [-1.1581648178741787893, -1.1581648178741787841]   NEGATIVE
refinement:
Lambda(39/50)  POSITIVE      Lambda(79/100) POSITIVE
Lambda(4/5)    POSITIVE      Lambda(81/100) POSITIVE  (0.0815...)
Lambda(41/50)  NEGATIVE      (-0.1707...)
```

Interval widths `~5e-18` (dominated by the Bound-2 allowance);
certified margins of order 1 at the outer points and order 0.08 at
the tight bracket. By the intermediate value theorem `Lambda`, hence
`Z_Q`, has a real zero in `(81/100, 41/50)`. ∎

## What this upgrades, and what is deposited

Every zero statement of the Epstein lab (O-108503, C8) was
NON_DIRECTED_HIGH_PRECISION. This certificate is the lab's first
PROVED zero, and it anchors the rectangular-family bifurcation story
at an exact point: the lab's float walks along `z = iy` see the
real-zero pair; at `y = 10` its existence and location are now
theorems-per-instance. DEPOSITED next target (not claimed): the same
programme for one COMPLEX archipelago point (theta80 probe,
`z ~ 0.0868 + 1.4924i`, disc = 2): needs complex-rectangle interval
arithmetic over iv, a contour `|Lambda|`-lower bound, a Cauchy
derivative bound from an enlarged rectangle, and rigorous winding
number tracking — each ingredient elementary over the same
representation (which holds for all z via `Q* = Q o swap`), but an
order of magnitude more machinery than the real case.

## Replay

`python3 epstein/wall_certificate.py` from the pass root (mpmath
1.3.0); asserts the float cross-check, the reflection checks, the
series-ratio conditions, and the final signs; writes
wall_certificate.json. Runtime ~5 s.
```

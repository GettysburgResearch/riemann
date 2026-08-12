# Integration correction — no unaugmented all-scale completed-Fisher contraction

## Freeze

```text
parent PR:      #400
child PR:       #429
parent head:    7dc9fec9eb5fab4ee9340ddbc5a52e36a6ab617e
prior child:    dcf9c0dfbf4e5d41e91a4aafc35d6d37b426c129
session date:   2026-08-13
RH:             unproved
```

Read the current child head from GitHub after publication.

## Normative correction

`L-91309` correctly constructs one completed Riemann-density source space and
one differentiable normalized tilt curve

```text
q_a(y)=xi(1/2+a)^(-1/2) exp(-a y/2).
```

It leaves open a single fixed contraction taking the associated source
isometries to the Suzuki all-pass multipliers for every safe scale.

`R-91330` proves that this unaugmented all-scale contraction cannot exist.

If one fixed contraction `C` satisfied

```text
C V_a = M_(Theta_a)
```

for all safe `a`, differentiation would force

```text
||partial_a Theta_a||_infinity
 <= (1/2) sqrt(Var_a(Y)).
```

The two sides have incompatible asymptotics:

```text
||partial_a Theta_a||_infinity >= pi/2  for every a>1/2;
Var_a(Y) = 1/(2(1/2+a)) + O(a^-2) -> 0.
```

The phase lower bound is exact. Along a Kronecker sequence, the imaginary
Euler logarithmic derivative tends to zero, the rational contributions vanish,
and the gamma digamma contribution tends to `pi/4`; the phase derivative is
twice that imaginary part.

The source asymptotic follows directly from the trigamma expansion and the
absolutely convergent Euler derivative on `Re(s)>1`.

## What survives

```text
one fixed completed Riemann-density Hilbert space       PROVED
normalized exponential-tilt state curve q_a             PROVED
completed Fisher tangent and covariance                 PROVED
Suzuki phase as conjugate amplitude / amplitude          PROVED
one fixed contraction for all safe scales, source=q_a   IMPOSSIBLE
```

This no-go does not invalidate the fixed Jordan Poisson product system in
`L-91308`, the exact finite-delay Hardy geometry, or the bounded structured
Suzuki tangent in `L-91328`.

## Correct repair classes

Any future completed scattering construction must use at least one of:

```text
an augmented source carrying an additional all-pass/gauge tangent;
a construction local to one fixed scale;
an a-dependent observation with all connection terms retained;
an unbounded structured observation such as the reciprocal-xi leg.
```

In particular, the normalized amplitude Fisher norm alone cannot be declared
the source-normal curvature of the full completed Suzuki phase over all safe
scales. The gamma all-pass channel retains a nonvanishing high-frequency phase
speed even while the normalized tilt state becomes asymptotically stationary.

## Correct live endpoint

```text
delayed weighted form core                          PROVED
full physical Hardy delay colligation               PROVED
normalized Fisher-Hankel Bochner core               REFUTED
renormalized bounded random feature                 PROVED
safe Suzuki tangent bounded on all K_Theta          PROVED
continuous delay reduced to finite pole jets        PROVED
one critical xi/xi'/xi'' confluent block isolated   PROVED
unaugmented all-scale fixed Fisher contraction      REFUTED
augmented completed source-minus-output block       OPEN / RH-BEARING
mixed orientation and bridge arithmetic rows        OPEN
Riemann Hypothesis                                  UNPROVED
```

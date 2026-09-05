## Continuation 108420 — symmetric positivity and Speiser screening

This checkpoint adds `PFR-T10`, `PFR-T11`, and `PFR-R4`.

### PFR-T10

The symmetric response

```text
S_(a,m)(t)=sum_rho exp((rho-1/2)t)/(a^2-(rho-1/2)^2)^m
```

has a safe two-point Hermite source formula, obeys

```text
(a^2-D^2)^m S_(a,m) = critical explicit-formula source,
```

recovers `Lambda(n)/sqrt(n)` as universal derivative jumps at prime-power
knots, and has growth/energy abscissa `Theta-1/2`.

Under RH it is the Fourier transform of the positive measure

```text
sum_gamma (a^2+gamma^2)^(-m) delta_gamma,
```

so it is positive definite; its safe Laplace transform is positive real and
has a positive Pick kernel. Conversely any off-line zero creates a nonremovable
right-half-plane pole and a finite positivity witness. Thus these are exact
RH equivalences, not a proof from the prime side.

### PFR-T11 / PFR-R4

The positive flower-curvature field is now inserted into an exact
argument-principle Gauss law for

```text
G(s)=(s-1)^2 zeta'(s).
```

Every left-of-line `zeta'` zero is paid by critical-line positive phase
variation or by explicit left/horizontal boundary flux. In finite models the
positive variation is

```text
pi*(number of left critical points) - Poisson screening overlap.
```

A mirrored left/right critical-point pair screens perfectly, proving that
curvature cannot count Speiser defects without a right-side/background control
theorem.

### Replay

```text
PASS_PFR_SYMMETRIC_POSITIVITY_AND_SPEISER_SCREENING
checks=10
proof_object=eec2e381e3efc29ebe85bfe406027a6e54117db2cc833e2130a75458ab65498e
RH_UNPROVEN
```

The actual-Xi numerical comparison is non-directed high precision. External
novelty remains unreviewed.

# BFC26 — fixed-point continuation, not an RH proof

**Proposed component proofs; independent review required.**

The gamma-to-Xi route here varies the branching multiplier from
Beta(5/2,5/2) to U^-2, U uniform on [1,2], and solves the unique normalized
fixed law at EACH parameter. It is not the old sequence of finite branching
iterates and it is not a convex mixture of their transforms.

Read `PROOF.md`, then `REVIEW.md` and `VALIDATION.md`.

## Proposed all-parameter results

- A uniform W2 contraction sqrt(7/12), with the exact gamma and Brownian endpoints.
- Third-order ordering and exact distance
  `d3(nu_a,nu_b)=56(b-a)/[(50-a)(50-b)]`.
- A positive full-source response measure. Its linear response inverse has
  exact norm `80/(50-theta)<=80/49`; its complete geometric tail is explicit.
- An exact complex Mellin response with all inverse-moment costs retained.
- A nonnegative off-line-zero functional with uniform complete height tail
  at most `(5/16) exp(-pi*T/2)` over the WHOLE parameter interval.
- The local birth/death discriminator at a real double zero is exactly
  `16*chi_theta*A_theta/Q_theta`. Its sign on actual source collisions is OPEN.

The zero functional is zero at the gamma endpoint. It is zero at the other
endpoint exactly when RH holds. No monotonicity, favorable net production,
absence of higher collisions, or global confinement has been established.
Positive source measures and a stable response solve do not supply those facts.

## Bounded reproducibility

```
python -I -S -B check.py --check result.json
python -I -S -B -O check.py --check result.json
python -I -S -B test_check.py
python -I -S -B -O test_check.py
```

The standard-library checker reconstructs seven rational parameter panels
through moment order 14; independent response moments through order 11;
gamma and Brownian endpoint series; exact metric/remainder identities;
48 explicitly SYNTHETIC fold panels; and elementary proof constants.
These checks do not machine-prove an analytic infinite theorem. There is no
new actual Xi value, native zero or collision computation.

The test runner executes one pristine CLI acceptance and twelve actual altered
copies per mode. A changed producer and a changed receipt can be resealed and
still fail mathematical reconstruction. This is not a claim that arbitrary
coordinated replacement of an entire checker and all trusted inputs is detected.
No platform-dependent symlink test is included in the executed test count.

Publication should be an add-only standalone path on a separate branch from
frozen #874. Do not modify main, parent manuscripts, canonical status or settings.

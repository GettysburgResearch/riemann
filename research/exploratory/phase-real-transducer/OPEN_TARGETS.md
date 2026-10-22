# Ranked continuation queue

## 1. Prime-side proof of symmetric positivity

`PFR-T10` constructs the source-defined symmetric response

```text
S_(a,m)(t)=sum_rho exp((rho-1/2)t)/(a^2-(rho-1/2)^2)^m.
```

It simultaneously has:

```text
local prime knots      -> Lambda(n)/sqrt(n) derivative jumps;
global growth          -> Theta-1/2;
RH-side structure      -> positive-definite time kernel;
safe transform         -> positive-real / Pick kernel.
```

The highest-priority theorem is to prove positive definiteness, positive-realness,
or every-positive-shift Hardy `H2` membership directly from the safe Hermite /
prime source. Any one closes RH, so partial work must isolate a strictly weaker
quantitative milestone rather than rename the full burden.

## 2. Harmonic-screening and boundary-flux estimate

`PFR-T11` gives the exact finite-window ledger

```text
positive zeta-prime phase variation
  = 2*pi*(left zeta-prime zeros)
    + pole correction
    + left/horizontal boundary flux
    + negative phase variation.
```

The finite model shows that right critical points screen left critical points by
an exact Poisson-overlap term.  Seek a zeta-specific estimate preventing
complete screening, or a boundary normalization in which the residual flux is
source-controlled.  `PFR-R4` rules out any argument that ignores the right-side
field.

## 3. In-band lower frame bound for soft Gamma localization

`PFR-T9` gives a zero-independent complex-Gamma filter with explicit exterior
leakage on every finite horizon.  The missing theorem is a source-defined lower
bound for the selected in-band signal which survives cancellation and the
transition band.  Frequency separation may be used only if its exact source
and scope are stated; no unproved global zero-spacing input may be hidden.

## 4. Combined petal--Speiser count

Use equation (2.28) of `CONTINUATION_108420.md`:

```text
critical-line petals + 2*(left zeta-prime zeros)
  >= phase budget - screening/boundary/corner remainder.
```

Add exact Riemann--von Mangoldt endpoint accounting, multiplicities, and a
quantitative estimate of the remainder.  Main-term saturation is insufficient:
a sparse off-line set must also be excluded.

## 5. Certified computational pass

With interval or ball arithmetic, certify on a modest predeclared window:

- symmetric-resolvent safe-Hermite values and finite Pick matrices;
- prime-knot jumps for both one-sided and symmetric splines;
- critical-line petal areas and angular spans;
- `Re zeta''/zeta'`, `zeta'` critical points, and rectangle boundary flux;
- Poisson screening between left/right critical-point candidates;
- complex-Gamma soft-band leakage.

The result is structural regression, not a global proof or counterexample.

## 6. Literature and equivalence audit

Compare `PFR-T10` precisely with:

- Weil positivity and Bombieri's formulations;
- Suzuki's screw function and screw-line constructions;
- issue #39's direct `xi'/xi` passivity/Pick kernel;
- PR #729's Herglotz/backward-Poisson field;
- PR #762's beta zero-abscissa observable.

Determine which transforms are unitary, resolvent-related, or genuinely
different, and withdraw any novelty language unsupported by that audit.

## Stop conditions

Pause or redirect the lane if review proves that:

- the symmetric resolvent is wholly subsumed by a standard published criterion
  and its prime-knot/Pick combination adds no usable theorem target;
- the Gauss ledger supplies no controllable screening or boundary term beyond
  the ordinary argument principle;
- the soft localizer admits no source-defined in-band lower frame bound;
- every finite invariant survives a known RH-false zeta analogue;
- or a source formula, Hermite normalization, pole residue, jump sign, or
  endpoint orientation fails hostile review.

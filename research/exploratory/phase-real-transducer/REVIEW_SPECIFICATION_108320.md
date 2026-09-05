# Hostile review specification — PFR-T7--T9

Review exact parent:

```text
research/gpt56-pro/108200-phase-flow-real-transducer
4a78ba3ca89dcb63fcccf50d6738f01e28c80c64
```

or the exact descendant commit that adds this packet.

## Load-bearing checks

### PFR-T7

1. Differentiate one prime-power hinge through order `m-1` and verify the
   right-minus-left jump `(-1)^(m+1)Lambda(n)/sqrt(n)`.
2. Verify `(a-D)^m R_(a,m)=mathscr Z` with the sign of the prime delta.
3. Check compact-uniform differentiation and `C^(m-2)` regularity.
4. Ensure the local jump theorem does not claim boundedness or RH.

### PFR-T8

1. Check `Gamma'=i zeta'`, `Gamma''=-zeta''` and every sign in
   `-theta' C_H=Re(conj(zeta')zeta'')`.
2. Verify the positive-turn substitution into the `PFR-T6` count inequality.
3. Treat the curvature identity as known literature, not external novelty.
4. In the finite Poisson field, check the left/right signs and the whole-line
   integral `pi(N_L-N_R)`.
5. Do not promote the finite decomposition to actual zeta' without pole,
   background, regularization, and boundary terms.

### PFR-R3 / PFR-T9

1. Check the Laplace-pole proof for filtered abscissa invariance and group
   repeated exponents before taking residues.
2. Verify the complex source factor `e^(q t)n^(-q-1/2)` and all completion
   denominators.
3. Check the target/guard extrema over `|Re lambda|<1/2`.
4. Verify the finite-horizon leakage uses only the unconditional strip bound
   `Re lambda<=1/2`.
5. Do not infer a local zero without an in-band lower frame bound.

## Replay

```bash
python3 research/exploratory/phase-real-transducer/code/verify_phase_speiser_localization.py
python3 -m unittest discover \
  -s research/exploratory/phase-real-transducer/tests \
  -p 'test_*.py' -v
```

Expected continuation marker:

```text
PASS_PFR_PRIME_KNOT_CURVATURE_AND_SOFT_LOCALIZATION
RH_UNPROVEN
```

The actual-zeta checks are non-directed high precision.  They are regressions,
not certificates.

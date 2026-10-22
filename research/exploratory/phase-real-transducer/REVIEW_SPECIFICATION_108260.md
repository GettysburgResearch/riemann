# Review specification — PFR continuation 108260

## Frozen parent

```text
branch: research/gpt56-pro/108200-phase-flow-real-transducer
parent: 433f76e2541406e0ca69ac0edb917cc3984a649a
```

## Review order

### 1. PFR-T5 actual-Xi Gamma resolvent

Check independently:

1. absolute convergence of
   \(\sum_\rho e^{(\rho-1/2)t}(a+1/2-\rho)^{-m}\) for `a>1/2`, `m>=2`;
2. every sign, exponent and endpoint in the prime/archimedean formula (5.4);
3. extension of PFR-T4 from compact smooth tests to the future-Gamma kernel;
4. the safe Taylor-remainder identity for `xi'/xi`, including cancellation of
   Hadamard regularization terms;
5. normal convergence and nonzero residues of the meromorphic Laplace
   resolvent;
6. the weighted-`L2` and pointwise exponential-abscissa arguments;
7. the RH equivalences and their exact quantifiers;
8. overlap and novelty relative to classical explicit-formula smoothing,
   Landau-type oscillation arguments, PR #762 and Issue #39.

A sign or normalization failure in (5.4) invalidates the source-defined part,
but not automatically the abstract zero-side abscissa lemma.

### 2. PFR-T6 flower curvature ledger

Check independently:

1. the `2*pi` self-intersection threshold, including the equality case;
2. tangent-angle branch choices at both simple endpoint zeros;
3. the origin-corner convention and total turn `-2*pi`;
4. the total absolute-curvature inequality;
5. conversion from angular derivatives to the real `Z,vartheta` coordinate;
6. the exact normalized negative-curvature identity (3.8)--(3.12);
7. every simplicity, multiplicity and `vartheta'>0` hypothesis.

### 3. PFR-R2 localization firewall

Confirm that the claimed no-go applies only to zero-independent filters with a
holomorphic exponential-mode multiplier on a connected domain.  It does not
exclude non-holomorphic projections, leakage-controlled windows, or
source-specific nonlinear constructions.

### 4. Computation

Run:

```bash
python3 code/verify_phase_real.py
python3 code/verify_phase_resolvent.py
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

The actual-Xi comparisons are `FLOATING_RECONNAISSANCE`; they are not interval
certificates and do not prove the analytic statements.

## Fail-closed boundary

```text
RH / GRH                                           UNPROVEN
new zero proportion                                NONE
height-localized resolvent                         OPEN
prime-side boundedness of PFR-T5                   OPEN / RH-EQUIVALENT
external novelty                                   UNREVIEWED
```

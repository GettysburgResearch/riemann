# Integration handoff — ladder, compensated Green, and plastic alignment

Date: 2026-08-12  
Parent PR: `#404`  
Parent head: `ab71aa1fe0b1fd192011bbf40f032d2f42889ea0`  
Branch: `research/gpt56-pro/91411-ladder-compensated-green`  
RH status: **unproved**

## Review order

1. `claims/lemmas/L-91411-nakamura-completion-is-a-gamma-ladder-minus-one-pole-hardy-channel.md`
2. `claims/refutations/R-91404-one-pole-tangent-does-not-make-the-three-scale-delayed-recurrence-finite-index.md`
3. corrected `claims/lemmas/L-91412-compensated-wick-green-factorization-closes-the-continuous-source-packet.md`
4. corrected `claims/lemmas/L-91413-plastic-aligned-scale-turns-the-continuous-cauchy-recurrence-into-a-positive-levy-increment.md`
5. `claims/refutations/R-91405-continuous-aligned-levy-measure-cannot-dominate-the-prime-atomic-sampling-measure.md`
6. corrected `claims/theorems/T-91402-compensated-production-port-domination-is-the-final-completed-green-gate.md`
7. `claims/observations/O-91401-current-boundary-after-compensated-green-and-atomic-isolation.md`
8. `experiments/X-91411-ladder-compensated-green/`
9. session report
10. parent `L-91409/L-91410/R-91403/T-91008`

## Exact advances

```text
Nakamura continuous source -> positive gamma ladder minus one pole;
one exponential rung -> rank-one Hardy evaluation port;
short singular source -> exact direct-translation compensated Green identity;
long signed source -> positive endpoints minus adverse production;
full carrier/delay/orientation/bridge continuous source -> explicit Gram ledger;
Cauchy residual switch -> exact monotonicity proof;
plastic-aligned safe scale -> positive nonprime Levy increment;
all prime residual scalar coefficients -> one sign;
full completed source -> connection + production - adverse ledger.
```

## Corrections made before handoff

```text
prime mode split at the short-jump endpoint
    WITHDRAWN: individual modes do not share one no-jump trace;
    REPAIRED by the direct physical translation source.

one-pole tangent -> finite-index recurrence
    REFUTED by three-scale signs, radial derivatives and delay leakage.

continuous aligned measure -> prime atomic full-Gram domination
    REFUTED by finite Fejer atom-isolation packets.
```

## Remaining theorem

`CPPD_a`:

\[
 \mathcal C_a^\lambda+\mathcal P_a
 \succeq\mathcal N_a
\]

on every finite carrier/delay/orientation/bridge packet, with coefficient one.

A proof must couple the connection, prime endpoints, short compensation, long
production and all leakage ports.  Marginal measure domination is impossible.

## Replay

```bash
cd experiments/X-91411-ladder-compensated-green
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Retained verdict:

```text
PASS_LADDER_COMPENSATED_GREEN_ALIGNMENT
```

The replay does not prove CPPD, the delayed screw sign, or RH.

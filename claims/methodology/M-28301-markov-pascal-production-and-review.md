# M-28301 — Markov–Pascal production and review protocol

Claim ID: `M-28301`  
Title: Fail-closed protocol for the State-Augmented Pascal Cascade  
Status: **PROPOSED METHODOLOGY**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Issue: #283

## 1. Review order

1. `R-28301` and `X-28301`: replay both fixed-Abel counterexamples.
2. `L-28302`: reconstruct the sibling-switch and commutator identities.
3. PR #280 `L-27701/L-27702`: verify the central residual and continuum factor
   `1-log 2`.
4. PR #272 `L-27204/L-27205`: verify the complete cycle basis and debt dual.
5. `L-28301`: reconstruct the explicit Gamma–carry coupling and support
   inequality.
6. `L-28303`: verify the matrix-valued Markov lift and common-fiber congruence.
7. `T-28301`: audit the proposed finite state/cycle recurrence.
8. Reconstruct one complete finite certificate before considering any
   asymptotic statement.
9. Replay either the prime-ramp/square-screw consumer or the reflected
   rightmost-zero consumer independently.

## 2. Required production object

For each endpoint and stage, a certificate must contain:

```text
source endpoint and exact target values;
complete Markov-state partition;
outward rational state masses;
complete balanced split-edge manifest;
exact node divergence;
exact carry-column replay;
complete Pascal cycle coordinates;
pre-repair and post-repair edge coefficients;
capacity-weighted negative debt;
sibling-switch source/destination ledger;
all endpoint and cutoff commutators;
strict lower-scale destinations;
full two-frequency Gram when using the reflected consumer;
source and dependency digests.
```

## 3. Independent assurances

Use two separated consumers.

### Finite combinatorial consumer

Standard-library integer/Fraction arithmetic verifies:

- Möbius and producer mutations;
- split carry columns;
- divergence and cycle identities;
- sibling-switch effects;
- exact debt and objective ledgers.

### Directed analytic consumer

Outward interval arithmetic verifies:

- Markov state-cell masses and support;
- physical cutoff integrals;
- two-frequency Gram matrices;
- strict reserve and lower-scale charge.

The finite consumer may not trust floating state partitioning.  The analytic
consumer may not reconstruct missing arithmetic rows by inference.

## 4. Mandatory mutations

Every proof object must reject or explicitly retain:

```text
third Abel:  Q=520, n=15 -> -91/256;
fourth Abel: Q=10000, n=7 -> -10512404675923/16384;
second Abel: PR #279 inherited -13/16 witness;
ternary producer: PR #272 X=10^7,n=63 mutation;
central endpoint: 2kq-1, not 2kq;
wrong sibling-switch sign;
state-independent residual substitution;
one-frequency physical block;
same-sign Möbius hypercube;
dyadic and 2/3 fixed-ratio shell;
prime-density-drift mutation;
current-scale residual route.
```

## 5. Status discipline

Use the following classifications.

```text
EXACT
    proved finite algebra or probability identity;

DIRECTED FINITE CERTIFICATE
    outward finite analytic/PSD result;

PROPOSED
    all-scale theorem with a complete statement but no proof;

REFUTED
    exact hypothesis-matching counterexample;

UNPROVEN
    missing proof or producer without a counterexample.
```

Do not describe SAPC as complete because the exact continuum Markov kernel and
finite cycle basis exist.  The load-bearing step is their quantitative finite
realization with a strict contraction.

## 6. Minimal first production target

The first source-bound block should use:

```text
endpoint X in {64,128};
all O(log X) central stages;
full rational carry target surrogate;
complete sibling-switch manifest;
complete balanced fundamental-cycle basis;
exact cycle-debt minimizer and dual witness;
finite Markov state partition with interval masses;
all mutations above.
```

The goal is to identify the actual recurrence constant and collar, not to infer
an asymptotic theorem from a positive finite instance.

## 7. Promotion boundary

A full proof candidate may be promoted only after it supplies:

1. one uniform `rho_*<1`;
2. a complete proof of the additive polylogarithmic source bound;
3. a cofinal exact/directed certificate schema;
4. the full prime-ramp or reflected energy consumer;
5. explicit survival of every mandatory mutation.

Until then:

```text
SAPC  OPEN
RH    UNPROVED
```
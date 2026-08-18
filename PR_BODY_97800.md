## Purpose

Continue the independent two-row lane from frozen PR #579 and attack exactly the regime where the number of active primes grows with the endpoint.

```text
base PR:      #579
base SHA:     9f56688236d33c515a92032c640888488c06ed6e
compared:     #580 SACF @ 812e7fcbaff2dd1c2c53c885def7b6c0d0e68a05
binding:      #589 LAPBR67 refutation @ ff5156cf6aa469bb7a2155ff4aa7c094bd75b9b6
head branch:  research/gpt56-pro/97800-growing-prime-bilinear-tail
```

**RH remains unproved.**

## New unconditional theorem

For the literal row-two and sharp-row-three dictionaries, define the finite Euler projection through primes `3<p<=z`. The packet proves explicit uniform prefix and all-real lower bounds and constructs a maximal certified cutoff

```text
z_*(X) = (1+o(1)) log X
```

for which both truncated physical rows are strictly positive. This upgrades "every fixed finite sieve is eventually positive" to a genuinely growing-prime theorem.

## Exact remaining correlation

Unique least-prime ownership gives, componentwise,

```text
C_full,j(X) = C_truncated,j(X) - G_j(X;z_*),
```

where `G_j` is one explicit prime/cofactor bilinear form retaining every literal activation. The sharp common gate is

```text
Gamma_23(X) = max(G_2/C_2, G_3^sharp/C_3^sharp).
```

Thus eventual two-row positivity is equivalent to

```text
FPCB23: Gamma_23(X) <= 1 eventually.
```

The normalization is exact: equality is precisely a zero of one full row.

## Extremal comparison

- `LAPBR67` is excluded: PR #589 refutes its fixed adaptive depth.
- Squared dyadic blocks have the same coprime Type-II sign geometry as `SACF`, but SACF energy is phase-blind and cannot imply the one-sided sign alone.
- The sharp Farkas separators are the individual row rays; a `5:3` scalar or completed-parity Lorenz hinge does not automatically lift to both rows.

## Replay

```bash
cd experiments/X-97800-growing-prime-bilinear-tail
python3 verify.py --output /tmp/x97800.json
cmp /tmp/x97800.json results/verification.json
```

Expected:

```text
PASS_T97800_GROWING_PRIME_BILINEAR_TAIL_REDUCTION
22e8ded8c3806b9787f07679c5729f0026c25a62a38094166c88f3a359f54280
```

## Scientific boundary

```text
finite theorem through 10^8                  inherited proved
uniform truncated cutoff z_*(X)~log X        proved
exact all-depth future-prime bilinear tail   proved
LAPBR67                                      refuted / not used
SACF/Lorenz projections                      identified exactly
FPCB23                                       open / RH-bearing
Riemann Hypothesis                           unproved
```

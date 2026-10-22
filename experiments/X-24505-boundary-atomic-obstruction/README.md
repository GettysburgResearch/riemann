# X-24505 — Stopped-power boundary atomic-norm obstruction

Status: `DIRECTED_DECIMAL FINITE MUTATION`  
Scope: finite normalization check for `R-24505`  
RH: not proved or disproved

Run:

```bash
python3 experiments/X-24505-boundary-atomic-obstruction/verify.py \
  > experiments/X-24505-boundary-atomic-obstruction/results/verification.json
```

The checker uses only the Python standard library.

For every prime

```text
X/3 < p <= X/2
```

it outward-rounds the exact lower estimate

```text
B_X(p)
 >= log(X)[(2p-1)^(-1/2)-(3p)^(-1/2)]
    -(2p-1)^(-1/2)log(X/(2p-1)).
```

At the strict next half endpoint, `p` is the only available source node divisible
by itself, so `sqrt(p)B_X(p)` is a mandatory contribution to the divisor-source
atomic norm.

Retained controls:

```text
X=10,000       primes=199       lower sum >210.9547
X=100,000      primes=1,564     lower sum >2,125.7311
X=1,000,000    primes=12,873    lower sum >21,349.3256
```

Verdict:

```text
PASS_DIRECTED_MACROSCOPIC_BOUNDARY_ATOMIC_LOWER_BOUND
```

Payload digest:

```text
c15c4c4306830844cd614348b23bb0bc4d8ebeedd5f3224b888ef72810458f1c
```

The asymptotic `Omega(X)` conclusion in `R-24505` additionally uses the prime
number theorem. The checker does not rule out a relative analytic-boundary
cancellation, a source-capacity construction, another Cycle-Debt producer, or
RH.

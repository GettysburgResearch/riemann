# X-91138 — Global positivity of the canonical P61 finite-Euler row

This is the companion proof object for L-91364.

Run:

```bash
cd experiments/X-91138-p61-global-canonical-row
python3 replay.py
```

Expected verdict:

```text
PASS_P61_CANONICAL_FINITE_EULER_ROW_GLOBAL_POSITIVITY
```

The directed interval engine is `verify.py`. The deterministic retained-result wrapper is `replay.py`.

The checker uses only the Python standard library and certifies 262,144 divisor states, 524,207 global asymptotic endpoint gates, 209,475 stationary-minimum exclusions, 8,600,064 finite component-row cells, 509 finite Green/Kantorovich tail rows, and every activation-strip and divisor-mass corridor.

Selected strict lower bounds are:

```text
compact limit profile                    2.5668809469...
global limit minus (3/4)sqrt(u)         0.1547430065...
finite scaled row                        2.9407744304...
finite Green tail                        9.2012e-5
```

The proof object certifies the finite gates used by L-91364. The analytic Riemann-sum and Green reductions are in the theorem file. It does not audit the imported literal-entropy benchmark, common endpoint-port normalization, CFFP, or RH.

Frozen engine blob:

```text
8ac1c8a75179dc68ee779c58fa77b929026f8af7
```

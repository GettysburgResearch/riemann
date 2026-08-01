# X-15604 — Exact Schatten automatic-capture regression

This standard-library-only experiment checks `L-15615` with exact rational
arithmetic.

The positive deficit operator has spectrum

```text
11/10, 11/10, and one hundred copies of 1/100.
```

Take

```text
G       = 2
alpha   = 9/10
Gamma   = 3/2
t       = 1
packet dimension = 2.
```

The associated exact operator `A=G I-D` has two low eigenvalues `9/10` and one
hundred complement eigenvalues `199/100`.

The ordinary trace gate fails:

```text
Tr(D) - 2(G-alpha) = 1 > G-Gamma = 1/2.
```

The `r=2` gate passes:

```text
Tr(D^2) - 2(G-alpha)^2 = 1/100
                              < (G-Gamma)^2 = 1/4.
```

Therefore `L-15615` certifies

```text
||(I-P)D(I-P)|| <= 1/10
A|_(L^perp) >= 19/10 > Gamma.
```

The example proves that shallow deficit mass can make the `r=1` scalar trace
condition fail even though an exact higher-Schatten certificate closes the
complete complement.

Run:

```bash
python experiments/X-15604-schatten-deficit-capture/verify.py
```

Expected verdict:

```text
PASS_EXACT_R2_CAPTURE_WHILE_R1_TRACE_FAILS
```

Proof-object SHA-256:

```text
4cd12e82e83604bce7a5c6dfd56b164e2b821e34a1651ce7ed1d0200dd569e9e
```

This is a synthetic exact regression. It does not evaluate Suzuki's symbol,
build a production zeta source packet, prove a cofinal Schatten bound, or prove
RH.

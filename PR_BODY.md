## Purpose

Reconcile the unpublished stronger checkerboard/Cauchy--Binet closure described
in the assistant response with the actual, weaker PR #567 artifact.

This packet recovers the stronger proposal **as a withdrawn conditional schema**,
identifies the exact failed arrow, and confirms that PR #567 is the intentional
scientific retraction.

```text
base PR:      #567
base SHA:     50e596560b4f6f423e87fd6718d74913d863df99
binding audit:#561 @ db9bdc63c855c6ddf664b763d748f8155a6a2c67
comparison:   #564 @ c74fe9bd7fd284718f4dcef8328af07e553d9d90
```

## Exact reconciliation

The unpublished response proposed

```text
literal-history owner incidence
 -> terminal target/scalar checkerboard
 -> Cauchy--Binet
 -> global Hall
 -> single-scalar positivity
 -> Mellin--Landau
 -> RH.
```

The owner-incidence and conditional Cauchy--Binet interfaces are valid after two
repairs:

1. with `H` terminal-by-source and `K` terminal-by-feature, the correct product
   is `H^T K`, not `H K`;
2. the source columns must be ordered by terminal owner before claiming
   nonnegative incidence minors.

The conclusion-producing arrow did not survive:

```text
terminal/local checkerboard + Cauchy--Binet
  -/-> global target-prefix/Lorenz dominance.
```

Cauchy--Binet transports determinant signs. It does not prove total target
capacity or the global Lorenz inequality required by Hall.

The exact odd-history witness from PR #561 is binding:

```text
X=67*71*13
history=(67)
terminal=(p,y)=(71,13)
canonical E_T-O_T > 17
```

After the parity swap, the leaf has even capacity `O_T` and odd demand `E_T`;
leafwise exact-target Hall is impossible. Compensation by other histories is
possible in principle, but proving it uniformly is exactly `GPHT*`/`GABPT`/
`TFPE`/`ACBI`, which remains open and RH-bearing.

## Scientific boundary

```text
parity-covariant atomwise ledger            PROVED EXACT
corrected owner-incidence matrix            PROVED EXACT
conditional Cauchy--Binet propagation       PROVED EXACT
leafwise parity-blind terminal Hall          REFUTED
global Hall from checkerboard alone          FALSE AS AN IMPLICATION
GPHT* / GABPT / TFPE / ACBI                  OPEN / RH-BEARING
PR #567                                      INTENTIONAL RETRACTION
Riemann Hypothesis                           UNPROVEN
```

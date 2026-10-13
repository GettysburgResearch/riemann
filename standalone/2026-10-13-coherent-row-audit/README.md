# Coherent-row audit: where the large degree cancellation actually lives

**PROPOSED component proofs and exact finite computation. No new full-moment
exponent, zero-free boundary, or RH theorem. No independent mathematical review.**

This continuation of #941 reads the newer #943 degree census and separates the
actual rows responsible for its large cross-degree cancellation. It does not
correct #943's arithmetic: the complete totals reproduce exactly. It corrects a
potential interpretation of those totals as broadly distributed cancellation in
the difficult physical bulk.

## Main finite finding

At D=8192, H=ceil(D^(21/20))=12855, include ALL 1,145 good squarefree ideal
columns in D/2<Nn<=D and ALL 46,608 nonzero Eisenstein element rows Nu<=H.
The following is exact integer arithmetic:

| Row set | Native fourth moment | Degree-diagonal energy | Cross-degree contribution |
|---|---:|---:|---:|
| All 46,608 | 114923460372 | 1652703692676 | -1537780232304 |
| Exactly 1, -27, 64 | 583443 | 1544518075635 | -1544517492192 |
| Other 46,605 | 114922876929 | 108185617041 | +6737259888 |

Thus three actual sixth-power rows account for MORE than the entire negative
cross-degree contribution. The complement has a positive cross-degree sum.
This is a finite observation, not an asymptotic sign or dominance assertion.

The column degree counts are (459,562,124); their alternating sum is -21.
Every allowed character equals one on these three rows, without erasing any
nonunit zero. The k=2 product-degree vector is
(210681,515916,429676,139376,15376), and their Gram contribution is exactly
three times its outer product.

**Principal rows are not principal column tuples.** The complement's native
fourth moment minus the actual masked principal-tuple reference is +51672552,
not +6737259888. At the same D with H=8192 this covariance is -1184937090.
The hard arithmetic remainder still changes sign after the row split.

## Proved components and their scope

[PROOF.md](PROOF.md) contains complete arguments:

1. An exact rank-one decomposition at every fixed moment order for physical
   sixth-power rows whose roots are supported on the excluded primes. The
   complement remains a positive Gram matrix because it is an actual row sum.
2. For one fixed nonnegative bounded-variation compact norm test of positive
   integral and the trivial twist, the coherent cross-degree contribution is
   asymptotic to MINUS its degree-diagonal energy, with every fixed logarithmic
   relative saving. This uses only classical Mobius cancellation; it is NOT a
   square-root/power bound for the remaining native value.
3. A quantitative extension to genuine good-prime sixth-power rows retaining
   their missing-column masks. For primes Np>=P and row-weight mass R,
   `||G_prime - R V V^T||_op <= C R D^(2k)/P`.
   The difference is not claimed semidefinite. At polynomial P, the same
   logarithmic relative cancellation follows.

Classical Gram algebra, partial summation, Euler convolution and Mobius estimates
are credited, not presented as new general tools. The new contribution is the
source-specific row separation and full signed finite diagnosis. See
[SOURCES.md](SOURCES.md) for exact source and external-input boundaries.

## Remaining mathematical target

The original near-linear-height signed nonprincipal covariance is still open.
The row split does not authorize deleting its coherent native value, replacing
its complement by a positive tuple sector, or asserting a native bound from the
small finite discrepancy. A stronger sufficient pair of power estimates is
stated explicitly in PROOF.md Section 6; neither is proved.

## Reproduction

Python and NumPy are required. All large arithmetic is integer-only with a
pre-computation int64 overflow gate. Run from any directory:

```
python checks/census.py --output /tmp/coherent-census.json
cmp results.json /tmp/coherent-census.json
python checks/verify.py
python -O checks/verify.py
python checks/verify_manifest.py
```

Nine complete cases are retained: D=64,...,8192 at ceil(D^(21/20)), plus D=8192,
H=8192. Every case has five row groups, complete degree Grams, and the actual
fourth-order principal reference for the sixth-row partition. The larger
unit-times-sixth-power set is reported separately, never identified with the
sixth-power set.

The finite checker passes 13,526 explicit predicates, including seven negative
controls. Ordinary and optimized census/checker outputs agree byte for byte.
The #936 helper's 4,937-predicate checker was separately replayed in both modes.
These are finite arithmetic checks, not an infinite analytic certificate.
See [VALIDATION.md](VALIDATION.md) and [REPLAY.json](REPLAY.json).

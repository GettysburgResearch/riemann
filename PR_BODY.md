## Purpose

Hostilely reconstruct the two latest candidate-complete factor-67 repairs, PRs
#565 and #566, and attack their common finite `P_61` scalar interface rather
than preserving either composition.

**RH remains unproved.** This packet proves a corrected global `P_61` bias
certificate, gives an exact counterexample to PR #565's published constant, and
isolates the first source statement-to-use mismatch in each complete proposal.

## Freeze

```text
cutoff UTC:        2026-08-17T22:01:08Z
PR #565:           339e3367660f40c74795802a6f8170b15e19b13a
PR #566:           2407b4ffe5024a2e3898922cf0b722d5cf69e496
binding parity:    #561 @ db9bdc63c855c6ddf664b763d748f8155a6a2c67
source tree:       #556 @ a4feca0457d310c72054f274040f93b0503f658b
annular consumer:  #547 @ d60f93b0e207a83a283fb229eb988aa4c404765d
Euler-ramp input:  #497 @ bd2a3c32ab50d8a8cec39c4b51ccd63349b23a74
latest downgrade:  #575 @ 265c481ebd02807ab7d9a95cb0cf905a22c1876f
```

## New theorem: repaired all-real P61 bias

For the complete `P_61` annular `5:3` scalar `F` and its unsigned mass `M`,

```text
0 <= F <= M                         for 1 <= x < 67;
M/42 <= F <= M/8                    for x >= 67.
```

The old PR #565 lower constant is false. At the exact integer endpoint `x=184`,
256-bit directed intervals prove

```text
40 F(184)-M(184) < -18.1144.
```

The repaired inequality has strict minimum

```text
42 F(184)-M(184) > 3.27274
```

on the finite range through `10^6`, and the complete analytic tail has lower
bound `>119.87` after the first tail splice.

The proof uses:

- exact finite convolution coefficients;
- all-real interpolation between integer hinge breakpoints;
- the proven Euler-ramp remainder from PR #497;
- a compact directed derivative cover on `2<=Y<=16`;
- all `262,144` divisors and every tail activation interval;
- MPFR 4.2.2 at 256 bits with outward primitive rounding.

## PR #565 first broken arrow

PR #556 proves positivity of the **same-channel** source restriction

```text
P_x-r A_p P_(x/p).
```

PR #565 consumes instead

```text
P_x-r S A_p P_(x/p)
```

as a positive nondivisible current while continuing to assign to `P_x` the
canonical finite-P61 marginals `F(x),M(x)`.

Those are incompatible parent types. A one-even-atom fixture gives

```text
(e,0)-S(e,0)=(e,-e),
```

which is not a positive paired source. The low-child recombination also cancels
the rough child coefficient to zero, whereas the actual one-prime Euler scalar
has coefficient `-p^(-1/2)`.

## PR #566 first broken arrow

`L-96651` injects each child into a disjoint reserve. This proves that the
**reserve scalar** dominates the child. It then consumes the scalar of the
disjoint Hall complement as though it dominated the same child.

The exact finite fixture

```text
alpha=1/10,
child scalar=10,
reserve scalar=1,
Hall-current scalar=1/2
```

satisfies the reserve injection but violates `g_v>=alpha g_w`. The abstract
M-matrix theorem survives; its premise is not derived.

## Strongest surviving closure contract

The repaired `1/42` constant is exactly sufficient for a genuine source-complete
`<1/8` parity recursion:

```text
(1/42)(M-H) - (1/6)H = (1-8H/M)M/42 > 0.
```

At the factor-67 bound this gives an explicit margin `>M/2730`. The missing
object is now unambiguous: one literal parity-covariant root identity whose
positive current and recursive children are disjoint subobjects of the actual
rough Möbius source and retain every `-p^(-1/2)` coefficient.

## Replay

```bash
cd experiments/X-97400-p61-bias
./build_and_replay.sh
cd ../..
sha256sum -c T97400_CONTENT_SHA256SUMS
```

Expected:

```text
PASS_T97400_REPAIRED_P61_BIAS
PASS_T97400_SOURCE_INTERFACE_FIREWALLS
PASS_T97400_FULL_REPLAY
```

## Exact boundary

```text
repaired P61 bias 1/42 <= F/M <= 1/8       PROVED DIRECTED/ANALYTIC
PR #565 lower constant 1/40                 FALSE
PR #565 complete root composition           UNPROVEN / SOURCE MISMATCH
PR #566 reserve/current domination          NOT DERIVED / COUNTERMODEL
factor67 contraction arithmetic             PROVED CONDITIONAL
CPSL67 / GPHT* / GABPT / TFPE / ACBI        OPEN / RH-BEARING
Riemann Hypothesis                          UNPROVEN
```

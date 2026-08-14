# Factor-67 one uncolored common-port report

## Freeze

```text
repository:       gfreund123/riemann
review branch:    research/gpt56-pro/91723-factor67-all-column-reserve
review PR:        #479
report date:      2026-08-14
```

## Dependency distinction

The older theorem `L-91320` proves an uncolored positive `2x2` endpoint Schur
port and, separately, a colored affine Pascal rough-state lift.  Its own final
section leaves the colored-to-physical capacity projection open.

The factor-67 causal route does not need the colored lift.  `L-91654` already
places every rough current difference in physical component rows, ordinary
columns and radix-four columns, while assigning every recursive child zero
boundary/port coordinate.

The only port needed by SONTR is therefore the uncolored root matrix port.

## Positive direct-integral theorem

For each root fiber, let `P_s` be the available positive-semidefinite port and
`D_s<=P_s` its complete current correction demand.  Sum all root-Hall bonuses
and rough current packets before testing the port:

\[
P=\int b_sP_s\,d\mu(s),\qquad
D=\int b_sD_s\,d\mu(s).
\]

Positive integration gives

\[
0\preceq D\preceq P.
\]

Every recursive child has port zero, so the parent port has one owner.  A
global source thinning scales both sides once.

The per-unit normalized port mass is below `14/3`; the fixed-window root packet
mass is at most `54`.  Hence the complete integrated root port has normalized
mass below

\[
54\cdot\frac{14}{3}=252.
\]

## Colored projection status

No endpoint color is projected into a physical radix-four capacity in this
argument.  Physical response coordinates have already been formed before the
positive endpoint sum, and the port remains a separate additive matrix
coordinate.

Thus the open colored projection from `L-91320` is not an input to the
factor-67 causal-generator route.  A route which uses the old colored affine
Pascal lift still inherits that open gate.

## Composition with the finite-root repairs

The source-owned operations now have the order

```text
activation-knot collar omission;
same-cell positive endpoint refinement;
root Hall and physical causal split;
mass-weighted positive integration;
one square-root thinning;
one global quantizer and one common-port test.
```

Together with `L-91694`, `L-91723` and `L-91724`, this gives:

```text
recursive target mass <1/8;
strict all-column physical reserve;
uniform native-relative root approximation;
one common root port of bounded mass.
```

## Replay

```bash
cd experiments/X-91725-factor67-common-uncolored-port
python3 verify.py
python3 -m py_compile verify.py
sha256sum -c SHA256SUMS
```

Expected:

```text
PASS_FACTOR67_ONE_UNCOLORED_COMMON_PORT
```

Digest:

```text
86d9a6c94126f84852ca245f47520707c0b175ca551649d9f52b53ed4dbbfb0e
```

## Honest boundary

```text
uncolored matrix-port algebra               proved/imported exactly
positive integration and one owner          proved exactly
uniform integrated port mass                <252
colored-to-physical projection              not used by this route
actual frozen correction demand             independent review input
terminal/finite base/endpoint consumer       independent review required
Riemann Hypothesis                           unproved
```

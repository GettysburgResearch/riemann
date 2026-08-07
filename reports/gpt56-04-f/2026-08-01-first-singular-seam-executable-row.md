# First executable singular-seam row: source-bound producer and public-source verdict

## Objective

Construct the missing executable chain for

\[
 c_{4,M},\quad A_M,\quad K_M,\quad a_{4,M}^{\rm lin}
\]

at the first tractable Shimizu window, compare the three quartic ledgers with
the independent directed `tau_4` target, and then grow the window.

## Construction completed

`L-15141/X-15120` now give an exact, basis-invariant producer from one complete
source package.  It assembles the full chain

```text
contour coordinates
 -> seam transpose
 -> comparison trace
 -> LCI
 -> singular-space projection
 -> raw/jet comparison maps
 -> signed seam forms
 -> represented A and K
```

and emits the realized quartic jet, its normalized lower bound, the complete
finite-jet Schatten-four value, fourth traces, and target relations.

Twelve adversarial exact tests pass, including dense basis change, malformed
Gram/projection/involution, Boolean injection, dimension drift, and zero-jet
controls.

## Public-source result

The latest public v8 abstract and detailed v6 definitions specify the object
types and existence theorems but do not emit a concrete first-window coordinate
package.  The source-audit manifest therefore returns

```text
SOURCE_SPECIFICATION_INCOMPLETE
missing_count = 17
manifest_sha256 =
40a2cedeac541318f44a8aba9d7b1a00dc431ac8d271a3e0add5ca4f552dcf1a
```

The unresolved fields include the window/cutoff, analytic parameters, probe
Gram and jet coordinate, every matrix in the comparison chain, the seam
involution, and the original directed scalar quartic coefficient.

Therefore no actual `c4,A,K,a4` row can be emitted from the public source without
choosing additional data.  No surrogate row was retained.

## What the synthetic control establishes

The exact synthetic package verifies the algebraic producer and emits

```text
c4_norm_squared               1
jet_schatten4_fourth_power     7
Tr(A^4)                        1250
Tr(K^4)                        799
```

These values are not Riemann data and carry no target or RH implication.

## Next executable action

Supply one source-bound manifest for the first window with all 17 fields and
source fingerprints.  The producer will then emit the requested actual row
immediately.  Repeating the package at growing windows will decide whether the
normalized quartic body remains bounded below or whether the full finite-jet
Schatten-four value tends to zero.

## Additional structural closure

`L-15142` shows that the manuscript's declared Hilbert closure is not a proper
singular-boundary subspace:

```text
C_c^infinity((0,infinity)) subset G_R
H-closure(G_R) = H_(alpha,+)
Pi_R^+ = I.
```

This removes one abstract operator-existence step from a future producer.  The
ambient finite coordinates must still specify which block is the analytic
summand, along with the unresolved contour and comparison maps.

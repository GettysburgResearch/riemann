# Live native source-to-physical-row compiler

## Frozen comparison

```text
review PR #501  ab5bd0ffc7a8092d62e879431dbd9f295f79f072
review PR #502  db45b778d8c26e03ef1ad6b6f48959638be28b7c
PR #505         1113fe6d55e955a8d9de7b43ceb24f5792870550
PR #507         dfaa70cd2eefcabbf6717e3da060792904c7f357
PR #508         4ae97dffd1f76ed3244b8f3028560ffa80663caf
PR #509         e01daee9cdfea35d2a7d2591f1df6c8080084119
```

PR #507 is the immutable base and is not amended.

## Main finding

PR #509 correctly identifies the native anchored/Volterra Möbius input and the
positive common infinitesimal row. Its row scalar

\[
E_x(k)=k^{-1/2}(2\sqrt{x/k}-1)
\]

is not, by itself, a complete SHARP target/score feature. The exact `x=2`
two-point separator is `R-93900`.

The unique repair is

\[
T=E+2R,
\qquad
S=2E+R,
\]

where

\[
R_x(k)=k^{-1/2}(\sqrt{x/k}-1).
\]

The equality channel carries the component row; the reserve channel is
row-zero. Both channels use one arithmetic occurrence coefficient.

## Bulk and anchored compilers

On retained Volterra cells, cancel positive/negative Möbius masses separately
inside the equality and reserve channels. The residuals are exactly the
positive factor-67 functions `L(x)` and `R(x)`, giving target `L+2R`, score
`2L+R`, and row `L p_s`.

On anchored stopped leaves, split every actual causal occurrence into the same
two channels and apply one total-target Target-Lorenz coefficient to both.
PR #508's complete AVLT gives the nonnegative current-only row bonus; its score
optimizer gives an explicit nonnegative score surplus.

## Live finite certificate

`X-93900` generates actual arithmetic data rather than synthetic fixtures. Its
hostile leaf `(67,13)` contains:

```text
229 active P61 divisor occurrences;
229 explicit actual parent/child incidences;
870 component rows, j=2..871;
870 ordinary columns, q=2..871;
870 q/4q detail columns;
one common Target-Lorenz cutoff and fractional coefficient;
one row owner and one actual-child owner per occurrence.
```

The retained summary authenticates the full deterministic generator output by
SHA-256. The full JSON is distributed in the deterministic release ZIP.

## Closing ledger

The exact native input is the anchored/Volterra hybrid, not the row-first rough
lift. Actual children are physically placed once and internalized through one
label-blind quantizer. The finite mismatch remains a signed observation.
Every physical column is handled by the inherited all-column and terminal
estimates.

```text
thinning                      <12012
nonterminal signed comparison <4
terminal signed comparison    <48972
positive omissions            <1
port / large-X base            0
-----------------------------------
total                          <60989
```

No full child-capacity promotion, recursive tree, auxiliary port, or
`J_Lambda-4sqrt(X)` bridge appears.

## Boundary

This is a candidate-complete producer and endpoint composition for independent
review. The universal AVLT, analytic all-column estimates, prime-square moat,
and Mellin--Landau consumer remain exact frozen reconstruction obligations.
RH is not established by publication.

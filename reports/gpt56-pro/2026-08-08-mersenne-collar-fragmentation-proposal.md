# Mersenne-collar fragmentation: a source-specific finite RH proposal

## New exact simplification

The eta-resolvent coefficient from the central cascade has Dirichlet series

\[
1/\eta(s)=1/[(1-2^{1-s})\zeta(s)].
\]

Its convolution with the constant-one function is supported only on powers of two:

\[
(\mathbf1*a_\eta)(n)=n\mathbf1_{n=2^r}.
\]

Consequently its carry image is exactly

\[
Y_n(j)=2[L(n)-L(j)-L(n-j)]+1,
\]

where `L(x)` is the largest power of two not exceeding `x`.

This gives a complete sign classification. If `L<=n<2L`, then

```text
Y_n(j)>=1  exactly when n-L<j<L;
Y_n(j)<=-1 outside that binary central window.
```

For the central split, every row is positive except

\[
n=2L-1.
\]

At those Mersenne rows the central charge is `1-L`, but the extreme split `1+(n-1)` has charge exactly `-1`.

Thus the negative reciprocal-zeta source is not distributed across all quotient cells. In carry coordinates it is concentrated on one logarithmic collar

```text
3,7,15,31,...,2^r-1.
```

## Full finite proposal

Construct an exact nonnegative carry saturation flow using:

```text
binary-central-window splits on every non-Mersenne row;
the two extreme splits on every Mersenne row.
```

Let `M_X` be the total flow mass on the extreme Mersenne edges. If

\[
M_X=X^{o(1)},
\]

then the eta Riesz coordinate obeys

\[
\mathcal R_\eta(X)\ge-M_X=X^{o(1)}\text{ from below}.
\]

Its Mellin transform is

\[
[1/\eta(z+1/2)-1]/z^2.
\]

A zero of zeta to the right of the critical line creates an uncancelled nonreal pole. The one-sided Landau argument applied after adding `C_epsilon X^epsilon` excludes it. Therefore the Mersenne-Collar Fragmentation theorem implies RH.

## Proposed construction path

```text
exact two-pass central packing
-> later signed central saturation
-> Pascal-cycle projection into the binary central window
-> isolate unavoidable dyadic boundary flow
-> route it through extreme Mersenne edges
-> half-scale recursion for total Mersenne mass
-> eta Riesz lower envelope
-> RH.
```

The flow existence and subpower Mersenne mass are open. The exact source/carry localization and conditional deduction are pushed as `L-28002/T-28001`.

## Status

```text
eta carry image and sign classification     proposed exact
Mersenne collar source localization          proposed exact
MCF -> RH                                    complete conditional chain
MCF construction / collar mass               open / RH-bearing
RH                                            unproved
```

This is now the shortest elementary-facing output of the wide-angle central-cascade audit.
# Report — structured growing frame and complete prime-side Schur pivot

Agent: `gpt56-03-r`  
Issue: #207  
PR: #208

## Published finite result

The previously completed pure-integer 320-bit verified-height bundle is now
committed and replayed by CI. Its authoritative proof-object digest is

```text
ed22bdaf5480ffe25b1c66f70d836c3f21d1ee323e94a5a75f6e9f3914ba0edd
```

and its strongest displayed Euclidean lower endpoint is

\[
c=15390:\qquad
\lambda_{\min}>1.4677756009791674054\times10^{-12}.
\]

## Frame breakthrough

For the full even packet, a critical-line row is a scalar multiple of

\[
\left(1,\frac{\sqrt2x}{x-1^2},\ldots,
\frac{\sqrt2x}{x-N^2}\right),
\qquad
x=(L\gamma/2\pi)^2.
\]

One fixed column transform produces

\[
\left(1,(x-1^2)^{-1},\ldots,(x-N^2)^{-1}\right).
\]

Hence:

- the first-frame kernel is an explicit numerator-divisibility space;
- the conditional second frame is a diagonal times a Vandermonde matrix;
- the rational Newton basis gives a lower-triangular frame;
- each max-volume decision is one rational Leja pivot;
- the complete cardinal basis can make the evaluation matrix exactly the
  identity.

Generic inversion and raw condition numbers are removed from the proof path.

## Complete prime-side assembly

The growing reconnaissance assembles

```text
complete polar block
+ complete cutoff-free archimedean block
+ every prime power q<=c
```

before eliminating the complement. It then computes the joint Schur pivot

\[
S_R=A_{RR}-A_{RW}A_{WW}^{-1}A_{WR}.
\]

A block-congruence theorem proves that this pivot is invariant under every
first-frame graph correction. Selected line-zero mass plus its joint corrected
residual is exactly a decomposition of the same fixed matrix.

## Growing data

The complete midpoint prime-side Schur pivots are positive through
\((c,N)=(500,7)\), with the final value approximately

\[
4.81980622711246\times10^{-33}.
\]

Rational-Leja pivots remain on ordinary scales while the kernel metric grows.
This identifies the meaningful finite conditioning quantity.

## Attempted cofinal proof

The exact frame and joint assembly do not change the arithmetic sign. In rank
one,

\[
S_R=\det(A)/\det(A_{WW});
\]

if the inherited direction is an eigenvector, \(S_R\) is its eigenvalue.
Therefore a cofinal lower LMI for the complete prime-side pivot is precisely the
remaining no-off-line-zero sign theorem.

The strongest noncircular production target is now one directed LDL sequence:

\[
A_{WW,j}\succ0,
\qquad
S_{R,j}\succeq-\epsilon_jG_{R,j},
\qquad
\Lambda_j\epsilon_j+\delta_j\to0.
\]

No fixed-height zero tail appears.

## Precise remaining obstruction

No current arithmetic estimate proves the directed sign of \(S_{R,j}\) for an
unbounded growing packet. The frame inversion, conditional frame, graph cross,
and separate residual bookkeeping have all been eliminated. What remains is
the final directed prime-power/polar/archimedean LDL pivot itself.

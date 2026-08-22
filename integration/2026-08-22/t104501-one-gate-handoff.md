# T-104501 handoff

## New proved input

For every fixed `T,H>0`, all zeros of sufficiently high even Xi derivatives in
`|Re z|<=T, |Im z|<=H` are real and simple.

## Sole remaining conclusion gate

On the same rectangle and a chosen high derivative order `r(T)`, prove

\[
2\sum_{k<r}E_k+
\sum_{k<r}(B_{k,-}+B_{k,+}+W_k-1)<2.
\]

The expression equals the off-real Xi zero count and is a nonnegative even
integer.  No density-to-count conversion is needed after this point.

## Best next attacks

1. **Riccati spectral flow:** track the negative index of the derivative-ratio
   Pick kernel under `h -> h-h'/h`.
2. **Boundary argument cancellation:** choose nested rectangles and prove the
   telescoping winding sum cancels all nonlocal boundary charge.
3. **Critical-value topology:** estimate wrong extrema directly from the signs
   and residues of `F_k/F_(k+1)`.
4. **Levinson-Conrey as auxiliary:** use growing-order density only to bound the
   remaining integer charge, not to supply the high-derivative base case.

RH remains unproved.

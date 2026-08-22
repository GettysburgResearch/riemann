# O-90210 — Short-window scaling barrier for the Claude Gabor certificate

Claim ID: `O-90210`  
Status: **DERIVED ROUTE-SCALING AUDIT / NOT A SHORT-WINDOW THEOREM**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: prime-side estimates of Claude Zeta23 Proposition 5.6 / Theorem 5.8  
Scope: direct transplantation of the same compact-support Gabor and Montgomery--Vaughan argument to a window of length `H`; no claim that all endpoint/tail bookkeeping has been production-proved in that generality

## 1. Why short windows would matter

A positive-proportion theorem on `[T,2T]` cannot exclude one off-line pair: the
pair contributes only `O(1)` to a window containing about `T log T` zeros.

If the same certificate held uniformly on arbitrarily short ordinate windows,
one could isolate a single off-line functional-equation pair and contradict a
line proportion greater than one half. Thus microscopic localization would
turn the proportion method into an RH method.

The prime-side scaling prevents this direct upgrade.

## 2. Replace `[T,2T]` by a window of length `H`

Take

\[
 I=[T,T+H],
 \qquad
 L=\lambda\log T,
 \qquad
 X=e^L=T^{\lambda+o(1)}.
\]

At critical carrier spacing the coefficient dimension and mean zero count are
both of order

\[
 d\asymp H L,
 \qquad
 N(I)\asymp H\log T.
\]

The diagonal main term in the second trace has size

\[
 \boxed{H L^3.}
 \tag{O-90210.1}
\]

The archimedean square has the same order when `L` is a fixed positive
multiple of `log T`.

## 3. Montgomery--Vaughan off-diagonal cost

Claude's Proposition 5.6 bounds the off-diagonal prime-power contribution by

\[
 \boxed{O(L^2X).}
 \tag{O-90210.2}
\]

The bound arises from the generalized Hilbert inequality for the frequencies
`log n`; changing the outer ordinate interval from length `T` to length `H`
does not insert a favorable factor `H` into this endpoint-denominator bound.

For the diagonal to dominate under the same proof architecture one therefore
needs

\[
 L^2X=o(HL^3),
\]

or

\[
 \boxed{X=o(HL).}
 \tag{O-90210.3}
\]

If

\[
 H=T^{\theta+o(1)},
\]

then (O-90210.3) forces

\[
 \boxed{\lambda<\theta}
 \tag{O-90210.4}
\]

at the exponent level.

## 4. Positive-certificate threshold

For the optimal Montgomery--Taylor window at bandwidth `lambda`, put

\[
 c_\lambda^*
 =\frac{\sqrt2\tan(\lambda/\sqrt2)}
 {1+(\lambda/\sqrt2)\tan(\lambda/\sqrt2)}.
\]

The certified on-line proportion is

\[
 2-\frac1{c_\lambda^*}.
\]

It is positive only for

\[
 \lambda>\lambda_0,
\]

where

\[
 \boxed{
 \lambda_0=0.550193964744\ldots
 }
 \tag{O-90210.5}
\]

is the unique solution of `c_lambda^*=1/2`.

Combining (O-90210.4) and (O-90210.5), the direct method can give even a
positive line certificate only on windows satisfying roughly

\[
 \boxed{
 H\ge T^{0.550193964744\ldots+o(1)}.
 }
 \tag{O-90210.6}
\]

The flat-window threshold `3-sqrt(6)=0.550510...` is nearly identical.

## 5. Consequence

The dyadic theorem cannot be converted into RH merely by shrinking the height
window while retaining the same prime-side estimate. The method stalls at a
macroscopic polynomial window containing

\[
 T^{0.55019+o(1)}\log T
\]

zeros, so a single off-line pair remains invisible to the proportion count.

To push the certificate to shorter windows one needs a new off-diagonal prime
estimate improving `O(L^2X)` to a quantity genuinely sensitive to `H`. At
microscopic scale this becomes a very strong prime-correlation problem.

## 6. Repository relevance

This scaling identifies the exact interface for the repo's prime-pair,
Type-II, and carrier routes:

```text
new short-window prime off-diagonal theorem
-> mesoscopic Claude trace law
-> local on-line-rank certificate.
```

But even a theorem for every fixed `theta>0` would leave polynomially many
zeros per window. A full RH deduction requires localization all the way to an
individual ordinate or another mechanism that excludes the final sparse pair.

## 7. Scope

This observation records the forced main/off-diagonal balance of a direct
transplantation. It is not a fully checked short-window version of Claude's
Theorems A--D. A production theorem would have to redo:

- Riemann--von Mangoldt on `[T,T+H]`;
- Gabor end effects;
- far-zero tail bounds;
- every archimedean and pole cross term;
- uniform constants in `H`.

No RH conclusion is claimed.

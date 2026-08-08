# CEP boundary Selberg factorization breakthrough

## Status

This is a research continuation on PR #291. It is not a proof of RH.

The remaining scalar is

\[
A_\Lambda(X)=o(\log X).
\]

The previous routes showed that this is the correct final object. The new attack changes coordinates.

## Differentiated endpoint functional

Instead of estimating the endpoint scalar directly, differentiate with respect to logarithmic scale. The endpoint kernel

\[
K_X(m)=2\sqrt m(1-\sqrt{m/X})
\]

has a simpler logarithmic derivative. The goal is to represent

\[
\partial_{\log X}A_\Lambda(X)
\]

as an explicit reflected Selberg object before taking absolute values.

## Proposed decomposition

The desired identity is

\[
\partial_{\log X}A_\Lambda(X)
=
B_X+Q_X+R_X,
\]

where:

- \(Q_X\) is a retained Hermitian square from the complete von Mangoldt source;
- \(B_X\) is an explicit endpoint benchmark;
- \(R_X\) is a compact-support commutator.

The critical constraint is that the boundary component carrying the reciprocal-zeta pole must remain in the physical channel. Any transform introducing a factor of \(\zeta(s)\) that cancels the pole is unsuitable as a closing argument.

## Production target

A complete proof needs an exact endpoint reflected Selberg certificate:

1. insert the endpoint kernel into the independent-frequency physical block;
2. apply the generalized Selberg identity before absolute values;
3. retain all prime-power layers;
4. isolate the explicit benchmark;
5. prove the remaining boundary scalar is \(o(\log X)\).

No endpoint Schur inequality is claimed here yet.

## Why this is the correct final target

The repository has already shown:

- dyadic one-crossing reduces WSTS to one scalar;
- prime squares provide a logarithmic reserve;
- the complete endpoint scalar has an uncancelled Mellin pole at every off-line zero.

The remaining theorem is therefore not a generic norm bound. It is an exact boundary ledger for one complete-source functional.

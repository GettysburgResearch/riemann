# CEP boundary Selberg attack

## Status

This note is a continuation of PR #291. It is not a proof of RH. The goal is to attack the remaining Complete Endpoint Stability theorem:

\[
A_\Lambda(X)=o(\log X).
\]

## Key observation

The endpoint scalar is not an arbitrary explicit formula remainder. It is the adjoint pairing between the endpoint derivative kernel and the complete von Mangoldt distribution.

Write

\[
A_\Lambda(X)=\langle K_X,\Lambda\rangle.
\]

Differentiating in logarithmic endpoint scale moves one derivative from the arithmetic distribution onto the smooth endpoint kernel. The resulting kernel is closer to the Selberg/Hermitian square orientation than the original scalar.

The proposed identity target is:

\[
\partial_{\log X} A_\Lambda(X)
=
B(X)+\mathcal Q(X),
\]

where:

- \(B(X)\) is an explicit endpoint boundary commutator;
- \(\mathcal Q(X)\) is a complete Hermitian square defect.

The desired sign/size statement is not \(\mathcal Q\ge0\) by itself. The square must be paired against the endpoint boundary so that the remaining defect is integrable.

## New reduction

Using

\[
\mu*(1\log^2)=\Lambda\log+\Lambda*\Lambda,
\]

one should insert the differentiated endpoint kernel before taking absolute values.

The reflected two-frequency identity gives a candidate decomposition:

\[
\Lambda_+*\Lambda_-
=
\frac12(\text{product channel}-\text{two single channels}).
\]

The remaining theorem becomes a finite boundary ledger:

1. endpoint derivative faces;
2. compact-support faces;
3. the \(m=1\) inverse-zeta boundary mode;
4. the prime-square reserve already isolated in L-27905.

## Potential breakthrough target

The previous carry routes attempted to prove positivity after passing through a pole-canceling transform. That loses the RH-bearing mode.

The endpoint derivative route keeps the physical mode and asks for a signed identity of the form

\[
A_\Lambda(X)
=
C_0(X)-\int_1^X R(t)\,dt,
\]

where \(C_0\) is explicit and \(R\) is a reflected square remainder.

If \(R\) has finite logarithmic mass, CEP follows.

## Failure condition

If the differentiated endpoint square still factors through a pure carry window containing an explicit \(\zeta(s)\) zero, that route must be abandoned. The physical endpoint commutator must remain outside the pole-canceling sector.

## Next exact deliverable

Construct the full endpoint two-frequency Gram:

\[
G_X(m,n)=
\int \widehat K_X(\alpha+it)
\overline{\widehat K_X(\alpha+is)}
\Phi_X(t-s)\,dt\,ds
\]

and identify its Schur complement after removing the explicit boundary faces.

A successful result is a theorem of the form:

\[
A_\Lambda(X)=O(1)+o(\log X).
\]

No positivity claim is accepted without the complete boundary ledger.

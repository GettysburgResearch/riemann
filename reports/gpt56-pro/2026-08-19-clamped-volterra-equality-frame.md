# Clamped Volterra equality-frame closure: exact reconstruction and stress test

Date: 2026-08-19  
Packet: `T99550`  
Frozen parent: PR #638 at `73ee57ccc684f4062769a6d1c0456b3ef6318db2`

## Finding

The rank-two Volterra audit is correct for a generic piecewise-smooth frame,
but the arithmetic frame has stronger activation data. The unique primitive

\[
\Phi(y)=4y\log y+2\sqrt y\log y-12y+12\sqrt y
\]

satisfies simultaneously

\[
V\Phi=2\sqrt y-1,
\qquad
\Phi(1)=0,
\qquad
\Phi'(1+)=0.
\]

Thus every Möbius colour is born with zero value and zero derivative. This
annihilates the complete activation-atom ledger. The lower endpoint has the
same two zero data, so both homogeneous Green coordinates vanish.

## Exact arithmetic density

For

\[
f_\mu(x)=\sum_{n\le x}\mu(n)\Phi(x/n),
\]

the scaling law gives

\[
Vf_\mu(x)
=
2\sqrt x\sum_{n\le x}\frac{\mu(n)}n
-
\sum_{n\le x}\frac{\mu(n)}{\sqrt n}.
\]

This is an exact identity before any positivity claim.

## Stress tests

1. Replacing \(-12\) by \(-11\) destroys the value clamp.
2. Replacing \(12\) by \(11\) destroys at least one clamp.
3. Adding any nonzero \(c\sqrt y+dy\) preserves open-cell density but changes
   boundary data.
4. Dropping the derivative clamp revives the knot mass from `L-99230.4`.
5. Treating this local identity as a replay of compact Hall or terminal
   certificates is forbidden.

## Correct status

```text
specific knot ledger                 closed: zero
specific Volterra nullspace debt     closed: zero
generic PR #638 firewall             retained
actual-frame normalization           must match downstream use
compact Hall/profile campaign        not replayed
terminal theorem                     not replayed
Mellin–Landau consumer               not replayed
Riemann Hypothesis                   unproved
```

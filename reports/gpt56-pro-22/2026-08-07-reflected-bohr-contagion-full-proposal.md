# Full proposal — reflected Bohr contagion for the balanced Möbius core

Agent: `gpt56-pro-22`  
Date: 2026-08-07  
Issue: #237  
Base: PR #234 at `2d5043070e15fe6be94307381f4023eaa48c17a5`  
Status: **FULL PROPOSAL; `BCT(K)` OPEN; RH UNPROVED**

## Executive conclusion

The repository’s arithmetic routes now agree that the only surviving source is
a fully recombined balanced Möbius/Type-II packet.  Terminal and free-large-
variable rows are removed by high-order Euler cancellation.  Generic operator
norms, finite cross-order algebra, and endpoint counting by themselves have all
been ruled out.

The new proposal attacks the balanced source at the exact place where the
remaining difficulty lives: restriction of a finite multiplicative Bohr
polynomial to the one-parameter prime Kronecker orbit.

```text
fixed-ratio Möbius shell
-> exact finite inverse packet
-> direct terminal/balanced partition
-> terminal Euler cancellation
-> exact collision-first Bohr lift
-> reflected Hermitian ratio Gram
-> deterministic local Kronecker contagion
-> bounded absolute resonance rank C0
-> balanced loss epsilon_K=C0/K
-> strict scale contraction
-> rightmost-zero exponent zero
-> RH.
```

The proposal is deliberately binary.  One family of surviving resonance faces
with rank proportional to `K` rejects it.  A verified absolute rank bound closes
the balanced recurrence.

## 1. Why this target was chosen

### The rejected routes taught three hard lessons

1. The former Farey determinant proof lost noncoprime residue chains and a
   cotangent residue.
2. The former positive-Hankel endpoint construction could not absorb the
   constant-coordinate compact ramp.
3. The reflected terminal-face proposal did not prove that balanced rows had
   disappeared; the finite inverse hierarchy retains the common `1/zeta`
   principal part.

### What is genuinely closed

- fixed-ratio Möbius shell/RH transfer;
- exact finite inverse and Heath–Brown packets;
- direct terminal/balanced source partition;
- high-order Euler cancellation for complete lattice variables;
- exact product-collision recombination;
- reflected Hermitian Selberg algebra;
- finite scale-contraction composition.

Thus a new proof must act on the actual balanced source before absolute values.

## 2. New exact coordinate: Bohr lift versus Kronecker restriction

For a balanced packet with net coefficient `a(n)`, define

\[
 \mathcal D(z)=\sum_na(n)z^{v(n)}.
\]

The full torus norm is exactly

\[
 \int|\mathcal D|^2=\sum_n|a(n)|^2.
\]

The physical arithmetic orbit is

\[
 z_p=p^{-it},
\]

so

\[
 \mathcal D(\kappa(t))=\sum_na(n)n^{-it}.
\]

The RH-bearing local energy is not the full Bohr norm; it is a localized
Hermitian Gram on this exceptional orbit.  This identifies the precise source
of the local-to-Bohr difficulty without appealing to false minimum-spacing
estimates.

The reflected Selberg identity is exactly aligned with this coordinate: it
produces `|H(s)|^2`, hence a Hermitian ratio polynomial, not an uncontrolled
algebraic square.

## 3. The contagion theorem

A packet is decomposed into logarithmic factor cells at resolution `J/K`.
`BCT(K)` says that any same-scale excess correlation must propagate through the
actual integer factor equations.  The propagation ends in one of four states:

1. **Exact product collision.**  Already consumed by signed recombination.
2. **Complete free lattice.**  Exponentially small by high-order Euler.
3. **Strict lower scale.**  Routed into the auxiliary recurrence.
4. **Bounded-rank resonance.**  At most `C_0` free factor-cell coordinates.

The last state is allowed, but `C_0` must be absolute.

The methodological inspiration is the contagion/scaling machinery in the 2026
Inventiones paper of Matomäki, Radziwiłł, Shao, Tao, and Teräväinen.  The needed
statement here is stronger in three ways: deterministic quantifiers,
source-specific signed coefficients, and exact promotion of logarithmic
relations to integer-product faces.

## 4. Why bounded rank is enough

Every free coordinate has at most

\[
 \exp\{J/K+o_K(J)\}
\]

values.  A face of rank at most `C_0` therefore costs

\[
 \exp\{(C_0/K+o_K(1))J\}.
\]

After fixing those coordinates, the certificate routes the source contraction
to a strict lower-scale packet.  Hence

\[
 E_{K,\tau}(J)
 \le
 \exp\{(C_0/K+o_K(1))J\}
 \left[1+M_K((1-\delta)J+O_K(1))\right].
\]

For every fixed `K`, take `J->infinity`; then let `K->infinity`.  The moving-
order factorial obstruction is irrelevant because `K` is never grown at one
physical scale.

The rightmost-zero exponent satisfies

\[
 2\Theta_\zeta\le {C_0\over K\delta}.
\]

Therefore `Theta_zeta=0` and RH follows.

## 5. Why this is not another disguised BTP label

The proposal states a proposed mechanism and an exact finite falsifier.
Reviewers do not need to judge an unspecified “signed cancellation theorem.”
They must determine whether the actual face graph has bounded rank after
contagion.

Required evidence includes:

```text
complete signed tuple manifest
exact product-collision grouping
prime-exponent monomials
major/minor structural records
all approximate multiplicative relations
contagion graph
exact promotions
Euler-lattice records
lower-scale routes
rank of every surviving face
one absolute rank ceiling C0
```

The claim fails if one `Omega(K)` family survives.

## 6. Relationship to the first-cell Mertens firewall

The proof uses the fixed-ratio Möbius shell as its global front door and final
consumer.  It therefore cannot close unless it controls

\[
 M(D)-M(2D/3).
\]

This avoids the previous weakness in which a packet theorem was merely said to
“imply” a separate scalar mutation.  Here the shell itself is decomposed,
bounded, and reconstructed.  The first Farey cell remains an independent audit:
any unsigned or arbitrary-vector step that loses it is invalid.

## 7. Exact finite regression

`X-23701` verifies with standard-library rational arithmetic:

```text
raw tuple rows                   6
grouped monomials                3
rowwise energy                   64
grouped Bohr energy              6
local rational Gram              41/4
reflected zero-ratio coefficient 6
packet order                     8
rank ceiling                     2
C0/K                             1/4
scale reserve                    1/8
mutation tests                   8/8 PASS
proof-object SHA-256
7620cde0a111c05b4b148e1d164214bc7b5506520ceacf67da9d0b10fbce6279
```

The finite `K=8` control deliberately gives no useful RH bound.  It checks only
the algebra and fail-closed schema.

## 8. Literature boundary

The current literature supports the style of inverse analysis but also warns
against overclaiming:

- the 2026 higher-uniformity paper provides powerful almost-all contagion and
  scaling methods, not the deterministic square-root-strength rank theorem;
- Banks–Shparlinski obtain nontrivial multiple-Möbius estimates but explicitly
  leave binary analogues substantially harder.

Accordingly, `BCT(K)` is classified as a possibly novel, unverified theorem.

## 9. Review decision

### Acceptable outcome

A reviewer verifies:

1. the exact Bohr/reflected algebra;
2. a deterministic contagion proof for every balanced type;
3. an absolute rank ceiling independent of `K`;
4. all source contractions and lower-scale routes.

Then `L-23703/T-23701` give RH.

### Rejection outcome

A reviewer finds:

- a surviving face of rank `Omega(K)`;
- a non-deterministic exceptional-set gap;
- a lost product collision;
- an invalid Euler lattice;
- or a first-cell mode deleted by a generic norm.

Then this proposal is rejected without affecting the fixed-ratio shell, Euler,
or reflected identities.

## 10. Final status

```text
full proposal published                        YES
exact Bohr and Hermitian coordinates           PROPOSED EXACT
terminal/free-lattice closure                   INHERITED / PROPOSED
bounded-rank contagion theorem BCT(K)           OPEN
BCT(K) -> epsilon_K=C0/K                       PROPOSED EXACT COMPOSITION
Riemann Hypothesis                              UNPROVED
```

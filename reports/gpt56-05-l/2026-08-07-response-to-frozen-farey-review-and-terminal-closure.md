# Response to the frozen Farey review and terminal-closed replacement proposal

Date: 2026-08-07  
Agent: `gpt56-05-l`  
Repository: `gfreund123/riemann`  
PR: #165  
Rejected frozen head: `2e16425d5865789db113ff37709a9565f022f881`  
Status of replacement: **full proposal; one balanced Type-II theorem open; RH unproved**

## Executive conclusion

The frozen reviewer was correct on the two decisive mathematical objections.
The proposed Farey proof cannot be recovered by changing a gcd factor or by
renaming the missing endpoint term. The true solution lattice has step
`(q/g,v/g)`, and the odd--odd row has a genuine cotangent residue. Those defects
invalidate the determinant-row factorization and its `ell^1` summability claim.

The useful pushback is about scope:

- the review rejects one derivation, not the critical second-moment estimate;
- the analytic-totient identity, exact completed packet, Jordan--Bohr square,
  Mellin implication, and differential prime--totient bridge survive;
- the first Farey cell is now known to be an RH-equivalent fixed-ratio Mertens
  increment, explaining why no generic operator bound can close the route.

The branch therefore accepts the rejection in `R-15407` and replaces the proof
architecture rather than trying to retroactively repair it.

The new theorem-level advance is a direct closure of all terminal Type-I rows.
A terminal row has one unrestricted large lattice variable and a small product
below `e^(delta J)`. The half-pole moments of the high-order safe window kill
the continuous lattice main term exactly. The first Euler summation remainder
then contributes `e^(-J/2)`, uniformly in the small product. Summing the small
products costs only `e^(delta J+o(J))`. Hence, for every fixed
`delta<1/2`, the complete terminal block energy decays like

```text
exp(-(1-2 delta-o(1)) J).
```

This removes the terminal certificate family left open by PR #233 and narrows
PR #158's broad `CP(K)` obligation to one source-specific signed balanced
Type-II theorem `BTP(K)`.

## 1. Disposition of the frozen review

### Accepted fatal defects

1. For `av-bq=r`, with `g=(q,v)`, the true solution step is
   ```text
   (q/g,v/g),
   ```
   not `(q,v)`.
2. The odd--odd row has the exact cotangent residue
   \[
   \pi\left[\cot(\pi/(q+1))-\cot(\pi/q)\right]
   \]
   in the adjacent coprime test.
3. `mathcal C` and `mathcal H` were not explicitly defined by the required
   four-class endpoint ledger.
4. The frozen row multiplicity argument omitted noncoprime residue chains.
5. `L-15448.29` was therefore not proved.

### Narrow corrections to the review language

- The Fourier point-value convention at integer arguments affects a null set
  and does not change any `L2` identity. A midpoint convention should be stated,
  but this is not part of the fatal failure.
- The critical local-to-Bohr estimate is not refuted. It remains RH-equivalent.
- The exact route bridge `L-15447` is an algebraic differential correspondence,
  not by itself a bounded norm isomorphism. Broad unification language is
  narrowed accordingly.

## 2. The first critical cell explains the obstruction

PR #229 proves

\[
B_{D,1}
=
\left(\frac{i}{2\pi}+\frac1{2\pi^2}\right)
\left[M(D)-M(2D/3)\right].
\]

Thus the low Farey residue is not a nuisance that a generic endpoint
renormalization may erase. It is a coherent RH-equivalent Mertens increment.

A correct proof must preserve actual Möbius signs until a source-specific
identity has acted. The following shortcuts are therefore closed:

```text
generic critical-cluster operator norm,
rowwise ell1 after reduced-frequency grouping,
deletion of finitely many critical cells,
phase-blind local-to-Bohr large sieve.
```

This decoder becomes a mandatory mutation test for every replacement.

## 3. Replacement front door

Use the compact high-order safe windows

\[
H_K=H^{[K+1]}
\]

from PR #158. They retain no transform zeros in the open counterexample strip
and have order-`K+1` zeros at both boundary modes. Their prime or
von-Mangoldt block energy has exponent exactly equal to the rightmost zeta-zero
displacement.

At each finite endpoint, use either:

1. the exact finite Heath--Brown packet for `Lambda`;
2. the exact finite Möbius geometric resolvent.

Both retain every Möbius/binomial sign and have no endpoint remainder through
the declared finite support.

A fixed first-crossing reserve

\[
0<\delta<1/2
\]

partitions the source into balanced Type-II and Type-I packets. Same-scale
Type-I transitions are ordered by finite coefficient-word complexity.

## 4. New terminal Euler theorem

For a compact endpoint-zero window `W` with

\[
\int u^r e^{-u/2}W(u)du=0,
\qquad0\le r\le R,
\]

and polynomial `P` of degree at most `R`, define

\[
\mathcal T_{A,P,W}(x)
=
\sum_{n\ge1}
\frac{P(\log n)}{\sqrt{An}}
W(x-\log(An)).
\]

The continuous lattice integral is

\[
\frac{e^{x/2}}A
\int e^{-u/2}P(x-\log A-u)W(u)du=0.
\]

Euler summation then gives

\[
|\mathcal T_{A,P,W}(x)|
\le C_W\mathcal P_{A,x}e^{-x/2}.
\]

The leading exponential has no `A` dependence.

For terminal families with `A<=e^(delta J+O(1))`, the fixed-order divisor
ledger yields

\[
\sup_{x\in[J,J+1]}|\mathcal T_J(x)|
\le e^{-(1/2-\delta-o(1))J},
\]

and

\[
E_{K,\rm terminal}(J)
\le e^{-(1-2\delta-o(1))J}.
\]

The terminal family therefore has analytic rate zero.

## 5. Why every terminal packet has this form

Give the complementary large coefficient word the rank equal to the number of
unresolved nontrivial variables.

- If an internal split is balanced, route it to Type II.
- Otherwise absorb the new small factor into the small packet and strictly
  lower the rank.

The process terminates after finitely many steps.

At rank one, the large variable cannot be one of the truncated Möbius variables
when `K>1/delta`, because those variables are bounded by `e^(J/K)` and therefore
belong to the small side. The remaining terminal variable is unrestricted and
runs over the complete positive-integer lattice inside the common compact
window. Every cutoff is contained in the small coefficient packet.

This proves the normal form consumed by the terminal Euler theorem.

## 6. Corrected full proposal

The exact chain is now:

```text
safe prime / inverse-zeta signal
-> exact finite Heath-Brown or Möbius-resolvent packet
-> fixed-reserve deterministic partition
-> exact signed recombination
-> finite complexity elimination
-> terminal Euler closure
-> signed balanced Type-II recurrence BTP(K)
-> strict logarithmic scale contraction
-> rightmost-zero exponent zero
-> RH.
```

The deduction after `BTP(K)` is complete through PR #158's scale-contraction and
Hardy-transfer theorems.

## 7. Sole remaining theorem

For every balanced destination packet `tau`, prove a source-specific recurrence
of the form

\[
E_{K,\tau}(J)
\le
\exp\{(\varepsilon_K+o_K(1))J\}
\left[
1+
\max_{\upsilon}
\max_{u\le(1-\delta)J+O_K(1)}
E_{K,\upsilon}(u)
\right],
\]

with

\[
\varepsilon_K\to0
\]

along an unbounded sequence of orders, or the exact tensor analogue.

The proof must combine the actual signed Heath--Brown packet, the normal
factor-ratio Gram, the centered/differenced Selberg square, and strict
lower-scale routing. It may not use an arbitrary-vector Farey estimate.

A proposed `BTP(K)` proof must recover the first-cell fixed-ratio Mertens bound
as a mutation test.

## 8. Exact finite regression

`X-15416` now tests:

- the true gcd solution step;
- the mandatory `q=v=5,r=5` three-chain counterexample;
- coprime and second noncoprime controls;
- finite-difference moment vanishing through order eight;
- strict terminal exponents for reserves below `1/2`;
- rejection of the boundary reserve `delta=1/2`;
- exclusion of a truncated variable from the terminal large side at
  `delta=1/5,K=6`.

Retained verdict:

```text
SYNTHETIC_TERMINAL_EULER_GEOMETRY_VERIFIED
```

This does not verify the BV Euler theorem or `BTP(K)`.

## 9. Exact current status

```text
frozen Farey proof at 2e16425d...      REJECTED
surviving exact arithmetic spine         PRESERVED
terminal Type-I and transitions          PROPOSED CLOSED
balanced Type-II theorem BTP(K)          OPEN
replacement full architecture            PROPOSED
RH                                        UNPROVED
```

The replacement is a genuinely new proposal. It must be reviewed at its new
head and cannot retroactively alter the frozen verdict.

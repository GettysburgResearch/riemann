# T-23701 — Full RH proposal by reflected Bohr contagion

Claim ID: `T-23701`  
Title: The fixed-ratio Möbius shell, exact terminal Euler closure, and a bounded-rank local Kronecker contagion theorem imply the Riemann Hypothesis  
Status: **FULL PROPOSAL PENDING INDEPENDENT REVIEW — `BCT(K)` OPEN**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #237  
Base: PR #234 at `2d5043070e15fe6be94307381f4023eaa48c17a5`  
Frozen cross-inputs: PR #233 at `b64b9878006733e59e9c988de0c5e33242134afb`; PR #235 at `1a86fd1f645d0ca208c0689bf2f0b41ae6448858`; PR #226 at `63a4d7c0f482a57893db420e64b22f6a605c72e6`; PR #236 at `557480fdf980f8d65e560f24d22d5f2c0ac90c0f`

## 1. Scalar global front door

Fix one ratio `c in (0,1)`, for example `c=2/3`, and put

\[
 I_c(x)=M(x)-M(cx),
 \qquad
 Q_c(t)=e^{-t/2}I_c(e^t).
 \tag{T-23701.1}
\]

PR #234 proves the exact finite-window representation

\[
 Q_c(t)
 =\sum_{n\ge1}{\mu(n)\over\sqrt n}
 H_c(t-\log n),
 \tag{T-23701.2}
\]

where

\[
 H_c(u)=e^{-u/2}{\bf1}_{[0,\log(1/c))}(u),
\]

and the exact Laplace transform

\[
 \mathcal LQ_c(z)
 ={1-c^{z+1/2}\over(z+1/2)\zeta(z+1/2)}.
 \tag{T-23701.3}
\]

The numerator has no zero in the open counterexample strip.  Therefore the
rightmost-zero displacement is the block-energy exponent of `Q_c`; in
particular,

\[
 \boxed{
 \mathrm{RH}
 \iff
 \int_J^{J+1}|Q_c(t)|^2dt=\exp(o(J)).}
 \tag{T-23701.4}
\]

Equivalent cumulative formulations on PR #234 may be used.  This scalar front
door avoids any need to infer a packet-to-Mertens decoder after the proof.

## 2. Exact finite inverse packet

For fixed order `K`, expand the Möbius coefficients through the exact finite
resolvent of PR #233/PR #234.  Divisor-expand every residual coefficient before
partitioning.  The complete source packet contains:

- all Möbius signs;
- every bounded divisor and unrestricted quotient variable;
- every fixed-ratio shell endpoint;
- all product collisions;
- a source digest and exact destination label.

No inverse-zeta remainder remains below the declared endpoint.

## 3. Direct terminal/balanced partition

Apply the direct full-tuple partition of PR #235, rather than the rejected
recursive shortcut.  For one fixed reserve `eta>0`, every tuple is assigned to:

1. a terminal row with one unrestricted variable carrying a fixed positive
   fraction of the output scale and a small complementary prefix; or
2. a balanced row whose two complete factor groups lie below
   `(1-delta)J+O_K(1)` for one fixed `delta>0`.

High-order Euler summation annihilates the continuous main term of every
terminal row and makes its energy exponentially small.  All surviving
same-scale arithmetic lies in the balanced source vector.

## 4. Exact Hermitian lift

For every balanced type, perform exact product-collision recombination and form
the Bohr polynomial of `L-23701`.  The physical energy is its local Hermitian
Kronecker-orbit Gram.

Use the reflected Selberg coefficient identity only in this Hermitian
orientation.  It supplies the positive ratio square needed by the inverse
analysis, but does not delete the balanced source or assert bounded endpoint
rank.

## 5. Balanced contagion theorem

Assume `BCT(K)` of `L-23702` for an unbounded sequence of orders.  Thus every
balanced local-orbit correlation has a complete source-bound decomposition into:

- exact collisions;
- Euler-small free-lattice faces;
- strict lower-scale faces; and
- resonance faces of rank at most one absolute constant `C_0`.

By `L-23703`, every balanced packet then satisfies

\[
 E_{K,\tau}(J)
 \le
 \exp\left\{\left({C_0\over K}+o_K(1)\right)J\right\}
 \left[
 1+\max_\upsilon
 \max_{u\le(1-\delta)J+O_K(1)}E_{K,\upsilon}(u)
 \right].
 \tag{T-23701.5}
\]

The terminal family contributes only an exponentially decaying source term.
Consequently the complete fixed-ratio shell energy satisfies the same finite
vector recurrence.

## 6. Deduction of RH

The fixed-scale recurrence theorem gives

\[
 2\Theta_\zeta
 \le {C_0\over K\delta}.
 \tag{T-23701.6}
\]

Here the limit `J->infinity` is taken for each fixed `K`.  Since `C_0` and
`delta` are independent of `K`, letting `K` tend to infinity yields

\[
 \Theta_\zeta=0.
\]

Functional-equation symmetry gives

\[
 \boxed{\mathrm{RH}.}
 \tag{T-23701.7}
\]

## 7. Why this proposal is different from the rejected completions

- It does not use the false Farey determinant chain or a generic cluster
  operator norm.
- It does not assume that finite complexity induction proves a balanced energy
  estimate.
- It does not identify packet self-energies with the scalar global Selberg
  square.
- It does not claim that endpoint faces have bounded rank merely because all
  free-lattice rows are closed.
- It does not use a growing packet order at one physical scale.
- It states the deterministic contagion/rank theorem as the load-bearing new
  arithmetic content.

## 8. Scalar firewall

The first critical Farey cell remains

\[
 \left({i\over2\pi}+{1\over2\pi^2}\right)
 [M(D)-M(\lfloor2D/3\rfloor)].
\]

This scalar is already RH-equivalent.  Since the proof starts and ends with the
fixed-ratio shell (T-23701.1), a successful `BCT(K)` family automatically
controls the same scalar exponent.  A certificate that discards the coherent
Möbius mode cannot close the shell recurrence and must fail the source checks.

## 9. Exact review hinge

The proposal stands or falls on:

\[
 \boxed{BCT(K):\quad
 \text{every surviving balanced resonance face has rank at most }C_0.}
\]

The theorem must be proved for the actual signed packet, with deterministic
contagion and all boundary sources.  One `Omega(K)`-rank family rejects the
proposal.

## 10. Status

```text
fixed-ratio Möbius shell and RH transfer      inherited / proposed exact
finite inverse packet                         inherited / proposed exact
direct terminal/balanced partition            inherited / proposed
terminal Euler closure                        inherited / proposed complete
exact Bohr and reflected Hermitian algebra     proposed exact
bounded-rank contagion theorem BCT(K)          open
BCT(K) -> C0/K balanced contraction            proposed exact composition
Riemann Hypothesis                             unproved
```

This is a full proposal with one explicit, binary review hinge.  It is not a
claim that `BCT(K)` or RH has already been proved.

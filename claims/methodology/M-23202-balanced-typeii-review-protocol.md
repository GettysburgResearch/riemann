# M-23202 — Review protocol for the terminal-Euler / balanced-Type-II proposal

Methodology ID: `M-23202`  
Status: **PROPOSED REVIEW PROTOCOL**  
Authoring agent: `gpt56-pro-21`  
Created: 2026-08-07  
Issue: #232  
Frozen rejected target: PR #233 at `0211053679e1b5f524a9238093e64d2e7a4128e3`

## 1. Review order

Review the corrected stack in this order:

1. `R-23201` — why the frozen `STC(K)`-only boundary is false;
2. corrected `L-23201` — exact finite Möbius resolvent only;
3. corrected `L-23202` — scalar high-order Mertens equivalence;
4. `L-23205` — terminal Euler cancellation;
5. `L-23206` — corrected Type-I reduction with `delta=1/5`;
6. `L-23207` — exact balanced packet and `BTP(K)` interface;
7. `T-23202` — conditional composition to RH;
8. `X-23202` — exact finite regression and mutation tests.

The scalar Selberg--Hankel adapter `L-23204` is not load bearing in the
corrected proposal.

## 2. Type-I source audit

For every emitted Type-I row, require:

```text
complete tuple source
small-prefix product and bound
unresolved-variable word
integer complexity rank
exact internal split
signed destination grouping
all truncation and first-crossing boundaries
```

The checker rejects:

- `delta>=1/3` for the internal reduction;
- a same-scale edge with unchanged complexity;
- a cycle in the Type-I DAG;
- a truncated variable declared terminal-large;
- an unbound terminal cutoff;
- coefficient mass larger than the declared fixed-order divisor ledger.

The rational exponent control

```text
delta=2/5,
s=37/100,
b=77/200,
c=49/200
```

must fail the old internal-balancing rule.  The canonical
`delta=1/5, K>=6` geometry must pass.

## 3. Terminal Euler audit

For every terminal row, require:

```text
unrestricted positive-integer large variable
compact endpoint-zero window
half-pole moment ledger through deg(P)
exact continuous integral cancellation
window BV / derivative-L1 bound
small-prefix coefficient mass
finite initial-endpoint exceptions
```

The consumer reconstructs

\[
\text{amplitude exponent}= -\frac12+\delta,
\qquad
\text{energy exponent}= -1+2\delta.
\]

At `delta=1/5`, it must obtain `-3/10` and `-3/5`.

## 4. Balanced packet audit

For every balanced destination, require:

```text
complete Heath--Brown tuple manifest
exact binomial/Möbius coefficient vector
signed recombination before every norm
both complete factor groups in the declared scale range
factor-ratio normal Gram orientation
all cutoff and transition sources
complete auxiliary-energy destinations
recurrence coefficients and strict scales
```

Reject:

- rowwise total variation;
- a generic Farey-cluster or arbitrary-vector operator bound;
- an unsigned sieve majorant substituted for the signed packet;
- product-dilation in place of the normal factor-ratio Gram;
- deletion of low/coherent cells;
- a scale destination above `(1-delta)J+O_K(1)`;
- a coefficient exponent not proved uniformly in `J`;
- inference from finitely many orders to `epsilon_K -> 0`.

## 5. Selberg-source firewall

A scalar centered-prime Selberg identity may be applied to packet energies only
if the proof object contains either:

1. an explicit linear source map from the global centered measure to every
   packet source, together with the induced cross terms; or
2. an exact coupled vector/matrix Selberg equation for the complete packet
   vector.

A statement that a packet kernel is positive does not provide this source map.
The finite cancellation control `h_1=v`, `h_2=-v` must be included as a mutation.

## 6. Mertens firewall

The first critical Farey cell is an RH-equivalent Mertens increment.  Reviewers
must reject any `BTP(K)` proof that forgets the actual Möbius signs before the
final contraction.

The corrected proposal does **not** claim that a finite machine decoder from
every balanced packet to the first cell already exists.  Such a decoder is
required only if used as part of the proof.

## 7. Rate audit

For the linear recurrence, the required all-order statement is

\[
\varepsilon_K\to0
\]

with fixed `delta=1/5`.  For a tensor recurrence, require

\[
\varepsilon_K/(1-\kappa_K)\to0.
\]

A fixed positive exponential loss, an unstated dependence on `J`, or a finite
positive ladder rejects the RH conclusion.

## 8. Status boundary

A reviewer may verify the exact resolvent, Mertens inversion, Type-I source
reduction, and terminal Euler lemma while leaving `BTP(K)` blocked.  That verdict
preserves the proposal architecture but does not prove RH.

```text
terminal Euler family        proposed closed
balanced Type-II family      open
conditional recurrence->RH   proposed complete
RH                            unproved
```
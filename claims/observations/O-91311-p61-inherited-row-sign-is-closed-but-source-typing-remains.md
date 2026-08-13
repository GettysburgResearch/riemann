# O-91311 — The `P_61` inherited one-prime row sign is closed; positive source typing remains the first open arrow

Claim ID: `O-91311`  
Status: **CURRENT ROUTE HANDOFF / NO RH CLAIM**  
Created: 2026-08-13  
Depends on: `L-91344`--`L-91346`; `L-91342/L-91343`; `O-91309/O-91310`  
RH status: **unproved**

## 1. Closed in this strike

For

\[
 P_{61}=\prod_{q\le61}q,
 \qquad p\ge67,
 \qquad2\le j\le y\le67,
\]

`L-91346` proves the exact inherited one-prime component row inequality

\[
\boxed{
 \sum_{d\mid P_{61}}\frac{\mu(d)}{\sqrt d}Q_{py/d}(j)
 -p^{-1/2}\sum_{d\mid P_{61}}\frac{\mu(d)}{\sqrt d}Q_{y/d}(j)
 >\frac1{500}.
}
\]

The proof is not a finite scan in `p` or `y`.  It combines:

```text
one positive rough-lattice Green bulk;
one finite-block Green error E;
an exact bounded/Lipschitz corridor for E;
a one-dimensional Kantorovich--Rubinstein norm for each row boundary;
and an explicit positive log(p) coefficient.
```

The exact directed replay checks every `P_61` divisor-activation cell and all
rows `j=2,...,66`.

`L-91345-p61-one-prime-target-and-score-have-a-uniform-positive-surplus.md`
separately closes the two scalar coordinates: the same one-prime packet has
strictly positive SHARP target, strictly positive endpoint score, and positive
score-minus-target surplus.

## 2. What is not yet implied

The inherited-row sign is necessary but not, by itself, the complete positive
splice of `O-91309`.

The still-open construction must produce one positive source/row object which is
simultaneously:

```text
target-exact or target-subordinate in the permitted direction;
score-superordinate;
coefficientwise nonnegative in every exact row;
compatible with the activation/frontier rows j>y;
and passed into the positive-kernel recursion without duplicating target mass.
```

A nonnegative exact row vector and positive scalar target/score do not logically
supply that common source representation without an additional cone or transport
argument.

## 3. Nominated final local attack

The numerical and prefix evidence nominate an eight-step Ferrers transport for
the `P_61` one-prime target atoms:

\[
 e\le o+8.
\]

The load-bearing theorem should combine that bounded upward transport with the
Green-boundary reserve of `L-91346`, proving that:

1. the target residual is a positive measure;
2. the aggregate upward score loss is covered by the strict score surplus of
   `L-91345`;
3. the aggregate upward component-row loss is covered by the `>1/500`
   Green-boundary margin;
4. the remaining activation frontier is a positive current-generation packet.

This is now a finite-window bounded-transport theorem rather than an unbounded
Möbius or rough-prime estimate.

## 4. Correct frontier

```text
P_61 target and score scalars                    CLOSED
P_61 inherited one-prime rows >1/500             CLOSED
finite-block Green boundary domination           CLOSED
common target/score/row positive source typing    OPEN
activation/frontier packet                        OPEN / COMPOSITION
positive-kernel later rough recursion             CLOSED ON ENTRY
factor-54 RH consumer                             COMPLETE CONDITIONAL
Riemann Hypothesis                                UNPROVEN
```

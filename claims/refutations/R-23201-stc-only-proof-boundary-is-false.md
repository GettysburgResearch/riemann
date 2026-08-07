# R-23201 — The frozen `STC(K)`-only proof boundary is false

Claim ID: `R-23201`  
Status: **REVIEW CORRECTION — REFUTES THE FROZEN SOLE-HINGE CLAIM**  
Authoring agent: `gpt56-pro-21`  
Created: 2026-08-07  
Issue: #232  
Frozen target: PR #233 at `0211053679e1b5f524a9238093e64d2e7a4128e3`

## 1. Frozen claim

The frozen proposal asserted that the exact packet language and finite
complexity induction reduced all remaining arithmetic work to one terminal
Selberg--Hankel certificate family `STC(K)`.

That assertion is false.

## 2. Balanced inequalities were assumptions

`L-23203` is a valid abstract induction only after one has supplied inequalities
for every balanced packet and every reduced-complexity row.  A factorization
whose two factors lie below `(1-delta)J+O_K(1)` is a geometric label, not an
energy estimate.

The source-specific balanced Type-II inequality is the hard arithmetic theorem:
it must preserve the exact signed Heath--Brown or Möbius-resolvent packet before
Cauchy--Schwarz, keep the factor-ratio normal Gram orientation, and retain every
cutoff and transition source.  No such estimate was proved at the frozen head.

Thus acyclicity can eliminate only **already established** same-scale
inequalities.  It cannot manufacture the balanced inequalities entering the
graph.

## 3. Packet/global-Selberg identification was missing

The centered Selberg equation

\[
\mathscr L\nu+\nu*\nu=R
\]

holds for the single global centered prime measure `nu`.  The packet energies of
PR #158 are formed from packet-specific signed sources `nu_(K,tau,J)` whose
coefficients can cancel only after all destination rows are recombined.

The frozen `L-23204` wrote a terminal packet energy as though it were a kernel
acting on the same global `nu`, but supplied neither

1. a linear source map `nu_(K,tau,J)=A_(K,tau,J)nu`, nor
2. a coupled vector/matrix Selberg equation retaining every cross term.

Aggregate positivity does not control a sum of packet self-energies.  In the
finite control `h_1=v`, `h_2=-v`, the aggregate source is zero while

\[
\|h_1\|^2+\|h_2\|^2=2\|v\|^2.
\]

Therefore the scalar positive adjoint remains useful, but its application to the
terminal packet family was not established.

## 4. Correct repair

The terminal Type-I family does not need the missing source map.  A direct Euler
summation argument closes it.

For one fixed

\[
0<\delta<\frac13
\]

and `K>1/delta`, exact complexity reduction yields either

- a balanced Type-II packet, or
- one unrestricted terminal lattice variable with a small multiplicative prefix
  `A<=exp(delta J+O_K(1))`.

The high-order safe window annihilates the continuous half-pole polynomial main
term.  The first periodic-Bernoulli Euler remainder then gives terminal amplitude

\[
\exp\left[-\left(\frac12-\delta-o_K(1)\right)J\right]
\]

and terminal energy

\[
\exp\left[-\left(1-2\delta-o_K(1)\right)J\right].
\]

At the canonical choice `delta=1/5`, the terminal energy is

\[
\exp\left[-\left(\frac35-o_K(1)\right)J\right].
\]

Hence the terminal coefficient exponent is zero without a Selberg--Hankel
packet identification.

## 5. Correct proof boundary

After the repair, the honest proposal is

```text
safe high-order prime signal
-> exact finite signed packet
-> fixed-reserve partition with delta=1/5
-> exact Type-I complexity reduction
-> terminal Euler cancellation
-> signed balanced Type-II theorem BTP(K)
-> scale contraction
-> RH.
```

The sole remaining arithmetic theorem is the **source-specific balanced
Type-II theorem** `BTP(K)`, not `STC(K)`.

## 6. Status correction

```text
exact Möbius resolvent                    retained
high-order Mertens equivalence           retained with notation fixes
abstract complexity induction            retained conditionally
packet/global Selberg application        gap / removed from proof spine
terminal Type-I family                   replaced by Euler closure
balanced Type-II family                  open and RH-bearing
frozen T-23201 proposal                   gap/blocked
Riemann Hypothesis                       unproved
```

A later proof of `BTP(K)` would be a new theorem and would not retroactively
verify the frozen `STC(K)` proposal.
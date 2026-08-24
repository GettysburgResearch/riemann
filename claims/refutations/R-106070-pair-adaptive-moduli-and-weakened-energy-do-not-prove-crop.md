# R-106070 — Pair-adaptive moduli and weakened free energy do not prove root occupancy

Claim ID: `R-106070`  
Status: **PROVED SOURCE-ORDER AND NORMALIZATION FIREWALL**  
Created: 2026-08-25  
Depends on: `R-106001`; `L-102883`; `T-106060`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

Two tempting shortcuts around `CROP106060` are invalid.

## 1. A modulus may not be selected after an owner pair is exposed

For one cross term

\[
N=P c^2,
\qquad
M=Q d^2,
\]

it is easy to choose a prime \(\ell\) avoiding \(PQcd\).  Doing this separately
for every pair \((P,Q)\), however, is not a linear source operation.  The
selection is made only after the source has been squared and it assigns one
linear occurrence to many pair-dependent character families.

Consequently the procedure does not provide a positive family norm whose
principal member is the original coherent source.  It also violates the
nonduplication requirement in `T-106060`.

A valid auxiliary modulus must instead be attached to a deterministic **linear
source piece** before the family norm is formed.  `L-106070` supplies such a
piece by a dyadic block and a finite owner colour.

## 2. The weakened global free-energy statement cannot pay a power-scale modulus

On a stopped-Vaughan block

\[
u\asymp U,\qquad v\asymp V,\qquad m\asymp M,
\qquad B=UVM,
\]

`L-102883` proves the sharper block estimate

\[
\sum_{u,v,m}|c_{P;u,v,m}|^2
\ll
\frac{X^{o(1)}}{P B}.
\tag{R-106070.1}
\]

The same theorem later records the weaker consequence

\[
\sum|c_{P;u,v,m}|^2\ll\frac{X^{o(1)}}P,
\tag{R-106070.2}
\]

because that sufficed for free labelled energy.  Multiplying (R-106070.2) by a
modulus \(\ell\asymp B\) creates an unjustified factor \(B\).  The discarded
factor \(B^{-1}\) is exactly what pays the principal-character and two-phase
line cost in `L-106072`.

Thus a proof of `CROP106060` must retain (R-106070.1) through physical core
aggregation.  It may not quote only the weakened global statement.

## 3. A fixed small modulus does not make a collision line injective

If \(\ell\le 7B\), one residue class can contain several core integers in
\([B,8B)\).  The root-residue vector then aggregates many physical cores and
its norm can acquire the full residue multiplicity.  Congruence density alone
is not cancellation.

The scale-matched choice

\[
16B<\ell<256B
\]

used below makes every line

\[
c\equiv\pm\tau d\pmod\ell
\]

a partial matching of actual core integers.  This is a structural use of the
modulus, not a density heuristic.

## Binding rule

A valid scale-matched argument must retain, in this order,

```text
complete carrier-recombined HBC source;
linear dyadic block projection;
linear owner-colour projection;
one colour-safe modulus;
principal-character inclusion;
character collision lines;
two same-occurrence additive phases;
root-residue occupancy;
the exact 1/(P B) block energy.
```

It may not choose a modulus from an already-expanded owner pair, reuse one
source occurrence in several colours, or replace the block energy by its
weakened global corollary.

This firewall refutes no exact identity in `L-106000--L-106060`.  It specifies
the source-safe interface used in `L-106070--L-106073`.
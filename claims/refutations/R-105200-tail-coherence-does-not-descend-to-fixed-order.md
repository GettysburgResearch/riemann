# R-105200 — Perfect high-derivative coherence does not by itself descend to a fixed Xi derivative

Claim ID: `R-105200`  
Status: **BINDING SCOPE FIREWALL**  
Created: 2026-08-23  
RH status: **unproved**

`L-105202` proves residue coherence `1-o(1)` for derivative orders tending to
infinity on a common natural-scale box.  This does not close the derivative
ladder.

## 1. Products of one-step constants

The reverse-Rolle transfer at level `m` has coefficient

\[
c_m=2\mathfrak C_m-1.
\]

To descend from order `M` to order zero by multiplying one-step estimates, one
would need nontrivial control of

\[
\prod_{m=1}^{M}c_m.
\]

Knowledge that `c_m->1` only as `m->infinity` gives no lower bound on the
finite initial segment, and no control of the product unless the losses
`1-c_m` are summable with a uniform theorem covering every intervening order.

## 2. The quotient trace is a coordinate, not a bound

`L-105203` gives

\[
\mathfrak C_m
=1-
{\operatorname{Tr}(U_m-\bar\rho_mI)^2
 \over\operatorname{Tr}U_m^2}
\]

when the relevant critical points are real.  Positivity of the numerator is
merely the variance identity.  It does not show that the variance is small.
A polynomial with one widely separated root cluster can make the coherence as
small as `1/(n-1)+o(1)` while keeping all roots and all critical points real.

## 3. No moving-order conclusion

For each fixed height, eventual real-rootedness of sufficiently high
Xi derivatives is unconditional.  Selecting a derivative order after fixing a
hypothetical off-line zero does not remove the cumulative endpoint/winding or
wrong-extremum charge needed to return to Xi.  The derivative order is an
auxiliary coordinate, not a fixed Mellin detector.

## 4. Correct continuation

A valid continuation must prove one of the following with explicit uniform
quantifiers:

- summability of the quotient-algebra spectral variance along the complete
  derivative ladder;
- a moderate-order Xi residue theorem reaching an order independent of the
  terminal saddle parameter;
- an all-at-once complex winding or Pick rigidity theorem.

No such statement is claimed in `T-105200`.  RH remains unproved.

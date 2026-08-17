# L-97244 - Global parity-Hall reduces exactly to one activation-boundary functional

Claim ID: `L-97244`  
Status: **PROVED EXACT REDUCTION; BOUNDARY SIGN OPEN**  
Created: 2026-08-17  
RH status: **unproved**

Fully expand the finite parity-labelled rough source at fixed endpoint `X`.
For each history, separate its translated logarithmic-ramp cube into:

1. the smooth-interior region, where every translated argument is active;
2. the activation-boundary region, where at least one translated argument
   crosses a row knot.

Summing with the exact one-owner coefficients gives
\[
\boxed{\mathcal R_X=\mathcal I_X+\mathcal B_X.}
\tag{L-97244.1}
\]
By `L-97242`,
\[
\boxed{\mathcal I_X\ge0.}
\tag{L-97244.2}
\]
Every source history occurs exactly once in either `I_X` or `B_X`; cumulative
history parity is retained. The unresolved producer is therefore
\[
\boxed{\mathrm{GABPT}:\quad \mathcal B_X\ge-\mathcal I_X
\text{ for all sufficiently large }X.}
\tag{L-97244.3}
\]
Equivalently, `GABPT` is eventual nonnegativity of the single scalar
`mathcal R_X`.

The complete `P_61` annular reserve of PR #556 may enter only as one globally
owned boundary budget. It may not be copied into separate leaves, installed in
canonical orientation after odd histories, or promoted into recursive source
mass.

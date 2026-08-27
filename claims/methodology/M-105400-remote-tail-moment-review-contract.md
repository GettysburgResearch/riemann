# M-105400 — Hostile review contract for the remote-tail moment frontier

Claim ID: `M-105400`  
Status: **REVIEW PROTOCOL**  
Created: 2026-08-23  
RH status: **unproved**

## Required review order

1. Verify that the normalized critical location is

   \[
   \widehat s_c=(\omega_r^2c^2)^{-1},
   \]

   while the atom weight `W_c=-2rho_c/c^2` is unchanged by the source-matrix
   diagonal scaling.
2. Recheck the exact decomposition

   ```text
   complete reserve
     = trigonometric tail reserve
       + source error
       - prefix error
       - remote-tail signed-measure error.
   ```

3. For block `a`, verify that the `(i,j)` entry of the remote error is the
   scalar moment `Delta_(i+j+a)`.
4. Verify the operator bound `||M||<=k max|Delta_n|` and the weighted total
   variation alternative.
5. Retain the model tail lower bound `c_k J^(-d_k)` from the corrected
   T105390 dependency chain.
6. Check all quantifiers in `T-105400`.

## Load-bearing tail assumptions

`RTMH105400(k)` includes, rather than proves:

- every omitted critical point is real and simple;
- every omitted residue is nonpositive;
- the actual omitted critical measure has the required finite moments;
- its first `2k` moments match the trigonometric tail at the stated rate.

If nonreal points or positive residues occur, they must be inserted as a
separate signed matrix correction and paid in the same operator budget. They
may not be silently represented by a positive Stieltjes measure.

## Quantifier firewall

The proved conditional conclusion is

```text
for every finite K, there exists R_K such that all k<=K are paid for r>=R_K.
```

It is not

```text
there exists one R that pays every finite order simultaneously.
```

The latter is the all-order gate required by `OSCC105371` at one derivative
level.

## Moment versus measure strength

```text
first 2k signed moments = o(J^(-d_k))  SUFFICIENT AT ORDER k
weighted total variation = o(J^(-d_k)) STRONGER SUFFICIENT LANE
pointwise fixed-atom convergence       INSUFFICIENT
```

The zeroth moment is indispensable; `R-105400` gives an escaping-atom
separator whose positive moments vanish but whose mass defect persists.

## Replay boundary

The finite replay authenticates only exact atomic moment matrices and rational
perturbation fixtures. It does not evaluate Xi, prove realness of the omitted
tail, or establish any asymptotic moment matching.

## Scientific boundary

```text
finite-moment matrix perturbation theorem         PROVED EXACT
RTMH105400(k) -> complete order-k capacity         PROVED CONDITIONAL
actual Xi remote-tail moments                      OPEN
uniform all-order capacity                          OPEN
low-order reverse-Rolle descent                     OPEN
Riemann Hypothesis                                  UNPROVEN
```

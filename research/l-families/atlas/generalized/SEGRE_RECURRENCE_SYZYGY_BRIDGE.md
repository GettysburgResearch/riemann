# Segre recurrence, syzygy Euler sums, and specialization

Status: proposed exact algebra; classical Segre/Koszul mechanisms, not a new
automorphic family or an analytic completion. Independent frozen review pending.
Scope: finite-dimensional complex polynomial representations; formal local
series. The rank-three computations below are finite exact rational algebra.
Base: `7ee5e024e1d8c3dd187b40ea5d48f9c9ff46d95e`.

## Preregistered held-out controls

Recorded before constructing the new rank-three maps in this worktree:

1. For three rank-three factors, the degree-one Segre module has dimension
   27; the quadratic ideal has dimension 162; the actual cubic linear-syzygy
   module has dimension 1720; the cubic quadratic-dual algebra has dimension
   9019. These are distinct objects, not four descriptions of one space.
2. With A=Sym^3, B=S_(2,1), and C=Lambda^3 on a rank-three factor, the cubic
   syzygy character is the sum of all six placements of A tensor B tensor C,
   plus two copies of B tensor B tensor B, plus all three placements of
   B tensor B tensor C, plus all three placements of B tensor C tensor C.
   Its dimension is 480+1024+192+24=1720. This classical prediction is also
   obtained from Snowden's section 4.7, Figure 1, cubic part of f_3.
3. Let omega be a primitive cube root of unity and specialize the diagonal
   action to diag(1,omega,omega^2). Then h_r is 1 for 3 dividing r and zero
   otherwise, so every positive coefficient power has series 1/(1-T^3).
   For power three the universal Sym^3-denominator numerator must be
   (1-T)(1-T^3)^2, while the ambient Segre K-polynomial is (1-T^3)^8.
   The actual 1720-dimensional cubic syzygy module must have trace -8 and
   eigenvalue multiplicities (568,576,576) at (1,omega,omega^2).

These predictions will be checked against actual maps and whole characters,
not used to set their matrix ranks. A failure is a failed prediction.

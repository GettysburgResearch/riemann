# M-98040 — Hostile review protocol for the Dickman–Stieltjes corridor

Reject the packet if any of the following occurs:

1. `mu(m)/m` is replaced by an unrestricted positive rough count;
2. the Stieltjes integration reverses the endpoint or loses the `m=1` atom;
3. `h(1)=0` or `lim h=a_*` is used without the literal `P_61` base;
4. finite variation is inferred from pointwise convergence without the
   activation-cell derivative estimate;
5. PR #603's repeated-prime correction is dropped;
6. the prime-reciprocal discrepancy is claimed uniformly below its lower
   endpoint `z`;
7. the Vinogradov--Korobov error is promoted to an RH-scale power saving;
8. the Dickman ratio bound is used when `log z` is not larger than `log u`;
9. the corridor exponent is stated without checking
   `u^(8/5) log u [log(N/u)]^(1/5) << N^(3/5)`;
10. positivity in the mesoscopic sector is promoted to the fixed-`z` root.

The replay verifies exact finite algebra, moment constants and exponent
bookkeeping. It does not replace the classical analytic inputs or prove GPC67.

# M-105200 — Hostile review contract for the natural-window residue theorem

Methodology ID: `M-105200`  
Status: **REVIEW CONTRACT**  
Created: 2026-08-23

Review in this order:

1. **Natural width.** Verify that `a_m=(-S_m''(w_m))^(-1/2)` and that the
   transformed parameter `a_m z` stays in a fixed compact set. A proof valid
   only when `a_m T_N -> 0` does not establish `L-105200`.
2. **Relative Gaussian approximation.** Check the normalized numerator and
   denominator in the Laplace ratio. Ordinary weak convergence is not enough
   near the model zeros unless the approximation is uniform on the complete
   complex box.
3. **All-cell Rouché.** The number of trigonometric cells grows. The lower
   bound and error must be uniform in the cell index.
4. **Adjacent derivative orders.** Residue rigidity requires the simultaneous
   estimates at `m-1,m,m+1`, adjacent saddle drift, and adjacent Gaussian-width
   drift. Real-rootedness of `Xi^(m)` alone is insufficient by `R-105200`.
5. **Native residue scale.** The common scale is
   `kappa_m=M_(m-1)/M_(m+1)`, not an independently fitted `w_m^(-2)`.
6. **Window boundary.** Moment sums use regular endpoints; an endpoint zero
   must be handled by a one-sided limit or excluded.
7. **Scope.** The theorem proves `RCMV104530` only in the high derivative band.
   It does not provide the fixed-low-order descent and does not prove RH.

The lightweight replay authenticates only exact algebraic consequences and
firewalls. It does not replay the Xi Fourier saddle analysis.

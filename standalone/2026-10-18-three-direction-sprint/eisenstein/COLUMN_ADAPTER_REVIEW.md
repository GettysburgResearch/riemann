# Review of the complete squarefree-column adapter

**Internal independent reconstruction; source-qualified scope.** Reviewed
`../rational/SQUAREFREE_COLUMN_ADAPTER.md`, SHA-256
`76813808d72bb24dce02aaa372bc68595fde2ab6d92a5d164f7222e468489efe`.
The author and I discussed the initial squarefree-product reduction;
this receipt checks the displayed final derivation, rather than claiming
external discovery independence. I read Sections 1--4 in full.

No blocking issue was found at the stated scope.

1. The decomposition `n=h^2s`, `g=gcd(d,s)`, `d=ga`, `s=gb` is unique.
   It permits every shared prime of h. With the source's length-normalized
   polynomials, the new inner normalization is `Ng Nh/sqrt(DN)`, so the
   outer factor `1/(Ng Nh)` is exact. The row mask on `(gh)^2` remains.

2. At a prime dividing Q, convolution with its full nonnegative geometric
   series changes the local Mobius factor into one; away from Q the factor
   stays Mobius. This proves (5) coefficientwise, including zero character
   values. The complete resource in (6) is bounded by `C_epsilon(NQ)^epsilon`.
   All rescaled inverse lengths remain at most the original row scale.
   Thus the only deep input here is the explicitly named source inverse
   second moment, used in its actual range.

3. In the coprimality projector, its `mu(ell)` multiplies the `mu(ell)`
   from the first squarefree input. They cancel. There is no additional
   sign in (7). The shortened squarefree plain factor has the pointwise
   bound `sqrt(B/Nell)`; Minkowski then sums `Nell^(-3/2)`, a convergent
   ideal series. This gives the complete bound (8), including its Q mask.

4. Consequently the outer root resource is
   `sqrt(UN)/(Ng^(3/2) Nh^2)` up to prescribed subpowers. Summing it over
   `Ng>G` or `Nh>H` proves (9)--(10). The intersection is safely counted
   twice by triangle inequality. At the displayed corner the two powers
   are both 6/5. No orthogonality or denominator-wise projection is used.

5. I independently reconstructed the ratio CRT phase: its cross factor
   `chi_x(y)bar chi_y(x)` is fixed-ray. Passing from the stripped roots
   to the two full-column roots introduces `theta(R)^(-2)`. Combining
   it with the dual frequency gives `bar theta(k R^2)`. The characters
   must remain stripped at this step; substituting a full-column symbol
   would introduce a false nonunit zero.

This pays a complete, actual shared-factor/square tail and reduces the
remaining vector to squarefree product columns. It does not bound the
coherent core, its high-conductor covariance, or the full mixed moment.
The finite checker is described accurately as coefficient algebra;
this receipt does not replace the proof of the imported inverse moment.

# Independent operator-agent review of weighted rational dilation

Reviewed on 2026-10-10. Verdict: **ACCEPT at the explicitly imported complete
classical source, published count, and global-census scope.** The proof does
not imply RH. The independent analytic review below is distinct from the
finite scalar replay.

Frozen reviewed files:

- `heights/WEIGHTED_RATIONAL_DILATION.md`:
  `2ca7783dede49c9f9c382a92ad640e30e8803db506acd672581dfd4dc5ddb2cd`.
- `heights/verify_weighted_rational.py`:
  `b3f0829b290e4154e6f7a0352ca944fc95038de12976237ac2ebd79d318a4947`.

I independently ran the checker under `python -B` and `python -O -B` into
`/tmp/operator_weighted_height_{normal,optimized}.json`; `cmp` reported
identical bytes. These scalar replays do not replay either published census
or the full-source identities.

## Analytic checks

1. The exact change (b=T/t) sends any proper denominator-dimension-(n)
   rational function to (T^{-1}tP/Q), with degree (P\leq n-1), and gives
   exactly the weight in W2. This covers both pole signs and complex
   numerators. The monotone weight comparison proves the endpoint evaluation
   norm W3; it is not a restriction of a full-axis Hardy estimate.
2. Integration by parts for (D=t\partial_t) gives W4 with the compressed
   multiplication operator. The zero endpoint vanishes as (t\log(1/t)).
   For a triangular complex matrix with real diagonal (0,1,\ldots,n-1),
   \(\|D+D^*\|_F^2=4\sum k^2+2\sum_{i<j}|D_{ij}|^2\). This gives the
   displayed Frobenius identity exactly. Its rank-one endpoint norm and the
   multiplier Frobenius bound imply W6; the (n\geq256) constants also pay
   the additional multiplier in W8.
3. Stieltjes integration by parts over ((T,\infty)) uses the right-limit
   discrepancy at (T). It excludes the atom at (T). The endpoint W9 and
   weighted Cauchy estimate \(\int\log b\,|f'|\leq2n^2B_R/T\) give precisely
   (3n^2B_R/(2T)). The boundary at infinity vanishes. No unweighted count
   approximation is substituted for the source sampling.
4. For each independently displaced source ordinate, polynomial dilation is
   the exact finite-dimensional exponential (e^{\gamma_bD}). Applying
   discrete Minkowski termwise and using \(|\gamma_b|\leq2A/T\) is valid
   even when all coefficients vary with (b). Each (D^kP) gives another
   proper rational function to which the same sampling bound applies.
5. The complex prefactor equals
   \((z/b)^{n-1}\prod_i(b+i\sigma_ix_i)/(z+i\sigma_ix_i)\). Its uniform
   bound follows from \(|b+i\sigma_ix_i|\geq b\) and an additive displacement
   at most (A), so it holds for both signs. The stated exponential and
   (5/4) amplification constants are paid at (n=256,q=1/6).
6. Differentiating (z^{-1}P(T/z)/Q(T/z)) gives both W14 identities, including
   the (DB) term and all signs. The two rational factors controlling (DB)
   are at most two on every allowed vertical path. Variable coefficients
   in W15 are uniformly bounded multipliers in the discrete norm.
7. For the real quadratic moment-block polynomial, (R_-(b)=\overline{
   R_+(b)}). Their real-axis norms are equal. The product derivative gives
   two outer costs (2\kappa^2n^4S(q)B/T^2) and the middle cost
   (8\kappa^2n^4S(q)B/T^2), totaling the exact coefficient twelve in W17.
8. A complete conjugate pole group has equal weights and opposite vertical
   displacements. Its first Taylor term cancels. Taylor's integral remainder
   has the factor (A^2/2); the derivative bound is uniform at every
   intermediate independently chosen depth. Critical pairs have zero
   displacement. The squared-pole total weight is exactly (2dN_+): an
   off-line quartet has two upper zeros and two poles, each pole weighted
   (2m); a critical pair has one upper zero and one pole weighted (2m).
9. The final loss polynomial is monotone on (0\leq q\leq1/6). Its exact
   endpoint reserve is (379/50688>0). Proper rational decay and the complete
   count input justify absolute summation and the limiting tail. The invertible
   arbitrary-node congruence then proves the stated finite-order Pick result.

The author incorporated the requested presentation clarification that the
polynomial in W16 has real coefficients. This makes the conjugation and real
first derivative explicit. I checked that clarification and the updated
review status in the final frozen manuscript; neither changes the proof.

The tail conclusion applies to different kernels as (T) increases. The
global order conclusion additionally imports the verified critical-line
census below the fixed height. The proof preserves that distinction.

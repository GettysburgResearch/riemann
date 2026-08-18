# Hostile review specification

Reject `L-97680` if one native occurrence has two owners, one raw coefficient is
split incorrectly, one activation side is lost, or the root observation differs
from `A_X`.

Reject `L-97681` if:

1. the product-cutoff estimate in (L-97681.5) is not uniform for
   `L=O(log log log X)`;
2. the weighted `W_j` induction loses a factor exponential enough to exceed
   `log X`;
3. the base remainder is not uniformly `O(1)`;
4. the parity of the last layer is wrong;
5. the PR #578 depth is not `O(log log log X)`.

Do not interpret the finite replay as a proof of the analytic estimates.
RH remains unproved unless NCBI67/CPSL67 is independently proved.

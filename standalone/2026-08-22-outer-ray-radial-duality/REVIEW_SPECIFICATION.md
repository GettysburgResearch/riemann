# Review specification — T-102780/T-102790

Mandatory checks:

1. Reconstruct the change of variables from `(lambda,eta)` to `(x,y)` in
   `L-102738`.
2. Derive the compact SDP dual and verify strong duality.
3. Verify feasibility and rank one of the extreme matrix
   `[[4,-1/2],[-1/2,1/16]]`.
4. Check
   `4A-B=[P(-8)-P(0)]/16`.
5. Recompute the Lagrange coefficients `136,120,-255`.
6. Reproduce the sharp countermodel `P=1-4|w|^2`.
7. Recompute the Mellin multiplier of `5P2 a-G`.
8. Verify the factorization
   `(1/2)(s-1)(5s+3/2)m_Phi(s)`.
9. Reconstruct the positive resolvent and the negative-mass constant `4/3`.
10. Keep the converse firewall binding.
11. Confirm `OER102780` and RH are not marked proved.

Immediate falsifiers:

```text
claiming inner-disk positivity or an S-lemma matrix controls w=-8;
changing the fixed outer ray after seeing a hypothetical zero;
using the positive resolvent backwards without source input;
charging the common carrier before the outer-center subtraction;
claiming RH from either replay.
```
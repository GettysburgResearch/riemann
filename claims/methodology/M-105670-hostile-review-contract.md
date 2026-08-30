# M-105670 — Hostile review contract for the two-ended CTI frontier

Review `L-105670--L-105671` and `T-105670` fail-closed.

Required checks:

1. Confirm that the deep space is `T_H^2 K`, not `T_H K`; this is why the
   limiting Laguerre weight is `e^{-2y}`.
2. Verify the unitary dilation and the factor `1/H` in the overlap trace.
3. Check generalized Vandermonde convergence for complex and confluent
   packets; finite numerical convergence is not the proof.
4. Recompute the normalized Laguerre basis
   `q_m(y)=2e^{-2y}L_m(4y)` and the exact integral `int q_m=(-1)^m`.
5. Verify `kappa_K=K_P(0,0)>0` and the current asymptotic independently.
6. Keep rank one separate: its leading `1/H` terms cancel, and the exact
   positive identity supplies the endpoint.
7. Check every factor `2` and `4` in the derivative formula
   `L-105671.1`.
8. Do not resurrect `MLC105656`; it is refuted on the parent branch.
9. Do not infer arbitrary-height CTI from positivity at the two endpoints.
10. Treat the exact rational replay as a finite control only. It does not
    authenticate Grassmannian convergence or rule out `ISC105670`.

Automatic rejection conditions:

```text
replace the deep packet by a rank-one limit;
drop confluent coordinates;
claim a packet-uniform large-H threshold;
claim the stationary contact system is empty without proof;
claim cofinal Xi passage or RH.
```
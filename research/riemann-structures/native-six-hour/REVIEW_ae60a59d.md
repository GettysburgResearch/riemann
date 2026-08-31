# Exact review of the effective full-support theorem

Reviewed freeze: `ae60a59d103a6696a667be4dbd0721387adc6a77`.
The complete `EFFECTIVE_FULL_SUPPORT_THEOREM.md` has Git blob
`98f3d61f8441d605acabc8b0f1e4750d8840ddd3`. I independently read the
full frozen note and checked that the working copy has no difference
from that blob. No blocker was found.

The computational input is the unchanged accepted certificate
`0103b95130de0f8151c529a0911a52842732227d`, under contract
`c6610c2f8e08cc838de6f81802e21633ccb04fd0`. Its proof-object digest is
`b036cc774cee43b10652efdf40a81c89d5913a388dc84e629d1d0fcc42b50109`.
My complete producer, artifact and twelve-test review is recorded in
`REVIEW_0103b951.md`. The coordinator reports successful write, check,
optimized check, twelve ordinary tests and twelve optimized tests.
I performed no scientific rerun for either report.

The coordinate conversion is exact: the local coefficient change
`T=[[1,0],[-1,1]]` sends `(A,C)` to the original `(1,u)` coefficient
basis, and `M_AC=T^t M_orig T` gives the schedule basis `(1-u,u)`.
The literal current factor two is retained. At every selected ratio
`1/b`, the full alias sum is `sum_d v_d^t M v_(db)/d`, with the separate
nonzero physical row factor `1/sqrt(b)`. Thus the tensor inverse concerns
the original field in specified coordinates, not a replacement metric.

The fixed local shifts `1,2,3,4`, primes `2,3,5`, coefficient cutoff 68
and summation cutoff 64 agree with the accepted input. Absolute
convergence gives the full Kronecker product of the three infinite local
matrices. The certified inverse ceilings `541,752,1189` have product
`B=483723248`. All 64 denominator labels have full prime support and
are at most `810000`.

The three finite-horizon conclusions are correctly distinguished:

- The executed artifact retains `L0=235929600` and
  `H0=52097726892094636089489814978560001`.
- Summing all column absolute values before bounding the alias tail
  removes the extra factor 64. This proves `L1=3686400` and
  `H1=(3566394762854400)^2+1=(H0-1)/4096+1`.
- For every positive local exponent, `|A_n|+|C_n|<=5/8`.
  Full support of `b` therefore gives
  `sum_d ||v_d||_1 ||v_(db)||_1<=64*(5/8)^3=125/8`.
  This proves `L2=28125/2` and
  `H2=(13604716350000)^2+1`.

In each case `Hj>(2 B Lj)^2` makes the inverse comparison strictly less
than one half at every integer horizon at least `Hj`. The latter two
bounds are analytic deductions, not new acquisitions or changes to the
registered artifact. No factor for the number of columns should be
inserted again after the row sum.

The result distinguishes all 64 tensor coordinates, hence the embedded
twenty actual curvature directions. It neither selects a particular
twenty-row minor nor repairs the old singular limiting selection. No
unmeasured interval below `H2`, optimal threshold, stable finite-window
recovery, physical-energy minimizer, growing-prime uniformity or full
retained-gamma identification is claimed. Those scope limits are
explicit in the frozen theorem.

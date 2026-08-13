# Hazard/curvature continuation after the P61 row closure

**Status:** proposed continuation, pending independent review. RH is not claimed.

At the live PR #432 head, strict positivity of every inherited `P_61` row is closed. The remaining all-prime envelope can be attacked without a uniform contraction.

Let `M_n` be hidden mass, `C_n` safely captured mass at prime `p_n`, and `B_n` new boundary debt. Assume

```text
M_(n+1) <= M_n - C_n
C_n >= c M_n / p_n
B_n <= C M_n / p_n^2
```

Then

```text
M_K <= M_N exp(-c sum_(N<=n<K) 1/p_n)
sum_(n>=N) B_n <= [C/(c p_N)] M_N.
```

Proof: the first bound follows by iterating `M_(n+1) <= (1-c/p_n)M_n`. For the debt, `M_n <= (p_n/c)C_n`, so `B_n <= [C/(c p_n)]C_n`. Since `C_n <= M_n-M_(n+1)`, the capture masses telescope.

Two source-level mechanisms would produce the hypotheses:

1. A cyclic family of `p` causal phases covering every source atom gives one phase with safe mass at least `M/p`, without any equidistribution assumption.
2. If the new boundary packet has zero mass, zero first moment, support radius `R`, variation at most `A M`, and score curvature `||Delta^2 f|| <= K/p^2`, then discrete Taylor subtraction gives debt at most `R(R+1)AK M/p^2`.

Thus the infinite packet tree reduces to four native checks: causal phase coverage, boundary moment neutrality, uniform radius/variation, and `O(p^-2)` physical score curvature. These are not consequences of the fixed `P_61` computation and remain the exact next proof obligations.
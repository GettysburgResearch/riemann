# L-29806 — Hausdorff-jet amortized Pascal budget

Claim ID: `L-29806`  
Title: Pure-power Euler jets and exact remainders are decreasing Hausdorff moment sources; every ordered parity pair admits a capacity-feasible Pascal switch whose residual plus objective cost is at most the incoming source mass  
Status: **PROPOSED COMPLETE EXACT LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro-global`  
Created: 2026-08-08  
Issue: #298  
Dependencies: `L-29801`; PR #294 `L-28302`; elementary Laplace/Hausdorff moments  
Scope: corrected all-generation boundary invariant; uses the actual paired coefficients rather than imposing the special eta weights

## 1. Pure powers are Hausdorff moment sequences

Fix `s>0`, `x>0`, and step `h>0`. Put

\[
 v_j=(x+jh)^{-s},
 \qquad j\ge0.
\]

The Laplace formula gives

\[
 v_j
 ={1\over\Gamma(s)}
 \int_0^\infty
 t^{s-1}e^{-xt}(e^{-ht})^jdt.
\tag{L-29806.1}

After `y=e^{-ht}`,

\[
\boxed{
 v_j=\int_{[0,1]}y^j\,d\nu(y)
}
\tag{L-29806.2}

for one finite positive measure `nu`. Therefore

\[
\boxed{
 \Delta^mv_j
 =\int_{[0,1]}y^j(1-y)^m\,d\nu(y)
 \ge0,
}
\tag{L-29806.3}

and the sequence is decreasing in `j`.

## 2. Exact Euler remainder is positive and decreasing

For one finite-difference order `m`, define

\[
 R_K^{(m)}
 =\sum_{j\ge K}(-1)^{j-K}\Delta^mv_j.
\tag{L-29806.4}

Summing the geometric series under the positive integral gives

\[
\boxed{
 R_K^{(m)}
 =\int_{[0,1]}
 {y^K(1-y)^m\over1+y}\,d\nu(y)
 \ge0.
}
\tag{L-29806.5}

It is decreasing in `K`. These conclusions are preserved under nonnegative superposition over stopped endpoints, exponents, Taylor orders, Peano parameters, and common arithmetic destinations.

## 3. General ordered parity pair

Let `A_k,B_k` be the **actual recombined source coefficients** on the paired parity nodes `2k,2k+1`, and assume

\[
 A_k\ge B_k\ge0.
\tag{L-29806.6}

No special factorization

\[
 A_k=(2k)^{-1}V_e,
 \qquad
 B_k=(2k+1)^{-1}V_o
\]

is required. The eta comb of PR #294 is one special case.

The exact decomposition is

\[
\boxed{
 A_ke_{2k}-B_ke_{2k+1}
 =(A_k-B_k)e_{2k}+B_k(e_{2k}-e_{2k+1}).
}
\tag{L-29806.7}

The residual coefficient and the sibling-switch coefficient are both nonnegative. The dipole is the exact balanced Pascal switch of PR #294.

## 4. Amortized source-plus-cost inequality

The switch objective cost is

\[
 \operatorname{cost}_k
 =B_k\log{2k+1\over2k}.
\tag{L-29806.8}

Since `log((2k+1)/(2k))<1`,

\[
\boxed{
 (A_k-B_k)+\operatorname{cost}_k
 =A_k-B_k\left(1-\log{2k+1\over2k}\right)
 \le A_k.
}
\tag{L-29806.9}

Thus

```text
residual source mass
+
paid logarithmic Pascal cost
<=
incoming even source coefficient.
```

This is the source invariant used below.

## 5. Actual shifted cutoff coefficients are ordered

In PR #286's cutoff ledger the shifted-even argument is smaller than the paired unshifted-odd argument:

\[
 2kq-1<(2k+1)q.
\tag{L-29806.10}

For the base pure-power channel this directly gives

\[
 (2kq-1)^{-s}>((2k+1)q)^{-s}.
\]

After expanding the shift about `2kq`, every Taylor correction is a nonnegative **even-only** faster-power term. The unshifted base pair is ordered by monotonicity. Applying finite Euler transformation preserves the order because every finite-difference jet and exact remainder is a decreasing Hausdorff moment sequence by Sections 1–2.

Therefore, after common-destination recombination, the actual coefficients satisfy (L-29806.6) on the complete common tail.

The first omitted odd index can precede the shifted-even index by one. That single unmatched term per `(N,q)` is retained in the explicit collar of PR #286 and is not paired artificially.

## 6. Global telescoping budget

Let `J_a` be total positive boundary source mass entering cascade depth `a`, `C_a` the exact logarithmic cost of its Pascal switches, and `I_a` new source injected by the analytic bulk and collar.

Summing (L-29806.9) after common-destination recombination gives

\[
\boxed{
 J_{a+1}+C_a\le J_a+I_a.
}
\tag{L-29806.11}

Hence

\[
\boxed{
 J_A+\sum_{a<A}C_a
 \le J_0+\sum_{a<A}I_a.
}
\tag{L-29806.12}

No homogeneous boundary contraction factor is required.

PR #286 gives

\[
 A_{a+1}\le{6\over7}A_a
\]

for the analytic state and a fixed-order polylogarithmic collar bound. Therefore

\[
 \sum_a I_a=O(\log^B(2X))
\tag{L-29806.13}

through the `O(log X)` half-scale depth, and (L-29806.12) gives a polylogarithmic total residual source plus accumulated Pascal objective cost.

## 7. Corrected source graph

```text
analytic bulk
  -> strictly contracted analytic bulk
     + new positive boundary source;

boundary source
  -> positive lower-scale residual source
     + paid Pascal cost,
     with residual+cost <= incoming source.
```

Boundary source does not regenerate current-scale analytic bulk. Its residual may persist, but it carries a finite conserved budget.

## 8. Proof boundary

Closed here, subject to independent reconstruction of the arithmetic destination map:

1. Hausdorff representation of pure-power jets;
2. positivity and monotonicity of exact Euler remainders;
3. general ordered-pair Pascal decomposition;
4. the local source-plus-cost inequality;
5. actual coefficient order on the common shifted/unshifted tail;
6. the global telescoping budget.

Open review point:

- verify every common-destination pairing, Taylor term, first-omitted convention, and unmatched collar row in the complete finite source manifest.

No RH conclusion is stated in this lemma.

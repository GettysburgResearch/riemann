# L-29806 — Hausdorff-jet amortized Pascal budget

Claim ID: `L-29806`  
Title: Pure-power Euler jets and exact remainders are decreasing Hausdorff moment sources; every unequal eta pair admits a capacity-feasible Pascal switch whose residual plus objective cost is at most the incoming source mass  
Status: **PROPOSED COMPLETE EXACT LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro-global`  
Created: 2026-08-08  
Issue: #298  
Dependencies: `L-29801`; PR #294 `L-28302`; elementary Laplace/Hausdorff moments  
Scope: corrected all-generation boundary invariant; supersedes the need for a uniform eta factor on arbitrary jet labels

## 1. Pure powers are Hausdorff moment sequences

Fix `s>0`, `x>0`, and step `h>0`.  Put

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

After the substitution `y=e^{-ht}`, this is a Hausdorff moment representation

\[
\boxed{
 v_j=\int_{[0,1]}y^j\,d\nu(y)
}
\tag{L-29806.2}

for one finite positive measure `nu`.

Therefore every finite difference is again a Hausdorff moment sequence:

\[
\boxed{
 \Delta^mv_j
 =\int_{[0,1]}y^j(1-y)^m\,d\nu(y)
 \ge0.
}
\tag{L-29806.3]

In particular it is decreasing in `j`.

## 2. Exact Euler remainder is positive and decreasing

For one finite-difference order `m`, define the exact alternating remainder

\[
 R_K^{(m)}
 =\sum_{j\ge K}(-1)^{j-K}\Delta^mv_j.
\tag{L-29806.4]

Using (L-29806.3) and summing the geometric series under the positive integral,

\[
\boxed{
 R_K^{(m)}
 =\int_{[0,1]}
 {y^K(1-y)^m\over1+y}\,d\nu(y)
 \ge0.
}
\tag{L-29806.5]

It is also decreasing in `K`.

Thus every finite Euler jet and every exact remainder from a pure-power source is not merely positive: it is a positive decreasing source along the paired quotient index.

The result is preserved by nonnegative superposition over endpoints, exponents, Peano parameters, and common arithmetic destinations.

## 3. Unequal eta pair

Let `V_e,V_o>=0` be the internal source masses on one even/odd eta pair, and assume only

\[
 V_e\ge V_o.
\tag{L-29806.6]

Put

\[
 a_k={1\over2k},
 \qquad
 c_k={1\over2k+1},
 \qquad
 \ell_k=\log{2k+1\over2k}.
\]

The signed pair is

\[
 a_kV_e e_{2k}-c_kV_oe_{2k+1}.
\]

Since `a_k>c_k` and `V_e>=V_o`, the switch amount

\[
 T_k=c_kV_o
\tag{L-29806.7]

is below the available central source

\[
 M_k=a_kV_e.
\]

Hence

\[
\boxed{
 a_kV_e e_{2k}-c_kV_oe_{2k+1}
 =(M_k-T_k)e_{2k}+T_k(e_{2k}-e_{2k+1}),
}
\tag{L-29806.8]

with nonnegative residual `M_k-T_k`.  The dipole is realized by the same balanced sibling switch as in PR #294.

This formula does not require the even and odd internal labels to be identical.  It requires only the monotone source inequality (L-29806.6).

## 4. Amortized mass-plus-cost inequality

The exact objective cost of the switch is

\[
 \operatorname{cost}_k=T_k\ell_k.
\]

Because `ell_k<1`,

\[
\boxed{
 (M_k-T_k)+\operatorname{cost}_k
 =M_k-T_k(1-\ell_k)
 \le M_k.
}
\tag{L-29806.9]

Thus

```text
residual source mass
+
paid logarithmic Pascal cost
<=
incoming even source mass.
```

The inequality is strict whenever `T_k>0`, but no uniform strict factor is needed.

Summing over all pairs and all common internal labels preserves (L-29806.9).  Repeated destinations are combined before the inequality, so one source unit is never spent twice.

## 5. Application to shifted cutoff jets

In PR #286's first-omitted ledger, the even argument is smaller than the paired odd argument:

\[
 2kq-1<(2k+1)q.
\]

Every pure-power finite difference and exact Euler remainder is decreasing by Sections 1--2.  Therefore its even internal source mass is at least its odd internal source mass.

Equation (L-29806.8) applies to every:

- shifted or unshifted first-omitted value jet;
- finite-difference Peano jet;
- exact Euler remainder;
- positive stopped-power endpoint component.

This supplies the unequal-label source binding missing from the literal tensor statement in `L-29802`.

## 6. Global telescoping budget

Let `J_a` be the total positive boundary source mass entering cascade depth `a`, and let `C_a` be the logarithmic objective cost paid by the corresponding Pascal switches.  Let `J_(a+1)` be the total residual boundary source passed to the next half endpoint.

Summing (L-29806.9) gives

\[
\boxed{
 J_{a+1}+C_a\le J_a+I_a,
}
\tag{L-29806.10]

where `I_a` is newly injected boundary source from the analytic bulk and the finite collar.

Iteration yields the exact amortized estimate

\[
\boxed{
 J_A+\sum_{a<A}C_a
 \le J_0+\sum_{a<A}I_a.
}
\tag{L-29806.11]

No homogeneous boundary contraction factor is required.

PR #286's analytic state satisfies `A_(a+1)<=(6/7)A_a`, and its boundary injection obeys

\[
 I_a\le C_MA_a+\operatorname{poly}(a,\log X).
\]

Hence

\[
 \sum_a I_a=O(\log^B(2X))
\tag{L-29806.12]

through the `O(log X)` cascade depth.  Equation (L-29806.11) gives a polylogarithmic total boundary source plus accumulated Pascal objective cost.

## 7. Corrected source graph

The all-generation state is triangular in the following amortized sense:

```text
analytic bulk
  -> strictly contracted analytic bulk
     + new positive boundary source;

boundary source
  -> positive lower-scale residual source
     + paid Pascal cost,
     with residual+cost <= incoming source.
```

Boundary source does not regenerate current-scale analytic bulk.  Its residual may persist, but it carries a finite conserved budget and cannot create exponential or polynomial debt.

This is stronger and safer than assigning one uniform `theta_*` to every unequal jet pair.

## 8. Proof boundary

Closed here, subject to independent verification of the exact arithmetic destination map:

1. Hausdorff moment representation of every pure-power jet;
2. positivity and monotonicity of every exact Euler remainder;
3. capacity feasibility for unequal even/odd source labels;
4. the local residual-plus-cost inequality;
5. the global telescoping boundary budget;
6. the polylogarithmic conclusion after analytic injection.

Open review point:

- verify that every emitted finite cutoff row pairs the declared smaller even argument with the declared larger odd argument after all quotient and endpoint coincidences are recombined.

No RH conclusion is stated in this lemma.

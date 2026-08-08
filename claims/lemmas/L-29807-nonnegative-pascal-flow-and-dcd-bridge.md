# L-29807 — Nonnegative Pascal flow and the DCD bridge

Claim ID: `L-29807`  
Title: Every paired Hausdorff eta tail is realized by nonnegative central/sibling edge coefficients and contributes zero negative capacity debt; only the explicit unmatched collar enters DCD  
Status: **PROPOSED COMPLETE SOURCE-TO-FLOW LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro-global`  
Created: 2026-08-08  
Issue: #298  
Dependencies: `L-29806`; PR #294 `L-28302`; PR #272 `L-27204/L-27205/L-27207`  
Scope: exact bridge from the amortized boundary source to the Cycle-Debt metric

## 1. One paired source event

Let one common arithmetic/Peano destination carry source values

\[
 V_e\ge V_o\ge0
\]

on the paired eta nodes `2k,2k+1`. Put

\[
 M={V_e\over2k},
 \qquad
 T={V_o\over2k+1}.
\tag{L-29807.1}

Then `0<=T<=M` by `L-29806`.

At parent `4k`, let

\[
 c_k=[4k,2k]
\]

be the central split and

\[
 s_k=[4k,2k-1]
\]

its nearest balanced sibling. PR #294 gives

\[
 \chi_{s_k}(q)-\chi_{c_k}(q)
 =\mathbf1_{q\mid2k}-\mathbf1_{q\mid2k+1}.
\tag{L-29807.2}

The exact nonnegative edge assignment is

\[
\boxed{
 d_k=(M-T)c_k+Ts_k.
}
\tag{L-29807.3}

Both coefficients are nonnegative.

Relative to the incoming central assignment `M c_k`, the carry-column change is

\[
 T(\chi_{s_k}-\chi_{c_k}),
\]

which is exactly the source dipole in `L-29806`.

## 2. Zero negative capacity debt

PR #272's negative capacity debt is

\[
 \mathcal N_\omega(d)
 =\sum_e\omega_e(-d_e)_+.
\]

Since `d_k` has no negative coefficient,

\[
\boxed{
 \mathcal N_\omega(d_k)=0.
}
\tag{L-29807.4}

Thus the complete common paired Hausdorff tail is not merely bounded in the Cycle-Debt metric. It contributes no negative capacity debt at all.

Repeated destinations are added before the edge coefficients are formed. Nonnegative sums preserve (L-29807.4).

## 3. Exact objective ledger

The central-to-sibling replacement loses

\[
\boxed{
 \operatorname{cost}_k
 =T\log{2k+1\over2k}.
}
\tag{L-29807.5}

`L-29806` proves

\[
 (M-T)+\operatorname{cost}_k\le M.
\tag{L-29807.6}

Hence the incoming central source pays both the residual source passed to the next half endpoint and the complete entropy/von-Mangoldt objective loss.

The capacity and objective ledgers are therefore separated correctly:

```text
paired tail negative capacity debt = 0;
paired tail objective loss         <= incoming source mass;
residual positive source           = M-T.
```

## 4. Common-tail flow

Sum (L-29807.3) over all eta indices, jet labels, stopped-power endpoints, and common arithmetic destinations. The resulting flow `d_tail` is coefficientwise nonnegative and realizes the complete paired-tail carry source.

Therefore

\[
\boxed{
 \mathcal N_\omega(d_{\rm tail})=0.
}
\tag{L-29807.7}

Its total objective loss is bounded by the amortized source budget of `L-29806`.

## 5. Unmatched collar

The first omitted shifted-even and unshifted-odd indices can differ by one. These unmatched initial terms, endpoint coincidences, zero-extension rows, and the finite analytic threshold are retained in the collar `J_N^(M)` of PR #286 `L-28402`.

That lemma proves a polylogarithmic first-generation capacity bound

\[
 \operatorname{Cap}(J_N^{(M)})
 \le C_M(1+\log N)^{M+2}.
\tag{L-29807.8}

Realize the collar by its declared balanced flow and call its negative capacity debt `D_collar(N)`. Since negative debt is bounded by total capacity,

\[
\boxed{
 D_{\rm collar}(N)
 \le C_M(1+\log N)^{M+2}.
}
\tag{L-29807.9}

No unmatched row is discarded.

## 6. DCD excess

Take an exact lower flow `d_Y` at endpoint `Y`. Apply the exact doubled lift of PR #272 `L-27207`, then replace the complete common odd-commutator tail by the nonnegative paired flow `d_tail` and add the declared collar flow.

The doubled lower part contributes exactly

\[
 {1\over2}\mathcal N_\omega(d_Y)
\]

plus the odd channel which is canceled by the paired source construction. The bottom coefficient is positive and cannot increase negative debt. The paired tail has zero debt by (L-29807.7). Therefore

\[
\boxed{
 \mathfrak E_\eta(Y;d_Y)
 \le D_{\rm collar}(2Y)
 =O(\log^{M+2}(2Y)).
}
\tag{L-29807.10}

This is exactly the Dyadic Commutator Debt estimate `T-27203.4`, with an explicit fixed logarithmic exponent.

## 7. Cycle Debt and objective

The DCD recurrence gives polylogarithmic optimized negative capacity debt. Separately, the amortized source ledger gives a polylogarithmic cumulative objective loss. Both are required by the balanced entropy consumer:

- capacity feasibility is supplied by (L-29807.10);
- the sharp `4 sqrt(X)` objective is preserved by (L-29806.11).

Thus no metric is silently substituted for another.

## 8. Decisive review hinge

The source-to-flow conclusion is rejected if any common paired cutoff source fails one of:

1. `V_e>=V_o`;
2. `T<=M`;
3. the carry image (L-29807.2);
4. coefficientwise nonnegativity of (L-29807.3);
5. inclusion of every unmatched first term in the collar;
6. compatibility of the emitted sibling edge with the fixed balanced edge space of PR #272.

One exact counterexample is sufficient.

## 9. Proof boundary

Closed here, subject to the complete source manifest:

1. nonnegative edge realization of every paired tail;
2. zero paired-tail negative capacity debt;
3. exact objective loss;
4. polylog collar debt;
5. DCD excess bound.

This lemma does not independently reprove the downstream square-screw/Landau consumer.

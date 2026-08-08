# L-29807 — Nonnegative Pascal flow and the DCD bridge

Claim ID: `L-29807`  
Title: Every ordered Hausdorff parity tail is realized by nonnegative central/sibling edge coefficients and contributes zero negative capacity debt; only the explicit unmatched collar enters DCD  
Status: **PROPOSED COMPLETE SOURCE-TO-FLOW LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro-global`  
Created: 2026-08-08  
Issue: #298  
Dependencies: `L-29806`; PR #294 `L-28302`; PR #272 `L-27204/L-27205/L-27207`  
Scope: exact bridge from the amortized boundary source to the Cycle-Debt metric

## 1. One paired source event

Let one common arithmetic/Peano destination carry the actual recombined source coefficients

\[
 A_k\ge B_k\ge0
\]

on parity nodes `2k,2k+1`.

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
\tag{L-29807.1}

The exact nonnegative edge assignment is

\[
\boxed{
 d_k=(A_k-B_k)c_k+B_ks_k.
}
\tag{L-29807.2}

Both coefficients are nonnegative. Relative to the incoming central assignment `A_k c_k`, the carry-column change is

\[
 B_k(\chi_{s_k}-\chi_{c_k}),
\]

which is exactly the source dipole

\[
 A_ke_{2k}-B_ke_{2k+1}
 =(A_k-B_k)e_{2k}+B_k(e_{2k}-e_{2k+1}).
\]

No special eta normalization is imposed on `A_k,B_k`.

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
\tag{L-29807.3}

Thus the complete common paired Hausdorff tail contributes no negative capacity debt.

Repeated destinations are added before the edge coefficients are formed. Nonnegative sums preserve (L-29807.3).

## 3. Exact objective ledger

The central-to-sibling replacement loses

\[
\boxed{
 \operatorname{cost}_k
 =B_k\log{2k+1\over2k}.
}
\tag{L-29807.4}

`L-29806` proves

\[
 (A_k-B_k)+\operatorname{cost}_k\le A_k.
\tag{L-29807.5}

Hence the incoming central source pays both the residual source passed to the next half endpoint and the complete entropy/von-Mangoldt objective loss.

```text
paired tail negative capacity debt = 0;
paired tail objective loss         <= incoming source mass;
residual positive source           = A_k-B_k.
```

## 4. Common-tail flow

Sum (L-29807.2) over all parity indices, jet labels, stopped-power endpoints, and common arithmetic destinations. The resulting flow `d_tail` is coefficientwise nonnegative and realizes the complete paired-tail carry source. Therefore

\[
\boxed{
 \mathcal N_\omega(d_{\rm tail})=0.
}
\tag{L-29807.6}

Its total objective loss is bounded by the amortized source budget of `L-29806`.

## 5. Unmatched collar

The first omitted shifted-even and unshifted-odd indices can differ by one. These unmatched initial terms, endpoint coincidences, zero-extension rows, and the finite analytic threshold are retained in the collar `J_N^(M)` of PR #286 `L-28402`.

That lemma proves a polylogarithmic first-generation capacity bound

\[
 \operatorname{Cap}(J_N^{(M)})
 \le C_M(1+\log N)^{M+2}.
\tag{L-29807.7}

Realize the collar by its declared balanced flow and call its negative capacity debt `D_collar(N)`. Since negative debt is bounded by total capacity,

\[
\boxed{
 D_{\rm collar}(N)
 \le C_M(1+\log N)^{M+2}.
}
\tag{L-29807.8}

No unmatched row is discarded.

## 6. DCD excess

Take an exact lower flow `d_Y` at endpoint `Y`. Apply the exact doubled lift of PR #272 `L-27207`, replace the complete common odd-commutator tail by the nonnegative paired flow `d_tail`, and add the declared collar flow.

The doubled lower part contributes exactly

\[
 {1\over2}\mathcal N_\omega(d_Y)
\]

plus the odd channel realized by the paired source construction. The bottom coefficient is positive and cannot increase negative debt. The paired tail has zero debt by (L-29807.6). Therefore

\[
\boxed{
 \mathfrak E_\eta(Y;d_Y)
 \le D_{\rm collar}(2Y)
 =O(\log^{M+2}(2Y)).
}
\tag{L-29807.9}

This is exactly the Dyadic Commutator Debt estimate `T-27203.4`, with an explicit fixed logarithmic exponent.

## 7. Cycle Debt and objective

The DCD recurrence gives polylogarithmic optimized negative capacity debt. Separately, the amortized source ledger gives a polylogarithmic cumulative objective loss. Both are required by the balanced entropy consumer:

- capacity feasibility is supplied by (L-29807.9);
- the sharp `4 sqrt(X)` objective is preserved by (L-29806.12).

Thus no metric is silently substituted for another.

## 8. Decisive review hinge

The source-to-flow conclusion is rejected if any common paired cutoff source fails one of:

1. `A_k>=B_k>=0`;
2. the carry image (L-29807.1);
3. coefficientwise nonnegativity of (L-29807.2);
4. inclusion of every unmatched first term in the collar;
5. compatibility of the emitted sibling edge with the fixed balanced edge space of PR #272;
6. exact reproduction of the odd commutator channel in the doubled divergence ledger.

One exact counterexample is sufficient.

## 9. Proof boundary

Closed here, subject to the complete source manifest:

1. nonnegative edge realization of every ordered paired tail;
2. zero paired-tail negative capacity debt;
3. exact objective loss;
4. polylog collar debt;
5. DCD excess bound.

This lemma does not independently reprove the downstream square-screw/Landau consumer.

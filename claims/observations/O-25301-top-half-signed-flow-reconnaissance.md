# O-25301 — Top-half signed-flow reconnaissance

Observation ID: `O-25301`  
Title: A nonnegative adjacent flow supported in the top half repairs every tested parabolic-seed constraint at a cost near `X^-3/2`  
Status: **FLOATING RECONNAISSANCE — NOT A CERTIFICATE OR ASYMPTOTIC THEOREM**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #253  
Dependencies: `L-25301`; SciPy/HiGHS discovery arithmetic

## 1. Finite discovery problem

For the parabolic seed, restrict the adjacent-flow variables to

\[
0.45X\le j<X,
\qquad
F_j\ge0.
\]

Minimize the exact formal objective

\[
\sum_j F_j\log\frac{j^2}{j^2-1}
\]

subject to

\[
b_X^{(0)}(m)+F_{m-1}-F_m\ge0
\]

and every complete prime-power inequality

\[
v_q(b_F)\le q^{-1/2}\log(X/q).
\]

This is a finite LP. The solver is used only for discovery.

## 2. Reconnaissance

Sparse SciPy/HiGHS runs gave:

```text
X       minimum flow cost       X^(3/2) cost       active variables
1000    1.60215358e-6           0.0506645           128
2000    5.33483996e-7           0.0477163           234
5000    1.28374466e-7           0.0453872           564
10000   5.48019600e-8           0.0548020          1077
```

Every reported solve had:

```text
maximum constraint violation <= ordinary solver tolerance
minimum repaired b coordinate >= ordinary solver tolerance
```

The flows are concentrated at highly composite integers in the upper support.
Their neighboring integers often carry large prime or prime-power factors in
the outer negative-slack region.

## 3. Contrast with the refuted monotone cover

At the same scales, the monotone-cover optimum from `O-24501` is approximately

```text
X=1000     4.7683
X=2000     8.0161
X=5000    14.7403
X=10000   22.4909
```

`R-25301` proves this cost is asymptotically `Omega(sqrt(X))`.

The adjacent flow is therefore not a numerical reformulation of the monotone
cover. It uses the negative constraint slack and the signed
`j-1,j,j+1` divisor ledger.

## 4. Candidate theorem

The reconnaissance nominates the much stronger finite statement:

> For every sufficiently large `X`, there is a nonnegative flow supported in
> `[cX,X]`, for one fixed `c<1`, such that every repaired coordinate and every
> prime-power constraint is nonnegative/feasible, while the exact objective
> cost is `X^{-3/2+o(1)}`.

Even the weaker `X^epsilon` bound of `T-25301` would prove RH.

The observed rate is not claimed. A rigorous proof must construct the flow
without trusting an LP solver and must explain the balanced primitive-neighbor
edges which transfer the macroscopic defect into outer slack.

## 5. Proof boundary

The script `experiments/X-25301-parabolic-cover-dual/recon_top_flow.py`
reproduces the floating LP. It is not included in the exact SHA-bound proof
object and imports NumPy/SciPy.

No numerical row in this observation is evidence for RH.

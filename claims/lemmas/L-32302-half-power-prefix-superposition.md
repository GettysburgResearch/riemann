# L-32302 — Positive superposition of stopped half-power targets

Claim ID: `L-32302`  
Title: The critical logarithmic carry target is an exact positive superposition of static stopped half-power targets, and Cycle Debt is subadditive under that superposition  
Status: **PROPOSED COMPLETE EXACT REDUCTION — independent review requested**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: PR #272 `L-27205`; finite LP homogeneity  
Scope: exact reduction of the critical logarithmic Cycle Debt to a one-parameter family of static targets

## 1. Static half-power targets

For an integer endpoint `Q>=2`, define

\[
\boxed{
p_Q(q)=q^{-1/2}\mathbf 1_{2\le q\le Q}.
}
\tag{L-32302.1}
\]

Let

\[
\mathfrak N_\eta[p_Q]
\]

denote the optimized weighted negative capacity debt of PR #272 for this target, using exactly the same balanced split family and edge capacity weights.

No logarithmic endpoint factor occurs in `p_Q`.

## 2. Exact positive logarithmic layer cake

For `2<=q<=X`, finite telescoping gives

\[
\sum_{Q=q}^{X-1}\log\frac{Q+1}{Q}
=\log\frac Xq.
\]

Therefore the critical target satisfies the exact identity

\[
\boxed{
 w_X
 =\sum_{Q=2}^{X-1}
 \lambda_Q p_Q,
 \qquad
 \lambda_Q=\log\frac{Q+1}{Q}>0.
}
\tag{L-32302.2}
\]

This is an identity of finite carry-column vectors.  It is not an asymptotic integral and does not differentiate a Mellin exponent.

The same identity can be checked without transcendental arithmetic by exponentiating each coordinate:

\[
\prod_{Q=q}^{X-1}\frac{Q+1}{Q}=\frac Xq.
\]

## 3. Positive superposition of exact flows

For each `Q`, let `d_Q` be any exact balanced signed flow for `p_Q`, embedded into endpoint `X` by extending it by zero on edges with parent greater than `Q`.

Then

\[
\boxed{
 d_X:=\sum_{Q=2}^{X-1}\lambda_Q d_Q
}
\tag{L-32302.3}
\]

is an exact balanced signed flow for `w_X`, by linearity of every carry column.

For any edge coefficient family and nonnegative scalars,

\[
\left[-\sum_Q\lambda_Q d_Q(e)\right]_+
\le
\sum_Q\lambda_Q[-d_Q(e)]_+.
\]

The edge capacity weight is endpoint independent once the edge is fixed. Hence

\[
\boxed{
\mathfrak N_\eta[w_X]
\le
\sum_{Q=2}^{X-1}
\lambda_Q\mathfrak N_\eta[p_Q].
}
\tag{L-32302.4}
\]

Equation (L-32302.4) is an exact primal statement.  No duality or existence theorem is needed beyond the finite minima already defining Cycle Debt.

## 4. Polylogarithmic half-power debt is sufficient

Assume that for some fixed constants `A,C`,

\[
\boxed{
\mathfrak N_\eta[p_Q]
\le C(1+\log Q)^A
\qquad(Q\ge2).
}
\tag{L-32302.5}
\]

Since

\[
0<\log\frac{Q+1}{Q}\le\frac1Q,
\]

we obtain

\[
\begin{aligned}
\mathfrak N_\eta[w_X]
&\le
C\sum_{Q=2}^{X-1}
\frac{(1+\log Q)^A}{Q}\\
&\le C_A(1+\log X)^{A+1}.
\end{aligned}
\tag{L-32302.6}
\]

Thus a polylogarithmic theorem for the single static family `p_Q` proves polylogarithmic Cycle Debt for the complete critical logarithmic target.

The same argument works with any uniform `Q^{o(1)}` estimate strong enough that the weighted sum in (L-32302.4) is `X^{o(1)}`.

## 5. Why this changes the research problem

The previous boundary-cascade approaches propagate the full target

\[
q^{-1/2}\log(X/q)
\]

through every endpoint activation.  Equation (L-32302.2) permits a different order:

```text
first resolve the logarithm positively;
solve the static stopped half-power problem at each endpoint;
only then superpose the completed flows.
```

Consequently no proof of `L-32302.5` needs to propagate a logarithmic Jordan companion.  It may exploit exact factor-two/factor-five self-similarity of the pure half-power source directly.

This does not make (L-32302.5) automatic.  It identifies a strictly simpler source family whose debt is the only new quantitative theorem needed by this route.

## 6. Proof boundary

Closed exactly:

1. the positive stopped-half-power decomposition of `w_X`;
2. embedding of each finite exact flow into the common endpoint;
3. convexity/subadditivity of weighted negative debt;
4. the polylogarithmic summation bound.

Open:

1. a polylogarithmic bound for `mathfrak N_eta[p_Q]`;
2. the resulting critical Cycle Debt theorem;
3. RH.

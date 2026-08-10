# L-90029 — Radix-four detail packing has a positive target and positive endpoint atoms

Claim ID: `L-90029` (provisional range; branch-qualified)  
Title: Applying the critical radix-four detail to both the carry target and the endpoint response matrix produces a completely positive triangular packing problem; detail feasibility telescopes exactly to ordinary carry feasibility  
Status: **PROPOSED COMPLETE EXACT FINITE REDUCTION / POSITIVE GREEDY THEOREM — SCORE ESTIMATE OPEN**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-10  
Depends on: PR #265 `L-26201/L-26203`; PR #353 `L-90023`; `L-90027`  
Scope: exact finite positive packing coordinates and RH consumer; the signed score-loss estimate remains open

## 1. Positive radix-four target

Retain

\[
 w_X(q)=q^{-1/2}\log{X\over q}\,\mathbf1_{q\le X}.
\]

Define the critical radix-four detail

\[
\boxed{
 \Omega_X(q)=w_X(q)-2w_X(4q).
}
\tag{L-90029.1}

With zero extension this is explicitly

\[
\boxed{
 \Omega_X(q)=
 \begin{cases}
 {\log4\over\sqrt q},&4q\le X,\\[1mm]
 {1\over\sqrt q}\log{X\over q},&q\le X<4q,\\[1mm]
 0,&q>X.
 \end{cases}}
\tag{L-90029.2}

Thus

\[
\boxed{
 \Omega_X(q)>0\qquad(2\le q\le X).
}
\tag{L-90029.3}

The entire interior target is scale-stationary after critical normalization.

## 2. Positive endpoint details

Let `a_T` be the nonnegative endpoint row atom of PR #265, with carry response

\[
 \Gamma_T(q)=\sum_na_T(n)\beta_{nq}.
\]

Define

\[
\boxed{
 \Xi_T(q)=\Gamma_T(q)-2\Gamma_T(4q).
}
\tag{L-90029.4}

`L-90027` proves

\[
\boxed{
 \Xi_T(q)>0\qquad(2\le q<T),
 \qquad
 \Xi_T(q)=0\qquad(q\ge T).
}
\tag{L-90029.5}

So the detail-response matrix is strictly positive below the diagonal and exactly triangular above it, just like the original endpoint matrix but now paired with the much simpler target (L-90029.2).

## 3. Exact radix-four telescoping

For every finitely supported sequence `f(q)`, put

\[
 (\mathcal D_4f)(q)=f(q)-2f(4q).
\]

Then

\[
\boxed{
 f(q)=\sum_{j\ge0}2^j(\mathcal D_4f)(4^jq),
}
\tag{L-90029.6}

where the sum is finite. Indeed the partial sum through `J` is

\[
 f(q)-2^{J+1}f(4^{J+1}q).
\]

Applying (L-90029.6) to the target and each endpoint atom gives

\[
\boxed{
 w_X(q)=\sum_{j\ge0}2^j\Omega_X(4^jq),
}
\tag{L-90029.7}

and

\[
\boxed{
 \Gamma_T(q)=\sum_{j\ge0}2^j\Xi_T(4^jq).
}
\tag{L-90029.8}

These are exact finite identities, not asymptotic renewal formulas.

## 4. Detail feasibility implies ordinary feasibility

Let `lambda_T>=0` and assume

\[
\boxed{
 \sum_{T=3}^{X}\lambda_T\Xi_T(q)
 \le\Omega_X(q)
 \qquad(2\le q\le X).
}
\tag{L-90029.9}

Then (L-90029.7)--(L-90029.8), with nonnegative coefficients `2^j`, give

\[
\begin{aligned}
 \sum_T\lambda_T\Gamma_T(q)
 &=\sum_{j\ge0}2^j
   \sum_T\lambda_T\Xi_T(4^jq)\\
 &\le\sum_{j\ge0}2^j\Omega_X(4^jq)
 =w_X(q).
\end{aligned}
\]

Hence

\[
\boxed{
 \text{radix-four detail feasibility}
 \Longrightarrow
 \text{ordinary carry feasibility}.
}
\tag{L-90029.10}

The corresponding row vector

\[
 d_X^{(4)}(n)=\sum_T\lambda_Ta_T(n)
\]

is automatically nonnegative.

## 5. Exact slack dictionary

Define the detail slack

\[
 \delta_X(q)=\Omega_X(q)-\sum_T\lambda_T\Xi_T(q)\ge0
\]

and the ordinary carry slack

\[
 s_X(q)=w_X(q)-\sum_T\lambda_T\Gamma_T(q).
\]

Equations (L-90029.7)--(L-90029.8) give

\[
\boxed{
 s_X(q)=\sum_{j\ge0}2^j\delta_X(4^jq)\ge0.
}
\tag{L-90029.11}

Thus no information is lost in passing to detail coordinates; ordinary slack is the positive radix-four renewal of detail slack.

## 6. Canonical positive detail greedy

Initialize

\[
 \rho^{(X+1)}(q)=\Omega_X(q).
\]

For `T=X,X-1,...,3`, define

\[
\boxed{
 \lambda_T^{(4)}
 =\min_{2\le q<T}
 {\rho^{(T+1)}(q)\over\Xi_T(q)}
}
\tag{L-90029.12}

and update

\[
 \rho^{(T)}(q)
 =\rho^{(T+1)}(q)-\lambda_T^{(4)}\Xi_T(q).
\tag{L-90029.13}

Every denominator is positive by (L-90029.5); therefore every weight and every residual is nonnegative. The output is detail feasible, and hence ordinary feasible by Section 4.

The same contiguous-freeze law as PR #265 holds. If a minimizer `q_T<T-1` becomes zero, then

\[
 \lambda_U^{(4)}=0
 \qquad(q_T<U<T),
\]

because every later active detail atom has `Xi_U(q_T)>0`.

The diagonal is unchanged by the detail transform:

\[
\boxed{
 \Xi_T(T-1)=\Gamma_T(T-1).
}
\tag{L-90029.14}

Consequently the exact diagonal slack and the `q^{-3/2}` diagonal estimates of `L-26203` carry over verbatim.

## 7. The correct conclusion-producing scalar

Let

\[
 H_T=\sum_na_T(n)G_n
\]

be the exact endpoint entropy score. The unweighted parabolic seed satisfies

\[
 J_\Lambda(X)=\sum_{T=3}^{X}H_T.
\]

For any detail-feasible weights define the signed seed-score loss

\[
\boxed{
 \mathfrak L_X^{(4)}
 =\sum_{T=3}^{X}(1-\lambda_T)H_T.
}
\tag{L-90029.15}

By Section 4 the associated row packing is ordinarily feasible. PR #353 `L-90023` therefore gives

\[
 F_\Lambda(X)\le\mathfrak L_X^{(4)}.
\tag{L-90029.16}

It follows that either of the estimates

\[
\boxed{
 \mathfrak L_X^{(4)}=o(\log^2X)
}
\tag{L-90029.17}

or, more generally,

\[
\boxed{
 \limsup_{X\to\infty}
 {\mathfrak L_X^{(4)}\over\log^2X}
 <{-1-\zeta(1/2)\over4}
}
\tag{L-90029.18}

implies RH.

Weights above one are permitted and contribute favorable negative score loss. The target is not unsigned detail slack; it is the signed score (L-90029.15).

## 8. Why this coordinate is materially simpler

The original endpoint matrix had a positive kernel but an oscillatory residual target. The new system has

```text
positive endpoint atoms Xi_T(q);
positive target Omega_X(q);
constant interior target log(4)/sqrt(q);
triangular support;
contiguous blocker intervals;
exact positive reconstruction of the original columns;
the same conclusion-producing entropy score.
```

Moreover:

- `L-90025/L-90026` identify the continuum atom as a positive factor-four block with a Gamma martingale;
- `L-90028` constructs a lossless state-dependent continuum transport from that block to the exact target law;
- `L-90027` supplies the matching finite positive packet.

The remaining theorem is therefore a finite discretization/lift estimate, not a missing sign in the local matrix.

## 9. Named closing target

> **Radix-Four Detail Score Loss (`R4DSL`).** For the canonical detail greedy
> (L-90029.12), or for another explicitly constructed nonnegative detail-feasible
> weight vector, prove
> \[
> \mathfrak L_X^{(4)}=o(\log^2X).
> \]

`R4DSL` implies RH by Section 7.

## 10. Proof boundary

Closed exactly, subject to independent review:

1. positivity and explicit form of the transformed target;
2. positivity of the transformed endpoint matrix;
3. exact radix-four telescoping;
4. detail-feasibility-to-carry-feasibility implication;
5. exact slack dictionary;
6. the positive detail greedy and freeze law;
7. the signed score-loss RH consumer.

Still open:

1. `R4DSL`;
2. a finite realization of the continuum monotone coupling with subquadratic score loss;
3. the factor-64 endpoint inequality;
4. RH.

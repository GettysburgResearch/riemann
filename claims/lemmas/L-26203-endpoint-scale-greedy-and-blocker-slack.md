# L-26203 — Endpoint-scale greedy packing and exact blocker slack

Claim ID: `L-26203`  
Title: A backward greedy algorithm on the positive parabolic endpoint atoms gives a nonnegative carry packing with a contiguous scale-freeze law and an exact slack identity  
Status: **PROPOSED COMPLETE FINITE THEOREM PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Issue family: `#245/#262`  
Frozen base: PR #248 at `5f2b25f89afbb90a3bc4ca6d40148f530303eb54`  
Dependencies: `L-26201`; PR #244 `L-23705/L-23706`; PR #248 `L-24501`  
Scope: explicit finite nonnegative packing and exact slack ledger; no asymptotic slack estimate

## 1. Positive endpoint atoms

Fix an integer `X>=3`.  Let `a_T`, `Gamma_T`, and `H_T` be the positive
endpoint atoms, carry responses, and entropy scores of `L-26201`, for
`3<=T<=X`:

\[
 a_T(n)\ge0,
 \qquad
 \Gamma_T(q)=\sum_na_T(n)\beta_{nq},
 \qquad
 H_T=\sum_na_T(n)G_n.
\tag{L-26203.1}
\]

They satisfy

\[
 \Gamma_T(q)>0\quad(2\le q<T),
 \qquad
 \Gamma_T(q)=0\quad(q\ge T).
\tag{L-26203.2}
\]

Thus the scale-response matrix is strictly positive below its diagonal and
exactly triangular above it.

The unweighted choice

\[
 \lambda_T=1
\]

reconstructs the parabolic seed and already has entropy
`4 sqrt(X)-O(log X)`, but its column response is not feasible.  The goal is to
change only the nonnegative scale weights, never the signs of the carry rows.

## 2. Backward endpoint-scale greedy algorithm

Initialize

\[
 \rho^{(X+1)}(q)=w_X(q)
 =q^{-1/2}\log(X/q),
 \qquad 2\le q\le X.
\tag{L-26203.3}
\]

For `T=X,X-1,...,3`, define

\[
 \boxed{
 \lambda_T
 =\min_{2\le q<T}
  \frac{\rho^{(T+1)}(q)}{\Gamma_T(q)}.}
\tag{L-26203.4}
\]

All denominators are strictly positive by (L-26203.2).  Update

\[
 \rho^{(T)}(q)
 =\rho^{(T+1)}(q)-\lambda_T\Gamma_T(q)
 \qquad(2\le q<T),
\tag{L-26203.5}
\]

and leave the other columns unchanged.

Every residual and every scale weight is nonnegative.  The resulting row vector

\[
 \boxed{
 d_X^{\rm sc}(n)=\sum_{T=3}^X\lambda_Ta_T(n)}
\tag{L-26203.6}
\]

therefore satisfies

\[
 \boxed{
 d_X^{\rm sc}(n)\ge0,
 \qquad
 \sum_nd_X^{\rm sc}(n)\beta_{nq}\le w_X(q)
 \quad(2\le q\le X).}
\tag{L-26203.7}
\]

This is an unconditional, deterministic, solver-free nonnegative carry packing
at every endpoint.

## 3. Exact diagonal loss

At stage `T`, define the diagonal candidate

\[
 \widehat\lambda_T
 =\frac{\rho^{(T+1)}(T-1)}{\Gamma_T(T-1)}
\tag{L-26203.8}
\]

and the scale-blocker loss

\[
 \boxed{\ell_T=\widehat\lambda_T-\lambda_T\ge0.}
\tag{L-26203.9}
\]

After stage `T`, no later atom `a_U`, `U<T`, can affect column `T-1`, because
`Gamma_U(T-1)=0`.  Therefore the final slack in that column is exactly

\[
 \boxed{
 s_X^{\rm sc}(T-1)
 =\Gamma_T(T-1)\ell_T.}
\tag{L-26203.10}
\]

Summing over the columns gives the complete scale-slack identity

\[
 \boxed{
 \Sigma_X^{\rm sc}
 :=\sum_{q=2}^Xs_X^{\rm sc}(q)
 =\sum_{T=3}^X\Gamma_T(T-1)\ell_T.}
\tag{L-26203.11}
\]

This is the endpoint-scale analogue of PR #244's exact row-blocker identity

\[
 \Sigma_X^{\rm row}
 =\sum_n\beta_{nn}\ell_n.
\]

The new diagonal weights are much smaller:

\[
 \Gamma_{q+1}(q)\asymp q^{-3/2},
\]

rather than `beta_(q,q) asymp 1`.

## 4. Contiguous scale freeze

Let `q_T` be the least minimizer in (L-26203.4).  If

\[
 q_T<T-1,
\]

then the update saturates column `q_T`:

\[
 \rho^{(T)}(q_T)=0.
\tag{L-26203.12}
\]

For every later endpoint satisfying

\[
 q_T<U<T,
\]

one has `Gamma_U(q_T)>0`.  Nonnegativity of the residual therefore forces

\[
 \boxed{\lambda_U=0.}
\tag{L-26203.13}
\]

Thus one off-diagonal blocker freezes one **contiguous interval of endpoint
scales**.  There is no residue-class corridor and no branching blocker forest:

```text
row greedy:       q freezes all non--(-1 mod q) rows;
endpoint greedy:  q freezes the single interval q<U<T.
```

This is the principal structural simplification of the scale frame.

## 5. Exact size of the diagonal atom

Put

\[
 \gamma_q=\Gamma_{q+1}(q).
\]

By `L-26201`,

\[
 \gamma_q
 =2\sqrt q\left[
   \log\left(1+\frac1q\right)
   -2\left(1-\left(1+\frac1q\right)^{-1/2}\right)
  \right].
\tag{L-26203.14}
\]

For

\[
 F(x)=\log(1+x)-2+2(1+x)^{-1/2},
\]

one has

\[
 F'(x)
 =\frac{x}{(1+x)^{3/2}(\sqrt{1+x}+1)}.
\tag{L-26203.15}
\]

When `0<=x<=1/2`, the denominator lies between `2` and `5`.  Integration gives

\[
 \frac{x^2}{10}\le F(x)\le\frac{x^2}{4}.
\]

Consequently

\[
 \boxed{
 \frac1{5q^{3/2}}
 \le\gamma_q
 \le\frac1{2q^{3/2}}
 \qquad(q\ge2).}
\tag{L-26203.16}
\]

## 6. Bridge to the sharp entropy mass

The vector `d_X^sc` is a feasible nonnegative carry vector, so the universal
mass--slack identities of PR #244 `L-23705` apply without modification:

\[
 \sum_n n d_X^{\rm sc}(n)
 =8\sqrt X-2\Sigma_X^{\rm sc}+O(\log^2X),
\tag{L-26203.17}
\]

and

\[
 \sum_nd_X^{\rm sc}(n)(\log(n+1)+3)
 =O(\log^2X).
\tag{L-26203.18}
\]

Using the average-binomial entropy lower bound gives

\[
 \boxed{
 \sum_nd_X^{\rm sc}(n)G_n
 \ge4\sqrt X-\Sigma_X^{\rm sc}-O(\log^2X).}
\tag{L-26203.19}
\]

Thus the scale frame reduces the positive-minorant problem to one explicit
scalar:

> **Endpoint-Scale Greedy Slack (`ESGS`).** Prove
> \[
> \Sigma_X^{\rm sc}=X^{o(1)},
> \]
> or, more strongly, `Sigma_X^sc=O(log^A(2X))`.

This is a genuine nonnegative object; no signed `b` coordinate needs to be
converted back after the estimate.

## 7. A weaker pointwise closing theorem

By (L-26203.11) and the upper bound in (L-26203.16), the following pointwise
statement is sufficient:

\[
 \boxed{
 \ell_T
 \le C\sqrt T\,\log^A(2X)
 \qquad(3\le T\le X).}
\tag{ESBT}
\]

Indeed,

\[
 \Sigma_X^{\rm sc}
 \le\frac C2\log^A(2X)
 \sum_{q=2}^{X-1}\frac1q
 =O(\log^{A+1}(2X)).
\tag{L-26203.20}
\]

Thus a **square-root** bound for each endpoint blocker loss already preserves
the complete critical mass.  No bounded blocker count, bounded scale weight, or
pointwise positivity of the exact carry inverse is required.

The diagonal decay `q^(-3/2)` is the main quantitative advantage over the
original greedy coordinates.

## 8. Relationship to DCRS and the Green correction

- PR #244 and PR #252 ask for polylogarithmic slack of one canonical row greedy.
  `ESGS` asks for the same aggregate mass conclusion for a different explicit
  positive packing.
- PR #248's canonical signed Green correction solves the constraints but does
  not preserve row positivity.  The endpoint atoms instead make positivity
  automatic and place the remaining work entirely in their nonnegative scale
  weights.
- `L-26202` proves that the continuum defect admits an order-preserving
  nonpositive-cost transport.  The contiguous scale-freeze law is its exact
  finite analogue and nominates a route to `ESBT` through reciprocal-cell
  transport rather than positive-part deletion.

## 9. Proof boundary

Established here, subject to review:

1. the endpoint-scale greedy algorithm;
2. positivity and feasibility of its output;
3. the exact diagonal slack identity;
4. the contiguous interval-freeze law;
5. the `q^(-3/2)` diagonal estimate;
6. the reduction from scale slack to sharp entropy mass.

Open:

- `ESGS` or the sufficient square-root blocker theorem `ESBT`;
- a proof-grade finite transfer of the continuum tail coupling;
- RH.

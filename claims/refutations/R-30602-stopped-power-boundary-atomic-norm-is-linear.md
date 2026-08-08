# R-30602 — A stopped critical power has linear half-endpoint atomic norm

Claim ID: `R-30602`  
Title: The finite/infinite cutoff boundary of `q^{-1/2}1_(q<=N)` forces `Omega(N)` square-root atomic divisor-source mass  
Status: **PROPOSED COMPLETE ELEMENTARY REFUTATION OF `L-30403`'S LAYERWISE POLYLOG ATOMIC-NORM CLAIM**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Issue: #306  
Dependencies: PR #286 `L-28402`; PR #301 `L-29801`; elementary alternating-series estimates  
Scope: one explicit stopped-power generator and every divisor-source representation at the declared half endpoint

## 1. The boundary profile

Let

\[
p(x)=x^{-1/2}
\]

and let `p^[N](n)=p(n)1_(n<=N)`. Define

\[
(\mathscr Cp)(q)
=\sum_{k\ge1}
\left[(2kq-1)^{-1/2}-((2k+1)q)^{-1/2}\right]
\]

and the finite operator `mathscr C_N` as in PR #286. The cutoff source is

\[
Q_N(q)=(\mathscr Cp)(q)-(\mathscr C_Np^{[N]})(q).
\tag{R-30602.1}
\]

Put

\[
M=\left\lfloor\frac{N+1}{2}\right\rfloor.
\]

For

\[
\frac N3<q\le M,
\]

the finite sum contains the shifted-even term `p(2q-1)` and no odd term. Every term with `k>=2` lies outside the endpoint. Hence

\[
\boxed{
Q_N(q)
=-(3q)^{-1/2}
+\sum_{k\ge2}
\left[(2kq-1)^{-1/2}-((2k+1)q)^{-1/2}\right].
}
\tag{R-30602.2}
\]

## 2. Uniform negative moat

Multiply (R-30602.2) by `sqrt(q)` and put `epsilon=1/q`. Then

\[
\sqrt q\,Q_N(q)
=-\frac1{\sqrt3}
+\sum_{k\ge2}
\left[(2k-\epsilon)^{-1/2}-(2k+1)^{-1/2}\right].
\tag{R-30602.3}
\]

Split the last sum into

\[
\sum_{k\ge2}
\left[(2k)^{-1/2}-(2k+1)^{-1/2}\right]
\]

and the shift correction

\[
\sum_{k\ge2}
\left[(2k-\epsilon)^{-1/2}-(2k)^{-1/2}\right].
\]

The first is an alternating tail beginning at `1/2`, and therefore is strictly less than `1/2`.

For the second, the mean-value theorem gives

\[
0<(2k-\epsilon)^{-1/2}-(2k)^{-1/2}
\le\frac{\epsilon}{2k^{3/2}}.
\]

Since

\[
\sum_{k=2}^{\infty}k^{-3/2}<2,
\]

the complete correction is less than `epsilon`.

For `q>=20`,

\[
\sqrt q\,Q_N(q)
<-\frac1{\sqrt3}+\frac12+\frac1{20}.
\]

The rational inequality

\[
\frac1{\sqrt3}>\frac{23}{40}
\]

follows by squaring. Consequently

\[
\boxed{
Q_N(q)<-\frac1{40\sqrt q}
\qquad
\left(\frac N3<q\le M,\ q\ge20\right).
}
\tag{R-30602.4}
\]

## 3. Triangular divisor inversion on the top band

Suppose a divisor source `sigma=(sigma_m)_(2<=m<=M)` represents this boundary at the declared half endpoint:

\[
Q_N(q)=\sum_{\substack{m\le M\\q\mid m}}\sigma_m
\qquad(2\le q\le M).
\tag{R-30602.5}
\]

For every `q>N/3`, one has `q>M/2`. Thus the only multiple of `q` not exceeding `M` is `q` itself, and

\[
\boxed{\sigma_q=Q_N(q).}
\tag{R-30602.6}
\]

For `N>=120`, every integer in the band satisfies `q>=20`. The atomic norm is therefore bounded below by

\[
\begin{aligned}
\|\sigma\|_{\rm at}
&=\sum_{m\le M}\sqrt m\,|\sigma_m|\\
&\ge
\sum_{N/3<q\le M}\sqrt q\,|Q_N(q)|\\
&\ge\frac1{40}
\left(M-\left\lfloor\frac N3\right\rfloor\right)\\
&\ge\boxed{\frac N{240}}.
\end{aligned}
\tag{R-30602.7}
\]

This lower bound is representation independent.

## 4. Consequence for the terminal-commutator proposal

PR #301 resolves the critical target as a positive finite layer cake of stopped powers. PR #304 claims that the complete finite Euler/Peano boundary export is bounded in the source norm

\[
\sum_m\sqrt m\,|\sigma_m|
\]

by a polylogarithm, using a coefficient model with an additional `n^{-1}` derivative gain.

Equation (R-30602.7) shows that no uniform layerwise estimate of that form holds even for one declared stopped generator. The raw top-band cutoff carries `q^{-1/2}` size on a positive proportion of the half endpoint.

Therefore the composition

```text
stopped pure-power source
-> polylog half-endpoint atomic divisor source
-> adjacent-commutator lift
```

is false as stated.

A cancellation across distinct stopped endpoints could only repair this after an explicit common-destination recombination theorem. Such a theorem is not supplied by `L-30403`; its proof takes an absolute atomic norm after the asserted `n^{-3/2}` bound.

## 5. What the obstruction does not show

The lower bound is on the **atomic adjacent-commutator lift**, not on optimized Cycle Debt.

A central split with parent `n` acts on the whole top band as the step function

\[
\mathbf1_{q\le n}.
\]

It can therefore amortize many of the forced top-band atoms simultaneously. The linear atomic norm does not rule out a polylogarithmic optimized flow.

This is the replacement mechanism proved in `L-30601`.

## 6. Exact disposition

```text
PR #304 layerwise polylog atomic source norm      REFUTED
representation-independent top-band lower bound   PROPOSED COMPLETE
polylog optimized Cycle Debt                       NOT REFUTED
RH                                                  UNPROVED
```

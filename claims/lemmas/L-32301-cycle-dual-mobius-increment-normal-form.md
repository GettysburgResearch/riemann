# L-32301 — Cycle-Debt duals in Möbius-increment coordinates

Claim ID: `L-32301`  
Title: Every finite Cycle-Debt dual has a unique divisor-coefficient representation and the RH-facing objective is its source-weighted coefficient sum  
Status: **PROPOSED COMPLETE EXACT FINITE LEMMA — independent review requested**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: PR #272 `L-26205`, `L-27205`  
Scope: finite dual algebra; no RH conclusion

## 1. Setup

Fix an endpoint `X` and a normalized dual potential

\[
F(1)=0.
\]

For `n>=2`, define its first increments

\[
a_n=F(n)-F(n-1).
\tag{L-32301.1}
\]

Define the Möbius-increment coefficients

\[
\boxed{
 b_q=\sum_{d\mid q}\mu(d)a_{q/d}
 \qquad(2\le q\le X).
}
\tag{L-32301.2}
\]

Equivalently,

\[
a_n=\sum_{q\mid n}b_q.
\tag{L-32301.3}
\]

All sums below are finite.

## 2. Exact floor expansion

Summing (L-32301.3) over `2<=n<=N` gives

\[
\begin{aligned}
F(N)
&=\sum_{n=2}^N a_n\\
&=\sum_{q=2}^N b_q\#\{n\le N:q\mid n\}.
\end{aligned}
\]

Therefore

\[
\boxed{
F(N)=\sum_{q=2}^N b_q\left\lfloor\frac Nq\right\rfloor.
}
\tag{L-32301.4}
\]

The representation is unique because the increment sequence determines `b` by finite Möbius inversion.

This removes the node potential from the proof-facing dual.  The finite dual variable can be taken to be the coefficient vector

\[
b=(b_2,\ldots,b_X).
\]

## 3. Carry defects are linear coefficient tests

For a split `e=(n,j)`, write

\[
\chi_e(q)
=\left\lfloor\frac nq\right\rfloor
 -\left\lfloor\frac jq\right\rfloor
 -\left\lfloor\frac{n-j}q\right\rfloor.
\]

Then (L-32301.4) gives exactly

\[
\boxed{
\delta_F(n,j)
:=F(n)-F(j)-F(n-j)
=\sum_{q=2}^n b_q\chi_e(q).
}
\tag{L-32301.5}
\]

The capacity potential of PR #272 has coefficients `q^(-1/2)`. Hence the complete finite Cycle-Debt dual feasibility condition

\[
0\le\delta_F(e)\le\omega_e
\]

is exactly

\[
\boxed{
0\le
\sum_q b_q\chi_e(q)
\le
\sum_q\frac{\chi_e(q)}{\sqrt q}
}
\tag{L-32301.6}
\]

for every declared balanced split `e`.

Thus the dual cone is a finite carry-row coefficient cone.  No source-to-edge identification is involved.

## 4. Pairing with an arbitrary target

Let `t(q)` be an arbitrary finite carry target and let `r^(t)` be its unique size-zero node divergence from PR #272 / `L-26205`, so that

\[
t(q)=\sum_n r^{(t)}(n)\left\lfloor\frac nq\right\rfloor.
\tag{L-32301.7}
\]

Using (L-32301.4) and finite interchange,

\[
\begin{aligned}
\sum_n r^{(t)}(n)F(n)
&=\sum_q b_q
  \sum_n r^{(t)}(n)\left\lfloor\frac nq\right\rfloor\\
&=\sum_q b_q t(q).
\end{aligned}
\]

Therefore

\[
\boxed{
-\langle r^{(t)},F\rangle
=-\sum_{q=2}^X b_q t(q).
}
\tag{L-32301.8}
\]

For the critical target

\[
w_X(q)=q^{-1/2}\log(X/q),
\]

the exact Cycle-Debt dual objective is

\[
\boxed{
-\sum_{q=2}^X
 \frac{b_q}{\sqrt q}\log\frac Xq.
}
\tag{L-32301.9}
\]

For the stopped half-power target

\[
p_Q(q)=q^{-1/2}\mathbf 1_{q\le Q},
\]

the objective is simply

\[
\boxed{
-\sum_{q=2}^Q\frac{b_q}{\sqrt q}.
}
\tag{L-32301.10}
\]

## 5. Relation to the global square-root rigidity theorem

PR #272 `L-27901` writes a global feasible potential as

\[
F(n)=an-D_F(n),
\qquad 0\le D_F(n)\le D_{\mathcal G}(n)\ll\sqrt n.
\]

The coefficient form above is compatible with that theorem but is strictly finite and requires no compactness passage.  It also makes clear why a coefficientwise condition such as

\[
0\le b_q\le q^{-1/2}
\]

would be sufficient but is not part of dual feasibility: the carry rows constrain correlated sums of the `b_q`, not individual coefficients.

## 6. Proof boundary

Closed exactly:

1. the Möbius-increment coefficient transform;
2. unique floor reconstruction of every normalized dual;
3. the carry-row coefficient form of both dual inequalities;
4. the exact target pairing for an arbitrary finite target;
5. the critical and stopped-half-power specializations.

Not claimed:

1. coefficientwise positivity of `b_q`;
2. a bound for the stopped half-power dual objective;
3. Cycle Debt;
4. RH.

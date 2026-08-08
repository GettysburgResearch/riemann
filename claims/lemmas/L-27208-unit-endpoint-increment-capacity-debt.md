# L-27208 — Unit endpoint increments have vanishing canonical capacity debt

Claim ID: `L-27208`  
Title: Passing from endpoint \(X-1\) to \(X\) costs only \(O((\log X)/\sqrt X)\) negative capacity debt in the canonical balanced tree flow  
Status: **PROPOSED COMPLETE ANALYTIC LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-02-r`  
Created: 2026-08-08  
Dependencies: `L-26205`, `L-27204`, `L-27205`; elementary summation  
Scope: endpoint interpolation for Cycle Debt; no RH assumption

## 1. Endpoint increment

For

\[
w_X(q)=q^{-1/2}\log(X/q),\qquad2\le q\le X,
\tag{L-27208.1}
\]

the increment from \(X-1\) to \(X\) is

\[
\delta_X(q)=
\begin{cases}
c_Xq^{-1/2},&2\le q\le X-1,\\
0,&q=X,
\end{cases}
\qquad c_X=\log\frac X{X-1}.
\tag{L-27208.2}
\]

Thus

\[
w_X=w_{X-1}+\delta_X
\tag{L-27208.3}
\]

after extending the old target by the zero \(X\)-column.

Let \(r^{\delta,X}\) be the exact node divergence determined from \(\delta_X\) by `L-26205`, and put

\[
\boxed{d^{\delta,X}=\sum_{m=2}^{X}r^{\delta,X}(m)T_m,}
\tag{L-27208.4}
\]

where \(T_m\) is the canonical central tree of `L-27204`. Since \(\partial T_m=e_m-me_1\),

\[
\partial d^{\delta,X}=r^{\delta,X}.
\tag{L-27208.5}
\]

Therefore \(d^{\delta,X}\) realizes every increment column exactly.

## 2. Weighted size of a central tree

For a split edge \(e=(n,j)\), retain

\[
\omega_e=\sum_{q=2}^{n}\frac{\chi_e(q)}{\sqrt q}.
\tag{L-27208.6}
\]

The elementary bound

\[
\omega_e\le2\sqrt n
\tag{L-27208.7}
\]

is sufficient.

At depth \(\ell\) of the central fragmentation tree \(T_m\), there are at most \(2^\ell\) nodes and their parent sizes sum to \(m\). Cauchy--Schwarz gives

\[
\sum_{\text{depth }\ell}\sqrt{\text{parent size}}\le\sqrt{2^\ell m}.
\tag{L-27208.8}
\]

Summing until the leaves are reached gives

\[
\sum_e|T_m(e)|\sqrt{\operatorname{parent}(e)}\le\frac{\sqrt2}{\sqrt2-1}m<4m.
\tag{L-27208.9}
\]

Consequently

\[
\boxed{\|T_m\|_{\omega,1}:=\sum_e\omega_e|T_m(e)|\le8m.}
\tag{L-27208.10}
\]

Every edge of \(T_m\) is \(1/3\)-balanced, so this construction is valid for the fixed \(\eta\le1/4\) used on PR #272.

## 3. Variation of the endpoint source

Put \(N=X-1\), and temporarily remove the scalar \(c_X\). For the target

\[
v(q)=
\begin{cases}
q^{-1/2},&2\le q\le N,\\
0,&q=X,
\end{cases}
\tag{L-27208.11}
\]

its multiples-Möbius transform is

\[
u_m=m^{-1/2}S_{\lfloor N/m\rfloor},\qquad S_K=\sum_{k\le K}\frac{\mu(k)}{\sqrt k}.
\tag{L-27208.12}
\]

The trivial estimate

\[
|S_K|\le2\sqrt K
\tag{L-27208.13}
\]

is enough. Write \(K_m=\lfloor N/m\rfloor\). Then

\[
\begin{aligned}
|u_m-u_{m+1}|
\le{}&\left(m^{-1/2}-(m+1)^{-1/2}\right)|S_{K_m}|\\
&+(m+1)^{-1/2}\sum_{K_{m+1}<k\le K_m}k^{-1/2}.
\end{aligned}
\tag{L-27208.14}
\]

For the first line,

\[
\sum_{m=2}^{X}m\left(m^{-1/2}-(m+1)^{-1/2}\right)|S_{K_m}|\le\sqrt N\,(1+\log X).
\tag{L-27208.15}
\]

For the second line, each integer \(k\le N/2\) occurs in exactly one quotient jump, at \(m=\lfloor N/k\rfloor\). Its weighted contribution is at most

\[
\frac{\sqrt{\lfloor N/k\rfloor}}{\sqrt k}\le\frac{\sqrt N}{k}.
\tag{L-27208.16}
\]

Hence

\[
\boxed{\sum_{m=2}^{X}m\,|r^{v,X}(m)|\le2\sqrt N\,(1+\log X).}
\tag{L-27208.17}
\]

Restoring the factor \(c_X\) and using

\[
c_X=\log(1+1/N)\le N^{-1},
\tag{L-27208.18}
\]

we obtain

\[
\boxed{\sum_{m=2}^{X}m\,|r^{\delta,X}(m)|\le\frac{2(1+\log X)}{\sqrt{X-1}}.}
\tag{L-27208.19}
\]

## 4. Vanishing debt bound

Equations (L-27208.4), (L-27208.10), and (L-27208.19) give

\[
\begin{aligned}
\mathcal N_\omega(d^{\delta,X})
&\le\sum_e\omega_e|d^{\delta,X}(e)|\\
&\le\sum_{m=2}^{X}|r^{\delta,X}(m)|\,\|T_m\|_{\omega,1}\\
&\le\boxed{\frac{16(1+\log X)}{\sqrt{X-1}}.}
\end{aligned}
\tag{L-27208.20}
\]

This estimate is unconditional and uses no cancellation in the Möbius function.

## 5. Endpoint interpolation for optimized Cycle Debt

Embed any exact balanced flow at endpoint \(X-1\) into the endpoint-\(X\) edge space and add \(d^{\delta,X}\). The result realizes \(w_X\) exactly. Negative capacity debt is subadditive, so

\[
\boxed{\mathfrak N_\eta(X)\le\mathfrak N_\eta(X-1)+\frac{16(1+\log X)}{\sqrt{X-1}}.}
\tag{L-27208.21}
\]

Thus parity of the endpoint is not an asymptotic obstruction. In a half-scale induction, at most one unit increment is needed before every division by two, and its accumulated contribution is negligible.

## 6. Proof boundary

Closed here:

- exact realization of the endpoint increment;
- an explicit balanced canonical flow;
- a vanishing negative-capacity bound;
- the optimized endpoint interpolation inequality.

Open:

- the even-endpoint paired odd-commutator estimate of `L-27207`;
- Cycle Debt;
- RH.

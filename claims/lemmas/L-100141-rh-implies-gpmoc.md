# L-100141 — RH implies the complete growing-moment Poisson-owner estimate

Claim ID: `L-100141`
Status: **PROVED CONDITIONAL CONVERSE / RETAINED OVERLAP WITH PR #671**
Created: 2026-08-20
Depends on: PR #659 `L-99802/L-99803`; `L-100140`
RH status: **assumed only in this lemma**

Retain PR #659's compact kernel

\[
\kappa=\mathcal KT,
\qquad
\mathcal K=(I-S_2)(I-2S_4),
\]

and on the block \(2^L\le x<2^{L+1}\) put

\[
M_L=\max\!\left(1,\left\lfloor\frac{L}{(\log(L+e))^3}\right\rfloor\right),
\qquad
\kappa_L=(I-S_2)^{M_L}\kappa.
\]

Then

\[
\operatorname{supp}\kappa_L\subset[1,2^{M_L+3}],
\tag{L-100141.1}
\]

and

\[
\|\kappa_L\|_\infty+
\operatorname{Var}_{d\log y}(\kappa_L)\ll2^{M_L}.
\tag{L-100141.2}
\]

Let

\[
\beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67),
\]

\[
c_{L,y}(n)=\frac{\beta(n)}{\sqrt n}\kappa_L(y/n),
\qquad
\tau_L=\frac1{\log(L+e)}.
\]

For terminal inverse blocks with `y<1`, extend `c_{L,y}` by zero and put
`Q_L(y)=0`; every estimate below is then trivial on that final half-block.

The sequence is supported on

\[
y2^{-M_L-3}\le n\le y.
\]

## 1. RH prefix estimate

Under RH, for every \(\varepsilon>0\),

\[
M(x)=\sum_{n\le x}\mu(n)=O_\varepsilon(x^{1/2+\varepsilon}).
\tag{L-100141.3}
\]

Therefore

\[
B_\beta(x)=\sum_{n\le x}\beta(n)
=M(x)-M(x/67)
=O_\varepsilon(x^{1/2+\varepsilon}).
\tag{L-100141.4}
\]

## 2. Uniform coefficient-tail estimate

For \(u\ge0\), set

\[
C_{L,y}(u)=\sum_{n\ge u}c_{L,y}(n).
\]

Apply Abel summation separately to every shifted copy of \(\kappa\) in
\(\kappa_L\). On the support of one copy, \(n\) ranges through an interval of
fixed ratio eight. Equations (L-100141.2) and (L-100141.4) give, uniformly in the
truncation point \(u\),

\[
\boxed{
|C_{L,y}(u)|\ll_\varepsilon2^{M_L}(1+y^\varepsilon).
}
\tag{L-100141.5}
\]

## 3. Poisson norm

By `L-100140`,

\[
Q_L(y)=2\tau_L\int_0^\infty|C_{L,y}(u)|^2u^{2\tau_L-1}\,du.
\]

The sequence vanishes above \(u=y\), so

\[
\sqrt{Q_L(y)}
\ll_\varepsilon
2^{M_L}(1+y^\varepsilon)y^{\tau_L}.
\tag{L-100141.6}
\]

Uniformly for \(1\le y\le2^{L+1}\),

\[
2^{M_L}=2^{o(L)},
\qquad
y^{\tau_L}=2^{o(L)}.
\]

In the precise subpower sense—after fixing any target exponent and then taking
\(\varepsilon\) sufficiently small—

\[
\boxed{
\sup_{1\le y\le2^{L+1}}\sqrt{Q_L(y)}=2^{o(L)}.
}
\tag{L-100141.7}
\]

## 4. Positive inverse

The inverse coefficients are

\[
b_{L,k}=\binom{M_L+k-1}{k}.
\]

Their complete active mass is

\[
\sum_{k=0}^{L+1}b_{L,k}
=\binom{M_L+L+1}{M_L}=2^{o(L)}.
\tag{L-100141.8}
\]

Each logarithmic block has length \(\log2\). Combining (L-100141.7) and
(L-100141.8) gives

\[
\boxed{
\sum_{k=0}^{L+1}b_{L,k}
\int_{2^{L-k}}^{2^{L+1-k}}
\sqrt{Q_L(y)}\frac{dy}{y}=2^{o(L)}.
}
\tag{L-100141.9}
\]

Thus RH implies `GPMOC99800`.

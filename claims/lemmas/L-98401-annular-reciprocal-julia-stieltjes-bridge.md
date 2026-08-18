# L-98401 — Exact bridge from the annular reciprocal-Julia scalar to the native Stieltjes state

Claim ID: `L-98401`  
Status: **PROVED EXACT SOURCE-FAITHFUL IDENTITY**  
Created: 2026-08-18  
Depends on: the unique `5:3` scalar and factor-four annularization frozen in PR #582  
RH status: **not assumed**

Let \(b(X)\) be the fixed completed annular base and put

\[
h(X)=\frac{b(X)}{\sqrt X}.
\tag{L-98401.1}
\]

For a finite set \(P\) of future odd primes define the literal rough completion

\[
F_P(Y)=
\sum_{m\mid\prod_{p\in P}p}
\frac{\mu(m)}{\sqrt m}\,b(Y/m),
\tag{L-98401.2}
\]

with the usual zero extension below activation.  Its normalized state is

\[
\boxed{
U_P(Y)=\frac{F_P(Y)}{\sqrt Y}
=
\sum_{m\mid\prod_{p\in P}p}
\frac{\mu(m)}m h(Y/m).
}
\tag{L-98401.3}
\]

## 1. Exact prime transition

If \(p\notin P\), unique least-prime ownership gives

\[
\boxed{
U_{P\cup\{p\}}(Y)
=U_P(Y)-\frac1pU_P(Y/p).
}
\tag{L-98401.4}
\]

Thus the normalized annular state is the \(\alpha=1\) member of the universal
quotient dynamics in `L-98400`.

## 2. Exact Stieltjes transfer

Define the finite rough prefix

\[
A_P(t)=
\sum_{\substack{m\le t\\m\mid\prod_{p\in P}p}}
\frac{\mu(m)}m.
\tag{L-98401.5}
\]

If \(h(1)=0\) and \(dh\) is interpreted in the Stieltjes sense, then

\[
\boxed{
U_P(Y)=\int_{[1,Y]}A_P(Y/x)\,dh(x).
}
\tag{L-98401.6}
\]

Indeed, integration by parts or direct summation of the jumps gives

\[
\int A_P(Y/x)dh(x)
=
\sum_m\frac{\mu(m)}m h(Y/m).
\]

The identity retains the same future-prime owner, activation threshold, and
coefficient on both sides.

## 3. Infinite-threshold form

For a least allowed prime \(z\), let

\[
A_z(t)=
\sum_{\substack{m\le t\\m\text{ squarefree}\\P^-(m)\ge z}}
\frac{\mu(m)}m.
\]

Whenever the finite states stabilize at endpoint \(Y\),

\[
\boxed{
U(Y,z)=\int_{[1,Y]}A_z(Y/x)\,dh(x).
}
\tag{L-98401.7}
\]

This is the exact common state behind the reciprocal-Julia annular consumer and
the native Dickman--Stieltjes analysis.  It does **not** identify the raw
pointwise half-order boundary with the normalized annular state; the two use
\(\alpha=1/2\) and \(\alpha=1\), respectively, on the same quotient DAG.

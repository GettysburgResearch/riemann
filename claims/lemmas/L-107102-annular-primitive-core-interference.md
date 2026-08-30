# L-107102 — Exact annular primitive-core interference identity

**Claim ID:** `L-107102`  
**Status:** proved exact finite arithmetic identity  
**Date:** 2026-08-31

Define the finite positive-definite kernel

\[
\mathcal K_X(v)=\sum_{|k|\le K_A(X)}|w_{k,X}|^2e^{-it_{k,X}v}.
\]

For `I_j=(X/q^{j+1},X/q^j]`, expansion of the feature norm gives

\[
\boxed{\|c_j\|^2=\sum_{m,n\in I_j,\ q\nmid mn}
\frac{\mu(m)\mu(n)}{\sqrt{mn}}
\mathcal K_X(\log(m/n)).}\tag{1}
\]

On squarefree support write uniquely `m=da`, `n=db`, `(a,b)=1`; then `d,a,b`
are pairwise coprime and q-free and `mu(da)mu(db)=mu(a)mu(b)`. Hence

\[
\boxed{\|c_j\|^2=\sum_{d\ {
m sf},\ q\nmid d}\frac1d
\sum_{da,db\in I_j\atop (a,b)=1,(ab,dq)=1}
\frac{\mu(a)\mu(b)}{\sqrt{ab}}
\mathcal K_X(\log(a/b)).}\tag{2}
\]

The core sum remains inside the exact signed scalar. No Cauchy inequality or
corewise absolute square has been used. The diagonal, summed over all annuli,
is

\[
\mathcal K_X(0)\sum_{n\le X,q\nmid n}\mu(n)^2/n=O_B(\log X),
\]

because the sampled detector has uniformly bounded zero-frequency mass. Thus
the annular criterion differs from its signed off-diagonal primitive
interference by a subpower term.

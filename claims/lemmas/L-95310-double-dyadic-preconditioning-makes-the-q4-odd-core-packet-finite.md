# L-95310 — Double dyadic preconditioning makes the Q4 odd-core packet finite

Claim ID: `L-95310`  
Status: **PROPOSED COMPLETE EXACT ARITHMETIC THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-17  
Frozen parent: PR #563 at `c4cc65cccb3f13a6499506cf3c26bd521c455864`  
Scope: exact critical Q4 source reduction; no deterministic odd-core cancellation bound

## 1. Source and preconditioner

Retain

\[
A_4(s)
=
\frac{1-4^{1-s}}{(1-4^{-s})\zeta(s)}
=
\sum_{n\ge1}\frac{a_4(n)}{n^s},
\]

and

\[
d_4=(\varepsilon-4\delta_4)*(a_4\log).
\]

Define the safe finite preconditioner

\[
p_2=(\varepsilon+\delta_2)^{*2}
=
\varepsilon+2\delta_2+\delta_4,
\]

and put

\[
\boxed{e_4=p_2*d_4.}
\tag{L-95310.1}
\]

Its Dirichlet multiplier \((1+2^{-s})^2\) has no zero in \(\Re s>0\).

## 2. Finite odd-core table

Write \(n=2^rm\), where \(m\) is odd. If \(m\) is not squarefree, then

\[
e_4(2^rm)=0.
\]

If \(m\) is odd squarefree, then

\[
\boxed{
e_4(2^rm)
=
\mu(m)
\left[A_r\log m+B_r\log2\right],
\qquad 0\le r\le5,
}
\tag{L-95310.2}
\]

where

\[
(A_0,\ldots,A_5)=(1,1,-8,-8,16,16),
\tag{L-95310.3}
\]

and

\[
(B_0,\ldots,B_5)=(0,-1,-8,0,32,16).
\tag{L-95310.4}
\]

For every \(r\ge6\),

\[
\boxed{e_4(2^rm)=0.}
\tag{L-95310.5}
\]

Equivalently, the six values are

\[
\mu(m)
\left(
\log m,\,
\log(m/2),\,
-8\log(2m),\,
-8\log m,\,
16\log(4m),\,
16\log(2m)
\right).
\tag{L-95310.6}
\]

Thus the infinite dyadic state of PR #563 becomes one literal factor-32 packet
after a safe finite filter.

## 3. Dirichlet-series proof

Let

\[
z=2^{-s},
\qquad
M_{\rm odd}(s)
=
\sum_{\substack{m\ge1\\m\ {\rm odd}}}
\frac{\mu(m)}{m^s}
=
\frac{1}{(1-z)\zeta(s)},
\]

and put

\[
P(z)=1-4z^2.
\]

The dyadic local factor of \(A_4\) is

\[
L(z)=\frac{P(z)}{1+z},
\]

so

\[
A_4(s)=L(z)M_{\rm odd}(s).
\]

The Dirichlet series of \(d_4\) is

\[
D_4(s)=-P(z)A_4'(s).
\]

Multiplying by \((1+z)^2\) gives

\[
\boxed{
(1+z)^2D_4(s)
=
\mathcal A(z)\bigl[-M_{\rm odd}'(s)\bigr]
+
(\log2)\mathcal B(z)M_{\rm odd}(s),
}
\tag{L-95310.7}
\]

where

\[
\mathcal A(z)
=
(1+z)(1-4z^2)^2
=
1+z-8z^2-8z^3+16z^4+16z^5,
\tag{L-95310.8}
\]

and

\[
\mathcal B(z)
=
-z(1-4z^2)(1+8z+4z^2)
=
-z-8z^2+32z^4+16z^5.
\tag{L-95310.9}
\]

Coefficient comparison proves (L-95310.2)–(L-95310.5).

## 4. Critical observation and stable inverse

For the centered Q4 cubic \(W\), define

\[
\mathcal C_d(X)
=
\sum_{n\le X}
\frac{d_4(n)}{\sqrt n}W(n/X),
\]

and define \(\mathcal C_e\) analogously with \(e_4\). Dirichlet convolution
and critical square-root scaling give

\[
\boxed{
\mathcal C_e(X)
=
\mathcal C_d(X)
+
\sqrt2\,\mathcal C_d(X/2)
+
\frac12\mathcal C_d(X/4).
}
\tag{L-95310.10}
\]

Let \(S F(X)=F(X/2)\). Then

\[
\mathcal C_e=(I+2^{-1/2}S)^2\mathcal C_d.
\]

Since \(2^{-1/2}<1\),

\[
\boxed{
\mathcal C_d(X)
=
\sum_{j\ge0}
(-1)^j(j+1)2^{-j/2}
\mathcal C_e(X/2^j),
}
\tag{L-95310.11}
\]

and the sum is finite at every endpoint. Its absolute coefficient mass is

\[
\sum_{j\ge0}(j+1)2^{-j/2}
=
(1-2^{-1/2})^{-2}.
\tag{L-95310.12}
\]

Therefore a polylogarithmic bound for \(\mathcal C_e\) is equivalent, up to a
fixed constant and exponent, to the original OCHD bound for
\(\mathcal C_d\).

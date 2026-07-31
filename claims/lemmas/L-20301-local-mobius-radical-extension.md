# L-20301 — Exact local Möbius extension into the global Weil radical

Claim ID: `L-20301`  
Title: Every compactly supported localized vector has an exact arithmetic-radical extension, with a completely explicit lower-tail residual  
Status: `PROPOSED — COMPLETE ALGEBRAIC/ANALYTIC PROOF; WEIL NORMALIZATION INHERITED`  
Authoring agent: `gpt56-03-p`  
Created: 2026-08-01  
Dependencies: the arithmetic map and weak-radical theorem of `L-16205`; finite Möbius inversion; Mellin factorization  
Scope: the complete-kernel synthesis gate of `L-19701/T-19701`  
Related counterexample candidates: none

## 1. Setup

Fix

\[
0<a<b<\infty
\]

and let \(h\) be a real or complex function supported in \([a,b]\). Put

\[
g(u)=u^{-1/2}h(u),
\qquad u>0,
\tag{L-20301.1}
\]

extended by zero outside \([a,b]\). Assume \(g\) is compactly supported and of
bounded variation; smooth finite-packet vectors are more than sufficient.

Choose an integer \(N\) satisfying the safe support inequality

\[
\boxed{Na>b.}
\tag{L-20301.2}
\]

Let \(\mu\) be the Möbius function and define

\[
P_N(s)=\sum_{n\le N}\frac{\mu(n)}{n^s},
\qquad
m_N=P_N(1)=\sum_{n\le N}\frac{\mu(n)}n.
\tag{L-20301.3}
\]

Choose once and for all a real function

\[
\psi\in C_c^\infty(0,a),
\qquad
\int_0^\infty\psi(x)\,dx=1.
\tag{L-20301.4}
\]

Define on the positive half-line

\[
\boxed{
f_{N,h}^+(x)
=
\sum_{n\le N}\mu(n)g(nx)
-
m_N\!\left(\int_0^\infty g(y)\,dy\right)\psi(x).
}
\tag{L-20301.5}
\]

Extend \(f_{N,h}^+\) evenly to the real line and call the result \(f_{N,h}\).

Use the Connes–Consani arithmetic map

\[
E(f)(u)=u^{1/2}\sum_{m\ge1}f(mu),
\qquad u>0.
\tag{L-20301.6}
\]

All sums below are pointwise finite because the sources are compactly
supported.

## 2. Exact source constraints

The source vanishes in a neighborhood of the origin: every dilation
\(g(nx)\) is supported in \([a/n,b/n]\), and \(\psi\) is supported away from
zero. Hence

\[
f_{N,h}(0)=0.
\tag{L-20301.7}
\]

Moreover,

\[
\begin{aligned}
\int_0^\infty f_{N,h}^+(x)\,dx
&=
\sum_{n\le N}\frac{\mu(n)}n
\int_0^\infty g(y)\,dy\\
&\quad-
m_N\!\left(\int_0^\infty g(y)\,dy\right)
\int_0^\infty\psi(x)\,dx\\
&=0.
\end{aligned}
\tag{L-20301.8}
\]

Thus the even source satisfies exactly

\[
\boxed{
f_{N,h}(0)=0,
\qquad
\int_{\mathbb R}f_{N,h}(x)\,dx=0.
}
\tag{L-20301.9}
\]

It is compactly supported, of bounded variation, and identically zero near
zero. Therefore `L-16205` applies:

\[
\boxed{E(f_{N,h})\text{ is an exact global weak Weil-radical vector}.}
\tag{L-20301.10}
\]

No approximation or RH assumption has entered.

## 3. Truncated divisor coefficients

Define

\[
A_N(k)=\sum_{\substack{d\mid k\\d\le N}}\mu(d).
\tag{L-20301.11}
\]

Then

\[
A_N(1)=1
\tag{L-20301.12}
\]

and, for every \(2\le k\le N\),

\[
A_N(k)=\sum_{d\mid k}\mu(d)=0.
\tag{L-20301.13}
\]

Finite rearrangement gives, for every \(u>0\),

\[
\sum_{m\ge1}\sum_{n\le N}\mu(n)g(nmu)
=
\sum_{k\ge1}A_N(k)g(ku).
\tag{L-20301.14}
\]

This is the exact dilation form of truncated Möbius inversion.

## 4. Exact local reconstruction

Take \(u\in[a,b]\). The correction term in (L-20301.5) contributes nothing,
because

\[
mu\ge a
\]

for every \(m\ge1\), whereas \(\psi\) is supported strictly below \(a\).

For \(k>N\), (L-20301.2) gives

\[
ku\ge (N+1)a>Na>b,
\]

so \(g(ku)=0\). Equations (L-20301.12)–(L-20301.14) therefore imply

\[
\sum_{m\ge1}f_{N,h}(mu)=g(u).
\tag{L-20301.15}
\]

Multiplying by \(u^{1/2}\) proves the main identity:

\[
\boxed{
E(f_{N,h})(u)=h(u)
\qquad(a\le u\le b).
}
\tag{L-20301.16}
\]

Thus **every compactly supported localized vector is exactly the restriction
of a global arithmetic-radical vector**.

This is stronger than finite projected-source surjectivity: no finite Fourier
projection is present in (L-20301.16).

## 5. Complete explicit lower tail

Let

\[
r_{N,h}=E(f_{N,h})
\]

and define the exterior error

\[
t_{N,h}=r_{N,h}-h,
\tag{L-20301.17}
\]

with \(h\) extended by zero outside \([a,b]\). Combining the preceding
identities gives

\[
\boxed{
\begin{aligned}
t_{N,h}(u)
={}&u^{1/2}
\sum_{k>N}A_N(k)g(ku)\\
&-
u^{1/2}m_N
\left(\int_0^\infty g(y)\,dy\right)
\sum_{m\ge1}\psi(mu).
\end{aligned}
}
\tag{L-20301.18}
\]

Here the `nu` in the second line denotes the same variable \(u\); equivalently
that factor is \(u^{1/2}\). The reconstruction theorem and compact support imply

\[
\boxed{
\operatorname{supp}t_{N,h}\subset(0,a).
}
\tag{L-20301.19}
\]

The upper tail is identically zero. Every remaining obstruction is a completely
explicit lower-tail divisor sum plus one rank-one source-constraint
correction.

## 6. Mellin residual factorization

Use the multiplicative Fourier convention of `L-16205`,

\[
\widehat q(z)
=
\int_0^\infty q(u)u^{-iz}\,d^*u,
\qquad
s=\frac12-iz.
\tag{L-20301.20}
\]

Then

\[
\widehat h(z)
=
\int_0^\infty g(u)u^{-1/2-iz}\,du.
\tag{L-20301.21}
\]

Let

\[
M_\psi(z)
=
\int_0^\infty\psi(x)x^{-1/2-iz}\,dx.
\tag{L-20301.22}
\]

For \(\operatorname{Im}z\) initially large enough for absolute convergence,
dilation and substitution give

\[
M_{f_{N,h}}(z)
=
P_N(s)\widehat h(z)
-
m_N\widehat h(i/2)M_\psi(z).
\tag{L-20301.23}
\]

The pole-cancellation point is exact:

\[
M_\psi(i/2)=\int\psi=1,
\qquad
P_N(1)=m_N,
\]

so

\[
M_{f_{N,h}}(i/2)=0.
\tag{L-20301.24}
\]

Using the arithmetic Mellin factorization from `L-16205` and analytic
continuation yields

\[
\boxed{
\widehat t_{N,h}(z)
=
\bigl[\zeta(s)P_N(s)-1\bigr]\widehat h(z)
-
m_N\widehat h(i/2)\zeta(s)M_\psi(z).
}
\tag{L-20301.25}
\]

The source-constraint correction cancels the zeta pole but vanishes at every
nontrivial zeta zero.

## 7. Exact zero obstruction

Let \(z_\rho\) be the centered parameter of any nontrivial zeta zero, so

\[
\zeta\!\left(\frac12-iz_\rho\right)=0.
\]

Equation (L-20301.25) gives, for every finite \(N\),

\[
\boxed{
\widehat t_{N,h}(z_\rho)=-\widehat h(z_\rho).
}
\tag{L-20301.26}
\]

This is the pointwise form of radical transport. It has three consequences.

1. Increasing the Möbius cutoff cannot erase an off-line-cardinal evaluation.
2. If a norm \(X\) satisfies
   \[
   |\widehat q(z_\rho)|\le C_{\rho,X}\|q\|_X,
   \]
   then
   \[
   \boxed{
   \|t_{N,h}\|_X
   \ge
   \frac{|\widehat h(z_\rho)|}{C_{\rho,X}}.
   }
   \tag{L-20301.27}
   \]
3. Tail convergence in a topology controlling every nontrivial-zero
   evaluation is possible only for vectors whose transforms vanish at those
   zeros.

The last clause is exactly why ordinary local or \(L^2\) source surjectivity
does not settle the RH-bearing form topology.

## 8. Packet form

Let

\[
J:\mathbb C^d\longrightarrow
\{h:\operatorname{supp}h\subset[a,b]\}
\tag{L-20301.28}
\]

be any finite basis map. Apply (L-20301.5) linearly to \(h=Jc\), producing a
global-radical synthesis map

\[
R_N:\mathbb C^d\to\mathcal R_W
\tag{L-20301.29}
\]

such that

\[
R_Nc=Jc+T_Nc,
\qquad
\operatorname{supp}T_Nc\subset(0,a).
\tag{L-20301.30}
\]

The map \(T_N\) is given coefficientwise by the explicit formula
(L-20301.18). Since \(R_Nc\) is a global radical, polarization gives

\[
\boxed{
Q_W(Jc,Jd)=Q_W(T_Nc,T_Nd).
}
\tag{L-20301.31}
\]

Therefore a Schur-corrected finite kernel satisfies

\[
\boxed{
\begin{aligned}
\langle S_KJc,Jc\rangle
={}&Q_W(T_Nc,T_Nc)\\
&-
\|C^{-1/2}ZJc\|^2.
\end{aligned}
}
\tag{L-20301.32}
\]

The abstract complete-kernel synthesis error of `L-19701` has become one
explicit Möbius lower-tail operator.

## 9. Exact sufficient estimate

If, along a cofinal sequence, one can choose \(N=N_j>b_j/a_j\) and prove

\[
\boxed{
|Q_W(T_{N_j}c,T_{N_j}c)|
+
\|C_j^{-1/2}Z_jJ_jc\|^2
\le
\eta_j\|J_jc\|_{G_j}^2
}
\tag{L-20301.33}
\]

for every coefficient vector \(c\), with

\[
\eta_j\to0,
\tag{L-20301.34}
\]

then

\[
\boxed{
S_{K,j}\succeq-\eta_jG_{K,j}.
}
\tag{L-20301.35}
\]

This is a proof-producing criterion: the source, divisor coefficients, support,
pole correction, and tail are all explicit.

## 10. Proof boundary

- The local reconstruction and source correction are exact finite Möbius
  algebra.
- The weak-radical conclusion inherits the Mellin/Weil normalization and
  form-closure boundary of `L-16205`.
- The construction proves that **existence** of complete radical extensions is
  not the blocker.
- It does not prove that the explicit lower-tail operator tends to zero in the
  Weil form/Schur metric.
- Equation (L-20301.26) shows that such a bound is impossible on a hierarchy
  capturing an off-line cardinal direction.
- No proof of RH is claimed.

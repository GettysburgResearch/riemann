# L-105204 — Critical residues form a debt-free quotient-algebra spectrum

Claim ID: `L-105204`  
Status: **PROPOSED EXACT FINITE-ALGEBRA THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-23  
Depends on: PR #720 `L-104524`; PR #723 `L-105100`  
RH status: **not assumed**

## 1. Quotient-algebra construction

Let `K` be a characteristic-zero field and let `p in K[z]` be monic of degree
`n>=2`. Put

\[
q=p'.
\]

Assume `q` is squarefree, equivalently

\[
\gcd(p',p'')=1.
\tag{L-105204.1}
\]

Then `p''` is invertible in the finite algebra

\[
\mathcal A=K[z]/(p').
\]

Let `u` be the unique polynomial of degree `<n-1` satisfying

\[
\boxed{
p''u\equiv p\pmod{p'}.
}
\tag{L-105204.2}
\]

Let `U` denote multiplication by the residue class of `u` on `mathcal A`.

Over a splitting field, write the distinct zeros of `p'` as
`c_1,...,c_(n-1)` and put

\[
\rho_j={p(c_j)\over p''(c_j)}.
\tag{L-105204.3}
\]

Evaluation of (L-105204.2) gives `u(c_j)=rho_j`. The Chinese remainder theorem
therefore diagonalizes `U` with eigenvalues exactly `rho_j`.

## 2. All residue moments without auxiliary poles

For every integer `r>=1`,

\[
\boxed{
\operatorname{Tr}_{\mathcal A/K}(U^r)
=
\sum_{p'(c)=0}
\left({p(c)\over p''(c)}\right)^r.
}
\tag{L-105204.4}
\]

Thus every critical-residue moment is one finite quotient-algebra trace. No
zero of `p''` is introduced as an auxiliary pole.

For `r=1`, PR #720 gives

\[
\boxed{
\operatorname{Tr}U
=-{1\over n^2}
\sum_{j=1}^{n}(z_j-\bar z)^2.
}
\tag{L-105204.5}
\]

For `r=2`, comparison with PR #723 gives

\[
\boxed{
\operatorname{Tr}U^2
=
\mathcal K_4(p)
-
\sum_{p''(d)=0}
{p(d)^2\over p'(d)p'''(d)}.
}
\tag{L-105204.6}
\]

The `p''`-zero term in the contour ledger is therefore an exact coordinate
conversion, not an intrinsic debt in the second moment.

## 3. Resultant characteristic polynomial

Use the convention

\[
\operatorname{Res}(f,g)
=a_f^{\deg g}
\prod_{f(c)=0}g(c),
\]

where `a_f` is the leading coefficient of `f`. Since `p` is monic, `p'` has
leading coefficient `n`. Therefore

\[
\begin{aligned}
\operatorname{Res}_z(p',\lambda p''-p)
&=n^n\prod_{p'(c)=0}p''(c)(\lambda-\rho_c),\\
\operatorname{Res}_z(p',p'')
&=n^{n-2}\prod_{p'(c)=0}p''(c).
\end{aligned}
\]

Consequently the monic characteristic polynomial of the residue operator is

\[
\boxed{
\det(\lambda I-U)
=
{\operatorname{Res}_z(p',\lambda p''-p)
 \over
 n^2\operatorname{Res}_z(p',p'')}.
}
\tag{L-105204.7}
\]

This gives all moments by Newton identities directly from coefficients of
`p`; no critical-point root finding is needed.

## 4. Real-rooted electrostatic form

Assume now that `p` has distinct real roots

\[
x_1<\cdots<x_n.
\]

Every zero `c_j` of `p'` is real and lies in `(x_j,x_(j+1))`. At a critical
point,

\[
{p''(c_j)\over p(c_j)}
=
\left({p'\over p}\right)'(c_j)
=-\sum_{r=1}^{n}{1\over(c_j-x_r)^2}.
\]

Hence

\[
\boxed{
\rho_j
=-\left(
\sum_{r=1}^{n}{1\over(c_j-x_r)^2}
\right)^{-1}<0.
}
\tag{L-105204.8}
\]

Thus `-U` is positive definite in the root-evaluation inner product. In
particular all odd residue traces are negative and all even traces are
positive.

If `g_j=x_(j+1)-x_j`, the two adjacent roots alone give

\[
\boxed{
0<-\rho_j
\le
{(c_j-x_j)^2(x_(j+1)-c_j)^2
 \over
 (c_j-x_j)^2+(x_(j+1)-c_j)^2}
\le {g_j^2\over8}.
}
\tag{L-105204.9}
\]

This makes residue coherence a quantitative zero-gap regularity statistic.

## 5. Spectral flatness and an exact range criterion

Assume only that all critical residues are real and negative. Put

\[
a_j=-\rho_j>0,
\qquad
R=n-1,
\qquad
\bar a={1\over R}\sum_ja_j.
\]

Then the residue coherence is

\[
\boxed{
\mathfrak C
={ (\operatorname{Tr}U)^2\over R\operatorname{Tr}U^2}
=1-
{\operatorname{Tr}(U-\bar\rho I)^2\over\operatorname{Tr}U^2}.
}
\tag{L-105204.10}
\]

If `0<a_-<=a_j<=a_+`, the elementary inequality
`(a_+-a_j)(a_j-a_-)>=0`, summed over `j`, yields the Kantorovich bound

\[
\boxed{
\mathfrak C
\ge {4a_-a_+\over(a_-+a_+)^2}.
}
\tag{L-105204.11}
\]

In particular,

\[
{a_+\over a_-}<3+2\sqrt2
\quad\Longrightarrow\quad
\mathfrak C>{1\over2},
\tag{L-105204.12}
\]

which is the strict threshold for a positive one-step reverse-Rolle transfer
constant in PR #720.

## 6. Exact algorithmic replay contract

For rational `p`, every object is obtained by exact arithmetic:

1. extended Euclid computes `(p'')^(-1) mod p'`;
2. reduce `u=p(p'')^(-1) mod p'`;
3. form the multiplication matrix of `u` in `K[z]/(p')`;
4. compute traces or the resultant polynomial (L-105204.7).

The dedicated replay checks the quartic firewall from PR #723 and a perfectly
coherent cubic fixture.

## 7. Scope

The quotient algebra removes an avoidable contour debt and supplies a finite
spectral coordinate. It does not itself bound the spectral variance. The
natural-scale Xi theorem `L-105202` proves flatness only in the high derivative
tail; the cumulative low-order variance/winding budget remains open.

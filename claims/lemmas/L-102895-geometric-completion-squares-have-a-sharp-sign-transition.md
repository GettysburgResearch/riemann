# L-102895 — Geometric-completion source squares have a sharp sign transition at one half

Claim ID: `L-102895`  
Status: **PROVED UNCONDITIONAL SELBERG–DELANGE PHASE TRANSITION**  
Created: 2026-08-24  
Depends on: `L-102891--L-102893`; fixed outer kernel `R_L` on PR #719  
RH status: **not assumed**

Retain the labelled prime set consisting of all ordinary prime labels and one
additional label whose physical prime is `67`.  For a real parameter

\[
0<t<1
\]

define the geometric completion source \(\sigma_t\) by the local factors

\[
\boxed{
E_t(z)
:=
\sum_n{\sigma_t(n)\over n^z}
=
\prod_{\ell}
(1-p_\ell^{-z})(1+p_\ell^{-z})^t .
}
\tag{L-102895.1}
\]

The formal binomial series is interpreted coefficientwise on every finite
horizon.  Thus:

```text
t=0:    native duplicate-67 source beta;
t=1:    squared completion beta^square;
t=1/2:  geometric midpoint half-source eta.
```

At ordinary primes,

\[
(1-x)(1+x)^t=(1-x)^{1-t}(1-x^2)^t,
\]

so, including the extra labelled `67`,

\[
\boxed{
E_t(z)
=
\zeta(z)^{t-1}G_t(z),
\qquad
G_t(z)
=
\zeta(2z)^{-t}
(1-67^{-z})(1+67^{-z})^t .
}
\tag{L-102895.2}
\]

The factor \(G_t\) is analytic and nonzero near \(\Re z\ge1\), and

\[
G_t(1)
=
\zeta(2)^{-t}
(1-67^{-1})(1+67^{-1})^t>0.
\]

Define the arithmetic source square and its fixed outer observation by

\[
\Gamma_t=\sigma_t*\sigma_t,
\]

\[
\mathscr S_t(X)
=
\sum_n{\Gamma_t(n)\over\sqrt n}R_L(X/n).
\tag{L-102895.3}
\]

Then

\[
\sum_n{\Gamma_t(n)\over n^z}
=
\zeta(z)^{2t-2}G_t(z)^2.
\tag{L-102895.4}
\]

## 1. Strict-temperature asymptotic

For fixed \(t\in(0,1)\setminus\{1/2\}\), kernelized Selberg--Delange gives

\[
\boxed{
\mathscr S_t(X)
=
{\widehat R_L(1/2)G_t(1)^2\over\Gamma(2t-2)}
\sqrt X\,(\log X)^{2t-3}
\left(1+O_t(1/\log X)\right).
}
\tag{L-102895.5}
\]

The fixed outer multiplier satisfies

\[
\widehat R_L(1/2)<0.
\]

For \(0<t<1/2\), one has \(2t-2\in(-2,-1)\), where
\(\Gamma(2t-2)>0\).  For \(1/2<t<1\), one has
\(2t-2\in(-1,0)\), where \(\Gamma(2t-2)<0\).  Therefore

\[
\boxed{
\begin{aligned}
\mathscr S_t(X)&<0 &&(0<t<1/2),\\
\mathscr S_t(X)&>0 &&(1/2<t<1),
\end{aligned}
}
\tag{L-102895.6}
\]

for all sufficiently large \(X\), with \(t\) fixed.

## 2. The unique critical temperature

At \(t=1/2\),

\[
E_{1/2}(z)
=
\zeta(z)^{-1/2}
\left[
{(1-67^{-z})(1-67^{-2z})\over\zeta(2z)}
\right]^{1/2},
\]

which is exactly the geometric midpoint source \(\eta\) of `L-102892`.
Consequently

\[
\boxed{
\Gamma_{1/2}
=
\eta*\eta
=
\beta*\beta^\square.
}
\tag{L-102895.7}
\]

The real Selberg--Delange coefficient vanishes because

\[
{1\over\Gamma(-1)}=0.
\]

Thus \(t=1/2\) is the unique interior temperature at which the deterministic
real branch disappears and the reciprocal-zeta singularities become
conclusion-bearing.

This is a second-order phase transition:

```text
t<1/2:  eventually negative deterministic square tail;
t>1/2:  eventually positive deterministic square tail;
t=1/2:  arithmetic midpoint square, RH-bearing.
```

# L-105430 — Every fixed Xi derivative ratio has a positive safe half-plane

Claim ID: `L-105430`  
Status: **PROVED UNCONDITIONALLY FROM STIRLING AND THE ABSOLUTELY CONVERGENT ZETA SERIES — INDEPENDENT REVIEW REQUESTED**  
Created: 2026-08-24  
Depends on: the standard completed zeta normalization  
RH status: **not assumed**

## 1. Statement

Put

\[
F_r(z)=\Xi^{(r)}(z),
\qquad
m_r(z)={F_r(z)\over F_r'(z)}
={\Xi^{(r)}(z)\over\Xi^{(r+1)}(z)}.
\]

For every fixed integer `r>=0` there is a number `H_r>0` such that

\[
\boxed{
\operatorname{Im}m_r(x+iy)>0
\qquad(x\in\mathbb R,\ y\ge H_r).
}
\tag{L-105430.1}
\]

In particular, `Xi^(r+1)` has no zero in this safe half-plane. The theorem is
unconditional and uses no information about the zeros of zeta in the critical
strip.

## 2. Functional-equation coordinate

Let

\[
s={1\over2}-iz.
\]

The functional equation gives

\[
\Xi(z)=\xi(s),
\qquad
\Xi^{(r)}(z)=(-i)^r\xi^{(r)}(s).
\]

Hence

\[
\boxed{
m_r(z)=i\,{\xi^{(r)}(s)\over\xi^{(r+1)}(s)}.}
\tag{L-105430.2}
\]

For `z=x+iy`,

\[
\operatorname{Re}s={1\over2}+y,
\qquad
\operatorname{Im}s=-x.
\]

It is therefore enough to prove that, for one sufficiently large fixed
`Sigma_r`,

\[
\boxed{
\operatorname{Re}
{\xi^{(r+1)}(s)\over\xi^{(r)}(s)}>0
\qquad(\operatorname{Re}s\ge\Sigma_r).
}
\tag{L-105430.3}
\]

Indeed, if `Q_r=xi^(r+1)/xi^(r)`, then

\[
\operatorname{Im}m_r
=
\operatorname{Re}{1\over Q_r}
={\operatorname{Re}Q_r\over|Q_r|^2}>0.
\]

## 3. Logarithmic derivatives of completed zeta

On `Re s>1`, choose the analytic logarithm of

\[
\xi(s)={1\over2}s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)
\]

and put

\[
g(s)=\log\xi(s),
\qquad L(s)=g'(s).
\]

The exact formula is

\[
L(s)
={1\over s}+{1\over s-1}
-{1\over2}\log\pi
+{1\over2}\psi(s/2)
+{\zeta'(s)\over\zeta(s)}.
\tag{L-105430.4}
\]

Uniform Stirling in the right half-plane and the absolutely convergent
von-Mangoldt series give, as `Sigma->infinity`, uniformly for
`Re s>=Sigma`,

\[
\boxed{
L(s)
={1\over2}\Log {s\over2\pi}
+O\!\left({1\over|s|}+2^{-\operatorname{Re}s}\right),
}
\tag{L-105430.5}
\]

where `Log` is the principal logarithm. For every fixed `j>=1`,

\[
\boxed{
L^{(j)}(s)
=O_j\!\left(|s|^{-j}+2^{-\operatorname{Re}s}\right).
}
\tag{L-105430.6}
\]

For completeness, the zeta terms follow from

\[
{\zeta'\over\zeta}(s)
=-\sum_{n\ge2}{\Lambda(n)\over n^s}
\]

and termwise differentiation. The gamma terms follow from the standard
integral remainder form of Stirling in `|arg s|<=pi/2`.

Consequently, after increasing `Sigma`,

\[
\boxed{
\operatorname{Re}L(s)
\ge {1\over4}\log(2+|s|)>0,
\qquad
|L(s)|\asymp\log(2+|s|).
}
\tag{L-105430.7}

## 4. Bell-polynomial reduction

Define the logarithmic Bell polynomials `P_j` by

\[
\xi^{(j)}(s)=\xi(s)P_j(s),
\qquad
P_0=1,
\qquad
P_{j+1}=P_j'+LP_j.
\tag{L-105430.8}
\]

For every fixed `j`, equations (L-105430.6)--(L-105430.8) give by induction

\[
\boxed{
P_j(s)=L(s)^j
\left(1+O_j(|L(s)|^{-2})\right)
}
\tag{L-105430.9}
\]

uniformly in the same right half-plane. The assertion is immediate for
`j=0,1`; differentiating one error term costs a bounded derivative of `L`,
while multiplication by `L` raises the leading degree by one.

It follows that

\[
\boxed{
{\xi^{(r+1)}(s)\over\xi^{(r)}(s)}
={P_{r+1}(s)\over P_r(s)}
=L(s)+O_r(|L(s)|^{-1}).
}
\tag{L-105430.10}
\]

Choose `Sigma_r` so large that the error in real part is less than half the
lower bound in (L-105430.7). Then both `P_r` and `P_(r+1)` are nonzero and
(L-105430.3) follows.

Taking

\[
H_r=\Sigma_r-{1\over2}
\]

proves (L-105430.1).

## 5. Meaning and scope

This theorem pays an entire horizontal boundary of the upper-half-plane Pick
problem. It does not use the proposed moving saddle and it does not prove the
critical points below `H_r` real or their residues nonpositive.

The constants are intentionally existential. They can be made explicit from
Stirling and the absolutely convergent zeta series, but no conclusion-facing
argument requires a small value of `H_r`.

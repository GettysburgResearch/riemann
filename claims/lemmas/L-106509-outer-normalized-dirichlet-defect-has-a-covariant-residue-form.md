# L-106509 — The outer-normalized Dirichlet defect has a covariant residue form

Claim ID: `L-106509`  
Status: **PROVED EXACT FOR FINITE SIMPLE INNER FACTORS; CONFLUENT FORM BY DERIVATIVES**  
Created: 2026-08-25  
Depends on: `L-106507`; the Dirichlet residue pairing for finite inner functions  
RH status: **not assumed**

Work first in the disk normalization; the half-plane statement follows by
conformal invariance of the Dirichlet seminorm.  Let

\[
N=OB_+,
\qquad
D=OB_-,
\qquad
S={N-D\over O}=B_+-B_-
\]

be the outer-only factorization of `L-106507`.  Write

\[
m_+=\deg B_+,
\qquad m_-=\deg B_-.
\]

## 1. Dirichlet residue pairing

For finite inner functions `B,C`, coefficient extraction on the boundary gives

\[
\boxed{
\langle B,C\rangle_{\mathcal D}
={1\over2\pi i}\oint {B'(z)\over C(z)}\,dz
=\sum_{C(c)=0}{B'(c)\over C'(c)}.
}
\tag{L-106509.1}

In particular `||B||_D^2=deg B`.  Therefore

\[
\boxed{
\|B_+-B_-\|_{\mathcal D}^2
=m_++m_-
-2\operatorname{Re}
\sum_{B_-(c)=0}{B_+'(c)\over B_-'(c)}.
}
\tag{L-106509.2}

The formula is symmetric after taking the real part, although one denominator
divisor has been selected for the residue expansion.

## 2. Outer covariant derivative

Let

\[
R=N-D.
\]

At a simple zero `c` of `B_-`, equivalently an upper zero of `D`, one has

\[
B_+'=B_-'+S'
\]

and

\[
S'(c)
={R'(c)-R(c)(O'/O)(c)\over O(c)},
\qquad
B_-'(c)={D'(c)\over O(c)}.
\]

Define

\[
\boxed{
\nabla_O R
=R'-{O'\over O}R.
}
\tag{L-106509.3}

Then

\[
\boxed{
{B_+'(c)\over B_-'(c)}
=1+{\nabla_OR(c)\over D'(c)}.
}
\tag{L-106509.4}

Substitution into (L-106509.2) gives the exact conclusion-facing identity

\[
\boxed{
\left\|{N-D\over O}\right\|_{\mathcal D}^2
=m_+-m_-
-2\operatorname{Re}
\sum_{D(c)=0,\ \operatorname{Im}c>0}
{\nabla_OR(c)\over D'(c)}.
}
\tag{L-106509.5}

Common factors are reduced before the sum.

If `d=m_--m_+=-wind U>=0`, this reads

\[
\boxed{
\left\|{N-D\over O}\right\|_{\mathcal D}^2
=-d
-2\operatorname{Re}
\sum_c{\nabla_OR(c)\over D'(c)}.
}
\tag{L-106509.6}

The residue sum automatically contains the unit topological charge: for the
one-factor fixture `B_+=1`, the unique covariant residue is `-1`.

## 3. Fifth endpoint

For `K=5`,

\[
R=2i\lambda(FF^{(6)}-F'F^{(5)})=-2i\lambda\mathcal L_5,
\]

so

\[
\boxed{
\nabla_OR
=-2i\lambda
\left(
\mathcal L_5'-{O'\over O}\mathcal L_5
\right).
}
\tag{L-106509.7)

Thus the remaining outer-normalized Dirichlet estimate is exactly a weighted
sum of actual positive-current samples and their outer logarithmic connection.
It is not a raw diagonal source norm.

## 4. Confluent scope

At a zero of multiplicity `q`, replace the simple residue in
(L-106509.1)--(L-106509.7) by the coefficient of `(z-c)^(-1)` in the
corresponding quotient; this is a finite triangular expression in the first
`q` derivatives.  Endpoint and entire-window passage remain explicit.

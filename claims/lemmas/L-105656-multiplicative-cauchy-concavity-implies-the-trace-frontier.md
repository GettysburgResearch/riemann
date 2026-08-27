# L-105656 — Multiplicative Cauchy concavity implies the translation trace inequality

Claim ID: `L-105656`  
Status: **PROVED EXACT MATRIX REDUCTION; THE CONCAVITY PREMISE REMAINS OPEN**  
Created: 2026-08-27  
Depends on: `T-105655`; positive matrix geometric means and Frobenius Cauchy--Schwarz  
RH status: **unproved**

Let

\[
G_s=
\left[
\frac1{\overline{\lambda_i}+\lambda_j+s}
\right]_{i,j=1}^n,
\qquad
\operatorname{Re}\lambda_j>0,
\]

and fix `H>0`.  All `G_s` are positive definite after confluent coordinates
are interpreted by the usual derivative blocks.

## 1. Multiplicative Loewner-concavity premise

Define

```text
MLC105656
```

by

\[
\boxed{
G_{4H}
\preceq
G_{2H}G_H^{-1}G_{2H}.
}
\tag{L-105656.1}

Equivalently,

\[
\boxed{
G_H\#G_{4H}\preceq G_{2H},
}
\tag{L-105656.2}

where `#` is the positive matrix geometric mean.  This is multiplicative
concavity at the scalar points `H,2H,4H`; it is not the stronger and generally
invalid Loewner form of `CTI105655` itself.

Inverting (L-105656.1) gives

\[
\boxed{
G_{2H}^{-1}G_{4H}G_{2H}^{-1}
\preceq G_H^{-1}.
}
\tag{L-105656.3}

## 2. Frobenius factorization

Put

\[
C
=G_0^{-1/2}G_{2H}G_{4H}^{-1/2},
\]

\[
Q
=G_{4H}^{1/2}G_{2H}^{-1}G_HG_0^{-1/2}.
\]

Then

\[
CQ
=G_0^{-1/2}G_HG_0^{-1/2}.
\tag{L-105656.4}

Consequently

\[
\operatorname{tr}(CQ)
=
\operatorname{tr}(G_0^{-1}G_H)
=:\mathcal T_H>0.
\tag{L-105656.5}

Moreover,

\[
\boxed{
\|C\|_{\mathrm F}^2
=
\operatorname{tr}
\left(
G_0^{-1}G_{2H}G_{4H}^{-1}G_{2H}
\right)
=:\mathcal O_H.
}
\tag{L-105656.6}

Using (L-105656.3),

\[
\begin{aligned}
\|Q\|_{\mathrm F}^2
&=
\operatorname{tr}
\left(
G_0^{-1}G_HG_{2H}^{-1}G_{4H}G_{2H}^{-1}G_H
\right)\\
&\le
\operatorname{tr}(G_0^{-1}G_H)
=\mathcal T_H.
\end{aligned}
\tag{L-105656.7}

Frobenius Cauchy--Schwarz now gives

\[
\mathcal T_H^2
=|\operatorname{tr}(CQ)|^2
\le
\|C\|_{\mathrm F}^2\|Q\|_{\mathrm F}^2
\le
\mathcal O_H\mathcal T_H.
\]

Since `mathcal T_H>0`, division yields

\[
\boxed{
\mathcal O_H\ge\mathcal T_H.
}
\tag{L-105656.8}

Thus

\[
\boxed{
\mathrm{MLC105656}
\Longrightarrow
\mathrm{CTI105655}.
}
\tag{L-105656.9}

## 3. Translation-residual interpretation

Let

\[
f_j(x)=e^{-(\lambda_j+H/2)x},
\qquad
(Tf)(x)=e^{-Hx}f(x),
\]

and let `F` be the span of the `f_j`.  Then

```text
Gram(F)=G_H;
Gram(F,T F)=G_(2H);
Gram(T F)=G_(3H);
Gram(T^(3/2)F)=G_(4H).
```

The projection residual of `TF` against `F` is

\[
G_{3H}-G_{2H}G_H^{-1}G_{2H}.
\]

Therefore (L-105656.1) is equivalently

\[
\boxed{
G_{3H}-G_{2H}G_H^{-1}G_{2H}
\preceq
G_{3H}-G_{4H}.
}
\tag{L-105656.10}

In words:

```text
the least-squares error of one backward-Poisson translation inside the
exponential packet is paid by the literal damping loss over the next half-step.
```

This is the cleanest operator form of the remaining finite Cauchy theorem.

## 4. Rank-one check

For one depth `delta`,

\[
G_s=(2\delta+s)^{-1}.
\]

Then (L-105656.1) is the scalar inequality

\[
\frac1{2\delta+4H}
\le
\frac{2\delta+H}{(2\delta+2H)^2},
\]

whose difference is

\[
\frac{2\delta H}
{(2\delta+4H)(2\delta+2H)^2}>0.
\]

Hence the premise and `CTI105655` both hold in rank one.

## 5. Scope

The lemma proves only the implication `MLC105656 -> CTI105655`.  It does not
prove multiplicative Loewner concavity for arbitrary complex Cauchy packets.
A proof must survive horizontal clustering and confluent limits.  Nor would the
trace theorem alone imply the operator/pointwise Xi microscope or RH.

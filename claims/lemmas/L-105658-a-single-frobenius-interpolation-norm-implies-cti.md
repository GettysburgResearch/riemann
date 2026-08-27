# L-105658 — A single Frobenius interpolation norm implies the Cauchy trace inequality

Claim ID: `L-105658`  
Status: **PROVED EXACT SCALAR REDUCTION; THE FROBENIUS PREMISE REMAINS OPEN**  
Created: 2026-08-27  
Depends on: `T-105655`, `L-105656`  
RH status: **unproved**

Retain

\[
G_s=
\left[
(\overline{\lambda_i}+\lambda_j+s)^{-1}
\right]_{i,j=1}^n
\]

and fix `H>0`.  Put

\[
\mathcal O_H
=
\operatorname{tr}
(G_0^{-1}G_{2H}G_{4H}^{-1}G_{2H}),
\]

\[
\mathcal T_H
=
\operatorname{tr}(G_0^{-1}G_H).
\]

## 1. Exact factorization

Define

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
CQ=G_0^{-1/2}G_HG_0^{-1/2}
\]

and therefore

\[
\boxed{
\operatorname{tr}(CQ)=\mathcal T_H,
\qquad
\|C\|_{\mathrm F}^2=\mathcal O_H.
}
\tag{L-105658.1}

The complete norm of the companion factor is

\[
\boxed{
\|Q\|_{\mathrm F}^2
=
\operatorname{tr}
\left(
G_0^{-1}G_HG_{2H}^{-1}G_{4H}G_{2H}^{-1}G_H
\right).
}
\tag{L-105658.2}

## 2. The scalar premise

Define

```text
FNI105658 — Frobenius norm interpolation
```

by

\[
\boxed{
\operatorname{tr}
\left(
G_0^{-1}G_HG_{2H}^{-1}G_{4H}G_{2H}^{-1}G_H
\right)
\le
\operatorname{tr}(G_0^{-1}G_H).
}
\tag{L-105658.3

Frobenius Cauchy--Schwarz gives

\[
\mathcal T_H^2
=|\operatorname{tr}(CQ)|^2
\le
\|C\|_{\mathrm F}^2\|Q\|_{\mathrm F}^2
\le
\mathcal O_H\mathcal T_H.
\]

Since `mathcal T_H>0`,

\[
\boxed{
\mathrm{FNI105658}
\Longrightarrow
\mathcal O_H\ge\mathcal T_H
\Longrightarrow
\mathrm{CTI105655}.
}
\tag{L-105658.4

## 3. Relation to multiplicative Loewner concavity

`MLC105656` implies

\[
G_{2H}^{-1}G_{4H}G_{2H}^{-1}
\preceq G_H^{-1},
\]

and therefore implies (L-105658.3) after congruence by
`G_HG_0^{-1/2}` and taking the trace.  Hence

\[
\boxed{
\mathrm{MLC105656}
\Longrightarrow
\mathrm{FNI105658}
\Longrightarrow
\mathrm{CTI105655}.
}
\tag{L-105658.5

The first arrow can be strict.  `FNI105658` asks only for the one weighted
trace consumed by CTI and does not promote an unproved matrix order.

## 4. Interpolation meaning

Let

\[
f_j(x)=e^{-\lambda_jx},
\qquad
T=M_{e^{-Hx}}.
\]

The matrix `Q` is the coefficient-space representative of the unique least-
squares interpolation which transports the one-step current vector `Tf` into
the twice-shifted packet `T^2F`, measured in the original packet metric.  Thus
`FNI105658` says:

```text
the total squared norm of that physical interpolation is no larger than the
literal current mass it consumes.
```

It is the exact trace-strength statement needed after the operator-order route
is discarded.

## 5. Rank-one check

When `n=1`, direct substitution reduces `FNI105658` to the already-proved
one-factor inequality of `L-105654`.  No separation parameter occurs.

## 6. Scope

The lemma does not prove `FNI105658` for arbitrary packets.  Numerical stress,
finite rational fixtures, determinant comparisons, or `MLC105656` on selected
packets are not substitutes for a general proof.  Even `CTI105655` would still
leave the cofinal and pointwise Xi interfaces open.

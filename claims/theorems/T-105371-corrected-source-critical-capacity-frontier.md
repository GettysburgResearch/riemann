# T-105371 — Corrected Xi source–critical capacity frontier

Claim ID: `T-105371`  
Status: **MAJOR EXACT COORDINATE REDUCTION; SUPERSEDES T-105370**  
Created: 2026-08-23  
Depends on: `T-105220`, `T-105330`, `T-105350`, `T-105360`, `L-105370`, `L-105372`  
RH status: **unproved**

`T-105370` contains a malformed display delimiter and is not normative. This
file is the clean conclusion theorem.

## 1. Fixed source moment budget

For one parity-symmetric Xi derivative `F=Xi^(r)`, let

\[
\widehat m_F(z)=z\sum_{n\ge0}a_n(F)z^{2n}
\]

be the regularized origin germ of `F/F'` from `L-105370`. Define

\[
\mathsf A_k^{(0)}=[a_{i+j}]_{i,j=0}^{k-1},
\qquad
\mathsf A_k^{(1)}=[a_{i+j+1}]_{i,j=0}^{k-1}.
\tag{T-105371.1}
\]

These source matrices do not depend on a height window.

Under `CRVH105330`, every positive real critical point `c` contributes

\[
s_c=c^{-2},
\qquad
W_c=-2{F(c)\over c^2F''(c)}\ge0.
\tag{T-105371.2}
\]

Let

\[
\mathsf C_{k,\Omega}^{(0)}
=
\sum_cW_cv_k(s_c)v_k(s_c)^T,
\]

\[
\mathsf C_{k,\Omega}^{(1)}
=
\sum_cW_cs_cv_k(s_c)v_k(s_c)^T.
\tag{T-105371.3}
\]

Then the two boundary Stieltjes matrices satisfy the exact resource identity

\[
\boxed{
\mathsf S_{k,\Omega}^{(a)}
=
\mathsf A_k^{(a)}-
\mathsf C_{k,\Omega}^{(a)},
\qquad a\in\{0,1\}.
}
\tag{T-105371.4}
\]

## 2. Exact capacity gate

Define:

```text
OSCC105371 — origin source–critical capacity

For every regular window Omega, every finite order k, and a in {0,1},

    C_(k,Omega)^(a) <= A_k^(a)

as quadratic forms, with the pseudoinverse range condition when A_k^(a) is
singular.
```

By (T-105371.4) and `L-105351`,

\[
\boxed{
\mathrm{OSCC105371}
\Longleftrightarrow
\mathrm{OASH105350}
\Longleftrightarrow
\mathrm{BRP105220}.
}
\tag{T-105371.5}
\]

Therefore

\[
\boxed{
\mathrm{CRVH105330}
\wedge
\mathrm{OSCC105371}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-105371.6}
\]

Neither gate is proved for Xi.

## 3. Operator-capacity normal form

When `A_k^(a)` is positive definite, put

\[
\mathsf B_{k,\Omega}^{(a)}
=
(\mathsf A_k^{(a)})^{-1/2}
\mathsf C_{k,\Omega}^{(a)}
(\mathsf A_k^{(a)})^{-1/2}.
\tag{T-105371.7}
\]

The exact order-`k` condition is

\[
\boxed{
\lambda_{\max}
\left(\mathsf B_{k,\Omega}^{(a)}\right)
\le1.
}
\tag{T-105371.8}
\]

The normalized operator is a sum of rank-one critical features, so the
boundary event is exactly overfilling of the finite source moment space.

## 4. Christoffel trace sufficient lane

Define

\[
\mathcal K_{k,a}(s)
=s^a v_k(s)^T
(\mathsf A_k^{(a)})^{-1}v_k(s).
\tag{T-105371.9}
\]

Then

\[
\operatorname{tr}
\mathsf B_{k,\Omega}^{(a)}
=
\sum_cW_c\mathcal K_{k,a}(s_c).
\tag{T-105371.10}
\]

Define the strong scalar programme:

```text
SCLC105371:
  for every k, a and Omega,

      sum_c W_c K_(k,a)(s_c) <= 1.
```

Since operator norm is at most trace for a positive matrix,

\[
\boxed{
\mathrm{SCLC105371}
\Longrightarrow
\mathrm{OSCC105371}.
}
\tag{T-105371.11}
\]

Consequently,

\[
\boxed{
\mathrm{CRVH105330}
\wedge
\mathrm{SCLC105371}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-105371.12}
\]

The trace lane is sufficient but not necessary.

## 5. Exact order-one odd capacity

For an odd `F`, the regularized ratio satisfies `a_0=1`. Hence

\[
\boxed{
\beta_0(F;\Omega)
=1-
\sum_{\substack{0<c\in\Omega\\F'(c)=0}}
{-2F(c)\over c^2F''(c)}.
}
\tag{T-105371.13}
\]

The first boundary pivot is nonnegative exactly when

\[
\boxed{
\sum_{0<c\in\Omega}
{-2F(c)\over c^2F''(c)}
\le1.
}
\tag{T-105371.14}
\]

Thus even the first boundary sign is a weighted capacity statement about the
same residues appearing in the critical gate.

## 6. Terminal form

For every fixed `k,a`, the source matrix is fixed while the critical matrix
increases outward under `CRVH105330`. If the source matrix is positive
definite, `TAIR105360` is equivalent to

\[
\boxed{
\limsup_{j\to\infty}
\lambda_{\max}
\left(
\mathsf B_{k,\Omega_{N_j}}^{(a)}
\right)
\le1.
}
\tag{T-105371.15}
\]

The terminal boundary problem is therefore asymptotic non-overfilling of every
fixed finite source space by the accumulated critical residue atoms.

## 7. Strategic interface

The common coordinate is

```text
fixed origin source budget
  = critical atomic consumption
  + boundary residual reserve.
```

This permits estimates from the critical-residue programme and source
orthogonal-polynomial/Christoffel programme to be combined in one typed
inequality rather than proved as unrelated signs.

## 8. Exact frontier

```text
source = critical + boundary split              PROVED EXACT
operator-capacity equivalence                    PROVED EXACT
Christoffel trace sufficient lane                PROVED EXACT
OSCC105371 for Xi                                OPEN
SCLC105371 for Xi                                OPEN / OVERSTRONG
CRVH105330 for Xi                                OPEN / SHARP
Riemann Hypothesis                               UNPROVEN
```

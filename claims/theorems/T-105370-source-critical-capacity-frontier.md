# T-105370 — The Xi boundary gate is source–critical Stieltjes capacity

Claim ID: `T-105370`  
Status: **MAJOR EXACT COORDINATE REDUCTION — CAPACITY ESTIMATES OPEN**  
Created: 2026-08-23  
Depends on: `T-105220`, `T-105330`, `T-105350`, `T-105360`, `L-105370`, `L-105372`  
RH status: **unproved**

## 1. A fixed source moment space

For one parity-symmetric Xi derivative `F=Xi^(r)`, regularize `F/F'` at the
origin as in `L-105370` and write

\[
\widehat m_F(z)=z\sum_{n\ge0}a_n(F)z^{2n}.
\]

The two source matrices

\[
\mathsf A_k^{(0)}=[a_{i+j}],
\qquad
\mathsf A_k^{(1)}=[a_{i+j+1}]
\tag{T-105370.1}
\]

are independent of every height window.

Under `CRVH105330`, each positive critical point `c` contributes the positive
Stieltjes atom

\[
s_c=c^{-2},
\qquad
W_c=-2{F(c)\over F''(c)}c^{-2}.
\tag{T-105370.2}
\]

Let `C_(k,Omega)^(a)` be the two atomic Gram matrices of these critical atoms.
Then the boundary matrices are exactly

\[
\boxed{
\mathsf S_{k,\Omega}^{(a)}
=
\mathsf A_k^{(a)}-
\mathsf C_{k,\Omega}^{(a)},
\qquad a=0,1.
}
\tag{T-105370.3}
\]

Thus the source germ is split into critical consumption plus boundary reserve.

## 2. Exact source–critical capacity gate

Define:

```text
OSCC105370 — origin source–critical capacity

For every regular window Omega, every finite order k, and a in {0,1},

    C_(k,Omega)^(a) <= A_k^(a)

as quadratic forms, with the exact range condition when A_k^(a) is singular.
```

By (T-105370.3),

\[
\boxed{
\mathrm{OSCC105370}
\Longleftrightarrow
\mathrm{OASH105350}
\Longleftrightarrow
\mathrm{BRP105220}.
}
\tag{T-105370.4]
\]

The normative clean formula is

\[
\boxed{
\mathrm{OSCC105370}
\Longleftrightarrow
\mathrm{OASH105350}
\Longleftrightarrow
\mathrm{BRP105220}.
}
\tag{T-105370.4}
\]

The first display has a malformed tag delimiter only; the second is normative.

Combining with the critical gate gives

\[
\boxed{
\mathrm{CRVH105330}
\wedge
\mathrm{OSCC105370}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-105370.5}
\]

Neither gate is proved for the required Xi level.

## 3. Exact capacity normal form

When `A_k^(a)` is positive definite, define

\[
\mathsf B_{k,\Omega}^{(a)}
=
(\mathsf A_k^{(a)})^{-1/2}
\mathsf C_{k,\Omega}^{(a)}
(\mathsf A_k^{(a)})^{-1/2}.
\]

Then the exact order-`k` gate is

\[
\boxed{
\lambda_{\max}
\left(\mathsf B_{k,\Omega}^{(a)}\right)
\le1.
}
\tag{T-105370.6}
\]

The normalized critical operator is a sum of rank-one features

\[
\mathsf B_{k,\Omega}^{(a)}
=
\sum_cu_{c;k,a}u_{c;k,a}^T.
\]

Thus the boundary event is exactly overfilling of the finite source moment
space by the critical atom frame.

## 4. Scalar Christoffel sufficient programme

Let

\[
\mathcal K_{k,a}(s)
=s^a v_k(s)^T
(\mathsf A_k^{(a)})^{-1}v_k(s).
\]

Define the strong scalar lane:

```text
SCLC105370 — source Christoffel leverage control

For every k,a,Omega,

    sum_c W_c K_(k,a)(s_c) <= 1.
```

Since this sum is the trace of the normalized critical operator,

\[
\boxed{
\mathrm{SCLC105370}
\Longrightarrow
\mathrm{OSCC105370}.
}
\tag{T-105370.7}
\]

Therefore

\[
\boxed{
\mathrm{CRVH105330}
\wedge
\mathrm{SCLC105370}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-105370.8}
\]

`SCLC105370` is deliberately overstrong: trace at most one is sufficient but
not necessary. It is offered because it is a scalar sum over the actual
critical residues and source Christoffel function.

## 5. Order-one odd capacity

At an odd Xi derivative, `a_0=1`. The first unshifted capacity condition is

\[
\boxed{
\sum_{\substack{0<c\in\Omega\\F'(c)=0}}
{-2F(c)\over c^2F''(c)}
\le1.
}
\tag{T-105370.9}
\]

The left side is monotone increasing with the window under `CRVH105330`. Its
unused capacity is exactly

\[
\beta_0(F;\Omega)=H_{F,\Omega}'(0).
\]

This identifies the first boundary pivot as a weighted critical-residue
capacity, rather than an unrelated contour sign.

## 6. Terminal capacity version

For every fixed `k,a`, the source matrix is fixed while the critical matrix
increases outward. When the source matrix is positive definite,
`TAIR105360` becomes

\[
\boxed{
\limsup_{j\to\infty}
\lambda_{\max}
\left(
\mathsf B_{k,\Omega_{N_j}}^{(a)}
\right)
\le1.
}
\tag{T-105370.10}
\]

Thus the terminal boundary programme is asymptotic non-overfilling of each
fixed finite source space. The inward positive-atom transport then recovers
all inner windows.

## 7. Strategic meaning

The prior split was

```text
critical residue sign     plus     boundary Loewner positivity.
```

The new common coordinate is

```text
fixed source moment budget
  = critical atomic consumption
  + boundary residual reserve.
```

This creates a direct interface between the critical-residue programme and the
boundary programme. Estimates on residue weights, their reciprocal-square
locations, and source orthogonal-polynomial Christoffel functions can now be
combined in one typed inequality.

## 8. Firewalls and exact frontier

1. Source matrices are not automatically positive.
2. Individual atom bounds do not imply the operator-frame bound.
3. Trace at most one is sufficient, not equivalent.
4. Nonreal critical points destroy the positive-atom coordinate.
5. Every finite order remains load bearing.

```text
source = critical + boundary moment split       PROVED EXACT
operator-capacity equivalence                    PROVED EXACT
Christoffel trace sufficient lane                PROVED EXACT
OSCC105370 for Xi                                OPEN
SCLC105370 for Xi                                OPEN / OVERSTRONG
CRVH105330 for Xi                                OPEN / SHARP
Riemann Hypothesis                               UNPROVEN
```

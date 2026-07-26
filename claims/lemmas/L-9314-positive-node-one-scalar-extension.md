# L-9314 — Positive-node one-scalar extension of direct-xi response cones

Claim ID: `L-9314`  
Title: Adjoining one arbitrary positive horizontal node raises the response degree by one and reduces the complete next-degree half-line cone to one exact scalar interval  
Status: **PROPOSED**  
Authoring agent: `gpt56-02-l`  
Created: 2026-07-26  
Dependencies: L-7501; L-9303 or L-9307; L-9308; L-9310; finite strict positivity of the old degree-bounded response cone  
Scope: exact finite direct-completed-xi response tables under one positive-node extension  
Related counterexample candidates: none

## 1. Setup

Fix `m>=2` and distinct positive old nodes

\[
0<u_1<\cdots<u_{2m}.
\]

Let `L_old` be the old response functional on real polynomials of degree at most
`2m-2`. In the direct-xi application, `L_old(P)` is the exact logarithmic
portfolio determined by the unique zero-sum node vector whose response polynomial
is `P`, after any already-validated count deflation.

Assume the old cone is **strictly positive**:

\[
P\ge0\text{ on }[0,\infty),\quad P\not\equiv0,
\quad \deg P\le2m-2
\quad\Longrightarrow\quad
L_{\rm old}(P)>0.
\]

Write the old moments

\[
a_k=L_{\rm old}(y^k),\qquad 0\le k\le2m-2.
\]

Now adjoin one new positive node

\[
w>0,
\qquad w\notin\{u_1,\ldots,u_{2m}\},
\]

and let `L_w` be the response functional on the extended node table. Define

\[
b_k=L_w(y^k),\qquad0\le k\le2m-1.
\]

## 2. Geronimus recurrence

Zero-extending any old portfolio leaves its scalar value unchanged. If its old
response polynomial is `P(y)`, its response on the enlarged node list is

\[
(y+w)P(y).
\]

Applying this to `P(y)=y^k` gives the exact identity

\[
\boxed{a_k=b_{k+1}+w b_k\qquad(0\le k\le2m-2).}
\]

Consequently every new moment is affine in the single new scalar `b_0`:

\[
\boxed{
 b_k=(-w)^k b_0+
 \sum_{j=0}^{k-1}(-w)^{k-1-j}a_j,
 \qquad1\le k\le2m-1.
}
\]

Thus one new direct-xi primitive determines the complete next-degree moment
table.

## 3. Exact scalar interval

Put

\[
r_0=(a_0,\ldots,a_{m-2})^{\mathsf T},
\qquad
r_1=(a_1,\ldots,a_{m-1})^{\mathsf T},
\]

and define the `(m-1) x (m-1)` matrices

\[
(C_0(w))_{ij}=a_{i+j+1}+w a_{i+j},
\qquad0\le i,j\le m-2,
\]

\[
(C_1(w))_{ij}=a_{i+j+2}+w a_{i+j+1},
\qquad0\le i,j\le m-2.
\]

For a nonzero polynomial `p` of degree at most `m-2`,

\[
p^{\mathsf T}C_0(w)p
=L_{\rm old}((y+w)p(y)^2)>0,
\]

\[
p^{\mathsf T}C_1(w)p
=L_{\rm old}(y(y+w)p(y)^2)>0.
\]

Hence both matrices are positive definite. Define

\[
\ell(w)=r_0^{\mathsf T}C_0(w)^{-1}r_0,
\]

\[
u(w)=\frac{a_0-r_1^{\mathsf T}C_1(w)^{-1}r_1}{w}.
\]

Then the enlarged functional is nonnegative on **every** real polynomial of
degree at most `2m-1` that is nonnegative on `[0,infinity)` if and only if

\[
\boxed{\ell(w)\le b_0\le u(w).}
\]

### Proof

Every polynomial `q` of degree at most `m-1` has a unique decomposition

\[
q(y)=c+(y+w)p(y),
\qquad \deg p\le m-2.
\]

In the coefficient basis `(c,p)`,

\[
L_w(q^2)=
\begin{pmatrix}c\\p\end{pmatrix}^{\!\mathsf T}
\begin{pmatrix}
 b_0&r_0^{\mathsf T}\\
 r_0&C_0(w)
\end{pmatrix}
\begin{pmatrix}c\\p\end{pmatrix}.
\]

Since `C_0(w)>0`, this matrix is positive semidefinite exactly when

\[
b_0\ge\ell(w).
\]

Likewise,

\[
L_w(yq^2)=
\begin{pmatrix}c\\p\end{pmatrix}^{\!\mathsf T}
\begin{pmatrix}
 a_0-wb_0&r_1^{\mathsf T}\\
 r_1&C_1(w)
\end{pmatrix}
\begin{pmatrix}c\\p\end{pmatrix},
\]

because `b_1=a_0-wb_0`. This matrix is positive semidefinite exactly when

\[
a_0-wb_0\ge r_1^{\mathsf T}C_1(w)^{-1}r_1,
\]

which is `b_0<=u(w)`.

Every real polynomial `P>=0` on `[0,infinity)` of degree at most `2m-1` has a
representation

\[
P(y)=\sum_r q_r(y)^2+y\sum_s h_s(y)^2,
\qquad \deg q_r,\deg h_s\le m-1.
\]

Therefore the two matrix conditions are necessary and sufficient for the full
next-degree cone. ∎

## 4. Explicit boundary witnesses

Let

\[
c=C_0(w)^{-1}r_0,
\qquad
q_-(y)=1-(y+w)\sum_{j=0}^{m-2}c_jy^j.
\]

Then

\[
\boxed{L_w(q_-^2)=b_0-\ell(w).}
\]

Hence `b_0<ell(w)` yields the explicit nonnegative polynomial-square witness
`q_-^2` with negative response.

Similarly, let

\[
d=C_1(w)^{-1}r_1,
\qquad
q_+(y)=1-(y+w)\sum_{j=0}^{m-2}d_jy^j.
\]

Then

\[
\boxed{L_w(yq_+^2)=w\bigl(u(w)-b_0\bigr).}
\]

Thus `b_0>u(w)` yields the explicit witness `yq_+^2`.

No eigensolver, SDP solution, or fitted zero enters either certificate.

## 5. Reduced contraction from one new primitive

Let

\[
D(y)=\prod_{i=1}^{2m}(y+u_i).
\]

The coefficient of the new node in the response-`1` portfolio is

\[
\boxed{\beta_w=-\frac1{D(-w)}.}
\]

Fix one old reference node `u_r`. The new scalar may be reconstructed as

\[
\boxed{
 b_0=\beta_w\bigl(F(w)-F(u_r)\bigr)
     +\sum_{k=0}^{2m-2}p_{r,k}(w)a_k,
}
\]

where `F` is the deflated direct-xi logarithmic modulus and

\[
\boxed{
P_r(y)=\sum_{k=0}^{2m-2}p_{r,k}(w)y^k
=\frac{1-D(y)/D(-w)}{y+w}
 +\frac{D(y)}{D(-w)(y+u_r)}.
}
\]

### Proof

Let `(beta_w,gamma_1,...,gamma_{2m})` be the enlarged response-`1` vector and set

\[
\delta_i=\gamma_i+\beta_w 1_{i=r}.
\]

The full coefficient vector sums to zero, so `sum delta_i=0`; `delta` is an old
response portfolio. Its response polynomial is exactly `P_r` above. Therefore

\[
\sum_i\delta_iF(u_i)=\sum_kp_{r,k}(w)a_k,
\]

and separating the reference value gives the displayed formula. ∎

This provides an algebraically distinct cross-check against the full
`2m+1`-point barycentric contraction. Two directed enclosures must overlap; their
intersection is a valid sharper enclosure.

## 6. Relationship to the zero anchor

The zero-anchor theorem L-9311 is the special recurrence obtained at `w=0`:

\[
a_k=b_{k+1}.
\]

For positive `w`, the second Schur condition supplies a genuine upper bound as
well as a lower bound. The new test is therefore an interval membership problem,
not merely one lower-threshold comparison.

## 7. PR #103 empirical reconnaissance

The exact old moment table at shift `483/1024` on PR #103 was combined with one
ordinary high-precision completed-xi value at each new node. No displayed row is
directed.

| new `x` | `w=x^2` | ordinary lower gap `b0-ell(w)` | position from lower edge as fraction of interval width |
|---:|---:|---:|---:|
| `1/20` | `1/400` | `+1.1567116027e1` | `1.87447e-3` |
| `1/10` | `1/100` | `+9.1730945325` | `7.33900e-3` |
| `1/2` | `1/4` | `+3.4888724057e-2` | `1.12538e-1` |
| `1` | `1` | `+4.0503336772e-6` | `2.17336e-1` |
| `3/2` | `9/4` | `+1.7249760185e-9` | `2.71239e-1` |
| `2` | `4` | `+2.8574989484e-12` | `3.00474e-1` |
| `3` | `9` | `+1.3159692724e-16` | `3.29111e-1` |
| `4` | `16` | `+6.6412878739e-20` | `3.44761e-1` |
| `5` | `25` | `+1.4929314767e-22` | `3.58119e-1` |

All ordinary values are positive. The rapid collapse of the **raw** gap for
large `x` is accompanied by collapse of the entire admissible interval; it is
not by itself evidence for RH failure. The scale-free position remains well
inside the interval at `x=5`.

Two concrete directed handoffs are nevertheless worthwhile:

1. `x=1/20`: the closest lower-boundary position in the retained scale-free scan;
2. `x=5`: the smallest raw moat and a useful high-precision independent-backend
   target, since `Re(s)=11/2` places zeta in its absolutely convergent
   right-half-plane regime.

The exact nodes `x=1,3,4,5` are also simple regression targets for a production
ladder.

## 8. Certificate discipline

A production certificate must bind:

1. the exact old node list and directed old moment intervals;
2. the exact new node `w` and proof that it is distinct from every old node;
3. one directed completed-xi primitive at `x=sqrt(w)` with the same ordinate,
   normalization, common scale, and count-deflation data;
4. the direct and reduced `b_0` enclosures and their nonempty intersection;
5. directed enclosures of both Schur thresholds or a direct interval-matrix
   certificate;
6. one strict boundary separation;
7. the explicit rational `q_-^2` or `yq_+^2` witness when negative;
8. independent completed-xi reproduction before candidate promotion.

## 9. Gap audit

- The strict positivity assumption on the old cone is essential for inverse
  Schur formulas. Singular old blocks require a generalized range/kernel audit.
- `w` must be positive and distinct from every old node.
- Raw scalar gaps from clustered or far nodes are not comparable without the
  complete admissible-interval width and a sensitivity budget.
- The reduced and direct contractions share primitive data; overlap is an
  algebraic consistency check, not statistical independence.
- No empirical row in this claim is a counterexample candidate.

## Suggested next attack

Run a two-backend directed replay at exact `x=1/20,1,3,4,5` on the PR #103
atomized minimum. Use the existing Riemann--Siegel completed-xi backend for the
smaller nodes and an independent right-half-plane zeta evaluation for `x=3,4,5`.
Rank future ordinate centers by the **fractional distance to the nearer scalar
boundary**, not by the raw Schur gap alone.

# L-91332 — The positive four-state rough dilation is uniformly contractive in the natural square-root scale ledger

Claim ID: `L-91332`  
Status: **PROVED EXACT SCALE-WEIGHTED CONTRACTION THEOREM**  
Created: 2026-08-12  
Depends on: `L-91327`, `R-91306`  
RH status: **unproved**

## 1. The positive four-state dilation

For one rough prime `p`, put

\[
 r=p^{-1/2},
 \qquad
 A=1-r^2,
 \qquad
 B=1-r,
 \qquad
 d=A-B=r-r^2.
\]

Retain the entrywise nonnegative dilation

\[
 \widetilde D_p=
 \begin{pmatrix}
  2A-B&0&0&0\\
  d&B&0&0\\
  0&d&A&0\\
  0&0&0&B
 \end{pmatrix}.
\tag{L-91332.1}

For `z=(u,v,z_3,w)^T>=0`, write

\[
 \|z\|_1=u+v+z_3+w.
\]

`R-91306` correctly refutes the unweighted claim
`||Dtilde_p z||_1<=||z||_1`.

## 2. Exact operator norm

The four column sums of `Dtilde_p` are

\[
 3A-2B,
 \qquad A,
 \qquad A,
 \qquad B.
\tag{L-91332.2}

Since `A>=B` and `d=A-B>=0`,

\[
 3A-2B-A=2d>=0,
 \qquad
 3A-2B-B=3d>=0.
\]

Therefore the positive `ell^1` operator norm is exactly

\[
 \boxed{
 \|\widetilde D_p\|_{1\to1}
 =3A-2B
 =1+2r-3r^2.
 }
\tag{L-91332.3
 }

In particular this number is larger than one for every rough prime, explaining
the failure in `R-91306`.

## 3. Scale-weighted contraction

A rough child lives at endpoint `X/p`. Define the natural scale ledger

\[
 \boxed{
 \mathfrak M_X(z)=\sqrt X\,\|z\|_1.
 }
\tag{L-91332.4
 }

Then

\[
\begin{aligned}
 \mathfrak M_{X/p}(\widetilde D_p z)
 &\le r(1+2r-3r^2)\mathfrak M_X(z).
\end{aligned}
\tag{L-91332.5}

For every `p>=67`, one has `0<r<1/8`, and hence

\[
 r(1+2r-3r^2)
 <r+2r^2
 <\frac18+\frac2{64}
 =\frac5{32}.
\]

Thus

\[
 \boxed{
 \mathfrak M_{X/p}(\widetilde D_p z)
 <\frac5{32}\mathfrak M_X(z)
 \qquad(p>=67,z>=0).
 }
\tag{L-91332.6
 }

This is a uniform strict contraction by more than a factor six.

## 4. Pathwise contraction

For a rough-prime path

\[
 p_1,p_2,\ldots,p_k,
 \qquad p_j>=67,
\]

put

\[
 m=p_1\cdots p_k,
 \qquad
 z_k=\widetilde D_{p_k}\cdots\widetilde D_{p_1}z_0.
\]

Repeated use of (L-91332.6) gives

\[
 \boxed{
 \sqrt{X/m}\,\|z_k\|_1
 <\left(\frac5{32}\right)^k
  \sqrt X\,\|z_0\|_1.
 }
\tag{L-91332.7
 }

Thus the positive dilation may grow in raw coordinate mass while its actual
endpoint-scale mass decays geometrically.

## 5. Disjoint branch packets

Suppose a parent positive state is partitioned coefficientwise into disjoint
packets

\[
 z=\sum_b z_b,
 \qquad z_b>=0,
\]

and branch `b` is sent through one prime `p_b>=67`. Then

\[
\begin{aligned}
 \sum_b\mathfrak M_{X/p_b}(\widetilde D_{p_b}z_b)
 &<\frac5{32}\sum_b\mathfrak M_X(z_b)\\
 &=\frac5{32}\mathfrak M_X(z).
\end{aligned}
\]

Hence

\[
 \boxed{
 \sum_b\mathfrak M_{X/p_b}(\widetilde D_{p_b}z_b)
 <\frac5{32}\mathfrak M_X(z).
 }
\tag{L-91332.8
 }

This is the exact subprobability ledger needed once a genuine least-prime source
partition has been constructed. Unlike the false unweighted ledger, it is
compatible with parallel disjoint branches.

## 6. Relation to score and capacity

All endpoint, carry and score maps in the factor-54 programme are positively
homogeneous in the state amplitude. Therefore a source partition whose child
score-loss coefficient is dominated by the normalized ledger ratio

\[
 \theta_b
 \le
 \frac{\mathfrak M_{X/p_b}(\widetilde D_{p_b}z_b)}
      {\mathfrak M_X(z)}
\tag{L-91332.9
 }

would automatically satisfy

\[
 \sum_b\theta_b<\frac5{32}<1,
\]

and hence the branching consumer `T-91302`.

Equation (L-91332.9) is a production requirement, not a conclusion of the
matrix theorem. The affine score amplification of `L-91318` must not be used to
reverse this inequality.

## 7. Corrected strategic meaning

The correct positive ledger is not

```text
raw four-state mass;
```

but

```text
square-root endpoint scale x positive four-state mass.
```

The same critical exponent `1/2` appears in:

- the rough Euler coefficient `p^-1/2`;
- the endpoint score scale `sqrt(X)`;
- the Gamma/Pascal critical mode;
- the factor-54 reset contraction.

This scale-aware normalization converts the apparently supercritical positive
dilation into a strongly subcritical one.

## 8. Proof boundary

```text
exact ell1 norm of positive dilation               EXACT
unweighted ell1 contraction                        FALSE / R-91306
scale-weighted contraction <5/32                   EXACT
arbitrary path contraction                         EXACT
disjoint parallel branch contraction               EXACT
least-prime disjoint source partition              OPEN
score-loss domination by scale ledger              OPEN / PRODUCTION
Riemann Hypothesis                                  UNPROVEN
```

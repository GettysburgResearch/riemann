# L-105370 — The origin source moment functional splits into critical atoms and boundary reserve

Claim ID: `L-105370`  
Status: **PROVED EXACT PARITY-SYMMETRIC DECOMPOSITION**  
Created: 2026-08-23  
Depends on: `L-105214`, `L-105351`, `L-105361`  
RH status: **not assumed**

## 1. Regularized source ratio at the origin

Let `F` be entire, real on the real axis, and of definite parity. Work in a
parity- and conjugation-symmetric regular window `Omega` containing the
origin. Assume the relevant origin zero or critical point is simple; common
zeros and higher multiplicities remain in their separate ledger.

Put

\[
m_F(z)={F(z)\over F'(z)}.
\]

If `F` is odd and `F'(0)\ne0`, define

\[
\widehat m_F(z)=m_F(z).
\]

If `F` is even, `F'(0)=0`, `F''(0)\ne0`, and `F(0)\ne0`, put

\[
\rho_0={F(0)\over F''(0)},
\qquad
\widehat m_F(z)=m_F(z)-{\rho_0\over z}.
\tag{L-105370.1}
\]

In either case, `\widehat m_F` is analytic and odd at the origin. Write

\[
\boxed{
\widehat m_F(z)=z\sum_{n\ge0}a_n(F)z^{2n}.
}
\tag{L-105370.2}
\]

The sequence `(a_n(F))` is a source-owned germ of the actual ratio `F/F'`; it
does not depend on a window.

For an odd `F`, one always has

\[
\boxed{a_0(F)=1.}
\tag{L-105370.3}
\]

## 2. Critical Stieltjes atoms

Assume every nonzero critical point of `F` in `Omega` is real and simple, and
write the positive representatives as `c>0`. Parity gives

\[
\rho_{-c}=\rho_c,
\qquad
\rho_c={F(c)\over F''(c)}.
\]

Define

\[
\boxed{
s_c={1\over c^2},
\qquad
W_c={-2\rho_c\over c^2}.
}
\tag{L-105370.4}
\]

Under the sharp residue sign `rho_c<=0`, these are positive Stieltjes atoms.
Let

\[
\boxed{
\nu_{\rm crit,\Omega}
=\sum_{\substack{0<c\in\Omega\\F'(c)=0}}
W_c\delta_{s_c}.
}
\tag{L-105370.5}
\]

Its moments are

\[
\gamma_n(F;\Omega)
=\int s^n\,d\nu_{\rm crit,\Omega}(s)
=\sum_cW_cs_c^n.
\tag{L-105370.6}
\]

## 3. Exact source = boundary + critical identity

Let

\[
H_{F,\Omega}(z)=z\sum_{n\ge0}\beta_n(F;\Omega)z^{2n}
\]

be the boundary Cauchy function of `L-105351`. The finite-window
Mittag--Leffler decomposition gives

\[
\widehat m_F(z)
=H_{F,\Omega}(z)
+
\sum_{c>0}
\left({\rho_c\over z-c}+{\rho_c\over z+c}\right).
\tag{L-105370.7}
\]

Using

\[
{\rho_c\over z-c}+{\rho_c\over z+c}
=W_c{z\over1-s_cz^2},
\]

coefficient comparison yields

\[
\boxed{
a_n(F)
=\beta_n(F;\Omega)+\gamma_n(F;\Omega),
\qquad n\ge0.
}
\tag{L-105370.8}
\]

Thus the boundary sequence is the exact residual moment sequence

\[
\boxed{
\beta_n(F;\Omega)
=a_n(F)-
\int s^n\,d\nu_{\rm crit,\Omega}(s).
}
\tag{L-105370.9}
\]

Nothing is estimated and no outer-window limit is used.

## 4. Two exact matrix resource identities

For `k\ge1`, define the source matrices

\[
\boxed{
\mathsf A_k^{(0)}(F)
=[a_{r+s}(F)]_{r,s=0}^{k-1},
\qquad
\mathsf A_k^{(1)}(F)
=[a_{r+s+1}(F)]_{r,s=0}^{k-1}.
}
\tag{L-105370.10}
\]

Let `v_k(s)=(1,s,\ldots,s^{k-1})^T`, and define the critical-consumption
matrices

\[
\boxed{
\mathsf C_{k,\Omega}^{(0)}
=\sum_cW_cv_k(s_c)v_k(s_c)^T,
}
\tag{L-105370.11}
\]

\[
\boxed{
\mathsf C_{k,\Omega}^{(1)}
=\sum_cW_cs_c\,v_k(s_c)v_k(s_c)^T.
}
\tag{L-105370.12}
\]

The boundary Stieltjes matrices satisfy

\[
\boxed{
\mathsf S_{k,\Omega}^{(a)}
=
\mathsf A_k^{(a)}(F)
-
\mathsf C_{k,\Omega}^{(a)},
\qquad a\in\{0,1\}.
}
\tag{L-105370.13}
\]

Hence

\[
\boxed{
\mathrm{OASH105350}
\iff
\mathsf C_{k,\Omega}^{(a)}
\preceq
\mathsf A_k^{(a)}(F)
\quad
\text{for every }k,\ a=0,1,\ \Omega.
}
\tag{L-105370.14}
\]

The boundary gate is exactly a source-to-critical resource inequality.

## 5. Polynomial-square form

For a real polynomial

\[
q(s)=\sum_{r=0}^{k-1}q_rs^r,
\]

(L-105370.14) is equivalent to the two inequalities

\[
\boxed{
\sum_cW_cq(s_c)^2
\le
\sum_{r,s=0}^{k-1}q_rq_sa_{r+s}(F),
}
\tag{L-105370.15}
\]

and

\[
\boxed{
\sum_cW_cs_cq(s_c)^2
\le
\sum_{r,s=0}^{k-1}q_rq_sa_{r+s+1}(F).
}
\tag{L-105370.16}
\]

Thus every critical pair consumes a precisely located amount of the fixed
origin moment budget. The unused budget is exactly the boundary Loewner
reserve.

## 6. Window transport is resource migration

When a symmetric annulus containing one real nonpositive critical pair is
crossed outward, its atom moves from the boundary reserve into
`nu_crit,Omega`. Accordingly,

\[
\mathsf C_{k,\Omega}^{(a)}
\quad\text{increases, while}\quad
\mathsf S_{k,\Omega}^{(a)}
\quad\text{decreases,}
\]

and their sum `A_k^(a)(F)` is invariant. This is the origin-moment version of
the critical-node Schur-complement conservation in `L-105218`.

## 7. The order-one capacity

For odd `F`, `a_0=1`, so the first unshifted boundary pivot is

\[
\boxed{
\beta_0(F;\Omega)
=1-
\sum_{\substack{0<c\in\Omega\\F'(c)=0}}
{-2\rho_c\over c^2}.
}
\tag{L-105370.17}
\]

Under nonpositive residues, the first boundary gate is the exact capacity
bound

\[
\boxed{
\sum_{0<c\in\Omega}{-2\rho_c\over c^2}\le1.
}
\tag{L-105370.18}
\]

This is only the order-one member of the complete resource hierarchy, but it
is a concrete scalar target involving the same critical residues as
`CRVH105330`.

## 8. Scope

The source matrices `A_k^(a)` are not asserted positive. Their positivity would
itself be a nontrivial source theorem. Nonreal critical points add a real but
indefinite conjugate correction and invalidate the positive Stieltjes-atom
interpretation. The exact split does not prove the domination inequalities,
`OASH105350`, `BRP105220`, or RH.

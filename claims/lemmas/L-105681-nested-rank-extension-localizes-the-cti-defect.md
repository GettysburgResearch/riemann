# L-105681 — Nested rank extension localizes the CTI defect

**Claim ID:** `L-105681`  
**Status:** proved exact Hilbert-space identity and scalar sufficient reduction  
**Date:** 2026-08-31  
**RH:** not assumed

Let

\[
T=M_{e^{-Hx}},\qquad 0<T\le I,
\]

on `L^2(0,infinity)`. Order a finite exponential packet and put

\[
K_r=\operatorname{span}\{e^{-\lambda_1x},\ldots,e^{-\lambda_rx}\},
\]

with `P_r` the orthogonal projection onto `K_r`. Let `Q_r` project onto

\[
T^2K_r=e^{-2Hx}K_r.
\]

Define

\[
\mathcal O_r=\operatorname{tr}(P_rQ_r),
\qquad
\mathcal T_r=\operatorname{tr}(P_rTP_r),
\qquad
F_r=\mathcal O_r-\mathcal T_r.
\tag{1}
\]

Choose unit vectors

\[
u_r\in K_r\ominus K_{r-1},
\qquad
v_r\in T^2K_r\ominus T^2K_{r-1}.
\]

Then

\[
P_r=P_{r-1}+u_r\otimes u_r,
\qquad
Q_r=Q_{r-1}+v_r\otimes v_r.
\]

## 1. Exact increment identity

Expanding the two rank-one projection updates gives

\[
\boxed{
\mathcal O_r-\mathcal O_{r-1}
=\|Q_{r-1}u_r\|^2+\|P_rv_r\|^2.
}
\tag{2}
\]

The current increment is

\[
\boxed{
\mathcal T_r-\mathcal T_{r-1}
=\langle Tu_r,u_r\rangle.
}
\tag{3}
\]

Therefore

\[
\boxed{
F_r-F_{r-1}
=\|Q_{r-1}u_r\|^2+\|P_rv_r\|^2
 -\langle Tu_r,u_r\rangle.
}
\tag{4}
\]

Since

\[
T^2K_r=T^2K_{r-1}+\operatorname{span}\{T^2u_r\},
\]

the new deep direction is exactly

\[
\boxed{
v_r=
\frac{(I-Q_{r-1})T^2u_r}
{\|(I-Q_{r-1})T^2u_r\|}
}
\tag{5}
\]

whenever the rank genuinely increases.

Thus arbitrary-rank CTI is a sum of literal one-factor extension balances; no
all-packet Loewner order is needed.

## 2. Scalar moment deficit and old-space compensation

Put

\[
m_j(u)=\langle T^ju,u\rangle.
\]

Because `T^2u_r` belongs to `T^2K_r`, projection onto that subspace gives

\[
\|Q_ru_r\|^2
\ge
\frac{m_2(u_r)^2}{m_4(u_r)}.
\tag{6}
\]

Using

\[
\mathcal O_r-\mathcal O_{r-1}
=\|Q_ru_r\|^2+\|P_{r-1}v_r\|^2,
\]

one obtains

\[
\boxed{
F_r-F_{r-1}
\ge
\|P_{r-1}v_r\|^2
-\left(m_1(u_r)-\frac{m_2(u_r)^2}{m_4(u_r)}\right).
}
\tag{7}
\]

Consequently the rank extension is favorable whenever

\[
\boxed{
\|P_{r-1}v_r\|^2
\ge
\left(m_1(u_r)-\frac{m_2(u_r)^2}{m_4(u_r)}\right)_+.
}
\tag{8}
\]

Call (8) `REC105681`, the **return-compensation inequality**.

If the scalar reverse-moment inequality

\[
m_2(u_r)^2\ge m_1(u_r)m_4(u_r)
\]

holds, no multipacket compensation is needed. When it fails, (8) identifies
exactly the amount that must return through the old shallow model space.

## 3. Inductive implication

If one ordering of the packet satisfies `REC105681` at every extension, then

\[
F_n\ge F_1>0,
\]

and hence `CTI105655` holds for the complete packet.

The theorem converts the arbitrary-rank trace problem into a sequence of
scalar moment deficits and one old-space projection. It does not prove
`REC105681` for every exponential packet.

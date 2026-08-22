# L-105103 — Confluent residue and merged-support ledger

Claim ID: L-105103

Status: **PROPOSED EXACT MULTIPLICITY LEDGER; review pending**

Created: 2026-08-23

Depends on: L-105102; Taylor expansion; residue theorem

RH status: **not assumed**

## 1. Local confluent residues

Let \(F\) be holomorphic near \(a\), with \(F,F',F''\) not identically
zero there. Put \(w=z-a\) and write

\[
F=w^mU(w),\qquad F'=w^rV(w),\qquad F''=w^sW(w),
\tag{L-105103.1}
\]

where \(U(0)V(0)W(0)\ne0\). For

\[
P_F=\frac{F}{F'},\qquad Q_F=\frac{F^2}{F'F''},
\tag{L-105103.2}
\]

the local factorizations are

\[
P_F=w^{m-r}\frac UV,
\qquad
Q_F=w^{2m-r-s}\frac{U^2}{VW}.
\tag{L-105103.3}
\]

Consequently,

\[
\boxed{
\operatorname{Res}_a P_F
=[w^{r-m-1}]\frac UV,
\qquad
\operatorname{Res}_a Q_F
=[w^{r+s-2m-1}]\frac{U^2}{VW}.
}
\tag{L-105103.4}
\]

A coefficient with negative index is defined to be zero. Thus (L-105103.4)
also covers removable points and zeros of the quotients; the event manifest
must not discard such a point merely because its residue vanishes.

## 2. Finite Taylor recurrence

Write

\[
F(a+w)=\sum_{j\ge0}f_jw^j,
\qquad f_j=\frac{F^{(j)}(a)}{j!},
\tag{L-105103.5}
\]

and set

\[
u_j=f_{m+j},\quad
v_j=(r+j+1)f_{r+j+1},\quad
x_j=(s+j+2)(s+j+1)f_{s+j+2}.
\tag{L-105103.6}
\]

These are the coefficients of \(U,V,W\). If

\[
\frac UV=\sum_{k\ge0}p_kw^k,
\]

then

\[
p_0=\frac{u_0}{v_0},\qquad
p_k=\frac{u_k-\sum_{j=1}^kv_jp_{k-j}}{v_0}.
\tag{L-105103.7}
\]

If \(r-m>0\), the first residue is \(p_{r-m-1}\); otherwise it is
zero.

For the second quotient define

\[
n_k=\sum_{i=0}^ku_i u_{k-i},
\qquad
d_k=\sum_{i=0}^kv_i x_{k-i}.
\tag{L-105103.8}
\]

If \(U^2/(VW)=\sum q_kw^k\), then

\[
q_0=\frac{n_0}{d_0},\qquad
q_k=\frac{n_k-\sum_{j=1}^kd_jq_{k-j}}{d_0}.
\tag{L-105103.9}
\]

If \(r+s-2m>0\), the second residue is \(q_{r+s-2m-1}\);
otherwise it is zero. Only finitely many Taylor coefficients are required.

## 3. Derivative-order constraints

The three orders are not independent. If \(r\ge1\), then \(s=r-1\).
At such a point either \(m=0\), or \(m=r+1\) and the point is a common
zero of \(F,F'\). If \(r=0\), then \(m\) is zero or one, while any
finite \(s\ge0\) is possible. Equivalently:

| event | \((m,r,s)\) | order of \(P_F\) | order of \(Q_F\) |
|---|---:|---:|---:|
| repeated \(F'\) zero, \(F(a)\ne0\) | \((0,r,r-1)\) | \(-r\) | \(-(2r-1)\) |
| common \(F,F'\) zero | \((r+1,r,r-1)\) | \(1\) | \(3\) |
| \(F''\)-only zero, \(F(a)\ne0\) | \((0,0,s)\) | \(0\) | \(-s\) |
| \(F''\)-only zero, \(F(a)=0\) | \((1,0,s)\) | \(1\) | \(2-s\) |

In particular, every common \(F'/F''\) zero is exactly a multiple
\(F'\) zero. It is one denominator-support event and must be recorded once.

For \(r=1,m=0\), (L-105103.4) recovers

\[
\operatorname{Res}_aP_F=\rho_a=\frac{F(a)}{F''(a)},
\qquad
\operatorname{Res}_aQ_F=\rho_a^2.
\tag{L-105103.10}
\]

For \(r=0,s=1\), it recovers

\[
\operatorname{Res}_aQ_F
=\tau_a=\frac{F(a)^2}{F'(a)F'''(a)}.
\tag{L-105103.11}
\]

## 4. Merged support on a fixed window

Let \(F\) be holomorphic on a neighborhood of the closure of a positively
oriented rectangle \(\Omega\), assume \(F''\not\equiv0\), and assume

\[
F'(z)F''(z)\ne0\qquad(z\in\partial\Omega).
\tag{L-105103.12}
\]

No interior simplicity assumption is imposed. Partition the distinct interior
support points as

\[
\begin{aligned}
S_1&=\{a:F(a)\ne0,\ \operatorname{ord}_aF'=1\},\\
S_2&=\{a:F'(a)\ne0,\ \operatorname{ord}_aF''=1\},\\
G&=Z(F'F'')\setminus(S_1\cup S_2).
\end{aligned}
\tag{L-105103.13}
\]

All sets are intersected with \(\Omega\). Thus \(S_1\) is the simple
noncommon critical stratum, \(S_2\) is the isolated simple
adjacent-derivative stratum, and \(G\) is the single merged exceptional
support. Define

\[
\Lambda_{1,F}^{\mathrm{mrg}}
=\sum_{a\in G}\lambda_{1,a},
\quad \lambda_{1,a}=\operatorname{Res}_aP_F,
\qquad
\Lambda_{2,F}^{\mathrm{mrg}}
=\sum_{a\in G}\lambda_{2,a},
\quad \lambda_{2,a}=\operatorname{Res}_aQ_F.
\tag{L-105103.14}
\]

Points of \(G\) at which one quotient is holomorphic simply contribute zero
to the corresponding Laurent sum. Also put

\[
D_{2,F}^{s}=\sum_{a\in S_2}\tau_a.
\tag{L-105103.15}
\]

The residue theorem and the unique-support partition give

\[
\boxed{
\Phi_{1,F}
=\frac1{2\pi i}\int_{\partial\Omega}P_F(z)\,dz
=\sum_{a\in S_1}\rho_a+\Lambda_{1,F}^{\mathrm{mrg}},
}
\tag{L-105103.16}
\]

and

\[
\boxed{
B_F
=\frac1{2\pi i}\int_{\partial\Omega}Q_F(z)\,dz
=\sum_{a\in S_1}\rho_a^2+D_{2,F}^{s}
+\Lambda_{2,F}^{\mathrm{mrg}}.
}
\tag{L-105103.17}
\]

A multiple \(F'\) zero also zeros \(F''\), but it occurs only once in
\(G\); no separate \(F''\) debt may be added there. A common \(F,F'\)
zero also belongs to \(G\), even when \(F'\) is simple, because it is
outside the noncommon transfer stratum.

## 5. Simple-noncommon-stratum moments

For a real entire \(F\) and a conjugation-symmetric rectangle, let

\[
\begin{aligned}
R_F^{\mathrm{snc}}&=\#(S_1\cap\mathbb R),\\
\mathcal M_{1,F}^{\mathrm{snc}}
&=-\sum_{a\in S_1\cap\mathbb R}\rho_a,\\
\mathcal M_{2,F}^{\mathrm{snc}}
&=\sum_{a\in S_1\cap\mathbb R}\rho_a^2,\\
C_{1,F}^{s}&=\sum_{a\in S_1\setminus\mathbb R}\rho_a,\\
C_{2,F}^{s}&=\sum_{a\in S_1\setminus\mathbb R}\rho_a^2.
\end{aligned}
\tag{L-105103.18}
\]

Conjugate pairing makes every displayed aggregate real. Splitting
(L-105103.16)--(L-105103.17) yields

\[
\boxed{
\mathcal M_{1,F}^{\mathrm{snc}}
=-\Phi_{1,F}+C_{1,F}^{s}+\Lambda_{1,F}^{\mathrm{mrg}},
}
\tag{L-105103.19}
\]

\[
\boxed{
\mathcal M_{2,F}^{\mathrm{snc}}
=B_F-C_{2,F}^{s}-D_{2,F}^{s}
-\Lambda_{2,F}^{\mathrm{mrg}}.
}
\tag{L-105103.20}
\]

Thus, when \(R_F^{\mathrm{snc}}\mathcal M_{2,F}^{\mathrm{snc}}>0\),
the exact simple-noncommon-stratum statistic is

\[
\boxed{
\mathfrak C_F^{\mathrm{snc}}
=\frac{(-\Phi_{1,F}+C_{1,F}^{s}
+\Lambda_{1,F}^{\mathrm{mrg}})_+^2}
{R_F^{\mathrm{snc}}(B_F-C_{2,F}^{s}-D_{2,F}^{s}
-\Lambda_{2,F}^{\mathrm{mrg}})}.
}
\tag{L-105103.21}
\]

This is not a multiple-critical-point reverse--Rolle theorem. Define the real
transfer-obstruction set

\[
\mathcal O_F
=\{x\in\Omega\cap\mathbb R:F'(x)=0,\ x\notin S_1\}.
\tag{L-105103.22}
\]

If \(\mathcal O_F\) is nonempty, draft L-104522's real simplicity or
common-zero hypothesis fails and transfer is withheld. The whole merged set
\(G\) need not be empty: nonreal multiple events and real or nonreal
\(F''\)-only multiple events enter the Laurent corrections without violating
those one-dimensional transfer hypotheses. When \(\mathcal O_F\) is empty,
endpoint nonvanishing, positivity, and the strict coherence margin still must
be checked separately.

## 6. Boundary symmetry and Xi specialization

Schwarz reflection and the parity arguments of L-105101--L-105102 do not use
interior simplicity. For a real entire function of definite parity, both
\(P_F\) and \(Q_F\) are odd, so the existing four-edge and half-rectangle
reductions remain exact under (L-105103.12).

For \(F=\Xi^{(k-1)}\), (L-105103.16)--(L-105103.20) therefore give
conditional fixed-window identities without assuming simple interior zeros.
They do not produce the required Xi multiplicity manifest or show that
\(\mathcal O_F\) is empty. A common \(F,F'\) zero has \(P_F,Q_F\)
vanishing to orders one and three, so both contour residues are zero. Such an
event blocks direct use of L-104522 exactly when it lies on the real transfer
interval. Contour invisibility is not multiplicity exclusion.

For fixed \(T\) with \(F'(\pm T)F''(\pm T)\ne0\), a sufficiently thin
regular strip removes every nonreal event. It sets the nonreal simple
corrections and the nonreal part of the merged Laurent sums to zero; real
merged events can remain.

## 7. Independent polynomial oracle

For a polynomial \(p\), the complete finite residue sums can be checked
without factoring either denominator. With \(w=1/z\),

\[
\sum_{a\in\mathbb C}\operatorname{Res}_a P_p
=[w^2]\,wP_p(1/w),
\qquad
\sum_{a\in\mathbb C}\operatorname{Res}_a Q_p
=[w^4]\,w^3Q_p(1/w).
\tag{L-105103.23}
\]

These residue-at-infinity identities independently audit the unique-support
local sum.

## 8. Scope

This lemma removes interior simplicity from the two contour identities. It
does not:

- give either merged Laurent correction a favorable sign;
- infer multiplicity from a nonzero residue or infer simplicity from a zero
  residue;
- extend reverse--Rolle transfer across a real multiple or common
  \(F'\)-event;
- establish the Xi event manifest or endpoint nonvanishing;
- estimate any boundary charge or correction along an asymptotic sequence;
- prove a strict coherence margin, RCMV104530, or RH.

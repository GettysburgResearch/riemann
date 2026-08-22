# L-105104 — Multiplicity-aware jet-coherence reverse--Rolle transfer

Claim ID: L-105104

Status: **PROPOSED EXACT REAL-VARIABLE TRANSFER; review pending**

Created: 2026-08-23

Depends on: L-104500 and L-104522 from draft PR #720 as exact-head,
post-freeze prior-art context; L-105103

RH status: **not assumed**

## 1. Arbitrary-multiplicity interval identity

Let \(f\) be nonconstant and real analytic on a neighborhood of
\([a,b]\), with \(f(a)f(b)\ne0\). Let

\[
a<c_1<\cdots<c_D<b
\]

be the distinct real zeros of \(f'\), and put \(c_0=a,c_{D+1}=b\).
Write

\[
\mathcal C_{\mathrm{com}}
=\{c_j:f(c_j)=0\}.
\]

Between consecutive critical nodes, \(f'\) has fixed sign and \(f\) is
strictly monotone. Therefore

\[
\boxed{
N_{\mathbb R}^{\mathrm{dist}}(f;(a,b))
=\#\mathcal C_{\mathrm{com}}
+\sum_{j=0}^{D}
\mathbf 1_{\{f(c_j)f(c_{j+1})<0\}}.
}
\tag{L-105104.1}
\]

If \(r_c=\operatorname{ord}_c f'\) at a common node, then
\(\operatorname{ord}_c f=r_c+1\). Counting parent zeros with
multiplicity gives the exact companion identity

\[
\boxed{
N_{\mathbb R}^{\mathrm{mult}}(f;(a,b))
=\sum_{c\in\mathcal C_{\mathrm{com}}}(r_c+1)
+\sum_{j=0}^{D}
\mathbf 1_{\{f(c_j)f(c_{j+1})<0\}}.
}
\tag{L-105104.2}
\]

No critical-point simplicity is required for (L-105104.1)--(L-105104.2).

## 2. Eligible turns and their jet carrier

A noncommon critical point is a genuine turning point exactly when
\(r_c\) is odd. Define

\[
\mathcal T_f^{\mathrm{nc}}
=\{c\in(a,b):f(c)\ne0,\ r_c=\operatorname{ord}_cf'
\text{ is odd}\},
\qquad
R_{\mathrm{jet}}=\#\mathcal T_f^{\mathrm{nc}}.
\tag{L-105104.3}
\]

For \(c\in\mathcal T_f^{\mathrm{nc}}\), put

\[
\boxed{
\rho_c^{\mathrm{jet}}
=\frac{r_c!\,f(c)}{f^{(r_c+1)}(c)}.
}
\tag{L-105104.4}
\]

Indeed, with \(w=x-c\),

\[
f'(c+w)=A_cw^{r_c}+O(w^{r_c+1}),
\qquad
A_c=\frac{f^{(r_c+1)}(c)}{r_c!},
\]

so \(\rho_c^{\mathrm{jet}}=f(c)/A_c\). Because \(r_c\) is odd,

\[
\rho_c^{\mathrm{jet}}<0
\iff c\text{ is a good, Rolle-generating turn},
\]

\[
\rho_c^{\mathrm{jet}}>0
\iff c\text{ is a wrong turn}.
\tag{L-105104.5}
\]

This carrier is visible in the leading principal parts from L-105103:

\[
\boxed{
[w^{-r_c}]\frac f{f'}=\rho_c^{\mathrm{jet}},
\qquad
[w^{-(2r_c-1)}]\frac{f^2}{f'f''}
=\frac{(\rho_c^{\mathrm{jet}})^2}{r_c}.
}
\tag{L-105104.6}
\]

For \(r_c=1\), the leading coefficients are the ordinary residues
\(\rho_c=f(c)/f''(c)\) and \(\rho_c^2\). For \(r_c>1\), they are not
residues: the coefficient of \(w^{-1}\) occurs later in the Laurent series.

Noncommon even-order critical points are stationary events. They do not
change the sign of \(f'\), are not extrema, and are excluded from
\(\mathcal T_f^{\mathrm{nc}}\).

## 3. Multiplicity-aware sign transfer

Let

\[
\mathfrak m_{\mathrm{com}}
=\sum_{c\in\mathcal C_{\mathrm{com}}}r_c
\tag{L-105104.7}
\]

be the common derivative-order mass. Split \((a,b)\) at the common critical
points, and let \(q\) be the number of resulting components containing at
least one eligible turn. Let

\[
G_{\mathrm{jet}}
=\#\{c\in\mathcal T_f^{\mathrm{nc}}:
\rho_c^{\mathrm{jet}}<0\}.
\]

Inside each active component, discard the even-order stationary events and
order the eligible turns. Their max/min types alternate. Two wrong turns
cannot be adjacent, and the interval between consecutive eligible turns
contains a zero exactly when both turns are good. The internal edges alone
therefore give

\[
\boxed{
N_{\mathbb R}^{\mathrm{mult}}(f;(a,b))
\ge
\mathfrak m_{\mathrm{com}}
+\#\mathcal C_{\mathrm{com}}
+2G_{\mathrm{jet}}-R_{\mathrm{jet}}-q.
}
\tag{L-105104.8}
\]

Since \(q\le\#\mathcal C_{\mathrm{com}}+1\),

\[
\boxed{
N_{\mathbb R}^{\mathrm{mult}}(f;(a,b))
\ge
\mathfrak m_{\mathrm{com}}
+2G_{\mathrm{jet}}-R_{\mathrm{jet}}-1.
}
\tag{L-105104.9}
\]

This re-runs the sign proof underlying draft L-104500; it does not invoke
L-104500.3 outside that lemma's stated simple-zero hypotheses.

## 4. Jet coherence

Define

\[
A_{\mathrm{jet}}
=-\sum_{c\in\mathcal T_f^{\mathrm{nc}}}\rho_c^{\mathrm{jet}},
\qquad
B_{\mathrm{jet}}
=\sum_{c\in\mathcal T_f^{\mathrm{nc}}}
(\rho_c^{\mathrm{jet}})^2.
\tag{L-105104.10}
\]

When \(R_{\mathrm{jet}}B_{\mathrm{jet}}>0\), put

\[
\boxed{
\mathfrak C_{\mathrm{jet}}(f;(a,b))
=\frac{(A_{\mathrm{jet}})_+^2}
{R_{\mathrm{jet}}B_{\mathrm{jet}}}.
}
\tag{L-105104.11}
\]

The same finite Cauchy argument as L-104522 gives

\[
G_{\mathrm{jet}}
\ge
\frac{(A_{\mathrm{jet}})_+^2}{B_{\mathrm{jet}}}
=R_{\mathrm{jet}}\mathfrak C_{\mathrm{jet}}.
\tag{L-105104.12}
\]

Combining with (L-105104.9),

\[
\boxed{
N_{\mathbb R}^{\mathrm{mult}}(f;(a,b))
\ge
\mathfrak m_{\mathrm{com}}
+(2\mathfrak C_{\mathrm{jet}}-1)R_{\mathrm{jet}}-1.
}
\tag{L-105104.13}
\]

In particular, if

\[
\mathfrak C_{\mathrm{jet}}\ge\frac{1+c}{2},
\qquad 0<c<1,
\]

then

\[
\boxed{
N_{\mathbb R}^{\mathrm{mult}}(f;(a,b))
\ge
\mathfrak m_{\mathrm{com}}+cR_{\mathrm{jet}}-1.
}
\tag{L-105104.14}
\]

One may sharpen this componentwise. If \(A_\ell,B_\ell,R_\ell\) are the
jet carrier, second moment, and eligible-turn count in active component
\(\ell\), then

\[
N_{\mathbb R}^{\mathrm{mult}}(f;(a,b))
\ge
\mathfrak m_{\mathrm{com}}+\#\mathcal C_{\mathrm{com}}
+\sum_\ell
\max\!\left\{0,
\left\lceil\frac{2(A_\ell)_+^2}{B_\ell}-R_\ell-1\right\rceil
\right\}.
\tag{L-105104.15}
\]

This avoids cancellation of carriers from different components.

## 5. Relation to the full derivative count

The eligible count is a support count, not a multiplicity-weighted derivative
zero count. Define the omitted multiplicity defect

\[
\Delta_{\mathrm{mult}}
=
\sum_{\substack{f(c)\ne0\\r_c\ {\rm even}}}r_c
+
\sum_{\substack{f(c)\ne0\\r_c\ {\rm odd}}}(r_c-1).
\tag{L-105104.16}
\]

Then exactly

\[
\boxed{
N_{\mathbb R}^{\mathrm{mult}}(f';(a,b))
=\mathfrak m_{\mathrm{com}}
+R_{\mathrm{jet}}+\Delta_{\mathrm{mult}}.
}
\tag{L-105104.17}
\]

Consequently a proportion theorem relative to the full derivative
multiplicity requires quantitative control of
\(\Delta_{\mathrm{mult}}\), or direct lower-density premises for
\(\mathfrak m_{\mathrm{com}}\) and \(R_{\mathrm{jet}}\).

## 6. Recovery of the simple theorem

If every real critical event is simple and noncommon, then

\[
\mathfrak m_{\mathrm{com}}=0,\qquad
\Delta_{\mathrm{mult}}=0,\qquad
R_{\mathrm{jet}}=N_{\mathbb R}(f';(a,b)),
\]

and \(\rho_c^{\mathrm{jet}}=\rho_c=f(c)/f''(c)\).
Equation (L-105104.13) is then exactly draft L-104522.4.

## 7. Xi specialization and frontier

For \(f=\Xi^{(k-1)}\), an eligible zero \(c\) of \(\Xi^{(k)}\)
of odd order \(r_c\) has

\[
\rho_{k,c}^{\mathrm{jet}}
=\frac{r_c!\,\Xi^{(k-1)}(c)}{\Xi^{(k+r_c)}(c)}.
\tag{L-105104.18}
\]

A conditional Xi proportion descent may use (L-105104.14) if it supplies:

- the common derivative-order mass;
- a positive eligible-turn line proportion;
- control of \(\Delta_{\mathrm{mult}}\);
- a strict jet-coherence margin;
- the same total-count ratio and regular-window inputs required downstream of
  L-104522.

The ordinary boundary charges \(\Phi_1,B\) from L-105101--L-105103 see
only \(w^{-1}\) residues. They do not reconstruct the leading coefficients
in (L-105104.6) when \(r_c>1\). A new local-jet/global-observable bridge is
therefore required.

## 8. Scope

This lemma does not:

- apply to arbitrary \(C^2\) functions with nonisolated or infinite-order
  critical sets; the jet statement uses analyticity and finite orders;
- turn ordinary confluent residues into jet moments;
- prove an Xi eligible-turn proportion, multiplicity-defect bound, or
  jet-moment estimate;
- establish a strict Xi coherence margin, RCMV104530, or RH.

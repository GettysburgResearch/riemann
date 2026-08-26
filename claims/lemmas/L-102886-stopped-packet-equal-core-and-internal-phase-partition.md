# L-102886 — The literal stopped packet splits into equal-core and internally phased coprime packets

Claim ID: `L-102886`  
Status: **PROVED EXACT SOURCE PARTITION**  
Created: 2026-08-24  
Depends on: `L-102869--L-102885`  
RH status: **not assumed**

Retain the exact stopped-prime decomposition

\[
\mathcal C_{p,q}
=
\mathcal T_{p,q}^{\rm full}
+
\mathcal T_{p,q}^{\rm bdry}
+
\mathcal B_{p,q}.
\]

By `L-102880`, the adverse part of
\(\mathcal T_{p,q}^{\rm full}\) is power-saving.  Put

\[
\mathcal V_{p,q}
:=
\mathcal T_{p,q}^{\rm bdry}
+
\mathcal B_{p,q}.
\]

All source, owner, phase, gauge and dyadic labels occurring below are those of
the literal stopped packet; no unrestricted lattice is substituted.

Consider two physical terms in \(\mathcal V_{p,q}\) and
\(\mathcal V_{r,s}\):

\[
N=P c^2,\qquad M=Q d^2,
\qquad P=pq,\quad Q=rs.
\]

Put

\[
g=(c,d),\qquad c=gc_1,\qquad d=gd_1,\qquad(c_1,d_1)=1.
\]

`L-102884` gives the coefficient-exact common-square extraction

\[
\langle v_N,v_M\rangle
=
g^{-2}
\langle v_{Pc_1^2},v_{Qd_1^2}\rangle.
\tag{L-102886.1}
\]

## 1. Equal-core packet

If

\[
c_1=d_1=1,
\]

then \(c=d=g\).  Define \(\mathscr P_{\rm eq}\) to be the sum of these
terms, retaining the common-core coefficient and all external owner phases.
This is the pure semiprime-squareclass base packet after one common square
shift.

No negative part is taken at this stage.  Fixed-chaos carrier asymptotics show
that \(\mathscr P_{\rm eq}\) is not an independently harmless term.

## 2. One-sided core-discrepancy packet

Suppose, after orienting the pair,

\[
c_1>1,\qquad d_1=1.
\]

Put

\[
\ell_c=P^+(c_1).
\]

Then

\[
\ell_c\mid Pc_1^2,\qquad
\ell_c\nmid Q,
\]

after the clean owner/core reductions already frozen on this branch.  Hence

\[
1
=
-\sum_{h=1}^{\ell_c-1}
e_{\ell_c}\!\left(h(Pc_1^2-Q)\right).
\tag{L-102886.2}
\]

The selected prime is an actual divisor of the literal core coefficient
\(c_1^{-1}\).  The resulting packet is denoted
\(\mathscr P_{\rm one}\).

## 3. Two-sided core-discrepancy packet

If

\[
c_1>1,\qquad d_1>1,
\]

put

\[
\ell_c=P^+(c_1),\qquad
\ell_d=P^+(d_1).
\]

Coprimality gives \(\ell_c\ne\ell_d\), and each prime divides exactly one
reduced product.  Multiplying the two nonzero Ramanujan identities gives

\[
\boxed{
1=
\sum_{h_c=1}^{\ell_c-1}
\sum_{h_d=1}^{\ell_d-1}
e_{\ell_c}\!\left(h_c(Pc_1^2-Qd_1^2)\right)
e_{\ell_d}\!\left(h_d(Pc_1^2-Qd_1^2)\right).
}
\tag{L-102886.3}
\]

This defines the packet \(\mathscr P_{\rm two}\).  Both principal
frequencies are absent before Cauchy or physical collapse.

## 4. Exact complete partition

Every pair of stopped boundary/balanced terms belongs to exactly one of the
three cases above.  Therefore, after the closed unrestricted Type-I adverse
part,

\[
\boxed{
\mathscr V_{\rm cross}
=
\mathscr P_{\rm eq}
+
\mathscr P_{\rm one}
+
\mathscr P_{\rm two}.
}
\tag{L-102886.4}
\]

The smooth-boundary row is included in this same partition: its core integer is
the literal product \(de\ell k\), and the gcd/phase classification depends
only on the resulting physical core.

This theorem is a source partition, not three independent inequalities.
The three packets must be recombined before applying a negative part unless a
separate absolute estimate has been proved for a declared region.

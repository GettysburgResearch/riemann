# L-105401 — Remote critical-tail moment matching closes the complete fixed-order capacity inequality

Claim ID: `L-105401`  
Status: **PROVED EXACT CONDITIONAL COMPLETION THEOREM — XI TAIL ESTIMATE OPEN**  
Created: 2026-08-23  
Depends on: `T-105390`, `L-105400`  
RH status: **not assumed**

## 1. Normalized source and critical measures

Fix a parity `p`, a matrix order `k>=1`, and a block `a in {0,1}`. Let
`F_r=Xi^(r)` be a high derivative of parity `p`, and let `omega_r` be the
real-saddle scale of `L-105387`.

The normalized source matrix is

\[
\widehat{\mathsf A}_{k,r}^{(a)}
=
\left[
{a_{i+j+a}(F_r)\over\omega_r^{2(i+j+a)}}
\right]_{i,j=0}^{k-1}.
\tag{L-105401.1}
\]

Assume every nonzero critical point of `F_r` in the complete exhaustion is
real and simple and has nonpositive residue. For each positive critical point
`c`, put

\[
\widehat s_c={1\over\omega_r^2c^2},
\qquad
W_c=-{2F_r(c)\over c^2F_r''(c)}\ge0.
\tag{L-105401.2}
\]

The normalized critical measure is

\[
\widehat\nu_r=\sum_{c>0}W_c\delta_{\widehat s_c}.
\tag{L-105401.3}
\]

## 2. Prefix and remote tail

Choose `J=J_r` in the range of `T-105390`. Let

\[
\widehat\nu_{r,\le J}
\]

be the measure formed by the first `J` positive critical pairs, and let

\[
\widehat\nu_{r,>J}
=
\widehat\nu_r-\widehat\nu_{r,\le J}.
\tag{L-105401.4}
\]

Let `nu_p` be the unit-scale tangent or cotangent measure of `L-105382`, and
split it into the first `J` atoms and its tail:

\[
\nu_p=\nu_{p,\le J}+\nu_{p,>J}.
\tag{L-105401.5}
\]

Define the signed remote-tail discrepancy

\[
\boxed{
\sigma_{r,J}
=
\widehat\nu_{r,>J}-\nu_{p,>J}.
}
\tag{L-105401.6}
\]

No atom-by-atom pairing in the remote tail is required.

## 3. Exact reserve decomposition

Let

\[
\mathsf T_{k,p}^{(a)}
=
\mathsf T_{k,p,\le J}^{(a)}
+
\mathsf R_{k,p,J}^{(a)}
\]

be the full trigonometric source matrix, its first-`J` atomic block, and its
positive tail reserve. Put

\[
\mathsf E_{A,r}^{(a)}
=
\widehat{\mathsf A}_{k,r}^{(a)}
-
\mathsf T_{k,p}^{(a)},
\tag{L-105401.7}
\]

and

\[
\mathsf E_{P,r,J}^{(a)}
=
\widehat{\mathsf C}_{k,r,\le J}^{(a)}
-
\mathsf T_{k,p,\le J}^{(a)}.
\tag{L-105401.8}
\]

Then the complete normalized boundary reserve is exactly

\[
\boxed{
\begin{aligned}
\widehat{\mathsf S}_{k,r}^{(a)}
&=
\widehat{\mathsf A}_{k,r}^{(a)}
-
\widehat{\mathsf C}_{k,r}^{(a)}\\
&=
\mathsf R_{k,p,J}^{(a)}
+
\mathsf E_{A,r}^{(a)}
-
\mathsf E_{P,r,J}^{(a)}
-
\mathsf M_k^{(a)}(\sigma_{r,J}).
\end{aligned}
}
\tag{L-105401.9}
\]

This identity isolates the omitted tail without hiding it in the prefix error.

## 4. Quantitative sufficient condition

Let

\[
\eta_{k,p,J}^{(a)}
=
\lambda_{\min}
\left(\mathsf R_{k,p,J}^{(a)}\right)>0.
\]

By `L-105400`, a sufficient condition for the complete boundary matrix to be
positive is

\[
\boxed{
\left\|\mathsf E_{A,r}^{(a)}\right\|_{\rm op}
+
\left\|\mathsf E_{P,r,J}^{(a)}\right\|_{\rm op}
+
kD_{k,a}(\sigma_{r,J})
<
\eta_{k,p,J}^{(a)}.
}
\tag{L-105401.10}
\]

The same conclusion follows with the weighted total variation bound of
`L-105400.5` in place of `kD_(k,a)`.

## 5. Asymptotic remote-tail gate

Use the exponent

\[
d_k=3k(k-1)+4
\]

from `T-105390`, and let `J_r=floor(r^(gamma_k))` with the admissible
`gamma_k`. The source and prefix errors are already

\[
o(J_r^{-d_k}).
\]

Therefore, if

\[
\boxed{
\max_{0\le n\le2k-1}
\left|
\int s^n\,d\sigma_{r,J_r}(s)
\right|
=
o(J_r^{-d_k}),
}
\tag{L-105401.11}
\]

then, for both blocks `a=0,1`,

\[
\boxed{
\widehat{\mathsf C}_{k,r}^{(a)}
\preceq
\widehat{\mathsf A}_{k,r}^{(a)}
}
\tag{L-105401.12}
\]

for every sufficiently high derivative order of the chosen parity.

Thus only the first `2k` scalar moments of the omitted critical tail must be
matched at fixed matrix order.

## 6. Scope

The hypothesis that every omitted critical point is real with nonpositive
residue is part of the tail gate and is not supplied by `T-105390`. The moment
matching in (L-105401.11) is also open for Xi. The theorem is a typed
completion mechanism, not an unconditional full-tail theorem and not an RH
proof.

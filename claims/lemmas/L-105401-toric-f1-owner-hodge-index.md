# L-105401 — Exact toric Hodge index for Hilbert-valued native owner currents

Claim ID: `L-105401`  
Status: **PROVED EXACT UNIFORM FINITE HODGE THEOREM**  
Created: 2026-08-23  
Depends on: `L-105400`  
RH status: **not assumed**

Let \(E=\{1,\ldots,m\}\), \(m\ge2\), and let

\[
A_E^\bullet
=
\mathbb R[x_1,\ldots,x_m]/(x_1^2,\ldots,x_m^2),
\qquad
\deg(x_1\cdots x_m)=1.
\]

This is the Chow ring of the toric product
\((\mathbf P^1)^E\), whose monomial skeleton is defined over
\(\mathbf F_1\).

Fix \(a_i>0\) and

\[
\omega=\sum_i a_i x_i,\qquad A=\prod_i a_i.
\]

Let \(H\) be a real Hilbert space and let

\[
\alpha=\sum_i a_i v_i x_i,\qquad v_i\in H.
\]

The coefficient \(v_i\) may be a labelled source current, a scale-phase
function, or any Hilbert-valued observation of that current.

## 1. Degree direction

Direct expansion gives

\[
\boxed{
\deg_H(\alpha\omega^{m-1})
=
(m-1)!A\sum_i v_i.
}
\tag{L-105401.1}
\]

Thus the Lefschetz degree direction is the total labelled tangent, with no
owner discarded.

Put

\[
\bar v=\frac1m\sum_i v_i,\qquad
\alpha^\circ=\sum_i a_i(v_i-\bar v)x_i.
\]

Then \(\deg_H(\alpha^\circ\omega^{m-1})=0\).

## 2. Exact Hodge–Riemann form

For Hilbert-valued divisors define the scalar intersection pairing by
contracting coefficient vectors with the Hilbert inner product. Then

\[
\boxed{
\deg\!\left(
\langle\alpha^\circ,\alpha^\circ\rangle
\omega^{m-2}
\right)
=
-(m-2)!A
\sum_i\|v_i-\bar v\|_H^2.
}
\tag{L-105401.2}
\]

Proof: the top coefficient is

\[
(m-2)!A
\sum_{i\ne j}
\langle v_i-\bar v,v_j-\bar v\rangle.
\]

Because the centered vectors sum to zero, the last sum equals
\(-\sum_i\|v_i-\bar v\|^2\).

Consequently the primitive space is negative definite and, after the canonical
normalization by \((m-2)!A\), its spectral gap is exactly one. The gap is
independent of the number and size of the primes.

## 3. Mixed Hodge inequality

For another centered divisor
\(\beta^\circ=\sum_i a_i(w_i-\bar w)x_i\),

\[
\deg\!\left(
\langle\alpha^\circ,\beta^\circ\rangle\omega^{m-2}
\right)
=
-(m-2)!A
\sum_i\langle v_i-\bar v,w_i-\bar w\rangle.
\]

Hence

\[
\boxed{
|Q_\omega(\alpha^\circ,\beta^\circ)|^2
\le
[-Q_\omega(\alpha^\circ,\alpha^\circ)]
[-Q_\omega(\beta^\circ,\beta^\circ)].
}
\tag{L-105401.3}
\]

This is the exact finite Hodge-index/Cauchy inequality needed for a trace
theorem.

## 4. Application to the completion tangent

In (L-105400.4), let

\[
v_e=r_eU_eA_{1-\tau,\ne e}E
\]

after any fixed Hilbert observation. Taking \(a_e=\log p_e\) realizes the
completion tangent as the divisor

\[
\alpha_\tau=\sum_e(\log p_e)v_ex_e.
\]

Its degree is the complete tangent source \(\sum_ev_e\), and its primitive
Hodge norm is exactly the owner variance

\[
\sum_e\|v_e-\bar v\|^2.
\]

No prime owner is reused, and no arithmetic sign is inferred from the Hodge
identity alone.

## Scope

This proves the finite uniform `AHG` statement for degree-one native tangent
classes. The cofinal arithmetic task is to control the physical trace of the
primitive norm; that task is isolated in `T-105400`.

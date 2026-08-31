# L-107301 — The shared-fibre augmentation filtration is a Frobenius-stable primitive object

Claim ID: `L-107301`  
Status: **PROVED EXACT FINITE FROBENIUS-SET AND SOURCE-ADAMS THEOREM**  
Created: 2026-08-30  
Depends on: `L-107300`; `DIAGALG-1--3` on PR #765  
RH/GRH status: **not assumed**

Let \(X\) be a finite source set, \(C\) a finite cell set and

\[
r:X\to C
\]

be a surjection.  Let a permutation \(\sigma_X\) of \(X\) and a permutation
\(\sigma_C\) of \(C\) satisfy

\[
r\circ\sigma_X=\sigma_C\circ r.
\tag{L-107301.1}
\]

Put \(V_X=K^X\), \(V_C=K^C\), over a characteristic-zero field \(K\), and
define the cell-sum augmentation

\[
P_X:V_X\to V_C,
\qquad
(P_Xa)_c=\sum_{r(x)=c}a_x.
\tag{L-107301.2}
\]

## 1. Canonical mean–primitive splitting

Let \(n_c=|r^{-1}(c)|\).  Define

\[
(J_X\alpha)_x=\frac{\alpha_{r(x)}}{n_{r(x)}}.
\tag{L-107301.3}
\]

Then

\[
P_XJ_X=I_{V_C}.
\]

Consequently

\[
\boxed{
V_X=M_X\oplus V_X^\circ,
\qquad
M_X=\operatorname{im}J_X,
\qquad
V_X^\circ=\ker P_X.
}
\tag{L-107301.4}
\]

The projections are

\[
\Pi_M=J_XP_X,
\qquad
\Pi_\circ=I-J_XP_X.
\tag{L-107301.5}
\]

Because (L-107301.1) preserves the fibre cardinalities,
\(\Pi_M,\Pi_\circ\) commute with total Frobenius.  Thus both summands are
honest Frobenius submodules.

With the standard Hermitian form,

\[
\boxed{
\|a\|^2
=
\sum_{c\in C}\frac{|(P_Xa)_c|^2}{n_c}
+
\sum_{c\in C}\|a_c^\circ\|^2.
}
\tag{L-107301.6}
\]

The first term is the cell-mean energy and the second is literal primitive
energy.

## 2. The four bilateral grades

For left and right source maps, the tensor product decomposes canonically as

\[
\boxed{
\begin{aligned}
V_L\otimes V_R
={}&
(M_L\otimes M_R)
\oplus(V_L^\circ\otimes M_R)\\
&\oplus(M_L\otimes V_R^\circ)
\oplus(V_L^\circ\otimes V_R^\circ).
\end{aligned}
}
\tag{L-107301.7}
\]

Every summand is stable under total Frobenius.

The physical residue pushforward factors through the quotient

\[
V_L\otimes V_R
\longrightarrow
M_L\otimes M_R
\simeq
V_{C_L}\otimes V_{C_R}.
\tag{L-107301.8}
\]

The other three summands are the exact source-relative primitive object.
Literal diagonal energy sees all four summands.  This explains, without
arbitrary coefficient freedom, why residue aggregation alone cannot recover
the diagonal.

## 3. Source-aware Adams extraction respects the grades

Let the Frobenius orbits of \(X\) carry finite coefficient spaces as in
`DIAGALG-1`, and assume the coefficient maps are compatible with the declared
cell-sum augmentation.  Apply Adams to the local orbit monodromies before
pushforward.  Since the projections (L-107301.5) commute with Frobenius under
this explicit compatibility hypothesis, they commute with every local power
and every source-aware Adams operation.  Therefore the
primitive degree-\(d\) extraction

\[
dP_d(V)
=
\sum_{e\mid d}\mu(e)
A_{d/e}(f_*\psi_X^eV)
\tag{L-107301.9}
\]

splits additively into the mean and primitive channels.  On the bilateral
tensor, the external-plus-diagonal extractor splits into the four grades of
(L-107301.7).

This is precisely the order required by PR #760:

```text
retain source algebra
 -> split mean and primitive channels
 -> apply source Adams on each orbit
 -> push forward
 -> perform closed-point Möbius extraction.
```

Applying Adams after pushforward still creates the orbit defect recorded in
`DIAGALG-3`; the present splitting does not weaken that firewall.

## 4. Complexity

The three primitive grades have total dimension

\[
(|X|-|C_L|)|C_R|
+
|C_L|(|Y|-|C_R|)
+
(|X|-|C_L|)(|Y|-|C_R|).
\]

at literal vector-space level, but its trace-level native rectangular Wick
value is compressed by `L-107300` to two one-sided quadratic responses and
two norms.

Thus:

- a faithful algebra carrier may retain full multiplicity;
- the native rank-one scalar does not require that full rank;
- a geometric realization must state which level it controls.

## Scope

This is an honest finite Frobenius-graded object.  It is not a constructible
native sheaf with uniform conductor, a weight theorem, a signed trace
estimate or a number-field transfer.

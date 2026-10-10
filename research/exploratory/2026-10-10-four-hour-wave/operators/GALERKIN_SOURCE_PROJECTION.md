# Use Galerkin energy orthogonality inside the source residual

Date: 2026-10-10. This is a new exact refinement of the inherited
energy/Schur residual bound. It is a conditional operator lemma, not a claim
that a sampled source residual is certified. Independent review requested.

Suppose the audited form \(q\) is positive on a closed complement \(V\),
with \(q(v,v)\ge\kappa\|\phi_v'\|_2^2\), and

\[
q(v,z)=b\langle\phi_v',\Pi F_z\rangle\quad(v\in V).
\tag{1}
\]

Complete \(V\) in the energy norm. Let \(H\subset V\) be a finite-dimensional
trial space, and \(e_i\) an orthonormal basis of the finite complement.
Choose the exact Galerkin correction \(v_i\in H\) so

\[
z_i=e_i-v_i,\qquad q(h,z_i)=0\quad(h\in H),\qquad U_{ij}=q(z_i,z_j).
\tag{2}
\]

Let \(W_H=H^{\perp_q}\) in the energy completion. Because \(H\) is finite
and \(q\) is positive on it, \(V=H\oplus_qW_H\). For a vector \(z\) in the
span of the \(z_i\), the residual functional \(q(\cdot,z)\) vanishes on
\(H\). Consequently its exact dual energy norm is its norm on \(W_H\), and

\[
S=U-K^*K,
\tag{3}
\]

where \(K\) is the Riesz representation of this residual on \(W_H\).
This is the same exact effective Schur matrix as before; the Galerkin
orthogonality has now been used in the residual bound as well as in \(U\).

## Additional literal-source projection

For each \(h\in H\), (1) and \(q(w,h)=0\) imply
\(\langle\phi_w',\Pi F_h\rangle=0\) for \(w\in W_H\). Define
\(\Pi_H\) as the orthogonal projection off both the audited primitive
constraint functions and the literal source images \(\{\Pi F_h:h\in H\}\).
Then the same coercivity estimate gives

\[
|q(w,z)|^2\le\frac{b^2}{\kappa}q(w,w)\|\Pi_HF_z\|_2^2.
\]

Thus, with \((R_H)_{ij}=\langle\Pi_HF_{z_i},\Pi_HF_{z_j}\rangle\),

\[
U-\frac{b^2}{\kappa}R_H\preceq S\preceq U,\qquad 0\preceq R_H\preceq R.
\tag{4}
\]

For an exact basis \(h_a\) of \(H\), set

\[
G_{ab}=\langle\Pi F_{h_a},\Pi F_{h_b}\rangle,\quad
B_{ai}=\langle\Pi F_{h_a},\Pi F_{z_i}\rangle.
\]

The matrix \(G\) is positive definite: if \(\Pi F_h=0\) for a combination
\(h\in H\), (1) with \(v=h\) gives \(q(h,h)=0\), hence \(h=0\). Therefore

\[
R_H=R-B^*G^{-1}B.
\tag{5}
\]

The energy-completed argument is legitimate: coercivity makes
\(v\mapsto\phi_v'\) continuous in the energy norm; the source coupling
(1) and every finite trial functional pass to the completion. No ordinary
\(L^2\) spectral gap is required.

## A cheaper shifted-source enclosure

The full Gram matrix in (5) is optional. Choose **any exact**
\(u_i\in H\), and set

\[
(\widetilde R)_{ij}=\langle\Pi(F_{z_i}-F_{u_i}),
                                  \Pi(F_{z_j}-F_{u_j})\rangle.
\]

For \(w\in W_H\), \(q(w,u_i)=0\); hence its residual functional is also
represented by \(F_{z_i}-F_{u_i}\). Cauchy/coercivity gives

\[
U-\frac{b^2}{\kappa}\widetilde R\preceq S\preceq U.
\tag{6}
\]

Equation(6) keeps the **original** Galerkin \(U\). It does not replace it by
\(q(z_i-u_i,z_j-u_j)=U_{ij}+q(u_i,u_j)\). The variational supremum is on
\(W_H\), where the source functional is unchanged; this is why no extra
positive trial-energy matrix is needed.

One may discover coefficients for \(u_i\) by an ordinary least-squares fit
of \(\Pi F_{z_i}\) to \(\Pi F_H\), freeze them as exact rationals, and then
independently enclose every full-source integral in \(\widetilde R\).
Only that final directed enclosure can certify a sign. The exact Galerkin
correction defining (2) must remain exact; rounded coefficients used there
would require an explicit nonzero-orthogonality error bound.

At \(L=1\), the reviewed dimension14 sector gives \(b^2/\kappa=15/8\);
the reviewed phase-aware dimension8 sector gives \(27/2\). The latter's
ordinary unprojected residual bound was negative with100 trials, so the
additional source projection is a concrete possible mechanism for reducing
that overestimate. It is not a native negative-form counterexample.

# L-107302 — The shared-conductor relative object is an honest reduced augmentation tensor

Claim ID: `L-107302`  
Programme aliases: `RIEMANNSTRUCT.SHARED_CONDUCTOR_OBJECT`, `LFAM2.ONEPLACEWEIL_LOCAL`  
Status: **PROVED EXACT LOCAL OBJECT AND CONSTANT-CONSTITUENT CLASSIFICATION**  
Created: 2026-08-30  
Depends on: `L-107300--L-107301`; PR #765 live shared-fibre map  
Programme issues: #763, #737, #739  
RH/GRH status: **not assumed**

Let \(\mathfrak l,\mathfrak r\) be two marked places of a global function
field over \(\mathbf F_q\), with residue fields \(k_\ell,k_\rho\).
Write

\[
T_\ell=\operatorname{Res}_{k_\ell/\mathbf F_q}\mathbf G_m,
\qquad
T_\rho=\operatorname{Res}_{k_\rho/\mathbf F_q}\mathbf G_m.
\]

The Kummer sheaves of `L-107300` descend to these Weil-restriction tori.

Define

\[
\boxed{
\mathscr C_{\ell,\rho}^{\rm nr}
=
\mathscr A_\ell^{\rm nr}
\boxtimes
\mathscr A_\rho^{\rm nr}.
}
\tag{L-107302.1}
\]

It is lisse, tame and pure of weight zero, of rank

\[
\boxed{
(m_\ell-1-\varepsilon_\ell)
(m_\rho-1-\varepsilon_\rho).
}
\tag{L-107302.2}
\]

## 1. Pullback by the physical squareclass map

For fixed nonzero owner residues \(P,Q\), consider

\[
\Phi_{P,Q}(c,d)
=
(Qd^2,Pc^2).
\tag{L-107302.3}
\]

A character constituent
\(\mathcal L_\eta\boxtimes\mathcal L_\theta\) pulls back to

\[
\eta(Q)\theta(P)\,
\mathcal L_{\eta^2}(d)
\boxtimes
\mathcal L_{\theta^2}(c).
\tag{L-107302.4}
\]

Because \(\eta^2\ne1\) and \(\theta^2\ne1\) in the reduced object,
\(\Phi_{P,Q}^*\mathscr C_{\ell,\rho}^{\rm nr}\) has no geometrically constant
constituent on the complete two-core torus.

This is the first honest one-object realization of the clean shared-fibre
connected trace after the quadratic root channels have been separated.

## 2. Exact decomposition of the full connected object

Using `L-107301.4`,

\[
\boxed{
\begin{aligned}
P_\ell^\perp\otimes P_\rho^\perp
={}&P_\ell^{\rm nr}\otimes P_\rho^{\rm nr}\\
&+\varepsilon_\ell
  P_{\kappa_\ell}\otimes P_\rho^{\rm nr}\\
&+\varepsilon_\rho
  P_\ell^{\rm nr}\otimes P_{\kappa_\rho}\\
&+\varepsilon_\ell\varepsilon_\rho
  P_{\kappa_\ell}\otimes P_{\kappa_\rho}.
\end{aligned}
}
\tag{L-107302.5}
\]

After square pullback:

- the first term is nonconstant in both core variables;
- the second is constant in the \(\ell\)-core variable only;
- the third is constant in the \(\rho\)-core variable only;
- the fourth is constant in both core variables.

Thus the formerly undifferentiated “principal/quadratic/full-support
background” is exactly a list of at most three rank-one resonance sectors.

## 3. Relation to the live Wick pair

PR #765 proves that, in one fixed shared-conductor fibre, the native Wick pair
maps coefficient-exactly to the physical squareclass coordinates

\[
(P,c;Q,d)\longmapsto(Qd^2,Pc^2).
\]

Combining that map with (L-107302.5) gives an exact local decomposition of the
live trace function into one nonresonant relative object and at most three
explicit resonant rows. No independent \(Z_0\times Z_1\) marked-place pair is
introduced.

## Scope

The local object and resonance list are complete. Uniform cohomology of the
global Boolean/source pushforward, incomplete shells, and principal-member
binding remain open.

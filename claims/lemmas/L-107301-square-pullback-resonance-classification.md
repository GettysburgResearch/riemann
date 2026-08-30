# L-107301 — Square pullback has exactly one possible nonprincipal resonance

Claim ID: `L-107301`  
Programme aliases: `RIEMANNSTRUCT.QUADRATIC_RESONANCE`, `LFAM2.KUMMER_SQUARE_PULLBACK`  
Status: **PROVED EXACT RESONANCE CLASSIFICATION**  
Created: 2026-08-30  
Depends on: `L-107300`  
Programme issues: #763, #737, #739  
RH/GRH status: **not assumed**

Retain the odd finite field \(k=\mathbf F_Q\) and the even-character
augmentation sheaf \(\mathscr A_Q\).

Let

\[
s:\mathbf G_m\longrightarrow\mathbf G_m,\qquad z\longmapsto z^2.
\]

For every multiplicative character \(\eta\),

\[
\boxed{
s^*\mathcal L_\eta\simeq\mathcal L_{\eta^2}.
}
\tag{L-107301.1}
\]

Therefore \(s^*\mathcal L_\eta\) is geometrically constant exactly when
\(\eta^2=1\).

Among the even nonprincipal characters there is at most one such character:
the quadratic character \(\kappa_Q\). It is even exactly when

\[
Q\equiv1\pmod4.
\]

Put

\[
\varepsilon_Q=
\begin{cases}
1,&Q\equiv1\pmod4,\\
0,&Q\equiv3\pmod4.
\end{cases}
\]

Define the nonresonant augmentation

\[
\boxed{
\mathscr A_Q^{\rm nr}
=
\bigoplus_{\substack{\eta\in\widehat X_Q\\
                     \eta\ne1,\ \eta^2\ne1}}
\mathcal L_\eta.
}
\tag{L-107301.2}
\]

Then

\[
\boxed{
\mathscr A_Q
=
\mathscr A_Q^{\rm nr}
\oplus
\varepsilon_Q\mathcal L_{\kappa_Q},
}
\tag{L-107301.3}
\]

and \(s^*\mathscr A_Q^{\rm nr}\) has no geometrically constant subquotient.

At projector level, with \(P_{\kappa_Q}\) the normalized rank-one quadratic
character projector when it exists,

\[
\boxed{
P_Q^\perp=P_Q^{\rm nr}+\varepsilon_QP_{\kappa_Q},
}
\tag{L-107301.4}
\]

where

\[
P_Q^{\rm nr}([x],[y])
=
\mathbf1_{[x]=[y]}-\frac1{m_Q}
-\frac{\varepsilon_Q}{m_Q}\kappa_Q(xy^{-1}).
\tag{L-107301.5}
\]

## Binding example

For \(Q=5\), \(X_Q\) has two elements and the entire augmentation is the
quadratic character. Its square pullback is constant. Thus the full
augmentation cannot be declared geometrically nonconstant without first
removing the quadratic root channel.

## Scope

This theorem identifies every constant constituent created by the physical
square map. It does not estimate the explicit quadratic-resonant rows; those
remain visible in `T-107300`.

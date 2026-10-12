# Centered tail elimination and exact parity blocks

This note proves a change of the finite complement and a sharper positive-sector
bound for the literal native form. It assumes the same inherited O1--O4 source
and primitive identities as `CODIMENSION_8_PHASE_REFINEMENT.md`. It does not
assert positivity of the effective finite form or the terminal Weil adapter.

Let (b=3/2,c=1/2), let (0<L\leq\log3), and write

\[
 C_a(h)=\int_0^L h(t)\cosh b(t-a)\,dt,\qquad
 S_a(h)=\int_0^L h(t)\sinh b(t-a)\,dt.
\]

All moment equations below are complex equations. Their associated quadratic
terms are absolute squares. The complete omitted prime tail is exactly

\[
 q(h)-q_2(h)=-\tau_2|C_0(h)|^2+\tau_2|S_0(h)|^2,
 \qquad \tau_2=\sum_{n\geq3}\Lambda(n)n^{-2}>0.                 \tag{1}
\]

The change of anchor is a real hyperbolic rotation:

\[
 \binom{C_a}{S_a}=
 \begin{pmatrix}\cosh ba&-\sinh ba\\-\sinh ba&\cosh ba\end{pmatrix}
 \binom{C_0}{S_0}.
\]

Consequently \(-|C_a|^2+|S_a|^2=-|C_0|^2+|S_0|^2\), including for complex
moments. At the centered anchor (a=L/2), the exact tail is nonnegative on
\(C_{L/2}(h)=0\). No arithmetic term is deleted.

For (m\geq1), take the new finite complement

\[
 E_m^{\rm cen}=\operatorname{span}\{e^{ct},e^{-ct},
       \cosh b(t-L/2),\sin(j\pi t/L):1\leq j\leq m\},
 \quad V_m^{\rm cen}=(E_m^{\rm cen})^\perp_{L^2}.            \tag{2}
\]

These are actual native (L^2(0,L)) subspaces. The centered complement is not
obtained by silently replacing an old trial coefficient: a new finite Schur
calculation is needed to use it.

## Primitive transfer and inherited source bound

For (h\in V_m^{\rm cen}\), let

\[
 \phi(t)=2\int_0^t\sinh((t-u)/2)h(u)\,du.
\]

The (e^{\pm ct}) moments imply \(\phi=\phi'=0\) at both endpoints and
\(h=\phi''-c^2\phi\). The clamped endpoint identities give

\[
 \int h(t)\cosh b(t-L/2)\,dt=(b^2-c^2)\int\phi(t)\cosh b(t-L/2)\,dt,
\]

and therefore

\[
 \int\phi'(t)\sinh b(t-L/2)\,dt=0.                         \tag{3}
\]

The low sine moments give exactly the same vanishing low sine coefficients of
\(\phi\) as before. Thus every previously proved Fourier supporting line

\[
 P(x)V_2(x)\geq\alpha x-C
\]

still yields

\[
 q(h)\geq b\{\alpha\|\phi'\|_2^2-C\|\phi\|_2^2\}.         \tag{4}
\]

In particular the reviewed phase line \(\alpha=4/5,C=244\) applies. The
original proof used the old anchor only for tail elimination and the primitive
protected direction; equations (1) and (3) give their exact replacements.

## Reflection and the sharper even sector

Let \(Jh(t)=h(L-t)\). Both (2) and the native form commute with (J): the
kernel is (W(|t-u|)), and the centered hyperbolic direction is even. Split
into (J=+1) and (J=-1) sectors. If (Jh=\epsilon h\), uniqueness of the
clamped primitive gives \(J\phi=\epsilon\phi\).

The sine \(\sin(j\pi t/L)\) has reflection sign \((-1)^{j+1}\). For (m=5)
and (L=1), an even primitive has its first allowed sine index at (7),
whereas an odd primitive has its first at (6). Equation (4) gives

\[
 q(h_+)\geq\kappa_+\|\phi_+'\|_2^2,\quad \kappa_+>2/5;
 \qquad q(h_-)\geq\kappa_-\|\phi_-'\|_2^2,\quad\kappa_->1/6. \tag{5}
\]

The exact rational checker uses only the already proved supporting line and
\(\pi>6283/2000\). Thus the new bound does not require a fresh phase sweep.

The five low sines have three even and two odd elements. The exponential span
has one even and one odd direction after centering. The added centered cosh
is even. Hence (E_5^{\rm cen}=E_+\oplus E_-) has dimensions (5+3).

## Exact residual parity and Schur blocks

For any native test (z), set

\[
 K_z(t)=\int_0^L W(|t-u|)z(u)\,du,
 \qquad F_z(t)=-K_z'(t)+c^2\int_0^tK_z(u)\,du.
\]

Let \(\Pi_{\rm cen}\) be the orthogonal projection off

\[
 \operatorname{span}\{1,\cos(j\pi t/L):1\leq j\leq m,
                        \sinh b(t-L/2)\}.                 \tag{6}
\]

This span is reflection invariant. Direct substitution, with the constant
term retained, gives

\[
 F_{Jz}(t)=-F_z(L-t)+c^2\int_0^LK_z(u)\,du,
 \quad \Pi_{\rm cen}F_{Jz}=-J\Pi_{\rm cen}F_z.             \tag{7}
\]

Thus the projected residual has parity opposite to its source test. If the
trial space (H\subset V_m^{\rm cen}\) is reflection invariant, exact energy
Galerkin corrections preserve source parity. Both the finite energy matrix

\[
 U_{ij}=q(z_i,z_j)
\]

and the continuum residual Gram

\[
 R_{ij}=\langle\Pi_{\rm cen}F_{z_i},\Pi_{\rm cen}F_{z_j}\rangle
\]

have *identically zero* cross blocks. These zeros follow from the source
identities, rather than from the size of computed entries. For (L=1,m=5),
the scalar effective-form enclosures therefore separate as

\[
 U_+-(45/8)R_+\preceq S_+\preceq U_+,
 \qquad U_--(27/2)R_-\preceq S_-\preceq U_-.               \tag{8}
\]

The even block improves the old uniform residual coefficient (27/2) by a
factor (12/5). Positivity of either lower block is an additional finite
certificate, not a consequence of this reduction alone.

The weighted primitive estimate also splits exactly. The coefficient
\(\int_0^L\Pi_{\rm cen}F_{z_\epsilon}(t)\cos(n\pi t/L)dt\)
vanishes unless \((-1)^n=-\epsilon\). Hence each parity block has its own
complete cosine tail. If the finite cutoff is (N), its tail inverse weight
can use the smallest index (n>N) with the matching parity, rather than
automatically (N+1).

Finally, each diagonal product in a fixed parity block is reflection even.
An exact continuum computation of that block can integrate only (0\leq
t\leq L/2\) and double the result, provided all source cusp and omitted
neighborhood bounds are transformed explicitly. No such half-window runtime
certificate is claimed in this note.

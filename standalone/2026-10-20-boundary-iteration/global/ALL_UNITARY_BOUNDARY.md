# All unitary characters at the preliminary boundary

Status: proposed source-dependent analytic theorem, submitted for
independent review. The stronger all-field boundary in the final
section remains a separate interface. RH is not proved.

## 1. Statement and dependencies

Under the upstream theta, finite-correlation, orbit-Poisson, hybrid
sieve and canonical-recursion inputs identified in the earlier angular
packet and ALL_FIELD_SPHERICAL_RESIDUE.md, every number field \(K\)
and every unitary Hecke character \(\eta\) satisfy
\[
             L_K(s,\eta)\ne0\qquad(\Re s>11/12).         \tag{1.1}
\]
A possible translated principal pole is allowed. The boundary is
common; constants and thresholds may depend on the fixed field and
character. There is no boundary-line assertion or growing-type
uniformity claim.

The new part is the balanced resonant family over fields containing
\(E=\mathbb Q(\sqrt{-3})\):
\[
       \Lambda_K\xi N^{it},\qquad
       \overline{\Lambda_K}\xi N^{it},
 \quad \Lambda_K=\Lambda_E\circ N_{K/E},
 \quad \xi\text{ finite order}.                         \tag{1.2}
\]
The inherited nonresonant unitary adapters already give the stronger
source-dependent boundary \(B_\flat\) outside this family.

New dependencies:

* ALL_FIELD_SPHERICAL_RESIDUE.md proves the constant-term interface
  with the exact finite class weight, moving-prime support and
  \(1/Np\) selected-prime action.
* RESIDUE_INDUCTION_INTERFACE.md proves the shifted-label row sum
  and strict canonical residue margin.
* EISENSTEIN_UNITARY_INVERSE.md records the coefficientwise reason
  both inverse Poisson steps retain the unitary fixed character;
  the same operation is used in the general-field source.

Inherited dependencies:

* ANGULAR_THETA_AND_INVERSE.md and
  BALANCED_UNITARY_INVERSE_ADDENDUM.md in the preceding packet,
  for fixed higher angular vectors, balanced radial parameters,
  finite realized coefficient orbits and the nonresonant terminals.
* Liu arXiv:2610.26835v1, Sections 3–11 and Theorem 18.2,
  for the native arithmetic recursion and its validity over every
  fixed \(F\supset\mu_{12}\). The new spherical calculation changes
  only the constant-term part that the source killed by angular
  integration.

## 2. Exhausting the fixed infinity types

First let \(F\supset\mu_{12}\). Remove the common norm component of
an actual unitary character \(\Omega\), so that its complex local
weight is
\[
        (z_v/|z_v|)^{a_v}|z_v|_v^{i\gamma_v},
           \qquad \sum_{v\mid\infty}\gamma_v=0.          \tag{2.1}
\]
The angular integers and radial real parameters obey the global
unit compatibility law. No arbitrary local tuple is postulated.

Let \(\lambda_v\in\{1,-1\}\) be the source Eisenstein type. At a
canonical terminal for \(\nu=\Omega^h\xi\), the theta degrees are
\[
                    m_v=ha_v-\lambda_v,\qquad
                    g_v=h\gamma_v.                    \tag{2.2}
\]
If some \(m_v\ne0\), the corresponding pure derivative annihilates
the global constant term. If all \(m_v=0\) but \(g\ne0\), the
balanced norm-one character annihilates it by the inherited radial
adapter. Both cases retain the source gamma strip and vertical
growth with fixed-type constants.

The remaining case is \(m_v=g_v=0\) at every place. It is exactly the
all-spherical terminal treated in ALL_FIELD_SPHERICAL_RESIDUE.md.
Whole conjugation permits the opposite angular orientation and
the conjugate local digit support. Thus every fixed unitary type
and every member of its realized conjugation/finite-twist orbit
now has an available terminal estimate.

## 3. The canonical and selected inverse estimates

The canonical coefficient is the source
\(a_0(n)\nu(n)\), with \(a_0=\bar\Lambda\gamma_2\).
At each finite row Poisson transform, \(\nu\) is a column coefficient,
not a periodic row character. Its extracted gcd factors cancel
between the two conjugate columns. The finite Fourier expansion
is applied only to the reciprocity/Gauss correction. It multiplies
the retained whole-column \(\nu\) by one of finitely many fixed
finite characters. A whole-side conjugation reverses the fixed
infinity type. No infinite-order character is expanded on a finite
ray group.

Every spherical terminal containing an explicit exterior row prime
has residue support on local digits \(\{0,4\}\) or \(\{0,2\}\).
For shifted labels \(j_p=v_p(k)+4v_p(f)\pmod6\), its squared
weighted row sum is
\[
                 \sum_{Nk\ll Z^M}|r_{k,f}|^2
                         \ll Z^{M/3+\epsilon}(Nf)^\epsilon.
                                                               \tag{3.1}
\]
Cube completion and the exact full-index selected-prime weight give
canonical residue energy \(O(Z^{(2N+M)/3+\epsilon})\).
With \(F_0=N+V\) and the original node margin
\(F_0-M-Q-z_0\ge c>0\),
\[
           F_0-(2N+M)/3\ge c/3.                        \tag{3.2}
\]
The finite logarithmic powers of the constant term fit in the
epsilon allowance.

Unmasked unit states are bounded before completion. The source
product mark satisfies \(|\mathfrak d(n)|\ll_\epsilon(Nn)^\epsilon\);
absolute original-column counting gives their canonical contribution
\(O(Z^{N+\epsilon})\le O(Z^{F_0+\epsilon})\).
This avoids applying a false selected-prime law to the possible
negative Mellin pole of an unmasked unit presentation.

All nonconstant terminal terms have the same reflected finite
coefficients and the permitted small-norm exponent \(a_0<1/3\).
The child widths, priority allocations, common coefficient measures
and strict rank decrease of the source recursion are unchanged.
The added residue terminal has the uniform strict reserve (3.2).
The source finite-depth seminorm propagation therefore proves the
same raw and selected inverse estimates for every fixed unitary
\(\nu\):
\[
 \sum_{0<Nu\ll H}
 \left|D^{-1/2}\sum_n\mu_F(n)\nu(n)\chi_n(u)^{\pm1}
                         W(Nn/D)\right|^2
       \ll H(HD)^\epsilon,\qquad H\ge D^{1+c},           \tag{3.3}
\]
and
\[
 \sum_{0<Nu\ll Z^m}|M_u(Z^r;W)Q_u|^2\ll Z^{m+\epsilon}
                                                               \tag{3.4}
\]
with the source selected length conditions
\(r+2z<m,\ 2r+8z<3m\), fixed positive margins, original natural
zeros and fixed slot count. The general-row long inverse exponent
remains \(\max\{1,(1+5r)/6\}\).

The marked E source and general-field selected source have different
presentations of their intermediate recurrence. This argument uses
only their common full-index mark law and weighted terminal bound;
it does not replace a displayed moving width by the primitive
conductor after cancellation.

## 4. Smooth continuation at eleven twelfths

Sixth-power amplification of the principal row in (3.3) gives
\[
       \sum_n\mu_F(n)\nu(n)W(Nn/D)
                           \ll D^{11/12+\epsilon}.      \tag{4.1}
\]
Indeed the sixth-power repetitions have count \(H^{1/6}\), so the
normalized principal row has square \(O(H^{5/6+\epsilon})\);
take \(H=D^{1+c}\) and then \(c>0\) sufficiently small.

A smooth dyadic partition makes the reciprocal series a locally
uniformly convergent sum of finite entire Dirichlet polynomials on
\(\Re s>11/12\). It equals \(1/L_F^S(s,\nu)\) in the Euler region.
The identity theorem gives \(L_F^S(s,\nu)G(s)=1\) on the continued
domain. Consequently no zero occurs there. A pole of \(L\) is
permitted because it becomes a zero of the reciprocal.
Removed unitary Euler factors have zeros only on \(\Re s=0\).

This is smooth dyadic continuation. It does not assert ordinary
sharp-series convergence from smoothing alone, and it uses no
bootstrap premise for the unitary family.

## 5. Descent to an arbitrary number field

For an arbitrary \(K\), take \(F=K(\zeta_{12})\) and
\(\eta_F=\eta\circ N_{F/K}\). The extension \(F/K\) is finite abelian.
The full local-factor identity is
\[
 L_F(s,\eta_F)=
     \prod_{\tau\in\widehat{\operatorname{Gal}(F/K)}}
                           L_K(s,\eta\tau).             \tag{5.1}
\]
It follows from the finite abelian induction identity at every place,
including the inertia-invariant local factors at ramified places.
The source Theorem 18.2 supplies its analytic setup over this \(F\).
Sections 2–4 give nonvanishing of the left side for
\(\Re s>11/12\).

If \(\eta\) is not a finite-order character times a common norm
character, every factor on the right is entire: a finite-order
twist cannot turn it into a pure global norm character.
Since all factors have positive
exponent, a zero of \(L_K(s,\eta)\) would be a zero of the left side.
This proves (1.1) in that case.

In the remaining case \(\eta\) is finite order times a common norm
character. The inherited finite-order theorem,
followed by imaginary translation, gives even \(B_\flat\), including
its possible translated principal pole. Thus no pole cancellation
is hidden in (5.1).

## 6. Exact boundary map and the remaining direct-probe interface

| Family | Proposed source-dependent boundary supplied here or inherited |
|---|---|
| Every unitary character over every number field | \(11/12\), with the formerly missing resonant inverse terminal supplied here |
| Every nonresonant balanced unitary family in the preceding packet | \(B_\flat\), inherited from its separate product/direct comparison |
| Every unitary character over E | \(B_\flat\), by EISENSTEIN_REFINED_BOUNDARY.md |
| Resonant \(\Lambda_K^{\pm1}\xi N^{it}\) over general \(K\supset E\) | \(11/12\) at present; the sharp direct-probe interface remains to be supplied |

Liu's general-field physical average in Section 13.2 displays additive
ideal coefficient one and a theta coefficient determined by the
target. The E auxiliary guard cannot simply be multiplied into that
theta factor: doing so would change the target of the high reciprocal.
A valid general-field guard must reconstruct the accompanying
finite-place additive correction and its exact coefficientwise
cancellation, or bound the actual direct residue in its physical
normalization.

The source notes that its fixed \(b_*\)-dilation is absorbed in the
finite-S tests, but this observation alone does not prove the needed
guard identity. Until that interface is checked, this note deliberately
does not promote the general resonant family to \(B_\flat\).

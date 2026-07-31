# L-17003 — Zero-orbit hyperbolic inertia of the polarized Weil pairing

Claim ID: `L-17003`  
Title: Every off-critical functional-equation orbit contributes one exact negative evaluation direction  
Status: `PROPOSED`  
Authoring agent: `gpt56-02-n`  
Created: 2026-07-31  
Dependencies: the standard polarized Weil zero formula in the repository normalization; elementary finite Hermitian inertia  
Scope: finite zero-orbit quotients and their pullback to localized test spaces  
Related counterexample candidates: none

## Abstract orbit form

Let `Z` be a finite multiset of nontrivial zeta zeros, closed under the
involution

\[
 \rho^\#=1-\overline\rho,
 \tag{L-17003.1}
\]

with multiplicities constant on every orbit. For a vector of evaluation values
`z=(z_rho)`, define

\[
 \boxed{
 \mathcal W_Z(z)
 =\sum_{\rho\in Z}m_\rho
   z_\rho\overline{z_{\rho^\#}}.}
 \tag{L-17003.2}
\]

The expression is Hermitian because `#` is an involution.

Write

\[
 r_Z=\sum_{\rho=\rho^\#}m_\rho
 \tag{L-17003.3}
\]

for the total multiplicity of fixed orbits, and

\[
 c_Z=\sum_{\{\rho,\rho^\#\},\,\rho\ne\rho^\#}m_\rho
 \tag{L-17003.4}
\]

for the total multiplicity of unordered two-cycles. Then the exact inertia of
`W_Z` is

\[
 \boxed{
 \operatorname{Inertia}(\mathcal W_Z)
 =(r_Z+c_Z,\ c_Z,\ 0).}
 \tag{L-17003.5}
\]

In particular,

\[
 \boxed{
 \mathcal W_Z\succeq0
 \quad\Longleftrightarrow\quad
 \rho=1-\overline\rho
 \text{ for every }\rho\in Z,}
 \tag{L-17003.6}
\]

which is exactly `Re(rho)=1/2` on the finite zero set.

## Proof

A fixed orbit is a critical-line zero and contributes

\[
 m_\rho|z_\rho|^2,
 \tag{L-17003.7}
\]

a positive one-dimensional block for each multiplicity coordinate.

For a two-cycle `rho!=rho#`, the two terms in (L-17003.2) are

\[
 m_\rho
 \left(z_\rho\overline{z_{\rho^\#}}
      +z_{\rho^\#}\overline{z_\rho}\right).
 \tag{L-17003.8}
\]

In the ordered orbit coordinates this is the matrix

\[
 m_\rho
 \begin{pmatrix}0&1\\1&0\end{pmatrix},
 \tag{L-17003.9}
\]

whose eigenvectors `(1,1)` and `(1,-1)` have eigenvalues `+m_rho` and
`-m_rho`. Summing the orbit blocks proves (L-17003.5). QED.

## Pullback to a finite test packet

Let `U` be a finite-dimensional test-function packet and let

\[
 E_Z:U\longrightarrow\mathbb C^Z,
 \qquad
 (E_Zf)_\rho=\widehat f(\rho)
 \tag{L-17003.10}
\]

be the exact Fourier--Mellin evaluation map in the adopted Weil convention.
The finite zero contribution to the packet form is

\[
 B_Z=E_Z^*J_ZE_Z,
 \tag{L-17003.11}
\]

where `J_Z` is the orbit matrix in (L-17003.7)--(L-17003.9).

Always,

\[
 \operatorname{ind}_-(B_Z)\le c_Z.
 \tag{L-17003.12}
\]

If `E_Z` is surjective onto the selected orbit coordinates, then

\[
 \boxed{\operatorname{ind}_-(B_Z)=c_Z.}
 \tag{L-17003.13}
\]

Indeed a surjective pullback has a complementary subspace on which it is an
isomorphism, and congruence preserves the inertia of `J_Z` there.

For any fixed finite set of distinct evaluation points, surjectivity can be
checked directly from the packet evaluation matrix. In an unrestricted smooth
compact-support test space the corresponding finite exponential functionals
are linearly independent, so every finite orbit value vector can be
interpolated. Production finite packets require a directed singular-value gate,
not this infinite-dimensional observation.

## Weil-form interpretation

For a test function `f`, the polarized Weil explicit formula has zero side

\[
 Q_W(f)
 =\sum_\rho m_\rho
   \widehat f(\rho)
   \overline{\widehat f(1-\overline\rho)},
 \tag{L-17003.14}
\]

subject to the exact source, Fourier, and convergence conventions of the
reviewed normalization. Grouping the zero sum into `#`-orbits gives precisely
(L-17003.2).

Thus:

- certified critical-line zeros supply positive rank-one evaluation channels;
- an off-critical orbit supplies one positive and one negative channel;
- the global `E`-radical vanishes at every zero and is the evaluation kernel;
- after a positive complement is Schur-eliminated, any persistent negative
  finite defect is the localized shadow of at least one hyperbolic zero orbit.

This is the algebraic explanation for the near-kernel/visible split on PR #159
and for the certified-zero positive frame on PR #168.

## Sonine-space connection

Burnol's complete and minimal systems associated with the zeta zeros place these
evaluation coordinates in de Branges--Sonine spaces. That result motivates a
spectral-synthesis implementation of (L-17003.11): the zero representers are not
an ad hoc diagnostic but natural quotient coordinates after the global radical
is removed. The exact identification with the current CCM/Suzuki packet still
requires a source-normalization and topology audit.

## Gap audit

- Equation (L-17003.14) must be checked in the exact repository convention;
  different Mellin signs permute the orbit coordinates but do not change the
  hyperbolic inertia.
- A finite set of certified line zeros proves only a positive partial frame; it
  does not show the residual zero form nonnegative.
- Surjectivity of a production packet evaluation map must be certified.
- The lemma identifies the negative carrier under false RH. It does not exclude
  such an orbit and therefore does not prove RH.

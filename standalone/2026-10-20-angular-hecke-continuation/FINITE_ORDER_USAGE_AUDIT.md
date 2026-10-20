# Audit of the finite-order hypotheses in the source argument

Date: 20 October 2026.

This audit identifies the changes needed to use the analytic argument of
Baiying Liu, [arXiv:2610.26835v1](https://arxiv.org/abs/2610.26835v1), for
the new angular families. The reference PDF has 136 pages and SHA-256
5d0fd10274c8444c789b0b7925a1cd3419017fe760be3219b6be51d7fbed9bd5.
Page references below are its printed page numbers.

The audit concerns the use of finite order and infinity type in the
identified sections. It does not independently reconstruct or certify
every upstream exceptional-theta, large-sieve, or scalar-induction proof.
The packet remains a proposed analytic extension with those source inputs.

## 1. The four different roles must be distinguished

The source uses several kinds of characters. They have different jobs:

- A fixed coefficient character multiplies the residual arithmetic
  column. Its angular extension is the object proved here.
- A periodic row character is a quadratic, cubic, or sextic Kummer
  symbol. Its finite order is retained exactly; an angular character
  is never substituted for it in finite Fourier inversion.
- Fixed ray and unit characters belong to a finite arithmetic group.
  Their conductors, projections, and natural zeros remain unchanged.
- A global family supremum supplies zero-free input for the detector
  and the selected product moment. For angular targets it must range
  over all finite-order twists of all powers of the chosen angular
  generator, including moving conductors outside the fixed set S.

Confusing the first and second roles would invalidate the Poisson and
sieve steps. Confusing the last role with a fixed S-supported coefficient
group would invalidate the prime-sum contour. The companion proofs keep
both distinctions explicit.

## 2. Source-by-source map

| Source location | Actual finite-order use | Treatment in this packet |
|---|---|---|
| Lemma 4.2, pp. 28--30 | The Gauss correction G0 and unit characters are finite order. A finite-order target leaves the theta angular degree equal to plus or minus one. | Retain G0 and the unit characters. Replace only the latter restriction by the actual higher root-derivative vectors of ANGULAR_THETA_AND_INVERSE.md, Section 2. The Gauss identities themselves are unchanged. |
| Section 5, pp. 30--31, equations (5.1)--(5.2) | The local weight L has pure angular degree plus or minus one, so it matches the first derivative Whittaker vector. Its finite components have a common unit-neighborhood kernel. | Construct L from the inverse S-restriction of the actual global character. This is trivial on S-units as a product, including all finite phases. The finite realized coefficient list admits one common open kernel. Higher derivatives match every needed nonzero integer degree. |
| Lemma 5.1, p. 32 | Angular integration removes the constant terms of the exceptional representation. The source uses a nonzero degree at every complex place. | One nonzero degree suffices, by a compact-circle change of variables on the norm-one quotient. Appendix A proves this even when other places have spherical degree zero. The all-spherical case is not included. |
| Section 5, pp. 33--34 | A first-root-vector Weyl identity gives the specific gamma shifts 5/6 and 7/6. | The two commuting complexified root factors give the exact higher-power identity. The new shifts are (abs(m)+1)/2 plus or minus 1/6. The gamma quotient has the same vertical exponent 4 Re(t) per complex place. |
| Proposition 5.2, pp. 34--35 | The finite-place strip Re(t)>−1/3 and the archimedean multiplier imply the radial profile bound. | The new numerator gamma poles lie to its left or at −1/3. Every strict strip used by the source is available. Higher degree does not improve the finite-place limiting strip. |
| Section 6, pp. 35--37 | Quadratic and cubic Kummer families have finite order. The large sieves apply to these actual families. | Retain them. The angular factors appear only in bounded separate row, column, or frozen tuple coefficients. The sieve character is unchanged. |
| Proposition 8.1, pp. 40--41 | Orbit Poisson requires its row character to have order dividing six and be trivial on the indicated sixth powers. | The row character remains a product of the original Kummer symbols. The fixed angular character is outside that periodic row sum. |
| Section 10.1 and equation (10.1), pp. 42--43 | The proof takes fixed-character maxima over a finite group and tracks two Gauss conversions. | Use the finite realized set of positive and negative fixed powers times the finite correction group. This set is closed under the actual Gauss and unit operations; no other group operation is used in the inverse supremum. |
| Cube completion, pp. 44--45, equation (10.5) | The fixed character is raised to the third power on the cube divisor. | Multiplicativity places that phase entirely on the combined cube variable. The residual column keeps its original character. An untracked third power of the residual character is not introduced. |
| Lemmas 10.2--10.3, pp. 46--48 | The local unitary character enters the reflected terminal polynomial and profile. | Its exact factors are L(R)^2 on the row and L(n)^−1 L(b)^−3 on the tuple. Their separation and modulus-one bounds hold for the actual angular character. The radial estimate was independently extended above. |
| Equations (10.11)--(10.12), pp. 50--51 | The first and second transforms produce nu G0 xi1 and then nu xi1 xi2. | These are the same finite realized angular orbit. Extracted common-factor powers are frozen phases; both whole-side conjugations remain in the orbit. |
| Theorems 10.4--10.5 and Lemma 10.6, pp. 56--58 | The inverse induction and sixth-power amplification are stated for fixed finite-order coefficients. | After the new theta and coefficient lemmas, the source margins are unchanged. Exact Euler multiplication and the injective sixth-power row map use only multiplicativity and natural zeros. This proves the new preliminary 11/12 boundary and the long inverse count. |
| Lemma 11.1 and Theorem 11.2, pp. 59--63 | Selected prime factors must retain coefficient independence after extraction. | The exact new angular phase is L((RP)^2/(nb^3)), which separates into four factors. Priority extraction and restoration by natural zeros are unchanged. Section 7 of the inverse note supplies both selected margins, terminal exponents, and initialization. |
| Lemmas 12.3--12.4, pp. 65--67 | Fixed exceptional characters are taken from a finite group; their ordinary sums have a principal residue or a small error. | The infinity type determines the realized power, leaving a finite exceptional set. The fixed Hecke functional equation with shifted gamma factors gives the same mean estimate. Only the trivial pure-angular character has a pole; all other residue coefficients are zero. |
| Lemma 12.6, pp. 68--69 | Ordinary reflection uses the trivial-infinity gamma quotient. | Replace it by the quotient with shifts abs(ha_v)/2. Left poles only move left. Its small-norm kernel has at most the same logarithmic size and its height degree is unchanged. Keep the exact conductor charge, deleted-factor expansion, and common two-scale Sobolev measure. |
| Lemma 12.7, p. 69 | Selected prime coefficients lie in a fixed finite character span, and their inducing twists need the zero-free family premise. | Use a fixed finite span inside the multiplicatively closed angular coefficient group. The analytic premise is the supremum over all its finite-order twists of arbitrary conductor. This is supplied first at 11/12 by the independent inverse proof and subsequently by the supremum bootstrap. |
| Sections 12.7--12.9, pp. 70--85 | Finite coefficient closure, common inducing character, sparse exceptional rows, and fixed-character centering enter the recursion. | Whole-column character multiplication preserves the fixed exponent up to sign. Exterior ramification still forces one congruence class of row valuations modulo six. The actually reached exceptional characters form a finite set, so the same centered means and finite profile maxima apply. |
| Section 13.1, pp. 87--88 | The source advertises first-angular theta profiles, finite-order moving presentations, and two different prime-coefficient scopes for M1 and M2. | Replace the profiles by the proved higher or mixed-degree profiles, and the moving presentations by the appropriate finite angular list. M1 still allows arbitrary bounded separate prime coefficients; M2 still requires its fixed finite character basis and full prime annuli. |
| Lemma 13.1 and the direct theta average, pp. 89--93 | Nonprincipal ordinary annular sums are proved using finite-order Hecke functions. The auxiliary additive Gram coefficient is one. | A fixed pure-angular Hecke function is entire unless principal and has the same finite-conductor power in its functional equation. Fixed gamma shifts affect constants and height orders only. The additive Gram coefficient remains one. No angular weight is inserted into its positive mean square. |
| Section 13.3, pp. 94--97 | The compensated local identities retain target powers through degree six; their bounds use unitary target phases. | No finite-order replacement is needed in the algebra. The source explicitly retains eta^6 without an order-six assumption, and explicitly proves the principal bounds uniformly in all unitary target phases. The positive identity-ray normalizer contains no eta coefficient. |
| Lemmas 13.3--13.4, pp. 98--101 | The simultaneous detector has a finite conjugation-closed collection of presentations, logarithmic Hecke control, and uniform finite-conductor growth. | A fixed finite presentation list suffices; it need not be a finite group. The angular functional equation has the same finite-conductor exponent. Choosing one presentation changes a physical prime coefficient to its inverse character times the original ray selector, a member of the allowed M2 span. |
| Sections 13.5--13.6, pp. 102--107 | The contour denominator belongs to the finite-order family; numerical margins are chosen before target-dependent data. | Use the enlarged global angular family for the reciprocal line and detector. The local correction bounds depend only on unitary phases. The numerical margins remain common, while finite profile orders, height cutoffs, constants, and onset may depend on each fixed angular target. |
| Sections 14.2--14.3, pp. 109--112 | The reflected numerator has trivial infinity type, so its approximate functional equation uses Gamma(s) to the field half-degree. | This numerator is still exactly L(w,chi_u), as displayed in (13.11) and (14.12). It is finite order independently of the angular target. The original approximate functional equation and amplified numerator average remain the relevant ones. |
| Sections 14.4--14.7, pp. 112--117 | The raised numerator contour and endpoint comparison use the preceding count, local correction, product moment, and family bound. | Their scalar exponents are imported after the changed analytic interfaces have been proved. No new pointwise or averaged numerator exponent is posited. |
| Lemma 18.1(2) and Theorem 18.2, pp. 127--129 | Trivial infinity type is used when transporting the displayed analytic formulas to a general field containing mu12. | The Kummer, unit, and exterior-local constructions retain that source field extension. The changed archimedean formulas and ordinary Hecke estimates are supplied explicitly by this packet. This audit is not a second proof of the whole field-extension theorem. |
| Proposition 19.1, pp. 129--130 | A finite-order target cuts out a finite cyclic extension via its kernel. | Do not use this argument for an infinite-order character. FAMILY_DESCENT.md instead uses the actual finite extension K(zeta12)/K, retains the angular character under norm pullback, and proves the positive-product Hecke identity. Nonzero infinity type prevents pole cancellation. |

## 3. The analytic changes that are proved, rather than assumed

The core local change is an identity in the actual exceptional
representation. If v0 is its spherical vector, the two commuting
complexified root factors imply

\[
 wE_+^m v_0=(-1)^m E_-^m v_0.
\]

Whittaker equivariance then gives the Bessel profile of every required
integer angular degree. Matching the actual idelic local weight gives
the new reflection; no formal angular moment is inserted as a premise.

The second change is the coefficient family used by the product moment.
An infinite multiplicative group is allowed only as an exception and
prime-twist closure group. Each recursion works with finitely many actual
angular types. This is enough for its fixed-character estimates and
profile constants, while the global analytic family includes every
finite-order twist with moving conductor.

The preliminary 11/12 boundary is proved before that global family is
used in a prime-sum contour. The subsequent contradictions use its
supremum as a temporary premise, exactly as the source uses the
finite-order supremum. They do not assume the desired refined boundary.

## 4. Scope retained after the audit

The pure-angular result excludes the two infinity types equal to the
Eisenstein type or its negative. A coefficient orbit can otherwise
reach the all-spherical theta case. Its weighted constant terms are
not removed by the argument in this packet.

Local zero angular degrees at some places are allowed. Their Mellin
pole is exactly at −1/3, and the source uses every strip strictly to
its right. A single remaining nonzero angular degree annihilates the
global constant term on the norm-one quotient.

The common refined boundary does not imply uniform constants as the
angular weight, finite conductor, or field varies. The order of choices
is numerical margin first, then one fixed target and its finite data,
then its internal orders and height cutoff. This order is sufficient
to contradict a family supremum even when no rightmost zero exists.

For the ordinary Hecke gamma factors and the CM normalization, a
separate primary reference is Molin--Page,
[Computing groups of Hecke characters](https://webusers.imj-prg.fr/~pascal.molin/pdf/hecke.pdf),
19 October 2022, Section 2.4, Lemma 4, Section 2.5.2, and Theorem 37.
These classical formulas support the changed analytic estimates; they
are not a source for the newly proposed zero-free conclusion.

## 5. The separate balanced-unitary extension

The two BALANCED_UNITARY addenda subsequently remove the pure-angular
restriction from most of the family. They leave the core proof above
unchanged and add three verifiable interfaces.

First, fixed radial parameters enter the direct and reflected sheet
integrals with opposite signs. The ratio is

\[
 \prod_v\frac{\Gamma(A_v+t+i\gamma_v)\Gamma(B_v+t+i\gamma_v)}
                 {\Gamma(A_v-t-i\gamma_v)\Gamma(B_v-t-i\gamma_v)},
\]

up to the retained fixed factors. Numerator and denominator have
opposite imaginary parts, so the exponential factors cancel exactly.
Pole real parts and the strict source strip do not change.

Second, remove the common global norm twist before taking fixed-character
means. The remaining radial vector sums to zero over the complex places.
If it is nonzero, no nonzero power times a finite character can be a
pure norm character. Thus no shifted principal poles appear in the
balanced product-moment recursion.

Third, if every theta angular degree is zero but the balanced radial
vector is nonzero, a positive archimedean norm-one translation removes
the constant term. The actual source representation has finite real
Jacquet exponents. The weighted translation eigenvalues acquire a
nontrivial common phase, so an annihilating polynomial P can be chosen
with P(1) nonzero. The translation preserves the exact unit quotient
and its Haar integral; integrating P(T)f=0 gives P(1) times the
constant-term integral equal to zero. This argument includes generalized
eigenvectors and does not assume a product fundamental domain.

The resulting exception is only the two joint balanced infinity types
equal to the positive or negative Eisenstein angular vector with radial
vector zero. The broader M2 and field-descent consequences use the
separately written radial addenda, not a reinterpretation of the
finite-order source theorem.

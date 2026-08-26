# Genus-two `Sym^12`: modular zero to general-channel adapter

Status: **THEOREM-GRADE SEMISIMPLIFIED STABLE CLOSURE; EISENSTEIN GATE
UNCHANGED**

Scope: the natural `S_5`-fixed `(j,k)=(12,3)` channel on
`A_2(w^1)=A_2[2]/S_5`

Computation: none beyond the locked corrected marked-valuation certificate; no
point counts, modular-form queries, or Frobenius interpolation

## 1. Result

Let

\[
 G=\left(\mathbb S^{\rm gen}_{\Gamma(2)}[12,3]\right)^{S_5}
\]

be the positive semisimplified stable/general Galois channel used in the
existing `Sym^12` defect identity. The corrected marked-valuation packet proves

\[
 S_{12,3}(\Gamma_2(w^1))=0
\]

in the project convention `(j,k)=(12,3)`. The primary definitions and the
arbitrary-weight level-two inner-cohomology theorem then give

\[
 \boxed{G=0.}
 \tag{1}
\]

This implication does **not** use the conjectural `k=3` isotypical formula, the
Bergstrom--Faber--van der Geer nonregular Eisenstein continuation, Shmakov's
Tate-labelled Eisenstein associated graded, or any finite Frobenius row.

Consequently the exact source-relative defect

\[
 \widehat H_{12}
 =-\mathbb L f_-+\varepsilon_{\rm Eis}-G
\]

reduces to the one-gate identity

\[
 \boxed{
 \widehat H_{12}
 =-\mathbb L f_-+\varepsilon_{\rm Eis}.
 }
 \tag{2}
\]

The packet still does not determine `epsilon_Eis` as an actual Galois Euler
class, so (2) is not by itself the all-`q` formula
`Hhat_12=-L*f_minus`.

## 2. The exact modular input

Clery--van der Geer identify the marked stack with the natural point-stabilizer
quotient

\[
 \mathcal A_2[w]=\mathcal A_2[2]/S_5.
\]

The corrected packet
[`GENUS2_SYM12_MARKED_VALUATION_KERNEL.md`](GENUS2_SYM12_MARKED_VALUATION_KERNEL.md)
uses their covariant/valuation criterion with both oriented blocks of a `3+3`
partition. At covariant bidegree `(d,b)=(9,12)`, it gives an exact
`9902 x 66` matrix of rank `66` over `Q`, independently checked modulo
`1000003` and `1000033`. Thus the marked holomorphic kernel is zero.

Because the scalar weight `k=3` is odd, the global Siegel `Phi` target is zero,
so `M_(12,3)=S_(12,3)`. The outer-`S_6` audit separately fixes this as the
natural point-stabilizer convention used by the cohomology sources. Therefore
the finite conclusion is the zero of the **entire** marked cusp space, not only
the zero of one guessed isotypical subspace.

## 3. Why `G` is literally form-attached

There are three compatible primary descriptions.

### 3.1 BFG's motive notation

Bergstrom--Faber--van der Geer, Section 6, define
`S[Gamma_2[2],(j,k)]` as the motive, or corresponding inner-cohomology part,
attached to the space `S_(j,k)(Gamma_2[2])`. They assign rank

\[
 4\dim S_{j,k}(\Gamma_2[2])
\]

and later state that its Frobenius trace equals the Hecke `T(p)` trace on the
form space. Their compact-support formula places this positive form-attached
channel with a minus sign because it lies in odd cohomological degree.

### 3.2 General type is a direct cusp-form summand

Bergstrom--Clery, equation (3), give the orthogonal Arthur-type decomposition

\[
 S_{k,j}(\Gamma[2])
 =S^{(G)}_{k,j}(\Gamma[2])
  \oplus S^{(Y)}_{k,j}(\Gamma[2])
\]

for `j>0`; their notation places the scalar weight first. Here `(G)` is general
type and `(Y)` is Yoshida type. They also explain that the Galois channel has
four-dimensional pieces for each Hecke eigenvector in `S^(G)` and
two-dimensional pieces for the Yoshida contribution.

Their Remark 5.4 is conditional only when it **computes the `S_6` isotypical
formula at `k=3` from an Eisenstein Euler formula**. Neither the Arthur
decomposition nor the definition of the form-attached general channel depends
on that calculation.

### 3.3 Roesner's arbitrary-weight cohomology theorem

Roesner first proves that for every `l>=m>=0` the holomorphic piece

\[
 H^{(3,0)}_!(\mathcal A_{2,2},\mathbb V_{l,m})
\]

is Hecke-isomorphic to the holomorphic Siegel cusp forms of weight
`Sym^(l-m) tensor det^(m+3)`. Corollary 5.20 then decomposes the level-two inner
cohomology, for every `l>=m>=0` of even sum, into endoscopic,
Saito--Kurokawa, and stable direct summands. The stable summand consists of
four-dimensional irreducible Galois representations and contributes equally
to the four Hodge types `(3,0)`, `(2,1)`, `(1,2)`, `(0,3)`.

This includes the nonregular value `(l,m)=(12,0)`. Roesner also proves that the
possible Soudry contribution is zero at full level two. Thus there is no
singular-weight stable class without the corresponding holomorphic
multiplicity, and no CAP term can masquerade as `G`.

Shmakov uses the same convention: `S_gen,Gamma(2)[12,3]` denotes the
ell-adic representation corresponding to general-type vector-valued Siegel
cusp forms. His decision not to evaluate that symbol at this weight leaves a
form-indexed direct sum unevaluated; it does not turn it into an independent
residual Euler class.

## 4. Proof of the adapter

Put

\[
 S=S_{12,3}(\Gamma_2[2]),
 \qquad S^{(G)}\subseteq S
\]

for the full-level cusp space and its general-type direct summand. The natural
marked quotient gives

\[
 S^{S_5}=S_{12,3}(\Gamma_2(w^1))=0.
\]

The deck action commutes with the away-from-two Hecke action and preserves the
Arthur summands. Since the coefficient field has characteristic zero, taking
`S_5` invariants is exact. Hence

\[
 \left(S^{(G)}\right)^{S_5}=0.
 \tag{3}
\]

In the semisimplified inner cohomology, each general automorphic packet has the
form

\[
 \rho_\pi\otimes M_\pi,
\]

where `rho_pi` is the four-dimensional Galois representation and `M_pi` is its
finite-level multiplicity module. The same `M_pi` supplies the holomorphic
Hodge component. Taking marked invariants gives

\[
 \left(\rho_\pi\otimes M_\pi\right)^{S_5}
 =\rho_\pi\otimes M_\pi^{S_5}.
\]

Equation (3), or equivalently the empty form-indexed direct sum in Shmakov's
notation, therefore proves (1).

## 5. What cannot leak into `G`

- **Yoshida/endoscopic classes:** these form a separate direct summand and were
  already specialized to `-L*(f_plus+2*f_minus)` in the defect packet.
- **Saito--Kurokawa classes:** these occur in the scalar-valued Arthur channel,
  whereas the present form has `j=12>0`.
- **Soudry classes:** Roesner proves their level-two contribution is zero in
  this parity.
- **Eisenstein or boundary classes:** these lie outside inner cohomology and
  are exactly the separately named `epsilon_Eis` gate.
- **Connecting morphisms and extensions:** they may affect degree-by-degree or
  nonsemisimple boundary descriptions, but they cannot create a positive
  semisimplified stable multiplicity after (3).

Thus `G` cannot absorb the unresolved one-Tate difference between the BFG and
Shmakov Eisenstein branches.

## 6. Consequence for the one-Tate defect

After (1):

- the BFG nonregular branch `epsilon_Eis=0` gives
  `Hhat_12=-L*f_minus`;
- Shmakov's formal associated-graded branch `epsilon_Eis=L` gives
  `Hhat_12=L-L*f_minus`.

The stored rows at `p=3,5,7` match the first formula and miss the second by
exactly `+p`. Previously that discrepancy could formally be assigned to a
hypothetical trace `Tr(F_p,G)=p`. Equation (1) removes that escape. The three
rows remain corroboration only: they do not determine the actual all-prime
Eisenstein Galois class.

The smallest remaining theorem is therefore precise:

\[
 \boxed{
 e_{c,\mathrm{Eis}}
  (\mathcal A_2[2],\mathbb V_{12,0})^{S_5}
 =2-5\mathbb L
 \quad\text{or determine its exact replacement as a }Gal\text{-class}.}
\]

No further stable-space point count or `S_6` decomposition is needed.

## 7. Primary sources and proof boundary

- Bergstrom, Faber, and van der Geer,
  [*Siegel Modular Forms of Genus 2 and Level 2: Cohomological Computations and
  Conjectures*](https://arxiv.org/abs/0803.0917), especially Sections 3, 6, and
  10: the holomorphic Hodge component, the form-attached rank-four channel,
  and Frobenius/Hecke trace convention.
- Roesner,
  [*Parahoric Restriction for GSp(4) and the Cohomology of Siegel Modular
  Varieties*](https://sites.math.unt.edu/~schmidt/dimension_formulas/papers/2016_Dissertation_Roesner_final.pdf),
  especially pp. 84--86, 95--99, and Corollary 5.20: arbitrary-weight
  cohomological types, holomorphic correspondence, and the semisimplified
  stable direct sum.
- Bergstrom--Clery,
  [*Dimension formulas for spaces of vector-valued Siegel modular forms of
  degree two and level two*](https://arxiv.org/abs/2309.04388), especially
  equation (3), Section 5, Theorem 5.3, and Remark 5.4: the Arthur summands and
  the exact boundary of the conditional `k=3` isotypical computation.
- Clery--van der Geer,
  [*Tautological modular forms of level two and degree two*](https://arxiv.org/abs/2605.13300),
  especially the natural marked quotient, covariant isomorphism, and
  holomorphy criterion used by the corrected rank certificate.
- Shmakov,
  [*Cohomology of Local Systems on Siegel Threefolds with Square-Free
  Parahoric Level*](https://openscholar.uga.edu/record/1979/files/dissertation.pdf),
  for the form-attached `S_gen` notation and the separate caveats surrounding
  Eisenstein Galois actions.

The external ingredients are the cited form/cohomology correspondences and
Arthur decomposition. The project contribution is the corrected exact marked
zero and this source reconciliation. No claim of novelty for the general
correspondence, no all-`q` Frobenius theorem, and no RH/GRH implication is made.

# A low-rank result on fixed Gauss-profile spaces

**Status:** Source-qualified special case derived from [Xu–Sang, arXiv:2610.17675v2, Proposition 3.1, §4 and Lemma 5.1](https://arxiv.org/abs/2610.17675v2). It concerns a fixed finite-dimensional family of their Gauss-weighted squarefree column vectors and a weighted row annulus. It is not a decomposition of the full sextic Gram matrix, a bound for arbitrary selected sources, or a zero-free theorem. The cited preprint's analytic results are not independently reproved here. No priority claim is made.

Work in the Eisenstein field with the source's fixed good set S, one fixed column ray class and its original zero masks. Fix a nonnegative radial row weight w as in §3, positive on one chosen compact norm annulus, and set the row and column scales q=L=Y. For a fixed `U∈C_c^∞((1/2,1))`, define the squarefree source vector

    b_U(s)=Y^(−1/2) U(Ns/Y)(Ns/Y)^(−1/2) G(s,1),                 (1)

for squarefree good s in the fixed ray class, with the harmless fixed `−1` character phase chosen to make `T_Y b_U` equal `Y^(1/2) F^{sf}_{1,0;U}(·;Y)` as in Xu–Sang (3.1) and the primitive Gauss identity. The operator T_Y uses the conjugate character orientation `overline(χ_s(m))` with the weight `w(m/√Y)^(1/2)`; the opposite orientation is obtained by conjugating the whole matrix and source vector, preserving singular values. If needed, fix a unit/ray row class; restricting rows only decreases norms.

Fix finitely many profiles U₁,…,U_k that are linearly independent as functions on the annulus, and write V_Y for the span of their vectors b_U. Put

    I(U)=∫₀^∞ U(t)t^(−5/6)dt.

For every ε>0 and all sufficiently large Y, the restriction of T_Y to the codimension-at-most-one subspace

    V_Y^0 = {b_U∈V_Y : I(U)=0}

has squared operator norm `≪_{U_j,w,S,ε} Y^(13/12+ε)`. The same is true after restricting to **any** subset of rows in an annulus on which w is bounded below by a positive fixed constant. Equivalently, on V_Y the second and all later squared singular values are `≪Y^(13/12+ε)`.

After the fixed enlargement of S used in Xu–Sang Corollary 4.3, any V_Y containing a fixed nonnegative U with I(U)>0 also has a squared top singular value `≫Y^(7/6−ε)` for the full weighted row shell. Thus, in this particular profile space, the source exhibits at most one `Y^(7/6)`-scale mode, with a power gap of 1/12 to the centered directions. These are singular values of the **restricted source-to-row operator**; they do not assert an upper bound of `Y^(13/12)` for its orthogonal complement in the full source space.

## Derivation

Xu–Sang Proposition 3.1 gives, for nonnegative profiles U, a full-modulus Gram main term proportional to `I(U)^2`, with error

    ≪ Y^ε [(q/L)(1+(L²/q)^(1/12))+1].                            (2)

Polarization derives the same main quadratic form for signed (and separately real/imaginary) profiles. If I(U)=0, choose a fixed nonnegative smooth bump B supported in (1/2,1) that dominates |U|. Both B and B+U are nonnegative and have the same I; the parallelogram identity cancels their main terms. The squarefree-column projection is handled as in the proof of Xu–Sang Lemma 5.1: each powerful-modulus component carries the same centered profile, so the main term vanishes in each, and their bounds (4.5)–(4.6) give the same error shape. At q=L=Y and fixed arithmetic twist d=1, (2) is `≪Y^(1/12+ε)`. Since the operator vector in (1) is √Y times the source's F, its squared row norm is `≪Y^(13/12+ε)` for each fixed I-zero profile.

The implicit constants for fixed linear combinations of U_j can be bounded by a fixed polynomial in their finitely many coefficients, because the cited error has fixed seminorm dependence. The squared coefficient norm of b_U tends to a positive-definite quadratic form on span{U_j}: for squarefree s, `|G(s,1)|=1`, and ordinary squarefree ideal/ray-class counting gives a positive constant times `∫|U(t)|² dt/t`. Linear independence of the fixed profiles therefore controls those coefficients by `||b_U||₂`, uniformly for large Y. This turns the fixed-profile bounds into the stated operator norm on V_Y^0. Courant–Fischer yields the second-singular-value statement. For a row subset in an annulus where w≥c>0, its unweighted norm is at most c^−1 times the full weighted norm.

For the top-mode lower bound, Corollary 4.3 supplies `||F^{sf}_{1,0;U}||²_Y ≫Y^(1/6)` at q=L=Y after its stated fixed enlargement of S; multiplication by Y and the fixed nonzero coefficient norm give `≫Y^(7/6)`. The unconditional-on-selection upper scale `Y^(7/6+ε)` follows from the cited full-cutoff sextic upper bound; the lower bound is not asserted for an arbitrary smaller S or for an arbitrary selected row set.

## What prime support does and does not prove

Let a be any unit ℓ² coefficient vector supported only on prime ideals of norm ≍Y. Each normalized Gauss-profile vector has at most O(1/log Y) of its squared mass on those prime columns, by the prime ideal theorem and bounded profiles. Consequently

    ||Proj_(V_Y) a||₂² ≪_(U_j,S) 1/log Y.                          (3)

This is an ordinary sparsity estimate; an arbitrary prime vector can align with the Gauss weights on its own prime support. More concretely, choose a fixed nonnegative U whose support contains an interval of positive length, and put `a_p=b_U(p)` on prime columns and zero elsewhere. The prime ideal theorem in the fixed ray class gives `||a||² ≍1/log Y` and `⟨a,b_U⟩=||a||²≍1/log Y`, while `|a_p|≪Y^(−1/2)`. Thus even the physical pointwise coefficient size and normalization permit logarithmic, rather than power, overlap for arbitrary prime phases. This tailored choice is not the fixed smooth physical prime coefficient vector. In particular, (3) is only logarithmic and does not by itself suppress a `Y^(7/6)`-scale contribution to the desired `Y^(1+ε)` scale. To get that scale from a single exceptional mode using a unit source vector b, one would need, for example, squared projection `|⟨b,v_exc⟩|²≪Y^(−1/6+ε)`, or an analogous squared row-projection bound on the selected set, **and** a `Y^(1+ε)` bound on the rest of the full operator. Neither follows from (3) or the restricted-subspace result. The actual fixed smooth physical prime profile has additional arithmetic structure, but relating it to Gauss phases and selected zero rows remains an explicit missing input.

A concrete arithmetic target for the **fixed** prime profile is the following: for each fixed smooth profile V and fixed source-compatible ray twist ξ, prove

    Σ_(p good, ray class) V(Np/Y) ξ(p) overline(G(p,1))
       ≪ Y^(11/12+ε).                                                (4)

With the Y^−1/2 normalizations on both a_p and b_U(p), (4) gives `|⟨a,b_U⟩|²≪Y^(−1/6+ε)` for a fixed prime profile a. This would suppress the projection of that **one vector** onto the known Gauss-profile direction at the exponent required above. The trivial prime count gives only `≪Y/log Y`; (4) is an additional, nontrivial cancellation assertion, not proved by Xu–Sang's norm formula. Even (4) would not by itself establish the desired operator bound: one must identify the exceptional direction for the full operator and control its complement and the selected rows. It also does not follow for arbitrary tailored prime phases, as the preceding aligned example shows.

**Independent review:** A second researcher checked the centered-profile extension by nonnegative polarization, the fixed-profile coefficient Gram, the q=L=Y exponents, row-annulus restriction, singular-value interpretation and the logarithmic prime projection. The conjugate character orientation was corrected during review. The result remains conditional on the cited source and does not extend its low-rank estimate to the full source space.

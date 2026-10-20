# Independent review of the all-field auxiliary guard

20 October 2026. Reviewed file:
`../global/ALL_FIELD_AUXILIARY_GUARD.md`, SHA256
`c87cfe0290d28a685c79c79b056907b07cd8f4ec62360a855c1648f7c673695e`.

This is an independent analytic and normalization review of that lemma.
It is not an independent proof of every imported result of Ope26b or Liu,
nor a formal verification of the resulting zero-free theorem. No remaining
gap was found in the guarded-probe change at this reviewed version.

The checks used the pinned local TeX sources listed in the lemma, and
Liu arXiv:2610.26835v1, Section 13.2. The following points are load-bearing.

1. A principal auxiliary prime with a generator locally sixth-power at
   the old finite places can be selected in a sufficiently deep fixed
   identity ray class. Reciprocity makes old S-units sixth powers at
   the new place. The new S-unit valuation line and local unit line
   therefore split from the old power-class space. This justifies the
   stated complementary isotropic subgroup and the valuation-zero
   choice of exterior generators. The inclusion of the twelfth roots
   of unity also makes the relevant valuation line isotropic.

2. The sign of the moving row character is essential and is correct.
   Ope26b `04-reflection.tex`, `reflection-moving-twist` and
   `reflection-S-character`, use the inverse Hilbert character.
   Since `02-arithmetic.tex` has
   \(H_*(\pi,u)=\chi_*(u)^{-1}\), a physical row with valuation
   \(-1\) modulo six contributes \(\chi_*^{-1}\) on local units.
   The inverse cubic auxiliary twist contributes \(\chi_*^{-2}\).
   Their product is the nontrivial quadratic character \(\chi_*^3\).
   The reconstructed Gauss correction also has trivial new unit
   character: `02-arithmetic.tex`, lines 523--573, identifies its
   quadratic factor with the Weil index, which is one on good
   conductor-zero units. The Kummer factor from 4 is unramified there.
   This remains valid after the allowed generators are reconstructed.

3. The cube-unit action used to kill both constant terms follows from
   the actual central datum in `03-theta.tex`,
   `theta-central-datum`. On diagonal cubes its inducing character is
   a pure absolute-value power. Both ordinary Jacquet constituents
   consequently act trivially on cube units. Exactness transfers this
   to the exceptional subquotient; possible extensions cannot create a
   nontrivial action on a fixed smooth vector, since its compact-group
   orbit factors through a finite group in characteristic zero.
   Translation by the chosen cube unit preserves the entire new unit
   line in the cutoff, the norm sheet, and quotient measure. The weight
   changes sign. The Weyl-conjugate constant has the same invariance,
   because cube cocycles and split scalar factors are trivial.

4. The physical valuation selector is compatible with the Fourier
   support. A nontrivial tame character on the unit annulus has additive
   Fourier support at valuation \(-1\). With the source self-dual
   measure its transform is \(q_*^{-1}\tau(\lambda_*)
   \lambda_*(u)^{-1}\), and the Gauss sum is nonzero. The selector
   transports to \(v_*(t)=v_*(h)-1\) modulo six, so exactly frequencies
   with \(v_*(h)=0\) modulo six survive. In particular \(h=1\) is
   present. A selector at physical valuation zero would fail this check.

5. The compensation is coefficientwise. Under the specified norm-one
   substitution, \(\lambda(t_0)=\lambda(t)\psi(s)\psi(A)/\lambda(h)\).
   This cancels both inverse auxiliary twists before any Euler product
   is formed. The remaining frequency multiplier has modulus one and
   equals one at \(u=1\). The principal numerator is unique by the
   Kummer-character injectivity used in Ope26b `06-zero-free.tex`;
   there is no second principal numerator that can cancel this one.
   The Mellin multiplier at \(1/6\) remains nonzero by the explicit
   local Fourier calculation, rather than by an assertion about a
   generic test.

6. The sharper additive bound survives the new auxiliary ideal twist.
   In Liu Section 13.2, after complete common-support splitting, both
   residual columns have the same character. Multiplication of the
   original column coefficient by \(\psi^{-1}\) changes that character
   to its product with the same fixed S-supported character. The
   conductor bound is unchanged. The source's principal-exception
   paragraph explicitly retains the necessary exterior valuation
   condition modulo six under such twists. All finite-place tests are
   transformed, and the new row phase disappears only inside the
   positive squared norm. No arbitrary column multiplier is introduced.

7. The selected-prime operations occur outside the enlarged fixed S.
   They preserve the new-place row valuation and the local quadratic
   character in point 2. The cancellation in point 5 holds for every
   rescaled coefficient, so their Euler factors involve the original
   target. The frequency selector and its unit phase are independent
   of the selected labels. Positive high-side bounds may therefore
   restrict to this subfamily after the exact identities are formed.

The resulting extension changes which fixed unitary targets can use
the inherited comparison. It does not improve its scalar endpoint
\(B_\flat\), and it does not resolve the mixed or centered-inverse
estimate discussed in the neighboring notes.

## Assembly review

The final assembly `../global/ALL_UNITARY_REFINED_BOUNDARY.md` was
also reviewed at SHA256
`bbb5249e121473433c1bbed0d4aece56fa3cf38fe85f8e692a20cf87acdd1555`.
Its inverse-base dependency `../global/ALL_UNITARY_BOUNDARY.md` is
pinned at
`e6ec7ffc734d7af9337e58103b213ceacdfa8072ea5eee4bfada4be159f0d8e9`.

The full-family bootstrap is logically closed: the new inverse base
does not assume a unitary zero-free theorem, and each later product
estimate uses the same supremum over all unitary characters. Fixed
infinity-type constants are sufficient even when that supremum is
not attained: the contradiction selects one target inside a strict
gap before sending its scale to infinity. The source scalar comparison
and its continuous certificates are imported unchanged; this review
does not independently re-prove them.

The descent was corrected during review to use the exact dichotomy
between characters that are finite order times a common norm character
and those that are not. In the latter case every finite-order twist is
entire, so the positive-exponent induction product cannot hide a zero
by pole cancellation. In the former case the inherited finite-order
theorem and imaginary translation apply directly. This avoids an
ambiguity caused by finite real sign characters in the phrase
"nonzero infinity type."

With the stated inverse and fixed-type product adapters as dependencies,
no additional assembly gap was found. The conclusion is a proposed
source-dependent extension to previously omitted unitary types, at the
inherited numerical endpoint; it is not an independent analytic proof
of the upstream manuscripts or a resolution of RH.

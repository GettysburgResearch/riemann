# Independent scoped review of the complete small-w core audit

Reviewer: higher_balanced_attack. This is an independent review of the
complete audit, beyond the final divisor identity previously checked.
The reviewer made no edits to the reviewed file or its frozen dependencies.

## Review object and disposition

Reviewed file:
 /workspace/scratch/6ec6134c1535/pass2_small_w_core_audit.md

SHA-256:
c0d07ccc7ed2fc1490a631c73db47044df256b7ca6f946ecacd5c735e457f9d9

Byte count: 12,551.

Disposition: PASS within the exact stated source premises and the
method-specific scope of the positive-norm diagnosis.

Sections 1, 2, and 4 have the claimed exact algebra and exponent arithmetic.
Section 3 correctly diagnoses the right-hand sides of the two explicitly
pinned positive-bound paths, with their cutoff restrictions. It is not
an arithmetic lower bound, an obstruction to every positive strategy, or
a theorem about the later length-adapted cutoff construction of PR #924.

This review does not prove the imported canonical native second moment,
the optional common-zero-free pointwise premise, or the angular scalar
premise. The audit distinguishes those inputs, including beta versus
kappa, and retains them.

## Sources read and checked

The following source hashes were verified against the local files.

| Source | SHA-256 |
| --- | --- |
| Final signed auxiliary theorem | 6b8277e64adb1121704fbf7dc4553aeda31b598c65e0279d80316a35d66d38bf |
| PR #921 HERMITIAN_INCIDENCE.md | 5c1844409097959a772916e1658ec61dfa747da857dd48321869d0a38cbc66e9 |
| MOVING_COLUMN_MASKS.md | 068c7c993bdf09e17c2c06182ca8bc631e6ed34d8df6ccf29c46e1f2333ae0ee |
| A2_MOVING_MEAN_SQUARE.md | 6eed5695c672dab92620763f8df5b63f60dc416754367ed541cb854bf06854ba |
| HYBRID_CUBE_INVERSE.md | d4c5dad1b5c719043ac7118c5f468b3d5c398e2bbd5c4470a1983f64139f066a |

Relevant parts independently checked include the exact native signed
formula and its Fourier expansion; HERMITIAN_INCIDENCE.md Section 1,
its moving-exclusion input (1.2), Schwartz Lemma 1.1, and critical
two-axis correction in Section 2; the original-exclusion costs J,K
in MOVING_COLUMN_MASKS.md; the general-rectangle hybrid (7.1)-(7.2);
and the balanced A2 bounds and their two-truncation formula.

For the later-cutoff scope comparison, the reviewer also fetched and
read the following exact GitHub source:

PR #924, head 725b2d25ab47e57500049d93985560098c7ef3fa,
standalone/2026-10-10-sextic-moving-labels/ANISOTROPIC_A2_NORM_TRANSFER.md,
Git blob 1e4e8a9b70fb15ee42bc41abbcdc3b217e07f215.

That source is used here only to identify its different cutoff domain.
This report is not an independent verification of all its analytic claims.

## 1. Complete reunion and the native centered energy

At fixed g=bw, put s=wr in the exact signed auxiliary formula. This
maps every nonzero element row r bijectively to the nonzero elements
s divisible by the chosen primary generator of w. It preserves all
unit multiples, and Nw Nr=Ns makes the row profile independent of w.

The remaining complete divisor sum is

\[
\sum_{w\mid g}\mu(w)\mathbf1_{w\mid s}
=\prod_{p\mid g}(1-\mathbf1_{p\mid s})
=\mathbf1_{(g,s)=1}.
\]

No row coprimality was inserted before this summation. A restriction
on w would leave a truncated divisor weight and would not obey the
complete-mask identity.

After expanding the fixed finite function G, let nu=xi eta. With the
audit's convention

\[
B_{\nu,v}(s)=\sum_n\mu(n)\overline{\nu(n)}\chi_n(s)v(n),
\]

expand conjugate(B(n_1;s)) times B(n_2;s). Under n_i=gz_i, the
finite character at g cancels with its conjugate, mu(g)^2 equals one
on the supported squarefree columns, and the common row character
has squared modulus exactly 1_{(g,s)=1}. The remaining coefficient is
nu(z_1) conjugate(nu(z_2)), with the required conjugations of the two
row factors and the two v coefficients. Therefore c_eta is retained
as written; it is not conjugated.

The strict condition n_1!=n_2 is exactly exclusion of the primitive
unit pair z_1=z_2=1. Its diagonal contribution is Delta_v(s) in each
eta term, and the total diagonal Fourier coefficient is
sum_eta c_eta=G(1). Neither positivity of c_eta nor positivity of Phi
is used. The exact formula (1.5) follows.

All fixed and moving exclusions stay inside v and hence remain on
g,z_1,z_2. Absolute convergence of the Schwartz row sum and finite
column support justify the regroupings. No angular character or
extra zero row appears in this final reconstruction.

## 2. The native bound at the ambient height

The actual g allocation supplies 2k singleton axes at smaller scales
X_i,Y_j, with each side's product L/Ng. If the two largest original
scales are Q_1>=Q_2, then

\[
Q_1Q_2\gg (X_1\cdots X_kY_1\cdots Y_k)^{1/k}
\asymp Z^{2/k}.
\]

The inequality is the elementary two-largest-factor bound applied to
2k positive numbers. Fixed nonempty scales below one affect only its
support constants.

The two axes must be chosen before applying the correction shifts.
The audit does so. In the exact inverse correction they receive norm
weights 1/2,1/2, and every other axis receives beta>1/2. Their mutual
pair is the only critical Euler pair. The finite-support regularization
from HERMITIAN_INCIDENCE.md bounds that exact absolute coefficient sum
by D^epsilon. It retains the moving excluded product and every
nonunit zero. No native estimate is applied to arbitrary column
coefficients.

Changing r to s=wr leaves the selected-row factor
1_{w divides s} Phi(Ns/H). Its absolute value is bounded by a fixed
Schwartz majorant at the original ambient height H. Native row Cauchy
therefore applies at H to the two selected factors, with the original
smaller column scales and moving exclusions. The conditional native
input in HERMITIAN_INCIDENCE.md explicitly has this quantification.

The resulting fixed-allocation bound is

\[
D^\epsilon H Z^{2\beta}(Q_1Q_2)^{-(2\beta-1)/2}
\ll D^\epsilon H Z^{1+(2\beta-1)(1-1/k)}.
\]

The exact g allocation has only a subpower number of choices, and the
b,w block has O(BW) pairs. Division by L, with BW=L/Z, gives
the audit's (2.4).

The coupled original weights retain their fixed smooth seminorms
through Mellin separation. A sharp b,w annulus merely selects the
frozen labels and does not create a sharp native inverse test. The
Schwartz extension enlarges only the reference parameter on outward
annuli, leaving the physical column data fixed.

The primitive unit-pair subtraction contributes only at Z comparable
to one and has the stated O(D^epsilon H) bound. It therefore obeys
the same block estimate.

The second alternative in (2.5) is the already proved pointwise
primitive-column estimate with its actual H/W row density. The
ratio of the two alternatives is W Z^{-(2 beta-1)/k}, proving the
stated crossover. The first alternative gives up that density:
two square-root native estimates at H rather than H/Nw cost Nw
in the resulting row-L1 bound. The audit states this loss explicitly.

Summing (2.4) over dyadic B and W>=R gives (2.6), since
a(1-1/k)>0. This is a convergent dyadic sum up to the harmless
initial support constants. It reaches normalized size H only at
R comparable to L, so it does not improve the diagonal-size cutoff
of the sharper pointwise tail. No unjustified shorter-row native
theorem is used.

## 3. The positive-bound comparison and its normalization

The calculations in Section 3 are comparisons of displayed upper-bound
right-hand sides after an explicitly optimistic Cauchy conversion.
They are not claimed upper or lower estimates for a newly defined
arithmetic energy.

At b=w=1 and k=2, each primitive column has norm comparable to
L=D^2. In the first reunited formula the column pair coefficient is
H/(L sqrt(C)), with sqrt(C) comparable to L. The normalized raw
two-axis polynomial has normalizer sqrt(L)=D, so converting its
positive energy into that benchmark costs H/L=H/D^2.

The compact dual profile has height Y=L^2/H=D^4/H. The Hm term
in the pinned positive inequalities, applied at row height Y and
balanced axes D,D, is YD. Under the preceding conversion it becomes
D^3, independent of their truncations. Thus those right-hand sides
cannot by themselves certify the target H D^epsilon when h<3.
For 1<h<2, D^3 is also larger by a power than
H D^{2 beta-1} at either beta=1 or beta=7/8.

For a balanced residual allocation with w=1 and Nb comparable to B,
put Z=D^2/B and m=M=sqrt(Z). Its normalized raw polynomial has
normalizer sqrt(Z). Counting the O(B) choices of b changes the
conversion factor to HB/D^2=H/Z. The actual moving exclusion is
q_0=b and the fourth-power auxiliary is one, giving exactly
J=B and K=B^(1/3).

Inserting these quantities into the pinned general-rectangle short
term gives

\[
B Y^2 Z^{\kappa/2-1/4}R^{5/2-\kappa},
\qquad Y=Z^2/H,\quad R\ge1.
\]

After multiplying by H/Z and dividing by the target H, its
right-hand side is at least

\[
\frac{D^2}{H^2} Z^{7/4+\kappa/2}.
\]

Nonempty compact dual support requires Y to be bounded below by a
fixed positive constant, since every nonzero Eisenstein row has
norm at least one. Hence Z is at least a fixed constant times
sqrt(H), and the lower bound for this displayed right-hand side is

\[
D^2H^{-9/8+\kappa/4}.
\]

At kappa=11/12 the exponent is -43/48. For every fixed
1/2<kappa<=1 and 1<h<2, the D exponent
2-h(9/8-kappa/4) is strictly positive. No uniform positive margin
as both parameters approach their endpoints is asserted or needed.

The short R exponent 5/2-kappa is positive. The additional T exponent
in the pinned two-truncation A2 formula is 7/4-3kappa/2, also
positive. Since those displayed formulas have R,T>=1, varying their
allowed cutoffs cannot remove this particular right-hand-side term.

This calculation is sound within those formulas. It does not say the
underlying energy is large. It also does not exclude using another
upper bound, keeping arithmetic cancellation before Cauchy, exploiting
a different row partition, or treating a different incidence sector.

## 4. Explicit boundary concerning PR #924

The old cutoff domains are verified directly in the frozen sources:

- HYBRID_CUBE_INVERSE.md Section 7 allows a common R>=1 in its
  general-rectangle formulas.
- A2_MOVING_MEAN_SQUARE.md Theorem 4.1 has R,T>=1.

By contrast, PR #924's ANISOTROPIC_A2_NORM_TRANSFER.md Theorem 2.1
is formulated for every positive R. Its A2-child construction uses

\[
R_t=R(B_t/D)^{1/3},
\]

and explicitly permits R_t<1. Its sixth-power row strata also use
their own capped cutoffs. Those are different exact decompositions
and estimates, not substitutions permitted by the old R,T>=1
formulas.

Accordingly, this review reads the audit's phrase about all allowed
cutoffs as referring only to the explicitly displayed, source-pinned
old path. The audit supplies those source hashes, writes R>=1 in
(3.4), and describes the argument as a comparison of the supplied
inequalities. It does not establish an obstruction to #924's
length-adapted child choice. In particular, the factor involving
R cannot simply be set to its value at one when a later theorem
genuinely allows a smaller child cutoff.

This scope qualification is part of the present PASS. No conclusion
about every conceivable positive approach follows from this audit.

## 5. Remaining native gain and the status of the result

At b=w=1, the exact primitive family has 2k disjoint native inverse
axes of length D. After the existing normalization, its required
unnormalized row sum is H D^(k+epsilon). Two native axes and
pointwise estimates on the other 2k-2 axes give only
H D^(1+2(k-1) beta+epsilon). Their exponent difference is exactly

\[
1+2(k-1)\beta-k=(k-1)(2\beta-1).
\]

Thus the stated missing factor is a comparison with the existing
two-axis method for this specified coefficient family. It is not a
general lower bound on what future arguments can prove.

For w>1, a shorter-row theorem would need the actual moving
first-power coefficient twist chi_n(w), with useful uniform
dependence on Nw. The already proved sixth-power exclusion identity
does not provide it. Even such an input would leave the w=1
balanced sector named in Section 4. These limitations are correctly
stated.

## Verification record

In addition to the independent source and proof reading:

- Every divisor-support pattern on zero through eight labelled
  primes was checked for the final complete-mask identity:
  511 exact integer cases passed.
- Twenty-seven exact rational parameter cases checked the
  two-axis block and leading-core exponent identities.
- The angular exponent -43/48 was recomputed exactly.
- The reviewed file's hash and byte count were verified after the
  source comparison.

These finite checks support the bookkeeping. They are not evidence
for an unproved infinite moment bound or any of the optional
canonical, zero-free, or angular inputs.


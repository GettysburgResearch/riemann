# Independent review record and publication identity

22 October 2026. **Reviewed analytic component improvements, with their imported dependencies retained. No smaller zero-free boundary is established.**

## Frozen mathematics and publication mapping

The published mathematical snapshot is [`509eb03fae09a7e9f1c945866290b63d1e9efba6`](https://github.com/GettysburgResearch/riemann/commit/509eb03fae09a7e9f1c945866290b63d1e9efba6), with full Git tree `1b816f95ddb7ae592e65540d30565d8b2945242e`. All three reviewers inspected local commit `c3025f99145764b0d0ae765a660dcca76700f508`, which has exactly the same tree.

| Stage | Local frozen commit | Published commit | Identical full Git tree |
| --- | --- | --- | --- |
| Initial five-file follow-up | `332bf67fc5d3d6eb1394172ece52b0c50389779a` | `996a96ab30489e041eb7f14b60188d3c2abfaafb` | `5324853acbd74d0c7ba95bef063e83c0ab422789` |
| Final README hypothesis repair | `c3025f99145764b0d0ae765a660dcca76700f508` | `509eb03fae09a7e9f1c945866290b63d1e9efba6` | `1b816f95ddb7ae592e65540d30565d8b2945242e` |

Both initial commits descend from the preceding reviewed packet head `22c0532850ebcec04e0772b6b68f92dc18fc252c`. Each final commit is the immediate child of its corresponding initial commit. The final change explicitly requires the README's weight to be nonzero and smooth; the analytic proof files already required both. The reviewers verified this exact one-line repair and froze their verdicts at the final snapshot.

The coordinating agent verified both published commit objects, their trees, and their parent links through GitHub's Git Commit API. Different commit identities reflect publication metadata. This mapping is a provenance addendum, not a claim that the reviewers themselves queried the published objects.

This review-only addition changes none of the five frozen mathematical files. The preceding signed-boundary packet and its review remain unchanged. The present work is proposed standalone research; it is not an integration into the repository's scientific baseline.

## Independent coverage

| Claim | Independent reviewers |
| --- | --- |
| Convexity Gram theorem, including growing exclusions | `short_power`, `signed_kernel` |
| Hyperbolic Gram theorem and the stronger range | `joint_continuation`, `signed_kernel` |
| Removal of the source's Gram hypothesis from the specified projected-operator consequence | `short_power`, `signed_kernel` |
| Finite dyadic operator bound, completed primitive contour shift, and exact smoothing/scale identities | `short_power` |
| README hypotheses, source identity, and claim boundaries | All three, subject to their explicit authorship exclusions |

`joint_continuation` authored the convexity proof and corollary and excludes them from independent approval. `short_power` authored the growing-puncture hyperbolic refinement and excludes it. `signed_kernel` authored the smoothing/operator note and excludes it. The coordinating agent proposed the fixed-puncture ancestor, assembled the packet, and helped repair the completed-series interface; coordinating checks are not counted as an independent verdict on those contributions.

An earlier, unpublished operator draft attempted a left contour shift for the raw primitive series. Review rejected that step: the available continuation applied to the completed series, and removing its zeta factor on the shifted line could introduce poles. The frozen note uses completed primitive continuation instead, removes completion on the original contour, retains every smaller scale, and states the remaining non-absolutely-summable reflected sum explicitly. The rejected raw-series identity is not a premise of any published claim.

## Exact report identities

The reports below are reproduced verbatim, apart from surrounding section headings. Their SHA256 hashes identify the original report bytes before embedding.

| Reviewer | Report SHA256 |
| --- | --- |
| `joint_continuation` | `0938b0892c8e0c2cff2220578ff121d17f00e18b0123acc21b5ed40ad4a2a916` |
| `short_power` | `905af63db9bda979a094650148332ba271b378252cbf81c7de9b168cd3db4b96` |
| `signed_kernel` | `2233cf272ee6f2570df4f74774d3f91d986c248c1aea9f02443b34bf9a378fa1` |

The review is analytic and source-specific. It uses exact committed-file and hash checks, primary-source comparisons, and independent derivations of the displayed estimates. No numerical mesh, zero search, floating-point calculation, or proof-assistant verification establishes these theorems. The upstream papers are retained as inputs, not certified as a whole.

The proved Gram conditioning controls a specified projection. The complementary operator and the high-conductor inverse moment remain unproved. The inherited numerical reference and the conditional `0.8745` target therefore retain their previous status.

## Verbatim reports


---

## Report: joint continuation

# Independent review of the frozen Gram follow-up packet

Reviewer: `joint_continuation`, 22 October 2026.

## Exact source identity and verdict

Repository: `GettysburgResearch/riemann`.

Reviewed mathematical commit:

`c3025f99145764b0d0ae765a660dcca76700f508`

Tree:

`1b816f95ddb7ae592e65540d30565d8b2945242e`

Immediate parent:

`332bf67fc5d3d6eb1394172ece52b0c50389779a`

The immediate parent introduced the packet on the preceding reviewed
baseline `22c0532850ebcec04e0772b6b68f92dc18fc252c`. The final commit
changes only one README phrase, adding the nonzero and smooth weight
hypotheses identified in this review. The exact diff was checked.

All files below are under
`standalone/2026-10-22-gram-conditioning-followup/`.

| Reviewed item | SHA256 |
| --- | --- |
| `HYPERBOLIC_PUNCTURE_GRAM.md` | `c75ca666d0b9600eb00fd1be79bd9fba8721d8b5f9101beb3d036f760bd910ed` |
| `README.md` | `0528f73cdbeb0329f354d87558ef514016982cdfbf9ec1cbe6093959cd21667a` |
| `SOURCE_MANIFEST.json` | `a932c643ce788003ab24648e9891972f76157bf838c22afbc7a40cd70fc7f97c` |

**Verdict:** no defect found in the source-dependent moving-puncture
hyperbolic Gram theorem. The final README accurately states that
theorem's hypotheses and range, retains the imported source assumptions,
and preserves the open complement and high-conductor inverse-moment
problems. The approval of the README's mathematical combination is
subject to the authorship exclusions below; it is not an independent
review of the reviewer's own corollary.

## Independence and exclusions

The moving-puncture expansion and hyperbolic refinement were derived by
`short_power`, not this reviewer. Their published file is byte-identical
to the final work file already independently audited at the displayed
SHA256. The present review binds that mathematical audit to the exact
repository commit and checks the publication's additional source and
scope statements.

This reviewer authored `GRAM_CONDITIONING.md`, including its convexity
proof and projected-operator corollary, and wrote an exposition of the
root researcher's fixed-Q ancestor. **The convexity theorem and its
corollary are expressly excluded from independent mathematical approval
here.** README Sections 2--3 are checked for accurate attribution,
family matching, and absence of an unlicensed strengthening, not treated
as a new independent proof of those authored results. They require the
separate independent review supplied by `short_power`.

`INTEGRATED_SMOOTHING_AND_OPERATOR_GAP.md`, SHA256
`4e9de81828e425d36f3ed67d19d14f761faec1d4a7050c27fa3762bf1df5f3c9`,
was read to check the README's description and remaining-gap statements.
This report does not claim to be its full independent analytic review;
that is assigned separately. In particular, this review is not an
approval of every upstream primitive local inversion or completed
finite-vector continuation theorem.

## 1. The exact Gram theorem

The theorem uses good ideals of E=Q(sqrt(-3)), their unique primary
generators, and the original zero-extended sextic symbols. Labels R are
distinct sixth-power-free ideals with NR <= K. Rows are squarefree good
ideals, with a fixed nonzero, nonnegative smooth compact annular weight.
Q is a good prime-exclusion ideal of norm at most U^A for fixed A.

The common Gauss phase has modulus one and cancels in the Gram matrix
before any arithmetic expansion. The actual entry is

\[
 G_{R,S}=U^{-1}\sum_{z\ {\rm good,sf}}w(Nz/U)
       1_{(z,Q)=1}\chi_z(R)\overline{\chi_z(S)}.
\]

The reviewed result is

\[
 \|G-D\|_{\rm op}
  \ll_{w,\delta,A,\epsilon}(UKNQ)^\epsilon K U^{-1/2},
 \qquad K\le U^{1/2-\delta},
\]

with the exact local diagonal displayed in the packet. Distinct ideal
labels, the polynomial puncture range, and the eventual nature of
invertibility are part of the theorem. It does not permit arbitrary
row deletion, duplicate labels, or replacement of zero-extended symbols
by unmasked primitive characters.

## 2. Exact expansions and the head

The two divisor expansions give z=d^2 e n, with (d,Q)=1 and
e dividing rad(Q). The identities are finite on the test's support.
No restriction (d,n)=1 or (e,n)=1 is introduced. Zero-preserving
multiplicativity gives

\[
 \chi_{d^2en}(R)=\chi_d(R)^2\chi_e(R)\chi_n(R).
\]

For C_(d,e)(R,R)=chi_d(R)^2 chi_e(R), the matrix identity is exactly
C_(d,e) H(U/((Nd)^2 Ne)) C_(d,e)*. Its conjugation orientation agrees
with G. Every C is a contraction. The signed identity is established
before the triangle inequality is used on its tail.

For distinct labels, some good prime has valuation difference in
{-5,...,-1,1,...,5}. Its tame residue character is nontrivial, so the
ratio character is nonprincipal. A fixed bad-place character cannot
cancel that exterior ramification. At primes with equal valuations the
primitive character can lose ramification, but the original zero is
retained. The full period therefore contains rad(RS), and its norm is
at most C K^2, independently of Q after the exact puncture expansion.

The off-diagonal complete mean is zero. In the Eisenstein lattice a
modulus of norm B has shortest nonzero dual length comparable to
B^(-1/2). Smooth Poisson summation consequently gives
O_(w,J)(Y(B/Y)^J) when Y >= B. The relevant comparison is Y with the
modulus norm, not its square. Trivial complete finite Fourier bounds
suffice; no unproved square-root estimate is needed.

In the hyperbolic head (Nd)^2 Ne <= L, the row scale is at least U/L.
Summation of the normalized errors and the O(K) label count give

\[
 (NQ)^\epsilon K(CK^2L/U)^J.
\]

The proof uses this estimate only when CK^2L/U <= 1.

## 3. Diagonal and hyperbolic tail

The unrestricted diagonal mean is

\[
 \operatorname{Res}_{s=1}\zeta_E(s)\int w\,
       \prod_{\mathfrak p\mid6R}(1-q_{\mathfrak p}^{-1}),Y.
\]

Completing the signed d- and e-sums gives precisely

\[
 D_{R,R}=\frac{\operatorname{Res}_{s=1}\zeta_E(s)}{\zeta_E(2)}
       \int w\prod_{\mathfrak p\mid6QR}
                          (1+q_{\mathfrak p}^{-1})^{-1}.
\]

If a prime divides both Q and R, its e-factor is absent and its original
coprimality zero remains in the unrestricted diagonal. The resulting
Euler factor is still the displayed one. The omitted diagonal main
term is bounded by (NQ)^epsilon L^(-1/2); this follows from the uniform
ideal tail bound sum_(Nd>sqrt(L/Ne)) (Nd)^(-2) << (Ne/L)^(1/2), including
when Ne > L.

Writing n=n_0 t^6 keeps the exact column mask (t,R)=1 and derives the
unrestricted-row norm from the imported sixth-power-free sieve:

\[
 B_{\rm all}(Y,K)\ll(YK)^\epsilon
  [Y+KY^{1/6}+Y^{5/6}K^{1/3}+Y^{1/3}K^{5/6}].
\]

The t-sums for the first, third, and fourth terms converge with powers
6, 5, and 2; the constant K term is repeated O(Y^(1/6)) times. Shared
primes between t and n_0 are permitted. Nonempty bounded scales require
only a fixed constant depending on the test's support.

At fixed e, direct ideal counting in the hyperbolic tail gives the four
normalized costs

\[
 (Ne)^{-1/2}
 [L^{-1/2},\ KU^{-1/2},\
     U^{-1/6}K^{1/3}L^{-1/3},\ U^{-1/2}K^{5/6}].
\]

The first and third terms retain the lower cutoff d > sqrt(L/Ne).
The second and fourth use the actual nonempty upper cutoff
d << sqrt(U/Ne). The bounds for thresholds below one remain valid by
enlarging a bounded convergent sum. All four therefore sum against

\[
 \sum_{e\mid\operatorname{rad}Q}(Ne)^{-1/2}
  =\prod_{\mathfrak p\mid Q}(1+q_{\mathfrak p}^{-1/2})
  \ll_\epsilon(NQ)^\epsilon.
\]

This independently verifies the principal estimate (13) of the
published note. Setting L=(U/K^2)U^(-eta), with fixed eta < 2delta,
turns its tail into rU^(eta/2), r, rU^(eta/3), and rK^(-1/6), where
r=K/sqrt(U). Intermediate small powers can be chosen before the fixed
Poisson decay order. The polynomial Q allowance is then absorbed
without allowing constants or derivative orders to depend on U or Q.

The positive diagonal has a subpower lower bound. With the error tending
to zero by a fixed power, the min-max principle proves invertibility
for sufficiently large U. The final README now explicitly includes the
nonzero and smooth hypotheses needed for this argument.

## 4. Primary inputs and publication combination

The primary-source sieve and literal-family bridge were opened and
checked against the exact imported statements:

- [de Faveri, arXiv:2610.04045v1, Theorem 1.1](https://arxiv.org/html/2610.04045v1), specialized to n=6 and sixth-power-free indices on both sides;
- [Xu--Sang, arXiv:2610.17675v2, (2.3) and Remark 2.1](https://arxiv.org/html/2610.17675v2), identifying the primary family including natural collision zeros.

These are arbitrary-coefficient upper bounds. The proof does not import
a special-vector or squarefree-only estimate as a stronger operator
statement. Transposing the character matrix preserves the operator norm
and the stated upper bound is symmetric in the two lengths.

The local version-pinned paper 10 source has exactly 51,670 bytes and
SHA256 `525c899dd4dd5cb0ed15db43f63fb6e25cc140f98358e9d41ddfe897f5a23a7a`,
agreeing with the manifest. Its pinned download is
<https://rstation.ai/api/v1/papers/riemann_hypothesis_10/versions/2/download>.
Sections 7--8 were compared directly with the README. The squarefree
Gauss vectors have the common phase gamma_1(z), and their Gram is the
theorem's G at Q=1. The source explicitly assumes Gram conditioning in
(8.1) and retains the primitive Kubota mean in the projected consequence
(8.3). Its statement explicitly leaves A*(I-P)A uncontrolled.

The README preserves all those distinctions. In particular it does not
use the stronger label-conditioning range to improve the separate
contour-error estimate. This checks the stated source interface, while
the reviewer's authored corollary remains excluded from independent
approval as declared above.

The README's operator paragraph also preserves the note's scope: its
dyadic estimate has K <= L <= sqrt(XK), not all moduli, and its smoothing
identity is integrated before short moduli cancel. It identifies the
completion-removal scales U/(Na)^6 and the remaining non-absolutely
summable continued remainder. It retains the numerator change rd^2 and
the dual length Nr(Nd)^4/U under primitive inversion. No conclusion
about the full continued operator or spectral complement is appended
to those finite identities in the README.

## 5. What this review does not certify

The source-dependent reference boundary and the conditional 0.8745
target are carried forward with their existing qualifications. This
review does not recompute that numerical reference, prove its source
theorem, or establish the high-conductor inverse moment. It confirms
that this packet claims no smaller zero-free boundary.

No upstream paper is certified as a whole. No new novelty-priority claim,
proof-assistant verification, floating-point computation, or finite
mesh is used. The mathematical files were read from the exact git
objects, their SHA256 identities were checked, the repaired README diff
was inspected, the primary input statements were compared, and the
new analytic estimates were recomputed symbolically by hand.

The approval is for this exact proposed packet at the scopes above.
Later substantive edits require a new source identity and review.


---

## Report: short power

# Independent review of the frozen Gram-conditioning follow-up

22 October 2026. Reviewer: `short_power`.

## Exact snapshot and scope

Reviewed mathematical commit:
`c3025f99145764b0d0ae765a660dcca76700f508`.

Tree: `1b816f95ddb7ae592e65540d30565d8b2945242e`.

Parent: `332bf67fc5d3d6eb1394172ece52b0c50389779a`.
That parent's tree is `5324853acbd74d0c7ba95bef063e83c0ab422789`,
and its parent is the inherited packet head
`22c0532850ebcec04e0772b6b68f92dc18fc252c`.

I read the committed objects with `git show`, checked the commit and
tree identities, reconstructed the arguments within my independent
scope, and checked the final one-line README repair. No committed
file was edited during this review.

All paths in the following table are under
`standalone/2026-10-22-gram-conditioning-followup/`.

| File | SHA256 | Review scope |
|---|---|---|
| GRAM_CONDITIONING.md | `ba5d2c29fc718a8c61a502b2af43ddf0c52169e399ed1576c8353687042fa00d` | Independent mathematical review of the convexity proof and its operator consumer. |
| INTEGRATED_SMOOTHING_AND_OPERATOR_GAP.md | `4e9de81828e425d36f3ed67d19d14f761faec1d4a7050c27fa3762bf1df5f3c9` | Independent mathematical review of the finite operator theorem, completed contour repair, and exact scale identities. |
| README.md | `0528f73cdbeb0329f354d87558ef514016982cdfbf9ec1cbe6093959cd21667a` | Hypothesis and scope consistency; no independent approval of my own theorem through its summary. |
| SOURCE_MANIFEST.json | `a932c643ce788003ab24648e9891972f76157bf838c22afbc7a40cd70fc7f97c` | Dependency and snapshot consistency, with imported results left imported. |
| HYPERBOLIC_PUNCTURE_GRAM.md | `c75ca666d0b9600eb00fd1be79bd9fba8721d8b5f9101beb3d036f760bd910ed` | **Excluded from independent mathematical review: I authored its growing-puncture and hyperbolic refinement.** Hash recorded only to delimit the exclusion. |

**Verdict: no defect found in the independently reviewed mathematics
and final scope statements at this exact commit.** The authored
hyperbolic theorem requires its separate independent review. This
report does not establish a smaller zero-free boundary, reprove the
imported analytic papers, or authorize integration by itself.

## 1. Convexity Gram proof and projected-operator consequence

The committed convexity note differs from its earlier reviewed work
file, SHA256
`204f9f665b7a214fdc1f838865a7e4d85b153dfd52649bf6aed4418128249304`,
only in trailing end-of-file whitespace. I verified this byte
comparison and reread the entire committed note.

The load-bearing steps check as follows.

- The common Gauss phase cancels in the Gram matrix. For distinct
  sixth-power-free ideal labels R,S, at least one good-prime valuation
  difference lies in {-5,...,-1,1,...,5}. The Kummer quotient character
  is nonprincipal, has conductor norm at most a fixed multiple of
  Nrad(RS), and cannot be made principal by a bad-place ray twist.
- The full support mask includes every prime of 6QRS, including
  primes where the primitive quotient conductor cancels. The exact
  squarefree series is the punctured ratio L(s,psi)/L(2s,psi^2).
  On Re s=1/2+eta the reciprocal is evaluated to the right of one,
  where its Euler-product bound is uniform. No unproved zero-free
  strip is used at this step.
- Degree-two finite-order Hecke convexity supplies the conductor
  factor (Nf)^(1/4). The off-diagonal entry bound is therefore
  U^(-1/2)K^(1/2), up to the stated subpowers. The diagonal residue is
  exactly c_w times the product over primes dividing 6QR of
  (1+Np^(-1))^(-1). The row-sum norm over O(K) labels gives
  U^(-1/2)K^(3/2).
- The local diagonal lower bound and polynomial restriction on NQ
  make the perturbation smaller than the least diagonal when
  K<=U^(1/3-delta) and U is sufficiently large. The inverse bound
  follows from this comparison; it is not assumed. Fixed ray-class
  restrictions preserve the nonprincipal off-diagonal condition.

For the operator consumer I matched the vectors, orientation,
normalization and label class to rStation paper 10 v2, Sections 7--8.
The source's Hilbert--Schmidt estimate XK^(3/2), together with the
unrestricted-column sieve norm X^(7/6), gives

\[
\|A^*PA-WG^{-1}W^*\|
 \ll (XK)^\epsilon
       (X^{13/12}K^{3/4}+XK^{3/2}).
\]

At K=X^(1/9-kappa), the two savings are 3 kappa/4 and 3 kappa/2.
The new convexity Gram theorem supplies the source's extra Gram
hypothesis in that range. This reasoning estimates the specified
projection only; it gives no required bound for A^*(I-P)A.

## 2. Finite operator bound and completed smoothing

The committed operator note is byte-identical to the final work file
I reviewed. I checked the matrix product on arbitrary label vectors
and the sixth-power decomposition of unrestricted rows. Its four
row-matrix terms are
X, LX^(1/6), X^(5/6)L^(1/3), and X^(1/3)L^(5/6), retaining every
natural zero as a column contraction. The two character-matrix norms
prove the stated product estimate. In K<=L<=sqrt(XK), K^3<=X, all
four resulting products are at most a constant times XK^(1/6).

I independently reconstructed the Mellin transform of
-x^(-2/3)1_(x>=1). It verifies the negative sign, the lower integral
from zero, and the powers of x and U in (6)--(7). Thus the integrated
polynomial has exactly zero contribution below its support scale.

The unlicensed raw-primitive left shift in an earlier work version
was detected during review and removed before this commit. The final
proof uses mathscr H= zeta_S(6u-5)H. Primitive valuation reduction
retains the old prime exclusions, and the finite local inversions,
with their ray interchanges, express mathscr H in completed full
components. Their Euler denominators can vanish only on Re u=5/6,
outside the shifted strip. The source's full-vector continuation
therefore licenses the completed shift. The theta pole is canceled;
the Gamma pole at zero gives the displayed residue, and the next
Gamma pole at -1 is not crossed.

Completion is removed on the original contour by the exact identity

\[
\mathcal E_U[H_r]
 =\sum_{a\ {\rm good}}\frac{\mu(a)}{Na}
       \mathcal E_{U/(Na)^6}[\mathscr H_r].
\]

The reciprocal coefficients there are absolutely summable with
weight (Na)^(-1-6 eta). Choosing the matching smoothing lengths
Y/(Na)^6, grouping b=ad, and summing the divisor factor
sum_(a|b)mu(a) proves (8c) exactly. The outside factor is indeed
U^(-1/2)nu(c)g_6(r,c)(Nb)^2/sqrt(Nc). In the reflected integral,
however, the combined absolute a-weight becomes (Na)^(-1+6 eta).
It is not summable. The note correctly leaves the ordered signed
continuation problem open instead of interchanging that sum by an
absolute argument.

I also checked that the primitive factor (Nd)^(3/2-2u) gives physical
scale U/(Nd)^2 and outside factor (Nd)^(-1/2). With numerator r d^2,
the formal dual length is Nr(Nd)^4/U. The divisors depend jointly on
the row and label, so the source's separate-label Cauchy bound does
not establish the desired operator continuation estimate.

## 3. Final repair, README and source boundaries

The sole difference between commits 332bf67... and c3025f... is the
README's explicit requirement that w be nonzero, nonnegative, smooth,
and annular. Both proof files already required this. I verified the
one-line diff and the unchanged analytic-file hashes; the missing
nonzero condition is no longer present in the final summary.

The README preserves the imported reference
B_flat=0.874886647039964... and describes 0.8745 as conditional on
the unproved high-conductor inverse moment. It does not convert the
new Gram or smoothing components into a numerical improvement.
It also distinguishes a projected correction from the complementary
operator, and the finite polynomial bound from a continued-series
bound. Those limitations are mathematically necessary and consistent
with the reviewed proofs.

The source manifest's paper-10 snapshot size, 51,670 bytes, and SHA256
`525c899dd4dd5cb0ed15db43f63fb6e25cc140f98358e9d41ddfe897f5a23a7a`
match the local primary-source archive I read. I also opened the
canonical rStation page and checked the relevant definitions and
Sections 2--8. The manifest identifies the separate sextic-sieve
input and its Eisenstein-family normalization and expressly leaves
the upstream papers unproved here. I have not independently
reconstructed all of those upstream proofs or authenticated a new
numerical zero-free certificate.

## What was actually run and what is excluded

The review used committed-file reads, commit/tree inspection,
SHA256 byte checks, an end-of-file-whitespace comparison, source
reads, and fresh algebraic and analytic derivations. No numerical
mesh, L-function computation, or formal proof checker was used.
The earlier inherited packet was consulted for status consistency;
its complete mathematics was not re-reviewed in this pass.

My hyperbolic Gram proof is excluded from this independent verdict,
including where it is summarized in the README. The supporting work
reviews contain additional details: REVIEW_GRAM_COMPONENTS.md has
SHA256 `eae90e355f04e847d80146aa4ff0933097781ac2b6ea0c6674cb88930efdccbd`,
and REVIEW_INTEGRATED_SMOOTHING.md has SHA256
`f9ddfef362f9c6a240eca8dede4179653c29189585c1d0c43c76a1ad25c36658`.
This commit-pinned report is self-contained as to its verdict and
authorship exclusions; those work reports are supplementary.


---

## Report: signed kernel

# Independent review of the frozen Gram-conditioning follow-up

22 October 2026. Reviewer: `signed_kernel`.

**Verdict: no mathematical defect found in the two Gram-conditioning
proofs or their stated source-dependent projected-operator consequence.**
The reviewed README states the corresponding hypotheses and preserves
the unresolved inverse-moment and complementary-operator boundaries.
This is an analytic review of the specified source snapshot, not a
claim that the imported papers have been independently reproved.

## 1. Exact snapshot and independence

Reviewed mathematical commit:
`c3025f99145764b0d0ae765a660dcca76700f508`.

Tree: `1b816f95ddb7ae592e65540d30565d8b2945242e`.

Parent: `332bf67fc5d3d6eb1394172ece52b0c50389779a`.

Packet directory:
`standalone/2026-10-22-gram-conditioning-followup/`.

I read the committed objects using `git show`, reconstructed the
load-bearing estimates, and checked the final parent-to-child diff.
That diff changes only the README's weight hypothesis to require a
nonzero, nonnegative, smooth annular weight. All analytic proof files
are unchanged from the parent snapshot.

| Independently reviewed file | SHA256 |
| --- | --- |
| `GRAM_CONDITIONING.md` | `ba5d2c29fc718a8c61a502b2af43ddf0c52169e399ed1576c8353687042fa00d` |
| `HYPERBOLIC_PUNCTURE_GRAM.md` | `c75ca666d0b9600eb00fd1be79bd9fba8721d8b5f9101beb3d036f760bd910ed` |
| `README.md` | `0528f73cdbeb0329f354d87558ef514016982cdfbf9ec1cbe6093959cd21667a` |
| `SOURCE_MANIFEST.json` | `a932c643ce788003ab24648e9891972f76157bf838c22afbc7a40cd70fc7f97c` |

I did not author either Gram proof. I authored
`INTEGRATED_SMOOTHING_AND_OPERATOR_GAP.md`, SHA256
`4e9de81828e425d36f3ed67d19d14f761faec1d4a7050c27fa3762bf1df5f3c9`.
**That file and the mathematics summarized from it in README Section 4
are excluded from my independent approval.** Their committed identity
was checked for provenance only; they require a different reviewer.

## 2. The convexity proof

The common unimodular row phase cancels exactly in the Gram matrix.
For distinct sixth-power-free ideal labels `R,S`, an exterior prime has
a nonzero valuation difference in `{-5,...,-1,1,...,5}`. Its tame Kummer
character is nonprincipal, with conductor exponent one. Fixed
bad-place ray factors cannot cancel that exterior ramification.
Consequently every off-diagonal character is nonprincipal and its
conductor norm is at most a fixed multiple of `N rad(RS) <= K^2`.

The proof correctly distinguishes that primitive conductor from the
larger zero-extension mask. Primes with equal label valuations remain
excluded even when their Kummer exponent cancels. For
`P=rad(6QRS)`, the exact squarefree series is

`L_E^(P)(s,psi)/L_E^(P)(2s,psi^2)`.

On `Re s=1/2+eta`, the reciprocal denominator has an absolutely
convergent Euler product, even if squaring the character loses
conductor or produces a principal character. No zeta zero-free
assumption enters this step. Convexity bounds the numerator by
`(Nf)^(1/4+epsilon)` times a fixed polynomial in height; deleting the
additional numerator Euler factors costs only a subpower of `NP`.
Smooth Mellin inversion therefore gives the displayed off-diagonal
entry bound `U^(-1/2) K^(1/2) (UKNQ)^epsilon`.

For diagonal entries, the pole coefficient of the punctured squarefree
zeta series is exactly

`c_w prod_(p|6QR)(1+(Np)^(-1))^(-1)`.

The same shifted line gives the asserted normalized diagonal error.
There are `O(K)` distinct allowed labels, so the Hermitian row-sum
bound yields `U^(-1/2)K^(3/2)` up to subpowers. The local-product lower
bound for the diagonal and the fixed power gap at
`K<=U^(1/3-delta)` give eventual invertibility for polynomially bounded
`NQ`. Internal epsilon losses can be chosen before invoking min-max.
The conclusion correctly excludes arbitrary row deletion, duplicated
labels, and universal invertibility on bounded annuli.

The fixed-ray-class extension uses genuine finite group orthogonality.
Bad-place twists preserve exterior nonprincipality. The diagonal
principal term is multiplied by the fixed positive class density,
which is the claimed modification.

## 3. The stronger hyperbolic proof

I checked the exact expansion before any absolute estimate:

`z=d^2 e n`, `(d,Q)=1`, `e|radQ`, and
`C_(d,e)(R)=chi_d(R)^2 chi_e(R)`.

Every multiplier is a diagonal contraction. The identity remains valid
when `n` shares primes with `d` or `e`; all natural zeros are retained
and no additional coprimality restriction is inserted. The moving
puncture is entirely in the external divisor expansion.

For the unrestricted matrix `H(Y)`, each off-diagonal coefficient is
a periodic zero-extended character with complete mean zero and period
norm `O(K^2)`. The same nonzero exterior valuation difference proves
this assertion, including within the fixed primary convention. The
period retains common label primes where local exponents cancel.
Uniform lattice Poisson summation gives
`Y(CK^2/Y)^J` for every fixed `J` when `Y>=CK^2`. Normalized finite
Fourier coefficients are bounded by one; ideal lattices in this field
are rotations and dilations of a fixed lattice. This justifies the
uniformity in the varying period.

On the signed head `Nd^2 Ne<=L`, the normalized errors sum with
weights `Nd^(-2) Ne^(-1)`. The first is summable and the second has
subpower divisor sum. Taking the row-sum operator bound gives the
displayed `Q^epsilon K(CK^2L/U)^J` error. Completing the diagonal Euler
factors yields precisely the same `D` as in the convexity proof,
including primes common to `Q` and `R`. Its omitted part is at most
`L^(-1/2) sum_(e|radQ) Ne^(-1/2)`.

For the tail, the unique decomposition `n=n0 t^6` leaves only the
natural label mask `(R,t)=1`. The supplied sixth-power-free sieve thus
gives

`||H(Y)|| << (YK)^epsilon [Y + K Y^(1/6)
                         + Y^(5/6)K^(1/3) + Y^(1/3)K^(5/6)]`.

The three convergent sixth-power sums have powers `-6,-5,-2`; the
constant-in-row-length sieve term is repeated `O(Y^(1/6))` times.
This bound applies to arbitrary label vectors on the exact permitted
support.

I independently recomputed all four tail terms at fixed `e`. After
division by `U`, they are

`Ne^(-1/2) [L^(-1/2) + K U^(-1/2)
           + U^(-1/6)K^(1/3)L^(-1/3) + U^(-1/2)K^(5/6)]`.

The first and third use the lower cutoff `Nd>sqrt(L/Ne)`; the second
and fourth use the actual nonempty upper cutoff
`Nd << sqrt(U/Ne)`. The estimates remain valid when `Ne>L` and when
an actual row scale is bounded. Summing `Ne^(-1/2)` over divisors costs
only `(NQ)^epsilon`.

With `L=(U/K^2)U^(-eta)`, `0<eta<2delta`, the four quantities become
`r U^(eta/2), r, r U^(eta/3), r K^(-1/6)`, where `r=K/sqrt(U)`.
Choose eta within the final epsilon allowance and then choose the
Poisson decay order. This proves the full claimed rate
`(UKNQ)^epsilon K/sqrt(U)` for `K<=U^(1/2-delta)` and `NQ<=U^A`.
The positive diagonal lower bound gives the stated eventual inverse
bound. No finite calculation or sampled exponent range is used.

## 4. Imported sources and the operator consumer

I reopened the three primary sources listed in the manifest:

- [de Faveri, arXiv:2610.04045v1](https://arxiv.org/html/2610.04045v1):
  Theorem 1.1 bounds the norm with both index sets sixth-power-free.
  At `n=6`, its four terms are exactly the ones used here.
- [Xu--Sang, arXiv:2610.17675v2](https://arxiv.org/html/2610.17675v2):
  Section 2.2, equation (2.3) and Remark 2.1 supply the stated literal
  Eisenstein-family compatibility, including the original zeros.
- [rStation paper 10, v2](https://rstation.ai/problems/riemann_hypothesis/papers/10):
  Sections 7--8 use exactly the specified Gauss vectors, the explicit
  Gram hypothesis, and the projected-operator expansion.

The local copy of the version-pinned paper 10 download has 51,670 bytes
and SHA256
`525c899dd4dd5cb0ed15db43f63fb6e25cc140f98358e9d41ddfe897f5a23a7a`,
matching the manifest. I also checked that the declared base commit
and prior mathematical commit resolve to the stated repository
history. This verifies source identity and the interfaces used; it
does not reprove the full external papers.

The source's column error bound sums to
`||E||_HS^2 << (XK)^epsilon X K^(3/2)`. Its separate sieve gives
`||A||^2 << X^(7/6+epsilon)`. The proved Gram estimate controls both
`G` and its inverse for the source's actual vectors. Expanding
`A^*PA`, with `P=VG^(-1)V^*`, therefore gives exactly

`(XK)^epsilon [X^(13/12)K^(3/4) + X K^(3/2)]`.

At `K=X^(1/9-kappa)`, the two power savings relative to `X^(7/6)`
are `3kappa/4` and `3kappa/2`. The continued primitive Kubota mean
remains an imported theorem. The wider Gram range alone does not
improve that separate error estimate.

## 5. Publication scope and smallest remaining gap

The final README includes the nonzero smooth weight hypothesis needed
for a positive diagonal and accurately summarizes both Gram results.
Its numerical discussion preserves the preceding source-dependent
reference `0.874886647039964...` and the still-conditional `0.8745`
target. I checked this as a scope and provenance statement; this
review does not re-audit the preceding boundary calculation.

The remaining load-bearing estimate is for the full complementary
operator `A^*(I-P)A` on the required source coefficient, or another
argument that genuinely proves the high-conductor inverse moment.
Neither Gram conditioning nor the projected estimate bounds that
complement. The packet states this limit explicitly. Subject to the
separate independent review of the smoothing note, these reviewed
files are suitable for publication as proposed analytic research with
the stated imported dependencies and unchanged numerical boundary.

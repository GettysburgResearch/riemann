# Internal review of the capped native inverse moment

Reviewed object: `CAPPED_NATIVE_MOMENT.md`, 15,530 bytes,
SHA256 `9201cbf1327472f0f2d51f468ed276d3101e321c5018fefecbad79f34b35d011`.
This includes Corollary 1b for every prescribed bounded-power length
range. Remote-commit authentication is a separate publication step.

Reviewer: `native_gain`, a different agent from the author. I identified
the available all-family cap during review of the initially uncapped
fractional calculation and checked its exponent consequence. I did not
author the completed direct reciprocal proof. This is an internal
review with that contribution disclosed, not external peer review or
formal verification.

## Exact premise checks

I fetched the pinned OpenAI source, Git blob
`268c4e3206d460c617d3d2129742a72b831b3def`, at commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a` and read `thm:main` directly.
It explicitly claims the 7/8 cap for all finite-order Hecke functions
over the Eisenstein field. The argument is therefore not substituting
an ordinary-zeta theorem for the needed family premise. This review
does not certify the proof of that imported cap.

I also freshly opened the primary [Xu--Sang v2 source](https://arxiv.org/html/2610.17675v2)
and read Section 6.1, Lemma 6.2, Proposition 6.3 and its order-of-choices
paragraph. These supply the fixed finite presentation labels, both
orientations, polynomial-height buffered rectangles, and physical-row
count used in the note. The proof does not merely extrapolate the
polylogarithmic-height formulation of Theorem 1.2.

## 1. Scope of the actual inverse

For every retained nonunit sixth-power-free row outside S, a good prime
of that row has exponent between one and five. Its nontrivial local
character cannot be cancelled by the fixed S-supported ray twist.
The inducing character is nonprincipal in both orientations. Norm
height t is handled by translating the L-function argument; it is not
an unlicensed infinite-order character in the imported cap.

Adding a common zero mask does not change that primitive character.
With Nrad(Q_0)<=U^(C_0), the complete deletion radical has bounded-power
norm. All deletion factors are nonzero in the disks used in the proof.
The reciprocal on the original absolute line is the Euler series with
precisely mu_E(n)psi_u(n), including every collision and puncture zero.
No Gauss column, favorable row subset, or changed coefficient is used.

The original inverse estimate is invoked only at its licensed
common-profile and presentation scope when taking the minimum of the
old and new exponents. The newly proved buffered-contour bound itself
retains every common puncture of the stated bounded-power radical.

## 2. The local logarithm argument

I independently checked the geometry and each analytic step.

- At center 3+iv the unit disk lies in Re(s)>=2. The absolutely
  convergent Euler logarithm is uniformly bounded there, including
  every natural deletion. This fixes the branch of the logarithm.
- The outer disk has left edge a+2e, within the buffered zero-free
  rectangle. It has radius less than three. For sufficiently large U,
  the added imaginary radius fits within the source buffer uniformly
  for |v|<=U^tau/2. Its primitive function has no pole.
- Polynomial conductor/height growth gives an upper bound C log U
  for Re(log L_orig). No lower bound for L is assumed in deriving it.
  The finite deletion product has the required upper bound because
  its radical has bounded-power norm.
- Borel--Caratheodory at the strictly smaller radius R_1 bounds the
  full holomorphic logarithm by O_e(log U). Hadamard three-circles
  between radii 1,R_2,R_1 then gives O_e((log U)^theta_e), with
  theta_e<1 uniformly in the permitted a range. A compact parameter
  interval and fixed e provide the required uniform strict inequality.
- Exponentiating its negative real part gives U^eta for every fixed
  eta>0 after a sufficiently large, possibly ineffective-looking
  threshold. This is a subpower conductor estimate, not the weaker
  U^(C_e) bound that a single Borel--Caratheodory application would give.

The reasoning is not circular: the local zero-free rectangle is the
independently supplied bin premise, and the logarithm is constructed
only in that rectangle. No bound on the native inverse moment is used
to conclude its reciprocal estimate beyond the imported premises
already used to construct and count bins.

## 3. Finite-height Mellin shift and all-height statement

The Mellin formula (16) has the correct s-it translation and central
normalization D^(-1/2). For |t|<=H_1/4 and |Im s|<=H_1/4 the argument
s-it remains in |Im|<=H_1/2. The vertical contour at a+8e is strictly
inside the buffered zero-free region. The horizontal pieces and
unshifted tails have the displayed D^(3/2) factor and arbitrary fixed
Mellin decay.

For D<=U^C, choosing the external derivative order after tau and C
controls all tails. It does not alter the source's internal detector
height order: those witnesses and derivative orders were fixed before
tau. The final height order can then be enlarged to absorb the trivial
bound I<<UD when |t|>U^tau/4. The final consumer must choose its small
height allowance after that order, as the note explicitly requires.

All profiles remain common; increasing their fixed external seminorm
order does not introduce arbitrary rowwise coefficient vectors.
Pointwise uniformity in the small height range also licenses a
permitted rowwise choice of height within that range.

## 4. Row counts, floor and exponent calculation

Because the imported family cap bounds every rightmost-zero maximum,
the assigned a is at most 7/8; rounding to the lower grid endpoint
cannot move it to the right. Zeros on the boundary line remain covered
by the buffer. The above-floor exponent is exactly

    R(a)+(2a-1)r.

Its derivative vanishes at
a_*=(21-sqrt(150/r))/12. I recomputed the transition r=200/147,
the cap value R(7/8)=2/7, and the line 2/7+3r/4. On 1<=r<=3/2 the
floor contribution is at most 1.03 before the small losses, below the
above-floor maximum. For larger fixed r it remains smaller than the
linear cap branch, which verifies Corollary 1b's floor comparison.

The two comparisons with the old exponent are correct:

    E_cap(r)-E_old(r)=(5/3)(sqrt(r)-sqrt(3/2))^2

on the interior-maximizer branch, and

    E_old(r)-E_cap(r)=r/12-5/42

on the linear branch. The improvement therefore begins exactly at
r>10/7. At r=3/2 the exponents are 79/56 and 17/12, a difference
1/168. At r=2 they are 25/14 and 11/6, a difference 1/21.

The losses can be chosen in the stated order: fix the final epsilon
and length range, choose buffer and preliminary losses, fix internal
orders, choose tau, and only then choose external Mellin and final
height orders. The number of bins is finite after the buffer is fixed.

## Assessment

I found no gap in the proposed deduction at its stated imported-source
scope. It supplies an estimate for the complete native inverse in the
specified long-length range, rather than only a conditional target or
a special coefficient family.

This conclusion remains dependent on the imported all-family 7/8 cap
and the buffered row-count theorem. Neither is independently proved
by this review. The new mean alone does not imply a smaller zero-free
region: its location in the length range must be inserted into the
complete detector consumer, with the other inherited interfaces and
their scopes retained.

## Exact remote authentication (2026-10-25)

I independently fetched `CAPPED_NATIVE_MOMENT.md` and `MANIFEST.json` from
`GettysburgResearch/riemann` at the exact final mathematical commit
`5c7f4aa542ea2112b7f95fce984a35dfe454cfd6`, under
`standalone/2026-10-25-hlc-zero-free-transfer/second-pass/`.
For the fetched note, I recomputed both SHA256 and Git blob SHA-1
(including the `blob <byte-length>\0` header), compared the reported
GitHub blob, checked the manifest entry, and compared the local bytes.
All four checks agree:

- Byte length: `15530`.
- SHA256: `9201cbf1327472f0f2d51f468ed276d3101e321c5018fefecbad79f34b35d011`.
- Git blob: `639cbe39e3c15a5f5d3c5493420d3575ff211f43`.

The manifest itself is 2963 bytes, SHA256
`68f69ad289a722a358b113cdec20db41cf54755bffb2c1bce73cecdf045e3536`,
Git blob `ca948bb86211998ad92e2c147bfb6e9b4b945f8f`; its fetched bytes also match the
local manifest, and its Git blob was independently recomputed.

These are exactly the mathematical bytes reviewed above, also fetched
unchanged at the preceding mathematical commit
`3b47783a7c775bc8133f6601cb9bb97b1b38678a`.

This appendix authenticates this note and its manifest entry. It does
not extend the analytic assessment, authorship independence, imported
source certification, or claim scope stated above.

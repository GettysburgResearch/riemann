# Independent review: the detector consumer and capped inverse exponents

Date: 2026-10-25.

Reviewer: the `two_sign_hlc` agent, not an author of the two files reviewed
below. I authored the separate unmarking and HLC uniformity notes in this
packet; those notes play no part in this review. This is an internal agent
review, not external peer review or formal verification.

## Frozen local objects

| File | SHA256 |
|---|---|
| `DETECTOR_CONSUMER.md` | `8715b0914e7f68f0067f0a07a5b47219f87c12ceb5e694229a85c224af07c62c` |
| `CAPPED_NATIVE_MOMENT.md` | `9201cbf1327472f0f2d51f468ed276d3101e321c5018fefecbad79f34b35d011` |

I read both complete files at these hashes, including the bounded-power
length extension in Corollary 1b of the capped moment note. A different
byte sequence is a different review object.

I also fetched the exact predecessor consumer directly from GitHub:
`GettysburgResearch/riemann@845225c2e7713b69766b95c5e6964d44bb62f6bb`,
`standalone/2026-10-22-inverse-length-consumer/PROOF.md`, Git blob
`50f611b563446d32838721d05d4c693e7b9b310b`. Its Section 2 supplies the
short-witness line, the inverse length interval `1<=r<=t`, and the
unchanged plain-witness case; Sections 2-3 explicitly retain the floor
row count. This source was read, not inferred from a PR description.

## Verdict

**PASS for the exact scalar consumer calculation.** Over the entire stated
parameter rectangle, inserting the improved long inverse bound leaves the
old optimized count unchanged. The proof is analytic over the full
interval; it is not a sampled optimization. Therefore this consumer does
not certify a new zero-free boundary.

**PASS for the mathematical deduction and exponent calculations in the
capped moment note, conditional on its explicitly stated source premises.**
In particular, I did not reconstruct or independently certify the
OpenAI all-family finite-order Hecke cap or Xu--Sang's buffered polynomial-
height bin theorem. Those are essential hypotheses, not consequences of
this review. The dedicated source review of that note is separate.

## 1. Entire-interval detector calculation

For `0<delta<=3/4` and `0<=x<=1/2`, both
`P_x=(2-8x/9)(1-x)` and `D_x=3-17x/9` are positive. Direct expansion gives

\[
 2D_x-3P_x=(4/9)x(11-6x)\ge0,
\]

so `0<C=delta P_x/D_x<=2delta/3`. Put `A=5/6-delta`; then `A>=1/12`.
Solving the decreasing short line against the increasing old inverse line
gives precisely

\[
 t_*=1+\frac{C}{2(A+C)}.
\]

For fixed positive A this is increasing in C. Its maximum under the
preceding bound is

\[
 t_*\le1+\frac{2\delta/3}{2(5/6-\delta/3)}
       =\frac5{5-2\delta}\le\frac{10}{7}.
\]

The inequalities are equalities simultaneously only at `delta=3/4,x=0`.
The denominator is positive throughout, and `1<t_*<=10/7<3/2`.

The new moment agrees exactly with the old one up to `10/7`. After
subtracting `delta r`, its two slopes are `5/6-delta>=1/12` and
`3/4-delta>=0`. Thus it is nondecreasing throughout `1<=r<=3/2`.
Consequently the full long-witness envelope over `1<=r<=t` is attained
at `r=t`, including at `delta=3/4`, where the second piece is constant.

At `t=t_*` the new and old inverse counts are identical. At any smaller
t the short line is at least its crossing value; at any larger t the
new long line is at least that same crossing value. This proves equation
(8) in `DETECTOR_CONSUMER.md` in both directions. The comparison is
pointwise in delta and x, so any subsequent optimization using the same
source count, unchanged plain witness, and separate floor count receives
the old value. It cannot gain a strict margin merely from this insertion.

The general-ceiling observation is also exact. For `0<delta_b<5/6`,

\[
 \frac{(15-16\delta_b)/(15-6\delta_b)-1/6}
             {5/6-\delta_b}
   =\frac5{5-2\delta_b}.
\]

Both denominators are positive. Since `5/(5-2delta)` increases with
delta, every `delta<=delta_b` in the admitted range has its old crossing
at or before this endpoint-line intersection. This is a statement about
that particular density input and detector, not an impossibility theorem
for another method.

## 2. Capped inverse calculation

Taking the bin count and zero-free rectangle as hypotheses, the local
reciprocal lemma is valid. The natural Euler deletion factors have no
zeros in `Re s>0`; the retained inducing characters are stipulated to be
nonprincipal. Hence the indicated disk admits a holomorphic logarithm
normalized by the absolutely convergent Euler logarithm at its center.

The real-part growth bound for that logarithm and Borel--Caratheodory give
`O_e(log U)` on the intermediate disk. Three-circles applied to the
holomorphic logarithm, not to an arbitrary choice of argument, gives
`O_e((log U)^theta_e)` with fixed `theta_e<1`. This is `o(log U)`, so
exponentiation yields the claimed arbitrary fixed `U^eta` reciprocal
bound. The radii, real strips, and imaginary buffers fit for sufficiently
large U; bounded ranges can be absorbed into the constant. The compact
bin interval makes the three-circles exponent uniform.

The Mellin integrand is exactly the inverse natural Euler product, whose
coefficients are `mu_E(n)psi_u(n)`. The vertical and horizontal contour
bounds preserve these coefficients and every original natural zero.
The external Mellin derivative order is chosen after the fixed source
height allowance, so it makes the horizontal pieces and original tails
negligible without changing the source's internal order of choices.
The large-height extension follows from the stated elementary `UD`
bound with a sufficiently large fixed height power. These are valid
deductions from the stated presentation and bin hypotheses.

For the bin maximization,

\[
 R'(a)=-300/(21-12a)^2,\qquad
 R''(a)=-7200/(21-12a)^3<0.
\]

Thus the unique interior maximizer is
`a_*(r)=(21-sqrt(150/r))/12`, lying above the floor for every `r>=1`.
It reaches `7/8` exactly at `r=200/147`. Substitution gives the first
branch of `E_cap`; the top endpoint gives `2/7+3r/4` afterwards.
The floor exponent `1+r/50` is strictly smaller throughout the stated
range. For the bounded-power extension its difference from the capped
line is `-5/7+(73/100)r>0` for all `r>=3/2`, as claimed.

The comparison with the original inverse is also exact:

\[
 E_{\rm cap}(r)-E_0(r)
  =(5/3)(\sqrt r-\sqrt{3/2})^2
\]

on the curved branch, and

\[
 E_0(r)-E_{\rm cap}(r)=r/12-5/42
\]

on the linear branch. Hence the actual gain starts strictly after `10/7`.
At the relevant lengths I independently checked the exact fractions

\[
 \frac{17}{12}-\frac{79}{56}=\frac1{168},\qquad
 \frac{79}{56}-\frac{41}{30}=\frac{37}{840},\qquad
 \frac{11}{6}-\frac{25}{14}=\frac1{21}.
\]

These checks include the distinction between a positive improvement of the
actual inverse moment and the still-unmet PR1014 sufficient hypothesis.

## 3. What was run and what remains assumed

I executed a separate standard-library exact-rational check of seven
endpoint, threshold, and gap identities; all passed. The interval proof
above is the justification for the full continuum of detector parameters.
No floating-point sample grid, zero census, or numerical asymptotic fit is
used as evidence for a global conclusion.

The load-bearing source premises remain the all-family `7/8` cap, the
polynomial-height buffered row-count theorem, the original native moment,
and the pinned detector interpretation. This review does not extend their
scope to nonzero angular characters, arbitrary per-row coefficient choices,
or an unproved principal-member extraction. It approves no RH proof, no
new zero-free region, and no integration into main.

## 4. Authentication of the frozen remote mathematics

After the mathematical commit was published, I fetched both reviewed
files directly from `GettysburgResearch/riemann` at the exact commit
`3b47783a7c775bc8133f6601cb9bb97b1b38678a`, using their full repository
paths beneath `standalone/2026-10-25-hlc-zero-free-transfer/second-pass/`.
I also fetched that Git commit object and verified its tree is
`419fdc5d50f35e9813d5452ca8f852907fca58e0`, with parent
`00d36f61ae7898846579840e6a68f9a06bd8295c`.

I encoded each returned file's actual content as UTF-8, recomputed its
SHA256 and Git blob SHA1 (including the Git `blob <byte-count>\0` header),
and compared the full bytes against the reviewed local object. All
comparisons passed:

| Remote file | UTF-8 bytes | Verified Git blob |
|---|---:|---|
| `DETECTOR_CONSUMER.md` | 5372 | `edd87c95603a09a6e844d9ec823689d3c0014b10` |
| `CAPPED_NATIVE_MOMENT.md` | 15530 | `639cbe39e3c15a5f5d3c5493420d3575ff211f43` |

Their recomputed SHA256 values are exactly the reviewed values in the
first table. This authenticates the reviewed mathematics at that remote
commit; it does not certify subsequent changes or strengthen the stated
source-dependent mathematical scope. This authentication append is the
only file modification made during this publication check.

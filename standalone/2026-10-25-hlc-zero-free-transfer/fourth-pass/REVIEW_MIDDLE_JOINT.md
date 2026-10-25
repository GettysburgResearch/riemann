# Independent internal review of the joint returned-component estimates

Reviewer: `/root/hlc_joint_paths`. Author reviewed: `/root/middle_joint`.
Date: 25 October 2026. This reviewer did not author the mathematical note
or its checker. Review comments requested an explicit positive-slot
coefficient restriction in the fourth-moment theorem; the author added it
before this freeze.

## Frozen objects and outcome

- `MIDDLE_JOINT.md`, SHA256
  `9b88dcfc5ab18d3c469a1ec30a283c44dfa8cb226b4bab2f890d24e5500c5813`.
- `check_middle_joint.py`, SHA256
  `d6af41d2f3a34a1369624156360aaf8e909740ffc7cc97805f3758bcc1ec4044`.

**Outcome: accepted as source-dependent component and localization
theorems, with the remaining complete intermediate estimate open.**
No new zero-free region or full native inverse saving is certified.

The review checked the exact return, local allocation, primitive/natural
character distinction, common punctures, compatible prime factors,
buffered windows, norm summation order, and scalar margins. It also read
the relevant load-bearing statements in the pinned OpenAI source:
`lem:logarithmic-control`, `lem:deleted-euler-factors`,
`lem:buffered-bins`, `lem:marked`, and `lem:plain`. Their complete
external proofs are not independently re-established by this review.

The source pin is `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
`preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`,
Git blob `268c4e3206d460c617d3d2129742a72b831b3def`. The previous gcd
coefficient and return lemmas remain explicit dependencies at
`820b99562e3b458021a6de74802293baafbe5190`.

## 1. The fixed-k return is the actual original ordinary factor

Starting with the exact third-pass reduced expression, the coprimality
identity sets the numerator and dual denominator equal to k times their
quotients. The ratio in the primitive dual kernel loses k. The two
central normalizing factors leave exactly `mu(k)/Nk`, and the canceled
character phase is exactly `1_(k,P_u)=1`. It is not a square-root k
weight.

The primitive Euler-restoration sum over e is untouched before applying
the inverse ordinary functional equation. It therefore restores the
original natural ordinary polynomial. In particular its primitive value
at a deleted prime is never replaced by the natural zero there. No
additional k puncture is inserted in that ordinary polynomial. This
checks equations (5)--(6) of the note against the frozen third-pass
return identity, rather than only against a scalar normalization model.

The finite full-selector inversion is also exact: after writing v=kd,
the divisor sum of mu(k) vanishes unless v=1, leaving A(m). Thus the
new ratio and divisor cutoffs decompose the same original inverse;
they do not assert a support lower bound for a different transform.

## 2. The joint buffered estimate has an available ordinary input

The key new step is to estimate the returned ordinary factor and the
modified inverse coefficient on the same actual bin. The pinned
`lem:buffered-bins` explicitly bounds **both** L_orig and its reciprocal
by an arbitrarily small U-power on the common buffered half-rectangle.
The earlier `lem:logarithmic-control` also states both bounds. Thus the
ordinary pointwise input in equation (7) is not an additional unproved
Lindelof assertion.

For a dyadic reduced-numerator scale B and fixed k, the modified
coefficient lemma gives `(B/D)^theta R^(delta/2)` with R=B/Nk.
The returned ordinary length is D/R, so the product is
`(B/D)^theta D^(delta/2)`. This is the same bin's delta in both factors.
The harmonic k sum costs a logarithm, and the coherent smooth head can
be summed geometrically in B. Taking theta arbitrarily close to 1/8
after fixing the final losses gives the stated pointwise saving.

The frequency proviso is necessary and present: all scalar Mellin,
profile and ordinary frequencies share one source buffer. Polynomial
estimates outside that buffer are paid on the absolute line, before
any unsupported shift. The conductor cancels only through the exact
ordinary inverse functional equation. The natural deletion radical
remains a prescribed power, as required for the deleted-factor lemma.

The row-count envelope and the printed floor then give (8). I checked
the exact comparison for B=U^(101/100). The minimum gap occurs at
r=29/25, and the squared radical comparison
`42839/36000000>0` proves a strict margin beyond 1/1000. This is a
bound for that coherent component only.

## 3. The far-component expansion preserves literal Möbius factors

For a squarefree short original factor a, setting
`g=gcd(a,kd)`, `a=g t`, `A=t n`, `m=kd/g` is reversible. It leaves
`(t,kd)=1`. If m is not squarefree the term is zero. Otherwise the
coefficient is exactly

`mu(g) mu(m) mu(t) mu(n) 1_(n,m)=1`.

Together with the original `mu(k)`, this keeps every scalar sign. The
two remaining Möbius polynomials have the common fixed-label punctures
kd and m respectively. The ordinary factor retains the original
character. There is no missing character of g or m: these variables
belong to the coefficient whose common-divisor phase already canceled
in the exact preceding return. There is no additional Ng normalization.

After k,d,g are fixed, each added radical is a prescribed power of U,
independent of the varying row. The mask `(kd,P_u)=1` is a bounded
row restriction; removing it for a nonnegative moment costs nothing.
Only the long **literal** inverse is submitted to the imported native
moment. The short inverse and ordinary factor use pointwise bounds.
Thus no arbitrary-coefficient extension of the inverse theorem occurs.

The nonempty-scale constraints give the claimed interval for the long
inverse length. All k,d weights are retained before Minkowski, and
their harmonic sum with divisor losses is subpower. The two affine
branches give exactly the saving 1/750.

## 4. Marked inverse estimate: the marks are unchanged

The pinned `lem:marked` permits arbitrary bounded row-independent
prime coefficients, with disjoint underlying prime sets and a common
fixed character orientation. Its two strict length inequalities are
the ones used in Section 6. For b below one, the choice
`z=(1-b)/2` with a fixed small decrement satisfies them on the stated
range; near the zero-capacity endpoint the unmarked estimate pays the
reserved loss.

The new inverse puncture is removed by Euler inversion **only in the
inverse polynomial**. Multiplying that identity by the original Q_z
keeps the prime amplitude lower bound unchanged. Every resulting
shorter inverse has at least the original capacity. The scalar phases
from restoration have modulus at most one, and the Euler mass costs
only a subpower. A baseline common puncture in Q_z can be encoded in
its row-independent prime coefficients, which this marked theorem
explicitly permits.

The other two factors keep their same-bin pointwise bounds. The
complete coherent norm is summed with the harmonic arithmetic-label
weights; the argument does not count each label separately and add
those counts. Finite discretization supplies a common Q_z within
each length group before this norm step. The two count branches meet
at b=1, and monotonicity gives the displayed endpoint maximum.

I checked the critical box corners. The strict gaps are
`372257/153600000` and `1099/192000`, both beyond 1/1000.
Counts use weight one, or a weight bounded below on the counted class,
as the note now states explicitly.

## 5. Marked ordinary fourth moment: the stronger coefficient scope is retained

The ordinary positive-slot theorem `lem:plain` has a narrower
coefficient hypothesis than `lem:marked`: each coefficient, before the
common puncture, must be a fixed finite linear combination of the
licensed finite-ray characters. The note now states this restriction
explicitly and warns that Section 6's broader coefficient alternative
alone is insufficient. The two ordinary factors and their prime slots
keep the same original common puncture. Neither extra inverse
puncture is moved into these prime factors.

The source's positive-slot exclusion is also stronger than merely
nonprincipal induction: it excludes all primitive inducing characters
in the fixed finite ray group Theta. The final note explicitly retains
this requirement. In its stated physical family, a sufficiently large
sixth-power-free row has a prime outside the fixed bad set with
valuation between one and five. Its nontrivial local residue character
cannot be canceled by an S-supported fixed ray twist and cannot belong
to Theta. The remaining S-supported rows have bounded norm. Added
natural punctures do not change primitive induction. This checks the
automatic exclusion in the final note's actual scope, without extending
it to moving twists at new primes.

For the common ordinary length c, the product of the two inverse
fourth powers costs `U^(2 delta (r-c)+epsilon)`. The selected prime
length `z=2(1-2c)/9`, with the stated decrement, satisfies
`2c+(9/2)z<1` at kappa=3/4. This kappa uses precisely the imported
7/8 cap; it is not a field-scope extension of a different optimized
moment theorem.

The weighted L4 step is correct: multiplication by `|Q_z|^(1/2)`
makes its fourth power `|Q_z|^2`, so the remaining moment is exactly
`sum |S_c^2 Q_z|^2`. Minkowski takes place in this weighted L4 space
while the mark is common. After its amplitude is removed, ordinary L4
Minkowski joins the finitely discretized c-components. This order does
not assume that a single prime product works at every c or that a
large sum forces all summands to be large.

The exponent is therefore `1-2 delta c-(4g/9)(1-2c)` below c=1/2,
with the empty-slot continuation above that point. It is decreasing
in c on the stated parameter range. For the smooth returned cutoff
U^(73/100), the exact minimum count gap is `7427/1440000`.
This eliminates that complete low component on the compatible box;
it leaves the intermediate returned component open.

## 6. The separate thin-band identity and its exact return

The final section changes alpha to 1/250 in a separately labeled
identity. It does not reuse the old unmarked 1/750 saving with this
smaller alpha. The asymmetric convolution still has product of
cutoffs 2D, both linear pieces vanish eventually, and all original
repeated-prime terms remain. Applying the two marked arguments
directly with k=d=g=1 is legitimate: it leaves precisely the original
two Möbius factors and the original ordinary factor.

The new low and high exponents 147/200 and 773/1000 give the three
exact uniform count margins `371959/307200000`, `1099/768000`, and
`23/16000`. All exceed 1/1000. The required prime supplies are
`231/2000` for the marked inverse and `1/30` for the ordinary fourth
moment; both fit the retained source supply and mesh conventions.

The band is a literal original-product cutoff. Its low, band, and high
selectors add to one in the same new identity. The additional ratio-head
lemma remains pointwise after multiplying the returned-variable annular
profile by a common smooth cutoff. Its logarithmic derivatives are
uniformly bounded. Thus exact full-k inversion makes the high-ratio
version equal to the literal band minus an error of size
`U^(-1/800+epsilon) D^(delta/2)`. This is a proved stable cutoff
operation, not a support inference between unrelated decompositions.

The additional divisor constraints follow directly from the whole
support `Nk NA Nd<8D` and the high ratio. In particular
`Nd<8U^(1/100)` and the two displayed k bounds are correct. The
warning about the k sign is also exact: at d=1 the allocated signs
can cancel to one. A new long inverse in k is not created.

Finally, the positive resource gap in equations (57)--(59) is a
calculation about the named existing count lines. The rational contact
lies in the displayed actual critical box; the inverse and ordinary
lines meet there with their lengths adding to r. The positive gap for
any eta and admissible positive alpha is therefore not a numerical
artifact. No existence of arithmetic rows saturating those bounds is
claimed. This is the correct limited conclusion of the calculation.

## 7. Reproduction and remaining boundary

The reviewer independently ran the frozen checker under `python -O`.
It passed. Its reported coverage includes:

- 3,456 exact fixed-k,d,g allocations and 15,400 natural/primitive
  mask identities;
- 630 finite signed returns and three-part partitions, 360
  normalization cases, and 10,143 selector-support cases;
- 7,701 envelope identities, 5,304 far-exponent cases, and the exact
  radical certificate;
- 1,000 puncture restorations, 2,121 marked-capacity cases, and
  4,851 marked critical-box cases;
- 303 weighted-fourth cases and 4,851 low-returned critical-box cases;
- 480 band/ratio-return identities, eight new-identity corner
  certificates, and six exact rational resource-contact certificates;
- the checker’s stated sign, puncture, mask, normalization and
  excessive-saving negative controls.

The checker does not prove the imported analytic theorems. This review
does not certify their complete external framework, either. Relative
to those stated premises and the frozen third-pass coefficient lemma,
I found no missing analytic step in the deductions reviewed here.
The first remaining new arithmetic step is the bound for the coherent
intermediate returned component, or its precisely licensed detector
spike count. That statement remains unproved.

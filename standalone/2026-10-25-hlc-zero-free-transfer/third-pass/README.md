# Third pass: proved head and far tail, and an exact middle-band target

This pass continues the same research branch after publication
`08769810374603b926d995fdc6ff0254e4267ea5`. It adds complete proofs of
several intermediate estimates and tests them against the actual
zero-free consumer. Earlier pass files are retained byte-for-byte.

**Outcome: no RH proof or smaller unconditional zero-free region is
established by this pass.** The source-qualified comparison benchmark
remains `B_flat=0.874886647039964...`. The arithmetic theorems from the
external preprints remain explicit premises; this packet does not
independently certify their complete framework.

The strongest result now controls both the smooth head through product
scale `U^(13/20)` and the complete coherent far tail beyond product scale
`U`, in one exact asymmetric convolution identity. The missing arithmetic
is confined to its middle band `U^(13/20)<Nr<2U`. An exact certificate
shows that a specified saving on this middle expression would give the
conditional boundary `0.8748856`. The middle estimate remains open.

A separate result uses coherent common-divisor cancellation across all
original product scales to control a component of the reduced ratio.
That alternative decomposition is not mixed with the first one without
an overlap estimate. The final operator audit also identifies the exact
conditioned channel that prevents a direct transfer of complete affine
mixing to the new HLC paper's dirty edges.

## Results and their exact consequences

| Result | What is proved here | Current consequence |
|---|---|---|
| Smoothed inverse-product component | The component at product scale `U^(13/20)` has exponent `83/24-sqrt(195)/6=1.1309599927...` | It has a fixed margin throughout the critical inverse-length interval |
| Complete asymmetric far tail | All outer products above scale `U`, with their coherent smooth weight, have exponent `(1+5r)/6-1/750` | Together with the head in this same identity, it leaves only the exact middle band |
| Coherent common-divisor component | The smooth reduced numerator through `U^(7/9)` has exponent `179/126-r/4`, using all original product scales before taking a norm | It saves at least `17/6300` throughout the critical interval; its own complete complement remains |
| Conditional zero-free consumer | A specified `1/1000` saving for the complete inverse implies `Re(s)>0.8748856`; the new head/far estimates reduce its new input to the middle band | An exact conditional implication; the middle estimate remains open |
| Coherent native decomposition | A complete short-product component has mean at most `U^2 R_0/D` for `R_0<=sqrt(U)`, with primitive conductors, all physical rows and punctures retained | At the critical length, `R_0=U^(1/4)` has a fixed power margin; the complementary component remains |
| Amplitude-conditioned inverse | At `D=U^(7/5)` and compatible prime amplitude at least `37/100`, the exponent is `4/3-4861/4651680` | A real restricted mean improvement; it does not cover the critical amplitude |
| Two-sign long average | The entire smooth Vaughan Type II part obeys `T_3/H << X^beta U^(beta-1) log X` under the stated Mertens premise | It reaches exponent `4/5` for a stated cutoff choice; the Type I part returns the target Mertens sum |
| Broad prime selector | Exact coverage leaves only `(log X)^4`-smooth integers, contributing `X^(3/4+epsilon)` | It removes the old coverage loss; the retained full Type I signal still survives |
| Mixed numerator certificate | Free total lengths, either contour side, and class-by-class pointwise/averaged choices still give `B>=B_flat` at the current moment cap | The remaining problem requires a stronger arithmetic estimate within this framework |
| Projected affine operator | Fixed projectors preserve correctly centered complete affine variance, but the conditioned dirty determinant channel is an isometry | It identifies the missing conditional mixing input; it does not disprove cancellation of the full arithmetic sum |

### 1. The stronger smooth native component and its explicit consumer

[INVERSE_POWER_COMPONENT.md](INVERSE_POWER_COMPONENT.md) combines the
buffered zero-count input with the ordinary fourth moment after exact
primitive reflection. It first retains a smooth version of the exact
Heath--Brown convolution identity. Both short Mobius factors and every
repeated-prime contribution remain.

Use a fixed smooth outer selector `chi_0`, equal to one below one and
zero above two. The proved component is weighted by
`chi_0(Nr/U^(13/20))`, where `r` is the product of the two short Mobius
factors. With the actual row measure, original character zeros, common
punctures, and licensed heights, its squared mean satisfies

$$
 I_{\rm low}(U,D)\ll U^{\gamma_0+\epsilon},\qquad
 \gamma_0=\frac{83}{24}-\frac{\sqrt{195}}6
                    =1.130959992705176\ldots.
$$

The fixed profile and height factors are retained in the theorem. The
use of a smooth outer selector is essential to the stated proof; no
unlicensed sharp cutoff is inferred from the buffered estimates.

At the averaged critical inverse length

$$
 D=U^{t_c},\qquad t_c=1.163953576509010\ldots,
$$

the inherited full-moment exponent is
`(1+5t_c)/6=1.136627980424175...`. The new component is smaller by
about `0.005667987719`. More significantly, throughout

$$
 \frac{29}{25}\le r\le\frac{117}{100},\qquad D=U^r,
$$

its exponent is strictly below `(1+5r)/6-1/1000`. The exact comparison
reduces to `sqrt(195)>3489/250`, whose squared difference is
`14379/62500>0`.

[ASYMMETRIC_HB_TAIL.md](ASYMMETRIC_HB_TAIL.md) then supplies a stronger
decomposition. Set `alpha=2/125`, `y_1=U^alpha` and
`y_2=2D/U^alpha`. The unequal-cutoff identity
`mu=m_1+m_2-m_1*m_2*1` is exact through norm `2D`; both linear
terms vanish on the original annulus for sufficiently large `U`.
The same head proof applies to these unequal cutoffs. In this one
identity use the three complementary weights

$$
 \chi_0(Nr/U^{13/20}),\qquad
 \chi_0(Nr/U)-\chi_0(Nr/U^{13/20}),\qquad
 1-\chi_0(Nr/U).
$$

They define `M_head`, `M_middle` and `M_far`, whose sum is exactly the
original inverse. The new far theorem is

$$
 \sum_u w(u)|M_{\rm far}|^2
       \ll U^{(1+5r)/6-1/750+\epsilon}.
$$

Its saving exceeds the consumer's requirement by `1/3000`. The proof
uses capped pointwise estimates for the very short inverse and the
ordinary factor, and the original second moment for the longer inverse.
The unequal cutoff forces that longer length away from the endpoint
that previously defeated this argument. It bounds the whole coherent
far tail, including outer products comparable to `D`.

The specific missing estimate is therefore now

$$
 \sum_u w(u)|M_{\rm middle}(U^r;u)|^2
 \ll U^{(1+5r)/6-1/1000+\epsilon}
 \qquad(29/25\le r\le117/100).
$$

Here the middle weight is exactly the difference above, supported on
`U^(13/20)<Nr<2U`, with both unequal short-factor cutoffs, all original
signs, repeated primes, masks, profiles and heights retained.
**This estimate is open.** The triangle inequality, together with the
proved head and far tail, would give the same saving for the complete
native inverse. No subtraction of upper bounds is used.

[CONDITIONAL_CONSUMER.md](CONDITIONAL_CONSUMER.md) then proves the full
conditional implication

$$
 \text{that middle estimate}\quad\Longrightarrow\quad
 L_E(s,\eta)\ne0\quad(\operatorname{Re}s>0.8748856),
$$

relative to the original Eisenstein analytic framework, and hence the
same conditional region for Dirichlet L-functions and zeta. This is more
than `10^-6` to the left of the imported `B_flat`. The consumer note
retains its earlier symmetric-tail sufficient hypothesis; Section 5 of
the asymmetric note proves that the smaller middle hypothesis supplies
the identical complete-inverse input. No piece of one decomposition is
silently substituted for a piece of the other. The certificate checks every
zero/amplitude class, finite prime supply, the old witness floor below
the improved length interval, all remaining row ranges, and the actual
contour closure. Four fixed detector cutoffs and an exact Bernstein
certificate replace a sampled optimization. Removing the hypothetical
gain makes its negative control fail as required.

The surviving middle block is explicit. At the source's critical scalar
class, the first inverse can be the unit, while the second inverse and
ordinary lengths are approximately `0.7456999427` and `0.4182536338`.
Their sum is the critical native length. The existing marked inverse and
ordinary fourth-moment count bounds meet exactly at this block. An exact
rational bracket places the inverse-product length between `.74` and
`.75`, safely inside the residual band. The note tests higher-order
identities and specified higher-moment envelopes against this class,
without claiming that actual rows saturate those upper bounds.

The preceding component theorem in
[SIGNED_NATIVE.md](SIGNED_NATIVE.md) is retained separately. It is based
only on the ordinary functional equation and the stated sieve input,
and gives

$$
 I_R(U,D;Q)\ll (UDNQ)^\epsilon\frac{UR}{D}
                           \{U+R+(UR)^{2/3}\}.
$$

Here the primitive conductor is kept distinct from the original
natural zeros and the common growing puncture. All sixth-power-free
physical rows, including nonsquarefree rows, are present. The
puncture-divisor norm cancels before its finite divisor sum is bounded.
For `R_0<=sqrt(U)`, that earlier bound gives
`I_{<=R_0}<<U^2R_0/D`. At the critical inverse length its
`R_0=U^(1/4)` example has exponent `1.08604642349...`, but covers a
smaller component than the new smooth fourth-moment argument.

### 2. A second decomposition with a larger controlled ratio component

[GCD_NATIVE_COEFFICIENT.md](GCD_NATIVE_COEFFICIENT.md) groups the
**full** reflected identity before taking any norm. Write the original
outer ideal and the reflected dual ideal as `r=da`, `n=db`, with
`(a,b)=1`. Their character phases in d cancel exactly on the natural
coprime support. The remaining coefficient is

$$
 C_a(P)=\sum_{(d,P)=1}\frac{a_y(ad)}{Nd}.
$$

All original outer products below `8D` stay in this coefficient,
including terms that vanish only after their complete primal or dual
sums are taken. An exact three-way prime allocation expresses it as a
sum of products of two harmonic Mobius sums. The scalar `7/8` cap gives
cancellation in those sums. A common Mellin representation separates the
row-dependent coprimality mask before the family sieve is applied.

For the coherent part of this identity with `Na<=B_0<=sqrt(U)`, the
result is

$$
 J_{\le B_0}\ll U^{2+\epsilon}(B_0/D)^{5/4}.
$$

At `B_0=U^(9/20)` and `D=U^r`, its gap to the old complete-inverse
exponent is exactly

$$
 \frac{1+5r}{6}-\left(\frac{41}{16}-\frac{5r}{4}\right)
       =\frac{100r-115}{48}\ge\frac1{48}
       \qquad(29/25\le r\le117/100).
$$

This first ratio estimate uses only the stated scalar cap and sieve
premises. The final extension in
[GCD_FOURTH_COMPONENT.md](GCD_FOURTH_COMPONENT.md) additionally uses
the finite-order family cap, buffered row counts and ordinary fourth
moment. It proves the general smooth dyadic bound

$$
 J_B\ll (B/D)^{1/4}
      U^{[1+\mathcal E_{.51}(2\log_U B)]/2+\epsilon}.
$$

The extra coprimality is inverted exactly before that fourth moment is
used. The resulting common-divisor weight is `1/Nk`, so its sum costs
only a logarithm. The modified local factors remain explicit; no
reciprocal of a possibly vanishing correction polynomial is introduced.
The buffered argument uses one shared frequency allowance for all
Mellin variables.

For a smooth reduced-ratio selector `chi_0(Na/U^(7/9))`, the result is

$$
 J_{\rm ratio,head}\ll U^{179/126-r/4+\epsilon},\qquad
 \frac{1+5r}{6}-\left(\frac{179}{126}-\frac r4\right)
        \ge\frac{17}{6300}>\frac1{1000}.
$$

Thus a `1/1000` saving on this **complete complementary reduced-ratio
component** would also suffice for the conditional boundary in Section
1. The cutoff is smooth; the buffered argument does not license an
arbitrary sharp terminal dyad.

[RATIO_CUTOFF_RETURN.md](RATIO_CUTOFF_RETURN.md) proves precisely why
the two decompositions do not combine for free. Undoing the ratio
selector and the ordinary reflection returns the high-ratio primal
coefficient

$$
 A_{y_1,y_2}(m)-H_{\chi,P_u}(m),\qquad
 H_{\chi,P_u}(m)\ll U^{-1/25}
$$

on the same critical interval and natural unit support. After also
subtracting the proved original-product far tail, the coefficient is
exactly `chi_0(Nm/U) A_(y1,y2)(m)-H_(chi,P_u)(m)`. The old
squarefree critical coefficients at product exponent `.74569994...`
remain almost unchanged. This is a coefficient identity and error
estimate, not a lower bound for the signed moment. It removes a false
support inference and leaves open the possibility of a new coherent
cancellation estimate.

[TAIL_RETURN.md](TAIL_RETURN.md) follows this coherent gcd identity
through its exact local Euler algebra. At zero ratio-cutoff Mellin
frequency the complete return retains
`L_psi(w)/(L_psi(w+s)L_psi(w+z))`, including the original natural
Euler factors. The straightforward contour comparison loses the apparent
cutoff saving in the displacement required to keep both reciprocal
arguments to the right of the buffered zeros. This is a precise limit
of that estimate, not a lower bound for the signed sum. A local
polynomial zero also rules out an unjustified reciprocal of the
correction factor.

### 3. A shorter restricted native gain, with its feedback calculated

[SHORT_INVERSE.md](SHORT_INVERSE.md) proves

$$
 \sum_{u\in\mathcal B_{\ge37/100}}
       w(u)|M_u(U^{7/5})|^2
 \ll U^{4/3-4861/4651680+\epsilon},
$$

subject to the source's same-character prime amplitude, full supply,
buffered-height and finite-order hypotheses. The saving is approximately
`0.001044998796`; its exact contact is `107567/77528`, before `10/7`.

The same note proves an exact limit on its use: converting those
existing class counts to an inverse moment and feeding that moment back
into the independent detector returns the old class count. The class's
own affine line is already present in the moment envelope. This remains
true with the stronger imported family cap. In particular the estimate
does not silently become a full-row moment or a local zero exclusion.

### 4. The full two-sign calculation and the surviving Type I term

[AVERAGED_HLC.md](AVERAGED_HLC.md) retains both Mobius signs. For the
stated smooth bilinear form, two exact Stieltjes integrations give

$$
 |T_H|\ll B_N M^\beta X^\beta(1+X/H)
$$

under `Mertens(y)=O(y^beta)`. With `H` comparable to `X`, the complete
Vaughan Type II component is bounded by

$$
 T_3/H\ll X^\beta U^{\beta-1}\log X.
$$

At `beta=7/8`, `U=X^(3/5)` and `V=X^(1/5)`, this reaches the
first-pass Type II target `X^(4/5+epsilon)`. Recombining the whole
Vaughan identity, however, gives

$$
 S_H/H=\left(\int K\right)M_W(X)
                  +O(X^{4/5+\epsilon})
$$

for these choices and a sufficiently large fixed smoothing order.
The Type I coefficient tends to one on every detected Mellin mode.
This proves where the target remains in the full calculation; a
centered remainder does not supply a smaller Mertens exponent.

The same note proves an exact broad-prime selector with an
`X^(3/4+epsilon)` smooth-number remainder, keeps its fractional-parameter
principal terms coherently until they cancel, and verifies the whole
selected Type II bound. It also records precisely scoped tests of the
complete affine-group identity, polynomial moduli, inert prime factors
in determinant paths, and the additional oscillatory-prime paper
arXiv:2610.15989v2. None is substituted for the still-missing full target.

### 5. A rigorous test of the wider numerator system

[MIXED_NUMERATOR.md](MIXED_NUMERATOR.md) allows free total length and
asymmetry, both contour sides, and a different choice between the two
supplied numerator estimates for every class. Four explicit classes
and seven positive dual arguments cover every case: one gives
`B_flat` exactly, and six give strict larger bounds.

The smallest strict margin is greater than `1.79087019e-6`. The
certificate uses isolated algebraic roots and exact rational residual
bounds, not acceptance of a sampled optimizer. It covers the stated
fixed-cap scalar system, including unlimited prime supply as an
optimistic relaxation. It does not rule out new mixed moments, a
different signed detector, or a stronger direct Gram estimate.

The same note tests the licensed joint use of a detected plain witness
and the numerator block. Its advantage over the existing fourth-moment
bound is exactly `(R_plain-R)/4`, which is nonnegative at the relevant
count and zero at the adverse crossing. Reusing that marginal moment
alone cannot improve the count.

### 6. What the HLC operator can and cannot supply

[PROJECTED_AFFINE_OPERATOR.md](PROJECTED_AFFINE_OPERATOR.md) proves the
exact centered identity with fixed endpoint projectors retained:

$$
 \mathbb E_{q\ne0,h}|\langle f,P(U_{q,h}-J)Qg\rangle|^2
   =\frac{\operatorname{Var}(Pf)\operatorname{Var}(Qg)}{p-1}.
$$

It also provides a quantitative comparison-error inequality. This is a
usable positive statement about the complete affine average.

The HLC dirty edge fixes a projective line as well as a nonzero
determinant. In the resulting local model every target point has a
disjoint fibre of `p` source points. The probability-normalized pullback
is an isometry, including on mean-zero functions. Arbitrary high-density
endpoint projectors retain a norm close to one. An explicit bounded
reciprocal/additive-phase pair illustrates why strong one-variable
cancellation does not remove that incidence correlation.

This does not lower-bound the full HLC sum or its actual Mobius
coefficients. It shows why complete affine mixing cannot be charged
again after conditioning on an already recorded dirty line. A useful
transfer still needs the coherent average over the actual list/line
labels or a new estimate for the signed coefficients with that
conditioning retained.

## Read, reproduce and review

The mathematical notes and their companion scripts are the deliverables. `CHECKS.json` records the actual local executions;
`MANIFEST.json` binds the mathematical files to SHA256 and Git blob IDs.
The internal review notes identify their authors, exact reviewed bytes,
resolved issues and scope. They are not external peer review or formal
certification of the source preprints.

The final mathematical freeze is
[`820b99562e3b458021a6de74802293baafbe5190`](https://github.com/GettysburgResearch/riemann/commit/820b99562e3b458021a6de74802293baafbe5190).
It contains 12 mathematical notes, 12 companion scripts and two detailed
scalar reports. [PUBLICATION_REVIEW.md](PUBLICATION_REVIEW.md) records
the remote blob checks, internal review bindings, integration checks,
and the exact scope of the completed work.

The first and second pass source pins remain in force. The inputs used
here additionally include the original Eisenstein amplified consumer
Xu--Sang arXiv:2610.15291v2, Liu arXiv:2610.26835v1, and the
applicability audit of Ye arXiv:2610.15989v2. Main was checked at
`f99d9e3908dde4865377c75d9ca051c1f545bf4f`; publication is additive on
`research/hlc-zero-free-transfer-20261025` in draft PR #1022.

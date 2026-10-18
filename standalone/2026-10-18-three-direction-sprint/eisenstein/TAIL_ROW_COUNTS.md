# The debiased detector inherits the old prime-assisted row counts by a union

**PROPOSED source-qualified transfer lemma.** This is an addendum to the
frozen `TAIL_DEBIASED_MOLLIFIER.md`, SHA256
`66415deed8a2c97c89c20049f8dd6d70ff33a41a1666a84ddc0cdcfa58b5a27a`.
It transfers a COUNT envelope, not a marked-moment theorem, and supplies
no improved count or new zero-free boundary.

Fix one physical row annulus U, one dynamic/amplitude bin, the finite
presentation, the common external parameters, and a chosen detector cutoff
t in [1,3/2]. The modified global mollifier has the same unit gate and
produces a matched witness with

    |Mstar_r S_m|^2 >= U^(delta(r+m)-epsilon),
    r+m>=t-o(1), r<=t+o(1), m<=1/2+O(epsilon).

The tail note proves the pointwise inverse-type upper bound for Mstar,
so the same argument forcing m<=1/2 is valid. Split its dyadic inverse
block as

    Mstar_r=M_r+c_D T_r.

Here M_r is the original Mobius inverse block with its original cutoff
and T_r is the positive squarefree/v tail, if nonempty. The common scalar
c_D is polylogarithmic. After fixing U,t and dyadic labels it is independent
of the varying row, character height and physical prime factors.

The triangle inequality partitions the witness rows into two sets:

1. `|M_r S_m|^2` is at least a fixed multiple of the same spike. The
   ORIGINAL inverse/plain pointwise upper bounds then imply the original
   two saturation inequalities. Every existing selected-prime count
   applies to this subset, with unchanged coefficients and masks.

2. `|c_D T_r S_m|^2` is at least a fixed multiple of that spike. The
   tail note's zero-slot TWO-PLAIN estimate bounds this whole product
   mean by U^(1+epsilon), including c_D. Markov therefore gives

       R_tail<=1-delta(r+m)<=1-t delta+o(1).              (1)

   No selected prime factor is inserted into this mean. The amplitude
   parameter q remains a pointwise label for the physical high estimate;
   restricting to that amplitude subset only reduces the positive sum.

The old source's count at that same t is

    R_old(t)=max(R_short(t),L(t)),
    R_short(t)=1-delta+delta(P_x/D_x)(3/2-t),
    L(t)=1-delta+(5/6-delta)(t-1).

For 0<=delta<=5/6 and 1<=t<=3/2, both branches are at least 1-delta.
Consequently

    1-t delta <=1-delta <=R_old(t).                        (2)

The union of the two sets therefore has exactly the same R_old(t)
upper exponent, up to the same prescribed losses. One may choose the
source's optimizing t after fixing the amplitude bin; the argument
holds for every such t. The finite presentation and dyadic subdivisions
cost only logarithms. Common-profile Sobolev separation handles the
rowwise smooth heights just as in the original detector, and the scalar
c_D contributes only more logarithms. All orders are fixed before the
external height exponent is chosen.

The tail does NOT automatically satisfy the original positive-slot
marked inverse-moment hypothesis. The transfer avoids that false claim
by applying the marked theorem only to the original-M branch. Thus the
global residue-debiased detector can be substituted in the original
counting interface without improving or degrading its exponent. Its
potential benefit is the changed correlated analytic representation of
the complete product observable, whose continuous primitive remainder
and full complementary row operator still require new estimates.

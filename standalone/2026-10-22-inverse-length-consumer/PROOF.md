# A native inverse-length hypothesis sufficient for the 0.874 boundary

Date: 22 October 2026. Status: **PROPOSED source-dependent conditional consumer**.

**No new unconditional zero-free boundary is established.** The inverse-moment
hypothesis below is OPEN. This note replaces the much stronger complete mixed
mean target by a particular pure-inverse target and closes its scalar consumer
over every detector bin, including the floor bin and both frequency endpoints.
The comparison benchmark B_flat = 0.874886647039964... remains imported and
unchanged. No literature-wide novelty claim or independent analytic review is
asserted.

## 1. Exact dependencies and the open hypothesis

Work only over E = Q(omega). The analytic framework is imported from
`openai/math` at commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
`preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`,
Git blob `268c4e3206d460c617d3d2129742a72b831b3def` and inherited raw SHA-256
`42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`.
In particular use its detector-counts proposition, reflection and selected-prime
moments, physical comparison, tails and continuation criterion. Fresh reading
covered relevant source ranges, not a complete independent reconstruction.

General physical geometry, aggregate rescaled-tuple costs and principal
protection are taken at their proposed source-dependent scope from
`GettysburgResearch/riemann`, commit
`0c838d130f275efb6e8ddb81dab42462b4ce9454`,
`standalone/2026-10-18-three-direction-sprint/eisenstein/MIXED_CONSUMER.md`,
blob `dd2ca1c6ef1922efe06e27b882966a968def850d`.
The inverse-length amplification interpretation is from commit
`64cb43c038d1828a478cb97cbc32e435e111d2d2`,
`standalone/2026-10-20-boundary-iteration/mixed/CENTERED_INVERSE_INTERFACE.md`,
blob `291d76fd2dcf1d9c72c40fd2e73814e8926f33af`.

Let M_u(D) be the source's normalized inverse polynomial

    M_u(D) = D^(-1/2) sum_d mu_E(d) nu(d) chi_d(u)^sign W(Nd/D).

Keep its original orientation, finite ray character, common height, common
smooth profiles and their Sobolev control, fixed or moving masks at their
licensed scope, and natural zeros at nonunits. Sum over all sixth-power-free
physical rows Nu about U. No independently chosen arithmetic coefficient
vector for each row is permitted.

The OPEN input is the conductor-uniform estimate

    sum_u |M_u(D)|^2 << (UD)^epsilon (1+T)^A
                             [U + U^(1/6) D^(4/5)].       (H)

It is required for the native range 1 <= log(D)/log(U) <= 3/2, with the fixed
small robust neighborhoods needed for dyadic endpoint and detector losses.
The height order A and common-profile seminorm orders must be fixed before
choosing the source's small height allowance. Constants may depend on epsilon
and fixed local data, but not on the growing moduli. For shorter inverse
lengths, the existing row-size bound suffices.

The existing displayed resource has D^(5/6), not D^(4/5). Thus (H) asks for a
D^(1/30) saving in that branch, not an estimate for Gauss-weighted marked sums.
It does not follow from any of the finite experiments in this continuation.
Under the cited conditional amplification interface, a raw row-size estimate
for H >= D^(24/25), equivalently D <= H^(25/24), would supply this exponent:
5(1-1/25)/6 = 4/5. That raw estimate is also OPEN.

## 2. All detector length cases, not one corner

Use the imported 7/8 foundation, kappa = 3/4, and Delta = 0. Write

    delta = 2a-1, 1/50 <= delta <= 3/4,
    0 <= x <= 1/2, q = x delta,
    D_x = 3 - 17x/9,
    P_x = (2 - 8x/9)(1-x), C = delta P_x/D_x.

Here x is the amplitude parameter, not a physical length exponent. The
unchanged selected-prime argument gives the short-witness count

    R_short(t) = 1-delta + C(3/2-t),  1 <= t <= 3/2.    (1)

For a long inverse witness of length U^r, (H) gives count at most
max(1-r delta, 1/6+(4/5-delta)r). On 1 <= r <= t the first branch decreases
and the second increases, so its full envelope is

    R_long(t) = max(1-delta, 1/6+(4/5-delta)t).          (2)

The source's plain-polynomial witnesses of length exponent at least 1/2
remain covered by the unchanged fourth-moment case. The shorter coupled
witnesses remain covered by (1), with the source's exact interpolation
r_* = [(2-8x/9)t - 5x/9]/D_x. Its bounds
23/37 <= r_* <= 1 and 1/3 <= t-r_* <= 1/2 retain the selected-prime interfaces.
No full mixed-moment assertion is substituted for them.

Choose

    t_* = (5/6-delta+3C/2)/(4/5-delta+C), delta <= 11/15;
          3/2,                              delta >= 11/15.

For the first branch, numerator minus denominator is 1/30+C/2 > 0;
t_* <= 3/2 is exactly delta <= 11/15. Its denominator is positive.
For the second branch, R_long(3/2) <= 1-delta exactly when delta >= 11/15.
Consequently the complete count envelope is

    R+delta = 1 + delta P_x(11/30-delta/2)/J,
                           1/50 <= delta <= 11/15;
              1,           11/15 <= delta <= 3/4,       (3)

where J = (4/5-delta)D_x + delta P_x. The branches agree at 11/15.
This treats the whole detector interval, not only the numerically binding bin.
The floor bin has no zero witness and must instead retain R = 1.

## 3. Physical comparison and both frequency endpoints

Take

    B = 437/500 = 0.874,
    ell = 6/35, b = 0, x_phys = y = 29/70, h = 53/70.

The available prime-length ratio ell/h = 12/53 exceeds 7/37 by 73/1961.
Thus the old selected-prime argument is licensed with fixed margin. Its
finite slot list may be chosen sufficiently fine after the strict margins
below. For b=0 take the fixed scale constant giving P_a=1 exactly in the
additive Gram input; do not apply P_a >= 1 to a smaller arbitrary constant.

Because ell < 1/5, the aggregate rescaled-tuple extra is zero. The low-side
boundary comparison is

    11/12 - ell/4 - B = -1/5250.                       (4)

The original central exponent relative to the principal signal is affine in
the physical frequency exponent d_row in [0,h]:

    E(d_row) = a-B+h(17/50-1/6)-ay-ell/2+q ell
                 + d_row[R+delta/2-17/50].             (5)

It therefore suffices to check both endpoints. No sign assumption on its
slope is made. At d_row=0, use the imported ceiling a <= 7/8, not a <= B:

    E(0) <= h(7/8+17/50-1/6)-B-ell = -10571/42000.     (6)

At the high endpoint,

    E(h) = 1/6-ell/2-B+h(R+delta)+ell delta(x-1/2).

Put E_base = 1/6-ell/2-B+h = -377/10500. In the first regime of (3),

    E(h) = E_base + ell delta(x-1/2)
                 + h delta P_x(11/30-delta/2)/J.        (7)

Here J>0 since 4/5-delta >= 1/15 and D_x >= 37/18. Exact rational
Bernstein subdivision of the entire rectangle
[1/50,11/15] x [0,1/2] certifies E(h) < -1/2000. The polynomial to check is

    Q(delta,x) = [1487/42000 + (3/35-6x/35)delta]
                    [12/5-68x/45 + delta(-1-x+8x^2/9)]
                 - (53/70)delta(2-26x/9+8x^2/9)
                              (11/30-delta/2).         (8)

This is exactly (-E(h)-1/2000)J, with degrees at most two in delta and
three in x. A checker must preserve that variable order and degree, cover
its full rectangle and retain every Bernstein coefficient; a sample grid
is not a certificate. The finite calculation in the accompanying checker
uses exact rational coefficients only. For delta >= 11/15, (3) gives
E(h) <= E_base < -1/2000 immediately.

For the separate floor bin delta_0=1/50, retain R=1 and q<=delta_0/2.
At d_row=h its comparison is

    E_floor(h) <= E_base + h/50 = -109/5250.            (9)

Equation (6) still covers its other frequency endpoint. No zero-detection
hypothesis is applied to the floor.

## 4. Remaining source interfaces and the conditional conclusion

With d_min=1/100 the unchanged small-row comparison is

    h(17/50-1/6)-y/2+(63/50)d_min = -6647/105000.

The principal leftover contours retain positive margins y/20 and h/600;
large rows are handled by the source's sufficiently large absolute contour.
Its full principal H factor is nonzero in the needed domain, as established
by the cited Euler-factor argument for Re(s)>2/3. The nonzero prime
normalizer has only logarithmic inverse growth. The unchanged principal
quantity H(s)/zeta_E^S(s) therefore retains every ordinary zeta zero via
zeta_E(s)=zeta(s)L(s,chi_-3); no auxiliary zero cancels a target zero.

All scalar margins are strict. Choose the profile orders first, then the
small fixed robustness, dyadic and height losses as in the source. Such
losses can be absorbed in (4), (6), (7), (9) and the tail margins. The
source's common Sobolev argument handles moving smooth profiles and
heights; it is not replaced by independent rowwise coefficient choices.
The amplitude/bin bounds are applied after the original holomorphic contour
move, not separately analytically continued as if they were new functions.

Conditional on (H) and all the pinned analytic interfaces, the source
continuation criterion thus excludes ordinary zeta zeros in Re(s)>437/500.
This is a conditional implication, not an achieved numerical improvement.
The decisive missing step is (H), or a complete signed raw-row estimate
that supplies it. A finite row-size trend, exact local cancellation, a
Gauss-weighted norm, and an uncentered positive majorant do not supply it.

## 5. What this changes

The earlier uniform U^(6/5) mixed-mean target asks for substantially larger
savings on parts of its full witness polygon. The present implication
identifies a smaller, specific pure-inverse target while retaining the
unchanged short and plain witness cases. The exact 0.874 parameter consumer
is the contribution; the power-saving inverse estimate is not proved.
This note has author-side algebra checks only. No independent analytic
referee, proof-assistant verification, upstream full reconstruction or new
unconditional zero-free boundary is claimed.

# A complete U^(6/5) mean would already improve the zeta boundary

**PROPOSED conditional consumer. The required arithmetic mean is OPEN.**
This supplements, rather than changes, `MIXED_CONSUMER.md`. Import exactly
its pinned original Eisenstein source, all target and tail interfaces,
the aggregate rescaled-tuple proof, and the robust whole witness polygon.
It uses only that fixed field, while retaining the entire fixed-field
analytic family needed by the detector. No all-number-fields theorem is
required. No new zero-free region has been proved here.

## 1. Weaker sufficient arithmetic target

Instead of the open row-size mean, suppose the COMPLETE original mixed
mean, with every original physical row, nonunit zero, shared prime,
common profile, finite twist and height, satisfies

    sum_rows |M_u(D)S_u(N)|^2
          <<_epsilon U^(6/5+epsilon)(UDN)^epsilon(1+T)^A.   (1)

The scope is the WHOLE polygon `1<=r<=3/2,0<=m<=1/2,3/2<=r+m<=2`,
where D=U^r,N=U^m, together with its small fixed neighborhoods as in
`MIXED_CONSUMER.md` (2a). A neighborhood may cost `U^(C eta)` for fixed
C, provided eta is chosen after the strict margins below. A bound only
at D=U,N=sqrt(U), or only for a projected sector, is insufficient.

Markov and the matched witness give the full count envelope

    R_mix(delta) <= max(0,6/5-3delta/2).                    (2)

Retain also the EXISTING selected-prime count, with kappa=3/4 and its
working 7/8 foundation. With amplitude ratio t in [0,1/2], put

    D_t=3-17t/9,  P_t=(2-8t/9)(1-t),
    J=(5/6-delta)D_t+delta P_t,
    R_old=1-delta+(5/6-delta)delta P_t/(2J).               (3)

One may take `R=min(R_mix,R_old)` in the unchanged retained-bin upper
bound. These are two bounds for the SAME original exceptional rows;
there is no replacement zero detector and no exchange of quantifiers.

## 2. Explicit physical geometry and every parameter cell

Choose

    ell=6/35, b=0, x=y=29/70, h=53/70, B=437/500=0.874.  (4)

The low comparison has margin `B-(11/12-ell/4)=1/5250`.
The selected-prime supply margin is `ell/h-7/37=73/1961>0`.
All aggregate tuple and fixed Gram-scale requirements are those proved
in the parent note, with ell<1/5 and the harmless fixed scale chosen
so the Gram parameter is exactly one.

At the high frequency endpoint the exact exponent is

    E_h=1/6-ell/2-B+h R+delta(h-ell/2+t ell).              (5)

For EVERY `delta in [1/50,3/4]` and EVERY `t in [0,1/2]`, the checker
`relaxed_mixed_consumer_check.py` proves `E_h<-1/1000000` using exact
rational interval arithmetic. This is a continuum cover, not a grid
sample. Each closed rectangle is either proved negative for one of the
two count bounds, or split into both closed halves. Successful finite
termination covers every point and boundary of the original rectangle.

Here are the interval inequalities themselves. On a cell
`[dl,dh] x [tl,th]`, D_t and P_t are positive and decreasing. Thus

    J >= (5/6-dh)D_th+dl P_th = J_low >0,
    R_old <= 1-dl+(5/6-dl)dh P_tl/(2J_low).

Inserting this last bound and delta=dh,t=th in (5) gives a valid source
upper bound. Since `6/5-3delta/2>0` throughout the domain, the mixed
upper bound is exactly

    1/6-ell/2-B+(6/5)h+dl(-h/2-ell/2+th ell).

Its coefficient of dl is negative. The smaller of these two upper
bounds certifies each accepted cell. There are 6,281 final cells, maximum
depth 29, with minimum certified gap strictly exceeding 1/1000000.
The code hashes their full ordered exact-bound stream for replay.

The exponent is affine in the row frequency. Its OTHER endpoint is at
most `-10571/42000`, using the legitimate source ceiling a<=7/8. The
floor bin, which has no zero witness, uses R=1 separately and gives
`-109/5250`. The small-row error at d_min=1/100 is `-6647/105000`.
All frequency endpoints, all dynamic and amplitude bins, and the floor
are therefore paid. The unchanged principal leftover and large-row
contours have the positive margins stated in the parent note.

Choose the robust length neighborhood and then all detector buffers,
meshes, arithmetic powers and height losses smaller than a fixed part
of these strict gaps. The target Euler factor and prime normalizer are
unchanged and nonzero. Every ordinary zeta zero is retained through
`zeta_E=zeta L(s,chi_-3)`. Conditional on (1) and the explicitly imported
source interfaces, the continuation criterion would exclude zeros with
real part greater than 437/500.

## 3. What this changes in the actual research target

The full `U` estimate in the parent note is stronger than necessary for
a first improvement over the reported working boundary near 0.874957.
The complete `U^(6/5)` target already suffices. In particular the legal
height-adapted norm comparison in `GROWING_PROFILE_COMPARISON.md` costs
UG, so G=U^(1/5) fits this arithmetic budget throughout the witness
polygon. Several paid conductor sectors fit it too. Their FULL signed
complement and the full modified norm remain OPEN. No sum of already
paid sectors is silently substituted for that missing norm.

The checker also exhibits an exact positive exponent at one parameter
point if only R_old is used. Thus the existing source estimates alone
do not prove (4), and the interval calculation is not a new zeta result.

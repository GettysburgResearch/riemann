# Any fixed power saving in deep failures would suffice

Status: proposed component proofs; independent mathematical review required.
RH and any native failure-count power saving are NOT proved.
Publication parent: PR #803, cdbe96a71523c81a7f50c8fe990f0f702ab49c82.

This pass combines two previously separate pieces: the full source's growth
is bounded by its unknown rightmost spectral *supremum*, while sparse
negative samples improve the analytic domain of its Mellin transform.
Feeding the latter back into the former strictly decreases the exponent.
No rightmost zero has to exist.

For the unchanged prime-power scalar D, a fixed h>=0, and r=1 or 2, define

    F_(r,h)(K)=#{2<=k<=K : D(k^r)<-h}.

The complete proposed theorem is

    RH iff there exist C>0 and delta>0 such that
           F_(r,h)(K)<=C K^(1-delta) for all K>=2.

This replaces the earlier square-root-count target by ANY one fixed power
saving. It also permits counting only deep failures, for example h=1,
and only the r=2 grid, corresponding to original prime scales X=k^4.
The terminal inequality in that version is

    #{2<=k<=K : B(k^2)<(135/2)k^8-240k^6} <= C K^(1-delta).

That estimate remains OPEN. No numerical range or count saving is added.

## New proved implications, at their stated paper-proof scope

1. If RH fails, every fixed-depth failure count above has upper growth
   exponent exactly one. This strengthens the old lower exponent beta.
2. A count saving delta gives the conditional feedback
   u -> max(0,u-delta/r) for the source growth exponent; the same counting
   hypothesis finishes after at most ceil(r/delta) steps.
3. The same full count exponent holds for failures below -m^q whenever
   0<=q<2Theta-1. Neither a rightmost zero nor zero simplicity is assumed.
4. If an off-line rightmost real part is actually attained, both signs
   have positive LOWER natural density, by an absolutely convergent
   almost-periodic leading spectrum. The extra hypothesis is explicit;
   no such density conclusion is asserted without it.

Read PROOF.md, especially sections 2--5. The pole and growth boundary must
belong to the SAME native source. The exact compact initial Mellin term,
prime-power jumps, logarithmic grid-interpolation loss, and every analytic
multiplicity remain present. The real pole at z=1 cancels explicitly.

The infinite arguments are not consequences of finite replay counts.
The checker reconstructs the elementary source constant and bounded
arithmetic fixtures, authenticates the three used parent proofs, and checks
the finite exponent and cell-geometry calculations. It does not run any
parent producer or establish the still-missing count hypothesis.

    python -I -S -B verify.py --check result.json
    python -I -S -B -O verify.py --check result.json
    python -I -S -B test_rejections.py
    python -I -S -B -O test_rejections.py

This is classical Landau/measure-oscillation methodology applied to our
source and sparse grid, not an external-priority claim. Prior art, source
locks and the limits of the broader synthesis are in SOURCES_AND_SYNTHESIS.md.

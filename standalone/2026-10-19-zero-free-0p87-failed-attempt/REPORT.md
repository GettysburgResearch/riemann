# Failed attempt to obtain the zeta half-plane Re(s)>87/100

**Outcome: no new zero-free region was proved. No new remote commit or pull
request was created. This is a failed-candidate record, not a proposed theorem.**

The objective was an actual improvement for ordinary zeta, not a new family
moment, matrix representation, or conditional RH criterion. The reported
external working benchmark is Liu v2's

    B* = 0.874957019420098946...,
    B*=(18x+7)/(18x+9),
    1188x^3-2160x^2+171x+190=0, .38858<x<.38859.

The attached code reproduces this reported number by rational root bracketing;
it does not verify the analytic theorem behind it. The all-field 271/300
proposal is numerically weaker for ordinary zeta and is not the benchmark.

## 1. The explicit 0.87 comparison fails

Adopt the balanced comparison and witness-capacity formulas described in
#934 notes A and E, and consider the stated variable-kappa continuation.
These are assumptions of the following estimate-budget calculation, not
independently re-proved analytic inputs.

Let

    B=87/100, ell0=14/75, delta=7/18, x=1/2, alpha=5/6.

Here (1+delta)/2=25/36 is an AUXILIARY zero class, not an asserted location
of an actual zero. To have 11/12-ell/4<=B requires ell>=ell0. Omitting every
additional positive penalty in the direct estimate only makes the attempted
comparison easier. The usual positive-length parameterization has

    ell>=ell0, b>=0, b+ell<=1,
    ly=(1+b-ell)/2, h=(1+b+3ell)/2.

For a given kappa put

    c=2/(3kappa), D=3-(1+c)x, P=(2-cx)(1-x),
    J=(alpha-delta)D+delta P,
    t=1+delta P/(2J),
    r=((2-cx)t-x(1-c/2))/D, m=t-r,
    zM=(1-r)/2, zS=(1-2m)/(6kappa),
    R=1-delta+(alpha-delta)delta P/(2J).

At kappa=3/4 these are the documented #934 formulas. They give

    t=443/394, r=141/197, m=161/394,
    zM=28/197, zS=8/197, R=2363/3546.

The inverse, plain and long-witness exponents all equal R. The second
inverse-capacity inequality 2r+8zM<3 is also satisfied.

The raw endpoint error relative to the FIXED candidate B is

    E=a-a*ly-ell/2+x*delta*ell+h*(R+delta/2-1/6)-B,
    a=(1+delta)/2.

At ell=ell0 this simplifies exactly to

    E=521/19700-b/7092.

For every b in [0,61/75], therefore,

    E >= 7003/265950 > 1/40.

Increasing ell does not fix the failure. On the enlarged triangle above,
write v=ell-ell0>=0 and u=1-ell-b>=0. Direct substitution gives

    E = Emin + (E_ell-E_b)*v + (-E_b)*u,
    E_ell=640/591, E_b=-1/7092.

Both added terms are nonnegative. This is an exact affine certificate,
not a sampled optimizer result. Extra physical side constraints can only
restrict the triangle; they do not invalidate this lower bound for the
error EXPONENT allowed by these upper estimates.

## 2. A more favorable moment parameter still does not rescue it

Granting the more favorable parameter kappa=37/50 gives

    R=2075/3114,
    E(ell0,b)=457/17300-b/6228,
    Emin=6139/233550 > 1/40.

This is an optimistic diagnostic, not a claim that the stronger analytic
input has independently been established. Within the displayed formula,
R increases with kappa. To see this, at x=1/2 set

    q=P/D=(4-c)/(2(5-c)), A=alpha-delta>0.

Then R=1-delta+A*delta*q/[2(A+delta*q)] increases with q;
q decreases with c; c decreases with kappa. Thus the favorable diagnostic
also bounds the error from below for every kappa>=37/50 within this model.

At b=1/8 the required count for this single class would be

    R <= 214/337 = 0.6350148367...,

rather than 2075/3114=0.6663455362... in the favorable calculation. The
missing count saving is exactly 32879/1049418=0.0313306994.... A different
signed physical estimate could change the comparison instead. No such
estimate was proved in this pass.

## 3. The raw new sieve is not the missing estimate

For the sextic four-term kernel, at column exponent v>=0,

    k(v)=max(1,v,5/6+v/3,1/3+5v/6).

At delta=7/18 the minimum of k(v)-delta*v is 7/9, attained at v=1.
The proof is the four affine pieces, with slopes

    -delta, 1/3-delta, 5/6-delta, 1-delta.

The first two are negative and the last two positive. This isolated
weighted-kernel calculation is too weak to replace the needed count above.
It is NOT a theorem that every application of the sieve, every residual
estimate, or every other method is limited by 7/9.

## 4. Other proposed shortcuts were not promoted

The live Gram-mechanism note explains why subtracting a scalar Gauss first
mean does not automatically remove the complete exceptional-frequency
covariance. The paired filters in #1002 have no proved stronger estimate
for that full physical covariance. I did not insert an assumed saving.

The common-factor quadratic-field average retains a common Mobius channel.
Cofactor orthogonality is not a bound for it. A full-product residual strictly
below one would be useful, but that strict inequality was not proved.

On the functional-equation diagonal, the leading residue cancels target
zeros as well as auxiliary zeros. The first transverse coefficient restores
the logarithmic derivative, but its full physical signed bound remains
unproved. I did not treat a meromorphic identity as that bound.

These statements describe why the attempted arguments did not finish.
They are not new obstructions to the actual Riemann zeta function.

## Sources and reproduction

- #934 at 3092feee25c583ec760c5f14f4aa4c98d9c5df39:
  research/exploratory/2026-10-10-quasi-rh-wave/notes/A_exponent_model.md,
  E_mechanism_lead.md, J_gram_loss_attack.md,
  O_hybrid_induction.md, N_floor_first_moment.md.
  The relevant live mathematical text was inspected. Its source-level
  claims retain their original proposed/review scopes.
- #1002 at 1319373815ee408146705b25a426fba6b22ed755:
  standalone/2026-10-18-five-route-zero-preserving-attack/SOURCES_AND_REVIEW.md.
  This records the Liu-v2 benchmark and the unsolved physical adapters.
- Liu, arXiv:2610.12234v2. The current turn's earlier primary HTML reading
  supplied the variable-kappa formulas; later fetches returned cache-miss
  errors. No fresh formal build, source archive, or complete upstream proof
  verification was achieved.
- #962 at b2032c663736ecd1e3872559d160ce069664ea06 was revisited at
  PR-description scope for the free-Mellin signed-extraction boundary.

Run `python -I -S -B verify.py` and `python -I -S -O -B verify.py`.
Both modes were actually executed and produced byte-identical RESULTS.json.
Only standard-library exact rational arithmetic is used. These checks certify
the displayed substitutions and the finite algebraic certificate, not any
new infinite analytic bound. No agents or external referees were used.

The currently exposed GitHub action set was read-only. Direct GitHub DNS
resolution in the container failed. More importantly, there is no new
zero-free theorem to publish. The preceding #1002 was already published;
this record neither duplicates its claimed advances nor changes main.

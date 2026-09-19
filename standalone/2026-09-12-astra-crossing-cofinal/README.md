# XCC26 — sparse crossing cuts, multiplicative signs, and the exact remaining covariance

**PROPOSED component proofs; independent mathematical review required. RH and
the cofinal native sign/covariance estimate remain OPEN.**

This addition-only continuation of PR848 does not raise Newton order again.
It replaces the rigid square/cubic ladder with a sparse, arithmetic choice of
cuts and uses that freedom to construct a different normalized source.

Parent: `2f0056d542603cb8118b9ac9da45b397162778e4`.
Read [PROOF.md](PROOF.md), particularly Sections 1,2,3 and5.

## Main connection

For the actual reciprocal Mobius sums m(k)=sum_(n<=k)mu(n)/n and
F_Y=sum_(k<=Y)m(k)^2, let Theta be the supremum of nontrivial zeta-zero real
parts. The written proof reconstructs the classical analytic implications to
obtain the TRUE limit

```
lim log(1+F_Y)/log(Y+1) = 2Theta-1.
```

The analogous limit holds for the original Mertens-prefix energy E_Y. No
value of Theta is obtained. This is not regular variation or a new zero-free
region. Its consequence is useful: a fixed subquadratic gain at ANY unbounded
sequence of cuts suffices for RH, with no restriction on gaps between them.
This is stronger than asking only for a recurrence on a predetermined ladder;
the source estimate supplying the gain is still missing.

The weak sign-crossing set

```
X={Y>=2:mu(Y)!=0, m(Y-1)m(Y)<=0}
```

is unbounded by a complete Landau oscillation argument. At every such cut,
|m(Y)|<=1/Y and a one-coefficient completion

```
c_n=mu(n) (n<=Y), c_(2Y)=-2Y m(Y), otherwise0
```

has ALL of the following:

```
|c_n|<=2, P_c(1)=0, support<=2Y,
J(c)=F_Y+(Y-1)m(Y)^2 <= F_Y+1/Y,
c_n=lambda(n)b_n with b_n>=0.
```

Thus all convolution powers have exactly Liouville-coherent signs. No future
Mobius input is used, no large balancing coefficient is introduced, and the
entire physical future is paid. The earlier unrestricted optimum and clipped
completion are not changed or assigned these new properties.

## Complete end-to-end criterion, not a proved antecedent

For z=c*c and the actual centered harmonic packets K_d, retain one term per
integer product before forming the ordered distinct-product covariance C_Y.
The complete diagonal and native output obey

```
D_Y <=288 H_(4Y^2)^4,
F_((Y+1)^2-1) <=F_Y+8/Y+576 H_(4Y^2)^4+2 C_Y.
```

If C_Y<=0 at arbitrarily large Y in X, RH follows. A suitable subquadratic
upper bound on that same sparse set also suffices. More sharply, failure of
RH would force

```
C_Y/F_((Y+1)^2-1) ->1 along X,
```

so the covariance would eventually be POSITIVE at every late crossing.
The crossing set is proved cofinal; favorable covariance within it is NOT.
Neither finite signs nor small endpoint values establish that missing fact.

## Direct tests of the attempted sign proof

All 34 native panels (every crossing through127, plus173,210,431) have negative
covariance in exact outward arithmetic. For example,

```
-12.978394364 < C_431 < -12.978394359.
```

They are not an all-scale sign theorem. The first crossing Y=5 already has
a POSITIVE individual covariance pair (2,5), greater than1/100. Moreover a
fully specified NON-NATIVE sign-coherent prefix at Y=19, completed by the
identical rule with reciprocal crossing +/-1/38, has covariance in(1.77,1.78).
It violates divisor inversion at n=2. Thus even complete multiplicative sign
alignment and a negligible collar do not prove the desired total sign.
The full native divisor constraints must still be used inside the signed sum.

## Latest-work reconciliation and evidence

[SOURCE_LOCK.json](SOURCE_LOCK.json) records the live main/PR848 pins, the
latest-20 updated PR reconnaissance and actual source-reading depths. New
finite-gamma exterior theorems, finite exceptional-divisor reductions, Ising
moment realizations and the polynomial boundary argument are kept at their
own scopes. Their fixed-stage/local conclusions do not supply this covariance
bound. In particular the same-path BHH26 alternatives #859/#860 are not
counted as independent acceptance. This is not a full mathematical review
of every active branch.

The independent-implementation finite protocol reconstructs95 crossings
through1024,34 full native output panels and the two countertests. Its exact
quotient-block identity covers5,538,817,076 product/time contributions through
2,874,506 evaluated groups; those billions were NOT iterated individually.
The largest native prefix ends at186623. [VALIDATION.md](VALIDATION.md)
distinguishes proofs, finite computations, source identities and non-replays.
The two programs have one author; they are not independent referee acceptance.

```
python -S -B produce.py --check result.json
python -S -B verify.py result.json --self-test
python -S -O -B produce.py --check result.json
python -S -O -B verify.py result.json --self-test
```

The most important review targets are the all-prefix zero lower bound and
generalized Littlewood upper bound, the Landau cofinality argument, the
lambda(2Y) sign and full norm of the collar, and the arbitrary-subsequence
quantifiers. The final infinitely-often arithmetic inequality is an explicit
research obligation, not a routine missing detail of a claimed RH proof.

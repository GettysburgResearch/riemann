# Mesoscopic prime-exchange covariance

**Status:** proposed complete unconditional component proofs; not independently
reviewed. **Not pushed.** No full critical-energy bound, native higher-moment
hierarchy, new zero-free exponent, or RH proof is claimed.

Intended location: `standalone/2026-10-17-mesoscopic-prime-exchange/`.
Intended base: PR #953 at `a93d382951f8fac7b0c28783061a7ddb99fcf0a4`.
Intended branch: `research/mesoscopic-prime-exchange-20261017`.

## The result

Use either the actual principal 0/1/m source over Q(omega), m>=4, with
arbitrary bounded powerful phases, or the original ideal Mobius source.
Group ALL ideals of each rational norm into A(n). In the complete Gaussian
critical energy retain every ordered pair whose reduced rational norm ratio
is p/q, where p,q are distinct split rational primes in [Y,2Y] with
0<|p-q|<=H. Denote this complete selected signed sum by X(D;Y,H).

For every fixed 0<eta<theta<1,

    X(D;D^theta,D^eta) asymp D^eta > 0.

In particular,

    X(D;D^(3/4),D^(1/4)) asymp D^(1/4),

while EVERY selected pair has norm ratio within D^(-1/2) of one. All pairs
are unequal and incomparable by ideal divisibility. The full Gaussian tail,
common factors, both conjugate prime ideals and all norm-fiber multiplicities
are included. This is a fixed-twist theorem, not a long Mellin average.

The ABSOLUTE upper bound also holds for arbitrary physical row phases and
nonunit masks, with total row mass Z:

    AbsX <= C_(K,c) Z H [1+log_+(D/Y)]^2
                              /[log(2Y) log(2H)],

uniformly in m>=4. Thus the power in the upper bound is sharp for this selector.
The signed lower statement has the stated principal ordinary phase and fixed
exclusion hypotheses; it is not extended to arbitrary rows.

## How it is proved

At every good split rational prime the complete norm coefficient satisfies

    A(p^(e+1)) conjugate(A(p^e))=-r_p(e)<=0,

with support e=0,1,m and explicit nonnegative coefficients. Hence

    A(pk) conjugate(A(qk))
       =r_p(v_p(k))r_q(v_q(k))|A(k0)|^2 >= 0.

The common k is not assumed coprime to pq. Its Dirichlet series has an explicit
double pole at one and a holomorphic remainder for Re(s)>1-1/m. A uniform
Mellin calculation gives a complete quadratic polynomial in log(D/sqrt(pq))
plus O((D/sqrt(pq))^(-delta)), for every fixed delta<1/m (delta<1/2 in the
native case). All moving primes are retained.

Classical fixed-modulus PNT, a bin-counting lower bound, and an explicitly
reconstructed Selberg upper sieve show that the number of close prime pairs
is of order YH/log^2 Y when H is a fixed positive power of Y. No prime-pair
conjecture or PNT in each short interval is assumed.

## Relationship to the live work

PR #953 controlled ideal-divisibility pairs. PR #954 added equal-norm
collisions and a long Mellin-average theorem. This packet addresses growing
INCOMPARABLE, UNEQUAL, NEAR-EQUAL-NORM ratios and their signs. It also
strengthens the quadratic norm-collision leading asymptotic to a full
logarithmic polynomial with a power error. Overlap and classical methods are
credited in SOURCES.md; global literature novelty has not been established.

A positive selected covariance is not a PSD subprojection of the full energy.
It would be invalid to infer E(D)>=X(D;Y,H). The remaining signed sectors can
cancel it. The critical total-energy estimate remains unproved.

## Files and replay

Read THEOREMS.md, especially Theorems 1, 1A and 2. VALIDATION.md states exact
finite coverage and review limitations. Run:

    python checks/check.py > /tmp/exchange-normal.json
    python -O checks/check.py > /tmp/exchange-opt.json
    cmp /tmp/exchange-normal.json outputs/EXACT.json
    cmp /tmp/exchange-opt.json outputs/EXACT.json
    python checks/verify_manifest.py

Optional, uncertified numerical quadrature checks require mpmath:

    python checks/check_numerical.py > /tmp/exchange-numerical.json
    cmp /tmp/exchange-numerical.json outputs/NUMERICAL.json

No remote publication, full-repository CI, Lean build, independent mathematical
review, or asymptotic inference from the finite checks is claimed.

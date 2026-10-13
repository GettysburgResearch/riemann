# A short neutral-divisor window for the native signed moment

**PROPOSED component mathematics. The full generalized moment and RH remain
unproved. No new full-moment exponent or zero-free boundary is asserted.
No independent mathematical review has been performed.**

This continuation of #943 goes back to #942's actual physical row kernel.
Read PROOF.md, particularly Theorem 2, Corollaries 3--5 and the surviving
large-active-conductor case in Section 6.

## Result

For a nonprincipal tuple, separate its active conductor C from the neutral
prime mask R. Write c=NC and

    h(u)=chi_C(u) 1_{(u,R)=1},
    S_chi(T)=sum_{v!=0} Phi(v/sqrt(T)) chi_C(v),

using the ONE fixed positive radial band-limited Schwartz majorant of #942.
The exact signed mask formula is

    K_{C,R}(H)=sum_{d|R} mu_K(d)chi_C(d)S_chi(H/Nd).

The small divisors Nd<=H/c vanish EXACTLY by Poisson quadrature. Divisors
Nd>H X^delta contribute a uniformly negligible tail. At every fixed k,
delta>0 and B>0, the COMPLETE native nonprincipal moment can consequently
be replaced, with error O(X^(-B)), by the signed divisor window

    H/c < Nd <= H X^delta.

This is a localization, not an estimate for the surviving signed window.
No neutral zero is dropped and no false condition (d,v)=1 is added.

## An order-uniform, almost log-square window

An explicit positive compact-frequency convolution makes the ONE fixed
majorant decay like exp(-c |z|^(1/s)), for any chosen fixed s>1. With this
choice, Theorem 3A is quantitative for EVERY k>=1:

    upper cutoff HL = H * O_eta([ (k+B+1)log(2X) ]^(2+eta)),
    absolute aggregate truncation error <= X^(-B).

Here eta>0 is fixed before X,H,k; the exact L and constants are in (8a).
There is no unspecified k-dependent error constant. The row mass remains
O_eta(H). This is not a growing Fourier-support scheme, a random-prime
model, or a full growing-order moment theorem. It controls the discarded
terms, not the signed sum in the surviving window.

## Genuine extension beyond the total-radical cutoff

If R has no divisor in that interval, the selected nonprincipal contribution
is O_B(X^(-B)) for every B. Its TOTAL radical CR can greatly exceed H.
A useful sufficient criterion is: every individual neutral prime is in the
exact-zero range, while the product of any two is already in the decaying
tail. A higher-j version uses the products of the j largest and j+1 smallest
neutral prime norms. It does not require enumerating all divisors.

There are actual annular native tuples of every fixed order 2k>=4 in this
region: take distinct conjugate singleton primes a,bar(a) of norm D^alpha,
a common prime factor p of norm about D^(1-alpha), and k-1 matched neutral
prime factors of norm about D. All columns have norm about D. For

    h=21/20, alpha=1/100, delta=2/5,

both required exponent inequalities hold. The total radical is about
D^(k+1/100), and the singleton primes exceed (log D)^2. Thus this is outside
both #942's total-radical cutoff and #940's log-square singleton condition.
The comparison is ONLY with those two conditions; no dominance over every
older signed large-gcd sector estimate is claimed.

The finite norm witness in the proof has D=16384, H=2097152, active norm 49,
neutral norm 21624607 and total radical norm 1059605743. It checks the
hypotheses, not an infinite numerical Schwartz sum.

## What remains unpaid

If c>H then d=1 survives. In particular R=1 and c near X^(2k), the primitive
long-singleton case, is untouched. The exact native Möbius signs must still
be used to prove a one-sided O(H X^(k+epsilon)) bound for that signed sum.
The present lemma neither proves that estimate nor assumes it implicitly.

The row majorant bounds the FULL nonnegative sharp moment. It does not
bound each selected signed sharp-row contribution by its smooth analogue.
The proof gives a concrete sharp-row counterexample to that substitution.

## Replay and scope

Run in this directory, with Python 3 and no third-party packages:

    python -I -S -B verify.py > replay.json
    python -I -S -B -O verify.py > replay.optimized.json
    cmp replay.json results.json
    cmp replay.optimized.json results.json

Both modes passed, with 183253 explicit predicates (including setup and
repeated local cases). The complete quartet test has all seven good
squarefree columns in 32<Nn<=64, all 54 nonzero rows Nu<=13, and all 2401
ordered tuples. The separate dilation fixtures include inert and split
primes, nonunit zeros and repeated prime powers. Six counterexample controls
cover invalid substitutions. The test does not sum an infinite Schwartz
series or certify an analytic theorem.

native_helper.py is an unchanged authenticated copy of #942's census.py;
its Git blob is 2a074ccede483324392a729056ccbf43a1f26eac. No parent large
census, remote CI or proof-assistant build was rerun. Proof and checker have
the same author. See SOURCES.md and VALIDATION.md for the precise boundaries.

# CANDIDATES.md

Registry of proposed counterexamples (`Z-####`).  Maintained by the integrator.
A candidate stays a candidate until **existence of a zero** and **separation
from the critical line** are both certified and independently reproduced
(README §7).

Current tally: **0 surviving candidates.**  Z-0001 refuted; Z-0002 refuted at
its five strongest instances, including the classical Lehmer pair at
`gamma ~ 7005` with the class still open at greater heights;
Z-0003 refuted throughout the tested range; Z-0004 searched with a purpose-built
screen whose sensitivity has been measured, no anomaly found.  Nothing in this
repository is evidence against RH.

---

## Z-0001 — the tightest Lehmer pair below height 500 is an off-critical pair

```text
Candidate ID:     Z-0001
Status:           REFUTED
Proposing agent:  claude-01
Object:           the pair of consecutive zero ordinates with the smallest
                  normalised gap in 0 < t <= 500, together with the assertion
                  that they are in fact a single complex-conjugate-symmetric
                  pair displaced off the critical line rather than two on-line
                  zeros
Claimed failure mode:  a tight "pair" is what an off-line pair looks like from
                  the critical line: as a zero moves off the line its mirror
                  image approaches it, and near the moment of collision the
                  Z-function's two sign changes merge and vanish
Dependencies:     X-0001, L-0002, L-0004
Verification status: REFUTED by X-0001
```

**Refutation.**  X-0001 certifies that the number of zeros of `xi` in
`[0,1] x [0,500]` is exactly `269`, and independently exhibits `269` certified
sign changes of the Hardy function `Z` in `(0, 500]`.  By L-0004 every zero in
that range is on the critical line and simple.  A displaced pair would produce
**two fewer** sign changes than the box count.  There is no deficit.  Hence no
pair below height 500 — tight or otherwise — is off the line.

**Why it was worth writing down anyway.**  This is the shape of the argument
that would work: the observable is a *deficit* between two independently
certified integers, and it is cheap.  Z-0002 applies it where it is not yet
settled.

---

## Z-0002 — an off-critical pair hides at a tight Lehmer pair above the certified range

```text
Candidate ID:     Z-0002
Status:           IDEA  (partially tested; the specific pair at gamma ~ 1977.17
                  is now REFUTED, the class remains open)
Proposing agent:  claude-01
Object:           a box D = [0.3, 0.7] x [t_1, t_2] straddling the critical
                  line and containing exactly the two members of an anomalously
                  close pair of zero ordinates
Claimed failure mode:  the two "zeros" are a conjugate pair in the w-coordinate
                  of T-0001, i.e. one zero at 1/2 - delta + i gamma and its
                  mirror at 1/2 + delta + i gamma
Dependencies:     T-0001, X-0004, L-0006
Verification status: see below
```

**Why Lehmer pairs are the right target.**  `Lambda >= 0` (Rodgers-Tao) and RH
`<=>` `Lambda <= 0`, so RH holds iff `Lambda = 0`: the zeros sit exactly on the
boundary of failing, and the historic route to lower bounds on `Lambda` is
precisely through anomalously close pairs.  A tight pair is also where T-0001
is most sensitive: by T-0001(e) the Hankel determinant is the discriminant
`prod (w_i - w_j)^2`, so a pair that is already nearly colliding contributes a
small positive factor that a displacement `delta` flips negative most easily.

**Concrete target found (X-0004).**  Scanning certified on-line zeros to
`T = 2000` (1517 zeros, all ordinates certified), the smallest normalised gap
is

```
n = 1495 :  gamma = 1977.173944...,  gamma' = 1977.271446...
            gap = 0.0975,  normalised gap nu = 0.0893,  D = 0.0259
```

i.e. the pair is about **11 times closer than the mean spacing** at that
height, and it lies *above* the range certified by X-0001.

**Status: the four tightest pairs below `T = 2000` are all REFUTED.**  Each was
attacked with **two independent certified methods** — the Hermite-Hankel
criterion (T-0001) and the argument principle plus sign changes (L-0004) — and
both agree in every case:

| `gamma` | normalised gap `nu` | T-0001 verdict | winding count | sign changes |
|---|---|---|---|---|
| 1977.174 | 0.0893 | PD | 2 | 2 |
| 1329.044 | 0.1376 | PD | 2 | 2 |
| 1415.586 | 0.1688 | PD | 2 | 2 |
| 1054.781 | 0.1803 | PD | 2 | 2 |
| **7005.063** | **0.0421** | **PD** | **2** | **2** |

(`experiments/X-0002-hermite-box-certificates/results/lehmer-pair-1977.json`
and `lehmer-pairs-top4.json`.)  In every box the two zeros are certified to lie
exactly on the critical line — and note that a `PD` verdict excludes an
off-critical zero at **every** displacement, not merely above some threshold,
because T-0001(c) is an equivalence.

**The targeting claim, now quantified (X-0002b).**  The displacement at which
this method would *positively announce* a counterexample rather than abstain is
`delta_detect ~ (gap/2) sqrt(rho)`, with `rho` the relative uncertainty of the
least certain Hankel pivot — proportional to the ordinate gap.  Measured on the
certificates already computed:

```
ordinary boxes            delta_detect  0.031 .. 0.280
the four Lehmer-pair boxes delta_detect 0.0043 .. 0.0057
```

roughly fifty times better at the tight pairs, which is the quantitative form
of the qualitative argument made above.

**The classical Lehmer pair is now settled.**  The pair Lehmer himself singled
out in 1956, at

```
gamma = 7005.062866174921...,  7005.100564672647...   (certified ordinates)
gap = 0.037698,  mean spacing 0.8955,  normalised gap nu = 0.0421
```

— about **24 times closer than the average spacing at that height**, and the
tightest pair this repository has examined — was certified by both methods:
T-0001 returns `PD`, the winding count is `2`, the certified sign-change count
is `2`, deficit `0`.  Both zeros lie exactly on the critical line.
(`experiments/X-0002-hermite-box-certificates/results/lehmer-pair-7005.json`.)

The class Z-0002 remains open at greater heights, where the far more extreme
pairs near `10^22` live — beyond this repository's `O(T^2)` toolchain until
Q-0001 is done.

**What a later agent must do to settle a Z-0002 instance:** run
`H.box_certificate(0.3, 0.7, t1, t2)` with `t1, t2` midway between the pair and
its neighbours.  A `PD` verdict refutes; a `NOT_PSD` verdict is a certified
counterexample and must immediately go to two independent adversarial reviews
(README §6).  `UNDECIDED` means raise `nsub` (error falls like `nsub^{-4}`).

---

## Z-0003 — a certified arithmetic witness (Robin / Lagarias / Nicolas)

```text
Candidate ID:     Z-0003
Status:           REFUTED in the tested range (open beyond it)
Proposing agent:  claude-01
Object:           an integer n with sigma(n) >= e^gamma n log log n and
                  n > 5040; or a primorial N_k with
                  N_k/phi(N_k) <= e^gamma log log N_k
Claimed failure mode:  a single integer is a complete counterexample -- no
                  contour, no continuation, no truncation
Dependencies:     X-0003
Verification status: no violation, certified
```

**Result.**  X-0003 tests the colossally abundant numbers up to `n` with 11541
decimal digits and the primorials up to `p_k = 2 * 10^6` (`log N_k ~ 2 * 10^6`).
Left-hand sides are **exact integers / exact rationals**; right-hand sides are
certified enclosures.  **Zero certified violations.**  The exceptional set
`n <= 5040`, where Robin's inequality is known to fail, is excluded by
hypothesis and is not a counterexample.

**But note how close it is.**  At the largest colossally abundant number
tested, the Robin ratio is

```
sigma(n) / (e^gamma n log log n) = 0.999493717304...
```

within `5.1 * 10^-4` of failing, and the Lagarias ratio is `0.999491586...`.
This is the *smallest margin of any criterion in this repository*, which is
either the most encouraging fact here or the most misleading one — see
NEGATIVE_RESULTS **R-0004** for why it is probably the latter (under RH the
ratio tends to 1 from below, so closeness is the *predicted* behaviour), and
O-0001 for the quantity that actually carries the information.

---

## Z-0005 — a negative Weil form: a counterexample made of primes

```text
Candidate ID:     Z-0005
Status:           IDEA (the format is implemented and certified; no violation
                  found in any space tested)
Proposing agent:  claude-01
Object:           a finite vector c and a finite basis of compactly supported
                  test functions phi_j with c^T Q c < 0, where Q is the Weil
                  quadratic form
Claimed failure mode:  Weil positivity is equivalent to RH; a negative value is
                  a counterexample, and it is computable from FINITELY MANY
                  PRIMES with no evaluation of zeta anywhere
Dependencies:     T-0002, X-0006
Verification status: every matrix tested is certified positive definite
```

**Why this is the most reviewable witness format in the repository.**  A
negative pivot here is a statement about a couple of dozen integers, a handful
of logarithms and one Gamma-function series.  An independent verifier needs a
prime table and a digamma routine — not a certified `zeta`, not a contour, not
an argument principle.  Compare Z-0002, whose verification needs the whole
`certzeta` stack.

**And height is free.**  With the matched filter of T-0002(e) the prime sum
does not depend on the height being probed: the same 143 prime powers certify
at `gamma_0 = 0` and at `gamma_0 = 7005`.  No other tool here has that
property.

**What is not true.**  A `PD` verdict does *not* prove RH on any region — the
Weil criterion is an equivalence only over all test functions, and any finite
basis sees only a projection.  This candidate can be refuted-by-search but its
negative result is much weaker than T-0001's.

**Next step:** the cost law in T-0002 says a filter narrow enough to resolve
individual zeros at height `T` costs `(T/2pi)^m` primes.  At `T ~ 100` with
`m = 2` that is a few hundred primes.  That computation is cheap and has not
been run; it is the honest test of the method's reach.

---

## Z-0004 — an anomalous frequency in `theta(x) - x`

```text
Candidate ID:     Z-0004
Status:           SEARCHED, no anomaly found (screen built; sensitivity measured)
Proposing agent:  claude-01
Object:           a frequency present in the oscillation of theta(x) - x whose
                  amplitude grows like x^{beta} with beta > 1/2
Claimed failure mode:  by the explicit formula the oscillation of theta(x) - x
                  is sum over rho of x^rho / rho; a zero with Re rho > 1/2
                  contributes a component of frequency gamma (in log x) whose
                  amplitude grows faster than x^{1/2}
Dependencies:     O-0001, X-0003, X-0005
Verification status: searched; no anomalous or growing line found within the
                  screen's measured sensitivity
```

Built and run in X-0005 (see O-0002).  The spectrum of `(psi(x)-x)/sqrt(x)`
from a prime sieve reproduces the first twelve zero ordinates with the
predicted `2/|rho|` amplitudes; no extra line and no growing line was found.

**What that null result is worth is exactly the screen's sensitivity**, and the
sensitivity was measured rather than assumed (M-0003).  Across three designs:

```
periodogram, two sieve limits    floor delta >= 0.2
paired equal-length Hann windows floor delta >= 0.1   (0.02 for isolated lines)
joint least-squares fit          estimator floor <= 0.0005; real-data floor ~0.013
```

So the honest statement is: **no off-critical displacement above roughly
`delta ~ 0.013` among the first twelve ordinates**, uncertified, from the
primes alone.  This does not compete with L-0004, which certifies *every*
displacement in its range; the screen's distinct value is that its cost does
not grow with the height of the target.

Remaining lever, diagnosed in O-0002: window length, i.e. a larger sieve.
See Q-0010.

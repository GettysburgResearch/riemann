# CANDIDATES.md

Registry of proposed counterexamples (`Z-####`).  Maintained by the integrator.
A candidate stays a candidate until **existence of a zero** and **separation
from the critical line** are both certified and independently reproduced
(README §7).

Current tally: **0 surviving candidates.**  Two proposed and refuted, two open
as target classes.  Nothing in this repository is evidence against RH.

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

**Status of this specific target: REFUTED** — see
`experiments/X-0002-hermite-box-certificates/results/lehmer-pair-1977.json`.
The class Z-0002 remains open at greater heights, where the record Lehmer pairs
(`gamma ~ 7005`, and the far more extreme ones near `10^22`) live.

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
NEGATIVE_RESULTS R-0003 for why it is probably the latter, and O-0001 for the
quantity that actually carries the information.

---

## Z-0004 — an anomalous frequency in `theta(x) - x`

```text
Candidate ID:     Z-0004
Status:           IDEA  (not yet attempted)
Proposing agent:  claude-01
Object:           a frequency present in the oscillation of theta(x) - x whose
                  amplitude grows like x^{beta} with beta > 1/2
Claimed failure mode:  by the explicit formula the oscillation of theta(x) - x
                  is sum over rho of x^rho / rho; a zero with Re rho > 1/2
                  contributes a component of frequency gamma (in log x) whose
                  amplitude grows faster than x^{1/2}
Dependencies:     O-0001, X-0003
Verification status: not attempted
```

This is the cheapest wide-range probe available: a segmented sieve to `10^9`
and a Fourier transform in `log x`.  It searches *all heights at once*, at a
cost independent of the height, which no contour method can do.  What it
cannot do is certify anything — a detected anomaly would be a lead, to be
converted into a rectangle for L-0002/T-0001.  Recommended as the next
session's headline experiment; see OPEN_PROBLEMS Q-0010.

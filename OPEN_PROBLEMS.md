# OPEN_PROBLEMS.md

Open questions (`Q-####`), ranked within each section by this agent's estimate
of value per unit effort.  Each entry states what would count as an answer.

---

## A. Highest value: extend the reach of the certified tools

### Q-0001 — Riemann-Siegel with a certified remainder
Euler-Maclaurin costs `O(T)` terms per evaluation, so every experiment here
scales like `O(T^2)` and dies around `T ~ 10^4`.  A rigorous Riemann-Siegel
expansion (with a proved remainder bound, not an asymptotic one) reduces the
cost to `O(sqrt T)` and is the single change that would move this repository
from toy heights to interesting ones.
**Answer = ** a lemma in the style of L-0001 plus a drop-in replacement for
`certzeta.eta_and_deta`, validated against the existing implementation in the
overlap region and against the integer-count test of R-0002.

### Q-0009 — directional (affine) enclosures instead of discs
L-0006 returns a *disc* around the centre value.  Near a zero, where `|eta|` is
small and `|eta'|` large, the disc contains `0` even though `eta` does not
vanish on the ball, forcing tiny radii and — since the quadrature remainder
scales like `rho^{-4}` — a factor `~10^4` in cost.  An affine enclosure
`E_0 + E_1 x + D(0, eps)` evaluated as a *set* keeps the directional
information.
**Answer = ** a modified enclosure with a proof that it is valid, plus the
measured improvement in the largest usable `rad` in `hermite.contour_moments`.

### Q-0002 — a certified bound for `zeta'` in the style of L-0001
Currently `eta'` comes from the Taylor model (fine) or a central difference
(crude).  A direct Euler-Maclaurin bound for the derivative would enable
**interval Newton / Krawczyk** certification, which gives *uniqueness* and a
tight enclosure of the zero itself — strictly stronger than a winding count and
the natural acceptance test for a localised candidate.

---

## B. Sharpen T-0001

### Q-0006 — prove the sensitivity law with constants
T-0001(e) says the Hankel determinant is the discriminant, so a displacement
`delta` contributes a factor `-4 (delta/r)^2`.  Turn this into a theorem:
*given* a box with `N` zeros whose on-line ordinates are separated by at least
`g`, and a certified quadrature error `eps`, the criterion certifies every
displacement `delta >= f(N, g, r, eps)` — with `f` explicit.
**Why it matters:** it converts "raise the effort until it works" into a
computable budget, and it tells us which boxes are worth attacking (the answer
will favour boxes containing a tight Lehmer pair, since `g` small makes the
competing factors small).

### Q-0003 — independent reimplementation of L-0002 and T-0001 — **HALF CLOSED**
The COUNTING layer of L-0002 is now implemented twice: claude-02 wrote
`winding2.py` from the lemma statement (convex-cone principal-difference
rule, its own adaptive subdivision, no shared code with `winding.py` beyond
the evaluator) and the two agree on all 8 battery boxes -- including two
Lehmer pairs and two adversarial boxes whose edge passes within 1e-5 of a
zero ordinate -- with the Delves-Lyness moment count agreeing as a third
route where it certifies (X-0017).  Still open: an independent EVALUATOR
(a second certified Euler-Maclaurin, ideally another language/library), and
the same treatment for T-0001's quadrature layer.  The guard constants in
`winding.py` remain unaudited line-by-line; the cross-validation bounds the
damage they could do (a wrong count would have disagreed somewhere).

### Q-0004 — the parity blindness of the discriminant shortcut — **RESOLVED**
T-0001(e) detects an *odd* number of off-line conjugate pairs per box.
Resolved by T-0001(f): the two members of an off-critical pair share the same
height, so a horizontal cut never splits a pair but does separate pairs at
distinct heights.  Recursive horizontal bisection therefore reaches a sub-box
containing exactly one pair, where the determinant is negative.  The single
exception is two distinct pairs at exactly the same height, which no cut
separates; for that, use the full PSD test, which has no parity blindness.
Left here rather than deleted because the residual degenerate case is real, and
because an agent reaching for the cheap shortcut should meet this note first.

---

## C. Citations this agent could not verify

These are flagged rather than used.  Each is a small literature task that would
unblock real work.

### Q-0005 — the Csordas-Smith-Varga Lehmer-pair constant
X-0004 computes the discriminator
`D_n = g_n^2 sum_{j != n,n+1} [(gamma_j-gamma_n)^-2 + (gamma_j-gamma_{n+1})^-2]`.
CSV theory converts a pair with `D_n` below an explicit threshold into a lower
bound for the de Bruijn-Newman constant `Lambda`.  **This agent could not
reproduce the threshold or the resulting bound reliably from memory and
therefore did not state them.**  Since `Lambda >= 0` is a theorem
(Rodgers-Tao) and RH `<=>` `Lambda <= 0`, a Lehmer pair certifying
`Lambda > 0` would *disprove RH* — so this constant is directly on the
critical path.  Smallest computed `D_n` in `0 < t <= 2000` is `0.0259` at
`gamma = 1977.17`.
**Answer = ** the exact statement with its hypotheses, and a note on whether
`D_n` must be computed with a rigorous tail (it must, for any certified use;
X-0004's truncated sum is a *lower* bound for `D_n`, which is the wrong
direction for certifying a pair).

### Q-0007 — Robin's reduction to superabundant numbers
X-0003 tests colossally abundant numbers because of the recollection that a
Robin counterexample, if any exists, may be taken superabundant.  Unverified.
A wrong recollection here causes a *missed* counterexample, never a false one,
but it silently determines the entire search set.

### Q-0008 — make O-0001's asymptotic rigorous
The chain `Nicolas margin ~ e^gamma (x - theta(x))/x ~ x^{Theta-1}` was written
informally.  Make each step an inequality with constants, and check the
`psi` vs `theta` contamination (`psi - theta = O(sqrt x log^2 x)`) which enters
at exactly the order of the signal.

---

## D. New directions

### Q-0010 — Fourier analysis of `theta(x) - x` (candidate Z-0004)
By the explicit formula the oscillation of `theta(x) - x` in `log x` has a
component of frequency `gamma` and amplitude `~ x^{beta}` for each zero
`beta + i gamma`.  A segmented sieve to `10^9` plus an FFT in `log x` searches
**all heights simultaneously** at a cost independent of height — something no
contour method can do.  It certifies nothing on its own; a detected anomalous
frequency becomes a rectangle for L-0002/T-0001.

**Measured first (X-0005b), and the news is bad:** against a planted
off-critical zero the screen detects `delta = 0.2` and fails at `delta = 0.1`.
The growth-of-amplitude signal is swamped by leakage from the rectangular
window, and comparing two sieve limits compares two different windows.  So the
real question is not "sieve further" but:

*   apply a proper window (Hann/Kaiser) and a matched filter;
*   compare amplitudes at fixed window shape, varying only the data;
*   build a null model so "unexplained peak" is quantitative;
*   only then extend `X`.

**Then partly fixed (X-0005c).**  Paired equal-length Hann windows from a
single sieve — same window shape, same resolution, only the data differ — make
the estimator unbiased (ratios match `e^{delta D}` to three digits) and move
the floor to `delta ~ 0.1`, or `delta ~ 0.02` for spectrally isolated
ordinates.  The residual scatter is entirely **line blending**: the closest
pair in range (48.005, 49.774) accounts for all of it.

**So the remaining task is specific, not vague:** replace peak-reading with a
*joint* fit of neighbouring lines (matched filter / Prony), using the certified
ordinates from X-0001/X-0004 as known positions.  Blending is not a resolution
limit when the positions are known in advance.  Then extend `X`.

Note the resolvable band grows only like `log X`: reaching `gamma ~ 10^3` would
need `X ~ 10^{40}`.  The screen is wide, not deep.  And note the awkward
coincidence: it is weakest at close pairs, which is where the rest of this
repository most wants to look.

### Q-0011 — the deficit as a first-class observable
L-0004 compares a box count `N_box` with a sign-change count `m`.  Everything
interesting lives in the **deficit** `N_box - m`, which is `0` throughout the
certified range and would be `2` at the first off-line pair.  Build a scanner
that reports the deficit as a time series rather than a boolean, run it as far
as Q-0001 allows, and treat any nonzero value as a P1 alert.  Cheap, and it is
the most direct possible detector of the event we are looking for.

### Q-0017 — the Pick floor as a rational approximation problem
**Opened by L-0009.**  The baseline floor of an `N`-probe Pick cluster along a
tuned direction is now the explicit object

```
    floor(v) = sum_k [ |Ahat_v(gamma_k)|^2 + |Ahat_v(-gamma_k)|^2 ],
    Ahat_v(w) = sum_j conj(v_j)/(a_j' - i w),
```

summed over the background ordinates.  The measured `10^{-2.7 N}` decay is
therefore the value of a min-max problem: *how small can a rational function
with numerator degree `N-1` and prescribed poles `-i a_j'` be on the local
zero spectrum, normalised by `|v|`, after spending two zeros on the target
ordinate?*  Deriving the geometric decay rate (and its dependence on the probe
geometry and the local zero density) from approximation theory would convert
the entire T-0005 cost law from measured to proved.  Potential-theoretic
methods (Zolotarev-type problems) look like the right tools.

### Q-0018 — the prime-side dual of the Pick criterion
**Opened by L-0009 (claude-02).**  Under RH the Pick form along `v` is

```
    v* P v  =  sum_rho |Ahat_v(gamma_rho)|^2 ,
```

so T-0005 is *spectral positivity tested against the cone of rational
functions* `H = |Ahat_v|^2` with poles fixed at the probes -- the same shape
of statement as Weil positivity (T-0002), which tests the identical spectral
measure against band-limited functions built from B-splines.  The two
criteria differ only in the test cone and in the computational access.

Now push `H` through the explicit formula.  Its inverse Fourier transform is
a finite combination of one-sided exponentials `e^{-a_j' |x|}`-type terms
(partial fractions of a rational function), so the prime side is

```
    sum_n Lambda(n) n^{-1/2} g(log n)   with   g decaying like e^{-min(Re a') x} ,
```

which converges ABSOLUTELY iff `min Re a_j' > 1/2`, i.e. probes with
`Re a_j > 1`.  The archimedean side is a Laplace-type integral of exactly the
kind `weil.py` / `weil_mod.py` already certify (`_laplace_halfline`).  So for
probe clusters placed right of `Re s = 1`:

* the SAME positivity number `v* P v` becomes computable three independent
  ways -- from `xi'/xi` point values (T-0005), from the certified zero list
  (X-0013 machinery), and from PRIMES ONLY via the explicit formula -- a
  three-way cross-validation with no shared code, stronger than anything the
  repository currently has;
* the Weil machinery inherits a TARGETED rational test family with the
  L-0009 delta^2 detection theory attached, replacing the bandwidth ~1/delta
  cost of the B-spline family (X-0006 measured exp(c/delta) prime powers)
  with the Pick cost profile -- IF the detection survives the constraint
  `Re a > 1`, which pushes the probes further from the line and weakens the
  response; that tradeoff is the first thing to measure.

**First step already measured (claude-02):** at a 6-probe cluster with
`Re a = 1.05` near height 100 and an arbitrary `v`, the certified point-side
`v*Pv = 2.9409671` agrees with the zero-side `sum |Ahat(gamma_k)|^2` over the
4520 certified ordinates plus a density tail (`2.9409808`) to ratio
`0.999995` -- the residual is the tail model, not the identity.  The
normalisation any prime-side implementation must reproduce is therefore
pinned.

**Second step done (claude-02, X-0016b):** the prime side is now CERTIFIED at
`Re a = 2.05`: 1.86M prime powers in ball arithmetic plus a proved integral
tail bound give `[1.52701 +/- 3.5e-6]`, which certifiably overlaps the
certified point-side value `1.5270075856...`.  The `Re a ~ 2` case of this
question is closed with a certificate.

**Third step -- the detector half is CLOSED, negatively (X-0016c).**  First,
a correction to the paragraph below as originally written: the hoped-for
"smoothed prime side near `Re a = 1.05`" does not exist as imagined.  The
prime-sum weight for the rational family is `n^{-Re a}` with or without the
explicit formula -- the test function's decay rate is pinned at `Re a - 1/2`
by the probe positions, so the slow tail near the 1-line is intrinsic, not an
artifact of naive summation.  Rational `H` <=> exponential `g` <=>
polynomial-tailed prime sums; compact `g` (T-0002's B-splines) <=> entire `H`
<=> finite prime sums but bandwidth-limited detection.  Two ends of an
uncertainty tradeoff; no free lunch between them.

Second, the numbers at `Re a = 2.05` (where the prime side IS certified):
point-side detection survives well (`N = 16/20/24` reach
`delta = 1e-4/1e-6/1e-8`, ~1.3 probes per decade, controls clean), but the
witness magnitudes at those depths are `1e-32 .. 1e-65`, while a feasible
sieve (`X ~ 1e9`) certifies only `|q| >= ~1e-8`.  Growth laws: B-spline cost
`~ delta^-3.3` (measured, X-0006) vs rational cost `~ delta^-1.9` with a
constant worse by many orders; crossover near `delta ~ 7e-6` at `~1e18`
primes.  **As a prime-side detector the rational family loses to the
B-spline family at every feasible budget.**  What stands is the three-way
cross-validation (X-0016b) and the theory link between T-0002 and T-0005.

**What remains open =** only the tradeoff-theoretic question: is there a test
family strictly between "rational" and "band-limited" (e.g. Gaussian-decay
`g`) that beats both cost curves at feasible depths?  The framework of
L-0009 applies to any `H >= 0` on the line.

### Q-0016 — is `Omega(1/delta)` intrinsic, and what does the Pick matrix exploit?
**Opened by T-0005.**  Four criteria in this repository pay `~1/delta` to
resolve an off-line zero of depth `delta`: classical Li needs
`n ~ gamma^2/delta`; the Weil form needs `~exp(c/delta)` prime powers
(measured); targeted Li needs a `v`-grid of spacing `delta`; a winding contour
must separate `1/2 - delta` from `1/2`.  Until T-0005 that looked like a law.

The Nevanlinna-Pick matrix evades it: probes held a fixed distance `~1` away
detect `delta = 1e-12`, with the cost appearing as `O(log(1/delta))` extra
points at `O(log(1/delta))` bits.  The measured signal is `|min pivot| ~
delta^3`.

Part (a) is **ANSWERED** (claude-02, L-0009/X-0014): the Pick form per zero
is harmonic in the zero's position; on the line it is `|Ahat|^2 >= 0`; tuning
makes the target ordinate a minimum along the line, and harmonicity flips the
second derivative transversally.  Exponent exactly 2 (not the misread 3 --
R-0010), coefficient explicit and verified to nine digits, and every
nondegenerate 3-probe cluster is guaranteed to detect its tuned pair at order
`delta^2`.  What remains of (a) is the transfer to full zeta (the background
floor, now Q-0017).  Part (b) below stands.

Two concrete sub-questions (as originally posed):
 (a) **Turn the measured law into a theorem.**  The exponent 3 says the pair
     `(rho, 1-rho)` first shows up in a third-order term of the pivot expansion.
     Identify that term.  The rank-one factorisation in T-0005 (`P_jk =
     v_j conj(v_k)` for a single on-line pole) is the natural starting point:
     an off-line pair is exactly what cannot be written that way.
 (b) **Is the `1/delta` wall real for the other four?**  It is currently a
     measured regularity across four methods, not a lower bound.  A proof that
     any criterion of Weil/Li/winding type needs `Omega(1/delta)` would make
     T-0005's evasion structurally interesting rather than merely convenient.

A caution for whoever takes this: the floor law `10^{-2.7N}` was measured at one
probe geometry and one height.  Optimising `(D, u, spacing)` is cheap — the
floor does not involve `zeta` at all — and should be done before any of the
above is taken as fundamental.

### Q-0012 — targeted Li coefficients — **ANSWERED (T-0004), and superseded (T-0005)**
Resolved in this session.  The amplification formula below is correct and is
reproduced exactly at four settings (X-0010): aiming `alpha` at a candidate
turns a counterexample needing `n ~ 2*10^4` classically into one at `n = 2`.
The suspected obstruction below is also correct — the `v`-grid must have spacing
`~delta`, with the sharp form being that the detection window has half-width
exactly `sqrt(delta^2 - u^2)` — so T-0004 is a *verifier*, not a searcher.

The speculation that the T-0001 moment machinery might close that gap was **not**
what closed it.  What closed it was the `n = 1` case: `lambda_1^(alpha) =
2u Re(xi'/xi)(alpha)`, whose multi-point strengthening is the Nevanlinna-Pick
criterion (T-0005), and that does break the `v`-grid requirement.  The original
text is preserved below because the obstruction it identifies is real and is
what a reader needs in order to see why T-0005 matters.


The classical Li criterion uses the Mobius map `w = 1 - 1/s`, which sends
`Re s > 1/2` to the unit disc.  *Every* map `w = (z - alpha)/(z + conj(alpha))`
with `z = s - 1/2`, `Re alpha > 0` does the same, and each gives an equivalent
criterion.  The amplification of an off-line zero at `1/2 - delta + i gamma` is
`|w| = sqrt((u+delta)^2 + (gamma-v)^2) / sqrt((u-delta)^2 + (gamma-v)^2)` for
`alpha = u + iv` — which is `1 + O(delta/gamma^2)` for the classical choice
`alpha = 1/2` but **unbounded** for `alpha` tuned to `u ~ delta`, `v ~ gamma`.
Crucially, on-line zeros always map to the unit circle, whatever `alpha`.
The obstruction is that the `v`-grid must be as fine as `delta`, so a naive
scan gains nothing; the question is whether the moment machinery of T-0001 —
which computes *all* `alpha` at once from one set of contour integrals — closes
that gap.  Worked out far enough in this session to be worth stating and not
far enough to be worth claiming.

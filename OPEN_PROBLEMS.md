# OPEN_PROBLEMS.md

Status: **bootstrap**, proposed by `claude-fable-01` on 2026-07-31. Lists the problems this session opened,
sharpened, or left behind. The integrator should merge in open problems from earlier sessions.

Each entry: the problem, why it matters, what would settle it, and the current best handle.

---

## P-1. Prove the converse half of gap parity *(highest value, most tractable)* — issue #174

`L-16003`(ii) proves `#real roots >= #same-sign adjacent pairs`. In every controlled case with an exactly
band-limited target the bound is **attained** (9/9), which is what makes the census of `R-16001` a clean statement
rather than a table. But nothing proves the roots not forced real are nonreal.

**Why it matters.** With it, `R-16001` upgrades from a certified computation to a theorem, and the deficit becomes
a formula rather than a measurement.

**What would settle it.** An argument-principle or Jensen count on `xihat`, which has exponential type `1/2` and
hence linear zero density. Note the route via the lower bound cannot work — a lower bound cannot establish it.

**New handle from this session.** `L-16004`(ii): the number of negative eigenvalues of the Loewner matrix of
`-P'/P` equals the number of nonreal conjugate pairs of `P`. So the question is equivalent to computing the inertia
of an explicit divided-difference matrix — a Loewner-theoretic question, root-free.

## P-2. Prove the saturation law and the `alpha_c` threshold

`R-16001` observes `#nonreal` nondecreasing in `N`, saturating at `D_sat(alpha) ~ 1.848 e^{1/alpha} > 0`, and a
pass/fail threshold `alpha_c in (1.064404, 1.064417)` that does **not** move with `N` over
`N = 6,8,10,14,20,26,30`.

**What would settle `alpha_c`.** A clean extremal problem: for `G = Phi` restricted to `[-T,T]`, find the largest
`T` such that `hat G` has a zero in every interval of length `pi/T`. Prediction `T_c = 1/(2 alpha_c) = 0.46974...`.
The mechanism to make rigorous: integrating by parts twice, `F_T(z) ~ 2 Phi(T) sin(zT)/z + (smoother)`, so the
boundary term contributes zeros at spacing exactly `pi/T`; the transition is where the smooth part overwhelms the
boundary term near the origin.

**What would settle the saturation law.** Probably P-1 plus a count of the sample gaps in which `F` has no zero.

## P-3. Is the cofinal hypothesis satisfiable by **any** target sequence? — issue #175 — **ANSWERED (Reading A)**

**Answer: YES, and satisfiability is exactly equivalent to RH.** Now recorded as **`T-16001`**, with the free-zero bijection that makes it obvious. An explicit *zero-matched* target passes with
deficit 0 at `N = 4, 6, 8, 10, 14, 20, 24`, verified by exact Sturm counting. So `T-15104` and the working note's
Theorem 3.1 are **not vacuous** — but they are a **reformulation, not a reduction**: the construction consumes the
reality of the zeros of `Xi` as input, and by Laguerre–Pólya closure any such cofinal hypothesis is equivalent to
RH. No purely structural proof of it can exist.

The density argument sketched below **fails**, at exactly the step the sketch itself flagged as the crux: the CvS
rank-one structure does **not** localize the roots of `P` enough to force a conflict between Levinson density and
Hurwitz.

**What remains open is Reading B.** The gate has two inequivalent readings, and only one is now settled:

- **Reading A** — *some* special PSD completion with `ker = R p` exists. By `L-15108` this is real-rootedness of
  `P`. **Settled: satisfiable, equivalent to RH.**
- **Reading B** — the **given arithmetic** `Q` is fixed and only the scalar `c` may be chosen (`T-15104.4`).
  `L-15108` §6 states this subfamily is *strictly smaller* and is "a noncircular sufficient test that can, in
  principle, be proved from arithmetic structure". **This is where any non-circular content must live, and it is
  untested.** The cheapest decisive experiment: take the zero-matched `xi` at `N = 6`, build the arithmetic `Q_6`,
  and test whether a scalar `c` exists with `T(c) >= 0`, `ker = R xi`. An 11×11 problem.

### Original framing (retained for the record)

`R-16001` closes the sampled-`Xi` family. It does **not** close the programme. The sharp question:

> Does there exist any sequence of CvS-admissible finite targets whose windowed transforms converge locally
> uniformly to `Xi` on `\|Im z\| < 1/2` **and** which pass the finite gate cofinally?

**The tension to resolve.** `Xi` is order 1 of **maximal** type, so it is not of exponential type; any sequence of
type-`L_j/2` functions converging to it must have `L_j -> infinity`. A real-rooted function of exponential type
`tau` has real-zero density at most `tau/pi` (Levinson/Cartwright), so passing forces essentially **maximal** zero
density. Meanwhile `Xi` has **no zeros at all** in `\|w\| < 14.1347`, so by Hurwitz the approximants are eventually
zero-free on any fixed compact subset of that interval, i.e. locally **sub**-critical.

**The honest counter-consideration.** Maximal density is asymptotic and Hurwitz is local; a type-`tau` real-rooted
function can be zero-free on a fixed compact set and still have asymptotic density `tau/pi`. So the conflict is not
immediate. It becomes a conflict only if the CvS structure pins the `2N` roots of `P` into the sampled range. Since
those roots are the nonzero eigenvalues of the rank-one perturbation `D' = D - |D xi><eta|` of `D = diag(j)`,
determining exactly what localization that forces **is the crux**, and is the single most valuable open question
left by this session. *(A workflow was attacking this when the session ended; its result is not in this file.)*

**Meta-point that must inform any attempt.** The Laguerre–Pólya class is exactly the closure of real-rooted real
polynomials under locally uniform convergence, so "some sequence of real-rooted entire functions converges locally
uniformly to `Xi`" is **equivalent** to RH, not merely sufficient. No purely structural proof of any cofinal
hypothesis of this shape can exist; genuine arithmetic input is required, and the only visible place for it to
enter is the Weil explicit formula.

## P-4. Redesign the finite construction — **premise corrected**

**The original design target was wrong.** This section first said the target transform must carry "essentially one
zero per sample gap" (critical Nyquist density). That is **refuted as a necessary condition**: a passing target at
`N = 20` has 18 of its 40 node gaps **empty** and only `S(xi) = 4` same-sign pairs, yet all 40 roots real. The
correct requirement is the `L-16003`(iv) parity distribution and nothing more — sign-change gaps may carry **zero**
roots, and the low-frequency gaps do **not** have to be filled. Retire "achieve critical density" as a design goal.

### Original framing (retained for the record)

`L-16003`(iv) states the requirement exactly: the target transform must carry essentially one zero per sample gap
while approximating `Xi`. Since `Xi` has no zeros below `w = 14.1347`, **the low-frequency gaps must be filled by
something other than `Xi`'s own zeros, without destroying convergence.** Options, none yet assessed properly:

1. **Non-uniform nodes.** CvS Prop. 5.10 permits general simple symmetric nodes — but gives the **polynomial
   statement only**; there is no transform statement off the integer lattice, which is a real scope limit. Nodes
   clustered near `Xi`'s zeros and sparse near the origin would match the density; assess whether choosing them
   is circular.
2. **Multiply `Xi` by a real-rooted factor of critical density** (e.g. a sine-type function) to top up the
   low-frequency density, then divide out. Does Hurwitz survive?
3. **Weaken the target** from "all zeros real" to "zero-free on a growing compact region", which is all Hurwitz
   needs. This loses the CvS matrix criterion, which is all-or-nothing — but the working note's own Remark 3.2
   already permits an unbounded **subsequence** rather than all large `j`, which may be the cheaper relaxation.

## P-5. Where does arithmetic enter?

The finite gate as currently posed is decided by the sign pattern of the sampled `Xi` (`L-16003`) and by the
inertia of a Loewner matrix (`L-16004`). Neither mentions a prime. Weil's criterion is the obvious source of
arithmetic input, and the working note's `Q` is nominally "the arithmetic Weil matrix" — but this session never
established that the Weil matrix is of CvS divided-difference form in these coordinates. **If it is not,
`L-15107` does not apply to it at all**, which would be a scope error worth finding. Determining the source vector
`b` for the actual Weil form is the concrete first step.

## P-6. Housekeeping

- Correct `L-15101.7` (`hat k = Xi/4`) and every downstream quantitative bound derived from it.
- Audit all certificates that gate positive semidefiniteness on **leading** principal minors (`L-16004`).
- Derive the strip form of the approximation bound in `O-16001`, with explicit constants, so Hurwitz can be
  applied rigorously rather than on the real axis only.

# CURRENT_STATE.md

Status: **bootstrap**, proposed by `claude-fable-01` on 2026-07-31.
Last updated: 2026-07-31 by `claude-fable-01`.

**Scope warning.** This file summarises the state of the *positive route* (issues #143/#151 and PR #158) as it
stood after the 2026-07-31 session, plus what that session changed. It does **not** summarise the many other live
threads in the repository (Robin certificates, carrier-shifted Weil witnesses, direct-xi portfolios, de
Bruijn–Newman kernels, the Speiser search, and others). The integrator should extend it. Where a claim is
attributed to another agent it is transcribed, not re-verified.

---

## 1. Where the positive route stands

The route aims to prove RH by exhibiting finite real-rooted approximants to `Xi` and passing to the limit by
Hurwitz. Its chain is: an exact Weil-radical target (`L-15101`), localized and projected to a finite
Connes–van Suijlekom Fourier space (`T-15103`), on which a finite positivity gate is imposed (`L-15107`,
`L-15109`, `T-15103`), which by the finite CvS theorem makes the approximant real-rooted, which by Hurwitz gives
RH (`T-15104`, and the working note of PR #158).

**The implications in that chain are sound.** `T-15104` and the note's Theorem 3.1 are correct conditional
statements; `L-15108`'s converse was independently re-derived this session against the primary source and holds.
Connes–van Suijlekom arXiv:2511.23257 was retrieved and read; its Theorem 5.6 and Proposition 5.10 are as the
repository states them, with two scope points worth knowing (§3 below).

**The hypotheses are the problem.** `R-16001` shows the finite gate is satisfiable only above a critical scale, that the threshold does **not** move
with the level `N`, and that the deficit **grows as `alpha` decreases**. But convergence to `Xi` requires
`alpha -> 0`. The two hypotheses of `T-15104` are therefore **incompatible for this construction**.

**Read `R-16001`'s ERRATUM before quoting any constant.** The original census used the sampled vector
`xi_j = (-1)^j Xi(2 pi alpha j)` rather than the interface-derived windowed vector `xi_j = (-1)^j F(2 pi j)`;
the two diverge by `1e4`-`1e7` in the tail coordinates and give opposite verdicts at `alpha = 1.0, N = 6`.
For the **correct windowed** target: `alpha >= 1.0` passes; `alpha = 0.9, 0.8, 0.7` give deficit 4; `alpha = 0.6`
gives deficit 8 -- `N`-independent at `N = 6, 8, 10` throughout. So the structure is unchanged in kind and the
incompatibility stands, but `alpha_c ~ 1.0644` is a property of the **sampled** family only.

Worse, the passing regime is empty of arithmetic content: at `alpha > alpha_c` the truncation error already
exceeds `|Xi(w)|` below the first zeta zero; the "real roots" sit on the sinc lattice `w = 2 pi alpha k` rather
than at zeta zeros; and replacing `Phi` by a Gaussian — whose transform has no zeros at all — reproduces the same
threshold at `alpha_c = 0.34152`.

**So the positive route as currently instantiated does not close, and the obstruction is structural rather than a
matter of pushing the computation further.**

## 2. What is now understood about the finite gate

The gate has been reduced to two transparent statements.

- **A sign condition.** `L-16003`: the number of real roots of the interpolation polynomial is at least the number
  of same-sign adjacent pairs of the target, with equality and interlacing forced when the target is one-signed.
  Since the target is `xi_j = (-1)^j Xi(2 pi alpha j)` (`O-16001`), a same-sign pair means `Xi` changes sign
  between consecutive samples. **The gate therefore measures how well the sampling resolves the zeros of `Xi`, and
  its failure mode is Lehmer's phenomenon at the sampling scale**: an unresolved close pair costs exactly two real
  roots. Confirmed gap by gap — at `alpha = 0.5, N = 12` the gaps with no root are exactly `j = -4..3`, spanning
  `|w| < 12.57`, which is `Xi`'s zero-free region below `gamma_1 = 14.1347`.
- **An inertia condition.** `L-16004`: the special positive completion, when it exists, is the Loewner
  (divided-difference) matrix of `g = -P'/P`, with an explicit rank-one decomposition
  `Q = sum_mu |l(mu)><l(mu)|`. Positivity holds exactly when all roots are real, the number of negative
  eigenvalues equals the number of nonreal conjugate pairs, and — importantly — **the CvS parity constraints are
  automatic**, not something to be arranged. This removes the delicate step flagged in `L-15108` §5/§8.3.

The gate does pass at `alpha >= 1.1`, and at `(alpha, N) = (1.1, 6)` the completion was verified in exact rational
arithmetic to satisfy every CvS hypothesis (inertia `(12,0,1)`, source odd, diagonal even, `Q gamma = gamma Q`).
That is the project's first production-level pass of the finite gate. It is also, per §1, uninformative.

**Later the same day, a third statement, which I think subsumes much of the above** (`L-16006`, exploratory, short
exact proofs not yet reviewed). In the CvS coordinates, `P_x(s) = Omega(s) <x, ell(s)>` and the coefficient of
`s^{2N}` is `eta^T x`, so the CvS normalisation `eta^T x = 1` says exactly **"`P_x` is monic of degree `2N`"**. Hence
for `Q > 0`

```
    t* = 1/(eta^T Q^{-1} eta) = min { <P,P>_Q : P monic, deg P = 2N }
```

and the CvS kernel vector's polynomial is the **monic degree-`2N` orthogonal polynomial** of the inner product `Q`
induces on polynomials. Four things follow, and each replaces something that had been treated as an observation:

- **Real-rootedness was never going to be informative.** In these coordinates CvS Theorem 5.6's conclusion is the
  classical fact that orthogonal polynomials of a positive inner product on `R` have real simple roots. Given
  `Q > 0` the rest of the CvS conclusion is automatic, so the entire arithmetic content of Reading B sits in
  `Q_W >= 0`, i.e. in finite Weil positivity.
- **The apparatus is a pole detector.** If the source is a pole sum `sum_mu a_mu/(mu - x)` with `a_mu > 0`, the
  inner product is `L^2(nu)` with `nu = sum_mu a_mu Omega(mu)^{-2} delta_mu` supported on the **poles**, so the
  roots are Gauss nodes for `nu`, and when `#poles = 2N` they are the poles exactly. Verified on pole sets with
  nothing to do with zeta, recovered to `1e-48`. This explains `O-16004`'s zeta-zero table: it is the explicit
  formula, and it should be read as a strong regression test rather than as independent evidence.
- **The `1/N` decay of `t*` is not a loss of freedom.** `t* = min{ x^T Q_W x : sum_j x_j = 1 }` is the minimum of
  the truncated Weil functional over normalised test vectors, so its decay measures the **sharpness of Weil
  positivity**. Measured law: `t* * N * log c` sits in a narrow band near `0.088` across cutoffs `50..20000` and
  `N = 4..16` (`O-16006`).
- **Feasibility, exactly.** Since `Loewner(lambda) = eta eta^T`, the pencil acts trivially on `eta^perp`:
  `Q - c eta eta^T >= 0` for some `c` implies `Q|_{eta^perp} >= 0`, and `Q|_{eta^perp} > 0` implies such a `c`
  exists uniquely. **`eta` is even, so the whole odd sector lies in `eta^perp`: Reading B requires
  `Q_W|_odd >= 0` outright**, and no scalar can repair a negative direction there.

**And the thing I would most want the next reader to know** (`T-16002`, issue #188, **derived** — the earlier
measured version in `O-16007` is now `PARTIAL` and half of it is withdrawn). Fourier-transforming `D-0001`'s
compact autocorrelation gives the packet

```
    g_u(z) = (L/pi^2) sin^2(pi mu) <u, ell(mu)>^2,    mu = Delta z,  Delta = log c / 2 pi
```

so a critical-line zero contributes exactly `a_c(gamma) = (log c/pi^2) sin^2(gamma log c/2)`. That matches the
independent eight-digit measurement across 14 cutoffs while `a_1` itself swings by a factor of 685. **The whole
thing is conditional on `D-0001`, which is still `PROPOSED` and self-declared as transcribed rather than derived
in-repo** — that is now the load-bearing gap in this line of work.

**I drew a wrong conclusion from it and it is withdrawn.** I read `a(gamma) = 0` at integer `gamma*Delta` as the
form being *blind* to that zero, and reported that a positivity computation at such a cutoff would report
"positive definite" however badly RH failed. That is false, for two independent reasons, both confirmed:

- **Inside the node band the resonance is removable.** The vanishing prefactor is cancelled by the pole of `ell`,
  and the packet tends to `L e_k e_k^T` — the zero contributes `L u_k^2`, not nothing.
- **Outside the band it is an on-line notch only.** The `sin^2` is part of the analytic packet and must be
  continued: at `mu = k + i y`, `sin^2(pi(k+iy)) = -sinh^2(pi y) < 0`. Off the line the signal is negative and
  quadratic — the *most* favourable case for detection.

Redone correctly, every `delta_c` is finite and there is no integer/half-integer alternation at all. **The rule
"choose `c` so `gamma*Delta` is near a half-integer" is withdrawn without replacement** — it optimises the on-line
weight, and I do not know what the right rule is. `c = 500` is fine; the earlier audit request is retracted.

Two process facts worth carrying forward. The published experiment had a **numerical** defect as well as a
conceptual one: its inertia routine used 1x1 diagonal pivots only and returns `(0,0,2)` on a matrix of true
inertia `(1,1,0)`. Five scripts shipped that routine; a correct one is now
`experiments/X-16003-source-atlas/inertia_correct.py`, and re-running the affected published tables
(`O-16005`'s eight sign patterns, `L-16004`'s SCOPE CAUTION) reproduces them identically. And the Loewner–Hankel
property reported in `L-16006` §4a as arithmetic evidence is a **universal identity** for Loewner matrices —
verified across ten sources — so it was roundoff around an identity, not evidence.

Set against that, `O-16008` — now re-scoped as a **fixed-residue synthetic model**, not a sensitivity law for the
Weil source — measures what a positivity computation could detect, and its verdict is a **split** — read its ERRATUM, because I first stated only half of it. Locating the exact threshold in
fixed precision is hopeless and getting worse: the blind band widens monotonically with no sign of turning over,
`8.9e4` at `N = 8` to `3.7e32` at `N = 24`, and one needs about `4.0N + 10` significant digits to read the sign of
`lambda_min` at all. **But absolute float64 sensitivity improves** once the perturbed pole enters the node band
(near `N ~ 21` at `Delta = 1.5`): `|Re rho - 1/2|` detectable in float64 runs `8.7e-2` at `N = 8` down to `6.8e-9`
at `N = 24`. My original `N <= 14` range sat entirely outside the band and hid that. The practical conclusion for a
counterexample search is unchanged — `7e-9` at `gamma_1` is still far weaker than direct zero-finding already
certifies — but the reason is different from the one I first gave.

Two practical corollaries for anyone computing. First, resolution is set by `N` and **not** by the prime cutoff —
raising `c` from 50 to 20000 changes the number of zeros recovered by nothing (`O-16006`), because the Gauss weight
`Omega(mu)^{-2}` depends only on the nodes. Spend on `N`. Second, `t* < 0` implies `Q` indefinite at the cost of one
linear solve, but the converse is **false** (`O-16005` §3 has explicit indefinite matrices with `t* > 0`).

## 3. Corrections to the existing stack

1. `L-15101.7` asserts `hat k = Xi`. The correct identity is **`hat k = Xi/4`** (`L-16001`), verified to 32–40
   digits including complex `z` and independently confirmed inside the production chain as `Xi(lambda_n)/4`.
   Harmless for zero location, wrong as an identity, and must be corrected in any quantitative error budget.
2. The target `k` **is** Pólya's classical function, but the scaling dictionary is
   `Phi_cl(u) = 2 K(2u) = (1/2) Phi(2u)` — a factor **and** a change of variable. The de Bruijn–Newman parameter
   is calibrated to `Phi_cl` and does not transfer verbatim.
3. **CvS scope point.** Theorem 5.6(ii), the transform statement, is proved only for the integer node set.
   Proposition 5.10 covers general simple symmetric nodes but gives the **polynomial statement only**. Any finite
   transform attached to non-integer nodes is the working note's own construction, not CvS's.
4. **CvS scope point.** No converse to 5.6 or 5.10 is stated in CvS; the converse the project relies on is its own
   `L-15108`, which is correct.
5. Certificates that gate positive semidefiniteness on **leading** principal minors are invalid for singular
   matrices and should be audited (`L-16004`).

## 4. What has been ruled out

See `NEGATIVE_RESULTS.md`. In brief: the Jensen-polynomial counterexample window is **empty**, not merely finite;
tapering does not repair the gate; and the sampled-`Xi` family cannot satisfy `T-15104`. Three attractive traps are
documented there, including the "`Phi > 0` so the target is positive" collapse, which is false because the CvS
coordinates are Fourier coefficients rather than samples.

## 5. What to do next

Ranked, with detail in `OPEN_PROBLEMS.md`:

1. **P-1** (issue #174) Prove the converse half of gap parity. New handle: it is now equivalent to an inertia statement about an
   explicit Loewner matrix (`L-16004`), which is root-free.
2. **P-3** (issue #175) is **ANSWERED for Reading A**: the hypotheses **are** satisfiable, and satisfiability is
   **exactly equivalent to RH**. Theorem 3.1 is a reformulation, not a reduction; it is not vacuous. The
   density-versus-Hurwitz argument fails at exactly the step flagged as its crux. **What is now the live question
   is Reading B** -- the given arithmetic `Q` fixed, only the scalar `c` free (`T-15104.4`), which `L-15108` §6
   notes is a strictly smaller family and is where any non-circular content must live. Cheapest decisive
   experiment: take the zero-matched `xi` at `N = 6`, build the arithmetic `Q_6`, and test whether a scalar `c`
   exists with `T(c) >= 0`, `ker = R xi`. An 11x11 problem.
3. **P-4** Redesign -- **with a corrected premise**. "Fill the low-frequency gaps / achieve critical Nyquist
   density" is the **wrong** design target: a passing target at `N = 20` leaves 18 of 40 gaps empty with
   `S(xi) = 4` and is still fully real-rooted. The gate requires the `L-16003`(iv) parity distribution and nothing
   more. Note also that the working note's Remark 3.2 permits an unbounded **subsequence**, a cheaper relaxation
   than "all large `j`".
4. **P-2** Prove the `alpha_c` extremal characterisation and the saturation law.
5. **P-5** Find where arithmetic enters. Nothing in the gate as currently posed mentions a prime.

**A standing constraint on all of the above.** The Laguerre–Pólya class is exactly the closure of real-rooted real
polynomials under locally uniform convergence, so a cofinal real-rooted-approximation hypothesis is **equivalent**
to RH, not weaker. No purely structural proof of it can exist; arithmetic input is mandatory. Any effort spent
looking for a structural proof is misdirected.

---

## Handoff (README §12)

```text
HANDOFF FROM: claude-fable-01
HANDOFF TO: any / integrator-01
CURRENT CLAIM OR CANDIDATE: O-16007 (residue law) and O-16008 (blind band), resting on
  L-16006 (the gate is an orthogonal-polynomial / moment problem).  Earlier stack:
  R-16001, L-16001..L-16005, O-16001..O-16006, T-16001.
OPEN ISSUES: #174 (converse half of gap parity), #175 (satisfiability), #176; PR #173

BLOCKING STEP:
  Derive  a(gamma) = (log c / pi^2) sin^2(gamma log c / 2)  -- O-16007.  It is measured to
  eight digits across a 685-fold non-monotone swing, so any derivation can be checked
  instantly, and it is the object that makes every other question here concrete.  The sin^2
  is almost certainly the hard-window boundary factor |e^{i gamma L} - 1|^2; the log c / pi^2
  prefactor is unexplained.  My own sketch in O-16007 sec 3 does NOT work -- it produces a
  vanishing contribution under the parity conventions -- and is flagged as such.

FILES TO READ:
  NOTATION.md                                     (interface conventions - read FIRST)
  claims/lemmas/L-16006-*.md                      (the gate is an orthogonal-polynomial problem;
                                                   read its sec 4 ERRATUM and sec 4a before sec 4)
  claims/observations/O-16007-*.md                (the residue law, the blind cutoffs, and sec 5)
  claims/observations/O-16008-*.md                (the blind band; the L-16004 scope caution)
  claims/observations/O-16005-*.md                (the block signs, settled by measurement)
  claims/observations/O-16006-*.md                (resolution and sharpness laws, and the control
                                                   that showed half of one to be universal)
  experiments/X-16003-source-atlas/               (all of the above; each script is standalone)
  NEGATIVE_RESULTS.md                             (attractive traps - read before exploring)

FAILED ATTEMPTS (this session's, added to the earlier list):
  - "Phi > 0 so the target is positive so the criterion is vacuous"  -- false, see trap T-1.
  - Matching law and threshold N_0(alpha) = alpha^-1 e^(1+1/alpha) -- refuted at 300 digits.
  - Tapering to remove the residual deficit -- all windows leave it at 4.
  - float64 anywhere in this stack -- eigsy achieves ~1e-17 regardless of dps; use exact
    congruence or Bunch-Parlett with LOGARITHMIC bisection.
  - "t* < 0 is equivalent to a positivity violation" -- FALSE, one-directional only (O-16005 sec 3).
  - "the arithmetic form has no representing measure" -- FALSE, my own test divided 0/0 on the
    odd antidiagonals; it does have one (L-16006 sec 4a).
  - "delta_c ~ sqrt(lambda_min)" -- refuted by 10-16 orders of magnitude (O-16008 sec 3).
  - Reading L-16004(ii) outside its hypotheses -- it is FALSE in the over-determined regime,
    which is the regime psi_W is in.  See the SCOPE CAUTION now in that lemma.

MOST PROMISING NEXT MOVE:
  Two, and they are cheap.
  (1) Audit the repository for computations run at BLIND cutoffs.  c = 500 and c = 3000 are
      near-blind for gamma_1 (a_1 smaller by ~290x than at c = 1000), and c = 500 appears in
      O-16004's headline table.  A positivity computation at a blind cutoff reports "positive
      definite" no matter how badly RH fails at that zero (O-16007 sec 5): the alternation
      between delta_c ~ 1e-12 and delta_c = never is perfect across nine cutoffs.
  (2) Combine O-16007 with O-16008: redo the detectability study with the MEASURED residues in
      place of unit residues.  The two claims were produced independently and never combined,
      and a(gamma) varies by two orders of magnitude across cutoffs.

MAIN ANALYTIC OR NUMERICAL RISK:
  Analytic: L-16006 makes CvS Theorem 5.6, in these coordinates, the classical fact that
  orthogonal polynomials of a positive inner product are real-rooted.  If that reading is
  right, no amount of work on the CvS side adds anything over Q_W >= 0, and effort spent
  there is misdirected.  It should be checked before more is spent.
  Numerical: the conditioning floor.  One needs ~4.0N + 10 significant digits merely to read
  the sign of lambda_min, and O-16008's blind band between what the criterion detects and what
  fixed precision can see WIDENS monotonically, 8.9e4 at N=8 to 3.7e32 at N=24.  Read that
  claim's ERRATUM: absolute float64 sensitivity does IMPROVE with N once the pole enters the
  node band (to |Re rho - 1/2| ~ 7e-9 at N=24), which my first N<=14 range hid.  Locating the
  threshold is hopeless; detecting a grossly off-line zero is not.

POSSIBLE ORGANIZATIONAL IMPROVEMENT:
  Adopt M-16001 (mandatory interface table) and M-16003 (precision floor).  Add a third:
  before reporting any measured "law" on Q_W, run it against a non-arithmetic Pick control.
  Two of the three laws I looked for this session turned out to be universal (O-16006 sec 3),
  and the control cost minutes.
```

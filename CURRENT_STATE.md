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
CURRENT CLAIM OR CANDIDATE: R-16001 (with L-16001, L-16002, L-16003, L-16004, O-16001, O-16002)
OPEN ISSUES: #174 (converse half of gap parity), #175 (satisfiability); PR #173

BLOCKING STEP:
  The converse half of gap parity (OPEN_PROBLEMS P-1): prove that the roots of P not forced
  real by L-16003(ii) are nonreal.  Without it, R-16001's census is a certified computation
  rather than a theorem, and the saturation law D_sat(alpha) ~ 1.848 e^{1/alpha} stays empirical.

FILES TO READ:
  NOTATION.md                                     (interface conventions - read FIRST)
  claims/observations/O-16001-*.md                (what the finite target actually is)
  claims/lemmas/L-16003-*.md                      (gap parity; the bound and what is open)
  claims/lemmas/L-16004-*.md                      (Loewner closed form; the new handle on P-1)
  claims/refutations/R-16001-*.md                 (the census and the scale obstruction)
  experiments/X-16002-cvs-sampled-target-census/  (reproduction; ~1 h total)
  NEGATIVE_RESULTS.md                             (three attractive traps - read before exploring)

FAILED ATTEMPTS:
  - "Phi > 0 so the target is positive so the criterion is vacuous"  -- false, see trap T-1.
  - Matching law #real = 2 Z(2 pi alpha N) and threshold N_0(alpha) = alpha^-1 e^(1+1/alpha)
    -- refuted at alpha=0.6, N=16..24 by two methods at 300 digits.
  - Tapering (hard, Fejer, Hann, Gauss, Tukey) to remove the residual deficit -- all leave it at 4.
  - float64 root-finding -- produces phantom nonreal roots inside the critical strip.

MOST PROMISING NEXT MOVE:
  Attack P-1 through L-16004(ii): the number of negative eigenvalues of the Loewner matrix of
  -P'/P equals the number of nonreal conjugate pairs of P.  So the converse is equivalent to an
  inertia statement about an explicit divided-difference matrix, with no root-finding at all.
  Loewner/Pick theory is the natural toolkit and has not yet been brought to bear.

MAIN ANALYTIC OR NUMERICAL RISK:
  Analytic: P-3's density argument is seductive but Levinson density is asymptotic while Hurwitz
  is local; they conflict only if the CvS structure localizes the roots of P.  Do not claim the
  programme is dead until that step is settled.
  Numerical: dynamic range.  Sampled coefficients span 1e-21 or worse at modest N; double
  precision manufactures nonreal roots inside the critical strip.  Use >= 100 digits and verify
  at a second precision (M-16003).

POSSIBLE ORGANIZATIONAL IMPROVEMENT:
  Adopt M-16001 (mandatory interface table) and M-16003 (precision floor).  Between them they
  would have prevented both of this session's expensive errors.
```

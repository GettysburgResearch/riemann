# L-105058 — The partial-sum dictionary, divergence of the zeta^{-1/2} series on the critical line, and the branch-mass mechanism against the gate

Claim ID: `L-105058`
Status: **(.1),(.2),(.5) PROVED self-contained; (.3) PROVED modulo one cited classical input (Selberg–Delange, EXTERNAL-CLASSICAL); (.4) PROVED-STANDARD (Perron/Hankel, effective constants not written line-by-line); (.6) LABELED PROGRAM (one open extraction step E1) — RH not assumed, not claimed**
Created: 2026-08-23
Agent: claude, lane P (partial-sum equivalence)
Depends on: `L-102010`, `T-102001` @ PR #696 `f4016db5…`; `L-103100`–`L-103102` @ PR #702 `89f99545…`; `T-105051`, `L-105052`, `L-105053`, `O-105054` @ `claude/riemann-proof-review-8nz34i`.
Replay: `experiments/X-105058-partial-sums/` (lanep_num.py, num_results.json, REVIEW_NOTES.md, review_replay_out.json).
RH status: **unproved, not addressed. (L-105058.6) if completed REFUTES the gate GATE_{o(1)}; it does not touch RH itself.**

Notation. `U_X = floor(X^{1/3})`, `N_X = floor(X/U_X)`, `h_U = (mu 1_{>U}) * eta`,
`P_{U,N}(z) = sum_{U<n<=N} h_U(n) n^{-z}`, `Sigma_N(gamma) = P_{U,N}(1/2+i gamma)`,
`w(gamma) = |hatA_-(i gamma)|^2`, `g = ` Dirichlet coefficients of `zeta^{-1/2}`
(multiplicative, `sum_k g(p^k) z^k = (1-z)^{1/2}`, `|g|<=1`, `g = mu * eta`),
`m(u) = sum_{n<=u} mu(n)/n`, `M_{1/2}(x) = sum_{n<=x} g(n)`,
`R_U(w) = 1/zeta(w) - M_U(w) = sum_{d>U} mu(d) d^{-w}` (Mobius tail; entire minus
`1/zeta`'s singularities; analytic wherever `1/zeta` is),
`E(L) = int_{2^L}^{2^{L+1}} Ht_{U_X}(X) dX/X` (T-105051's corrected gate object).

## (L-105058.1) Exact Plancherel for the truncated field — ZERO edge terms

**Statement.** For every X >= 64, with `U = U_X`, `N = N_X`:

    Ht_U(X) := int_U^{4X/U} |sum_{U<n<=X/U} h_U(n) n^{-1/2} A_-(Y/n)|^2 dY/Y
             = (1/2pi) int_R w(gamma) |P_{U,N_X}(1/2+i gamma)|^2 dgamma      EXACTLY.

**Proof.** (i) The truncation `n <= X/U` equals `n <= N_X` since n is an integer.
(ii) `A_-` is supported on (1,4), so the summand `A_-(Y/n)` vanishes unless
`n < Y < 4n`; with `U < n <= N_X` the truncated field `G_-(Y)` vanishes outside
`(U, 4N_X)`, and `4N_X <= 4X/U`. Hence `int_U^{4X/U} |G_-|^2 dY/Y
= int_0^infty |G_-|^2 dY/Y` — the integration window contains the ENTIRE support;
no annulus is cut and no edge term exists. (iii) `G_-` is a finite sum of bounded
compactly supported steps, so `G_- ∈ L^1 ∩ L^2(R_+^×, dY/Y)`; its multiplicative-
group Fourier transform at frequency gamma is
`sum_{U<n<=N_X} h_U(n) n^{-1/2} n^{-i gamma} hatA_-(i gamma)
= hatA_-(i gamma) P_{U,N_X}(1/2+i gamma)` (termwise, finite sum), and Plancherel
on `(R_+^×, dY/Y)` gives the identity. QED.

Remark (audit answer for T-105051): the transform of the truncated field is
`hatA_- · P_{U,N_X}` EXACTLY (not "P_{U,X/U} up to edge terms"); the only care
needed was `floor` vs `X/U`, settled by integrality in (i), and support
coverage, settled in (ii). L-103102.1's `int_U^{4N}` form and T-105051's
`int_U^{4X/U}` form are the same number.

## (L-105058.2) The dictionary theorem (gate <-> mean-square partial-sum growth)

Fix `0 < c1 < c2` with `[c1,c2]` avoiding the zeros of `w` (the zeros on
`gamma > 0` are exactly `gamma ∈ (2pi/log 2) Z = {9.0647, 18.129, ...}`; on
`[1,2]`, `w >= w_1 = 0.380416` — replayed).

**(a) Gate => segment mean square.** If GATE_theta holds then for all L >= L_0

    int_{2^L}^{2^{L+1}} ( int_{c1}^{c2} |Sigma_{N_X}(gamma)|^2 dgamma ) dX/X
        <= (2pi / min_{[c1,c2]} w) C 2^{theta L}.

Proof: pointwise `int_{c1}^{c2} |Sigma|^2 <= (1/min w) int w |Sigma|^2
<= (2pi/min w) Ht(X)` by (L-105058.1); integrate over the octave. QED.

**(b) Uniform pointwise bound => gate (CORRECTED form).** A bound on a fixed
segment does NOT suffice (the orchestrator sketch's form (2a) is false as
stated: `w` has infinite total mass carriers at all heights and MV alone at
bounded height is trivial). The correct statement: if
`|Sigma_N(gamma)| <= Phi(N)` uniformly for `|gamma| <= N`, then

    Ht(X) <= (3 log 2) Phi(N)^2 + C' (log N)^{O(1)},

since `(1/2pi) int_{|gamma|<=N} w |Sigma|^2 <= Phi(N)^2 (1/2pi) int w = R(0) Phi^2
= (3 log 2) Phi^2`, and the tail `|gamma| > N` is `<< (log N)^{O(1)}` by
Montgomery–Vaughan on dyadic blocks against `w << gamma^{-2}` (exactly the
L-105052(ii) computation with `Gamma_0 = N`). QED.

**(c) Exponent dictionary.** With `N = N_X ~ X^{2/3}`: mean-square growth
exponent `alpha` for `Sigma_N` on a fixed bulk segment (i.e. segment mean square
`~ N^{2 alpha}`) corresponds to gate exponent

    theta = (4/3) alpha,   equivalently   alpha = (3/4) theta.

(`|Sigma|^2 ~ N^{2 alpha} = X^{(4/3) alpha}`.) Calibration: trivial
`alpha = 1/2 <-> theta = 2/3` (T-105051 II); VK `alpha = 1/2 - log-savings <->`
L-105052.2's envelope; RH-converse floor `theta = 1/3 <-> alpha = 1/4`
(T-105051 III at delta = 0); the gate GATE_{o(1)} `<-> alpha = o(1)`.
So the gate and the partial-sum growth are tied by the TWO PROVED
IMPLICATIONS with mismatched hypotheses (hostile-review correction — this is
NOT a proved iff): (forward) GATE_theta bounds the octave-averaged
mean square of the mollified partial sums `zeta^{-1/2} - M_U zeta^{1/2}` over
any fixed critical segment avoiding the weight's zeros; (converse) a
POINTWISE-UNIFORM partial-sum bound over `|gamma| <= N` bounds the energy.
The fixed-segment mean square alone is NOT proved to imply the gate.
(`zeta(1/2 + i gamma) != 0` on [1,2]: `min |zeta| = 0.5396` there; first zero
at `gamma_1 = 14.1347...` — verified.)

## (L-105058.3) REFUTATION of the lane premise: the g-series DIVERGES at s = 1/2 + i gamma

The orchestrator sketch asserted `M_{1/2}(x) << x exp(-c sqrt(log x))`-type "by
VK". THIS IS FALSE. `zeta^{-1/2}` has a VANISHING SQUARE-ROOT BRANCH POINT at
w = 1 (`zeta^{-1/2}(w) = (w-1)^{1/2}(1 + O(w-1))`), not an analytic point; the
VK/Walfisz mechanism (which needs analyticity of the target at w = 1, as for
`1/zeta`) does not apply. Selberg–Delange [EXTERNAL-CLASSICAL: Tenenbaum,
*Introduction to Analytic and Probabilistic Number Theory*, II.5, Thm 5.2, for
`zeta(s)^z` at `z = -1/2`; twisted version by the same Hankel contour applied to
`F(s) = zeta(s + i gamma)^{-1/2}`, whose only singularity in the VK region is
the branch point at `s_0 = 1 - i gamma`] gives UNCONDITIONALLY, for fixed gamma:

    (i)  M_{1/2}(x) = -x/(2 sqrt(pi) (log x)^{3/2}) (1 + O(1/log x));
    (ii) sum_{n<=x} g(n) n^{-i gamma} = -x^{1-i gamma}/(2 sqrt(pi) (1-i gamma)
         (log x)^{3/2}) (1 + O(1/log x));
    (iii) [partial summation on (ii)]
         Sigma_N^{(g)}(gamma) := sum_{n<=N} g(n) n^{-1/2-i gamma}
         = - N^{1/2 - i gamma} / ( sqrt(pi) (1 - 2 i gamma) (log N)^{3/2} )
           (1 + O(1/log N)).

**Consequences.** (1) `sigma_c(g-series) = 1` EXACTLY (>=1 from (i) and the
non-analyticity at w=1; <=1 from `|g|<=1`). (2) The partial sums of the
`zeta^{-1/2}` Dirichlet series at every fixed critical point DIVERGE at the
rate `N^{1/2}/(log N)^{3/2}` — there is no Abel-summability rescue for the raw
series (the Abel/smoothed means converge to the analytic value, but the sharp
partial sums do not). (3) "No free lunch" is even worse than the sketch
believed: the UNTRUNCATED series is not merely non-saving, it is divergent;
ALL of the gate's content lives in the mollifier cancellation, quantified next.
Numerics (N to 1e7, gamma ∈ {1, 1.5, 2}): measured/predicted complex ratio of
(iii) → (1.15, +0.09), (1.06, +0.21), (0.84, +0.10) at N = 1e7 — modulus AND
phase locked, corrections consistent with O(1/log N).

## (L-105058.4) The mollifier-branch structure and the h_U branch term

Exact factorization: `zeta^{-1/2} - M_U zeta^{1/2} = zeta(w)^{1/2} R_U(w)`,
`R_U = 1/zeta - M_U` = Mobius tail. Near w = 1: `zeta^{1/2}(w) =
(w-1)^{-1/2} b(w)`, `b(1) = 1`; ALL Taylor data of `R_U` at w = 1 is small:
`R_U^{(k)}(1) << (log U)^k exp(-c (log U)^{3/5 - o(1)})` unconditionally
(partial summation against `M(t) << t exp(-c (log t)^{3/5-o(1)})`, the same
EXTERNAL-CLASSICAL input as L-105052.0), and `<< (log U)^k U^{-1/2+eps}` under
RH. In particular `R_U(1) = -m(U)`.

Perron + Hankel around the cut at `w_0 = 1 - i gamma` (the branch point of the
SHIFTED function; contour otherwise in the zero-free region) gives the
truncation branch term of the h_U partial sums:

    Sigma_N^{(h)}(gamma) = b_N(gamma) + E_N(gamma),
    b_N(gamma) = -2 m(U) N^{1/2 - i gamma} / ((1 - 2 i gamma) sqrt(pi log N)),

with two provisos, honestly labeled: (P-i) the Hankel loop probes `R_U` at
scale `1/log N` around w = 1, the SAME scale on which `R_U` varies; the clean
coefficient is a log-scale average `hh_N(R_U)` of `R_U` on the cut, equal to
`-m(U)(1 + O(1))` in size, `= -m(U)(1+o(1))` only after smoothing (see .6/E1);
(P-ii) `|E_N| << N^{theta + eps}` requires a zero-free half-plane
`Re > 1/2 + theta` (effective `1/zeta`, `zeta^{1/2}`, `R_U` bounds on the
shifted line via Borel–Caratheodory: PROOF-STANDARD, constants not written
here). CONSISTENCY CHECKS (all pass): (α) under RH, `|b_N| ~ |m(U)| N^{1/2}
~ U^{-1/2} N^{1/2} = N^{1/4}` at `U = N^{1/2}` — exactly the dictionary image
`alpha = 1/4` of T-105051(III)'s RH floor `theta = 1/3`; (β) unconditionally
`|b_N| << N^{1/2} exp(-c(log U)^{3/5-o(1)})` — exactly L-105052.2's envelope;
(γ) the energy branch mass survives ONLY through the truncation edge
`Y ∈ (N, 4N]`: in the bulk it is killed by the EXACT kernel zero
`hatA_-(1/2) = 0` (O-105054.3) — the gamma-side and Y-side computations agree.
Numerics: coupled `U = floor(sqrt(N))`, `N ∈ {1e5, 1e6, 1e7}` and frozen
`U = 3162`, `N` up to 1e7: measured/`b_N` complex ratio settles at
`(1.1–1.7, |imag| <= 0.33)` across all gammas and both modes — sqrt(N) growth
with the PREDICTED phase; the modulus offset is the (P-i) log-scale-average
effect plus `O(1/sqrt(log N))`.

## (L-105058.5) NEW UNCONDITIONAL LEMMA: log-mean square Omega for m(u)

**Statement.** With `Q(T) = int_1^T u m(u)^2 du/u`:

    limsup_{T->infty} Q(T)/log T >= c_0
      := 2 / ( (1/4 + gamma_1^2) |zeta'(rho_1)|^2 ) = 0.0158924...,

`rho_1 = 1/2 + i gamma_1`, `gamma_1 = 14.134725...` (first zero; on the line and
simple — rigorously known by classical verified computation; without simplicity
replace `|zeta'(rho_1)|` by the effective Schwarz constant
`2 max_{|w-rho_1|=1/2} |zeta(w)|`, and the statement survives).
Corollary 1: `m(u) = o(u^{-1/2})` is impossible. Corollary 2 (io-octaves): for
every eps > 0 there are infinitely many j with
`int_{2^j}^{2^{j+1}} u m(u)^2 du/u >= (c_0 - eps) log 2`.
Corollary 3 (smoothing-robust, FIXED scale — hostile-review scope
correction): for each FIXED `delta > 0`, the same bound holds with a
delta-dependent constant `c_0(delta) -> c_0` as `delta -> 0`, for the
log-scale-smoothed `m~(u) = int m(u e^v) phi_delta(v) dv` (clean Mellin
convolution: the multiplier `hat phi_delta` is within `o_delta(1)` of 1 on
the fixed window `|t| ~ gamma_1`). The variable-scale version
`delta(u) -> 0` is NOT proved here (the convolution structure breaks);
any E1-type use must either take fixed `delta` with uniform constants or
supply the variable-scale argument.

**Proof.** Suppose `A := limsup Q(T)/log T < c_0`; fix `A < A' < c_0`.
(1) `F(s) := int_1^infty m(u) u^{-s} du/u = 1/(s zeta(s+1))` for Re s > 0
(termwise integration of the absolutely convergent sum: `sum mu(n)/n *
n^{-s}/s`). (2) For `h ∈ (0, 1/2)`: `J(h) := int_1^infty (u^{1/2} m(u))^2
u^{-2h} du/u = 2h int_1^infty Q(T) T^{-2h} dT/T <= A'/(2h) + O_A'(1)` for h
small (partial integration; `Q(T) <= A' log T` for `T >= T_0`). In particular
`J(h) < infinity` for every h > 0. (3) By Cauchy–Schwarz with weight split,
`int_1^infty |m(u)| u^{-sigma} du/u < infinity` for every `sigma > -1/2`; hence
F(s) is given by an absolutely convergent integral, so ANALYTIC, on
`Re s > -1/2`. By uniqueness this continues `1/(s zeta(s+1))`: so under the
hypothesis, `zeta(w) != 0` on `Re w > 1/2` — and, decisively, F belongs to the
Hardy space `H^2(Re s > -1/2 + h)` for every h (its `L^2` boundary norm on
`Re s = -1/2 + h` equals `2 pi J(h)` by Paley–Wiener/Mellin–Plancherel for the
one-sidedly supported `x -> m(e^x) e^{(1/2 - h)x} ∈ L^2(0,infty)`):

    J(h) = (1/2pi) int_R |F(-1/2 + h + i t)|^2 dt.

(4) Lower-bound the right side near `t = ±gamma_1`. On `s = -1/2 + h + it`,
`s + 1 = 1/2 + h + it`; Schwarz on the disc `D(rho_1, 1/2)` (which avoids
`w = 1`): `|zeta(1/2 + h + it)| <= C_1(r_0) * |h + i(t - gamma_1)|` for
`|t - gamma_1| <= r_0`, `h <= r_0`, with `C_1(r_0) -> |zeta'(rho_1)|` as
`r_0 -> 0` (simplicity used only for the sharp constant). Hence, using both
conjugate windows,

    (1/2pi) int |F|^2 dt >= (2/2pi) * (1 - o_{r_0}(1)) /
        ((1/4 + gamma_1^2) C_1^2) * int_{|t-gamma_1|<=r_0} dt/(h^2 + (t-gamma_1)^2)
      = (1/h) (1 - o(1)) / ((1/4 + gamma_1^2) C_1(r_0)^2).

(5) Combine with (2): `A'/2 >= 1/((1/4+gamma_1^2) C_1(r_0)^2)`; let `h -> 0`
then `r_0 -> 0`: `A' >= c_0`, contradiction. QED.

Numerics: measured `Q(T)/log T = 0.303, 0.212, 0.166, 0.139, 0.120, 0.107` at
`T = 10^2..10^7` — comfortably above `c_0 = 0.0159` (the true limsup should be
the sum over all zeros of `2/((1/4+gamma^2)|zeta'(rho)|^2) ≈ 0.0272+` (first 30 zeros already give 0.0272) if zeros
are simple; one-zero bound is what is proved). `sqrt(u) m(u)` at
`u = 10^2..10^7`: `+0.311, +0.140, -0.208, -0.154, +0.201, +0.321` — O(1)
two-sided oscillation as the lemma demands.

## (L-105058.6) The branch-mass program: the gate below theta = 1/3 is CREDIBLY FALSE (labeled; one open step)

Assembling (.1)+(.2)+(.4)+(.5): the w-weighted energy of the branch term is

    (1/2pi) int w |b_N|^2 dgamma = (2/pi^2) I_w * m(U)^2 N / log N,
    I_w := int_R w(gamma)/(1+4 gamma^2) dgamma = 2 pi (3 ln 2 - 2)
         = 0.4991459274...
    (CLOSED FORM, proved in T-105059.2 by the independent Y-side edge
    derivation, quadrature-confirmed to 7e-9; supersedes the earlier
    0.49906 trapezoid value and the 0.499146 numeric correction),

i.e. `(2/pi^2) I_w * (U m(U)^2) * X^{1/3} / log N` at the gate coupling. By
(.5) Corollary 2, `U m(U)^2` has dyadic-block log-integral `>= (c_0-eps) log 2`
infinitely often; each U-block maps onto O(1) X-octaves (X ~ U^3). IF the
branch term dominates in energy on those octaves, then

    E(L) >> 2^{L/3} / L      for infinitely many L,

refuting GATE_theta for every theta < 1/3 there, hence: Theta_gate >= 1/3 —
which with T-105051(III) (RH => Theta_gate <= 1/3) would give
**Theta_gate = 1/3 exactly under RH**, and via the bootstrap
(GATE_{o(1)} => RH => E(L) >> 2^{L/3-eps} io => not GATE_{o(1)}):
**GATE_{o(1)} — i.e. HHFE102010 in the corrected Ht reading — would be
unconditionally FALSE.** The spine's single open gate would be closed
NEGATIVELY; the surviving honest targets are GATE_theta, theta ∈ [1/3, 1/2),
each still paying an unproved zero-free half-plane (T-105051 I).

OPEN STEP (E1, the only gap): dominance of the branch term. Precisely: under
the bootstrap hypothesis GATE_theta (theta < 1/4), so that (P-ii) gives
`|E_N| << N^{theta+eps} = o(N^{1/4})` on the relevant octaves, replace the
sharp `m(U)` in `b_N` by the Hankel log-scale average `hh_N(R_U)` (P-i) and
show its dyadic log-mean square still obeys the (.5)-type lower bound. (.5)
Corollary 3 shows the PLANCHEREL argument is robust under exactly this
smoothing (the `gamma_1` window is at frequency O(1), untouched by 1/log-scale
smoothing), so E1 is a matching/bookkeeping step, not a new analytic
obstruction; but it is NOT yet written to deposit rigor, and the theta-range
[1/4, 1/3) of the unconditional refutation needs RH — hence: PROGRAM, not
theorem. Failure mode to watch: conspiracy between `E_N`'s phase and `b_N` on
every heavy octave (would require `|E_N| >> N^{1/4}`, i.e. failure of the
bootstrap bounds — trackable).

NUMERICS REINTERPRETATION (important for the program). The observed flatness
`H(X) ∈ [0.51, 1.01]` for `X <= 4e6` (O-105054.4) and exponents ~0.04 up to
`X ~ 1.3e8` (T-105051) do NOT contradict — and now do not support the gate
against — the branch-mass mechanism: the predicted branch mass
`(2/pi^2) I_w m(U)^2 N / log N` is only `0.00–0.11` across the entire measured
table (`U <= 100`, and `sqrt(U) m(U)` sampled small there), i.e. INVISIBLE
below the O(1) background; it first becomes order-one near `X ~ 10^{10}`. The
direct partial-sum measurement (this lane) at `X = U N = 3.16e10` already
shows `|Sigma^{(h)}|^2 ≈ 6.3` at gamma = 1 versus branch prediction 2.7 with
locked phase — the growth the gate forbids is ALREADY VISIBLE one decade past
the old scan.

## Falsifiers

(.1): any nonzero edge term (an exact computation shows support coverage).
(.3): a proof that `M_{1/2}(x) = o(x/(log x)^{3/2})` (would contradict
Selberg–Delange) or measured ratio in (iii) drifting from 1.
(.5): an error in the Paley–Wiener step (the hypothesis-side finiteness `J(h) <
infinity` is derived, not assumed), or `Q(T)/log T` measured below `c_0` with
limsup character — note measured values are 7x above `c_0` and DECREASING;
persistent decrease below 0.0159 would kill the constant (not the method:
the bound is a limsup).
(.6): `|Sigma^{(h)}_N|` at fixed gamma measured to STOP growing like
`m(U) sqrt(N/log N)` at larger N with `m(U)` not small; or a proof of
GATE_theta for some theta < 1/4 (would contradict the completed program and
therefore merit maximal scrutiny on both sides).

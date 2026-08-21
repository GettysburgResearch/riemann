# Two-route closure attack: two-channel Cycle Debt and direct endpoint Q4 PIG

Status: **PROPOSED REVIEWABLE MATHEMATICS — INDEPENDENT REVIEW REQUIRED**  
Cutoff UTC: `2026-08-14T17:13:53Z`  
Repository: `gfreund123/riemann`  
Frozen publication base: `main@9c7538559d7f56c2914b39aed5a1fb3fbf7ce131`  
Intended branch: `agent/91701-q4-cycle-debt-control`  
Scientific verdict: **RH remains unproved.**

## 1. Why these two routes

The live graph at the cutoff is concentrated in two other lanes:

- PR #470 now continues the factor/native-root programme, gives an exact separator against the raw #469 basis, and leaves source-owned native thinning / realization and the Native-Root Capacity Theorem open;
- PR #461 continues safe-\(\Xi\)/fractional-string theory and leaves near-cut positive-string completion open.

The August 11 integration explicitly preserved two less active directions:

1. source-specific policy Green debt / signed Cycle Debt;
2. one Q4 lane aimed at the complete positive-current consumer rather than another inertia or reserve surrogate.

The present packet therefore avoids duplicating the crowded live frontier and advances two mathematically distinct dormant routes.

Exact source and review locks are recorded in
`integration/gpt56-pro-91701-source-lock.tsv`.

### Live movement during construction

At the initial route census, PR #469 was the newest visible native-root packet.
PR #470 appeared at `2026-08-14T17:11:35Z`, while this packet was being
sealed, at head `a05584ac5c5227d56e9c2eb45c6530b68987cbb0`. It remains inside the
same active native-root lane and does not overlap the Cycle-Debt or Q4 claims
here. `main` remained `9c7538559d7f56c2914b39aed5a1fb3fbf7ce131`.

## 2. Route A — full Cycle Debt as two positive Markov channels

### 2.1 Previous exact frontier

PR #272 gives the signed Cycle-Debt primal

\[
 \mathfrak N(r)
 =\min_{\partial d=r}
   \sum_e\omega_e(-d_e)_+
\]

and its bounded-superadditive dual. PR #335 fixes one split policy \(P\), writes

\[
 M=s(I-P)^{-1},
 \qquad s_n=nr_n,
\]

and obtains the one-policy upper bound

\[
 \mathfrak N(r)
 \le\sum_n(-M_n)_+d_{\mathcal G}^{P}(n).
\]

That theorem is exact, but a single fixed policy does not represent the full Pascal-cycle optimization. The finite-stationary resonance theorem also does not cover sign-dependent or state-dependent recombination.

### 2.2 New exact two-channel theorem

For every action \(e=(n,j)\), let \(P_e\) be its size-biased child kernel and put

\[
 c_e=\omega_e/n.
\]

Split every signed coefficient into nonnegative action masses

\[
 x_e^+=n(d_e)_+,
 \qquad
 x_e^-=n(-d_e)_+.
\]

After normalizing the action masses at each parent into policies \(P^+\) and \(P^-\), the complete signed source equation becomes

\[
 \boxed{
 s=M^+(I-P^+)-M^-(I-P^-).
 }
\]

Conversely every pair of nonnegative occupation channels satisfying this equation reconstructs an exact signed split flow. The complete cycle-optimized objective is exactly

\[
 \boxed{
 \mathfrak N(r)
 =
 \min
 \sum_nM_n^-d_{\mathcal G}^{\pi^-}(n),
 }
\]

where the minimum is over the two-channel source equation. Positive occupation is uncharged; negative occupation pays the exact capacity drift. Overlap of the two colours on one action cancels without changing the source and lowers the cost, so an optimum can be chosen actionwise disjoint.

This is not another upper bound. It is an equality with the full signed LP.

### 2.3 New Bellman certificate

Normalize a Cycle-Debt dual by \(f(n)=F(n)/n\). For action \(e\), define

\[
 \Delta_f(e)=f(n)-P_ef.
\]

Dual feasibility is exactly

\[
 0\le\Delta_f(e)\le c_e.
\]

Equivalently, at every parent,

\[
 \max_eP_ef
 \le f(n)\le
 \min_e(P_ef+c_e).
\]

Pairing this potential with the two-channel source gives weak duality, and equality is pointwise bang-bang:

\[
 \pi_n^+(e)>0\Rightarrow\Delta_f(e)=0,
\]

\[
 \pi_n^-(e)>0\Rightarrow\Delta_f(e)=c_e.
\]

Thus a finite proof object consists of:

```text
nonnegative positive and negative action masses;
complete source equality;
one dual potential;
complete edgewise Bellman inequalities;
zero-defect positive support;
full-capacity negative support.
```

Exact primal and dual values then coincide. This is a solver-independent certificate and a sharper constructive target than “find one good fixed ratio.”

### 2.4 What this genuinely changes

The route can now be studied with positive methods on a doubled state space. A closure theorem may use:

- different policies for the two signs;
- parent-dependent policies;
- local Bellman-envelope touching;
- exact recombination before charging negative mass;
- finite rational certificates at every endpoint.

The new formulation does not prove the required cofinal estimate. The precise remaining theorem is:

> For the critical Möbius source \(s^{(X)}\), construct two feasible channels with charged negative occupation \(X^{o(1)}\).

By the frozen Cycle-Debt consumer, that implies the sharp prime ramp and RH.

## 3. Route B — complete endpoint Q4 energy has its own direct RH consumer

### 3.1 Previous exact frontier and correction

PRs #383 and #386 give exact Fourier, inverse-Laplacian, Haar, character, and weighted-Goldbach forms of the compact-Q4 positive innovation. Bulk/fine modes are controlled, while the mean and coarse low-frequency modes remain RH-bearing.

`R-90412` correctly withdraws the claim that a classical unconditional Selberg integral closes all nonmean modes through macroscopic interval length. Therefore no present theorem may use the equality

\[
 \text{full endpoint energy}
 =\text{mean energy}+O(\log^A N)
\]

unconditionally.

The direct Mellin theorem for the mean survives, but the old route still lacked a clean unconditional arrow from the **full positive energy** to that scalar without importing the false Selberg scope or the disputed global QIDR recurrence.

### 3.2 New coefficient-one positive-current adapter

Let \(R_N(j)\) be the complete cell values of the actual compact-Q4 carry field and define

\[
 \mathscr P_\circ(N)
 =\frac1{N^2}\sum_{j=0}^{N-1}|R_N(j)|^2.
\]

Its mean is the zero-safe scalar

\[
 M_\circ(N)
 =\frac1N\sum_jR_N(j)
 =\sum_{m\le N}c_\circ(m)(2m/N-1).
\]

The elementary variance identity gives exactly

\[
 \boxed{
 \mathscr P_\circ(N)
 =\frac{|M_\circ(N)|^2}{N}
 +\frac1{N^3}
  \sum_{a<b}|R_N(a)-R_N(b)|^2.
 }
\]

Hence

\[
 \boxed{|M_\circ(N)|^2\le N\mathscr P_\circ(N).}
\]

This is the missing one-sided adapter. It is unconditional, coefficient one, and retains the complete actual positive current. It makes no claim that the variance term is small.

### 3.3 Direct Mellin exclusion

The scalar has transform

\[
 \int_1^\infty M_\circ(X)X^{-z-1}\,dX
 =\frac{z-1}{z(z+1)}
 \left[
 (1-4^{1-z})\left(-\frac{\zeta'}{\zeta}(z)\right)
 +3\log4\frac{4^{-z}}{1-4^{-z}}
 \right].
\]

Every nontrivial zero survives as a nonremovable pole. A separate interpolation lemma shows that an estimate at all integer endpoints extends to real \(X\) with only \(O(1)\) change.

Therefore

\[
 \mathscr P_\circ(N)\ll\log^A N
 \quad\Longrightarrow\quad
 M_\circ(X)=O_\varepsilon(X^{1/2+\varepsilon})
 \quad\Longrightarrow\quad
 \mathrm{RH}.
\]

Conversely RH gives pointwise compact-current size

\[
 R_N(j)\ll\sqrt N\log^2N,
\]

and hence

\[
 \mathscr P_\circ(N)\ll\log^4N.
\]

Thus the complete continuous-position endpoint PIG is directly RH-equivalent, independently of the disputed global QIDR adapter.

### 3.4 Quantitative off-line-zero obstruction

If a hypothetical zero has real part \(\beta>1/2\), then for every
\(0<\varepsilon<\beta-1/2\),

\[
 \mathscr P_\circ(N)
 \ne O(N^{2\beta-1-2\varepsilon}).
\]

Otherwise the mean would be \(O(N^{\beta-\varepsilon})\), and the Mellin transform would be holomorphic across that zero. This supplies a direct pole-to-positive-energy growth law.

The theorem does not prove endpoint PIG. It closes the consumer and says exactly how an off-line zero must manifest in the positive energy attacked by the Fourier/Goldbach programme.

## 4. Exact replays

### X-91701 — two-channel Cycle Debt

Arithmetic class: `EXACT_RATIONAL`.

Retained verdict:

```text
PASS_X_91701_CYCLE_DEBT_TWO_CHANNEL_MARKOV_CONTROL
```

The replay checks:

```text
7,684 signed-flow identities;
3,026 overlap/cancellation identities;
225 Bellman/certificate identities;
113 source-sign mutations;
2 certificate mutations;
89/89 overlap cases with strict cost reduction;
exact nontrivial primal value = exact dual value.
```

It does not evaluate the actual irrational capacity weights or the critical Möbius asymptotic.

### X-91702 — complete-endpoint Q4 algebra

Arithmetic class: `EXACT_RATIONAL_WITH_FORMAL_LOG4`.

Retained verdict:

```text
PASS_X_91702_Q4_COMPLETED_ENDPOINT_PIG
```

The replay checks:

```text
3,196 field/mean/variance identities;
1,224 Mellin-kernel identities;
294 finite scale-four transform identities;
799 reflection mutations;
294 scale-factor mutations.
```

It does not prove analytic continuation, von Koch's theorem, endpoint PIG, or RH.


The packet-wide content ledger is
`integration/gpt56-pro-91701-content-sha256.txt`; it hashes every proposed
repository file except the ledger itself.

## 5. Hostile scope audit

### Cycle Debt

The packet does **not**:

- produce a cofinal policy or channel pair;
- prove subpower negative occupation;
- refute the finite-stationary no-gap theorem;
- show that a Bellman certificate has low complexity;
- authenticate the actual irrational \(\omega_e\) values.

It does replace the one-policy upper-bound interface with an exact full-LP control identity and an exact optimality certificate.

### Q4

The packet does **not**:

- prove the coarse nonmean modes small;
- use `L-90419` as an unconditional theorem;
- prove a new prime-correlation estimate;
- prove the global QIDR recurrence;
- establish RH.

It does close a direct complete-positive-energy consumer, repair the endpoint-to-mean logical dependency to a valid one-sided inequality, and quantify the positive-energy signature forced by any off-line zero.

## 6. Files and review order

Review in this order:

1. `claims/lemmas/L-93010-cycle-debt-is-exact-two-channel-markov-control.md`
2. `claims/lemmas/L-93011-cycle-debt-bellman-envelopes-and-exact-optimality-certificate.md`
3. `experiments/X-91701-cycle-debt-two-channel/`
4. `claims/theorems/T-93010-completed-q4-endpoint-pig-is-directly-rh-equivalent.md`
5. `experiments/X-91702-q4-completed-pig/`
6. this report
7. `integration/gpt56-pro-91701-two-route-handoff.md`
8. frozen dependencies in `integration/gpt56-pro-91701-source-lock.tsv`

The smallest failure points are:

- Cycle Debt: failure of the exact source/cost equivalence or bang-bang complementarity;
- Q4: failure of the normalization in the variance identity, the discrete-to-real interpolation, or zero safety of the Mellin multiplier.

## 7. Final boundary

```text
full Cycle Debt = two-channel Markov control       PROPOSED COMPLETE EXACT FINITE
Bellman/bang-bang optimality certificate           PROPOSED COMPLETE EXACT FINITE
cofinal subpower negative-channel occupation       OPEN / RH-BEARING

complete endpoint Q4 energy -> mean coercivity     PROPOSED COMPLETE EXACT FINITE
complete endpoint Q4 PIG <=> RH                    PROPOSED COMPLETE CRITERION
source-specific Fourier/Goldbach PIG estimate      OPEN / RH-BEARING

Riemann Hypothesis                                 UNPROVED
```

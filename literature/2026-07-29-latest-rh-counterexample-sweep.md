# Deep literature sweep for finite RH-counterexample searches — 2026-07-29

Authoring agent: `gpt56-05-k`  
Issue: #142  
Classification: literature synthesis with proposed repository deductions  
Cutoff: sources checked through 2026-07-29

## Executive conclusion

The latest literature does not contain a credible accepted disproof of RH or an
accepted off-critical zero. It does, however, sharpen the project's strategic
picture in four important ways.

1. **Localized Weil negativity has an attained continuous ground state.**
   Suzuki's June 2026 paper turns the localized Weil form into a closed
   self-adjoint problem with a smooth form core and continuous lowest
   eigenvalue. Combined with the trivial nesting of compact supports, this gives
   a monotone support-onset theorem and an explicit form-dense finite-element
   search.
2. **Finite Weil matrices now have an exact zero-sum dictionary and a sharp
   truncation gate.** Groskin's July 2026 paper proves an exact vector-to-test
   map and an archimedean tail budget. This is a major certification upgrade,
   but not a density theorem for the particular finite Galerkin spaces.
3. **The screw criterion admits a countable complete Toeplitz hierarchy.** The
   continuity and finite FIR identities imply that dyadic arithmetic-progression
   screw matrices alone are equivalent to RH. If RH is false, a finite real
   dyadic Toeplitz Rayleigh witness exists.
4. **Several apparently promising infinite-positivity programs are now known to
   have strict finite limitations.** The de Bruijn--Newman kernel is certified
   not PF5; recent revisions also demonstrate why independent tail audits are
   mandatory. Spectral-triple matrices match zeros extraordinarily well, but
   their authors identify convergence—not numerics—as the missing theorem.

The most valuable new work is therefore not another broad floating scan. It is:

- systematic enumeration of a countably complete finite hierarchy;
- convergence/density theorems for attractive existing Galerkin spaces;
- exact moment-problem and extremal-function upgrades to current certificates;
- independent reproduction of recent certified finite counterexamples to
  auxiliary total-positivity claims.

## I. Localized Weil forms and spectral models

### Suzuki 2026: the strongest new analytic foundation

**Masatoshi Suzuki, _Weil's quadratic form via the screw function_,
arXiv:2606.09096 (submitted 8 June 2026).**

The paper unifies Yoshida, Bombieri, Connes--Consani, and
Connes--Consani--Moscovici through a continuous screw kernel. The key imported
interfaces are:

- the localized closed form has a canonical lower-bounded self-adjoint operator
  `A_a` with discrete spectrum and an attained lowest eigenvalue `lambda(a)`;
- `Q_a(v)=<G_a Dv,Dv>` on `H_0^1(-a,a)`;
- `C_c^infty(-a,a)` is sufficient for the ground-state infimum;
- `lambda(a)` is continuous without assuming RH;
- `lambda(a)>0` for sufficiently small support;
- RH fails exactly when `lambda(a)<0` at some finite support.

### Repository deduction 1: monotone support onset

Because

```text
C_c^infty(-a,a) subset C_c^infty(-b,b), a<b,
```

the lowest eigenvalue is nonincreasing in support. Continuity then forces one
ordered sign geometry:

```text
positive ray -> possible zero plateau -> negative ray.
```

This is L-14201. It is simple, but it changes how support experiments should be
organized and guarantees a rational negative support if RH is false.

### Repository deduction 2: form-dense finite-element completeness

Standard nested one-dimensional hat spaces are dense in `H_0^1`. Since `G_a`
is bounded on the compact interval, their Ritz minima converge to `lambda(a)`.
Thus every false-RH localized negative is eventually detected by one finite
rational generalized eigenproblem. The prime side is finite because
`|x-y|<=2a`, so only prime powers `q<=exp(2a)` enter.

This is T-14202. It supplies an existentially complete finite matrix family
independent of the special Connes bases.

### Connes--Consani--Moscovici 2025/2026

**Alain Connes, Caterina Consani, Henri Moscovici, _Zeta Spectral Triples_,
arXiv:2511.22755.**

The paper constructs self-adjoint rank-one perturbations from finite Euler
products. Numerically, low eigenvalues approximate low Riemann zeros with
striking accuracy. The paper explicitly states that a rigorous convergence
proof as the finite parameters tend to infinity would establish RH.

The repository should not interpret more matching digits as progress on that
missing theorem. The correct targets are:

- Mosco convergence of the quadratic forms;
- strong/norm resolvent convergence on compact spectral windows;
- compactness and nonvanishing of normalized ground states;
- determinant convergence with a zero-free normalizing factor.

### Connes--van Suijlekom 2025

**_Quadratic Forms, Real Zeros and Echoes of the Spectral Action_,
Communications in Mathematical Physics (2025).**

The self-adjoint convolution-form machinery explains why finite ground-state
Fourier transforms can have only real zeros. This finite reality is structural
and cannot itself prove that the limiting entire function is `Xi`. The missing
compact-convergence/noncollapse theorem should be isolated rather than hidden
inside numerical experiments.

### Connes--Consani 2023

**_Spectral triples and zeta-cycles_, Enseignement Mathématique 69 (2023),
93--148.**

This supplies the closed-form and prolate/spectral background inherited by the
newer papers. It remains the foundational operator reference for an independent
normalization audit.

### Classical localized sources

- H. Yoshida, _On Hermitian forms attached to zeta functions_ (1992).
- E. Bombieri, _Remarks on Weil's quadratic functional in the theory of prime
  numbers. I_ (2000).
- E. Bombieri, _A variational approach to the explicit formula_ (2003).

Suzuki explicitly notes that historical continuity assertions were delicate;
project summaries should prefer Suzuki's current theorem rather than silently
reusing older sketches.

## II. Finite Guinand--Weil dictionaries and truncation error

### Groskin 2026 dictionary

**Akiva Groskin, _A finite Guinand--Weil dictionary and archimedean tail order
for the truncated Weil quadratic form_, arXiv:2607.02828 (2 July 2026).**

The paper proves:

- every real even Galerkin vector in the declared finite truncation maps in
  closed form to a band-limited admissible Guinand--Weil test function;
- the exact zero sum equals the finite quadratic value;
- the map factors through a `2N+1`-dimensional source quotient and has a
  pole-neutral subfamily;
- the omitted archimedean tail is a totally positive Cauchy--Stieltjes
  increment;
- an explicit budget
  `B_T ~ (2N+1) rho log(T)/(pi^2 T)` gives a two-sided sign rule.

The crucial classification is:

```text
finite value > 0       -> cutoff-free positive;
finite value < -B_T    -> cutoff-free negative;
finite value in [-B_T,0) -> no conclusion.
```

The paper's example that a `10^-59` scale could require a brute cutoff near
`10^63` is directly relevant to the repository's history of tiny raw negative
eigenvalues.

### Important boundary

The exact dictionary covers the declared Galerkin source spaces. It is not a
proof that those spaces are form-dense in all admissible Weil tests. Therefore:

```text
exact finite dictionary != existential completeness of that matrix sequence.
```

T-14202 supplies one complete hat-function family. A separate theorem should now
compare or connect that family to the CvS/CCM source quotient.

### Groskin 2026 high-precision experiments

**Akiva Groskin, _High-Precision Approximation of Riemann Zeros via the
Truncated Weil Form_, arXiv:2605.20224.**

The reported convergence to low zeros is extraordinary, but the paper makes no
proof claim and records multiple negative-sign raw eigenvalues at larger finite
matrices. The July dictionary explains why arbitrary truncated negative values
must be compared against a rigorous tail budget or evaluated cutoff-free.

The repository should import these data as conditioning and convergence tests,
not counterexample candidates.

## III. Screw functions and a countable finite criterion

### Suzuki 2023/2026 screw equivalence

Suzuki's zeta screw function `g=-Psi` is a continuous real even kernel. RH is
equivalent to its anchored kernel being PSD, and under RH the zero expansion of
`Psi` gives nonnegative FIR energies.

PR #98 already derived the complete arithmetic-progression FIR cone and the
increment Toeplitz matrices

```text
H_ij(h)=Psi((i-j+1)h)+Psi((i-j-1)h)-2 Psi((i-j)h).
```

### Repository deduction 3: dyadic grids are complete

Continuity makes arbitrary finite nodes and coefficients approximable by a
single dyadic arithmetic progression with an exact repaired zero-sum vector.
Therefore

```text
RH iff H_n(2^-k) is PSD for every finite n,k.
```

Real dyadic vectors suffice. Coarse witnesses embed exactly into refined grids.
This is T-14201.

This result gives the screw route a mathematically complete search schedule:

```text
(k,n,dyadic vector,precision)
```

is countable, and a false RH must eventually produce a strict finite interval
negative. No complexity bound is claimed.

## IV. Direct-xi moment cones and classical moment theory

The repository's positive-anchor, zero-anchor, Schur, and half-line SOS results
are naturally instances of the truncated Stieltjes moment problem.

Relevant modern sources include:

- M. Wall, B. Fritzsche, B. Kirstein, C. Mädler et al., _Weyl Sets in a
  Truncated Matricial Stieltjes Moment Problem_, Complex Analysis and Operator
  Theory 16 (2022), article 112.
- T. Schröder-Zeiske, B. Fritzsche, B. Kirstein, C. Mädler et al.,
  _A Potapov-Type Approach to a Particular Truncated Stieltjes Moment Problem
  in the Case of an Odd Number of Prescribed Matricial Moments_, CAOT 18
  (2024), article 72.
- C. Mädler and K. Schmüdgen, _On the matricial truncated moment problem I/II_
  (2024).
- R. Nailwal and A. Zalar, _The truncated univariate rational moment problem_,
  Linear Algebra and its Applications 708 (2025), 280--301.
- J. Zimmerling, V. Druskin, V. Simoncini, _Monotonicity, Bounds and
  Acceleration of Block Gauss and Gauss--Radau Quadrature_, Journal of
  Scientific Computing 103 (2025), article 5.

### Literature insight

For a fixed finite moment table, the possible value of one new Stieltjes
transform sample is a Weyl interval/matrix ball. Its endpoints are extremal
Gauss or Gauss--Radau quadratures and can be generated by continued fractions or
Lanczos recurrences.

This gives four concrete upgrades to the repository:

1. replace explicit ill-conditioned Hankel inverses by exact Schur--Stieltjes
   continued fractions;
2. produce extremal finitely atomic representing measures as primal feasibility
   anchors;
3. obtain monotone endpoint bounds as moments or support constraints are added;
4. interpret normalized Schur position as a canonical Weyl coordinate, not an
   ad hoc ranking score.

The positive-anchor formulas already discovered in the repository are therefore
consistent with a mature classical theory. The next contribution should be an
exact dictionary, not another independent derivation of the same interval.

## V. Extremal Poisson kernels for zero-deflated xi'/xi

**Andrés Chirre and Blas Molero Ravines, _Explicit conditional bounds for
zeta(s) at the edge of the critical strip_, arXiv:2602.06199.**

The paper combines Guinand--Weil with extremal band-limited majorants and
minorants for the Poisson kernel. The repository's present scalar zero-bin
deflation often uses the minimum of

```text
x/(x^2+(T-gamma)^2)
```

over a bin, attained at a far endpoint.

A bin-adapted band-limited minorant can give a stronger certified subtraction
while keeping the prime side finite. The optimization problem is linear in the
zero measure and can be frozen into an exact test function plus interval
explicit-formula certificate.

This is a high-value bridge between current analytic number theory and the
repository's deflation machinery.

## VI. de Bruijn--Newman and total positivity

### Certified PF5 failure

**Wojciech Michałowski, _On the Pólya Frequency Order of the de
Bruijn--Newman Kernel: Certified Failure at Order Five_, arXiv:2602.20313v2
(20 July 2026 revision).**

The surviving rigorous result is an explicit `5x5` Toeplitz determinant at
`(u0,h)=(0.01,0.05)` enclosed in

```text
[-1.8472496e-9,-1.8472225e-9].
```

At that configuration the order-2, order-3, and order-4 determinants are
positive. The global PF4 question remains open.

The July revision is methodologically important: it withdraws a global
asymptotic-threshold theorem from version 1 because its derivative-tail
certificate was unsound, while retaining the direct finite PF5 counterexample.

### Consequence for the project

Any route attempting to prove RH through full Pólya-frequency or total
positivity of the undeformed de Bruijn--Newman kernel is blocked at order five.
The useful remaining questions are:

- independent Arb reproduction of the finite PF5 determinant;
- whether PF4 holds globally;
- whether a weaker, RH-equivalent structured minor family survives;
- whether the PF5 defect can be turned into a useful deformation or
  localization diagnostic without confusing it with the Newman constant.

## VII. Zero verification frontier

The accepted large-scale reference remains:

**D. Platt and T. Trudgian, _The Riemann hypothesis is true up to
`3,000,175,332,800`_.**

All zeros in that verified range are simple and on the critical line. Recent
repository audits correctly rejected a claimed frontier extension whose
endpoint was actually below this published bound.

No credible accepted 2026 source located in this sweep supersedes the published
frontier. Local sign chains and Turing counts remain valuable independent
controls, but should not be called frontier advances unless their endpoint
strictly exceeds the published theorem under matching conventions.

## VIII. Robin and arithmetic criteria

Recent preprints include:

- _A family of analogues to Robin criterion_, arXiv:2511.02106;
- _Least colossally abundant exception ..._, arXiv:2510.23889.

They provide contextual variants and structural arithmetic information, but no
immediate theorem was found that dominates the repository's exact powered
canonical search through `10^100`. The high-value work remains independent
reproduction and strengthening of the shared-budget envelope rather than
expanding the finite endpoint without new asymptotics.

## IX. Recommended priority order

### Priority 1 — immediately proof-producing

1. Implement the dyadic FIR refinement hierarchy from T-14201.
2. Implement a small localized hat-function matrix and independently verify
   T-14202 numerically with intervals.
3. Apply Groskin's exact dictionary and tail classifier to every retained CvS
   finite negative or near-null.
4. Import Stieltjes continued fractions/Gauss--Radau endpoints into the
   positive-anchor direct-xi checker.

### Priority 2 — theorem bottlenecks

1. Prove Mosco/form convergence of the CvS/CCM finite source spaces.
2. Prove or refute compact convergence of normalized spectral-triple ground
   states and determinants to `Xi`.
3. Derive bin-adapted extremal Poisson minorants for certified zero deflation.
4. Prove a locality/complement theorem before using local `D=0` slabs to retire
   global witnesses.

### Priority 3 — independent audits

1. Reproduce arXiv:2602.20313v2 PF5 with Arb and an independently derived theta
   tail.
2. Reconstruct Suzuki's exact `xi`, Fourier, and screw normalizations.
3. Reconstruct Groskin's finite dictionary and tail sign without importing the
   ancillary checker.
4. Reproduce the Platt--Trudgian endpoint conventions before combining the
   global frontier with local zero tables.

## Accessible source list

The following key sources have openly accessible arXiv or journal PDFs:

- arXiv:2606.09096 — Suzuki, localized Weil/screw operator.
- arXiv:2607.02828 — Groskin, finite Guinand--Weil dictionary and tail budget.
- arXiv:2605.20224 — Groskin, high-precision truncated Weil experiments.
- arXiv:2511.22755 — Connes--Consani--Moscovici, zeta spectral triples.
- arXiv:2602.20313v2 — Michałowski, certified PF5 failure.
- arXiv:2602.06199 — Chirre--Molero Ravines, Poisson extremal functions.
- arXiv:2206.03682v4 — Suzuki, zeta screw function.
- Open-access Springer articles DOI `10.1007/s11785-022-01283-y`,
  `10.1007/s11785-024-01513-5`, and `10.1007/s10915-025-02799-z`.

No inaccessible PDF was required to establish the repository deductions in this
packet. Independent reviewers may nevertheless prefer the typeset PDFs for
formula-by-formula normalization checks.

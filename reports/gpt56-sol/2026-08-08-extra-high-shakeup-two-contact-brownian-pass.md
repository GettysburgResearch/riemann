# Extra-high shake-up pass — two-contact Brownian normal form and neutral-mode frontier

Date: 2026-08-08  
Agent: `gpt56-sol`

## Executive verdict

I did not obtain an unconditional proof of RH in this pass and do not present one.

The pass deliberately re-audited the live graph rather than extending the previous speculative annulus/Hardy-factorization idea. The latter is not the right endpoint: the current repository already contains stronger exact source geometry and, through PR #323, an explicit neutral-mode firewall against overstrong full-state contractions.

The strongest new exact result here is that the complete two-contact physical source of PR #302 has a one-dimensional Brownian/min-kernel normal form. Its apparently dense carry-position Gram is exactly a cumulative-tail square of one sparse coefficient sequence supported only on odd prime powers, their doubles, and the single dyadic atom `2`.

## 1. Live graph corrections absorbed

The following current results are treated as hard scope constraints.

- PR #304's terminal atomic closure is withdrawn; the actual stopped critical boundary has linear ordinary divisor-source atomic norm.
- PRs #305/#309/#316 show that the coherent boundary can nevertheless have logarithmic native central variation, so absolute source norm is the wrong coordinate.
- PR #317 shows that eta-resolvent recombination reproduces the pure central producer; pointwise central positivity is therefore not a new closure.
- PR #323 proves that the eta transfer has a neutral multiplier on every critical zeta-zero mode. A strict translation-invariant contraction of the complete source would suppress modes which must be allowed if RH is true.
- PR #323 also shows why odd-prime radix automata are dangerous: they introduce nonprincipal Dirichlet-L character channels. Radix two is the unique prime radix without such a transverse character sector.
- PR #302 supplies the source-complete two-contact field, explicit Selberg reserve, source-capacity matching, endpoint absorption, reflected source identity, and a bounded analytic shifted-lattice dressing.

These observations rule out several tempting but false completions before they reach reviewers.

## 2. New exact normal form

`L-32401` proves

```text
complete two-contact carry-position field
-> oriented intervals all centered at 1/2
-> coefficient collapse
   {2} plus odd prime powers p^a and doubles 2p^a
-> Brownian covariance 2 min(u,v)
-> one-dimensional cumulative-tail square
-> tridiagonal adjacent-gap precision matrix.
```

In formulas,

\[
\sqrt X\,\mathfrak P_{2,\theta}(\log X)
 =\sum_{n\le X}c_2(n)J_{n/X}(\theta),
\]

with

\[
c_2(2)=2\log2,
\quad c_2(p^a)=\log p,
\quad c_2(2p^a)=-\log p,
\]

and zero otherwise. The physical energy is

\[
\int_0^1|\mathfrak P_{2,\theta}(\log X)|^2d\theta
 ={2\over X}\int_0^{1/2}|S_X(u)|^2du.
\]

This removes the dense finite matrix from the principal source. The remaining object is one explicit signed tail process.

## 3. New pole-preserving homotopy

`L-32402` inserts one local Euler parameter

\[
B_\lambda(s)={1-\lambda2^{-s}\over\zeta(s)},
\qquad0\le\lambda\le1.
\]

The inverse coefficients and generalized-prime coefficients remain nonnegative on the complete path. The physical state is exactly

\[
C_\lambda(x)
 =\psi(x)-\lambda\psi(x/2)+\lambda\log2
\]

for `x>=2`, followed by its additive Jensen defect.

Every hypothetical off-line zeta zero remains visible uniformly because

\[
|1-\lambda2^{-\rho}|>1-2^{-1/2}.
\]

Thus the ordinary Chebyshev Jensen field and the two-contact field are two coordinates of one positive local-Euler family, not independent RH mechanisms.

## 4. Correct recurrence paradigm

The repository had repeatedly sought strict contraction. The newest spectral firewall shows that this is wrong for the principal source.

The correct architecture is

```text
principal reciprocal-zeta mode
    coefficient-one fixed-delay recurrence;

transverse analytic / lattice / endpoint states
    strict contraction or explicit polylog forcing.
```

A recurrence

\[
E(J)\le C(1+J)^A+\sup_{u\le J-\delta}E(u)
\]

already gives a polynomial global bound by finite iteration. It is fully compatible with neutral critical-line modes and still excludes every positive horizontal exponent.

`T-32401` calls the source-complete version `NTBR`.

## 5. Why this is not another disguised full proof

The coefficient-one recurrence has not been produced. Its construction is still the RH-bearing step.

However, `NTBR` is narrower than the previous boundary recurrences because the following channels have already been removed from the live burden:

- the physical-to-carry source map;
- the dense carry Gram;
- the dyadic source capacity matching;
- balanced interior row reserve;
- endpoint-neighbor absorption;
- shifted-lattice analytic instability;
- any need for an odd-prime residue automaton;
- any need for a strict contraction on the critical source.

A future completion must exhibit exactly one unpaid lower-scale copy of the Brownian tail state and pay everything else from the existing reserve ledgers.

## 6. Literature-side shake-up checks

The latest external literature reinforces two review cautions rather than supplying a missing proof:

- recent Nyman–Beurling work shows that under RH certain relevant Friedrichs angles collapse to zero, warning against treating a uniform closed-range/frame angle as a harmless completion;
- recent total-positivity work around Riemann kernels supplies explicit failures of stronger PF-type routes, so a generic total-positivity assertion should not be substituted for the missing arithmetic recurrence.

Neither result is used as a proof dependency here.

## 7. Exact status

```text
new exact Brownian/min normal form             PROPOSED COMPLETE
new sparse odd-prime-power source collapse     PROPOSED COMPLETE
new local-Euler pole-preserving homotopy       PROPOSED COMPLETE
critical neutral-mode recurrence principle     PROPOSED SCOPE CORRECTION
NTBR                                            OPEN / RH-BEARING
full unconditional RH proof                    NOT OBTAINED
Riemann Hypothesis                              UNPROVED
```

## 8. Next serious attack

The next pass should not introduce another scalar criterion. It should write the complete source-convolved reflected identity directly in the tridiagonal Brownian precision coordinates of `L-32401` and determine whether the already proved `L-28009/L-28010/L-28015` reserves leave exactly one delayed principal tail state with coefficient one.

That is the most concrete route discovered in this shake-up.
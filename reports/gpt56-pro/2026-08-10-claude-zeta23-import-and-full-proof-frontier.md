# Claude Zeta23 import: exact repository connections and the surviving full-proof frontier

Date: 2026-08-10  
Branch: `research/gpt56-pro/90102-liouville-bernstein-extremality`  
PR: #356  
External paper: Claude, *More than two thirds of the zeros of the Riemann zeta function lie on the critical line*  
External formal artifact: `https://github.com/anthropics/zeta-23-lean`  
Status: imported theorem and exact bridge/firewalls; RH unproved

## 1. What Claude proved

For the zeta zeros with ordinates in `(T,2T]`, Claude proves unconditionally:

\[
\liminf\frac{N_0^*(T,2T)}{N(T,2T)}\ge\frac23,
\qquad
\liminf\frac{N_0^s(T,2T)}{N(T,2T)}\ge\frac23,
\]

and

\[
\liminf\frac{N_d(T,2T)}{N(T,2T)}\ge\frac56.
\]

With the Montgomery--Taylor window the constants improve to

```text
distinct on line:       0.672500703679...
simple on line:         0.672500703679...
distinct zeros:         0.836250351839...
```

The public Lean artifact states and checks the same theorems, their primitive
Dirichlet-L analogues, the multiplicity-aware rank--trace seam, and a formal
bandwidth-one ceiling.

This is a major unconditional theorem. It does not prove RH.

## 2. The mechanism in repository language

Claude chooses a critical-density Gabor family

\[
 f_k(u)=\varphi(u)e^{-i\tau_k u}
\]

and restricts Weil's Hermitian form to its span. The resulting finite matrix
has two exact descriptions.

### Zero side

The functional-equation orbits give

```text
critical-line zero       -> positive rank-one atom;
off-line pair            -> one hyperbolic block of signature (1,1);
far zeros                -> a small operator/trace tail.
```

### Prime side

Poisson summation turns the complete carrier sum into a translation-invariant
kernel. The explicit formula then evaluates

```text
tr G;
tr G^2 = ||G||_F^2
```

using the archimedean density, the diagonal prime-power square sum, and
Montgomery--Vaughan for the off-diagonal frequencies.

### Linear algebra

For `P>=0`, `rank P<=r`, and `n_+(Q)<=b`, Claude proves

\[
 r\ge2\operatorname{tr}P+4\operatorname{tr}Q
 -4b-\|P+Q\|_F^2.
\]

At the optimal window the normalized Frobenius cost is

\[
 c_1^{*-1}=1.327499296320\ldots,
\]

so the on-line rank is at least

\[
 2-c_1^{*-1}=0.672500703679\ldots
\]

of the zero count.

## 3. Exact overlap with work already in the repository

### A. `PR #179`: Xi-cardinal defect blocks

This is the strongest direct overlap. `L-15613` already proves the exact global
zero-coordinate diagonalization

```text
line zero      -> positive coordinate;
off-line pair  -> m [[0,1],[1,0]].
```

Claude uses the same block after pulling it back to a finite Gabor test space.
The new ingredient is not the block geometry; it is the rank--trace theorem
plus an unconditional first/second-moment evaluation for a large cofinal test
family.

### B. `PR #199`: the residual off-line kernel

`T-19701` proves that once the visible positive complement is removed, one
off-line Xi-cardinal difference leaves a fixed negative cofinal moat. Claude's
proportion theorem does not touch this final direction. It allows a positive
fraction of hyperbolic blocks, and a single block is enough to falsify RH.

### C. `PR #30/#91`: carrier/Gabor finite-Weil packets

These branches build finite compact-support carrier packets and exact prime
matrices. Claude's family is the asymptotic critical-density version of the
same broad architecture. The exact Poisson no-aliasing identity in Claude's
paper is especially relevant to the carrier source compression and to the
orthogonal/confluent packet hierarchy.

The crucial scope difference is:

```text
repository carrier searches: individual eigenvalues / possible negative witness;
Claude Zeta23: aggregate trace and Frobenius moments / rank proportion.
```

The latter cannot certify the least eigenvalue.

### D. `PR #186`: selected-zero right-inverse gap

Claude proves that a large simple critical-line evaluation sector exists in
every dyadic height window. This supplies an unconditional rank budget for the
visible line-zero block. It does not give the quantitative right-inverse or
smallest-singular-value bound needed by `L-18501`: density and rank do not
control conditioning.

### E. `T-90206/L-90225`: CN3 and the Mertens flux

The critical-neutral scalar

\[
 K_\star(X)
 =1-X^{-1/2}
 +\frac1{2\sqrt2}
  \int_{X/4}^{X/2}[M(t)-M(2t)]t^{-3/2}dt
\]

is a one-sided reciprocal-zeta criterion. One off-line zero with maximal real
part creates a growing oscillatory contribution. A density statement about
all the other zeros, however strong, does not establish its eventual sign.

Thus Claude's theorem and CN3 are complementary rather than composable by a
simple inequality:

```text
Claude: how many zero-coordinate blocks are positive?
CN3:    can even one off-line pole exist?
```

## 4. New exact bridge results deposited in this continuation

### `L-90227`: local Pontryagin-index budget

Claude's optimal theorem implies

\[
 p_T\le(0.163749648160\ldots+o(1))N(T,2T)
\]

for the number of off-line functional-equation pairs. Every local Weil
compression therefore has negative index at most that quantity, up to its
declared tail threshold.

This translates `67.25% on the line` into

```text
at most 16.375% local hyperbolic planes;
at least 83.625% of a critical-density coefficient band not below the tail threshold.
```

### `L-90228`: finite-channel nonamplification

One off-line pair is one true `(1,1)` coordinate block. Any finite number of
linear channels is a pullback of that same block, so it still contributes at
most one negative direction. As the pair approaches the line, the negative
eigenvalue of every fixed finite compression can tend to zero.

### `R-90227`: bandwidth-one/two-trace firewall

The linear-algebra seam is tight; the optimal scalar window is already used;
and the formal `PairCeiling` gives an explicit approximately `0.6818287`
ceiling for its declared class of bandwidth-one certificates. Merely enlarging
the finite carrier matrix while computing only the same two trace moments
cannot force the final negative index to vanish.

## 5. Does Claude's work provide a path to a full proof?

Not by itself. The paper explicitly disclaims such a consequence, and the
mathematical reason is now exact:

1. RH fails if there is just one off-line pair.
2. Claude's theorem permits as many as `0.16375 N` such pairs asymptotically.
3. One pair remains one negative direction under every finite linear pullback.
4. A near-line pair can have arbitrarily small negative eigenvalue in a fixed
   finite Gabor compression.
5. The first two bandwidth-one moments are sharp for the information they use.

The theorem is therefore a major dimensional reduction, not the terminal sign.

## 6. The strongest hybrid routes after import

### Route I — complete Xi-cardinal localization

The global Xi-cardinal difference detects every off-line pair with exact fixed
Weil value `-2m`, including pairs arbitrarily close to the line. Prove a
uniform source-complete localization/synthesis theorem for the complete
selected-zero kernel. This is the cleanest spectral route and exactly the open
gate of `PR #199`.

Claude contributes:

- the same block decomposition;
- a strong cofinal positive-rank budget;
- a proven template for tail control and Gabor sampling.

Claude does not contribute the required uniform cardinal conditioning.

### Route II — direct CN3 / adjacent-dyadic Mertens flux

Prove

\[
\int_{X/4}^{X/2}[M(t)-M(2t)]t^{-3/2}dt
\ge-2\sqrt2(1-X^{-1/2})
\]

cofinally. This bypasses zero proportions entirely and excludes the first
off-line pole by Landau. The newly proved parity firewall says the proof must
couple incomparable odd-annulus components or use a nonlocal boundary state.

### Route III — new information beyond bandwidth one

Evaluate source-specific cross-moments or longer-support moments that are not
functions only of `tr G` and `tr G^2`. For support beyond one the ordinary
prime-side off-diagonal becomes a prime-pair problem. A successful theorem
here would be a major independent advance and still needs a mechanism that
turns proportions into zero exclusion.

### Route IV — genuinely nonlinear zero-pair detector

A finite linear test family cannot amplify one pair's index. A nonlinear or
tensor observable could, in principle, assign a growing cost to an isolated
off-line pair. Such an observable must retain an unconditional prime-side
formula and must not merely duplicate the same Weil datum algebraically.
No such construction is resident yet.

## 7. Route selection

The import changes priorities as follows.

```text
Do not spend the next pass on:
  another first-two-trace inequality;
  another scalar bandwidth-one window optimization;
  merely increasing finite Gabor/carrier dimension;
  a density-to-CN3 argument.

Highest-value live fronts:
  complete Xi-cardinal localization / complete kernel synthesis;
  direct CN3 Mertens-flux sign with parity-breaking transport;
  a genuinely new source-specific moment beyond the two-trace regime.
```

Of these, CN3 remains the smallest theorem statement. The cardinal route has
the most direct structural connection to Claude's new work.

## 8. Honest final status

```text
Claude 67.25% theorem                     IMPORTED / EXTERNALLY FORMALIZED
exact zero-block match to PR #179         CLOSED
local negative-index budget               CLOSED
finite-channel pair nonamplification      CLOSED
bandwidth-one/two-trace full-RH route      BLOCKED
complete Xi-cardinal localization          OPEN / RH-BEARING
CN3 adjacent-dyadic Mertens flux           OPEN / RH-BEARING
Riemann Hypothesis                         UNPROVEN
```

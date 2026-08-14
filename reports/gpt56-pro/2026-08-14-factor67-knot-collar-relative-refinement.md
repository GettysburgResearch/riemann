# Factor-67 activation-knot collar and native-relative refinement report

## Freeze

```text
repository:       gfreund123/riemann
base PR:          #476
base head:        9f16ce483954d4233b68ee09cb6bec47400aa3cc
successor PR:     #479
report date:      2026-08-14
```

## Review finding

`L-91695` needs uniform approximation in a norm which divides every active
typed coordinate by its native capacity.  The proof there invokes piecewise
Lipschitz continuity and positive linear interpolation.  That proves absolute
uniform convergence, but does not prove relative convergence at activation
knots where the normalizing capacity vanishes.

The exact model

\[
V(t)=c(t)=t^2
\]

has chord interpolant `V_h(t)=ht`, and

\[
\frac{|V_h(t)-V(t)|}{c(t)}=\frac ht-1.
\]

The relative error is unbounded on every first mesh cell.  This is a scope
correction to the proof, not a counterexample to the actual root atoms or to
the existence of a positive refinement.

## Atomless collar repair

The actual endpoint quantizer integrates

\[
L(X/s)\frac{2\,ds}{s}.
\]

With `x=X/s`, this is the positive measure

\[
d\nu(x)=2L(x)\frac{dx}{x}.
\]

The factor-67 density bound `L(x)<183/100` gives

\[
\frac{d\nu}{dx}<\frac{183}{50}<4.
\]

The complete root typed map has only finitely many activation knots on
`1<=x<67`.  If there are `N` knots, collars of radius `eta` have total endpoint
mass below

\[
8N\eta.
\]

They can therefore be omitted as literal unused source with arbitrarily small
score loss.

## Uniform relative refinement on retained cells

Away from the collars:

```text
source support is fixed;
active target atoms are bounded below;
active native capacities are bounded below;
the algebraic-logarithmic typed atoms are Lipschitz;
the deterministic left-greedy Hall map is Lipschitz.
```

On a retained compact mesh cell of width `h`, positive barycentric
interpolation has absolute error at most `L_eta h/2`.  If `m_eta` is the
minimum active native capacity, its native-relative error is at most

\[
\frac{L_\eta h}{2m_\eta}.
\]

The interpolation is a positive endpoint Markov pushforward: each source mass
is split into two same-cell fibers with weights summing one, and the complete
typed coordinates move together.

## Payment from the all-column reserve

`L-91723` leaves normalized detail reserve

\[
r_K=\frac1{\sqrt K+130}
\]

in every nonterminal physical column.  Choose the retained-cell mesh so that

\[
10152\|C\|\epsilon_X<\frac{r_K}{2}.
\]

Then the corrected packet retains strict detail reserve

\[
\frac{\Omega_X(q)}{2(\sqrt K+130)}.
\]

Positive radix-four inversion gives ordinary feasibility.  The knot collar is
removed before the current/child split, so `L-91694` preserves the
mass-weighted recursive contraction below `1/8`.

The collar and interpolation schedules can each have score cost below `X^-2`.
The all-column square-root thinning still costs less than `4290`.  Hence the
new repair does not affect the required `o(log^2 X)` endpoint scale.

## Replay

```bash
cd experiments/X-91724-factor67-knot-collar-relative-refinement
python3 verify.py
python3 -m py_compile verify.py
sha256sum -c SHA256SUMS
```

Expected:

```text
PASS_FACTOR67_KNOT_COLLAR_RELATIVE_REFINEMENT
```

Proof-object digest:

```text
78b06f7dc034f76c1b65bb0146ec22164588581134dc887771d19315d9b71550
```

## Honest boundary

```text
raw Lipschitz/native-relative inference          refuted exactly
atomless finite activation collars               proved exactly
positive cellwise native-relative refinement     proved exactly
reserve payment and score schedule               proved exactly/conditional
frozen Hall/mismatch/collar/port/endpoint stack   reconstruction required
SONTR / NRCT                                      conditional proposal
Riemann Hypothesis                                unproved
```

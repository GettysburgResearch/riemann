# O-91688 — Three-route closure synthesis after the native-capacity separator

Status: **PROPOSED STRATEGIC SYNTHESIS — NEW LEMMAS SEPARATELY PROVED; RH UNPROVED**  
Created: 2026-08-14

## Frozen fronts

```text
Route A / native thinning:  PR #470  89af3206ea1894884613e1188b5ab9a6a4cd74f0
Route B / root score Hall:  PR #464  2eb70463f3d0ae791a9f140694d2ace7032ae864
Route C / passive string:   PR #453  a9cecbd3228bc26d4d0c3375c9694ee1e836f66a
Near-cut continuation:      PR #461  ea633d416609565b3926f37c9302c93e1b818e2d
```

## Route A — source-owned native thinning

PR #470 proves that the unthinned raw current is natively infeasible and
reduces the closure theorem to `SONTR`. `L-91688` now removes the provenance
ambiguity completely: the rough reservoir has an exact ordered first-owner
partition in every physical coordinate.

The remaining task is no longer “find where the reservoir came from.” It is:

```text
choose current/recursive fractions inside explicit first-owner slices;
use the Y4-zero triangular repair cone;
keep recursive mass below 1/8;
return nonnegative current and bounded weighted slack;
or return an exact activation-cell dual.
```

This route is the most finite and fail-closed.

## Route B — one-shot root Hall and causal envelope

PR #464 already avoids the false stopped-leaf Hall theorem. Its finite Hall
algebra and subcritical causal recursion are exact. The principal uncertainty
is the analytic endpoint realization and one-use correction budget.

`L-91689` proves a universal stability constant on the entire root window:

\[
 \text{unsigned root score mass}<188.
\]

Hence an atom-map error `epsilon` changes one fiber by less than `188 epsilon`,
and a mass-54 root packet by less than `10152 epsilon` before the norm of the
correction operator is applied.

This changes the reconstruction target from an impossible exact
finite/continuum identity to a quantitative compact-window estimate with one
explicit reserve. If those analytic constants close, Route B is the shortest
complete composition because every later generation uses the already exact
causal envelope with recursive mass below `1/8`.

## Route C — finite passive strings

PR #453 reduced RH to finite positive-string membership at all safe packets,
but its dual still appeared to require arbitrary half-line polynomial
positivity.

`L-92112` turns every stage into exactly two truncated Stieltjes-Hankel PSD
tests. A failing eigenvector produces a square-polynomial separator
immediately. The actual zeta problem is therefore:

```text
prove two explicit barycentric Hankel matrices positive at every finite stage;
or identify the first exact square-polynomial obstruction.
```

PR #461 supplies high-axis fractional-string asymptotics through growing order;
the remaining analytic mechanism must control the near-cut boundary layer.
This is the strongest independent non-factor-54 route.

## Cross-route connection

All three routes now have deterministic finite witnesses:

```text
A: first-owner source slices + one activation-cell native-capacity dual;
B: deterministic root Hall + one compact operator-norm reserve inequality;
C: two Hankel matrices + one square-polynomial separator.
```

There is no remaining justification for an opaque global search. The most
promising campaign order is:

1. attack Route B's explicit compact analytic constants because success gives
   the shortest full composition;
2. run Route A's source-owned activation-cell thinning in parallel as the
   arithmetic fallback and independent audit of root ownership;
3. build Route C's exact Hankel packets at increasing safe orders, using PR
   #461 only where its near-cut error is quantitatively controlled.

## Serious resolution path

**A serious full-resolution path is present, but no route is complete.**

The smallest missing theorem on each front is:

```text
A: SONTR — source-owned native thinning with bounded Y4 slack;
B: a compact-window endpoint approximation/reserve inequality satisfying
   the 10152 stability multiplier and all one-use port ownership;
C: all finite barycentric Xi Hankel pairs are PSD, equivalently a uniform
   near-cut positive-string realization.
```

Any one of the three would close its corresponding conditional implication to
RH. None is asserted here.

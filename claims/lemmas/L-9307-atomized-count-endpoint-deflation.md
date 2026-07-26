# L-9307 — Atomized endpoint-count deflation

Claim ID: L-9307  
Title: Exact endpoint counts give a sharper shifted-ordinate deflation profile  
Status: PROPOSED  
Authoring agent: `gpt56-07-c`  
Reviewing agents: none  
Created: 2026-07-26  
Last updated: 2026-07-26  
Dependencies: L-9303, L-9306  
Scope: unconditional total-count reuse in direct completed-xi witnesses  
Related counterexample candidates: none

## Statement

Let

```text
a_0 < a_1 < ... < a_n
```

be exact ordinates at which an unconditional Turing or argument-principle
certificate proves exact total-zero counts `N(a_j)`, counted with multiplicity.
Define exact atom multiplicities

```text
m_j = N(a_(j+1)) - N(a_j) >= 0.
```

For any exact direct-xi ordinate `T`, define

```text
D_j(T) = max(|T-a_j|, |T-a_(j+1)|).
```

Then the open interval `(a_j,a_(j+1))` contains exactly `m_j` nontrivial zeros,
and every such zero has distance at most `D_j(T)` from `T`.

Under RH, the subtraction

```text
sum_j m_j log(u + D_j(T)^2)
```

is therefore licensed in the L-9303 direct-xi modulus hierarchy. Grouping equal
`D_j(T)` values and taking cumulative multiplicities yields a valid nested
total-count profile.

This atomized profile is at least as strong as the L-9306 profile obtained by
widening each symmetric source radius by `|T-C|`.

## Definitions

- `N(t)` counts all nontrivial zeta zeros with `0 < Im rho < t`, with
  multiplicity, under the same endpoint convention used by the count producer.
- Endpoint balls must isolate unique integers.
- Atom intervals use consecutive distinct certified endpoints.
- A zero on an endpoint must be excluded by the count primitive's endpoint
  semantics or handled by a closed-interval convention consistently.

## Motivation

L-9306 treats all mass in one symmetric shell as if it lay at the shell's
farthest shifted endpoint. Exact values of `N` at the left and right endpoints
contain more information: they determine asymmetric consecutive atom counts.
At a shifted target, near-side atoms can then be removed at substantially
smaller radii without identifying any individual zero.

## Proof

By exact endpoint counting,

```text
m_j = N(a_(j+1)) - N(a_j)
```

is the exact number of zeros in the atom interval, with multiplicity. For every
ordinate `gamma` in that interval,

```text
|T-gamma| <= max(|T-a_j|, |T-a_(j+1)|) = D_j(T).
```

Assume RH. The `m_j` zeros are then critical-line zeros whose squared distances
from `T` are bounded above by `D_j(T)^2`. L-9303's order-statistic argument
permits subtraction of the corresponding `m_j` Stieltjes atoms. Summing over
disjoint endpoint atoms cannot double count.

For a symmetric source shell, the L-9306 radius is the maximum distance from
`T` to either outer shell endpoint. Every constituent atom's `D_j(T)` is no
larger. Moving positive mass inward strengthens the removable Stieltjes
measure, proving the dominance statement.

## Analytic domain audit

Every subtraction term is `log(u+D^2)` with `u>0` and `D^2>=0`; it is real
analytic on the tested domain. No contour, branch cut, or completed-xi
normalization is changed.

## Dependency audit

- Exact endpoint differences and interval disjointness are unconditional.
- Only the conversion to critical-line mass assumes RH, inside the
  contradiction argument.
- Complete monotonicity and Loewner positivity follow from L-9303.

## Gap audit

- Endpoint `N` values must be independently reconstructed from unique-integer
  balls; claimed integer fields are not trusted.
- Endpoints must be sorted and duplicate endpoints must carry identical counts.
- Decreasing endpoint counts are rejected.
- Atom counts must not be combined across uncovered gaps.
- A midpoint determinant is not a witness.
- The profile proves only the retained lower mass; zeros outside the endpoint
  span remain in the positive residual.

## Adversarial tests

X-9302 tests:

- derive one atom from one exact source window;
- shift the target by `1/2` and recover the farthest-endpoint radius `3/2`;
- reject inconsistent duplicate endpoint counts;
- reject nonunique endpoint balls and decreasing `N`;
- independently reconstruct every cumulative atomized shell.

## Remaining uncertainty

Independent review is needed for endpoint-open/closed semantics and the
inherited L-9303 normalization. Primitive count and completed-xi computations
also require independent reproduction.

## Suggested next attack

Use all exact endpoint atoms from one expensive count table to scan a rational
mesh of nearby direct-xi ordinates. Escalate only atomized, scale-normalized
negative nominees with an independent backend.

# M-15409 — Adversarial review protocol for the critical local-to-Bohr proof

Methodology ID: `M-15409`  
Title: Freeze, expand, mutate, and independently replay the Farey determinant proof before any RH promotion  
Status: **REVIEW PROTOCOL**  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-07  
Primary claims: `L-15447`, `L-15448`, `T-15414`  
Scope: fail-closed review of the full proposed proof

## 1. Freeze the object

At the start of review, record:

```text
repository: gfreund123/riemann
PR:         #165
branch:     agent/gpt56-05-l/154-nonlocal-barta-floor
head SHA:   exact current head
```

Review that frozen commit. Do not silently consume later branch repairs.

Also freeze the imported source heads:

```text
PR #226  analytic-totient identity, second moment, Jordan Bohr square
PR #224  semiprime H1 and pole tomography
PR #222  signed cubic Type-II cells
PR #216  prime-only Hardy exponent and balanced semiprime Gram
PR #158  repaired double-centered dispersion recurrence
PR #218  curvature-corrected prime transport
PR #217  Brownian SAT/annihilator endpoint
```

The proof itself uses PR #226 plus the new exact arithmetic ledger. The other
heads are independent route replays, not logical dependencies.

## 2. Review order

1. `claims/lemmas/L-15448-critical-farey-selberg-local-to-bohr.md`
2. `claims/theorems/T-15414-critical-local-to-bohr-proposed-proof-of-rh.md`
3. `claims/lemmas/L-15447-joint-inverse-zeta-differential-bridge.md`
4. PR #226 `L-9512`, `L-9513`, `T-9506`
5. exact synthetic checker `X-15415`
6. route-consolidation report and integration note

The main theorem should not receive credit from the correctness of the transfer
layers. The determinant ledger must be reconstructed independently.

## 3. Exact algebra gates

### Gate A — completed packet

Verify for every real `X<=x<=2X`, `D=ceil(2X)`:

\[
2E^{\rm AN}(x)
=S_D(x)+1+{M(D)\over3}
+x^2\sum_{d>D}{\mu(d)\over d^2}.
\]

Mutation tests:

- replace `d>D` by `d>=D`;
- replace `ceil(2X)` by `floor(2X)`;
- drop `M(D)/3`;
- change the strict fractional-part endpoint convention.

Every mutation must fail on a small exact rational example.

### Gate B — reduced rational frequencies

Reconstruct

\[
A_D(a,q)=\sum_{m\le D/q}\mu(qm)c_{am}
\]

with

\[
c_h={i\over2\pi h}+{1\over2\pi^2h^2}.
\]

Require a duplicate-free map from every `(d,h)` to one reduced `(a,q,m)` and
an independent reverse enumeration.

Mutation tests:

- omit negative `h`;
- identify `a/q` and `-a/q`;
- lose the `1/h^2` term;
- replace `mu(qm)` by `mu(q)mu(m)` without the coprimality gate.

### Gate C — determinant numerator

For every off-diagonal reduced pair, verify

\[
r=av-bq,
\qquad
{a\over q}-{b\over v}={r\over qv}.
\]

Expand the four coefficient classes and the polynomial/tail cross terms. The
complete row must be divisible by `r/(qv)` before any interval or absolute value
is applied.

The reviewer must produce a machine-readable table:

```text
row class
source indices
raw coefficient
endpoint contribution
factored coefficient
residual after factoring
```

Every residual must be identically zero in exact arithmetic.

Mutation tests:

- reverse `av-bq` to `aq-bv`;
- omit one endpoint integration-by-parts term;
- remove the quadratic tail `x^2 R_D`;
- use only the odd Fourier coefficient;
- take real parts before pairing conjugates.

### Gate D — multiplicity/summability

Verify that each reduced coefficient appears in only divisor-many factored rows
and that all endpoint rays are included in the additive `D` budget.

The proof may use

\[
2|zw|\le|z|^2+|w|^2,
\qquad
\tau(n)\ll_\varepsilon n^\varepsilon,
\]

but may not use an unproved average cancellation of `mu`.

A reviewer should attempt to construct a family with fixed coefficient norm but
super-divisor row multiplicity. Any such family rejects the proof.

### Gate E — Jordan coverage

Map every coefficient square produced at Gate D into one of the two positive
Jordan ledgers in `L-9513`:

\[
J_2(q)\left(\sum_{q\mid d}{\mu(d)\over d}\right)^2,
\qquad
J_4(q)\left(\sum_{q\mid d}{\mu(d)\over d^2}\right)^2.
\]

No unweighted Mertens square may be inserted outside these ledgers.

## 4. Analytic gates

After the arithmetic theorem passes:

1. confirm `D` is comparable with `X` uniformly;
2. verify dyadic summation of the local second moment;
3. check normal convergence of the Mellin integral on compact subsets of
   `Re s>1/2`;
4. verify `zeta(rho-1)!=0` by the functional equation and Euler product;
5. check multiplicity and endpoint poles at `0,1,2`;
6. confirm the functional-equation reflection gives the full critical line.

These steps must be reviewed independently of the Farey calculation, but they
are not expected to be the fragile part.

## 5. Circularity audit

Reject the proof if any step imports one of the following under another name:

- `M(X)=O(X^(1/2+epsilon))`;
- a zero-free half-plane `Re s>1/2`;
- square-root cancellation for a Möbius or prime bilinear sum;
- PR #217's SAT equality;
- PR #218's cofinal transport-minus-square inequality;
- PR #158's Type-II recurrence;
- finiteness of PR #224's critical vertical integral;
- positivity of every square-screw level.

The exact Jordan Bohr square is unconditional and is permitted.

## 6. Independent computational replay

`X-15415` is only a synthetic algebra regression. A serious review should add:

1. exact rational `X,D` completed-packet comparisons;
2. exhaustive reduced-frequency grouping for small `D`;
3. direct local integration versus grouped kernel integration;
4. exact determinant-row factorization;
5. deliberate endpoint mutations;
6. two independent implementations, one pair-first and one determinant-first.

A floating agreement is insufficient. The central residual must be exactly zero
or enclosed by an interval containing only zero because the expression is
symbolically identical.

## 7. Classification

Use the following verdicts:

```text
VERIFIED
  every gate passes and no circular input is found;

VERIFIED WITH FIXES
  only non-load-bearing notation, endpoint wording, or implementation binding
  needs repair;

GAP/BLOCKED
  determinant divisibility is plausible but one coefficient class or
  summability map is not closed;

REJECTED
  an uncancelled endpoint, wrong determinant factor, super-divisor multiplicity,
  or hidden RH-equivalent estimate is found.
```

A repair proposed after a failed frozen review is a new proposed theorem; it
cannot retroactively verify the frozen claim.

## 8. Promotion rule

Do not change the public status of RH from open on the basis of this branch
until:

1. `L-15448` is independently classified `VERIFIED` or `VERIFIED WITH FIXES`;
2. the transfer theorem `T-9506` is independently reviewed in the same
   normalization;
3. one second implementation reproduces the determinant ledger;
4. all exact endpoint mutations fail closed;
5. the review SHA and final accepted SHA are recorded.

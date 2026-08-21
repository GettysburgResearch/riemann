# R-23803 — The current producer sign is not yet an unconditional closure

Claim ID: `R-23803`  
Title: Exact recurrence algebra and long positivity scans do not establish cofinal binary–ternary producer positivity  
Status: **SCOPE CORRECTION / ADVERSARIAL AUDIT**  
Authoring agent: `gpt56-pro-09-w`  
Created: 2026-08-08  
Issue: #238  
Dependencies: `L-23810`--`L-23814`, `T-23803`

## 1. What is durable

The following parts of the binary–ternary proposal are exact:

1. the target floor-transform inversion `w -> u -> r`;
2. the descending binary–ternary recurrence for `A_X`;
3. exact reconstruction of every target column;
4. the Pascal/divergence identity;
5. the finite conditional deduction `BTF -> RH`;
6. the theorem `L-23814` that producer positivity automatically gives the
   required `O((log X)^2)` BTF rate.

These are useful and independently reviewable.

## 2. What finite reconnaissance does not prove

Large finite scans may show

\[
 A_X(n)\ge0
\]

for all tested endpoints.  Such scans are evidence only.  They do not prove the
cofinal assertion

\[
\boxed{
 A_X(n)\ge0\qquad(2\le n\le X)
}
\tag{R-23803.1}
\]

for every sufficiently large `X`.

Mutation tests of the finite recurrence verify implementation and algebra, not
this all-level sign theorem.

## 3. The weighted rate is no longer a separate hinge

`L-23814` proves that if (R-23803.1) holds, then the exact balanced column load
gives

\[
\boxed{
 \sum_{n=2}^{X}A_X(n)\sqrt n
 =O((\log X)^2).}
\tag{R-23803.2}
\]

Since the coefficients are then nonnegative, this is the absolute weighted
variation required by BTF.  Thus the current producer route has only one open
theorem:

```text
cofinal producer positivity.
```

The scalar half-moment of `L-23812`,

\[
 \mathfrak H_X=-\sum_mr_X(m)\sqrt m,
\]

is an exact diagnostic.  Under positivity it also becomes `O((log X)^2)`.  Its
Dirichlet representation contains `1/zeta(s)`, so it remains a useful mutation
showing that the producer sign cannot be justified by a phase-blind estimate.
It is not an additional hypothesis after `L-23814`.

## 4. Profit/debt obstruction

The alternative attempt to rotate a signed flow until every row is
entropy-profitable is governed by `L-23813`:

\[
 \sum d_{n,j}\pi(n,j)
 =\mathcal P(X)-\mathcal C(X).
\]

Thus an `X^{o(1)}` negative-debt construction directly proves the sharp prime
ramp.  It cannot be inferred from generic flow feasibility alone.

## 5. Correct proposal boundary

The binary–ternary architecture should now be presented as a full
**single-hinge conditional proposal**:

```text
cofinal positivity of the explicit producer
-> O(log^2 X) weighted variation
-> sharp prime ramp
-> square-screw/Landau
-> RH.
```

A genuinely unconditional proposal still needs a proof of producer positivity,
or a different positive transport theorem such as the profitable-debt criterion
of `L-23813`.

## 6. Classification

```text
L-23810 exact inversion/divergence            RETAIN
L-23811 exact recurrence identities           RETAIN
L-23814 positivity -> BTF rate                 RETAIN
T-23803 conditional deduction                 RETAIN
producer positivity as established theorem    NOT PROVED
accepted proof of RH                           NO
```

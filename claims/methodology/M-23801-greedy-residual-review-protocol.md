# M-23801 — Greedy Residual review protocol

Methodology ID: `M-23801`  
Title: Review the carry proposal by one deterministic residual theorem rather than exact inverse positivity  
Status: **PROPOSED REVIEW AND PRODUCTION PROTOCOL**  
Authoring agent: `gpt56-pro-23`  
Created: 2026-08-07  
Issue: #238

## Review order

1. `D-23801` — finite matrix, greedy producer, and residual statistic.
2. `L-23801` — exact carry/Legendre identity, entropy, and coefficient mass.
3. `L-23802` — finite Möbius decoder and continuum mass eight.
4. `L-23803` — global pivot potential and reduction to the final residual.
5. `L-23804` — upper square-screw Landau transfer.
6. `T-23801` — complete conditional composition.
7. `X-23801` — exact finite regression and discovery-only scans.
8. report and integration handoff.

## Load-bearing questions

### Exact carry algebra

- Does `beta_(nq)` equal the average `q`-place carry?
- Are all prime powers retained in the Legendre identity?
- Does every greedy update preserve every residual inequality?
- Are pivot ties resolved exactly or with directed intervals?

### Mass and entropy

- Is `sum_q beta_(nq)/q` uniformly bounded below?
- Does this give `sum d(n)=O(log X)` for every all-column packing?
- Is the entropy error therefore only `O(log^2 X)`?
- Is the required weighted mass exactly `8 sqrt(X)`?

### Potential

- Is `beta_(nq)<=K(n/q)` exact?
- Is the ramp Riemann-sum error in `L-23803` bounded with the stated constant?
- Does `a(q)=2-64/sqrt(q)` satisfy every row inequality?
- Is its initial target potential `8 sqrt(X)+O(log^2 X)`?

### Analytic transfer

- Does the packing lower bound give an upper envelope for `Psi`?
- Is the Landau proof valid after replacing `Psi` by `-Psi`?
- Are the compact correction and real-axis zero-free inputs source bound?

### Greedy Residual theorem

- What exact pivot blocks a positive residual column?
- Can every residual column be charged to a saturated pivot?
- Do complete quotient layers contract only after Möbius recombination?
- Are quotient endpoints and modular holes bounded by `X^(o(1))` in the positive potential?

## Preferred proof decomposition for GR

A review-ready proof should export two lemmas.

### Pivot charging lemma

For every final residual column `q`, emit a decreasing chain of saturated pivot
columns and an exact inequality charging

\[
\left(2-64q^{-1/2}\right)_+\rho(q)
\]

to the first blocking pivot or a declared quotient endpoint.

### Quotient-layer endpoint lemma

Group all charges with

\[
\left\lfloor\frac Xq\right\rfloor=r.
\]

After complete Möbius recombination, prove the sum of the uncharged endpoint
terms is `X^(o(1))` over all `r`.

Together these lemmas prove GR. A stronger diagonal-minimizer invariant is also
accepted.

## Automatic rejection conditions

Reject a claimed proof if it:

```text
assumes positivity of the signed triangular inverse
checks only finitely many X
uses a prime-only matrix while invoking all-column coefficient mass
bounds Möbius terms separately before quotient-layer recombination
loses X^c for any fixed c>0
confuses Psi<=small with a bound on (-Psi)_+
uses reflected two-contact counting without an exact packet-to-obstacle map
uses floating pivot comparisons without outward certification
```

The allowed residual is `O_epsilon(X^epsilon)` for every positive `epsilon`.
An error such as `sqrt(X)/log X` is insufficient.

## Proof-object schema

For each endpoint:

```text
schema version
X and square root N if X=N^2
carry-row generator digest
outward log/sqrt intervals
pivot order and exact tie data
packing coefficient intervals
final residual intervals
positive residual-potential upper bound
weighted mass lower bound
entropy-error upper bound
proof-object SHA-256
```

The global theorem additionally needs a symbolic all-endpoint proof of GR; a
finite family of proof objects is only regression.

## Exact status

```text
finite consumer and producer            reviewable now
potential row theorem                    reviewable now
upper-envelope Landau transfer           reviewable now
Greedy Residual theorem                  open
RH                                       unproved
```

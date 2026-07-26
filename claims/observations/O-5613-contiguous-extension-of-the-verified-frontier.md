# O-5613 — A contiguous 22,801-unit extension of the verified frontier

Claim ID: O-5613
Title: `D = 0` certified over `(3000017499999.5, 3000017522800.5)` — a
contiguous chain abutting the Platt–Trudgian frontier, so every zero of `zeta`
with `0 < Im rho <= 3000017522800.5` is on the critical line
Status: CERTIFIED-COMPUTATION (for the chain; the statement about the full
region below is additionally conditional on the published Platt–Trudgian
verification, an external result)
Authoring agent: `fable5-01`
Reviewing agents: none
Created: 2026-07-26
Last updated: 2026-07-26
Dependencies: X-5604 (Platt engine); the published verification of RH to
height `3.0000175e12` (Platt–Trudgian 2021), imported and not re-derived
Scope: the four slabs below and their union with the published verified region
Related counterexample candidates: none

## What is new here

Every previous certificate in this repository (`O-5608`, `O-5610`, `O-5612`)
is a *spot* certificate: a slab at great height with unverified ocean below
it.  This one is different in kind: it **abuts the exhaustively verified
region** and therefore extends the contiguous statement.

Platt–Trudgian verified RH for all zeros with `0 < Im rho <= 3.0000175e12
= 3000017500000`.  This claim certifies, unconditionally within the X-5604
machinery:

```text
sub-slab                                            N        D    per zero
(3000017499999.5, 3000017500000.5)   stitch          5        0    (seconds)
(3000017500000.5, 3000017507600.5)               32528        0    0.024 s
(3000017507600.5, 3000017515200.5)               32527        0    0.024 s
(3000017515200.5, 3000017522800.5)               32527        0    0.024 s

chain: 97,587 zeros over 22,801 contiguous units, D = 0 everywhere,
all zeros on the critical line, all simple, all rigorously located.
```

Joint consistency is re-derived, not assumed: adjacent sub-slabs share their
boundary dyadic *exactly*, each sub-slab's count gate passed independently
(so no zero is lost at a joint — and no zero sits exactly on a joint, since a
`zeta_nzeros` ball at an ordinate carrying a zero would fail the
unique-integer gate), and the ball chains across each joint are separated by
a positive measured gap (`0.288` and `0.279` at the two interior joints).

**Therefore, combining with the published verification:** every zero of
`zeta` with `0 < Im rho <= 3000017522800.5` lies on the critical line.  The
contiguous verified height moves forward by `22,800.5` units.

## Cost, and what it implies

The three main sub-slabs ran in parallel, one core each: `~13.5` minutes
wall, `0.024` s per zero per worker — `0.008` s per zero aggregate.  At this
rate the contiguous frontier advances at roughly

```text
~ 100,000 zeros  /  13.5 min  /  3 cores  ~  2.8 million zeros per CPU-day
                                          ~  640,000 units of height per CPU-day
```

at heights near `3e12` (the per-zero cost grows like the main sum toward
higher `t`).  Advancing the frontier by a factor of two — to `6e12` — would
need `~1.3e13` more zeros, i.e. `~4,600` CPU-days at this rate: out of reach
for this environment, but squarely in reach of a modest cluster, and the
work shards perfectly (each block of 2000 zeros is independent given its
anchor index).

That is worth stating because the original Platt–Trudgian computation was a
major undertaking; the fact that a pip-installable library plus a ctypes
binding plus fail-closed glue reproduces frontier-grade certification at
this throughput is itself the observation.

## Limitations

1. **The statement about the full region is conditional on Platt–Trudgian.**
   Their verification is imported as published, not re-derived.  The chain
   itself is unconditional within the X-5604 trust model.
2. The chain rests on Arb's `zeta_nzeros` and Platt isolation — the same
   external-library trust class audited in `O-5611` (argument principle,
   second-library `mpmath.nzeros` confirmations, cross-engine sign audits).
3. The exact frontier value `3.0000175e12` is taken from the literature as
   stated; if their verified height were actually lower than that round
   figure, the union claim would inherit the discrepancy.  The stitch slab
   deliberately *overlaps* their region by half a unit to absorb exactly
   this kind of edge ambiguity.
4. `97,587` zeros is `~0.0008%` of the zeros below the new frontier; the
   heavy lifting remains the published computation.

## Reproduction

```bash
cd experiments/X-5604-exact-slab-discrepancy
python3 platt_certify.py --a 6000034999999/2 --b 6000035000001/2 --prec 128 --block 16
for k in 0 1 2; do
  A=$((6000035000001 + 15200*k)); B=$((A + 15200))
  python3 platt_certify.py --a $A/2 --b $B/2 --prec 128 --block 2000 &
done
```

## Suggested next attack

Nothing clever — just more of this, sharded.  The frontier now advances at
`~640k` units per CPU-day with existing, audited tools.  The interesting
research question is orthogonal: whether the close-pair census (`O-5612`),
run *during* frontier advancement at zero marginal cost, ever shows a pair
tight enough to warrant the full Lehmer-quality workup.

## Addendum: the census by-product

Running `gap_census.py` over the chain's `97,582` rigorous ordinate balls
(zero marginal cost — the balls already existed) produced the tightest
certified pair in this project's `156,061` certified zeros:

```text
mean normalised gap over 97,581 gaps    1.00000
GUE-expected minimum (heuristic)        0.0146
observed minimum                        delta = 0.02198  RIGOROUS
  at t = 3000017500950.7515             (950 units past the frontier)
  interior Z at the dyadic midpoint     [-0.000508884472776 +/- 4.6e-16]
```

The interior `|Z| ~ 5.1e-4` is an order of magnitude smaller than the
tightest pair at `t = 10^{13}` (`4.9e-3`), and the `delta` sits at `1.5x` the
GUE-expected minimum for a sample this size — consistent with expectation,
recorded because it is the sharpest certified close-pair object on file.  The
`Z` ball is evaluated at the census midpoint, not at the true interior
extremum, so the true `max |Z|` between the two zeros may be slightly larger;
a Lehmer-quality workup would refine that.

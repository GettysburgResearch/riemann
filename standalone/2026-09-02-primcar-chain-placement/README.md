# The PRIMCAR chain: exact placement

```text
Status:            PROVED (T-109100: PRIMLS <=> RH; L-109103: PRIMCAR is a square function of
                   short sifted Möbius sums), PROVED WITH ONE CITED INPUT (T-109102: RH plus
                   J_{-1}(T) << T^{1+eps} implies the frozen-weight model of PRIMCAR).
                   Neither PRIMCAR, COREAGG, COREWAVE nor RH is proved. RH remains unproved.
Scope:             the chain COREWAVE => COREAGG <=> PRIMCAR => PRIMLS => RH of PRs #757 / #760.
Exact sources or dependencies:
                   PR #757 @ b870366 (FFPS_BOUNDARY_FIELD_PRIMITIVE_PAIR_LARGE_SIEVE_GATE.md,
                   FFPS_PRIMITIVE_PAIR_HARMONIC_INCIDENCE_CARLESON.md);
                   PR #760 @ e3747c9 (FFPS_PRIMITIVE_CORE_WAVELET_CLOSURE.md);
                   Titchmarsh Thm 14.2, 14.25; Montgomery-Vaughan Thm 13.23; Ng (2004); Selberg (1943).
What was actually run:   nothing; the packet is analytic.
Smallest remaining gap:  Theorem B cites Ng's explicit formula for M(x) under RH + J_{-1}.
```

## Result in one paragraph

PR #757 posed PRIMLS as "deliberately stronger than RH" and did not claim the converse.
Theorem A proves `PRIMLS ⟺ RH`: opening the coprimality condition turns every panel into
a Möbius-weighted sum of products of two sieved, twisted Möbius sums, each `≪ y^ε` under
RH uniformly in the sieve modulus, the twist and the endpoint. So the chain contains no
statement below RH. Proposition C identifies what PRIMCAR adds: the height layers of a
panel are `μ(t)t^{-1/2}` times slowly varying arithmetic weights, so PRIMCAR at block
scale `ℓ` is the mean square of Möbius sums over intervals of length `ℓ` at height `H`,
for every `ℓ ≤ H`. That is not known under RH for `ℓ < H^{1-ε}`; Theorem B shows the
frozen-weight model follows from RH together with Gonek's negative second moment
`J_{-1}(T) ≪ T^{1+ε}`. The placement is

```text
RH  <==  PRIMCAR  <==  RH + short-interval Möbius mean square at every scale  <==  RH + J_{-1}(T) << T^{1+eps}.
```

A proof of any of PRIMCAR, COREAGG or COREWAVE is a proof of RH. Read `PROOF.md`.

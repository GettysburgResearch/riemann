# Three-route RH assault — 5 September 2026

**Status:** PROPOSED MATHEMATICS; complete proofs supplied; independent mathematical review required. **RH remains unproved.**

**Scope:** one additive packet pursuing the three routes from the preceding strategy discussion. No historical source, canonical claim, integrated release, production experiment, or formal library is modified.

**Exact base:** `gfreund123/riemann main@6dda8b5125457ed936330229f8c9eb6491728e76`.

**What was actually run:** 447 exact rational finite controls, independently recomputed ordered-pair energies and Schur complements, and 17 unit/rejection tests; both ordinary and optimized Python runs passed. These authenticate finite algebra, not infinite analytic theorems. No Lean build, broad zero/prime scan, directed numerical certificate, or independent referee review was run.

**Smallest remaining gaps:** a positive scalar theta determinant; a new signed Möbius estimate in a fixed frequency window; an arithmetic bound for the conditioned horizontal Schur defect with a complete tail ledger.

## The three routes and the results of this pass

| Route | New work in this packet | Still missing |
|---|---|---|
| 1. Theta source → positive operator | A source-coefficient-defined trace-class companion whose Fredholm determinant is exactly invariant xi; a strict obstruction to preserving the actual theta occupation labels in a positive determinant; a direct-integral compactness correction; explicit scalar covariance/cumulant debts | Positivity of a scalar realization, or all-order scalar coefficient signs. The constructed companion is explicitly nonpositive. |
| 2. Möbius source → cancellation | An exact two-sided comparison with **any fixed frequency ensemble of finite second moment**, reducing the ratio-67 energy to `[1,2]` up to logarithmic factors; the sharp causal `L^2` twist-transport constant | Any new arithmetic power saving. Frequency transport alone cannot contract the exponent. |
| 3. One off-line zero → Hilbert contradiction | An exact basis-free positive-surplus identity; an explicit positive definite horizontal Schur matrix; sharp single-pair surplus; a tail-error survival criterion; sixth-order and all-depth screening laws | A source-specific arithmetic estimate that controls the conditioned defect at an unaveraged scale. |

The strongest constructive result is Route 3's surplus identity. Route 1 produces an actual scalar determinant while ruling out an attractive stronger marked construction. Route 2 gives a much smaller exact target but no new cancellation theorem. These are different levels of progress; the packet does not describe all three as advances in the zero-free region.

## Read in this order

1. [Route map and continuation](ROUTES_AND_NEXT_PASS.md).
2. [Horizontal-surplus theorem](proofs/R3_HORIZONTAL_SURPLUS_IDENTITY.md).
3. [Screening and conditioning](proofs/R3_SCREENING_AND_CONDITIONING.md).
4. [Theta determinant and marked obstruction](proofs/R1_SOURCE_DETERMINANT_AND_MARKED_OBSTRUCTION.md).
5. [Fixed-frequency Möbius reduction](proofs/R2_FIXED_FREQUENCY_AND_SHARP_TRANSPORT.md).
6. [Claim ledger](CLAIMS.tsv), [self-audit](SELF_AUDIT.md), [sources](SOURCES.md), and [validation](VALIDATION.md).

## Main theorem: the retained horizontal surplus

For a finite conjugation-invariant multiset with total multiplicity `M`, `S` simple real points, and pair energy `E`, the packet proves

\[
 E-(2M-S)=2d+2\ell+4h_E+8h_N+\mathcal R,
\]

with every term nonnegative and all quantities defined by an intrinsic three-step Hilbert-space flag. Moreover,

\[
 H=C^*C-C^*B(B^*B)^{-1}B^*C,\qquad h_N=\operatorname{Tr}H,
\]

is positive definite precisely when the finite packet has nonreal pairs. Thus

\[
 E\ge2M-S+8\operatorname{Tr}H+4\operatorname{Tr}(H^2).
\]

For simple packets with `q` conjugate pairs,

\[
 E\ge2M-S+8h_N+8h_N^2/q,
\]

with equality for one pair and no real points. This makes an additional matrix-valued defect explicit rather than discarding it in a counting inequality.

The important limitation is proved, not merely cautioned: for a single nonreal pair at displacement `y` and two close real neighbors, the conditioned gap can scale as `y^6/1575` rather than `y^2/3`. The arithmetic continuation must control that conditioning.

## Scientific boundary

No positive scalar theta operator, Möbius exponent improvement, new zero proportion, all-zero bound, or RH proof is claimed. All construction and obstruction claims have complete arguments but remain proposed until independently reviewed. The mechanisms are built from standard Fredholm, Abel/Plancherel, and Hilbert/Schur theory; external novelty and priority are not asserted.

Packet IDs `R1.*`, `R2.*`, and `R3.*` are local to this directory and do not allocate or overwrite historical numerical claim IDs.

# Checks: how to rerun the Lemma 18.1 review scripts, and what they do and do not authenticate

```text
Status: PROPOSED (part of an integration packet draft). These are review instruments: finite,
  small-scale checks written by the bounded agent reviewers. They are not proof-producing
  computations and not certificates.
Scope: the seven scripts behind L18a, L18b, L18c, L13 and SEC4, plus their shared modules
  a2/eis.py and numerics/eisenstein.py
Exact sources or dependencies: scripts at commit c8515d4ea045e7b685f53feb6dd801bf0f529211
  (hashes in §1); manuscript paper.tex SHA-256
  42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3 (no script reads it)
What was actually run (2026-10-10, 16:51-16:54 UTC, nice -n 10, one process at a time):
  lemma18_ledger.py 14/14; lemma18_local.py 283 checks; lemma18_support_checks.py 24/24;
  lemma18_case2_ledger.py 50/50; sep30_l13_checks.py 33/33; sep30_sec4_checks.py in quick mode,
  ALL PASS (38 PASS lines); lemma18_moments.py on K = 1e3, 3e3, 1e4 only. All exited 0 with
  empty stderr.
  Not rerun: the full sec4 run (1252 s), the large-K moment runs (205-321 s each, several in
  sequence), and sep30_junction_check.py.
Smallest remaining gap: none of these checks replays an analytic estimate of Lemma 18.1. The
  load-bearing verification is the hand reading recorded in the reviews.
```

RH remains unsolved. Passing these checks says nothing about RH. It also does not establish
Lemma 18.1. The scripts test conventions, exact finite identities and exponent bookkeeping on
small instances, plus floating-point moments at small `K`.

## 0. Environment and conventions

**Environment used for the rerun.** Python 3.13.16, numpy 2.5.3, sympy 1.14.0, mpmath 1.3.0, on
Linux with 4 cores. The load average was about 3.8. The coordinator reported that the session
disk was full for a few minutes before about 16:57 UTC, overlapping these runs. Every run exited
0, every stderr was empty, every output was complete, and every value matched the reviews, so no
run was affected. Outputs were written to the session scratchpad, not to the repository.

**How to run.**

* Use `nice -n 10 python3 -I -B`.
  * `-I` (isolated mode) keeps the current directory and `PYTHON*` variables off the import path.
    The scripts add `../a2` or `../numerics` to `sys.path` themselves, from their own location.
  * `-B` stops `.pyc` files from being written into `reviews/__pycache__/`.
* Run from any directory; pass absolute or repository-relative script paths.
* Write the JSON outputs of `sep30_sec4_checks.py` and `lemma18_moments.py` **outside the
  repository**.

**Arithmetic classes** (vocabulary of [CONTRIBUTING.md](../../../../../CONTRIBUTING.md#computational-artifacts)):

* `EXACT_RATIONAL`: Fractions, sympy rationals, or integer arithmetic in `Z[ω]` or `Z[ζ_L]`.
* `FLOATING_RECONNAISSANCE`: ordinary double precision. It is neither directed nor certified.
* `NON_DIRECTED_HIGH_PRECISION`: mpmath at 25-60 digits.
* No check here is `DIRECTED_INTERVAL` or `CERTIFIED_INTEGER_COVERAGE`.

**Verify the scripts before running.** From `research/exploratory/qrh-2026-10/`:

```sh
sha256sum -c <<'EOF'
fc965201564ed3f74e26269498376ff8260aee4fc0abe1380b2b16e137f65a3c  reviews/lemma18_ledger.py
874d643f5fcbcf297262174ee266763d6b1f95460932fe0d8c6be07d66d2d2db  reviews/lemma18_local.py
7fad465776f2513f4b06a10fe03973c4e5ec2c3b2c2a612a307ca9cc14dc1abe  reviews/lemma18_moments.py
509a3dbb2c4aafb0f7f63db073becf22204b33d9d8e298d07a2566386f2d2c7b  reviews/lemma18_support_checks.py
7a7c0d2d09107f9608338261eb0f21529011fc7f80f22c03cbe33aabe960a3f9  reviews/lemma18_case2_ledger.py
d1587c070646425eded2887e68024964662bd16671afd05cf72ae81aafd5278d  reviews/sep30_l13_checks.py
3c656a22e8ae7aa9e1bcdd848268010590e6ce71821bee5b2a089179a5bb9c97  reviews/sep30_sec4_checks.py
87ca11d98bf3ee130a6dab613b5f7efe444058320b7c22b005327686f2798e65  a2/eis.py
bc6af6580f96da8e930634fb4d6af70a1f74654dac2b53f04101da411e584ae9  numerics/eisenstein.py
EOF
```

All nine lines printed `OK` for this draft.

* **Hashes recorded in the reviews.** Five script hashes match the hash recorded in their review:
  `lemma18_ledger.py`, `lemma18_support_checks.py`, `lemma18_case2_ledger.py`,
  `sep30_l13_checks.py` and `a2/eis.py`. `numerics/eisenstein.py` matches L18a's prefix
  `bc6af658…e584ae9`.
* **Hashes not recorded.** `lemma18_local.py` and `lemma18_moments.py` have no recorded hash.
  `SEP30_SEC4_REVIEW.md` says "sha256 in Sec. 8", but its Sec. 8 gives none. For these three, the
  hash above is that of the file at `c8515d4ea`.

**Re-extract and hash the manuscript.** The scripts do not read it; this step binds the line
numbers.

```sh
git show pr908:standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex | sha256sum
# expect 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3 (16,677 lines)
```

## 1. The scripts

### 1.1 `reviews/lemma18_ledger.py` (L18a: exponent ledgers of case 1 and case 2)

| Field | Value |
|---|---|
| SHA-256 / git blob / size | `fc965201…7f65a3c` / `8a028b08` / 161 lines (last changed `1c257757c`) |
| Dependencies | sympy, `fractions` |
| Command | `nice -n 10 python3 -I -B reviews/lemma18_ledger.py` |
| Wall time | review: 6 s; this rerun: 7 s |
| Arithmetic class | `EXACT_RATIONAL` |
| Pass rule | final line `SUMMARY: 14/14 checks passed`, exit 0 |
| This rerun | 14/14, exit 0. Stdout SHA-256 `8d7e851a43cadf1dff3ed483d42494fe42d461f2e0468fae5a0a7d92e6e88a25` (deterministic) |

**What it authenticates.**

* As symbolic identities: (2.13), (2.12), (2.15)-(2.16), the intermediate form of (2.15), (3.14)
  and the first-transform ledger.
* (2.6) prime by prime for all `1 ≤ j ≤ i < 200`.
* The `F_2 ≥ 2b_2/3` table for `i < 120`.
* (2.19) on a grid of `v ∈ [0, 3M]`.
* The comparison margins: `z = 0` gives `A_comp − 5M/6 ≤ −M/6` before `ξ`. For `z > 0`, the grid
  maxima are `1063/1400 < 23/30` and `647/700 < 14/15`.

**What it does not authenticate.** It does not check that the displayed ledgers describe the
analysis; that was read. The (2.19) and comparison checks are on grids. L18c K1 gives the exact
suprema `16/21` and `13/14`.

### 1.2 `reviews/lemma18_local.py` (L18a: local Gauss sums)

| Field | Value |
|---|---|
| SHA-256 / git blob / size | `874d643f…66d2d2db` / `5d37abe4` / 77 lines (`1c257757c`) |
| Dependencies | numpy, `numerics/eisenstein.py` |
| Command | `nice -n 10 python3 -I -B reviews/lemma18_local.py` |
| Wall time | this rerun: 3 s |
| Arithmetic class | `FLOATING_RECONNAISSANCE`; exact symbols |
| Pass rule | one line `gauss-local: 283 checks, max relative deviation …`; exit 0. The script asserts a maximum deviation below `1e-8` |
| This rerun | `gauss-local: 283 checks, max relative deviation 2.18e-16` (review: `2e-16`). Stdout `ad3f810f…dbc146` |

**What it authenticates.** eq:gauss-local (Lemma 13.2, 7056-7079) on 283 split prime powers,
including the `6 | a` branch. **Superseded** by L13's exact check D2 (797 values, exact in
`Z[ζ_L]`).

**What it does not authenticate.** Inert primes, and Lemma 13.2 for all moduli (the proof was
read in L13 §3).

### 1.3 `reviews/lemma18_support_checks.py` (L18b: common-support allocations)

| Field | Value |
|---|---|
| SHA-256 / git blob / size | `509a3dbb…2f2c7b` / `a859a688` / 709 lines (`fb7c6d4a6`) |
| Dependencies | numpy, `a2/eis.py`; seeded `random.Random` |
| Command | `nice -n 10 python3 -I -B reviews/lemma18_support_checks.py` |
| Wall time | review: about 24-30 s; this rerun: 24 s |
| Arithmetic class | MIXED. A1-A5, L1-L4 and B1 are exact; B2-B4, D, E and F are `FLOATING_RECONNAISSANCE` with exact symbols |
| Pass rule | final line `24/24 PASS`, exit 0 |
| This rerun | 24/24. Every value matches the review's printed block. The review condenses the D and E lines; the script prints `lhs`/`rhs` and five E configurations. Stdout `0b9c7dbf…e7f27f` (deterministic; seeded) |

**What it authenticates.**

* The bijection of the common-support decomposition (A1).
* `R ≤ p`, `E ≤ p − R` (A2).
* (2.6) on 20,000 random multi-prime configurations, with zero slack exactly at local types
  `(1,1)` and `(2,1)` (A3).
* The Möbius and `𝔱`-allocation identities (A4, A5), and ledgers L1-L4. L4 shows that (2.19) is
  maximised exactly at `v = L` with value `A − M`.
* The row-character factorisation, the primitivity of `ξ_𝔯`, CRT, and the four-class reciprocity
  ratio on 3298 pairs (B1-B4).
* **D, the strongest check:** the first-transform bridge, both sides, on four common-support
  configurations, agreeing to `≤ 6.5e-13`. Negative controls are detected: dropping the
  `𝔢`-sum, dropping `ξ_𝔯(𝔢)`, and `1/(q_aq_b)` for `1/√(q_aq_b)`. Dropping `R̄(a,b)` is detected
  only in the fourth configuration, the one where `R(a,b) = −1`; elsewhere the control is printed
  as "not applicable/undetected".
* The complete-support correlation (E) and the single-prime correlation and local table (F).

**What it does not authenticate.**

* The kernel (`Φ̂_1`) in D is a shifted Gaussian, not the paper's radial kernel.
* The Fourier-measure `L¹` bounds, tails and induction.
* Lemma 4.4 as a theorem: B4 checks it only on small pairs.

### 1.4 `reviews/lemma18_case2_ledger.py` (L18c: case 2 and Sec. 18.8)

| Field | Value |
|---|---|
| SHA-256 / git blob / size | `7a7c0d2d…e960a3f9` / `763b5efa` / 660 lines (`e45f655b3`) |
| Dependencies | sympy, numpy, `fractions`; seeded `random.Random(20261010)` |
| Command | `nice -n 10 python3 -I -B reviews/lemma18_case2_ledger.py` |
| Wall time | review: 24 s; this rerun: 22 s |
| Arithmetic class | `EXACT_RATIONAL`, except G2 and G3 (floating sextic Gauss sums, tolerance `1e-9`) |
| Pass rule | final line `50/50 PASS (17 of them failing controls detected)`, exit 0 |
| This rerun | 50/50 with 17 controls detected. Stdout `e69a8abd…ec408ee` |

**What it authenticates.**

* Case 2 ledgers: the amplifier local values (G1-G3), (2.12)-(2.13) for the four norm types (A),
  (3.14)-(3.16), the greedy removal and the edge cost (C).
* The zero-slack points Z1-Z4, with mutations that break Z4.
* The exact comparison suprema `16/21` and `13/14` (K1).
* The Sec. 18.8 choice order and depth (S1-S3), with controls showing that a per-edge `σ/6` loss
  or summed terminal losses would fail.

**What it does not authenticate.** Any analytic estimate. **Case 1 relies on it only for the
completion checks S1-S3 and Z1-Z3**; its other content is case 2.

### 1.5 `reviews/sep30_l13_checks.py` (L13: Lemmas 13.2-13.4, 4.5)

| Field | Value |
|---|---|
| SHA-256 / git blob / size | `d1587c07…aafd5278d` / `06a26421` / 951 lines (`7ac3cf7b3`) |
| Dependencies | numpy, sympy (cyclotomic polynomials), `a2/eis.py`; seeded |
| Command | `nice -n 10 python3 -I -B reviews/sep30_l13_checks.py` |
| Wall time | review: 114 s; this rerun: 113 s |
| Arithmetic class | A, B, C, D and X are `EXACT_RATIONAL` (integers in `Z[ω]`, `Z[ζ_L]` mod `Φ_L`); S is `FLOATING_RECONNAISSANCE` |
| Pass rule | final line `33/33 PASS   (<s> s)`, exit 0 |
| This rerun | 33/33. The PASS lines are **identical** to the review's printed block once the timing is removed. Stdout `b0e34d3c…ab39e2b` (contains a timing) |

**What it authenticates.**

* Lemma 13.3 exactly on 21 configurations (2,631,375 values of `j`), with its local factors on
  291,296 cases (A, B).
* Lemma 13.4 on 15 configurations (C), with each `R`-factor equal to `−1` somewhere.
* Lemma 13.2 exactly (D2).
* The paper's own warnings that the artificial extensions differ from the genuine sums (X1, X2).
* Thirteen mutation controls.
* Lemma 4.5's integration-by-parts identity, order count and Sobolev constant (S, floating).

**What it does not authenticate.** The use of these lemmas inside Lemma 18.1 with the claimed
uniformity, and Lemma 4.4 beyond the pairs used (A5).

### 1.6 `reviews/sep30_sec4_checks.py` (SEC4: Lemmas 4.1, 4.6-4.10, 13.1)

| Field | Value |
|---|---|
| SHA-256 / git blob / size | `3c656a22…a5bb9c97` / `bc303a6c` / 951 lines (`ba5090e6a`). The review records no hash |
| Dependencies | numpy, sympy, mpmath, `a2/eis.py` (its hash is asserted at start-up) |
| Command | full: `nice -n 10 python3 -I -B reviews/sep30_sec4_checks.py OUT.json`; quick: add the argument `quick` |
| Wall time | full (review): 1252 s; quick (this rerun): 58 s |
| Arithmetic class | A is exact in `Z[ω]` (refutations by exact collision are proofs; minimal moduli are EMPIRICAL); D and E are `NON_DIRECTED_HIGH_PRECISION`; B, C, F and G are `FLOATING_RECONNAISSANCE` |
| Pass rule | final lines `ALL PASS` and `total <s>s`, exit 0 |
| This rerun | **quick mode only**: ALL PASS, 38 PASS lines (the full log `reviews/results/sec4_full.log` has 42). Quick mode uses prime ideals up to norm 6000 (778 ideals) instead of 30,000, and fewer D2/E1 cases. Stdout `4ee22c13…a185bd`; JSON `5ab3398c…9c65c2d5` (contains timings) |

**What it authenticates (full run, per SEC4 §8).** Lemma 4.1's Kummer conductors, with every
strict divisor refuted by exact collisions. Lemma 4.8's functional equation and explicit constant
`C ≈ 0.69`. Lemma 4.9's three-circle chain on sample cases. Lemma 4.10 on 3000 random trials.

**What it does not authenticate.** Lemmas 4.8-4.9 for all characters. The constant `C` is
computed by mpmath on a grid and is not certified. The quick rerun reproduces a subset only; the
full run was not repeated (over 5 minutes).

### 1.7 `reviews/lemma18_moments.py` (L18a §4: EMPIRICAL moments of case 1)

| Field | Value |
|---|---|
| SHA-256 / git blob / size | `7fad4657…14dc1abe` / `c26991f6` / 272 lines (`1c257757c`) |
| Dependencies | numpy, `numerics/eisenstein.py` (self-test 2400 checks) |
| Command | `nice -n 10 python3 -I -B reviews/lemma18_moments.py OUT.json K1,K2,... MODE [chunk]`, with `MODE ∈ {bal, sq, long}` |
| Wall time | review: 30-321 s per recorded run; this rerun (`1e3,3e3,1e4 bal 65536`): about 1 s |
| Arithmetic class | `FLOATING_RECONNAISSANCE` with exact symbols |
| Pass rule | none; it reports moments |
| This rerun | three `K` values. After the timing field is removed, every recorded field is **bit-identical** to `reviews/results/lemma18_bal.json` (SHA-256 `7a512f83…16b2823`). The rerun adds one key, `second_moment_mean_R0`, which the recorded file lacks, presumably because the recorded run predates the final script; the review quotes these second moments separately. JSON `1faccb45…cc5f81` |

Rerun values (mean over `ℛ_0` of `|S S|²`, its ratio to the generalised diagonal, and the share
of the excluded principal rows):

| K | rows | (N1, N2) | mean over ℛ_0 | ratio to diagonal | principal / ℛ_0 |
|---:|---:|---|---:|---:|---:|
| 1e3 | 3 642 | (32, 32) | 0.021717 | 1.0025 | 0.0085 |
| 3e3 | 10 890 | (55, 55) | 0.009915 | 1.0178 | 0.0104 |
| 1e4 | 36 294 | (100, 100) | 0.013266 | 0.9845 | 0.0146 |
| 1e4 | 36 294 | (10, 1000) | 0.003482 | 1.0003 | 0.0279 |

**What it authenticates.** Nothing about the proof. It shows that the balanced fourth moment is
flat and close to the diagonal on a small range. L18a §4 records the range up to `K = 3·10⁶`.

**What it does not authenticate.** It cannot distinguish `K^ε` from a constant, cannot see beyond
its range, and is floating point. Its family convention differs slightly from the lemma's:
`S = {(2), (λ)}`, `τ = 1`, and all ideals prime to 6.

## 2. Summary of this rerun

| Script | Exit | Result | Comparison with the review |
|---|---|---|---|
| `lemma18_ledger.py` | 0 | 14/14 | same count and maxima |
| `lemma18_local.py` | 0 | 283 checks, `2.18e-16` | same |
| `lemma18_support_checks.py` | 0 | 24/24 | values identical; the review condenses the printed format |
| `lemma18_case2_ledger.py` | 0 | 50/50 (17 controls) | same |
| `sep30_l13_checks.py` | 0 | 33/33 | PASS lines identical apart from timing |
| `sep30_sec4_checks.py` (quick) | 0 | ALL PASS (38) | subset of the recorded full run (42 PASS, 1252 s) |
| `lemma18_moments.py` (3 small K) | 0 | moments | bit-identical to the recorded JSON on all common fields |

**Not rerun.**

* `sep30_sec4_checks.py` in full (1252 s in the review).
* `lemma18_moments.py` at `K ≥ 3·10⁴` (the review's runs took 30-321 s each and were chained).
* `sep30_junction_check.py`. It concerns the use in Prop 19.2, not case 1 as a standalone
  statement.
* The cubic spin-off scripts.

## 3. Independence and limits

* **Authorship.** The same family of agent reviewers wrote and ran every script. This rerun
  repeats their computations; it is not an independent implementation.
* **Code paths.** Three implementations of the symbols are involved: `a2/eis.py` (L18b, L13,
  SEC4), `numerics/eisenstein.py` (L18a), and the internal arithmetic of the ledger scripts. They
  were not cross-checked against one another for this draft.
* **No primitive data.** No script reads external data. Each one recomputes from definitions, so
  there is no primitive-replay or coverage contract to authenticate.
* **Small, finite scales.** Norms are at most about `10⁶`, and the moments use `K ≤ 3·10⁶` (at most
  `10⁴` in this rerun).
* **What would be needed.** An independent reviewer should treat these checks as evidence that
  conventions, finite identities and exponent ledgers are right. They are not evidence for any
  estimate. The load-bearing step, the centred Θ-row cancellation (README §8), has no mechanical
  check beyond the ledger identity L4 and the grid check of (2.19).

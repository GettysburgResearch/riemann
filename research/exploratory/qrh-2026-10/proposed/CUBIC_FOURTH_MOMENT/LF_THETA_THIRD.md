# (LF) at θ = 1/3: the F_2 ledger formula of Lemma 4.G, re-derived with θ generic

```text
Status:      PROPOSED (exploratory, unreviewed, not integrated). RH is not addressed. Verdict:
             (LF) is DERIVED at theta = 1/3. It is an exact algebraic consequence of the
             manuscript's theta-free ledger definitions together with the cubic exceptional-row
             count Z^{(m'-f)/3}, f = v_1 (Corollary 4.H(3)-(4) of LEMMAS_4BCD_GH.md). The count
             exponent is the only place where theta enters. Lemma 4.G (the F_2 table, kappa_2 = 1)
             therefore no longer depends on (LF) as an import. It still depends on Corollary
             4.H(4), whose input A4 is unchanged (see gap). Inside a CONDITIONAL scheme
             (SKETCH.md, Theorem C4); nothing here is evidence for a global statement.
Scope:       one finite exponent-ledger identity, (old-eq:2.15)-(old-eq:2.16), case z = 0 of the
             manuscript's Lemma 18.1 proof, with theta = 1/n symbolic and then n = 3. This
             note does not show that the ledger describes the analysis. That is the
             inherited order-free core (A) of CUBIC_N3_GAPS Sec. 4.
Exact sources or dependencies:
             manuscript paper.tex at commit 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6,
             path standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/
             The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex,
             sha256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3 (re-hashed
             here; read as untrusted data). Lines read: 13270-13300 (K_0, (2.3)), 13405-13445
             ((2.7), (2.8)), 13555-13575 ((2.10)), 13596-13940 (second transform through (2.14)),
             14300-14540 (Theta rows, (2.15)-(2.17), F_2 table).
             This directory: LEMMAS_4BCD_GH.md (Sec. 4 Corollary 4.H, Sec. 5 Lemma 4.G),
             SKETCH.md Sec. 4. ../../CUBIC_N3_GAPS.md ([L1], [T1]-[T3]);
             ../../reviews/CUBIC_ALLOCATION_LOSS.md (Sec. 1.2, 2: F_2 = b_2 tight types);
             ../../scripts/cubic_local_checks.py part_L (the [L1] sympy identity, read only).
             Repo HEAD at time of writing: 63bbcc04022f3d381f52539daf6bb843cac6c88a.
What was actually run:
             nice -n 10 python3 -I lf_theta_third_checks.py (this directory)
             -> lf_theta_third_checks.out: 14/14 checks PASS; 7/7 failing controls detected;
             under 1 s, one process. Script sha256 daee1ba0...20d2870, output sha256
             3cf1cc40...94f9c. Arithmetic: sympy polynomial identities in a free symbol theta;
             Fractions; exact integer residue symbols on Z[omega]. No floating point. No Lean,
             lake or comparator process.
Smallest remaining gap:
             (i) Corollary 4.H(4): at a nonunit equal-multiplicity second-transform prime with
             i = 1, there is no older moving character (manuscript l. 14352-14353). This gives
             e_p = 2, residue 1 mod 3, and f = v_1. Its stated basis is the order-free support
             disjointness at l. 14317-14324, which is not re-derived here.
             (ii) The theta-free definitions (2.7), (2.13), (2.14), the exponent table
             l. 13846-13861 and the volume exponent a_0 - b_2 are inherited as the manuscript's
             bookkeeping (core (A)). They contain no n and need no change at n = 3.
```

Notation is that of LEMMAS_4BCD_GH.md Sec. 5 and the manuscript. Every exponent is in `log_Z`
units, and `θ = 1/n` with `n` the order of the residue symbol.

## 0. Verdict

**(LF) holds at θ = 1/3 (PROPOSED, derived).** Section 3 rewrites the manuscript's derivation of
(old-eq:2.15)-(old-eq:2.16) with `θ` a free symbol. It yields

    F_2(θ) = 2b_2 − (1−θ)g_2 − p_2 + t_2 + θV + θf,                                    (LF_θ)

where `f` is any valid lower bound for `log_Z q_{𝔥_0}` contributed by the forced residues. At
`θ = 1/6` with the manuscript's `f = 2v_1`, this is (old-eq:2.16) verbatim. At `θ = 1/3` with
`f = v_1`, it is (LF). The only `θ` input in the whole ledger is the exponent `θ(m' − f)` of the
exceptional-row count. Every other ingredient is `θ`-free.

Both alternatives in the task are excluded:

* No different formula arises: the split into `F_1` and `F_2` is forced ([A5]).
* No step fails to generalise: the only `n`-dependent ingredients are the count exponent and the
  selection rule for `t_2`, `V`. Both are supplied at `n = 3` by Corollary 4.H(3) and Lemma 4.G(a),
  which are already proved in LEMMAS_4BCD_GH.md.

**One transcription hazard, flagged.** The manuscript defines `f = 2v_1` (l. 14350); (LF) uses
`f = v_1`. Both contribute `v_1/3` per unit length, because `(2v_1)/6 = v_1/3`. A literal
`6 → 3` transcription that kept `f = 2v_1` would claim `2v_1/3`. That claim is false: it would
need `q_{𝔥_0} ≥ Z^{2v_1}`, but at `n = 3` the exceptional row `h' = p` has norm `q_p^1`
([B3], [B-CTRL1]). It would also manufacture an unearned spare of `1/3` at nonunit `i = 1`
([C-CTRL2]).

## 1. (LF) exactly as used

LEMMAS_4BCD_GH.md Sec. 5, Lemma 4.G: let `D_2, E_2` be the second-transform moduli with complete
common support. Define:

* `c_2, d_2`: their log-norms; `b_2 = (c_2 + d_2)/2`;
* `G_c = (D_2, E_2)`, `g_2 = log_Z q_{G_c}`;
* `p_2`: the log-norm of the common radical;
* `t_2` (resp. `V`): the radical length of the equal-multiplicity primes with `3 ∤ i` at which
  `j/G_c` is a unit (resp. nonunit);
* `f = v_1`: the radical length of the nonunit primes with `i = 1`.

Then

    F_2 = 2b_2 − (2/3)g_2 − p_2 + t_2 + V/3 + f/3.                                       (LF)

In 4.G, (LF) is used only as a per-prime additive formula. It produces the table in Sec. 5(b)
there and `κ_2 = 1`. Here "`F_2`" means the second-transform part of the identity

    θ(m' − f) + a_0 − b_2 − (M' + Δ_child) = A − (1−θ)M − F_1 − F_2              (old-eq:2.15)_θ

at `θ = 1/3`. Its left side is the exceptional count, plus the volume, minus the child allowance.

## 2. The manuscript's derivation, line by line, with every θ-entry marked

`[θ]` marks a place where the order `n = 6` (`θ = 1/6`, a sixth power or root, "mod six") enters;
`[free]` marks a `θ`-generic one. Lines refer to paper.tex at the commit above.

| lines | content | mark | n = 3 replacement / status |
|---|---|---|---|
| 13284 | `K_0 = 2A − c − d + R + E − m` (first-transform frequency scale) | free | unchanged |
| 13293 | (2.3): `q̃ = q + R + E` | free | unchanged (which primes are in `R` is `n`-dependent; that sits in `F_1`, not `F_2`) |
| 13417-13423 | `a_0 = A − c − w`; (2.7): `Λ_c = a_0 + q̃ + w_o + w + B_c − s_0 + ε_G` | free in form | `B_c` is the cubic allowance (in `F_1` only) |
| 13441-13446 | (2.8): `J = d − c + (K_0 − K) − 2w + w_o` | free | unchanged |
| 13706, 13710 | one-sided residual `χ_p(j)^i`; unequal case nonzero only if `6 | j_0` | θ | `3 | j_0` (Lemma 4.B Corollary) |
| 13727-13732 | `c_2, d_2, b_2, p_2, G_c, g_2` | free | unchanged |
| 13733-13738 | unit/nonunit split at equal `i ≢ 0 (mod 6)`; `t_2`, `V_id`, `V` | θ (selection) | `3 ∤ i` (Lemma 4.G(a)); control [C-CTRL3] |
| 13744-13750 | absolute table (`6 ∤ i`, `6 | i`, `6 | j_0`) | θ | cubic table, Lemma 4.G(a), [G0] of lemmas_4bcd_gh_checks |
| 13752-13762 | partitioned scalar `/ Z^{g_2 − t_2}` has modulus `≤ 1` | free in form | holds at `n = 3` by 4.G(a) |
| 13767-13789 | `e_p = v_p(G_cV_id) mod 6`; active primes lie in the `t_2` or `V` set; a nonunit prime with `e_p = 0` "counted in `V` only enlarges the bound"; moving support `≤ q̃ + w_o + t_2 + V` | θ (`mod 6`) | `mod 3`. Unit, `3 ∤ i`: `e_p = i ≢ 0`, active. Nonunit: `e_p = i + 1`, inactive at `i ≡ 2 (mod 3)`, and the same enlargement remark covers it. Equal `3 | i` and unequal `3 | j_0`: `e_p = 0`. The bound `q̃ + w_o + t_2 + V` is unchanged |
| 13790-13800 | (2.13): `m' = 2a_0 − K − g − g_2 − V`, `q' = q̃ + w_o + t_2 + V`, `M' = m' + q' = M + J − g − g_2 + t_2 ≤ M − σ` | free | unchanged ([A2]) |
| 13801-13827 | `δ_fr,2`, `m'_act` | free | unchanged |
| 13846-13861 | exponent table: `−a_0`, `K + g − a_0`, `−ℓ`, `p_2 − s_0`, `g_2 − t_2`, `a_0 − b_2`; their sum | free | unchanged |
| 13862-13873 | (2.14): allowance `M' + Δ_child`, `Δ_child = b_2 − p_2 + w + B_c + ℓ` | free | unchanged ([A1]: equals (2.7) minus the table) |
| 14317-14324 | second-transform radical disjoint from the old moving support (zero-extended `τ_1(D_2)`, `τ_1(E_2)`, old masks) | free | basis of A4; not re-derived |
| 14336-14347 | fixed-ray reduction; "valuations modulo six"; "sextic exponent" | θ | Lemma 4.H(5), Corollary 4.H(1) |
| 14349-14350 | `v_1`; **`f = 2v_1`** | θ (convention) | **`f = v_1`** (Sec. 4 below) |
| 14351-14357 | valuation of `G_cV_id` is 2; no older moving character (A4); `v_p(h') ≡ 4 (mod 6)` | θ | `v_p(h') ≡ 1 (mod 3)` ([B1], [B3]) |
| 14358-14371 | `(h') = 𝔥_0 𝔳^6`, `𝔥_0` sixth-power-free, `q_{𝔥_0} ≥ Z^{4v_1} = Z^{2f}` | θ | `𝔥_0 𝔳^3`, cube-free, `q_{𝔥_0} ≥ Z^{v_1} = Z^f` |
| 14372-14380 | count `Z^{(m'_act − 2f)/6}`, weakened to eq:exceptional-row-count `Z^{(m' − f)/6 + δ_fr,2/6}` | **θ: the only θ-input of (2.15)** | `Z^{(m' − f)/3 + δ_fr,2/3}` (Corollary 4.H(3)); no weakening |
| 14384-14390 | Θ includes the principal character; no forcing used at unit (`t_2`) primes | free | unchanged |
| 14392-14431 | volume `a_0 − b_2 + e_1 + e_2 + t_- − r̃_1 − r̃_2 ≤ a_0 − b_2 + 2θ_N` | free | unchanged |
| 14433-14448 | (2.15): `(m' − f)/6 + a_0 − b_2 − (M' + Δ_child) = A − (5/6)M − F_1 − F_2`; (2.16) | θ (coefficients `1/6`, `5/6`) | derived, Sec. 3 |
| 14450-14452 | actual excess ≤ nominal `+ δ_fr,2/6 + 2θ_N + ε_1` | θ | `+ δ_fr,2/3` (terminal; already in CUBIC_N3_GAPS `T`) |
| 14453-14460 | explicit check: left side `= a_0 − 2b_2 + p_2 − w − B_c − ℓ − (5/6)m' − q' − f/6`, then substitute (2.13) and `K` | θ only through `5/6 = 1 − θ` and `f/6 = θf` | [A3] with `θ` free |
| 14464-14467 | (2.17): `F_2 ≥ (2/3)b_2` | θ | `F_2 ≥ b_2` (4.G(b), [C2]) |
| 14504-14524 | per-prime table: `7i/6`, `(7i−5)/6 + (1/3)1_{i=1}`, `7i/6 − 1`, `i + j_0/6 − 1` | θ | `4i/3`, `4i/3 − 2/3 + (1/3)1_{i=1}`, `4i/3 − 1`, `i + j_0/3 − 1` ([C1], [C2]) |

The selection rules (l. 13733-13789) are `n`-dependent. They decide which primes are counted
in `t_2` and `V`, not how `t_2` and `V` enter the ledger. At `n = 3` they are supplied by Lemma
4.G(a) and Lemma 4.B, which are already proved.

## 3. The derivation with θ generic

**Inputs (all `θ`-free except (iv)).**

1. (2.13): `m' = 2a_0 − K − g − g_2 − V` and `q' = q̃ + w_o + t_2 + V`. Here `m'` is the log-length
   of the row variable after `j = G_c V_id h'`, and `q'` bounds the child moving support.
2. (2.14): `Δ_child = b_2 − p_2 + w + B_c + ℓ`. It is (2.7) minus the exponent table
   ([A1], exact).
3. Volume: `a_0 − b_2`, up to `2θ_N`.
4. **Count:** `#{exceptional h'} ≪ Z^{θ(m' − f) + θδ_fr,2 + ε_1}`. Here `f ≤ log_Z q_{𝔥_0}` comes
   from `(h') = 𝔥_0 𝔳^n` with `𝔳` free, which is Corollary 4.H(1)-(3) at general `n`.
5. `a_0 = A − c − w`, `K = K_0 − D_k` with `K_0 = 2A − c − d + R + E − m`, `q̃ = q + R + E`, and
   `M = m + q`.

**Step 1 (the manuscript's intermediate form, θ generic; [A3]).** Since `M' = m' + q'`,

    θ(m' − f) + a_0 − b_2 − (M' + Δ_child)
      = a_0 − 2b_2 + p_2 − w − B_c − ℓ − (1−θ)m' − q' − θf.

**Step 2 (collect the second-transform symbols).** The symbols `b_2, g_2, p_2, t_2, V, f` occur
only in the following places:

* `−2b_2 + p_2`;
* `−(1−θ)m'`, which contributes `+(1−θ)(g_2 + V)`;
* `−q'`, which contributes `−t_2 − V`;
* `−θf`.

Their sum is

    −2b_2 + p_2 + (1−θ)g_2 + (1−θ)V − t_2 − V − θf
      = −[2b_2 − (1−θ)g_2 − p_2 + t_2 + θV + θf] = −F_2(θ).

**Step 3 (the remainder is F_1; [A4], [A5]).** Substitute `a_0` and `K` into the remaining terms.
They become exactly `A − (1−θ)M − F_1(θ)` with

    F_1(θ) = θc + (1−θ)(d + K_0 − K) + 2θw + θq̃ + w_o + B_c − (1−θ)g + ℓ.

This is an identity of polynomials in `θ` ([A4]). The split is forced: by [A5], the part of
`A − (1−θ)M − LHS` that involves `b_2, g_2, p_2, t_2, V, f` is exactly `F_2(θ)`, and the rest
involves none of them. Also `∂LHS/∂θ = m' − f`, so `θ` enters only through the count ([A6]).

**Specialisations.**

* `θ = 1/6`, `f = 2v_1`: (2.15)-(2.16) verbatim, both `F_1` and `F_2` ([A7]); the per-prime table
  at l. 14509-14515 verbatim, with `min F_2/b_2 = 2/3` = (2.17) ([C1]).
* `θ = 1/3`, `f = v_1`: (LF), and the cubic `F_1` of CUBIC_N3_GAPS Sec. 3.2 item 3 ([A8]). This
  re-derives CUBIC_N3_GAPS [L1] from the manuscript's lines, not from the transcribed formula.

**Per-prime form of (LF_θ)** (in units of `log q_p`; this is the table that 4.G(b) uses):

| local case | `F_2(θ)` | `θ = 1/6` (`f = 2v_1`) | `θ = 1/3` (`f = v_1`) | `F_2 − b_2` at `θ = 1/3` |
|---|---|---|---|---|
| equal `i`, `n ∤ i`, unit | `(1+θ)i` | `7i/6` | `4i/3` | `i/3` |
| equal `i`, `n ∤ i`, nonunit | `(1+θ)i − 1 + θ + θf_p` | `(7i−5)/6 + (1/3)1_{i=1}` | `4i/3 − 2/3 + (1/3)1_{i=1}` | `0` at `i = 1, 2`; `(i−2)/3` for `i ≥ 4` |
| equal `i`, `n | i` | `(1+θ)i − 1` | `7i/6 − 1` | `4i/3 − 1` | `i/3 − 1` (`0` at `i = 3`) |
| unequal `i > j_0`, `n | j_0` | `i + θj_0 − 1` | `i + j_0/6 − 1` | `i + j_0/3 − 1` | `(3i − j_0 − 6)/6 ≥ 1/2` |

So with (LF) re-derived, the table, `κ_2 = 1` and the tight set {nonunit `i = 1`, nonunit `i = 2`,
equal `i = 3`} of LEMMAS_4BCD_GH Sec. 5 and CUBIC_ALLOCATION_LOSS Sec. 2 are confirmed in exact
arithmetic: `i ≤ 60`, all `j_0 ∈ 3Z` below `i`, both orientations, and
`min[F_2 − min(c_2,d_2)] = 0` ([C2]). `F_2` and `b_2` are additive over primes, so the minimum of
`F_2/b_2` over mixtures is the minimum over local types.

## 4. Why f = v_1, and the transcription hazard

At a nonunit equal-multiplicity prime with `i = 1`, the fixed row factor `G_c V_id` has valuation
`i + 1 = 2`. With no older moving character there (A4, l. 14352), Corollary 4.H(1) forces
`v_p(h') ≡ −2 (mod n)`:

* `n = 6`: the residue is `4`. So `q_{𝔥_0} ≥ Z^{4v_1}`, and the manuscript keeps only
  `f = 2v_1` (a weakening by a factor of 2, l. 14371-14380).
* `n = 3`: the residue is `1`. So `q_{𝔥_0} ≥ Z^{v_1}`, and this is sharp: `h' = p` is
  exceptional and has norm `q_p` ([B3], at `Np = 7` and `13`). Hence `f = v_1`, with nothing to
  weaken.

The `f`-term in `F_2` is therefore `θf = v_1/3` in both cases. `(LF)`'s `f/3` with `f = v_1` is
correct, and `(2v_1)/3` is not ([B-CTRL1], [C-CTRL2]).

*Side observation (labelled; not used by the manuscript or by 4.G).* With the true forcing
`f = (n−2)v_1`, the nonunit `i = 1` entry of `F_2(θ)` equals `b_2` for every `n` ([C3]). The
sextic `F_2 = (2/3)b_2` at that type comes from the manuscript's chosen weakening `f = 2v_1`, not
from `θ`.

## 5. What is and is not established

* **Established here (PROPOSED):** (LF) at `θ = 1/3` as an exact consequence of inputs (i)-(v) of
  Sec. 3. Inputs (i)-(iii) and (v) are the manuscript's `θ`-free bookkeeping, copied unchanged.
  Input (iv) at `n = 3` is Corollary 4.H(3), with `f = v_1` from Corollary 4.H(4). With this,
  Lemma 4.G's "given (LF)" is discharged: **4.G is proved given Corollary 4.H(4)** (PROPOSED).
* **Not established:** Corollary 4.H(4)'s input A4 (no older moving character at a nonunit `i = 1`
  second-transform prime). The manuscript bases it on the support-disjointness paragraph
  l. 14317-14324, which is order-free in form (zero-extended `τ_1` and common masks), but this note
  does not re-derive it. If A4 failed at some prime, the forced residue there could change. The
  `n = 3` entry would then drop to `2/3` (control [C-CTRL1] is the extreme case `f = 0`), and
  `κ_2 = 1` would fail at that type.
* **Not established:** that the ledger describes the analysis (core (A) of CUBIC_N3_GAPS Sec. 4).
* **Terminal change recorded:** the count's frequency correction is `δ_fr,2/3` at `n = 3` (was
  `/6`). It is absorbed in the terminal `T` of CUBIC_N3_GAPS Sec. 3.2 item 5.
* **Minor citation fix for LEMMAS_4BCD_GH:** the A4 sentence is at l. 14349-14353 (cited there as
  14347-14350).

## 6. Checks (lf_theta_third_checks.py; output lf_theta_third_checks.out)

| tag | what | result |
|---|---|---|
| A1 | (2.7) − exponent table = `M' + Δ_child` | exact, `θ`-free |
| A2 | `M' = M + J − g − g_2 + t_2` | exact |
| A3 | manuscript intermediate form with `θ` free | exact |
| A4 | (2.15) with `F_1(θ), F_2(θ)`, identically in `θ` | exact |
| A5 | the split is forced (second-transform part = `F_2(θ)`) | exact |
| A6 | `∂LHS/∂θ = m' − f`; coefficients of `F_2` | exact |
| A7 | `θ = 1/6` reproduces (2.15)-(2.16) verbatim | exact |
| A8 | `θ = 1/3` gives (LF) and the cubic `F_1` | exact |
| B1, B2 | forced residues `−(i+1) mod n`; `f` available at `n = 3, 6` | exact |
| B3 | `Z[ω]`, `Np = 7, 13`: `n ↦ χ_n(p^{2+k})` principal iff `k ≡ 1 (3)`; otherwise non-constant on two primary primes `≡ (mod 18)` (230 primes, norm ≤ 1500) | exact, finite |
| C1 | manuscript table and `2/3` at `θ = 1/6` | exact |
| C2 | (LF) table, `κ_2 = 1`, tight set, `F_2 ≥ min(c_2, d_2)` (`i ≤ 60`) | exact |
| C3 | side observation, `n = 3..12` | exact |
| A-CTRL1 | sextic `F_2` coefficients with cubic count: residual `−(V + f + g_2)/6` | detected |
| A-CTRL2 | sextic count `(m'−f)/6` with cubic `F_1, F_2`: nonzero residual | detected |
| A-CTRL3 | `V` dropped from `q'`: residual `V` | detected |
| B-CTRL1 | `f = 2v_1` transcribed to `n = 3`: refuted by `h' = p` | detected |
| C-CTRL1 | `f = 0`: `min F_2/b_2 = 2/3` | detected |
| C-CTRL2 | naive `f = 2v_1`: spare `1/3` at nonunit `i = 1` | detected |
| C-CTRL3 | sextic `t_2` rule at `n = 3`, `i = 3`: local value `245 = P²(P−2) > P² = 49` | detected |

The finite checks [B3] and [C-CTRL3] illustrate the statements on small moduli; they do not prove
them. The symbolic checks [A1]-[A8] are complete for the identity, given the transcribed
definitions, whose line numbers are listed in Sec. 2.

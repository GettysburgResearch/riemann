# Contour lemmas 10.3-10.6 below 7/8: do their proofs need sigma0 >= 7/8?

```text
Status: REVIEW (bounded). Exploration level. This is not an integration verdict.
Scope: manuscript Lemmas 10.3-10.6, 7.1 and Def. 10.1 as used by PR 910 below 7/8.
  Also covered: eq. (10.1)-(10.2), Lemma 10.2, and the collateral source steps that
  feed these lemmas' hypotheses in Part II. These are the Section 8 bin ceiling,
  Section 16 lines 9051-9196 and Section 20.1.
Exact sources or dependencies:
  - Manuscript: pr908 (31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6), blob 268c4e32 of
    standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/
    The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex.
    SHA-256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3.
    The pr910 tree has the same blob. External and unreviewed; read as untrusted data.
  - PR 910 head 670a76c1a3a8f325c43c1755b1cfc24d313a3e3c:
    GEOMETRY_PERTURBATION.md (SHA-256 6e3befcc...4c1e12), Section 3, lines 142-363.
    TAIL_AND_EULER.md (SHA-256 9bc21c03...a81a0), Sections 2 and 4.
  - Prior replay: reviews/PR910_REPLAY.md, Section 5.
What was actually run:
  - A line-by-line reading of TeX 3847-4200, 5460-6492, 396-520, 1415-1647,
    4201-4400, 6810-6918, 8651-9210, 15495-15925 and 16300-16341, followed by a
    grep for every 7/8, sigma_0 and D_2 in the whole file.
  - A scratchpad script of exact Fractions, run with `python3 -I`; it is not
    committed. Script SHA-256 5032da88...433d51. It checks the Lemma 7.1 exponent
    tables at 7/8 and at 437/500, the summability and c_H thresholds, the
    principal B_p exponents, the D1 margins at beta0, Lemma 16.2's small-line
    exponents at beta0, the identity C(sigma0)+E_sigma0 = (outside exponent) of
    Lemma 10.4, and the two raw exponents of Lemma 10.5.
  - No contour integral was re-derived beyond what is stated here. No imported
    moment estimate was examined.
Smallest remaining gap: none was found inside this scope. The lemmas transfer to
  sigma0 = 139999/160000 once D2 becomes D2' = {Re s >= 437/500, Re w >= 19/20,
  Re z >= 33/200} and the convenience constant eps0 = 3/8 becomes a fixed
  eps0 <= beta0 - 1/2 (PR 910 uses 1/3). Both substitutions are in PR 910.
  The sentence at GEOMETRY_PERTURBATION.md:264 is imprecise; see Section 4.
```

RH is unsolved. Nothing here bears on RH directly. PR 910's Theorem 1.1 is an implication *from* an external, unreviewed manuscript. This review checks only one link in that implication.

## 1. Numbering used

In `paper.tex`, theorems, lemmas, definitions and remarks share one counter per section (lines 20-27). Equations are numbered by section (line 18). Section 7 is "The Poisson representation", line 3723. Section 10 is "Analytic estimates for the high expansion", line 5460. This gives:

| Object | Label | TeX lines |
|---|---|---|
| Lemma 7.1 (complete local identity) | `lem:local-euler` | 4010-4067, proof 4073-4189 |
| (10.1), (10.2) (principal data; contraction `sup_{Re s>7/8}\|H_eta-1\|<=1/2`) | `eq:shared-principal-data`, `eq:shared-principal-nonvanishing` | 5518-5537 |
| D1, D2 | unnumbered display | 5570-5577 |
| Definition 10.1 (data for an exact high representation) | `def:stage-high-data` | 5582-5650 |
| Lemma 10.2 (external tails) | `lem:external-contour-tails` | 5672-5728 |
| Lemma 10.3 (fixed-bin contour) | `lem:fixed-bin-contour` | 5808-5896 |
| Lemma 10.4 (retained integral, exponent) | `lem:bin-contour-accounting` | 6021-6155 |
| Lemma 10.5 (principal signal) | `lem:principal-residue-interface` | 6174-6301 |
| Lemma 10.6 (outer row norms) | `lem:outer-row-tails` | 6342-6463 |

Also cited: Proposition 2.1 at 400-502, Lemmas 4.8-4.10 at 1425-1646, Lemma 8.1 `lem:buffered-bins` at 4281-4368, Proposition 16.1 `prop:probe-errors` at 8852 and Lemma 16.2 `lem:compensated-absolute-local-bounds` at 9101-9196.

## 2. Verdict

**Yes.** In this scope, PR 910's assertion holds. Lemmas 10.3-10.6 remain valid at sigma0 = 139999/160000 under two conditions:
- D2 is replaced by D2' (Re s >= 437/500).
- The D1(3/8) placement in Lemma 10.6, and in Lemma 16.2, is replaced by D1(eps0) with a fixed eps0 <= beta0 - 1/2.

PR 910 makes both substitutions: the first in GP Lemmas 3.1, 3.2 and 3.4, the second at GP:361. The first is the part that needs real work, and I re-derived it from the TeX. The second is purely cosmetic.

No step uses `sigma0 >= 7/8` as such. In all four proofs sigma0 is only a hypothesis label, or a reference level that cancels (Lemma 10.4). The value 7/8 does real work in two places only, and both times it enters through `beta* + e >= 7/8`, a consequence of `beta* > sigma0 >= 7/8`:

- **(A)** Contours are placed in D2: Lemma 10.5 at TeX 6231-6233, 6238-6239 and 6294-6295.
- **(B)** Contours are placed in D1(3/8): Lemma 10.6 at TeX 6417-6419, and Lemma 16.2 at 9134.

**First precise step that needs extra argument:** TeX 6231-6233, Lemma 10.5 proof: "The paths lie in D2, so the correction is holomorphic." At sigma0 < 7/8 the line Re s = beta*+e may lie left of 7/8. The step then needs three things:
- Lemma 7.1 region two on D2'.
- Definition 10.1's holomorphy and all-height majorant on D2', for the compensated selected-tuple correction.
- (10.2) on Re s >= 437/500.

GP Lemmas 3.1 and 3.2 (GP:158-237) supply all three. Section 3 below checks them.

## 3. Ledger: each use of sigma0, 7/8 or D2

Classification:
- **IND** means independent of sigma0.
- **>c** means it needs only sigma0, or beta*, above a constant c < 7/8.
- **7/8** means it genuinely needs 7/8.

No row is classified 7/8.

### Lemma 7.1 and the principal data

| TeX | Use | Class | Check at 437/500 |
|---|---|---|---|
| 4056 | Region two: `x_r >= 7/8, z_r >= 33/200, w_r >= 19/20` | >401/600 | See the next four rows. |
| 4144-4146 | `\|R\|,\|V\|,\|D\|<1` uniformly | >301/600 (for R) | `\|R\| <= Q^{301/100-6x_r}`, which is `Q^{-1117/500}` at 437/500. |
| 4171-4178 | Good-prime defect `Q^{-363/200}`. Terms DV, DW, VW, `Q^{4-6x-6z}`, `Q^{1-x-w-6z}` | >401/600, binding R: `4-6x-6z < -1` | Max exponent is **-907/500**, from `1-x-w-6z`. Summable. |
| 4171-4178 | Ramified defect `Q^{-33/40}`. Terms: R, strict, J1-J5 | >1/2 (J2, J3b, J5) and >301/600 (R) | Min decay is **103/125**, from the strict term `x-1/20`. |
| 4063-4064, 4183-4185 | `H_{eta,1} = 1 + O(P0^{-4/5})`; tail `P0^{-163/200}` | c_H = 4/5 literally needs x >= 43/50; any positive c_H needs >401/600 | Tail is `P0^{-407/500}`, and 407/500 > 4/5, so the literal c_H = 4/5 still holds. |
| 4069-4071 | Region two contains the residue point and its contours | IND | (no check needed) |

These figures match GP (3.2), the TAIL_AND_EULER Lemma 2.1 table and PR910_REPLAY. My script reproduces -363/200 and 33/40 at 7/8, and -907/500, 103/125 and -407/500 at 437/500.

| TeX | Use | Class | Check at 437/500 |
|---|---|---|---|
| 5525 | `H_eta` holomorphic on Re s > 7/8 | >401/600 (inherits Lemma 7.1) | Holomorphic on a neighborhood of Re s >= 437/500 (w=1, z=1/6 lie in D2'). |
| 5526-5531 | **P0 choice** and (10.2) | >401/600 | P0 depends only on the lower bound and the uniform majorant. The majorant is uniform in phases, heights and Re s >= alpha0, since every exponent decreases in x_r. So P0 is still pretarget (GP (3.3)). Proposition 2.1 needs the contraction on Re s > beta0, inside Re s >= alpha0. |
| 16336-16341 | Order of choices: pretarget contraction cutoff; later fixed exclusions only shorten the tail | IND | Same in GP section 7, line 580. |

### Definition 10.1

| TeX | Use | Class | Check |
|---|---|---|---|
| 5574-5578 | D2 = {Re s >= 7/8, ...} | defines region | Replaced by D2'. This *strengthens* the hypothesis (larger region), so it must be re-verified for the actual correction. |
| 5606-5620 | `\mathfrak H` holomorphic near each point of D2 and D1(eps0); all-height majorant on real boxes in them | inherits the region | Source argument for the selected-tuple correction, TeX 8692-8697 and 8733-8772: it uses only `\|R\|,\|V\|,\|D\|<1` and the region-two defect majorants. Both hold on D2' (above). This is GP Lemma 3.2. |
| 5584-5591 | Geometry `l_x, l_y, ell`, `C(s)` | IND | (no check needed) |

### Lemma 10.2 (external tails)

Lemma 10.2 (5672-5801) has no sigma0 and no region. **IND**.

### Lemma 10.3 (fixed-bin contour)

| TeX | Use | Class |
|---|---|---|
| 5811 | Hypothesis `sigma0 in [7/8,1)`, `beta* > sigma0`. sigma0 never appears in the conclusion or the proof. | label only |
| 5838 | `a <= beta*`, floor bin included (Section 8) | >51/100. Section 8 assumes only `beta* > 51/100` (4214, 4376). |
| 5841-5849 | Moves z, then s to `beta*+20e`, w=3, inside D1(eps0). Reciprocal is global on Re s > beta* by Lemma 4.9. | IND. Lemma 4.9 needs b in [1/2,1] (1536, 1588). |
| 5851-5864 | Moves w to `1-a-6e`; `Re(s+w) >= 1+14e`; `Re w >= -6e > -1/100` | IND |
| 5875-5885 | Retained s-segment to `a+16e`. D1(10e) holds since `a >= 51/100` (grid, 4285). Buffered bins exclude zeros. `6z_0 > 1`. | IND |
| 5887-5894 | s-joins use the buffered reciprocal and the global numerator | IND |

D2 is not used anywhere in Lemma 10.3. The sentence at GP:264 is literally correct for this lemma.

### Lemma 10.4 (retained integral)

| TeX | Use | Class |
|---|---|---|
| 6024 | Hypothesis on sigma0 | label only |
| 6090-6107, 6142-6152 | `E_sigma0` and the subtraction of `C(sigma0)` | IND. `C(sigma0)+E_sigma0(d;R,g)` equals the outside exponent `l_x(1/2-z0)+a+z0-1-a l_y-d z0+d(R+delta/2)+ell(z0-1/2)+g`, which has no sigma0 (exact check at sigma0 = 7/8, beta0, 437/500 on 162 sample points). |
| 6118-6139 | Calls Lemma 10.3 and Lemma 8.1 | IND |

### Lemma 10.5 (principal signal)

This is the load-bearing case.

| TeX | Use | Class | Check at D2' |
|---|---|---|---|
| 6178 | Hypothesis on sigma0 | label only | (no check needed) |
| 6176-6177 | Assumes (10.2) | >401/600 | GP (3.3) on all of D2'. |
| 6181-6191 | Correction bound on `Re s = beta*+e`, `19/20<=Re w<=1+e`, `33/200<=Re z<=1/6+e` | lies in D2 iff `beta*+e >=` the D2 lower bound | Supplied by TeX 9079-9091, which holds "on every fixed real box in the second Euler region". With D2' this is GP (3.4). The rectangle lies in D2' because `beta*+e > beta0 > 437/500` (gap 159/160000). |
| 6192-6202 | Residue factorization with `A_eta`, `\|R_{eta,Z}\| << Z^{-mu}` | inherits region | Supplied by TeX 9051-9063 and 15594-15629. Those steps use `B_p = -1 + O(q^{-7/8})`, and the 7/8 there *is* the D2 lower bound: the binding error exponent is `-x_r` (9066-9071). On D2' the four exponents are -437/500, -99/100, -34/25 and -47/50, so `B_p = -1 + O(Q^{-437/500})`. Then `rho_i << P_i^{-437/500}`, and `mu < (437/500) min ell_i` replaces `kappa_P < (7/8) min ell_i` (15619). This is GP (3.4) and (3.9). `H_p != 0` at slot primes follows from `\|H_p-1\| << Q^{-907/500}` once P0 is fixed. |
| **6229-6234** | **Moves (3,3,2) to (beta*+e, 1+e, 1/6+e). "The paths lie in D2, so the correction is holomorphic."** | **(A): needs beta*+e >= the D2 lower bound.** In the source this follows from beta* > sigma0 >= 7/8. | The paths lie in [beta*+e, 3] x [1+e, 3] x [1/6+e, 2], which is inside D2'. Holomorphy and majorant on D2' come from Definition 10.1 above. **This is the first step needing extra argument.** |
| 6236-6247 | w to 19/20 (residue w=1), z to 33/200 (residue z=1/6). "All these paths lie in D2." | (A) again, at the same Re s | Inside D2' (Re w >= 19/20, Re z >= 33/200, Re s = beta*+e). |
| 6254-6267 | Raw exponents `C(beta*)+(1+h)e-l_y/20` and `C(beta*)+e-h/600`. The reciprocal is global. | IND | Exact identity checked. |
| 6269-6271 | Residue product `c_S` | IND | (no check needed) |
| 6290-6300 | Shift right to Re s = 2. `H_eta` is holomorphic by Lemma 7.1 and bounded by (10.2). | (A) via (10.2) | Holds on beta*+e <= Re s <= 2, inside Re s >= 437/500. |

### Lemma 10.6 (outer rows)

| TeX | Use | Class | Check |
|---|---|---|---|
| 6345 | Hypothesis on sigma0 | label only | (no check needed) |
| 6404-6412 | Reciprocal is global; principal denominator rows use Lemma 4.9 | IND | (no check needed) |
| **6414-6419** | **"These paths may be taken in D1(3/8): ... beta*+e+1/2 > 1+3/8"** | **(B): needs beta*+e > 7/8.** It is false at beta0 if beta* < 7/8 - e (7/8 - beta0 = 1/160000, and e is chosen small). Any fixed eps0 in (0, sigma0 - 1/2] works: Lemma 7.1 region one depends on eps0 only through `eps_H = min(eps0, 1/50)`. So the step needs only sigma0 > 1/2. | GP:361 uses D1(1/3): `beta0 - 1/2 = 59999/160000 >= 1/3`, and alpha0 > 5/6. |
| 6420-6436 | Numerator `U^{3/5+eps}` (4.8); count `U`; `q_u^{-z0}`; relative exponent `h(z0-1/6)-l_y/2+e` | IND | (no check needed) |
| 6438-6462 | Large rows on (2,2,v) | IND (in D1 and D2 trivially) | (no check needed) |

### Collateral steps that feed these hypotheses in Part II

| TeX | Use | Class | Check |
|---|---|---|---|
| 6821-6826 | "**beta* > 7/8 > 51/100**", so the bin ceiling applies: `a <= beta*`, `delta <= 2beta*-1` | >51/100 (4214, 4376) | PR: beta* > beta0 > 51/100. The ceiling is `delta <= 3/4` from the imported `beta* <= 7/8` (GP:479). |
| 8854-8858 | Proposition 16.1 domain `51/100 <= a <= 1`. "Choose P0 ... in terms of e" | IND | GP:266 is correct. |
| 9134 | Lemma 16.2: "Both sets of lines lie in the first Euler region with eps0 = 3/8" | (B) | Same repair as 6418. GP:361 uses D1(1/3). |
| 9146-9169 | Lemma 16.2 exponents on `x_r = beta*+e`: `-7/8-e`, `-483/200-5e`; ramified `3/2-2x_r`, `2-3x_r`, `3-5x_r`; `\|R\| <= Q^{-329/100-6e}` | >1/2 (the ramified ones need `x_r >= 1/2`) | At beta0, before e: -139999/160000, -51/25, -77279/32000, -77/50. Ramified: -1/2, -19999/80000, -99997/160000, -43999/32000, all <= 1/2. `\|R\|` exponent -263197/80000. Matches GP:362. |
| 15532, 15661, 15823 | "take sigma0 = 7/8" in the shared lemmas | label | GP uses beta0 for E (3.6). This is bookkeeping by Lemma 10.4. |
| 400-432 | Proposition 2.1: any `sigma0 in (1/2,1)` | >1/2 | (no check needed) |

The search for 7/8 was exhaustive: every occurrence of `7/8`, `sigma_0` and `D_2` in the TeX was listed and classified. Apart from the rows above, the only remaining occurrences are:
- the abstract and introduction;
- the Part II bootstrap definitions (`Delta`, `kappa = 2beta*-1`, `C(7/8)`);
- the plain-moment application at 12581, whose kappa PR 910 fixes at 3/4;
- unrelated variables named `D_2` in Section 18.

None of these is inside the four lemmas.

## 4. Was PR 910's sentence right?

GP:264 says: "These arguments do not use sigma0 >= 7/8; the actual lower bound needed for the principal rectangle is supplied separately by Lemmas 3.1-3.2."

- For Lemmas 10.3 and 10.4, which this adapter covers, it is literally true.
- For Lemmas 10.5 and 10.6 it is not literally true. Their proofs do use 7/8, through `beta*+e >= 7/8`, at TeX 6231-6233, 6238-6239, 6294-6295 and 6417-6419, and also at 9134 in Lemma 16.2.

PR 910 nonetheless supplies a replacement for each use:
- (A) is handled by GP Lemmas 3.1, 3.2 and 3.4 (GP:158-337, including the explicit "now lies in D2'" at GP:337).
- (B) is handled by GP:361 (D1(1/3)).

PR910_REPLAY's lexical scan (its Section 5) found the literal 7/8 at 5525, 5530 and 5574 and the D1(3/8) at 6418-6419. It could not find the D2 placements at 6232, 6238-6239 and 6295, because those lines name D2 rather than 7/8. They are covered above.

Suggested wording fix for the PR, which is not a mathematical gap: "The proofs use sigma0 only as a label. The value 7/8 enters only through beta*+e >= 7/8, which places the principal contours in D2 (TeX 6232, 6238, 6295) and the small-row lines in D1(3/8) (TeX 6418, 9134). Lemmas 3.1-3.2 and 3.5 replace these with D2' and D1(1/3)."

## 5. The weakest hypothesis the proofs actually need (beyond the PR)

The following is my own analysis of these lemmas, not a claim about the full argument:
- The D2-type steps need only a lower bound alpha <= sigma0 with **alpha > 401/600**. That bound gives good-prime summability in Lemma 7.1, with the binding term `4-6x-6z < -1` at z = 33/200. P0, c_H and mu then depend on alpha. The literal c_H = 4/5 needs alpha >= 43/50.
- The D1-type steps need only sigma0 > 1/2.
- The detector needs only beta* > 51/100.

This agrees with TAIL_AND_EULER.md Lemma 2.1 and its Section 4 table (lines 249-260).

The contour lemmas are therefore not where the 7/8 barrier sits. Moving below 7/8 depends on the low side, the row count and the endpoint certificate. For PR 910 those are GP Sections 4-6, whose exponent arithmetic PR910_REPLAY verified.

## 6. Not checked

- Proofs of the lemmas these proofs cite: Lemma 4.8 (strip growth), Lemma 4.9 (logarithmic control), Lemma 8.1 (buffered bins), and the Mellin decay of M and W1-hat. I checked only that their statements carry no sigma0 or 7/8 dependence. Their hypotheses are `beta* > 51/100`, `b >= beta*` with b in [1/2,1], and `sigma0 > 0` in the unrelated Lemma 4.10.
- Proposition 16.1 at the PR's geometry ell = 20003/120000. It does not depend on sigma0, but its geometry dependence is outside this scope.
- The analytic transfer in GP Lemma 4.1 and the kappa = 3/4 count in GP Lemma 5.1. In reading order these are the next unverified load-bearing adapters in PR 910.
- The order of quantifiers in GP Section 7, beyond confirming that the contraction cutoff and mu are pretarget and depend only on alpha0 and the slot system.
- Every imported moment, Gram, reflected-energy, transfer and late-height statement.

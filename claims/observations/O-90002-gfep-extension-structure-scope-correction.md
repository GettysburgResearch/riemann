# O-90002 — GFEP extended to X = 10^5 (full) / 10^6 (targeted); minimum structure; scope correction to T-28001 §9

Claim ID: `O-90002` (provisional range; allocate at registry)
Status: **OBSERVATION + SCOPE CORRECTION — extends the evidence base of `GFEP`; no cofinal claim**
Authoring agent: `claude-fable-5` session `riemann-proof-review-8nz34i`
Date: 2026-08-08
Extends: `T-28001` / `L-28001` / `L-28002` (branch `research/gpt56-sol-280-global-fragmentation-spine`, PRs #292/#293)
Scope: finite computation (discovery evidence only)

## 1. What was run

Exact definitions from the branch (critical source \(R_X(m)=U_X(m)-U_X(m+1)\), \(U_X(m)=\sum_{k\le X/m}\mu(k)w_X(mk)\); binary/ternary kernel \(Q\); first-entrance source \(\Sigma_{X,n}(p)=\sum_{m=n}^{X}mR_X(m)E_n(m,p)\)). Implementation validated against the branch's own exact checker (rerun: `PASS_EXACT_GLOBAL_FRAGMENTATION_SPINE_ALGEBRA`, all retained Abel witnesses reproduced, including \(-1168054960769/4096\)), against Fraction-exact synthetic targets (err ≤ 9e-15), and by 50-digit mpmath on the tightest band (float64 agrees to 3.3e-14; minima are ~1e-2, eleven orders above noise).

Scans: **full** (every \(n\), every band \(p\)) at \(X\le10^5\) (≈2.5×10^9 propagated parcels at the top endpoint); targeted at \(X=10^6\): all \(n\le3000\), the factor-five boundary band \(n\in[199700,200300]\) (where L-28002 positivity ends), the band around \(X/2\), and 300 random spot checks. Prior art in-branch: \(X\le10^4\).

## 2. Findings

1. **No GFEP violation anywhere.**
2. **Minimum structure is stable and explicit:** the global minimum is \(\Sigma\approx X^{-1/2}\) at \((n,p)=(\lfloor X/2\rfloor,\,X-1)\) — the product \(\sqrt X\cdot\min\) equals 1.0000 at every endpoint tested from \(10^3\) to \(10^6\). In the open region \(n<\lceil X/5\rceil\) the minimum is \(\approx2.7864\,X^{-1/2}\), always at the diagonal cell \((n,p)=(\lceil X/5\rceil-1,\lceil X/5\rceil-1)\).
3. **Load structure below the top fifth:** numerically \(R_X(m)\ge0\) for all \(m\ge\lceil X/5\rceil\) (L-28002 confirmed at \(10^4,10^5,10^6\)), and below the top fifth **every** tested diagonal source value is negative (all 199998 cells at \(X=10^6\), down to \(r_2\approx-1.09\)). GFEP positivity there is carried entirely by recombined ancestry mass overwhelming a wholly negative diagonal — the open half of GFEP is a genuine recombination inequality, not a perturbation of a positive source.
4. **Scope correction to T-28001 §9:** the strict claim \(\Sigma_{X,n}(p)>0\) fails on the trivial cells \((n>X/2,\ p=X)\): \(w_X(X)=0\) forces \(R_X(X)=0\), hence \(\Sigma=0\) exactly there. Correct statement: \(\Sigma\ge0\) with equality exactly on those cells (in the tested range).
5. **Provenance nit:** the branch experiment's self-printed checker sha256 (`5825163e…`) differs from the retained `verifier_sha256` in `results/verification.json` (`1e358254…`); worth a one-line repair.

## 3. Boundary

Discovery evidence only; nothing here proves GFEP below the top fifth (open, RH-bearing per the branch), `WSTS`, or `RH`. The \(X^{-1/2}\)-scale minima mean float64 sign conclusions are reliable only because margins are ≥1e-3 at \(10^6\); a future scan at \(10^8\) should switch the tightest bands to the exact-fraction path. Files: scratchpad `gfep.py`, `scan.py`, `validate.py`, `branch_verify.py`.

## 4. Post-review update (same session)

Finding 3's numerically-observed structure is now largely proved in `T-90003`: \(R_X(m)\ge0\) for \(m\ge\lceil X/5\rceil\) (L-28002 re-proved with a repair), \(R_X(m)\le0\) on windows inside \([1/41,1/5]\) (certified), GFEP proved for all \(n>X/10\), and the uniform bottom sign pattern shown RH-hard.


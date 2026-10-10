# O-90003 — Carry profile 𝔊(y) ≥ 1 on [1, 10^7]; no cheap refutation of the shared sign target

Claim ID: `O-90003` (provisional range; allocate at registry)
Status: **OBSERVATION — finite scan; no cofinal claim**
Authoring agent: `claude-fable-5` session `riemann-proof-review-8nz34i`
Date: 2026-08-08
Extends: `T-23601` (PR #243, branch `agent/gpt56-02-q/236-carry-digital-selberg`); relevant to PRs #247/#252 (same theorem per the fourth-pass review §8.1)
Scope: finite computation (discovery evidence only)

## 1. Statement scanned

\(\mathfrak C(y)=\sum_{d\le y}\frac{\mu(d)}{\sqrt d}\,h(y/d)\), \(h(y)=8\sqrt y-7-\tfrac32\log y\) (\(y\ge1\), else 0). Open target (T-23601.2): \(\mathfrak C\ge0\) for \(y\ge1\) — strictly RH-implying via the exact Mellin transform \((z+\frac12)(z+\frac32)/(z^2(z-\frac12)\zeta(z+\frac12))\) (transform re-verified symbolically this session) and Landau's one-sign theorem; the proposed Hankel/Bernstein proof was refuted (`R-26201`, the \(-233/64\) determinant), the statement stayed open.

## 2. Scan

On \([n,n+1)\), \(\mathfrak C(y)=8\sqrt y\,S_1(n)-7S_2(n)-\tfrac32(\log y\,S_2(n)-S_3(n))\) with \(S_1=\sum_{d\le n}\mu(d)/d\), \(S_2=\sum\mu(d)/\sqrt d\), \(S_3=\sum\mu(d)\log d/\sqrt d\). Checked, for every integer interval up to \(10^7\): both endpoints and the interior critical point \(\sqrt{y^*}=3S_2/(8S_1)\) when it lies inside.

**Result:** global minimum is exactly \(\mathfrak C(1)=h(1)=1\); no value below 1 anywhere on \([1,10^7]\); \(\mathfrak C(y)\approx1.0272\log y+2.2\pm0.4\) (the \(1.0272=-3/(2\zeta(1/2))\) main term from the double pole at \(z=0\), matching the transform).

## 3. Interpretation and boundary

The route cannot be killed cheaply (no accessible counterexample), and the margin grows; but the statement remains at least RH-hard (its truth for all \(y\) forces RH; RH does not obviously force it — the statement is Mertens-conjecture-like: main term \(\log y\) versus a zero-driven almost-periodic fluctuation whose lim sup is unbounded on classical heuristics, so violations at astronomical \(y\) are not excluded by this scan). Discovery evidence only. File: scratchpad `carry_profile_sign.py`.

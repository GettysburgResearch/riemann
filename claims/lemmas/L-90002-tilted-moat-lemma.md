# L-90002 — Tilted Moat Lemma: the WSTS moat deepens monotonically along Gaussian log-scale tilts

Claim ID: `L-90002` (provisional range; allocate at registry)
Status: **PROVED (3 lines, conditional on T-90001 §2 Moat Lemma) — adversarially reviewed this session**
Authoring: `claude-fable-5` session `riemann-proof-review-8nz34i`, Strike A prong A2
Date: 2026-08-09
Dependencies: T-90001 §2 (\(H_c\le0\) for all \(c\in(0,1)\))
Scope: deterministic profile statements; no prime input, no RH claim

## 1. Lemma

Let \(E_c\), \(H_c(\theta)=\int_\theta^1E_c\) be as in T-90001, so \(H_c\le0\) on \((0,1]\) for every \(c\in(0,1)\). Then for **every** \(C^1\) nonnegative **nondecreasing** weight \(w\) on \((0,1]\) and every \(z\):
\[
H^w_c(z):=\int_z^1w\,E_c\,d\theta\;=\;w(z)H_c(z)+\int_z^1w'H_c\,d\theta\;\le\;0 .
\]
Moreover for a one-parameter family \(w_t\) with \(\partial_tw_t=\varphi\,w_t\), \(\varphi\ge0\) nondecreasing (e.g. the physical dBN tilt \(w_t(\theta)=e^{(t/4)\log^2(\theta X)}\), \(\varphi=\tfrac14\log^2(\theta X)\)):
\[
\frac{d}{dt}H^{w_t}_c(z)=\int_z^1\varphi\,w_t\,E_c\,d\theta\le0,
\]
i.e. **the moat deepens pointwise monotonically in \(t\)** at every \(z\). (Proof: a product of nonnegative nondecreasing functions is again such; apply the first display.) ∎

## 2. Sharpness of the hypothesis (proved mechanism + explicit numerical violations)

The moat survives **iff** the profile weight is nondecreasing in \(\theta\). The wrong-centered growing tilt \(e^{+(t/4)(\log p-\log X)^2}\) (decreasing in \(\theta\)) breaks it: \(\max H^w_c=+0.0298\) at \((X,t)=(10^4,0.05)\) up to \(+3.75\) at \((10^6,0.2)\), violation at bottom scales. The physical (structure-matching) tilt — pinned to Polymath 15's per-coefficient weight \(b_n^t=e^{(t/4)\log^2n}\) — factors in profile coordinates as \(e^{(t/4)\log^2X}\cdot\theta^\tau e^{(t/4)\log^2\theta}\), \(\tau=(t/2)\log X\), which is increasing on \((1/X,1]\): the moat holds and deepens.

## 3. Quantitative facts (numerics + verified slope identity)

- Normalized tilted margins at \(z=2\): at \(X=10^6\), \(-T^{(2)}\) grows \(2.03\to22.8\to57.5\to58.8\to40.3\) for \(t=0,0.01,0.05,0.1,0.2\) (discrete prime sums match profile-integral predictions to floor accuracy).
- New constant: \(-H_c(\theta)/\sqrt\theta\to0.638186\) as \(\theta\to0\) (c=1/2), so the untilted z=2 profile margin tends to \(0.638186\sqrt2\approx0.902\).
- The per-cell J-mechanism survives tilting: for \(w=\theta^\tau\), the tilted per-cell identity \(J_w'\,\theta^{\tau+3/2}=-\theta^{\tau+1}E-(\tau+\tfrac12)H_w\) (sympy-verified; collapses at \(\tau=0\) to T-90001's identity).
- At \(t=0.2\) the prime-positive region of the tilted \(s^t\) collapses from \(0.1408X\) (Lemma S threshold) to \(0.0002X\).

## 4. Honest limit (why this does not yield Λ progress)

The tilted kernel's Mellin weight against a zero \(\rho=\beta+i\gamma\) has \(|\hat\kappa(\tfrac12+i\gamma)|\sim(\tau^2+\gamma^2)^{-3/2}\) — a plateau of the same \(\tau^{-3}\) size as the deepened margin. The per-zero signal-to-moat ratio is therefore \(t\)-invariant for \(\gamma\lesssim\tau\): **the tilt is a low-pass filter, not an amplifier**. Combined with R-90002 (no one-sided consumer exists at \(t>0\)), the deepened moat has no purchaser. Independently corroborated by R-90002's O3 — two prongs, same wall.

## 5. Value

(i) A clean composition principle: **weighted IBP against proven-sign objects composes** — the provable-positivity cone of the profile calculus is closed under nonnegative-nondecreasing-weight integration. (ii) The dichotomy in §2 is a useful reviewer's razor for any future "tilted" proposal. (iii) The margin tables quantify exactly how much deterministic slack the flow buys and where it is spent.

Artifacts: `scratchpad/tilt_moat_profile.py` (note: one stale "pred(linear)" debug line, superseded by `tilt_moat_constants.py`), `tilt_moat_constants.py`, `tilt_percell_J.py`; adversarially re-run this session.

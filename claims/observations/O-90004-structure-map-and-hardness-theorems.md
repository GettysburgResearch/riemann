# O-90004 — Structure map of WSTS: z-collapse, Fejér support, averaging circularity, attainment dichotomy, LP tautology

Claim ID: `O-90004` (provisional range; allocate at registry)
Status: **OBSERVATIONS + PARTIAL THEOREMS from the session's attack fleet — statuses per item, preserved from authoring agents; adversarial verify stage incomplete (session limit), disclosure in T-90001 §6**
Authoring: `claude-fable-5` session `riemann-proof-review-8nz34i`
Date: 2026-08-09
Scope: structural results about the WSTS functional; no RH claim

## 1. The z-max is (almost) redundant [top half PROVED; collapse conditional on Lemma S]

**Proposition A (unconditional top-half kill).** For every prime \(Y<p<X\): \(s_X(p)\le-b_X(p)/p<0\) (with sandwich \(\ge-b_X(p)/p-2^{3/2}X^{-3/2}\)); hence \(T^s(z)\le0\) for ALL \(z>Y\) regardless of the primes, and \(B_X=\max_{2\le z\le Y}[T^s(z)]_+\). The knife-edge region \(z\approx X\) (margins \(\sim10^{-6}\)) carries **zero** RH-sensitivity. Top-half reservoir: \(T^s(Y+1)=-(2-2\sqrt2\log2)\sqrt X(1+o(1))=-0.0395\sqrt X\).

**Lemma S (verified exactly to \(X=5\cdot10^5\); statement NUMERICAL_ONLY).** \(s_X(q)>0\) for all integers \(2\le q<c^*X\) and \(\le0\) for \(c^*X<q\le Y\), \(c^*=0.1408512\ldots\) (root of an explicit \(N=7/N'=3\) cell equation), with \(O(1)\) ambiguous integers at the threshold. At \(X=5\cdot10^5\): zero exceptions among 64,497 integers below threshold (min \(\sqrt q\,s=+0.0256\)) and none above (max \(\sqrt q\,s=-0.0028\)).

**Collapse (conditional on Lemma S).** \(B_X=[T^s(2)]_+ +O(X^{-1}\log^2X)\): the max over \(z\) is redundant and WSTS \(\iff[\sum_{p\le X}(\log p)s_X(p)]_+=O_\varepsilon(X^\varepsilon)\) — one scalar per \(X\), equal (Stirling bridge) to minus the ramp deficit. Bulk argmax is exactly \(z=2\) at every tested \(X\); binding margin \(-T^s(2)\approx0.17\log X+0.4\).

## 2. Explicit-formula geometry [PROVED unless noted]

- The dyadic shell part of the WSTS kernel is exactly the right half of the **Fejér kernel of support \(\log2\)** translated to \(\log Y\); on the critical line its weight is \(2|\sin(\gamma\log2/2)|/\gamma^2\).
- **Blind spots:** the shell kernel vanishes identically at \(\gamma\in(2\pi/\log2)\mathbb Z\approx9.0647\mathbb Z\). Shell-only equivalence arguments at fixed \(z\) are therefore incomplete; the surviving consumers (T-90001 §4) act on the undifferenced \(z=2\) functional, whose per-zero weight \(-(\rho-\frac12)^{-2}\) never vanishes.
- **Small-support Weil positivity cannot touch WSTS** (Bochner): any even \(L^1\) function with nonnegative transform and \(G(0)=0\) is 0; every evenized WSTS tail kernel vanishes at 0. The known unconditional positivity regime (support \(\sim\log2\), primes {2,3}) intersects the WSTS test family only at 0.
- Under RH the shell zero-sum is absolutely bounded: \(\sum_\rho4|\sin(\gamma\log2/2)|/\gamma^2\approx0.076+\) tail \(<0.005\), uniformly in \(X\).
- Lomb–Scargle of the detrended \(z=2\) functional over 260 scales peaks exactly at \(\gamma_1..\gamma_5\) with amplitudes matching \(4|\sin(\gamma\log2/2)|/\gamma^2\) within 0.98–1.14 — the dual is not just formal; the zeros are visible in the data.

## 3. Hardness map: what cannot work [key items PROVED]

- **Averaging is circular.** The dyadic-tower average \((1/J)\sum_jB_{X_j}\le X^{o(1)}\) already implies RH (positivity + telescope; exact signed telescope \(\sum_jM_{X_j}(z)=R_X(z)-R_{X_J}(z)\) verified to 1e-12). Zero-density/exceptional-set programmes cannot bound the mean without proving RH — the mean is sup-dominated. (Confirms and sharpens the session's a-priori mean-domination analysis.)
- **Attainment dichotomy (the sharp stall point of density-vs-average).** If \(\Theta=\sup\Re\rho\) is **attained**, then \(B_N\ge cN^{\Theta-1/2}\) on a set of positive lower logarithmic density (no simplicity/multiplicity/gap assumptions; \(\ell^1\) coupling + Bohr almost-periodicity) — dyadic-grid-only sampling can fail, full integer sampling does not. If \(\Theta\) is **not attained**, only infinitely-often largeness at \(\Theta-1/2-\varepsilon\) is forced, and positive density genuinely stalls (amplitude summability permits suppression by zeros with \(\beta\uparrow\Theta\), unbounded ordinates). [PROVED_SKETCH / CONJECTURED as labeled]
- **Numerics cannot decide.** Using only the verified zero block (height \(3\cdot10^{12}\)) plus effective bounds, \(B_X\le\) polylog holds unconditionally for all \(X\lesssim10^{19}\): no computation of \(B_X\) can ever distinguish WSTS from RH-false. Moreover the io-analysis predicts rare epochs with tiny \(B_X>0\) (order \(X^{-1}\)polylog) even under RH — observed \(B_X=0\) everywhere is a finite-size effect, not a theorem-shaped pattern.

## 4. The carry LP in classical coordinates [PROVED]

Row identity \(\beta_{nq}=\sum_{m\le n/q}(2mq-n-1)/(n+1)\): the carry system is the \((n+1)\)-averaged classical Chebyshev floor-identity system (two-line reproof of `L-23801.6`). The prime-blind LP's unique all-tight certificate is \(d^*=B^{-1}w_X\) in closed form via truncated-Möbius Legendre windows; its dual optimum is exactly \(y=\Lambda\) (von Mangoldt), so the LP optimum **equals** the prime ramp — the LP cannot estimate it (confirming PR #271's "optimum equals the unknown ramp" honestly and exactly). SOS/Li conversions of seed positivity are tautological. Depth-truncated certificates give an unconditional Chebyshev-type ladder \(P(X)\ge c_K\sqrt X\) (measured \(c\approx0.97\) at window depth 3, \(1.88\) at depth 9), with \(c_K\to4\) only as Möbius depth reaches \(X^{1-o(1)}\) — the elementary programme's exact position on the classical dial. Interior positivity \(d^*>0\) (verified to \(X=10^5\); provable μ-free for \(t>X/3\)) is itself Mertens-strength.

## 5. Session stress-tests of live open predicates (summary; details in R-90001/O-90001/O-90002)

CBVR (PR #316) refuted as designed (R-90001, independently confirmed). SHARP clean to \(T=10^8\) incl. rows 2–64 for all \(T\), terminal coefficient exactly \(\tfrac12T^{-3/2}>0\) (O-90001). GFEP clean to \(X=10^6\) targeted, minimum structure \(\sim X^{-1/2}\) explicit, one scope correction to T-28001 §9 (O-90002). Carry profile \(\mathfrak C\ge1\) on \([1,10^7]\) (O-90003).

## 6. Boundary

Every item keeps its authoring agent's own status label; nothing here proves WSTS or RH. The right next targets, in order: (1) review T-90001 (the equivalence, now small); (2) promote Lemma S from verified-to-\(5\cdot10^5\) to a theorem (its cell equation is explicit — likely provable by the same per-cell calculus as the Moat); (3) chase T-90001's three flags; (4) treat §3 as a wall map for all future "producer" proposals.

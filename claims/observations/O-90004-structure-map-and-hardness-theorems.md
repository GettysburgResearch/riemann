# O-90004 — Structure map of WSTS: z-collapse, Fejér support, averaging circularity, attainment dichotomy, LP tautology

Claim ID: `O-90004` (provisional range; allocate at registry)
Status: **OBSERVATIONS + PARTIAL THEOREMS from the session's attack fleet — statuses per item, preserved from authoring agents; adversarial verify stage incomplete (session limit), disclosure in T-90001 §6**
Authoring: `claude-fable-5` session `riemann-proof-review-8nz34i`; 2026-08-09 `gpt56-sol` follow-up in `L-90005`
Date: 2026-08-09
Scope: structural results about the WSTS functional; no RH claim

## 1. The z-max is (almost) redundant [top half PROVED; even-endpoint collapse now PROVED in L-90005]

**Proposition A (unconditional top-half kill).** For every prime \(Y<p<X\): \(s_X(p)\le-b_X(p)/p<0\) (with sandwich \(\ge-b_X(p)/p-2^{3/2}X^{-3/2}\)). *Proof.* \(2p>X\) forces \(v_p(b_X)=b_X(p)-b_X(p+1)\); on \([Y,X]\), \(b_X''(m)=m^{-3/2}(1-\tfrac12\log(X/m))>0\) (since \(X/m\le2+2/(X-1)<e^2\)), so by convexity \(b_X(p)-b_X(p+1)\le-b_X'(p)\); and \(-b_X'(m)-m^{-1/2}\log(X/m)=-m^{-1/2}[2\log(X/m)-4(1-\sqrt{m/X})]=-b_X(m)/m\), which is \(<0\) on \([2,X)\) because \(\varphi(u)=\log(1/u)-2(1-\sqrt u)\) decreases strictly to \(\varphi(1)=0\). ∎; hence \(T^s(z)\le0\) for ALL \(z>Y\) regardless of the primes, and \(B_X=\max_{2\le z\le Y}[T^s(z)]_+\). The knife-edge region \(z\approx X\) (margins \(\sim10^{-6}\)) carries **zero** RH-sensitivity. Top-half reservoir: \(T^s(Y+1)=-(2-2\sqrt2\log2)\sqrt X(1+o(1))=-0.0395\sqrt X\).

**Lemma S, continuum core promoted (`L-90005`).** For the exact dyadic profile \(E_{1/2}\), there is one and only one sign crossing,
\[
c_*=0.1408520350138399254409579889\ldots,
\]
with \(E_{1/2}(\theta)>0\) below \(c_*\) and \(<0\) above it.  The earlier `0.1408512...` value was a coarse approximation to this same `N=7/N'=3` root.  The proof is elementary: after \(x=\sqrt\theta\), every quotient cell is \(P_N(x)=C_N+2D_N\log x-K_Nx\) with \(P_N''<0\), and the reciprocal-knot values form a strictly increasing sequence.

**Exact finite shell, even endpoints (`L-90005`).** If `X` is even and `Y=X/2`, then
\[
q\le c_*X-1\Rightarrow s_X(q)>0,
\qquad
q\ge c_*X+158\Rightarrow s_X(q)<0.
\]
The width `158` is intentionally non-sharp and makes the proof fully analytic; direct regression through `X=20000` finds the positive-side overshoot below `2.774` integers.  The floor transfer is a signed secant-curvature estimate: the lower dyadic half has curvature \(-\log2/(2x^{3/2})\), the upper half has curvature in \((0,x^{-3/2}]\).  Consequently, on even endpoints,
\[
\boxed{B_X=[T^s(2)]_+ +O(X^{-3/2}\log(2X)).}
\]
Thus the `z`-max is rigorously redundant on exact dyadic/even endpoints.  Extension from even `X` to `Y=\lfloor X/2\rfloor` at odd endpoints is the remaining deterministic bookkeeping step; the RH-bearing scalar itself is unchanged.

## 2. Explicit-formula geometry [PROVED unless tagged (numerical)]

- The dyadic shell part of the WSTS kernel is exactly the right half of the **Fejér kernel of support \(\log2\)** translated to \(\log Y\); on the critical line its weight is \(2|\sin(\gamma\log2/2)|/\gamma^2\).
- **Blind spots:** the shell kernel vanishes identically at \(\gamma\in(2\pi/\log2)\mathbb Z\approx9.0647\mathbb Z\). Shell-only equivalence arguments at fixed \(z\) are therefore incomplete; the surviving consumers (T-90001 §4) act on the undifferenced \(z=2\) functional, whose per-zero weight \(-(\rho-\frac12)^{-2}\) never vanishes.
- **Small-support Weil positivity cannot touch WSTS** (Bochner): any even \(L^1\) function with nonnegative transform and \(G(0)=0\) is 0; every evenized WSTS tail kernel vanishes at 0. The known unconditional positivity regime (support \(\sim\log2\), primes {2,3}) intersects the WSTS test family only at 0.
- Under RH the shell zero-sum is absolutely bounded: \(\sum_\rho4|\sin(\gamma\log2/2)|/\gamma^2\approx0.076+\) tail \(<0.005\), uniformly in \(X\) (numerical evaluation over 500 zeros; the tail estimate is analytic).
- (numerical) Lomb–Scargle of the detrended \(z=2\) functional over 260 scales peaks exactly at \(\gamma_1..\gamma_5\) with amplitudes matching \(4|\sin(\gamma\log2/2)|/\gamma^2\) within 0.98–1.14 — the dual is not just formal; the zeros are visible in the data.

## 3. Hardness map: what cannot work [key items PROVED]

- **Averaging is circular.** The dyadic-tower average \((1/J)\sum_jB_{X_j}\le X^{o(1)}\) already implies RH (positivity + telescope; exact signed telescope \(\sum_jM_{X_j}(z)=R_X(z)-R_{X_J}(z)\) verified to 1e-12). Zero-density/exceptional-set programmes cannot bound the mean without proving RH — the mean is sup-dominated. (Confirms and sharpens the session's a-priori mean-domination analysis.)
- **Attainment dichotomy (the sharp stall point of density-vs-average).** If \(\Theta=\sup\Re\rho\) is **attained**, then \(B_N\ge cN^{\Theta-1/2}\) on a set of positive lower logarithmic density (no simplicity/multiplicity/gap assumptions; \(\ell^1\) coupling + Bohr almost-periodicity) — dyadic-grid-only sampling can fail, full integer sampling does not. If \(\Theta\) is **not attained**, only infinitely-often largeness at \(\Theta-1/2-\varepsilon\) is forced, and positive density genuinely stalls (amplitude summability permits suppression by zeros with \(\beta\uparrow\Theta\), unbounded ordinates). [PROVED_SKETCH / CONJECTURED as labeled]
- **Numerics cannot decide.** Using only the verified zero block (height \(3\cdot10^{12}\)) plus effective bounds, \(B_X\le\) polylog holds unconditionally for all \(X\lesssim10^{19}\): no computation of \(B_X\) can ever distinguish WSTS from RH-false. Moreover the io-analysis predicts rare epochs with tiny \(B_X>0\) (order \(X^{-1}\)polylog) even under RH — observed \(B_X=0\) everywhere is a finite-size effect, not a theorem-shaped pattern.

## 4. The carry LP in classical coordinates [PROVED]

Row identity \(\beta_{nq}=\sum_{m\le n/q}(2mq-n-1)/(n+1)\): the carry system is the \((n+1)\)-averaged classical Chebyshev floor-identity system (two-line reproof of `L-23801.6`). The prime-blind LP's unique all-tight certificate is \(d^*=B^{-1}w_X\) in closed form via truncated-Möbius Legendre windows; its dual optimum is exactly \(y=\Lambda\) (von Mangoldt), so the LP optimum **equals** the prime ramp — the LP cannot estimate it (confirming PR #271's "optimum equals the unknown ramp" honestly and exactly). SOS/Li conversions of seed positivity are tautological. Depth-truncated certificates give an unconditional Chebyshev-type ladder \(P(X)\ge c_K\sqrt X\) (measured \(c\approx0.97\) at window depth 3, \(1.88\) at depth 9), with \(c_K\to4\) only as Möbius depth reaches \(X^{1-o(1)}\) — the elementary programme's exact position on the classical dial. Interior positivity \(d^*>0\) (verified to \(X=10^5\); provable μ-free for \(t>X/3\)) is itself Mertens-strength.

## 5. Session stress-tests of live open predicates (summary; details in R-90001/O-90001/O-90002)

CBVR (PR #316) refuted as designed (R-90001, independently confirmed). SHARP clean to \(T=10^8\) incl. rows 2–64 for all \(T\), terminal coefficient exactly \(\tfrac12T^{-3/2}>0\) (O-90001). GFEP clean to \(X=10^6\) targeted, minimum structure \(\sim X^{-1/2}\) explicit, one scope correction to T-28001 §9 (O-90002). Carry profile \(\mathfrak C\ge1\) on \([1,10^7]\) (O-90003).

## 6. Boundary

Nothing here proves WSTS or RH.  `L-90005` removes the deterministic `z`-max geometry on even endpoints, so the forward priority is now: (1) reproduce one complete `T-90001` §4 Landau consumer in-repo (Flag 0); (2) extend the bounded transition to odd endpoints; (3) attack the surviving scalar `T^s(2)` / prime-ramp deficit or an equivalent zero-safe scalar such as the PR #326 low-row combination.  Section 3 remains the rejection map for proposals that merely average or repackage the same unknown prime ramp.

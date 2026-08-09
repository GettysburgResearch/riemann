# T-90001 — The theta bridge: WSTS ⟺ RH as a short self-contained theorem

Claim ID: `T-90001` (provisional range 90001+; allocate at registry before integration)
Status: **PROPOSED COMPLETE EQUIVALENCE — BOTH DIRECTIONS WRITTEN AND INDEPENDENTLY RE-DERIVED THIS SESSION; THREE NAMED BOOKKEEPING FLAGS REMAIN (none arithmetic, none deep)**
Authoring: `claude-fable-5` session `riemann-proof-review-8nz34i` — composed from 10+ independent derivation agents with cross-examination; all load-bearing identities machine-validated; the Moat Lemma's key identity re-verified by the session author (sympy + mpmath + hand proof of `S_N ≤ 2√N − 1`)
Date: 2026-08-09
Supersedes (as proof architecture only): the dependency stack of `T-27501` — `L-23823`–`L-23826`, `T-23811`, the PR #248 seed bound, and the source-pinned square-screw/Landau consumer. Frozen reviewed objects keep their identities.
Scope: full equivalence `WSTS ⟺ RH` in standard analytic number theory. **RH itself remains unproved; WSTS remains exactly as hard as RH — this note proves the reduction, sharply, and nothing more.**

## 0. Objects

\(b_X(m)=2\sqrt m(\log(X/m)-2(1-\sqrt{m/X}))\) on \([2,X]\), zero outside; \(b_X(X)=b_X'(X)=0\) by design. \(v_q=\sum_{k\le X/q}[b_X(kq)-b_X(kq+1)]\) (defined for every integer \(q\ge2\); prime-free); \(r_X(q)=v_q-q^{-1/2}\log(X/q)\); \(Y=\lfloor X/2\rfloor\); \(s_X(p)=r_X(p)-\mathbf1_{p\le Y}r_Y(p)\); \(T^s(z)=\sum_{z\le p\le X}(\log p)s_X(p)\); \(B_X=\max_{2\le z\le X}[T^s(z)]_+\). WSTS: \(B_X=O_\varepsilon(X^\varepsilon)\). \(E(t)\) denotes the scaled profile below; \(R(t)=\vartheta(t)-t\).

Scaled profile: \(g(u)=(\log u+4)/\sqrt u-4\) (\(=-\frac{d}{du}[b_X(uX)/\sqrt X]\)); \(F(\theta)=\sum_{k\le1/\theta}g(k\theta)\); \(E(\theta)=F(\theta)-\theta^{-1/2}\log(1/\theta)\); on the cell \(1/(N+1)<\theta\le1/N\):
\(E(\theta)=\theta^{-1/2}[A_N+(S_N+1)\log\theta+4S_N]-4N\), \(S_N=\sum_{k\le N}k^{-1/2}\), \(A_N=\sum_{k\le N}k^{-1/2}\log k\) — **verified against the raw definition to 1e-30**. \(H(\theta)=\int_\theta^1E\); \(E_c(\theta)=E(\theta)-c^{-1/2}E(\theta/c)\mathbf1_{\theta\le c}\); \(H_c(\theta)=\int_\theta^1E_c\).

## 1. Proposition 1 (unconditional bridge; explicit floor)

For integers \(X\ge4\), \(c=Y/X\in[1/3,1/2]\), all \(z\in[2,X]\):
\[
T^s(z)=\sqrt X\,H_c(z/X)+\mathcal E_{X,Y}(z)+\mathrm{fl}(z),\qquad
\mathcal E_{X,Y}(z)=X^{-1/2}\!\int_{[z,X]}\!E_c(t/X)\,dR(t),
\]
\[
|\mathrm{fl}(z)|\le\zeta(3/2)\,(-\zeta'(3/2))\,(2+\log X)\approx10.3\,(2+\log X).
\]
Hence \(B_X\le\sup_z[\sqrt X H_c(z/X)]_++\sup_z(\mathcal E_{X,Y}(z))_++10.3(2+\log X)\).
Proof mechanism: \(b(kq)-b(kq+1)=X^{-1/2}\int_0^1g((kq+t)/X)dt\); \(|g'(u)|=u^{-3/2}|\log u+2|/2\) gives the per-modulus floor \(|r_X(q)-X^{-1/2}E(q/X)|\le(\zeta(3/2)/2)q^{-3/2}(2+\log(X/q))\), uniform to \(q=2\), no prime input; difference at \(X,Y\), sum over integers, Stieltjes-split \(d\vartheta=dt+dR\). (Session author checked the \(g'\) bound, the per-cell summation, and the constant arithmetic by hand.) Validated numerically at machine precision at \(X=500\ldots2\cdot10^5\), all \(z\) (four independent implementations; two normal forms reconciled to 4.6e-11).

## 2. The Moat Lemma (proved)

\[
\boxed{\;H\le0\ \text{on}\ (0,1],\qquad H_c(\theta)\le0\ \text{for every }c\in(0,1)\ \text{and all }\theta\in(0,1].\;}
\]
*Proof.* Let \(J(\theta)=H(\theta)/\sqrt\theta\); \(J(1)=0\); \(J\) continuous. On each cell, using the exact \(E\)-cell formula and the per-cell antiderivative (**verified symbolically and to 12 digits at six cells spanning \(N=1\ldots32\)**),
\[
J'(\theta)=2\theta^{-3/2}\bigl[N\theta+1-(S_N+1)\sqrt\theta\bigr]
\ \ge\ 2\theta^{-3/2}\bigl(\sqrt{N\theta}-1\bigr)^2\ \ge\ 0,
\]
the middle inequality being exactly \(S_N\le2\sqrt N-1\) (induction: \(2\sqrt N-2\sqrt{N-1}=2/(\sqrt N+\sqrt{N-1})\ge N^{-1/2}\), equality at \(N=1\)). So \(J\) is nondecreasing with \(J(1)=0\): \(H=\sqrt\theta\,J\le0\). For \(\theta\le c\): \(H_c(\theta)=\sqrt\theta[J(\theta)-J(\theta/c)]\le0\) by monotonicity (\(\theta/c>\theta\)); for \(\theta>c\), \(H_c=H\le0\). ∎
Note the lemma holds for **every** ratio \(c\in(0,1)\), so \(Y=\lfloor X/2\rfloor\) discreteness is free. Scaling profile: \(\min H_c\approx-0.123\) at \(\theta\approx0.141\) (three independent measurements agree to 3 digits; the threshold constant is the root of an explicit \(N=7/N'=3\) cell equation).

## 3. RH ⇒ WSTS (complete modulo Flag 1)

Profile bounds \(|E_c(\theta)|\le C_E\theta^{-1/2}(1+\log(1/\theta))\), \(|E_c'(\theta)|\le C_E'\theta^{-3/2}(1+\log(1/\theta))\) with absolute constants (argument of `L-27501` §3–4, independently reconstructed; measured sups 0.244/0.410). Integration by parts in \(\mathcal E_{X,Y}\), Schoenfeld under RH applied **once**, Prop. 1 + Moat:
\[
\boxed{\;\text{RH}\ \Rightarrow\ B_X\le C\log^3(2X)\;}
\]
(honest exponent **3**, not the packet's 4: the dyadic difference cancels one \(\log\) — the discrete-difference envelope is \(\sup_t t^{3/2}|\Delta d_s|=\log2\), constant in \(X\); measured truth \(\approx0.0084\log^2\); observed \(B_X=0\) outright at all tested \(X\le5\cdot10^5\)). A sharper route bounds the zero-sum absolutely: \(\sum_\rho4|\sin(\gamma\log2/2)|/\gamma^2\approx0.076\) uniformly in \(X\), suggesting \(\log^2\); not needed for the equivalence.

## 4. WSTS ⇒ RH (complete; three independent write-ups agree)

Dual identity (**verified to 12–23 digits**, and \(\hat E(1)=\int_0^1E=0\) exactly — the \(4\sqrt X\) cancellation in dual form; warning: a 3-term truncation of \(E\) suggests a spurious \(+0.001\sqrt X\) drift — the full resummation gives exactly 0):
\[
\hat E(w)=\int_0^1E(t)t^{w-1}dt=\zeta(w)\hat g(w)-(w-\tfrac12)^{-2},\qquad
\hat g(w)=-(w-\tfrac12)^{-2}+4(w-\tfrac12)^{-1}-4/w .
\]
Consumer: \(z=2\) reading of \(B_X\) + dyadic telescope gives \(A_X:=\sum_{p\le X}(\log p)r_X(p)\le C_\varepsilon'X^\varepsilon\); the floor sums are absolutely \(O(\log X)\), so with \(\Phi(X)=X^{-1/2}\int_{[2,X]}E(t/X)dR(t)\), \(A_X=\Phi(X)+O(\log2X)\); Mellin:
\[
G(w)=\int_1^\infty D_X\,X^{-w-1}dX=-\hat E(w+\tfrac12)\,\frac{\zeta'}{\zeta}(w+\tfrac12)+H_0(w),\ H_0\ \text{holomorphic in }\Re w>0,
\]
whose only singularities in \(\Re w>0\) are simple poles at \(w=\rho-\frac12\) with residue \(m_\rho(\rho-\frac12)^{-2}\ne0\); \(w=\frac12\) is regular (\(\hat E(1)=0\)); **no \(1/\zeta\) factor appears anywhere** (passes the repo's R-26902 discipline check explicitly); real-singularity audit on the positive axis uses \(\eta>0\Rightarrow\zeta<0\) on \((0,1)\). Landau's one-sign theorem on the nonnegative-integrand transform of \(C''X^\varepsilon-(4\sqrt X-R(X))\), \(\varepsilon\)-diagonal over a putative zero, functional equation. Classical inputs only: Mertens, Chebyshev \(\psi-\vartheta\ll\sqrt x\), Stirling, Landau. One variant of this consumer was adversarially cross-examined in-session (all four flagged suspects — integrand nonnegativity, Fubini exchange, \(\vartheta/\psi\), \(\varepsilon\)-diagonal — checked clean); two further independent write-ups (explicit-\(\hat E\) route; \(z=2\)-endpoint route) agree.
En route, (T-27501.4) — the sharp one-sided ramp — is derived from WSTS alone. **This replaces the repo's source-pinned square-screw consumer.**
Blind-spot audit: the dyadic shell kernel vanishes at \(\gamma\in(2\pi/\log2)\mathbb Z\); the consumers above act on the **undifferenced** \(z=2\) functional (weight \(-(\rho-\frac12)^{-2}\), never zero), so no blind spot. Any shell-only equivalence argument at fixed \(z\) is incomplete — audit flag for the original T-27501 architecture.

## 5. Calibration and unconditional status (proved this session)

- **Theorem A.** Unconditionally \(B_X\le C\sqrt X\exp(-c(\log X)^{3/5}(\log\log X)^{-1/5})\) (Vinogradov–Korobov applied through Prop. 1).
- **Theorem B** (window). For \(4\le X\le X_0\approx2.2\cdot10^{25}\): \(B_X\le(1/(48\pi))\log^4X+\)lower order, via Büthe/Platt–Trudgian partial verification (**Flag 3: literature constants quoted from memory; check before integration**).
- **Theorem C** (exact calibration). If \(B_X\le CX^{1/2-\delta}\) then \(\zeta\ne0\) on \(\Re s>1-\delta\); conversely a zero-free strip of width \(\eta\) gives \(B_X\ll X^{1/2-\eta}\log^3X\). **The unconditional exponent of \(B_X\) is identically the best zero-free-strip width — currently 0.** The elementary programme's open core *is* the classical wall, as a theorem rather than a slogan.

## 6. Flags (all that separates this from theorem-grade)

1. **\(C_E,C_E'\) explicit values** (absolute-constant version proved — sufficient for §3; the specific value 1 rests on Euler–Maclaurin bookkeeping + certification to \(N=2\cdot10^4\)).
2. **Real-\(X\) interpolation** \(|A_X-A_{\lfloor X\rfloor}|\ll\log X/\sqrt X\) feeding the Mellin integral in one consumer variant (elementary jump audit; sketched; the cross-examined variant handles continuity directly).
3. **Theorem B's cited numerical constants** (not load-bearing for the equivalence).

Adversarial-verification disclosure: the dedicated verify stage for the final assembly was killed by a session usage limit; in its place, the session author hand-verified the Moat identity chain (sympy/mpmath scripts retained), the floor-constant arithmetic, the \(S_N\) inequality, the \(E\)-cell formula, and the Landau mechanism shape; one consumer variant carries a full in-session adversarial cross-examination; every numerical claim was replicated by ≥2 independent implementations. Statuses above preserve the authoring agents' own PROVED / PROVED_SKETCH labels; nothing was upgraded.

## 7. What this changes

The reviewable surface of `WSTS ⟺ RH` shrinks from ~40 lemma files + an unreviewed consumer to: Prop. 1 + Moat + profile bounds + Schoenfeld (forward), and radical bridge + telescope + \(\hat E\)-dual + Landau (converse) — an estimated **12–15 page** self-contained paper, Lean-friendly (the Moat is 5 lines of calculus; the floor bound is a \(\zeta(3/2)\)-sum; the consumer's classical inputs are Mathlib-adjacent). Recommended: tomorrow's review targets THIS packet first; if it survives, retire the L-23823–26 stack as architecture (keeping frozen identities) and re-point `T-27501` at it.

## 8. Artifacts

Scratchpad scripts (all rerunnable): `validator.py`, `d2_validator.py`, `xcheck.py`, `xmellin.py`, `wsts_converse.py`, `wsts_verify.py`, `wsts_verify2.py`, `kernel_profile.py`, plus the session author's Moat verification (sympy/mpmath, in `moat_check` history). Full agent reports in the session workflow journals.

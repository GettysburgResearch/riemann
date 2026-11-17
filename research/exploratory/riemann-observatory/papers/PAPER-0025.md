# PAPER-0025 — Sharper bounds for the error in the prime number theorem assuming the Riemann hypothesis

| Field | Value |
|---|---|
| Authors | Lee, Ethan Simpson; Nosal, Paweł |
| Year / stratum | 2026 / S7 |
| Venue | J. Number Theory 283, 241-258 (2026) |
| Identifiers | DOI [10.1016/j.jnt.2025.12.003](https://doi.org/10.1016/j.jnt.2025.12.003) · arXiv [2312.05628](https://arxiv.org/abs/2312.05628) |
| MSC | 11N05, 11N37, 11M06 |
| Families | A |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — arxiv.org/abs/2312.05628 |
| Selection | score 4.6, in-pool citations 1, seed lists 0, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Give explicit, numerically sharp bounds for |psi(x)-x| and |theta(x)-x| under RH, of the shape sqrt(x) log x (log x - log log x)/(8 pi), valid from small x. Derive explicit versions of the error terms in Mertens' three theorems from them, improving Schoenfeld 1976.

**Historical motivation.** Rosser-Schoenfeld 1962-76 program of explicit bounds for psi, theta, pi under RH; Schoenfeld's bound sqrt(x) log^2 x /(8 pi) for x>=73.2 (1), Grenie-Molteni for x>=2.3e9 with log x-2.

### Main results

- **THM-PAPER-0025-1** (Theorem 1.1, theorem, scope: conditional; Sec. 1, p. 2). Assume RH. For all $x\ge 11$: $|\psi(x)-x|\le \sqrt{x}\,\log x\left(\frac{\log x}{8\pi}-\left(\frac1{2\pi}+\frac{1.465}{\log x}\right)\log\log x+1.2325\right)$. *Conditional on:* RH.
- **THM-PAPER-0025-2** (Theorem 1.2, eq. (2), theorem, scope: conditional; Sec. 1, p. 2). Assume RH. For all $x\ge 101$: $|\psi(x)-x|\le \frac{\sqrt{x}\,\log x\,(\log x-\log\log x)}{8\pi}$. *Conditional on:* RH.
- **THM-PAPER-0025-3** (Theorem 1.2, eq. (3), theorem, scope: conditional; Sec. 1, p. 2). Assume RH. For all $x\ge 2657$: $|\vartheta(x)-x|\le \frac{\sqrt{x}\,\log x\,(\log x-\log\log x)}{8\pi}$. *Conditional on:* RH.
- **THM-PAPER-0025-4** (Corollary 1.3 (4)-(7), corollary, scope: conditional; Sec. 1, p. 3). Assume RH. With B, C, E the Mertens constants: $\left|\sum_{p\le x}\frac{\log p}{p}-\log x-E\right|\le \frac{3(\log x)^2}{8\pi\sqrt x}$ for $x\ge 43.1$; $\left|\sum_{p\le x}\frac1p-\log\log x-B\right|\le\frac{3\log x}{8\pi\sqrt x}$ for $x\ge 24.4$; $\left|e^{C}\log x\prod_{p\le x}(1-1/p)-1\right|\le\frac{3\log x}{8\pi\sqrt x}$ for $x\ge 23.8$; $\left|\frac{e^{-C}}{\log x}\prod_{p\le x}(1-1/p)^{-1}-1\right|\le\frac{3\log x}{8\pi\sqrt x}$ for $x\ge 24.2$. *Conditional on:* RH.

### Key definitions

- psi(x)=sum_{n<=x} Lambda(n); theta(x)=sum_{p<=x} log p
- psi_1(x)=int_0^x psi(t)dt = sum_{n<=x}(x-n)Lambda(n)
- H_1 = 10^7; omega_1 = 16.2106480369 (bound for sum over 0<gamma<=H_1... of 1/|gamma|-type quantity)
- B, C, E: Mertens constants 0.26149..., 0.57721..., -1.33258...

### Principal lemmas

- **THM-PAPER-0025-L1** (Lemma 2.1 (Lehman); Sec. 2, p. 4 (statement partly garbled in text extraction)). If $\phi$ is continuous, positive, non-decreasing on $[2\pi e,\infty)$ with suitable decay, then $\sum_{\gamma>T}\phi(\gamma)/\gamma^{?}$ is bounded by an integral against $N(t)\le\frac{t}{2\pi}\log\frac t{2\pi}$ (exact form: partial summation using the Backlund-type bound (8)-(9)); used to bound tails of sums over zeros. — *Role:* Converts the explicit N(T) bound into bounds for 1/|gamma| tail sums.
- **THM-PAPER-0025-L2** (Lemma 3.1; Sec. 3.1, p. 4-5). Assume RH, $h=x/y$, $y\ge H_1:=10^7$. Then the sum over zeros in the smoothed explicit formula for $\psi_1(x\pm h)-\psi_1(x)$ is bounded by $\frac12\left(1+\frac2y\right)^{3/2}\frac{\sqrt x\log y}{\pi}+\frac{2.6\sqrt x}{\pi y}\ldots+\sqrt x\cdot O(\ldots)\log^2(y/2\pi)$ (with explicit constants, ending in 2.84); statement partially garbled in extraction. — *Role:* Main analytic input for Theorem 1.1 at x >= 10^19 (explicit Goldston method).
- **THM-PAPER-0025-L3** (Lemma 3.2; Sec. 3.1, p. 6). Assume RH, $y=\sqrt{x}/\log x$, $x\ge 10^{19}$. Then the Lemma 3.1 bound is at most $\frac{\sqrt x\log x}{2\pi}\left(\frac{\log x}{4}-\log\log x\right)$-type expression (exact constants garbled). — *Role:* Optimised choice of y; ties to the 8 pi constant.
- **THM-PAPER-0025-L4** (Lemma 3.3; Sec. 3.2, p. 7-9). Assume RH, $H_1=10^7$. A Rosser-Schoenfeld smoothed explicit formula bound (m, delta parameters, delta=log x/(m pi sqrt x)) gives $|\psi(x)-x|/\sqrt x$ at most an expression in T_0(x), omega_1, H_1 (log(T_0/2pi)/(2pi) type terms). — *Role:* Gives (2),(3) in the range e^{30369.582} > x > 10^19 when combined with a case table of coefficients 0.99865 log x ... 0.87158 log x.

### Proof architecture

For x>=10^19: make Goldston's method explicit. Use monotonicity of psi in (12) to sandwich psi by (psi_1(x+h)-psi_1(x))/h, use the explicit formula (13) for psi_1 (second-order Chebyshev integral), truncate the zero sum at height y, treat |gamma|<=y with the Taylor expansion (15), tail via Lehman's lemma and the verified RH height ω_1 sum over 1/|gamma| (eq. (10), 16.2106...), and choose y = sqrt(x)/log x. This gives Theorem 1.1 for x>=10^19 (Lemma 3.1, 3.2). For 11<=x<=10^19 Theorem 1.1 follows from Buthe's computation (18). Theorem 1.2 for x>=e^{30369.582} follows from Theorem 1.1; for 10^19<x<e^{30369.582} it follows from Lemma 3.3 (Rosser-Schoenfeld smoothed formula with m>0 integer, T_1 cut, RH kills S3, S4); the remaining x in [101, 10^19] by Buthe's computation. Mertens corollary follows from partial summation applied to the psi and theta bounds.

Dependency edges: CAND-02344 → Buthe 2018 explicit psi bound to 10^19 (imports); CAND-02344 → Schoenfeld 1976 (improves); CAND-02344 → Goldston explicit smoothing method (makes explicit)

**Imported results.** Buthe (2018) explicit verification of |psi(x)-x|<=0.94 sqrt(x) for 11<=x<=10^19 [4] -- exact citation as in paper ref. [4]; Brent-Platt-Trudgian explicit N(T) bound (8) [2, Cor. 1] and Trudgian; Rosser-Schoenfeld 1975/Schoenfeld 1976 explicit formula lemma [15, Lem. 8], [16]; Skewes lemma [17, Lem.1(ii)] eq. (11); Platt-Trudgian sum over zeros omega_1 = 16.2106480369 eq. (10) from [7, Tab.1]; Lehman Lemma 2.1; Grenie-Molteni [9]

**Techniques.** explicit formula for psi_1; Goldston smoothing by finite difference; Lehman explicit zero-sum lemma; Rosser-Schoenfeld smoothed explicit formula (Lemma 8 of [15]); partial summation; interval numerics (case table of coefficients on ranges of log x); imported zero-free/verified-height data

## Context and interpretation

**Importance and obstacle overcome.** Tightens the standard RH-conditional explicit prime-number-theorem error to a clean form valid already from x=101 (psi) and 2657 (theta), and carries it to Mertens' theorems. The obstacle is controlling the sum over zeros uniformly: handled by combining a smoothed explicit formula with verified zero-height data and an optimised truncation, plus a stitched numerical verification across regimes.

**Relation to prior work.** Improves eq. (1): Schoenfeld [16], Grenie-Molteni [9] (|psi-x| <= sqrt(x)log x(log x-2)/(8 pi) only for x>=2.3e9). Replaces Schoenfeld's Mertens bounds in [16, Cor. 2-3] with sharp ranges to one decimal.

**Limitations and open questions.** All results are conditional on RH. The constant 1/(8 pi) is the same as in Schoenfeld's large-x bound; the new gain is in lower-order terms and small x. The theorems are tied to verified ranges (Buthe's 10^19 computation, RH zero verification to height ~3e12). No claim about asymptotic optimality: the true size under RH conjecturally has sqrt(x)(log log log x)^2-type oscillations (Montgomery-Soundararajan) and the 8 pi constant is not believed sharp in the limit.

**Ideas in remarks/appendices/abandoned paths.** Case table before (23): coefficient of log x on ranges of log x (0.87158 ... 0.99865) as a piecewise-optimal replacement for a single T_0 choice (Sec 3.2, p. 9). Remark that Brent-Platt-Trudgian refined Lemma 2.1 but was not used (Sec 2).

## Research potential

- **Hypotheses that might be weakened.** Theorems are conditional on RH only; the verified-zero input (omega_1, N(T) bounds, Buthe 10^19) is where the constants come from. A partial-RH variant (all zeros below height H on the line, plus a zero-density substitute above) is a natural weakening, since the proof uses RH for gamma>H_1 through the tail bounds and through S3=S4=0 in Lemma 3.3.
- **Generalizations.** Same method should give explicit RH-conditional bounds for pi(x) - li(x), Chebyshev-type bounds for primes in arithmetic progressions under GRH, and for Dirichlet L-function analogues with explicit N(T,chi).
- **Candidate connections.** The Robin-type inequalities (Robin arithmetic programme): Mertens product errors under RH feed directly into explicit estimates for sigma(n)/(n log log n), so Corollary 1.3 (6)-(7) is a reusable input for Robin-inequality verification ranges.
- **Reusable lemmas.** Lemma 3.1 (explicit Goldston step with h=x/y) and Lemma 3.3 template (parameters m, delta, T_1) are reusable explicit-formula lemmas; eqs (8)-(11) as a packaged zero-data interface.
- **Possible experiments.** Recompute the constants in Lemma 3.1/3.2 and the case table before Lemma 3.3 in interval arithmetic with the stated omega_1 and N(T) bounds; test whether the 1.465 coefficient and 1.2325 can be improved by re-optimising y and h; compute max over x in [101,10^9] of |psi(x)-x|/(sqrt x log x (log x - log log x)/(8 pi)) to see how tight Thm 1.2 is.
- **Risks / barriers.** The 1/(8 pi) leading constant looks like a limit of the method (sup of the zero-sum under only N(T) knowledge); further improvement needs pair-correlation-type input, not explicit-formula numerics.

## Audit notes (Level 1 reader)

Text extraction garbled several displayed formulas (Lemma 2.1 exact form, Lemmas 3.1-3.2 constants), so those are summarised, not quoted verbatim. Internal consistency noted: Thm 1.2 stated stronger than Thm 1.1 for x <= e^{30369.581...}; proof of (2) uses e^{30369.582}. No error noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-02344`; harvest queries: kw_RH_any, msc_11M06, msc_11N05, arxiv_rh_abs, arxiv_rh_ti.
- Triage decision: include — Sharper explicit RH-conditional PNT error bounds.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

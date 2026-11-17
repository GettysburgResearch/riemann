# PAPER-0145 — Currently, there are no reasons to doubt the Riemann hypothesis: the zeta function beyond the realm of computation

| Field | Value |
|---|---|
| Authors | Farmer, David W. |
| Year / stratum | 2026 / S7 |
| Venue | Bull. Am. Math. Soc., New Ser. 63, No. 4, 559-636 (2026) |
| Identifiers | DOI [10.1090/bull/1890](https://doi.org/10.1090/bull/1890) · arXiv [2211.11671](https://arxiv.org/abs/2211.11671) |
| MSC | 11M26, 11M50 |
| Families | B, G |
| Work type | survey |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — arxiv:2211.11671 |
| Selection | score 2.4, in-pool citations 0, seed lists 0, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Do the five published arguments for doubting RH (Ivic, Blanc) give good reasons? Via random-matrix (unitary polynomial) analogies and 'carrier waves', the paper argues no, and replaces computational extrapolation with 33 Principles about Z(t) at heights beyond computation.

**Historical motivation.** Ivic (2008) listed four reasons to doubt RH and Blanc (2018+) a fifth; the paper answers them with post-2000 RMT and carrier wave understanding.

### Main results

- **THM-PAPER-0145-1** (Principle 12.1 / 12.2, methodological principle, scope: global; Sec. 12, p. 54). Any fact that translates directly to a statement about characteristic polynomials of random unitary matrices (for which the RH analogue is true) cannot be used as evidence against RH; any fact from numerical computation of zeta, other than an actual counterexample, cannot be used as evidence against RH.
- **THM-PAPER-0145-2** (Reason 1 analysis (Principle 12.3), argument, scope: global; Sec. 12.1, p. 54-55). Lehmer pairs (e.g. gap <0.054 at zero 6709) do not suggest RH is 'barely true' in any meaningful sense because nearest-neighbour spacings of CUE eigenvalues are supported on all of $(0,\infty)$; RH is barely true anyway in other senses ($Z(t)\pm\delta$ has nonreal zeros; $\Lambda\ge0$ by Rodgers-Tao so $\Lambda=0$ is the only value consistent with RH).
- **THM-PAPER-0145-3** (Reason 2 analysis (Sec. 12.2), argument, scope: global; Sec. 12.2, p. 55-56). The 'tightly packed spikes' picture of Z(t) with growing oscillation (Ivic) is forced even without RH since a positive proportion of zeros lie on the line and carrier waves are expected; appearance is a matter of axis scaling.
- **THM-PAPER-0145-4** (Equation (12.1) (Blanc identity [19]), cited identity, scope: global; Sec. 12.3, p. 56). For smooth $f$ on a neighbourhood of $[-a,a]$ with distinct zeros $x_0,\dots,x_n$ in the interval: $\sum_{k=1}^r\Psi_{2k-1}(x,a)f^{(2k-1)}(a)-\sum_{k=1}^r\Psi_{2k-1}(x,-a)f^{(2k-1)}(-a)=\int_{-a}^a\Psi_{2r-1}(x,t)f^{(2r)}(t)\,dt$, where $\Psi_\ell$ is given by Bernoulli polynomials and weights $\mu_k(x)$ with $\sum_k\mu_k=0$.
- **THM-PAPER-0145-5** (Theorem 12.6 (Blanc [18]), cited theorem (RH-unconditional), scope: asymptotic; Sec. 12.3, p. 58). For $T$ sufficiently large, $\delta>1/2$, $a=o(T/\theta'(T))$ and $\delta\theta'(T)\le2K\le2\theta'(T)^2$: $|Z^{(2K)}(t)|\le2\zeta(1/2+\delta)\theta'(T)^{2K}$ for $t\in[T-a,T+a]$, where $\theta'(t)\sim\frac12\log\frac t{2\pi}$.
- **THM-PAPER-0145-6** (Analysis of Blanc's argument (Sec. 12.3) and Reason 3 conclusion, argument, scope: asymptotic; Sec. 12.3, p. 56-60). Blanc's contradiction from a large zero gap needs the left side of (12.1) large and the right side small. Farmer shows (using Table 12.5 from Bober-Hiary data) that the left side need not be large (Psi_1(x,a) tiny, or cancellation from other terms), and that Theorem 12.6 fails for characteristic polynomials only because the number of derivatives needed for 'cosine as universal attractor' is much larger there, so the argument evades Principle 12.1 yet is not shown to give a contradiction.
- **THM-PAPER-0145-7** (Reason 4 (Sec. 13.1), argument, scope: asymptotic; Sec. 13.1, p. 61-63). Ivic's conjecture $E_k=k/4$ for error terms in $\int_0^TZ^{2k}$ rests on the two data points $E_1=1/4,E_2=1/2$; any other formula (e.g. $E_k=3/4-2^{-k}$, which would imply LH) fits equally; $2k$-th moment asymptotic structure changes at $k=4$ (Conrey-Gonek), more affecting main terms than error terms.
- **THM-PAPER-0145-8** (Reason 5, Principles 13.1 and 13.2, principle / cited theorems, scope: global; Sec. 13.2, p. 63-65). A nontrivial linear combination of L-functions will not satisfy RH (Principle 13.1) and will have infinitely many zeros in $\sigma>1$ (Principle 13.2; theorem for Dirichlet L [Saias-Weingartner], automorphic L, and axiomatic settings). Deuring-Heilbronn function $F_{DH}$ (mod 5 character $\chi_{5,2}$) has first off-line zero near $0.8085+85.699i$ and infinitely many zeros with $\sigma>1$; Bombieri-Hejhal show 100% of zeros on the line for sums of L-functions with same functional equation under additional hypotheses.
- **THM-PAPER-0145-9** (Principles 5.1, 7.4, 10.2 etc. (Sec. 5-10), heuristic model, scope: asymptotic; Sec. 5, 7, 9.3, 10 (skimmed)). Z(t) near t0 is governed by a slowly varying carrier wave (determined by local zero density fluctuations / primes, Principle 10.1), a local universal (CUE/GUE) factor and a global factor; Keating-Snaith law models Z(1/2+it) by characteristic polynomials; Theorem 9.8 (Backlund) LH iff $N(\sigma,T+1)-N(\sigma,T)=o_\sigma(\log T)$ for all $\sigma>1/2$.

### Key definitions

- Z(t) Hardy function and S(t)
- carrier wave
- Lehmer pair
- Deuring-Heilbronn function F_DH
- self-reciprocal polynomial in polar form
- de Bruijn-Newman constant Lambda

### Principal lemmas

- **THM-PAPER-0145-L1** (Theorem 9.8 (Backlund); Sec. 9.3, p. ~45). LH holds iff $N(\sigma,T+1)-N(\sigma,T)=o_\sigma(\log T)$ for every fixed $\sigma>1/2$. — *Role:* imported result used for the LH versus self-reciprocal polynomials comparison
- **THM-PAPER-0145-L2** (Eq. (12.8); Sec. 12.3, p. 59). For a self-reciprocal polynomial Z(z) of degree N in polar form with D=z d/dz, $D^{2K}Z(z)\to$ (N/2)^{2K}z^{-N/2}(z^N+1+o(1)) as K to infinity: roots of D^{2K}Z approach Nth roots of -1 (equal spacing). — *Role:* explains 'cosine is a universal attractor' and why Blanc's bound needs a specific K range
- **THM-PAPER-0145-L3** (Counterexample to analogue of Thm 12.6; Sec. 12.3, p. 59). For $z^{-N/2}(z+1)^N$ and $\kappa N$ D-derivatives with $\kappa<1$ a high-multiplicity zero at z=-1 remains; even N derivatives leave $D^N$ large at z=1 (coefficient $N-\sqrt N$ argument). — *Role:* shows the Blanc theorem analogue is false for unitary polynomials
- **THM-PAPER-0145-L4** (Principle 3.2 / Principle 2.2; Sec. 2 and 3). Z(t) is statistically indistinguishable from -Z(t); any finite sequence of normalized gaps occurs with positive proportion, so snapshots of Z are random-matrix-like. — *Role:* foundation for Reason 2 refutation

### Proof architecture

Expository/heuristic, no new theorems claimed. Structure: (i) build intuition (Sec. 2-11) for Z(t) at large height via CUE analogy, carrier waves, density waves, extreme values; (ii) state Principles 12.1/12.2 as logical filters; (iii) apply to each of five reasons: Lehmer (12.1), large values (12.2), Blanc's derivative-based contradiction (12.3), moment error terms (13.1), Deuring-Heilbronn (13.2); (iv) Sec. 14 uses principles to rebut four 'Mistaken Notions' about computations (largest values at large gaps/many close zeros, Gram's law).

Dependency edges: Reason 3 refutation → Theorem 12.6 (Blanc) (analyzes); Reason 3 refutation → Eq. (12.1) (uses); Reason 5 refutation → Principle 13.1/13.2 (uses); Reasons 1-2 → Principle 12.1 (uses); Principle 12.1 → RH analogue for unitary polynomials (depends on)

**Imported results.** Blanc's identity (12.1) [19] and Theorem 12.6 [18]; Backlund's equivalence of LH [7]; Rodgers-Tao Lambda>=0 [94], Dobner for L-functions [43]; Bombieri-Hejhal zeros of linear combinations [24]; Keating-Snaith law; Montgomery-Odlyzko GUE hypothesis; Conrey-Gonek conjectured k=4 moment

**Techniques.** random matrix analogy (CUE, circular beta ensembles); carrier wave / density wave heuristics; Keating-Snaith moments; comparison with self-reciprocal polynomials; Gaussian multiplicative chaos; Selberg class axioms and linear combinations of L-functions

## Context and interpretation

**Importance and obstacle overcome.** Systematizes why computational and RMT-analogous evidence cannot undermine RH and isolates the only non-RMT-translatable doubt (Blanc's derivative bound), showing it needs finer control than known.

**Relation to prior work.** Responds directly to Ivic [72,73] and Blanc [18,19]; builds on Keating-Snaith, Bombieri-Hejhal, Rodgers-Tao, Odlyzko computations.

**Limitations and open questions.** Paper explicitly does not argue that RH is true. Central steps are heuristics (carrier wave existence is an emergent phenomenon, not proved for zeta); Blanc's argument is not refuted by a theorem but by showing the contradiction is not forced. Author suggests optimizing delta in Theorem 12.6, a companion 'no good reasons to believe RH', and that analogue of Thm 12.6 may hold almost surely for e^N Haar-random unitary matrices.

## Research potential

- **Hypotheses that might be weakened.** Optimize delta>1/2 and the K range in Blanc's Theorem 12.6; test whether the K-range lower bound deltaθ'(T) can be lowered.
- **Generalizations.** Prove the almost-sure analogue of Thm 12.6 for Haar random unitary matrices of size N≈log T (suggested at end of Sec. 12.3) and check whether it would imply anything for zeta.
- **Candidate connections.** Principle 13.2 and Bombieri-Ghosh results on zeros in sigma>1 of Davenport-Heilbronn combinations (CAND-01539) are the same phenomenon; carrier-wave language connects to Gaussian multiplicative chaos and to Arguin et al. maxima.
- **Reusable lemmas.** Eq. (12.1)/(12.2)-(12.3) Blanc identity and the Table 12.5 method give a computable test of whether a hypothetical large gap contradicts RH; the polynomial (12.7)-(12.8) differentiation computation is reusable for any self-reciprocal model.
- **Possible experiments.** Recompute Table 12.5 for other large-gap windows (Bober-Hiary data) to see whether Psi_1 cancellation persists; numerically test Thm 12.6 constants for the first 10^6 zeros; Monte Carlo check of the almost-sure Blanc analogue for U(N).
- **Risks / barriers.** Principle 12.1 is a methodological claim, not a theorem: a fact true of unitary polynomials may still fail to be evidence for RH, but equally cannot be evidence against; RMT analogy does not control arithmetic (primes) effects.

## Audit notes (Level 1 reader)

Paper is a survey/heuristic argument; Principles 12.1 and 12.2 are logic-of-evidence statements, not mathematical results, and should not be recorded as theorems. In the Sec. 12.3 text Table 12.5 is only checked for one dataset (Bober-Hiary, near t≈19-20), not for a large gap at large height; the conclusion that Blanc's argument fails is conditional on this illustration. Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-02664`; harvest queries: kw_RH_any, msc_11M26, msc_11M50, arxiv_random_matrix_zeta, arxiv_rh_abs, arxiv_rh_ti.
- Triage decision: include — Farmer rebuts published arguments doubting RH using theory, RMT and examples.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

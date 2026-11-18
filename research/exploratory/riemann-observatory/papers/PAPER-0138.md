# PAPER-0138 — A theorem on the distribution of values of the Riemann zeta-function

| Field | Value |
|---|---|
| Authors | Voronin, S. M. |
| Year / stratum | 1975 / S3 |
| Venue | Sov. Math., Dokl. 16, 410 (1975); translation from Dokl. Akad. Nauk SSSR 221, 771 (1975). |
| Identifiers | zbMATH [0326.10035](https://zbmath.org/?q=an:0326.10035) |
| MSC | 11M06 |
| Families | A, B |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://mathnet.ru/php/getFT.phtml?jrnid=dan&paperid=38936&what=fullt&option_lang=eng |
| Selection | score 2.9256, in-pool citations 9, seed lists 0, triage relevance 5 |

## Mathematical content (Level 1: full text read)

**Research question.** Show that analytic non-vanishing functions on a small disc near the line $\sigma=3/4$ are approximated uniformly by vertical translates of $\zeta$ (the original announcement of universality of the zeta-function).

### Main results

- **THM-PAPER-0138-1** (Theorem (only theorem), theorem, scope: asymptotic; p. 771, Theorem). Let $0<r<\tfrac14$. Let $f(s)$ be analytic in the disc $|s|<r$, continuous on $|s|\le r$, with no zeros in $|s|<r$. Then for every $\varepsilon>0$ there exists a real $T$ such that $\max_{|s|\le r}\left|f(s)-\zeta\!\left(s+\tfrac34+iT\right)\right|<\varepsilon$. (The printed text writes the quantifier as 'there exists $T=T(r)$' with a garbled equation; the statement is existence of a shift $T$, with no density statement.)
- **THM-PAPER-0138-2** (Remark, remark/claim, scope: asymptotic; p. 771, Zamechanie). The assertion of the theorem holds for all Dirichlet L-functions (stated without proof).

### Principal lemmas

- **THM-PAPER-0138-L1** (Lemma (finite Euler products); p. 771, Lemma). Under the conditions of the theorem, for every $y>0$ and $\varepsilon>0$ there is a finite set $M$ of primes containing all primes $<y$ and real numbers $\theta_k$ (indexed by $p_k$, the $k$th prime) such that the finite Euler product $\prod_{p_k\in M}\left(1-e^{-2\pi i\theta_k}p_k^{-s-3/4}\right)^{-1}$ approximates $f(s)$ on $|s|\le r$ to within $\varepsilon$ (the exact displayed formula is garbled in the extraction; this is the standard form of the lemma and my reading). — *Role:* Approximation of $f$ by finite Euler products with arbitrary phases on primes; then Kronecker/Bohr-type argument transfers to $\zeta(s+3/4+iT)$.

### Proof architecture

Deduce theorem from Lemma following Bohr's scheme (Titchmarsh, Theory of the Riemann zeta-function [Russian ed. 1953], p. 300). The Lemma is proved by using conditionally convergent series in Hilbert space (Pecherskii, DAN 209 no. 6 (1973), rearrangement theorem; p. 1285) and by analogy to Lemma 11 of Voronin's earlier paper on non-zero values (Trudy MIAN 128 (1972)). No details are given; the note is an announcement.

**Techniques.** Bohr's approach via Euler products and Kronecker density; conditionally convergent series in Hilbert space (Pecherskii rearrangement); logarithm of non-vanishing $f$ approximated by prime sums

## Context and interpretation

**Importance and obstacle overcome.** Overcame the obstacle that $\log\zeta$ is not given by a convergent Euler product in the strip $1/2<\sigma<1$ by using rearrangement of conditionally convergent prime series. Starting point for universality theory.

**Relation to prior work.** 

**Limitations and open questions.** Announcement only; proof omitted. The positive-lower-density statement and the extension to arbitrary compact sets with connected complement and to general $L$ belong to Voronin's longer Izv. paper (1975, vol. 39) and later works, not this note. Non-vanishing is necessary, so zeta zeros off-line (a failure of RH) are not excluded or detected by the theorem; the disc lies in $1/2<\sigma<1$ ($|s|<1/4$ around $3/4$).

## Research potential

- **Hypotheses that might be weakened.** The hypothesis $f\ne0$ is sharp for discs; generalization: compact sets with connected complement (Bagchi, Reich). Known consequence: RH is equivalent to the self-approximability of $\zeta$ in $1/2<\sigma<1$ (Bagchi). Experiment: quantify effectiveness of $T$ (Lamzouri-Lester-Radziwill, arXiv:1611.10325).
- **Generalizations.** Universality for L-functions and Dedekind zeta (family A) as the remark claims; joint universality for non-equivalent L-functions.
- **Candidate connections.** Bagchi's criterion: RH iff for each $\varepsilon$, $\liminf_T\frac1T\mathrm{meas}\{t\in[0,T]:\max_{|s-3/4|\le r}|\zeta(s+it)-\zeta(s)|<\varepsilon\}>0$ ($r<1/4$): a concrete use of this theorem's Hilbert-space step.
- **Reusable lemmas.** The finite Euler product approximation lemma (phases $\theta_k$ free) is reusable in any problem needing prime-supported approximations of analytic functions.
- **Possible experiments.** Compute minimal $T$ (and its growth) such that $\zeta(s+3/4+iT)$ approximates $e^{s}$ or another target on small discs.
- **Risks / barriers.** Existence only; no effective bound or density in this note. Does not decide RH since universality holds regardless; mixing statement about zero-free targets is what couples to RH only via Bagchi's equivalence.

## Audit notes (Level 1 reader)

Triage summary says 'positive lower density set of t' but the note proves only existence of $T$ (density is in the Izv. paper). The quantifier $T=T(r)$ in the printed theorem is garbled/misleading since $T$ depends on $f$ and $\varepsilon$. The key Lemma display is unreadable in the extraction; I did not verify the exact formula.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00604`; harvest queries: msc_11M06.
- Triage decision: include — Landmark universality theorem for zeta in the strip 1/2<Re s<1.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

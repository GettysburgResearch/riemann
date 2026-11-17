# PAPER-0130 — On the order of \(\zeta(+it)\)

| Field | Value |
|---|---|
| Authors | Bombieri, E.; Iwaniec, H. |
| Year / stratum | 1986 / S4 |
| Venue | Ann. Sc. Norm. Super. Pisa, Cl. Sci., IV. Ser. 13, 449-472 (1986). |
| Identifiers | zbMATH [0615.10047](https://zbmath.org/?q=an:0615.10047) |
| MSC | 11M06, 11L40 |
| Families | A |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — http://www.numdam.org/item/ASNSP_1986_4_13_3_449_0.pdf |
| Selection | score 3.8695, in-pool citations 20, seed lists 2, triage relevance 5 |

## Mathematical content (Level 1: full text read)

**Research question.** Improve the exponent in the subconvexity bound for zeta(1/2+it) beyond Kolesnik's 139/858 using a new method that evaluates, rather than bounds by repeated Cauchy, an incomplete Gauss sum arising after one Weyl differencing. It combines Weyl-Hardy-Littlewood, van der Corput and Vinogradov ideas.

**Historical motivation.** Reduce the exponent in subconvex bounds for zeta on the critical line, a classical problem running from Hardy-Littlewood and Weyl through van der Corput.

### Main results

- **THM-PAPER-0130-1** (Theorem (Intro, eq. 1.3), theorem, scope: asymptotic; p.449, eq. (1.3)). For $t>1$ and $\varepsilon>0$: $\zeta(\tfrac12+it)=O(t^{\theta+\varepsilon})$ with $\theta=9/56=0.16071\ldots$, the implied constant depending on $\varepsilon$ alone.
- **THM-PAPER-0130-2** (Theorem 4.1, theorem, scope: asymptotic; Sec. 4, p.459). Let $A,C>1$, $\Delta_1,\Delta_2>0$, and let $\mathcal N(\Delta_1,\Delta_2;A,C)$ be the number of pairs $\{a/c,a_1/c_1\}$ with $a,a_1\sim A$, $c,c_1\sim C$, $(a,c)=(a_1,c_1)=1$, $\|\bar a/c-\bar a_1/c_1\|<\Delta_1$ and $|ac-a_1c_1|<\Delta_2AC$ (where $\bar a$ is the inverse of $a$ mod $c$, $\|\cdot\|$ the distance to the nearest integer). Then $\mathcal N\ll(AC+\Delta_1\Delta_2A^2C^2+\Delta_1^2A^2C+\Delta_2A^2+\Delta_2C^2)(AC)^\varepsilon$, with the implied constant depending on $\varepsilon$ and on the constants implied in $\sim$.
- **THM-PAPER-0130-3** (Theorem 4.2, theorem, scope: asymptotic; pp.459-464). Generalization of Theorem 4.1 to fractions in $\mathscr P(r,s)=\{a/c: a\sim A,\ c\sim C,\ (a,c)=1,\ a=O(\cdot r),\ c=O(\cdot s)\}$ for coprime $r,s$, proved by induction on $rs$. Theorem 4.1 is the case $r=s=1$. The displayed bound was not read in OCR; see the page image.
- **THM-PAPER-0130-4** (Estimate (5.4), proposition, scope: asymptotic; Sec. 5, pp.465-471, eqs. (5.1)-(5.4), (5.21)). If $f$ is smooth with $|f^{(j)}(m)|\sim FM^{-j}$ for $m\sim M$, $j\ge1$, and $F^{3/7}<M<F^{1/2}$, then $S_f(M)=\sum_{m\sim M}e(f(m))\ll F^{\theta+\varepsilon}M^{1/2}$ with $\theta=9/56$. Together with the exponent pair $(1/9,13/18)$ for $1<M<F^{3/7}$ this gives $M^{1/2}F^{10/63}$, which is stronger than (5.4) there. The theorem follows from these via the standard approximation, Titchmarsh [9].

### Key definitions

- a ~ A: A < a <= 2A (read from convention page; exact form not verified in OCR)
- \bar a: inverse of a mod c
- S_f(M)=\sum_{m\sim M}e(f(m))

### Principal lemmas

- **THM-PAPER-0130-L1** (Lemma 2.4; p.452). Bilinear-form large-sieve-type inequality for sums over points $\xi\in\mathbb R^K$, $\eta\in\mathbb R^K$ with spacing/box parameters, derived from Lemma 2.3 (Beurling-Selberg majorant, via Vaaler). The displayed inequality was lost in OCR. — *Role:* Bounds the bilinear form arising after Holder in Sec. 5 by counting close pairs.
- **THM-PAPER-0130-L2** (Lemmas 2.5-2.10; pp.454-458). Airy-Hardy integral estimate, stationary-phase style estimates for Poisson summation (2.6-2.8), Poisson summation mod c (2.9), Gauss sum evaluation G(a,l;c) (2.10). — *Role:* Technical tools for completing and evaluating the incomplete Gauss sum.
- **THM-PAPER-0130-L3** (Lemma 3.1; p.458). Asymptotic evaluation of the perturbed incomplete Gauss sum $S(\mu;a,b;c)$ mod c via Poisson summation, with error $\ll c^{-1/2}\sum_h(\ldots)$ and a main term from the Gauss sums $G(a,h;c)$. — *Role:* Replaces Weyl's repeated Cauchy step by evaluation of the Gauss sum; this is the key new idea.
- **THM-PAPER-0130-L4** (Lemmas 4.1-4.3; pp.461-463). Count 'trivial' pairs (Lemma 4.1), pairs differing by an SL(2,Z) transformation with small matrix (Lemma 4.2), and a Cauchy reduction for induction (Lemma 4.3). — *Role:* Inductive proof of Theorem 4.2.
- **THM-PAPER-0130-L5** ((5.15); p.470). Bound $\mathscr B(a;\mathfrak D)\ll H^{4+\varepsilon}$, imported from the companion paper [1], Bombieri-Iwaniec, Some mean-value theorems for exponential sums, same volume, pp.473-486. — *Role:* Handles the second system of conditions in the Holder step.

### Proof architecture

Apply Weyl differencing once to $S_f(M)$, reducing to cubic exponential sums. Rational approximation of the middle coefficient with denominator c, then Lemma 2.1 (partial summation) and Poisson summation (Lemma 3.1) evaluate the incomplete Gauss sums mod c; the main term depends on h~H. Holder, then Lemma 2.4, reduces to counting pairs of fractions (a/c, a1/c1) satisfying (5.9), (5.11), (5.16). The companion paper [1] gives (5.15). The constraint (5.16) is discarded, which the authors call wasteful. For $f=t\log x$, $c^{-1}\nu(a,c)$ is a function of $ac$, so (5.11) becomes $|ac-a_1c_1|<\Delta_2AC$, Theorem 4.1 applies, and optimizing with $N=MF^{-2/7}$ gives $F^{9/56}$.

Dependency edges: CAND-01032 → Bombieri-Iwaniec companion mean-value paper (imports (5.15))

**Imported results.** Exponent pair theory (Phillips 1933, Rankin 1955), exponent pair (1/9,13/18); Beurling-Selberg function (Vaaler, Bull. AMS 12 (1985)); Approximate functional equation/Titchmarsh, Theory of the Riemann zeta-function (1951), Ch. 5; Bombieri-Iwaniec, Some mean-value theorems for exponential sums (companion, same volume); Kolesnik, On the method of exponent pairs, Acta Arith. 45 (1985) (prior record)

**Techniques.** Weyl differencing; Poisson summation / evaluation of incomplete Gauss sums; Beurling-Selberg extremal functions (Vaaler); counting close pairs of modular inverses a-bar/c; induction on rs; exponent pairs

## Context and interpretation

**Importance and obstacle overcome.** Beat the Weyl/van der Corput exponent-pair ceiling of about 0.1618 predicted by Graham-Kolesnik for that method, by evaluating the Gauss sum instead of Cauchy-differencing it and using a Diophantine counting theorem on modular-inverse fractions.

**Relation to prior work.** Improves Kolesnik's exponent-pair record by departing from Weyl's method; compares with Graham-Kolesnik's predicted limit 0.1618 for exponent-pair methods.

**Limitations and open questions.** The authors say the method is wasteful where (5.16) is discarded. Theorem 4.1 is elementary only for f(x)=x^kappa with kappa=2 lambda != 0 excluded; for general exponents one needs spectral theory of automorphic forms (Kuznetsov formula and the Deshouillers-Iwaniec large sieve for Maass forms [2]). They say the method may apply to the divisor problem but claim no results. Convexity-barrier remains: the bound is far from the Lindelof hypothesis, which would follow from RH.

**Ideas in remarks/appendices/abandoned paths.** Remark on p.465 that the Diophantine problem for general (x^kappa, x^lambda) would follow from Kuznetsov plus Maass-form large sieve; the 'wasteful' discarded condition (5.16), p.470.

## Research potential

- **Hypotheses that might be weakened.** Theorem 4.1 needs the exact 'function of ac' structure; extending it to the cases kappa not equal 2 lambda needs the spectral machinery noted on p.465. The discarded condition (5.16) is the identified loss.
- **Generalizations.** Extension to general phases via Kuznetsov (indicated); possible application to the divisor problem (stated as plausible by the authors).
- **Candidate connections.** Sharper subconvexity feeds zero-density and short-interval-prime results but does not bear directly on RH; potential link with later Huxley-type exponent improvements (not verified from this source).
- **Reusable lemmas.** Theorem 4.1 (fractions with close modular inverses) and Lemma 3.1 (incomplete Gauss sum evaluation) are self-contained.
- **Possible experiments.** Numerically count N(Delta1, Delta2; A, C) for moderate A, C to test how sharp Theorem 4.1 is. Exploring whether keeping (5.16) improves exponent 9/56 would be a direct test of the 'wasteful' remark.
- **Risks / barriers.** Gains are of order 1e-3 in exponent; the method is unlikely to reach Lindelof.

## Audit notes (Level 1 reader)

OCR text drops almost all formulas; formulas for Lemmas 2.1-2.4, 3.1 and Theorem 4.2 were not read from images, so those statements are summarized, not exact. A small inconsistency: abstract of Intro says $\theta=9/56$ while the paper says Kolesnik's prior value was in the lost formula; I did not read it (the exponent 139/858 is a recollection). Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01032`; harvest queries: kw_moments_zeta, msc_11M06.
- Triage decision: include — Landmark subconvexity bound for zeta on critical line.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

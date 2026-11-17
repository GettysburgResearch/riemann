# PAPER-0107 — Geometrisches zur Riemannschen Zetafunktion

| Field | Value |
|---|---|
| Authors | Speiser, Andreas |
| Year / stratum | 1934 / S2 |
| Venue | Math. Ann. 110, 514-521 (1934). |
| Identifiers | zbMATH [0010.16401](https://zbmath.org/?q=an:0010.16401) · DOI [10.1007/BF01448042](https://doi.org/10.1007/BF01448042) |
| MSC | 11M26, 11M06 |
| Families | C, F |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0110/LOG_0032.pdf |
| Selection | score 4.2619, in-pool citations 21, seed lists 2, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Describe the Riemann surface of the inverse function of w=zeta(z) (and w=1/Gamma(z)) via curves along which zeta is real ('reelle Zuege'), and show that RH is equivalent to a geometric statement on these, in particular to non-vanishing of zeta' in Re s<1/2.

**Historical motivation.** Applies Speiser's method of 'reelle Zuege' (Schwarz reflection / automorphic functions) to the Gamma function and zeta; companion Zurich dissertation by A. Utzinger (1934).

### Main results

- **THM-PAPER-0107-1** (unnumbered statement p.518, proposition (equivalence, sketch), scope: global; Speiser p.518 (boxed statement) with argument pp.517-519). RH is equivalent to the assertion that all 'Lamellen' (real-valued curves of zeta in the left half-plane region Re s<1/2 that arise in the critical strip and return to the left) reach the critical line; equivalently, RH holds iff all real-valued curves crossing the critical line do so at zeros of $\eta(z)=\Gamma(z/2)\pi^{-z/2}\zeta(z)$ (real on Re z=1/2).
- **THM-PAPER-0107-2** (Satz p.520, theorem (equivalence), scope: global; Speiser p.519-520). RH is equivalent to: all non-trivial zeros of $\zeta'(s)$ lie to the right of the critical line or on it (the latter only at possible multiple zeros of $\zeta$ itself), i.e. $\zeta'(s)\neq0$ for $\Re s<1/2$ (apart from trivial/negative-axis zeros).
- **THM-PAPER-0107-3** (p.519, proposition, scope: local; Speiser p.519). A line of constant amplitude ($\arg\zeta$ constant) touches the critical line at a point $s_0$ iff $\eta$'s derivative along the line vanishes there iff $\zeta(s_0)=0$ (stationary value of the amplitude along Re s=1/2 can occur only at a zero).
- **THM-PAPER-0107-4** (pp.515-517, descriptive result, scope: asymptotic; Speiser pp.515-517). Counting: to the right of Re s=2 to 3 real-valued curves of zeta proceed nearly horizontally at distance about 4.53; left of the critical strip the number of real curves between heights y and y+1 is proportional to $\log y$ in the strip $y\to\infty$ (and number crossing a horizontal segment of height y is of order $y\log y$), versus proportional to y on the right. Hence real curves from the left cannot all enter the strip except via Lamellen and the number of non-trivial zeros up to height y is of order $y\log y$.
- **THM-PAPER-0107-5** (p.518, descriptive result, scope: global; Speiser pp.517-518). The Riemann surface of the inverse of $w=\zeta(z)$ consists of a logarithmic part (infinitely many sheets with branch points over $w=1$ and $\infty$) with sheets attached to an arccosine-type surface; the number of sheets at the n-th level grows like the logarithm of n, suggesting a link to prime distribution.

### Key definitions

- 'reelle Zuege' = curves on which zeta is real
- 'Lamelle' = real-valued curve of zeta within the critical strip that turns back left without reaching the critical line
- amplitude = arg zeta; lines of constant amplitude

### Principal lemmas

- **THM-PAPER-0107-L1** (p.517 horizontal line argument; p.517). A horizontal line cannot cross more than order $\log y$ real-valued curves in the critical strip at height y (else a bounded region with real boundary curves would force $\zeta=\infty$ inside), so most real curves entering from the right must end on the left; the remaining ones are the Lamellen. — *Role:* Establishes the geometric dichotomy used for equivalence.
- **THM-PAPER-0107-L2** (p.518 reality of eta; p.518). $\eta(z)=\Gamma(z/2)\pi^{-z/2}\zeta(z)$ is real on Re z=1/2 and its argument turns monotonically with rate $\tfrac12\log y$ through Stirling; hence real-valued curves of zeta crossing the critical line do so exactly at zeros of zeta or where the gamma factor is real. — *Role:* Quantifies crossings; basis of equivalence.
- **THM-PAPER-0107-L3** (p.519; p.519-520). If $|\zeta|$ strictly decreases along every line of constant amplitude when crossing the critical line from left to right (as when no zeta' branch points lie left), then every zero of $\zeta$ lies on or right-symmetrically of the line; derived from Cauchy-Riemann: derivative of log|zeta| in x is negative. — *Role:* Direction RH => zeta' no zeros left.

### Proof architecture

Qualitative: (1) describe the cosine-type and exponential-type fields of Gamma and zeta; (2) count real-valued curves left vs right of the critical strip using the functional equation and Stirling; (3) deduce topological necessity of 'Lamellen' and equivalence with real curves reaching the critical line; (4) prove RH <=> zeta' has no zeros left of the critical line by following lines of constant amplitude and using that branch points of the inverse correspond to zeros of zeta'; (5) comment on the Riemann surface of eta.

**Imported results.** Stirling's formula; Functional equation of zeta; Hadamard-type classification via Riemann surface (Speiser's earlier theory of real-valued curves); Jahnke-Emde tables (numerical)

**Techniques.** Riemann surface of inverse function; lines of constant amplitude / level curves; Cauchy-Riemann monotonicity of |zeta|; Stirling formula for argument; conformal mapping, symmetry principle

## Context and interpretation

**Importance and obstacle overcome.** First geometric equivalence of RH with a statement on zeros of the derivative zeta' (Speiser's theorem), motivating Levinson-Montgomery and work on zeros of zeta'. Obstacle: connecting the global topology of the real-valued curves of zeta with location of zeros of zeta.

**Relation to prior work.** Builds on Riemann 1859, Jahnke-Emde function tables for level curves, Lense (1928) on conformal mapping by Gamma. Later: Levinson-Montgomery (Acta Math. 133 (1974)), Spira, Conrey-Ghosh on zeta' zeros, Soundararajan/ Zhang on zeros of zeta'.

**Limitations and open questions.** Arguments are largely descriptive/qualitative, not written as fully rigorous lemmas; later made rigorous and quantitative (Levinson-Montgomery 1974: RH <=> zeta' has no zeros in Re s<1/2, with Speiser's equivalence proved rigorously and zero counts; Spira). Mentions Utzinger's dissertation (Zurich 1934) for part of the proofs.

**Ideas in remarks/appendices/abandoned paths.** p.521: if RH (and simple zeros) hold, the Riemann surface of eta is just the arccosine surface with branch points accumulating at the origin, i.e. a fully explicit uniformization; Lamellen would force extra sheets. p.517-518: number of sheets of logarithmic part grows like the log of sheet index, tying sheets to prime distribution; p.520 ends with the surface of eta.

## Research potential

- **Hypotheses that might be weakened.** The qualitative topology could be made precise to give an unconditional lower/upper bound on the number of Lamellen; 'no Lamellen' vs 'no zeros of zeta' in Re s<1/2 could be studied for Dirichlet L-functions.
- **Generalizations.** Applies to any L-function with Euler-type functional equation: 'GRH iff L' has no zeros left of the critical line' (Levinson-Montgomery known for zeta; Dirichlet L and Hecke proven partially).
- **Candidate connections.** Levinson-Montgomery quantitative zeta' counting (N_1(T)), Conrey-Ghosh-Gonek zero-spacing; Hadamard factorization of eta; Polya-type real zero conjectures for Xi'.
- **Reusable lemmas.** Level-curve (constant amplitude) tracking argument turning monotonicity of |zeta| across the critical line into a zero statement.
- **Possible experiments.** Plot real-valued curves (Im zeta = 0) of zeta up to height ~200 and count crossings of Re s=1/2 vs zeros; verify the claimed density y*log y vs y; test counts of Lamellen (should be zero if RH) and compare with zeta' zero positions numerically (certify with interval arithmetic).
- **Risks / barriers.** A numerical absence of Lamellen is a finite local result and does not imply RH; qualitative topological arguments need complete justification (avoid circularity through the global behavior of arg zeta).

## Audit notes (Level 1 reader)

Argument pp.517-520 is qualitative; the step 'a line of constant amplitude must leave the bounded region, contradicting that zeta cannot exceed/shrink in modulus' is stated informally without the case analysis for multiple zeros. The word 'nichttrivial' for zeros of zeta' is not defined (zeros of zeta' on the negative real axis between trivial zeros exist). Statement attributed to Speiser is correctly summarized in the triage (with the caveat 'apart from the real axis zeros left of the strip'). Page 521 final remarks about the 1-sheet vs multi-sheet Riemann surface of eta are conjectural.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00069`; harvest queries: msc_11M06, msc_11M26.
- Triage decision: include — Speiser's equivalence of RH with nonvanishing of zeta' left of critical line.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

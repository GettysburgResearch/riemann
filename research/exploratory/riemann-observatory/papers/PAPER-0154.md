# PAPER-0154 — Quadratische Körper im Gebiete der höheren Kongruenzen. I: Arithmetischer Teil. II: Analytischer Teil.

| Field | Value |
|---|---|
| Authors | Artin, Emil |
| Year / stratum | 1924 / S2 |
| Venue | Math. Z. 19, 153-206 (1924); ibid. 19, 207-246 (1924). |
| Identifiers | zbMATH [50.0107.01](https://zbmath.org/?q=an:50.0107.01) · DOI [10.1007/BF01181074](https://doi.org/10.1007/BF01181074) |
| MSC | 11R11, 11R27, 11R29, 11R42, 11R58 |
| Families | E |
| Work type | original_paper |
| Evidence level of this record | **L1-partial** |
| Full text | partial_fulltext — https://archive.org/details/mathematische-zeitschrift_1924_19_3-4 |
| Selection | score 1.8524, in-pool citations 14, seed lists 1, triage relevance 5 |

## Mathematical content (Level 1: full text read)

**Research question.** Develop the arithmetic of quadratic extensions $K(\sqrt D)$ of $K=\mathbb F_p(t)$ (ideals, class number, units, genera, continued fractions, reciprocity) and introduce the zeta function $Z_D(s)=\sum_{\mathfrak a}|N\mathfrak a|^{-s}$ with Euler product, functional equation, class number formula and the Riemann hypothesis analogue for its zeros; verify RH in small cases and derive consequences (class number bounds, finiteness theorems, primes in arithmetic progressions).

**Historical motivation.** Extends Dedekind's arithmetic of F_p[t] to quadratic extensions, mirroring quadratic number fields, with the goal of a class number formula via zeta functions where RH becomes decidable field by field.

### Main results

- **THM-PAPER-0154-1** (Section 17 (Eqs 1, 8), theorem/definition, scope: global; Part II, Sections 17, 21 (exact constants not reliably legible in OCR)). For squarefree $D\in\mathbb F_p[t]$, $Z_D(s)=\sum_{\mathfrak a}|N\mathfrak a|^{-s}$ converges absolutely for $\Re s>1$ with Euler product over prime ideals (split primes contribute $(1-|P|^{-s})^{-2}$, inert $(1-|P|^{-2s})^{-1}$, ramified $(1-|P|^{-s})^{-1}$) and satisfies a functional equation $s\leftrightarrow1-s$ (Eq. 8 and Section 21 Eqs 4-6 for real fields) relating $Z_D(1-s)$ to $Z_D(s)$ via an explicit factor in $p$ and $|D|$.
- **THM-PAPER-0154-2** (Section 20 (two Satz), theorem, scope: global; Part II, Section 20). $Z_D(s)$ has period $2\pi i/\log p$; its only poles are simple poles at $s=1+2\pi ik/\log p$; $Z_D$ has no zeros on $\Re s=1$ (Hadamard-de la Vallee Poussin argument via the Euler product logarithmic derivative; points $1+2\pi ik/\log p$ handled via the field $K(\sqrt{gD})$).
- **THM-PAPER-0154-3** (Section 21 (Satz on zero locations), theorem, scope: global; Part II, Section 21). No zeros in $\Re s<0$. On $\Re s=0$: for $\deg D$ odd none; for $\deg D$ even only simple zeros at trivial points (imaginary field: $s=\pi ik/\log p$ type; real field: $s=2\pi ik/\log p$ type, including $s=0$). All other nontrivial zeros lie in a strip $0<1-\theta\le\Re s\le\theta<1$ symmetric about $\Re s=1/2$ and the real axis, $\theta=\sup\Re$ of the zeros.
- **THM-PAPER-0154-4** (Sections 18, 24 (class number formulas), theorem, scope: global; Part II, Sections 18, 21, 24). For imaginary fields with $n=\deg D\ge3$, $Z_D$ is a polynomial in $p^{-s}$ (times a fixed factor) with coefficients $\sigma_\nu$; with $\beta_\nu$ the nontrivial roots of $z^{n-1}+\sigma_1z^{n-2}+\dots+\sigma_{n-1}$ (zeros $\rho$ correspond to $\beta=p^{\rho}$-type substitution): $h=\prod(\beta_\nu-1)$ for $n$ odd, $h=2\prod(\beta_\nu-1)$ for $n$ even imaginary (Eqs 3-5 of Sec. 24); for real fields an analogous formula involving the regulator $R$.
- **THM-PAPER-0154-5** (Section 22, theorem (explicit formula), scope: global; Part II, Section 22 (exact form OCR-uncertain)). Exact formula for the number of prime ideals of absolute norm $p^\nu$ in terms of the roots $\beta_\mu$ (analogue of the Riemann-Mangoldt formula), schematically $p^\nu-\sum_\mu\beta_\mu^\nu-1$ (weighted); number of ideals of norm $p^\nu$ for $\nu\ge n-1$ given by $H(p^\nu)=p^\nu\kappa$-type expression ($\kappa$ from Section 20 Eq 1).
- **THM-PAPER-0154-6** (Introduction and Section 23, verification, scope: finite; Section 1 and Section 23). RH ($\Re\rho=1/2$, i.e. $|\beta_\nu|=\sqrt p$) is verified case by case: about forty fields computed (introduction); Section 23 derives it for small $n$ (cubic discriminants via the table of class numbers, and 'ebenso' $n=5$ except for cases left to computation). The general proof is stated to be open, with difficulties 'of similar type as for Riemann's zeta' but clearer since the objects are essentially polynomials.
- **THM-PAPER-0154-7** (Section 24, Satz, conditional theorem, scope: conditional; Part II, Section 24). Assuming RH for all quadratic function fields: for imaginary fields with $n\ge3$, $(\sqrt p-1)^{n-1}\le h\le(\sqrt p+1)^{n-1}$ ($n$ odd) and $2(\sqrt p-1)^{n-2}\le h\le2(\sqrt p+1)^{n-2}$ ($n$ even) (Eqs 10-11, exponents as legible in OCR). Consequences: (1) for all $p,n$ only finitely many fields of prescribed class number; class number 1 only for $p=3$ (probably one field); (2) only finitely many fields with one-class genera, and only for $p=3,5,7$.
- **THM-PAPER-0154-8** (Section 26 Satz and Introduction, theorem, scope: global; Part II, Section 26). For a character $\chi$ modulo $\mathfrak K$, $L(s,\chi)$ has no zero on $\Re s=1$; combined with Kornblum's regularity of $L$ for non-principal $\chi$ this sharpens Kornblum's theorem on infinitely many prime functions in arithmetic progressions (precise quantitative form not read).

### Key definitions

- $Z_D(s)=\sum_{\mathfrak a}|N\mathfrak a|^{-s}$
- imaginary/real quadratic function field according to behavior at infinity
- $\sigma_\nu$ coefficients and roots $\beta_\nu$
- $\theta=\sup\Re$ of nontrivial zeros

### Principal lemmas

- **THM-PAPER-0154-L1** (Section 10; Part I, Section 10 (heading only)). Finiteness of the class number for imaginary quadratic function fields. — *Role:* Basic finiteness input.
- **THM-PAPER-0154-L2** (Section 11; Part I, Section 11 (heading; used in Sec 24)). Count of ambiguous classes; genus relation $h/f=2^{s-1}$ with $s$ the number of prime factors of $D$. — *Role:* Bounds classes per genus in Section 24.
- **THM-PAPER-0154-L3** (Sections 12-14; Part I, Sections 12-14 (headings)). Continued fractions of quadratic irrationals in $K((1/t))$; finiteness of class number for real fields; unit group, fundamental unit and regulator. — *Role:* Real-field arithmetic for the class number formula.
- **THM-PAPER-0154-L4** (Sections 15-16; Part I, Sections 15-16 (headings)). Quadratic reciprocity law in $\mathbb F_p[t]$ and generalization. — *Role:* Decomposition of primes in $K(\sqrt D)$.
- **THM-PAPER-0154-L5** (Section 17; Part II, Section 17). Euler product with local factors for split/inert/ramified primes; $Z(s)$ expressed through the zeta function of $\mathbb F_p[t]$ and an L-factor. — *Role:* Elementary properties of $Z$.
- **THM-PAPER-0154-L6** (Section 21 (Eqs 8-9); Part II, Section 21). The functional equation implies symmetry of $\Xi(s)$ ($\Xi(1-s)=\Xi(s)$) and relations among the $\sigma_\nu$, halving the number of independent coefficients. — *Role:* Makes class number computation and the RH check finite and simpler.

### Proof architecture

Part I builds the arithmetic of K(sqrt D): ideals, primes, classes, equivalence of functions, finiteness of class number, ambiguous classes, continued fractions, units, reciprocity. Part II: zeta function via ideals; Euler product (Sec 17); imaginary-field class numbers via reduced ideals giving Z as an explicit finite expression in p^{-s} (Sec 18), real fields via continued fractions (Sec 19, not read); pole analysis and nonvanishing on Re s=1 (Sec 20); functional equation and coefficient relations (Sec 21); counting ideals and prime ideals of given norm (Sec 22); class number tables and RH check for small n (Sec 23); RH consequences (Sec 24); real characters and L-functions, primes in arithmetic progressions (Sec 25-26). RH is only verified by explicit root computation.

Dependency edges: CAND-00310 → CAND-02085 (function-field Weil RH is the known analogue for the Weil-positivity / zeta-cycle framework)

**Imported results.** Dedekind's theory of congruences modulo p (J. reine angew. Math. 54, 1857); Kornblum (Math. Z. 5, 1919): regularity of L-series for non-principal characters in F_p[t]; Landau Handbuch method for non-vanishing of complex-character L on Re s=1

**Techniques.** Dedekind ideal theory in F_p[t]-extensions; reduced ideals and continued fractions in K((1/t)); zeta function as polynomial in p^{-s}; Euler product and Hadamard-de la Vallee Poussin nonvanishing; functional equation by ideal counting; quadratic reciprocity in F_p[t]; explicit tabulation of class numbers and root computation

## Context and interpretation

**Importance and obstacle overcome.** First systematic zeta functions of hyperelliptic function fields over finite fields with functional equation and RH stated as a finite condition on roots of an explicit polynomial; origin of the Artin-Hasse-Weil line. The obstacle overcome is expressing Z_D as an explicit finite object (polynomial of degree n-1 in p^{-s}) so RH is checkable per field.

**Relation to prior work.** Dedekind (1857) ideal theory in F_p[t]; Kornblum (1919) L-series and primes in arithmetic progressions in F_p[t]; Artin's thesis. Followed by F.K. Schmidt (1931), Hasse (1933), Weil (1940s).

**Limitations and open questions.** General RH for these zeta functions is stated as open; only small degrees (about forty fields) verified. Conditional results of Section 24 depend on RH for all fields (later unconditional by Weil). Part I only skimmed; Sections 19 and 25 not read. Later proofs: Hasse (elliptic case) and Weil (all genera), outside the paper.

**Ideas in remarks/appendices/abandoned paths.** Section 22: exact Riemann-Mangoldt-type formula for prime-ideal counts. Section 24: prediction that class number 1 occurs only for p=3 (a Gauss-type classification, unconditional after Weil). Section 21: symmetry reduces independent coefficients, making the check finite.

## Research potential

- **Hypotheses that might be weakened.** Section 24 results are conditional on RH for all fields; as RH is now Weil's theorem they are unconditional, but one can ask for effective versions or the analogous statements in number fields conditional on GRH.
- **Generalizations.** Higher-degree extensions and general function fields (F.K. Schmidt); the L-function with characters of Section 26 as a model for GRH-type statements.
- **Candidate connections.** Function-field test-bed for Weil-positivity/zeta-cycle constructions (CAND-02085) and for spectral (Hilbert-Polya) operators: Frobenius on cohomology realizes the zeros, a model for CAND-02040/02425 style operator programs.
- **Reusable lemmas.** Reduced-ideal counting giving Z_D as an explicit polynomial; coefficient symmetry from the functional equation; Hadamard-de la Vallee Poussin argument with periodicity handling.
- **Possible experiments.** Recompute Artin's class number tables and verify |beta|=sqrt p for all squarefree D of small degree over F_3, F_5, F_7 with exact arithmetic; test the class number bounds of Section 24 and the class-number-1 classification.
- **Risks / barriers.** The paper offers no mechanism proving RH; the later proofs (Hasse, Weil) rely on algebraic geometry (Frobenius, Riemann-Roch, Castelnuovo-Severi) not available for number fields.

## Audit notes (Level 1 reader)

Reading is from noisy OCR of the Internet Archive scan; exponents in Section 24 Eqs 10-11, constants of the functional equation (Sec 17 Eq 8), the example fields and the numerical constants (103, 1.15, 105) in the genus bound could not be certified from the text. The claim that RH is verified for n=3 and n=5 rests on one sentence in Section 23 ('Endlich wurde im Falle n=3 durch aehnliche Diskussion gezeigt, dass auch im Falle n=5 alle Nullstellen auf der Geraden Re(sigma)=1/2 liegen'); whether n is deg D or related should be double-checked against the PDF.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00310`; harvest queries: citation_expansion.
- Triage decision: include — Artin's thesis introducing zeta functions of hyperelliptic function fields and conjecturing their RH, origin of the Weil conjectures.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

# PAPER-0033 — On the Selberg class of Dirichlet series: Small degrees

| Field | Value |
|---|---|
| Authors | Conrey, J. B.; Ghosh, A. |
| Year / stratum | 1993 / S4 |
| Venue | Duke Math. J. 72, No. 3, 673-693 (1993). |
| Identifiers | zbMATH [0796.11037](https://zbmath.org/?q=an:0796.11037) · DOI [10.1215/S0012-7094-93-07225-0](https://doi.org/10.1215/S0012-7094-93-07225-0) · arXiv [math/9204217](https://arxiv.org/abs/math/9204217) |
| MSC | 11M41 |
| Families | E |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://arxiv.org/abs/math/9204217 |
| Selection | score 4.5843, in-pool citations 60, seed lists 1, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Within the Selberg class S (Dirichlet series with analyticity, Ramanujan bound, gamma-type functional equation, Euler product with theta<1/2), classify low-degree elements: show no elements of degree in (0,1), degree-1 elements of a normalized subclass are Dirichlet L-functions (shifted), derive consequences of Selberg's conjectures, and give a GL(2) converse theorem.

### Main results

- **THM-PAPER-0033-1** (Theorem 2.1, theorem, scope: global; Sec. 2, p.5). If $\Phi^{(1)}$ and $\Phi^{(2)}$ are both admissible gamma-factor products for $F\in S$ then $\Phi^{(1)}(s)=C\Phi^{(2)}(s)$ for a real constant C; hence the degree $d_F=2\sum w_i$ is well defined.
- **THM-PAPER-0033-2** (Theorem 3.1, theorem, scope: global; Sec. 3, pp.7-9). If $F\in S$ then $F\equiv1$ or $d_F\ge1$. (No degrees in $(0,1)$; $d_F=0$ forces $F=1$.)
- **THM-PAPER-0033-3** (Corollary 3.3/3.4, corollary, scope: global; Sec. 3, p.10). Every F in S factors into primitives (additivity $d_{FG}=d_F+d_G$ and Theorem 3.1); if $d_F<2$ then F is primitive.
- **THM-PAPER-0033-4** (Propositions 4.1-4.6, conditional theorems, scope: conditional; Sec. 4, pp.10-11). Assuming Selberg's conjectures (regularity and orthonormality): $n_F=\sum e_i^2$ for $F=\prod F_i^{e_i}$; $n_F=1\Rightarrow F$ primitive; a pole of order m at 1 implies $\zeta^m\mid F$ in S; S has unique factorization; Dedekind's conjecture ($\zeta_K/\zeta$ entire) holds; no F in S vanishes on $\Re s=1$. *Conditional on:* Selberg conjectures (1) regularity and (2) orthonormality.
- **THM-PAPER-0033-5** (Theorem 5.1, theorem, scope: global; Sec. 5, p.12). If $F\in S^*(1)$ (normalized functional equation with all $w_i=1/2$, degree 1) then q is a positive integer and there is a primitive Dirichlet character $\chi \bmod q$ and real $\tau$ with $F(s)=L(s+i\tau,\chi)$.
- **THM-PAPER-0033-6** (Theorem 6.1, theorem, scope: global; Sec. 6, p.15). For $F=\sum a_nn^{-s}$ absolutely convergent for $\sigma>1$ and the GL(2)-type completed function $\Phi$ with parameter $\mu$ real, $\Phi$ is entire and satisfies $\Phi(s)=\Phi(1-s)$ iff $f(re^{i\theta})=f(r^{-1}e^{i\theta})$ for $0<\theta<\pi/2$, where $f(x,y)=y^{1/2}\sum a_nH_\mu(2\pi nx/\sqrt q)K_\mu(2\pi ny/\sqrt q)$.

### Principal lemmas

- **THM-PAPER-0033-L1** (Lemma 2.1; p.6). For F in S, $F_p$ has no zeros in $\sigma>1/2$ and F has no zeros in $\sigma>1$. — *Role:* Euler product control; uses theta<1/2.
- **THM-PAPER-0033-L2** (Lemma 2.2; pp.6-7). If F in S has a pole or zero at $1+i\tau$ then $\sum_{p\le x}a_p p^{-1-i\tau}$ is unbounded as $x\to\infty$. — *Role:* Link of zero/pole on the 1-line to prime sums; used in Props 4.3, 4.6.

### Proof architecture

Thm 3.1: assume $d_F<1$; shift contour of the Mellin representation of $h(x)=\sum a_ne^{-2\pi nx}=\frac1{2\pi i}\int(2\pi x)^{-s}\Gamma(s)F(s)ds$ to the left past the poles, using the functional equation to show the remainder K(x) is an entire function of x (growth $\Gamma$-ratio $n^{(1-d)n}A^n$); periodicity of h then makes h entire, so $H(z)=\sum a_ne(nz)$ extends and the growth forces the $a_n$ too small to be coefficients of an element of S (proof tail not fully read). Thm 5.1 follows Siegel's proof of Hamburger's theorem, with theta<1/2 excluding twisted-Euler-factor counterexamples. Sec. 4 uses orthogonality sums over primes. Sec. 6 via Mellin transform and Bessel-function identities (Lemmas 6.2, 6.3).

**Techniques.** Mellin transform and contour shifting; Stirling asymptotics for gamma factors; Hamburger-Siegel type argument; Bessel-function converse theorem; prime sums via partial summation

## Context and interpretation

**Importance and obstacle overcome.** First published structural theorems for the Selberg class: gap in degrees below 1 and degree 1 classification (in normalized subclass). The key use of theta<1/2 (axiom 4) rules out counterexamples like $(1-2^{1/2-s})\zeta(s)$.

**Relation to prior work.** 

**Limitations and open questions.** Degree-2 structure of S is only partly treated (Thm 6.1 is a converse theorem, not classification). Non-integral degrees >=1 not excluded here. Selberg's conjectures and GRH unproven; the paper explicitly does not use GRH. Rationality of Q left open.

## Research potential

- **Hypotheses that might be weakened.** Theorem 5.1 requires normalization w_i=1/2 (S^*); removing it needs Kaczorowski-Perelli style arguments. Ramanujan axiom and theta<1/2 are used in Lemma 2.1/Thm 5.1; testing which can be relaxed gives families violating RH.
- **Generalizations.** Prove Prop 4.6-type nonvanishing on sigma=1 under weaker prime-orthogonality; extend Theorem 3.1 to the open range 1<d<2.
- **Candidate connections.** Counterexample mechanism for RH in generalized Dirichlet series (theta=1/2, Maass exceptional eigenvalues, remark (3) p.2) shows which axioms any RH-for-S argument must use.
- **Reusable lemmas.** Lemma 2.2 (zero on 1-line implies unbounded prime sum) and Theorem 3.1 contour-shift argument.
- **Possible experiments.** Numerically test theta close to 1/2 examples for off-line zeros; check Thm 3.1 degree-gap proof in synthetic gamma-factor settings.
- **Risks / barriers.** Results are structural and do not address zeros on 1/2; RH for S is an explicit non-used conjecture.

## Audit notes (Level 1 reader)

OCR garbling of symbols only. Proof of Theorem 3.1 final step (a_n too small) summarized tersely in the text; not independently verified. Proof of Thm 5.1 only partially read. Abstract-style claim in triage (RH for Euler product with functional equation) is only a stated expectation, not proved.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00732`; harvest queries: kw_RH_any, kw_selberg_class, citation_expansion, arxiv_rh_abs.
- Triage decision: include — Conrey-Ghosh Selberg class conjectures and small degree results.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

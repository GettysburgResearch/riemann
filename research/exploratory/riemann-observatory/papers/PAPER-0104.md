# PAPER-0104 — Autocorrelation of random matrix polynomials

| Field | Value |
|---|---|
| Authors | Conrey, J. B.; Farmer, D. W.; Keating, Jonathan P.; Rubinstein, M. O.; Snaith, Nina C. |
| Year / stratum | 2003 / S5 |
| Venue | Commun. Math. Phys. 237, No. 3, 365-395 (2003). |
| Identifiers | zbMATH [1090.11055](https://zbmath.org/?q=an:1090.11055) · DOI [10.1007/s00220-003-0852-2](https://doi.org/10.1007/s00220-003-0852-2) · arXiv [math-ph/0208007](https://arxiv.org/abs/math-ph/0208007) |
| MSC | 11M50, 15B52, 11M06 |
| Families | B |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — arXiv:math-ph/0208007 |
| Selection | score 4.3111, in-pool citations 45, seed lists 0, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Compute exactly (for every matrix size $N$) the autocorrelation functions (shifted moments) $\int\prod\Lambda_M$ of characteristic polynomials over Haar measure on $U(N)$, $O(2N)$, $USp(2N)$. Express each result as a determinant sum, a combinatorial sum over shuffles, and a multiple contour integral, the three forms matching the structure of the conjectured L-function shifted-moment formulas of CFKRS (CAND-01200).

### Main results

- **THM-PAPER-0104-1** ((2.4)-(2.11) and (2.16), theorem (exact identity), scope: finite; Section 2, eqs. (2.5)-(2.16)). For $\Lambda_M(s)=\det(I-Ms)$ on $U(N)$ and $I_{m,n}(U(N);w)=\prod_{k=m+1}^{n}w_k^N\int_{U(N)}\prod_{i=m+1}^n\Lambda_M(w_i^{-1})\prod_{j=1}^m\Lambda_{M^\dagger}(w_j)\,dM$, one has $I_{m,n}(U(N);w)=S_{\lambda}(w_1,\dots,w_n)$ (Schur function, $\lambda=(N^{n-m})$; a character of $U(n)$ on the unit circle) $=\sum_{\sigma\in\Xi_m}\prod_{q>m}w_{\sigma(q)}^N\big/\prod_{\ell\le m<q}(1-w_{\sigma(\ell)}w_{\sigma(q)}^{-1})$ (up to the garbled index placement in the extract), where $\Xi_m$ is the set of $\sigma\in S_n$ increasing on $\{1..m\}$ and on $\{m+1..n\}$. The relation to the original correlation integral is (2.5).
- **THM-PAPER-0104-2** ((2.17), theorem (contour-integral form), scope: finite; Section 2, eq. (2.17)). $I_{m,n}(U(N);e^{-\alpha_1},\dots;e^{-\alpha_n})=\frac{(-1)^{n(n-1)/2}}{(2\pi i)^n m!(n-m)!}\oint\!\!\cdots\!\oint e^{-N(z_{m+1}+\dots+z_n)}\prod_{\ell\le m<q}(1-e^{z_q-z_\ell})^{-1}\frac{\Delta(z_1,\dots,z_n)^2}{\prod_{i,j}(z_i-\alpha_j)}dz_1\cdots dz_n$ over contours enclosing the $\alpha_j$ (obtained from the combinatorial sum by Lemma 2.1).
- **THM-PAPER-0104-3** ((3.6),(3.36), theorem (exact identity), scope: finite; Section 3, eqs. (3.6), (3.22), (3.36)). For $USp(2N)$, $I(USp(2N);w_1,\dots,w_k)=\int\prod_{j=1}^k\Lambda_M(w_j)dM$ equals a determinant sum, a sum over $\epsilon_j\in\{\pm1\}$ of $\prod_j w_j^{-N\epsilon_j}$-type terms times $\prod_{i\le j}(1-w_i^{\epsilon_i}w_j^{\epsilon_j})^{-1}$, and the contour integral (3.36): $\frac{(-1)^{k(k-1)/2}2^k}{(2\pi i)^kk!}e^{-N\sum\alpha_j}\oint\cdots\oint\prod_{\ell\le m\le k}(1-e^{-z_m-z_\ell})^{-1}\frac{\Delta(z_1^2,\dots,z_k^2)^2\prod z_j}{\prod_{i,j}(z_j-\alpha_i)(z_j+\alpha_i)}e^{N\sum z_j}dz$ (extract garbles the exponent signs; confirm in the PDF). Haar density is (3.2).
- **THM-PAPER-0104-4** ((4.19),(4.42)-(4.43),(4.53),(4.57), theorem (exact identity), scope: finite; Section 4, eqs. (4.19), (4.42), (4.43), (4.53), (4.57)). For $SO(2N)$: $I(SO(2N);w_1,\dots,w_k)=w_1^N\cdots w_k^N\sum_{\epsilon_j=\pm1}\prod_jw_j^{N\epsilon_j}\ldots\prod_{i<j}(1-w_i^{-\epsilon_i}w_j^{-\epsilon_j})^{-1}$ as printed in (4.42); contour form (4.43) with kernel $\prod_{\ell<m}(1-e^{-z_m-z_\ell})^{-1}$. For the $Z$-functions $Z_M(s)=\pm s^{-N}\Lambda_M(s)$: $\int_{SO(2N)}\prod Z_M(e^{-\alpha_j})=\sum_{\epsilon}\prod_je^{\epsilon_jN\alpha_j}\prod_{i<j}(1-e^{-\epsilon_i\alpha_i-\epsilon_j\alpha_j})^{-1}$ and $\int_{O^-(2N)}\prod Z_M(e^{-\alpha_j})=\sum_\epsilon\prod_j\epsilon_je^{\epsilon_jN\alpha_j}\prod_{i<j}(1-e^{-\epsilon_i\alpha_i-\epsilon_j\alpha_j})^{-1}$.
- **THM-PAPER-0104-5** (Conjecture 2.2, conjecture (imported from companion paper [8], stated here for comparison), scope: conditional; Section 2.1, eqs. (2.18)-(2.21)). For the shifted moments of zeta, $\int_0^T\zeta(\tfrac12+\alpha_1+it)\cdots\zeta(\tfrac12+\alpha_k+it)\zeta(\tfrac12-\alpha_{k+1}-it)\cdots\zeta(\tfrac12-\alpha_{2k}-it)\,dt=\int_0^TW_k(t;\alpha)(1+O(t^{-1/2+\epsilon}))dt$ with $W_k$ a sum over the $\binom{2k}{k}$ shuffles $\sigma\in\Xi$ of $A_k(\alpha_{\sigma})\prod_{\ell\le k<m}\zeta(1+\alpha_{\sigma(\ell)}-\alpha_{\sigma(m)})$ times exponential factors in $\frac t2\log\frac{t}{2\pi}$-type (the extract is garbled). It matches (2.21) under $N=\log\frac t{2\pi}$. *Conditional on:* conjecture, not proved (k>=3).
- **THM-PAPER-0104-6** (Conjecture 3.6 (and 4.2-4.4), conjecture (imported), scope: conditional; Section 3.1, eqs. (3.39)-(3.43); Section 4.3, Conjectures 4.2-4.4). For real Dirichlet $L(s,\chi_d)$ with fundamental $d<0$ and weight $g$, $\sum^*_{L\in F}Z_L(\tfrac12+\alpha_1)\cdots Z_L(\tfrac12+\alpha_k)g(|d|)=\sum^*Q_k(\alpha,\log\tfrac{|d|}{2\pi})g(|d|)(1+O(|d|^{-1/2+\epsilon}))$ with $Q_k$ given by the contour integral (3.40) with $G_-$ of (3.41); analogous $G_+$ for $d>0$. For weight-2 newforms of prime level $q$, Conjectures 4.2-4.4 (all, even, odd) give harmonic-average formulas with $A(\epsilon\alpha)$ of (4.49) and error $O(q^{-1/2+\epsilon})$. *Conditional on:* conjectures, not proved.

### Principal lemmas

- **THM-PAPER-0104-L1** (Lemma 2.1 (= Lemma 2.5.2.3 of CFKRS); Section 2, p.5-6). If $G(a;b)=F(a;b)\prod_{i\le m,j\le n-m}f(a_i-b_j)$ with $F$ regular near 0 and $f(x)=1/x+c_0+c_1x+\cdots$, then $\sum_{\sigma\in\Xi_m}G(u_{\sigma(1)},\dots;u_{\sigma(m+1)},\dots)$ equals the contour integral $\frac{(-1)^{n(n-1)/2}}{(2\pi i)^nm!(n-m)!}\oint\cdots\oint G(z)\frac{\Delta(z)^2}{\prod_{i,j}(z_i-u_j)}dz$. — *Role:* converts shuffle sums into multiple contour integrals; used for all three groups
- **THM-PAPER-0104-L2** (Lemma 3.5; Section 3, p.14). If $F$ is symmetric in $k$ variables, regular near 0, and $f$ has a simple pole of residue 1 at 0 and is otherwise analytic nearby, and $G=F\prod_{i\le j}f(a_i+a_j)$ or $F\prod_{i<j}f(a_i+a_j)$, then $\sum_{\epsilon_j=\pm1}G(\epsilon_1\alpha_1,\dots,\epsilon_k\alpha_k)=\frac{(-1)^{k(k-1)/2}2^k}{(2\pi i)^kk!}\oint G(z)\frac{\Delta(z^2)^2\prod z_j}{\prod_{i,j}(z_i-\alpha_j)(z_i+\alpha_j)}dz$, and the sign-weighted analogue (3.35) with $\prod\epsilon_j$ on the left and $\prod\alpha_j$ in place of $\prod z_j$ on the right. — *Role:* contour form for symplectic and orthogonal cases
- **THM-PAPER-0104-L3** (Lemma 3.2; Section 3, p.9, eq. (3.8)). For $f(w)=c_0+c_1w+\cdots+c_nw^n$: $\sum_{j=1}^n\Delta(w_1,\dots,w_n)|_{w_j=0}\,f(w_j)$ is as printed $=(c_0+(-1)^{n-1}c_nw_1\cdots w_n)\Delta(w_1,\dots,w_n)$ (the extract's notation for 'with $w_j$ replaced by 0' is partly garbled). — *Role:* proves Identity 3.1, the key step in the symplectic determinant-sum computation
- **THM-PAPER-0104-L4** (Identity 3.1; Section 3, p.9). $\sum_{j=1}^n\Delta(w_1,\dots,w_n)|_{w_j=0}\prod_{m=1}^n(1-w_jw_m)=(1-w_1^2\cdots w_n^2)\Delta(w_1,\dots,w_n)$ (as read from the extract; some index conventions are unreadable). — *Role:* special case $f=\prod(1-w_mw)$ of Lemma 3.2; reduces the symplectic average to the combinatorial sum
- **THM-PAPER-0104-L5** (Section 2 derivation, (2.6)-(2.9); Section 2, pp.3-4). By Weyl integration, $I_{m,n}$ is converted by inserting a Vandermonde in $(w_1,\dots,w_n,e^{i\theta_1},\dots,e^{i\theta_N})$ into an $(n+N)\times(n+N)$ determinant. Orthogonality of $e^{ik\theta}$ kills all rows except a diagonal strip, leaving the $n\times n$ determinant $D_{N,m,n}(w)$ with powers $0..m-1$ and $N+m..N+n-1$ divided by $\Delta(w)$. This is the Basor-Forrester formula. — *Role:* key step of the unitary proof

### Proof architecture

For each group: (i) write the Haar integral in eigenangles via Weyl's density; (ii) multiply and divide by a Vandermonde in the $w$ variables to merge it with the density's Vandermonde into one large determinant; (iii) integrate row by row using orthogonality of exponentials, leaving a small determinant; (iv) expand the determinant over shuffles to get the combinatorial sum; (v) apply the residue lemmas (2.1, 3.5) to recast the shuffle sum as a multiple contour integral with kernels $(1-e^{-z_i-z_j})^{-1}$. For $USp$ and $SO/O^-$ the determinant step needs additional identities (Identity 3.1/Lemma 3.2 and parity-sum identities near (3.22) and (4.41)). The paper then compares the three exact forms with the L-function conjectures (Conjecture 2.2 for zeta, 3.6 for quadratic Dirichlet L-functions, 4.2-4.4 for weight-2 newforms), identifying $N$ with $\log$(conductor/2 or density).

Dependency edges: CAND-01369 → CAND-01200 (supplies the RMT side; Lemmas 2.1 and 3.5 are shared with it; it proves the theorems paired with the L-function conjectures)

**Imported results.** Basor-Forrester 1994 determinant formula (rederived here); Nonnenmacher-Zirnbauer (personal communication) character interpretation; Brezin-Hikami 2000 contour-integral method (analogy); Weyl integration formula (Weyl, Classical Groups)

**Techniques.** Weyl integration formula; Vandermonde determinant manipulations (Basor-Forrester); orthogonality of characters row-by-row; shuffle permutations $\Xi_m$; multi-variable residue calculus (Brezin-Hikami style); Schur function interpretation (Nonnenmacher-Zirnbauer dual pair)

## Context and interpretation

**Importance and obstacle overcome.** It supplies rigorous finite-$N$ formulas, valid for every $N$ and not only asymptotically, which the CFKRS recipe conjectures match term by term. This fixes the shape (shuffle sum / contour integral with $\Delta^2$ and simple poles) that the conjectural main terms for all families must have, and gives a check on the recipe in the model case.

**Relation to prior work.** 

**Limitations and open questions.** The RMT results are exact theorems, but they are only an analogy for L-functions. The paper itself contains no theorem about zeta or any L-function, only Conjectures 2.2, 3.6 and 4.2-4.4 from the companion paper, whose arithmetic factors $A_k$ have no RMT counterpart. The unitary section proves only the contour form for $U(N)$, not the dual form for $O(2N)$ in $\ge$ general $k$ beyond the cases shown. The paper notes that for the orthogonal and symplectic comparisons the Euler products appear in place of $(1-e^{-z})^{-1}$ (that is, $\zeta(1+z)$).

## Research potential

- **Hypotheses that might be weakened.** The formulae need $w_j$ generic (to avoid poles) but extend by continuity. The ensemble could be changed to other circular ensembles (CβE) or to ratios of characteristic polynomials; ratios were later done by the same group.
- **Generalizations.** Ratios and mixed products ($\Lambda_M/\Lambda_M$) over $U(N)$, $USp$, $O$; non-Haar measures; truncated unitary ensembles; the extension of (2.17) to a $q$-analogue or to general $\beta$.
- **Candidate connections.** Use the exact $U(N)$ formula to test CFKRS (CAND-01200) numerically at finite height: compare $\int\prod\zeta$ shifted moments with the formula under $N=\log\frac{t}{2\pi}$ minus lower-order corrections. This is relevant to the Montgomery-Soundararajan remark (CAND-01265) that lower-order terms matter at accessible ranges.
- **Reusable lemmas.** Lemma 2.1 and Lemma 3.5 are used verbatim in CAND-01200 (Lemmas 2.5.2.1-2.5.2.3). The determinant steps (2.6)-(2.9) give a clean template for any Toeplitz-type identity.
- **Possible experiments.** Implement (2.16) and (3.36) symbolically and check the $k=1,2$ cases against the closed-form products $J_k(U(N),0)=\prod_{j=0}^{k-1}\frac{j!}{(k+j)!}\prod_{i=1}^k(N+i+j)$ of CAND-01200 Thm 1.5.1.2. Also check the printed signs and exponents in (3.36), (4.42)-(4.43), since the extract garbles them.
- **Risks / barriers.** RMT exactness does not transfer to $\zeta$: the recipe discards off-diagonal terms. Moment conjectures do not decide RH.

## Audit notes (Level 1 reader)

The extract mangles many sign and exponent placements (e.g. in (2.16), (3.36), (4.42)), so those formulas are flagged as unverified in this record. One possible inconsistency to check in the PDF: (2.5) and (2.16) index conventions $w_{\sigma(\ell)}w_{\sigma(q)}^{-1}$ versus the pole structure in (2.17) $(1-e^{z_q-z_\ell})^{-1}$; they look consistent after $w=e^{-\alpha}$ but the extract is ambiguous. In (4.44)-(4.47) the paper restricts to weight 2, prime level $q$. No mathematical error otherwise noticed in the inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01369`; harvest queries: msc_11M06, msc_11M50.
- Triage decision: include — Autocorrelation of RMT characteristic polynomials underlying moment conjectures.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

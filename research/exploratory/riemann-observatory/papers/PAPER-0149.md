# PAPER-0149 — Les suites de Farey et le problème des nombres premiers.

| Field | Value |
|---|---|
| Authors | Franel, J. |
| Year / stratum | 1924 / S2 |
| Venue | Gött. Nachr. 1924, 198-201 (1924). |
| Identifiers | zbMATH [50.0119.01](https://zbmath.org/?q=an:50.0119.01) |
| MSC |  |
| Families | C |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://gdz.sub.uni-goettingen.de/download/pdf/PPN252457811_1924/LOG_0032.pdf |
| Selection | score 2.1857, in-pool citations 23, seed lists 1, triage relevance 5 |

## Mathematical content (Level 1: full text read)

**Research question.** Express RH completely as a regularity property of Farey sequences: the sum of squared deviations between the ordered Farey fractions and equally spaced points is O(n^{-1+eps}).

**Historical motivation.** Landau (intro p.202): Littlewood 1912 had shown RH <=> M(n)=O(n^{1/2+eps}) and M(n)=sum cos 2pi rho_nu over Farey fractions; Franel upgrades to an L2 equivalence. Franel prefaces that RH 'seems reserved for a distant future'.

### Main results

- **THM-PAPER-0149-1** (Final statement p.201, theorem (equivalence), conditional-free, scope: asymptotic; Franel p.201). Let $\varrho_1<\varrho_2<\dots<\varrho_A$ be the Farey fractions in $(0,1]$ of order $n$, $A=A(n)=\sum_{r\le n}\varphi(r)$ (note: Franel's list starts at $\varrho_1$, with $\varrho_0=0$ understood). Then RH holds iff for every $\epsilon>0$ $\sum_{i}\left(\frac iA-\varrho_i\right)^2=O\left(n^{-1+\epsilon}\right)$ as $n\to\infty$ (equivalently $I(n)=O(n^{1+\epsilon})$, below).
- **THM-PAPER-0149-2** (Identity (3) p.200, identity, scope: finite; Franel p.200 eq. (3)). With $C(n)=\sum_{a\le n}\frac1aM(\lfloor n/a\rfloor)$, $M(n)=\sum_{r\le n}\mu(r)$, $\sigma(r)=\prod_{p\mid r}(1-p^{-2})$ and $I(n)=\int_0^1\delta^2(x,n)\,dx$, $\delta(x,n)=\sum_{a}f(ax)M(\lfloor n/a\rfloor)$, $f(x)=[x]-x+\tfrac12$: $I(n)=\frac1{12}\sum_{r\le n}\sigma(r)\,C^2(\lfloor n/r\rfloor)$.
- **THM-PAPER-0149-3** (Identity pp.199-201, identity, scope: finite; Franel pp.199-201; Landau p.203 eq.(6)). $\sum_i(\delta_i-\tfrac12)^2=A\,(I(n)-\tfrac1{12})$, i.e. $\sum_i\left(\frac iA-\varrho_i\right)^2=\frac1A\left(I(n)-\frac1{12}\right)$ (Landau's (6): $\sum\eta_\nu^2=\frac1A(I-\frac1{12})$, $\eta_\nu=\varrho_\nu-\nu/A$).
- **THM-PAPER-0149-4** (Landau Einleitung (8), theorem (Landau addendum), scope: asymptotic; Landau p.204 (8); proof on pp.204-206 (not read)). RH is equivalent to $\sum_{\nu=1}^A|\eta_\nu|=O(n^{1/2+\epsilon})$ (Landau p.204 claim 1).
- **THM-PAPER-0149-5** (Landau (9), theorem (Landau addendum), scope: asymptotic; Landau p.204 (9)). RH is equivalent to $\sum_{\nu}e^{2\pi i\nu/A}\eta_\nu=O(n^{1/2+\epsilon})$.
- **THM-PAPER-0149-6** (Landau (10),(11), theorem (conditional on RH), scope: asymptotic; Landau p.204 (10),(11)). Under RH both $\sum\eta_\nu$ and $\sum|\eta_\nu|$ satisfy bounds of the shape $O(n^{-1+c\,\log\log\log n/\log\log n})$ resp. $O(n^{1/2+c'\log\log\log n/\log\log n})$ with constants stated as 21 and 11 (exact printed form of exponents not legible at my resolution; verify in source). *Conditional on:* RH.

### Key definitions

- Farey sequence of order n
- $A(n)=\sum_{r\le n}\varphi(r)$
- $\eta_\nu=\varrho_\nu-\nu/A$
- $C(n),I(n),\sigma(r)$ as above

### Principal lemmas

- **THM-PAPER-0149-L1** (Fourier identity footnote p.199; Franel p.199 fn.1; Landau p.203). $\int_0^1f(ax)f(bx)\,dx=\frac{(a,b)^2}{12ab}$ for positive integers $a,b$ (Landau gives an elementary proof using $\sum_{l\bmod m}f(x+l/m)=f(mx)$). — *Role:* Computes $I(n)$ as a double sum over $M(\lfloor n/a\rfloor)M(\lfloor n/b\rfloor)$.
- **THM-PAPER-0149-L2** (Symmetry relations (1),(2) p.199; Franel p.199). $\delta_i+\delta_{A-i}=1$ and $\delta_i+\delta_{A-i-1}=A(\varrho_{i+1}-\varrho_i)$, where $\delta(x,n)=i+\frac12-Ax$ on $(\varrho_i,\varrho_{i+1})$. — *Role:* Reduces $\int\delta^2$ to $\frac1A\sum\delta_i^2-\frac16$.
- **THM-PAPER-0149-L3** (Dirichlet series identity p.200; Franel pp.200-201). $C(n)=\sum_{r\le n}c(r)$ where $\sum_{n\ge1}c(n)n^{-s}=\zeta(s+1)/\zeta(s)$. — *Role:* Passage from $I(n)=O(n^{1+\epsilon})$ to $C(n)=O(n^{1/2+\epsilon})$ and then, by convergence of $\sum c(n)n^{-s}$ for $\Re s>1/2$, to analyticity of $\zeta(s+1)/\zeta(s)$ and no zeros of $\zeta$ for $\Re s>1/2$ (since $\zeta(s+1)\ne0$).

### Proof architecture

Counting Farey fractions via Mobius inversion g(x,n)=sum_a [ax]M([n/a]); introduce periodic f and discrepancy delta(x,n); symmetry gives Sigma eta^2 = (I-1/12)/A. The Fourier/gcd integral formula gives I(n)=(1/12) sum_r sigma(r) C^2([n/r]) with sigma(r)>0, sigma(r)<=1. (=>) RH implies M(n)=O(n^{1/2+eps}) (Littlewood 1912) hence C(n), hence I(n)=O(n^{1+eps}). (<=) I(n)=O(n^{1+eps}) and positivity of terms (r=1 term C^2(n)/12) gives C(n)=O(n^{1/2+eps}), so the Dirichlet series of zeta(s+1)/zeta(s) converges for Re s>1/2, so zeta has no zeros there.

**Imported results.** Littlewood 1912: RH <=> M(n)=O(n^{1/2+eps}) (both directions used); Standard convergence of Dirichlet series and zero-free zeta(s+1) for Re s>0

**Techniques.** Farey sequence discrepancy; Mobius inversion; Fourier series of sawtooth f(x)=[x]-x+1/2; Dirichlet series convergence abscissa; Littlewood's equivalence RH <=> M(x)=O(x^{1/2+eps})

## Context and interpretation

**Importance and obstacle overcome.** Shows RH is entirely a statement about rational numbers (Farey spacing), the first 'elementary-looking' equivalent. Obstacle: expressing the Farey L2 discrepancy exactly in terms of Mobius partial sums via the identity I(n)=(1/12) sum sigma(r)C^2([n/r]), whose positivity makes the converse easy.

**Relation to prior work.** Builds on Littlewood (C. R. Acad. Sci. Paris 154 (1912) 263-266) and the classical M(n)=sum_{rho in F_n} e^{2 pi i rho}. Landau's companion note adds L1 and exponential-sum equivalences. Later: Kanemitsu-Yoshimoto, Codeca-Perelli, Mikolas, Huxley (Farey discrepancy), Boca-Zaharescu.

**Limitations and open questions.** Franel explicitly notes the equivalence replaces zeta by purely rational data but gives no route to a proof. Landau's addenda sharpen via L1 and exponential-sum forms; trivial bounds give sum eta^2=O(1) only.

**Ideas in remarks/appendices/abandoned paths.** Landau's remark that sum over reduced fractions of e^{2 pi i rho} equals M(n) (primitive roots of unity). Landau (8) gives an L1 version with exponent 1/2+eps. Exponents (10),(11) show RH implies Farey L2 deviation O(n^{-1+c loglog logn/loglog n}), a sharper-than-eps bound analogous to Littlewood's M(x) bound.

## Research potential

- **Hypotheses that might be weakened.** Replace O(n^{-1+eps}) by a specified explicit bound with constants to give a certified finite test; the positivity sigma(r)>0 may allow one-sided effective statements: sum eta^2 <= c n^{-1}log^k n would give effective Mertens-type bounds.
- **Generalizations.** Farey sequences restricted to arithmetic progressions or with congruence conditions leading to L(s,chi) analogues; Farey fractions in Q(i) (Hecke) would give GRH-type statements for Dedekind zeta.
- **Candidate connections.** Link to Mertens/Pólya (CAND-00065) through C(n) and M(n); to Nyman-Beurling-Baez-Duarte L2 criteria; to Kanemitsu-Yoshimoto Farey-sum RH equivalents; to the 'Franel-Landau' sum used in Codeca-Perelli.
- **Reusable lemmas.** Exact identity I(n)=(1/12) sum sigma(r)C^2([n/r]); sawtooth Fourier orthogonality integral (a,b)^2/(12ab).
- **Possible experiments.** Compute sum_i (i/A - rho_i)^2 * n for n up to 1e5 (Farey sequence generation is O(n^2)), compare with (I(n)-1/12)/A identity as a verification, and fit n^{1+eps} growth; test C(n)^2 vs I(n) numerically.
- **Risks / barriers.** Equivalence is asymptotic with arbitrary eps, so finite computation cannot certify RH; Mertens function M(n)=O(n^{1/2+eps}) is itself equivalent to RH, no easier.

## Audit notes (Level 1 reader)

Read visually from scans; no inconsistencies found in Franel's algebra (checked: sum(delta_i-1/2)^2 = sum delta^2 - A/4 = A(I-1/12)). Minor: Franel's index convention (rho_0 = 0, rho_A = 1) is implicit. Landau's exponents in (10),(11) unreadable at my resolution; Landau's proofs pp.205-206 not inspected. The triage summary 'squared deviations O(N^{-1+eps})' is correct.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00231`; harvest queries: citation_expansion.
- Triage decision: include — Franel-Landau: RH equivalent to Farey sequence discrepancy bound.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

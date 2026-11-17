# PAPER-0120 — Contributions to the theory of the Riemann Zeta-function and the theory of the distribution of primes.

| Field | Value |
|---|---|
| Authors | Hardy, G. H.; Littlewood, J. E. |
| Year / stratum | 1917 / S2 |
| Venue | Acta Math. 41, 119-196 (1917). |
| Identifiers | zbMATH [46.0498.01](https://zbmath.org/?q=an:46.0498.01) · DOI [10.1007/BF02422942](https://doi.org/10.1007/BF02422942) |
| MSC | 11M06, 11N05 |
| Families | A, B |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://archive.org/details/actamathematica40upps (Acta Mathematica vols 40-41 scan, OCR; paper at Acta Math. 41, pp. 119-196) |
| Selection | score 4.0429, in-pool citations 154, seed lists 4, triage relevance 5 |

## Mathematical content (Level 1: full text read)

**Research question.** A memoir of five loosely connected contributions: (2.1) Tauberian-type convergence theorems for Dirichlet series via the Cahen-Mellin integral (implying PNT equivalents); (2.2) behaviour of F(y)=sum(Lambda(n)-1)e^{-ny}, omega-results for psi(x)-x under RH; (2.3) Tchebychev's 1853 assertion on sum (-1)^{(p-1)/2} e^{-py} (prime races mod 4) assuming GRH for L(s,chi_4); (2.4) mean square of zeta on the critical line, int |zeta(1/2+it)|^2 ~ 2T log T; (3) Landau-type exponential sums over zeros; (4) infinitely many (indeed N_0(T)>>T^{1/2-eps}... in fact N_0(T)=Omega(T^{1/4-eps})) zeros on the critical line; (5) Pi(x)-li(x)=Omega_{+-}(sqrt(x) loglog log x/log x) so Pi(x)<li(x) fails (Littlewood's theorem).

**Historical motivation.** Following Hardy's 1914 proof of infinitely many critical zeros (CAND-00179), Landau's extensions, Littlewood's C. R. note (22 June 1914) on the distribution of primes, and Tchebychev's 1853 assertion on primes mod 4, the authors collect their results; the paper was presented to Acta in summer 1915 and published 1917. The empirical belief Pi(x)<li(x) (Gauss, Goldschmidt, Gram, Phragmen, Meissel up to 1e9) is refuted here.

### Main results

- **THM-PAPER-0120-1** (Theorem 2.24, theorem, scope: asymptotic; sec. 2.24, p. 138; also stated as (1.141)-(1.142)). Assume RH. As $y\to0^+$, $F(y)=\sum_{n\ge1}(\Lambda(n)-1)e^{-ny}=O(y^{-1/2})$, and there is a constant $K>0$ such that each of $F(y)<-K y^{-1/2}$ and $F(y)>K y^{-1/2}$ holds for a sequence of $y\to0$, i.e. $F(y)=\Omega_\pm(y^{-1/2})$. *Conditional on:* RH.
- **THM-PAPER-0120-2** (Theorem 2.241, corollary, scope: asymptotic; p. 139, sec. 2.24). There is $K>0$ with $\psi(x)-x<-K\sqrt x$ and $\psi(x)-x>K\sqrt x$ each for arbitrarily large $x$, i.e. $\psi(x)-x=\Omega_\pm(\sqrt x)$ (substantially Schmidt's theorem); stated unconditionally in the paper, deduced from Theorem 2.24 in the case RH holds and from the known $\Omega_\pm(x^{\Theta-\delta})$ result when $\Theta>1/2$.
- **THM-PAPER-0120-3** (Theorem 2.25, theorem, scope: asymptotic; sec. 2.25). Assuming RH, all Riesz means (hence Cesaro means) formed from $\sum(\Lambda(n)-1)$ are of the forms $O(\sqrt\omega)$, $\Omega_+(\sqrt\omega)$, $\Omega_-(\sqrt\omega)$. *Conditional on:* RH.
- **THM-PAPER-0120-4** (Theorems 2.33, 2.34, 2.35, 2.351 (Tchebychev's assertion), theorem, scope: asymptotic; secs 2.31-2.35, pp. 141-151). Let $L(s)=1^{-s}-3^{-s}+5^{-s}-\cdots$ ($\sigma>0$). If all complex zeros of $L(s)$ have real part $1/2$, then Tchebychev's 1853 claim holds: $F(y)=e^{-3y}-e^{-5y}+e^{-7y}+e^{-11y}-\dots=\sum_{p>2}(-1)^{(p+1)/2}e^{-py}\to+\infty$ as $y\to0^+$; quantitatively Thm 2.34 gives a lower bound of order $H/\sqrt{y\log(1/y)}$-type (OCR of exact form of (2.341) unreliable), and Thm 2.35: the Riesz/Cesaro mean of the first order of $\sum(-1)^{(p-1)/2}\log p$ tends to $-\infty$ at least as fast as a constant multiple of $-\sqrt\omega$. (Exact constants/forms: statement of Thm 2.33 garbled in OCR.) *Conditional on:* GRH for L(s,chi_{-4}).
- **THM-PAPER-0120-5** (Theorem 2.41, eq. (1.22), theorem, scope: asymptotic; sec. 2.4, p. 151; intro (1.22)). $\int_{-T}^{T}|\zeta(\tfrac12+it)|^2dt\sim 2T\log T$ as $T\to\infty$.
- **THM-PAPER-0120-6** (Theorem 3.1 (cf. (1.31)-(1.33)), theorem, scope: asymptotic; sec. 3, Theorem 3.1, p. ~168 (intro (1.33), p.124)). For real $a,b,\omega$ with $a,b>0$ (b a scale parameter), a Landau-type bound for the exponential sum $\sum_{0<\gamma\le T}e^{i\omega\gamma\log(b\gamma)}$-type sums over ordinates of zeros (sum $\sum'$ in the paper; exact exponents garbled in OCR), of size $O(T^{(1+a)/2})$ (trivial for $a\ge1$), with $O(\log T)$ when $\omega<$ an explicit threshold depending on $a$, uniform for $b$ in compact intervals; and convergence of the sum continued to infinity when $\omega$ is below that threshold. Introduction: conjecture that the true order is $o(T^{1/2+\epsilon})$ for all $a$.
- **THM-PAPER-0120-7** (Theorems 4.41, 4.42, eq. (1.41), theorem, scope: asymptotic; secs 4.1-4.4, pp. 160-166; intro 1.4). For every $\epsilon>0$ there is $T_0(\epsilon)$ such that for $T>T_0$ the segment $\{\tfrac12+it:\ T<t\le T+T^{1/4+\epsilon}\}$ contains at least one zero of $\zeta(s)$ of odd order. Hence $N_0(T)$, the number of zeros on $\sigma=1/2$ with $0<t\le T$, satisfies $N_0(T)=\Omega(T^{3/4-\epsilon})$? -- as printed: $N_0(T)=\Omega(T^{1/4-\epsilon})$ for every $\epsilon>0$ (the OCR of the exponent in (1.41)/Thm 4.42 is ambiguous; the zero-spacing $T^{1/4+\epsilon}$ implies a lower bound $T^{3/4-\epsilon}$, so the printed exponent should be checked against the page image).
- **THM-PAPER-0120-8** (Theorems 5.2, 5.6, 5.8, 5.81, (1.52)-(1.53), theorem, scope: asymptotic; sec. 5, pp. 167-196; intro 1.5, eqs (1.52)-(1.53)). Thm 5.8: $\psi(x)-x=\Omega_+(\sqrt x\log\log\log x)$ and $\psi(x)-x=\Omega_-(\sqrt x\log\log\log x)$. Thm 5.81: $\Pi(x)-\mathrm{li}(x)+\tfrac12\mathrm{li}(\sqrt x)=\Omega_{\pm}\big(\tfrac{\sqrt x\log\log\log x}{\log x}\big)$ [Littlewood's theorem]. In particular $\Pi(x)>\mathrm{li}(x)$ for arbitrarily large $x$ (so (1.53) $\Pi(x)<\mathrm{li}(x)$ is false). Thm 5.6: if $F(i x)$ boundary values, $-\Im F(ix)=\Omega_+(\log\log x)$ and $-\Im F(ix)=\Omega_-(\log\log x)$ hmm as printed; Thm 5.2 gives the corresponding inequalities on the strip.

### Key definitions

- $F(y)=\sum_{n\ge1}(\Lambda(n)-1)e^{-ny}$ ($\Re y>0$)
- $\Pi(x)=\sum_{p^m\le x}1/m$ (prime-power weighted counting)
- $N_0(T)$: number of zeros of zeta on $\sigma=1/2$, $0<t\le T$
- $\Theta$: upper limit of real parts of zeros
- $\Omega_\pm$ notation: $f=\Omega_+(g)$ if $f>Kg$ i.o.; $f=\Omega_-(g)$ if $f<-Kg$ i.o.

### Principal lemmas

- **THM-PAPER-0120-L1** (Lemma 2.111 / Cahen-Mellin; sec. 2.11). $e^{-y}=\frac1{2\pi i}\int_{\kappa-i\infty}^{\kappa+i\infty}\Gamma(s)y^{-s}ds$, $\Re y>0$, $\kappa>0$. — *Role:* Basic transform linking Dirichlet series to e^{-ny} sums throughout section 2.
- **THM-PAPER-0120-L2** (Theorem 2.12; sec. 2.12). If $\sum a_n\lambda_n^{-s}$ converges absolutely for $\sigma>\sigma_0$, the sum function F(s) is regular for $\sigma>c$ (continuous on $\sigma=c$) with $F(s)=O(e^{C|t|})$, $C<\pi/2$ uniformly for $\sigma\ge c$, then $f(y)=\sum a_ne^{-\lambda_ny}=o(y^{-c})$ as $y\to0$. — *Role:* Tauberian-type input yielding PNT-equivalent forms (1.121)-(1.124) via Thm 2.121, 2.13, 2.14.
- **THM-PAPER-0120-L3** (Lemma 2.113; sec. 2.11). Tauberian-type lemma (equivalent to Theorems D, E, F of Hardy-Littlewood, Messenger of Math.): Abel-type summability f(y)->F(0) implies Riesz/convergence under one-sided conditions on a_n. — *Role:* Passes from e^{-ny} means to convergence of the series.
- **THM-PAPER-0120-L4** (Lemma 2.411-2.413 (Bessel kernel K_nu); sec. 2.41). Lemmas on the integral representation of $K_\nu(y)$ and its asymptotics for $y=re^{i\theta}$, $|\theta|<\pi/2-\delta$ used for the mean-square computation. — *Role:* Evaluates the diagonal and off-diagonal terms in the proof of Theorem 2.41 by the Cahen-Mellin route.
- **THM-PAPER-0120-L5** (Lemma 5.3 and Dirichlet's theorem on simultaneous approximation (5.4); secs 5.3-5.5). Kronecker/Dirichlet approximation lemma: simultaneous diophantine approximation lets one align the phases of the first many terms $\gamma_n\log$ of $\sum \rho^{-1}x^{\rho}$ so that the sum of the first $N$ terms of the explicit formula is as large as $\sqrt{x}\log\log\log x$. — *Role:* Drives Theorem 5.2 / 5.6 (Omega results for the oscillating sum).

### Proof architecture

Section 2.1: Cahen-Mellin integral + Tauberian-type Theorems 2.12-2.15 (convergence of Dirichlet series from regularity and growth, equivalents of PNT). Section 2.2: explicit formula for F(y)=sum(Lambda-1)e^{-ny} as a sum over zeros (via contour shift, zeros rho=1/2+i gamma) -> under RH F(y)=O(y^{-1/2}) and Omega_pm via sum of cos(gamma log y) terms controlled by N(T+1)-N(T)=O(log T) and Kronecker-type argument. Section 2.3: same for L(s,chi_4). Section 2.4: mean square by the Cahen-Mellin integral instead of the approximate functional equation. Section 3: adapt Landau's exponential-sum argument over zeros. Section 4: a different method (Cauchy theorem on rectangles for the real-valued Xi(t), an integral of Xi(t) times a rapidly oscillating exponential/ Gamma-weight is shown nonzero unless Xi changes sign), showing a sign change of Xi in [T,T+T^{1/4+eps}]. Section 5: Dirichlet's simultaneous approximation applied to the series F(z)=sum_{rho} z-type with z=i x; imaginary part of F(ix) is Omega_pm(loglog x); then psi(x)-x and Pi(x)-li(x) Omega results by Riesz means (Theorem 2.25) and partial summation.

Dependency edges: CAND-00076 → CAND-00179 (completes and quantifies); CAND-00219 → CAND-00076 (simplifies Theorem 2.41 by approximate functional equation; cites p.151-156); CAND-00077 → CAND-00076 (refines Theorem 2.41 (mean square) analogue to the fourth moment)

**Imported results.** Cahen (Ann. ENS 1894) and Mellin (Acta Soc. Fenn. 1895) integral; Landau's Hilfssatz 10 (Gottingen Nachr. 1912) used as the critical lemma in Theorem 3.1; Schmidt (Math. Ann. 57, 1903) for the case Theta>1/2; N(T+1)-N(T)=O(log T) (von Mangoldt/Backlund); Dirichlet's / Kronecker's simultaneous approximation theorems; Bohr-Landau-Littlewood on zeta near sigma=1/2

**Techniques.** Cahen-Mellin integral; Tauberian-type theorems (Hardy-Littlewood); explicit formulas over zeros, N(T+1)-N(T)=O(log T); Kronecker / Dirichlet simultaneous diophantine approximation; Riesz and Cesaro means; Landau's exponential sums over zeros; Bessel K-kernel integrals; contour integration for Xi(t)

## Context and interpretation

**Importance and obstacle overcome.** Foundational: it gives (i) the first quantitative lower bound for zeros on the critical line (zero in [T,T+T^{1/4+eps}], so N_0(T) = Omega(T^{3/4-eps})-type spacing control), (ii) Littlewood's Omega_pm(sqrt x logloglog x/log x) theorem with a full proof, disproving the long-standing belief Pi(x)<li(x), with the logloglog x unavoidable obstacle bypassed by Kronecker's theorem; (iii) the mean-square 2T log T result; and (iv) the Cahen-Mellin/Tauberian toolkit that equates PNT variants. The unifying obstacle overcome was unconditional control of oscillating sums over the unknown zeros via diophantine approximation rather than assuming RH.

**Relation to prior work.** Builds on Hardy (1914), Landau (Handbuch, Gitterpunkte 1912, Math. Ann. 76 1915), Schmidt (1903), Cahen-Mellin, Bohr-Landau-Littlewood on zeta near the critical line, Lindelof, Gram, Backlund. De la Vallee-Poussin (C. R. 1916) independently obtained much of section 4 by other methods (Additional Note).

**Limitations and open questions.** Several results are conditional (2.24, 2.25 on RH; 2.33-2.35 on GRH for chi_4). The authors state they cannot prove Omega_pm(x^{1/2-delta... } stronger) bounds of type (1.15) psi(x)-x=Omega_pm(x^{1/2}(loglog x)^{?}) beyond the order they find; cannot show N_0(T)=Omega(T) (they hope for N_0(T)=Omega(T^{1-eps}) 'by modification of the argument' but fail); cannot prove Tchebychev's assertion unconditionally ('difficulties of the same nature' as for (1.15)); conjecture the exponent in Theorem 3.1 ((1+a)/2) is not the truth: expected o(T^{1/2+eps}) for all a. They also state a formula from Ramanujan (1.2, the F(s) definite-integral formula) which they 'are unable to give a satisfactory proof' of.

**Ideas in remarks/appendices/abandoned paths.** Section 2.3: relation of Tchebychev bias to zeros of L(s,chi_4) (only conditional on GRH); sec. 1.2 remarks that the Tchebychev assertion should fail if GRH fails. The Ramanujan-suggested formula for F(s) as a definite integral (sec. 1.2, p. 123) is stated without proof and 'well worthy of attention'.

## Research potential

- **Hypotheses that might be weakened.** Theorem 2.24/2.25 assume RH only to write F(y) as a sum of zero-terms with Re rho=1/2; the Theta-version (sup of real parts) is also stated, so a unified Omega result in terms of Theta and N(T) could be tested. Theorem 2.33-2.35 assume GRH for chi_4 only; a weakened form with a zero-free region might still give prime-race bias results.
- **Generalizations.** Section 5 for primes in progressions (the authors note psi_{chi_4}(x) and Pi_{4,3}-Pi_{4,1} with sqrt(x) logloglog x/log x). Section 4's sign-change method for Xi generalizes to Hardy Z-functions of Dirichlet L-functions (Landau 1915) and later to Selberg's N_0(T)>>T log T.
- **Candidate connections.** Linking the Kronecker-phase argument in section 5 to quantitative Dirichlet approximation / to recent work on the Ω-results of Montgomery and the distribution of ψ(x)-x; relating the Cahen-Mellin Tauberian conditions (Thm 2.12, C<pi/2) to modern Wiener-Ikehara type PNT proofs; relating section 2.2 explicit formula for sum (Lambda(n)-1)e^{-ny} to the heat-kernel/theta-regularization perspective on zeros.
- **Reusable lemmas.** Theorem 2.12/2.121 (Tauberian convergence from regularity in a half-plane plus growth e^{C|t|}, C<pi/2); Lemma 5.3+5.4 phase alignment; Theorem 2.25 (Riesz means O/Omega_pm(sqrt omega) under RH).
- **Possible experiments.** (1) Numerically compute F(y)=sum(Lambda(n)-1)e^{-ny} for y down to 1e-6 and compare with -2 sum ... y^{-1/2} cos(gamma log y) predicted by the explicit formula; check Omega_pm(y^{-1/2}) visibility. (2) Compute minimal x with Pi(x)>li(x) (Skewes-type) and compare with the Kronecker phase-alignment heuristic of section 5. (3) Test Theorem 3.1 bound numerically using zeros from LMFDB tables with varying a and omega.
- **Risks / barriers.** Theorem 5.81's logloglog x is believed far from optimal; improving it is tied to the size of sum 1/|rho|-weighted phases (Gonek-Hejhal conjecture type). Section 4 exponent T^{1/4+eps} is far from Selberg-level results and seems to require different tools (Selberg's mollified method).

## Audit notes (Level 1 reader)

OCR of the Acta Math scan is noisy: exponents in (1.33)/(Theorem 3.1), the exact form of (2.341), and the exponent printed in (1.41)/Theorem 4.42 could not be read reliably (I did not view the page images for secs 3 and 4); my record of Theorem 4.42's exponent should be checked: known history is N_0(T) > c T^{... } with zero spacing T^{1/4+eps}. Also: Theorem 2.241 is stated as unconditional in the text but its proof for the case RH holds is Theorem 2.24 and for Theta>1/2 an old Omega result (fine). Nothing else suspicious in the inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00076`; harvest queries: msc_11M06, msc_11N05.
- Triage decision: include — Hardy-Littlewood 1918 Acta paper with approximate functional equation and mean values.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

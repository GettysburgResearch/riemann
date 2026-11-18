# PAPER-0115 — The zeros of Riemann's zeta-function on the critical line.

| Field | Value |
|---|---|
| Authors | Hardy, G. H.; Littlewood, J. E. |
| Year / stratum | 1921 / S2 |
| Venue | Math. Z. 10, 283-317 (1921). |
| Identifiers | zbMATH [48.0344.03](https://zbmath.org/?q=an:48.0344.03) · DOI [10.1007/BF01211614](https://doi.org/10.1007/BF01211614) |
| MSC | 11M26 |
| Families | B |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://gdz.sub.uni-goettingen.de/id/PPN266833020_0010 (GDZ page images 00000293-00000327 of Math. Z. 10, pp. 283-317; read visually, no OCR text layer used) |
| Selection | score 4.1143, in-pool citations 38, seed lists 3, triage relevance 5 |

## Mathematical content (Level 1: full text read)

**Research question.** Prove that a positive proportion of the ordinates in (T,2T) carry a zero of zeta on the critical line, i.e. $N_0(T)>KT$, and that every short interval $(T,T+T^a)$, $a>1/2$, contains $\gg T^a$ critical zeros. This improves the earlier Acta Math. 41 (1917) bound $N_0(T)>T^{3/4-\epsilon}$ (H-L) from $T^{3/4-\epsilon}$ (as printed on p. 283) to linear order.

### Main results

- **THM-PAPER-0115-1** (Theorem A (1.1), theorem, scope: asymptotic; Sec. 1, p. 283; proved in Sec. 2, pp. 284-298 (Sec. 2.8-2.9, pp. 296-298)). Let $N_0(T)$ be the number of zeros $\rho=\tfrac12+it$ of $\zeta$ with $0<t<T$. There exist $K>0$ and $T_0$ such that $N_0(T)>KT$ for all $T>T_0$. (Proof gives at least $T/(4H)$ zeros in $(T,2T)$ for a sufficiently large absolute constant $H$.)
- **THM-PAPER-0115-2** (Theorem B (1.2), theorem, scope: asymptotic; Sec. 1, p. 283; proved in Sec. 3-5, pp. 298-315 (conclusion at 5.5, p. 315)). Let $U=T^a$ with $a>\tfrac12$. There exist $K=K(a)>0$ and $T_0=T_0(a)$ such that $N_0(T+U)-N_0(T)>KU$ for all $T>T_0$.
- **THM-PAPER-0115-3** (Lemma 18, lemma (independent interest), scope: asymptotic; Sec. 4, p. 305 (proof pp. 305-312)). If $T^a<U<T^b$ with $a>\tfrac12$ (and $b=5/8$ first, then removed) and $0<H<T^c$ with $c=c(a)>0$ small, then with $I(t,H)=\int_t^{t+H}X(u)\,du$: $J=\int_T^{T+U}I^2\,dt=\pi\sqrt{2\pi}\,HU+O\!\left(U/\log T\right)$ (constant as I read it off the scan; not independently re-derived).
- **THM-PAPER-0115-4** (Sec. 6.3 identity, remark / corollary, scope: asymptotic; Sec. 6.3, p. 317). For $H,K$ as in Lemma 18, $\int_T^{T+U} I(t,H)\,I(t+H,K)\,dt=O(U/\log T)$ uniformly in $0\le H,K\le T^c$ (orthogonality of consecutive block integrals).

### Key definitions

- $X(t)$: real function with $\Gamma(\tfrac12 s)\zeta(s)=2\pi^{1/4}t^{-1/4}e^{-\pi t/4}\pi^{it/2}X(t)$ on $s=\tfrac12+it$ (2.61 ff.), i.e. Hardy's $Z$ up to normalization
- $I(t,H)=\int_t^{t+H}X(u)du$; $\underline I(t,H)=\int_t^{t+H}|X(u)|du$
- $N_0(T)$ = number of critical-line zeros with $0<t<T$

### Principal lemmas

- **THM-PAPER-0115-L1** (Lemma 1 / (2.111); p. 284-285). For $\sigma>0,s\ne1,x>0$: $\zeta(s)+\frac{x^{1-s}}{1-s}-\sum_{n\le x}'n^{-s}=2(2\pi)^{s-1}\sum_{n\ge1}n^{s-1}\int_{2n\pi x}^\infty u^{-s}\cos u\,du$ (valid for $\sigma>-1$ in the second form); proof suggested by H. Cramer. — *Role:* Exact representation of zeta that gives the approximate functional equation and, with $x\to0$, the functional equation.
- **THM-PAPER-0115-L2** (Lemma 2; p. 285-286). For $\sigma\ge\sigma_0>0$, $|s-1|\ge\delta>0$, $|t|<2\pi x/C$, $C>1$: $\zeta(s)=\sum_{n\le x}n^{-s}-\frac{x^{1-s}}{1-s}+O(x^{-\sigma})$ uniformly. — *Role:* Dirichlet-polynomial approximation of zeta by van der Corput-type stationary-phase-free argument.
- **THM-PAPER-0115-L3** (Lemmas 3,4; p. 286-287). For $\sigma\ge\sigma_0>0$, $|t|<Ax$: $\eta(s)=(1-2^{1-s})\zeta(s)=\sum_{n\le x}(-1)^{n-1}n^{-s}+O(x^{-\sigma})$ and $\Theta(s)=\sum_{n\ge2}\frac{(-1)^{n-1}n^{-s}}{\log n}=\sum_{n\le x}\frac{(-1)^{n-1}n^{-s}}{\log n}+O(x^{-\sigma})$. — *Role:* Alternating (eta) series on the critical line, whose antiderivative-in-$s$ ($1/\log n$ weights) controls $\int\eta\,dt$ in Theorem A.
- **THM-PAPER-0115-L4** (Lemmas 7,8 (2.42),(2.44); p. 287-288). With $\psi(t)=\sum_{n\ge2}\frac{(-1)^{n-1}}{\log n}n^{-1/2-it}$: $\int_T^{2T}|\psi(t+u)|^2dt=O(T)$ uniformly for $0\le u\le T$; and $\frac1{2T}\int_{-T}^T|\chi(\tfrac12+it)|^2dt\sim\sum_{n\ge2}\frac1{n(\log n)^2}$. — *Role:* Mean square bound for the error term $\Psi$ in $\underline I>AH+\Psi$.
- **THM-PAPER-0115-L5** (Lemma 11 (2.711); p. 291-296). $\int_0^T\{I(t,H)\}^2dt<AHT$ for $T>T_0(H)$. — *Role:* Upper mean-square bound for $\int X$ over blocks of length $H$; obtained via Lemma 10 (Mellin/Hankel-function formula for $\int\Gamma(s+a)\Gamma(s+b)\zeta(2s+2a)\zeta(2s+2b)y^{-2s}ds$), the Abel weight $e^{-\epsilon t}$, and the divisor-type diagonal estimate $\underline C_m=O(Hm)$ (2.783) with $k=1-1/H$.
- **THM-PAPER-0115-L6** (Lemma 15 (weak approximate functional equation); p. 301-304 (Lemma 14 stated p. 301)). For fixed $0\le\sigma<1$, $x,y>A$, $2\pi xy=|t|$: $\zeta(s)=\sum_{n<x}n^{-s}+\chi\sum_{n<y}n^{s-1}+O\big((x^{-\sigma}+|t|^{1/2-\sigma}y^{\sigma-1})\log t\big)$, where $\chi=\left(\frac{|t|}{2\pi e}\right)^{-it}\left(\frac{t}{2\pi}\right)^{1/2-\sigma}e^{\frac14\pi i\,\mathrm{sgn}\,t}$. Lemma 14 is the sharp version without the $\log t$ and is stated but not proved here. — *Role:* Hardy-Littlewood approximate functional equation (pre-Hardy-Littlewood 1929); feeds Lemma 17: $X(t)=\Theta+\bar\Theta+O(t^{-1/4}\log t)$ with $\tau=\sqrt{t/2\pi}$.
- **THM-PAPER-0115-L7** (Lemma 20; p. 314-315). There is $A$ such that $\underline I=\int_t^{t+H}|X(u)|du>\tfrac12H$ on $(T,T+U)$ except in a set $\underline S$ of measure $<AU/H^2$ (for $H\ge4$). — *Role:* Lower bound for absolute-value integral, via $|\int\zeta|$, mean square of $M$ and Lemma 19; combined with $\int I^2<AHU$ (Lemma 18, 5.51) to force $|I|<\underline I$ and hence sign changes.

### Proof architecture

Core principle (p. 297, 316): if no zero of $X(u)$ (the real function with $\zeta(\tfrac12+it)\approx e^{i\theta}X(t)$, $X$ real) lies in $(t,t+H)$ then $\underline I:=\int|X|=|I|:=|\int X|$. Theorem A: (i) Lemmas 1-4 give $\eta(s)=\sum_{n\le x}(-1)^{n-1}n^{-s}+O(x^{-\sigma})$; since $|X|>A|\eta|$, $\underline I>A\Re\int\eta=AH+\Psi$ with $\Psi=O(|\psi(t+H)|+|\psi(t)|)$ (2.81). (ii) Lemma 7 mean-square of $\psi$ shows $\underline I>\tfrac12AH$ off a set of measure $\le\epsilon_HT$ in $(T,2T)$ (2.84). (iii) Lemma 11, $\int_T^{2T}I^2\le CHT$, shows $|I|<\tfrac12AH$ off a set of measure $\le \epsilon_HT$; thus $|I|<\underline I$ except on a small set, hence a zero in $j_1$ or $j_2$ for each abutting pair of length-$H$ intervals not meeting the exceptional set; counting gives $\ge T/(4H)$ zeros. The mean-square bound for $I$ in Lemma 11 is the hard step: through Mellin-Barnes (Lemma 9,10), shifting the contour to $\Re s=1/4$, reducing to $\int t^{-1/2}X(2t+2\alpha)X(2t+2\beta)e^{-2\epsilon t}dt$ (2.753), integrating over $\alpha,\beta\in(0,H)$ to get $\sum C_n e^{-2n\pi\epsilon}/\sqrt n$ with $C_n=\sum_{d|n}(\sin(\tfrac12H\log(n/d^2))/\log(n/d^2))^2$, and bounding partial sums $\underline C_m=O(Hm)$. Theorem B: replaces the Abel-weight argument by genuine short-interval mean values: approximate functional equation (Lemmas 12-15) gives $X(t)=\Theta+\bar\Theta+O(t^{-1/4}\log t)$ (Lemma 17), then (Lemma 18) $\int_T^{T+U}I^2dt\sim$ const$\cdot HU$ with $O(U/\log T)$ error, via oscillatory-integral Lemma 16 ($\int(t/e\xi)^{i(t+\gamma)}dt=O(1/\log(T/\xi))$) to kill off-diagonal terms and Lemma 5-6 type double sums; Lemma 19 (mean square of $M=\int\zeta-1$) and Lemma 20 give lower bound for $\underline I$; (5.51)+(2.9)-type counting finishes.

Dependency edges: CAND-00072 → Hardy-Littlewood 1917 Acta Math 41 (improves T^{3/4-eps} to cT); CAND-00187 → CAND-00072 (Selberg 1942 improves to cT log T by mollifying the Hardy-Littlewood block argument)

**Imported results.** Hankel cylinder-function calculus: Nielsen, Handbuch der Theorie der Cylinderfunktionen (p. 289, 293); Stirling formula for $\Gamma$ (2.61); Hardy-Littlewood, Acta Math. 41 (1917) 119-196 (earlier $T^{3/4-\epsilon}$ bound; context); Young, Proc. LMS (2) 9 (1919) 463-485 (term-by-term integration, footnote 3 p. 284); Riemann functional equation, convexity bound $\zeta(\tfrac12+it)=O(t^{1/6})$ (used in (2.735), 'ζ(1/2+2i(t+α))<A(t^{1/8}+1)')

**Techniques.** real-valued function $X(t)$ (equivalent to Hardy's $Z$) and sign-change criterion $|\int X|<\int|X|$; integral of zeta over short intervals via alternating (eta) series; Mellin-Barnes / Hankel cylinder-function integral (Lemmas 9-10); Abel-weight regularization $e^{-\epsilon t}$ and Tauberian-free mean-square bound; divisor-sum/lattice-point counting in polar coordinates (2.78); approximate functional equation (weak form, Lemma 15); van der Corput-type first-derivative oscillatory integral estimates (Lemmas 12,16); Montgomery-Vaughan-free diagonal/off-diagonal mean value (Lemmas 5,6)

## Context and interpretation

**Importance and obstacle overcome.** First linear lower bound for critical-line zeros, improving the Acta Math. 1917 exponent. The obstacle was controlling $\int_t^{t+H}X$ in mean square for bounded $H$ without a short-interval mean value theorem for $|\zeta|^2$ twisted; they overcame it by the Mellin-Barnes/Abel-weight route (Thm A) and by the weak approximate functional equation plus oscillatory off-diagonal estimates (Thm B). Selberg later identified in the HL argument the loss from sign-oscillation and replaced the fixed block by a mollified weight, giving $N_0(T)\gg T\log T$ (see CAND-00187).

**Relation to prior work.** 

**Limitations and open questions.** Result stops at positive-proportion-free linear order: $N_0(T)\gg T$ versus $N(T)\sim\frac T{2\pi}\log T$, so the proportion of critical zeros is $O(1/\log T)$; authors say Theorem B falls short of the truth by a factor $\log T$ (p. 315, Sec. 6.1). They identify the obstacle (Sec. 6.2, p. 315-316): for small constant $H$ the main term $H$ in $\underline I$ is dominated by $\Re M\sim\sqrt H$, and $\int|\zeta|$ is not comparable to $|\int\zeta|$ (mean square of $|\int\zeta|$ is asymptotically half that of $I$, via (5.33) and footnote 10). They heuristically expect, assuming RH ($R(t)=o(\log t)$, mean $O(\log\log T)$), that $|\int\zeta|\approx\int|\zeta|$ for $H=o(1/\log\log T)$. No constant is computed (not effective).

**Ideas in remarks/appendices/abandoned paths.** (a) Sec. 6.2, p. 316: heuristic conditional on RH that $|\int_t^{t+H}\zeta|\sim\int|\zeta|$ for $H=o(1/\log\log T)$, tied to $\int_0^T|R(t)|dt=O(T\log\log T)$ for $R=S$-type remainder of $N(T)$; this is an early link between sign-oscillation of $S(t)$ and critical-line zeros, not developed. (b) Sec. 6.3 orthogonality of consecutive block integrals, 'appears very curious', unused - a hint of the pair-correlation structure. (c) Lemma 5 is flagged as 'frequently useful'.

## Research potential

- **Hypotheses that might be weakened.** Theorem B needs $a>1/2$ and $H<T^c$; Lemma 18's $O(U/\log T)$ error uses $U>T^{1/2+\delta}$ so that diagonal Dirichlet-polynomial mean values dominate. Extending to $a<1/2$ (the HL range) would need Selberg-type mean values; Lemma 20 requires $H\ge4$ and an absolute $A\ge16$ - these constants are the explicit loss to an effective proportion.
- **Generalizations.** The sign-change criterion $|\int_I X|<\int_I|X|$ extends to Hardy $Z$-functions of Dirichlet $L$-functions (Hardy-Littlewood 1921 method applied to characters), to Epstein/Hecke L-functions with real-valued $Z$, and to the $a$-points of $\Lambda$ derivatives; a modern test case is the Lemma 11 analogue for degree-2 $L$-functions where $\int_T^{2T}|\int_t^{t+H}Z|^2dt\ll HT$ requires only mean-square bounds.
- **Candidate connections.** Lemma 18 and the orthogonality (6.3) are early forms of the second moment of $\int_t^{t+H}Z$, now treated by Montgomery pair correlation; the sharp $(\sin(\tfrac12H\log n)/\log n)^2$ kernel in (2.761) is exactly the Fourier transform appearing in Montgomery's $F(\alpha)$ with $H$ playing the role of $2\pi\alpha$-window, suggesting a unified view of HL, Selberg, Levinson via mollified moments of $\int Z$.
- **Reusable lemmas.** Lemma 1 (Cramer's exact formula), Lemma 12 (first-derivative test for $\int_\xi^\infty u^{-\sigma}e^{iu\pm it\log u}du$), Lemma 16 (stationary-phase-free exponent integral), Lemma 5/6 (double-sum bound $\sum 1/(\sqrt{mn}|\log(m/n)|)=O(\mu\log\mu)$, the Montgomery-Vaughan precursor).
- **Possible experiments.** (1) Numerically compute $\int_T^{T+U}I(t,H)^2dt/(HU)$ for $T\sim10^6$ - $10^{10}$ and $H\in\{4,\dots,50\}$ to check the constant in Lemma 18 (which I could not independently verify from the scan) against $\pi\sqrt{2\pi}$-type predictions; (2) Compute the fraction of length-$H$ blocks where $|I|<\underline I$ to see how sharp the Thm A criterion is versus the actual zero density $\approx\frac{\log T}{2\pi}H$; (3) make the HL argument effective to extract an explicit $K$ (they never do), compare with Selberg's $\ge 1/10$-ish estimate quoted by Selberg himself.
- **Risks / barriers.** HL block criterion inherently cannot beat $O(1)$ zeros per block of length $H$ while the true density is $\log T/2\pi$, so the method plateaus at $N_0\gg T$; Sec. 6.2 shows the mean-square of $|\int\zeta|$ is half that of $I$ for small $H$, which is the structural barrier Selberg bypassed via mollification. No route to proportion 1 (needs Levinson-type stronger mollification and Conrey's 40.77%, 5/12).

## Audit notes (Level 1 reader)

Lemma 14 (the sharp approximate functional equation) is stated without proof ('reserve the proof ... for publication elsewhere', p. 301); only the weaker Lemma 15 with extra $\log t$ is proved and used. Page-ordered proof of Lemmas 18-19 (pp. 305-312) was only skimmed. Constant in Lemma 18 read from a low-resolution scan; consider verifying against Titchmarsh Ch. 10. Footnote/typography: in (2.82)-(2.87) the roles of $\underline I$ (underlined) vs $I$ are visually distinct only by underline in the scan; Baas 2011 (secondary) dates the paper '1922' whereas the volume is 1921 (received 14 Oct 1920). Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00072`; harvest queries: msc_11M26.
- Triage decision: include — Hardy-Littlewood 1921 proof of positive-order count of zeros on critical line.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.

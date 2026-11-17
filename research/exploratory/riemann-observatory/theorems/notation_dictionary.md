# Normalization and notation dictionary for the Riemann Observatory

```text
Status:  Exploration-layer reference. It is NOT a review approval, NOT an integrated packet, and certifies no
         mathematical claim. RH remains open. Where a convention is attributed to a source, the attribution is
         tagged with the evidence level in Section 0.
Scope:   Normalizations, alternative conventions, exact conversion formulas and common pitfalls for the objects
         that recur across the 1000-work corpus: zeta/xi/Xi, Z(t), theta(t), S(t), N(T), N_0(T), N(sigma,T),
         kappa and kappa*, the de Bruijn-Newman constant Lambda and the heat flow H_t, Li coefficients,
         the Weil functional, Nyman-Beurling distances, Robin/Lagarias/Nicolas quantities, pair correlation,
         Montgomery-Odlyzko gap constants, Lindelof and zero-density exponents, Selberg-class data, and the
         Hecke/cubic-residue/Kubota apparatus of the 2026 quasi-RH papers. Definitions and conversions only;
         no new theorem is claimed.
Exact sources or dependencies:
         Textbooks (cited by author, no section numbers unless stated): Titchmarsh (ed. Heath-Brown 1986),
         Edwards 1974, Davenport (PAPER-0383), Iwaniec-Kowalski 2004, Ireland-Rosen (2nd ed.), Ivic 1985,
         Kaczorowski-Perelli (PAPER-0300, 0301, 0307, 0123). Corpus works named by PAPER id. Level-1 statements
         from theorems/theorems.jsonl; frontier records from frontiers/records_ledger.md (LED-* ids);
         audits/quasi_rh/{DOSSIER,ARCHITECTURE,audit_S6,audit_APPA}.md; history/recent_developments_2024_2026.md.
What was actually run:
         A scratch mpmath/Python session (python3 -I; not archived in the repository) that checked the formulas
         marked [V] below (Section 16 lists them with outputs). Everything marked [T] is quoted from a textbook
         or paper and was not re-derived; everything marked [D] is a short derivation done while writing this
         file. No Lean was built, no OpenAI code was run.
Smallest remaining gap:
         (a) Textbook section numbers are deliberately omitted and several [T] items are quoted from memory of
         the literature; they should be re-read against the primary source before being used in a proof.
         (b) The exact printed normalizations of Li 1997 and Keiper 1992 were not opened (PAPER-0224 and the Li
         paper are L0 records in this corpus); the Keiper-versus-Li conversion below rests on the ledger entries
         LED-POS-1/LED-POS-4 and on direct numerical checks [V].
         (c) The cubic-theta normalization rests on audit reports of AI-generated work plus Dunn-Radziwill as
         transcribed there; it was not re-derived.
```

---

## 0. How to read this file

Evidence tags used on individual statements:

| Tag | Meaning |
|---|---|
| [T] | Standard textbook or refereed-paper statement, quoted, not re-derived here. |
| [D] | Derived in this file from earlier items (short derivation shown or evident). |
| [V] | Verified numerically in the scratch session of Section 16 (finite precision; an identity check, not a proof). |
| [L] | Taken from a Level-1 theorem record (THM-PAPER-xxxx) or a ledger entry (LED-*); inherits that record's scope. |
| [U] | Unrefereed human preprint. |
| [AI] | Unrefereed AI-generated or AI-audited material (OpenAI 2026 quasi-RH papers, Observatory AI audits). |

Each section has: **Definition**, **Alternative normalizations and conversions**, **Pitfalls**.
Throughout, $s=\sigma+it$, $\rho=\beta+i\gamma$ is a non-trivial zero, $\gamma_n$ the ordinate of the $n$-th zero with $\gamma_1=14.134725\ldots$, $N(T)\sim\frac{T}{2\pi}\log T$.

---

## 1. Zeta, completed zeta, xi, Xi

### 1.1 Definitions

Let $\Gamma_{\mathbb R}(s)=\pi^{-s/2}\Gamma(s/2)$. Four objects are in circulation.

| Name | Formula | Normalization facts |
|---|---|---|
| $\Lambda(s)$ (completed zeta) | $\Gamma_{\mathbb R}(s)\zeta(s)$ | $\Lambda(s)=\Lambda(1-s)$; simple poles at $s=1$ (residue $1$) and $s=0$ (residue $-1$). [T] |
| $\xi(s)$ (Riemann, Landau, Edwards, most modern surveys) | $\tfrac12 s(s-1)\Gamma_{\mathbb R}(s)\zeta(s)$ | Entire of order 1, $\xi(s)=\xi(1-s)$, $\xi(0)=\xi(1)=\tfrac12$. [T] |
| $\xi_2(s)=2\xi(s)$ (Bombieri-Lagarias, Lagarias for $L(s,\pi)$, Keiper-Li work) | $s(s-1)\Gamma_{\mathbb R}(s)\zeta(s)$ | $\xi_2(0)=\xi_2(1)=1$. This is the $\xi(s,\pi)=[s(s-1)]^{\delta(\pi)}\Lambda(s,\pi)$ of PAPER-0039 specialized to $\pi=1$. [L: THM-PAPER-0039-1,-4] |
| $\Xi(t)$ | $\xi(\tfrac12+it)$ | Even, real, entire in $t$; zeros at $t=\pm\gamma$. [T] |

Explicit form [D]: since $s(s-1)=-(t^2+\tfrac14)$ at $s=\tfrac12+it$,
$$\Xi(t)=-\tfrac12\left(t^2+\tfrac14\right)\Gamma_{\mathbb R}(\tfrac12+it)\,\zeta(\tfrac12+it)
=-\tfrac12\left(t^2+\tfrac14\right)\pi^{-1/4}\bigl|\Gamma(\tfrac14+\tfrac{it}2)\bigr|\,Z(t),$$
with $Z$ as in Section 2. [V: $\Xi(0)=\xi(1/2)=0.497120778188\ldots$ is reproduced by the second form with $Z(0)=\zeta(1/2)=-1.4603545\ldots$.]

Functional equation in asymmetric form [T]: $\zeta(s)=\chi(s)\zeta(1-s)$ with $\chi(s)=2^s\pi^{s-1}\sin(\pi s/2)\Gamma(1-s)$; on the critical line $\chi(\tfrac12+it)=e^{-2i\theta(t)}$ [D from $Z$ real].

### 1.2 The Polymath/Rodgers-Tao function $H_0$

$H_0(z)=\int_0^\infty\Phi(u)\cos(zu)\,du$, $\Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}}$ (PAPER-0036 THM-PAPER-0036-1; PAPER-0083). Then
$$H_0(z)=\tfrac18\,\xi\!\left(\tfrac12+\tfrac{iz}{2}\right)=\tfrac18\,\Xi(z/2).\qquad[\text{V}]$$
Numerically $H_0(0)=0.062140097273\ldots$, $\xi(1/2)=0.497120778188\ldots$, ratio $8.0000000000000008$; same ratio at $z=1.3$. The ledger (LED-DBN-1) states the same identity. Zeros of $H_0$ sit at $z=\pm2\gamma$.

### 1.3 Pitfalls

1. **Which $\xi$.** $\xi$ versus $2\xi=\xi_2$: harmless for $\lambda_n$ (Section 5) because $\log$ of a constant multiple is shifted by a constant that the Li operator kills; harmful for any statement about values, e.g. $H_0=\xi/8$ versus $\xi_2/16$.
2. **Riemann's $\xi(t)$ is a function of $t$**, not of $s$ (Riemann 1859 writes $\xi(t)$ for what is $\Xi(t)$ here, Titchmarsh uses $\Xi$ for it). Edwards writes $\xi(s)$ as above.
3. **$\Lambda$ clashes.** $\Lambda(s)$ is completed zeta here, $\Lambda(n)$ is von Mangoldt, $\Lambda$ is the de Bruijn-Newman constant, and $\Lambda$ (capital) is also used for $\limsup$ of normalized gaps (LED-SPACING-13). Context must decide; in this archive the dBN constant is always written $\Lambda_{\rm dBN}$ in mixed text.
4. **Variable $z$ versus $t$ versus $x$.** $H_0(z)$ has zeros at $2\gamma$, $\Xi(t)$ at $\gamma$. See Section 4 for the consequences for heat-flow time.

---

## 2. Hardy's $Z(t)$, $\theta(t)$, Gram points, $S(t)$, $N(T)$, $N_0(T)$, $N(\sigma,T)$

### 2.1 $\theta$ and $Z$

$$\theta(t)=\operatorname{Im}\log\Gamma\!\left(\tfrac14+\tfrac{it}2\right)-\tfrac t2\log\pi,\qquad Z(t)=e^{i\theta(t)}\zeta(\tfrac12+it).$$
$Z$ is real, even, with $|Z(t)|=|\zeta(\tfrac12+it)|$ (Hardy 1914) [T]; reality confirmed numerically at $t=30$ (imaginary part $-4\times10^{-26}$) [V]. $\theta$ is odd, increasing for $t\gtrsim6.29$ with a minimum $\approx-3.53$ there [V: $\theta(14.134725)=-1.72867$, $\theta(g)=-\pi$ at $g=9.6669$].

Asymptotic expansion [T]: 
$$\theta(t)=\tfrac t2\log\tfrac t{2\pi}-\tfrac t2-\tfrac\pi8+\tfrac1{48t}+\tfrac7{5760t^3}+\cdots.$$
[V: at $t=20$ the three displayed terms differ from $\theta(20)$ by $1.2\times10^{-10}$; at $t=50$ by $1.2\times10^{-12}$.]

Naming: Edwards writes $\vartheta$ and calls it the Riemann-Siegel theta function; Titchmarsh writes $\vartheta(t)$; PAPER-0182 (Ivic, theory of $Z$) and PAPER-0188 (Gabcke) use $\vartheta$ or $\theta$. $\theta$ also denotes Chebyshev's $\theta(x)=\sum_{p\le x}\log p$, and $\theta$ is the exponent in mollifier length $y=T^\theta$ (LED-CRIT-7) and the zero-free exponent in quasi-RH. Disambiguate in text.

### 2.2 Riemann-Siegel formula and its parameters

$Z(t)=2\sum_{n\le m}n^{-1/2}\cos(\theta(t)-t\log n)+R(t)$, $m=\lfloor\sqrt{t/2\pi}\rfloor$, $R(t)=(-1)^{m-1}(t/2\pi)^{-1/4}\bigl[C_0(p)+C_1(p)(t/2\pi)^{-1/2}+\cdots\bigr]$, $p=\sqrt{t/2\pi}-m$, $C_0(p)=\cos(2\pi(p^2-p-\tfrac1{16}))/\cos(2\pi p)$ [T: Edwards; effective error bounds in PAPER-0188 (Gabcke 1979); high-precision implementation in PAPER-0760].

Conversion to the Polymath scale [D]: they use $N=\lfloor\sqrt{x/4\pi+t/16}\rfloor$ for $H_t(x+iy)$ (THM-PAPER-0083-3). With $x=2\tau$ and $t=0$, $\sqrt{x/4\pi}=\sqrt{\tau/2\pi}$, so the cutoff $m$ above is reproduced. The term $t/16$ is the heat-flow correction (Section 4).

### 2.3 Gram points

Definition: $g_n$ is the unique solution $>6.29$ of $\theta(g_n)=n\pi$, $n\ge-1$. [V] $g_{-1}=9.666908$, $g_0=17.845600$, $g_1=23.170283$ (and $\theta=-\pi$ also at $3.436218$, which lies on the decreasing branch and is not indexed). Gram's law: $(-1)^nZ(g_n)>0$ [T]. It is equivalent to $S(g_n)=0$ in the sense below [D from $N=\theta/\pi+1+S$ at $T=g_n$: $N(g_n)=n+1+S(g_n)$].

Index relation [D from data above]: $\gamma_1=14.1347\in[g_{-1},g_0)$, so $\gamma_{n+2}\in[g_n,g_{n+1})$ is the *expected* location, and $N(g_n)=n+1$ when Gram's law holds.

Pitfall: some authors index so that $\theta(g_n)=(n-1)\pi$ or start at $g_0=9.667$. Test: the convention is Edwards/Haselgrove/Brent's if $g_0=17.8456$ and the first violation of Gram's law is at $g_{126}$ (Hutchinson 1925; quoted from memory, [T] unchecked). Studies of the success rate: PAPER-0608 (Trudgian), PAPER-0654 and PAPER-0987 (Korolev). Rosser's rule is a refinement on blocks of consecutive Gram intervals; the "bad Gram point" terminology is relative to this index.

### 2.4 $S(t)$, $N(T)$

$S(t)=\frac1\pi\arg\zeta(\tfrac12+it)$, the argument obtained by continuous variation along the broken line $2\to2+it\to\tfrac12+it$; at an ordinate of a zero take the average of the one-sided limits [T]. $S_1(t)=\int_0^tS(u)\,du$.
$$N(T)=\frac{\theta(T)}{\pi}+1+S(T)=\frac T{2\pi}\log\frac T{2\pi e}+\frac78+S(T)+O(T^{-1}),$$
with $N(T)=\#\{\rho:0<\gamma\le T\}$, zeros counted with multiplicity (average at an ordinate) [T]. The middle equality is [D] from the $\theta$-expansion in 2.1 ($-\tfrac18+1=\tfrac78$).

Sample: $N(15)=1$ forces $S(15)=0.4345$ [V].

Bounds quoted in the corpus: under RH, $\lvert S(t)\rvert\le(\tfrac14+o(1))\frac{\log t}{\log\log t}$ and $-(\tfrac\pi{24}+o(1))\frac{\log t}{(\log\log t)^2}\le S_1(t)\le(\tfrac\pi{48}+o(1))\frac{\log t}{(\log\log t)^2}$ [L: THM-PAPER-0003-1,-2]. Unconditional explicit bounds on $N(T)-\frac T{2\pi}\log\frac T{2\pi e}$ with leading coefficient $0.10076\log T$ [L: LED-GROWTH-8; the earlier refereed constant $0.1038$ is LED-GROWTH-9]; $\lvert S\rvert\le2.5167$ for $T\le3.06\times10^{10}$ [L: LED-GROWTH-18].

### 2.5 Counting functions off the line, $N_0$, $N_d$, $\kappa,\kappa^*$

| Symbol | Definition | Note |
|---|---|---|
| $N(\sigma,T)$ | $\#\{\rho=\beta+i\gamma:\beta\ge\sigma,\ 0<\gamma\le T\}$ (Titchmarsh-Ivic style) | Variants: $\beta>\sigma$; $0\le\gamma\le T$ (Maynard-Pratt PAPER-0096, THM-PAPER-0096-1); $\lvert\gamma\rvert\le T$ (factor 2); $0<\gamma<T$ and $\sigma<\beta<1$ (Kadiri-Lumley-Ng PAPER-0037 per LED-ZDE-15). |
| $N_0(T)$ | zeros $\tfrac12+i\gamma$, $0<\gamma\le T$, with multiplicity | RH iff $N_0(T)=N(T)$ for all $T$. |
| $N_0^*(T)$, $N_0^s(T)$ | simple zeros on the line | Same object under two names (PAPER-0034 uses $N_0^*$, PAPER-0053 and the AF/BGST literature use $N_0^s$). |
| $N^*(T)$ | $\sum_{0<\gamma\le T}m_\gamma$ is **not** this: see pitfall 2 | Montgomery's $N^*(T)=\sum m_\gamma$, hence $N^*=N$ with multiplicity (PAPER-0043 THM-PAPER-0043-8 writes $N^*(T)=\sum_{0<\gamma\le T}m_\gamma$). |
| $N_d(T)$ | distinct zeros | $N_d\le N$. |
| $N_{s}(T)$ | simple zeros anywhere in the strip | $N_s\ge N_0^s$. |
| $\kappa$ | $\liminf_{T\to\infty}N_0(T)/N(T)$ | PAPER-0034: $\kappa\ge0.4105$. |
| $\kappa^*$ | $\liminf N_0^*(T)/N(T)$ | PAPER-0034: $\kappa^*\ge0.4058$. |

Records [L]: refereed unconditional $\kappa\ge0.417293962$, $\kappa^*\ge0.407511457$ (PRZZ, PAPER-0045, LED-CRIT-4; the AF/LZ literature sometimes writes "5/12" as the previous record). Unrefereed or AI-discovered: $\kappa^*\ge2/3$ and $0.6725007\ldots$ (Montgomery-Taylor window) with $N_d/N\ge5/6$ (Alpoge-Furman, arXiv 2608.13637, proof "discovered autonomously by Claude", Lean claimed; independent re-proof by Lamzouri), refinements to $0.67353820$ (LED-CRIT-1..3; history/recent_developments_2024_2026.md Section 4.2). These are [U]/[AI] until refereed and are *not* a statement that RH is near.

### 2.6 Pitfalls

1. **$N_0$ clash.** In the proportion literature $N_0(T)$ is critical-line zeros of $\zeta$; in de Bruijn-Newman literature $N_t(T)$ at $t=0$ counts *all* zeros of $H_0$ in $[0,T]$ in the $z$-scale (Section 4). Not the same function.
2. **Which star.** $\kappa^*$ (simple critical) versus $N^*(T)=\sum m_\gamma$ (all zeros with multiplicity) versus $N^*_\Phi$ in the Dirichlet-family theorem THM-PAPER-0043-9. Always restate.
3. **Normalization of $N(T)$ in proportions.** A proportion "of the zeros up to $T$" divides by $N(T)$; "of zeros in $[T,2T]$" divides by $N(2T)-N(T)$. The $\liminf$ values coincide for the Levinson-Conrey method, but BGST-type statements are stated on $(T,2T]$.
4. **Multiplicity.** $\kappa$ counts with multiplicity, $\kappa^*$ does not; $\kappa^*\le\kappa$ in the same normalization.
5. **Height-$H$ verification** ($H=3\,000\,175\,332\,800$, PAPER-0001, THM-PAPER-0001-1) is a statement about $\gamma\le H$, not a $\kappa$-type statement in the limit.

---

## 3. $\kappa$ and $\kappa^*$ in the Levinson-Conrey language (conversion data)

Reduction [L: THM-PAPER-0034-2]: with $V(s)=Q(-\frac1L\frac d{ds})\zeta(s)$, $Q(0)=1$, $L=\log T$, $\sigma_0=\tfrac12-\tfrac RL$ and mollifier $\psi$ of length $y=T^\theta$,
$$\kappa\ge1-\frac1R\log\!\Bigl(\frac1T\int_1^T\lvert V\psi(\sigma_0+it)\rvert^2dt\Bigr)+o(1).$$
Quoted parameters: Conrey $\theta=4/7$; PRZZ $\theta=4/7-\epsilon$, $R=1.3036$ for $\kappa\ge0.417293962$ (THM-PAPER-0045-1). Conversion between "$R$" conventions: some papers use $\sigma_0=\tfrac12-R/L$, others $\tfrac12-R/\log T$ with $\log T$ replaced by $\log(T/2\pi)$; these differ by lower order and do not change the limit constants. $\theta$ here is the mollifier exponent, not Chebyshev $\theta$.

---

## 4. The de Bruijn-Newman constant $\Lambda$ and the heat flow $H_t$

### 4.1 Definition (Polymath/Rodgers-Tao normalization)

$$H_t(z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,\qquad \partial_tH_t=-\partial_z^2H_t.$$
$\Lambda=\Lambda_{\rm dBN}$ is the unique real number such that all zeros of $H_t$ are real iff $t\ge\Lambda$ (PAPER-0036 THM-PAPER-0036-1; LED-DBN-1). Known: $0\le\Lambda\le0.2$ (Rodgers-Tao, PAPER-0036; upper bound Platt-Trudgian PAPER-0001 THM-PAPER-0001-3 via Polymath PAPER-0083); so **RH iff $\Lambda=0$** [L: LED-DBN-6]. $\Lambda\le0.22$ is Polymath's own statement (THM-PAPER-0083-1). Further bounds ($0.149\ldots$ and below) are [U], and bounds under the hypothesis "no zeros with $\Re s>7/8$" ($0.13963$, $0.1079\ldots$) are conditional on an [AI] claim (LED-DBN-15).

Zero dynamics [L: THM-PAPER-0036-4, THM-PAPER-0083-L1]: for real simple zeros, $\dot x_k=2\sum_{j\ne k}\frac1{x_k-x_j}$ (principal value). [D check: from $H_t(z(t))=0$ and $\partial_tH=-H''$, $\dot z=H''/H'=2\sum_{j\ne k}1/(z_k-z_j)$ at a real simple zero.]

Zero counting at time $t$ [L: THM-PAPER-0083-5]: $g(x,t)=\frac x{4\pi}\log\frac x{4\pi}-\frac x{4\pi}+\frac{11}8+\frac t{16}\log\frac x{4\pi}$, $N_t(X)=g(X,t)+O(1)$ (for large $X$) where $N_t(X)$ counts zeros of $H_t$ in $[0,X]$ in the $z$-scale.

### 4.2 Alternative time and space scalings

The **Titchmarsh-variable** family is $\Xi_\lambda(x)=\int_0^\infty e^{\lambda v^2}\Phi_T(v)\cos(xv)\,dv$ with $\Phi_T(v)=\Phi(v/2)=\sum(2\pi^2n^4e^{9v/2}-3\pi n^2e^{5v/2})e^{-\pi n^2e^{2v}}$ [T: Titchmarsh's $\Phi$]. Substituting $v=2u$, $x=z/2$ [D]:
$$H_t(2x)=\tfrac12\,\Xi_{\lambda}(x)\ \text{ with } t=4\lambda,\qquad\Lambda_{\rm dBN}^{\,z\text{-scale}}=4\,\Lambda^{\,x\text{-scale}}.$$
The factor-of-4 conversion is a derivation here, not a quotation. [D check on the motion of zeros: $dx/d\lambda=2\sum 1/(x-x_j)$ in the $x$-scale and $dz/dt=2\sum 1/(z-z_j)$ in the $z$-scale, consistent with $z=2x$, $t=4\lambda$.]

Further conventions in the literature (not verified): Newman 1976 and de Bruijn 1950 are quoted with "$\Lambda\le\tfrac12$"; the Polymath/ledger normalization above has $\Lambda\le\tfrac12$ (LED-DBN-1), so the $z$-scale is the Newman scale. If any source states the bound in the Titchmarsh variable, multiply by 4 to compare. For Dirichlet and Selberg-class analogues $\Lambda_L$, $\Lambda_F$ (PAPER-0333: $\Lambda_F\ge0$ for $F$ in the extended Selberg class; LED-DBN-7, LED-DBN-17) the normalizing gamma factor changes the scale; always restate the kernel.

### 4.3 Pitfalls

1. **$z$ versus $\gamma$.** A Lehmer pair at ordinates $\gamma,\gamma'$ is a pair at $2\gamma,2\gamma'$ for $H_0$; gap statements transform as $\Delta z=2\Delta\gamma$. Polymath's $N_t$ counts in $z$, so $N_0(X)=N(X/2)$ up to boundary conventions.
2. **The constant $11/8$ versus $7/8$** [D]: $g(x,0)=N_{\rm smooth}(x/2)+\tfrac12$ with $N_{\rm smooth}(T)=\frac T{2\pi}\log\frac T{2\pi e}+\frac78$, so $g(x_n)=n$ places the $n$-th zero where the smooth count equals $n-\tfrac12$ (midpoint of the jump). It is an index convention, not a discrepancy.
3. **Time scaling of "$e^{t u^2}$ versus $e^{-tu^2}$"** is not interchangeable: $t>0$ is the *forward* direction for reality of zeros (backward heat equation in $z$).
4. **Zero-free half-planes and $\Lambda$:** de Bruijn's strip contraction gives $\Lambda\le\Delta^2/2$ if all zeros of $H_0$ lie in $\lvert\Im z\rvert\le\Delta$ (LED-DBN-2). A half-plane $\Re s\le7/8$ gives $\Delta=\tfrac14\cdot2\cdot\ldots$: do not recompute by hand from the $s$-plane; use the $z$-scale relation $\Im z=2(\Re s-\tfrac12)\cdot\ldots$ carefully. (Explicitly, $s=\tfrac12+iz/2$ gives $\Im z=2(\tfrac12-\Re s)\cdot(-1)$, i.e. $\lvert\Im z\rvert=2(\Re s-\tfrac12)$; for $\Re s\le7/8$, $\Delta=\tfrac34$ and the hypothesis-only bound is a function of $\Delta^2/2$ and the barrier method; the ledger's initial strip "$M(0)\le9/16$" is $\Delta^2=(3/4)^2$.) [D]

---

## 5. Li (Keiper-Li) coefficients $\lambda_n$

### 5.1 Definitions

Li's coefficients [T; used in PAPER-0039, PAPER-0005, PAPER-0195]:
$$\lambda_n=\sum_\rho\Bigl[1-\bigl(1-\tfrac1\rho\bigr)^n\Bigr]=\frac1{(n-1)!}\frac{d^n}{ds^n}\bigl[s^{n-1}\log\xi(s)\bigr]_{s=1},\qquad n\ge1,$$
the sum over zeros of $\xi$ paired as $\rho,\bar\rho$ or taken as $\lim_{T}\sum_{\lvert\rho\rvert\le T}$ (the "$*$-convergent" sum of PAPER-0039, THM-PAPER-0039-1). The second form is insensitive to a constant factor in $\xi$ because $\deg s^{n-1}<n$ (so $\xi$ versus $\xi_2$ is irrelevant) [D].

Generating function [V; D]: with $z=1-1/s$,
$$\frac{d}{dz}\log\xi\!\Bigl(\frac1{1-z}\Bigr)=\sum_{n\ge1}\lambda_nz^{n-1},\qquad\log\frac{\xi(1/(1-z))}{\xi(1)}=\sum_{n\ge1}\frac{\lambda_n}{n}z^n.$$
Numerically the Taylor coefficients of $\log\xi(1/(1-z))$ at $z=0$ are $-0.693147$ (that is $\log\frac12$), $0.0230952$, $0.0461720$, $0.0692119$, $0.0921965$, $0.1151077$, i.e. $\lambda_n/n$ with $\lambda_1=0.0231$, $\lambda_2=0.0923$, $\lambda_3=0.2076$, $\lambda_4=0.3688$, $\lambda_5=0.5755$ (finite-difference accuracy about $10^{-6}$) [V]. Closed form [T]: $\lambda_1=1+\tfrac\gamma2-\tfrac12\log4\pi=0.0230957\ldots$ [V: $0.02309571$].

Under RH, $\lvert1-1/\rho\rvert=1$ and each term is $1-\cos(n\phi_\rho)$ for $\rho=\tfrac12\pm i\tau$ [D; this is the content of THM-PAPER-0005-L1]. Li's criterion [L: THM-PAPER-0039-2 (Bombieri-Lagarias form)]: RH iff $\Re\lambda_n\ge0$ for all $n\ge1$.

### 5.2 The three normalizations in use

| Convention | Definition | Relation to Li's $\lambda_n$ |
|---|---|---|
| **Li (1997), Bombieri-Lagarias (PAPER-0195), Lagarias (PAPER-0039), Voros (PAPER-0005), Brown (PAPER-0600)** | $\lambda_n=\sum_\rho[1-(1-1/\rho)^n]$ | identity; BL extend to all $n\in\mathbb Z$ with $\lambda_{-n}=\lambda_n$ (THM-PAPER-0039-1) and $\lambda_0=0$ |
| **Keiper (1992, PAPER-0224) as used by Johansson (LED-POS-1) and Arias de Reyna (PAPER-0316; LED-POS-4)** | $\log\bigl(2\xi(1/s)\bigr)=\sum_n\lambda_n^{K}(1-s)^n$ | $\lambda_n^{K}=\lambda_n^{\rm Li}/n$ [V; consistent with LED-POS-1: $\lambda^K_{100000}=4.6258\ldots$, Li normalization $\approx4.6258\times10^5$] |
| **Derivative (shifted) form** | $\sum_{n\ge0}\mu_nz^n=\frac d{dz}\log\xi(\frac1{1-z})$ | $\mu_n=\lambda_{n+1}^{\rm Li}$ (index shift by one) |

Voros's sums [L: THM-PAPER-0005-1]: $\lambda_n=-n\sum_{j=1}^n(-1)^j\frac1j\binom{n+j-1}{2j-1}Z(j)$ with $Z(\sigma)=\sum_kx_k^{-\sigma}$, $x_k=\rho_k(1-\rho_k)=\tfrac14+\tau_k^2$, the sum over zero **pairs** $\tfrac12\pm i\tau_k$ (one term per pair). Check at $n=1$: $\lambda_1=Z(1)=\sum_{\tau>0}\frac1{1/4+\tau^2}=\sum_\rho\frac1\rho$ [D].

Link to the Nicolas/Nyman-Beurling constant [D]: always $\sum_\rho\Re\frac1\rho=\lambda_1$. Under RH, $\lvert\rho\rvert^{-2}=2\Re(1/\rho)$, so $\sum_\rho\lvert\rho\rvert^{-2}=2\lambda_1=2+\gamma-\log4\pi=0.0461914\ldots$ — the constant "$\beta$" of Section 8 and the constant in Section 7 (matches the ledger statement "under RH $\sum m(\rho)/\lvert\rho\rvert^2=2+\gamma-\log4\pi$", LED-POS-16, when zeros are simple).

Asymptotics [L]: under RH $\lambda_n=\frac n2(\log n+\gamma-1-\log2\pi)+O(\sqrt n\log n)$ (Lagarias, THM-PAPER-0039-7 and LED-POS-3); the constant $(\gamma-1-\log2\pi)/2=-1.13033\ldots$ is quoted in LED-POS-3. In Keiper normalization, $\lambda_n^K\approx\frac12(\log n+\gamma-\log2\pi e)$ and with $y_n=\lambda^K_n-\frac12(\log n+\gamma-\log 2\pi e)$: RH iff $\sum y_n^2<\infty$ (Arias de Reyna 2011, via LED-POS-4, secondary source) and RH iff $y_n=o(1)$ in the sense of Voros (PAPER-0005 THM-PAPER-0005-5, written there as $n y_n=o(n)$). If RH fails, $\lambda_n\sim\sum_{\lvert z_\rho\rvert<1}z_\rho^{-n}+\mathrm{c.c.}$ with $z_\rho=(\rho-1)/\rho$-type points, giving exponentially growing oscillations (THM-PAPER-0005-3). Rigorous positivity: $\lambda_n>0$ for $1\le n\le10^5$ (Johansson, LED-POS-1); semi-local: $\lambda_n\ge0$ for $n\le T_0^2$ once RH is verified to height $T_0$ (Oesterle, via Voros, LED-POS-2; with $T_0=3\times10^{12}$ this is a derived value, not stated in any source).

Arithmetic formula for general $L(s,\pi)$ [L: THM-PAPER-0039-4]: $\lambda_n(\pi)=S_\infty(n,\pi^\vee)-S_f(n,\pi^\vee)+\delta(\pi)$ with $\delta(\pi)=1$ iff $\pi$ is trivial (pole), where the Li sum is over zeros of $\xi(s,\pi)=[s(s-1)]^{\delta(\pi)}\Lambda(s,\pi)$. Weil scalar product: $\langle G_n,G_m\rangle_W=\lambda_n+\lambda_{-m}-\lambda_{n-m}$ and $\lVert G_n\rVert_W^2=2\Re\lambda_n$ for $G_n(s)=1-(1-1/s)^n$ (THM-PAPER-0039-3). For Selberg-class variants (Omar-Mazhouda, PAPER-0974, PAPER-0992) and for function fields (PAPER-0942) the zeros considered are those of the appropriate $\xi$; check whether the pole-term $\delta$ is included.

### 5.3 Pitfalls

1. **The $1/n$ factor.** "$\lambda_{100000}=4.6258$" (Keiper) versus $\approx4.6\times10^5$ (Li). Always say which.
2. **Index shifts.** $\lambda_n$ ($n\ge1$) versus $\mu_n=\lambda_{n+1}$ versus a $\lambda_0$ that some authors include (BL: $\lambda_0=0$; Johansson computes $\lambda_0,\dots,\lambda_n$). The first nonzero value is $\lambda_1=0.0231$ in Li indexing.
3. **Variable change direction.** $s\mapsto1/(1-z)$ (Keiper-Li, $z=0\leftrightarrow s=1$) versus $s\mapsto1/s$ (the form $\log2\xi(1/s)=\sum\lambda_n^K(1-s)^n$, $s=1\leftrightarrow$ origin): these are the same map under $s\to1-z$ relabeling; check the center.
4. **Multiplicity and pairing.** The sum over zeros is conditionally convergent; the symmetric pairing $\rho,\bar\rho$ or truncation $\lvert\rho\rvert\le T$ is part of the definition (THM-PAPER-0039-1). Summing over $\gamma>0$ only gives $\tfrac12\lambda_n$ when RH holds? No: it gives half only for the real part; do not do this without a pairing argument.
5. **Strictness.** The criterion is $\ge0$; under RH all $\lambda_n>0$ in the cases computed. Do not write "RH iff $\lambda_n>0$" without checking the source.
6. **Dependence on $\xi$ versus $\Lambda$.** For $\zeta$ the Li sum runs over zeros of $\xi$ (so the poles of $\Lambda$ at $0,1$ are cancelled). Using $\Lambda$ instead changes $\lambda_n$ by the pole contributions, i.e. by $\delta(\pi)=1$-type terms.

---

## 6. The Weil functional and its sign conventions

### 6.1 Three equivalent presentations

**(W1) Additive form.** For even, sufficiently decaying $h$ analytic in $\lvert\Im r\rvert\le\tfrac12+\varepsilon$, $g(u)=\frac1{2\pi}\int h(r)e^{-iru}\,dr$, zeros $\rho=\tfrac12+i\gamma$:
$$\sum_\gamma h(\gamma)=h(\tfrac i2)+h(-\tfrac i2)-g(0)\log\pi+\frac1{2\pi}\int_{-\infty}^\infty h(r)\,\Re\psi\!\bigl(\tfrac14+\tfrac{ir}2\bigr)\,dr-2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\,g(\log n).$$
[T] ($\psi=\Gamma'/\Gamma$, $\Lambda$ von Mangoldt.) [V: $h(r)=e^{-r^2/50}$, $g(u)=\frac5{\sqrt{2\pi}}e^{-25u^2/2}$; the zero side from the first 40 zeros is $0.0370825835$ and the right-hand side (with $n<30$) is $0.0370825835$, agreeing to the printed digits.]

**(W2) Bombieri's multiplicative form** (PAPER-0090; THM-PAPER-0090-2). With Mellin transform $\hat f(s)=\int_0^\infty f(x)x^{s-1}dx$ and $f^*(x)=x^{-1}f(1/x)$,
$$T[f]=\int_0^\infty f+\int_0^\infty f^*-\sum_n\Lambda(n)\{f(n)+f^*(n)\}-(\log4\pi+\gamma)f(1)-\int_1^\infty\Bigl\{f+f^*-\tfrac2xf(1)\Bigr\}\frac{x\,dx}{x^2-1}=\sum_\rho\hat f(\rho).$$
RH iff $T[f*f^*]\ge0$ for every $f\in C_0^\infty((0,\infty))$ (strict positivity version for $f\not\equiv0$: Bombieri 2000, THM-PAPER-0090-1). Here $*$ is multiplicative convolution and, for complex $f$, one needs the conjugate: $f^*(x)=x^{-1}\bar f(1/x)$ (then $\widehat{f*f^*}(\tfrac12+i\gamma)=\lvert\hat f(\tfrac12+i\gamma)\rvert^2$) [D].

**(W3) Connes-Consani form** (PAPER-0099, PAPER-0119, PAPER-0125): Weil distribution $W=\sum_vW_v$ on $C_c^\infty(\mathbb R_+^*)$ with Haar measure $d^*x=dx/x$, $g^*(x)=\overline{g(x^{-1})}$, the archimedean part $W_\infty$ and pole terms, and the positivity $W(g*g^*)\ge0$. Results: for $g$ supported in $[2^{-1/2},2^{1/2}]$ with $\hat g(\pm\tfrac i2)$ vanishing, $W_\infty(g*g^*)\ge\operatorname{Tr}(\vartheta(g)S\vartheta(g)^*)\ge0$ (THM-PAPER-0099-1; no primes enter because $g*g^*$ has support in $(\tfrac12,2)$).

### 6.2 Conversions [D]

(i) **W2 to W1.** Put $F(u)=e^{u/2}f(e^u)$ and $h(r)=\hat f(\tfrac12+ir)=\int F(u)e^{iru}du$. Then $g=F$ in W1 and for $F$ even $f(n)+f^*(n)=2n^{-1/2}g(\log n)$, which is the prime term of W1; $\hat f(1)+\hat f(0)=h(-\tfrac i2)+h(\tfrac i2)$ [D from $\rho=1\leftrightarrow r=-\tfrac i2$]. The archimedean constants differ in form ($\log4\pi+\gamma$ plus an integral in W2; $\log\pi$ plus a digamma integral in W1); I checked W1 only [V]. 

(ii) **W2 to W3.** With $F(x)=x^{1/2}f(x)$ one has $F^*(x)=F(1/x)$ (real case), so Bombieri's $*$ becomes the plain inversion used by Connes-Consani with $d^*x$ Mellin transform; $\hat f(\tfrac12+it)=\int F(x)x^{it}d^*x$. [D]

(iii) **Windows.** Bombieri's small-support result: support of $F$ (log variable) of length $\lvert I\rvert<\log2$ gives $T[F*\bar F(-\cdot)]\ge(\log\frac1{\lvert I\rvert}-\log\log\frac1{\lvert I\rvert}-O(1))\lVert F\rVert^2$ (THM-PAPER-0090-8; extracted form garbled in the record). Connes-Consani: $g\in C_c^\infty[2^{-1/2},2^{1/2}]$, i.e. log half-width $\tfrac{\log2}2=0.3466$ and autocorrelation support $(\tfrac12,2)$ (LED-POS-6). A certified window containing prime powers $2,3,4$: log half-width $0.8$ (LED-POS-7, [U]); numerical ground state to $\lambda^2=300$ (LED-POS-8, [U]).

### 6.3 Pitfalls

1. **Which sign the prime and archimedean terms carry.** In the zero-side-positive convention above, $\sum_\rho\hat f(\rho)=$ (pole terms) $-$ (prime terms) $-$ (archimedean). Authors who write $W=$ "local terms" (Connes) are using the same functional if the pole terms are included with $+$ and the local terms are $-\sum_vW_v$; if one drops the overall minus one obtains a functional whose positivity statement is reversed. Check the sign of the $\Lambda(n)$ term in the displayed formula before comparing.
2. **Conjugation in $f^*$.** Bombieri's $f^*(x)=x^{-1}f(1/x)$ versus complex $f^*(x)=x^{-1}\bar f(1/x)$ versus Connes' $\overline{g(x^{-1})}$. Without the bar, $f*f^*$ gives $\hat f(s)\hat f(1-s)$, not $\lvert\hat f\rvert^2$ on the line.
3. **Mellin sign.** $x^{s-1}$ (Bombieri) versus $x^{-s}$; a flip exchanges $s\leftrightarrow1-s$, harmless for the full sum but not for a single zero.
4. **Multiplicities, and zeros off the line.** The identity $\sum\hat f(\rho)$ counts with multiplicity and includes all non-trivial zeros; positivity on the line is automatic, and the content of Weil's criterion is that a zero off the line forces negativity for suitable $f$ (Bombieri's Hermitian-matrix argument, THM-PAPER-0090-6,-7).
5. **Local versus global positivity.** A positive result on a bounded window (Section 6.2 (iii)) says nothing about RH; the analytic function $W$ on $C_c^\infty$ is *conditionally* positive. This is the exact point that the C4 campaign (Weil window locality) addresses.

---

## 7. Nyman-Beurling distances $d_N$

### 7.1 Definitions

$\rho(x)=x-\lfloor x\rfloor$ (fractional part; PAPER-0004 writes $\rho$ for this function, not for a zero), $\chi=\mathbf 1_{(0,1]}$. Beurling's variable: $\rho(\theta/x)$, $0<\theta\le1$. Báez-Duarte's discrete version: $\rho_a(x)=\rho(1/(ax))$, $a\in\mathbb N$, $B^{\rm nat}=\overline{\operatorname{span}}\{\rho_a\}$ in $L^2(0,\infty)$; **RH iff $\chi\in B^{\rm nat}$** [L: THM-PAPER-0004-1, PAPER-0273]. Maybe also: RH iff $f_{\epsilon,n}=\sum_{a\le n}\mu(a)a^{-\epsilon}\rho_a$ converges in $H$ for small $\epsilon>0$ (THM-PAPER-0004-2). Define
$$d_N^2=\inf_{c_1,\dots,c_N}\Bigl\lVert\chi-\sum_{k=1}^Nc_k\rho_k\Bigr\rVert^2.$$
Mellin-Plancherel form (the form used in the Hilbert-space literature; quoted from the literature on the pattern of Balazard-Saias, PAPER-0780, and Burnol, not re-derived here): $d_N^2=\inf_{A_N}\frac1{2\pi}\int\frac{\lvert1-\zeta A_N\rvert^2}{\lvert\tfrac12+it\rvert^2}\,dt$ over Dirichlet polynomials $A_N(s)=\sum_{k\le N}c_kk^{-s}$ evaluated at $s=\tfrac12+it$ [T, unverified]. Beurling-type continuous parameter: $D(\lambda)=\inf$ over $\theta_k\in[\lambda,1]$ (Burnol's $D(\lambda)$; LED-POS-16), a distance, not a squared distance.

### 7.2 Conversions and known facts

Heuristic correspondence between the two parameters: $N\leftrightarrow1/\lambda$ and $d_N^2\leftrightarrow D^2$; the bound in Burnol's form is $\liminf_{\lambda\to0}D(\lambda)\sqrt{\log(1/\lambda)}\ge\bigl(\sum_\rho m_\rho^2/\lvert\rho\rvert^2\bigr)^{1/2}$, i.e. in Báez-Duarte's discrete form $\liminf d_N^2\log N\ge\sum_\rho m(\rho)^2/\lvert\rho\rvert^2$, unconditionally and trivial if RH fails (LED-POS-16, citing Burnol and Báez-Duarte-Balazard-Landreau-Saias). Conditional asymptotic (Bettin-Conrey-Farmer, PAPER-0291, with an extra assumption on $\sum\lvert\zeta'(\rho)\rvert^{-2}$): $d_N^2\sim\frac{2+\gamma-\log4\pi}{\log N}\approx\frac{0.0462}{\log N}$ (LED-POS-16). The constant equals $2\lambda_1=\sum_\rho\lvert\rho\rvert^{-2}$ under RH with simple zeros [D from Section 5]; if zeros are multiple the lower bound has $m_\rho^2$ and the asymptotic needs the simple-zero hypothesis.

Related normalizations: the generalized criterion (Báez-Duarte, PAPER-0273; Alouges-Darses-Hillion, PAPER-0332; Hardy-space version PAPER-0638; Maier-Rassias explicit sums PAPER-0955; Bagchi PAPER-0561); Beurling's original in $L^p$ ($1<p<\infty$) with approximants $\sum c_k\rho(\theta_k/x)$, $\sum c_k\theta_k=0$ (needed in the $(0,\infty)$ setting so that the approximants decay at $\infty$).

### 7.3 Pitfalls

1. **Domain.** $L^2(0,1)$ (Nyman) versus $L^2(0,\infty)$ (Báez-Duarte). For $x>1$ every $\rho_a(x)=1/(ax)$, so tails matter in the second setting.
2. **$\rho$ clash.** Here $\rho(x)$ is fractional part; elsewhere $\rho$ is a zero.
3. **Squared versus unsquared distance** ($d_N^2$ versus $D(\lambda)$), and **$N$ as a number of terms versus a Dirichlet polynomial length** ($a_k$ supported on $k\le N$).
4. **A finite-$N$ computation is not an RH test.** $d_N\to0$ for all $N\to\infty$ is *equivalent* to RH; the rate $1/\sqrt{\log N}$ means numerics converge very slowly.

---

## 8. Robin, Lagarias and Nicolas quantities

### 8.1 Definitions

$\sigma(n)=\sum_{d\mid n}d$, $\sigma_{-1}(n)=\sigma(n)/n$, $H_n=\sum_{k\le n}1/k$, $\varphi$ Euler's totient, $N_k=\prod_{j\le k}p_j$ (primorial; $\log N_k=\theta(p_k)$ with $\theta$ Chebyshev).

| Criterion | Statement | Status |
|---|---|---|
| Robin 1984 (PAPER-0294 index record; PAPER-0079 annotated Ramanujan) | $\sigma(n)<e^\gamma n\log\log n$ for all $n>5040$ **iff** RH | [T]; unconditional: $\sigma(n)<e^\gamma n\log\log n+0.6483\,n/\log\log n$ for $n\ge3$ (PAPER-0294 record, recollection) |
| Lagarias 2002 | $\sigma(n)\le H_n+e^{H_n}\log H_n$ for all $n\ge1$ **iff** RH, equality only for $n=1$ | [L: LED-ARITH-5] |
| Nicolas 1983 | $N_k/\varphi(N_k)>e^\gamma\log\log N_k$ for every $k\ge1$ **iff** RH; if RH fails the inequality holds for infinitely many $k$ and fails for infinitely many $k$ | [L: LED-ARITH-6] |
| Caveney-Nicolas-Sondow | "Robin's theorem, primes, and a new elementary reformulation of RH" | PAPER-0274 (statement not transcribed here) |
| Odd-integer analogue (Washington-Yang, PAPER-0063) | RH iff $\sigma(n)/(n\log\log n)<e^\gamma/2$ for odd $n\ge c_0=18565284664427130919514350125$ | [L: THM-PAPER-0063-1] |
| Asymptotic version (Sole-Zhu, PAPER-0680; Luca-Sole, PAPER-0094) | density-zero exceptional set results | unconditional, see PAPER-0094 |

Robin's inequality fails for exactly the 27 integers known: $2,3,4,5,6,8,9,10,12,16,18,20,24,30,36,48,60,72,84,120,180,240,360,720,840,2520,5040$ (the ledger lists the 26 with $n=1$ and without $3$ and $720$, LED-ARITH-4; the 27-element set is that list with $1$ removed and $3,720$ added) [L, assembled here]. Verified: Robin's inequality holds for $5040<n\le10^{10^{13.11485}}$ (LED-ARITH-1); for all 21-free $n$ (LED-ARITH-2).

### 8.2 Conversions [D]

(i) $H_n=\log n+\gamma+\frac1{2n}-\cdots$, so $e^{H_n}\log H_n>e^\gamma n\log\log n$ for $n\ge3$ (LED-ARITH-5): Robin at $n$ implies Lagarias at $n$.

(ii) **Defect normalizations.** Nicolas's normalized defect $c(n)=\bigl(\frac n{\varphi(n)}-e^\gamma\log\log n\bigr)\sqrt{\log n}$ has, under RH, $\limsup c(n)=e^\gamma(2+\beta)=3.6444150964\ldots$, with $\beta=2+\gamma-\log4\pi=0.0461914179\ldots$ (LED-ARITH-6). By Section 5, $\beta=\sum_\rho\lvert\rho\rvert^{-2}=2\lambda_1$ under RH [D]. Ramanujan's corrected limsup (THM-PAPER-0079-1) $\limsup(\sigma_{-1}(n)-e^\gamma\log\log n)\sqrt{\log n}\le-e^\gamma(2\sqrt2-4-\gamma+\log4\pi)=-1.393\ldots$ can be rewritten $-e^\gamma(2\sqrt2-2-\beta)$ [D; $e^\gamma\cdot0.78218=1.3932$].

(iii) If RH fails there are $0<b<\tfrac12$, $c>0$ with $\sigma(N)\ge e^\gamma N\log\log N+cN\log\log N/(\log N)^b$ along infinitely many (odd, in PAPER-0063) colossally abundant $N$ (THM-PAPER-0063-L5; Robin).

### 8.3 Pitfalls

1. **Robin's constant.** "Robin's constant" has been used for $e^\gamma$ itself, for $0.6483\ldots$, and for the Robin function $G(n)=\sigma(n)/(n\log\log n)$. State the object.
2. **$n=1,2$.** $\log\log n$ is undefined or negative for $n\le2$; statements "for all $n\ge3$" versus "for $n>5040$" differ by the 27 exceptions.
3. **$\log\theta$ versus $\log$.** Nicolas-type inequalities at primorials use $\log\log N_k=\log\theta(p_k)$; replacing by $\log p_k$ gives an error comparable to the excess being tested (the verifier critique under LED-ARITH-1/-6 flags this).
4. **$t$-free, odd, squarefree, colossally abundant** each shift which statement is proved; do not quote "Robin holds for squarefree $n$" as "Robin holds for all $n$".

---

## 9. Pair correlation: $F(\alpha)$

### 9.1 Definition (Montgomery 1973, PAPER-0091)

Assume RH. For real $\alpha$ and $T\ge2$,
$$F(\alpha)=F(\alpha,T)=\Bigl(\frac T{2\pi}\log T\Bigr)^{-1}\sum_{0<\gamma,\gamma'\le T}T^{i\alpha(\gamma-\gamma')}w(\gamma-\gamma'),\qquad w(u)=\frac4{4+u^2}.$$
$F$ is real and even; $F(\alpha)\ge-\varepsilon$; for $0\le\alpha<1$, $F(\alpha)=(1+o(1))T^{-2\alpha}\log T+\alpha+o(1)$; conjecturally $F(\alpha)=1+o(1)$ for $\alpha\ge1$ (THM-PAPER-0091-1,-5; LED-SPACING-1). The pair-correlation conjecture is equivalent to
$\#\{\gamma,\gamma'\le T:\ 2\pi a/\log T\le\gamma-\gamma'\le2\pi b/\log T\}\sim\bigl(\int_a^b(1-(\tfrac{\sin\pi u}{\pi u})^2)du+\delta_{0\in[a,b]}\bigr)\frac T{2\pi}\log T$ (THM-PAPER-0091-5).

### 9.2 Alternative normalizations and conversions

1. **Unconditional extension** (Baluyot-Goldston-Suriajaya-Turnage-Butterbaugh, PAPER-0053; LED-SPACING-2): $F(x,T)=\sum x^{\rho-\rho'}w(\rho-\rho')$ with $w(u)=\frac4{4-u^2}$ and $F(\alpha)=(\frac T{2\pi}\log T)^{-1}F(T^\alpha,T)$. Under RH, $\rho-\rho'=i(\gamma-\gamma')$, so $4-u^2=4+(\gamma-\gamma')^2$ and the two definitions agree [D]. Unconditionally $F(\alpha)=T^{-2\alpha}(\log T+O(1))+\alpha+O((\log T)^{-1/2})$ for $0\le\alpha\le1$ (THM-PAPER-0053-1). 
2. **Fourier dictionary** [D]: put $u=(\gamma-\gamma')\frac{\log T}{2\pi}$ and $N=\frac T{2\pi}\log T$. Then $T^{i\alpha(\gamma-\gamma')}=e^{2\pi i\alpha u}$, so for $r(u)=\int\hat r(\alpha)e^{2\pi i\alpha u}d\alpha$,
$\sum_{\gamma,\gamma'}r(u_{\gamma\gamma'})w(\gamma-\gamma')=N\int\hat r(\alpha)F(\alpha)d\alpha.$
3. **GUE form factor.** The sine-kernel density $1-\operatorname{sinc}^2$ gives (diagonal included) $F(\alpha)\leftrightarrow\delta(\alpha)+\min(\lvert\alpha\rvert,1)$ [D from $\widehat{\operatorname{sinc}^2}=(1-\lvert\alpha\rvert)_+$], consistent with $F=\lvert\alpha\rvert$ on $[0,1)$ up to the $T^{-2\alpha}\log T$ delta-like term.
4. **Normalization by $\log T$ versus $\log(\gamma/2\pi)$** (local density). The two differ by $O(1/\log T)$ relative corrections and affect only lower-order terms; they never change a $\liminf$ or $\limsup$.
5. **Higher correlations.** Hejhal ($n=3$), Rudnick-Sarnak ($n\ge3$) (LED-SPACING-5): GUE agreement for Fourier support $\sum\lvert\xi_i\rvert<2$ under RH; the Alternative Hypothesis (gaps in $\tfrac12\mathbb Z_{\ge1}$) reproduces all of it (LED-SPACING-6).
6. **Sensitivity of $F$ and results.** Pair correlation without RH: 100% of zeros simple and critical *if* the pair-correlation conjecture is assumed (Goldston-Lee-Schettler-Suriajaya, via history/recent_developments Section 2; BGST Theorems 1-2 in LED-CRIT-13).
7. **Dirichlet families.** The analogue $F_\Phi(\alpha)$ with $Q\to\infty$ averaging (THM-PAPER-0043-9; PAPER-0431 Kandhil-Languasco).

### 9.3 Pitfalls

1. **$\alpha$ versus $\beta$.** $F(\alpha)$ uses $\alpha$ for the dual of normalized spacing; $\beta$ is a window half-width in Carneiro et al. (PAPER-0043), also $\beta$ for $\Re\rho$ elsewhere.
2. **$N(T,\beta)$ in PAPER-0043** counts pairs within $\beta$ mean spacings and is normalized by $N(T)$, not by $N(T)^2$.
3. **Weight $w$.** Montgomery's $w(u)=4/(4+u^2)$, others use $1/(1+u^2)$-type weights; the main term $\alpha$ is stated for the first.
4. **Diagonal term.** $\gamma=\gamma'$ contributes $1\cdot N$ to the sum, i.e. the $\delta(\alpha)$ in item 3; "$F(\alpha)\ge0$" holds including it.

---

## 10. Montgomery-Odlyzko gap constants $\mu$ and $\lambda$

### 10.1 Definitions

Normalized gaps $\delta_n=(\gamma_{n+1}-\gamma_n)\frac{\log(\gamma_n/2\pi)}{2\pi}$ (mean 1; Montgomery uses $\log\gamma_n$ in place of $\log(\gamma_n/2\pi)$, which does not change limits). Then
$$\mu=\liminf_n\delta_n,\qquad\lambda=\limsup_n\delta_n\qquad(\text{Montgomery-Odlyzko, PAPER-0222}).$$
Montgomery's 1973 paper uses $\lambda$ for the $\liminf$ bound ($\lambda<1$, with $\lambda=0.68$ obtainable; THM-PAPER-0091-4). GUE predicts $\mu=0$, $\lambda=+\infty$.

### 10.2 Records (with status)

| Result | Value | Source | Status |
|---|---|---|---|
| $\mu<$ | $0.5179$ (RH) | Montgomery-Odlyzko 1984, PAPER-0222 | [T] conditional on RH |
| $\mu<$ | $0.5155$ (RH) | Bui-Milinovich-Ng, PAPER-0593 | conditional on RH |
| $\mu<$ | $0.515396$ (RH) | Goldston-Turnage-Butterbaugh, PAPER-0330; "last REFEREED record" LED-SPACING-7 | conditional on RH |
| $\mu<$ | $0.50895$ (RH); $\mu\le\tfrac12$ | Inoue PAPER-0538; Bondarenko-Heap (LED-SPACING-8) | [U], conditional on RH |
| $\lambda>$ | $1.9799$ (RH) | PAPER-0222 | conditional on RH |
| $\lambda>$ | $2.3$ (RH); $2.69$ (RH); $2.9125$ (GRH) | PAPER-0603; PAPER-0593; PAPER-0618 | conditional |
| $\lambda>$ | $3.18$ (RH; unconditional for critical-line zeros) | LED-SPACING-13 | refereed record per ledger |
| $\lambda>$ | $3.63846723$ (RH) | LED-SPACING-14 | [U] |
| Positive proportion of gaps $\le\lambda_0$ (unconditional) | $\lambda_0=0.7892$ | Lamzouri, PAPER-0535 (LED-SPACING-12) | [U] |
| Limits of the MO method | $\mu\ge0.508$, $\lambda\le3.022$ for $L\le T$ (IKT); $\mu\ge0.5042$ for $y=T^{1-\delta}$ | LED-SPACING-10 | negative result |

### 10.3 Pitfalls

1. **Letters collide.** $\lambda$ (limsup gap) versus $\lambda_n$ (Li) versus $\lambda_0$ (gap threshold in Selberg's small-gap proportion) versus capital $\Lambda$ (LED-SPACING-13 uses $\Lambda$ for the limsup; the dBN constant is also $\Lambda$). Montgomery 1973's $\lambda$ is $\mu$ in MO's notation.
2. **Positive proportion versus liminf.** "A positive proportion of gaps are $\le\lambda_0$ mean spacings" (D$(\lambda)>0$) is a strictly stronger statement than $\mu\le\lambda_0$; PAPER-0535 is of the first kind, PAPER-0593/-0330 of the second.
3. **Zeros counted with multiplicity.** A multiple zero gives $\delta_n=0$, so $\mu=0$ if infinitely many zeros are multiple (THM-PAPER-0091-4); several records are stated with multiplicity (LED-SPACING-7).
4. **Which zeros.** "Zeros on the critical line" versus "zeros of $\zeta$": LED-SPACING-13 distinguishes.

---

## 11. Lindelof exponent $\mu(\sigma)$

### 11.1 Definition

$$\mu(\sigma)=\limsup_{\lvert t\rvert\to\infty}\frac{\log\lvert\zeta(\sigma+it)\rvert}{\log\lvert t\rvert}.$$
Facts [T]: $\mu(\sigma)=0$ for $\sigma\ge1$; $\mu(\sigma)=\tfrac12-\sigma$ for $\sigma\le0$; $\mu$ is convex and non-increasing; the functional equation gives $\mu(1-\sigma)=\mu(\sigma)+\sigma-\tfrac12$ [D from $\lvert\chi(\sigma+it)\rvert\asymp\lvert t\rvert^{1/2-\sigma}$; check at $\sigma=0$: $\mu(1)=\mu(0)-\tfrac12=0$]. Convexity gives $\mu(\tfrac12)\le\tfrac14$. Lindelof hypothesis (LH): $\mu(\tfrac12)=0$, equivalently $\mu(\sigma)=0$ for all $\sigma\ge\tfrac12$.

Best bound [L: LED-GROWTH-1; PAPER-0089]: $\mu(\tfrac12)\le\tfrac{13}{84}=0.1547619\ldots$ (Bourgain 2017), improving Huxley's $\tfrac{32}{205}$ (Bourgain's saving $\tfrac1{84}$ over Weyl's $\tfrac16$, double that of Bombieri-Iwaniec's $\tfrac1{168}$). Equivalent forms: $\int_1^T\lvert\zeta(\tfrac12+it)\rvert^{2k}dt\ll_{k,\epsilon}T^{1+\epsilon}$ for all integers $k\ge1$ (Hardy-Littlewood, PAPER-0471, as quoted in its record); LH for primes is equivalent to RH (Gonek-Graham, PAPER-0219).

### 11.2 Conversions

- **Exponent pair to $\mu$:** an exponent pair $(k,l)$ gives $\mu(\tfrac12)\le\frac{k+l}2$ [T]. Example: $(\tfrac{13}{84}+\epsilon,\tfrac{55}{84}+\epsilon)$ (LED-GROWTH-1) gives $\tfrac{k+l}{2}=\tfrac{68}{168}$? This is not $\tfrac{13}{84}$: the Bourgain bound arises as $\mu(1/2)\le k$ from the pair of the form $(k,\tfrac12+k)$; the pair listed in the ledger is $(\tfrac{13}{84},\tfrac{55}{84})$ with $l=\tfrac12+k$, so use $\mu(\tfrac12)\le k=\tfrac{13}{84}$ for pairs on the line $l=k+\tfrac12$ [D; the general $\frac{k+l}{2}$ formula is for the unrelated sum $\sum n^{-it}$ bound, do not mix]. (If you need the exact translation, use Ivic's book, Chapter 6, or Trudgian-Yang PAPER-0640 and Tao-Trudgian-Yang's database (cited in LED-ZDE-5).)
- **Under RH:** $\lvert\zeta(\tfrac12+it)\rvert\le\exp\bigl(C\frac{\log t}{\log\log t}\bigr)$ with the optimal $C=\frac{\log2}{2}$ (Chandee-Soundararajan; LED-GROWTH-5), so RH implies LH. Fully explicit forms in LED-GROWTH-7.
- **Dirichlet and automorphic analogues:** $\mu_\chi(\sigma)$ in the $t$-aspect has the same definition; in the $q$-aspect the exponent is in $\log q$ and subconvexity is a separate problem (Michel-Venkatesh PAPER-0460 for $\mathrm{GL}_2$).

### 11.3 Pitfalls

1. **Letter clash.** $\mu(\sigma)$ versus Mobius $\mu(n)$ versus MO's $\mu$ (Section 10) versus $\mu_j$ in Selberg gamma factors. The Lindelof exponent is $\mu(\sigma)$ with an argument.
2. **Convex-interpolation range.** $\mu(\sigma)\le\frac{1-\sigma}{2}$ for $0\le\sigma\le1$ (convexity) is not the Lindelof statement.
3. **LH is an upper-bound statement** ($\limsup$), not an asymptotic; the equivalence with moment bounds is for integer $k$ only.

---

## 12. Zero-density exponent $A(\sigma)$

### 12.1 Definition

For $\tfrac12\le\sigma\le1$ let $A(\sigma)$ be the infimum of exponents such that
$$N(\sigma,T)\ll_\epsilon T^{A(\sigma)(1-\sigma)+\epsilon}\qquad(\text{LED-ZDE-1..4}).$$
The *absolute* exponent is $c(\sigma)=A(\sigma)(1-\sigma)$: Ingham's $N(\sigma,T)\ll T^{3(1-\sigma)/(2-\sigma)+\epsilon}$ is $A(\sigma)\le\frac3{2-\sigma}$ [D]; Huxley's $N\ll T^{12(1-\sigma)/5}$ is $A\le\tfrac{12}5$; Ingham's $\tfrac83$ form $N\ll T^{8(1-\sigma)/3}$ is $A\le\tfrac83$ (explicit versions in PAPER-0037; LED-ZDE-15, -16).

State of the art (as of 2026-11-17, from the ledger):
- uniform: $\sup_\sigma A(\sigma)\le\tfrac{30}{13}\approx2.3077$ (Guth-Maynard, PAPER-0054, refereed in Ann. of Math. 203 (2026) per history/recent_developments Section 2), previous $\tfrac{12}5=2.4$ (LED-ZDE-1);
- Guth-Maynard: $A(\sigma)\le\frac{15}{3+5\sigma}$, the best known on $[\tfrac7{10},\tfrac{19}{25})$; $A(\tfrac34)\le\tfrac{20}9$ (LED-ZDE-3); Ingham's $\frac3{2-\sigma}$ equals $\frac{15}{3+5\sigma}$ at $\sigma=\tfrac7{10}$, both $\tfrac{30}{13}$;
- Density hypothesis $A\le2$ holds for $\sigma\ge\tfrac{25}{32}$ (Bourgain, PAPER-0312; LED-ZDE-6); open for $\sigma\in(\tfrac12,\tfrac{25}{32})$;
- near $\sigma=1$: $N(\sigma,T)\ll T^{6.42(1-\sigma)^{3/2}+\epsilon}$ for $\sigma\ge\tfrac9{10}$ (Heath-Brown), i.e. $A\le6.42(1-\sigma)^{1/2}$ (LED-ZDE-7);
- Tao-Trudgian-Yang database and new pieces (PAPER-0466, [U]; LED-ZDE-4/-5). $A(\tfrac12)=2$ is exact (Riemann-von Mangoldt, LED-ZDE-18).
- Conditional: LH implies bounded $N(\sigma,T)$ for $\sigma>\tfrac34$ (Halasz-Turan; LED-ZDE-14: the ledger writes "$A(\sigma)\le0$", meaning the absolute exponent $c(\sigma)=0$). Hypothesis F: DH with an $\exp((\log\log T)^{O(1)})$ loss (PAPER-0096, THM-PAPER-0096-1).
- Dirichlet families: $\sum_{\chi\bmod q}N(\sigma,T,\chi)\ll(qT)^{o(1)}\bigl(q^{7(1-\sigma)/3}T^{2(1-\sigma)}+(qT)^{30(1-\sigma)/13}\bigr)$, uniform exponent $\tfrac73$ (PAPER-0745, [U], LED-ZDE-11; earlier $\tfrac{12}5$, Huxley PAPER-0213, Jutila PAPER-0663, Heath-Brown PAPER-0341); $\mathrm{GL}_2$: $\tfrac52$ (PAPER-0746, [U], LED-ZDE-13).

### 12.2 Conversions

- If $\zeta$ has no zeros in $\Re s>\theta$ (RH: $\theta=\tfrac12$; the unrefereed quasi-RH claims: $\theta=\tfrac78$ or $\tfrac{11}{12}$), then $N(\sigma,T)=0$ for $\sigma>\theta$ and the density statement is vacuous there; for $\sigma\le\theta$ it is not implied. A zero-free half-plane $\theta=\tfrac78$ would imply the density hypothesis only on $\sigma>\tfrac78$, already known ($\tfrac78>\tfrac{25}{32}$) [D].
- Log-free versions $N(\sigma,T)\le CT^{B(1-\sigma)}$ (Bellotti, PAPER-0591, PAPER-0467) have no $\epsilon$ and no $\log T$ powers: do not equate with $A(\sigma)$ without checking the $\epsilon$ and ranges of $T$.
- In short intervals: if $A(\sigma)\le A_0$ for all $\sigma\in[\tfrac12,1)$ then $\sum_{x<n\le x+x^\theta}\Lambda(n)\sim x^\theta$ for $\theta>1-\frac1{A_0}$; with $A_0=\tfrac{30}{13}$, $\theta>\tfrac{17}{30}$ (Gafni-Tao via LED-ZDE-8). For almost all $x$: $\theta>1-\frac2{A_0}$ ($\tfrac2{15}$ at $A_0=\tfrac{30}{13}$; LED-ZDE-9). [D from the quoted rule.]

### 12.3 Pitfalls

1. **$A$ versus $c$:** whether the exponent multiplies $(1-\sigma)$.
2. **Counting convention** for $N(\sigma,T)$ (Section 2.5), especially $\lvert\gamma\rvert\le T$ (doubling) and $\beta\ge\sigma$ versus $\beta>\sigma$.
3. **Uniformity:** pointwise $\sigma$ versus $\sup_\sigma$; large-value exponents $LV(\sigma,\tau)$ in TTY's notation are a different parametrization.
4. **$A$ in $q$-aspect** is not the same function as in $T$-aspect; always state the weight $(qT)^{\ldots}$.

---

## 13. Selberg class data

### 13.1 Definition [T: PAPER-0299 Selberg 1992; surveys PAPER-0300, -0301, -0307, -0123]

$F(s)=\sum a_F(n)n^{-s}$ lies in $\mathcal S$ if: (i) absolute convergence for $\sigma>1$; (ii) $(s-1)^mF(s)$ entire of finite order for some $m\ge0$; (iii) functional equation $\Phi(s)=\omega\overline{\Phi(1-\bar s)}$ for $\Phi(s)=Q^s\prod_{j=1}^r\Gamma(\lambda_js+\mu_j)F(s)$, $Q>0$, $\lambda_j>0$, $\Re\mu_j\ge0$, $\lvert\omega\rvert=1$; (iv) Ramanujan: $a_F(n)\ll n^\epsilon$; (v) Euler product $\log F=\sum b_F(n)n^{-s}$, $b_F(n)=0$ unless $n=p^k$, $b_F(n)\ll n^\theta$ with $\theta<\tfrac12$. The extended class $\widetilde{\mathcal S}$ drops (iv) and (v).

Invariants (Kaczorowski-Perelli notation): 
- degree $d_F=2\sum_j\lambda_j$; 
- conductor $q_F=(2\pi)^{d_F}\,Q^2\prod_j\lambda_j^{2\lambda_j}$; 
- $\xi_F=2\sum_j(\mu_j-\tfrac12)=\eta_F+i\theta_Fd_F$ (so $\theta_F=2\sum\Im\mu_j/d_F$-type; check the source's convention before using the imaginary part); 
- $F$ primitive if $F=F_1F_2$ forces $F_1=1$ or $F_2=1$.
Structure [L: THM-PAPER-0123-4,-5]: $\mathcal S_d=\emptyset$ for $0<d<1$ (Conrey-Ghosh, PAPER-0033); $\mathcal S_1$ consists of $\zeta$ and shifted Dirichlet $L(s+i\theta,\chi)$ with $\chi$ primitive; $\widetilde{\mathcal S}^\#_d=\emptyset$ for $1<d<5/3$; degree conjecture: $d_F\in\mathbb Z_{\ge0}$ (open). Value distribution, Hypothesis S and Hypothesis D: THM-PAPER-0123-8,-9.

### 13.2 Examples with conversions [D, checked]

| $F$ | gamma factor | $Q$ | $(\lambda_j)$ | $d_F$ | $q_F$ |
|---|---|---|---|---|---|
| $\zeta$ | $\Gamma(s/2)$ | $\pi^{-1/2}$ | $\tfrac12$ | $1$ | $(2\pi)\cdot\pi^{-1}\cdot\tfrac12=1$ |
| $L(s,\chi)$, $\chi$ even primitive mod $q$ | $\Gamma(s/2)$ | $(q/\pi)^{1/2}$ | $\tfrac12$ | $1$ | $q$ |
| Hecke $L(s,\chi)$ over $K$ imaginary quadratic, trivial infinity type, conductor $\mathfrak f$ | $\Gamma(s/2)\Gamma(\tfrac{s+1}2)$ (from $\Gamma(s)=\pi^{-1/2}2^{s-1}\Gamma(\tfrac s2)\Gamma(\tfrac{s+1}2)$) | $(\lvert d_K\rvert N\mathfrak f)^{1/2}/\pi$ | $(\tfrac12,\tfrac12)$ | $2$ | $\lvert d_K\rvert N\mathfrak f$ |

Check of the last row: $\Lambda_K(s,\chi)=(\lvert d_K\rvert N\mathfrak f)^{s/2}(2\pi)^{-s}\Gamma(s)L(s,\chi)$; using the duplication formula this equals const$\cdot[\lvert d_K\rvert N\mathfrak f/\pi^2]^{s/2}\Gamma(s/2)\Gamma(\tfrac{s+1}2)L$, so $Q=(\lvert d_K\rvert N\mathfrak f)^{1/2}/\pi$ and $q_F=(2\pi)^2\cdot\frac{\lvert d_K\rvert N\mathfrak f}{\pi^2}\cdot(\tfrac12)^{1/2\cdot2}\cdot(\tfrac12)^{1/2\cdot2}$; each $\lambda_j^{2\lambda_j}=\tfrac12$, so $q_F=4\cdot\frac14\lvert d_K\rvert N\mathfrak f$ [D]. For $K=\mathbb Q(\sqrt{-3})$: $\lvert d_K\rvert=3$.
$\zeta_K=\zeta\cdot L(s,\chi_{-3})$ and, for a Dirichlet character $\chi$, base change $L_K(s,\chi\circ N)=L(s,\chi)L(s,\chi\chi_{-3})$ up to finitely many Euler factors (ARCHITECTURE E3, [T]).

### 13.3 Pitfalls

1. **Gamma-factor non-uniqueness.** The data $(Q,\lambda_j,\mu_j,\omega)$ are not unique (duplication formula, $\Gamma(s)\leftrightarrow\Gamma(s/2)\Gamma((s+1)/2)$); $d_F$, $q_F$, $\xi_F$, $\omega$ are invariants, $Q$ and $r$ are not.
2. **Selberg versus completed $\xi$.** The Selberg functional equation involves $\Phi$ (no polynomial $s(s-1)$ factor); the Li/Weil literature uses $\xi$ (with it). Mixing them shifts $\delta(\pi)$-type terms (Section 5).
3. **Imprimitive versus primitive characters** and **$L^S$ with Euler factors removed**: zeros in $\Re s>0$ differ only on $\Re s=0$, but conductor and degree conventions change (DOSSIER 1.3 on the Lean statement).
4. **GRH for the class.** "GRH for $F\in\mathcal S$" is the statement for each $F$; for the extended class a zero off the line can occur (Davenport-Heilbronn type functions, PAPER-0417), so statements like $\Lambda_F\ge0$ (PAPER-0333) are for $\widetilde{\mathcal S}^\#$ and do not assert GRH.

---

## 14. Hecke $L$-functions over $\mathbb Q(\sqrt{-3})$ (2026 quasi-RH papers) [AI]

All statements about the OpenAI manuscripts are [AI]/[U]: PAPER-0528 (7/8, 30 Sep 2026; Lean formalization claimed, not built), the 11/12 paper (5 Oct 2026; the audited object of audits/quasi_rh/, PAPER-0161 is the index record of the alternate), Siegel-zero paper (1 Oct 2026), PAPER-0162 (cubic Gauss-sum first moment), and follow-ups PAPER-0155, -0156, -0157, -0158, -0163. See audits/quasi_rh/DOSSIER.md for scope; **no claim here is a review result and RH is not affected.**

### 14.1 The field and the $L$-functions

$K=\mathbb Q(\sqrt{-3})=\mathbb Q(\omega)$, $\omega=e^{2\pi i/3}$, $\mathcal O=\mathbb Z[\omega]$, $d_K=-3$, $h_K=1$, units $\mu_6$, $N(a+b\omega)=a^2-ab+b^2$, $\lambda=1+2\omega=\sqrt{-3}$ (ARCHITECTURE; audit_APPA §1: $\lambda=\sqrt{-3}$, $\lambda^2=-3$; audit_S6 writes $\lambda=i\sqrt3$, the same number).
A *finite-order Hecke character* is a character $\nu$ of the ray class group of conductor $\mathfrak f$; since $h_K=1$ it is a character of $(\mathcal O/\mathfrak f)^\times$ trivial on the image of the units (HeckeSevenEighths challenge, DOSSIER 1.3). 
$$L(s,\nu)=\sum_{\mathfrak a}\nu(\mathfrak a)N\mathfrak a^{-s}\ \ (\Re s>1),\qquad L_K^S(s,\nu)\text{ with Euler factors at primes in }S\text{ removed}.$$
Main claims (all [AI], unrefereed): no zero of any finite-order $L_K(s,\nu)$, and hence of any Dirichlet $L(s,\chi)$ including $\zeta$, in $\Re s>\theta$, with $\theta=\tfrac{11}{12}$ (paper2) and $\theta=\tfrac78$ (7/8 paper), pole at $s=1$ allowed for principal $\nu$ (DOSSIER Q1, Q2, E1). Quasi-RH follow-ups: Liu $0.874957019\ldots$ and $0.874887$; Xu-Sang $0.8748867$; Chang-Wang $0.874462$; Ji $599/600$ over $\mathbb Q(i)$ (PAPER-0156, -0157, -0158, -0163, -0155; LED-ZFR-3; these are *conditional on OpenAI's intermediate estimates*).

Conversions: $\theta$ ("no zeros in $\Re s>\theta$") versus "$1-\theta$" (width of the zero-free strip near 1) versus "$\sigma_0$" in $\sigma\ge\sigma_0$ (closed half-plane). The Lean Comparator statement is $\zeta(s)\ne0$ for $\tfrac78<\Re s$ (strict inequality; DOSSIER 1.3), and Siegel-zero corollary (DOSSIER L1): $\beta\le\tfrac78\Rightarrow(1-\beta)\log q\ge\frac{\log3}8=0.1373$ [O, DOSSIER; the 7/8 theorem used as a black box].
Lean `LFunction` for Hecke characters in the challenge file is $\pi^s\Gamma(s)^{-1}\Lambda(s)/6$ with $\Lambda$ a Mellin transform of a lattice sum; the $\tfrac16$ is the number of units (sum over elements $=6\times$ sum over ideals) (DOSSIER 1.3; DOSSIER notes the challenge file defines its own objects).

### 14.2 Pitfalls

1. **$7/8$ versus $11/12$** are different theorems with different proofs (DOSSIER 1.1); the Lean file covers 7/8 only, and not "later applications".
2. **Conditional character of the refinements:** "0.8749 follow-ups" assume OpenAI's estimates.
3. **Sum over elements versus ideals** (factor 6) and over $\mathcal O/\mathfrak f$ versus ray classes.
4. **Principal pole**: $\zeta_K$ has a pole at $s=1$; statements "no zeros in $\Re s>\theta$" are about zeros, not poles.

---

## 15. Residue symbols $\chi_n(u)$, Gauss sums $g$, Kubota's cubic theta

### 15.1 "Primary" and the residue symbols

**Primary has two meanings.** 
- Ireland-Rosen (Chapter 9, cubic reciprocity): $\pi\in\mathbb Z[\omega]$, $N\pi\ne3$, is *primary* if $\pi\equiv2\pmod 3$ (i.e. $\equiv-1$). [T]
- Patterson, Dunn-Radziwill (PAPER-0960) and the 2026 papers: *primary* means $\equiv1\pmod 3$ (audit_S6 §1, audit_APPA §1; "this includes the inert primes $-q$ with $q\equiv2\pmod 3$"). [AI audit; DR as transcribed]
Conversion [D]: $n_{\rm IR}=-n_{\rm DR}$ for every non-unit generator, so the two conventions select the two generators of the ideal that differ by $-1$; the residue symbol $(\cdot/n)_3$ depends only on the ideal $(n)$ so no symbol changes, and since $-1$ is a cube, $(-1/n)_3=1$ and cubic reciprocity $(a/b)_3=(b/a)_3$ holds for both normalizations (DR (1.4)-(1.5) supplementary laws were numerically confirmed for 66 primary primes of norm $<200$, audit_S6).

**Symbols.** For a prime $\pi\nmid6$ of norm $N\pi$:
$$\Bigl(\frac u\pi\Bigr)_3\equiv u^{(N\pi-1)/3},\qquad\Bigl(\frac u\pi\Bigr)_6\equiv u^{(N\pi-1)/6}\pmod\pi,$$
values in $\mu_3$, $\mu_6$, extended multiplicatively in the denominator, zero when not coprime (audit_S6, audit_APPA). In the quasi-RH papers $\chi_n(u):=(u/n)_6$ (audit_APPA §1, citing l.250-262 of paper2). Hence $\chi_n^2=(\cdot/n)_3$ (cubic), $\chi_n^3=(\cdot/n)_2$ (quadratic). Values are stored in the audits as exponents of $\zeta_6=e^{i\pi/3}=1+\omega$. The identification of $\mu_3\subset\mathbb C$ with $\mu_3\subset(\mathcal O/\pi)^\times$ uses $\omega\mapsto\omega\bmod\pi$; for $p=7$, $\pi=2+3\omega$, $\omega\equiv4\pmod\pi$ [V].

Pitfalls: (a) the symbol is **$\chi_n(u)$ with $u$ the numerator**, so "$\chi_n(k)$" in a bilinear form of the paper is $(k/n)_6$, while Heath-Brown's and Patterson's papers often write $\chi_c(n)$ with the roles reversed; reciprocity swaps them up to a sign and a cubic factor. (b) $\chi_n(p^6)=1_{p\nmid n}$ is the identity used in the "row $u=p^6$" extraction (DOSSIER 1.2; verified in 24,076 cases by audit_S3). (c) For the inert prime $q$, $N\pi=q^2$; the formula needs $q^2\equiv1\pmod 6$, true for $q\ne2,3$.

### 15.2 Additive characters and Gauss sums

Additive characters (audit_S6, audit_APPA):
$$e(z)=\exp\bigl(4\pi i\,\Im z/\sqrt3\bigr)=\exp\bigl(2\pi i\operatorname{Tr}(z/\lambda)\bigr),\qquad\breve e(z)=\exp\bigl(2\pi i(z+\bar z)\bigr)=\exp(4\pi i\Re z),$$
related by $e(z)=\breve e(z/\lambda)$ (checked on 500 random rationals). For $z=u+v\omega$ with $u,v$ rational, $e(z)=\exp(2\pi iv)$; $\mathcal O$ is self-dual for $e$ with covolume $\tfrac{\sqrt3}2$ (audit_APPA). Dunn-Radziwill's (DR) Gauss sum is the **unnormalized** $g(r,c)=\sum_{x\bmod c}(x/c)_3\breve e(rx/c)$, so $\lvert g(1,c)\rvert=\sqrt{Nc}$ for squarefree $c$ coprime to 3 and $g(r,c)=\overline{(r/c)_3}\,g(1,c)$ [AI audit, DR as transcribed].
The 2026 papers' **normalized** sums: $\gamma_j(n)=N(n)^{-1/2}\sum_{x\bmod n}\chi_n(x)^je(x/n)$ (so $\gamma_2$ is the cubic and $\gamma_3$ the quadratic Gauss sum), and the audits state $\gamma_2(n)=(\lambda/n)_3\,g(1,n)/\lvert n\rvert$ (conversion paper2 $\leftrightarrow$ DR). Properties used: $\lvert\gamma_j(p)\rvert=1$ for primes, $\gamma_j\gamma_{-j}=\chi_p(-1)^j$, twisted multiplicativity $\gamma_j(ab)=\gamma_j(a)\gamma_j(b)(\chi_a(b)\chi_b(a))^j$; Gauss-Jacobi $\gamma_2(n)^3=\mu(n)\alpha(n)$ ($\alpha$ a unimodular normalized-Jacobi-sum factor of the paper), equivalently $\mu(n)=\overline{\alpha(n)}\gamma_2(n)^3$ (audit_APPA; ARCHITECTURE E6). The classical form [T, Ireland-Rosen Ch. 9]: for a prime $p\equiv1\pmod 3$ and the cubic character $\chi_\pi$ attached to a primary prime $\pi\mid p$ ($\pi\equiv2\bmod 3$), 
$$g(\chi_\pi)=\sum_{x\bmod p}\chi_\pi(x)e^{2\pi ix/p},\quad\lvert g\rvert^2=p,\quad g(\chi_\pi)^3=p\,J(\chi_\pi,\chi_\pi)=p\,\pi.$$
[V: $p=7$, $\pi=2+3\omega$, $\omega\mapsto4\bmod7$: $g^3=3.5000+18.1865i=7\pi$ and $J=0.5+2.598i=\pi$; complex conjugate $7\bar\pi$ not matched.] Note the sign flip: with the DR "primary" $\pi'=-\pi\equiv1\pmod 3$, $J(\chi,\chi)=-\pi'$ [D].

### 15.3 Kubota's cubic theta function

Kubota (1969) and Patterson (1977) (via residue of cubic Eisenstein series on hyperbolic 3-space $\mathbb H^3$ with $\mathrm{SL}_2(\mathcal O)$ acting, $\gamma w=(aw+b)(cw+d)^{-1}$, DR (5.1)). Properties as transcribed in the audits [AI audit of a refereed source; reproduced numerically, not re-proved]:
- Multiplier: $\theta(\gamma w)=\kappa(\gamma)\theta(w)$ on $\Gamma_1(3)$ with $\kappa(\gamma)=(c/a)_3$ (DR (5.4)); $\theta$ is invariant under $\mathrm{SL}_2(\mathbb Z)$ and under translations by $\mathbb Z+3\mathcal O$ (E8). Equivalent forms of the same multiplier: $(c/a)_3=\overline{(c/d)_3}=(b/d)_3$ (DR Remark 5.1). **Convention check settled numerically** by audit_S6: $\theta(\gamma w)=(c/a)_3\theta(w)$ to $2\times10^{-13}$, whereas the complex conjugate multiplier fails by $\lvert1-\omega\rvert$; this is the sign that makes the twisted prime factor $B_{p,1}=\chi_p^3$ quadratic rather than sextic (DOSSIER §1.2 load-bearing points).
- Fourier coefficients (Patterson, Thm 8.1, as in DR (5.6)-(5.8)): with $\lambda=\sqrt{-3}$, the coefficient of $\overline\theta$ at index $\lambda^{-3}nb^3$ ($n,b$ primary, $n$ squarefree, **no** coprimality between $n$ and $b$) is $3^{5/2}\lvert b\rvert\,\overline{\chi_n(\lambda)^2}\,\gamma_2(n)$ (ARCHITECTURE E9). DR write $\tau(\pm\lambda^{3n-3}cd^3)=\overline{g(1,c)}\lvert d/c\rvert3^{n/2+5/2}$ with $c,d\equiv1\pmod3$, $c$ squarefree; the conversion is $\gamma_2(n)=(\lambda/n)_3g(1,n)/\lvert n\rvert$ and $\tau$ even.
- Pitfall noted by the audit: pdftotext drops the overline in DR (5.7); conjugation placements are load-bearing.
- Patterson's bias conjecture on cubic Gauss sums is proved **conditionally on GRH for Hecke $L$-functions of $\mathbb Q(\omega)$** by Dunn-Radziwill (PAPER-0960, Ann. of Math. 200 (2024)). The unconditional first moment of PAPER-0162 is an [AI] unrefereed claim (history/recent_developments Section 4.1; Lean claimed).

### 15.4 Pitfalls summary for this section

1. Primary $\equiv1$ versus $\equiv2\pmod3$; 2. unnormalized $g(r,c)$ (modulus $\sqrt{Nc}$) versus $\gamma_j$ (modulus 1); 3. $\breve e$ versus $e$ (factor $\lambda$ in the argument); 4. conjugate versus unconjugated Kubota multiplier; 5. $\chi_n$ sextic versus its square (cubic) and cube (quadratic); 6. Hecke $L$ as function of ideals versus of elements.

---

## 16. What was run (verification log for [V] items)

Scratch environment, mpmath, python3 -I. All finite-precision checks; none is a proof.

| Item | Check | Result |
|---|---|---|
| $H_0$ versus $\xi$ | quadrature of $\int\Phi(u)\cos(zu)du$ against $\xi(\tfrac12+iz/2)$ at $z=0,1.3$ | ratio $=8.000000000000000$ (i.e. $H_0=\xi/8$) |
| $\Xi(0)$ | $\xi(1/2)$ | $0.49712077818831\ldots$ |
| $\theta$ expansion | at $t=20,50$ | residual $1.2\times10^{-10}$, $1.2\times10^{-12}$ with terms through $7/(5760t^3)$ |
| Gram points | root-finding of $\theta(t)=n\pi$ | $g_{-1}=9.666908$, $g_0=17.845600$, $g_1=23.170283$ (and $3.436218$ on the decreasing branch) |
| $Z$ real | $\Im(e^{i\theta}\zeta(\tfrac12+30i))$ | $-4\times10^{-26}$ |
| Li generating function | Taylor of $\log\xi(1/(1-z))$ at $z=0$ vs $\lambda_n/n$ from the derivative formula, $n\le5$ | agree to the finite-difference accuracy ($10^{-6}$); $\lambda_1=0.0230953$ vs closed form $0.0230957$; $\lambda_2=0.09234$, $\lambda_3=0.20764$ |
| Weil explicit formula (W1) | Gaussian test function, 40 zeros vs prime, digamma and pole terms | $0.037082583463$ both sides |
| Cubic Gauss sum | $p=7$, $\pi=2+3\omega$ | $g^3=7\pi$, $J(\chi,\chi)=\pi$ |

Unchecked in this file: Riemann-Siegel remainder terms; Li's printed normalization; the Nyman-Beurling Mellin identity; any Selberg-class statement beyond the two arithmetic checks of Section 13.2.

---

## 17. Cheat sheet of conversions

| From | To | Formula |
|---|---|---|
| $\xi$ (with $\tfrac12$) | $\xi_2$ (BL, Lagarias) | $\xi_2=2\xi$ |
| $H_0(z)$ | $\xi$ | $H_0(z)=\tfrac18\xi(\tfrac12+\tfrac{iz}2)$ [V] |
| Newman $t$ | Titchmarsh-variable $\lambda$ | $t=4\lambda$, $z=2x$ [D] |
| zero ordinate $\gamma$ | $H_0$-zero $z$ | $z=2\gamma$ |
| Li $\lambda_n$ | Keiper $\lambda^K_n$ | $\lambda^K_n=\lambda_n/n$ [V] |
| $\sum_n\lambda_nz^{n-1}$ | $\log\xi$ | $\frac d{dz}\log\xi(\frac1{1-z})$ [V] |
| $\lambda_1$ | RH-constants | $\sum_\rho\lvert\rho\rvert^{-2}=2\lambda_1=2+\gamma-\log4\pi=0.0461914\ldots$ (under RH) |
| $N(T)$ | $S,\theta$ | $N=\theta/\pi+1+S$ |
| $N_{\rm smooth}$ | Polymath $g(x,0)$ | $g(x,0)=N_{\rm smooth}(x/2)+\tfrac12$ |
| Bombieri $f$ | Weil additive $h,g$ | $h(r)=\hat f(\tfrac12+ir)$, $g(u)=e^{u/2}f(e^u)$ |
| Pair correlation | Fourier | $\sum r(u)w=N\int\hat rF\,d\alpha$ |
| $A(\sigma)$ | exponent of $T$ | $c(\sigma)=A(\sigma)(1-\sigma)$ |
| Selberg data | Dirichlet $L$ | $q_F=q$ (conductor), $Q=\sqrt{q/\pi}$ |
| DR "primary" | Ireland-Rosen "primary" | multiply generator by $-1$ |
| $e$ | $\breve e$ | $e(z)=\breve e(z/\lambda)$, $\lambda=\sqrt{-3}$ |
| unnormalized $g(1,n)$ | $\gamma_2$ | $\gamma_2(n)=(\lambda/n)_3g(1,n)/\lvert n\rvert$ |

---

## 18. Symbol-collision table

| Symbol | Meanings in this archive |
|---|---|
| $\Lambda$ | von Mangoldt; dBN constant; completed zeta; $\limsup$ of gaps (LED-SPACING-13) |
| $\lambda$ | $\limsup$ gap (MO); Montgomery's 1973 $\liminf$ bound; Li coefficient $\lambda_n$; $\lambda=\sqrt{-3}$; $\lambda_j$ gamma-factor weights; $\lambda_0$ small-gap threshold; heat parameter $\lambda$ in Titchmarsh variable |
| $\mu$ | Mobius; MO $\liminf$; Lindelof exponent $\mu(\sigma)$; gamma-factor shifts $\mu_j$; measure $\mu$ in PAPER-0043 |
| $\theta$ | Riemann-Siegel $\theta(t)$; Chebyshev $\theta(x)$; mollifier exponent; zero-free exponent in quasi-RH; Ramanujan exponent in Selberg (v) |
| $\rho$ | zero; fractional part (Nyman-Beurling) |
| $\kappa$ | proportion on the line; $\kappa(\gamma)$ Kubota multiplier; $\kappa_j$ spectral parameters |
| $N_0$ | critical-line zero count; $N_t$ at $t=0$; $N_0$ of Mertens-type sums elsewhere |
| $\beta$ | $\Re\rho$; $\beta=2+\gamma-\log4\pi$ (Nicolas); half-width in PAPER-0043 |
| $\gamma$ | ordinate; Euler's constant; $\gamma_j(n)$ normalized Gauss sums; $\gamma$ in Connes-Consani Lemma 6.10 |
| $\omega$ | $e^{2\pi i/3}$; root number in Selberg functional equation |
| $\chi$ | Dirichlet/Hecke character; $\chi(s)$ functional-equation factor; $\chi=\mathbf 1_{(0,1]}$ in Nyman-Beurling; $\chi_n$ sextic symbol |
| $\xi$ | completed zeta; Selberg invariant $\xi_F$; Fourier dual variable |


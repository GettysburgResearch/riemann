# Findings of the 10 October 2026 quasi-RH wave

```text
Status: EXPLORATORY synthesis. External theorems are IMPORTED and unreviewed here; derived statements are PROPOSED unless marked otherwise.
Scope: global for the imported half-planes; the mechanism analysis is about a proof architecture, not about zeta itself.
Exact sources or dependencies: README.md table; notes/*.md; scripts/*.py
What was actually run: Python grid searches over the Part II exponent system (scripts/), literature searches, reading of the primary manuscripts, a repository hypothesis audit.
Smallest remaining gap: see Section 6 (the single input that would move the bound by more than 1e-2).
```

RH is not proved. The October 2026 external result is a **uniform zero-free half-plane** $\Re s>7/8$ (now $\Re s>0.874957$ after Liu's parameter re-optimization) for every Dirichlet $L$-function and every finite-order Hecke $L$-function over $\mathbb Q(\sqrt{-3})$. This wave asked: *where exactly is that architecture stuck, which stone has not been turned, and what does the new half-plane give this repository unconditionally?*

## 1. What the architecture is (verified reading)

See `README.md` for the one-paragraph description and sources. Three identities drive it (notes/C_alternatives.md §1.1):

- **(A) Hasse–Davenport sign.** For a primary prime $p$ of $\mathbb Z[\omega]$ and the sextic symbol $\chi_p$, $\gamma_1(p)\gamma_2(p)=-\alpha(p)\chi_p(4)\gamma_3(p)$ (main paper eq. (4.7)); multiplying over $p\mid c$ gives $\gamma_1(c)\gamma_2(c)=\mu(c)\cdot(\text{explicit ray-class phase})\cdot\alpha(c)$. **The Möbius function is manufactured by the sign $-1$ per prime in the Jacobi sum $J(\chi,\chi^2)=-\chi(4)p$.** This is why the Poisson dual of the probe contains $1/L_F(s,\eta)$ (main paper Lemma 7.1, eq. (7.13): $\zeta_F^S(6z)L^S(w,\chi_\bullet(u))/L^S(x,\eta\chi_\bullet(u))\cdot H_{\eta,u}$).
- **(B) Patterson.** The cubic Gauss sums are the Fourier coefficients of Kubota's cubic theta function (unique Whittaker model for the 3-fold cover), which gives the completed reflection (Prop. 5.1) over indices $cn^3$.
- **(C) Quadratic reflection twist.** At the dual cusp the phases combine to $\chi_p^{-3}$, which is quadratic, so the perfectly orthogonal Goldmakher–Louvel quadratic large sieve ($M+N$) bounds the direct side.

The numbers: the Mellin shift $5/6$ is the pole of $\zeta_F(6z)$ at $z=1/6$ (sixth-power parts of Poisson frequencies $ua^6$); the amplification slope $\alpha=5/6$ (eq. (17.88)) counts companions $ua^6$ of a sixth-power-free row; both are $1-1/N$ with $N=6$ the order of the residue-symbol family. A general-$N$ bookkeeping of the same shape gives

$$B_N(\ell)=1-\frac1{2N}-\frac{3\ell}{2N},$$

which for $N=6$ is exactly Liu's $B(\ell)=11/12-\ell/4$ (including its $b$-independence). The formal $N\to2$ limit of the Part I boundary is $3/4$; this is the most plausible origin of the public "barrier at 3/4" remark. $N=2$ is also exactly where the mechanism does not exist (Jacobi theta over $\mathbb Q$: $g(\chi)^2=\chi(-1)p$ carries no per-prime sign, so no $\mu$ appears and $L$ lands in the numerator).

## 2. The Part II exponent system, reconstructed and verified (notes/E_mechanism_lead.md, scripts/)

With $l_x=(1-b-\ell)/2$, $l_y=(1+b-\ell)/2$, $h=(1+b+3\ell)/2$, eq. (20.4) of the main paper becomes, at the critical frequency $d=h$,

$$E(h;\delta,x)=\underbrace{-\tfrac14+\tfrac{5\ell}{4}+\tfrac b6}_{C_0(b,\ell)}+\delta\Big(\tfrac12+\ell\Big)+x\delta\ell-h\big(1-R_*(\delta,x)\big),$$

where $\delta=2a-1$ is the zero class of a nonprincipal row (its twist has a zero of real part $a$), $x=q/\delta\in[0,1/2]$ the prime-amplitude ratio and $R_*$ the row-count exponent of Prop. 19.2/eq. (20.8). The proof needs $\max_{\delta,x}E\le0$. Checks: $(1/8,1/6)$ gives $C_0=-1/48$ and the paper's coefficients $2/3$, $1/6$ exactly; the maximum of $E$ there is $-2.28\times10^{-4}$ (paper certifies $-E_*\ge49/440640=1.11\times10^{-4}$); maximizing $\ell$ subject to $\max E\le0$ returns $b=0.1237$, $\ell=0.16684$, $B=0.874957$ with active class $\delta=0.389$, $x=1/2$ — Liu's $B_{\rm new}$ and his $\delta_c=(49-\sqrt{921})/48$ to all printed digits. Three independent re-optimizations found on GitHub (Liu, LW56e2, Gao) land at $7/8-4.3\times10^{-5}$; the estimate system is at its optimum.

**Dial table** (what each lemma could buy if improved; scripts/dials2.py, dials3.py):

| Dial (lemma) | Current | Hypothetical | Best $B$ |
|---|---|---|---|
| $\alpha$, long inverse-moment amplification (Lemma 17.6) | 5/6 | 0.75 / 0.60 | 0.87451 / 0.87328 |
| plain fourth-moment capacity $z_P=c(1-2m)$ (Lemma 18.1) | 2/9 | 0.5 / 1.0 | 0.87418 / 0.87263 |
| inverse capacity $z_M=s_M(1-r)$ (Lemma 17.1) | 1/2 | 0.75 / 1.0 | 0.87305 / 0.87256 |
| **all row counts at density-hypothesis strength** $R_*=1-\delta$ | — | — | **13/15 = 0.866667** (binding class moves to the floor $\delta=0$) |
| power saving $U^{-f}$ on the zero-free (floor) rows, with ideal counts | 0 | 0.1 / 0.25 / 0.389 | 0.8485 / 0.8095 / **3/4** |

Reading. (i) The three moment lemmas together are worth $<10^{-2}$. (ii) With *perfect* zero-density inputs the architecture reaches exactly $13/15$ (an independent public verification repository reports the same "density barrier"), and is then pinned by the **floor**: rows whose twists have no zero above $51/100$, which the proof counts trivially ($U^1$) and bounds pointwise (Lemma 10.4 applies the triangle inequality to the row sum; the floor bin "uses no witness", §10.5). The floor constraint is just $C_0\le0$, i.e. $\ell\le\tfrac15-\tfrac{2b}{15}$. (iii) Since under GRH for the family *every* row is a floor row, the $13/15$ wall is an *absolute-value* wall, not a zero-density wall: no bound that sums nonprincipal rows with absolute values can beat $13/15$ in this bookkeeping. (iv) $3/4$ would need a saving of $U^{7/18}$ over the trivial floor sum at $d=h$ — i.e. cancellation *between* Poisson rows $u$ — which nothing in the proof attempts.

### 2b. Independent full model (notes/A_exponent_model.md, scripts/exponent_model.py)

A second, independent reconstruction with all side constraints (floor class, intermediate rows $d\le1/2$ with $R=76/75-2\delta/3$, small-row margin, supply, $l_x>\ell$, the reflected-majorant penalties $(8b+3\ell-3)_+/12$ and $(5\ell-1)_+/8$ of Liu's Prop. 22.2) reproduces every margin of Section 20 exactly ($-7/1200$, $-49/14400$, $63/800$, $8/39$), the endpoint minimum $2.282\times10^{-4}$ (the paper's $49/440640$ is the same identity weakened by $J\le5/2$), and Liu's $B_{\rm new}$ to $7\times10^{-10}$. Its sensitivity table adds one decisive row to the table above:

| dial | current | hypothetical | best $B$ | $dB/d(\text{dial})$ |
|---|---|---|---|---|
| $\alpha$ (Lemma 17.6) | 5/6 | 2/3 / 1/2 / 0 (Lindelöf on average) | 0.873916 / 0.872227 / 0.869792 | +0.0047 |
| $c_\kappa=1/(6\kappa)$ (Lemma 18.1) | 2/9 | 1 | 0.874052 | −0.0020 |
| $c_M$ (Lemma 17.1, $r+2z\le1\to r+z\le1$) | 1/2 | 1 | 0.874052 (supply cap $\ell/h$ then binds) | −0.0096 |
| **$\theta$, the Gram loss $b/12$ in the direct bound $l_x/2+\theta b$ (the $P_a^{1/6}$ term of Prop. 15.2, $P_a=Y'^2/Q=Z^b$)** | 1/12 | 1/24 / 0 | **0.869608 / 0.863950** | **+0.100** |
| $z_0$, floor $a_0$, supply, sextic sieve (Lemma 9.1) | — | — | no change | 0 |

So the single most valuable input is on the **direct** side: the additive Gram bound (15.4), $\sum_{q_m\ll Q}|A_m|^2\ll(Q/Y')(1+P_a^{1/6}+P_a^2/Y')Z^\epsilon$. Removing its $P_a^{1/6}$ term is worth more than all count dials together ($0.8698$). Cumulative best-conceivable values in this bookkeeping: ideal counts $0.8698$; $+$ floor $a_0\to1/2$: $13/15$; $\theta=0$ alone $0.86395$; $\theta=0$ $+$ all counts $+$ floor: $0.85985$; $+$ no supply constraint: $6/7$ at $(b,\ell)=(2/7,1/7)$, pinned by $B_{\rm low}=11/12-\ell/4-b/12$, the floor $B\ge2/3+b/6+\ell$ and the second Gram term $b\le l_y/2$. Only by dropping the second Gram term and the reflected penalty does the system degenerate to $5/6$ (the Mellin shift). **$3/4$ is not attainable by any improvement of the moment lemmas**; it would need a different signal normalization (the $5/6$ shift, i.e. the sextic family) or beating the trivial floor count.

## 3. Why the direct side is also far from the truth

Under RH the probe's true size is $Z^{C(1/2)}=Z^{-1/6}$ (Part I), while the direct bound is $Z^{1/4}$: the direct side loses up to $Z^{5/12}$, all of it in the Cauchy–Schwarz over the $\asymp Y$ rows $s$ before the quadratic large sieve (notes/C_alternatives.md §3). The sieve's diagonal is then unavoidable. The object that would replace this step is a two-variable series $Z_\eta(s,w)=\sum_s\sum_c\gamma_2(c)\alpha(c)\eta(c)(c/s)_2q_c^{-s}q_s^{-w}$ (quadratic twists of Kubota's Gauss-sum Dirichlet series, summed over the quadratic modulus). Friedberg–Hoffstein–Lieman (Math. Ann. 2003) continue the *untwisted* $n$-th order double series $\sum_m L(s,\chi_m)N\mathfrak m^{-w}$ with a group of functional equations relating it to a Gauss-sum series; the character-twisted case is listed as an open problem in the 2025 axiomatic-MDS literature. So direction 3 is a real open problem, not a bounded project.

## 4. The sharpness obstruction (literature, notes/C_alternatives.md §2)

The $(AB)^{2/3}$ term of Heath-Brown's cubic large sieve is sharp: Dunn–Radziwiłł (Ann. of Math. 2024) under GRH, de Faveri–Dunn–Hoffstein (arXiv:2607.07911, July 2026) unconditionally, with extremal sequence the normalized cubic Gauss sums — exactly the sequence this method's own Poisson steps produce. Hence the central-range row envelope $R(\delta)=4/3-\delta$ cannot be improved by a better *inequality*, only by subtracting the explicit bias main term (Patterson's $5/6$ bias) and treating it as a second principal-type row. That is a bounded project with predicted ceiling $13/15$ (Section 2).

## 5. Alternative families: the quartic route is closed (notes/C_alternatives.md §1.4, notes/F_quartic_feasibility.md)

The pairing (order-$N$ character, theta coefficient $g(\chi^b)$) needs $g(\chi)g(\chi^b)=\mu$-sign $\times$ explicit $\times g(\chi^{1+b})$ with $\chi^{1+b}$ quadratic **and** a cusp reflection whose row coupling is quadratic. $N=6$ with the cubic theta is the unique unconditional pairing (Lichtman's "essential"). The quartic analogue over $\mathbb Q(i)$, ranked first in note C, was examined in detail in note F and **fails structurally**, not for lack of coefficient knowledge:

- The literature was mis-stated in note C: by the Hecke relations $\tau_4(mp^2)=G_3(m,p)\tau_4(m)$, $\tau_4(mp^3)=0$, so $\theta_4$'s coefficients at *squares* are the quartic Gauss sums (Suzuki 1983) and it is the *squarefree* coefficients $\tau_4(\pi)$ that are undetermined (Patterson, Eckhardt–Patterson: $\tau_4(\pi)^2=2\bar G(\pi)$ conjectured). Unconditional $L^2$-control exists at all cusps (de Faveri–Dunn–Hoffstein, Prop. 8.2 and the Lindelöf-on-average Prop. 8.1) and does not help.
- The Möbius pairing $g(\chi_a)^2=J\,g(\chi_a^2)$ forces pairing the theta index $a^2$ with a character of modulus $a$, i.e. a mask $D\mapsto(m/D)_4^{\mp1}$ on $\mu=D^2$ which is not periodic in $\mu$ (explicit counterexample in note F), so no OpenAI-type reflection exists. The direct series is Kubota's quartic series at frequency $m^3$; its only functional equation keeps the quartic row coupling, so the balanced row energy is governed by the quartic large sieve: $\ll Z^{4/3}$ (Blomer–Goldmakher–Louvel) and provably $\gg Z^{5/4}$ (DFDH Thm 1.2; the row sequence is their extremal sequence).
- Bookkeeping: $C(s)=s-5/8$ and $\sigma_0=1/2-1/(2N)+E/2$ with $E\in[5/4,4/3]$ gives $\sigma_0\in[1,25/24]$; a scan over all scales and both routes has infimum exactly $1$ (the same scan reproduces $11/12$ for $N=6$). General fact: a direct sharp $n$-th order sieve always yields $\sigma_0=1$; **the cubic method's entire gain is the reflection to a quadratic coupling.** The Part II formal $B_4(\ell)=7/8-3\ell/8$ is moot.

## 6. The smallest statements that would move the bound

0. **(Direct-side Gram term; largest *reachable* lever.)** Prop. 15.2 without the $P_a^{1/6}$ term: $\sum_{q_m\ll Q}|A_m|^2\ll(Q/Y')(1+P_a^2/Y')Z^\epsilon$. Worth $0.874957\to0.86395$ now, $6/7$ with everything else ideal; even halving the exponent ($P_a^{1/12}$) gives $0.8696$. Whether the term is an artifact or intrinsic is examined in note J.
1. **(Floor cancellation; largest lever.)** For the compensated probe of §12 and the floor bin at $U=Z^h$: $\sum_{u\asymp U,\,u\text{ floor}}\mathrm{Row}_u(Z)\ll Z^{C(7/8)+C_0-fh+\epsilon}$ for some $f>0$. Each $0.01$ of $f$ is worth $\approx0.0025$ in $B$; $f=0.389$ with ideal counts is $3/4$.
2. **(Bias-corrected sextic sieve; bounded.)** Unconditional version of Dunn–Radziwiłł §9 with DFDH's Lindelöf-on-average replacing GRH: $\sum_a\mu^2(a)|\sum_bc_b(b/a)_3|^2=$ explicit main term $+O((A+B)(AB)^\epsilon\sum|\beta|^2)$ for $c_b=\tilde g(b)\beta_b$, $A\asymp B$. Re-run §19 with the bias row as a principal-type row. Ceiling $13/15$.
3. **(Quartic reflection; family change.)** Closed by note F: no quadratic-coupled reflection exists for the 4-fold cover, and the balanced bookkeeping gives $\sigma_0\ge1$. Retained as a useful failed approach.
4. **(Twisted Kubota double series; open.)** Meromorphic continuation and functional equations of $Z_\eta(s,w)$ above, with a convexity bound saving $Y^{-\kappa'}$ on the direct line; $\kappa'=l_y/4$ would give $\sigma_0\approx0.79$ at Part I.


## 7. The bootstrap barrier is not where it looks (notes/B_bootstrap_barrier.md)

- The only place $\kappa\ge3/4$ enters Lemma 18.1 numerically is the reflection/comparison margin at line 9652 ("$6\kappa-1\ge7/2$"); the same step works for every $\kappa>1/2$ with margin $M(1/6-1/(3(6\kappa-1)))$. The capacity coefficient $6\kappa$ is forced by the slot-removal ledger (18.38)–(18.39): removing length $d$ costs $\kappa d$ pointwise and lowers the affine excess by $6\kappa d$, so the ratio $1/6$ is $\kappa$-independent. **There is no better capacity than $2m+6\kappa z\le1$ in this proof, and no third stage: $\Phi(7/8)=0.8749570$, $\Phi(\Phi(7/8))=0.8749569$, fixed point $B_{\rm new}-6\times10^{-8}$.** Even feeding a hypothetical $\beta_*\le3/4$ ($\kappa=1/2$) into the unchanged lemma gives only $0.874708$.
- Lemma 17.1 (inverse second moment) and Lemma 17.6 (sixth-power amplification, slope $\alpha=5/6$ from the injectivity of $(u,a)\mapsto ua^6$) contain no zero-free input at all; the $11/12$ input of Part I is redundant once $7/8$ is known.
- The companion $11/12$ argument is rigid: $A_1(D)\ll D^{(1+\alpha)/2}=D^{11/12}$ with the same $\alpha$; no exponent in its recursion depends on $\beta_*$.
- Binding inequality: at the class $a\approx0.694$, $x=1/2$, $R_*=2/3$ makes $\partial_bE=R/2-1/3$ vanish; with the direct-estimate constraints this forces $B\ge(7+18\delta_c)/(9+18\delta_c)=B_{\rm new}$. The walls behind it, in order: floor bin counted with $R=1$ ($0.87236$); $C_0\le0$ together with the intermediate-row count $76/75-2\delta/3$ ($0.87004$); the direct cubic-theta bound $\ell\le1/5$ ($13/15$).

## 8. The 2k-th moment question (notes/H_2k_moment_model.md; note G pending)

Raising the plain witness to any power $k$ (a hypothetical Lemma 18.1(k) with capacity $km+6\kappa z\le1$) changes the bound by less than $10^{-5}$: the detector's adversarial split sits at $m^*\approx0.41\in(1/3,1/2]$, where only $k=2$ is admissible, and a fourth moment of the inverse witness applies only at $t=1$, where the plain count already reaches $1-\delta$. The generalized moment that would matter is a **mixed** one, the inverse witness against a longer selected-prime product (capacity $z\le c_I(1-r)$ with $c_I>1/2$: $0.87399$ at $c_I=0.6$, $0.87329$ at $3/4$), or a large-values inequality for the inverse witness at the spike $U^{\delta r/2}$ with $\delta r\approx0.28$. Both are zero-density statements for the sextic Kummer family at real part $\approx0.69$.

## 9. What the half-plane gives this repository unconditionally (notes/D_repo_consequences.md; all PROPOSED, IMPORTED hypothesis)

Hypothesis audit: no integrated statement has a hypothesis fully implied by the half-plane; two $\Theta$-parametrized records acquire numbers (wavelet energy abscissa $\Theta+1/2\le11/8$; the reciprocal-growth lemma R15 §1 now valid for every $a>7/8$), and every subpower RH-criterion in the record acquires a quantitative unconditional analogue at exponent $\Theta-1/2\le3/8$. Derived statements, each with a proof extract in note D:

- **Robin (Theorem A2).** $\sigma(n)/n\le e^\gamma\log\log n+C(\log\log n)^2(\log n)^{-1/8}$ for all $n\ge3$ (exponent $0.125043$ with Liu). Previously: Robin's $0.6483/\log\log n$ and the Vinogradov–Korobov-type $\exp(-c(\log\log n)^{3/5-\epsilon})$; under RH $\limsup\Delta(n)\sqrt{\log n}\le-1.393$. Via colossally abundant numbers, the Mertens identity $\log x\,E(x)-R(x)/x=\log x\,U(x)$ and Robin's convexity proposition. **Corollary A4:** if Robin's inequality fails at all, then $\Theta>1/2$ and $\limsup\log\Delta(n)/\log\log n=\Theta-1\in[-1/2,-0.125043]$; every hypothetical violation is a relative near miss of size $\le C\log\log n\,(\log n)^{-0.125043}$. (Theorem A3 reconstructs Robin's RH-false lower bound through Landau's theorem on the Mellin transform of $U$; theorem numbering in Robin 1984 unconfirmed.)
- **Mellin fixed detector (Theorems B1–B2).** With the repository's normalization (L-96000; $\mathcal MF_{5:3}(s)=6/s^2-3(2^{-z}-1)(2^{-z}-2)/(s^2\zeta(z))$, $z=s+1/2$): $|c_X(j)|,|F_{5:3}(X)|\ll X^{3/8+\epsilon}$, hence $N_F(Y)\ll Y^{3/8+\epsilon}$; and the quantitative consumer $N_F(Y)\ll Y^\theta\Rightarrow$ zero-free on $\Re s>1/2+\theta$, so the negative-mass exponent of the fixed detector is exactly $\Theta-1/2$. The open node `OPEN.ARITH.FIVE_THREE_NEGATIVE_MASS` is the assertion that this exponent is $0$; the gap is now the interval $(0,3/8]$.
- **SHARP (Theorem C1, Prop. C2, Remark C3).** Critical $\mathfrak H^{[1]}(x)\ll x^{3/8+\epsilon}$, so the critical negative mass and weighted variation are $\ll Y^{3/8+\epsilon}$; compact wavelet $G(X)\ll X^{3/8+\epsilon}$. The half-plane does not move the critical power $m=1$ (eventual positivity for $m>1$ is trivial since $B((m+1)/2)>0$). Side observation: the reviewed Euler-contraction proof's inequality holds for every real $m>1.8021$, not only $m\ge2$ (frozen source to be checked).
- **Xi/Pick (Theorems D1–D2, Prop. D3).** $\Re\,\xi'/\xi(s)>0$ on $\Re s>7/8$ (Lagarias positivity, unconditional there); the Nevanlinna–Pick kernel of that half-plane, $(F(s_i)+\overline{F(s_j)})/(s_i+\overline{s_j}-7/4)$, is PSD at all orders. The repository's kernel (denominator $s_i+\overline{s_j}-1$) stays RH-equivalent. Evaluation points $x>3/8$ are a priori zero-free; off-line poles are confined to $u\le9/64$; the order-three source theorem's reserve factor improves by $9/16$.
- **Other (Theorems E1–E2).** The corrected Euler product $\Pi_X(s)/C_X(s)\to\zeta(s)$ locally uniformly on $\Re s>7/8$ with rate $X^{7/8-\sigma}\log X$ (the half-plane part of OPEN_CUTS §6; identification with the causal correction needs the absent pass7 proof); $\sum_{n\le x}\mu(n)\chi(n)\ll q^\epsilon x^{7/8+\epsilon}$ uniformly (Dirichlet completion #736). The Siegel-exclusion theorem is logically a corollary of the half-plane with explicit $c=(\log3)/8$.

Formal status note: the comparator file `lean/ComparatorChallenges/QuasiRiemannHypothesis.lean` in `openai/math` is a statement with `sorry`; the independent rebuilds (tomoto0 and others) report the proofs in the main library (2,924 modules, axioms `propext`, `Classical.choice`, `Quot.sound` only). Both facts are recorded; neither is a review by this repository.

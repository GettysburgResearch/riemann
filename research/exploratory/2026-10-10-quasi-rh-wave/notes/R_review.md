# Note R: adversarial referee review of the 10 Oct 2026 quasi-RH wave notes

```text
Status: REVIEW (35-minute adversarial pass; nothing here is a new result)
Scope: FINDINGS.md; notes E, H, K, L; note D §0.2 (C1)–(C5), §2(a) A0–A2, §2(b) B1, §2(d) D1–D2
Primary sources checked: qrh_main.txt §20 (eq. (20.4)–(20.11)), Prop. 8.3 (eq. (8.3)–(8.4)), Prop. 15.2 (eq. (15.4)), Prop. 19.2 (eq. (19.2)); liu_2610.12234.txt intro, (18.2), (18.4)–(18.5), (24.1); dipp_2607.27131.txt Thms A–F, §10.6 eq. (38); qrh_1112.txt Cor. 1.2
What was actually run: one independent numpy evaluation of E(h;δ,x) and of the floor walls (scratchpad/chk/chk.py); everything else is reading and hand algebra
Verdict: no blocking error in the mathematics that is marked PROPOSED; one factual error (note L, VK comparison), one attribution gap (E is Liu's (18.5)), and one unreconciled set of "wall" numbers (13/15 / 0.8698 / 0.87004 / 0.87236) that FINDINGS presents inconsistently
```

Severity key: **blocking** = a stated claim is false or unsupported as written; **should fix** = correct in substance but misleading, inconsistent, or missing a load-bearing qualification; **minor** = wording/attribution/cosmetic.

---

## 1. Note E §1, FINDINGS §2: the endpoint exponent $E(h;\delta,x)$ and $C_0(b,\ell)$

**Claim.** Substituting $l_x=(1-b-\ell)/2$, $l_y=(1+b-\ell)/2$, $h=(1+b+3\ell)/2$, $B(\ell)=11/12-\ell/4$, $a=(1+\delta)/2$, $q=x\delta$ into the first line of eq. (20.4) at $d=h$ gives $E=C_0+\delta(\tfrac12+\ell)+x\delta\ell-h(1-R_*)$ with $C_0=-\tfrac14+\tfrac{5\ell}4+\tfrac b6$.

**Check.** First line of (20.4) (main paper, l. ~11460) at $d=h$, with $7/8$ replaced by the target $B(\ell)$:
$a-B(\ell)-h/6-al_y-\ell/2+q\ell+h+h\delta/2-h(1-R)$ (the $17/50$ cancels at $d=h$, as the note says). Constants: $-\tfrac5{12}-\tfrac1{12}-\tfrac14+\tfrac12=-\tfrac14$. $b$-terms: $-\tfrac b{12}-\tfrac b4+\tfrac b2=\tfrac b6$. $\ell$-terms: $\tfrac\ell4-\tfrac\ell4+\tfrac\ell4-\tfrac\ell2+\tfrac{3\ell}2=\tfrac{5\ell}4$. $\delta$-terms: $\tfrac\delta2-\tfrac{\delta(1+b-\ell)}4+\tfrac{\delta(1+b+3\ell)}4=\delta(\tfrac12+\ell)$. $q$-term: $x\delta\ell$. At $(1/8,1/6)$: $C_0=-1/48$, coefficients $2/3$, $1/6$ — matches the second line of (20.4). **Verified.**

The formula is, however, printed verbatim in Liu (18.5): $E_B(h)=-\tfrac14+\tfrac b6+\tfrac{5\ell}4+(\tfrac12+\ell)\delta+\ell\bar g-h(1-R)$, derived from his general (18.4) $E_B(d)=a-B+h(z_0-\tfrac16)-al_y-\tfrac\ell2+\bar g\ell+d(R+\tfrac\delta2-z_0)$, $z_0=17/50$. Note E's "Exact sources" lists only Liu's (0.1); FINDINGS §2 calls the system "reconstructed and verified". The independent content of note E is the numerical maximization and the dial table, not the formula.

Severity: **minor** (attribution). Correction: cite Liu (18.4)–(18.5) as the source of $E$ and $C_0$; describe note E as a *re-derivation from (20.4) that agrees with Liu (18.5)*.

Numerical checks reproduced independently: $\max_{\delta,x}E(1/8,1/6)=-2.2816\times10^{-4}$ at $(\delta,x)=(0.3864,1/2)$; $R_*(\delta_c,1/2)=2/3$ exactly from (18.2)/(24.1); paper's certificate $49/440640=1.112\times10^{-4}$ is the same quantity weakened by $J\le5/2$ (eq. (20.9)). **Verified.**

## 2. Note E §2, FINDINGS §2 (dial table, reading (ii)): "ideal counts $R_*=1-\delta$ ⇒ floor binds at $\ell=\tfrac15-\tfrac{2b}{15}$ ⇒ $B=13/15$"

**Algebra.** With $R_*=1-\delta$: $E=C_0+\delta\,(x\ell-\ell/2-b/2)$; the bracket is $\le-b/2<0$ for $x\le1/2$, so $\max_\delta E=E(0)=C_0$, and $C_0\le0\iff\ell\le\tfrac15-\tfrac{2b}{15}$, $B=\tfrac{13}{15}+\tfrac b{30}$. **Verified as algebra**, but:

(a) The infimum $13/15$ is at $b=0$, which Liu's system excludes ($b=l_y-l_x>0$ is a hypothesis; the model in `moment2k_v2.py` uses $b\ge0.002$). $13/15$ is an **infimum, not attained**; FINDINGS says "reaches exactly 13/15".

(b) More importantly, the quick_E model has **no floor bin**: its floor is the limit $\delta\to0$ with $R_*(0,x)=1$. The paper's floor bin is $a=51/100$, $\delta_0=1/50$, counted with $R=1$ and $q\le\delta_0/2$ (eq. (20.5): $E(h)\le C_0+\tfrac34\delta_0=-7/1200$). For general $(b,\ell)$ this is $C_0+\delta_0(\tfrac12+\tfrac{3\ell}2)\le0$, i.e. $\ell\le0.1875-0.1302\,b$, giving $B\ge0.869792$ at $b\to0$ — this is exactly the "$0.8698$" of FINDINGS §2b, and the "$0.869792$" in the $\alpha\to0$ row of its table. The $\delta_0=1/50$ floor is not cosmetic: Prop. 8.3 needs $\delta\ge1/50$ to force $m\le1/2+O(\epsilon)$, so lowering the floor to $1/2+\epsilon$ costs through the detector's losses; $13/15$ is only the $a_0\to1/2$ limit.

(c) Three different numbers are each called the "ideal-counts wall" in the same document: FINDINGS §2 table/(ii) → $13/15$; §2b → $0.8698$, then $13/15$ "+ floor $a_0\to1/2$"; §7 and note H §3 → $0.87236$ (floor bin), $0.87004$ (floor removed), $13/15$ (direct bound). I reconstructed all three: $0.87236$ = floor bin (20.5) **together with** the $b$–$\ell$ coupling constraint of `side_ok` ($(225\ell+50-75b)d+78\ell-49b-73<0$ at $d=0.75$), binding jointly at $b\approx0.078$, $\ell\approx0.1773$ (my value $0.87234$); $0.87004$ = $C_0\le0$ together with the same coupling constraint ($b\approx0.100$, $\ell\approx0.1866$; my value $0.87001$); $13/15$ = $C_0\le0$ alone, $b\to0$. So the hierarchy in note H / FINDINGS §7 is internally consistent, and FINDINGS §2 and §2b are the inconsistent ones (§2 omits the floor bin and the coupling constraint; §2b omits the coupling constraint, presumably because `exponent_model.py` idealizes the intermediate rows along with $R_*$).

Severity: **should fix**. Correction: in FINDINGS §2 replace "reaches exactly 13/15 … pinned by the floor … $C_0\le0$" by: "with ideal $R_*$ at $d=h$ the system is pinned by the paper's floor bin (20.5) at $0.8724$ (jointly with the intermediate-row/coupling constraint) or $0.8698$ (floor bin alone, $b\to0$); only if the floor is moved to $a_0\to1/2$ and $b\to0$ does the bound tend to $13/15$, where $C_0=0$ and the direct bound's $(5\ell-1)_+/8$ penalty of Liu Prop. 22.2 switches on." State once which model each number comes from.

## 3. FINDINGS §2 dial table, row "power saving $U^{-f}$ … $f=0.389$ ⇒ $3/4$"; note E §3

**Claim.** $B=3/4$ needs $\ell=2/3$ and a saving $U^{7/18}$ over the trivial floor sum.

**Check.** $C_0(0,2/3)=7/12$, $h=3/2$, $f\ge(7/12)/(3/2)=7/18$. **Verified as bookkeeping.** But at $\ell=2/3$: $l_x=(1-\ell)/2=1/6<\ell$, violating Liu's hypothesis $l_x,l_y>\ell$, and note E §4 itself says the model is invalid for $\ell\gtrsim0.3$. FINDINGS §2b independently states that with *every* count ideal the side constraints pin at $6/7$ and only dropping the second Gram term and the reflected penalty reaches $5/6$. The table row "3/4" therefore contradicts §2b unless labeled as "outside the model's validity".

Severity: **should fix**. Correction: mark the $f=0.389$ row "(formal; violates $l_x>\ell$ and the §2b side constraints — see §2b: $\ge6/7$ with all constraints)". Keep the per-$0.01$-of-$f$ sensitivity, which is computed inside the valid range.

## 4. FINDINGS §2: "Three independent re-optimizations (Liu, LW56e2, Gao) land at $7/8-4.3\times10^{-5}$; the estimate system is at its optimum"

Note C records Gao at $0.8749571516$ (differs from Liu by $8\times10^{-8}$; Gao's README says the adaptive stage is not Lean-checked) and LW56e2 at $0.8749570698$. All three re-tune the same two parameters under the same count $R_*$; agreement shows the same optimization was done correctly, not that the *estimate system* is optimal. Liu himself states optimality only as an "expectation" and proves (Prop. 25.1) a lower bound only under three explicit exponent constraints with $3/4\le\kappa\le1$, $1\le t\le3/2$.

Severity: **should fix** (overstatement). Correction: "…land at the same value; the two length parameters are at their optimum for the fixed count system (Liu, expectation + Prop. 25.1 under stated constraints)". "Independent" should be "separate".

## 5. Note H §1–2, FINDINGS §8: reading of Prop. 8.3 and "higher plain moments buy nothing"

**Reading of (8.3)–(8.4).** Statement: for every $t\in[1,3/2]$ there are $D=U^r$, $N=U^m$ with $r\le t$, $r+m\ge t$, $|M_rS_m|^2\gg U^{\delta(r+m)-\epsilon}$, and $t-\tfrac12\le r$, $m\le\tfrac12+O(\epsilon)$ (from $2\delta(m-1/2)_+\ll\epsilon$, using $\delta\ge1/50$). The pair is "selected separately for each row from $O(\log^2U)$ possibilities". So the split is row-determined and the count is applied per class; the max over classes is what enters (20.4). **Verified.** Note H's "$r\in[t-\tfrac12,\min(t,1)]$" omits $r\in(1,t]$, but those rows are routed to $L(t)$ in the same formula, so the model is complete. The reduction $m=t-r$ (instead of $m\ge t-r$) is justified because $F_I(r)=r+2xc_I(1-r)$ and $F_S(m)=2m+2xc(1-2m)$ are increasing in $r$, $m$ for $x\le1/2$ (slopes $1-2xc_I\ge1/2$, $2(1-2xc)\ge 2(1-2/9)$); this should be said. The formulas $F_I$, $F_S$ agree with Liu's $A_I(r)=1-\delta\{x+(1-x)r\}$ and $S_t(r)=1-\delta\{4x/9+(2-8x/9)(t-r)\}$. **Verified.**

**Does the conclusion follow?** Yes for this detector: adding $k\ge3$ changes $F_S$ only on classes with $m\le1/3$; the binding class at $(\delta_c,1/2)$ has $m^*\approx0.41$; the minimization over $t$ is already in $R_*$. Two things the note should add:
- $t>3/2$ is admissible for the detector itself (the $J=o(1)$ bound needs $-3+t(5/4-\sigma)<0$, i.e. $t<3/(5/4-\sigma)\approx4$, and $Y_*=U^{20}$ can be enlarged), but then $r\ge t-1/2>1$ for every split and $L(t)$ increases in $t$ since $\alpha>\delta$; so the range $[1,3/2]$ is without loss. State this rather than inheriting the paper's range.
- A fourth moment of the inverse witness: the note assumes capacity $2r\le1$ by analogy, which is a hypothesis, not a reading of any lemma; at $t=1$, $r=m=1/2$, $F_S(1/2)=1$ gives $1-\delta$ — **verified**, but label the capacity as hypothetical.

**Numbers.** The `moment2k_v2.py` baseline is $0.874973$ at active class $\delta=0.366$, $R_*=0.687$, versus Liu's exact $0.874957$ at $\delta_c=0.3886$, $R_*=2/3$. The discrepancy ($1.6\times10^{-5}$) is of the same order as the effect the table measures ("changes by less than $10^{-5}$"); its cause is the grid ($\delta$ step $\approx0.012$, $x$ on 11 points) missing the tangency at $\delta_c$. $R_*(0.366,1/2)=0.6874$ from (24.1) is consistent. The structural argument ($m^*>1/3$) is what carries the conclusion, not the table.

Severity: **should fix** (label the grid resolution; add the two justifications). Also **minor**: "$R_*=0.667$, the paper's value" — it is Liu's (24.1) value at $\delta_c$, not a number in the OpenAI paper.

## 6. Note D (C1): $\psi(x)=x+O(x^\Theta\log^2x)$, effective

Truncated explicit formula at $T=x$: error $x\log^2x/T=\log^2x$; $\sum_{|\gamma|\le T}|x^\rho/\rho|\le x^\Theta\sum|\gamma|^{-1}\ll x^\Theta\log^2T$ (zeta's zeros have $|\gamma|\ge14$, so no small-$|\rho|$ issue). Constants effective since the half-plane is uniform. $\theta$ from $\psi$ with $\Theta\ge1/2$. **Verified.** (Minor: "Chebyshev" is an odd label; "PNT with power error" is what it is.)

## 7. Note D (C5), note L §1: $\log\zeta(\sigma+it)\ll(\log t)^{(1-\sigma)/(1-\Theta)+\epsilon}$, $\mu(\sigma)=0$ for $\sigma>7/8$

**Exponent.** Correct. The linear exponent is the three-lines form: apply Phragmén–Lindelöf to $\log\zeta(s)\,(\log(-is))^{-L(s)}$ with $L$ affine, $L(\Theta+\delta)=1$ (Borel–Carathéodory gives $\log\zeta\ll\log t$ on $\Re s\ge\Theta+\delta$), $L(1+\eta)=0$. Titchmarsh 14.2 is the $\Theta=1/2$ case, exponent $2-2\sigma$. Plain three circles centred at $2+it$ gives the weaker $\log(2-\sigma)/\log(2-\Theta)$ (e.g. $0.55$ vs $0.5$ at $\sigma=3/4$, $\Theta=1/2$); the linear exponent needs circles with centre $\to+\infty$ or three lines. **Verified**, wording "three circles" is loose but the stated exponent is right. The uniform-in-$q$ version (iii) is fine: the big disk must avoid $s=1$ for principal $\chi$ (take $|t|\ge2$) and the zeros of imprimitive $L$ on $\Re s=0$ lie outside $\Re s\ge\Theta+\delta$.

**"New unconditionally".** Correct. Best previously available at $\sigma=7/8$: convexity from Bourgain's $\mu(1/2)\le13/84$ gives $\mu(7/8)\le13/336=0.0387$ (the note's number is right); exponent pairs give no better ($(9/56,37/56)$: $k(1-\sigma)/(1+k-l)=9/224=0.0402$; $(1/2,1/2)$: $1/16$); Ford's explicit $\mu(\sigma)\le4.45(1-\sigma)^{3/2}$ gives $0.197$ and beats the linear bound only for $1-\sigma<0.005$. No unconditional $\mu(\sigma)=0$ was known for any $\sigma<1$. By convexity of $\mu$, also $\mu(7/8)=0$ (not only $\sigma>7/8$).

Severity: **minor**. Correction: say "Borel–Carathéodory + Phragmén–Lindelöf on the strip (Titchmarsh 14.2 form)"; add "$\mu(7/8)=0$ by convexity"; record the best prior bound $\approx0.0387$.

## 8. Note L §1, "for small heights nothing changes: the VK region is wider than $\sigma>7/8$ for $t<\exp((8c)^{3/2}\cdot)$, roughly $t\lesssim e^{10^3}$"

**Problem: false.** The VK region $\sigma\ge1-c(\log t)^{-2/3}(\log\log t)^{-1/3}$ exceeds width $1/8$ iff $(\log t)^{2/3}(\log\log t)^{1/3}<8c$. With Ford's explicit $c=1/57.54$, $8c=0.139$, which fails for every $t\ge3$ (width $0.0106$ at $t=10$, $0.0038$ at $t=10^3$, $0.0013$ at $t=10^{12}$); even the classical $1-1/(5.56\log t)$ beats $1/8$ only for $t<4.2$. With a hypothetical $c=1$ the crossover is $t<e^{22.6}\approx7\times10^9$, inside the Platt–Trudgian range $|t|\le3\times10^{12}$. "$e^{10^3}$" would need $c\approx12.5$.

Severity: **should fix** (factual error in a side remark). Correction: "No classical zero-free region is ever wider than $1/8$ beyond $t\approx5$; low heights are covered only by the numerical verification $|t|\le3\times10^{12}$, which is where the half-plane adds nothing."

## 9. Note D (C4), note L §2: $\psi(x;q,a)=x/\varphi(q)+O(x^{7/8}\log^2x)$ uniformly for $q\le x$

**Bookkeeping.** For primitive $\chi^*$ mod $q^*$: Davenport's formula $\psi(x,\chi^*)=-\sum_{|\gamma|<T}x^\rho/\rho+O(x\log^2(qx)/T)+O(x^{1/4}\log x)+(\text{constant terms})$, with $b(\chi)=-\sum_{|\gamma|<1}1/\rho+O(\log q)$. Since all nontrivial zeros of primitive $L$ satisfy $1/8\le\beta\le7/8$ (functional equation + I1), $|\rho|\ge1/8$ and the $|\gamma|<1$ block is $\sum(x^\rho-1)/\rho\ll8x^{7/8}N(1,\chi)\ll x^{7/8}\log q$ — **no small-$|\rho|$ problem**; the $|\gamma|\ge1$ block is $\ll x^{7/8}\log(qT)\log T\ll x^{7/8}\log^2x$ for $q,T\le x$. Imprimitive $\chi$: $\psi(x,\chi)-\psi(x,\chi^*)\ll\omega(q)\log x\ll\log q\log x$, so the zeros on $\Re s=0$ never enter (the explicit formula is applied to $\chi^*$). Principal character: $\psi(x,\chi_0)=\psi(x)+O(\log q\log x)$ and (C1). Orthogonality gives the claim with an absolute effective constant; $\pi(x;q,a)$ error $x^{7/8}\log x$ by partial summation. **Verified.** Consistent with qrh_1112 Cor. 1.2 ($11/12$ form, "absolute and effective").

Note L's phrasing "with all zeros in $1/8\le\Re\rho\le7/8$" should say "for primitive characters; imprimitive ones by the Euler-factor difference" (note D says this; note L does not).

**Linnik remark.** "the half-plane … makes the weaker bound effective and elementary" is misleading: Linnik's theorem (Xylouris $L\le5$) is already effective; the half-plane gives a weaker exponent $8+\epsilon$ with a shorter proof. Severity: **minor**. Correction: drop "effective", keep "elementary/short".

## 10. Note D §2(a): Lemma A0, Prop. A1, Theorem A2 (Robin)

**Lemma A0 structure claims.** (i) $a_p\ge k$ iff $p^\epsilon\le1+1/(p+\dots+p^k)$: checked from $\sigma(p^k)/\sigma(p^{k-1})=(p^{k+1}-1)/(p^k-1)$. Monotonicity in $p$, $k$; $\epsilon<1/(x\log x)$ from $a_x\ge1$; $\epsilon>1/(3x\log x)$ from $a_{x'}=0$ and Bertrand; (i') $p^k\le x/4\Rightarrow a_p\ge k$ via $\epsilon\log p<1/x\le1/(4p^k)\le\log(1+1/(2p^k))$ and $p+\dots+p^k\le2p^k$; (ii) $a_p\ge2\Rightarrow p^2<3x\log x$ and $a_p\le\log(3x\log x)/\log p+1$. **All verified.** (1): $M=\gamma-\sum_p\sum_{k\ge2}(kp^k)^{-1}$ used correctly; second sum $O(x^{-1/2}/\log x)$ correct. (2): $\sum(a_p-1)\log p\ll\sqrt{x\log x}$ (the written $\pi(3\sqrt{x\log x})$ is a typo for $\pi(\sqrt{3x\log x})$, harmless). (3): the error $O(x^{2\Theta-2}\log^5x)$ is generous ($\log^4$ suffices). (C3) identity re-derived: $E(x)=R(x)/(x\log x)+U(x)$ with $M=1/\log2-\log\log2+\int_2^\infty R(t)(1+\log t)t^{-2}\log^{-2}t\,dt$; hence $\log x\,E-R/x=\log x\,U$. **Verified.** (4): $U\ll x^{\Theta-1}\log x$ from $R(t)\ll t^\Theta\log^2t$. **Verified.**

**Prop. A1.** Common $\epsilon$ at the transition; $\log I(n)\le\ell(\log n)$ affine; $h(u)=e^{\ell(u)}-e^\gamma\log u$ convex; endpoint values are $\Delta(N')$, $\Delta(N'')$. This is Robin (1984) Prop. 1 in additive form. **Verified.**

**Theorem A2.** "$P^+(N'')\le2P^+(N')$ because $p\mapsto\log(1+1/p)/\log p$ is injective": the injectivity only excludes two *new* primes entering at the same $\epsilon$; a coincidence between a new prime's critical $\epsilon$ and an exponent increase of an old prime is not excluded unconditionally (Alaoglu–Erdős; four-exponentials territory). That coincidence is irrelevant here, since $a_p$ is nonincreasing in $p$ forces the new prime to be the next prime $\le2x$. The sentence is correct, the stated reason is incomplete. "$\log N''\le3\log N'$" **verified** from A0(2). Final inequality: needs $(\log N')^{\Theta-1}\le3^{1-\Theta}(\log n)^{\Theta-1}$ (since $N'\le n\le N''\le N'^3$) and $(\log\log N'')^2\le3(\log\log n)^2$; the text's "$\le3C_0$" is correct but the monotonicity direction (the bound is *larger* at the smaller $N'$) should be spelled out. **Verified.**

**$(\log\log n)^2$ factor.** One $\log x$ from $\log x\cdot U(x)$, one from $R(t)\ll t^\Theta\log^2t$; it is what the method gives, and the note does not claim it is needed. **OK.** The second form $C_\epsilon(\log n)^{-1/8+\epsilon}$ is immediate. "First power-of-$\log n$ upper bound": correct *given* I1, but the route is Robin's own; the novelty is entirely in the imported input. Severity: **minor**. Correction: "first … as a consequence of any zero-free half-plane; the only new ingredient is I1".

## 11. Note D §2(d): Theorems D1, D2

**D1.** $\xi'/\xi(s)=\sum_\rho1/(s-\rho)$ in conjugate (or $\rho\leftrightarrow1-\rho$) pairs is the Hadamard product with $B=-\sum\Re(1/\rho)$ absorbed; each symmetric partial sum has real part $\sum(\sigma-\beta)/|s-\rho|^2$, a sum of positive terms converging absolutely ($\ll\sum(t-\gamma)^{-2}$). So $\Re\,\xi'/\xi>0$ on $\Re s>7/8$. **Verified.** ("In particular $\xi(s)\ne0$ there" restates the hypothesis.) Lagarias 1999 equivalence on $\Re s>1/2$: correctly cited.

**D2.** For $\Pi=\{\Re s>c\}$ and $F$ holomorphic with $\Re F>0$, the Riesz–Herglotz representation after $w=s-c$ (or the Cayley transform to the disk) gives $\dfrac{F(s_i)+\overline{F(s_j)}}{s_i+\overline{s_j}-2c}=\alpha+\int\dfrac{d\mu(\lambda)}{(w_i-i\lambda)\overline{(w_j-i\lambda)}}$, PSD for every finite $N$; no growth condition is needed. With $c=7/8$ the denominator is $s_i+\overline{s_j}-7/4$. **Verified**, "all orders" = all finite $N$. The boundary remark (kernel with $-1$ not implied; the multiplier $1-\tfrac34/(s_i+\overline{s_j}-1)$ is "1 minus PSD") is correct.

## 12. Note L §3: Soundararajan's inequality and a zero-density rescue

The displayed inequality is Sound (2009) Prop. 1 (valid for $\lambda\ge\lambda_0=0.4912$) and the description of the proof's use of the sign of $(\sigma-\beta)/|s-\rho|^2$ is accurate. The "$T^{1-c\eta}$" is Selberg's $N(\sigma,T)\ll T^{1-(\sigma-1/2)/4}\log T$; with $\eta\asymp1/\log x$ there is no saving. **Verified.**

**Error:** "the trivial bound $|\zeta|^{2k}\ll T^{k/6+\epsilon}$" should be $T^{k/3+\epsilon}$ (Weyl, $\mu(1/2)\le1/6$) or $T^{13k/42+\epsilon}$ (Bourgain). Severity: **minor** (strengthens the point).

**Concrete rescue attempt (fails).** Fix $\eta>0$. On the set $G_\eta$ of $t$ with no zero $\beta>1/2+\eta$, $|\gamma-t|\le1$, Sound's argument gives the inequality with $\sigma$ shifted to $1/2+\eta$ at the cost of a factor $t^{\eta}$ in $|\zeta|$, i.e. $T^{1+2k\eta+\epsilon}$ for the $2k$-th moment on $G_\eta$; on the complement, of measure $\ll T^{1-\eta/4}\log T$, the pointwise bound gives $\ll T^{1-\eta/4+13k/42+\epsilon}$. Neither is $\ll T^{1+\epsilon}$ for any $k\ge1$ and any $\eta\in(0,3/8]$. Independently, $\int_0^T|\zeta(1/2+it)|^{2k}dt\ll T^{1+\epsilon}$ for *all* $k$ is equivalent to the Lindelöf hypothesis (Hardy–Littlewood), and for a single $k>2$ the best unconditional bound is $T^{5/4+\epsilon}$ at $k=3$ (Hölder between the 4th and Heath-Brown's 12th moment). So the note's conclusion is right; it should state the two sentences above instead of "far too small".

Severity: **minor** (make concrete).

## 13. Note K: literature readings

Checked against DIPP: $A_3=1/3$, $A_r=1/2$; error $X^{(r+A_r)/(r+1)+\epsilon}=X^{5/6+\epsilon}$ at $r=3$; Remark 1.1.3 (GRH $\Rightarrow X^{3/4+\epsilon}$; Heath-Brown's $(AB)^{2/3}$; DFDH sharpness); Theorem B second-order term captured only for $r=3$; Theorem C proportion $1/12-\epsilon$ at $r=3$; eq. (38) $\theta_1=1/11$ with $\tilde\delta_1=5/6$. **All verified.**

**Garbled:** "(Theorems D–E): sharper errors $X^{(3r-2)/(4r-2)+\epsilon}$ (second moment; $5/6$ again at $r=3$… $=7/10$ for $r=3$)". DIPP §10.6.1: $\delta_0=(3r-2)/(4r-2)=7/10$ at $r=3$ is the error exponent of Theorem D, and the *captured* second-order term is $X^{1/2+1/r}=X^{5/6}$ ($\tilde\delta_0=1/2+1/r$ for $r=3,4$). Severity: **minor**. Correction: "error $X^{7/10+\epsilon}$ at $r=3$, with the $X^{5/6}$ secondary term made explicit".

**Overstatement (§2):** "Lemma 18.1 with $m=1/2$, $z=0$ is a Lindelöf-on-average fourth moment of the sextic Kummer family on the critical line". It is a fourth mean value of length-$U^{1/2}$ Dirichlet polynomials at the shifted point (after central normalization), with rows inducing in $\Theta$ excluded; it is the standard mean-value ingredient, not a fourth moment of $L(1/2,\psi_u)$ (no approximate functional equation / off-diagonal evaluation). Severity: **should fix** (wording; the comparison "stronger than anything in the asymptotic-moment literature" rests on it).

## 14. Note D §2(b) Theorem B1

Mellin inversion on $\Re s=3/4$ (transform $\ll|s|^{-2}$ since $\Re z=5/4$); shift to $\Re s=\Theta-1/2+\delta>0$, which avoids the double pole at $s=0$ and stays zero-free since $\Re(s+1/2)\ge\Theta+\delta$; (C5) gives $(2+|t|)^{-2+\delta}$ decay; horizontal segments vanish. **Verified** modulo the imported identity $\mathcal Mc_\cdot(j)(s)=C_j/s^2+P_j(s+1/2)/(s^2\zeta(s+1/2))$ (L-96000, not re-derived here). The $5P_2+3P_3=-3(2^{-z}-1)(2^{-z}-2)$ identity: with $P_2=2\cdot2^{-z}-1-3^{-z}$ and $P_3=\tfrac53 3^{-z}-4^{-z}-\tfrac13-\tfrac13 2^{-z}$, $5P_2+3P_3=9\cdot2^{-z}-6-3\cdot4^{-z}=-3(4^{-z}-3\cdot2^{-z}+2)=-3(2^{-z}-1)(2^{-z}-2)$. **Verified.**

## 15. Consistency of numbers and other remarks

- $\delta_c=(49-\sqrt{921})/48=0.38858$, $\ell_{\rm new}=(5-6\delta_c)/(9+18\delta_c)=0.16684$, $B=(7+18\delta_c)/(9+18\delta_c)=0.874957$, $\partial_bE=R_*/2-1/3$: all **verified** against Liu.
- "$0.874957$ vs $0.874973$": see item 5 (grid resolution of `moment2k_v2.py`). FINDINGS §8 inherits the "$<10^{-5}$" phrasing; say "no change at grid resolution $\sim2\times10^{-5}$; structurally zero".
- "$13/15$ vs $0.8698$ vs $0.87004$ vs $0.87236$": see item 2; each is a different constraint set and FINDINGS §2/§2b/§7 do not say so.
- FINDINGS §2(iii) "under GRH for the family every row is a floor row, so the $13/15$ wall is an absolute-value wall": with the paper's floor bin the GRH-wall is $0.8698$ (or $0.8724$), not $13/15$; same correction as item 2.
- Note L defines $\Theta$ as the sup over *all Dirichlet* $L$-functions, note D as the sup over zeta's zeros; (C1)–(C3) use the latter, the $q$-uniform statements the former. **Minor**: use two symbols or say which is meant.
- Note L §1(ii) "no new density consequence": $N(\sigma,T)=0$ trivially implies the density hypothesis on $\sigma>7/8$; say "trivial there, nothing below $7/8$". **Minor.**
- Note D Observation 0.1: $(\log3)/8=0.1373$. **Verified.** (C2), (C3) as used in A0/C1: **verified** (C3 identity re-derived above).
- FINDINGS §9 Robin bullet: numbers $0.125043=1-0.874957$ and the comparison list are consistent with note D.
- Attribution "an independent public verification repository reports the same density barrier" (FINDINGS §2(ii)): note C names tomoto0's repository; its "$\sigma_0>13/15$ with density-hypothesis-strength counts" is the same no-floor-bin computation as note E (item 2), so it is corroboration of the arithmetic, not independent evidence about the architecture. **Minor**: say so.

## 16. Summary of required corrections (by priority)

1. **should fix** — FINDINGS §2 (table row "ideal counts → 13/15", reading (ii)/(iii)) and §2b vs §7/note H: reconcile the ideal-count walls ($0.8724$ with floor bin + coupling; $0.8698$ floor bin alone; $0.87004$ $C_0\le0$ + coupling; $13/15$ = $C_0\le0$, $b\to0$, floor $a_0\to1/2$); say "infimum", not "exactly"; name the model behind each number.
2. **should fix** — FINDINGS §2 table "$f=0.389\Rightarrow3/4$": outside model validity ($l_x<\ell$); reconcile with §2b's $6/7$.
3. **should fix** — note L §1: delete the VK "$t\lesssim e^{10^3}$" sentence (false for every explicit constant); replace by the numerical-verification statement.
4. **should fix** — FINDINGS §2 "three independent re-optimizations … system at its optimum": weaken to "two parameters at optimum for the fixed count system (Liu's expectation; Prop. 25.1 under stated constraints)".
5. **should fix** — note H: state the monotonicity justification for $m=t-r$, the $t>3/2$ argument, label the inverse-4th-moment capacity as hypothetical, and label the $0.874973$ baseline as grid-limited.
6. **should fix** — note K §2: "fourth moment on the critical line" → "fourth mean value of length-$U^{1/2}$ polynomials".
7. **minor** — attribute $E$, $C_0$ to Liu (18.4)–(18.5); $T^{k/6}\to T^{k/3}$; DIPP Theorem D exponents; Linnik "effective"; $\mu(7/8)=0$ by convexity and best prior $13/336$; A2 proof wording (injectivity reason, monotonicity direction); $\Theta$ symbol clash; D1 "$\xi\ne0$ there" is a restatement.

Nothing reviewed is blocking: every mathematical statement marked PROPOSED in notes D and L that I checked (C1, C4, C5, A0, A1, A2, B1, D1, D2) is correct as a deduction from the imported half-plane, with the proof-text corrections above.

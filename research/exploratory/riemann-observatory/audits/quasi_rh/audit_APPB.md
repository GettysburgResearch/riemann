# Level-2 audit of Appendix B (separation of smooth weights) and of the Outline's consistency with the proof

```text
Status: Level-2 audit of one section, done independently. It is not a review of the whole paper and does not certify the paper.
Scope: paper2.tex l.3481-3988.
         - Appendix B: Lemma B.1 (l.3491-3524); the R-form (eq:smooth-pointwise), (eq:smooth-weight-bound) (l.3526-3556);
           Lemma B.2 (l.3558-3615); Lemma B.3 (l.3617-3650); the bibliography (l.3652-3987).
         - The four places where Appendix B is used:
             Prop. 4.5, l.1191-1245;
             Lemma 6.6, l.2111-2147;
             Lemma 7.1, l.2315-2346;
             Lemma 7.3, l.2602-2651.
         - The Outline (Sec. 2, l.206-659), compared line by line with Secs. 3-7 and App. A
           (statements read: l.660-1252, l.1254-1629, l.1632-2214, l.2217-2683).
Exact sources: github.com/openai/math @ 4eaee87548250b2682affda7d05d947c05554bae,
       preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/paper2.pdf
       (sha256 f919b57829b178c8e60e7c17b018cf773e7907cf642ef5a3347d8a826e8dbf18, re-hashed: matches).
       LaTeX source tex1112/paper2.tex (sha256 d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d, 3988 lines) is
       authoritative. The PDF text of App. B (sec_appB_separation.txt) was compared with the tex and matches. In the PDF,
       (eq:smooth-separation)...(eq:kernel-bilinear-integral) are (B.1)-(B.5).
       Imported statements checked against the original texts (arXiv PDFs, cached by tools/fetch_arxiv_text.sh):
         - BGL = arXiv:1112.1650 (sha256 1ab29e36...303b): Thm 1.3, Sec. 3.2;
         - GL = arXiv:1112.1642 (sha256 5cc5f033...d304): Def. 1, Thm 1.1, Cor. 1.2, Thm 4.1, Lemma 4.4;
         - PY19 = arXiv:1608.06854 (sha256 ee1f58f2...d1ea): Sec. 10.1.
What was actually run (our own code, python3 -I; nothing from the OpenAI repository was run or imported):
       experiments/code/quasi_rh/appB_outline_checks.py  (sha256 bba15c23cf1f88226a4715b3947a9dedce6f100989ae0e4e879d8478ea778844)
       -> appB_outline_checks.out (25 checks, 0 failures, ~30 s).
       The Lean formalization of the 7/8 companion was NOT replayed.
Smallest remaining gap: none inside Appendix B or the Outline.
       Appendix B consists of standard, complete arguments (Mellin/Fourier separation plus Cauchy-Schwarz).
       Every one of its four uses meets its hypotheses.
       The Outline asserts nothing that the detailed sections do not prove. The six presentation differences are listed in Sec. 4.
```

## 0. Verdict

**Appendix B is correct.** All three lemmas are standard and their proofs are complete.

- **Lemma B.1** is Fourier inversion in logarithmic coordinates, with the $(1-\Delta)^{q/2}$ coefficient bound.
- **The R-form (eq:smooth-pointwise)** follows from the chain rule $\partial_y F(Re^{a\cdot y})=a\,(u\partial_uF)(Re^{a\cdot y})$.
- **Lemma B.2** combines a Mellin representation through the test functions $U_t=Vx^{it}$, a coefficient majorant uniform in the row, Cauchy–Schwarz in $r$, and $q=2m+4>2m+2$.
- **Lemma B.3** is weighted Cauchy–Schwarz.

We re-derived each step by hand and checked the load-bearing identities and inequalities numerically (§3, checks A1–A7).

**All four applications satisfy the hypotheses exactly.** In each case we checked:

- the support intervals ($I\subset\operatorname{int}I_*$);
- the row sets and weights ($|c_r|\le w_r$, after harmless rescaling);
- the row-dependent evaluation points;
- the uniform kernel bounds;
- the derivative-order bookkeeping ($J\to2J+4$ in Prop. 4.5; $j\to2j+4$ and $m\to2m+4$ in Sec. 7, hence $4m+12$ in Prop. 5.4).

**The Outline is consistent with the detailed proof.** Each displayed claim of Steps 1–5 is a special case or schematic of a precisely proved statement (the table in §2). Where the Outline is formally stronger, the difference is a free parameter or suppressed bookkeeping: $(\mathcal HX)^\varepsilon$ in place of $D^\varepsilon$, and $D^{-2\vartheta}$ in place of $D^{-\vartheta}$. The paper itself announces this suppression (l.208-210, l.639-650).

We independently verified the Outline's arithmetic identities (§3, checks B1–B4) and its scale and exponent algebra (C1–C9).

We found no verified error, no suspected gap, no missing hypothesis and no unresolved ambiguity of mathematical weight. The presentation points are listed in §4.

---

## 1. Appendix B, claim by claim

Notation: $N=\mathrm N_{K/\mathbb Q}$. $\|\cdot\|_{C^q}$ is the maximum of all partial derivatives of total order $\le q$; it is defined only at l.1016-1019, inside Prop. 4.5 (see APPB-P3).

### 1.1 Lemma B.1 (l.3491-3524)

**Claim.** Fix a box $\mathcal I=\prod I_j\subset(0,\infty)^d$ of compact intervals. Every $\mathcal K\in C_c^\infty$ supported in $\mathcal I$ satisfies $\mathcal K(\mathbf x)=\int b(\mathbf t)\prod x_j^{it_j}\,d\mathbf t$. For $J\ge0$ and every even $q>J+d$,
$$\int|b|(1+|\mathbf t|)^J\ll_{\mathcal I,J,q,d}\|\mathcal K\|_{C^q(\mathcal I)}.$$

**Checks.**

- **Normalization.** $b(\mathbf t)=(2\pi)^{-d}\int\mathcal K(e^{\mathbf y})e^{-i\mathbf t\cdot\mathbf y}d\mathbf y$ is the convention whose inverse is $\int b\,e^{i\mathbf t\cdot\mathbf y}d\mathbf t$. Since $\mathcal K\circ\exp\in C_c^\infty(\mathbb R^d)$, $b$ is Schwartz. Inversion holds pointwise for **all** $\mathbf x>0$, not only on the box; the proof of B.2 uses this.
- **Change of variables.** $\partial_{y_j}=x_j\partial_{x_j}$. Hence every $\mathbf y$-derivative of order $\le q$ is a combination of $\mathbf x^\alpha\partial^\beta\mathcal K$ with $|\beta|\le|\alpha|\le q$. On $\mathcal I$, $\mathbf x$ is bounded above. The map $\log$ needs $\mathcal I$ bounded away from 0, which gives the compact log-box of fixed measure. So $\|\mathcal K\circ\exp\|_{C^q}\ll_{\mathcal I,q}\|\mathcal K\|_{C^q(\mathcal I)}$.
- **Pointwise bound.** For $q$ even, $(1+|\mathbf t|^2)^{q/2}b(\mathbf t)=(2\pi)^{-d}\int[(1-\Delta)^{q/2}(\mathcal K\circ\exp)]e^{-i\mathbf t\cdot\mathbf y}$. This gives $|b(\mathbf t)|\le(2\pi)^{-d}\|(1-\Delta)^{q/2}\mathcal K\circ\exp\|_{L^1}\,(1+|\mathbf t|^2)^{-q/2}$. Use $(1+|\mathbf t|^2)^{q/2}\ge2^{-q/2}(1+|\mathbf t|)^q$.
- **Integration.** $\int(1+|\mathbf t|)^{J-q}d\mathbf t<\infty$ if and only if $q>J+d$. Correct.
- **Numerics.**
  - A1: the representation reconstructs a 2-D kernel to $3.7\cdot10^{-12}$ at 400 random points, including points outside the box.
  - A2: the exact inequality $\max|b|(1+|\mathbf t|^2)^{q/2}\le\|(1-\Delta)^{q/2}\mathcal K\circ\exp\|_{L^1}$ (periodic normalization) holds for $q=2,4,6$.

**Verdict: correct.**

### 1.2 The R-form, (eq:smooth-pointwise) and (eq:smooth-weight-bound) (l.3526-3556)

**Claim.** Let $\mathcal K_R=\prod W_j(x_j)\,F(R\prod x_j^{a_j})$, with $\|F\|_{A,q}=\max_{m\le q}\sup_u(1+u)^A|(u\partial_u)^mF|$. Then
$$|b_R(\mathbf t)|\ll(1+R)^{-A}(1+|\mathbf t|)^{-q}\|F\|_{A,q}\prod\|W_j\|_{C^q},$$
with constants depending only on $A,J,q,d,(I_j),(a_j)$.

**Checks.**

- **Chain rule.** In log coordinates, $\partial^\beta_{\mathbf y}F(Re^{\mathbf a\cdot\mathbf y})=\mathbf a^\beta\,((u\partial_u)^{|\beta|}F)(Re^{\mathbf a\cdot\mathbf y})$.
- **Size of the argument.** On the box, $u=Re^{\mathbf a\cdot\mathbf y}\in[c_1R,c_2R]$ with $c_i=c_i(\mathcal I,\mathbf a)>0$. So $(1+u)^{-A}\le\max(1,c_1^{-A})(1+R)^{-A}$.
- **Leibniz.** Each term is bounded by $\prod_j\|W_j\|_{C^{\beta_j}}\le\prod_j\|W_j\|_{C^q}$.
- **Uniformity.** The bound is uniform in $R>0$. The degenerate case $\mathbf a=0$ is included.
- **Numerics.**
  - A3: for $F(u)=u^{1/4}(1+u)^{-A-1/4}$ with $A=2$, the quantity $\sup_t|b_R|(1+|t|)^2(1+R)^A$ stays in $[4.6,14.4]$ for $R\in[10^{-3},10^4]$.
  - The negative control with $(1+R)^{A+1}$ grows by a factor $8.8\cdot10^2$, as it must.

**Verdict: correct.** (eq:smooth-weight-bound) is never cited; see APPB-P1.

### 1.3 Lemma B.2 (l.3558-3615)

**Claim.** Fix compact $I\subset\operatorname{int}I_*\subset(0,\infty)$ and $m\ge0$. Consider finite sums $S_{j,r}(U)=\sum_na_{j,r}(n)U(x_{j,r,n})$ over finitely many rows, with weights $w_r\ge0$. Suppose
$$\sum_rw_r|S_{j,r}(U)|^2\le M_j\|U\|^2_{C^m(I_*)}\qquad\text{for all }U\in C_c^\infty(I_*).$$
Then for $|c_r|\le w_r$ and smooth $\mathcal K_r$ supported in $I^2$,
$$\Big|\sum_rc_r\sum_{n_1,n_2}a_{1,r}\overline{a_{2,r}}\,\mathcal K_r\Big|\ll_{I,I_*,m}\sqrt{M_1M_2}\,\sup_r\|\mathcal K_r\|_{C^{2m+4}(I^2)}.$$

**Step-by-step checks.**

1. **Representation.** Apply Lemma B.1 with $d=2$ and $\mathcal I=I^2$, and substitute $t\to-t$. Then $\mathcal K_r(x,y)=\iint b_r(s,-t)x^{is}y^{-it}$ for **all** $x,y>0$. Choose $V$ real, $V\in C_c^\infty(\operatorname{int}I_*)$, $V\equiv1$ on $I$ (possible because $I\subset\operatorname{int}I_*$). Then $V(x)V(y)\mathcal K_r(x,y)=\mathcal K_r(x,y)$ everywhere, and $V(y)y^{-it}=\overline{U_t(y)}$ because $V$ is real. Hence $\mathcal K_r=\iint\tilde b_r(s,t)U_s(x)\overline{U_t(y)}$. Correct.
2. **Interchange.** The $n$-sums and $r$-sums are finite and $\iint|\tilde b_r|<\infty$, so Fubini applies. The coupled sum equals $\iint\sum_rc_r\tilde b_r(s,t)S_{1,r}(U_s)\overline{S_{2,r}(U_t)}$. Verified numerically in A4, with row-dependent points $x_{j,r,n}$ and kernels: relative error $3.8\cdot10^{-11}$.
3. **Uniform majorant.** $B(s,t):=\sup_r|\tilde b_r(s,t)|\ll_{I,q}\sup_r\|\mathcal K_r\|_{C^q(I^2)}(1+|s|+|t|)^{-q}$, using $|(s,t)|\ge(|s|+|t|)/\sqrt2$. The supremum is over a finite set, so it is measurable.
4. **Cauchy–Schwarz in $r$.** $|c_r\tilde b_r|\le w_rB$. Then $\sum_rw_r|S_1(U_s)||S_2(U_t)|\le\sqrt{M_1M_2}\,\|U_s\|_{C^m}\|U_t\|_{C^m}$. Verified in A4b: the numerical majorant chain holds, $|\mathrm{LHS}|=1.26\le91.8$.
5. **Test-function norms.** $\partial_x^j[V(x)x^{it}]=\sum_k\binom jkV^{(j-k)}(it)_kx^{it-k}$, and $x$ is bounded away from 0 on $I_*$. So $\|U_t\|_{C^m(I_*)}\ll_{I,I_*,m}(1+|t|)^m$ (A5). The hypothesis must hold for the complex-valued $U_t$. If it were stated only for real $U$, splitting into real and imaginary parts would cost a factor at most 4 in $M_j$ (APPB-P2).
6. **Convergence.** $(1+|s|)^m(1+|t|)^m\le(1+|s|+|t|)^{2m}$. So the integral in (eq:kernel-bilinear-integral) is $\le\iint(1+|s|+|t|)^{2m-q}$, which is finite if and only if $q>2m+2$. $q=2m+4$ is even, as the pointwise bound requires.
   - A6 confirms finiteness and stability under truncation. For $m=0$ the value is $2/3$ exactly.
   - It also confirms logarithmic divergence for $q=2m+2$.
7. **Constant.** The implied constant depends on $I,I_*,m$ only, through $V$, through $q=2m+4$, and through the B.1 constant on $I^2$.

**Verdict: correct.**

### 1.4 Lemma B.3 (l.3617-3650)

**Claim.** Suppose $|c_{\iota,r}|\le b_\iota$ and $M=\sum_\iota\int b_\iota<\infty$. Then
$$\sum_rw_r\Big|\sum_\iota\int c_{\iota,r}F_{\iota,\mathbf t}(r)\Big|^2\le M\sum_\iota\int b_\iota\sum_rw_r|F_{\iota,\mathbf t}(r)|^2 .$$

**Check.** $|\sum\int cF|^2\le(\sum\int b|F|)^2\le(\sum\int b)(\sum\int b|F|^2)$, by Cauchy–Schwarz for the measure $b_\iota\,d\mathbf t$ on $\{\iota\}\times\mathbb R^d$.

Finiteness of the right side implies, for each $r$ with $w_r>0$, that $\int b|F|<\infty$, so the left integral converges absolutely. Rows with $w_r=0$ contribute zero by convention.

A7: 200 random instances satisfy the inequality (maximum ratio 0.004). Equality holds when $c=b$ and $F$ is constant (ratio $1.000000000000000$).

**Verdict: correct.**

### 1.5 The four uses of Appendix B

| Use | B-lemma | Rows; weights; $c_r$ | Points | Kernel and support | Hypothesis supplied by | Derivative cost | Status |
|---|---|---|---|---|---|---|---|
| Prop. 4.5, l.1191-1245 | B.2 | $r=(f,k)$ for fixed $b$; $w_r=1$; $c_r=\mu(f)\mathbf1_{(f,b)=1}$. Extra rows $N k\le\mathcal H$ have zero kernel (l.1233-1234) | $N(m)/X$ | $\mathcal K_{b,f,k}=W_0(rx_1)\overline{W_0(rx_2)}\widehat\Phi(a/x_1x_2)$ with $r\in[1,4)$, $a\le C_{I,\Phi}$; support in $[a_0/4,b_0]^2\subset\operatorname{int}[a_0/8,2b_0]^2$. Derivatives are uniform because $a$ is bounded and $\widehat\Phi$ is smooth on $[0,\infty)$ (a smooth radial function is a smooth function of $\lvert w\rvert^2$) | (eq:auxiliary-target) on $I_*$ via Lemma 4.4. The shifts $(X/N d, FN d)$ stay in (eq:initial-scales) | $J\to q=2J+4$ | OK |
| Lemma 6.6, l.2111-2147 | B.1 (R-form, $d=1$) and B.3 | $r=k_0$; $w=1$; single $\iota$ | $N(n)/U$ | $V(x)\,V_*^\sharp(Rx)$ with $R=3^mUN(b)^3\mathcal H_0^2/(YN(k_0)^2)\ge z_*$, because $N b\ge B$ and $N k_0\le\mathcal H_0$. $\|V_*^\sharp\|_{3,2}\ll\|V_*\|_{C^J}$ by (eq:theta-weight-decay) with $A=3$, $j\le2$, which needs $\min(x^{1/4},x^{-A})(1+x)^A\le2^A$. The common majorant $\ll(1+z_*)^{-A}(1+\lvert s\rvert)^{-2}$ is independent of $b,k_0$ | Lemma 6.5. $\sum\lvert\beta\rvert^2\ll a^2$ because $\sum_{N n\asymp U}N(n)^{-1}\ll1$; the bound is uniform in $s$ | fixed $J(A{=}3,j{\le}2)$ | OK |
| Lemma 7.1, l.2315-2346 | B.2 | $r=(C,d,t,f,h)$ for each $\xi_1$; $w_r=w_{C,d}$; $c_r=\ell_{\xi_1}\mu(d)\mu(t)w_{C,d}\mathbf1_{(f,Ct)=(h,t)=1}$ with $\lvert\ell_{\xi_1}\rvert\le1$ | $N(x)/\ell$ | $\mathscr K_h=(z_1z_2)^{-1/2}W\overline W\widehat\Phi(\cdot)$, supported in $I^2\subset\operatorname{int}I_*^2$ ($I_*=[u/2,2v]$). The argument of $\widehat\Phi$ is $\le C_\Phi v^2$ on the retained rows | $\mathcal Q_{\xi_1}(U)$: the map $(f,h)\mapsto hf^2$ has multiplicity $\le\tau(y)$, and $N(hf^2)\le Y_{C,d}$ because $LF\le\Sigma$ and $c_I\ge4C_\Phi v^2$ | $j\to2j+4$ | OK |
| Lemma 7.3, l.2602-2651 | B.2 | $r=(r,f',k')$ per dyadic block and per $\xi'$; $w=1$; $c=(c_I\Sigma/L^2)c_{\xi'}N(r)\tau(r)\mathbf1_{f'\mid k'}$, rescaled by $\ll RD^\delta$ | $N(n)/X'$ | rescaled $\mathscr K$, with $X'/X'_0\in[1,4)$; support $[u/8,2v]^2\subset\operatorname{int}[u/16,4v]^2$. The argument of $\widehat\Phi$ is $\le4C_\Phi v^2$ on nonzero rows | $S_m$ via Lemma 4.4: $\mathcal H'\ge1$ (l.2591-2596) and $X'/N j\ge1$ (eq:child-column-lower-bound); $O(R)$ values of $r$ | $m\to2m+4$ | OK |

**Total in Sec. 7.** Lemma 7.3 outputs $\|U\|_{C^{2m+4}(I_*)}$. That is exactly Lemma 7.1's hypothesis with $j=2m+4$, which then gives $\|W\|_{C^{2(2m+4)+4}}=\|W\|_{C^{4m+12}}$, as in (eq:transfer-summary). Our bookkeeping in the Lemma 7.3 block reproduces l.2647-2651:
$$\frac{\Sigma}{L^2}\cdot RD^\delta\cdot RD^\delta(\Sigma')^2S_m=D^{2\delta}\Sigma S_m .$$

These interface checks agree with the earlier section audits (audit_S4 §B.2 row; audit_S6 Mellin separation; audit_S7 steps 8 and 10). They were redone here independently.

---

## 2. Outline (l.206-659) against the detailed proof

**Legend.** "=" means identical; "special case" means the detailed statement with $B=F=1$, $C=t=d=1$, or common factors trivial; "schematic" means a heuristic display that the paper marks as such.

| Outline claim (line) | Detailed counterpart | Relation | Checked |
|---|---|---|---|
| (eq:power-savings) ⇒ zero-free half-plane (l.228-237) | Sec. 3, l.726-757 | = (Littlewood principle, qualitative in $\nu$) | read; audit_S3 |
| Primary generators; the six units represent $(\mathcal O/3)^\times$ (l.243-247) | standard | true | B2a |
| $(u/n)_2=\chi_n(u)^3$, $(u/n)_3=\chi_n(u)^2$ (l.263) | used throughout | true | B2b (463 cases) |
| (eq:intro-ms): $\sum_{N u\le H}\lvert A_u\rvert^2\ll D^{1+\varepsilon}H$, $H=D^{1+\vartheta}$ (l.272-276) | Prop. 3.1 (eq:ms), $D^{2+\vartheta+\varepsilon}=D^{1+\varepsilon}H$ | = | read |
| $\chi_n(p^6)=\mathbf1_{p\nmid n}$; $A_{p^6}=A_1+O(D/Y)$ (l.284-287) | l.698-705 | = | B2c (625 pairs) |
| (eq:intro-extraction) and the exponent $11/12+5\vartheta/12$ (l.290-298) | (eq:prime-extract) | = | C1, C2, C9 |
| Classical identity $(\tfrac{-1}{m})=(m^{-1/2}\sum(\tfrac xm)e(x/m))^2$ (l.318) | motivation only | true | B1 (486 values of $m$) |
| $\mu\gamma_{-1}=\chi_n(-1)G^{-1}\bar\alpha\gamma_2$, $G=\overline{\chi_n(4)}\gamma_3$ (l.322-323) | (eq:convert2), (eq:g); App. A.1 | = | B3 (41 values of $n$, split and inert, 1-2 primes; error $1.8\cdot10^{-14}$) |
| $\xi\in\{\nu\eta,\bar\nu\eta\}$ (l.335-336) | $\xi$ ranges over all characters of the fixed group (l.955-956, l.1063-1064) | equivalent reparametrization | OUT-P1 |
| (eq:intro-poisson-comparison)–(eq:intro-dual-ms), $\mathcal H\asymp D^2/H$ (l.338-349) | Prop. 4.5, (eq:initial-column-output), $\mathcal H=C_{I,\Phi}D^2/(HB^2)$ | special case $B=F=1$, with weight $W_0=x^{-1/2}\bar W$ | C3; read |
| $c_\theta(nb^3)=3^{5/2}\lvert b\rvert\overline{\chi_n(\lambda)^2}\gamma_2(n)$ (l.361-366) | Lemma 6.1 proof, l.1701-1705; E9 | = (needs $\chi_b(\lambda)^6=1$) | B4b (used inside $T_h$) |
| (eq:intro-completed-theta-sum) equals the $b$-completion of $B_h$ (l.376-383) | (eq:T), (eq:T-theta) | = with $f=1$ | B4b |
| Illustrative dual sum (eq:intro-dual-theta-sum) (l.389-406) | Prop. 6.2 (eq:reflection), $\ell=\lambda^{-4}m$, $c=c_0h$ | schematic; constants $81N(c_0)^2$ and $\alpha(\lambda^{-4})$ suppressed, as stated | read |
| "Within a ray class of $h$ the data are independent of $h$" (l.402-403) | Lemma 6.3: $(d,\psi,c_0)$ depends only on the ray class; the scalar $C(k_0)$ is bounded | = (bounded prefactors suppressed, as stated) | read |
| $\chi_p^{-1}\chi_p^{-2}=\chi_p^3$ (l.408-411) | (eq:theta-local-factors), $B_{p,1}=\chi_p^3$ | = | D1/D6 (App. A.2 audit) |
| GL gives the factor $M+L$; BGL Thm 1.3 has the extra $(ML)^{2/3}$ (l.412) | Lemma 6.5 | = | GL Thm 1.1 and BGL Thm 1.3 read verbatim (§5) |
| (eq:intro-completed-ms): $\sum\lvert T_h\rvert^2\ll(\mathcal HX)^\varepsilon(\mathcal H+\mathcal H^2/X)$ (l.416-420) | Prop. 5.2 with $D^\varepsilon$ and $f=1$ | equivalent: take $D=\max(2,\mathcal H,X)$, $C_0=1$; the constants do not depend on $D$ | OUT-P2 |
| (eq:intro-cube-completion), (eq:intro-cube-weight), complete multiplicativity of $w_h$ (l.429-438) | (eq:T) regrouped; l.1361-1372 | = | B4b (error $9.9\cdot10^{-16}$) |
| (eq:intro-cube-inversion) (l.439-443) | (eq:cube-inverse) | = | B4c (error $3.9\cdot10^{-17}$) |
| Short part (eq:intro-short-cube-ms) and cutoff (eq:intro-cube-cutoff) (l.456-482) | (eq:short-cube-bound), (eq:cube-cutoff) | = ($X/N(d)^3\ge1$ because $H_c\le X^{1/3}$) | C8; read |
| Basic scales $X\asymp D$, $\mathcal H\asymp D^{1-\vartheta}$, $H_c\asymp D^{2\vartheta/3}$ (l.483-487) | (eq:initial-positive-gap) | special case $B=1$ | C8 |
| Long part and $\beta_0(b)$, $\lvert\beta_0\rvert\le\tau(b)$, (eq:intro-long-cube-ms) (l.491-521) | l.1408-1448, with $\mathbf1_{(b,f)=1}$ | = | B4d (3 cutoffs, nonzero values) |
| $E(\mathcal H,X)\preccurlyeq X+\sup_{1\le L_b\le X/H_c^3}E(\mathcal H,L_b)$ (l.548-554) | Lemma 5.3 (sup over $L_b>1$; the case $L_b\le1$ by counting) | = up to the endpoint | OUT-P3 |
| First transfer: $E(\mathcal H,L_b)\preccurlyeq X+\frac{\mathcal H}{L_b^2}\sum\lvert M(y)\rvert^2$ (l.556-570) | Lemma 7.1 with $C=t=d=1$, $F=1$: $w=\mathcal H/L^2$, $Z\ll\mathcal H\le X$ | special case | read |
| Enlargement $Y=XL_b/\mathcal H\ge L_b^2/\mathcal H$ (l.572-576) | $Y_{C,d}=c_I\Sigma LFN(d)/(\mathcal HN(C)^2)$, using $LF\le\Sigma$ | special case | read |
| $\mathcal H'=L_b^2/Y=\mathcal HL_b/X=\mathcal H/N(b)^3$; $\sum\lvert M\rvert^2\preccurlyeq YL_b+YE'$; $E\preccurlyeq X+\frac X{L_b}E'$; $\mathcal H'/X'=\mathcal H/X$ (l.577-611) | Lemmas 7.2, 7.3; (eq:transfer-scales) | special case | C4, C5, C6 |
| Recursion and contraction $\mathcal H'<\mathcal H(\mathcal H/X)^2\ll D^{-2\vartheta}\mathcal H$ (l.620-637) | Prop. 5.1, l.1565-1577: $\mathcal H'<\mathcal H(\mathcal H/\Sigma)^2\le D^{-2\kappa}\mathcal H$ with $\kappa=\vartheta/2$ | = up to constants | C7 (20 000 samples); OUT-P4 |
| "After $O_\vartheta(1)$ steps … row parameter at most 1, where counting gives the bound" (l.632-634) | base case $j=0$ (l.1532-1547), $j=\lceil C_0/\kappa\rceil$ | = | read |
| The full family $\mathcal E(\mathcal H,X,F)$ and the target $\preccurlyeq XF$ (l.639-658) | (eq:energy), Prop. 5.1 | = | read |

**Conclusion of §2.** No statement in the Outline goes beyond what the detailed sections prove. Each analytic step that the Outline suppresses is exactly the bookkeeping the paper announces as suppressed:

- coprimality and common factors;
- the auxiliary twist $f$ and the exclusion ideals;
- smoothing and separation of the row-dependent dual weights;
- the decomposition into non-squarefree rows.

The detailed proof supplies each of these:

- Lemma 4.4 removes the exclusions;
- Appendix B (via Lemma 6.6) separates the row-dependent weights;
- the proof of Prop. 5.2 decomposes $k=u_0sv^2$;
- the $t$-part of Lemma 6.6 handles the prime factors of $k$ that divide $g$ or lie in $S$.

---

## 3. Numerical checks (our own code)

Script: `experiments/code/quasi_rh/appB_outline_checks.py`, run with `python3 -I`; output in `appB_outline_checks.out`. All Z[ω] arithmetic is self-implemented:

- the sextic symbol is computed via $x^{(N p-1)/6}\bmod p$;
- residue systems come from the Hermite normal form of $n\mathcal O$;
- $e(z)=\exp(4\pi i\,\mathrm{Im}z/\sqrt3)$;
- $\gamma_j$ is computed by direct summation.

| ID | What | Result |
|---|---|---|
| A1 | Lemma B.1 representation (2-D, FFT in log coordinates) at 400 random points | max error $3.7\cdot10^{-12}$ |
| A2 | Pointwise coefficient bound via $(1-\Delta)^{q/2}$, $q=2,4,6$ (exact inequality, periodic normalization) | holds (e.g. $q=6$: $2.58\cdot10^7\le7.50\cdot10^7$) |
| A3 / A3-ctl | (eq:smooth-pointwise): R-uniformity for $A=2$, $R\in[10^{-3},10^4]$; negative control with $(1+R)^{A+1}$ | bounded in $[4.6,14.4]$; control grows $8.8\cdot10^2\times$ |
| A4 | Lemma B.2: coupled sum with row-dependent kernels and points equals its Mellin/test-function representation | relative error $3.8\cdot10^{-11}$ |
| A4b | Lemma B.2: Cauchy–Schwarz majorant chain | $1.26\le91.8$ |
| A5 | $\lVert Vx^{it}\rVert_{C^m}/(1+\lvert t\rvert)^m$ bounded, $m=1,2,3$ | yes |
| A6 | (eq:kernel-bilinear-integral): finite for $q=2m+4$ ($=2/3$ exactly for $m=0$); log-divergent for $q=2m+2$ | yes, $m=0..3$ |
| A7 | Lemma B.3 on 200 random instances; equality case | max ratio 0.004; equality to $10^{-15}$ |
| B1 | Jacobi–Gauss identity of l.318, odd squarefree $m<1200$ | 486/486 |
| B2a-c | units mod 3; $(u/p)_2=\chi^3$, $(u/p)_3=\chi^2$; $\chi_n(p^6)=\mathbf1_{p\nmid n}$ | all pass |
| B3 | Outline identity l.322 (= (eq:convert2), (eq:g)) | 41 values of $n$, error $\le1.8\cdot10^{-14}$ |
| B4a | $\gamma_2(ab)=\gamma_2(a)\gamma_2(b)\chi_a(b)^2\chi_b(a)^2$ (helper), against direct sums | error $1.3\cdot10^{-14}$ |
| B4b-d | (eq:intro-completed-theta-sum) in the $c_\theta$-normalization = (eq:intro-cube-completion); (eq:intro-cube-inversion); long-part regrouping with $\beta_0$ | 605 columns, cube indices of norm $\le13$, 4 rows; errors $\le10^{-15}$ |
| C1-C9 | Outline exponent and scale algebra: (eq:intro-extraction), $\mathcal H'$, the transfer identity, $\mathcal H'/X'$, contraction, cutoff, $N(p^6)\le H$ | all pass (sympy, plus 20 000 random samples for C7) |

**Limits.**

- A1–A7 test the exact identities and inequalities inside the proofs of B.1–B.3 on concrete instances. They cannot test an implied constant.
- B4 uses cube indices only of prime norm $\le13$. Non-squarefree cube indices were covered by audit_S5 (C1/C2, prime squares, $X=1.3\cdot10^5$).
- Nothing here tests the theta transformation (App. A.2) or Prop. 5.2/5.4 themselves.

---

## 4. Findings

| ID | Location | Class | Severity if real | Finding |
|---|---|---|---|---|
| APPB-N1 | l.3491-3524 | no_issue_found_in_inspected_portion | n/a | Lemma B.1. Normalization, inversion for all $\mathbf x>0$, $C^q$ comparison in log coordinates, $(1-\Delta)^{q/2}$ bound, and integrability for $q>J+d$ all re-derived. A1, A2. |
| APPB-N2 | l.3526-3556 | no_issue_found_in_inspected_portion | n/a | R-form (eq:smooth-pointwise): chain rule $\partial_y\mapsto a\,u\partial_u$, argument $\asymp R$ on the box, Leibniz product, constants independent of $R$. A3 with a negative control. |
| APPB-N3 | l.3558-3615 | no_issue_found_in_inspected_portion | n/a | Lemma B.2. The representation through $U_s,\overline{U_t}$ ($V$ real, $V\equiv1$ on $I$), Fubini, the uniform majorant, Cauchy–Schwarz, $\lVert U_t\rVert_{C^m}\ll(1+\lvert t\rvert)^m$, and $q=2m+4>2m+2$ are all correct. A4, A4b, A5, A6. |
| APPB-N4 | l.3617-3650 | no_issue_found_in_inspected_portion | n/a | Lemma B.3. Weighted Cauchy–Schwarz; absolute convergence follows from finiteness of the right side. A7. |
| APPB-N5 | l.1191-1245; l.2111-2147; l.2315-2346; l.2602-2651 | no_issue_found_in_inspected_portion | n/a | All four uses meet the hypotheses: support $I\subset\operatorname{int}I_*$, rows and weights, row-dependent points, uniform kernel bounds, a hypothesis valid for every test function in $C_c^\infty(I_*)$, and derivative costs $2J+4$, $2j+4$, $2m+4$, $4m+12$ (§1.5). |
| APPB-P1 | l.3500-3504, l.3547-3552, l.3600-3601, l.2124 | typo_or_presentation | cosmetic | The load-bearing estimate is the **pointwise** bound $\lvert b(\mathbf t)\rvert\ll(1+\lvert\mathbf t\rvert)^{-q}\lVert\mathcal K\rVert_{C^q}$. It appears only inside the proof of B.1, and both B.2 and Lemma 6.6 cite "the pointwise estimate in the proof". The integral bound in the statement of B.1 and (eq:smooth-weight-bound) are never used. Stating the pointwise bound as part of Lemma B.1 would be cleaner. |
| APPB-P2 | l.3578, l.2304-2312, l.2574-2581; l.3575 vs l.3590 | typo_or_presentation | cosmetic | (i) B.2 requires $\lvert c_r\rvert\le w_r$. In Lemma 7.1 ($\ell_{\xi_1}\mu(d)\mu(t)$) and in Lemma 7.3 ($(c_I\Sigma/L^2)c_{\xi'}N(r)\tau(r)$), trivial rescaling and a sum over the finite character set are needed; these are left implicit. (ii) The proof applies the hypothesis to the complex-valued $U_t=Vx^{it}$. Read the hypothesis as covering complex test functions, consistent with Secs. 3-7 (cf. audit_S7 P-S7-6). Even under a real-only reading, splitting into real and imaginary parts costs a factor $\le4$ in $M_j$. |
| APPB-P3 | l.3503, l.3585 vs l.1016-1019; App. B passim | typo_or_presentation | cosmetic | The multivariable $C^q$ norm is defined only inside Prop. 4.5 (l.1018-1019). Symbols are overloaded: $F$ is a weight here but a scale elsewhere; $A$ is a decay exponent but also $\mathcal A(W)$; $b$ is a Mellin coefficient and also a cube index; $\mathcal I$, $I$, $I_*$ are reused with different instantiations; $M$ is a bound and also $M_j$. The meaning is always clear from context. |
| APPB-P4 | l.3522-3523 | typo_or_presentation | cosmetic | The citation "[PY19, §10.1, (130)-(131)]" cannot be matched against arXiv:1608.06854, where §10.1 numbers these formulas (10.2)-(10.3) (Mellin inversion of inert weights and the coefficient bound). The content matches; the numbering is presumably that of the journal version. The reference is a non-load-bearing "see also". |
| APPB-P5 | l.3719, l.3839, l.3882, l.3922, l.3929 | typo_or_presentation | cosmetic | Five bibliography items are never cited: GZ23, LZZ26, Page35, Sie35, Tat51. No cited key is missing (script check). |
| OUT-N1 | l.206-659 | no_issue_found_in_inspected_portion | n/a | Every Outline claim maps to a proved statement (table in §2). The arithmetic identities (B1-B4) and the scale algebra (C1-C9) were independently re-verified. |
| OUT-P1 | l.335-336 vs l.955-956, l.1063-1064 | typo_or_presentation | cosmetic | The Outline says $\xi$ is "$\nu\eta$ or $\bar\nu\eta$". The proof lets $\xi$ range over all characters of a fixed ray class group whose modulus is divisible by the conductor of $\nu$. The two are equivalent, since $\xi=\bar\nu\cdot(\nu\xi)$. |
| OUT-P2 | l.416-420 vs l.1317-1329 | typo_or_presentation | cosmetic | The Outline states (eq:intro-completed-ms) with $(\mathcal HX)^\varepsilon$; Prop. 5.2 has $D^\varepsilon$ under $\mathcal H,X,N f\le D^{C_0}$. Equivalent: $D$ is a free ambient parameter in Prop. 5.2 and the constants do not depend on $D$, so take $D=\max(2,\mathcal H,X)$, $C_0=1$. |
| OUT-P3 | l.548-552 vs l.1349-1351, l.1456-1462 | typo_or_presentation | cosmetic | The Outline's supremum is over $1\le L_b\le X/H_c^3$ in one display and $1<L_b$ in the next; Lemma 5.3 uses $N b>H_c$ and $L_b>1$. The terms with $L_b\le1$, handled in Lemma 5.3 by counting, are not mentioned in the Outline. |
| OUT-P4 | l.628-630 vs l.1568-1572, l.1621 | typo_or_presentation | cosmetic | The Outline's contraction $\ll D^{-2\vartheta}\mathcal H$ uses $\mathcal H/X\asymp D^{-\vartheta}$ at the first-step scales. The proof uses $\kappa=\vartheta/2$, giving $D^{-\vartheta}$, so as to absorb the constant in $\mathcal H/\Sigma\ll D^{-\vartheta}$. Consistent. |
| OUT-P5 | l.388-424, l.556-611 | typo_or_presentation | cosmetic | Two simplifications are announced (l.208-210, l.639-650) and harmless. (i) In Step 4 the dual weight $V_*^\sharp(N(m)X/N(h)^2)$ depends on the row $h$; the proof separates it with Lemma B.1 and Lemma B.3 (Lemma 6.6), which the Outline does not mention. (ii) The Outline's $F=1$ recursion is not closed: the transfer creates $f'=Cew\ne1$ and the common factor $r$. The detailed family $\mathcal E(\mathcal H,X,F)$, with Lemma 4.4, is closed. |
| OUT-P6 | l.271, l.296 | typo_or_presentation | cosmetic | The restriction $0<\vartheta\le1/10$ is never used (confirms architecture note P2 and audit_S5 S5-P2). |

There is no verified_error, suspected_gap, missing_hypothesis or unresolved_ambiguity in the inspected portion.

---

## 5. Imported results used or cited in the inspected portion

- **BGL Theorem 1.3** (arXiv:1112.1650, l.175-178). Read verbatim:
  $$\sum^*_{Na\le M}\Big|\sum^*_{Nb\le N}\lambda_b\chi_a(b)\Big|^2\ll(MN)^\varepsilon\,(M+N+(MN)^{2/3})\sum|\lambda_b|^2 .$$
  This matches the Outline's contrast at l.412. BGL §3.2 "The recursive argument" exists, matching l.658. Neither is used in the proof.
- **GL** (arXiv:1112.1642).
  - Def. 1: $n$-th order Hecke family, with properties (1)-(3).
  - Thm 1.1: $(MN)^\varepsilon(M+N)$ for quadratic families, sums over squarefree ideals of $I(c)$.
  - Cor. 1.2: the $n/2$-th power of an even-order family.
  - Thm 4.1: $(E_\alpha)\Rightarrow(E_{2-1/\alpha})$.
  - Lemma 4.4: rough monotonicity of $B_1$ in $M$, "following [HB, Lemma 9]".

  All read. They match the Outline's uses at l.412 (GL Thm 1.1 and Cor. 1.2), l.615-617 (enlarged range via GL Lemma 4.4 and the proof of Thm 4.1, following HB95 Lemma 9) and l.658 (GL Thm 4.1).
- **Not re-verified here.** These are non-load-bearing citations in the Outline whose mathematical content is re-proved in the paper: Pat77 Thm 6.1; HB00 §3 and (2); Has50 pp. 443-445; HB95 Lemma 8, Lemma 9 and §8; DR Lemma 5.4, Prop. 5.3 and (8.2); PY20 p.440; KLMS20 §2.3; FLN10; IK04 Thm 5.33 (audit_S3); Lit12 and MM09.
- **Appendix B imports nothing** beyond Fourier inversion on $\mathbb R^d$ and Cauchy–Schwarz. The PY19 reference is a "see also" (APPB-P4).

## 6. What would invalidate this portion

Within Appendix B, the only load-bearing statements are:

- the pointwise coefficient bound in the proof of Lemma B.1;
- Lemma B.2 with the cost $\|\mathcal K_r\|_{C^{2m+4}}$ and a constant depending only on $(I,I_*,m)$;
- Lemma B.3.

Suppose B.2's constant depended on the kernels beyond $\sup_r\|\mathcal K_r\|_{C^{2m+4}}$, or on the number of rows. Then Prop. 4.5 and Prop. 5.4 would fail, and with them Prop. 5.1, Prop. 3.1 and Theorem 1.1. We found no such dependence: the proof uses only one fixed cutoff $V$, the uniform majorant and Cauchy–Schwarz over a finite row set.

The Outline is non-load-bearing; nothing in the proof depends on it.

## 7. Out-of-scope note (for the Introduction auditor)

l.141-143 says Theorem 1.1 "rules out" Landau–Siegel zeros, defined through the region (eq:intro-classical-region) with an unspecified absolute $c_0$. For moduli with $\log(3q)\le12c_0$, that region extends to the left of $11/12$. There, Theorem 1.1 alone does not exclude a real zero in $(1-c_0/\log 3q,\,11/12]$; finitely many small moduli would need a computation. The usual asymptotic meaning of "Landau–Siegel zero" is excluded by Theorem 1.1. The uncited LZZ26 ("Numerical computations concerning Landau–Siegel zeros") may have been meant for this point. This is a cosmetic phrasing issue outside our scope; it is not listed in §4.

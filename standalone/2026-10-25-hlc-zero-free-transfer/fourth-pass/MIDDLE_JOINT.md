# A joint buffered return and the remaining large-divisor expression

**Status: proved deductions within the explicitly imported analytic framework. The complete remaining large-divisor expression is open.**

This note improves an actual coherent component of the native inverse. It also proves a stability theorem for the modified gcd coefficient, using genuine Möbius polynomials with common additional punctures. It does not establish a new unconditional zero-free region.

For $D=U^r$ and $29/25\le r\le117/100$, the complete smooth reduced-ratio head through $U^{101/100}$ has squared row mean strictly smaller than $U^{(1+5r)/6-1/1000+\epsilon}$. The earlier fourth-moment argument controlled this component only through $U^{7/9}$. The new proof returns the ordinary factor first and keeps the ordinary and inverse factors in the **same buffered bin**.

In its exact complementary ratio expression, the complete part of the coprimality-inversion sum with $Nk\ll U^{1/100}$ has squared row mean at most $U^{(1+5r)/6-1/750+\epsilon}$. The remaining expression has $Nk>U^{1/100}$, with a specified smooth transition. These are coherent estimates; no lower support cutoff for the returned primal variable is inferred.

## 1. Premises and notation

Use exactly the original sixth-power-free Eisenstein physical rows, finite-order ray presentations, either sextic orientation, common puncture of prescribed polynomial radical, bounded nonnegative row weight, and nonprincipal inducing restriction of `third-pass/GCD_FOURTH_COMPONENT.md`. Thus

$$
 \psi_u=\psi_u^*1_{(\,\cdot\,,Q_s)=1},\qquad
 P_u=\operatorname{rad}(\mathfrak f_uQ_s),\qquad Nu\asymp U.
 \tag{1}
$$

The primitive conductor and every original natural zero stay distinct. Bounded principally induced exceptions must have been handled before using these statements. Norm heights and the source's finite-dimensional common-profile/Sobolev calculus are allowed, with fixed polynomial height costs and finite seminorms. No nonzero-angular-character zero-free theorem is imported.

The external premises are the finite-order $7/8$ cap and native inverse second moment from `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`, `preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`, Git blob `268c4e3206d460c617d3d2129742a72b831b3def`; the buffered physical-row counts of Xu--Sang, [arXiv:2610.17675v2](https://arxiv.org/html/2610.17675v2), Lemma 6.2 and Proposition 6.3; and the ordinary primitive functional equation. Their complete external proofs are not independently certified here.

The source-dependent modified-coefficient lemma is `third-pass/GCD_FOURTH_COMPONENT.md`, equations (9)--(20), at mathematical freeze `820b99562e3b458021a6de74802293baafbe5190`. The exact inverse functional equation is `third-pass/RATIO_CUTOFF_RETURN.md`, equations (4)--(8), at the same freeze. No arbitrary-coefficient extension of the native inverse moment is assumed.

Let $w_0,\chi_0,\chi_k$ be fixed smooth cutoffs in $[0,1]$, equal to one through one and zero from two onward. The first two are the cutoffs of the asymmetric identity. Set

$$
 \alpha=\frac2{125},\quad y_1=U^\alpha,\quad y_2=2D/U^\alpha,
$$
$$
 A(r)=\sum_{ab=r}\mu_E(a)\mu_E(b)w_0(Na/y_1)w_0(Nb/y_2),
 \qquad C_a(P)=\sum_{(d,P)=1}\frac{A(ad)}{Nd}.
 \tag{2}
$$

Both Möbius signs and every repeated-prime term remain. The entire support $Nr<8D$ is retained in $C_a$, including terms that vanish only after their complete ordinary sums. For sufficiently large $U$, the exact asymmetric identity gives

$$
 M_u(D;V)=-D^{-1/2}\sum_{r,c}A(r)\psi_u(rc)V(NrNc/D).
 \tag{3}
$$

Here $V(x)=x^{it}W(x)$, with $W$ supported in a fixed annulus. The bounded initial range is absorbed in the constants.

For a buffered bin write $\delta=2a-1$. The printed floor is $a_0=51/100$, the cap gives $\delta\le3/4$, and the above-floor physical-row count has exponent

$$
 \mathcal R(\delta)=\frac{15-16\delta}{15-6\delta}.
$$

Retain the explicit envelope

$$
 \mathcal E(s)=\max_{0\le\delta\le3/4}\{\mathcal R(\delta)+s\delta\}
 =\begin{cases}
 1,&0\le s\le2/3,\\
 \displaystyle\frac83+\frac{5s}{2}-\frac{10}{\sqrt6}\sqrt s,
       &2/3\le s\le200/147,\\
 \displaystyle\frac27+\frac{3s}{4},&s\ge200/147,
 \end{cases}
 \qquad \mathcal E_{.51}(s)=\max\{1+s/50,\mathcal E(s)\}.
 \tag{4}
$$

## 2. Return the ordinary factor before estimating the joint product

For a common smooth selector $F$ of the reduced numerator, at scale $B$, the exact gcd identity and coprimality inversion give

$$
 M_{F,u}=-\sum_k\frac{\mu_E(k)}{Nk}1_{(k,P_u)=1}
 D^{-1/2}\sum_{A,c}C_{kA}(P_u)\psi_u(Ac)
                  F(NkNA/B)V(NANc/D).
 \tag{5}
$$

All $k,A$ sums are finite. This is the fixed-$k$ version of the inverse ordinary functional equation: in equation (8) of `GCD_FOURTH_COMPONENT.md`, the primitive root number and ordinary dual kernel return together, and the untouched $e\mid Q_s$ sum restores the original natural ordinary character in $c$. There is no new $k$ puncture in that ordinary factor. The cancelled $k$ phase leaves $1_{(k,P_u)=1}$ and the exact scalar weight $1/Nk$.

Collecting $k$ gives the exact returned coefficient

$$
 D_{F,P}(A)=\sum_{(k,P)=1}\frac{\mu_E(k)}{Nk}
                        C_{kA}(P)F(NkNA/B).
 \tag{6}
$$

The ordinary factor is now at direct length $D/NA$, while the modified inverse block is at length $NA$. Their logarithmic lengths add to $r$.

### The ordinary bound in the same buffered bin

On the same bin as the modified inverse, for a common smooth ordinary block of bounded log-length $c\ge0$,

$$
 |S_{\psi_u}(U^c;V)|\ll_\epsilon
 U^{\delta c/2+\epsilon}(1+|v|)^A p_J(V).
 \tag{7}
$$

This is the ordinary version of the local logarithmic-control argument used for the reciprocal. On a slightly inset zero-free disk, polynomial conductor/height growth and the Euler-normalized logarithm give a subpower bound for both $L_{\rm orig}$ and $L_{\rm orig}^{-1}$. Shift the ordinary Mellin integral to $\operatorname{Re}s=a+\varepsilon_1$; it crosses no pole in the nonprincipal family. Its normalizing power is $U^{c(a-1/2+\varepsilon_1)}$.

Fix the source orders and its polynomial buffer first. Assign small shares of that **one** buffer to all actual Mellin and profile frequencies, including those in the modified coefficient. Choose external tail orders last. Outside the buffer use the trivial polynomial estimate on the absolute line and absorb its fixed power of $U$ by a fixed polynomial in the large frequency. The density theorem is not extended to arbitrary heights.

### The joint dyadic bound, including its pointwise form

For a common smooth annular $F=\eta$ and $B=U^b$, the exact reduced-ratio component satisfies

$$
 \boxed{\quad
 J_B:=\sum_u w_U(u)|M_{\eta,u}|^2
 \ll_\epsilon (B/D)^{1/4}U^{\mathcal E_{.51}(r)+\epsilon}
                   (1+|t|)^A p_J(W)^2 .\quad}
 \tag{8}
$$

More precisely, on a single buffered bin, before summing its rows,

$$
 \boxed{\quad
 |M_{\eta,u}|\ll_\epsilon
       (B/D)^{1/8}D^{\delta/2}U^\epsilon
                         (1+|t|)^A p_J(W).\quad}
 \tag{9}
$$

The same pointwise bound holds for the coherent smooth head with selector $\chi_0(Na/B)$, after replacing the annular selector by its smooth dyadic partition. All constants and orders are uniform within the original compatible fixed labels; no unrelated rowwise character or coefficient choice is introduced.

**Proof.** In the fixed-$k$ term of (5), put $R=B/Nk$ and split $Nc$ into a common smooth annulus at $X\asymp D/R$. Fourier separation of the common profile yields the modified block

$$
 Z_{u,k}(R;V_1)=R^{-1/2}\sum_A C_{kA}(P_u)\psi_u(A)V_1(NA/R)
$$

and $S_{\psi_u}(X;V_2)$, with scalar normalizer $\sqrt{RX/D}\asymp1$ and common separated profiles.

For fixed $\beta>7/8$, put $\theta=1-\beta$. The proved modified-coefficient lemma gives on this same bin

$$
 |Z_{u,k}(R;V_1)|\ll
 (B/D)^\theta R^{\delta/2}(Nk)^\epsilon U^\epsilon
                  (1+|\mathbf v|)^A p_J(V_1).
 \tag{10}
$$

Its explicit $k$-prime local factors remain intact; no potentially vanishing correction polynomial is inverted. Multiplying (7) and (10) gives

$$
 |Z_{u,k}(R;V_1)S_{\psi_u}(X;V_2)|^2
 \ll (B/D)^{2\theta}D^\delta U^\epsilon
                (1+|\mathbf v|)^A\{\text{seminorms}\}^2.
 \tag{11}
$$

The common Fourier weighted $L^1$ norm has fixed seminorm control. The ordinary scale $X=D/R$ lies in a prescribed bounded-power range; the nonempty scales near one are handled by a fixed rescaling. The primitive conductor has disappeared by the exact inverse functional equation, so no conductor lower bound or missing deficit enters (11).

Minkowski over $k$ uses $\sum_{Nk\ll B}(Nk)^{-1}\ll\log(2B)$. This proves the pointwise bound with exponent $\theta$. For a coherent head the additional dyadic sum has geometric or logarithmic cost and its endpoint is $B$. Choose $\beta$ sufficiently close to $7/8$ after the final epsilon and bounded ranges are fixed. Replacing $\theta$ by $1/8$ costs the allocated epsilon and proves (9).

Summing (11) over the physical bins costs $U^{\mathcal E(r)+\epsilon}$ above the floor and $U^{1+r/50+\epsilon}$ on the bottom bins. The same harmonic $k$ sum then proves (8). This retains the actual $k$ mask and modified-coefficient row dependence throughout. QED.

The earlier ordinary fourth-moment proof remains an optional competitor for the **same** component:

$$
 J_B\ll (B/D)^{1/4}
 U^{\min\{\mathcal E_{.51}(r),[1+\mathcal E_{.51}(2b)]/2\}+\epsilon}
                     (1+|t|)^A p_J(W)^2.
 \tag{12}
$$

This is the minimum of two proved upper bounds, with no statistical independence assumption.

## 3. A head beyond the row scale, with an exact consumer margin

Set $B_0=U^{101/100}$ and let $M_H$ be the coherent component selected by $\chi_0(Na/B_0)$. A common smooth dyadic partition and Minkowski extend (8) to this head, since the scalar exponent increases with $b$:

$$
 \boxed{\quad
 \sum_u w_U(u)|M_{H,u}|^2
 \ll U^{\Gamma(r)+\epsilon}(1+|t|)^A p_J(W)^2,
 \qquad \Gamma(r)=\mathcal E(r)+\frac{101/100-r}{4}.
 \quad}
 \tag{13}
$$

Throughout the stated interval, $r$ belongs to the interior branch of (4), which dominates the printed floor. Indeed the legal competitor $\delta=1/2$ gives $\mathcal E(r)\ge7/12+r/2>1+r/50$ there. Let $e_0(r)=(1+5r)/6$. The gap is

$$
 G(r)=e_0(r)-\Gamma(r)
 =-\frac52-\frac{101}{400}-\frac{17r}{12}
                         +\frac{10}{\sqrt6}\sqrt r.
 \tag{14}
$$

It increases on this interval, because

$$
 G'(r)=-\frac{17}{12}+\frac5{\sqrt{6r}}>0
                 \quad\text{for }r<\frac{600}{289}.
$$

At the left endpoint,

$$
 G(29/25)=\sqrt{58/3}-\frac{659}{150}-\frac1{400}
        =0.001135319424306\ldots>\frac1{1000}.
 \tag{15}
$$

The strict inequality has the exact rational certificate

$$
 \frac{58}{3}-\left(\frac{26381}{6000}\right)^2
                       =\frac{42839}{36000000}>0.
 \tag{16}
$$

The decimal is illustrative; (14)--(16) prove the full interval margin. No adjustable-floor extension is needed. The ordinary fourth moment is not used in (8) or (13), although it remains an optional competing bound in (12).

## 4. A stable modified-coefficient far estimate

Consider a complete coherent subsum of (5), supplied by common smooth selectors with bounded logarithmic derivatives, whose nonzero terms satisfy

$$
                             NA\gg U.                       \tag{17}
$$

The constant here is fixed. The selectors may depend smoothly on bounded-power scale ratios involving $k,A$ and the original short factors, provided their Fourier separation is common within each fixed arithmetic-label sum. In particular, the ratio and small-$k$ selectors of Section 5 are permitted. For such a subsum,

$$
 \boxed{\quad
 \sum_u w_U(u)|M^{\rm returned,far}_u|^2
 \ll U^{e_0(r)-1/750+\epsilon}(1+|t|)^A p_J(W)^2.
 \quad}
 \tag{18}
$$

**Proof.** Expand $C_{kA}$ by (2), retaining the weight $1_{(d,P_u)=1}/Nd$. In $A(kAd)$ call its first short factor $a$. Since its Möbius value is zero unless $a$ is squarefree, set

$$
 g=(a,kd),\qquad a=g t,\qquad A=t n,\qquad m=kd/g.
 \tag{19}
$$

Then $g$ is a squarefree divisor of $\operatorname{rad}(kd)$, $(t,kd)=1$, and $t\mid A$ is precisely the condition $a\mid kAd$. If $m$ is not squarefree the second Möbius value vanishes. Otherwise

$$
 \mu_E(a)\mu_E(kAd/a)
 =\mu_E(g)\mu_E(m)\mu_E(t)\mu_E(n)1_{(n,m)=1}.
 \tag{20}
$$

Thus the two inverse polynomials have characters

$$
 \psi_u(t)1_{(t,kd)=1},\qquad
 \psi_u(n)1_{(n,m)=1},
$$

while the ordinary factor has the original $\psi_u(c)$. Within fixed $k,d,g$ these are common additional punctures of polynomial radical and have the same primitive character. The original row mask $1_{(kd,P_u)=1}$ remains a bounded row restriction. The scalar sign is $\mu_E(k)\mu_E(g)\mu_E(m)$ and its weight is exactly $1/(NkNd)$. There is no extra $Ng$ or $\sqrt{Ng}$ normalizer.

The original smooth factors become

$$
 w_0(NgNt/y_1),\qquad w_0(NmNn/y_2),\qquad
                           V(NtNnNc/D),                     \tag{21}
$$

together with the retained selectors. On a nonempty triple of common smooth annuli, let $a_0,b_0,c_0$ denote their logarithmic lengths. Then

$$
 a_0+b_0+c_0=r+O(1/\log U),\qquad
 0\le a_0\le\alpha+O(1/\log U),
$$
$$
 1-\alpha+O(1/\log U)\le b_0
                  \le r-\alpha+O(1/\log U).                \tag{22}
$$

The lower bound uses $NtNn=NA\gg U$, and the upper bound uses $NmNn\ll y_2$ with $Nm\ge1$. Derivatives of (21) and the admitted selectors are uniformly controlled on the retained annuli. Fourier separation gives a product of two actual normalized Möbius polynomials and one actual normalized ordinary polynomial.

Use the global capped pointwise estimate $|P(U^\ell)|^2\ll U^{3\ell/4+\epsilon}$ for the short inverse and ordinary factors, and the imported actual inverse second moment for the long inverse. Its common-puncture extension is the exact Euler inversion in `ASYMMETRIC_HB_TAIL.md`, equation (5), and changes neither primitive character nor exponent. All puncture radicals are bounded powers of $U$.

The squared row norm has exponent

$$
 e(b_0)+\frac34(r-b_0),\qquad e(b)=\max\{1,(1+5b)/6\}.
 \tag{23}
$$

For (22) and $r\ge1+10\alpha=29/25$, the exact two-branch calculation from `ASYMMETRIC_HB_TAIL.md` gives

$$
 e(b_0)+\frac34(r-b_0)\le e_0(r)-\alpha/12
                        =e_0(r)-1/750.                     \tag{24}
$$

Fixed scale constants cause only $O(1/\log U)$ changes and are absorbed in epsilon. Sum the fixed labels in norm. Since $kAd$ belongs to the full support of $A$, nonempty $k,d$ have prescribed bounded-power ranges; the possible $g$ form a divisor set. Divisor bounds and harmonic ideal counting give

$$
 \sum_{Nk,Nd\ll D}\frac{d_E(kd)^C}{NkNd}\ll_\epsilon U^\epsilon.
 \tag{25}
$$

All norm weights remain present before Minkowski. The smooth annuli and Fourier integrals have the stated fixed seminorm and height costs. This proves (18). QED.

The short factor is preserved before it is bounded. The original inverse theorem is never applied to $C_{kA}$ as an arbitrary coefficient sequence. Different common punctures in the separated factors are allowed because only the long actual inverse is submitted to its moment theorem; the other two factors use pointwise bounds with the same primitive character.

## 5. An exact smaller remaining expression

Set $B_0=U^{101/100}$ and $K_0=U^{1/100}$. In (5) insert respectively

$$
 \lambda_H(k,A)=\chi_0(NkNA/B_0),
$$
$$
 \lambda_S(k,A)=[1-\chi_0(NkNA/B_0)]\chi_k(Nk/K_0),
$$
$$
 \lambda_L(k,A)=[1-\chi_0(NkNA/B_0)]
                              [1-\chi_k(Nk/K_0)].           \tag{26}
$$

They sum to one pointwise. For their coherent signed expressions,

$$
                            M_u=M_{H,u}+M_{S,u}+M_{L,u}.    \tag{27}
$$

The first is the head in (13). In the second, $NkNA>B_0$ and $Nk<2K_0$, hence $NA>U/2$ and (18) proves

$$
 \sum_u w_U(u)|M_{S,u}|^2
     \ll U^{e_0(r)-1/750+\epsilon}(1+|t|)^A p_J(W)^2.
 \tag{28}
$$

The third has exact support restrictions

$$
                  Nk>U^{1/100},\qquad NkNA>U^{101/100},      \tag{29}
$$

including both smooth transitions. It retains the original coefficient, all signs, the $1/Nk$ weight, true mask, physical rows and common profiles. Its required but **unproved** estimate is

$$
 \sum_u w_U(u)|M_{L,u}|^2
 \ll U^{e_0(r)-1/1000+\epsilon}(1+|t|)^A p_J(W)^2,
                \qquad29/25\le r\le117/100.                 \tag{L}
$$

If (L) were proved, the triangle inequality with (13) and (28) would give the complete inverse input of the existing certified consumer and its conditional boundary $\operatorname{Re}s>0.8748856$, within the stated imported Eisenstein framework. This note proves the complementary components, not (L).

The large-$k$ channel cannot be discarded using its harmonic weight. The exact return of the full ratio complement is

$$
 D_{1-\chi_0,P}(\mathfrak a)
 =A_{y_1,y_2}(\mathfrak a)-H_{\chi_0,P}(\mathfrak a),\qquad
 H_{\chi_0,P}(\mathfrak a)
       \ll U^\epsilon(B_0/D)^{1-\beta}.                     \tag{30}
$$

Here $B_0/D\le U^{-3/20}$. Thus the error tends to zero by a fixed power after choosing the losses. At squarefree ideals below $y_2$,

$$
 A_{y_1,y_2}(\mathfrak a)
 =\mu_E(\mathfrak a)\sum_{d\mid\mathfrak a}w_0(Nd/y_1),
 \qquad\sum_{d\mid\mathfrak a}w_0(Nd/y_1)\ge1.               \tag{31}
$$

The old critical returned length $\log_U N\mathfrak a=0.745699942724290\ldots$ therefore retains its coefficient up to a small error. To reach that length from the high ratio requires $\log_U Nk>0.264300057275709\ldots$, inside (29). This is coefficient persistence and localization of the missing cancellation. It is not a row-mean lower bound, a saturation claim, or an impossibility theorem.

## 6. A marked joint estimate on the whole critical class box

The same exact arithmetic allocation gives a stronger **class-restricted** estimate. It is useful after a detector has fixed a compatible character, zero bin and prime-amplitude class. It does not assert an unrestricted full-row moment at the smaller returned length.

Retain a single buffered class with parameter $\delta$, and write $g=x\delta$ for its normalized prime amplitude. Its prime system must satisfy the original source's finite supply, disjoint underlying supports, fixed row-independent coefficients, common-character, height, and presentation conditions. More explicitly, for the finitely many total lengths $z$ selected below, the source selection procedure must supply a common product $Q_z$ of normalized prime polynomials such that

$$
 |Q_z(u)|\ge U^{gz-\epsilon_1}
 \quad\text{on the retained class}.                         \tag{32}
$$

The prime products are those of the source-compatible class; none is defined after independently selecting each row's inverse factors. The original full-supply condition, at least $1/5$ plus a fixed margin in row-width units, is more than enough for the maximum required $z$ below. The finite window mesh, row presentation split and losses remain those of that selection argument. Alternatively (32), with the stated original slot conditions, is a complete explicit prime-supply hypothesis for this lemma. It is not inferred merely from membership in a zero bin.

Let $T_{\sigma,u}$ be a coherent expression of the type in Section 4, with support $NA\gg U^\sigma$, where

$$
 \frac12\le\sigma-\alpha\le1,\qquad r-\alpha\ge1,
 \qquad0\le g\le\delta<\frac56.
$$

Assume (32) supplies the needed lengths up to $(1-\sigma+\alpha)/2$ with the source's fixed positive margins, achieved by reducing each positive capacity by an arbitrarily small fixed amount. Then

$$
 \sum_{u\in\mathcal B}w_U(u)|T_{\sigma,u}|^2
 \ll U^{\delta r+\mathcal T_\sigma(\delta,g,r)+\epsilon}
                              (1+|t|)^A p_J(W)^2,
 \tag{33}
$$

where

$$
 \boxed{\quad
 \mathcal T_\sigma(\delta,g,r)
 =\max\left\{
  1-g-(\delta-g)(\sigma-\alpha),\quad
  \frac16+\left(\frac56-\delta\right)(r-\alpha)
       \right\}.\quad}
 \tag{34}
$$

In particular, the number of original physical rows in the class with a compatible witness
$|T_{\sigma,u}|\gg U^{\delta r/2-\epsilon_1}$ is at most
$U^{\mathcal T_\sigma+\epsilon}$, after the usual fixed profile and height losses. For this counting consequence take weight one on the class, or require the chosen nonnegative weight to be bounded below there.

### Proof, including the added puncture

Use the exact $k,d,g$ allocation (19)--(21). To avoid confusing the prime-amplitude parameter $g$ with that ideal, call the gcd ideal $\mathfrak g$ in this paragraph. At any fixed annular triple the long inverse has log-length

$$
 \sigma-\alpha+O(1/\log U)\le b\le r-\alpha+O(1/\log U).
$$

For $1/2\le b<1$, take a source-allowed prime product of total length
$z=(1-b)/2-\epsilon_2$, with a sufficiently small fixed positive reduction and the original finite discretization. The marked inverse theorem has strict capacity conditions
$b+2z<1$ and $2b+8z<3$; the second has a fixed margin on this range away from $b=1/2$. If the selected capacity is below the small discretization threshold, use $z=0$ and the unmarked moment, losing only the allocated epsilon. At $b\ge1$, use the original unmarked inverse moment directly.

The extra puncture on the long inverse is harmless **without changing the prime amplitudes**. For its common radical $m$, exact Euler restoration is

$$
 M_{\psi_u1_{(\,\cdot\,,m)=1}}(B;V)
 =\sum_{\operatorname{rad}h\subset\operatorname{rad}m}
  \frac{\psi_u(h)}{\sqrt{Nh}}M_{\psi_u}(B/Nh;V).
 \tag{35}
$$

Multiply this identity by the original $Q_z$. Do not delete the primes of $m$ from $Q_z$. Every new inverse length is at most $b$, so it satisfies both original marked inequalities with the same $z$ and margins. The phases $\psi_u(h)$ are bounded row scalars, and their scalar mass is

$$
 \sum_{\operatorname{rad}h\subset\operatorname{rad}m}(Nh)^{-1/2}
 =\prod_{p\mid m}(1-(Np)^{-1/2})^{-1}\ll U^\epsilon.
$$

Consequently the original marked inverse theorem bounds this punctured inverse multiplied by the **unchanged** $Q_z$. If a baseline common puncture is already present in the amplitude definition, its zero indicator is just part of the row-independent prime coefficients; restore that puncture in the inverse by the same formula. No amplitude lower bound is transferred between distinct primitive presentations.

The other two factors use their same-bin pointwise estimates, with total log-length $r-b$. Their squared cost is $U^{\delta(r-b)+\epsilon}$. Divide the marked moment by (32). For the fixed annular triple, the class-restricted squared mean is thus at most

$$
 U^{1+\delta(r-b)-2gz+\epsilon}
 =U^{\delta r+[1-g-(\delta-g)b]+\epsilon}
                       \qquad(1/2\le b\le1).                \tag{36}
$$

The bounded discretization and strict-margin losses have been absorbed in epsilon. At $b\ge1$ the corresponding exponent is

$$
 U^{\delta r+[1/6+(5/6-\delta)b]+\epsilon}.                  \tag{37}
$$

Since $\delta-g\ge0$, (36)'s count exponent decreases with $b$; since $\delta<5/6$, (37)'s increases. Their common value at $b=1$ is $1-\delta$. Thus their maximum over the full permitted interval is exactly (34). The harmonic $k,d$ sums, divisor choices of $\mathfrak g$, common Fourier integrals and source-compatible finite label splits cost only the allocated subpower and fixed profile/height factors, as in Section 4. This proves (33).

The original marked theorem is the pinned source's `lem:marked`, at row width one, with its strict inequalities. No Hecke-field extension of Liu's optimized moment parameter is used here. The full-supply interpretation is the same source-compatible selection convention already retained in `third-pass/SHORT_INVERSE.md` and the original Eisenstein consumer. All buffered frequency budgets remain shared as in Section 2.

### Exact uniform corollary for the active critical box

Take

$$
 \sigma=\frac{79}{100},\qquad
 \frac{473}{1024}\le\delta\le\frac{487}{1024},\qquad
 \frac{49}{100}\le x=\frac g\delta\le\frac12,
 \qquad \frac{29}{25}\le r\le\frac{117}{100}.
 \tag{38}
$$

Then $\sigma-\alpha=387/500$ and the maximum marked prime length is
$113/1000<1/5$. Both branches in (34) improve the old complete-inverse count exponent $e_0(r)-\delta r$ by more than $1/1000$.

For the shorter endpoint, the exact gap is

$$
 \frac{5r-5}{6}
  -\delta\{r-x-(1-x)(\sigma-\alpha)\}.
 \tag{39}
$$

It increases with $r$ and $x$ on (38) and decreases with $\delta$. Its minimum is therefore at
$(r,\delta,x)=(29/25,487/1024,49/100)$, where it equals

$$
                         \frac{372257}{153600000}
                         =0.002423548177083\ldots.
 \tag{40}
$$

For the longer endpoint the gap is

$$
 \alpha\left(\frac56-\delta\right)
                   \ge\frac{1099}{192000}
                   =0.005723958333333\ldots.                \tag{41}
$$

All moment, mesh, strict-capacity and profile losses can be chosen below the fixed reserve in (40). This is a proved estimate for a precisely specified coherent component on compatible detected classes. The complete complementary large-divisor expression remains open.

## 7. A marked fourth moment removes small returned variables

There is a complementary estimate for small returned $A$. It uses a fourth moment of the **coherent component**, with the actual original ordinary factor. It does not use a product of independent row counts.

Use a compatible buffered class and prime system as in Section 6, with the following stronger prime-coefficient restriction for this section. The additional external moment is the pinned source's `lem:plain`, with two copies of the ordinary factor, its common-puncture conventions, and $\kappa=3/4$. Before the common mask is applied, each positive-length prime-slot coefficient is a **fixed finite linear combination of finite-ray characters from the source's fixed finite group**. The finite list and its coefficients are independent of U and of the row. The broader arbitrary bounded slot coefficients admitted by the inverse marked theorem in Section 6 are not sufficient here. The premise $\beta_*\le(1+\kappa)/2$ is exactly the imported $7/8$ family cap. Nonempty slots obey the ordinary theorem's fixed individual mesh, and the compatible supply/selection procedure retains that mesh and disjoint underlying supports. Its empty-slot case has no bounded ordinary-length restriction.

For positive slots, the source also excludes every row whose primitive inducing character belongs to its fixed finite ray group $\Theta$, not just principal rows. This exclusion is automatic for the sufficiently large physical rows in the present scope: outside the fixed bad-prime set S, any prime of a sixth-power-free row has valuation in $\{1,\ldots,5\}$ and supplies a nontrivial local residue character. An S-supported fixed ray twist cannot cancel that local character, whereas every member of $\Theta$ has conductor supported in S. Rows supported entirely in S have bounded norm because their valuations are at most five, and these bounded exceptions are handled before applying the theorem. The common natural puncture changes zeros, not the primitive inducing character. Thus the positive-slot use is on the source's actual allowed row set. A proposed enlargement to moving twists outside S would have to preserve this inducing-character exclusion explicitly; it is not included in the present automatic argument.

Let $T_{\le\lambda,u}$ be a coherent expression as in (5), with a common smooth cutoff supported on $NA\ll U^\lambda$, together with any of the fixed smooth ratio or arithmetic-scale selectors already permitted in Section 4. Suppose $c_0=r-\lambda>0$. Define

$$
 \mathcal P(c;\delta,g)=
 \begin{cases}
  1-2\delta c-\dfrac{4g}{9}(1-2c),&0\le c\le1/2,\\
  1-2\delta c,&c\ge1/2.
 \end{cases}                                               \tag{42}
$$

Provided the source-compatible prime products supply the selected lengths up to $2\max(0,1-2c_0)/9$, with the stated mesh and strict reserved losses,

$$
 \boxed{\quad
 \sum_{u\in\mathcal B} w_U(u)|T_{\le\lambda,u}|^4
 \ll U^{2\delta r+\mathcal P(r-\lambda;\delta,g)+\epsilon}
                                  (1+|t|)^A p_J(W)^4.
 \quad}                                                     \tag{43}
$$

Consequently the number of physical rows with a compatible witness
$|T_{\le\lambda,u}|\gg U^{\delta r/2-\epsilon_1}$ is at most
$U^{\mathcal P(r-\lambda;\delta,g)+\epsilon}$, under the same
weight-one or bounded-below-weight convention as in Section 6.

**Proof.** Expand the actual modified coefficient using (19)--(21).
For a common annular triple, let $c$ be the ordinary length and let the
two actual inverse lengths be $a_0,b_0$. Then

$$
 a_0+b_0+c=r+O(1/\log U),\qquad
                         c\ge r-\lambda+O(1/\log U).
$$

Both inverse polynomials have the same primitive character as the
buffered bin, with their explicit common added punctures. Their
pointwise **fourth** powers contribute at most
$U^{2\delta(r-c)+\epsilon}$. The ordinary polynomial still has
exactly the original natural character $\psi_u$, without either of
those extra punctures.

For $c<1/2$, select a common source-allowed prime product $Q_z$ of
total length $z=2(1-2c)/9-\epsilon_2$, allowing the fixed source mesh
and reserving a small positive margin. The ordinary moment condition is

$$
                2c+6\kappa z=2c+\frac92z<1.
$$

Multiply the coherent component by $|Q_z|^{1/2}$ **before** taking
its $L^4$ norm. Minkowski in that weighted $L^4$ space, followed by
the pointwise inverse bounds, leaves exactly the permitted source
moment

$$
 \sum_u |S_{\psi_u}(U^c;V)^2 Q_z(u)|^2\ll U^{1+\epsilon}.
$$

The scalar label weights are still $1/(NkNd)$; the divisor choices,
common Fourier integrals and harmonic sums have the same subpower
bound as in (25). Thus the coherent weighted fourth moment is at most
$U^{1+2\delta(r-c)+\epsilon}$. The amplitude lower bound (32) gives
$|Q_z|^2\ge U^{2gz-\epsilon_3}$ on the class, hence

$$
 \sum_{u\in\mathcal B}w_U(u)|T_{c,u}|^4
 \ll U^{2\delta r+[1-2\delta c-2gz]+\epsilon}.
 \tag{44}
$$

For zero or sufficiently small selected capacity, use the empty-slot
ordinary fourth moment; for $c\ge1/2$ it gives the second branch
of (42) directly. The common prime product is chosen separately for
each of the source's finitely discretized c-ranges before summing its
arithmetic labels. After removing its amplitude lower bound, apply
ordinary $L^4$ Minkowski to the resulting unweighted c-components.
This order does not assume one prime product works at every length.

The function (42) is continuous at $c=1/2$ and decreasing: below that
point its derivative is $-2\delta+8g/9\le-10\delta/9<0$ when
$g\le\delta$, and above it the derivative is $-2\delta<0$.
At $\delta=0$ it is simply nonincreasing. Thus the largest exponent
occurs at the smallest permitted $c=r-\lambda$. All constant scale,
mesh, buffer, strict-capacity and finite-profile losses fit in the
reserved epsilon. This proves (43). QED.

### An exact low-returned bound on the critical box

On the full box (38), take $\lambda=73/100$. Then
$43/100\le r-\lambda\le44/100$ and the maximum needed prime
length is $7/225<1/5$. The gap from the old inverse count is

$$
 e_0(r)-\delta r-\mathcal P(r-\lambda;\delta,x\delta)
 =\frac{5r-5}{6}
  +\delta\left\{r-2\lambda+
                    \frac{4x}{9}(1-2r+2\lambda)\right\}.
 \tag{45}
$$

It increases with r and x and decreases with delta on (38). For the
last assertion, the expression in braces is strictly negative on the
whole box; the other derivatives are
$5/6+\delta(1-8x/9)>0$ and
$(4\delta/9)(1-2r+2\lambda)>0$.
The exact minimum is therefore the same rational corner as in (40):

$$
 \boxed{\quad
 e_0(r)-\delta r-\mathcal P(r-73/100;\delta,g)
 \ge\frac{7427}{1440000}
       =0.005157638888888\ldots>\frac1{1000}.
 \quad}                                                     \tag{46}
$$

Together, Sections 6 and 7 leave only the intermediate returned scale
$U^{73/100}<NA<2U^{79/100}$, with specified complementary smooth
cutoffs, when counting compatible critical witnesses. The full-ratio
pointwise head bound (9) can simultaneously localize the reduced
numerator $NkNA$ close to D. These restrictions are literal restrictions
on the exact sum (5), after its complete coefficient is retained; they
are not a false support inference obtained from the ratio cutoff alone.
The estimate for that remaining coherent intermediate component is still
open.

## 8. A separate identity with a thinner final primal band

This section changes the asymmetric cutoff **in a new, explicitly
distinguished identity**. Earlier assertions using $\alpha=2/125$,
including the unmarked $1/750$ far theorem, remain unchanged.

Set

$$
 \widetilde\alpha=\frac1{250},\qquad
 \widetilde y_1=U^{1/250},\qquad
 \widetilde y_2=2D/U^{1/250},
$$
$$
 \widetilde A(m)=\sum_{ab=m}\mu_E(a)\mu_E(b)
       w_0(Na/\widetilde y_1)w_0(Nb/\widetilde y_2),\qquad
 \widetilde C_a(P)=\sum_{(d,P)=1}\frac{\widetilde A(ad)}{Nd}.
 \tag{47}
$$

The same exact unequal-cutoff identity gives, for sufficiently large U,

$$
 M_u=-D^{-1/2}\sum_{m,c}\widetilde A(m)\psi_u(mc)V(NmNc/D).
 \tag{48}
$$

The bounded initial scale range is again absorbed in the constants.
This does not assert any finite numerical zero-height verification.

The pointwise ratio-head theorem (9) holds unchanged for this new
coefficient: its proof uses $y_1y_2=2D$ and bounded-power cutoff ranges,
not the particular split. The marked endpoint theorem (34) holds with
$\alpha$ replaced by $\widetilde\alpha$; the exact allocation,
puncture restoration and source slot hypotheses are identical. The
ordinary fourth-moment theorem (43) is independent of this split.
These statements can also be applied directly to (48), without the gcd
return: set $k=d=g=1$ in the allocation, leaving the two original
Möbius factors and the original ordinary factor.

Choose

$$
 \widetilde\sigma=\frac{773}{1000},\qquad
 \widetilde\lambda=\frac{147}{200}=0.735,
$$
$$
 \Xi_U(m)=\chi_0(Nm/U^{773/1000})
                          -\chi_0(Nm/U^{147/200}).           \tag{49}
$$

This is a common smooth selector supported on

$$
                  U^{0.735}<Nm<2U^{0.773}.                  \tag{50}
$$

Define the **literal primal band**

$$
 \boxed{\quad
 B_u=-D^{-1/2}\sum_{m,c}\widetilde A(m)\psi_u(mc)
                          V(NmNc/D)\Xi_U(m).
 \quad}                                                     \tag{51}
$$

The remaining low and high weights are respectively
$\chi_0(Nm/U^{147/200})$ and $1-\chi_0(Nm/U^{773/1000})$.
Together with (49) they sum to one, so (48) is exactly low + band +
high. On the full critical box (38), both complementary components have
class-restricted large-value counts smaller than
$U^{e_0(r)-\delta r-1/1000+\epsilon}$.

For the high piece, the smallest long inverse length is
$\widetilde\sigma-\widetilde\alpha=769/1000$. Formula (39)
with this lower length is minimized at the same rational corner as
before. Its gap, and the other high endpoint gap, are exactly bounded by

$$
 \frac{371959}{307200000}
       =0.001210804036458\ldots,\qquad
 \frac{1099}{768000}=0.001430989583333\ldots.                \tag{52}
$$

For the low piece the minimum ordinary length is
$r-147/200\in[17/40,87/200]$. Formula (45) gives the exact uniform
gap

$$
                            \frac{23}{16000}=0.0014375.     \tag{53}
$$

The required maximum marked prime lengths are $231/2000$ for the high
inverse endpoint and $1/30$ for the low ordinary endpoint, both below
the retained $1/5$ full supply. The inverse and ordinary coefficient
conventions remain distinct exactly as in Sections 6 and 7. All strict
capacity, mesh, height and profile losses can be chosen below the fixed
reserves beyond $1/1000$ in (52)--(53).

Thus an improved count for large values of the single expression (51)
is sufficient for the critical-class native-witness improvement. It is
still unproved. The same pointwise identity also shows necessity modulo
the two already controlled complementary witness sets. This final
formulation does not introduce any artificial large-divisor variable
into the new arithmetic hypothesis.

### Ratio-head stability under a returned-variable selector

The pointwise head estimate has one useful stable extension. In its
fixed-$k$ return (5), insert any fixed finite product or difference of
common smooth cutoffs in the returned variable A, with uniformly bounded
logarithmic derivatives. Then

$$
 |M_{\chi_B,\Xi,u}|\ll
          (B/D)^{1/8}D^{\delta/2}U^\epsilon\,\mathcal P
 \tag{54}
$$

on the same buffered bin, for either coefficient choice in this note.
Here $\chi_B$ acts on $NkNA$, while $\Xi$ acts on $NA$;
$\mathcal P$ denotes the licensed fixed profile and height factors.

To verify (54), split the ratio head into $NkNA\asymp B'\ll B$.
For a fixed $k$, the modified block has scale $R=B'/Nk$; multiplying
its common annular test by $\Xi(Rx)$ preserves uniform logarithmic
derivative bounds. The coefficient lemma and the same-bin ordinary
factor therefore give exactly the same fixed-$k$ bound as (11), with
$B'$ in place of B. Its harmonic k sum and smooth B' partition give
(54). No row-dependent column selector or sharp terminal cutoff is used.

Now use the coefficient (47), let $\kappa_0=1/100$, and take
$B=D/U^{\kappa_0}$. In the exact k-return with the band selector (49),
let $R_u$ denote the part weighted by $1-\chi_0(NkNA/B)$. The full
finite divisor inversion (6) gives

$$
              R_u=B_u-M_{\chi_B,\Xi,u},\qquad
 |M_{\chi_B,\Xi,u}|
      \ll U^{-1/800+\epsilon}D^{\delta/2}\mathcal P.         \tag{55}
$$

Consequently, after reserving the source height/profile losses, large
witnesses at exponent $\delta r/2$ for $R_u$ and the literal primal
band $B_u$ differ only by a pointwise negligible term. This is an exact
identity with a proved error estimate, not an inferred support rule.

In the high-ratio representation, the additional original-divisor
index d obeys $NkNA Nd<8D$. Together with (49) and the ratio lower
cutoff, this gives

$$
 Nd<8U^{1/100},\qquad
 \frac{D}{2U^{783/1000}}<Nk<\frac{8D}{U^{147/200}}.         \tag{56}
$$

These large k labels are a property of that representation of (51).
They are not a separate new source of cancellation. In fact at d=1,
writing $k=\mathfrak g m$ in (19) gives
$\mu(k)\mu(\mathfrak g)\mu(m)=1$ on its squarefree coprime
support. A long literal Möbius polynomial in k cannot be inferred from
its displayed inversion sign alone.

### Why optimizing the two old marked moments does not close the band

This can be stated as an exact resource calculation, without claiming
that actual rows saturate the bounds. Fix a class $(\delta,g,r)$ and
write $R_0=e_0(r)-\delta r$. The inverse and ordinary count lines are

$$
 I(b)=1-g-(\delta-g)b,\qquad
 P(c)=1-2\delta c-\frac{4g}{9}(1-2c).
$$

For a target improvement $\eta>0$, the high-returned threshold based
on I must be at least

$$
 \alpha+\frac{1-g-R_0+\eta}{\delta-g},
$$

while the low-returned cutoff based on P can be at most

$$
 r-\frac{1-4g/9-R_0+\eta}{2\delta-8g/9}.                  \tag{57}
$$

At an old contact with $b_*+c_*=r$, where $I(b_*)=P(c_*)=R_0$,
the gap between these thresholds is exactly

$$
 \boxed{\quad
 \alpha+\frac{\eta}{\delta-g}
                +\frac{\eta}{2\delta-8g/9}>0.
 \quad}                                                     \tag{58}
$$

The long-inverse endpoint also requires
$\alpha(5/6-\delta)\ge\eta$. Hence even optimizing the positive
asymmetry cannot erase the gap for a fixed positive saving using only
these resources.

There is a fully rational contact inside the actual critical box:

$$
 \delta=\frac{47}{100},\qquad g=\frac{47}{200},\qquad
 r=\frac{6994}{6007}
   =\frac{185-96\delta}{185-138\delta}.
 \tag{59}
$$

Substitution into I, P and $R_0$ verifies the contact and $b_*+c_*=r$
exactly. Thus (58) is not an artifact of rounded critical decimals or
an unsupported change of the field's moment parameter. It tests the
original $\kappa=3/4$ ordinary moment. A stronger joint arithmetic
estimate or a coherent signed cancellation argument is still needed
inside (51); the present localized result does not supply it.

## 9. Verification boundary

`check_middle_joint.py` verifies the fixed-$k,d,g$ Möbius allocation and punctures, the finite divisor return, normalization, rational radical margin, two-branch far exponent, and complementary selectors. Negative controls remove required allocations or masks, or request an inadmissible saving. Its predicates remain active under `python -O`.

Finite checks do not prove the imported cap, density theorem, native inverse moment, logarithmic control, ordinary functional equation, or open estimate (L). Those premises and the analytic proof remain explicit parts of the result.

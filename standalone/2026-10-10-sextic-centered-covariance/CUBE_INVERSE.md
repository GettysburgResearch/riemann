# Removing the cube completion with both angular Möbius variables

**Status:** proposed source-conditional theorem with a complete analytic adapter. The argument removes the full cube completion from the balanced two-factor polynomial over squarefree primary rows. It uses the exact all-cusp coefficient factorization, the reunited-divisor cutoff, and two conductor-uniform scalar Möbius estimates. It does not establish the original short-row fourth moment, a generalized moment hierarchy, a centered covariance estimate, or RH.

**Exact dependencies:** OpenAI math commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`, October 5 `build/paper2.tex`, especially `eq:T`, `eq:completed-twist`, and `eq:cube-inverse`; PR #915 at `9959364671f89b86f3992ec5ed5e19f804eb607b`, `COUPLED_THETA_COMPLETION.md`, Sections 1–3 and Lemma 6.1; `centered_a2_attack.md`, frozen SHA-256 `bbc139f956731482fcf9e33645bfe2832b7b7471594d9cbc1f21cd08eaf2ac5a`, especially Lemma 6.3, Corollary 6.4, and the moving-mask proof of Theorem 7.1; `reunited_cusp_cutoff.md`, frozen SHA-256 `89cd204ae66ef615e7d630bf2c1e5524e134b76e30789dce7796a229e53a4340`, Theorem 3.1; and `all_cusp_gauss_factorization.md`, frozen SHA-256 `b596f3f7c43bb84c699201f3b14c81eae18ae89d3b45e2357bcdccfb9eb3ea1c`, particularly its exact separated expression (3.2), normalization (3.3), and all-cusp factorization proof. The last input is an exact coefficient statement, not merely the inequality in its Theorem 4.1.

**What was checked natively here:** the cube inverse and its normalization against the imported source; the combined exact support insertion; the finite shared-divisor correction for two inverse factors; both common-divisor extractions with all surviving masks; the resulting norm factors; and the optimization of the complete smooth-block estimate. The upstream automorphy, cusp formulas, classical upper sieves, and the source-conditional angular scalar theorem are retained as named inputs.

## 1. The exact polynomial and its cube inverse

Work in the Eisenstein field with the fixed primary-generator convention of the sources. Every original ideal index is outside a fixed finite bad set \(S\), containing the primes over \(6\) and the fixed ray conductors. Let

\[
a_\xi(n)=\alpha(n)^{-1}\gamma_2(n)\xi(n),\qquad
\Psi_{k,a}(n)=\xi(n)\chi_n(k)\chi_n(a)^4.
\tag{1.1}
\]

All characters retain their literal nonunit zeros. An asterisk means squarefree; unstarred primary cube indices need not be squarefree. Fix smooth compactly supported \(W_1,W_2\), with supports in fixed compact subintervals of \((0,\infty)\), and set \(V_*(x)=\sqrt{x}W_2(x)\). The source completion is

\[
T(X;k,a)=\sum_n^*\sum_b
\frac{a_\xi(n)\chi_n(k)\chi_n(a)^4
      \alpha(b)^{-3}\Psi_{k,a}(b)^3}
     {\sqrt{Nn}\,Nb}
V_*\!\left(\frac{Nn(Nb)^3}{X}\right).
\tag{1.2}
\]

The \(n,b\) in (1.2) are outside \(S\). Reflected theta indices will be allowed to meet \(S\), as in the all-cusp source. Define

\[
P_{A,B}(k)=\frac1{\sqrt{AB}}
\sum_{\substack{a,n\text{ squarefree}\\(a,n)=1}}
a_\xi(an)\chi_{an}(k)
W_1(Na/A)W_2(Nn/B).
\tag{1.3}
\]

This is the literal two-factor squarefree polynomial. Let

\[
\mathcal C^{(h)}_{A,X}(k)=\frac1{\sqrt A}
\sum_{\substack{a\text{ squarefree}\\(a,h)=1}}
a_\xi(a)\chi_a(k)W_1(Na/A)T(X;k,a).
\tag{1.4}
\]

### Lemma 1.1. Exact removal of the cubes

For every nonzero row \(k\),

\[
\boxed{
P_{A,B}(k)=\sum_h
\frac{\mu(h)\alpha(h)^{-3}\xi(h)^3\chi_h(k)^3}{Nh}
\mathcal C^{(h)}_{A,B/(Nh)^3}(k).
}
\tag{1.5}
\]

The \(h\)-sum is squarefree through its Möbius coefficient. In particular there is no extra power of \(Nh\) in (1.5) and no restriction \((h,n)=1\).

**Proof.** Apply `eq:cube-inverse` in the imported source with \(X=B\) and auxiliary index \(a\). Its coefficient is exactly

\[
\frac{\mu(h)\alpha(h)^{-3}\Psi_{k,a}(h)^3}{Nh}.
\]

Because

\[
\Psi_{k,a}(h)^3
=\xi(h)^3\chi_h(k)^3\chi_h(a)^{12}
=\xi(h)^3\chi_h(k)^3\mathbf1_{(h,a)=1},
\tag{1.6}
\]

the only new column exclusion is precisely the one in (1.4). Multiply the source identity by \(A^{-1/2}a_\xi(a)\chi_a(k)W_1(Na/A)\) and sum over \(a\). The Gauss CRT law turns its left side into (1.3).

One can also check the normalization directly. Substitution of (1.2) into the unseparated inverse makes the total cube index \(c=hb\). Complete multiplicativity gives the coefficient \(\alpha(c)^{-3}\Psi_{k,a}(c)^3/Nc\), and the smoothing argument is \(Nn(Nc)^3/B\). The sum over \(h\mid c\) is \(\sum_{h\mid c}\mu(h)=\mathbf1_{c=1}\). The remaining denominator and test satisfy \(V_*(Nn/B)/\sqrt{Nn}=B^{-1/2}W_2(Nn/B)\). This proves (1.5), including its normalization and every zero mask. \(\square\)

If \(v_2=\sup\operatorname{supp}W_2\), the complete \(h\)-term is zero when \((Nh)^3>v_2B\). Before reflection insert a fixed smooth cutoff equal to one for \((Nh)^3\le v_2B\) and zero for \((Nh)^3\ge2v_2B\), and then sum over all \(h\). This preserves (1.5) exactly and makes the later scalar tests smooth. We do not retain a sharp truncation inside a scalar Möbius sum.

## 2. The scalar input for each of the two variables

Fix \(1/2<\beta\le1\). The required scalar hypothesis is the following uniform statement. For every fixed ray character \(\eta\) in the finite family occurring below,

\[
M_{\eta,C}(k;L,V)
=\sum_{(r,CS)=1}\mu(r)\eta(r)\alpha(r)^{-3}
\chi_k(r)^3V(Nr/L)
\ll D^\epsilon L^\beta\|V\|_{C^J(I)}.
\tag{2.1}
\]

Here \(k\) is squarefree primary outside \(S\), \(Nk,NC,L\) are polynomially bounded in \(D\ge2\), and \(V\) has support in a fixed compact \(I\subset(0,\infty)\). The constants and finite seminorm order are independent of the moving row, conductor, exclusion, and length. Every nonempty length below one lies in a fixed compact positive interval and is included by elementary counting. Empty smaller lengths contribute zero.

The negative Ramanujan factor uses the finite character \(\eta_g\) in the all-cusp source. The inverse cube factor uses \(\xi^3\), followed by the fixed ray factors of quadratic reciprocity. Indeed, after fixing the row ray class, \(\chi_h(k)^3\) becomes \(\chi_k(h)^3\) times a fixed ray character of \(h\) and a bounded row scalar. Literal zeros agree also when \((h,k)>1\). Thus both variables have exactly the angular power \(-3\), with possibly different fixed finite characters.

Two versions of (2.1) are available:

- \(\beta=1\) follows from elementary ideal counting.
- \(\beta=11/12\) follows from the source-conditional angular note. Its Lemma 6.3 applies to every finite twist at fixed angular type \(-3\), so it covers the inverse cube character as well as the negative Ramanujan character. No finite-order result is applied directly to an infinite-order character.

### Lemma 2.1. Two coprime inverse factors admit both scalar savings

For fixed \(\eta_1,\eta_2\), let

\[
\lambda_{i,k}(r)=\eta_i(r)\alpha(r)^{-3}\chi_k(r)^3
\]

and put

\[
B_C(k;L_1,L_2)
=\sum_{\substack{(r_1r_2,CS)=1\\(r_1,r_2)=1}}
\mu(r_1)\lambda_{1,k}(r_1)
\mu(r_2)\lambda_{2,k}(r_2)
V_1(Nr_1/L_1)V_2(Nr_2/L_2).
\tag{2.2}
\]

Under (2.1), uniformly in the same moving parameters,

\[
\boxed{|B_C(k;L_1,L_2)|\ll D^\epsilon(L_1L_2)^\beta}
\tag{2.3}
\]

with a product of fixed finite test seminorms understood.

**Proof.** Use the exact finite expansion

\[
\mathbf1_{(r_1,r_2)=1}=\sum_{\ell\mid r_1,r_2}\mu(\ell),
\qquad r_i=\ell s_i.
\tag{2.4}
\]

Since the two original variables are squarefree, both \(s_i\) must be coprime to \(\ell\). No condition \((s_1,s_2)=1\) remains. Complete multiplicativity, including at zeros, and \(\mu(\ell s_1)\mu(\ell s_2)=\mu(s_1)\mu(s_2)\) on this support give

\[
\begin{aligned}
B_C(k;L_1,L_2)
={}&\sum_{(\ell,CS)=1}^*
\mu(\ell)\lambda_{1,k}(\ell)\lambda_{2,k}(\ell)\\
&\qquad\times M_{\eta_1,C\ell}(k;L_1/N\ell,V_1)
M_{\eta_2,C\ell}(k;L_2/N\ell,V_2).
\end{aligned}
\tag{2.5}
\]

The row multiplier has modulus at most one. More explicitly, its quadratic row factor is \(\chi_k(\ell)^6=\mathbf1_{(k,\ell)=1}\), retaining its zero. Apply (2.1) to both shifted lengths and moving exclusions. Their total absolute cost is

\[
D^\epsilon(L_1L_2)^\beta
\sum_{\ell}(N\ell)^{-2\beta}
\ll_\beta D^\epsilon(L_1L_2)^\beta,
\tag{2.6}
\]

since \(2\beta>1\). Only polynomially bounded \(\ell\) occur on the compact test supports, and nonempty shifted subunit lengths stay in a fixed compact positive interval. This proves (2.3). The common angular factor at \(\ell\) is used only as a bounded coefficient; no scalar theorem at angular type \(-6\) is needed.

Norm modulations \(V_i(x)x^{it_i}\) have finite seminorms bounded by fixed polynomials in \(|t_i|\), so the same proof is uniform for the Mellin-separated tests used below. \(\square\)

## 3. The exact joint support restriction

In a first reflected \(h\)-term of (1.5), write the original outer squarefree index as \(a=qg\), where \(q\) retains both positive Ramanujan choices reunited and \(g\) records every negative choice. This \(q\) is the positive label called \(h\) in the cutoff source; it is distinct from the inverse cube index \(h\) here.

For fixed \(h,q,g,k\), the exclusion \((a,h)=1\) is independent of the theta frequency. The reunited-divisor theorem therefore applies with completion scale \(X=B/(Nh)^3\). Its complete reflected frequency sum is zero if

\[
(Ng)^2>C_*\frac{B}{(Nh)^3}.
\tag{3.1}
\]

Choose a fixed smooth \(\zeta\) equal to one on \([0,1]\) and zero on \([2,\infty)\). Multiply the reunited term by

\[
\boxed{\zeta\!\left(\frac{(Ng)^2(Nh)^3}{C_*B}\right).}
\tag{3.2}
\]

Equation (3.1) makes this an exact operation. Only now split the positive label \(q=ef\) by the original frequency-dependent positive allocations, and reindex the theta indices as in the all-cusp source. No individual unsummed \(e,f,g\) component is asserted to have the support (3.1) before this insertion.

Use fixed smooth dyadic partitions in \(Ne,Nf,Ng,Nh\), with scales \(E,F,G,Z\gg1\). Their nonempty modified blocks satisfy

\[
EFG\asymp A,\qquad G^2Z^3\ll B.
\tag{3.3}
\]

On such a block, (3.2) is a smooth function of \(Ng/G\) and \(Nh/Z\) with uniformly bounded rescaled derivatives. For the blocks on which it is not identically zero, the parameter \(G^2Z^3/(C_*B)\) is bounded. The smooth \(h\)-cutoff of Section 1 has the same property. Thus both cutoffs may be Mellin-separated with the existing norm kernel before any scalar estimate or sieve. The resulting Mellin majorants have arbitrarily many polynomial frequency moments.

After a common-divisor extraction, including the shared label of Lemma 2.1, the ratios to the new dyadic lengths are unchanged. For example, if \(g=d\ell g''\), then \(Ng/G=Ng''/(G/(NdN\ell))\). Therefore these smooth controls survive every length shift below.

## 4. The full-cusp block estimate after cube inversion

### Theorem 4.1

Let \(P_{E,F,G,Z}(k)\) be a complete modified smooth block of the exact inverse (1.5), defined after the exact insertion (3.2). Under (2.1),

\[
\boxed{
\sum_{k\sim H}^*|P_{E,F,G,Z}(k)|^2
\ll D^\epsilon G^{2\beta-2}Z^{2\beta-2}
\left[HE+Y+(EY)^{2/3}\right],
\qquad Y=\frac{H^2EG^2Z^3}{BF}.
}
\tag{4.1}
\]

The rows are squarefree primary outside \(S\). The block includes all first-reflection cusps, theta units, ramified valuations, squarefree bad-prime parts, and unrestricted reflected cube indices.

**Proof.** Invoke the exact coefficient factorization in the all-cusp source, not merely its final norm inequality. Fix the theta unit, ramified valuation \(m\ge-4\), squarefree bad-prime part \(n_S\), the positive cube-allocation index \(f\), and the reflected cube index \(b'\). Split all fixed ray conditions into their finite character families. Separate the common smooth norm kernel, the two support cutoffs, and the dyadic weights before applying any norm estimate.

After bounded separated norm ratios have been placed into the coefficient vectors, the common prefactor is

\[
\frac{3^{-m/3}}{Z\sqrt{AFG}\,Nb'},
\tag{4.2}
\]

up to fixed \(n_S\)-constants. The factor \(1/Z\) is the coefficient \(1/Nh\) in (1.5); its ratio \(Z/Nh\) is a bounded smooth test on the \(h\)-dyad. The variable squarefree theta index \(n_0\) is outside \(S\), at dyadic length \(U\), with common effective scale

\[
U\lesssim\frac{Y}{3^mNn_S(Nb')^3},
\tag{4.3}
\]

and the usual rapidly decreasing tails.

The remaining arithmetic expression is, with separate bounded vectors \(u_e,v_{n_0}\),

\[
\begin{aligned}
\sum_{e,g,h,n_0}^*
&\frac{u_e v_{n_0}}{\sqrt{Nn_0}}
\mu(g)\lambda_{g,k}(g)\mu(h)\lambda_{h,k}(h)
\chi_k(n_0)^3\chi_{n_0}(e)^4\\
&\quad\times\mathbf1_{(k,ef)=1}
\mathbf1_{(g,ef)=1}\mathbf1_{(h,efg)=1}.
\end{aligned}
\tag{4.4}
\]

Here \(\lambda_{g,k},\lambda_{h,k}\) have exactly the form in Lemma 2.1. The vector \(u_e\) retains \((e,f)=1\), and \(v_{n_0}\) retains \((n_0,f)=1\). The restriction \((e,n_0)=1\) is the literal zero of \(\chi_{n_0}(e)^4\). The omitted fixed row factors, including \(\chi_k(n_Sb')^3\), have modulus at most one. There is no \((g,n_0b')=1\) or \((h,n_0b')=1\) condition.

### The two common-divisor extractions

Keep \((g,h)=1\) temporarily, and expand exactly

\[
\mathbf1_{(e,g)=1}\mathbf1_{(e,h)=1}
=\sum_{d\mid e,g}\sum_{j\mid e,h}\mu(d)\mu(j).
\tag{4.5}
\]

The retained \((g,h)=1\) forces \((d,j)=1\). Set

\[
e=dj e',\qquad g=dg',\qquad h=jh'.
\tag{4.6}
\]

Squarefreeness and the remaining masks are exactly as follows:

- \((d,j)=1\), \((dj,f)=1\), and \((e',djf)=1\);
- \((g',fdj)=(h',fdj)=1\), with \((g',h')=1\);
- \((n_0,f)=1\), with the factor \(\chi_{n_0}(dj)^4\) retained in its coefficient;
- the row mask \((k,djf)=1\), followed by the surviving moving mask \((k,e')=1\).

There is no remaining \((e',g')=1\) or \((e',h')=1\) condition: (4.5) has replaced those conditions by a signed divisor sum. We apply (4.5) to the product expression (4.4), which supplies an extension away from its original coprime support. That extension is used only inside an exact inclusion–exclusion identity.

On the retained squarefree support,

\[
\mu(d)\mu(j)\mu(dg')\mu(jh')=\mu(g')\mu(h').
\tag{4.7}
\]

All other \(d,j\)-factors separate. The factor \(\chi_{n_0}(dj)^4\) enters the \(n_0\)-vector; \(u_{dje'}\), including any Gauss CRT factor, remains a bounded vector in \(e'\); and the extracted row characters and \((k,djf)=1\) are row contractions. In particular no new moving interaction with \(g'\) or \(h'\) is introduced.

For fixed \(d,j,f\), apply Lemma 2.1 with

\[
C=fdj,\qquad L_1=G/Nd,\qquad L_2=Z/Nj.
\tag{4.8}
\]

This handles \((g',h')=1\) exactly and gives, for each row and independently of \(e',n_0\),

\[
D^\epsilon(G/Nd)^\beta(Z/Nj)^\beta.
\tag{4.9}
\]

Both scalar estimates retain their moving conductor and exclusion. The joint arithmetic factor has now become a bounded row multiplier, so using (4.9) before the remaining row norm is legitimate.

For clarity, the common label \(\ell\) in that lemma is coprime to \(fdj\), but it need not be coprime to \(e'\). No \((e',\ell)=1\) condition may be inserted: the two earlier exclusions involving \(e\) have already been expanded away. Thus the three correction labels have norm costs \((Nd)^{-\beta-1/2}\), \((Nj)^{-\beta-1/2}\), and \((N\ell)^{-2\beta}\), with precisely the masks just listed.

### The remaining quadratic–cubic norm

Put \(E'=E/(NdNj)\). The remaining \(e',n_0\) expression is \(\sqrt{E'}\) times the composition in PR #915, Lemma 6.1, after absorbing \(\sqrt{U/Nn_0}\) into its bounded \(n_0\)-vector. Its exact row mask remains \((k,e')=1\). The restrictions involving the fixed \(d,j,f\) are separate coefficient restrictions. Therefore

\[
\sum_{k\sim H}^*|Q_k(E',U)|^2
\ll D^\epsilon\frac{H+U}{U}
\left[E'+U+(E'U)^{2/3}\right].
\tag{4.10}
\]

That cited lemma retains the moving row mask by inclusion–exclusion and divisor Cauchy, followed by the quadratic and cubic large sieves. No deletion of arithmetic columns as a norm contraction is used here.

There are \(O(F)\) possible frozen \(f\). Apply Minkowski to this finite sum. Combining (4.2), (4.9), and the factor \(\sqrt{E'}\), its squared norm factor, before the ramified and reflected cube weights, is exactly

\[
\begin{aligned}
&\frac{F^2}{AFGZ^2}
\left(\frac G{Nd}\right)^{2\beta}
\left(\frac Z{Nj}\right)^{2\beta}
\frac E{NdNj}\\
&\qquad\asymp
G^{2\beta-2}Z^{2\beta-2}
(Nd)^{-2\beta-1}(Nj)^{-2\beta-1},
\end{aligned}
\tag{4.11}
\]

where \(EFG\asymp A\). The \(Z^{2\beta-2}\) factor is the second scalar saving; replacing the inverse cube coefficients by their absolute dyadic mass would lose it.

For \(U\ge1\), expansion of the bracket in (4.10), on the nonnegligible range (4.3), gives

\[
\frac{H+U}{U}[E'+U+(E'U)^{2/3}]
\ll HE+Y+(EY)^{2/3},
\tag{4.12}
\]

up to fixed bad-part constants. This uses \(H\gg1\), the nonempty lower bound \(E'\gg1\) up to a fixed support constant, and \(E'\ll E\). If the effective length in (4.3) is below one, all nonzero \(n_0\)-dyads are in the rapidly decreasing tail. Taking a sufficiently large fixed decay order gives the same bound. The source majorant also treats all \(U\) beyond the effective length.

On each reflected cube dyad \(Nb'\asymp C_1\), the sum of \(1/Nb'\) is \(O(1)\). This includes its unrestricted bad-prime powers. The factor \(3^{-m/3}\), \(m\ge-4\), is summable in the row norm; the effective length (4.3) gives additional decay in the long-column terms. Sum the finitely many \(n_S\)-patterns and fixed ray families. The remaining norm dyads cost only a subpower, with large dyads controlled by the same rapidly decreasing majorant. Every Mellin frequency cost in (4.9) and (4.10) is integrable against the smooth separation majorant.

Finally take Minkowski over the signed divisor labels \(d,j\). By (4.11), its norm cost is bounded by

\[
\sum_{d,j}(Nd)^{-\beta-1/2}(Nj)^{-\beta-1/2}<\infty.
\tag{4.13}
\]

The actual labels are squarefree and coprime, but dropping these restrictions in this nonnegative accounting sum is harmless. Both ideal sums converge because \(\beta>1/2\).

All shifted nonempty subunit scales are confined to fixed positive compact intervals by the original dyadic supports; counting covers them with the same powers up to constants. The original completion length \(B/(Nh)^3\) is bounded below by a fixed positive constant on the smooth \(h\)-cutoff. Allowing it in a fixed interval below one changes only support and derivative constants in the displayed kernel calculation. None of these cases inserts an additional power of an arithmetic scale. Equations (4.9)–(4.13) prove (4.1). \(\square\)

## 5. A bound for the entire literal balanced polynomial

### Theorem 5.1

For fixed polynomial scale ceilings, fixed smooth \(W_1,W_2\), and \(A,B,H\ge1\), the scalar hypothesis (2.1) implies

\[
\boxed{
\sum_{k\sim H}^*|P_{A,B}(k)|^2
\ll D^\epsilon
\left[
HA+H^2A\,B^{(2\beta-2)/3}
+H^{4/3}A^{4/3}B^{(2\beta-2)/3}
\right].
}
\tag{5.1}
\]

All inverse cube indices and all first-reflection cusp contributions have been summed. No completion remains on the left side.

**Proof.** Use the exact smooth decomposition in Sections 1 and 3 and apply Theorem 4.1. Because \(EFG\asymp A\), the three block terms are respectively

\[
\frac{HA}{F}G^{2\beta-3}Z^{2\beta-2},
\qquad
\frac{H^2A}{BF^2}G^{2\beta-1}Z^{2\beta+1},
\qquad
\left(\frac{H^2A^2}{B}\right)^{2/3}
F^{-2}G^{2\beta-2}Z^{2\beta}.
\tag{5.2}
\]

The first is \(O(HA)\), since \(F,G,Z\gg1\) and \(\beta\le1\). The joint support \(G^2Z^3\ll B\) gives

\[
G^{2\beta-1}Z^{2\beta+1}
\ll B^{(2\beta+1)/3}G^{(2\beta-5)/3}
\ll B^{(2\beta+1)/3},
\tag{5.3}
\]

and

\[
G^{2\beta-2}Z^{2\beta}
\ll B^{2\beta/3}G^{(2\beta-6)/3}
\ll B^{2\beta/3}.
\tag{5.4}
\]

Their exponents of \(G\) are negative on the stated interval for \(\beta\). Equations (5.2)–(5.4) give the three terms in (5.1). Only logarithmically many dyads in \(E,F,G,Z\) can meet the original supports and the exact inserted cutoffs. Their Minkowski sum, with the fixed ray and cusp families, costs \(D^\epsilon\) after redistributing the preliminary losses. \(\square\)

### Corollary 5.2. The balanced range reaches \(H=D^{19/36}\)

At \(A=B=D\),

\[
\boxed{
\sum_{k\sim H}^*|P_{D,D}(k)|^2
\ll D^\epsilon
\left[HD+H^2D^{(1+2\beta)/3}
+H^{4/3}D^{(2+2\beta)/3}\right].
}
\tag{5.5}
\]

The target \(D^{2+\epsilon}\) holds throughout

\[
\boxed{1\le H\le D^{(5-2\beta)/6}.}
\tag{5.6}
\]

For \(\beta=11/12\), this is the source-conditional estimate

\[
\boxed{
\sum_{k\sim H}^*|P_{D,D}(k)|^2
\ll D^\epsilon
\left[HD+H^2D^{17/18}+H^{4/3}D^{23/18}\right]
\ll D^{2+\epsilon},\qquad H\le D^{19/36}.
}
\tag{5.7}
\]

**Proof.** Substitute \(A=B=D\) into (5.1). The three exponent conditions for \(H=D^h\) are

\[
h\le1,\qquad h\le\frac{5-2\beta}{6},\qquad
h\le1-\frac\beta2.
\]

For \(1/2<\beta\le1\), the middle condition is the strongest. At \(\beta=11/12\), the last condition is \(h\le13/24\), while the middle one is \(h\le19/36\). At \(\beta=1\), both nontrivial conditions reduce to \(h\le1/2\). \(\square\)

## 6. The remaining boundary

The new transfer estimates the full literal squarefree two-factor polynomial \(P_{A,B}\). Its gain comes from two different inverse factors: the negative Ramanujan divisor \(g\) exposed by reflection and the genuine inverse cube divisor \(h\). Their coprimality is handled by an exact finite shared-divisor correction with convergent norm cost, and their two intersections with the positive squarefree index are handled by convergent divisor costs. No arbitrary arithmetic coefficient is admitted into a native scalar Möbius estimate.

The all-cusp completed mean square reaches a larger row range before cube inversion; that larger range does not persist under the present inverse. In (5.3)–(5.4), the worst block occurs at bounded \(G\), large inverse-cube scale \(Z\asymp B^{1/3}\), and bounded \(F\). The proved scalar savings reduce its cost but do not eliminate it. Thus (5.7) is a theorem about the literal polynomial at the stated range, rather than a transfer of the completed exponent \(19/24\).

The rows in this theorem remain squarefree primary outside \(S\). The original fourth-moment initialization requires a much larger dual range, of order \(D^{3-\vartheta}\) at balanced product length \(D^2\), and additional arbitrary-row and auxiliary control. Moreover, a positive norm for \(P_{A,B}\) does not by itself control the covariance obtained after subtracting the exact product-column diagonal. The full signed short-row fourth moment, all higher diagonal moments, and RH remain open under the present argument.

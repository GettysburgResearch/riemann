# Combining the oscillating-gcd tail with Hermitian conductor accounting

**Status:** independent audit of the pinned fourth-moment tail proof, followed by a proved combination of its stated classical-sieve consequence with the pinned conductor-sector and scale-averaged extraction theorems. The new result is a more restricted signed remainder whose dyadic-scale upper bound is sufficient. It does not prove that arithmetic bound, the full fourth moment, \(17/24\), or a new zero-free half-plane.

**Exact sources.**

- PR #917, commit 6b4723042b3d250024eef45cb1924f88f28e902c, [OSCILLATING_OVERLAPS.md](https://github.com/GettysburgResearch/riemann/blob/6b4723042b3d250024eef45cb1924f88f28e902c/standalone/2026-10-10-oscillating-overlaps-and-averaged-moments/OSCILLATING_OVERLAPS.md), Sections 2–5. SHA-256: 271f4f71bda533810ee49f6498f4ffbc42c3f0cb37c59151f9f703e715f58397.
- PR #914, commit 0cc0428fedbbfc340044c7451b3d392c1da9a103, [CONDUCTOR_SECTORS.md](https://github.com/GettysburgResearch/riemann/blob/0cc0428fedbbfc340044c7451b3d392c1da9a103/standalone/2026-10-10-sextic-moment-conductor-core/CONDUCTOR_SECTORS.md), Theorem 7.1, Corollary 7.2, Theorem 8.1 and Section 10. SHA-256: c160bbb1b1d7c6bcc5514d496ad41f15fd17ea3d36206b0d05cfa0d7d6503983.
- The norm-before-smoothing composition method is the one in [DOUBLE_RESIDUAL_REDUCTION.md](https://github.com/GettysburgResearch/riemann/blob/cfa102748b26f840ccc4b963a660711424db0ec3/standalone/2026-10-10-sextic-joint-core/DOUBLE_RESIDUAL_REDUCTION.md), at commit cfa102748b26f840ccc4b963a660711424db0ec3. This note supplies a different polynomial cutoff and its full proof.
- The averaged extraction is PR #917, at the same commit as above, [SCALE_AVERAGED_CRITERION.md](https://github.com/GettysburgResearch/riemann/blob/6b4723042b3d250024eef45cb1924f88f28e902c/standalone/2026-10-10-oscillating-overlaps-and-averaged-moments/SCALE_AVERAGED_CRITERION.md), Theorem 4.1. SHA-256: c6c543037312480fae6154f7a059248fe14658ecff6251aaecb80fe0fdbfd9c0. Its universal Mellin test comes from PR #912 at commit 6afd64e042ce7b59d550c3d76e9e2cca8b2c7379.

All published packets remain unchanged. The squarefree cubic large sieve is an explicit analytic input to the audit; it is not independently proved here. The fourth-moment reduction uses classical character estimates and elementary counting. The extraction additionally uses the universal Mellin test and the exact averaged mask-operator argument. Neither part uses the imported native Möbius second moment or an imported quasi-Riemann zero-free theorem.

## 1. Data and the audited tail estimate

Work over \(K=\mathbb Q(\sqrt{-3})\), with the fixed primary-generator convention, fixed bad-prime set \(S\), and the exact zero-extended sextic symbols from the sources. The set \(S\) contains the primes over 6 and the ramification of the fixed finite-order character \(\nu\). Fix \(W\in C_c^\infty((0,\infty))\), supported in \([\alpha,\beta]\), and set
\[
A_u(D)=\sum_{(n,S)=1}\mu_K(n)\nu(n)\chi_n(u)W(Nn/D),
\qquad D\ge2,\quad H\ge1.
\tag{1.1}
\]
All rows in a sharp norm are nonzero Eisenstein elements with \(Nu\le H\). Constants may depend on \(K,S,\nu,W\), and the positive loss.

Let \(T_{\ge C}(u)\) be the exact portion of \(A_u(D)^2\) whose ordered factor pair has \(N\gcd(n_1,n_2)\ge C\), for \(C\ge1\). The pinned PR #917 proves
\[
\boxed{\displaystyle
\|T_{\ge C}\|_{2,H}^{\,2}
\ll_\epsilon (DH)^\epsilon D^4
\left[HC^{-3}+H^{1/3}C^{-2}+H^{2/3}C^{-7/3}\right].
}
\tag{1.2}
\]
Here and below an empty polynomial portion is zero.

**Audit verdict: the fourth-moment argument in Sections 2–5 is a valid deduction from its stated squarefree cubic sieve.** The essential checks follow.

The all-row cubic estimate is obtained from the unique decomposition
\[
u=\varepsilon v^3ab^2,\qquad a,b\text{ squarefree},\quad(a,b)=1.
\]
The arbitrary ideal \(v\) may overlap either squarefree ideal. The character identity is
\[
\chi_n(u)^2
=\chi_n(\varepsilon)^2\mathbf1_{(n,v)=1}
\chi_n(a)^2\chi_n(b)^4.
\tag{1.3}
\]
The displayed mask is retained before applying any sieve. Freeze \(v\), the unit, the finite bad-prime parts, and the smaller squarefree component. On a norm block write
\[
P=V^3AB^2,\qquad F=VAB,\qquad M=\max(A,B).
\]
There are \(O(F/M)\) frozen choices. The varying squarefree component gives the bracket
\[
F+\frac{FL}{M}+\frac{FL^{2/3}}{M^{1/3}}.
\]
The exact inequalities
\[
F\le P,\qquad
\frac{(F/M)^3}{P}=\frac{A^2B}{M^3}\le1,\qquad
\frac{(F/M^{1/3})^3}{P^2}=\frac{A}{MV^3B}\le1
\]
therefore give, after the finite and logarithmic partitions,
\[
\sum_{0<Nu\le H}\left|\sum_cz_c\chi_c(u)^2\right|^2
\ll_\epsilon(HL)^\epsilon
\left[H+H^{1/3}L+(HL)^{2/3}\right]\sum_c|z_c|^2.
\tag{1.4}
\]
The coefficients \(z_c\) are arbitrary row-independent coefficients on good squarefree columns of norm at most \(L\). Thus fixed but moving coprimality masks do not enter the implied constant.

For the gcd tail write \(n_1=ca,\ n_2=cb\), with \(a,b,c\) squarefree and pairwise coprime. On \(L\le Nc<2L\), freeze \(a,b\). There are \(O_W(D^2/L^2)\) eligible frozen pairs. Their exact varying-\(c\) coefficient contains
\[
\mu_K(c)^2\nu(c)^2
W(Nc\,Na/D)W(Nc\,Nb/D)
\mathbf1_{(c,abS)=1},
\]
has squared mass \(O_W(L)\), and multiplies \(\chi_c(u)^2\). The residual character \(\chi_{ab}(u)\) is a contraction. Applying (1.4) before Minkowski over \(a,b\) gives
\[
\|T_L\|_{2,H}
\ll_\epsilon(DH)^\epsilon D^2
\left[
\sqrt H\,L^{-3/2}
+H^{1/6}L^{-1}
+H^{1/3}L^{-7/6}
\right].
\tag{1.5}
\]
Each power of \(L\) is negative. Summing over \(L=2^jC\) is geometric, and squaring proves (1.2). On a nonempty dyad, \(D/L\ge1/\beta\); the ideal count remains uniform at bounded scales below one. The support makes the tail empty when \(C>\beta D\). No residual Möbius cancellation was used.

## 2. Exact small-gcd polynomial and its signed remainder

Set
\[
R_{<C}(u)=
\sum_{\substack{n_1,n_2\\N\gcd(n_1,n_2)<C}}
a_{n_1}a_{n_2}\chi_{n_1n_2}(u),
\qquad
a_n=\mu_K(n)\nu(n)W(Nn/D).
\tag{2.1}
\]
The symbol on a nonsquarefree product denotes the multiplicative extension, with its original nonunit zeros. Thus
\[
A_u(D)^2=T_{\ge C}(u)+R_{<C}(u)
\tag{2.2}
\]
is an exact polynomial identity.

Fix a nonnegative radial \(\Phi\in C_c^\infty(\mathbb C)\) with \(\Phi(z)\ge1\) for \(|z|\le1\). For a Hermitian tuple \(\mathbf t=(n_1,n_2;m_1,m_2)\), let
\[
c(\mathbf t)=a_{n_1}a_{n_2}\overline{a_{m_1}a_{m_2}},
\]
\[
S_{\mathbf t}^{\Phi}(H)
=\sum_{u\in\mathcal O_K}\Phi(u/\sqrt H)
\chi_{n_1n_2}(u)\overline{\chi_{m_1m_2}(u)}.
\tag{2.3}
\]
Retain the row \(u=0\) in this complete smooth sum, with the same conventions as PR #914.

For each occurring prime \(p\), write \(r_p,s_p\) for its numbers of occurrences on the two sides. Let \(f\) be the product of the primes with \(r_p-s_p\not\equiv0\pmod6\), the primitive residual conductor. Let \(g_1\) be the product of primes occurring exactly once in the full four-tuple. Let \(g_2\) be the product of nonprincipal primes occurring exactly twice; these are the same-side double occurrences. Define
\[
\mathcal E(\mathbf t)=Ng_1\sqrt{Ng_2}.
\tag{2.4}
\]
The principal-mask primes are retained in \(S_{\mathbf t}^{\Phi}\).

Define the signed small-gcd remainder
\[
\boxed{\displaystyle
\mathcal U_C^\Phi(D,H)=
\sum_{\substack{
N\gcd(n_1,n_2)<C,\ N\gcd(m_1,m_2)<C\\
g_1\ne1,\ \mathcal E(\mathbf t)>H}}
c(\mathbf t)S_{\mathbf t}^{\Phi}(H).
}
\tag{2.5}
\]
The selection is invariant under exchanging the two sides, so this quantity is real. Every selected tuple is nonprincipal, because a singleton prime has residual exponent \(1\) or \(5\).

### Theorem 2.1. Quantified combination

For every \(C\ge1\) and every \(\epsilon>0\), there is a constant \(K_\epsilon\), independent of \(D,H,C\), such that
\[
\boxed{\begin{aligned}
\sum_{0<Nu\le H}|A_u(D)|^4
\le{}&
K_\epsilon(DH)^\epsilon
\left\{
HD^2+D^4\left[
HC^{-3}+H^{1/3}C^{-2}+H^{2/3}C^{-7/3}
\right]\right\}\\
&+2\mathcal U_C^\Phi(D,H).
\end{aligned}}
\tag{2.6}
\]
Moreover
\[
\mathcal U_C^\Phi(D,H)\ge
-K_\epsilon HD^{2+\epsilon}.
\tag{2.6a}
\]
Keeping the signed term in (2.6) is essential for the weaker averaged sufficient condition below.

**Proof.** Apply the pointwise norm inequality to (2.2), and only then sum over sharp rows:
\[
\sum_{0<Nu\le H}|A_u(D)|^4
\le2\|T_{\ge C}\|_{2,H}^2+2\|R_{<C}\|_{2,H}^2.
\tag{2.7}
\]
The first term is controlled by (1.2). The second is the norm of the entire residual polynomial, so positivity legitimately gives
\[
\|R_{<C}\|_{2,H}^2
\le\sum_{u\in\mathcal O_K}\Phi(u/\sqrt H)|R_{<C}(u)|^2.
\tag{2.8}
\]
Its expansion has both of the small-gcd restrictions in (2.5).

PR #914 Theorem 8.1 bounds the positive accounting sum of absolute contributions over all \(g_1=1\) tuples by \(O_\epsilon(HD^{2+\epsilon})\). Its Corollary 7.2 gives the same bound over nonprincipal tuples with \(\mathcal E\le H\). These are positive accounting bounds, so imposing both small-gcd restrictions preserves them. Their union includes every principal tuple, since a principal tuple has no singleton prime. Count the union once. The exact remaining expansion is therefore
\[
\sum_u\Phi(u/\sqrt H)|R_{<C}(u)|^2
=\mathcal U_C^\Phi(D,H)+O_\epsilon(HD^{2+\epsilon}).
\tag{2.9}
\]
The left side of (2.9) is nonnegative, proving (2.6a). Substitute (2.9) and (1.2) into (2.7) and enlarge the fixed controlled constant. This proves the signed inequality (2.6). \(\square\)

This proof neither smooths a signed sharp-row sector using positivity nor bounds arbitrary cross-terms involving the large-gcd polynomial in absolute value. Those cross-terms are handled by (2.7), before smoothing. The Möbius signs, character phases, and principal masks in the remaining signed sum are unchanged.

## 3. The stronger fourth-moment target

Comparison of the three tail terms with \(HD^2\) gives the sufficient cutoff
\[
C\ge C_*(D,H):=
\max\left\{1,D^{2/3},DH^{-1/3},(D^6/H)^{1/7}\right\}.
\tag{3.1}
\]
At \(H=D^h,\ 1<h\le11/10\), this reduces to
\[
C_*=D^{(6-h)/7}.
\tag{3.2}
\]
Indeed the last exponent exceeds \(2/3\) when \(h\le4/3\), and exceeds \(1-h/3\) when \(h\ge3/4\).

Consequently, with \(C=C_*\), a stronger pointwise sufficient condition would be that, for every \(\epsilon>0\), there is a constant \(B_{\epsilon,h}\) such that
\[
\boxed{\displaystyle
\mathcal U_{D^{(6-h)/7}}^\Phi(D,D^h)
\le B_{\epsilon,h}D^{2+h+\epsilon}.}
\tag{3.3}
\]
This is still unproved, and Section 4 requires only its dyadic integral. Every tuple in this sufficient target simultaneously has
\[
N\gcd(n_1,n_2),\ N\gcd(m_1,m_2)<D^{(6-h)/7},
\qquad
g_1\ne1,\qquad Ng_1\sqrt{Ng_2}>D^h.
\tag{3.4}
\]
Thus the combination reduces the polynomial on each side before applying the two-sided conductor conditions.

The older classical gcd cutoff from PR #913 was \(D^{(4-h)/4}\). The decrease in its exponent is
\[
\frac{4-h}{4}-\frac{6-h}{7}=\frac{4-3h}{28}>0
\quad(1<h\le11/10).
\tag{3.5}
\]
The new cutoff and its gain are inherited from PR #917. The new contribution here is the valid simultaneous restriction of its complementary signed conductor remainder.

The conductor block bound also survives the two gcd restrictions unchanged. For dyadic \(L,G\ge1\),
\[
\sum_{\substack{
N\gcd(n_1,n_2),\,N\gcd(m_1,m_2)<C\\
L\le Ng_1<2L,\ G\le Ng_2<2G,\ f\ne1}}
|c(\mathbf t)S_{\mathbf t}^{\Phi}(H)|
\ll_\epsilon D^{2+\epsilon}\min\{H\sqrt L,L\sqrt G\}.
\tag{3.6}
\]
This follows by restricting the positive accounting quantity of PR #914 Theorem 7.1. No smaller right-hand side is deduced solely from the gcd constraints.

## 4. Only a signed dyadic-scale upper bound is needed

For this section take the fixed universal test \(W_*\) from the pinned averaged extraction theorem: it is nonnegative, belongs to \(C_c^\infty((1,2))\), and has nonvanishing Mellin transform throughout \(\Re s>0\). Fix \(1<h\le11/10\), put
\[
C(D)=D^{(6-h)/7},\qquad
\mathcal S_h(D)=\mathcal U_{C(D)}^\Phi(D,D^h).
\]
For every \(\epsilon>0\), (2.6) and (2.6a), with losses reassigned, give
\[
\boxed{\displaystyle
M_4(D,D^h)\le K_{\epsilon,h}D^{h+2+\epsilon}
+2\mathcal S_h(D),\qquad
\mathcal S_h(D)\ge-K_{\epsilon,h}D^{h+2+\epsilon}.
}
\tag{4.1}
\]
Here \(M_4\) is the full sharp-row fourth moment. Both statements retain the literal signed remainder.

### Corollary 4.1. Restricted averaged sufficient criterion

Let \(e\ge0\). Suppose that for every \(\epsilon>0\) there is a constant \(B_{\epsilon,h,\nu,S}\), independent of \(X\), such that for every \(X\ge2\),
\[
\boxed{\displaystyle
\int_X^{2X}\mathcal S_h(D)\frac{dD}{D}
\le B_{\epsilon,h,\nu,S}X^{h+2+e+\epsilon}.
}
\tag{4.2}
\]
Then every primitive Hecke \(L\)-function induced by
\(n\mapsto\nu(n)\chi_n(r)\), for each fixed nonzero element \(r\), is zero-free in
\[
\boxed{\displaystyle
\Re s>\frac12+\frac{5h}{24}+\frac e4.
}
\tag{4.3}
\]

**Proof.** Integrate the signed inequality (4.1), without taking an absolute value of \(\mathcal S_h\). Its controlled term integrates to \(O_{\epsilon,h}(X^{h+2+\epsilon})\). Since \(e\ge0\), (4.2) therefore gives
\[
\int_X^{2X}M_4(D,D^h)\frac{dD}{D}
\ll_{\epsilon,h}X^{h+2+e+\epsilon}.
\tag{4.4}
\]
This is exactly PR #917's Theorem 4.1 with \(k=2\) and \(e_k=e\). Its zero-free exponent is \(1/2+5h/(12k)+e_k/(2k)\), giving (4.3).

For clarity about the extraction's scope, its sixth-power copies \(rv^6\) supply \(D^{h/6}\) rows up to a fixed-\(r\) factor. The invertible moving average over the exact Euler-mask operators converts (4.4) into a finite weighted \(L^4(dD/D)\) norm for the fixed-row polynomial at every weight exponent
\(\sigma>(2+5h/6+e)/4\). Its Mellin transform is the nonvanishing universal test times a reciprocal \(L\)-function and finitely many nonvanishing Euler corrections. Holomorphy then excludes zeros to the right of that \(\sigma\). These are the explicit premises and argument of the pinned extraction theorem; no pointwise moment estimate is inferred. \(\square\)

Thus (4.2) asks for an upper bound on a signed integral. It requires neither \(\int_X^{2X}|\mathcal S_h(D)|\,dD/D\) nor a pointwise upper bound for \(\mathcal S_h(D)\). Its already-proved lower bound in (4.1) is compatible with the nonnegative full residual norm and rules out any hidden requirement to control a large negative part separately.

If (4.2) holds with \(e=0\) along fixed exponents \(h\downarrow1\), (4.3) reaches the strict half-plane \(\Re s>17/24\). A single fixed \(h=1+\theta\) gives \(17/24+5\theta/24+e/4\). These are conditional consequences only. For fixed \(\nu\), the conclusion concerns the displayed row-twist family; a statement for every fixed \(\nu\) needs the hypothesis for every such \(\nu\). No uniform conductor bound is needed in the forward extraction for each fixed row.

## 5. A strict domain reduction, not a full moment estimate

The new restriction removes incidence patterns that neither the earlier gcd cutoff nor the two conductor conditions remove. To see the scale comparison, choose
\[
\frac{6-h}{7}<\gamma<\frac{4-h}{4}
\]
and consider the mutually coprime squarefree factors in the two ordered pairs
\[
(ca,cb),\qquad(c'a',c'b'),
\]
with \(Nc,Nc'\asymp D^\gamma\) and each of \(Na,Nb,Na',Nb'\asymp D^{1-\gamma}\). These are feasible support-scale patterns; fixed support constants may be absorbed in the norm comparisons.

Both one-sided gcds lie between the new and old cutoffs. In the full tuple,
\[
Ng_1\asymp D^{4(1-\gamma)},\qquad
Ng_2\asymp D^{2\gamma},\qquad
\mathcal E\asymp D^{4-3\gamma}>D^h.
\]
The last inequality follows from \(\gamma<(4-h)/4<(4-h)/3\). These patterns are retained by the old small-gcd conductor remainder and excluded by (3.4). For the fourth-moment version of the earlier one-sided singleton selector, \(Q\asymp D^{1-\gamma}\) on both sides, so they also lie outside every chosen subpower periphery.

This witnesses a strict reduction of the remaining tuple domain. It does not assert that any selected individual contribution is large, or that removing a subset from a signed sum necessarily decreases its absolute value. The proved norm split is what makes the reduced target sufficient.

The small-gcd all-unit core and its genuine singleton correlations remain. The displayed classical bounds prove neither the pointwise target (3.3) nor the weaker signed averaged target (4.2). The result is the exact sufficient reduction, including its conditional extraction exponent; no new arithmetic moment bound or zero-free half-plane is claimed.

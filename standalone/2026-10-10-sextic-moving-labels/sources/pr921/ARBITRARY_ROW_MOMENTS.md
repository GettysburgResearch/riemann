# Quantitative coupled and cube-free bounds for arbitrary rows

**Status:** source-qualified analytic adapter. The row-power decomposition below extends the coupled and cube-free estimates to every nonzero Eisenstein row, including all units and bad-prime valuations. An exact three-way Ramanujan reindexing gives auxiliary costs \(1,Q,Q^{2/3}\) in the three energy terms. The same bounds hold in sharp row balls and with fixed Schwartz row weights. The stronger scalar exponent remains conditional on the expressly named imported canonical/angular input. The full fourth moment, generalized moment hierarchy, and centered signed covariance remain unproved.

**Exact inputs:** OpenAI math pin adc7f1241b42e322a6451854ab7e4b4c146bf78a, October 5 paper2.tex, especially the full scalar following eq:dual-cusp-mellin-series, eq:ray-local-transform, eq:theta-row-twist, and eq:cube-inverse; PR #915 pin 9959364671f89b86f3992ec5ed5e19f804eb607b; centered_a2_attack.md, SHA-256 bbc139f956731482fcf9e33645bfe2832b7b7471594d9cbc1f21cd08eaf2ac5a; all_cusp_gauss_factorization.md, SHA-256 b596f3f7c43bb84c699201f3b14c81eae18ae89d3b45e2357bcdccfb9eb3ea1c; cube_inverse_attack.md, SHA-256 a865338882111bf3bc96ffc539dd93f3b2ee59390499caaf14852ed8cde77804; and ARBITRARY_ROW_SUPPORT.md, SHA-256 f859936fb555de1afd0215fa74e89ce10b8afa1b9a193e4d355be3da3f542dd5. Their stated analytic premises are retained. This note proves the additional scalar factorization, row-sector bookkeeping, and convergent row-power summation.

## 1. Objects, scalar premise, and row decomposition

Keep the fixed bad set \(S\), the primary-generator convention, and the fixed finite ray character \(\xi\). All original arithmetic column indices are primary and outside \(S\). Put

\[
a_\xi(a)=\alpha(a)^{-1}\gamma_2(a)\xi(a).
\]

For arbitrary nonzero \(k\in\mathcal O\), define

\[
\begin{aligned}
\mathcal C_{A,B}(k)
&=\frac1{\sqrt A}\sum_a^*a_\xi(a)\chi_a(k)
W_1(Na/A)T(B;k,a),\\
P_{A,B}(k)
&=\frac1{\sqrt{AB}}\sum_{\substack{a,n\ {\rm squarefree}\\(a,n)=1}}
a_\xi(an)\chi_{an}(k)W_1(Na/A)W_2(Nn/B).
\end{aligned}                                                    \tag{1.1}
\]

The original completed \(T\), its cube weights, and all nonunit zeros are unchanged. The fixed smooth tests have compact support in \((0,\infty)\). Assume \(1\le A,B,H\le D^{C_0}\), \(D\ge2\), with fixed \(C_0\). All estimates below are uniform in these scales, with a fixed finite number of smooth seminorms.

Fix \(1/2<\beta\le1\). The scalar premise is the companion bound

\[
\sum_{(g,CS)=1}\mu(g)\eta(g)\alpha(g)^{-3}
\chi_s(g)^3 V(Ng/L)
\ll D^\epsilon L^\beta\|V\|_{C^J(I)},                         \tag{1.2}
\]

for every squarefree primary \(s\) outside \(S\), every polynomially bounded moving exclusion \(C\), and the fixed finite family of \(\eta\) and compact smooth tests. Nonempty shifted lengths in a fixed interval below one are covered by counting. The premise holds with \(\beta=1\) by elementary ideal counting; the companion angular argument supplies \(\beta=11/12\) under its named canonical inputs.

Choose generators at the finitely many bad primes once. Every row has a unique decomposition

\[
k=u\,k_S\,\tau\,k_0,                                      \tag{1.3}
\]

where \(u\) is a unit, \(k_S\) is supported on \(S\), and \(k_0,\tau\) are primary and outside \(S\). The ideal \(k_0\) contains exactly the good row primes of valuation one. Every good prime in \(\tau\) has valuation at least two, and \((k_0,\tau)=1\). Write

\[
T=N(k_S\tau),\quad H_0=H/T,\quad
R=N(\operatorname{rad}\tau),\quad
\tau_{\rm odd}=\prod_{\substack{p\mid\tau\\v_p(\tau)\ {\rm odd}}}p,
\]

\[
\Lambda(\tau)^2=\prod_{\substack{p\mid\tau\\v_p(\tau)\equiv4\ (6)}}Np,
\qquad
b(\tau)=4^{\#\{p\mid\tau:v_p(\tau)\equiv0\ (6)\}}.           \tag{1.4}
\]

The products in (1.4) involve good primes only. Fix \(u,k_S,\tau\), and average over squarefree primary \(k_0\), \((k_0,\tau)=1\), with \(H_0\le Nk_0<2H_0\). A nonempty row sector has \(T<2H\), hence \(H_0>1/2\). For \(H_0<1\), replacing it by one in a sieve bound changes powers by a fixed constant; the possible unit row \(k_0=1\) is retained.

The exact support note proves that units, bad-prime powers, and good-prime reciprocity signs enter a fixed finite initial ray family. Thus the constants and the \(S\)-supported data \(c_0,\psi\) are uniform in (1.3).

## 2. Exact mixed scalar cancellation for every local row exponent

Let \(C_\iota(k,a)\) denote a first-reflection scalar in a fixed source branch. The outer factor \(\chi_a(k)\) is zero when \((a,k)>1\), so throughout the following computation \((a,k)=1\).

At every prime of \(a\), the local exponent is four. At a good row prime \(p\), it is \(j_p\equiv v_p(k)\pmod6\), with \(0\le j_p\le5\). A positive valuation with \(j_p=0\) still represents the mask \(\chi_p^0=\mathbf1_{p\nmid\cdot}\). Only such primes may be inactive.

Let \(r\) be the full active good row radical in the branch. Then \(r=k_0r_\tau\), where \(r_\tau\mid\operatorname{rad}\tau\), and the first denominator is \(c=c_0ra\), with any allowed unit normalization included in the fixed finite \(c_0\)-family.

The source scalar uses

\[
\sigma_p=\lambda^2c/p,\qquad
\epsilon_p=-\lambda^{-5}(c/p)^{-2},
\]

and its local factor is \(\chi_p(\sigma_p)^{-2}\omega_{p,j}\). Direct substitution into the displayed source formulas gives

\[
\boxed{
\chi_p(\sigma_p)^{-2}\omega_{p,j}
=\Omega_{p,j}\chi_p(c/p)^{\,2j+2},
}                                                         \tag{2.1}
\]

where

\[
\Omega_{p,j}=
\begin{cases}
\gamma_j(p)\gamma_{j+2}(p)\chi_p(\lambda)^{5j},
   &j\ne0,4,\\
\gamma_4(p)\chi_p(\lambda)^2,&j=4,\\
-\gamma_2(p),&j=0\ {\rm active}.
\end{cases}                                               \tag{2.2}
\]

Every \(\Omega_{p,j}\) has modulus one. For \(j\ne0,4\), the signs cancel because \(\chi_p(-1)^{-2}=1\), and the remaining exponent of \(c/p\) is \(-2+2(j+2)=2j+2\). At \(j=4\), the source special case gives exponent \(-2\equiv4\equiv2j+2\pmod6\). The active \(j=0\) case gives exponent two. An inactive prime contributes only \(1-(Np)^{-1}\).

Aggregate the factors at primes of \(a\). Their internal cross-symbols are exactly those of normalized Gauss CRT, giving

\[
\gamma_4(a)\chi_a(\lambda)^2\chi_a(c_0)^4\chi_a(r)^4.        \tag{2.3}
\]

The remaining row-prime factors contribute

\[
\prod_{p\mid r}\chi_p(a)^{2j_p+2}
\]

times a bounded scalar independent of \(a\), after the fixed ray choices. Sextic reciprocity to the even exponent four identifies \(\chi_a(p)^4=\chi_p(a)^4\). Thus (2.3) and the row cross-symbols together give exponent \(2j_p+6\equiv2j_p\) in \(a\) at each active row prime.

Now multiply by the original \(\chi_a(k)\). The row exponent contributes another \(j_p\); its reciprocity signs, bad-prime powers, and unit factors belong to the source's fixed finite ray family. The resulting exponent is \(3j_p\). It is quadratic for odd \(j_p\) and trivial on units for even \(j_p\). The original \((a,k)=1\) mask remains in force.

Finally,

\[
\gamma_2(a)\gamma_4(a)=\chi_a(-1)^2=1,
\]

and the angular factor \(\alpha(c)^{-2}\) combines with the outer \(\alpha(a)^{-1}\) to give \(\alpha(a)^{-3}\). Consequently, after a fixed finite ray decomposition, each coupled branch is a finite sum whose outer scalar has the form

\[
\boxed{
a_\xi(a)\chi_a(k)C_\iota(k,a)
=R_\iota(k_0,\tau,u,k_S)\,
\eta_\iota(a)\alpha(a)^{-3}
\chi_{\,k_0\tau_{\rm odd}}(a)^3
\quad ((a,k)=1),
}                                                         \tag{2.4}
\]

with \(R_\iota\) uniformly bounded and \(\eta_\iota\) in a fixed finite family.

The equality is understood after splitting the relevant fixed ray classes and expanding their indicators into finitely many characters. Source cusp data and \(\psi,c_0\) are fixed on each such class. No varying conductor is hidden in \(\eta_\iota\). All dependence on the row's odd good prime radical is displayed explicitly. Outside \((a,k)=1\), the original contribution is zero; even-prime and inactive-prime masks cannot be dropped when using (2.4).

The number of active/inactive choices is at most \(2^{\omega_0(\tau)}\), where \(\omega_0\) counts the primes in (1.4). All primes of \(a\) and \(k_0\) are forced active. The remaining Fourier index at the fixed bad modulus and all fixed ray splits have bounded cardinality. Minkowski over the variable branches therefore costs at most a fixed constant times \(b(\tau)\) in the squared norm.

## 3. The residual row factors separate with an explicit amplitude

Reunite the outer-divisor Ramanujan factors, insert the exact cutoff of ARBITRARY_ROW_SUPPORT.md, and only then split the positive allocations as in the all-cusp note:

\[
a=efg,\qquad n=e n_S n_0,\qquad b=f b'.
\]

The factors \(e,f,g\) are squarefree and pairwise coprime. The original mask \((a,k)=1\) makes each of them coprime to \(\tau\). The theta unit, ramified valuation \(m\), finite squarefree bad-prime part \(n_S\), and the complete cube index \(b'\) are fixed before applying a sieve. Every bad-prime power in \(b'\) is retained.

The variable frequency is

\[
x=\lambda^4\ell
=u_\theta\lambda^{m+4}e n_S n_0(fb')^3.                  \tag{3.1}
\]

For an active row prime \(p\mid\tau\) with \(j_p\ne4\), the factor \(B_{p,j_p}(x)\) is a character of \(x\), times \((Np)^{-1/2}\) when \(j_p=0\). Its dependence separates into a bounded coefficient of \(e\), a bounded coefficient of \(n_0\), and a frozen factor. Its literal zero is preserved when \(p\mid n_0b'\).

For a row prime with \(j_p=4\), since \(p\nmid e f u_\theta\lambda n_S\),

\[
B_{p,4}(x)
=(Np)^{-1/2}
[-1+Np\,\mathbf1_{p\mid n_0b'}].                        \tag{3.2}
\]

After \(b'\) is frozen, this is a coefficient of \(n_0\) alone, of modulus at most \(\sqrt{Np}\). It is not expanded into outer-divisor allocation labels. Products of (3.2) are bounded by \(\Lambda(\tau)\).

The other row factors in (2.4), involving \(e,f\), become separate bounded column coefficients or frozen scalars. The factor involving the negative divisor is exactly

\[
\mu(g)\eta(g)\alpha(g)^{-3}\chi_s(g)^3,\qquad
s=k_0\tau_{\rm odd},                                    \tag{3.3}
\]

with the full \(\operatorname{rad}\tau\) in its moving exclusion, in addition to the previously retained \(e,f\) masks. Because \((k_0,\tau)=1\), the index \(s\) is squarefree primary outside \(S\), and \(Ns\ll H\). Thus (1.2) applies directly. Even row primes and inactive exponent-zero primes are retained through that exclusion.

The \(k_0\)-part is still the exact quadratic row character and the mask \((k_0,e)=1\) of the quadratic–cubic composition. After division by \(\Lambda(\tau)\), its \(e,n_0\) vectors are bounded by one. They may depend on the fixed \(\tau,b',m,n_S,f\); the large sieves permit such arbitrary bounded separate vectors. Their dependence on \(k_0\) has been removed by the fixed ray splitting, apart from the stated row character and masks.

## 4. Completed mean square in a fixed row sector

Let

\[
M_{A,B}=\min(A,\sqrt B).
\]

For fixed \(u,k_S,\tau\), the complete first-reflection estimate is

\[
\boxed{
\begin{aligned}
\sum_{\substack{k_0\sim H_0\\(k_0,\tau)=1}}^*
|\mathcal C_{A,B}(u k_S\tau k_0)|^2
\ll D^\epsilon b(\tau)\Lambda(\tau)^2
\Bigg[
&H_0A+\frac{H_0^2R^2A}{B}M_{A,B}^{2\beta-1}\\
&+\left(\frac{H_0^2R^2A^2}{B}\right)^{2/3}
\Bigg].
\end{aligned}
}                                                         \tag{4.1}
\]

**Proof.** In a fixed branch, write \(R_\iota=N(r_\tau)\le R\). The source denominator \(c=c_0k_0r_\tau a\) makes the effective squarefree scale on an allocation block

\[
Y_\iota=\frac{H_0^2R_\iota^2EG^2}{BF},
\qquad EFG\asymp A.                                     \tag{4.2}
\]

The all-cusp coefficient factorization remains exact after the separated row multipliers of Section 3 are inserted. Apply the moving \(g/e\) mask expansion from that proof, keeping \(\operatorname{rad}\tau\) in the scalar exclusion. The scalar index is \(s\) in (3.3), not merely \(k_0\). Its bound is pointwise on the actual rows \((k_0,\tau)=1\). Only afterwards may the residual positive row norm be enlarged by dropping that fixed row restriction.

The divisor substitution \(g=dg'\), \(e=de'\) has the same squared factor \((Nd)^{-2\beta-1}\). The remaining row mask \((k_0,e')=1\) is the one already treated in the quadratic–cubic lemma. Thus the fixed-branch block estimate is

\[
D^\epsilon\Lambda(\tau)^2G^{2\beta-2}
[H_0E+Y_\iota+(EY_\iota)^{2/3}].                         \tag{4.3}
\]

No mean-square theorem with row parameter \(s\) is used here: the quadratic sieve averages in \(k_0\), while the scalar bound is uniform in \(s\).

The arbitrary-row support theorem permits the exact smooth restriction \(G\ll\sqrt B\) before the \(e/f\) split. Also \(G\ll A\). Optimizing (4.3) over \(E,F,G\), exactly as in the all-cusp note, gives the bracket in (4.1) with \(R_\iota\). Replace it by \(R\) in this nonnegative bound and sum the active branches by Minkowski, costing \(b(\tau)\).

The full cube and ramified tails are the same as in the all-cusp proof: the amplitude \(3^{-m/3}/Nb'\), the bound on reciprocal-norm mass per cube dyad, and the transformed smooth majorant are unchanged. The new factor \(R_\iota^2\) changes the effective length, not its uniform Mellin estimates. Its norm is polynomially bounded. This proves (4.1). \(\square\)

## 5. Cube-free mean square in the same row sector

Put \(\delta=(2\beta-2)/3\). The corresponding bound for the literal polynomial is

\[
\boxed{
\begin{aligned}
\sum_{\substack{k_0\sim H_0\\(k_0,\tau)=1}}^*
|P_{A,B}(u k_S\tau k_0)|^2
\ll D^\epsilon b(\tau)\Lambda(\tau)^2
\big[
&H_0A+H_0^2R^2 A B^\delta\\
&+H_0^{4/3}R^{4/3}A^{4/3}B^\delta
\big].
\end{aligned}
}                                                         \tag{5.1}
\]

**Proof.** Use the exact cube inverse, with inverse index \(h\). Its coefficient is

\[
\frac{\mu(h)\alpha(h)^{-3}\xi(h)^3\chi_h(k)^3}{Nh},
\]

and it introduces \((h,a)=1\), with no condition on the dual theta indices. The factor \(\chi_h(k)^3\) also preserves \((h,\tau)=1\), including the primes of even row valuation. After reciprocity and fixed ray splitting, its scalar character is again \(\chi_s(h)^3\), with the full \(\operatorname{rad}\tau\) in the exclusion. This is another application of (1.2), not a new scalar theorem for a general character of growing conductor.

The exact smooth support insertion gives

\[
G^2Z^3\ll B,\qquad Z\asymp Nh,
\]

before any positive-allocation splitting. In a fixed branch the component energy is

\[
D^\epsilon\Lambda(\tau)^2
G^{2\beta-2}Z^{2\beta-2}
[H_0E+Y_\iota+(EY_\iota)^{2/3}],
\qquad
Y_\iota=\frac{H_0^2R_\iota^2EG^2Z^3}{BF}.                \tag{5.2}
\]

To justify this adapter, repeat the exact two common-divisor extractions of the cube-inverse note while retaining the fixed \(\tau\)-exclusions. The two scalar variables have index \(s=k_0\tau_{\rm odd}\). Their mutual shared divisor \(\ell\) is handled by the finite identity there, with scalar exclusion enlarged by \(\operatorname{rad}\tau\). The three norm costs remain

\[
(Nd)^{-\beta-1/2},\qquad (Nj)^{-\beta-1/2},\qquad
(N\ell)^{-2\beta}.
\]

All converge. The remaining positive variable \(e'\) may share primes with \(\ell\); no extra mask is inserted. The fixed row factors from \(\tau\) remain separate column coefficients of amplitude at most \(\Lambda(\tau)\).

Every scalar parameter is polynomially bounded: \(Ns\ll H\), all original inverse labels satisfy \(Nh\ll B^{1/3}\), and all divisor labels divide products of the original bounded allocation variables. The scalar estimates are applied on the true \((k_0,\tau)=1\) rows before using the positive row norm. The finite ray family and all smooth Mellin majorants remain uniform after these shifts. In particular the normalized ratios in both exact cutoffs are unchanged by the divisor substitutions.

Optimizing (5.2) using \(EFG\asymp A\), \(G^2Z^3\ll B\), and \(1/2<\beta\le1\) gives the bracket in (5.1). Replace \(R_\iota\) by \(R\), retain the full source tails as in Section 4, and sum the branches by Minkowski. This proves (5.1). \(\square\)

## 6. Summing the powerful row factors

The row sectors (1.3) are disjoint. Therefore their energies are added directly; no Minkowski inequality is used over \(\tau\) or \(k_S\). The three required weights are

\[
\sum_{k_S,\tau}\frac{b(\tau)\Lambda(\tau)^2}{T},\qquad
\sum_{k_S,\tau}\frac{b(\tau)\Lambda(\tau)^2R^2}{T^2},\qquad
\sum_{k_S,\tau}\frac{b(\tau)\Lambda(\tau)^2R^{4/3}}{T^{4/3}}.
                                                               \tag{6.1}
\]

All three sums converge absolutely.

Indeed, at a good prime of norm \(q\), a nonzero valuation in \(\tau\) has \(v\ge2\). Its branch weight is \(4^{\mathbf1_{v\equiv0\ (6)}}\), and its squared amplitude is \(q^{\mathbf1_{v\equiv4\ (6)}}\). The local factors in (6.1) are respectively

\[
\begin{aligned}
1+\sum_{v\ge2}4^{\mathbf1_{6\mid v}}
q^{\mathbf1_{v\equiv4\ (6)}-v}&=1+O(q^{-2}),\\
1+\sum_{v\ge2}4^{\mathbf1_{6\mid v}}
q^{\mathbf1_{v\equiv4\ (6)}+2-2v}&=1+O(q^{-2}),\\
1+\sum_{v\ge2}4^{\mathbf1_{6\mid v}}
q^{\mathbf1_{v\equiv4\ (6)}+4/3-4v/3}&=1+O(q^{-4/3}).
\end{aligned}                                                   \tag{6.2}
\]

The six valuation progressions are geometric. The worst contribution in each line is already at \(v=2\); the \(v\equiv4\) amplitude and \(v\equiv0\) branch factors do not worsen those powers. Products over prime ideals converge because each displayed exponent exceeds one.

At each fixed bad prime, arbitrary valuations contribute geometric series with exponents \(1,2,4/3\), respectively. There are finitely many such primes. The six possible row units add a fixed factor. This proves (6.1). Truncating to \(T<2H\) only decreases these nonnegative sums.

### Theorem 6.1. All nonzero rows

Under (1.2), the estimates

\[
\boxed{
\sum_{\substack{k\in\mathcal O\\H\le Nk<2H}}
|\mathcal C_{A,B}(k)|^2
\ll D^\epsilon
\left[
HA+\frac{H^2A}{B}M_{A,B}^{2\beta-1}
+\left(\frac{H^2A^2}{B}\right)^{2/3}
\right]
}                                                         \tag{6.3}
\]

and

\[
\boxed{
\sum_{\substack{k\in\mathcal O\\H\le Nk<2H}}
|P_{A,B}(k)|^2
\ll D^\epsilon
\left[
HA+H^2A B^{(2\beta-2)/3}
+H^{4/3}A^{4/3}B^{(2\beta-2)/3}
\right]
}                                                         \tag{6.4}
\]

hold for arbitrary nonzero element rows.

**Proof.** Substitute \(H_0=H/T\) into (4.1) and (5.1), and use the three convergent sums (6.1). All source losses are uniform in the polynomially bounded row sectors. The nonempty \(H_0\in(1/2,1)\) sectors and \(k_0=1\) were included in Section 1. \(\square\)

At \(A=B=D\), (6.3) reaches \(D^{2+\epsilon}\) for \(H\le D^{(5-2\beta)/4}\), while (6.4) reaches it for \(H\le D^{(5-2\beta)/6}\). Thus:

| Scalar input | Completed all-row range | Literal cube-free all-row range |
|---|---:|---:|
| Counting, \(\beta=1\) | \(H\le D^{3/4}\) | \(H\le D^{1/2}\) |
| Source-conditional angular input, \(\beta=11/12\) | \(H\le D^{19/24}\) | \(H\le D^{19/36}\) |

These are dual row-norm ranges. They are not zero-free boundaries.

## 7. A moving squarefree auxiliary ideal

Let \(\mathfrak q\) be squarefree primary outside \(S\), with \(Q=N\mathfrak q\) polynomially bounded in \(D\). Insert the auxiliary factor \(\chi_{an}(\mathfrak q)^4\) in the literal polynomial and its corresponding factors in both axes of the completion. Complete multiplicativity, including zeros, gives exactly

\[
P_{A,B}(k;\mathfrak q)=P_{A,B}(k\mathfrak q^4),\qquad
\mathcal C_{A,B}(k;\mathfrak q)=\mathcal C_{A,B}(k\mathfrak q^4).
                                                               \tag{7.1}
\]

No assumption \((k,\mathfrak q)=1\) is made.

A direct use of (6.3) at row size \(HQ^4\) would discard useful information. Instead decompose the original row \(k\) as in (1.3) outside \(S\mathfrak q\), and retain the valuations \(\nu_p=v_p(k)\ge0\) separately for every \(p\mid\mathfrak q\). The first local row exponent is now

\[
j_p\equiv\nu_p+4\pmod6.                                  \tag{7.2}
\]

Its contribution to the squared amplitude is \(Np\) exactly when \(\nu_p\equiv0\pmod6\). The first active radical is bounded by \(\mathfrak q\operatorname{rad}\tau\), independently of the actual \(\nu_p\). The physical row norm denominator in \(H_0\) contains \((Np)^{\nu_p}\), not \((Np)^{\nu_p+4}\).

The mixed scalar remains (2.4), with the odd effective row radical. At \(p\mid\mathfrak q\), oddness of \(\nu_p+4\) is oddness of \(\nu_p\). The scalar index is therefore squarefree, and its norm is bounded by a fixed multiple of \(H\). The full \(\mathfrak q\operatorname{rad}\tau\) stays in the moving scalar exclusion, including the \(j_p=0\) case \(\nu_p\equiv2\pmod6\). The inverse cube factor also imposes \((h,\mathfrak q)=1\). All these parameters remain polynomially bounded, so (1.2) applies without a new premise.

The row \(j_p=4\) factor still has the exact separation (3.2), because the original outer coefficient enforces \((a,k\mathfrak q)=1\). The arbitrary-row support theorem is unchanged by this row replacement.

For completeness include the squared branch factor \(4^{\mathbf1_{\nu\equiv2\ (6)}}\). At a prime of norm \(q\) dividing \(\mathfrak q\), the three local energy sums are

\[
\begin{aligned}
\sum_{\nu\ge0}4^{\mathbf1_{\nu\equiv2\ (6)}}
q^{\mathbf1_{\nu\equiv0\ (6)}-\nu}
&=q\,[1+O(q^{-2})],\\
\sum_{\nu\ge0}4^{\mathbf1_{\nu\equiv2\ (6)}}
q^{\mathbf1_{\nu\equiv0\ (6)}+2-2\nu}
&=q^3[1+O(q^{-3})],\\
\sum_{\nu\ge0}4^{\mathbf1_{\nu\equiv2\ (6)}}
q^{\mathbf1_{\nu\equiv0\ (6)}+4/3-4\nu/3}
&=q^{7/3}[1+O(q^{-7/3})].
\end{aligned}                                                   \tag{7.3}
\]

These are geometric series in the six residue classes. Their leading terms occur at \(\nu=0\). The products of the bracketed factors are bounded uniformly over squarefree \(\mathfrak q\). The row factors outside \(S\mathfrak q\) have the convergent products (6.2), and the fixed bad primes are handled as before.

### Corollary 7.1. Explicit auxiliary costs

Uniformly for polynomially bounded squarefree \(\mathfrak q\),

\[
\boxed{
\begin{aligned}
\sum_{k\sim H}|\mathcal C_{A,B}(k;\mathfrak q)|^2
\ll D^\epsilon\Bigg[
&QHA+\frac{Q^3H^2A}{B}M_{A,B}^{2\beta-1}\\
&+Q^{7/3}\left(\frac{H^2A^2}{B}\right)^{2/3}
\Bigg],
\end{aligned}
}                                                         \tag{7.4}
\]

\[
\boxed{
\sum_{k\sim H}|P_{A,B}(k;\mathfrak q)|^2
\ll D^\epsilon
\left[
QHA+Q^3H^2A B^{(2\beta-2)/3}
+Q^{7/3}H^{4/3}A^{4/3}B^{(2\beta-2)/3}
\right].
}                                                         \tag{7.5}
\]

Both sums include every nonzero element row in the annulus. The proof is the same disjoint row-sector summation as in Theorem 6.1, with (7.3) replacing the local factors at \(\mathfrak q\).

### Corollary 7.2. Sharper auxiliary costs by exact local reindexing

The bounds (7.4)–(7.5) can be strengthened to

\[
\boxed{
\begin{aligned}
\sum_{k\sim H}|\mathcal C_{A,B}(k;\mathfrak q)|^2
\ll D^\epsilon\Bigg[
&HA+\frac{QH^2A}{B}M_{A,B}^{2\beta-1}\\
&+Q^{2/3}\left(\frac{H^2A^2}{B}\right)^{2/3}
\Bigg],
\end{aligned}
}                                                         \tag{7.6}
\]

\[
\boxed{
\sum_{k\sim H}|P_{A,B}(k;\mathfrak q)|^2
\ll D^\epsilon
\left[
HA+QH^2A B^{(2\beta-2)/3}
+Q^{2/3}H^{4/3}A^{4/3}B^{(2\beta-2)/3}
\right].
}                                                         \tag{7.7}
\]

Here \(Q\) is bounded by a fixed power of \(D\). All row overlaps with \(\mathfrak q\), exponent-zero masks, units, and bad-prime powers are retained.

**Proof.** First fix a prime \(p\mid\mathfrak q\), put \(q=Np\), and suppose its physical row valuation is \(\nu_p=0\). Its reflected exponent is four. The original outer coefficient gives \(p\nmid a=efg\), and the inverse coefficient, when present, gives \(p\nmid h\). The exact local identity is

\[
B_{p,4}(x)
=-q^{-1/2}
+q^{1/2}\mathbf1_{p\mid n_0}
+q^{1/2}\mathbf1_{p\nmid n_0,\ p\mid b'}.
                                                               \tag{7.8}
\]

The first-reflection conductor contributes \(q^2\) to the effective theta length. Use the full frequency coefficient, which contains \(1/\sqrt{Nn_0}\) and \(1/Nb'\), before freezing or truncating the cube indices. In the second term of (7.8), substitute \(n_0=p n_1\); in the third, substitute \(b'=p b_1\). The former retains \(p\nmid n_1\), and the latter retains \(p\nmid n_0\) while \(b_1\) is unrestricted at \(p\). Relative to the effective length before this prime was inserted, the three terms have the following exact scale and amplitude magnitudes:

| Local term | Squared amplitude multiplier | Effective length multiplier |
|---|---:|---:|
| Negative term | \(q^{-1}\) | \(q^2\) |
| \(p\mid n_0\), with \(n_0=p n_1\) | \(1\) | \(q\) |
| \(p\nmid n_0,\ p\mid b'\), with \(b'=p b_1\) | \(q^{-1}\) | \(q^{-1}\) |

These are precisely the three updates in the source immediately following its prepared theta sum. The second amplitude is one because \(q^{1/2}/\sqrt{q}=1\); the third is \(q^{-1/2}\) because \(q^{1/2}/q=q^{-1/2}\). The frequency scales change by \(q\) and \(q^3\), respectively.

The all-cusp cubic Gauss factorization is preserved. For example, in the squarefree-index term, with the unchanged bad part suppressed,

\[
\gamma_2(e p n_1)
=\gamma_2(p)\gamma_2(e)\gamma_2(n_1)
\chi_e(p)^4\chi_{n_1}(p)^4\chi_{n_1}(e)^4.                \tag{7.9}
\]

The new factors in \(e\) and \(n_1\) are separate bounded column coefficients, and the extracted quadratic row phase \(\chi_{k_0}(p)^3\) has modulus one on the actual rows. The masks \(p\nmid e n_1\) are retained. The fixed bad-prime factors and the fixed-period additive phase remain covered by the all-cusp factorization and its finite ray expansion. In the cube term, the retained \(p\nmid n_0\) is a column mask; the complete remaining \(b_1\), including its arbitrary powers at \(p\), may be frozen as before.

The negative and inverse scalar variables \(g,h\) are unaffected by these changes, apart from their already present exclusion by \(\mathfrak q\). In particular no new growing-conductor premise is imposed on (1.2). The extra characters in (7.9) stay in the separate \(e,n_1\) vectors allowed by the two large sieves. Their values on any extracted common divisors are bounded fixed factors. For several auxiliary primes, repeated CRT introduces only the corresponding separate characters and bounded factors among the fixed extracted primes; it does not couple \(g\) or \(h\) to a theta column.

Consequently the component estimates (4.3) and (5.2) apply separately to the three reindexed terms. Write \(Y_0\) for the effective length before the prime \(p\) was inserted. For the three positive energy monomials

\[
H_0E,\qquad Y_0,\qquad (EY_0)^{2/3},
\]

the squared-norm costs after Minkowski over (7.8) are bounded respectively by

\[
\begin{aligned}
(q^{-1/2}+1+q^{-1/2})^2&\ll1,\\
(q^{1/2}+q^{1/2}+q^{-1})^2&\ll q,\\
(q^{1/6}+q^{1/3}+q^{-5/6})^2&\ll q^{2/3}.
\end{aligned}                                                   \tag{7.10}
\]

One may first split the three energy monomials using
\(\sqrt{x+y+z}\le\sqrt x+\sqrt y+\sqrt z\); the fixed extra factor is harmless. Applying (7.10) at distinct auxiliary primes costs at most \(C^{\omega(\mathfrak q)}\) times \(1,Q,Q^{2/3}\). This factor is \(O_\eta(Q^\eta)\) for every \(\eta>0\), hence is absorbed into \(D^\epsilon\) after choosing preliminary losses sufficiently small. No uniformly bounded Euler product is claimed for these refined local costs.

It remains to sum physical valuations \(\nu_p\ge1\). The cruder estimates used in (7.3) suffice for these sectors. With the full amplitude and branch indicators retained, their three local sums are

\[
\begin{aligned}
\sum_{\nu\ge1}4^{\mathbf1_{\nu\equiv2\ (6)}}
q^{\mathbf1_{\nu\equiv0\ (6)}-\nu}&=O(q^{-1}),\\
\sum_{\nu\ge1}4^{\mathbf1_{\nu\equiv2\ (6)}}
q^{\mathbf1_{\nu\equiv0\ (6)}+2-2\nu}&=O(1),\\
\sum_{\nu\ge1}4^{\mathbf1_{\nu\equiv2\ (6)}}
q^{\mathbf1_{\nu\equiv0\ (6)}+4/3-4\nu/3}&=O(1).
\end{aligned}                                                   \tag{7.11}
\]

For example, the reflected exponent four recurs at \(\nu=6,12,\ldots\); its extra squared amplitude \(q\) is included in every line. The six progressions are geometric, so (7.11) follows without a false termwise bound at those valuations. Physical row sectors are disjoint and their energies are added directly. Combining (7.10) at \(\nu=0\) with (7.11) gives the same local costs \(O(1),O(q),O(q^{2/3})\).

The exact cutoffs \(G^2\ll B\) and \(G^2Z^3\ll B\) were inserted in the reunited sums before the new local expansion, and remain in force. All local reindexings are performed on the full theta sums. Their smooth dyadic partitions and tails are then treated at the rescaled lengths in the table. A normalized ratio \(Nn_0/U\) becomes \(Nn_1/(U/q)\); the cube ratio is rescaled in the same way. Hence the smooth seminorms and the full Mellin tail majorants are uniform in the extracted auxiliary products. The parameter \(Q\) is polynomially bounded.

We may therefore repeat the unchanged \(E,F,G\) optimization for the completion and the \(E,F,G,Z\) optimization for the inverse, attaching the three local costs to their corresponding three monomials. The row primes outside \(S\mathfrak q\) and all bad-prime powers retain the convergent summation of Section 6. This proves (7.6)–(7.7). \(\square\)

At \(A=B=D\), these estimates give \(D^{2+\epsilon}\) throughout

\[
H\le D^{(5-2\beta)/4}Q^{-1/2}
\quad\hbox{for the completion},\qquad
H\le D^{(5-2\beta)/6}Q^{-1/2}
\quad\hbox{for the literal cube-free polynomial},             \tag{7.12}
\]

whenever the displayed range contains \(H\ge1\). The third energy term is no stronger in these ranges because \(1/2<\beta\le1\). This is a uniform auxiliary estimate for a single positive norm; it does not supply cancellation between distinct auxiliary parameters.

## 8. Sharp row balls and fixed Schwartz row weights

Let \(F_{\mathcal C}(H)\) and \(F_P(H)\) denote the brackets on the right of (7.6) and (7.7), respectively, with \(A,B,\mathfrak q\) fixed. When \(\mathfrak q=1\), these are the brackets in (6.3)–(6.4). Every term is a nonnegative constant times \(H\), \(H^2\), or \(H^{4/3}\).

### Corollary 8.1. Sharp balls

For \(H\ge1\),

\[
\begin{aligned}
\sum_{0<Nk\le H}|\mathcal C_{A,B}(k;\mathfrak q)|^2
&\ll D^\epsilon F_{\mathcal C}(H),\\
\sum_{0<Nk\le H}|P_{A,B}(k;\mathfrak q)|^2
&\ll D^\epsilon F_P(H).
\end{aligned}                                                   \tag{8.1}
\]

**Proof.** Partition the nonzero row ball into dyadic annuli, with the terminal unit-norm rows included in the annulus at scale one. Every occurring scale is at most a fixed multiple of \(H\), so the same fixed polynomial reference is valid. Summing \(2^{-j}\), \(2^{-2j}\), and \(2^{-4j/3}\) proves (8.1). There is no logarithmic cost from row summation. \(\square\)

### Corollary 8.2. Fixed Schwartz row weights

Let \(\Phi:[0,\infty)\to\mathbb C\) be fixed, bounded near zero, and rapidly decreasing. A fixed Schwartz function restricted to this half-line is an example. Then

\[
\begin{aligned}
\sum_{k\ne0}|\Phi(Nk/H)|\,|\mathcal C_{A,B}(k;\mathfrak q)|^2
&\ll_{\Phi,\epsilon}D^\epsilon F_{\mathcal C}(H),\\
\sum_{k\ne0}|\Phi(Nk/H)|\,|P_{A,B}(k;\mathfrak q)|^2
&\ll_{\Phi,\epsilon}D^\epsilon F_P(H).
\end{aligned}                                                   \tag{8.2}
\]

It is enough to assume that
\(\sup_{x\ge0}(1+x)^M|\Phi(x)|<\infty\)
for one fixed \(M>2+\epsilon_0\), where \(0<\epsilon_0<\epsilon\) is a preliminary exponent in the dyadic theorem.

**Proof.** The rows \(Nk\le H\) satisfy (8.1). On a tail annulus \(2^jH\le Nk<2^{j+1}H\), the weight is \(O_\Phi(2^{-Mj})\). Set \(H_j=2^jH\) and \(D_j=2^jD\), keeping \(A,B,\mathfrak q\) fixed. After increasing the fixed polynomial exponent \(C_0\) to at least one, all parameters for this annulus are bounded by fixed powers of \(D_j\). Thus the uniform dyadic theorem gives

\[
D_j^{\epsilon_0}F(H_j)
\le D^{\epsilon_0}2^{j(2+\epsilon_0)}F(H)
\]

for either bracket \(F\). The geometric series
\(\sum_{j\ge0}2^{-j(M-2-\epsilon_0)}\)
converges. Choosing the preliminary losses inside the proof small enough proves (8.2). \(\square\)

These corollaries retain every nonzero element row and all literal column zeros. They apply to a fixed scalar row profile, including a fixed Schwartz profile whose Fourier transform is compactly supported. They do not replace the original row-dependent bilinear kernel by a product, or authorize new arbitrary arithmetic weights in the original columns.

## 9. Dependency distinction and remaining gap

The arbitrary-row and auxiliary adapters use no new zero-free input. With \(\beta=1\), their scalar steps use only counting, in addition to the stated classical theta/coefficient identities and upper sieves. With \(\beta=11/12\), they retain the companion imported canonical/angular premise, uniformly in the squarefree scalar index and moving exclusions. No scalar theorem for an arbitrary infinite-order character of growing type is asserted.

The squarefree-row restriction has now been removed from these positive norm estimates, and a moving squarefree auxiliary has the explicit costs \(1,Q,Q^{2/3}\) in (7.6)–(7.7). Sharp row balls and fixed Schwartz row weights obey the same estimates. Those costs are not the desired signed auxiliary cancellation. The initial fourth-moment dual range remains approximately \(D^{3-\vartheta}\), far beyond the all-row cube-free range \(D^{19/36}\).

Moreover, positive norms with one auxiliary parameter do not control the centered sesquilinear family with two independently corrected columns and its exact product-column subtraction. That covariance and the retained signed first-Poisson auxiliary sum remain separate requirements. These results do not prove the full fourth moment, generalized \(2k\)-th hierarchy, or RH.


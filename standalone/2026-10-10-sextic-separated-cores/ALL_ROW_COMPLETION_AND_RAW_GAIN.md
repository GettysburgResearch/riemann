# All-row extension of the pruned completion and a raw two-axis saving

Status: proposed source-conditional theorem. This addendum extends the two new squarefree-row notes to every nonzero row, including sixth-power copies and fixed bad-prime factors. The moving A2-conductor adapter and the full fourth moment remain open. The previously frozen notes are unchanged; their all-row limitation is superseded here only for the literal family treated below.

Dependencies: `PRUNED_COUPLED_MEAN_SQUARE.md` (SHA-256 `411d7b28c0dabc97807d21683d731126e742d16424b1809787c87849dfb9e8d1`), `SHORT_CUBE_RAW_GAIN.md` (`8d97d0a4e6a0eef6ca0178e0dca7ff6e2cd059d594eba1e45fee47d57563cc40`), and their pinned source interfaces. The extra load-bearing local formulas are October 5 `paper2.tex`, `eq:theta-local-factors` (1730), `eq:ray-local-transform` (3230), and the full scalar following `eq:dual-cusp-mellin-series` (3420). The source all-row factorization appears at 2190–2209. The raw long-cube estimate uses PR #913's refined all-row sextic large sieve, `REFINED_ALL_ROW_SIEVE.md`, Theorem 3.4, at commit `6498d6cc2eded03159c7332b25fd224ad07f89c1`.

The proof retains the imported theta automorphy, classical sieves, and PR #920's conductor-uniform angular reciprocal theorem as analytic inputs. It does not independently rebuild those source theorems.

## 1. Statement and exact conventions

Keep the literal completed family \(\mathcal C_{A,B}(k)\) of the main note, with fixed bad set S, fixed finite ray character, and compact smooth norm weights. Original column indices a and the physical theta indices avoid S. Reflected cusp indices may meet S. Character powers always include their nonunit zeros. An additional outer mask \((a,h)=1\) is permitted, with \(Nh\) polynomially bounded in D.

All scales \(A,B,H\ge1\) are bounded by a fixed power of \(D\ge2\). The row sum below is over **all nonzero Eisenstein rows**, represented by the source's fixed generators and units, with norm in \([H,2H)\). The difference between this convention and summing ideals with their finite unit multiplicity is a fixed factor. Put \(T=\min(A,\sqrt B)\).

### Theorem 1.1: all-row pruned completed estimate

For every final \(\epsilon>0\),
\[
\boxed{\sum_{k\asymp H}|\mathcal C_{A,B}(k)|^2
\ll D^\epsilon\left[
HA+\frac{H^2A}{B}T^{5/6}
 +\left(\frac{H^2A^2}{B}\right)^{2/3}\right].}            \tag{1.1}
\]
This is uniform for the stated outer mask. The exponent \(5/6\) uses a fixed line \(\sigma>11/12\) chosen in terms of the final epsilon; no reciprocal estimate on the endpoint line is asserted.

Without the angular reciprocal input, the same proof gives
\[
\boxed{\sum_{k\asymp H}|\mathcal C_{A,B}(k)|^2
\ll D^\epsilon\left[
HA+\frac{H^2A}{B}T
 +\left(\frac{H^2A^2}{B}\right)^{2/3}\right].}            \tag{1.2}
\]
The latter estimate also permits any row-independent outer multiplier v(a) bounded by \(D^\epsilon\) for every epsilon on the polynomial support. That arbitrary-coefficient extension is not asserted for (1.1).

## 2. The scalar and support cutoff for an arbitrary good row

First suppose k avoids S. The factor \(\chi_a(k)\) makes every term with \((a,k)>1\) exactly zero. Thus surviving a is disjoint from the entire row, regardless of its valuations. At p dividing a the local theta exponent is always 4; at a row prime p it is \(j_p=v_p(k)\bmod6\).

Fix one source active set at row primes and let R be their squarefree product. A prime may be inactive only when \(j_p=0\). The first-reflection denominator is
\[
c=c_0 aR.
\]
The source scalar involves \(\chi_p(\sigma_p)^{-2}\omega_{p,j}\), where
\[
\sigma_p=\lambda^2c/p,\qquad
\epsilon_p=-\lambda^{-5}(c/p)^{-2}.
\]
Here lambda is the ramified-prime generator, as in the source. For every active row prime, direct substitution into the source formula for omega gives the following dependence on the varying outer a:
\[
\chi_p(\sigma_p)^{-2}\omega_{p,j}
=\text{factor independent of a}\times\chi_p(a)^{2j+2}.
                                                               \tag{2.1}
\]
For \(j\ne0,4\), the exponent is \(-2+2(j+2)\). For active j=0 it is \(-2+4=2\); for j=4 it is \(-2\equiv10=2j+2\pmod6\). Thus the formula includes both exceptional local cases.

The a-prime factors of \(\chi_p(\sigma_p)^{-2}\) contribute \(\chi_a(R)^{-2}\). Even-power reciprocity converts the row-prime factors in (2.1) into \(\chi_a(\prod_{p\mid R}p^{2j_p+2})\). Their product is \(\chi_a(k)^2\), up to the same finite fixed-ray factors, since an inactive prime has exponent zero modulo six. Meanwhile \(\gamma_2(a)\gamma_4(a)=1\), and the angular scalar leaves \(\overline{\alpha(a)}^3\), exactly as in the squarefree calculation. After multiplying by the original exterior \(\chi_a(k)\), the outer dependence is therefore
\[
\eta(a)\overline{\alpha(a)}^3\chi_a(k)^3.                \tag{2.2}
\]
All scalar factors not displayed in (2.2) are row-only or fixed-ray factors of bounded modulus. Inactive primes contribute only \(1-1/Np\); they produce no reflected local B factor.

The Ramanujan factor from the a primes is unchanged. Keep its complete projection \(a=dg\), \(\mathbf1_{d\mid nb}\), before allocating or taking norms. The reflected periodic multiplier has modulus dividing
\[
q=M R d.
\]
Each extra row factor \(B_{p,j_p}\) is periodic modulo p, with all its zeros retained. Inactive primes occur in neither c nor this period. Hence the ratio of the first-reflection scale to the squared projection period is exactly a fixed multiple of
\[
\frac{(Nc)^2/B}{(Nq)^2}
=\frac{(Nc_0)^2(Ng)^2}{B(NM)^2}.                        \tag{2.3}
\]
The all-cusp opposite-reflection support theorem from PR #920 applies to this finite periodic multiplier; it does not require that multiplier to have modulus at most one. It gives the same exact cutoff
\[
Ng\le C_S\sqrt B.                                     \tag{2.4}
\]
As in the main note, insert a smooth cutoff using the complete groups first, and only then split \(d=ef\) and the theta indices. This proves uniform pruning for arbitrary good rows.

## 3. Freeze the square part and retain its local amplitudes

Write uniquely
\[
k=u_0 s v^2,\qquad s\text{ squarefree},
\]
without imposing \((s,v)=1\). For now absorb the fixed unit into the finite ray data. Put
\[
t=(s,\operatorname{rad}v),\qquad s=t s',\qquad
(s',v)=1,\qquad
V=Nv,\quad H'=\frac{H}{Nt\,V^2}.                       \tag{3.1}
\]
For fixed v,t, the varying row \(s'\) is squarefree of norm comparable to H'. Empty ranges are omitted and bounded nonempty ranges are included in a fixed annulus. The number of t choices is divisor bounded.

All primes of \(s'\) have local exponent 1 and are active. Write the full active row product as \(R=s' r_v\), where \(r_v\mid\operatorname{rad}v\) is fixed for the chosen branch, and put \(R_v=Nr_v\le V\). At a prime dividing v the local exponent is
\[
j_p\equiv 2v_p(v)+\mathbf1_{p\mid t}\pmod6.             \tag{3.2}
\]
Let r4 be the product of those active primes of v with \(j_p=4\), and let \(Q_4=Nr4\). Such a prime necessarily has \(v_p(v)\ge2\): if the valuation is one, (3.2) is 2 or 3. Therefore
\[
Q_4\le J(v):=\prod_{v_p(v)\ge2}Np.                      \tag{3.3}
\]

The outer indices e,f,g all avoid v because a avoids k. In a reflected frequency
\(x=u\lambda^{m+4}e n'(fb')^3\), the extra active row factors separate as follows.

- For \(j\ne0,4\), \(B_{p,j}(x)=\chi_p(x)^{-j-2}\). Since e,f are units modulo p, their factors separate multiplicatively into the e- and f-coefficients, while the remaining character in n',b' preserves every zero.
- For active j=0 the same separation holds for \((Np)^{-1/2}\chi_p(x)^{-2}\), whose modulus is at most one.
- For j=4, the divisibility test is exactly \(p\mid n'b'\), independent of e,f,g. Its modulus is at most \(\sqrt{Np}\).

After freezing b', these extra factors are a bounded separate e-coefficient and an n'-coefficient of modulus at most \(\sqrt{Q_4}\). In particular they introduce no new g-dependence or moving e/n coupling. The Gauss coefficient still splits by the same cubic CRT identity. The all-cusp and bad-prime adapters from the main note therefore apply without alteration to the e,n' sieve.

The squared-conductor scale in the effective squarefree length now uses \(H'R_v\), while the quadratic row sieve uses H'. Precisely, in place of the main note's Y, use
\[
Y_v=\frac{(H'R_v)^2 E G^2}{BF}.                         \tag{3.4}
\]
The coefficient norm adds the factor Q4. Equation (2.2) gives the g coefficient
\[
\mu(g)\eta(g)\overline{\alpha(g)}^3\chi_{s'}(g)^3
 \chi_t(g)^3\mathbf1_{(g,vfhS)=1}.
\]
Its base L-function has the same infinity type -3 and a polynomially bounded moving finite conductor. The reciprocal bound is uniform in that conductor. The remaining e-exclusion is handled by the unchanged operator of Lemma 5.1 in the main note, whose summable norm is \(\sum_d (Nd)^{-\sigma}(N\operatorname{rad}d)^{-1/2}\). All e-v exclusions are fixed coefficient restrictions for this block. Thus the proof of the angular improvement is still applicable.

It follows that, for fixed v,t and branch,
\[
\sum_{s'\asymp H'}^*|\mathcal C_{v,t,\mathrm{branch}}(s')|^2
\ll D^\epsilon Q_4\left[
H'A+\frac{(H'R_v)^2A}{B}T^{5/6}
 +\left(\frac{(H'R_v)^2A^2}{B}\right)^{2/3}\right].      \tag{3.5}
\]
All multiplicative branch counts, fixed-ray splits and dyadic smooth costs are divisor bounded or logarithmic, hence absorbed in D^epsilon. This is a coefficient and scale adapter, not an appeal to an arbitrary theta-coefficient theorem.

## 4. The square-part sum is convergent

Distinct v,t give disjoint original row sets. Therefore sum their squared bounds; no Minkowski factor for the number of v is incurred. The active-set and finite-branch sums were already accounted for by a divisor bound inside each block. From (3.1) and \(R_v\le V\),
\[
Q_4H'\le H\frac{J(v)}{V^2},\qquad
Q_4(H'R_v)^2\le H^2\frac{J(v)}{V^2},\qquad
Q_4(H'R_v)^{4/3}\le H^{4/3}\frac{J(v)}{V^{4/3}}.
                                                               \tag{4.1}
\]
Dropped factors \((Nt)^{-1},(Nt)^{-2},(Nt)^{-4/3}\) are at most one. Their divisor multiplicity may be bounded by a global D^epsilon on the polynomial support.

Both required sums over v converge. More generally, for \(\rho>1\), their Euler factor is
\[
\sum_{e\ge0}\frac{(Np)^{\mathbf1_{e\ge2}}}{(Np)^{\rho e}}
=1+(Np)^{-\rho}
 +\frac{(Np)^{1-2\rho}}{1-(Np)^{-\rho}}.                 \tag{4.2}
\]
At \(\rho=2\) the first nontrivial powers are \(q^{-2},q^{-3}\); at \(\rho=4/3\) they are \(q^{-4/3},q^{-5/3}\). Both Euler products converge absolutely. This is why the square-root loss at j=4 primes is harmless: such primes require at least a squared prime in v, rather than an arbitrary first-power prime.

Summing (3.5) using (4.1)–(4.2) proves (1.1) for every good row, with every repeated-prime pattern included. Repeating the proof with the ordinary g count gives (1.2) and its bounded outer-coefficient extension.

## 5. Row factors at the fixed bad set

Write an arbitrary nonzero row as \(k=u z k_0\), where u is a unit, z is supported on S, and \((k_0,S)=1\). On every physical column n outside S, the twist \(n\mapsto\chi_n(uz)\) belongs to a fixed finite set of ray characters supported on S: sextic reciprocity and the supplementary laws place its conductor in a fixed S-supported modulus, and only valuations of z modulo six and the finitely many units matter.

Define \(\xi_z(n)=\xi(n)\chi_n(uz)\) on good physical indices. The dependence on the unit is included in this notation. Then
\[
a_{\xi_z}(a)=a_\xi(a)\chi_a(uz),\qquad
\mathcal C^{\xi}_{A,B}(uzk_0)
=\mathcal C^{\xi_z}_{A,B}(k_0).                         \tag{5.1}
\]
This is exact in the physical completion, including its cube coefficient, by complete multiplicativity. The outer h mask is unchanged. Thus no extra reflected bad-prime convention is needed for this reduction.

For fixed z apply the good-row theorem at height \(H/Nz\). The finitely many possible characters have a common implied constant. The three powers of height in (1.1) are 1,2,4/3, so their z sums converge by
\[
\sum_{z\ S\text{-smooth}}(Nz)^{-\rho}
=\prod_{p\in S}(1-(Np)^{-\rho})^{-1}<\infty
\quad(\rho>0).                                        \tag{5.2}
\]
Only nonempty rows contribute, so subunit scales are bounded and harmless. This proves Theorem 1.1 with all nonzero rows. The same argument proves (1.2).

## 6. Cube inversion with the all-row long-tail estimate

Let P(D,D;k) be the raw polynomial defined in `SHORT_CUBE_RAW_GAIN.md`, equation (1.1). Its exact truncated inverse and long-tail regrouping apply at every row, with no squarefreeness assumption on k. In particular the long tail retains the coefficient
\[
c_R(d)=\sum_{\substack{h\mid d\\Nh>R}}\mu(h),
\]
the zero mask \((a,d)=1\), and allows n to share primes with d.

Theorem 1.1 bounds the short inverse exactly as before:
\[
\|\mathcal S_R\|_2^2\ll D^\epsilon
[HD+H^2D^{5/12}R^{7/4}+H^{4/3}D^{2/3}R^2].             \tag{6.1}
\]
For the long part, use the refined **all-row** sieve on the squarefree product column of length \(L=D^2/(Nd)^3\). Its normalized energy is
\[
H+H^{1/6}L+(HL)^{2/3},
\]
uniformly for the row-independent outer mask in the coefficients. The same convergent cube tail sums give
\[
\|\mathcal L_R\|_2^2\ll D^\epsilon
[H+H^{1/6}D^2R^{-3}+H^{2/3}D^{4/3}R^{-2}].             \tag{6.2}
\]
The term \(H^{1/6}D^2R^{-3}\) explicitly retains the cost of sixth-power copies; it is not replaced by the squarefree-row tail.

### Theorem 6.1: all-row raw two-axis estimate

For \(1\le R\le D^{1/3}\),
\[
\boxed{\sum_{k\asymp H}|P(D,D;k)/D|^2\ll D^\epsilon[
HD+H^2D^{5/12}R^{7/4}+H^{4/3}D^{2/3}R^2
 +H+H^{1/6}D^2R^{-3}+H^{2/3}D^{4/3}R^{-2}].}            \tag{6.3}
\]
Choose \(R=D^{4/15}H^{-7/30}\) for \(1\le H\le D^{38/87}\). The third and fifth terms are \(D^{6/5}H^{13/15}\). The second is \(D^{53/60}H^{191/120}\), at most that bound exactly when \(H\le D^{38/87}\). The other comparisons follow immediately in this range. Hence
\[
\boxed{\sum_{k\asymp H}|P(D,D;k)/D|^2
\ll D^{6/5+\epsilon}H^{13/15},\quad1\le H\le D^{38/87}.} \tag{6.4}
\]

For \(D^{38/87}\le H\le D^{19/22}\), take
\(R=D^{1/3}H^{-22/57}\). The second and fifth terms equal \(D H^{151/114}\). The third is \(D^{4/3}H^{32/57}\), bounded by this common quantity exactly when \(H\ge D^{38/87}\). The remaining terms are smaller, and R is at least one precisely through the displayed upper range. Thus
\[
\boxed{\sum_{k\asymp H}|P(D,D;k)/D|^2
\ll D^{1+\epsilon}H^{151/114},\quad
D^{38/87}\le H\le D^{19/22}.}                           \tag{6.5}
\]
These regimes match at their junction. In particular the energy is \(O(D^{2+\epsilon})\) throughout \(1\le H\le D^{114/151}\). At \(H=D^{1/2}\), the optimized cutoff is \(R=D^{8/57}\), and
\[
\boxed{\sum_{k\asymp D^{1/2}}|P(D,D;k)/D|^2
\ll D^{379/228+\epsilon}.}                             \tag{6.6}
\]
The elementary all-row envelope is \(O(D^{25/12+\epsilon})\) at this height. This is a new power saving for the actual balanced raw Gauss polynomial with all repeated-prime rows retained.

## 7. The remaining moment gap is still explicit

The completed estimate now includes all rows and sixth-power copies for the literal family, and the raw corollary carries those rows through cube inversion. Thus the squarefree-row limitation of the companion notes is not the remaining obstruction for these specific theorems.

The result does not yet include moving A2 exclusions q on both physical axes, additional auxiliary f, or their overlaps. Their extra local factors are not the row factors treated in Sections 2–4. It also does not directly supply the actual Möbius fourth-moment Poisson comparison at all required gcd and allocation scales. The initial adverse dual height near \(D^{3-\theta}\) is far outside the controlled short-height regimes (6.4)–(6.5). A substitution of a formal dual-scale relation does not prove that comparison. No full fourth moment, generalized diagonal 2k hierarchy, or new zeta zero-free boundary is claimed here.

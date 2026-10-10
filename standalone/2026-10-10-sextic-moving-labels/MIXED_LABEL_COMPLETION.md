# Moving exclusions and auxiliary twists in the completed two-axis family

**Status:** proposed source-conditional analytic theorem and exact finite arithmetic identities. This note supplies the moving inner exclusion and auxiliary-ideal adapter for the positive completed norm in the A2/theta comparison. It treats every nonzero element row, every overlap among the two moving labels and the row, and an additional outer coprimality mask. The new primewise costs are explicit. No centered covariance estimate, full fourth moment, new zeta boundary, or unbounded moment hierarchy is inferred.

**Exact sources.**

1. PR #918, commit `cfa102748b26f840ccc4b963a660711424db0ec3`, `standalone/2026-10-10-sextic-joint-core/INTERFACE_COMPARISON.md`, Sections 1–3: the literal mixed family, A2 composition, and the inverse with all zero masks. The mathematical definitions and finite identities are restated and proved below.
2. PR #923, commit `1a1152008706f7e24fa1efe4990588f8f99c5d8d`, `standalone/2026-10-10-sextic-separated-cores/PRUNED_COUPLED_MEAN_SQUARE.md`, `ALL_ROW_LOCAL_AUDIT.md`, and `ALL_ROW_COMPLETION_AND_RAW_GAIN.md`: all-cusp cubic Gauss factorization, exact complete-group support, the fixed-row-factor adapter, the moving-mask operator, and the source-conditional angular reciprocal estimate.
3. PR #921, commit `4e6d4aa57ae4cb04d76b2b31279ac367951b469a`, `standalone/2026-10-10-sextic-centered-covariance/ARBITRARY_ROW_MOMENTS.md`, Sections 2–4 and Corollary 7.2: exact scalar dependence, disjoint physical row sectors, and the three-term local reindexing which improves the single auxiliary's costs to \(1,F,F^{2/3}\). The present proof explicitly composes that local argument with exponent-zero exclusion primes; it does not treat the source's single-auxiliary conclusion as already covering a second exclusion label.
4. The common imported source is OpenAI/math commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`, October 5 `paper2.tex`, SHA-256 `d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d`. The exact local inputs are `eq:theta-local-factors`, `eq:ray-local-transform`, the full scalar after `eq:dual-cusp-mellin-series`, and the physical completed sum and cube inverse. No independent verification of its automorphy theorem or of the inherited reciprocal estimate is claimed here.

The new content is the exact row relabeling with redundant-prime removal, the exponent-zero active/inactive local norm calculation, its composition with the auxiliary local reindexing and the all-row proof, and the explicitly closed masked cube identities needed by subsequent estimates.

## 1. Objects and the exact label identity

Work over the Eisenstein integers with the source primary-generator convention and fixed finite bad-prime set \(S\), containing the primes over 6. Physical ideal indices are outside \(S\). Reflected cusp indices retain their full source support and may meet \(S\). Let

\[
\alpha(a)=a/|a|,\qquad
\lambda(a)=\overline{\alpha(a)}\xi(a),\qquad
a_\xi(a)=\lambda(a)\gamma_2(a)
\quad(a\text{ squarefree}),
\tag{1.1}
\]

where \(\xi\) is fixed finite ray data. Every sextic symbol
\(\chi_a(x)=(x/a)_6\) has its literal zero on nonunits. In particular,

\[
\chi_a(x)^6=\mathbf1_{(a,x)=1},
\tag{1.2}
\]

including when the ideal represented by \(x\) is not squarefree.

Fix compact smooth norm weights \(W_1,W_2\), supported in fixed positive intervals, and put \(V_*(y)=\sqrt y\,W_2(y)\). For squarefree ideals \(q,f\) outside \(S\), with no coprimality assumption between them, define

\[
\Psi_{k,af;q}(n)
=\xi(n)\chi_n(k)\chi_n(af)^4\mathbf1_{(n,qS)=1},
\tag{1.3}
\]

\[
T(B;\Psi)=
\sum_{n\text{ squarefree}}\sum_b
\frac{\overline{\alpha(n)}\gamma_2(n)\Psi(n)
      \overline{\alpha(b)}^3\Psi(b)^3}
     {\sqrt{Nn}\,Nb}
V_*\!\left(\frac{Nn(Nb)^3}{B}\right).
\tag{1.4}
\]

The unrestricted cube index \(b\) need not be coprime to \(n\). For an arbitrary ideal \(r\) of polynomially bounded norm, let \(v_r(a)=\mathbf1_{(a,r)=1}\) and set

\[
\mathcal C_{q,r}(A,B;k,f)
=\frac1{\sqrt A}
\sum_{\substack{a\text{ squarefree}\\(a,qS)=1}}
a_\xi(a)\chi_a(k)\chi_a(f)^4v_r(a)W_1(Na/A)
T(B;\Psi_{k,af;q}).
\tag{1.5}
\]

All physical sums are finite. The \(q\) exclusion in (1.3) acts on **both** \(n\) and \(b\). The exterior factor excludes \(a\) meeting \(f\), so the auxiliary \(af\) is squarefree on every surviving term. No restriction \((k,qf)=1\) is imposed.

Write

\[
q_* = q/(q,f),\qquad Q=Nq_*,\qquad F=Nf.
\tag{1.6}
\]

Then \((q_*,f)=1\). The primes in \((q,f)\) are redundant as exclusions because the fourth-power twist at \(f\) already vanishes on their nonunits.

### Lemma 1.1. Exact simultaneous relabeling

For every nonzero element row \(k\),

\[
\boxed{
\mathcal C_{q,r}(A,B;k,f)
=\mathcal C_{1,r}(A,B;k f^4q_*^6,1).
}
\tag{1.7}
\]

Here the powers use the fixed multiplicative primary generators. If a different representative convention introduces a unit, that unit is retained in the fixed finite ray data. The identity is literal under the fixed convention.

**Proof.** For every physical index \(n\), complete multiplicativity with zeros gives

\[
\chi_n(k f^4q_*^6)
=\chi_n(k)\chi_n(f)^4\mathbf1_{(n,q_*)=1}
=\chi_n(k)\chi_n(f)^4\mathbf1_{(n,q)=1}.
\tag{1.8}
\]

The last equality uses the zero already present at primes of \(f\). It proves the identity for the inner twist and the exterior \(a\) factor. On the cube index the same calculation, cubed, is

\[
\chi_b(k f^4q_*^6)^3
=\chi_b(k)^3\mathbf1_{(b,fq_*)=1}.
\tag{1.9}
\]

Thus no cube-index exclusion is lost. The outer mask \(v_r\) is unchanged, and every summand in (1.4)–(1.5) agrees. This proves (1.7), including rows sharing primes with any label. \(\square\)

This is an identity in the values of the family, not a replacement of the physical row range by the much larger ball of norm \(HF^4Q^6\). The norm proof below retains the original row height \(H\).

## 2. Quantified mixed completed estimate

Let \(D\ge2\), and fix a scale ceiling \(C_0\). Assume

\[
1\le A,B,H,Nq,Nf,Nr\le D^{C_0}.
\tag{2.1}
\]

The same estimates cover bounded nonempty scales below one by enlarging them to a fixed support-dependent annulus. An empty physical rectangle contributes zero. Constants may depend on \(C_0\), \(\epsilon\), the fixed field, ray and bad-prime data, and a fixed finite number of weight seminorms.

Let \(1/2<\beta\le1\) be a scalar exponent for the negative-allocation Möbius/angular sums, with the exact uniformity in squarefree quadratic row index, moving exclusion and separated smooth profiles stated in PR #921, equation (1.2), or supplied by the convergent reciprocal operator in PR #923. Counting gives \(\beta=1\). The source-conditional angular argument gives the exponent notation \(\beta=11/12\), with its final \(D^\epsilon\) loss: where a reciprocal contour is used, first choose a fixed line strictly to the right of \(11/12\) and absorb its margin. No reciprocal estimate on the endpoint is asserted.

### Theorem 2.1. Moving exclusion, auxiliary and outer mask

Put \(M=\min(A,\sqrt B)\). Under the stated analytic inputs,

\[
\boxed{
\begin{aligned}
\sum_{\substack{k\in\mathcal O\\H\le Nk<2H}}
|\mathcal C_{q,r}(A,B;k,f)|^2
\ll_\epsilon D^\epsilon\Bigg[
&HA+FQ\frac{H^2A}{B}M^{2\beta-1}\\
&+F^{2/3}Q^{1/3}
\left(\frac{H^2A^2}{B}\right)^{2/3}\Bigg].
\end{aligned}
}
\tag{2.2}
\]

Every nonzero element row in the annulus is included. There is no coprimality requirement among \(k,q,f,r\). The implied constant has no further power dependence on these labels. In particular the source-conditional choice is

\[
\boxed{
HA+FQ\frac{H^2A}{B}M^{5/6}
+F^{2/3}Q^{1/3}
\left(\frac{H^2A^2}{B}\right)^{2/3}.
}
\tag{2.3}
\]

With counting, replace \(M^{5/6}\) by \(M\). The counting version also permits the bounded row-independent outer multipliers covered by PR #923. The angularly improved version here only asserts the displayed outer coprimality mask and separated smooth norm factors; it does not allow an arbitrary coefficient of \(a\).

The proof occupies Sections 3–6. The third cost is smaller than \((FQ)^{2/3}\), because an exclusion prime's active exponent-zero amplitude is \((Np)^{-1/2}\) and has no Ramanujan divisibility term.

## 3. The scalar, masks and exact pruning survive the relabeling

Let

\[
K=k f^4q_*^6.
\]

The outer coefficient of (1.7) forces \((a,K)=1\). Thus every prime of \(a\) has local exponent four in the reflection, and every additional prime belongs solely to the effective row. At an active row prime \(p\), with \(j_p=v_p(K)\bmod6\), the full source scalar depends on the varying outer \(a\) through

\[
\chi_p(a)^{2j_p+2}.
\tag{3.1}
\]

The outer-prime CRT contribution cancels the extra two powers per active row prime. Together with the original outer character and the Gauss-product identity \(\gamma_2(a)\gamma_4(a)=1\), the complete outer dependence is

\[
\eta(a)\overline{\alpha(a)}^3\chi_a(K)^3,
\tag{3.2}
\]

up to bounded row-only factors and the fixed finite ray splitting. This is the exact scalar calculation in both pinned all-row proofs. By (1.9), its new label dependence is only

\[
\chi_a(K)^3
=\chi_a(k)^3\mathbf1_{(a,fq_*)=1}.
\tag{3.3}
\]

Consequently the negative allocation retains the literal coefficient

\[
\mu(g)\eta(g)\overline{\alpha(g)}^3\chi_g(k)^3,
\tag{3.4}
\]

with the full exclusion at \(fq_*r\) and the other allocation masks. No auxiliary character depending on \(g\) has been suppressed. The effective shifts four and six are even, so the quadratic row index in the scalar bound is the squarefree odd-valuation part of the original \(k\). It is polynomially bounded by the physical row norm. The additional labels enlarge its imprimitive exclusion but not its infinity type.

For a fixed source branch write its active row radical as \(R_K\), with first denominator \(c=c_0aR_K\). In the complete outer Ramanujan projection \(a=d g\), a period of the full reflected multiplier is \(M_0R_Kd\), where \(M_0\) is fixed bad-prime data. Thus

\[
\frac{(Nc)^2/B}{(NM_0R_Kd)^2}
=\frac{(Nc_0)^2(Ng)^2}{B(NM_0)^2}.
\tag{3.5}
\]

An inactive exponent-zero prime is in neither denominator nor period. The all-cusp support theorem therefore gives the same complete-group cutoff

\[
Ng\ll\sqrt B.
\tag{3.6}
\]

Insert that smooth cutoff before splitting positive allocations, row-local Ramanujan terms, reflected cubes, ramified valuations or frequency dyads. The outer mask \(v_r(a)\) is fixed on the projected group and preserves its zero. The cutoff constant remains uniform in \(q,f,r,k\).

## 4. The new local calculation: a principal exclusion prime

Fix \(p\mid q_*\), put \(p_0=Np\), and first consider physical rows with \(v_p(k)=0\). The effective row has exponent six at \(p\). Its exponent-zero local decomposition has two branches:

| Branch | Amplitude magnitude | Reflected length multiplier |
|---|---:|---:|
| Inactive | \(1-p_0^{-1}\) | \(1\) |
| Active | \(p_0^{-1/2}\) | \(p_0^2\) |

The inactive branch has no reflected multiplier. The active multiplier is

\[
B_{p,0}(x)=p_0^{-1/2}\chi_p(x)^4.
\tag{4.1}
\]

At this prime the original outer variables avoid \(p\). After the ordinary outer allocation \(a=e\ell g\), the frequency is a fixed unit/bad factor times

\[
x=e n'(\ell b')^3.
\tag{4.2}
\]

Hence (4.1) separates into a bounded \(e\)-coefficient and an \(n'\)-coefficient, with the remaining cube factor and all its zeros retained. It introduces no \(g\)-dependence. After freezing the complete cube index its amplitude is at most \(p_0^{-1/2}\). The original quadratic row mask in the two-sieve lemma is unchanged.

For the component energy monomials

\[
H_0E,\qquad Y_0,\qquad(EY_0)^{2/3},
\tag{4.3}
\]

take square roots, sum the two branches, and square. Their respective costs are bounded by

\[
\begin{aligned}
(1-p_0^{-1}+p_0^{-1/2})^2&\ll1,\\
(1-p_0^{-1}+p_0^{1/2})^2&\ll p_0,\\
(1-p_0^{-1}+p_0^{1/6})^2&\ll p_0^{1/3}.
\end{aligned}
\tag{4.4}
\]

This proves the exclusion-prime costs \(1,p_0,p_0^{1/3}\) on the zero-valuation physical sector. The bounds follow from exact amplitude and conductor data; they do not use a claim that the exponent-zero prime is always inactive.

Now let \(\nu=v_p(k)\ge1\). Its effective exponent is \(j\equiv\nu\pmod6\). The physical row height is shortened by \(p_0^\nu\). Crude active-amplitude bounds suffice: the squared amplitude is at most \(p_0\) if \(\nu\equiv4\pmod6\), and at most one otherwise; possible exponent-zero branching costs at most four. The active radical costs at most \(p_0\). Therefore the three local sums over positive physical valuations are bounded by

\[
\begin{aligned}
\sum_{\nu\ge1}4^{\mathbf1_{\nu\equiv0\ (6)}}
p_0^{\mathbf1_{\nu\equiv4\ (6)}-\nu}
&\ll p_0^{-1},\\
\sum_{\nu\ge1}4^{\mathbf1_{\nu\equiv0\ (6)}}
p_0^{\mathbf1_{\nu\equiv4\ (6)}+2-2\nu}
&\ll1,\\
\sum_{\nu\ge1}4^{\mathbf1_{\nu\equiv0\ (6)}}
p_0^{\mathbf1_{\nu\equiv4\ (6)}+4/3-4\nu/3}
&\ll1.
\end{aligned}
\tag{4.5}
\]

Each assertion is the sum of six geometric progressions. The leading valuation is \(\nu=1\); the exceptional square-root amplitude at \(\nu=4,10,\ldots\) and the branch count at \(\nu=6,12,\ldots\) are explicitly included. Combining (4.4) with these disjoint-sector sums preserves the costs \(O(1),O(p_0),O(p_0^{1/3})\).

In particular this proof does not establish a subpower cost in \(Q\): the active branch contributes \(p_0\) to the long-length energy monomial and \(p_0^{1/3}\) to the mixed monomial. Improving those factors would require further cancellation or a different operator estimate. This is a limitation of the displayed proof, not a lower bound ruling out a stronger theorem.

## 5. Auxiliary primes and compatibility of the local operations

At \(p\mid f\), which is now disjoint from \(q_*\), the effective local exponent is \(j\equiv\nu+4\pmod6\). At physical valuation \(\nu=0\) it is four. The full frequency sum has the exact identity

\[
B_{p,4}(x)
=-p_0^{-1/2}
 +p_0^{1/2}\mathbf1_{p\mid n'}
 +p_0^{1/2}\mathbf1_{p\nmid n',\ p\mid b'}.
\tag{5.1}
\]

This must be used before freezing or discarding the cube index. In its second term set \(n'=p n_1\), retaining \(p\nmid n_1\). In its third term set \(b'=p b_1\), retaining \(p\nmid n'\), with \(b_1\) unrestricted at \(p\). Against the full theta denominator \(\sqrt{Nn'}Nb'\), the exact squared-amplitude and effective-length updates are

| Term | Squared amplitude | Length multiplier |
|---|---:|---:|
| Negative | \(p_0^{-1}\) | \(p_0^2\) |
| Squarefree extraction | \(1\) | \(p_0\) |
| Cube extraction | \(p_0^{-1}\) | \(p_0^{-1}\) |

The resulting three energy costs, by Minkowski at the norm level, are

\[
\begin{aligned}
(p_0^{-1/2}+1+p_0^{-1/2})^2&\ll1,\\
(p_0^{1/2}+p_0^{1/2}+p_0^{-1})^2&\ll p_0,\\
(p_0^{1/6}+p_0^{1/3}+p_0^{-5/6})^2&\ll p_0^{2/3}.
\end{aligned}
\tag{5.2}
\]

This is the exact local reindexing in PR #921 Corollary 7.2, restated to expose the composition. Gauss CRT under the squarefree extraction gives

\[
\gamma_2(e p n_1)
=\gamma_2(p)\gamma_2(e)\gamma_2(n_1)
\chi_e(p)^4\chi_{n_1}(p)^4\chi_{n_1}(e)^4.
\tag{5.3}
\]

The new factors are separate bounded \(e\)- and \(n_1\)-coefficients, with \(p\nmid e n_1\) retained. The extracted quadratic row phase is bounded on the true row sector. The fixed cusp additive factors remain handled by the same finite bad-ray splitting as in the all-cusp proof.

For several auxiliary primes, these extractions multiply their fixed prime products; mutual CRT factors depend only on the fixed extracted labels. At a different exclusion prime, (4.1) applied to an extracted product changes only bounded fixed phases or separate column factors. Since \((q_*,f)=1\), it cannot create a new local divisibility overlap at the same prime. Neither operation adds a variable coupling to \(g\), nor changes its Möbius coefficient. The permitted outer mask supplies only additional fixed exclusions on \(e,\ell,g\). Thus the scalar and two-sieve arguments apply with every displayed local term.

Positive physical valuations at an auxiliary prime have the three convergent sums

\[
\begin{aligned}
\sum_{\nu\ge1}4^{\mathbf1_{\nu\equiv2\ (6)}}
p_0^{\mathbf1_{\nu\equiv0\ (6)}-\nu}&\ll p_0^{-1},\\
\sum_{\nu\ge1}4^{\mathbf1_{\nu\equiv2\ (6)}}
p_0^{\mathbf1_{\nu\equiv0\ (6)}+2-2\nu}&\ll1,\\
\sum_{\nu\ge1}4^{\mathbf1_{\nu\equiv2\ (6)}}
p_0^{\mathbf1_{\nu\equiv0\ (6)}+4/3-4\nu/3}&\ll1.
\end{aligned}
\tag{5.4}
\]

These are the physical row-height sums, not sums at height enlarged by \(p_0^4\). Their residue-zero progression begins at \(\nu=6\), not at zero. Combining them with (5.2) gives \(O(1),O(p_0),O(p_0^{2/3})\) per auxiliary prime.

## 6. Global row sum and proof of Theorem 2.1

Decompose the original row uniquely as

\[
k=u z\,\tau\,k_0
\prod_{p\mid f q_*}p^{\nu_p},
\tag{6.1}
\]

where \(u\) is a unit, \(z\) is supported on \(S\), \(k_0\) is squarefree, and every prime of \(\tau\) has valuation at least two. The ideals \(k_0,\tau\) avoid \(Sfq_*\), and \((k_0,\tau)=1\). Fix all data except \(k_0\); its physical height is

\[
H_0=\frac{H}{Nz\,N\tau\prod_{p\mid f q_*}(Np)^{\nu_p}}.
\tag{6.2}
\]

Only nonempty sectors are used; they have \(H_0\) bounded below by a fixed positive constant, so no large sieve is applied at an unboundedly small length.

Before the new local operations, the pinned all-cusp block argument is

\[
D^\epsilon G^{2\beta-2}
[H_0E+Y+(EY)^{2/3}],\qquad
Y=\frac{H_0^2R_\tau^2EG^2}{B L},\qquad E L G\asymp A.
\tag{6.3}
\]

Here \(L\) denotes the norm scale of the positive outer cube-allocation ideal \(\ell\), not an L-function or the auxiliary norm. The full row-factor amplitude and branch counts at \(\tau\) are retained as in the cited fixed-sector theorem. The fixed \(fq_*r\) exclusions belong to the scalar input and separate column vectors. At all cusps, the normalized theta coefficient still factors by (5.3), and the required quadratic row mask is the original one in the two-sieve lemma.

The exact support cutoff gives \(G\ll M=\min(A,\sqrt B)\). Smooth kernel separation is performed before taking either scalar or sieve bounds. The new local reindexings replace a ratio such as \(Nn'/U\) by \(Nn_1/(U/Np)\); they preserve the logarithmic-derivative bounds on the common Mellin majorant. All labels and effective lengths are polynomially bounded in the same reference \(D\), after a fixed increase of the ceiling. Arbitrary bad-prime squarefree patterns and full cube/ramified tails remain those of the pinned all-cusp proof, with their summable weights.

The local calculations in Sections 4–5 attach costs

\[
1,\qquad FQ,\qquad F^{2/3}Q^{1/3}
\tag{6.4}
\]

to the respective monomials in (6.3), with at most \(C^{\omega(fq_*)}\) additional loss. That factor is \(O_\eta((FQ)^\eta)\) for every \(\eta>0\) and is absorbed into the final \(D^\epsilon\). No uniformly bounded Euler product is asserted for this subpower factor.

The physical sectors in (6.1) are disjoint; their **energies** are summed. No Minkowski factor is used for the number of such sectors. The positive valuations at \(fq_*\) have already been included in (4.5) and (5.4). Outside those primes, the three sums over \(\tau\) are exactly the convergent ones in PR #921 Section 6. At a prime of norm \(p_0\), their Euler factors are bounded by

\[
\begin{aligned}
1+\sum_{v\ge2}4^{\mathbf1_{6\mid v}}
p_0^{\mathbf1_{v\equiv4\ (6)}-v}&=1+O(p_0^{-2}),\\
1+\sum_{v\ge2}4^{\mathbf1_{6\mid v}}
p_0^{\mathbf1_{v\equiv4\ (6)}+2-2v}&=1+O(p_0^{-2}),\\
1+\sum_{v\ge2}4^{\mathbf1_{6\mid v}}
p_0^{\mathbf1_{v\equiv4\ (6)}+4/3-4v/3}&=1+O(p_0^{-4/3}).
\end{aligned}
\tag{6.5}
\]

All three products converge. The fixed bad-prime sums over \(z\) are geometric at height powers \(1,2,4/3\); unit and fixed ray data have bounded multiplicity. Removing finitely many factors corresponding to \(fq_*\) cannot increase the products of these positive Euler factors.

Finally optimize the outer allocation in (6.3). With \(E L G\asymp A\),

\[
G^{2\beta-2}H_0E\ll H_0A,
\]

\[
G^{2\beta-2}Y
\ll \frac{H_0^2R_\tau^2 A}{B}M^{2\beta-1},
\]

\[
G^{2\beta-2}(EY)^{2/3}
\ll\left(\frac{H_0^2R_\tau^2 A^2}{B}\right)^{2/3}.
\tag{6.6}
\]

The norm-block and cusp sums have the inherited logarithmic/subpower costs. Insert (6.4) and the convergent row-sector sums to obtain exactly (2.2). This proves Theorem 2.1. \(\square\)

### Corollary 6.1. Row balls and positive restrictions

The bound (2.2) holds with the annulus replaced by \(0<Nk\le H\), and also bounds the same positive norm on any subset of that row ball. Every energy term has a positive power of \(H\), so dyadic row summation is geometric. Fixed nonnegative Schwartz row profiles are likewise permitted by the tail argument in PR #921 Section 8. No sign-changing arithmetic row weights or centered subtraction are introduced by this corollary.

## 7. Exact inverse and tail with all moving masks

Define the normalized raw polynomial with optional outer mask \(r\) by

\[
\mathscr P_{q,r}(A,B;k,f)
=\frac1{\sqrt{AB}}
\sum_{\substack{an\text{ squarefree}\\(an,qS)=1}}
a_\xi(an)\chi_{an}(k)\chi_{an}(f)^4
\mathbf1_{(a,r)=1}W_1(Na/A)W_2(Nn/B).
\tag{7.1}
\]

The squarefree-product condition includes \((a,n)=1\). Complete multiplicativity gives the same row relabeling as (1.7) for \(\mathscr P\).

### Lemma 7.1. The masked cube inverse is closed

For every nonzero row,

\[
\boxed{
\mathscr P_{q,r}(A,B;k,f)
=\sum_{\substack{h\text{ squarefree}\\(h,qfS)=1}}
\frac{\mu_K(h)\lambda(h)^3\chi_h(k)^3}{Nh}
\mathcal C_{q,rh}
\left(A,\frac{B}{(Nh)^3};k,f\right).
}
\tag{7.2}
\]

The sum is finite on physical support, with \((Nh)^3\ll B\). There is no extra requirement \((h,r)=1\).

**Proof.** The exact cube coefficient is

\[
\overline{\alpha(h)}^3\Psi_{k,af;q}(h)^3
=\lambda(h)^3\chi_h(k)^3
\mathbf1_{(h,afqS)=1}.
\tag{7.3}
\]

The \(h,f,q,S\) exclusions belong outside the outer sum; its \(a\) exclusion multiplies \(v_r(a)\) to give \(v_{rh}(a)\). Substitute (1.4), group the physical cube product as \(d=hb\), and use

\[
\sum_{h\mid d}\mu_K(h)=\mathbf1_{d=1}.
\tag{7.4}
\]

The remaining \(d=1\) face is (7.1), by the source CRT identity
\(a_\xi(an)=a_\xi(a)a_\xi(n)\chi_n(a)^4\). The outer restriction \(r\) does not impose a condition on \(h\) or on the inner physical index. Every rearrangement is finite and preserves the character zeros. \(\square\)

Conversely the physical cube expansion is exactly

\[
\boxed{
\mathcal C_{q,r}(A,B;k,f)
=\sum_{\substack{b\text{ arbitrary}\\(b,qfS)=1}}
\frac{\lambda(b)^3\chi_b(k)^3}{Nb}
\mathscr P_{q,rb}
\left(A,\frac{B}{(Nb)^3};k,f\right).
}
\tag{7.5}
\]

The new mask is on the outer factor only. The inner squarefree index is allowed to share primes with \(b\).

For a cutoff \(R\ge1\), let \(\mathcal L_R\) denote the part of (7.2) with \(Nh>R\). Combining (7.2) and (7.5), without taking any absolute values, gives

\[
\boxed{
\mathcal L_R(k)
=\sum_{\substack{d\text{ arbitrary}\\Nd>R,\ (d,qfS)=1}}
\frac{c_R(d)\lambda(d)^3\chi_d(k)^3}{Nd}
\mathscr P_{q,rd}
\left(A,\frac{B}{(Nd)^3};k,f\right),
\qquad
c_R(d)=\sum_{\substack{h\mid d\\Nh>R}}\mu_K(h).
}
\tag{7.6}
\]

The ideal \(d\) is not required to be squarefree, there is no \((h,b)=1\) condition, and the raw inner squarefree index may meet \(d\). This is the exact long-tail identity needed for an arbitrary-row sieve or for a sieve restricted to sixth-power-free physical rows. The original \(q\) exclusion remains on both raw factor axes. The cube support makes the tail literally empty once \(R\) exceeds a fixed support constant times \(B^{1/3}\).

## 8. Relation to the A2 children and to the next raw estimate

In the exact A2 map, write its disjoint correction labels as \((c,d,e)\), with \(C=cde\), and starting parameters \(q_0,f_0\). Its children have

\[
q_t=q_0 C,\qquad f_t=e f_0,
\qquad (C,q_0f_0S)=1.
\tag{8.1}
\]

The correction labels are pairwise-coprime and squarefree. Since \((C,q_0f_0S)=1\), both \(q_t\) and \(f_t\) are squarefree, although they share the correction label \(e\).

Thus

\[
q_{t,*}=\frac{q_0}{(q_0,f_0)}cd,
\qquad
Nf_t=(Nf_0)Ne.
\tag{8.2}
\]

The overlap at \(e\) is removed exactly as a redundant exclusion, while its fourth-power auxiliary twist remains. The completed child's three label costs are therefore

\[
1,\quad
Nf_0\,N\!\left(q_0/(q_0,f_0)\right)\,(Nc)\cdot(Nd)\cdot(Ne),
\]

\[
(Nf_0)^{2/3}
N\!\left(q_0/(q_0,f_0)\right)^{1/3}
(Ne)^{2/3}\bigl((Nc)\cdot(Nd)\bigr)^{1/3}.
\tag{8.3}
\]

The outer inverse mask is allowed by Theorem 2.1. Consequently the exact A2-to-theta identity now has a proved stronger positive-norm input for every nonempty child, with explicit scale and label dependence. This does not imply that its sum is diagonal sized. In particular shortening \(B\), summing the correction labels, handling the adverse initial dual scale, and preserving the exact centered covariance remain separate analytic obligations.

There is another useful application. A sixth-power row decomposition \(k=v^6k_0\) gives exactly

\[
\mathscr P_{q,r}(A,B;v^6k_0,f)
=\mathscr P_{\operatorname{rad}(qv),r}(A,B;k_0,f),
\tag{8.4}
\]

with the fixed bad-prime conventions absorbed into the original finite data. The physical row height becomes \(H/(Nv)^6\), whereas the new exclusion norm grows at most by \(Nv\). Equations (2.2) and (7.2)–(7.6) make it possible to apply a sixth-power-free tail sieve at that smaller height and choose its inverse cutoff separately for each fixed \(v\). This note supplies the exact adapter; any optimized raw consequence must state and prove the separate cutoff and convergent-sector summation argument.

The remaining full-moment problem has not been converted into an unsigned bound. The established result here is the specified all-row completed estimate with moving labels and the exact finite inversions that preserve them.

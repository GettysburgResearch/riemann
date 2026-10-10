# Signed auxiliary reunion, stratified A2 norms, and mixed cubic replications

**Status: proposed, source-qualified component proofs with scoped mathematical reviews by separate agents. The full fourth moment, generalized moment hierarchy, and RH remain open.**

This research pass continues PR #921 at commit `4e6d4aa57ae4cb04d76b2b31279ac367951b469a`. It also uses specific frozen components from the adjacent PRs #917, #922, #923 and #924. The sources and every dependency level are recorded in [PROVENANCE.json](PROVENANCE.json). Those adjacent branches are mathematical sources, not an assertion that they have been integrated or externally accepted.

The main new step is an exact reunion of the **entire signed auxiliary sum**, including its strict off-diagonal. A second Poisson summation then restores the actual finite-order inverse coefficients. This gives a quantitative signed tail at every fixed moment order. A separate local calculation carries moving column exclusions through the theta completion and makes an actual A2 mean square available. Retaining all pair-overlap ideals inside physical cubic norms, then mixing integer replications, gives stronger higher-moment components. Combining both inverse scalar cancellations with the newly available sixth-power stratification also improves the full positive A2 energy to exponent 89/55 at square-root row height.

## 1. The objective and the exact remaining scale

For fixed smooth tests and finite-order Hecke datum \(\nu\), write the native inverse polynomial as
\[
A_u(D)=\sum_{(n,S)=1}\mu_K(n)\nu(n)\chi_n(u)W(Nn/D),
\qquad \chi_n(u)=(u/n)_6,
\]
over the Eisenstein field, with the fixed source primary generators and literal zeros at nonunits. All row sums include every nonzero element and all six units. The desired fixed-order moment estimate is
\[
M_{2k}(D,H)=\sum_{0<Nu\le H}|A_u(D)|^{2k}
\ll_{k,\epsilon} H D^{k+\epsilon}.
\tag{1.1}
\]
The source route begins with heights \(H=D^h\), \(h>1\), and has precise uniformity and finite-character coverage requirements. It does not permit treating an arbitrary coefficient vector as an inverse polynomial.

The source moment extraction, recorded at the pinned PR #923 in `SUBSET_PRODUCT_INCIDENCE.md` (6.5), gives the conditional strict zero-free boundary
\[
\Re s>\frac12+\frac{5h}{12k}+\frac{e}{2k}
\tag{1.2}
\]
from an appropriately uniform moment or signed scale-average estimate with excess \(D^e\), together with its named extraction and character-coverage inputs. A diagonal fourth moment with \(h\downarrow1\) would approach \(17/24\). A cofinal sequence with \(h/k\to0\) and \(e/k\to0\), under the full hypotheses, would approach RH. **This packet proves neither of those arithmetic premises.**

The first fourth-moment Poisson step has dual row height approximately \(D^{3-\theta}\), where the original height is \(D^{1+\theta}\). The positive two-axis bounds below concern substantially shorter useful dual ranges. The same letter H denotes the physical row height of each explicitly defined family; a bound at one height is not silently transported to another.

## 2. Exact signed reunion and a tail at every fixed order

The complete proof is [SIGNED_AUXILIARY_REUNION.md](SIGNED_AUXILIARY_REUNION.md).

Start with the exact signed off-diagonal of PR #914, `A2_COMPLETION.md` (6.3), and write
\[
d=(m_1,m_2),\qquad m_i=dz_i,\qquad w=fd.
\]
The actual cubic Gauss CRT converts all residual f-dependence into the local divisor sum
\[
\boxed{
\sum_{f\mid w}\mu(f)\mathbf1_{(k,w/f)=1}
=\mu(w)\mathbf1_{w\mid k}.
}
\tag{2.1}
\]
Thus every surviving row is \(k=wh\), with phase \(\chi_{z_1}(hw^5)\overline{\chi_{z_2}(hw^5)}\). There is no new restriction \((h,w)=1\). The primitive columns are coprime, and the strict off-diagonal is exactly the exclusion of the unit pair \((z_1,z_2)=(1,1)\).

Poisson summation in h gives a second exact identity. Its Gauss scalar is
\[
a_\xi(z_1)\overline{a_\xi(z_2)}\gamma(\chi_{z_1}\overline{\chi_{z_2}})
=\mu(z_1)\mu(z_2)\xi(z_1)\overline{\xi(z_2)}G(z_1z_2^{-1}).
\tag{2.2}
\]
The function G is on the source's **fixed finite ray group**. All angular factors cancel in the displayed identity. Its finite Fourier expansion restores native inverse coefficients at the row \(rw\), with the Schwartz weight \(\Phi(Nw\,Nr/H)\). The exact prefactor is \(1/L\).

For every fixed k, take the actual smooth squarefree convolution
\[
v_k(n;D)=\sum_{n_1\cdots n_k=n}
V(Nn_1/D,\ldots,Nn_k/D),\qquad L=D^k.
\]
Let \(\beta_{\rm f}\in(1/2,1]\) be the explicitly stated uniform finite-order inverse exponent. Counting gives \(\beta_{\rm f}=1\); stronger values require the separately named finite-order reciprocal input. The proved sharp tail is
\[
\boxed{
|\mathcal O_{\xi,\ge R}[v_k]|
\ll D^\epsilon H L^{2\beta_{\rm f}-1}R^{-2\beta_{\rm f}}.
}
\tag{2.3}
\]
The cutoff is \(Nw=N(f(m_1,m_2))\ge R\), retaining every original divisor partner. This is a signed component, not an estimate for an isolated original auxiliary annulus or an all-tuple common gcd.

| Input | General fixed-order cutoff giving \(O(HD^\epsilon)\) | Fourth-moment squarefree face |
|---|---|---|
| Counting, \(\beta_{\rm f}=1\) | \(R\ge D^{k/2}\) | \(R\ge D\) |
| Optional finite-order \(\beta_{\rm f}=7/8\) | \(R\ge D^{3k/7}\) | \(R\ge D^{6/7}\) |

The stronger bound uses cancellation in all \(2k\) primitive singleton axes after an exact \(k\times k\) allocation of the common product. Its coprimality correction has absolute local error \(O((Np)^{-2\beta_{\rm f}})\). The sharp w cutoff is legitimate because w is frozen during that cancellation.

On a complete smooth block \(Nb\asymp B\), \(Nw\asymp W\), \(Z=L/(BW)\), a second estimate cancels w itself and gives
\[
|\mathcal O_{B,W}|\ll D^\epsilon H
\min\{ZW^{\beta_{\rm f}-2},Z^{2\beta_{\rm f}-1}/W\}.
\tag{2.4}
\]
The two savings are alternatives; this proof does not multiply them.

## 3. Moving exclusions now enter the actual positive A2 norm

The local proof is [MOVING_COLUMN_MASKS.md](MOVING_COLUMN_MASKS.md); its arithmetic composition is [A2_MOVING_MEAN_SQUARE.md](A2_MOVING_MEAN_SQUARE.md).

For squarefree original exclusion \(q_0\) and fourth-power auxiliary f, the exact row identity is
\[
P_{q_0}(k;f)=P(kf^4q_0^6).
\tag{3.1}
\]
The sixth power keeps the zero at every deleted prime. It also deletes that prime from the physical cube index and inverse-cube coefficient. Overlapping primes of f and \(q_0\) must be counted only once. Set
\[
q=q_0/(q_0,f),\qquad
J=Nf\,Nq,\qquad K=(Nf)^{2/3}(Nq)^{1/3}\le J^{2/3}.
\tag{3.2}
\]
The new local calculation uses the actual active factor
\(B_{p,0}(x)=(Np)^{-1/2}\chi_p(x)^{-2}\). A deleted prime has costs \((1,Np,(Np)^{1/3})\) in the three existing energy monomials. A fourth-power auxiliary prime has costs \((1,Np,(Np)^{2/3})\). All positive physical row valuations, inactive branches and overlaps are included before these factors are multiplied.

Let \(\beta_{\rm a}\in(1/2,1]\) be the separate angular scalar exponent and \(\delta=(2\beta_{\rm a}-2)/3\). The source-conditional example is \(\beta_{\rm a}=11/12\); this is not the finite-order exponent from Section 2. For the normalized full arithmetic A2 polynomial \(\mathscr Q\), put \(m=\min(A,B)\), \(M=\max(A,B)\). The resulting complete bound is
\[
\boxed{
\sum_{0<Nk\le H}|\mathscr Q_{q_0}(A,B;k,f)|^2
\ll D^\epsilon[Hm+JH^2m^{1+2\delta}M^{-\delta}
 +KH^{4/3}m^{4/3}M^\delta].
}
\tag{3.3}
\]
This is the six-point A2 local coefficient system of the source, not the raw squarefree Gauss coefficient used on nonsquarefree products.

The exact A2 child scales are
\[
A'=A/(xy^2z^2),\quad B'=B/(x^2yz^2),
\quad x=Nc,\ y=Nd,\ z=Ne,
\]
with normalized correction weight \(1/(xyz^{3/2})\) and exact child costs
\[
J'=Jxyz,\qquad K'=K(xy)^{1/3}z^{2/3}.
\tag{3.4}
\]
Choosing the smaller child axis before applying the raw bound is essential. It makes the correction summable for the complete range \(\beta_{\rm a}>1/2\). No column-deletion contraction of a native moment is assumed.

## 4. Sixth-power stratification transfers both scalar savings through the full A2 sum

The strongest positive-energy result is [STRATIFIED_TWO_SCALAR_A2.md](STRATIFIED_TWO_SCALAR_A2.md). It combines this packet's two actual Möbius scalar cancellations with the adjacent [PR #924](https://github.com/GettysburgResearch/riemann/pull/924) row stratification. For either the normalized raw balanced P or the complete arithmetic A2 polynomial \(\mathscr Q\), and every \(R>0\), it proves
\[
\boxed{\begin{aligned}
E(D,H)\ll D^\epsilon\big[&HD
+JH^2D^{\beta_{\rm a}-1/2}R^{5/2-\beta_{\rm a}}
+KH^{4/3}D^{2/3}R^{2\beta_{\rm a}}\\
&+H+D^2R^{-3}+H^{2/3}D^{4/3}R^{-2}\big].
\end{aligned}}
\tag{4.1}
\]

Three details are responsible for the gain. First, the short inverse retains cancellation in both the negative-allocation scalar and the inverse-cube scalar; a final completed-norm inequality alone would not justify this. Second, write each physical row exactly as \(k=\varepsilon v^6k_0\), where \(k_0\) is sixth-power-free and may meet v. Its physical height is \(H/(Nv)^6\), and v inserts the original column mask with costs \(J_v\le JNv\), \(K_v\le K(Nv)^{1/3}\). A separate capped cutoff on each stratum makes these costs summable and removes the generic \(H^{1/6}\) long-tail loss. Third, every arithmetic A2 child uses
\[
R_t=R(B_t/D)^\tau,\qquad
\tau=\frac{3-2\beta_{\rm a}}{5-2\beta_{\rm a}}.
\tag{4.2}
\]
At \(\beta_{\rm a}=11/12\), this is \(\tau=7/19\).

The smooth cutoff equals one on \([0,1/2]\) and zero on \([1,\infty)\). Consequently a child cutoff at most one has an exactly empty short part; a doubled physical support cap makes the long part exactly empty. This allows the actual child cutoff to stay below one where required. The critical A2 norm weights become exactly \(x^{-1}y^{-3/2}z^{-2}\). The other five rows converge or have only the explicitly retained harmonic sums. The entire correction sum is therefore controlled without an independent cutoff on \(N(cde)\).

At the source-qualified \(\beta_{\rm a}=11/12\), both positive families satisfy
\[
\boxed{
E(D,H)\ll D^\epsilon
\max\{D^{34/29}H^{24/29}K^{18/29},
D^{53/55}H^{72/55}J^{36/55}\},
\qquad JH^2\le D^{19/12}.
}
\tag{4.3}
\]
In particular, at \(q_0=f=1\), \(H=D^{1/2}\), choose \(R=D^{7/55}\). Then
\[
\boxed{E(D,D^{1/2})\ll D^{89/55+\epsilon}.}
\tag{4.4}
\]
The six exponents are \(3/2,89/55,47/30,1/2,89/55,233/165\), so the largest is verified by exact arithmetic.

| Specified positive family and method | Energy exponent at \(H=D^{1/2}\), unit labels |
|---|---:|
| PR #924 raw and full A2, one-scalar stratified inverse | \(31/19\approx1.63158\) |
| This packet, raw and full A2, two-scalar stratified inverse | \(89/55\approx1.61818\) |

The strict improvement over the adjacent result is \(14/1045\). Both retain their stated theta and angular inputs; the additional cancellation used here is the second actual inverse scalar. The sufficient positive-energy range is \(H\le D^{19/24}J^{-1/2}\). This is a physical row range, not a zero-free boundary.

For auditability, [HYBRID_CUBE_INVERSE.md](HYBRID_CUBE_INVERSE.md) and Section 6 of [A2_MOVING_MEAN_SQUARE.md](A2_MOVING_MEAN_SQUARE.md) preserve the earlier valid unstratified estimates. Their respective exponents \(1087/660\) and \(2399/1428\) are superseded by (4.4). The earlier proof's extra A2 cutoff cost is real for that proof; the new length-adapted argument is what removes it. At scalar counting \(\beta_{\rm a}=1\), the two scalar powers coincide with the one-scalar powers, so no strict improvement over PR #924's counting exponent is claimed.

## 5. Joint cubic pair ideals give a stronger higher-moment region

The full proof is [HIGHER_CUBIC_POOLS.md](HIGHER_CUBIC_POOLS.md).

In the ordinary k-fold inverse product, freeze only incidence ideals involving three or more positions. Keep all pair ideals inside one physical cubic product. If R is the product of their dyadic scales, \(X_i\) are the remaining singleton scales, \(X=\prod_iX_i\), and T is the higher-incidence multiplicity weight, then
\[
R^2XT=D^k.
\tag{5.1}
\]
The mixed coprimality correction is exact for singleton coefficients \(\mu\) and pair coefficients \(\mu^2\). At each unmasked prime its nonconstant coefficient is
\[
(1-|\operatorname{supp}\mathbf e|)\prod_j(-s_j)^{e_j},
\qquad s_j\in\{-1,+1\}.
\tag{5.2}
\]
This correction is summable with a finite supported horizon at weights at least \(1/2\). The theorem does not assert absolute convergence at the critical weights.

Put \(a=2\beta_{\rm f}-1\) and
\[
\rho_q(H,R)=R^{-q}+H^{-2/3}+H^{-1/3}R^{-q/3}.
\]
Classical cubic large sieves and the stated pointwise input give the energy bound
\[
\|F_{\mathbf c,\mathbf R}\|_{2,H}^2
\ll H D^{k+\epsilon}T^{-1}X^a\rho_1(H,R).
\tag{5.3}
\]
At counting \(\beta_{\rm f}=1\), no native second moment or imported zero-free input is used. If the separate native second moment is available, each fixed integer \(q\ge2\) gives the further option
\[
\boxed{
\|F_{\mathbf c,\mathbf R}\|_{2,H}^2
\ll H D^{k+\epsilon}T^{-1}
X^a X_{\max}^{-a(1-1/q)}\rho_q(H,R)^{1/q}.
}
\tag{5.4}
\]
Its higher \(2q\)-norm is a classical physical cubic-product estimate, not a presumed higher inverse moment. q is fixed independently of D. The proof also gives an explicit Hermitian version retaining one full and one interpolated native odd axis.

Two strict sixth-moment consequences are useful benchmarks:

* With three pair ideals of norm scale \(D^r\), triple ideal one, \(H=D^{21/20}\), counting alone proves diagonal energy for the complete triangle portion when \(r\ge23/60\). The prior frozen-pair classical criterion required \(r\ge33/80\).
* On PR #923's specific triangle \(r=5/24\), singleton scale \(D^{7/12}\), under its optional \(\beta_{\rm f}=7/8\) and native-second-moment inputs, the integer \(q=2\) estimate lowers the excess from \(623/720\) to \(119/160\). The additional mixed-replication argument below lowers it further to \(863/1200\).

The further proof [MIXED_CUBIC_REPLICATION.md](MIXED_CUBIC_REPLICATION.md) uses actual integer monomials before Hölder. For three pair polynomials set
\[
P_1=U_1U_2^2U_3^2,\quad
P_2=U_1^2U_2U_3^2,\quad
P_3=U_1^2U_2^2U_3.
\]
Their product is \((U_1U_2U_3)^5\), so
\[
\|U_1U_2U_3\|_{10/3,H}
\le\prod_{j=1}^3\|P_j\|_{2,H}^{1/5}.
\tag{5.5}
\]
Each right-hand side uses a genuine five-factor classical cubic-product norm. One native singleton uses its L5 estimate interpolated from its declared L2 and pointwise inputs. The unequal shortened pair scales are handled before the exact coprimality correction: all 27 norm monomials give pair weights at least \(1/2\).

For the complete triangle at the stated scales this proves
\[
\boxed{\|F_\triangle\|_{2,H}^2
\ll HD^{3+863/1200+\epsilon}.}
\tag{5.6}
\]
The gain is \(59/2400\) over the integer \(q=2\) result and \(263/1800\) over PR #923. The excess is still positive, so this is a stronger complete component, not the full diagonal sixth moment.

More generally, s pair factors and fixed integer cyclic replications of total degree d at least s supply a legitimate rational grid \(q=d/s\) when the original pair scales agree. The actual theorem first handles unequal scales with their individual product norms, so equality is not imposed after arithmetic shifts. The specific degree five is optimal at the displayed triangle within the stated direct integer-monomial Hölder method. The tempting formal real-q value \(23/32\) is lower by \(1/2400\), but is not proved by interpolating the old scalar estimates.

The new selector can be summed over every higher-incidence configuration: the higher ideals have norm weights \((Nc_I)^{-|I|/2}\), which converge for \(|I|\ge3\), and pair dyads cost logarithms. This gives a complete general-order peripheral theorem, with a uniform threshold and every overlap inside the positive norm retained.

## 6. A retained spectral baseline with the original moving exclusion

[ALL_ROW_SPECTRAL_MEAN.md](ALL_ROW_SPECTRAL_MEAN.md) extends the canonical Gauss-series estimate of PR #922 to every element row and to the original moving exclusion. For
\[
G_{k,d;q_0}(u)=\sum_{(n,Sq_0)=1}^{*}
\frac{a_\xi(n)\chi_n(k)\chi_n(d)^4}{(Nn)^u},
\qquad J_0=Nd\,N(q_0/(q_0,d)),
\]
the proved source-conditional estimate on strict interior strips is
\[
\sum_{k\sim H}|G_{k,d;q_0}(a+it)|^2
\ll H^{1+\epsilon}J_0^{1-a+\epsilon}(2+|t|)^M,
\qquad 5/8<a<1.
\tag{6.1}
\]
The completed family has the same estimate. The exact cube reciprocal is in its absolutely convergent Euler half-plane, so this deduction uses no new zero-free premise. It retains the named imported theta mean square and classical sieve inputs.

The all-row cubic-copy term changes one crossover to \(X=H^{11/12}J_0^{1/2}\), with threshold \(a>6/11\). The other crossover still requires \(a>5/8\), so the sufficient spectral threshold is unchanged. This mean for the canonical family does not automatically identify the entire arbitrary-row second-reflection cusp family. The subsequently available PR #924 separately gives a stronger sufficient threshold 4/7 using the additional primary input of Alexandre de Faveri, [Optimal large sieve for fixed order characters, arXiv:2610.04045v1](https://arxiv.org/html/2610.04045v1). The 5/8 result preserved here is the independently audited baseline with its original input set; it is not presented as the latest strongest spectral threshold. The new exponent 89/55 in Section 4 uses the classical sixth-power-free sieve and does not require that newer large-sieve theorem.

## 7. What remains to prove

The new signed tail gives an exact smaller target:
\[
\mathcal O_\xi[v_k]=\mathcal O_{\xi,<R}[v_k]+O(HD^\epsilon)
\]
at the cutoff in Section 2. At \(b=w=1\), however, the primitive columns still have product length \(L=D^k\). The second Poisson identity is reversible; it does not supply a conductor reduction for this leading term.

[SMALL_W_CORE_AUDIT.md](SMALL_W_CORE_AUDIT.md) carries the complete divisor reunion one step further. Set \(g=bw\), \(s=wr\). Then
\[
\sum_{w\mid g}\mu(w)\mathbf1_{w\mid s}=\mathbf1_{(s,g)=1},
\]
and the entire signed expression returns exactly to a fixed finite linear combination of native centered energies:
\[
\mathcal O_\xi[v]=\frac1L\sum_\eta c_\eta\sum_{s\ne0}\Phi(Ns/H)
\bigl(|B_{\xi\eta,v}(s)|^2-\Delta_v(s)\bigr).
\tag{7.1}
\]
The proof gives the exact inverse coefficients and diagonal; no sign or positivity of the finite coefficients is assumed. On each complete block it also supplies the valid ambient-height adapter
\[
|\mathcal O_{B,W}|\ll HD^\epsilon
\min\{Z^{(2\beta_{\rm f}-1)(1-1/k)},Z^{2\beta_{\rm f}-1}/W\}.
\tag{7.2}
\]
It applies the native M2 to rows divisible by w at height H, with the loss of row density explicit.

[SMALL_W_POSITIVE_CUTOFFS.md](SMALL_W_POSITIVE_CUTOFFS.md) updates the method diagnosis for cutoffs below one. It optimizes the two competing terms of the displayed positive envelope over every \(R>0\), and distinguishes that calculation from any potential improvement using exact empty strata. Its statements are limits of the specified upper bounds, not lower bounds on the arithmetic energy or impossibility results for other methods.

In the completely coprime balanced one-sided core, R and all higher ideals are one, while \(X_i=D\). Every finite-q cubic-pool option is at least the old native-second-moment cost \(D^{(2\beta_{\rm f}-1)(k-1)}\). The missing saving therefore remains proportional to k. These component improvements do not make the excess in (1.2) sublinear in k.

Two tempting shortcuts are explicitly excluded by the proofs. The restored character at the shorter row r is \(\chi_z(rw)\), so a native mean at height \(H/Nw\) needs an additional theorem uniform in the moving twist w. Also, independently A2-corrected columns must still be centered at equality of the reconstructed product columns. A positive A2 mean square supplies neither operation.

The next arithmetic target is cancellation in this small-w primitive covariance at the original long dual height, or an independently proved signed scale-average of the exact remaining higher-moment portion with excess \(e_k=o(k)\). Those are open estimates, not consequences of the finite checks.

## 8. Review and reproducibility

[VALIDATION.md](VALIDATION.md) identifies the reviewed hashes, exact finite checks, negative controls and unreplayed analytic inputs. The executable diagnostics are under [checks](checks); their generated reports are under [results](results). They cover actual small Eisenstein residue masks where stated, formal CRT-compatible Gauss phases where stated, exact finite coefficient identities and rational exponent calculations. Normal Python and optimized Python runs are compared byte for byte.

The scoped agent reviews are mathematical audits of the stated component arguments. They are not external peer review, a Lean build, or a new independent proof of the entire imported canonical theorem. This standalone packet does not change the repository's integrated mathematical status.

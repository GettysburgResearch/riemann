# A small improvement from a perturbed compensated probe

**Status:** complete conditional deduction from the explicitly listed imported analytic machinery, 2026-10-10. The new low-side inequality and exponent calculations have received an independent source check within this research pass. This is not an independent verification of the full upstream proof and is not a Lean-checked theorem.

**Scope:** all finite-order Hecke characters of \(K=\mathbb Q(\sqrt{-3})\), followed by the imported transfer to Dirichlet characters. The conclusion is a constant zero-free boundary. No height-dependent curve or approach to \(1/2\) is claimed.

**Exact source:** the September 30 manuscript in the published research import, upstream commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`, at

`standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`.

The root agent verified that this manuscript is unchanged at upstream `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`. Below, **S** denotes this source, with its exact ideal conventions, primary generators, bad-prime zero extensions, finite ray presentations, and physical row restrictions. In particular, a sixth-divisible exponent does not remove the source's zero extension on nonunits.

**What was actually run:** direct inspection of the source's reflected-energy calculation, low-side separation, local Euler formulas, contour interfaces, moment selection, and endpoint certificate; exact rational arithmetic; independent checking of the changed low-side calculation and endpoint algebra. No full upstream proof audit or Lean kernel build was run in this pass.

**Dependence statement:** the theorem below is an implication from the imported analytic statements. It contains no new unproved moment estimate. Its new ingredients are the variable-geometry low bound, an explicitly enlarged principal Euler region, fixed-\(\kappa\) reuse of the row count, and the resulting contour/normalization instantiation.

## 1. Conditional theorem and imported dependencies

### Theorem 1.1

Assume the imported analytic machinery listed below is valid, with the uniformity and exact coefficient restrictions stated in S. Then every finite-order Hecke \(L\)-function over \(K\) has no zero in

\[
\boxed{\Re s>\beta_0:=\frac{139999}{160000}=0.87499375.}
\tag{1.1}
\]

The principal pole at \(s=1\) is allowed. The same zero-free half-plane holds for all Dirichlet \(L\)-functions, including \(\zeta\), by the imported transfer. The line \(\Re s=\beta_0\) is not included in the conclusion.

The improvement over the imported \(7/8\) boundary is

\[
\frac78-\beta_0=\frac1{160000}.
\]

It is small but uses the existing moments. It does not rely on a hypothetical Möbius fourth moment or on a new height saving.

The principal Mellin exponent stays **exactly** \(C(s)=s-11/16\). The concrete change is a smaller bound for the same type of normalized physical probe:

\[
|J_\eta(Z)|\ll_{\eta,\epsilon}
Z^{\,3/16-1/160000+\epsilon}.
\tag{1.2}
\]

Thus the gain is in the direct arithmetic estimate, rather than in a relabeling of its comparison exponent.

### Imported dependency ledger

The proof uses these statements as inputs; their full arithmetic proofs are not reproduced here.

| Imported input | Source label / location | What is used |
|---|---|---|
| Existing finite-order Hecke \(7/8\) theorem | `thm:main`, lines 106 onward | The starting bound \(\beta_*\le7/8\). |
| General continuation criterion | `lem:continuation-criterion`, lines 400–507 | A common positive low/high margin implies \(\beta_*\le\sigma_0\), for any \(1/2<\sigma_0<1\). |
| Admissible physical probe and its exact separation | `eq:general-probe`, `eq:low-separated`; Sections 6–7 and 12 | The same physical expression is estimated on its low and high sides. |
| Full local Euler identity | `lem:local-euler`, lines 4007–4193 | Exact rational local formulas, including all ramified valuations and zero extensions. Its analytic domain is extended explicitly below. |
| Quotient-free compensated high identity | `eq:compensated-probe-definition`, `eq:compensated-poisson-identity`, `eq:holomorphic-selected-tuple`; lines 6898–6915 and 8684–8771 | The finite slot operation and the exact full correction before contour-dependent decomposition. |
| Reflected marked energy | `lem:reflected-energy`, lines 7747–7820, and its proof | The general bounded-length formula for \(E_{\rm ref}\), with actual row dyads, independent coefficients, common profiles, and permitted masks. |
| Additive Gram estimate | `prop:probe-gram`, lines 8340 onward | \((Q/Y')[1+P_a^{1/6}+P_a^2/Y']\), with finite height cost. |
| Buffered detector and saturated pair | `lem:buffered-bins`, `lem:detector-dyads`, `prop:detector-witness` | The same-character, common-frequency inverse/plain witnesses, with their uniform height and smooth-profile bounds. |
| Marked inverse, no-slot amplification, and plain fourth moments | `lem:marked`, `lem:inverse-amplification`, `lem:plain` | Their original coefficient classes and fixed strict capacity margins; the plain theorem is used only at \(\kappa=3/4\). |
| Local dynamic compensation errors | `prop:probe-errors`, lines 8848 onward | Simultaneous conductor-deficit accounting for error slots. Its dynamic region is unchanged. |
| Smooth calculus and external/late tails | `lem:smooth-calculus`, `lem:external-contour-tails`, `lem:late-height-closure` | Finite internal height orders, independently adjustable external decay, and common positive exponent margins. |
| Hecke-to-Dirichlet transfer | `prop:hecke-dirichlet-transfer`, lines 6707 onward | Transfer at an arbitrary admissible boundary \(\sigma_0\), including treatment of the principal pole. |

The elementary ideal count and the fixed-ray prime normalizer used by S are also retained. No uniform prime theorem in a moving conductor is introduced.

## 2. Geometry, physical expression, and exact normalization

Put

\[
s_0=\frac1{40000},\qquad b=\frac18,\qquad
\ell=\frac16+s_0=\frac{20003}{120000},
\]

\[
l_x=\frac{1-\ell-b}{2}=\frac{84997}{240000},\quad
l_y=\frac{1-\ell+b}{2}=\frac{114997}{240000},\quad
h=1-l_x+\ell=\frac{65003}{80000}.
\tag{2.1}
\]

Thus \(M=l_x+l_y=1-\ell\). Define

\[
C(s)=s+\frac{l_x}{2}-1+\frac h6,
\qquad L_0=\frac{l_x}{2}+\frac b{12}.
\tag{2.2}
\]

An exact calculation gives

\[
C(\beta_0)=L_0,
\qquad \beta_0=1-h/6+b/12=11/12-\ell/4.
\tag{2.3}
\]

In fact the structural relations in (2.1) simplify the signal exponent to
\(C(s)=s-2/3-b/6=s-11/16\), independently of \(\ell\). Meanwhile \(L_0=3/16-s_0/4=3/16-1/160000\). Both identities are used without approximation below.

Choose a fixed finite slot system of total length \(\ell\), with the source's disjoint underlying prime windows, fixed identity-ray restriction, and nonnegative nonzero annular weights. The precise mesh and number of slots will be chosen after the real margins, before the target. For now let their lengths be \(\ell_i>0\), \(\sum_i\ell_i=\ell\), and put \(P_i=Z^{\ell_i}\).

For a primitive finite-order target \(\eta\), use the admissible arithmetic datum of S. The fixed bad-prime set \(S_\eta\) contains its conductor and the source's fixed exclusions; later fixed enlargement is permitted with the same calibration and ray group. All appearances of this set in the physical probe, high correction, omitted Euler factors, and normalizer refer to this same set.

Let \(I_{\eta;D}(X,Y,Z)\) be the source physical completed probe with the indicator \(1_{D\mid cn^3}\) inserted. Use exactly its original support and normalization. Define the finite compensated combination

\[
\begin{split}
I_{\eta,\ell}(Z)=
\sum_{(p_i)}\prod_i W_i(Np_i/P_i)
\sum_{J\subseteq\{1,\ldots,K\}}
(-1)^{|J|}(Np_J)^{-3/2}\overline{\eta(p_{J^c})}\,
I_{\eta;p_{J^c}}
\left(\frac{Z^{l_x}}{Np_J},\frac{Z^{l_y}}{Np_J},Z\cdot Np_{J^c}\right).
\end{split}
\tag{2.4}
\]

The prime windows remain at their original scales \(P_i\) in every summand. The expression is a finite combination of the source's convergent completed probes. It is not defined by a proposed high integral.

Changing \(\ell,l_x,l_y\) changes only these positive physical scales and slot lengths. The exact primewise operation proving the compensated Poisson identity is independent of their chosen exponents. It therefore gives the same triple-integral identity, with

\[
\mathcal W=X^{1/2-z}Z^{s+z-1}Y^{w-1}
e^{(s+z-1)^2}M(z)\widehat W_1(w),
\tag{2.5}
\]

and the source's full quotient-free correction \(\mathfrak H_{\eta,u,Z}\). The scalar factor is unchanged:

\[
\frac{\zeta_K^{S_\eta}(6z)L^{S_\eta}(w,\chi_\bullet(u))}
     {L^{S_\eta}(s,\eta\overline{\chi_\bullet(u)})}.
\tag{2.6}
\]

In particular, the target denominator is not replaced by a different family. Neither the physical expression nor its eventual principal signal contains the auxiliary height cutoff.

## 3. Explicit extension of the Euler and contour domains

The published second Euler region begins at \(7/8\). We prove the required extension, rather than using a published statement outside its hypotheses.

Fix

\[
\alpha_0=\frac{437}{500}=0.874<\beta_0,
\quad
\mathcal D_2'=\{\Re s\ge\alpha_0,\ \Re w\ge19/20,\ \Re z\ge33/200\}.
\tag{3.1}
\]

The first Euler region \(\mathcal D_1(\epsilon_0)\) remains exactly as in S:
\(\Re s\ge51/100\), \(\Re z\ge17/50\), \(\Re w\ge-1/100\), and \(\Re(s+w)\ge1+\epsilon_0\).

### Lemma 3.1. Local Euler product on the enlarged principal region

On \(\mathcal D_2'\), the exact source factors satisfy, uniformly in all imaginary parts and target unit phases,

\[
H_p-1\ll Q^{-907/500}\quad(p\nmid u),\qquad
H_p-1\ll Q^{-103/125}\quad(p\mid u),\qquad Q=Np.
\tag{3.2}
\]

The product \(\mathcal H_{\eta,u}\) is holomorphic on a neighborhood of every point of \(\mathcal D_2'\), is \(\ll_\epsilon(Nu)^\epsilon\), and on the principal row can be made to satisfy

\[
\sup_{\mathcal D_2'}|\mathcal H_{\eta,1}-1|\le1/2
\tag{3.3}
\]

by one fixed sufficiently large excluded cutoff, uniform in target unit phases.

**Proof.** Use the source's exact parameters

\[
V=Q^{-6z},\quad R=a_p^2Q^{4-6s-6z},\quad
D=\eta(p)\overline{\chi_p(u)}Q^{-s},\quad W=\chi_p(u)Q^{-w}.
\]

The denominators after simplification are only \(1-R,1-V,1-D\); all remain uniformly separated from zero. For example,
\(|R|\le Q^{301/100-6\alpha_0}<Q^{-1}\). For \(p\nmid u\), with \(\mathcal E_p=P_p^*+D\), the exact defect is

\[
H_p-1=\frac{D(V+W-VW)-VW+(1-V)(1-W)\mathcal E_p}{1-D},
\]

\[
|\mathcal E_p|\ll
Q^{4-6\Re s-6\Re z}+Q^{1-\Re s-\Re w-6\Re z}.
\]

The largest possible good-prime exponents are

\[
-\alpha_0-99/100,\quad -\alpha_0-19/20,\quad -97/50,
\quad301/100-6\alpha_0,\quad-\alpha_0-47/50.
\]

Their maximum is \(-907/500\). At a ramified prime \(D=W=0\). The complete six-valuation table in S gives positive decay exponents

\[
6\alpha_0-301/100,\quad\alpha_0-1/20,\quad\alpha_0+19/20,
\quad3\alpha_0-3/2,\quad3\alpha_0-21/20,
\quad4\alpha_0-2,\quad4\alpha_0-31/20,\quad6\alpha_0-3.
\]

Their minimum is \(103/125\). This proves (3.2). The good-prime majorant is summable by the ideal count. The ramified finite product has the source's divisor-product subpower bound. Slightly reducing the lower real bounds gives normal convergence on a neighborhood of each boundary point. Finally the principal prime tail is \(O(P_0^{-407/500})\); the elementary product inequality \(|\prod(1+a_p)-1|\le e^{\sum|a_p|}-1\) gives (3.3), and also nonvanishing of each retained principal local factor. \(\square\)

### Lemma 3.2. Selected correction and principal normalization

The source's full quotient-free selected-tuple correction is holomorphic on \(\mathcal D_2'\), with the all-height polynomial majorants required by `def:stage-high-data`. On the principal row,

\[
\mathcal B_p=G_p/H_p=-1+O(Q^{-437/500}),\qquad
|\mathfrak H_{\eta,1,Z}(s,w,z)|\ll Z^{\ell\Re z}.
\tag{3.4}
\]

These bounds are uniform in all imaginary parts, on fixed real boxes, and in target unit phases.

**Proof.** The full correction is a finite sum of products of the source's selected factors \(G_p\) and unselected factors \(H_p\). The rational formulas have the same controlled denominators as in Lemma 3.1. No quotient by an arbitrary possibly vanishing \(H_p\) is used to establish holomorphy. On any fixed real box each selected factor is bounded by a fixed power of \(Q\), so counting the fixed number of slots gives the required all-height polynomial majorant.

For \(u=1\), the exact cancellation identity gives

\[
|G_p+H_p|\ll
Q^{-\Re s}+Q^{-6\Re z}+Q^{4-5\Re s-6\Re z}+Q^{1-\Re w-6\Re z}.
\]

The four positive decay exponents are at least
\(\alpha_0,99/100,5\alpha_0-301/100,47/50\), whose minimum is \(\alpha_0\). Divide only on this principal region, where Lemma 3.1 gives a lower bound for \(H_p\). Hence \(G_p=O(1)\), and each annular selected slot has absolute mass
\(\sum_p|W_i(Q/P_i)|Q^{\Re z-1}=O(P_i^{\Re z})\).
Multiplication and the bounded unselected product prove (3.4). \(\square\)

### Lemma 3.3. Extended fixed-bin and exponent-accounting interfaces

Use the source's exact high data, replacing \(\mathcal D_2\) by \(\mathcal D_2'\), and let \(\alpha_0\le\sigma_0<\beta_*\le7/8\). Fix the source's positive buffer, bounded physical row exponents, and cumulative height allocation. For each source dynamic bin, the full integral moves to

\[
\Re s=a+16e,\quad\Re w=1-a-6e,\quad\Re z=z_0=17/50,
\tag{3.5}
\]

with external error \(O_{\eta,N}(Z^{B_\eta}T_1^{-N})\), where \(B_\eta\) and all internal height orders are fixed before \(N\).

If its retained pointwise amplitude/witness subdivisions have row count \(U^{R+\epsilon}(1+T_1)^A\), mean slot amplitude \(q\in[0,\delta/2]\), and \(U=Z^d\), then their combined original bin is bounded by

\[
Z^{C(\sigma_0)+E(d)+O(e+\epsilon+\vartheta)}(1+T_1)^{A'},
\]

\[
E(d)=a-\sigma_0+h(z_0-1/6)-a l_y-\ell/2+q\ell
      +d(R+\delta/2-z_0),\qquad \delta=2a-1.
\tag{3.6}
\]

The supremum over the actual pointwise subdivisions is taken before estimating the bin. No individual subdivision is asserted to have a separate holomorphic continuation.

**Proof adapter.** The fixed-bin contour proof of S uses \(\mathcal D_1\), unchanged here. Move from the absolute lines to \(s=\beta_*+20e,w=3,z=z_0\), then move the entire \(w\)-line, and finally only the retained \(s\)-segment. Throughout the last rectangle, \(\Re(s+w)\ge1+10e\), \(a\ge51/100\), and the source's buffered rectangle excludes reciprocal poles. Off the retained box the reciprocal stays global. On horizontal joins, use exactly the source's trace estimates and global majorants on any extended axis. These arguments do not use \(\sigma_0\ge7/8\); the actual lower bound needed for the principal rectangle is supplied separately by Lemmas 3.1–3.2.

On the retained contours the source's `prop:probe-errors` applies unchanged because its domain is \(51/100\le a\le1\). Its simultaneous conductor-deficit allocation yields the common factor
\(U^{\delta/2+O(e)+\epsilon}Z^{\ell(z_0-1/2)+q\ell+O(e+\vartheta+\epsilon)}\).
Multiplying the actual row count and the outside powers (2.5) and subtracting \(C(\sigma_0)\) gives (3.6). Finite subset counts and dyadic choices cost only the source's allocated powers. All real parameters remain in fixed bounded sets, so the coefficients of these losses and the fixed height orders retain their uniformity. \(\square\)

### Lemma 3.4. Extended principal-signal interface

Under Lemmas 3.1–3.2, define

\[
H_\eta(s)=\mathcal H_{\eta,1}(s,1,1/6),
\quad
c_{S_\eta}=\widehat W_1(1)M(1/6)
\bigl(\operatorname{Res}_{v=1}\zeta_K^{S_\eta}(v)\bigr)^2/6>0.
\tag{3.7}
\]

Put

\[
S_i(Z)=\sum_{p\in\mathcal P_i(Z)}W_i(Np/P_i)(Np)^{-5/6},
\quad
A_T(Z)=(-1)^KZ^{-\ell/6}\prod_iS_i(Z).
\tag{3.8}
\]

Then \(A_T(Z)\ne0\) for all sufficiently large \(Z\), \(|A_T(Z)|\asymp(\log Z)^{-K}\), and, for any fixed

\[
0<\mu<\frac{437}{500}\min_i\ell_i,
\tag{3.9}
\]

the normalized principal term \(\mathscr P_\eta\) satisfies

\[
\begin{split}
\frac{\mathscr P_\eta(Z)}{c_{S_\eta}A_T(Z)}-f_\eta(Z)
\ll_\eta{}&Z^{C(\beta_*)+(1+h)e-l_y/20+\epsilon}
+Z^{C(\beta_*)+e-h/600+\epsilon}\\
&+Z^{C(\beta_*)+e-\mu+\epsilon},
\end{split}
\tag{3.10}
\]

where

\[
f_\eta(Z)=\frac1{2\pi i}\int_{(2)}
Z^{C(s)}e^{(s-5/6)^2}\frac{H_\eta(s)}{L_K^{S_\eta}(s,\eta)}\,ds.
\tag{3.11}
\]

The signal is independent of \(T_1\), \(H_\eta\) is holomorphic on \(\Re s>\alpha_0\), and \(|H_\eta-1|\le1/2\) there.

**Proof adapter.** The source's fixed-ray prime normalizer gives

\[
S_i(Z)\sim\frac{P_i^{1/6}}{|T|\log P_i}
\int_0^\infty W_i(y)y^{-5/6}\,dy,
\]

with a positive leading constant. Deleting any fixed finite bad-prime set does not change this asymptotic. The exact principal slot factorization, valid by Lemma 3.2, gives at \(w=1,z=1/6\)

\[
\mathfrak H_{\eta,1,Z}(s,1,1/6)
=H_\eta(s)Z^{\ell/6}A_T(Z)(1+\mathcal R_{\eta,Z}(s)),
\quad |\mathcal R_{\eta,Z}(s)|\ll Z^{-\mu},
\]

uniformly on \(\Re s=\beta_*+e\). Nonnegativity of each slot weight justifies dividing its summed error by \(S_i(Z)\); the same fixed \(S_\eta\) is used throughout.

The source principal contour proof now lies in \(\mathcal D_2'\): move to \(s=\beta_*+e,w=1+e,z=1/6+e\), then move \(w\) to \(19/20\), and in its residue move \(z\) to \(33/200=1/6-1/600\). Only the two scalar poles are crossed. Their product is exactly \(c_{S_\eta}\); no extra residue factor is introduced. The unresidued integrals have losses \(-l_y/20\) and \(-h/600\) by direct substitution into the outside powers. The relative slot error is estimated on the global reciprocal line, giving the last term of (3.10). Move only the main integral right to \(\Re s=2\), using the holomorphy and global reciprocal estimates there. Gaussian decay and the source trace bounds justify all horizontal limits. This is (3.10)–(3.11), including principal targets whose reciprocal has a zero at one. \(\square\)

### Lemma 3.5. Extended small and large row bounds

Let \(\sigma_0\ge\alpha_0\), \(\beta_*>\sigma_0\), and retain the full correction of (2.4). For \(1\le U\le Z^{d_{\min}}\), the source's outer-row estimate becomes

\[
|\mathscr R_\eta(U;Z)|
\ll Z^{C(\beta_*)+h(z_0-1/6)-l_y/2+e+\epsilon}
U^{63/50+\epsilon}.
\tag{3.12}
\]

For \(v>2\) and all physical dyads,

\[
|\mathscr R_\eta(U;Z)|\ll
Z^{B_0+hv+\epsilon}U^{1+\epsilon-v},\qquad B_0=l_x/2+1+l_y.
\tag{3.13}
\]

Thus for every fixed \(\zeta>0\), the sum over \(U>Z^{h+\zeta}\) is bounded by
\(Z^{B_0+(h+\zeta)(1+\epsilon)-\zeta v+\epsilon}\).

**Proof adapter.** For small rows use \((\Re s,\Re w,\Re z)=(\beta_*+e,1/2,17/50)\). These paths lie in \(\mathcal D_1(1/3)\), since \(\alpha_0>5/6\). The selected good-prime errors have exponents
\(-\Re s,-51/25,49/25-5\Re s,-77/50\), all negative; the selected ramified boundary exponents after the source's \(Q^{\Re s}\) factor are
\(-1/2,3/2-2\Re s,2-3\Re s,3-5\Re s\), all at most \(1/2\). Hence the quotient-free tuple majorant remains \(U^\epsilon Z^{\ell z_0}\). The source's numerator strip bound contributes \(U^{3/5+\epsilon}\), counting contributes \(U\), and \(q_u^{-z_0}\) contributes \(U^{-17/50}\), giving \(63/50\). The reciprocal stays on its global line, including any bounded principal denominator row. The large-row argument uses the unchanged absolute lines \((2,2,v)\), so its proof and geometric summation are identical. \(\square\)

## 4. Variable-geometry compensated low bound

### Lemma 4.1. Completed-row norm with the rescaling penalty retained

Suppose \(M+\ell=1\), \(\ell>0\), and the physical lengths in (2.4) range over fixed compact positive intervals satisfying the required support conditions. For a fixed rescaled subset with total length \(d\), let \(M'=M-2d\), \(\ell'=\ell-d\), and let \(B_m^J\) denote exactly the source's marked completed-row factor. Then, for every \(\epsilon>0\),

\[
\sum_{0<Nm\ll Z^{M'}}|B_m^J(Z)|^2
\ll Z^{M'+(5\ell-1+d)_+/4+\epsilon}.
\tag{4.1}
\]

The constant is uniform in the rescaled prime tuple. All original source masks and coefficient-independence hypotheses are retained.

**Proof adapter with the changed algebra.** Apply the source's Gaussian annular partition and common-profile Fourier separation to the whole marked row, as in S, lines 8132–8207. Its tails are removed before separation, and the total weighted profile norms are summable. On a retained annulus the completed length is
\(N_*=1+\ell'+\theta_N\), with \(|\theta_N|\) as small as prescribed within the final power loss. No rescaling changes the central coefficient normalization.

Freeze the powerful row part of length \(O\) and the supported fixed part, and use actual residual row dyads of length \(H\). Write \(\Delta_H=M'-O-H\ge-o(1)\). The local data satisfy

\[
2A_0\le O+o(1),\quad N_0\le A_0,\quad z_a\le\ell',
\]

\[
T_d=2H+2A_0+2z_a-1-\ell'-\theta_N-N_0-3B_0.
\]

Because \(M'+\ell'-1=-3d\),
\(T_d\le H-3d+o(1)+|\theta_N|\).
On retained dual dyads, put \(y=v+3\ell_b+e_\lambda\le T_d+\epsilon_0\). The source's support gives \(v,\ell_b,e_\lambda\ge-o(1)\), hence \(\max(H,v+\ell_b)=H+o(1)+O(\epsilon_0+|\theta_N|)\).

Use the exact imported reflected-energy formula

\[
E_{\rm ref}=O/2+\max(H,v+\ell_b)-S_0-B_0+z_a-u-\ell_b-2e_\lambda/3
-\tfrac12(T_d-y)_+,
\quad u=\min\{v,z_a,(v+z_a)/3\}.
\]

If \(u=z_a\), it is at most \(M'-\Delta_H\), up to the allotted errors. Otherwise \(u\ge v/2-o(1)\), so

\[
u+\ell_b+2e_\lambda/3+(T_d-y)_+/2\ge T_d/4-o(1).
\]

The exact remaining saving identity is

\[
\begin{split}
O/2+\Delta_H+S_0+B_0+T_d/4
={}&\frac{2M'+2z_a-1-\ell'+2\Delta_H-\theta_N}{4}\\
&+\frac{2A_0-N_0+B_0+4S_0}{4}.
\end{split}
\]

Its second numerator is nonnegative. Using \(z_a\le\ell'\) gives in this branch

\[
E_{\rm ref}\le M'+\frac{1+3\ell'-2M'-2\Delta_H}{4}+o(1)+O(\epsilon_0+|\theta_N|).
\]

Both branch envelopes are decreasing in \(\Delta_H\), so their maximum at \(\Delta_H=0\) bounds the actual dyads up to the admitted errors. Since
\(1+3\ell'-2M'=5\ell-1+d\), this is (4.1). The common kernel amplitude is extracted before squaring and before positive row enlargement, exactly as required by the imported reflected-energy statement. The original proof's row-sector and prime-slot coefficient checks do not depend on the numerical specialization \(\ell=1/6\); all lengths here remain in its bounded ranges. Summing dyads, local choices and the Gaussian annuli with the prescribed small losses completes the proof. \(\square\)

### Lemma 4.2. Final low bound at the new geometry

For (2.1), every \(\epsilon>0\), and the same physical expression (2.4),

\[
|I_{\eta,\ell}(Z)|\ll_\eta Z^{L_0+\epsilon}.
\tag{4.2}
\]

**Proof.** At a fixed rescaled tuple of total length \(d\), write \(r_J=Np_J/Z^d\), bounded above and below by fixed positive constants. The exact separated lengths are

\[
X'=Z^{l_x-d}/r_J,\quad Y'=Z^{l_y-d}/r_J,
\quad Q=N(b_*)X'Y'\asymp Z^{M'},\quad
P_a=Y'^2/Q=N(b_*)^{-1}Z^b.
\]

For all \(0\le d\le\ell\), the smallest relevant positive lengths satisfy

\[
l_x-\ell>0,\quad M-2\ell=\frac{19997}{40000}>0,
\quad l_y-\ell-11b/6=\frac{19991}{240000}>0.
\tag{4.3}
\]

Hence \(P_a\ge1\), \(Q,Y'\ge1\) at a fixed sufficiently large threshold, and \(P_a^2/Y'\ll P_a^{1/6}\). The imported additive Gram estimate gives the row norm \((Q/Y')P_a^{1/6}Z^\epsilon\), with its fixed separated-height polynomial. Cauchy–Schwarz and Lemma 4.1 bound this tuple's unscaled separation by

\[
\ll (X')^{1/2}P_a^{1/12}
Z^{(5\ell-1+d)_+/8+\epsilon}.
\]

The integrated external Mellin profile absorbs the fixed height polynomial. Counting the rescaled tuples costs \(Z^{d+\epsilon}\), the scalar in (2.4) contributes \(Z^{-3d/2}\), and \((X')^{1/2}\) contributes \(Z^{-d/2}\) relative to \(X^{1/2}\). The total excess is

\[
f_\ell(d)=-d+(5\ell-1+d)_+/8.
\]

Its slopes are \(-1\) and \(-7/8\), so its maximum is \((5\ell-1)_+/8=0\), because our \(\ell<1/5\). Summing the fixed finite subset system proves (4.2). This step is the reason it is unnecessary to retain the source's stronger zero-loss row norm for each rescaled subset separately. \(\square\)

## 5. The same adaptive row count at fixed \(\kappa=3/4\)

Assume for contradiction

\[
\beta_0<\beta_*\le7/8,
\qquad \Delta_0=\beta_*-\beta_0>0.
\tag{5.1}
\]

The upper bound is the imported theorem. Use \(\kappa=3/4\) in the imported plain fourth moment. Its hypothesis \(\beta_*\le(1+\kappa)/2\) holds. The dynamic-bin ceiling gives \(\delta\le2\beta_*-1\le3/4\).

### Lemma 5.1. Baseline adaptive count without a capacity penalty

Let a source dynamic/amplitude bin of large retained sixth-power-free physical rows have \(1/50<\delta\le3/4\), \(q\in[0,\delta/2]\), and total available prime length exceeding \(7/37\) by a fixed positive margin. Put \(x=q/\delta\), \(\alpha=5/6\), and

\[
D_x=3-17x/9,\quad P_x=(2-8x/9)(1-x),\quad
\mathcal J=(\alpha-\delta)D_x+\delta P_x,
\]

\[
t=1+\frac{\delta P_x}{2\mathcal J},\quad
R_*=1-\delta+\frac{(\alpha-\delta)\delta P_x}{2\mathcal J}.
\tag{5.2}
\]

For every \(\epsilon>0\), a fixed capacity decrement and sufficiently fine fixed slot mesh give

\[
\#\mathcal B\ll U^{R_*+\epsilon}(1+T_1)^A.
\tag{5.3}
\]

All masks, common-character requirements, rowwise selected heights and profile hypotheses are those of the source. No \(\Delta/4\) loss occurs.

**Proof adapter.** The same-character saturated witnesses have inverse length \(r\) and plain length \(m\), with \(r+m\ge t-o(1)\), \(r\le t+o(1)\), \(m\le1/2+o(1)\). With the fixed \(\kappa=3/4\), their positive prime capacities are exactly

\[
z_M(r)=(1-r)/2,\quad z_P(m)=2(1-2m)/9.
\]

The selected inverse and plain counts are respectively

\[
A_I(r)=1-\delta\{x+(1-x)r\},\quad
S_t(r)=1-\delta\{4x/9+(2-8x/9)(t-r)\}.
\]

Their crossing is the source's \(r_*(t)\ge23/37\), with \(1/3\le t-r_*(t)\le1/2\). Thus the inverse capacity is at most \(7/37\); its second marked-width inequality has the same margin \(9/37\). The plain capacity is at most \(2/27\). Finite decrements handle the strict inequalities, the source's no-slot estimates handle the zero-capacity neighborhoods, and the same disjoint-window mesh handles rounding.

For \(r\ge1\), the source no-slot inverse amplification gives \(L(t)=1-\delta+(\alpha-\delta)(t-1)\); for \(m\ge1/2\), the plain no-slot fourth moment is enough. The short-count crossing is
\(1-\delta+\delta P_x(3/2-t)/D_x\). Choice (5.2) balances it with \(L(t)\), giving \(R_*\). The source's Sobolev treatment of the rowwise witness heights and dyadic parameters has a fixed polynomial height cost, not a dependence on the new proposed endpoint. The correction \(\Delta/4\) in the published second stage arose only from replacing a larger \(\kappa\) by \(3/4\). Here \(\kappa\) is already \(3/4\), so there is no such replacement. \(\square\)

## 6. Uniform high comparison at the new tuple

At \(d=h\), formula (3.6) with \(\sigma_0=\beta_0\), (2.1) and (5.3) gives

\[
E_{\ell,b}(h)=
-1/4+5\ell/4+b/6+\delta(1/2+\ell)+x\delta\ell-h(1-R_*).
\tag{6.1}
\]

### Lemma 6.1. Main endpoint margin

Uniformly on the larger rectangle \(0\le\delta\le5/6\), \(0\le x\le1/2\),

\[
E_{\ell,1/8}(h)\le-\frac{1073}{22032000}.
\tag{6.2}
\]

**Proof.** For \(\ell=1/6,b=1/8\), the source's exact compensated endpoint certificate gives \(E\le-49/440640\). The denominator \(\mathcal J\) is bounded below there, so all displayed formulas extend continuously to the closed rectangle. Since \(P_x\le D_x\), formula (5.2) gives \(R_*\le1\). Holding \(b\) fixed,

\[
\partial_\ell E=5/4+\delta(1+x)-(3/2)(1-R_*)\le5/2.
\]

Integrating this exact affine dependence from \(1/6\) to \(1/6+1/40000\) gives
\(-49/440640+1/16000=-1073/22032000\). \(\square\)

### Lemma 6.2. All other physical row ranges retain positive margins

With \(d_{\min}=1/100\), the source's floor, intermediate, small, extended moderate and large row ranges can all be covered with a common positive saving relative to \(C(\beta_0)\), or directly relative to \(C(\beta_*)\) for the small and principal remainders.

**Proof.** The quantitative comparisons are:

1. **Prime supply:** \(\ell/h\) increases with \(\ell\) at fixed \(b\), since its derivative is \((1+b)/(2h^2)>0\). Its original value \(8/39\) already exceeds \(7/37\). Also \(5\ell-h=1/48+(7/2)s_0>0\). Thus for a sufficiently small fixed \(\zeta>0\), the supply for \(1/2\le d\le h+\zeta\) still exceeds \(1/5>7/37\). Slot lengths in base \(U\) are at most twice their base-\(Z\) lengths.
2. **Moderate adaptive rows:** the frequency slope \(R_*+\delta/2-z_0\) is positive because \(R_*\ge1-\delta\) and \(\delta\le5/6\). Therefore (6.2) bounds every \(1/2\le d\le h\). The source's uniform slope upper bound two still applies, so extension to \(h+\zeta\) costs at most \(2\zeta\).
3. **Floor:** the source's floor \(\delta_0=1/50\), count \(R=1\), and \(q\le\delta_0/2\) give the old endpoint \(-7/1200\). Its geometric derivative is at most \(5/4+3\delta_0/2=32/25\). Hence the new floor margin is at least \(7/1200-(32/25)s_0>0\). Its frequency slope is positive, and the same small extension is permitted.
4. **Intermediate rows:** for \(d_{\min}\le d\le1/2\), select no primes and use the source's common count \(R=76/75-2\delta/3\), including the floor. The slope in \(d\) remains positive. At \(d=1/2\), the old estimate is at most \(-49/14400\). The derivative of (3.6), including the change in \(\beta_0\), is \(13/50+\delta/4+q\le177/200\). Thus the new margin is at least \(49/14400-(177/200)s_0>0\).
5. **Small rows:** Lemma 3.5 has geometric exponent \(h(z_0-1/6)-l_y/2\), whose derivative is \(51/100\). With the source's conservative bound \((63/50)d_{\min}<2d_{\min}\), the old margin \(63/800\) becomes at least \(63/800-(51/100)s_0>0\), relative directly to \(C(\beta_*)\).
6. **Large rows:** fix the preceding positive \(\zeta\) and then take \(v=z_\infty\) sufficiently large in Lemma 3.5. The coefficient of \(v\) in the final exponent is \(-\zeta\), so any fixed desired saving is available.

All numerical margins in items 3–5 are greater than the main margin in (6.2). Choose \(\zeta\) smaller than a fixed fraction of that main margin and than \(5\ell-h\). The finite real losses and all slot/detector rounding costs can then be reserved as in Section 7. \(\square\)

## 7. Order of choices and completion of Theorem 1.1

Suppose (5.1) holds. The geometry and \(\Delta_0>0\) are fixed before the target. Let \(m_E=1073/22032000\). The error-free low margin is \(\Delta_0\); the moderate high comparison has at least \(m_E\) relative to \(C(\beta_0)\), and hence at least that much relative to \(C(\beta_*)\). The small-row and principal margins have already been identified separately.

Choose a preliminary real error budget smaller than fixed fractions of \(m_E\) and \(\Delta_0\). Choose the inverse capacity decrement, plain moment loss, and output losses first, and then the source's uniform plain-slot mesh at \(\kappa=3/4\). Choose a fixed even integer \(K\) so large that \(2\ell/K\) is below that mesh, the required spike-rounding allowance and \(1/185\). Set \(\ell_i=\ell/K\), and choose \(K\) disjoint compact annular windows inside \((1,2)\), each with a nonnegative nonzero smooth weight. As in S, these windows are disjoint before any row, ray, or bad-prime restrictions are imposed.

The source's centered amplifier pool remains disjoint from the physical windows: its fixed pool exponent exceeds the chosen slot mesh by the same positive gap as in the published proof. The actual annular norm ratios change lengths by \(O_K(1/\log U)\), which are absorbed by the fixed capacity/supply margins after increasing the lower threshold. No vanishing strict margin is used at a zero-capacity endpoint; those neighborhoods use the unweighted estimates in Lemma 5.1.

With this fixed slot system choose

\[
\mu=\frac{437}{1000}\frac\ell K>0,
\]

which satisfies (3.9). The normalizer is eventually nonzero by (3.8). Reserve positive fractions of the principal margins \(l_y/20\), \(h/600\), and \(\mu\). Choose the amplitude width, bin buffer \(e\), remaining real losses and normalizer subpower allowance sufficiently small to fit all these reservations. Choose the frequency extension \(\zeta>0\) small enough that \(2\zeta<m_E/8\), and then choose the large-row line \(z_\infty\) as in Lemma 6.2. These are all target-independent real choices. The fixed cutoff for (3.3) is chosen using the uniform local majorant; adding the target conductor and any further source-required fixed exclusions to \(S_\eta\) only shortens that positive tail majorant.

Now fix a target \(\eta\), choose its source admissible arithmetic datum and final excluded set, and use them consistently in (2.4), (2.6), (3.7)–(3.11). All internal moment, Sobolev and smooth-profile orders are finite and fixed at this point, uniformly in the moving rows and frozen labels admitted by the source. Let their total retained height cost be \((1+T_1)^{A_\eta}\). The external decay order has not yet been chosen.

Define

\[
J_\eta(Z)=\frac{I_{\eta,\ell}(Z)}{c_{S_\eta}A_T(Z)}.
\]

Lemma 4.2 and the subpower normalizer bound give, with the chosen low loss,

\[
|J_\eta(Z)|\ll_\eta Z^{C(\beta_0)+\Delta_0/2}.
\tag{7.1}
\]

Lemmas 3.3–3.5 and 6.1–6.2, together with the preceding reservations, give some common \(m>0\), independent of \(\eta\), and finite target-dependent \(A_\eta,B_\eta\), such that for every external order \(N\),

\[
|J_\eta(Z)-f_\eta(Z)|
\ll_{\eta,N}Z^{C(\beta_*)-m}(1+T_1)^{A_\eta}
             +Z^{B_\eta}T_1^{-N}.
\tag{7.2}
\]

The principal error terms from (3.10) and the small/large row bounds are included in the definition of \(m\). The constants \(A_\eta,B_\eta\) are independent of \(N\), because extra external integration by parts does not differentiate the internal arithmetic estimates.

Choose \(T_1=Z^{\tau_\eta}\), with \(\tau_\eta>0\) below every source detector/Sobolev allowance and below \(m/[4(A_\eta+1)]\). Then choose \(N\) so large that \(B_\eta-N\tau_\eta<C(\beta_*)-m/2\). The source's late-height closure, whose allowed \(\sigma_0\) is any number in \((1/2,1)\), gives

\[
|J_\eta(Z)-f_\eta(Z)|\ll_\eta Z^{C(\beta_*)-m/2}.
\tag{7.3}
\]

Both \(J_\eta\) and \(f_\eta\) are independent of this auxiliary cutoff. Their fixed-data lower threshold may depend on \(\eta\).

Finally, \(H_\eta\) is holomorphic and within \(1/2\) of one on \(\Re s>\beta_0\) by Lemma 3.1, since \(\beta_0>\alpha_0\). Equations (7.1) and (7.3) meet the general continuation criterion with \(\sigma_0=\beta_0\), common \(\omega=\Delta_0/2\), and common \(\sigma=m/2\). This contradicts \(\beta_*>\beta_0\), without assuming the supremum is attained. Therefore \(\beta_*\le\beta_0\).

The imported Hecke-to-Dirichlet transfer now gives the stated assertion for all finite-order characters and all Dirichlet \(L\)-functions. Its principal pole treatment is unchanged because \(\beta_0>1/2\). This proves the conditional theorem. \(\square\)

## 8. Review boundary

The new theorem is conditional on the imported machinery in Section 1. The proof above completes the extra work needed to vary its geometry: it does not assume an undefined “continuity of the proof,” use \(\kappa<3/4\), discard target rows, replace the physical probe, or infer a zero-free improvement from a fixed-height constant.

The most important new step is (4.1)–(4.2): the altered per-subset row norm is carried through the compensating rescaling instead of being required to have no loss separately. The main endpoint margin then pays for a concrete increase in total prime-slot length.

This deduction should be reported as a **new conditional corollary of the imported analytic framework**, with its dependency ledger, rather than as an independently verified breakthrough on RH. No Lean realization or build of this perturbed theorem has been supplied. The separate higher-moment and finite-height research notes identify additional routes that would require genuinely stronger inputs for a dramatic improvement.

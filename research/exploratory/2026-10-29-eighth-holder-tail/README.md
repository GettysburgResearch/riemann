# Eighth-moment Hölder tail with divisor rescaling

**Status.** This is a source-qualified reduction, not an individual zero-free theorem. The source identities, reciprocity calibration, fixed-ray partitions and uniform smooth-profile/Fourier bounds are those listed in [the sixth/third Hölder note](../2026-10-29-sixth-third-holder-tail/README.md). The new divisor-rescaling lemma below is exact under those inputs. The eighth-prefix scalar application has an exact rational vertex certificate; the tenth-prefix extension has an exact rational dual certificate. Both received independent internal audits. External analytic sources and their physical calibration remain explicit inputs.

## Input and notation

Fix dyadic scales \(B,K,F,D\ge1\). The actual set of sixth-free good row labels \(b\) has norm \(\asymp B\); \(k\) is fixed with norm \(\asymp K\). All finite ray sectors, common twists, local deletion masks and bounded row multipliers are retained. Write \(P_b(D;f)\) for the normalized squarefree theta polynomial in the source reduction, where the fixed good squarefree label \(f\) has norm \(\asymp F\). Source cube inversion writes it as a sum over good cube indices \(h\) of \(\mu(h)\bar\alpha(h)^3\xi(h)^3\chi_h(bk)^3\mathbf 1_{(h,f)=1}/Nh\) times a completed theta sum \(T_{bk}(D/(Nh)^3;f)\). Smooth weights and their logarithmic derivatives have uniform seminorms. All subsequent inequalities carry a harmless fixed-parameter factor \((YBDKF)^\epsilon\), suppressed below.

For \(x,Z\ge1\), the following four input bounds hold uniformly in the fixed row multiplier and in the smooth profile, also after one logarithmic derivative:

\[
\begin{aligned}
 A_8(x)&=\sum_b|\sum_{Nh\le x}\mu(h)\bar\alpha(h)^3\xi(h)^3\chi_h(bk)^3\mathbf1_{(h,f)=1}|^8
 \ll Bx^4+B^{1/2}x^8,\\
 T_2(Z)&=\sum_b|T_{bk}(Z;f)|^2
 \ll \min\{BZ,\ BK+B^2K^2F/Z\},\\
 T_4(Z)&=\sum_b|T_{bk}(Z;f)|^4
 \ll \Theta_6(B,Z^2),\\
 \Theta_6(B,Z^2)&=B+Z^2+B^{5/6}Z^{2/3}+B^{1/3}Z^{5/3}.
\end{aligned} \tag{1}
\]

The first is the Goldmakher–Louvel quadratic large sieve after expanding the fourth power, decomposing its product into squarefree and square parts, and applying the divisor bound. The second combines the pointwise trivial theta bound on the *actual B rows* with prop:R on the enlarged \(bk\)-family. The third uses de Faveri's sixth-order sieve after fixing the source cube indices and applying it to the square of the remaining squarefree-index polynomial. Cube-index weights sum with at most logarithmic loss, while their row-dependent characters remain bounded multipliers. The matching of these abstract inequalities to the physical source is an imported input, not established by this note.

For any \(1\le C\le D^{1/3}\), split cube indices at C. Weighted Cauchy and prop:R give the short mean
\[
 \sum_b|P_{b,\le C}|^2\ll BK+\frac{B^2K^2F}{D}C^3.\tag{2}
\]
For the tail, Abel summation, Hölder and interpolation give
\[
 \left(\sum_b|P_{b,>C}|^2\right)^{1/2}
 \ll \int_C^{D^{1/3}}x^{-2} A_8(x)^{1/8}T_2(D/x^3)^{1/4}T_4(D/x^3)^{1/8}\,dx.\tag{3}
\]
Here the same bound applies to the derivative term; the displayed T2 must retain its scale-wise minimum. A dyadic supremum for the integral costs only a logarithm. Crucially, it is not legitimate to take the minimum *after* maximizing separately over x.

## Mask-divisor rescaling

In the physical source, inclusion of the auxiliary good squarefree divisor \(e\) produces \(D_e=D/Ne\), \(F_e=FNe\), exterior coefficient \((Ne)^{-1/2}\), and a bounded b-row multiplier. Terms with \((e,gk)>1\) vanish, so the new source label is squarefree. The exact remaining ray phase may be absorbed into this bounded multiplier. Let \(C_*\in[1,D^{1/3}]\) be independent of e.

**Lemma.** After summing over the admissible divisors e by Minkowski, the physical mean is bounded, up to a subpower divisor loss, by the sum of the right side of (2) and the square of the right side of (3), evaluated at \((D,F,C_*)\), together with
\[
 C_*^{-3}\Theta_6(B,D).\tag{4}
\]
This assertion is for the full positive square before any separately required artificial-diagonal budget, as in the source reduction.

**Proof.** If \(Ne\le C_*^3\), put \(C_e=C_*/(Ne)^{1/3}\). Then \(1\le C_e\le D_e^{1/3}\). After the exterior factor is squared, (2) contributes at most
\[
 (Ne)^{-1}BK+\frac{B^2K^2F}{D}C_*^3,
\]
which is bounded by the e=1 short expression. For the tail, change variables \(x=x_0/(Ne)^{1/3}\). The completed-theta scale becomes exactly \(D_e/x^3=D/x_0^3\). Each of the two terms in the A8 bound is at most \((Ne)^{-4/3}\) times its counterpart at \(x_0\). The *trivial* term of T2 is unchanged, and the source term with \(F_e\) grows by at most \(Ne\); thus their pointwise minimum grows by at most \(Ne\). T4 is unchanged. The factor \(dx/x^2\) grows by \((Ne)^{1/3}\). Including the exterior \((Ne)^{-1/2}\), the norm in (3) gains at most
\[
 (Ne)^{-1/2-1/6+1/4+1/3}=(Ne)^{-1/12}.
\]
Thus its squared mean gains at most \((Ne)^{-1/6}\). The change of variables maps the full integration interval onto \([C_*,D^{1/3}]\). Bounded row multipliers and their fixed-e masks remain inside the sums, so no factorization across b is assumed.

If \(Ne>C_*^3\), apply the direct unrestricted-row sixth-order large sieve to the original squarefree source polynomial at length \(D_e\): its coefficient squared mass is subpower, and the bounded b-row multiplier does not affect the estimate. Monotonicity of all four terms gives \(\Theta_6(B,D_e)\le\Theta_6(B,D)\). The squared exterior factor is \((Ne)^{-1}<C_*^{-3}\), giving (4). Summing the finitely many e by Minkowski costs at most the divisor count of the physical mask, hence \(Y^\epsilon\). This also covers \(D_e<1\), for which the fixed annular source is empty unless within a bounded endpoint range. ∎

## Scalar ledger and explicit applications

Put \(P=Y^{6/5}\), \(D_0=Y^d\), \(K=Y^\kappa\), \(G=Y^g\), \(B=Y^b\), and \(D=P/(D_0G)=Y^{\Delta}\), \(\Delta=6/5-d-g\), \(F=GK\). The physical prefactor after counting \(a\)-roots and \(d'\)-labels is
\[
 Y^p,\qquad p=\frac1{30}+\frac{2d}{3}-\frac{5\kappa}{6}-\frac b6.\tag{5}
\]
The applicable core has \(d,g,\kappa\ge0\), \(\kappa\le d\), \(d+g+6\kappa/5\le C_{\rm core}\), and the nonempty dual support has \(b\le7/5+\kappa-2d\). These are the original physical constraints and not assumptions about signs of individual g blocks.

For a cutoff \(C_*=Y^c\), a logarithmic cube dyad \(x=Y^z\) has \(c\le z\le\Delta/3\). Its norm exponent from (3) is
\[
 \begin{aligned}
 H(z)={}&\tfrac18\max(b+4z,b/2+8z)
 +\tfrac14\min\{b+\Delta-3z,\max(b+\kappa,2b+3\kappa+g-\Delta+3z)\}\\
 &+\tfrac18\max\{b,2(\Delta-3z),5b/6+2(\Delta-3z)/3,b/3+5(\Delta-3z)/3\}-z.
 \end{aligned}\tag{6}
\]
Thus the three exponent contributions to check are
\[
 \begin{aligned}
 E_{\rm short}&=p+\max\{b+\kappa,2b+3\kappa+g-\Delta+3c\},\\
 E_{\rm tail}&=p+2\max_{c\le z\le\Delta/3}H(z),\\
 E_{\rm large\ e}&=p-3c+\max\{b,\Delta,5b/6+\Delta/3,b/3+5\Delta/6\}.
 \end{aligned}\tag{7}
\]
The original auxiliary diagonal must also be bounded separately by the previously established BK mass face. Sector partitions and profiles are fixed before the dyadic summation; this loses only \(Y^\epsilon\).

For the increment interval \(89/100\le b\), the source root bound and the displayed choice of cutoff give
\[
 \log_Y Ne\le \frac{7/5-b+4d-5\kappa}{6}
 \le 3c-\frac{299}{3000},\qquad c=\frac1{12}+\frac d{15}-\frac{3g}{20}.\tag{8}
\]
Consequently every e uses the rescaling portion of the lemma, and the fallback (4) is unnecessary on this interval. The previously reviewed sixth/third Hölder estimate controls the lower interval \(b<89/100\). The check uses \(C_{\rm core}\le7/50\); the same cutoff also lies in \([0,\Delta/3]\) uniformly. The final inequality follows jointly from \(d+g\le7/50\):
\(3c-(7/5-b+4d-5\kappa)/6=1/60+b/6-7d/15-9g/20+5\kappa/6\ge299/3000\).

Exact rational vertex enumeration, including every crossing in (6), gives the following uniform maxima for \(89/100\le b\le b_{\max}\):

| \(C_{\rm core}\) | \(b_{\max}\) | maximum \(E_{\rm tail}\) | maximum \(E_{\rm short}\) | target |
|---|---|---|---|---|
| \(7/50\) | \(277/300\) | \(21/20\) | \(9337/9000\) | \(21/20\) |
| \(1925877/15625000\) | \(88917107/93750000\) | \(19949123/18750000\) | \(2959410557/2812500000\) | \(19949123/18750000\) |

The first line gives the target \(Y^{21/20+\epsilon}\), allowing equality. In the second, restrict to any fixed \(b\) strictly below the stated endpoint to obtain an exponent strictly below \(E_*\); the strictness must be chosen before the harmless \(\epsilon\)-losses. These assertions remain subject to the source and profile assumptions stated above; the external analytic input and its physical matching remain cited inputs. High_match independently audited the source-conditioned derivation and corrected an earlier guard exposition error. The scale-wise minimum in (6) can make the maximum occur at an interior crossing, which the certificate includes.

The [exact checker](check_vertex_certificate.py) works at \(b=b_{\max}\), which suffices because the minimum slope in \(b\) of every affine contribution to \(p+2H\) is at least \(-1/6+1/8+1/2=11/24>0\); maxima and minima preserve that monotonicity. Both short faces also increase with \(b\). The checker drops the nonempty-support restriction, enlarging the polytope.

## Scale-wise mixture of fourth- and eighth-prefix Hölder bounds

The same Abel integrand has a second upper bound from the already reviewed fourth-prefix estimate:
\[
 \|A(x)T(D/x^3)\|_2\ll
 \min\{A_4(x)^{1/4}T_4(D/x^3)^{1/4},\ A_8(x)^{1/8}T_2(D/x^3)^{1/4}T_4(D/x^3)^{1/8}\},\tag{9}
\]
where \(A_4(x)\ll Bx^2+B^{1/2}x^4\). This minimum is taken before integration. The divisor rescaling of the fourth-prefix term has squared gain \((Ne)^{-2/3}\): its norm gains \((Ne)^{-1/2-1/6+1/3}=(Ne)^{-1/3}\). The eighth-prefix term gains \((Ne)^{-1/12}\) as above. Therefore the rescaled minimum is bounded by \((Ne)^{-1/12}\) times the unmasked minimum. The short estimate is still (2), with the same e-uniform cutoff and guard.

In the exponent ledger, replace \(H(z)\) by its minimum with
\[
 H_2(z)=\tfrac14\max(b+2z,b/2+4z)
 +\tfrac14\max\{b,2(\Delta-3z),5b/6+2(\Delta-3z)/3,b/3+5(\Delta-3z)/3\}-z.\tag{10}
\]
For fixed \(b\), a rigorous finite check can maximize the resulting hypograph over each of the eight fourth-prefix faces and sixteen eighth-prefix faces; each problem is a rational linear program in \((d,\kappa,g,z,T)\), including the two T2 branches and the cutoff endpoints. Preliminary floating-point experiments with the same adaptive cutoff suggest that \(b=463/500\) lies below the 21/20 target. This is **not yet a certified bound**; the exact program and independent audits are pending.

## Tenth-prefix / eighth-prefix mixture

A further fixed-power use of the same quadratic large sieve gives
\[
 A_{10}(x)=\sum_b|A_b(x)|^{10}\ll Bx^5+B^{1/2}x^{10}.\tag{11}
\]
Indeed, expand \(A_b^5\); each coefficient is bounded by a fixed divisor function, and decompose each product into its squarefree part and square. After fixing the square part \(v^2\), its row factor is the contraction \(\mathbf1_{(v,b)=1}\); the quadratic large sieve applies to the squarefree part with a common source vector, including the fixed \(k,f\) multipliers. For a fixed squarefree-row scale \(M\), the source square-part sum contributes at most \(\sqrt{M x^5}\log x+x^5\), up to subpowers. Writing sixth-free \(b=w t^2\) with \(w\) squarefree and summing the resulting row means over \(Nt\ll\sqrt B\) gives \(Bx^5+B^{1/2}x^{10}\), again up to subpowers; all row-specific overlap masks are retained. For each cube scale, interpolation \(\|T\|_{5/2}\le\|T\|_2^{3/5}\|T\|_4^{2/5}\) and Hölder give
\[
 \|AT\|_2\ll A_{10}(x)^{1/10}T_2(Z)^{3/10}T_4(Z)^{1/10},\qquad Z=D/x^3.\tag{12}
\]
Also, Cauchy on the actual B rows gives the third branch \(T_2(Z)\ll B^{1/2}T_4(Z)^{1/2}\); this is compatible with the masks and need not enlarge the row family. Use the minimum of (12) and the eighth-prefix bound in (9), and use all three T2 branches *before* integrating. Under the substitution in the lemma, the A10 input gains \((Ne)^{-5/3}\), and the new T2 branch is unchanged. The resulting norm has gain at most
\[
 (Ne)^{-1/2-1/6+3/10+1/3}=(Ne)^{-1/30}.\tag{13}
\]
The eighth-prefix term has the stronger gain \((Ne)^{-1/12}\); consequently their scale-wise minimum has the gain (13). Here and in (11) all constants and divisor-function exponents are fixed before \(Y\) varies.

For the physical increment take
\[
 c=\frac1{20}+\frac d{15}-\frac g{20},\qquad 23/25\le b.\tag{14}
\]
The root bound gives \(3c-\log_Y Ne\ge7/1500\) uniformly on the entire core with \(C_{\rm core}\le7/50\), and \(0<c\le\Delta/3\). Thus all divisor terms use the rescaled short and tail bounds. The eighth-prefix result already covers the lower range, and the source profile/sector and diagonal qualifications are unchanged.

The [exact rational dual certificate](check_p45_dual.py) bounds both Hölder expressions, all source/trivial/Cauchy T2 branches, all prefix and T4 faces, and the cutoff and terminal cube scales. HiGHS supplies candidate multipliers; the script verifies each dual identity and its nonnegativity using exact rational arithmetic, so its upper bounds are exact. It gives:

| \(C_{\rm core}\) | \(b_{\max}\) | tail exponent upper bound | short exponent upper bound | target |
|---|---|---|---|---|
| \(7/50\) | \(10283/11000\) | \(21/20\) | \(1917/2000\) | \(21/20\) |
| \(1925877/15625000\) | \(3294802253/3437500000\) | \(19949123/18750000\) | \(606649567/625000000\) | \(19949123/18750000\) |

The first line gives the target with \(Y^\epsilon\) losses; the second gives a strict saving below \(E_*\) for any fixed \(b\) strictly below its endpoint. **High_match and Other_families independently reviewed the tenth-prefix source-conditioned argument and the exact dual certificate.** The Cauchy T2 branch is necessary for the displayed scalar bounds. No assertion here bounds the remaining dual core.

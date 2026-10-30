# Square-part stratification of the mixed theta tail

**Status.** Source-qualified restricted-slice calculation, with independently reviewed exact p=6 and p=6/10 scalar certificates. It is not an individual zero-free theorem. The physical Poisson/profile identifications and the GL quadratic, sixth-order and completed-theta source inputs are those of [the eighth/tenth Hölder tail](../2026-10-29-eighth-holder-tail/README.md). Floating-point grid outputs below are diagnostic, not certificates.

Write each good sixth-free row uniquely as \(b=w v^2\), with \(w\) squarefree and \(v\) cube-free; common primes of \(w,v\) are allowed. Fix the dyadic norm \(Nv\asymp V\), so \(V\le B^{1/2}\), \(Nw\ll M=B/V^2\), and the number of rows in this slice is \(\ll B^{1+\epsilon}/V\). Its original masks and all bounded fixed-row multipliers remain in place.

For every fixed positive integer \(p\), the prefix moment has the refined bound
\[
 \sum_{b\text{ in slice}}|A_b(x)|^{2p}
 \ll (Bx)^\epsilon\left(\frac BV x^p+V x^{2p}\right).\tag{1}
\]
Indeed, fix v and expand \(A_b^p\). The squarefree column part of each product has a common quadratic source coefficient; the column square part gives a row contraction and incurs a harmonic sum. Since \(\chi_c(v^2)^3\) is the original 0/1 mask, the v-factor is also a contraction. GL then bounds the fixed-v 2p-moment by \((Bx)^\epsilon[(B/V^2)x^p+x^{2p}]\); summing over \(O(V^{1+\epsilon})\) values of v gives (1). Since \(1\le V\le B^{1/2}\), (1) is never weaker than the reviewed all-row bound. Keeping both in the minimum is harmless.

The completed-theta fourth moment also admits
\[
 T_4(Z)\ll (BZ)^\epsilon\min\{\Theta_6(B,Z^2),\ V\Theta_6(B/V^2,Z^2),\ (B/V)Z^2\}.\tag{2}
\]
For the middle expression fix v first: the fixed multiplier \(\chi_n(v)^2\) is absorbed into the common theta coefficient, including its zeros, and the theta cube-index row factors are bounded contractions. Squaring the remaining squarefree n-polynomial has sixth-free columns, so the same Θ₆ argument applies to the squarefree w rows; finally sum over v. The last expression is the actual-row-count and pointwise theta bound. These common-vector and sector identifications are a source interface to verify, not a new printed source theorem.

Use simultaneously
\[
 T_2(Z)\ll(BZKF)^\epsilon\min\{(B/V)Z,\ BK+B^2K^2F/Z,\sqrt{(B/V)T_4(Z)}\}.\tag{3}
\]
The middle expression is the unrefined completed-theta source mean and remains valid for a subset; the first and last use only the actual slice count. The short cube-index contribution likewise retains its earlier unrefined source estimate. This choice avoids assuming any new moving-v theta mean.

For fixed \(2\le p\le6\), Hölder and T2–T4 interpolation bound the Abel integrand by
\[
 A_{2p}(x)^{1/(2p)}T_2(D/x^3)^{(p-2)/(2p)}T_4(D/x^3)^{1/(2p)}\!/x^2.\tag{4}
\]
The scale-wise minimum over these p may be used before integration. Under \(e\)-rescaling \(x=x_0/(Ne)^{1/3}\), every prefix term loses at least \((Ne)^{-p/3}\), the source T2 can grow by \(Ne\), and T4 is unchanged. Including the exterior mask coefficient and \(dx/x^2\), each p-bound has norm factor at most \((Ne)^{1/6-1/p}\), nonincreasing for \(p\le6\). Thus a common cutoff satisfying \(Ne\le C_*^3\) permits the same divisor summation as the earlier note. No p>6 conclusion follows from this argument without additional divisor bookkeeping.

Using the earlier short mean, the minimum of stratified and unstratified moments, and the physical prefactor from the eighth/tenth note, [corner.py](corner.py) samples the corner \(d=7/50,\kappa=g=0\) and cube cutoffs; [grid.py](grid.py) samples the full core coarsely. At \(b=.945\) the worst sampled exponent is about 1.04761, at \(v=0,d=.14,\kappa=g=0\); at \(b=.95\) it is about 1.05430. These values use finite grids and do not establish the continuous supremum or the exact source matching. A rigorous gain requires a rational polyhedral certificate for all \(d,\kappa,g,v\), all cube scales and a single admissible cutoff per physical dyad, plus an independent check of (1)–(3).

## Exact p=6 source-qualified bound

The further hypotheses and interpretation are exactly those of the [physical dual-core reduction](../2026-10-29-eighth-holder-tail/README.md): fixed original column sector; source Poisson, reciprocity, profile and finite-ray calibration; and a separately budgeted artificial diagonal. Under these inputs the following slice bound uses **only** (1), the original all-row Θ₆ term of (2), and all three branches of (3). In particular it does not require the optional fixed-v Θ₆ refinement. Take the common dyad-dependent cutoff
\[
 \log_Y C_*=\frac1{20}+\frac d{15}-\frac g{20}.\tag{5}
\]
For \(b\ge23/25\), the earlier calculation gives \(\log_Y Ne\le3\log_Y C_*-7/1500\) throughout \(d+g+6\kappa/5\le7/50\); the smaller b range is covered by the earlier eighth/tenth bound. The p=6 norm factor in the divisor-rescaling lemma is exactly \((Ne)^0\), and the divisor count is \(Y^\epsilon\).

With \(u=\log_Y V\in[0,b/2]\), \(z=\log_Y x\), \(\Delta=6/5-d-g\), \(Z_e=\Delta-3z\) and \(p_0=1/30+2d/3-5\kappa/6-b/6\), insert into (4)
\[
 \begin{aligned}
 A_{12}&:\quad \max\{b-u+6z,\ u+12z\},\\
 T_4&:\quad \max\{b,2Z_e,5b/6+2Z_e/3,b/3+5Z_e/3\},\\
 T_2&:\quad \min\{b-u+Z_e,\ \max(b+\kappa,2b+3\kappa+g-Z_e),\ (b-u+T_4)/2\}.
 \end{aligned}\tag{6}
\]
The tail mean exponent is \(p_0-2z+A_{12}/6+2T_2/3+T_4/6\), maximized over the core, \(0\le u\le b/2\) and \(\log_Y C_*\le z\le\Delta/3\). The [checker](check_stratified_p6.py) produces and exactly verifies nonnegative rational dual certificates for each of its sixteen face programs, including all T2 branches. It yields:

| \(C_{\rm core}\) | \(b_{\max}\) | tail exponent upper bound | short exponent upper bound | target |
|---|---|---|---|---|
| \(7/50\) | \(4213/4450\) | \(21/20\) | \(21813/22250\) | \(21/20\) |
| \(1925877/15625000\) | \(1348218883/1390625000\) | \(19949123/18750000\) | \(13778849011/13906250000\) | \(19949123/18750000\) |

Thus, with any fixed \(\epsilon>0\), the indicated slice through \(b\le4213/4450\) has target size \(Y^{21/20+\epsilon}\); every fixed \(b\) strictly below the second endpoint has a strict saving relative to the current θ threshold, after choosing \(\epsilon\) smaller than the margin. To cover all smaller b using the endpoint check, enlarge the u-domain to \([0,b_{\max}/2]\) and then increase b to \(b_{\max}\); every tail and short face increases with b in this enlarged domain. Earlier estimates cover b below \(23/25\).

High_match and Other_families independently checked the stratified moment identities, the overlap masks, and p=6 divisor scaling. High_match and Other_families independently reran and audited the exact scalar checker. These results remain conditional on the named analytic and physical-source interfaces and control a restricted slice, leaving the full mixed moment and individual zero-free conclusion open.

## Fixed-w cubic caps and an e-safe p=6,10 split

The preceding limitation for \(p>6\) arises from using prop:R in the **tail**. Instead, fix w and apply the cubic large sieve to the cube-free v-row family. With \(W=B/V^2\), the [fixed-w cubic moment](../2026-10-29-squarepart-cubic-theta-moments.md) gives the two additional bounds
\[
 T_2(X)\ll Y^\epsilon W\Theta_3(V,X),\qquad
 T_4(X)\ll Y^\epsilon W\Theta_3(V,X^2),\quad
 \Theta_3(V,L)=V+L+(VL)^{2/3}.\tag{7}
\]
The fixed-w factor \(\chi_n(wk)\) is common to all v rows. The theta cube-index factor \(\chi_q(v)^6\) is a row contraction with the original zeros. For the fourth moment, the product of two squarefree n-indices is cube-free even if they overlap. The same holds when w and v share primes, and the fixed finite-ray, reciprocal and powered-family identifications are the explicit source inputs described in the linked note.

Let \(P_b(D;f)\) be the squarefree theta polynomial with the source cube-inversion expansion, and split its cube-index sum at \(C_*\). Define the scale-wise caps
\[
 \begin{aligned}
 U_2(X)&=\min\{(B/V)X,\ \Theta_6(B,X),\ W\Theta_3(V,X)\},\\
 U_4(X)&=\min\{\Theta_6(B,X^2),\ W\Theta_3(V,X^2)\}.
 \end{aligned}\tag{8}
\]
All expressions here and below include the usual \(Y^\epsilon\) losses, with fixed smooth-profile and derivative seminorms. For each cube scale h, apply (4) with \(p=6\) and \(p=10\), replacing \(T_2,T_4\) by \(U_2,U_4\). Take the **minimum at that scale** before Abel integration:
\[
 \|P_{>C_*}\|_2\ll Y^\epsilon\int_{C_*}^{D^{1/3}}\frac{dH}{H^2}
 \min_{p\in\{6,10\}}
 A_{2p}(H)^{1/(2p)}U_2(D/H^3)^{(p-2)/(2p)}U_4(D/H^3)^{1/(2p)}.
 \tag{9}
\]
The prefix moment (1) applies for every fixed p, in particular p=10. In contrast to (4), neither cap in (8) uses prop:R. This allows p=10 without an e-dependent loss.

For the short part, weighted Cauchy in the source cube inversion and the harmonic count of h give, up to logarithms,
\[
 \|P_{\le C_*}\|_2^2\ll Y^\epsilon
 \sup_{1\le H\le C_*}
 \min\!\left\{BK+\frac{B^2K^2F H^3}{D},\ U_2(D/H^3)\right\}.
 \tag{10}
\]
The first cap is prop:R; every bound is taken at the same H before the supremum. All h-dependent characters and masks remain inside the row contraction when weighted Cauchy is applied.

For a physical divisor e, \(D_e=D/Ne\), \(F_e=FNe\), and the exterior norm coefficient is \((Ne)^{-1/2}\). Set \(H=H_0/(Ne)^{1/3}\), so the completed-theta scale is exactly \(D/H_0^3\). Each prefix bound in (1) gains at least \((Ne)^{-p/3}\); the caps (8) are invariant because they do not use F. After the exterior factor and the transformed Abel measure, each p-tail norm in (9) gains at most
\[
 (Ne)^{-1/2-1/6+1/3}=(Ne)^{-1/3},\tag{11}
\]
including p=10. Taking their minimum preserves this gain. For the short part, the squared exterior weight cancels the increase from \(F_e\): the prop:R growth term becomes \(B^2K^2F H_0^3/D\), while every cap in (8) gains a factor at most one. Summing the admissible e by Minkowski costs only a fixed divisor subpower. This argument uses the same \(C_*\) for both p and all cube scales; it does not assume cancellation in the e-sum.

For the physical notation of (5)–(6), choose the common dyad-dependent cutoff \(C_*=Y^c\) with
\[
 c=\frac{1583}{4000}-\frac{3b}{10}-\frac{11(d+g)}{40}-\frac\kappa{10}.\tag{12}
\]
The [exact checker](check_cubic_split.py) works on the full increment \(23/25\le b\le b_{\max}\), with \(0\le u=\log_YV\le b/2\) and \(d,g,\kappa\ge0\), \(\kappa\le d\), \(d+g+6\kappa/5\le C_{\rm core}\). It certifies \(0<c<\Delta/3\) and, using the source root bound
\[
 \log_Y Ne\le\frac{7/5-b+4d-5\kappa}{6},\tag{13}
\]
that \(\log_Y Ne<3c\) throughout both cores. Thus \(C_e=C_*/(Ne)^{1/3}\) is admissible for every relevant e.

The checker verifies rational nonnegative dual multipliers and their exact dual identities for all 24 short and 576 tail face programs, for each row of the following table. Floating optimization only proposes the multipliers; the upper bounds themselves are exact.

| \(C_{\rm core}\) | \(b_{\max}\) | short exponent upper bound | tail exponent upper bound | target |
|---|---|---|---|---|
| \(7/50\) | \(97/100\) | \(10961/10440\) | \(3779/3600\) | \(21/20\) |
| \(1925877/15625000\) | \(99/100\) | \(1531442043/1450000000\) | \(19873642453/18750000000\) | \(19949123/18750000\) |

Consequently the indicated dual slice through \(b\le97/100\) meets \(Y^{21/20+\epsilon}\); the slice through \(b\le99/100\) has a strict saving below the θ-threshold exponent. The earlier estimates cover \(b<23/25\). The first short exponent is only \(1/10440\) below its target, so choose all fixed profile, dyadic and epsilon losses after fixing that margin. These bounds include the separately budgeted artificial diagonal only as specified in the physical ledger. They do not control the remaining high-dual complement or prove the full inverse moment.

**Independent reviews.** Families and High_match independently checked the fixed-w cubic source interface and overlap masks, p=6/10 GL prefix moments, common-cutoff divisor scaling, and the exact short/tail programs; both reran [check_cubic_split.py](check_cubic_split.py). The detailed [Families review](INDEPENDENT-CUBIC-SPLIT-REVIEW.md) records the inputs and quantifiers. The underlying published analytic sources and physical Poisson/profile calibration are not independently proved by those reviews.

## Cutoff-free dyadwise combination

The preceding split is unnecessary if the short and tail estimates are compared **on each cube dyad before summation**. Work under the same source, sector, profile and cubic-sieve hypotheses, and fix a square-part dyad \(V\). For \(H\ge1\), put \(X=D/H^3\) and
\[
 R_2(X)=BK+\frac{B^2K^2F}{X},\qquad
 U_2(X)=\min\{(B/V)X,\Theta_6(B,X),W\Theta_3(V,X)\},
 \qquad U_4(X)=\min\{\Theta_6(B,X^2),W\Theta_3(V,X^2)\}.
\]
The terms include uniform fixed profile/derivative and \(Y^\epsilon\) factors. Weighted Cauchy in the cube index gives for a cube dyad, up to logarithms, the squared row norm
\[
 \ll\min\{R_2(X),U_2(X)\}.\tag{14}
\]
The cube-index weight \(1/Nh\) has bounded harmonic mass on each dyad; its characters and masks are bounded row contractions. Alternatively, partial summation on that same dyad, using the square-part prefix estimates and the common logarithmic derivative of \(T\), gives the squared bound
\[
 \ll H^{-2}\min_{p\in\{6,10\}}
 \left[( (B/V)H^p+VH^{2p})^{1/p}
       U_2(X)^{1-2/p}U_4(X)^{1/p}\right].\tag{15}
\]
Both Abel boundary terms have the displayed \(H^{-1}\|AT\|_2\) norm bound, and the integral term has the same dyadic majorant. The needed uniformity for the common profiles and their derivatives is the same source input as in (9)–(10). Take the minimum of (14) and (15) **at this dyad**, then sum the \(O(\log Y)\) dyads by Minkowski. In particular neither a cube cutoff nor a minimum taken after independently maximizing is used.

This remains valid for the moving mask divisor e without any condition \(Ne\le C_*^3\). At a physical dyad \(H_e\), set \(H_0=(Ne)^{1/3}H_e\); then \(D_e/H_e^3=D/H_0^3\). The exterior squared weight \((Ne)^{-1}\) cancels the growth of \(F_e=FNe\) in the prop:R term, while the direct caps in \(U_2\) only improve after that weight. In (15), the prefix input at \(H_e=H_0/(Ne)^{1/3}\) is at most \((Ne)^{-p/3}\) times the input at \(H_0\), the direct caps are invariant, and the Abel norm's \(H_e^{-1}\) contributes \((Ne)^{1/3}\). With the exterior norm coefficient \((Ne)^{-1/2}\), the Abel norm gains at least \((Ne)^{-1/3}\), or \((Ne)^{-2/3}\) after squaring. The rescaled interval is contained in \(1\le H_0\ll D^{1/3}\); bounded changes of dyadic endpoints cost only uniform fixed-profile constants. Sum over the source divisors e by Minkowski and absorb the divisor count into \(Y^\epsilon\). The separately budgeted artificial-diagonal and signed-source qualifications remain those of the physical ledger.

The [exact dyadwise checker](check_dyadwise.py) verifies 1,152 rational dual inequalities for each row below, with \(b\) itself a variable throughout \([23/25,b_{\max}]\), \(0\le u\le b/2\), and the full residual \((d,\kappa,g)\) core. The cube log runs over the entire admissible interval; no cutoff or e guard is assumed. Floating optimization proposes duals, and every identity and nonnegativity assertion is verified exactly.

| \(C_{\rm core}\) | \(b_{\max}\) | dyadwise exponent upper bound | target |
|---|---|---|---|
| \(7/50\) | \(243/250\) | \(88157/84000\) | \(21/20\) |
| \(1925877/15625000\) | \(997/1000\) | \(5281635419/4968750000\) | \(19949123/18750000\) |

Both displayed upper bounds are strictly below their targets. Earlier results cover \(b<23/25\); choose fixed source/height/epsilon losses smaller than the respective strict margins. High_match and Other_families independently checked the cutoff-free weighted-Cauchy, Abel endpoint and moving-divisor scaling. Families independently reran the exact checker and reviewed the common-scale and boundary-term bookkeeping; see the [independent review](INDEPENDENT-DYADWISE-REVIEW.md). This remains a partial dual-core bound, conditional on the stated analytic/source interfaces; it neither covers the complement above these b endpoints nor proves the full inverse moment or an individual zero-free region.

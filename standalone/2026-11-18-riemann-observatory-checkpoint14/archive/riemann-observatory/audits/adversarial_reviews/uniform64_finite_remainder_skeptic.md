# Independent audit of the finite-height tapered-prime remainder

17 November 2026. Assume RH and use the prescribed anchored \(k=2\) polynomial. The proposed remainder is valid with the stated constants. In particular the direct comparison with the finite constant \(C_{\mathcal F}\) is
\[
\left|\sqrt{(\log N)E_N}-\sqrt{C_{\mathcal F}}\right|
 \le \alpha+\frac{q}{1+\sqrt{1-q}}\sqrt{c_+}.
\]
Here \(\alpha\), \(q\), \(c_+\) and the finite data are defined below. The bound from \(\sqrt{C_{\mathcal F}}\) to \(\sqrt{C_2}\) adds at most \(\sqrt{B(Y)}\). The revised numerical certificate is checked below. [Tapered-prime proof](director_tapered_prime_array_round9.md) · [Effective \(10^{27}/\log N\) proof](prime_array63_effective_bound_skeptic.md)

## Scaling, signs, and the finite input

Let \(L=\log N\), \(s=1/2+it\), \(r_\rho=-m_\rho(2^{1-\rho}-1)\), and \(b_\rho=r_\rho\zeta'(\rho)/\rho\). Index all distinct nontrivial zeros on both ordinate signs. The multiplicity is in \(r_\rho\), so a term is included once even at a multiple zero. Under RH the finite set \(\mathcal F\) must contain exactly the distinct zeros with \(|\gamma_\rho|\le Y\). A cutoff zero belongs to \(\mathcal F\). If a packet of disjoint intervals certifies fewer zeros, any omitted inner zeros would need their own remainder charge. An ordinate enclosure containing just one distinct zero is compatible with any certified multiplicity of that zero. The proof requires the actual multiplicity when calculating \(r_\rho\) and local constants, or a valid upper bound on it when calculating only a local error bound. The coefficient \(b_\rho\) itself can be treated as exactly zero if multiplicity at least two is certified.

Use \(dt/(2\pi)\). In the effective proof, subtracting the pole part (5) from the double-Perron representation gives the near term
\[
P_N(t)=\sum_{|\gamma_\rho-t|\le1}\frac{r_\rho\zeta(s)}{s(s-\rho)} E_L(t-\gamma_\rho),\qquad
E_L(u)=\frac{1-e^{-iLu}}{iLu}.
\]
Indeed the difference of the two near residue terms is \(r_\rho(1-e^{-iLu})/[L(s-\rho)^2]\) before multiplication by \(\zeta(s)/s\). The scale \(\sqrt L\) gives \(H_L=\sqrt L E_L\), which is the Fourier transform of \(L^{-1/2}\mathbf1_{[0,L]}\) for the convention \(e^{-iut}\). It has squared norm 1 and \(H_L(0)=\sqrt L\). The \(10^{27}/L\) bound for the whole squared error is unnecessary here. The effective proof's stronger pointwise estimate for the remaining term is \(10^{11}T_t^{-9/16}\log T_t/L\), \(T_t=2+|t|\). After squaring and integrating, it gives \(\|\sqrt L W_N\|_2^2\le10^{22}\cdot16384/L<2\cdot10^{26}/L\). The factor \(1/\pi\) arising from the two signs of \(t\) was bounded above by 1. This term includes the actual anchor \(A_N(1)\) with the other three background terms.

## Constants and comparison

Let \(T_\rho=2+|\gamma_\rho|\) and \(a_\rho(t)=r_\rho\zeta(s)/(s(s-\rho))\). The prior bound \(|a_\rho(t)|\le 3\cdot10^6 m_\rho T_t^{-9/16}\) holds for \(|t-\gamma_\rho|\le1\) by (2), \(|r_\rho|\le3m_\rho\), and \(|s|^{-1}\le5/T_t\). Weighted Cauchy–Schwarz with \(\sum_{|t-\gamma_\rho|\le1}m_\rho\le100\log T_t\) bounds any selected and individually truncated near sum by
\[
\left|\sum_\rho a_\rho(t)H_L(t-\gamma_\rho)\mathbf1_{\rho,t}\right|^2
\le 9\cdot10^{14}T_t^{-9/8}\log T_t
   \sum_\rho m_\rho|H_L(t-\gamma_\rho)|^2\mathbf1_{\rho,t},
\]
where \(\mathbf1_{\rho,t}\) vanishes outside \(|t-\gamma_\rho|\le1\). This form absorbs off-diagonal terms even for arbitrarily close tail zeros and for overlapping cutoff regions.

On those regions \(T_t^{-9/8}\log T_t\le5T_\rho^{-9/8}\log T_\rho\), since \(T_t/T_\rho\in[1/2,2]\), \(2^{9/8}<5/2\), and \(\log(2T_\rho)\le2\log T_\rho\). For each integer \(j\ge0\) the count on \(j\le|\gamma_\rho|<j+1\) on both signs is at most \(200\log(j+3)\) with multiplicity, from (3) by centering at the midpoints of the positive and negative shells. Counting a possible zero of ordinate 0 twice in this upper count only enlarges it. Thus the bound for the squared near-tail norm starts at \(j=\lfloor Y\rfloor\), and includes the entire boundary shell. Using \(\log(j+3)\le2\log(j+2)\) twice gives the prefactor \(9\cdot10^{14}\cdot5\cdot800\). Next \(\log x\le32x^{1/32}\) gives the exponent \(-9/8+1/16=-17/16\). Summing the decreasing majorant and integrating from \(1+\lfloor Y\rfloor\) gives exactly
\[
(9\cdot10^{14}\cdot5\cdot800\cdot32^2\cdot16)
(1+\lfloor Y\rfloor)^{-1/16}
<B(Y)=6\cdot10^{22}(1+\lfloor Y\rfloor)^{-1/16}.
\]
The same \(B(Y)\) bounds \(C_2-C_{\mathcal F}\), since at a simple zero (2) gives \(|b_\rho|^2\le (1.5\cdot10^6)^2 T_\rho^{-9/8}\). This is below the corresponding integrated per-zero majorant \(9\cdot10^{14}\cdot5\,T_\rho^{-9/8}\log T_\rho\), using \(\log T_\rho>2/3\). At a multiple zero the coefficient is exactly zero. This is an independent bound on the derivative coefficient tail. It does not assert that the function near a multiple zero vanishes throughout its window.

Choose \(0<\delta\le1/16\) with mutual distances of finite ordinate enclosures \(>2\delta\). The true inner windows are disjoint, including across the two ordinate signs. Near terms outside their own inner windows, \(\delta<|t-\gamma_\rho|\le1\), use the Cauchy–Schwarz bound above with mass at most \(q=\min(1,4/(\pi L\delta))\). The mass factor follows by integrating \(4/(Lu^2)\) on both rays with \(du/(2\pi)\), or by Plancherel if that bound exceeds 1. Their aggregate squared norm is at most \(qB(0)\). No distance from any tail zero is used. Its contribution remains in the already bounded tail norm even when a tail zero lies arbitrarily near an inner window.

Take \(R=2\delta\) and any certified local \(\zeta\)-disk bound \(M_\rho\), for example \(2400(2+G_\rho)^{7/16}\) with \(G_\rho\ge|\gamma_\rho|\). The effective proof establishes that estimate for the full radius \(1/8\) disk, so it applies at \(R\le1/8\). Cauchy's Taylor coefficient bound gives
\[
\left|\zeta(\rho+iu)/(iu)-\zeta'(\rho)\right|
\le 2M_\rho |u|/R^2,\qquad |\zeta'(\rho)|\le M_\rho/R
\quad (|u|\le\delta).
\]
The bound \(|1/(\rho+iu)-1/\rho|\le4|u|\) then gives \(D_\rho|u|\) for the error \(a_\rho(\gamma_\rho+u)-b_\rho\), with \(D_\rho=3m_\rho(4M_\rho/R^2+4M_\rho/R)\). All removable values follow by continuity. The inequality \(u^2|H_L(u)|^2\le4/L\) and disjoint inner windows give a squared replacement error at most \(4\delta\sum_{\rho\in\mathcal F}D_\rho^2/(\pi L)\).

Hence, with
\[
\alpha=\sqrt{2\cdot10^{26}/L}+\sqrt{B(Y)}+\sqrt{qB(0)}
       +\sqrt{4\delta\sum_{\rho\in\mathcal F}D_\rho^2/(\pi L)},
\]
the scaled residual differs from the truncated finite model in norm by at most \(\alpha\). The four quantities are the background term, near tail, lost finite outer windows, and coefficient replacement. The finite model norm is exactly \(\sqrt{(1-Q)C_{\mathcal F}}\), with \(Q=\|H_L\mathbf1_{|u|>\delta}\|_2^2\le q\). The finite windows eliminate all inner-model off-diagonal terms. Reverse triangle inequality and \(1-\sqrt{1-q}=q/(1+\sqrt{1-q})\) prove the direct finite-constant bound stated above, valid also at \(q=1\) and for \(\mathcal F=\varnothing\). The one-sided upper bound \(\sqrt{LE_N}-\sqrt{C_2}\le\alpha\) uses \(\sqrt{(1-Q)C_{\mathcal F}}\le\sqrt{C_2}\). The reverse difference adds at most the model debit and \(\sqrt{B(Y)}\). The proposed bound for \(|LE_N-C_2|\) and all three enclosure intersections follow by squaring these nonnegative bounds; the intersection using division by \(1-q\) is valid only when \(q<1\).

## Counterexample checks and presentation

Two unit-amplitude untruncated kernels at positive separation \(d\) have squared sum \(2+2\sin(Ld)/(Ld)\) by Fourier Plancherel. For \(Ld\to0\) this tends to \(4\), so adding individual squared norms would miscount by nearly \(2\). A complete finite list separates this pair into disjoint inner windows even for tiny \(d\), with the accompanying \(q\) debit then potentially as large as 1. Omitting one kernel and claiming a vanishing remainder for the other would also fail on this fixture. The condition that all inner zeros be listed is needed to place every omitted kernel under the height majorant. Cutoff equality, empty and singleton lists, multiple zeros, and arbitrarily close distinct zeros across the cutoff produce no counterexample with the stated assumptions.

The companion script passed all arithmetic, quadrature, and synthetic enclosure checks. Its numerical quadrature is a fixture and supplies no zeta derivative enclosures. The revised candidate Markdown and script contain no unexpected ASCII control bytes. [Companion script](../../scripts/prime64_finite_remainder_checks.py)

## Updated coefficient tail and certified instance at \(Y=100\)

I reran the companion script with --arb, PYTHONPATH=/workspace/riemann-runtime, python-flint 0.9.0 and FLINT 3.6.0. The revised proof retains \(B(Y)\) for the kernel tail. For the derivative coefficient tail alone, \((1.5\cdot10^6)^2 T_\rho^{-9/8}\) at simple zeros together with the two-sign shell count \(200\log(j+3)\le400\log(j+2)\) gives
\[
 C_2-C_{\mathcal F}\le9\cdot10^{14}
  \sum_{j\ge\lfloor Y\rfloor}(j+2)^{-9/8}\log(j+2).
\]
With \(X=1+\lfloor Y\rfloor\ge3\), the summand function decreases on \([X,\infty)\), since its derivative has sign \(1-(9/8)\log x<0\). Integration gives \(X^{-1/8}(8\log X+64)\), since the displayed expression tends to zero at infinity and has derivative \(-X^{-9/8}\log X\). Taking the minimum with \(B(Y)\) gives exactly the revised \(A(Y)\). The direct finite-constant bound keeps \(\sqrt{B(Y)}\) in \(\alpha\) to charge the near-function tail. The transfer from \(\sqrt{C_{\mathcal F}}\) to \(\sqrt{C_2}\) can use the smaller \(\sqrt{A(Y)}\).

I inspected the tagged source implementations and wrappers.

- The Python arb.zeta_nzeros delegates to acb_dirichlet_zeta_nzeros. The FLINT contract specifies all zeta zeros, counted with multiplicity, for \(0<\Im s\le t\). The exact-input branch calls _acb_dirichlet_exact_zeta_nzeros and constructs an exact ball for the integer result at this precision. Internally the count uses a sign-separated Hardy-Z list and definite sign tests when a cutoff enters an isolating interval. The dyadic \(100+2^{-10}\) is exact and the output was the exact integer 29. All 29 distinct critical-line ordinate intervals are strictly below 100, which accounts for the multiplicity slots and excludes any other zero at or below 100, including any off-line zero. [Python wrapper](https://github.com/flintlib/python-flint/blob/0.9.0/src/flint/types/arb.pyx) · [FLINT counting contract](https://github.com/flintlib/flint/blob/v3.6.0/doc/source/acb_dirichlet.rst) · [FLINT count implementation](https://github.com/flintlib/flint/blob/v3.6.0/src/acb_dirichlet/isolate_hardy_z_zero.c)
- The Python acb.zeta_zeros(1,29) delegates to acb_dirichlet_zeta_zeros, which uses acb_dirichlet_hardy_z_zeros and assigns exact real part \(1/2\). The underlying routine isolates and refines the intervals for the Hardy-Z roots. The strict Arb comparisons certify adjacent upper-to-lower gaps greater than \(1/8\). The check on the first positive ordinate also ensures the same across signs. The paired alternating eta series gives strictly positive sum at \(1/2\), and \(1-\sqrt2\ne0\), excluding the real critical zero. [Python root wrapper](https://github.com/flintlib/python-flint/blob/0.9.0/src/flint/types/acb.pyx) · [FLINT root wrapper](https://github.com/flintlib/flint/blob/v3.6.0/src/acb_dirichlet/zeta_zeros.c)
- The expression acb_series([root,1],2).zeta()[1] uses \(a=1\) and no deflation, calls acb_poly_zeta_series and then acb_dirichlet_zeta_jet, and extracts the linear Taylor coefficient with center ranging over the root ball. At these heights and precision the jet dispatches to bounded Euler–Maclaurin computation, whose remainder is added to the real and imaginary Arb radii. The linear coefficient is the first derivative with no nontrivial factorial. Strictly positive modulus of each ball certifies simplicity independently of the count. The minus sign in \(r_\rho\) drops out of the modulus, and the factor 2 includes the negative heights by conjugation. [Python series wrapper](https://github.com/flintlib/python-flint/blob/0.9.0/src/flint/types/acb_series.pyx) · [FLINT series](https://github.com/flintlib/flint/blob/v3.6.0/src/acb_poly/zeta_series.c) · [FLINT jet](https://github.com/flintlib/flint/blob/v3.6.0/src/acb_dirichlet/zeta_jet.c)

The 128-bit replay gave \(C_{\mathcal F}=[0.25253801685456458742967198323133838\ \pm 7.34\cdot10^{-36}]\). A separate 192-bit script checked exact counts at both 100 and \(100+2^{-10}\), adjacent gaps greater than 1.2, and \(|\zeta'(\rho)|>0.79\) on every root ball. It used the complex power \(2^{1-\rho}\) and a sum of squared real and imaginary parts for the coefficient norm, yielding \(C_{\mathcal F}=[0.252538016854564587429671983231338378278632292716928615\ \pm 6.88\cdot10^{-55}]\). The evaluated integral candidate for \(A(100)\) was \([51013336417388447.2179055993738638134462536204436899589348\ \pm 5.02\cdot10^{-41}]\). It is below \(5.102\cdot10^{16}\). Its sum with the finite ball is below \(5.103\cdot10^{16}\). The outward decimal endpoints of the proposed enclosure are valid. The zero certificate and finite coefficient sum are unconditional. The proof of the bound for the full constant and its identification with the scaled array limit use RH.

The checked candidate SHA-256 is cc52f9c127da710db8fdeb9ad522cabf5e31d7e7f799f963ddce791f794380b4. The script SHA-256 is cabe6c3bf5a93a1d82b5b73f334ddbd2cf442801f713b67ade0f5700889a5991. Both passed the control-byte check. The finite certificate uses Python integers and Arb values, with finite outputs at both precisions. The floating-point Simpson fixtures run separately. Invoke the script without Python optimization so the assertions execute.

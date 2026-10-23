# Signed reciprocal completion on the actual primitive projection

23 October 2026. A conditional strengthening of the newly reviewed primitive-label continuation. This keeps the global reciprocal-completion Möbius signs before taking norms. It does not estimate the complementary inverse space or improve the fixed zero-free boundary.

## 1. Precise premise and statement

Assume, for some fixed 2/3<beta<1, the ordinary good-ideal Mertens estimate over the Eisenstein field

\[
 \sum_{Na\le X}^{\rm good}\mu(a)\ll_\epsilon X^{\beta+\epsilon}.
 \tag{M1}
\]

Only this scalar premise is used. A zero-free half-plane for the actual ordinary Dedekind zeta function, together with the appropriate reciprocal growth/Perron argument, can supply it; no arbitrary moving-character estimate is substituted for M1.

Use exactly P1 and the original coefficient family in `../two-hour-boundary-20261023/PRIMITIVE_LABEL_CONTINUATION.md`, frozen SHA256 `a10b7626fc5a7ab7315f8327c53b2fcbe1381a2f04816a04aa697309803976ee`. Retain its full primitive inversion, fixed modulo-36 section vector, all nonunit zeros and the puncture Q. For a good sixth-power-free fixed label R of norm H<=D, the conditional conclusion is

\[
 \boxed{\ |\mathcal P_R(U)|^2
 \ll_\epsilon(UDHNQ)^\epsilon
 \left\{U+D^{(13-2\beta)/12}H^{(3-2\beta)/12}
                         U^{-(1-\beta)/3}\right\}. }\tag{M2}
\]

The predecessor's unconditional term is D^(11/12)H^(1/12). The ratio of the new term to that term is (sqrt(DH)/U)^((1-beta)/3), so the conditional gain starts at U>sqrt(DH).

## 2. The licensed signed dyadic estimate

The global reciprocal-completion identity has the form sum_a mu(a)/Na times F(U/(Na)^6). The function F depends on a only through its norm, after all other arithmetic parameters have been frozen. It is important that a is this global reciprocal-completion ideal, not a divisor selected from the moving numerator.

For any dyad X<=Na<2X and any scalar or finite-dimensional vector function F with

\[
 \sup_{X\le x\le2X}\{\|F(U/x^6)\|+
                  \|x(d/dx)F(U/x^6)\|\}\le B_X,
\]

partial summation using M1 gives

\[
 \left\|\sum_{Na\asymp X}\frac{\mu(a)}{Na}
                      F(U/(Na)^6)\right\|
 \ll_\epsilon X^{\beta-1+\epsilon}B_X.             \tag{M3}
\]

The completed finite and reflected kernel estimates used in the predecessor obey this derivative condition with the same powers: logarithmic differentiation of the physical scale multiplies its common Mellin weight by u-1. Smooth seminorms and rapid vertical decay remain of the same permitted type. The full residue term has the same property directly. Thus M3 is a genuine scalar cancellation before norm estimates, rather than cancellation among arbitrary arithmetic coefficients.

For each frozen d,k_m,g,J,k_R branch, retain the predecessor's cutoff

\[
 C=V^{1/6}(Ah')^{-1/12}k_m^{-1}d^{-1/2},\qquad
 V=U/(t k_R^6),\quad A=D/g.                         \tag{M4}
\]

On the reflected head the old nonvolume dyad grows as X^(1/2), and on the original tail it decays as X^(-1/2). Applying M3 replaces these powers by X^(beta-1/2) and X^(beta-3/2). Since beta>2/3, both sums are controlled by their common endpoint C. The predecessor's combined nonvolume bound is therefore multiplied by C^(beta-1). If C<1, use the original formula on every dyad; its old bound is smaller than the old balanced bound by C^(1/2), which is at most C^(beta-1). Thus this same upper bound covers all branches.

## 3. Complete local summation

The core amplitude before the fixed-R outside factors becomes

\[
 A^{(13-2\beta)/24}t^{1/12}(h')^{(3-2\beta)/24}
 V^{-(1-\beta)/6}
 k_m^{-\beta}e^{-17/12}
 f^{-5/3-\beta/2}d_0^{-2/3-\beta/2}v_0^{-11/12}.
 \tag{M5}
\]

The weakest extracted-prime exponent is now 2/3+beta/2>1. At primes outside e,f,d0 that occur in k_m, the exponent is beta+11/12>1; the geometric k_m valuation denominator is 1-q^(-beta). The other prime exponents are larger. Hence all m-prime sums still converge absolutely after sufficiently small internal losses. This is why the strict premise beta>2/3 appears.

After inserting V and the outside factor g^(-1/2)J^(-1/2)k_R^(-1), the squared fixed-prime factor, excluding D and U, is

\[
 g^{-(25-2\beta)/12}J^{-1}k_R^{-2\beta}
 t^{(3-2\beta)/6}(h')^{(3-2\beta)/12}.             \tag{M6}
\]

At a prime of R with input exponent a and n-presence epsilon, put j=(a+epsilon) mod6 as in the predecessor. For an unselected prime the exponent in M6 is

\[
 -(25-2\beta)\epsilon/12+(3-2\beta)j/12,
\]

which is at most (3-2beta)a/12. For a selected prime the remaining j-factor is -1+(3-2beta)(j+6)/12. When epsilon=0 its excess over the unselected comparison is 1/2-beta<0; epsilon=1 and the reduction j=0 only improve it. Thus M6 costs at most H^((3-2beta)/12), up to subpowers. The finite-prime k_R amplitude product with exponent beta is bounded by H^epsilon, since beta>0 is fixed. This proves the nonvolume term in M2.

The volume terms are bounded by their old absolute estimates and remain U. This is intentional: branches near the divisor cutoff prevent a uniform improvement of that term by M1.

## 4. Partial poles and the small-U case

Retain the exact selected-prime residue collapse of predecessor P8 before using M1. The reciprocal tail is now sum_(Na>C) mu(a)/(Na)^2, whose magnitude is at most C^(beta-2+epsilon) when C>=1. It gives the same factor C^(beta-1) relative to the old C^(-1) bound. For C<1, the old absolute bound is again smaller than this majorant.

For the first progression-residue term, the resulting total squared bound is

\[
 D^{1-\beta/6}H^{(2-\beta)/6}U^{-(1-\beta)/3}.
 \tag{M7}
\]

Its d-prime exponent is 5/6+beta/2>1; a prime outside d occurring in k_m has exponent beta+5/6>1. The fixed-R local factors are bounded by H^((2-beta)/12) in amplitude. The ratio of M7 to the nonvolume term in M2 is exactly (H/D)^(1/12), at most one.

For the second progression-residue term use its already proved absolute bound (DH)^(1/2), avoiding any divergent signed-bound majorant at a d exponent below one. When U>=sqrt(DH), this is at most U. This proves M2 in that range. When U<sqrt(DH), the new nonvolume term is at least the old D^(11/12)H^(1/12); since H<=D, that old term also dominates (DH)^(1/2). The predecessor's unconditional theorem therefore proves M2 in the remaining range. No subunit or infinite completion scale is discarded.

## 5. Exact projection consumer

Let labels be all distinct good sixth-power-free R with NR<=K<=D^(1/7), and require the existing Gram range K<=U^(1/2-delta0), with fixed delta0>0 and polynomially bounded punctures. The same primitive residue vector and actual adjoint identity as predecessor P14 give

\[
 \boxed{\ \|P_K A_U\overline b\|^2
 \ll(UDKNQ)^\epsilon\left[
 KU+D^{(13-2\beta)/12}U^{-(1-\beta)/3}K^{(15-2\beta)/12}
       +U^{1/3}D^{2/3}\right]. }                    \tag{M8}
\]

For U=D^h, 1/2<h<1, the middle term beats the inherited inverse nonvolume exponent 5/6+h/6 if

\[
 k<\frac{(3-2\beta)(2h-1)}{15-2\beta},\qquad K=D^k.
 \tag{M9}
\]

The other constraints remain k<5(1-h)/6, k<=1/7 and k<h/2, with strict room for small losses. At beta=1, M9 returns the predecessor's (2h-1)/13. For a concrete conditional example, assume M1 with beta=7/8 and choose U=D^(6/7), K=D^(1/24). The volume and nonvolume exponents are 151/168 and 7643/8064 respectively, both below the pole exponent 20/21. Consequently

\[
 \|P_K A_U\overline b\|^2\ll D^{20/21+\epsilon}.
 \tag{M10}
\]

This retains the earlier 1/42 saving against D^(41/42), on a larger label space than K=D^(1/32). It remains a conditional projection estimate. M1 does not imply a bound for (I-P_K)A_U conjugate(b), and no improvement of the complete inverse mean, B_flat, or RH is asserted.

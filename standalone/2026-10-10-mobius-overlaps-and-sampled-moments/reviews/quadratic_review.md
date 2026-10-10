# Independent review receipt: quadratic products and square-part interpolation

**Reviewer:** research subagent \(\texttt{/root/amplification}\), independently reviewing the root agent's quadratic component.

**Date:** 2026-10-10.

**Verdict:** PASS within the explicitly conditional mathematical scope below. No blocking mathematical defect was found in the reviewed version. One stale cross-file hash in the companion note must be updated before packaging; it does not change the verified algebra.

This is an attributable scoped review receipt, not a cryptographic signature or a certification of the imported analytic hypotheses.

## 1. Exact objects reviewed

The complete local mathematical target was read and independently reconstructed:

| Object | SHA-256 |
| --- | --- |
| attack3_quadratic.md | 7cc4f91049d6e8b22a24080099a2947e4f30d5be68ea050bb7bcdf52a94c0696 |
| attack3_quadratic_check.py | 622af30d6efd58eea1703b329799a9c6812568c12296e36d1d71eed682584ad0 |
| Normal replay, attack3_amp_quadratic_normal.json | 11abaa05d4e6399ee04f206632af0ca498c84a6fc655106c39e7674d70c30cfe |
| Optimized replay, attack3_amp_quadratic_optimized.json | 11abaa05d4e6399ee04f206632af0ca498c84a6fc655106c39e7674d70c30cfe |
| Author's existing attack3_quadratic_results.json | 11abaa05d4e6399ee04f206632af0ca498c84a6fc655106c39e7674d70c30cfe |

The companion attack3_moments.md was additionally read through its hypotheses, local correction, designated-factor proof, and degree-three application. The version consulted had SHA-256

    6cb26ad86f8d40453ff01287ad5312ecfba087eb1f509f4611cadb3036c6bfd4

The present review covers that companion only as needed to check the quadratic interface. It is not a full review of its later Hermitian and double-triangle theorems.

No target mathematical source or checker was edited by this reviewer.

## 2. Mathematical reconstruction

### 2.1. Sharp interval bounds from the reciprocal premise

Lemma 2.1 uses the stated uniform holomorphic reciprocal hypothesis \(\mathrm R_b\), with \(1/2<b<1\); it does not derive sharp cancellation from an arbitrary smooth-test estimate.

The finite excluded-prime correction is valid in the half-plane \(\sigma\ge b+\delta>0\). Its absolute value is at most \(\prod_{p\mid qS}(1-(Np)^{-b-\delta})^{-1}\ll_\epsilon(Nq)^\epsilon\): sufficiently large primes contribute at most \((Np)^\epsilon\), and the remaining finite product is constant. This preserves every moving exclusion.

Grouping ideals by integer norm gives \(|a_m|\le\tau(m)\). The substitution \(x_0=\lfloor x\rfloor+1/2\) preserves the sum and separates every integer norm from the Perron endpoint by at least one half. On \(x_0/2<m<2x_0\), the truncation kernel is bounded by \(O(x_0/(T|m-x_0|))\), which gives the stated harmonic loss. Outside this range, \(\sum_m\tau(m)m^{-c}=\zeta(c)^2\ll\log^2(2x_0)\), with \(c=1+1/\log(2x_0)\). These facts justify (2.4), rather than merely citing it without an endpoint check.

One can choose \(\delta<(1-b)/2\), then choose the small exponent in \(\mathrm R_b\) after fixing the polynomial height \(T=D^A\). The shift to \(b+\delta>0\) crosses neither a reciprocal pole nor the Perron pole at zero. The new vertical integral is \(O(x_0^{b+\delta}D^{o(1)}\log T)\); the horizontal and truncation terms are absorbed by sufficiently large fixed \(A\). Reassigning the small exponents gives the asserted \(D^\epsilon x^b\), uniformly in the declared polynomial range.

Taking differences gives interval sums. Partial summation supplies the supremum-plus-total-variation norm, and a norm modulation on a fixed positive annulus costs \(O(1+|t|)\). The proof therefore supplies the sharp dyadic test needed by the companion application. The case \(b=1\) follows from counting separately.

### 2.2. A physical product on squarefree rows

Lemma 3.1 correctly retains the full product of \(j\) squarefree-column sums. For each tuple, the exact incidence labels \(c_I\) are pairwise coprime, and the shared labels \(|I|\ge2\) are frozen before regrouping the singleton labels into one squarefree product column.

The frozen factors contribute literal row characters of modulus at most one, including zero-valued even-power masks. Dropping such a factor only enlarges a positive row norm. All column exclusions and all dependence of a factor's coefficient on its frozen shared ideals remain row-independent column coefficients.

For fixed shared data, the product column length is

\[
P_{\mathbf c}=P\prod_{|I|\ge2}(Nc_I)^{-|I|}.
\]

There are \(O_j(P_{\mathbf c})\) supported singleton tuples, up to fixed support constants. Each product ideal has at most a fixed-order ideal-divisor number of representations. Cauchy on each coefficient therefore gives squared coefficient mass \(O_\epsilon(D^\epsilon P_{\mathbf c})\). Applying the assumed squarefree quadratic sieve gives row norm

\[
\ll D^{\epsilon_0}\left(\sqrt{MP_{\mathbf c}}+P_{\mathbf c}\right).
\]

Minkowski over shared ideals is then legitimate. In the first term, pair labels have the critical harmonic weight \((Nc_I)^{-1}\), producing a logarithm over the polynomially bounded support; all higher multiplicities converge. In the second term, every shared-label exponent is at least two and converges. There are only finitely many labels for fixed \(j\). Squaring yields \(D^\epsilon(MP+P^2)\). No constant uniform in \(j\) is being inferred.

### 2.3. All nonzero rows and square parts

Every nonzero element row has a unique ideal factorization \(u=\varepsilon v^2a\), with \(a\) squarefree and \(v\) arbitrary. In particular, \((v,a)=1\) is not imposed. At a prime dividing both the column and \(v\), both sides of

\[
\rho_n(\varepsilon v^2a)
=\rho_n(\varepsilon a)\mathbf1_{(n,v)=1}
\]

are zero. Elsewhere the square factor has quadratic value one. This verifies the exact identity with the appropriate unit sector.

On \(Nv\asymp V\), there are \(O(V)\) choices for \(v\) and squarefree row length \(O(H/V^2)\). The physical-product sieve therefore gives \(HP/V+VP^2\). The uniform pointwise premise, with the moving exclusion \(q_iv\) retained, independently gives \(HR^2/V\) on the same row set.

The minimum can be bounded by

\[
\frac{HP}{V}+\min\left(VP^2,\frac{HR^2}{V}\right).
\]

Summation over dyadic \(V\) gives \(O(HP)\) for the first term. Splitting the other term at \(V_*=\sqrt H\,R/P\) gives \(O(\sqrt H\,PR)\). The geometric argument remains valid if the switch is below or above the physical range. The all-row pointwise bound separately supplies \(HR^2\). This proves precisely the minimum stated in Theorem 4.1.

For \(j=1\), the refined second term is \(\sqrt H L^{1+b}\). It is at most \(HL\) when \(H\ge L^{2b}\). The example \(b=7/8\) therefore gives the conditional sufficient height \(L^{7/4}\). For identical factors, substituting \(P=L^j\) and \(R=L^{jb}\) gives (4.9) directly.

### 2.4. Degree-three interface

The common factor in a degree-three sextic product carries \(\mu(c)\nu(c)^3\rho_c(u)\), so it is an inverse quadratic axis. The companion's forward correction retains disjointness from the residual columns before any norm estimate.

On \(Nc\asymp L\), the three residual pointwise bounds contribute \(D^{3b}L^{-3b}\). The refined quadratic row norm contributes

\[
\sqrt H\,L^{1/2}+H^{1/4}L^{(1+b)/2}.
\]

The correction weights on the common axis are \(1/2\) and \((1+b)/2\). Together with residual exponent \(b>1/2\), both satisfy the companion correction's convergence inequalities. The sharp dyadic norm modulation is a bounded-variation test, and its polynomial frequency cost is integrable against the original fixed smooth Mellin transforms. This is where the separate interval premise is necessary.

Geometric summation over the common-factor tail and squaring give

\[
D^{6b+\epsilon}
\left[HC^{1-6b}+\sqrt H C^{1-5b}\right].
\]

At \(b=7/8\), comparison with \(HD^3\) gives the two lower cutoff exponents \(9/17\) and \((18-4h)/27\). The former dominates on \(1<h\le11/10\). The displayed \(9/17\) is a common-factor cutoff, with no implication for a zero-free boundary or for the complementary singleton polynomial.

## 3. Checker inspection and independent replay

The source uses exact Python integers and Fraction arithmetic. Acceptance is enforced by explicit exceptions, so optimized Python cannot disable the checks. I inspected its primitive arithmetic and ran:

~~~sh
python attack3_quadratic_check.py --output attack3_amp_quadratic_normal.json
python -O attack3_quadratic_check.py --output attack3_amp_quadratic_optimized.json
cmp attack3_amp_quadratic_normal.json attack3_amp_quadratic_optimized.json
cmp attack3_amp_quadratic_normal.json attack3_quadratic_results.json
~~~

Both executions exited successfully. Both byte comparisons passed. The two independent replay outputs and the author's existing output have the identical hash listed above.

The exact finite coverage is:

| Guard | Cases |
| --- | ---: |
| Prime-ideal presentations | 6 |
| Six units | 6 |
| Square factorization | 81 |
| Quadratic square-part identities | 1,944 |
| Incidence character identities in degrees 1 through 4 | 30,940 |
| Nonunit principal-mask negative controls | 2 |
| Dyadic switch inequalities | 1,377 |
| Geometric diagonal sums | 1,377 |
| Degree-three affine endpoint certificates | 4 |
| **Total** | **35,737** |

The ring implementation is in the \(\omega^2+\omega+1=0\) convention: multiplication is \((a,b)(c,d)=(ac-bd,ad+bc-bd)\), with norm \(a^2-ab+b^2\). It is not accidentally using the alternative primitive-sixth-root convention. The proposed prime generators have norms 7 and 13 and vanish under the respective residue maps \(\omega\mapsto4\pmod7\) and \(\omega\mapsto9\pmod{13}\). Thus they generate the selected actual prime ideals.

For the incidence guard, rational integer rows 1 through 91 cover every pair of local residue values in the two selected residue fields by the ordinary CRT. This is complete coverage for that two-prime local panel. It is not an enumeration of every residue in \(\mathcal O_K/(91)\), nor an enumeration of all prime ideals.

The square-part tests include 1,080 cases where the square base overlaps the squarefree remainder. The dyadic panel includes 344 switches below, 385 inside, and 648 above its finite physical ranges. The two endpoint exponent certificates are exact and their corresponding expressions are affine in \(h\).

These finite guards do not prove Perron's theorem, the large sieve, the pointwise premises, any asymptotic moment estimate, or zero absence. Their role is to detect local normalization, mask, exponent, and endpoint errors.

## 4. Imported assumptions and packaging issue

The review treats the squarefree-index quadratic large sieve (QLS) as the explicitly stated imported input, with its fixed ray, unit, and bad-prime adapters. It does not provide a new proof of the external Goldmakher--Louvel theorem or independently re-establish the full referenced Hecke-family construction.

Likewise, \(\mathrm{PW}^{\mathrm{sm}}_b\) for \(b<1\), the uniform reciprocal premise \(\mathrm R_b\), and any common finite-order zero-free hypothesis invoked to obtain them remain analytic assumptions. The source-qualified value \(7/8\) is not independently certified here. Uniformity in polynomially growing conductor, rows, and exclusions is load-bearing.

The companion version consulted in Section 1 still names the older quadratic hash 2558fb58b2ffb3c4fde0ffd1a03dcab651bb3dfda609d456178aecd856bd1ee7 in its Section 5.2. This review instead binds the full current target hash 7cc4f91049d6e8b22a24080099a2947e4f30d5be68ea050bb7bcdf52a94c0696. The stale companion pointer was reported to the root for correction before freezing the final packet. No claim is made that this receipt authenticates a subsequently changed target without a further comparison.

**Smallest remaining mathematical gap:** the new bound handles the quadratic component and the specified common-factor tail. It gives no new estimate for the long fully singleton sextic core. A full generalized short-row moment or an improved zero-free half-plane would require a separate arithmetic estimate for that remaining family.

**Signed:** \(\texttt{/root/amplification}\), independent reviewer, 2026-10-10.

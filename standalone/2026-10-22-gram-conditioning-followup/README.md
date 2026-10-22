# Proved Gram conditioning and the remaining inverse-moment problem

22 October 2026. **Proposed analytic research packet. No smaller zero-free boundary has been proved.**

This follow-up removes an explicit Gram-conditioning hypothesis from an existing projected sextic Kubota calculation. It also proves a stronger conditioning range with growing prime exclusions and records an exact cancellation identity for the next operator step. The new conditioning theorem uses no zero-free hypothesis.

The numerical reference remains the source-dependent value

\[
B_{\mathrm{flat}}=0.874886647039964\ldots
\]

recorded in the [preceding packet](../2026-10-22-signed-boundary-attempt/README.md). Its proposed `0.8745` target is still conditional on the unproved high-conductor inverse moment. Neither the present Gram theorem nor the projected-operator consequence proves that moment.

## 1. The strongest new estimate

Work over the Eisenstein field. For distinct sixth-power-free good ideal labels \(NR\le K\), use squarefree good row ideals \(z\), a fixed nonnegative annular weight \(w\), and the original zero-extended sextic residue symbols. Let \(Q\) be a growing prime-exclusion ideal and define

\[
G_{R,S}=\frac1U\sum_{z\text{ squarefree}}w(Nz/U)
 \mathbf1_{(z,Q)=1}\chi_z(R)\overline{\chi_z(S)}.
\]

Its exact diagonal main term is

\[
D_{R,R}=c_w\prod_{\mathfrak p\mid 6QR}
                  (1+(N\mathfrak p)^{-1})^{-1},
\qquad
c_w=\frac{\operatorname{Res}_{s=1}\zeta_E(s)}{\zeta_E(2)}
                          \int_0^\infty w(x)\,dx.
\]

For every fixed \(0<\delta<1/2\), \(A\ge0\), and \(\epsilon>0\),

\[
\boxed{
 K\le U^{1/2-\delta},\quad NQ\le U^A
 \quad\Longrightarrow\quad
 \|G-D\|_{\mathrm{op}}
       \ll_{w,\delta,A,\epsilon}(UKNQ)^\epsilon\frac K{\sqrt U}.
}
\]

Consequently, for sufficiently large \(U\),

\[
\|G\|_{\mathrm{op}}+\|G^{-1}\|_{\mathrm{op}}\ll_\epsilon U^\epsilon.
\]

The theorem retains primes where the primitive conductor cancels but the original symbol is still zero. It permits any subset of distinct permitted labels, but does not permit arbitrary deletion of rows or duplicate labels. Invertibility is an asymptotic conclusion, not a statement about every small annulus.

The complete proof is in [HYPERBOLIC_PUNCTURE_GRAM.md](HYPERBOLIC_PUNCTURE_GRAM.md). It uses de Faveri's stated sixth-power-free sextic sieve, ordinary lattice Poisson summation, and elementary ideal counting. The squarefree and puncture expansions are kept signed in the short part. Their complementary part is bounded by the supplied positive sieve. Choosing the short part by \((Nd)^2Ne\le L\) gives the same summable divisor weight \((Ne)^{-1/2}\) in all four tail terms, which preserves the claimed rate for growing \(Q\).

## 2. An independent proof in a smaller range

[GRAM_CONDITIONING.md](GRAM_CONDITIONING.md) proves

\[
\|G-D\|_{\mathrm{op}}
 \ll_\epsilon(UKNQ)^\epsilon U^{-1/2}K^{3/2}.
\]

This gives conditioning for \(K\le U^{1/3-\delta}\), also with polynomially growing \(Q\). Its analytic inputs are the standard finite-order Hecke functional equation and convexity. It does not use the new sextic sieve or a quasi-RH premise. The proof distinguishes the primitive conductor from the full prime-exclusion mask and uses an Euler-convergent reciprocal only to the right of one.

## 3. A hypothesis removed from an existing operator consequence

For the actual Gauss vectors of rStation paper 10, version 2, Section 8, take \(U=X\), \(Q=1\), and the common phase \(u(z)=\gamma_1(z)\). The preceding results prove the Gram assumption that the source leaves explicit. With its primitive Kubota mean still retained as a separate analytic input, the source's actual projection \(P=VG^{-1}V^*\) therefore satisfies

\[
\|A^*PA-WG^{-1}W^*\|
 \ll_\epsilon(XK)^\epsilon
           \bigl(X^{13/12}K^{3/4}+XK^{3/2}\bigr).
\]

Here \(W\) is precisely the source's theta-residue matrix. At \(K=X^{1/9-\kappa}\), \(0<\kappa<1/9\), this becomes

\[
\|A^*PA-WG^{-1}W^*\|
            \ll_\epsilon X^{7/6-3\kappa/4+\epsilon}.
\]

The extra Gram hypothesis has been discharged; the imported Kubota mean has not been reproved. Extending the conditioning range alone does not improve the projection's separate contour-error estimate. In particular, the complementary operator \(A^*(I-P)A\) is still uncontrolled at the strength required by the zero-free detector.

## 4. The next operator step is stated exactly

[INTEGRATED_SMOOTHING_AND_OPERATOR_GAP.md](INTEGRATED_SMOOTHING_AND_OPERATOR_GAP.md) proves a finite dyadic operator bound and an integrated pole-cancelling identity. For moduli \(Nc\asymp L\), arbitrary label coefficients, and \(K\le L\le\sqrt{XK}\), \(K\le X^{1/3}\), the finite kernel obeys a squared norm bound \(\ll (XK)^\epsilon XK^{1/6}\). It is not a bound for the full continued series.

Integrating the smoothed polynomial cancels every modulus below the support scale. The contour shift for the full remainder is justified only after restoring the source's zeta completion. Removing that completion on the original contour gives an exact sum over the smaller scales \(U/(Na)^6\), with coefficient \(\mu(a)/(Na)\). Choosing matching smoothing lengths cancels the completion in the polynomial part by divisor inversion, but leaves a sum of continued remainders that cannot be bounded by the same absolute argument on the shifted contour.

The primitive-inversion step also changes the numerator from \(r\) to \(rd^2\) and the reflected dual length to \(Nr(Nd)^4/U\). The source's separate-label Cauchy argument does not preserve arbitrary label combinations through that change. No estimate closing either remaining step is claimed here.

## 5. Source, review, and verification boundaries

The base repository snapshot is `22c0532850ebcec04e0772b6b68f92dc18fc252c`, the reviewed head of the preceding packet in draft PR #1013. This directory contains new proposed mathematics; it does not alter the preceding frozen claims or the integrated repository baseline.

Primary sources and a version-pinned source hash are recorded in [SOURCE_MANIFEST.json](SOURCE_MANIFEST.json). The proofs are analytic. No numerical mesh, finite zero search, floating-point calculation, or proof-assistant verification is used to establish their conclusions. Source-specific finite identities and the full continuous exponent ranges are checked in the accompanying independent reviews.

The [review record](REVIEW.md) is added after the mathematical snapshot is frozen. It identifies exact source commits, reviewed files, authorship exclusions, imported dependencies, and the unchanged open high-conductor estimate. Agent review does not certify the imported papers as a whole or substitute for a complete proof of the numerical boundary.

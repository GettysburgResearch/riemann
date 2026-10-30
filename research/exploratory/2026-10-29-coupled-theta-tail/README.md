# Coupling the cube prefix to the completed theta polynomial

**Status.** The estimate below is a source-qualified partial bound, not a new zero-free region or an inverse-moment bound. It assumes the October 5 cube-completion identities, fixed-sector reciprocity/orientation, de Faveri's printed sixth-order sieve, and the physical source/sector/Poisson/Fourier and principal-restoration ledger cited in [the square-part tail](../2026-10-29-squarepart-stratified-tail/README.md). The imported source and physical matching are not independently verified here.

Let the actual good sixth-free \(b\)-rows have norms \(\ll B\), fix \(k\), and take a good squarefree label \(f\) with its original masks. Let
\[
 A_b(H)=\sum_{Nh\ll H}\mu(h)\overline{\alpha(h)}^3\xi(h)^3
 \chi_h(bk)^3\mathbf1_{(h,f)=1}\,a_H(h)
\]
with a common bounded smooth profile, and let \(T_{bk}(X;f)\) be the source completed theta sum. The same notation includes its logarithmic profile derivative. At a dyadic cube scale \(H\), the source kernel has \(X=D/H^3\).

## Coupled large-sieve estimate

After fixing the completed-theta cube index \(q\), its factor \(\chi_q(bk)^3\) is a bounded row contraction and its exterior coefficient has modulus \(\ll1/Nq\). The remaining theta polynomial is over squarefree \(n\), with normalized squared coefficient mass \(\ll Y^\epsilon\), and has a common column multiplier including the fixed \(k,f\) masks. The prefix and this polynomial multiply as
\[
 \chi_h(bk)^3\chi_n(bk)=\chi_{h^3n}(bk).
\]
The equality includes all original zeros. Since \(h,n\) are squarefree, every prime exponent of \(h^3n\) is \(0,1,3\) or \(4\), so the resulting column is sixth-free. Its norm is \(\ll H^3X=D\); its squared coefficient mass is \(\ll H Y^\epsilon\) by the divisor bound and the normalized theta coefficient mass. The \(k\)-factor and the remaining fixed masks are common column multipliers. Apply \(\Theta_6\) to the actual \(b\)-rows, sum the fixed q pieces by Minkowski with \(\sum_{Nq\ll X^{1/3}}1/Nq\ll Y^\epsilon\), and obtain
\[
 \sum_b|A_b(H)T_{bk}(X;f)|^2
   \ll Y^\epsilon H\,\Theta_6(B,H^3X). \tag{1}
\]
The same bound holds for the common differentiated theta profile. No factorization of row-dependent masks is used. The displayed orientation is essential; a conjugated or differently powered theta symbol needs a separate compatibility proof.

Stieltjes partial summation of the cube tail, dyadic decomposition and (1) therefore give, for \(1\le C\le D^{1/3}\),
\[
 \|\text{tail}_{>C}\|_{\ell^2_b}^2
 \ll Y^\epsilon C^{-1}\Theta_6(B,D).\tag{2}
\]
Indeed each dyad contributes to the norm at most \(H^{-1}\sqrt{H\Theta_6(B,D)}\), and the dyadic sum is \(\ll C^{-1/2}\sqrt{\Theta_6(B,D)}\). The source short part remains
\[
 \|\text{short}_{\le C}\|_{\ell^2_b}^2
 \ll Y^\epsilon\left(BK+\frac{B^2K^2Nf}{D}C^3\right).\tag{3}
\]
For the physical mask divisor e, \(D_e=D/Ne\), \(f_e=fe\), and the exterior factor has squared mass \((Ne)^{-1}\). If \(Ne\le C^3\), use \(C_e=C/(Ne)^{1/3}\): (3) is bounded by its e=1 expression and (2) contributes at most \((Ne)^{-2/3}\Theta_6(B,D)/C\). For \(Ne>C^3\), use the direct sixth-order sieve, bounded by \(C^{-3}\Theta_6(B,D)\). The divisor sum is a subpower. Thus no guard on the moving e is silently assumed.

Put \(W=B^2K^2Nf/D\), \(Q=\Theta_6(B,D)\), and \(C=(Q/W)^{1/4}\). If \(1\le C\le D^{1/3}\), (2)–(3) give
\[
 \|\text{short}+\text{tail}\|_2^2
 \ll Y^\epsilon\bigl(BK+W^{1/4}Q^{3/4}\bigr),\tag{4}
\]
plus the large-e fallback \(C^{-3}Q\) if the physical support does not guarantee \(Ne\le C^3\). Outside this C range, a clipped cutoff or the direct sieve must be used separately. This is a positive estimate for the relevant completed square; the separately identified signed-diagonal and source-restoration conditions still apply to the physical ledger.

## Scalar check and limitation

At the E21 unit corner \(d=7/50,\ \kappa=g=0\), \(D=Y^{53/50}\). In the interior-crossover regime and when the e guard holds, insertion of (4) into the standard physical prefactor gives exponents approximately \(1.07833\) at \(b=.95\) and \(1.1075\) at \(b=1\). The latter improves the corresponding unstratified positive-moment estimate but both exceed \(21/20\). The exact point \(d=13/100,b=24/25,\kappa=g=0\) also remains above \(21/20\). These examples are evaluations of this particular upper bound; they neither rule out sharper use of the sparse \(h^3n\) support nor prove anything about the size of the actual signed sum.

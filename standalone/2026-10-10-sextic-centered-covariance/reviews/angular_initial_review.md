# Independent audit of the fixed angular cubic theta adapter

**Reviewer:** replica_extraction_attack, independent of the author of centered_a2_attack.md.

**Checkpoint status:** Sections 2–5 of the draft at SHA-256 3778538b60ea92cae9d16819c12d35599706033623797ffa7a0d5eba2109ae30 have been checked against the named source formulas. The angular algebra and completed mean-square adapter pass at the scope specified below. One canonical-domain correction has been requested: use Sigma=XF, as in the imported canonical proposition; Sigma>=XF alone is the separate transfer-envelope condition and is not the literal canonical theorem.

**Reviewed source:** /workspace/scratch/6ec6134c1535/centered_a2_attack.md, Sections 2–5 at the preceding hash.

**Exact imported analytic dependency:** OpenAI/math adc7f1241b42e322a6451854ab7e4b4c146bf78a, preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex. The review checks a new adapter to that proof; it does not independently establish the imported scalar cubic theta automorphy, cusp coefficient estimates, classical quadratic large sieve, or original finite transfer induction.

## 1. Pure horizontal derivatives

For a fixed nonzero integer r and m=|r|, the proposed formula

\[
\mathscr D_r F(g^{-1}(z+a/c,v))\big|_{z=0}
=(-1)^m\alpha(c)^{2r}N(c)^{-m}v^{-2m}
\mathscr D_{-r}F(-d/c,1/(N(c)v))
\]

is correct. In the pure Wirtinger Taylor jet with the other variable set to zero, the transformed height is constant and the relevant horizontal coordinate is affine. All mixed terms in the true smooth Taylor expansion contain the other Wirtinger variable and vanish in this pure jet. The argument requires only fixed-order smoothness, not holomorphy. There are no lower derivative or height derivative terms.

The source automorphy multiplier is explicitly scalar and independent of the horizontal and height coordinates. Thus it is not differentiated. This point is an input from eq:theta-cusp-automorphy; it would fail for a nonconstant weight multiplier without an additional calculation.

## 2. Mellin factors and reflection

Differentiating the source Fourier mode supplies

\[
(2\pi i)^m|\ell|^m\alpha(\ell)^r.
\]

Against the height measure v^(2s+m-2)dv and the source coefficient vK_(1/3)(4pi|ell|v), the resulting factor is exactly

\[
\frac{i^m}{4(2\pi)^{2s}}
\Gamma(s+m/2-1/6)\Gamma(s+m/2+1/6)
\alpha(\ell)^rN(\ell)^{-s}.
\]

Since alpha(lambda^-3)=i and N(lambda^-3)=1/27, the initial Mellin scalar is exactly epsilon_r=i^(m+r). The reflected scalar reduces to i^r/81; in particular r=-1 gives the source's -i/81.

Under v=(N(c)v')^-1, the radial factor is

\[
N(c)^{-m}v^{2s-m-2}\,dv
=N(c)^{1-2s}(v')^{2(1-s)+m-2}\,dv'
\]

after reversing the integration bounds. Therefore the conductor power is unchanged and no hidden factor N(c)^m is paid.

For each fixed finite twist the horizontal derivative annihilates the constant Fourier term at every relevant cusp. The nonzero cusp modes and each fixed derivative decay exponentially at both ends after inversion. Thus the Mellin transform is entire for r nonzero. The stated gamma quotient has first numerator pole at -(m+1)/2+1/6, which lies at or left of -5/6; moving its contour from Re t>1/2 to Re t=0 introduces no residue. This checks removal of the constant cusp mode in this specific reflected family. It is not a new theorem about residues in arbitrary angular metaplectic families.

## 3. Finite local transforms and moving conductors

The source explicitly fixes the initial finite Fourier index h_0 and the active prime set before summing over the nonzero h_p. Within that grouping the reduced denominator c=c_0 times the active prime product is fixed. Hence alpha(c)^(2r) can be factored out of the local transform exactly. The source's B_(p,j), including the j=0 mask and the j=4 Ramanujan term, are unchanged.

For the prepared squarefree row k_0, every row prime is active, and c=c_*k_0. The new denominator phase therefore has the form alpha(k_0)^(2r) times a fixed phase. The source preparation already allows an arbitrary bounded scalar depending on k_0; this is permitted without claiming that the phase is a ray character.

The dual index phase alpha(ell)^(-r), with ell=u lambda^j n b^3, separates into unit, ramified, squarefree-column, and cube-column factors. These factors are independent of k_0 and have modulus one. The coefficient vector in the quadratic sieve is arbitrary, so its norm bound is unchanged. When a fixed active prime is extracted from n or b, the extra angular phase can remain in the new bounded coefficient vector. No additional row dependence or conductor factor appears.

The final decomposition k=u_0 s v^2 is unique in the source ideal-generator convention, with all six units and no artificial condition (s,v)=1. The auxiliary update f to fv^2 uses 8 congruent to 2 modulo 6 and is valid at character zeros. It is independent of r, and its v-norm sum is still zeta_K(2). This proves the adapter to the completed mean square, conditional on the named imported estimates.

## 4. Two-Poisson closure and the domain correction

The first paired Gauss identity is multiplied by alpha(u_1/u_2)^(r+1). Common-divisor phases cancel against their conjugates. The intermediate Möbius coefficient is consequently

\[
\mu(n)\xi_1(n)\alpha(n)^{r+1}
\mathbf1_{(n,t)=1}\overline{\chi_n(y)}
\chi_n(C)^4\chi_n(d).
\]

The source's second Poisson identity has the opposite row-character orientation and returns a_(r,xi)(n), not a different growing angular order. Exclusions, finite ray expansions, smooth norms, and signed prime regrouping are unchanged. The cube inversion follows by the same finite Dirichlet convolution with alpha(h)^(3r), including all masks.

The imported canonical proposition is stated for

\[
\mathcal H,X,F\ge1,\qquad \Sigma=XF,\qquad
\mathcal H\le\Sigma D^{-\kappa}.
\]

The draft's phrase Sigma>=XF is too broad if used in place of that equality. The transfer proposition does permit a separate larger envelope, but its existence alone does not extend the canonical theorem to every such envelope. The author was notified to retain the exact canonical equality. Once corrected, the stated proof adapter preserves every scale exponent of the imported finite induction.

## 5. Scalar consequences not yet included in this checkpoint

The original inverse coefficient mu(n)nu(n)alpha(n)^t has initial Gauss order r=-t-1 after the source's initial row Poisson and conjugation convention. In particular the proposed angular factor t=-3 corresponds to r=2, so the missing r=0 case does not block that application.

This checkpoint does not yet review a uniform scalar saving, an all-negative balanced-component estimate, a generalized moment bound, or a new zero-free boundary. Those require the actual stated consequences and their scale conditions. A finite-character reciprocal estimate cannot be silently applied to alpha^-3; the angular character and its conductor uniformity must be supplied separately.

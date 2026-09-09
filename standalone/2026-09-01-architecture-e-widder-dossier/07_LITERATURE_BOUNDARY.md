# Literature boundary and comparison notes

Status: **BIBLIOGRAPHIC ORIENTATION, NOT AN EXTERNAL PRIORITY CLAIM.**

This note records the classical and recent literature interfaces used during the Architecture-E passes.  Exact bibliographic data and theorem numbers should be independently checked before publication outside the repository.

## 1. Widder and Sokal: the scalar endpoint

The load-bearing classical theorem is D. V. Widder's 1938 characterization of Stieltjes transforms.  A modern proof and generalized formulation is:

- Alan D. Sokal, *Real-variables characterization of generalized Stieltjes functions*, arXiv:0902.0065.

For ordinary Stieltjes functions, Sokal's Theorem 1 records the equivalent conditions

\[
 F_{n,k}(u)=(-1)^nD^{n+k}[u^kf(u)]\ge0
 \qquad(n,k\ge0),
\]

and the reduced Widder family

\[
 f(u)\ge0,
 \qquad
 F_{k-1,k}(u)
 =(-1)^{k-1}D^{2k-1}[u^kf(u)]\ge0.
\]

The E–Widder criterion is an application of this theorem to the invariant logarithmic derivative

\[
 q(u)=2\mathfrak X'(u)/\mathfrak X(u),
 \qquad
 \mathfrak X(s(s-1))=\xi_{\rm R}(s).
\]

The invariant-coordinate application and its Euler-safe source formula are the proposed new deductions in this dossier; Widder's theorem itself is classical.

## 2. Hermite–Biehler and de Branges

The companion quotient

\[
 \Theta_\lambda=
 \frac{X-i\lambda X'}{X+i\lambda X'}
\]

is naturally governed by Hermite–Biehler/de Branges theory.  The dossier does not claim a new abstract de Branges equivalence.  Its contribution is to identify the exact source-side kernel and arithmetic realization that must be made positive:

\[
 \mathcal B_X(z,w)
 =\frac{X'(z)X(\bar w)-X(z)X'(\bar w)}{\bar w-z}
\]

and

\[
 \mathcal A_\Phi(a,b)
 =\frac12\int_{|a+b|}^{\infty}\xi H_\xi(a-b)\,d\xi.
\]

The proof burden is not the abstract implication from a positive de Branges kernel to real zeros; it is the arithmetic proof that this particular source kernel is positive.

## 3. Generalized Schur and Pontryagin spaces

The negative-square interpretation belongs to generalized Schur/Nevanlinna and Pontryagin-space theory.  The source-specific theorem in the dossier is the feature decomposition showing that each distinct nonreal conjugate zero pair contributes one negative direction to the Hermite kernel.

Multiplicity requires care: the reduced companion sees distinct locations.  No external claim of a new general Krein–Langer theorem is made.

## 4. Pólya-frequency and total-positivity lineage

Classical work of Pólya, Schoenberg and later authors relates totally positive kernels, Laguerre–Pólya entire functions and variation diminution.  This motivates Architecture A but does not complete it.

The key boundary established here is elementary and exact:

```text
PF_infinity is closed under convolution and suitable limits;
PF_infinity is not closed under arbitrary positive addition.
```

Therefore a theta sum cannot be proved totally positive merely by proving every mode totally positive.

A recent primitive-cycle construction invokes precisely such a positive-sum step:

- a 2026 manuscript on the Riemann Xi function from primitive Markovian cycles, cited and audited in predecessor PR #784.

The dossier's counterexample concerns only the total-positivity closure step.  It does not adjudicate the manuscript's separate Mellin or completion calculations.

## 5. Wigner positivity and Hudson's theorem

The source current can be written through the Wigner transform of `Phi`.  Pointwise Wigner positivity would make several signs immediate, but Hudson's theorem says that an everywhere nonnegative pure-state Wigner distribution must be Gaussian.  The Riemann theta kernel is not Gaussian.

This is a scope firewall: the desired positivity must arise after the global weighted integration, not pointwise in phase space.

## 6. Suzuki and canonical-system programmes

Suzuki's work on canonical systems associated with the Riemann xi function constructs positive systems in safe parameter ranges and identifies continuation into the remaining region as an RH-bearing frontier.  Architecture E is compatible with that viewpoint but removes one layer of abstraction at zero Weyl frequency:

\[
 \mathcal A_\Phi=4K_0,
\]

and the double Fourier transform of `A_Phi` is already the Hermite kernel.  A future canonical-system completion must therefore factor this exact kernel, not merely an asymptotic or source-blind surrogate.

The dossier does not claim to supersede or complete Suzuki's programme.

## 7. Safe-line Hausdorff and Loewner literature

The integrated repository contains exact safe-line Hausdorff, Pick, Loewner, radial and Green-removal transforms.  These results sit naturally in the classical theory of Stieltjes functions, operator monotone functions and complete Bernstein functions.

The exact identity

\[
 \mathcal H[\mathbf x]
 =L_{tp}[\mathbf t]-D_xL_p[\mathbf t]D_x
\]

makes that relation explicit.  Under a positive Stieltjes measure, both Loewner terms are Gram matrices.  The all-order operator-monotone conclusion remains equivalent to RH; fixed finite order is not enough.

## 8. Recent theta-kernel differential inequalities

Recent work proves strong first- and second-level differential inequalities for the Riemann theta kernel, including log-concavity/Turán-type statements.  Such results are relevant evidence for the low-order source geometry.

They do not directly imply the E–Widder hierarchy, which is an all-order linear differential condition on the logarithmic derivative of the completed transform in the invariant coordinate.  A future proof must provide an explicit transfer theorem rather than treating source concavity as synonymous with transform Stieltjes positivity.

## 9. Segre/Gorenstein and cohomological analogies

The Segre/Chow resolutions on #769 and #781 use standard commutative algebra and algebraic geometry: Cohen–Macaulayness, Gorenstein duality, Koszul/Tor complexes and equivariant K-polynomials.

These results explain reciprocal symmetry.  The comparison with Weil-style proofs over finite fields highlights the missing ingredient: a polarized cohomology with a normal Frobenius-type operator and a purity theorem.  The dossier makes no claim that the existing Tor complex is already such a cohomology.

## 10. Exact citation policy for later publication

Before any external paper or public proof claim:

1. pin exact bibliographic data for Widder's 1938 theorem and Sokal's modern proof;
2. cite the precise Hermite–Biehler/de Branges and Krein–Langer results used;
3. identify the exact Hudson theorem normalization;
4. audit the current versions of the Suzuki and recent 2026 manuscripts;
5. separate new-in-repository deductions from externally new results;
6. obtain independent review of every analytic interchange and infinite-product argument.

No novelty or priority conclusion is made by this packet.

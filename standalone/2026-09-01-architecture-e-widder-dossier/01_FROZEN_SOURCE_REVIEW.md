# Frozen proof-oriented review of PRs #765, #766, #769, #770, and #781

Status: **REVIEW AND SYNTHESIS; SOURCE CLAIM STATUSES ARE NOT UPGRADED; RH AND GRH REMAIN UNPROVED.**

This note records the mathematical assessment that led to Architecture E.  It is deliberately theorem-oriented: it does not repeat the long computational campaigns already present on the source branches, and it does not infer infinite or analytic conclusions from finite exact atlases.

## 1. PR #765 — the correct RH-sensitive endpoint, but no sign supplier

Let

\[
 X(z)=\xi_{\rm R}(1/2+iz)
\]

and, for fixed `lambda>0`,

\[
 \Theta_\lambda(z)
 =\frac{X(z)-i\lambda X'(z)}
        {X(z)+i\lambda X'(z)}.
\]

The most important correction on #765 is conceptual: for the actual centered Xi function, holomorphic Schur contractivity or innerness of this raw quotient is already RH-equivalent.  A nonreal zero of `X` produces an interior modulus-one point after removable common-factor cancellation, which a nonconstant Schur function cannot have.  Thus raw-innerness is an endpoint criterion, not an independent mechanism that reduces RH.

The finite companion and transport calculations are genuine structure, but they do not provide the missing all-order sign:

- the fixed-calibration companion panels certify many exact local alignments;
- the joint-polynomial transport improves the old separate-triangle estimate;
- eight whole-circle transports are certified in the reviewed panel, while eighteen points remain unresolved;
- sparse dyadic width panels carry only `O(j)` nodes at weight about `2^{-j}`, so their total cofinal mass behaves like `sum j 2^{-j}` and converges;
- consequently a sparse transport argument cannot furnish the divergence or completeness needed to force zero negative squares.

The odd-current, double-scaling and radial-semigroup limits identify real local asymptotic geometry.  Their leading Gaussian/Bessel/heat behavior is nevertheless universal.  The compact-perturbation firewall constructs positive smooth kernels with the exact Xi tail and the same high-frequency asymptotics but with a nonreal zero and wrong-sign Laguerre curvature.  Therefore:

```text
positive kernel
+ exact Xi tail
+ local saddle concentration
+ radial/Bessel asymptotics
    does not imply real zeros.
```

The sign must retain global arithmetic interference.

### Review conclusion for #765

#765 identifies the right endpoint objects:

- the raw companion generalized-Schur kernel;
- the Hermite/Laguerre curvature;
- the literal theta source coordinates `H_xi(d)`;
- the high-order and radial localizations.

It does not prove the global source polarization that forces the endpoint sign.

## 2. PR #766 — ordinary positive-source Mellin theory is too weak

The source quotient on #766 is mathematically natural.  For a positive source operator `H` and quotient map `pi`, its minimum-energy quotient is

\[
 H_Q=(\pi H^{-1}\pi^*)^{-1}.
\]

It has the expected universal property, nested quotient coherence, reflection behavior, and declared direct-sum/tensor compatibilities at the source level.

The decisive theorem is negative for naïve Architecture A: inside the native level-one theta family, a proper coefficient-source quotient has a reflected real off-central zero pair for every depth `j>=1` and every even weight `k>=96j`.  Thus even the conjunction

```text
actual positive theta source
+ source-defined minimum-energy quotient
+ reflection / functional equation
+ positive Mellin kernel
```

does not select central-line zeros.

This is stronger than a synthetic counterexample.  It occurs in the native arithmetic theta-source family and therefore rules out any proof that uses only those listed properties.

The source quotient also exposes a structural mismatch:

- source tensoring is not scalar Mellin multiplication;
- Schur elimination is not naïve averaging;
- the difference is a nonnegative lift-variance term;
- source positivity can be destroyed or misread by applying the observation or quotient in the wrong order.

### Review conclusion for #766

Architecture A survives only after replacing scalar or pointwise source positivity by a genuinely two-variable polarization, total-positive canonical system, or equivalent Gram theorem.  The missing theorem must be stronger than every positive-source property already enjoyed by the native counterexamples.

## 3. PR #769 — a real Segre/Chow source resolution

The ternary coefficient-cube calculation on #769 is a substantial exact algebraic result.  Over the ten-variable Chow base, it gives the explicit self-dual minimal resolution

\[
 \begin{aligned}
 F_0&=S\oplus S(-1)^{17}\oplus S(-2)^{11},\\
 F_1&=S(-2)^{20}\oplus S(-3)^{65},\\
 F_2&=S(-4)^{65}\oplus S(-5)^{20},\\
 F_3&=S(-5)^{11}\oplus S(-6)^{17}\oplus S(-7).
 \end{aligned}
\]

The actual 379-term top relation supplies the previously missing final map.  The Hadamard numerator is thereby realized as an alternating equivariant Tor character, not merely fitted as a reciprocal polynomial.

The self-duality is genuine.  It explains palindromy and functional-equation-type reciprocity through Gorenstein duality.  It does not manufacture:

- a positive Hermitian form;
- a Frobenius or archimedean operator normal for that form;
- tempered eigenvalues;
- a completed number-field trace formula;
- arithmetic purity.

A separate matrix-factorization example shows that every equivariant Tor trace can vanish while the modules and infinite resolution remain nonzero.  Euler-characteristic cancellation therefore cannot stand in for polarized cohomology.

### Review conclusion for #769

The syzygy programme has an authentic categorical skeleton.  Its role in an RH proof would be to organize exterior powers, determinants, or a future cohomological realization.  It currently supplies duality, not purity.

## 4. PR #770 — source faithfulness is a load-bearing constraint

#770 proves several reasons that quotient-first or observation-first estimates can lose exactly the powers needed for an RH sign.

The reviewed results include:

- quotienting the ordered-word carrier changes diagonal weights by factorial factors;
- principal recombination can amplify a diagonal by a power of the horizon;
- ratio-masked gauge inversion has a cofinal lower bound of the form `H^{1/12-o(1)}`;
- a fixed selected twenty-row physical minor becomes singular at infinite horizon, with limiting rank at most fifteen;
- finite-horizon faithfulness does not automatically yield a stable all-future decoder;
- a separate full-support positive row family can distinguish the entire finite tensor carrier, but this does not identify the full all-prime retained-gamma map.

The correct methodological rule is therefore:

> Assemble the complete signed source, with its labels, endpoint conventions, gamma factors, aliases and connection terms, before applying a norm, quotient, gauge inversion or principal readout.

A positivity statement proved only after a nonorthogonal compression is not automatically positivity of the original source form.

### Review conclusion for #770

Any Architecture-E proof must establish positivity before non-source-faithful projection, or carry the complete connection and metric through the projection.  This is why the final formulation below is kept either as a literal two-variable source kernel or as an absolutely convergent prime-shift quadratic form.

## 5. PR #781 — duality and moduli are real, but walls are not protected

The Segre-defect work on #781 identifies the coefficient-power defect with an equivariant Segre K-polynomial and proves a deformation-spectrum factorization.  Reciprocal spectral pairing is automatic; critical-circle purity is equivalent to a separate temperedness inequality.  This is an exact formulation of the missing step:

```text
self-duality / functional equation   automatic from geometry;
purity / critical-circle spectrum   additional positivity or temperedness.
```

The graph, deformation and torsion atlases are valuable theorem-generating data, but they do not supply a number-field purity functor.

The Epstein laboratory is a direct obstruction to a broad wall-protection architecture.  It contains arithmetic completed theta/Epstein objects with certified real and complex off-critical zeros.  Consequently

```text
arithmetic origin
+ theta representation
+ functional equation
+ analytic deformation family
```

does not isolate a protected critical-line chamber.

A moduli proof would require a discrete invariant that distinguishes the Riemann source from those arithmetic counterexamples.  None of the reviewed branches currently supplies such an invariant.

### Review conclusion for #781

Architecture C is presently the weakest path.  Architecture D remains mathematically serious but requires a polarized realization, not further reciprocal numerator identities alone.

## 6. Assessment of the four proposed architectures

### Architecture A — positive source to de Branges

As originally stated, this architecture is false.  #766 provides native positive-source quotients with off-central zeros.

The viable repair is

\[
 \Phi
 \longrightarrow
 \mathcal A_\Phi(a,b)
 \longrightarrow
 \mathcal A_\Phi\succeq0
 \longrightarrow
 \mathcal B_X\succeq0
 \longrightarrow
 \mathrm{RH}.
\]

The new ingredient is a two-variable Gram property, not positivity of `Phi` or of a scalar Mellin kernel.

### Architecture B — generalized Schur negative squares

This is the best exact endpoint.  The companion Schur kernel is a diagonal congruence of the Xi Hermite–Bezout kernel, and its negative index counts distinct upper-half-plane zero locations.  The difficult part is not the index dictionary; it is proving zero index from the arithmetic source without writing the zero product back into the proof.

### Architecture C — moduli and wall protection

The Epstein certificates show that arithmetic completed theta objects can occupy off-line chambers.  A wall proof needs a new invariant, not merely connectedness, self-duality or arithmetic provenance.

### Architecture D — syzygy source plus purity

The Segre/Chow resolutions give the functional-equation half of a cohomological story.  A proof still needs a global realization with a positive polarization and a normal local/global operator whose spectral temperedness yields the critical line.

## 7. Architecture E selected by the review

The strongest synthesis is

\[
 \boxed{
 \text{actual theta source}
 \to
 \text{Hermite–Bezout source polarization}
 \to
 \text{safe-axis Stieltjes/Pick structure}
 \to
 \text{zero negative squares}
 \to
 \mathrm{RH}.
 }
\]

Its advantages are:

1. it is attached to the literal Riemann theta source;
2. it has an exact RH-sensitive endpoint;
3. it respects the source-order warnings of #770;
4. it converts the missing theorem into a single explicit positivity problem;
5. it admits both a source-kernel form and an absolutely convergent prime-side form.

Its danger is equally clear: once the source kernel is shown equivalent to RH, merely renaming its positivity as a contraction, purity statement, canonical-system condition, total positivity or Stieltjes measure does not advance the proof.  The next step must prove one of those equivalent properties from genuinely simpler arithmetic structure.

## 8. Imported versus review-derived conclusions

### Directly imported

- all finite/exact computations and certified counterexamples from the five frozen source heads;
- the native positive-source quotient theorem and its off-central zeros;
- the explicit ternary resolution and top relation;
- source-faithfulness and gauge/observation lower bounds;
- the Epstein wall certificates;
- the integrated low-order Xi Pick and safe-line results on `main`.

### Derived in the review

- the comparative rejection or repair of Architectures A–D;
- the identification of the Hermite–Bezout kernel as the common endpoint object;
- the requirement that the missing source theorem be two-variable and source-faithful;
- the selection of Architecture E as the shortest coherent route;
- the exact list of mechanism firewalls that any claimed completion must survive.

No statement here claims that RH or GRH has been proved.

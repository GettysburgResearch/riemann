# Annotated external import and source boundaries

Status: IMPORTED external theorem as reported by its authors; NOT an
independently replayed theorem or an accepted addition to the integrated
record. Reviewed 2026-10-16. All new deductions are separately PROPOSED.

## Versions: do not conflate the linked v1 with the current v2

Dean Cureton and Jesse Thorner, *A quasi-Riemann hypothesis for Dedekind zeta
functions*, AxiomProver/Axiom Math, Hexagon 2610.00200, CC BY 4.0.

|Object|Version-specific source|What was observed|
|---|---|---|
|User's link|https://hexagonmath.org/2610.00200v1|History: Oct 12, superseded; the landing abstract displays 31/32|
|v1 manuscript|https://hexagonmath.org/pdf/2610.00200v1|33 pages; Theorem 1.1 on printed page 3 says 1-1/6000, NOT 31/32|
|Current record|https://hexagonmath.org/2610.00200v2|History records the replacement on Oct 14; header still displays Oct 12|
|v2 manuscript|https://hexagonmath.org/pdf/2610.00200v2|36 pages; Theorem 1.1 says Re(s)>31/32, s!=1|
|v2 TeX|https://hexagonmath.org/api/v1/works/2610.00200v2/source?path=DedekindZeta.tex|Read directly; Sections 2, 5-13 and 15 used for this packet|
|v1 TeX|https://hexagonmath.org/api/v1/works/2610.00200v1/source?path=DedekindZeta.tex|Read for the version and exponent comparison|

The v1 printed theorem and the v2 final Table 1 were also inspected as PDF
images, not only parsed equations. We preserve this metadata/manuscript
mismatch rather than silently relabeling v1. The v1 exponent arithmetic is
8/15+933/2000=5999/6000. The v2 arithmetic is 61/100+287/800=31/32.

This is an ANNOTATED IMPORT with selected transcribed source extracts, exact
interfaces and a version-specific fetcher, not a complete PDF or Lean-library
mirror. The full upstream bytes could not be downloaded into the execution
container in this pass. `fetch_sources.py` retrieves them on a networked
machine and records full hashes; it was syntax-checked but not network-run.
The Hexagon source indexes expose only SHA-256 prefixes in the accessible
page (v1 fe4107a2ac3fd506; v2 f54808ad0f967b54). Those are not represented as
complete content hashes. The local manifest authenticates OUR packet only.

## Imported statement and why it matters

For every number field K, zeta_K has no zero in Re(s)>31/32, away from its
pole at one. Every finite-order Hecke L-function over K has the same
zero-free half-plane wherever holomorphic; for nonprincipal characters,
one is included. The bound's exponent is universal; the proof's constants,
height-growth exponents and thresholds are allowed to depend on the fixed
field and arithmetic data. This is not a discriminant-uniform reciprocal
estimate, a theorem for every infinite-order Hecke character, or full GRH.

The advance is breadth across number fields, not a better Riemann-zeta
exponent than the earlier 7/8 manuscript discussed in the paper. The general
field is the useful new platform for the repository's L-family programme.

## Proof map with the interfaces that matter here

1. Work over F containing mu_12; obtain the general K statement through the
   abelian extension K(mu_12)/K. This is descent, not iterative exponent gain.
2. Build one fixed arithmetic average I_Z. Cubic metaplectic/theta machinery
   transforms a completed sextic Gauss-sum family into quadratic characters.
   The general-field local/global compatibility, infinite places and units
   must be retained; they are not cosmetic replacements of integer norms.
3. Apply the quadratic large sieve to a reflected mean square. Proposition
   9.1, on dyadic powerful/squarefree parts P,D, gives
   Z^epsilon P^(1/2)(D+D^2 P/Z). On support PD<=Z^M with M>1 this becomes
   Z^(2M-1+epsilon). An additive second mean and Cauchy then bound I_Z.
4. Evaluate the SAME fixed average by Poisson summation. The frequency
   Euler product contains zeta_F^S(6z)L^S(w,chi_u)/L^S(xi,bar(chi_u)) times
   a correction. Common primes and nonunit zeros are not discarded.
5. Split nonprincipal frequencies by a zero detector before moving their
   reciprocal contours. For the principal residue, keep the precise H(s)
   of equation (11.3). Its nonvanishing is essential to detecting zeta zeros.
6. The comparison is I_Z=c0 f(Z)+O(Z^(717/2000)), c0!=0, while the theta
   estimate gives I_Z<<Z^(287/800+epsilon). Thus f has that bound and its
   Mellin transform excludes zeros to the right of 31/32.

`PARAMETER_BARRIER.md` reconstructs the actual margins and states the limited
meaning of the resulting Cauchy ceiling. `EULER_STRIPPING.md` uses the exact
principal factor, not a guessed generic Euler product.

## Formalization: what was and was not checked

Repository: https://github.com/AxiomMath/DedekindZetaZeroFree
Frozen observed main: `09afbb4ce6570c1615d58509dc197fc9f0956b7d`.

The upstream README reports only Lean's standard axioms propext, Quot.sound,
and Classical.choice. That is an UPSTREAM report; no local Lean build or
axiom audit was performed here. Dependencies include Mathlib, Tau Ceti,
vendored class-field theory and other credited libraries.

The challenge and solution statements were inspected. They ask for a
holomorphic continuation away from one agreeing with NumberField.dedekindZeta
on Re(s)>1, then nonvanishing in Re(s)>31/32. The Hecke statement similarly
identifies the actual convergent ideal series and requires nonprincipal
entireness. Thus the public target is not merely an unconnected symbol
named zeta. This statement-level inspection does not validate every proof
or dependency behind it.

The challenge's `sorry` declarations are specification placeholders; the
separate solution supplies proofs using `dedekindZeta_ne_zero` and
`heckeL_ne_zero`. They must not be advertised as discovered proof gaps.
Read identities:

- README.md: blob `836f3d5bb6cb6f96a04680dbe62b3b61a122e654`.
- Challenge/DedekindZetaChallenge.lean: blob
  `98daca8451aa04c30b9a8fc50ef60b3b075899cb`.
- Solution/DedekindZetaSolution.lean at the frozen commit: blob
  `16e98688137243e7822e0cee5529b29945c2684a`.

The README/challenge were fetched from the then-current main; the solution
was fetched explicitly at the frozen commit. Their displayed blob identities
are recorded rather than claiming a full-tree build. Independent review
should freeze the dependency manifest, build, run the comparator, inspect the
axiom closure and then audit the mathematical statement interfaces.

## Exact repository comparison and reading levels

Main was read through AGENTS.md and STATUS.md at observed main
`f99d9e3908dde4865377c75d9ca051c1f545bf4f`. Main is unchanged by this packet.
Active research below is proposed/unmerged, not accepted background theorems.

|Source|Frozen head and reading level|Connection and limitation|
|---|---|---|
|#945 compensated Euler phases|90d0a737789821092fec27c04c6d96099a0a1b35; full PROOF.md, blob 84c339c8e3dfc0eea93eab49de8048fd1a7bc6c6|Two-way source-faithful critical convolution; its bounded degree-three multiplier has constant cost. The new q^2-weighted sixth-power source has only logarithmic cost; isolated q^3 stripping is worse.|
|#946 positive singleton flow|c90818b3a671bb3d124019f3be93a439697deab1; full PR description and MATHEMATICS.md Sections 6-7/source notes, blob fc1709449f46f19df78a614c5513f37f7803ddee|M=G+I-D retains positive compensation. Target I<=D+diagonal remains open. The extraction exponent is already stated there.|
|#944 conductor-divisor window|18290b5cdc646022ed0693519aa54c20e3296b5a; PR description only|Signed remaining divisor window, not a proven full covariance estimate. General-field geometry/row adapters would need their own proofs.|
|#947 coherent rows|0ef2eeb731f5528df04a14685b35dc887fcfee36; PR description only|Large finite degree cancellation is concentrated on a few coherent sixth-power rows, not evidence of a uniform complement saving.|
|#935/#939 native completions|a7a7fad2c5fa1929c7e04570cde4188e3191b071 / 751eff5d759f82ae8316f141613f2214c97b7553; PR descriptions|Liouville/determinant critical convolution comparisons are prior mechanisms, not inventions of this packet.|
|#941/#943 freezing/phase barriers|f106e31f12b8a10f2d57b336c983a25fb8dd6adc / 24cb2cdd6e768c2c35ef87227ed8319cfc2d14ed; PR descriptions|Do not erase native signs, freeze large-prime phases freely, or infer an asymptotic power from a finite ratio.|
|#934 quasi-RH research wave|3092feee25c583ec760c5f14f4aa4c98d9c5df39; PR description only|Parallel concern about signed pairings; its different exponent model was not imported or independently reviewed here.|

No analytic theorem from a description-only source is a premise of the new
proofs. Broader historical programme connections are strategic, not claimed
new integrations or an exhaustive review of the repository.

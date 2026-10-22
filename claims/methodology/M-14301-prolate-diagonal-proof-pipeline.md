# M-14301 — Proof-producing diagonal prolate–Weil pipeline

Claim ID: M-14301  
Title: A fail-closed finite certificate pipeline for the positive prolate route  
Status: PROPOSED  
Authoring agent: `gpt56-09`  
Reviewing agents: none  
Created: 2026-07-29  
Last updated: 2026-07-29  
Dependencies: T-14301 and L-14301  
Scope: methodology for a positive proof sequence plus its required asymptotic closure  
Related counterexample candidates: none

## Objective

Reduce the positive prolate route to finite, independently checkable records at
each level and one explicit asymptotic theorem.  Every finite level should end
in exact rational inequalities and source hashes; floating computations may
nominate parameters but may not cross a proof gate.

A finite prefix is evidence only.  A completed RH proof must also include a
finite mathematical argument establishing the per-level inequality for all
sufficiently large levels.

## Parameter convention

The Connes–Consani–Moscovici support parameter is `lambda>1`, with interval
`[lambda^-1,lambda]` and logarithmic length `2 log lambda`.  Implementations
that use the prime cutoff `c` usually have

```text
c = lambda^2,
2 log lambda = log c.
```

Every artifact must state which convention it uses.  Confusing `lambda` and
`c` changes both the prime manifest and the Hardy-strip weight.

## Per-level proof object

For each level `j>=3`, freeze

```text
lambda_j,
prime cutoff c_j=lambda_j^2,
frequency half-band N_j,
Hardy weight tau_j=1/2-1/j,
target eta_j=2^-j.
```

The level passes only if all gates below pass.  Here `j` is a proof-ledger
index, not a prescribed physical growth rate for `lambda_j`: once convergence
is established, one may pass to a sufficiently sparse subsequence to meet the
canonical `2^-j` target.

### Gate 1 — matrix identity and normalization

1. Construct a directed interval enclosure of the exact finite matrix
   `QW_{lambda_j}^{N_j}`.
2. Bind the artifact to the exact formulas, prime-power manifest,
   archimedean convention, basis ordering, `lambda/c` convention, and source
   digest.
3. Use the cutoff-free matrix or a one-sided archimedean tail budget whose
   direction is proved.  A finite-cutoff sign without its tail budget is not a
   matrix enclosure.
4. Verify exact real symmetry and the analytic identity
   `Q[-m,-n]=Q[m,n]`, not merely approximate numerical symmetry.
5. Record the Dirichlet-boundary vector `delta_N` in the same basis.  The
   nonvanishing normalization used by the finite real-zero theorem is imported
   from the exact even-simple argument, not inferred from a floating dot
   product.

The finite Guinand–Weil dictionary of Groskin (arXiv:2607.02828) is a natural
source for the vector/test-function identity and archimedean tail accounting.
Existing repository interval, provenance, and SHA-ledger machinery should be
reused rather than replaced.

### Gate 2 — construct the explicit prolate target

1. Reconstruct the prolate functions `h_{0,lambda}` and `h_{4,lambda}` in the
   precise Fourier convention of Connes–Consani–Moscovici.
2. Form the normalized linear combination `h_lambda` with vanishing integral.
3. Apply their map `E` and restrict to `[lambda^-1,lambda]` to obtain
   `k_lambda`.
4. Certify every normalization and the inversion symmetry
   `k_lambda(u)=k_lambda(u^-1)`.
5. Independently reproduce the convention connecting the transform of
   `k_lambda` to the centered `Xi` used by T-14301.

A source implementation is discovery data until these steps are reproduced
with directed arithmetic or explicit analytic error bounds.

### Gate 3 — weighted projection of the target

Let

\[
 w_{j}(u)=u^{2\tau_j}+u^{-2\tau_j}.
\]

Compute directed enclosures for

```text
p_j = P_{N_j} k_{lambda_j},
q_j = ||p_j||_2,
t_j = ||k_{lambda_j}-p_j||_{w_j},
G_j[m,n] = integral V_m(u) conjugate(V_n(u)) w_j(u) d*u.
```

The weighted tail `t_j`, not the ordinary Fourier tail, is the quantity that
enters the strongest theorem.  Two viable proof routes are:

1. direct interval quadrature of the weighted residual function;
2. a weighted Parseval/Sobolev identity whose endpoint and periodicity terms
   are explicit.

An ordinary Parseval subtraction can still be useful for discovery, but it
reintroduces the support penalty if converted to the weighted norm by a
supremum.

### Gate 4 — freeze a rational even candidate

Choose a nonzero rational even vector on the line of, or rigorously close to,
`p_j`, and call it `v_j`.  The verifier normalizes this vector internally, so no
irrational square root is placed in the certificate.  Carry any line and
normalization mismatch into all of:

```text
matrix residual,
weighted target tail,
projection norm,
weighted Gram/complement factor.
```

The frozen vector, not the floating eigenvector, is the certificate primitive.

### Gate 5 — residual and parity-sector gaps

Using the interval matrix from Gate 1:

1. bound the midpoint Rayleigh residual of `v_j`;
2. build a complete rational basis of the even complement;
3. build a complete rational basis of the odd sector;
4. certify strict shifted positive definiteness in both sectors by exact LDL;
5. subtract the full `2 delta` operator-radius budget from both midpoint gaps;
6. apply L-14301 to obtain an effective residual `R_j`, even gap `g_j`, global
   simple-even status, and a projective ground-state angle.

`X-14301` verifies the finite algebra of this gate.  A production adapter must
also prove matrix provenance and exact parity.

### Gate 6 — weighted complement geometry

Certify a rational `kappa_j` such that

\[
 \|w\|_{w_j}\leq\kappa_j\|w\|_2
 \qquad
 (w\in E_{N_j}(\lambda_j)\cap v_j^\perp\cap H_+).
\]

If `B_+` is the rational even-complement basis and `G_j` the weighted Gram
matrix, it is enough to certify

\[
 B_+^T(\kappa_j^2I-G_j)B_+\succeq0.
\]

Use a strict rational LDL certificate after enlarging `kappa_j` by a directed
rounding margin.  This step is what prevents the proof from paying the crude
worst-case factor `lambda_j^tau_j`.

### Gate 7 — combine the Hardy-strip target error

Form the directed upper bound

\[
 d_j^+
 :=t_j+q_j\kappa_j\frac{R_j}{g_j}
   +\text{rationalization and Gram-enclosure budgets}.
\]

The free scalar multiplying the exact ground state is chosen projectively, so
there is no unnecessary `sqrt(2)` unit-vector alignment loss.

### Gate 8 — moving-strip decision

Certify the exact scalar inequality

\[
 d_j^+\leq\eta_j=2^{-j}.
\]

No additional factor involving `lambda_j` or `log lambda_j` appears.  T-14301
then converts this weighted source norm into local-uniform transform
convergence on every smaller fixed strip.

Record the exact rational endpoint and a clearly labelled non-rigorous decimal
for display.

### Gate 9 — asymptotic closure

No amount of finite-prefix computation crosses this gate.  Prove a finite
theorem giving, for all sufficiently large `j`, bounds such as

```text
t_j <= T(j),
q_j <= Q(j),
kappa_j <= K(j),
R_j <= R(j),
g_j >= G(j) > 0,
T(j) + Q(j) K(j) R(j)/G(j) <= 2^-j.
```

A recurrence, monotonicity theorem, operator comparison, or explicit
large-parameter asymptotic is acceptable.  Curve fitting and extrapolation are
not.

## Search strategy

The proof target is not the smallest finite eigenvalue and not the accuracy of
the first reconstructed zeta zero.  Rank candidates by the actual T-14301
budget:

```text
weighted projection tail
+ projection norm * weighted complement factor * residual / even gap.
```

Useful discovery diagnostics are:

1. decay of the weighted prolate projection tail as `N` grows at fixed
   `lambda`;
2. residual of the projected prolate vector against the exact finite Weil
   matrix;
3. even and odd complement gaps;
4. the weighted complement factor `kappa`;
5. stability of the aligned vector across nearby cutoffs;
6. the log-slope of the full Hardy-strip error `d_j^+`.

The public finite-Weil data report very high cross-cutoff ground-vector
alignment and rapidly improving zero accuracy.  These are motivation, not
substitutes for any of the six quantities above.

## Promising analytic attacks on Gate 9

### A. Prolate coercivity transfer

Compare the even Weil complement form directly with the prolate-wave
Hamiltonian on the orthogonal complement of `k_lambda`.  A coercive inequality
of the schematic form

\[
 QW_\lambda-\mu_\lambda
 \geq a_\lambda(PW_\lambda-\chi_{0,\lambda})-\varepsilon_\lambda
\]

would simultaneously control the gap and suppress high weighted modes.  The
repo's exact matrix tables can test the finite analogue before an analytic
proof is attempted.

### B. Weighted residual identity

Instead of bounding the residual norm after assembling the whole matrix,
expand `(QW_lambda-mu)k_lambda` using the differential equation for the prolate
functions and the explicit-formula decomposition.  Search for cancellations
between the archimedean and prime pieces that are invisible in entrywise
matrix norms.

### C. Resolvent-weighted certificate

The factor `kappa_j` is worst-case over the whole even complement.  A sharper
certificate can bound the actual residual-to-error map

\[
 w=-(C-\lambda_0I)^{-1}b\alpha
\]

directly in the weighted norm.  An exact matrix inequality for
`G_j^(1/2)(C-sI)^(-1)` over the certified eigenvalue interval may dramatically
reduce the finite budget.

### D. Strip-Hardy compactness

The weighted norms define a Hardy-space compactness framework for the
transforms.  It may be possible to prove convergence from a uniform energy
bound plus convergence on a uniqueness set, replacing full weighted target
convergence by finitely many moment or interpolation conditions per level.
Any such replacement must include a normal-family and uniqueness theorem, not
only matching zeros.

## Reuse of repository mathematics

The positive route should reuse, with sign-neutral interfaces:

- directed matrix assembly and exact fixed-vector contraction;
- rational vector freezing and perturbation survival;
- midpoint/operator-radius whole-matrix certification;
- exact LDL/Schur complement checkers;
- source-digest, precision-nesting, and artifact-ledger gates;
- complete finite prime-power manifests;
- independent normalization and archimedean-tail audits.

The counterexample project has already built much of the proof engineering.
The new content is the target functional: instead of seeking one negative
Rayleigh value, certify one simple-even Hardy-strip approximation at each
level and then prove its asymptotic decay.

## Failure modes

1. **Even-only eigensolve.** This does not exclude a lower odd eigenvalue.
2. **Raw overlap.** High overlap between successive numerical ground vectors
   does not identify the explicit prolate target or provide a rate.
3. **Zero accuracy as proxy.** Accurate real zeros do not by themselves prove
   locally uniform convergence to `Xi`.
4. **Wrong support convention.** Confusing `lambda` with `c=lambda^2` changes
   the operator and the Hardy weight.
5. **Unweighted L2 convergence.** `d_j->0` alone is insufficient on a growing
   support; endpoint-weighted control or an equivalent direct transform bound
   is needed.
6. **Finite prefix.** Any finite collection of passing levels is only partial
   evidence.
7. **Hidden matrix tail.** A truncated archimedean integral can perturb the
   residual and both gaps in the dangerous direction.
8. **Weighted-tail cancellation.** Every interval subtraction must use the
   orientation that enlarges the tail upper bound.
9. **Nonprojective scaling.** Fixing unit normalizations can add a needless
   alignment error; the theorem permits a scalar and the certificate should
   optimize it.
10. **Stale CCM normalization.** The finite real-zero theorem requires its
    exact `delta_N` normalization; a basis or support convention change can
    silently invalidate the import.

## Deliverables for the next implementation PR

- a proof-grade `k_lambda` evaluator and normalization audit;
- exact weighted Fourier projection and tail certificates;
- a production adapter from interval Weil matrices to X-14301;
- exact weighted Gram and complement-factor certification;
- a pilot table over public cutoffs `c=13,...,67` reporting `t`, `R`,
  `g_even`, `g_odd`, `kappa`, and the full Hardy-strip budget;
- a theorem attempt explaining any observed decay rate rather than merely
  extrapolating it.

## Remaining uncertainty

No production level currently passes Gate 8, and no asymptotic closure for
Gate 9 has been proved.  M-14301 is a concrete proof architecture, not a claim
that the required sequence exists.

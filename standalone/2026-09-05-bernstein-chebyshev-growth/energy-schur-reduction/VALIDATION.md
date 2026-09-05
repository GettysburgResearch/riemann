# Validation and self-audit

## Finite exact replay

`verify_schur.py` uses only Python's standard library and Fraction arithmetic.
It authenticates three parent proof Git blobs and its exact SOURCE_LOCK.json.
It reconstructs result.json and compares typed canonical JSON; floats,
Booleans in integer positions, duplicate keys and nonfinite constants do not
alias accepted integers or rational strings.

The 581 distinct controls comprise piecewise-polynomial weak residual
identities (including shifted absolute-value cusps), clamped endpoints,
constant-direction residual projection, signed finite Schur remainders,
Galerkin monotonicity, non-Galerkin trial enclosures, and exact geometric
compact-operator models, and twelve rational controls for the improved actual
L=1 scalar barrier. The matrix tests use synthetic rational kernels and matrices,
not counterfeit data passed off as actual primes or zeros.

Normal Python and python -O produce identical reconstructed JSON. Sixteen
intended corruption runs cover eight cases in both modes: saved count,
float alias, Boolean alias, duplicate key, changed new proof, changed parent
proof, changed source lock, and changed checker bytes. Every run must exit 2
with the expected error. REPLAY.json records actual completed commands and
output hashes. These are execution receipts, not analytic certificates.

## Non-certifying arithmetic reconnaissance

`reconnaissance.py` evaluates the literal L=1 source from the finite-window
formula, using the safe scalar P2=-zeta'(2)/zeta(2) at 50 mpmath digits. The
finite prime term is n=2; the full unbounded tail is represented by P2.
The rest of the calculation uses ordinary NumPy/SciPy floating point.

The test grids have 256, 512 and 1024 cells, with 104 sampled exceptional
functions. At 1024 cells, the tested positive-sector trial ranks are
0,32,128,384,704,880. The trial-zero sampled lower eigenvalue is approximately
-1.03e-4; at trial rank 880 it is approximately -1.40e-6. The corresponding
upper-matrix smallest eigenvalues are approximately 5e-10. The proved L=1
refinement replaces the residual factor 3 by 15/8; at trial ranks 384,704,880
its sampled lower matrices have positive minima approximately 4.31e-10,
4.59e-10,4.60e-10. These observations do not supply a continuum certificate.

No interval arithmetic, analytic cell/quadrature remainder or exact continuum
constraint projection was used in this experiment. Thus even the reported
signs are NOT certified signs of exact continuum matrices. In particular,
a negative lower approximation is not evidence that S_L or T_L is negative.
The experiment is not an independent mathematical review. Its wall times are
ordinary diagnostics, not performance guarantees.

## Mathematical self-audit

- W' is integrable on each finite interval despite its logarithmic origin
  singularity. W'' is not assumed bounded or silently integrated across
  prime cusps.
- The damping is removed by a bounded invertible map on fixed L only.
  Inertia/positivity, not eigenvalues, is preserved under that congruence.
- Energy coercivity is a primitive bound, not a uniform L2 inverse bound.
- Riesz vectors belong to the energy completion and need not be L2 vectors.
- The Schur correction is a Gram subtraction. Galerkin values are UPPER
  bounds; positivity of an upper bound does not prove positivity below it.
- The residual enclosure is a matrix Loewner bound for all complex linear
  combinations at once. Its general constant is b^2/(b/2)=2b=3; the
  improved L=1 constant is b^2/(6/5)=15/8.
- Negative index is preserved, but nullity is not automatically preserved.
- No residual-norm convergence rate or guaranteed terminating PSD test is
  inferred from Galerkin energy convergence.
- The all-L effective sign remains open. The present finite-dimensional
  reduction is not a reduction of the whole RH problem to 104 numbers.

No actual effective S_L matrix, complete actual residual certificate, new
zero census, predecessor-suite rerun, Lean build, independent referee verdict,
or remote CI result is claimed. No mathematical theorem is inferred from a
stored Boolean such as rh_proved=false or a replay PASS string.

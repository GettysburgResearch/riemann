# Arithmetic cutoff inertia — what the attempted completion actually gives

**RH and the original subexponential inequality remain unproved.** This packet
contains proposed complete proofs about the *literal finite arithmetic cutoffs*
of the source-built operator, not a proof about the sign of the full operator.
Independent mathematical review is required.

Parent: PR #792 at `39c13367f4b3956631ea1e00fac6c3005fc32057`.
No parent file is modified. This is not a correction of a claimed cutoff-positivity
theorem: the parent made no such claim.

## Results

For every finite prime-power cutoff X>=2, with the complete gamma series or any
of the parent's gamma truncations:

```
L_X = 30(1+log X)
chi(s) = s^3(1-s)^3 on [0,1], zero outside
f_X(t) = exp(3t/4) (D^2-1/4) chi(t/L_X)

<f_X,T_(X,J)f_X>/||f_X||^2 <= -(4/3)exp(-45)X^(-45) < 0.
```

The same source cutoffs have **infinitely many negative eigenvalues**. With the
complete gamma series there are infinitely many positive eigenvalues as well.
These are analytic all-X statements, not extrapolations from finite spectra.
No PNT, zeta zeros, or RH assumption is used.

The natural repair that replaces the omitted prime measure by its continuous
average is also not automatically positive. Its X=2 Fourier multiplier is
strictly negative at zero, by elementary bounds. This only refutes positivity
for all such repaired cutoffs; it does not rule out an unproved cofinal positive
subsequence or other, more structured completions.

## Why this matters for the requested proof

The proposed completion was to factor the convergent arithmetic source at finite
cutoff as a positive square, then pass to the trace-norm limit. The first step is
false for EVERY raw cutoff of this family. The earlier absolute trace-norm bounds
remain valid, but do not supply its sign.

Do not confuse these two operations:

```
T_(X,J)    truncate the arithmetic series, retaining an infinite-dimensional operator
P_M T P_M  compress the FULL arithmetic operator to M basis vectors
```

The new negative witnesses concern the first operation. They do not contradict
the parent's positive 4-by-4 compression, and do not show that RH is false.
The full-source sign, or a signed trace-moment bound, remains the exact open step.

## Reading and replay

Read `PROOF.md`, then `SOURCES.md` and `VALIDATION.md`.

```
python verify_cutoff.py --check result.json
python -O verify_cutoff.py --check result.json
sha256sum -c SHA256SUMS
```

Place the unchanged parent `cross-route-hardy-laguerre/BRIDGE.md` in the sibling
directory when replaying outside the repository. The checker authenticates its
Git blob against a literal constant. Its 141 controls are finite rational algebra
and source-integrity checks, not machine verification of the analytic theorems.

# Execution, review boundary, and failed completion

Status: AUTHOR EXECUTION; independent proof/code review pending.
No RH proof or all-rank arithmetic sign is claimed.

## Executed in this pass

- `python verify.py --check result.json` and the same command under `python -O`
  each reconstruct and pass 65 finite exact comparisons. Full JSON outputs
  are byte-identical. Repeated rational sample controls are counted as
  comparisons, not as independent theorem proofs.
- `python test_rejections.py` and its optimized-mode run each reject six
  deliberately corrupted records/sources for the expected diagnostic:
  RH flag, numeric type alias, duplicate JSON key, flipped margin, proof
  alteration, and source-lock alteration. All twelve subprocesses fail
  as intended. Disposable copies are used; published files are unchanged.
- `SOURCE_LOCK.json` and `PROOF.md` are bound by literal SHA-256 constants
  in the verifier before any controls are run.
- The full local pass8 projection proof was read and its Git blob identity
  was checked against the published 38574a2ba02ccfec1ba0eaf4164bb7862ef7bdc0.
  The live PR head and the proof were also read through GitHub.
- A small ordinary-high-precision mpmath check of the balanced X=2 scalar
  expression was used during exploration. It is NON_DIRECTED, not a
  certificate, and not an input to either the proof or the acceptance code.

The recorded 65 comparisons cover elementary exponential bounds, the
negative X=2 symbolic jet and rational margin, the continuum exponent,
scalar Gaussian resolvents, the differentiated contour constants, the
PNT-tail antiderivative, trace normalizations and original-metric examples.
They do NOT prove the infinite contour, Stieltjes, trace-norm, PNT or
projection-limit arguments. Passing these checks does not prove RH.

The exact negative X=2 value relies on the standard digamma special values
and the analytic differentiation in PROOF.md. The finite verifier checks
its algebra and rational inequalities, not an independent interval
implementation of every special function.

## What was not done

No full-source xi matrix was evaluated in this continuation. No broad
prime or zero scan, finite zero-verification replay, directed special-function
certificate, Lean build, remote CI run, independent referee review, or new
numerical PNT constant was produced. Predecessor suites were not rerun;
their existing execution records are not relabeled as new validation.

The PNT constants C,c in the error estimate are an explicit dependency,
not numerically certified here. Equation (9) is a valid bound in terms
of the actual discrepancy; equation (13) gives dependence on any independently
valid explicit PNT constants. Do not advertise a computed all-rank numeric
error tolerance based on an unspecified constant.

## Review priorities

Read the Banach-space derivative of the shifted Gaussian atom first. Check
that differentiating at fixed contour height precedes selecting its height,
and that the integration-by-parts boundary tends to zero in trace norm.
Then check the right-continuous Stieltjes endpoint in (11), the erfc factor
and unbounded continuum mode in (15), and the compiler's removable pole.
Finally check the unchanged metric in (27), the X=2 source jet, and the
separation between rank-uniform approximation and positivity.

The final attempted sign step is explicitly false in its proposed
'all finite balanced cutoffs are positive' form. Its counterexample is
actual arithmetic at X=2, not a counterexample to RH. A cofinal/asymptotic
lower bound remains open. Trace-norm convergence and the positive limiting
trace do not supply such a bound.

## Publication scope

All new files are under operator-renormalization-pass9/. The scientific
base is c64a0ae131d60cce48bc0dcc73358f7a1a857a89. No existing source,
canonical registry, integrated theorem, main file or formal module is changed.
The exact resulting publication head belongs in an external receipt or PR
comment, not in a tracked file that purports to contain its own commit hash.

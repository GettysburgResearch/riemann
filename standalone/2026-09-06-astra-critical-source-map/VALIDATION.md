# Execution and assurance boundary

Environment: Python 3.13.5, SymPy 1.14.0, Linux. The arithmetic certificate
uses only the Python standard library. No secret, upstream executable,
network input, floating-point value or zeta/gamma oracle enters it.

## Executed

    python -B checks.py --output checks.normal.json
    python -B -O checks.py --output checks.optimized.json
    cmp checks.normal.json checks.optimized.json
    python -B source_certificate.py --output source.normal.json
    python -B -O source_certificate.py --output source.optimized.json
    cmp source.normal.json source.optimized.json
    python -B rejections.py --output rejections.json
    python -B validate.py

Both mathematical outputs are byte-identical between normal and optimized
Python. The exact checker executes 13 named controls and 1,004 bounded
fixtures in each mode. These cover elementary rational/polynomial identities,
synthetic finite Toeplitz matrices through dimension 13, causal inverse
coefficients, interval primitives and invalid-input refusals. They are not
1,004 new theorems, and do not prove the analytic claims by finite sampling.
The rejection driver runs the ACTUAL CLI comparison of four corrupted exact
records and four corrupted source records in each mode: sixteen executions,
all rejected. The proof-code uses explicit exceptions, not assert statements
whose removal changes acceptance under -O.

## Actual source certificate (one vector only)

At b=3/4 and eta=1, source_certificate.py integrates the exact formula

    d_b(t)=exp(-bt)[n+log(n!)-nt]

on EVERY cell [log n,log(n+1)], n=1,...,4095. The complete remaining
half-line has the analytic tail bounds (D7) and

    integral_T^infinity d_b(t)exp(-t)dt
      <=exp(-(b+1)T)[(1+T)/(b+1)+1/(b+1)^2].

Every endpoint is an integer over 2^192. Logs use binary range reduction and
72 terms of the positive atanh series plus its complete geometric tail.
Powers n^(-k/4) use exact fourth-root inequalities on integers. The cell
antiderivatives are independently differentiated by the rational-symbolic
checker. Directed arithmetic rounds at every operation.

A SECOND elementary enclosure of D_b(1) uses its positive Dirichlet series
at exponent 7/4 with the full lower/upper integral tail; the two certified
enclosures are intersected. No externally computed zeta value is supplied.

The retained exact endpoints imply, using decimal values ONLY for display,

    0.5890751 < ||d_(3/4)||_2^2 < 0.5893298,
    0.48056812 < D_(3/4)(1) < 0.48056825,
    0.2159035 < eps_0(3/4;1) < 0.2162429 < 11/50.

The serialized dyadic integers, not those display decimals, are proof
endpoints. This is the projection onto span{d_(3/4)} only. No actual
higher-rank matrix, small-a gamma integral or xi zero is numerically evaluated.
The bound is an implementation calibration, not an extrapolation to eps_N=0.

## Authoring corrections disclosed

The first source checker run reached the tail formulas but stopped because
integer/Interval reverse division had not been implemented. This was repaired
before a certificate was generated. A Boolean parenthesization in its
positivity guard was also corrected. The final directed results, mode replay
and corruption tests use the corrected source. Symbolic checks also verify
the seventh-order desmoothing and all endpoint antiderivatives.

Non-directed mpmath reconnaissance compared low-order source norms while the
argument was developed. Its values are not stored as certificates or used as
premises. The committed proof certificate is the independent directed integer
implementation above.

## What is not claimed

No Lean/kernel proof, Comparator, CI, external reviewer acceptance, exhaustive
literature priority, all-rank arithmetic sign, or proof of RH. Hardy
factorization, Paley--Wiener, beta integrals, and xi reflection are named
classical mathematical inputs. The full source-domain cyclicity limit is
unproved. The local recovery from the old Jordan measure has no asserted
global norm bound in L2(mu_a).

The original PR804 files are preserved as an immutable sibling packet; this
new directory does not change their inventory contract or their review
status. The publication receipt is stored outside the committed packet to
avoid a self-referential commit hash. Finite checks and byte authentication
are different from mathematical proof verification.

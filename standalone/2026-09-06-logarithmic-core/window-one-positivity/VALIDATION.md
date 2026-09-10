# Validation actually performed

The accepting calculation reconstructs2049 explicit coefficient inequalities
(n=0 through2048) and proves the remaining infinite tail through256 residue
classes and a1024-term positive gamma lower bound. These counts have different
roles; they are not a count of distinct mathematical theorems.

`python -B verify.py` and `python -B -O verify.py` were both completed. Their
full mathematical JSON outputs are byte-identical. The accepted finite margin
is2^-35; the worst enclosed scaled coefficient is greater than9.36e-11. The
all-tail lower endpoint exceeds0.4883; its accepting threshold is2/5. Exact
rational endpoints and a digest of every finite enclosure are in result.json.

The constants pi, gamma_E, C_b and P2 are freshly enclosed from elementary
series, an explicit digamma remainder, and Euler--Maclaurin/Cauchy estimates.
All accepting operations are outward192-bit dyadic arithmetic. The proof
explains every infinite passage; finite execution is not a machine proof of
Fourier completeness or the imported special-function remainder theorem.

The separate bounded-controls driver completed2736 fixtures in19 named groups
in ordinary and optimized modes, with byte-identical outputs. Those controls
check rational rounding, interval corners, special values, a recurrence,
normalization and strict JSON types; most are elementary arithmetic fixtures.

Six deliberate CLI corruptions were rejected in each target interpreter mode:
float mode-denominator, negative weight, missing frequency, enlarged source
window, deleted cosine weights, and duplicate JSON key. In particular deleting
the atoms fails the actual n=0 arithmetic inequality, not just a manifest.
Run the two mode batches separately:

    python -B test_rejections.py
    python -B test_rejections.py --optimized

Earlier combined orchestration calls timed out before producing a complete
receipt. They are not counted as successful executions. The final split-mode
receipts are refusals.json and refusals-optimized.json. Development also used
non-directed mpmath/SciPy cross-checks and larger-window fits; these are NOT
certificates. Only lengthone received the complete accepting calculation.

Reproduce:

    python -B validate.py
    python -B verify.py --check result.json
    python -B -O verify.py --check result.json
    python -B test_checks.py
    python -B -O test_checks.py
    python -B test_rejections.py
    python -B test_rejections.py --optimized

No actual Schur-entry quadrature, upstream suite, broad prime/zero campaign,
Lean/Comparator/Nanoda, remote CI, or independent referee acceptance is claimed.
The positive extension differs from W beyond the certified window. In
particular its first derivative has a nonzero mismatch at1, recorded in the
result. No unbounded-length positivity or RH proof was obtained.

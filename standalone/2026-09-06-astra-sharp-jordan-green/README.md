# Sharp all-scale Jordan Green closure

Status: **PROPOSED PROOF-COMPLETE COMPONENT THEOREMS / REVIEW PENDING**.
Scope: literal generalized-Jordan source; all s>0, all t>=0; all-rank
positive kernels on the safe Laplace half-plane. **RH is not proved.**
Base: `GettysburgResearch/riemann@051808c1f8367b4320c52f94b40908eb2173d622`.
This is new research, not a Reviewer D verdict. It does not edit prior reviews,
source branches, accepted registries, integrated mathematics, or formal code.

## Results

1. The Green-removal density is positive for every scale and time whenever
   kappa>=2; 2 is the sharp universal threshold. The old coefficient
   sqrt(275/14) admits the explicit bound **B_(2a,a)(t)>8a/45**.
2. Its complete contact/atom/density Laplace representation gives every finite
   safe kernel a proved positive metric lower bound. The completed gamma
   source is positive at all scales after an exact regrouping of factors.
3. The prime-deletion mean inequality left open in PR #440 satisfies
   **s^2 sum_p log(p)/(p^s(p-1))-1/zeta(1+s)>13s^3/1800**, for 0<s<=1.
4. The direct exponential continuation of these positive measures to the
   critical contour is not defined. An exact source map / critical norm
   exhaustion remains open; the full conditional conclusion to RH is stated.

The unexpected useful connection is

    factorial valuations -> harmonic von Mangoldt lower bound
    -> positive prime-power subsource -> exponential-integral envelope
    -> sharp global Green positivity.

No PNT, zero verification, infinite-grid extrapolation or large campaign is
used for the new positivity and mean theorems.

## Read and reproduce

Read PROOF.md, then REAL_AXIS.md and RH_ATTEMPT.md. CLAIMS.tsv and EDGES.tsv
separate proved component deductions from the open critical bridge.
SOURCES.tsv records exact SHA/path/blob predecessor identities.
EXTERNAL_INPUTS.md identifies the few classical identities used.

Run `python checks.py --output /tmp/jgc.json` and compare to checks.normal.json.
Run the same command with `python -O` for the optimized control.
Run `python rejections.py` and `python validate.py` for the refusal and file
integrity checks. See VALIDATION.md for what was actually run.
The bounded checker requires Python and SymPy; it evaluates no zeta values.
No external referee, Lean proof, or literature priority is claimed.

# Sources, claim boundary, and hostile self-review

## Source pins and reading boundary

The current PR #793 head read for this pass was `6ebbe5efe6430584736649b87495af2be073f693`, on `GettysburgResearch/riemann`, branch `research/astra/20260905-three-route-assault`.

Read in full at that head:

- `standalone/2026-09-05-three-route-assault/SIGNED_ENERGY_IMPORT.md`;
- `standalone/2026-09-05-three-route-assault/pass4/MOBIUS_FALSE_CONVERGENCE.md`;
- `standalone/2026-09-05-three-route-assault/pass4/PRIME_TAIL_TRANSITION.md`.

The author-provided signed-energy archive was checked to have SHA-256 `dcbc0ac035051ececc061ef8a9b279c0378e3028a2d794941f3270f8567833cc`, matching the remote import receipt. It was relocated by the publisher to `pass4-signed-energy-attempt/` because an independent pass4 had already landed. No work from either directory is overwritten.

PR #792 at `dc4bb9dbb49876732eb656339e79ee4ec43b157f` was read at the current PR-summary level for its cutoff-inertia and full-source-compression distinction. Its full latest proof was not independently reviewed in this pass. Older Route-1/Route-3 component results are retained context, not newly recertified here.

## Standard external ingredients

- NIST DLMF 18.12.13: ordinary Laguerre generating function,
  https://dlmf.nist.gov/18.12.E13
- NIST DLMF 18.14.8 at alpha=0: `exp(-t/2)|L_n(t)|<=1`,
  https://dlmf.nist.gov/18.14.E8
  DLMF attributes the bound to Koornwinder (1977), Remark 4.1; no priority for that inequality is claimed here.
- Classical Cauchy coefficient bounds, dominated convergence in the Gaussian saddle integral, and the probability characteristic-function continuity theorem.
- The elementary Mobius squarefree inversion and its Euler-product density. The quantitative `4sqrt(x)` remainder used here is reproved.
- The standard functional equation and Euler zero-free absolute-convergence half-plane for zeta, used only in the terminal equivalence and the retained positive-control principal part.

The new contribution claimed within this packet is the quantitative growing-degree tail contract, its exact vector threshold, and the source-support/Gaussian/large-deviation assembly in this normalization. External novelty remains unassessed. General saddle-point asymptotics or new RH-equivalent notation are not presented as discoveries by themselves.

## What the proof actually pays

AT-1 pays the infinite coefficient tail for an entire degree vector before passing to any cofinal limit. It does not require cancellation. AT-2 uses that estimate to make a valid finite-record formulation of the preexisting RH endpoint. AT-3 pays the negative mass of a signed comparison measure before applying a probability limit theorem. AT-4 pays the arithmetic count remainder, including its lower-endpoint term, after the continuous saddle calculation. AT-5 controls the complete degree-vector tail and proves sharpness with ONE fixed positive squarefree source.

The critical number describes a universal approximation class. It is not a lower bound on how much arithmetic is logically necessary for every possible RH proof, nor an optimality result for the actual signed Mobius tail.

## Hostile review questions

1. Is the Cauchy-circle maximum `p/(1+p)` rather than `p/(1-p)`? Check the extremum at the negative real point; the prefactor still uses `1/(1-p)`.
2. Does the same cutoff apply to every degree in each finite energy? It must. The geometric degree sum, not a sum of unrelated endpoint errors, gives AT-1.
3. Is the squarefree density `1/[zeta(2)(1+1/q)]`? Removing the q-factor from the squarefree Euler product gives the denominator `1+1/q`, not `1-1/q`.
4. Was the lower Stieltjes endpoint retained? The boundary `-R_q(X)g_n(X)` is included in K(p); at p=1/3 the total is 36.
5. Is the density in (13) positive? Not everywhere. Its negative mass is removed explicitly, with exponentially small total variation cost. Its mean and variance are algebraic cumulants before that correction.
6. Is the saddle proof uniform at c=8/3? No. The pole approaches the contour there, and AT-4 is only fixed-c above that value. AT-3 treats that transition separately.
7. Is c_* an estimate of zeta zeros? No. It is the sign change of a purely kernel-based exponential tail rate, certified from rational logarithm bounds.
8. Is vector sharpness merely scalar sharpness? No. The recurrence proves simultaneous row signs and geometric degree domination; the fixed-j saddle ratio and dominated summation supply the vector constant.
9. Does a controlled diagonal now prove cancellation? No. The exact same-support, same-diagonal positive source still grows exponentially even after the tail is accurately included.
10. Was a finite record at 1728^N actually evaluated for large N? No. Neither the proof nor the regression makes that claim. The cutoff is very expensive computationally.
11. Does the finite control count prove an infinite analytic result? No. The written analytic proofs require independent mathematical review.
12. Is the branch changed or a remote commit promised? Only an actual successful publication receipt may say so. This folder itself makes no such assertion.

## Actual execution

The new standard-library verifier was run normally and under `python -O`. Both runs reconstructed the same 498-control result, with byte-identical output. Fourteen unit/rejection tests passed in both modes. These reject altered values, numeric type aliases, missing keys, duplicate JSON keys, invalid domains, modified hashed files, incomplete manifest coverage, and path traversal.

The optional 90-digit mpmath regression was executed. It compares continuous exact finite-polynomial tails with the derived Gaussian and saddle limits at degrees 50, 200, and 800. Scalar and vector saddle ratios approach one. Those ordinary high-precision numbers are not interval certificates and are not used to accept the proof.

No broad predecessor suite, actual high-degree Mobius sum, zero census, prime scan, Lean build, independent referee review, or remote CI result is claimed. The earlier archive's import was authenticated but its 706-control suite was not rerun in this pass.

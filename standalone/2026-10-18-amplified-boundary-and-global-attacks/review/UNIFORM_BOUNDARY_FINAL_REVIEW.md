# Final independent review: global boundary 0.87488666

**Verdict: PASS.** I found no mathematical or implementation defect in the
frozen proof and exact parameter certificate listed below. The supported
conclusion is the explicitly import-dependent half-plane
\(\operatorname{Re}s>43744333/50000000\) at every height. This review does
not establish the upstream analytic assumptions or RH.

## 1. Frozen files reviewed

The paths in this table refer to the curated packet layout. During review,
the independent files were staged under `riemann_breakthrough/theta/`;
moving them to `review/` does not change their contents or hashes.

| File | SHA-256 |
|---|---|
| `correlated/UNIFORM_BOUNDARY.md` | `61149bdf31f4e12541da5d7543a2cb0311fd93878f1c5e034e2e1b0e4a24a385` |
| `correlated/certify_boundary.py` | `79a1519c18ed8f8caf014acc4637147f1eb1c6e1f2f73cad227cf6160694afbf` |
| `correlated/rational_polynomial.py` | `e9d3966ae6ace7e3bcab042e739e548e7389ba1ace0172aeb1243ce62f350133` |
| `correlated/certificate.json` | `c3cbac1ea1b98e1227757189c3958b616235ab69701fe69e51d710e8d1145d2f` |
| `review/check_xu_candidate_independent.py` | `3073b30e1d5e0223b424d95789d107b1ff59e810aa6f824fddcf5061da23fdbb` |
| `review/xu_candidate_independent_root_params.json` | `c4e7acaeaaa0f3e35725509631549ebfcd53f27a16f2bfa28337794a1171e4e3` |
| `review/XU_PARAMETER_INDEPENDENT_REVIEW.md` | `b56506f30e6dcebc371bd59ecf19a987492158593fde9eb8607a5771a2726888` |

Any load-bearing change to those files requires a renewed review. This
report supplements the earlier independent review; that earlier file was
not edited after the parent proof was frozen.

## 2. Mathematical review

I read the complete frozen proof and checked it against the primary
source, Yuanda Xu and Hejian Sang, *Amplified moments and a refinement of
the quasi-Riemann hypothesis*,
[arXiv:2610.15291v2](https://arxiv.org/html/2610.15291v2), specifically
equations (21) and (28), all conditions in Section 6.2, Proposition 6.1,
Sections 7--8, Lemma 8.1, and the principal-region conditions in Appendix C.

The following load-bearing points pass:

- The stated new parameters remain inside the source's existing parameter
  and contour ranges. No new moment or contour extension is silently
  assumed.
- The moment parameter is licensed by the previously established
  **family-wide** first stage:
  \((1+\kappa)/2=69991/80000\). The proposed new conclusion is not used to
  license itself, and an ordinary-zeta boundary is not substituted for the
  required auxiliary-family hypothesis.
- The endpoint formula, the clearing factor \(-8J\), and every sign in
  the numerator expansion agree with the source. Both factors forming
  \(J\) are positive on the required rectangle.
- The coefficient proof gives \(A(y)>0\) and
  \(4A(y)C(y)-B_q(y)^2>0\) for every \(y\ge0\). Completing the square
  therefore proves \(E<-10^{-8}\) on the entire continuous rectangle.
  This is not an inference from a sampled grid.
- All remaining source conditions are included: direct geometry, prime
  supply, the enlarged row range, numerator displacement, the detector
  floor, small rows, and the positive loss margins.
- Lemma 8.1 has exactly the quantified consumer needed here: a common
  positive saving for the full target family contradicts its zero
  supremum, without requiring that the supremum be attained. Target
  constants and thresholds may vary without weakening the zero-free
  half-plane statement.
- The ordinary-zeta consequence also follows directly from
  \(\zeta_F=\zeta L(s,\chi_{-3})\). The nonprincipal factor is entire,
  so it cannot cancel an ordinary zeta zero. Principal poles at one are
  correctly allowed.

The exact gain over the source's stated final boundary is
\(1/25000000=4\cdot10^{-8}\). The frozen proof states this small size
plainly, attributes the analytic mechanism to its source, and makes no
literature-wide priority claim or claim of an effective numerical height
threshold.

## 3. Independent implementation and executions

The independent checker was written directly from the source formulas in
a bivariate rational polynomial ring. It imports neither the parent's
checker nor the parent's polynomial operations or coefficient lists.
The parent implementation expands univariate coefficient polynomials
using a separate construction.

I compared the two outputs exactly. Every parameter, all 24 scalar
margins, and every coefficient of \(A,B_q,C,4AC-B_q^2\) agree. The
independent implementation also checks the completed-square identity as
a full bivariate polynomial identity.

Both parent replay commands passed against the frozen certificate:

```sh
python correlated/certify_boundary.py --check correlated/certificate.json
python -O correlated/certify_boundary.py --check correlated/certificate.json
```

The independent normal and optimized executions also passed and produced
byte-identical receipts:

```sh
python review/check_xu_candidate_independent.py --b 173/2000 --output independent_replay.json
python -O review/check_xu_candidate_independent.py --b 173/2000 --output independent_replay_optimized.json
```

The independent receipt has the hash recorded in Section 1. All acceptance
checks use exact integers and rational numbers and explicit exceptions;
Python optimization does not disable them. No floating-point comparison
participates in the acceptance proof.

## 4. Authentication boundary

The certificate authenticates the new rational algebra against the cited
source's explicit interface. The analytic reflection, detector, Hecke
moment estimates, Euler corrections, and initial family-wide \(7/8\)
statement remain imported hypotheses, as explicitly stated in the proof.
This scoped dependence is not hidden by the successful arithmetic replay.

Within that stated scope, the frozen result is a global zero-free
corollary, rather than a finite zero census or a finite theta-matching
certificate.

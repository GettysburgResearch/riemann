# GHE26 validation record

Date: 2026-09-12. **Author-executed validation, not independent analytic review or formal verification. RH is not proved.**

## Exact finite checks

The final `check.py` is standard-library-only and was run with isolated mode and site initialization disabled, in both normal and optimized Python:

```sh
python -I -S -B check.py
python -I -S -B -O check.py
python -I -S -B test_check.py
python -I -S -B -O test_check.py
```

Both checker reconstructions passed. Both seven-method test suites passed. The exact result record was originally produced separately with `--write` and was reconstructed after the later strict-JSON and additional numerator checks were added. The source moment series is generated from sinh, independently of the Gaussian continued fraction. All accepting arithmetic uses `fractions.Fraction`; no zeta evaluator, floating eigensolver or zero table is used.

Coverage: complete rational Riccati and adjacent-continuant identities through m=24; source moment matching through order 2m; exact continuants, norm, total shape, trace, tail moments and minimal-shape dual; complete-edge coefficient formula and both coefficient remainder bounds in the tested ranges, including coefficients beyond the polynomial degree; reversed numerator and its hyperbolic correction coefficients. Nine scaled Gaussian nodes are isolated by exact LDL inertia at m=8,32,64, three nodes at each order, each using 55 exact bisections. They are **quadrature nodes, not xi zeros**.

Each test-suite run exercises five changed-record refusals through the actual checker CLI, a duplicate-JSON-key CLI refusal, a pristine CLI acceptance, and an in-process perturbation of the off-diagonal primitive. It also checks a one-node inertia example independently and tests the omitted coefficient tail. Optimized Python preserves all checker predicates; the accepting code does not rely on `assert` statements. Detailed original command output is in `validation.log`.

## Nondirected diagnostics

`diagnostic.py` was run at 65 and 80 decimal working digits. The files `diagnostics.json` and `diagnostics_80.json` retain both runs. Three complex q values were evaluated at m=4,8,16,32,64. All retained 35-digit strings for K_m, K_0, K_1 and A_m(K_m-K_0) agree between the two runs. This is a same-backend precision repeat, not an independent numerical certificate.

At q=3/4+i, the uncorrected |K_m-K_0| and corrected |K_m-K_0-K_1/A_m| are approximately:

| m | Uncorrected | Corrected |
|---|---:|---:|
| 8 | 3.6484562e-3 | 3.5066410e-5 |
| 32 | 2.6058289e-4 | 1.8823071e-7 |
| 64 | 6.6667366e-5 | 1.2358301e-8 |

The two closed-form Mellin expressions were also compared with direct nondirected quadrature of the Fermi and sech-squared integrals at that exponent. The 65-digit absolute discrepancies were about 9.19e-36 and 2.97e-67; the 80-digit discrepancies were about 3.62e-43 and 2.64e-82. These small numbers are consistency observations, not rigorous error bars. No root of eta or xi was located by the diagnostic.

A preliminary diagnostic demanded floating k_i>1 for every computed shape. That was not resolvable for shapes extremely close to one at the working precision, so it rejected. The final diagnostic checks node/shape positivity only. Strict k_i>1 is proved analytically by the exact pole identity in Section 3, not inferred from that floating comparison.

## Source authentication and packaging

The retained #851 principal proof is 22,828 bytes, with Git blob SHA `8398cff6185b89d9964d5152dec9ce2640f52a53`, matching fresh repository metadata at head `57726ef9b3bf90561df5a361e3b01169c892a62a`. Other sources and reading boundaries are in `SOURCES.json`.

The archive is additive and uses the repository-relative directory `standalone/2026-09-12-gauss-hard-edge-eta/`. A clean extraction replay checks all SHA256 hashes, both exact-checker modes and both seven-method test suites. The accompanying patch is checked and applied in a fresh local Git fixture, and its resulting file bytes are compared with the archive. This does not verify a remote branch or promise conflict-free application to every possible current checkout. No remote write occurred.

## Mathematical limits

The tests do not establish the infinite-order formulas, uniform analytic tail passages, first-order Mellin expansion, minimal-shape theorem, positive deconvolution, auxiliary zero-displacement theorem or corrected reflected convergence by computation. Those are proposed analytical arguments in `PROOF.md`, awaiting independent review. The finite tests and diagnostics support consistency only.

No all-height xi zero confinement, cofinal zero-free theorem, weighted-defect vanishing, new native xi-zero certificate, complete novelty review, whole-repository validation or Lean proof is supplied. Every auxiliary/gamma/quadrature zero statement is distinguished from a claim about actual xi zeros.

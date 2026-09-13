# GPP26 validation and limitations

**The analytic proofs are proposed and have not received independent review. No RH proof, new xi-zero certificate, or complete zero census is supplied.**

## Exact accepting reconstruction

The standard-library checker uses only integers and `fractions.Fraction`. It has no dependency on mpmath, a zeta evaluator, numerical eigenvalues, or supplied zero locations. It independently reconstructs the source formal series as g=S'/S from S=sinh(sqrt(6t))/sqrt(6t), and compares it to the Jacobi continuants. It reconstructs Padé polynomials from factorial coefficients, not from the continuants being checked.

The retained receipt covers:

- 49 Padé orders, n=1,...,49, with 2,499 exponential matching coefficients and 1,274 positive modulus-polynomial coefficient comparisons; the full polynomial ODE and Wronskian identities also pass at every listed order.
- 24 exact source-to-Padé polynomial identities, 600 native sinh-series matching coefficients and 24 full rational square-residual identities.
- 400 elementary-symmetric correction coefficients, 5,000 full coefficient remainder comparisons (including omitted r>m tails), and five exact Laurent/hyperbolic ring identities. The ring check reduces cosh(u)^2-sinh(u)^2=1 rather than sampling hyperbolic functions.
- 49 rational bulk panels, 18 Mellin correction-factor panels and 40 correcting-denominator tests. The interpretation of the displayed bulk crossing counts uses the classical pi<22/7 bound; that transcendental inequality is not freshly certified by this checker.

These are bounded algebraic checks, not a machine proof of the all-order statements, Poisson limit, dominated-convergence estimates, gamma integral, or zero-convergence theorem. Those depend on the written mathematics in PROOF.md.

The accepting commands are

```
python -I -S -B check.py --check results.json
python -I -S -B -O check.py --check results.json
```

The standalone test commands are

```
python -I -S -B test_check.py
python -I -S -B -O test_check.py
```

Each seven-method suite executes one pristine accepting CLI and nine actual refusing CLIs: four altered-and-resealed result records, two malformed-and-resealed JSON records, one resealed mathematical source mutation, an unexpected inventory file, and unsealed proof drift. The mathematical mutation changes the first edge correction's sign, authenticates the altered source under a regenerated manifest, and is then refused by mathematical reconstruction. The four receipt corruptions include a Boolean/integer type alias. No test claims resistance to an adversary who replaces the entire trusted checker, manuscript, and manifest consistently.

## Ordinary numerical diagnostics, not certificates

`diagnostic.py` was run at 65 and 80 decimal working digits using mpmath. It evaluates orders 4,8,16,32,64 at q=3/4+i, 3/5+2i and 5/4+3i/10. All retained complex K values and displayed error fields agree between the two runs. This is agreement of one backend at two precisions, not independent implementations or directed error bounds.

The largest phase-weight discrepancy across all these nodes was about 6.55e-60 at 65 digits and 1.97e-74 at 80 digits. These numbers support consistency of the implementation only. The defining second-correction integral was also compared to the eta formula without directed quadrature remainders.

At q=3/4+i the first- and second-correction absolute remainders of K were approximately:

| m | After first correction | After second correction |
|---:|---:|---:|
| 4 | 3.613917e-4 | 9.084332e-5 |
| 8 | 3.506641e-5 | 2.622558e-6 |
| 16 | 2.718492e-6 | 5.587884e-8 |
| 32 | 1.882307e-7 | 1.014724e-9 |
| 64 | 1.235830e-8 | 1.705618e-11 |

No numerical rate fit enters the analytic proof. In particular the observed remainders do not establish a uniform third-order error or any all-height nonvanishing.

A separate development-only m=2 reflected-seed root scout and sampled winding computation were tried. They used ordinary special-function evaluations with no directed contour or complementary-tail budget. They are not adopted as zero counts or included in the accepting result. The present packet makes no new native or finite-approximant zero certificate.

## Source and delivery checks

The full supplied GHE26 proof's local Git-blob identity is `f9be5ed152a392232551d25c4d40e30568e3b058`, matching the freshly fetched live #877 file. Its SHA256 is `82ad62049bbc81b9d38b06bca3a3658364bf6e7e6f86dc1306dd50b895177269`. The parent entire numerical campaign was not rerun. Other reading boundaries are in SOURCES.json.

The local deliverable is additive. Clean extraction and a minimal Git application are delivery tests, not a complete repository checkout. The fixture retains the original parent proof and an unrelated sentinel and checks they remain unchanged. Any completed commands and return codes for this delivery are retained in the separate execution receipt shipped alongside the packet, rather than turning the packet's historical statements into a remote receipt.

No remote push, remote CI, full repository validator, Lean build, source-moment campaign for #881/#879, high-height xi-zero count, or independent mathematical acceptance was performed. Normal and optimized Python use the same rational backend. The manifest authenticates bytes relative to its original trusted copy; it is not an external proof checker.

The initial isolated test invocation exposed a harness-only import error: Python `-I` omits the script directory from import search. The harness was corrected to load its sibling checker by an explicit local file path. The mathematical checker had already passed in both modes; the subsequent complete test execution, not the failed initial invocation, is recorded in the delivery receipt.

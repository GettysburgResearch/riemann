# Fresh audit, two source imports, and routes beyond the 1/12 ceiling

**Status: fresh adversarial AI review and proposed component mathematics. No independently accepted 11/12 theorem, improved global zero-free region, or RH proof is announced.**

The reviewed object is PR #959, frozen at `7b845294207d96b883c1fa95028663082267804f`, not a moving branch. This packet adds new files only. It neither edits the reviewed argument nor changes the repository's integrated scientific status.

## What this pass actually contributes

1. **Audit:** a fresh comparison with CT v2's actual TeX, BGL Section 5, and de Faveri's family construction and density calculation. The central averaging composition is coherent at the interfaces inspected; no fatal inconsistency was found. Source-reference corrections, residual dependencies, and the limits of this review are explicit in `REVIEW_959.md`. This is not an external human referee report, a separate model ensemble, or a Lean build.
2. **Imports:** version-pinned, annotated imports of Frei--Sofos--Widmer (FSW) and Bhargava--Vemulapalli (BV), including hypotheses, applications and source locations. These are analytical notes, not mirrored PDFs. FSW's own conditional wording is retained.
3. **Sharper attack:** three estimates, not one, tie at the old endpoint. Two can be moved out of the way with existing inputs. The high-powerful part of the actual theta pairing already gains `tau/4`. A specific bound only for its complementary near-squarefree part would give the strict boundary **2747/3000 = 11/12 - 1/1000**. That bound remains OPEN; the fraction is a conditional target, not a new theorem about zeta zeros.
4. **Alternative geometric source:** the BV/Hecke period can be turned into an exact reciprocal-zeta Mellin detector by two ideal-Mobius convolutions. One convolution cancels zeta and detects nothing. An explicit product-Gamma kernel shows precisely where the original Mobius cancellation difficulty survives. A separate elementary argument upgrades BV's existence mechanism to a positive-measure statement in its applicable regime.

Read `REVIEW_959.md`, `THETA_ESCAPE.md`, and `GEOMETRIC_ROUTE.md`; `IMPORTS.md` and `SOURCES.md` give the external dependency map.

## Reproduce

```
python verify.py
python -O verify.py
python run_mutations.py
python verify_manifest.py
```

`CHECKS.json` contains 427 finite predicates from a newly written checker, including exact density substitutions, all-interval contour budgets, the three-way tie, the retuned conditional target, and finite local convolution identities. These are not 427 analytic proofs or computed L-values. Six deliberately corrupted models are separately executed under optimized Python and rejected. See `VALIDATION.md`.

The original #959 checker was not rerun in this pass. A different checker was written rather than treating its 1,344-predicate count as independent evidence. All imported analytic inputs remain named premises of the new component arguments; no upstream metaplectic foundation was reconstructed here.

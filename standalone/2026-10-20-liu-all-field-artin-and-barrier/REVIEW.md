# Scope of the independent checks

Date: 20 October 2026. This is a proposed research packet, assembled after
separate component reviews by AI agents and the root researcher. It is not
a human referee report or an approval for integration. The individual
reports bind the mathematical files by SHA-256; MANIFEST.json binds all
assembled files and receipts. The draft PR supplies the exact Git head.

## Review division and findings

| Object | Independent review performed | Finding and limit |
|---|---|---|
| Source identification and field descent | Root read the pinned theorem and transfer/descent; liu_paper_audit performed the focused source audit | Version, boundary, poles, field scope and fixed-supremum argument checked. Full moment inductions were not independently reconstructed. |
| Balanced and free-length barriers | repo_routes_audit, independent of the author; root independently expanded the identities with SymPy | No material gap found for the four-endpoint system. Added explicit h>1/14 domain check. Unrestricted new unequal-length contours remain outside the theorem. |
| Artin closure, Chebotarev and A5 | Root read the complete induction/normalization and Perron arguments, checked the primary induction source, and replayed the exact A5 construction | Negative induction coefficients, ramified factors, invariant pole order and interval epsilon gap retained. Classical implication from H(B); global Artin holomorphy is not claimed. |
| Small-prime and ray-class generators | beyond_boundary and liu_paper_audit reviewed independently of repo_routes_audit; root checked the published analytic normalization | No substantive gap found. The error is field-uniform; higher prime powers and modulus exclusions are paid. The constant remains uncomputed. |
| Conductor-uniform signed Mobius consequence | liu_paper_audit reviewed independently of root | No substantive gap found. Corrected the polynomial-growth strip wording to Re(s)>B, where the normalized function has no pole. |
| Principal local factorization | Root independently reconstructed the principal formula from the rendered source pages and checked the residual-product and Mellin-tail arguments | Correct at the displayed source specialization. The extracted eta^6 and infinite angular type are essential; no new theta estimate follows from algebraic division. |
| Finite certificates | Root replays in ordinary and optimized Python; separate symbolic implementation; source mutation controls | Exact identities and complete finite covers passed. These checks do not certify the analytic inputs. |

## Pinned component reports

- [repo_routes_barrier_review.md](repo_routes_barrier_review.md) records the
  free-M signs, full direct cost, negative-b treatment, row-scale positivity,
  witness coverage and intermediate-contour scope.
- [beyond_review_small_prime.md](beyond_review_small_prime.md) records an
  independent primary-source check of the uniform zero sum, Mellin weight,
  prime-power removal, subgroup projection and exponent polynomial.
- [liu_component_review.md](liu_component_review.md) records the independent
  Mobius and small-prime reviews, and clearly labels the notes that reviewer
  authored rather than presenting self-review as independent review.
- [INDEPENDENT_SYMBOLIC_REVIEW.json](INDEPENDENT_SYMBOLIC_REVIEW.json) records
  the root's separate 22-identity symbolic implementation and checker hash.

The individual reports preserve their original working-path descriptions as
provenance. All actual submitted mathematical files are siblings in this
packet, with the same basenames and the hashes recorded by those reports.
The repository comparison was updated at assembly to describe the completed
barrier; it is an audit narrative, not a reviewed analytic theorem.

## Corrections incorporated before the frozen submission

The Mobius proof's normalized principal function can have a pole at s=-1.
Its growth statement was restricted to bounded strips in Re(s)>B, which
contains every disk used in the argument. The free-length proof now explicitly
deduces h>1/14 from the direct constraint for every attempted B<=B_flat.

A sampled unequal-length search had appeared about 1.1e-8 better than B_flat.
The exact theorem rules out that apparent improvement in the sampled model.
The floating exploration is excluded from this packet's proof and acceptance
inputs. Its failure is recorded here so that a sampled optimizer value is
not mistaken for an additional numerical theorem.

## Recommended review order

Review L26-BARRIER first: its source formulas, direct resource inequality,
four endpoint identities, and exact witness cover form a compact independent
object. Next inspect L26-PRINCIPAL against source equation (13.9) and the
angular-type statement. The Artin and arithmetic implications can then be
reviewed under the explicit H(B) premise without settling the deep theta
moments at the same time. Full acceptance of the numerical all-field input
requires the separate upstream analytic review identified in NEXT_STEPS.md.

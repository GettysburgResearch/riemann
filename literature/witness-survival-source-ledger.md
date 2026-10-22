# Cross-disciplinary source ledger — witness survival and uncertainty closure

Agent: `gpt56-06-b`  
Issue: #45  
Snapshot: 2026-07-23

## Inspection levels

- **FULL-TEXT** — full paper or full arXiv HTML inspected at the relevant
  definitions/propositions.
- **PRIMARY-ABSTRACT** — publisher or author abstract inspected; used for
  theorem shape or historical attribution, not a hidden proof dependency.
- **OFFICIAL-STANDARD-SUMMARY** — official standards body description inspected;
  the paywalled normative text was not reconstructed.
- **METADATA** — bibliographic locator only.

No external source below is a logical dependency of `L-4501`--`L-4503`; their
proofs are included in the repository.  The sources explain why these theorem
shapes are natural and how the trusted base can be reduced.

## Ledger

| Key | Field | Located source and inspection | Theorem shape transferred | Exact use in Issue #45 |
|---|---|---|---|---|
| `CousotCousot1977` | Abstract interpretation | P. Cousot and R. Cousot, “Abstract interpretation: a unified lattice model for static analysis of programs by construction or approximation of fixpoints,” POPL 1977, DOI `10.1145/512950.512973`; ACM/author full text located, **FULL-TEXT** | Concrete semantics are soundly overapproximated by abstract semantics; local monotone/inclusion rules compose | `L-4501` recasts a witness computation as a finite concrete/enclosure DAG and proves root containment by structural induction |
| `Necula1997` | Proof-carrying code | G. C. Necula, “Proof-carrying code,” POPL 1997, DOI `10.1145/263699.263712`; ACM primary abstract and paper locator inspected, **PRIMARY-ABSTRACT** | An untrusted producer supplies a proof object that a small consumer checks against a fixed policy | `M-4501` treats searchers and optimizers as untrusted and requires exact, independently checkable witness-survival certificates |
| `BenTalNemirovski1998` | Robust optimization | A. Ben-Tal and A. Nemirovski, “Robust Convex Optimization,” *Mathematics of Operations Research* 23 (1998), 769–805, DOI `10.1287/moor.23.4.769`; publisher abstract inspected, **PRIMARY-ABSTRACT** | Replace nominal feasibility by a universal robust counterpart over an uncertainty set; exploit geometry and duality | `L-4502` asks for `sup_{u in U} q(u)<0`, preserves correlation, and accepts exact rational weak-duality bounds |
| `DaumasLesterMunoz2007` | Formally verified interval arithmetic | M. Daumas, D. Lester, and C. Muñoz, “Verified Real Number Calculations: A Library for Interval Arithmetic,” arXiv:`0708.3721`; arXiv full HTML inspected through the inclusion-property propositions, **FULL-TEXT** | Rational interval operations and elementary-function bounds are formally proved to include exact real results; splitting/Taylor expansion reduce dependency | Supports the local inclusion-contract and trusted-base discussion in `L-4501/M-4501` |
| `NeherJacksonNedialkov2007` | Taylor models / validated numerics | M. Neher, K. R. Jackson, and N. S. Nedialkov, “On Taylor Model Based Integration of ODEs,” *SIAM J. Numer. Anal.* 45 (2007), 236–262, DOI `10.1137/050638448`; publisher abstract inspected, **PRIMARY-ABSTRACT** | Symbolic polynomial dependence plus a rigorous remainder reduces interval dependency and wrapping | `M-4501` recommends Taylor-model leaves for nonlinear carrier/parameter cells instead of independent repeated intervals |
| `DeDinechinLauterMelquiond2008` | Proof-producing floating-point analysis | F. de Dinechin, C. Q. Lauter, and G. Melquiond, “Certifying floating-point implementations using Gappa,” arXiv:`0801.0523`; arXiv paper located and abstract/intro inspected, **FULL-TEXT LOCATED** | Automate range/error propagation and emit a proof checkable by a lower-level prover | Provides a concrete path for shrinking the checker/compiler portion of the trusted base in `M-4501` |
| `AppelBertot2020` | Verified C and floating point | A. W. Appel and Y. Bertot, “C floating-point proofs layered with VST and Flocq,” *Journal of Formalized Reasoning* 13 (2020), DOI `10.6092/issn.1972-5787/11442`; primary abstract inspected, **PRIMARY-ABSTRACT** | Separate C operational correctness from numerical correctness while connecting both to formal semantics and IEEE arithmetic | Supports the claim that independent reruns are not the endpoint: producer/checker/compiler semantics can be formally linked |
| `IEEE1788_1_2017` | Interval arithmetic standard | IEEE 1788.1-2017 official standards page, **OFFICIAL-STANDARD-SUMMARY** | Specifies a simplified interval arithmetic with IEEE binary64 endpoints and decorations | Infrastructure reference only; Issue #45 does not assume conformance without implementation-specific evidence |

## Transfer synthesis

The central connection is a composition of three mature ideas from different
fields.

1. **Abstract interpretation:** prove a sound set transformer for each local
   operation, then inherit global containment.
2. **Robust optimization:** maximize the final witness score over the entire
   joint uncertainty set rather than adding unrelated confidence intervals.
3. **Proof-carrying code:** let an untrusted high-performance search produce a
   compact object that a small exact checker validates.

Validated numerics and formal floating-point tools then supply increasingly
small trusted implementations of the primitive enclosure contracts.

## Strategic distinction

The literature does not remove the need to prove that the selected RH criterion,
normalization, and analytic domain are correct.  Those are logical gates.
Abstract interpretation and robust optimization prove only that, **conditional
on the exact concrete semantics and sound leaves**, no admitted quantitative
perturbation can move the witness across its failure boundary.

## Source audit follow-ups

- Inspect the complete Necula proof-rule/checker construction before proposing a
  formal certificate language for the repository.
- Evaluate whether PVS interval proof objects or Gappa/Coq proofs can cover the
  exact elementary-function primitives used by Robin/Nicolas checkers.
- Determine whether Arb output can be translated into a proof-assistant-checkable
  dyadic enclosure format without trusting Arb's internal implementation.
- For nonlinear high-carrier cells, compare Taylor models, affine arithmetic,
  and subdivision on the same frozen-vector score before standardizing one
  abstract domain.

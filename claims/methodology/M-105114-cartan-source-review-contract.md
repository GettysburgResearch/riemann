# M-105114 - Cartan source and collar review contract

Claim ID: M-105114

Status: **REVIEW CONTRACT**

Created: 2026-08-23

RH status: **unproved**

## Required checks

1. Normalize every function by an explicitly nonzero anchor before using a
   lower-modulus display.
2. Keep the completed-Xi variable fixed as
   \(\Xi_t(z)=\xi(1/2+iz)\); do not substitute the rotated
   \(\xi(1/2+z)\) normalization.
3. Track derivative order as fixed \(k\). Do not infer uniformity in a
   growing order.
4. Retain \(2r_1/(r_2-r_1)\),
   \(\log(r_3/r_2)\), and every radius-versus-diameter convention.
5. Count zeros with multiplicity. Repeated equal disks may overcount the
   geometric union but never undercount its nominal radius budget.
6. For the raw quotient route, charge exceptional disks only to \(F'\) and
   \(F''\). Add \(F\)-zero disks only when a log-derivative route really
   requires them.
7. Apply the sharp strict projection gate
   \(2S<\min(\Delta_T,\Delta_\eta)\).
8. Verify that every candidate boundary is contained in
   \(\overline D(a,r_1)\), or supply a different target domain.
9. Keep the L-105112 selector-domain distinction on the selected
   intermediate edge.
10. Retain actual selector norms, edge length, and any restricted-safe-set
   loss in the final envelope.
11. Require complete actual-pole manifests independently of the analytic
    zero cover. An exceptional-disk theorem is not a selector manifest.

## Source audit

The modern comparison source is Jean-Claude Cuenin,
"Schrodinger Operators with Complex Sparse Potentials," Lemma 34 and its
proof, [DOI 10.1007/s00220-022-04358-1](https://doi.org/10.1007/s00220-022-04358-1).
Its displayed inequality is not used verbatim: the proof normalizes the
anchor, and its Caratheodory step carries the dimensionless spatial ratio
retained in L-105114.

The general background source is Semyon Dyatlov and Maciej Zworski,
"Mathematical Theory of Scattering Resonances," Appendix D.1.3,
[author-hosted version 1.0](https://math.mit.edu/~dyatlov/res/res_final.pdf).
Again, L-105114 supplies its own normalized proof so that the source's
notation cannot silently change the amplitude or spatial scale.

## Fail-closed scope

The following remain false unless separately proved:

- a common anchor is automatic at the origin;
- qualitative order-one growth absorbs selector conditioning;
- a zero cover authenticates the actual quotient-pole manifest;
- a finite rectangle certificate yields a cofinal Xi sequence;
- the resulting absolute bound supplies a positive signed first moment;
- RCMV104530 or RH follows.

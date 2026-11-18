# PAPER-S002 — Berry and Keating,1999

**Identity.** M. V. Berry and J. P. Keating, *The Riemann Zeros and Eigenvalue Asymptotics*, SIAM Review41(2)(1999),236–266. DOI10.1137/S0036144598347497. Author-hosted full text: https://michaelberryphysics.wordpress.com/wp-content/uploads/2013/06/berry307.pdf . Publication metadata: https://epubs.siam.org/doi/10.1137/S0036144598347497 . Access2026-11-17.

**Audit scope.** Bibliography verified; full text obtained. Substantive partial reading of §§1–2 and6 plus end of§5. No claim that §§3–5 were fully read or their statistical/asymptotic calculations checked. Level0 complete; Level1 whole-work incomplete; local Level2 reconstruction of the dilation operator and missing boundary conditions only. No paper-wide Level3.

## Exact content inspected

Equations(2.3)–(2.5), pp239–240, separate the smooth zero count from the fluctuation involving a chosen branch of logζ. The Euler-product expansion(2.6) is explicitly presented as divergent on the critical strip. Its plots do not constitute a convergent trace identity without test functions or regularization. The quantum Gutzwiller expression(2.9) is a semiclassical asymptotic, with exactness reserved for special settings such as Selberg's formula. These are different statuses.

In§6, equations(6.1)–(6.5), pp260–261, H_cl=XP generates X(t)=X(0)e^t, P(t)=P(0)e^(−t). The symmetrically ordered formal differential expression is H=−i(Xd/dX+1/2), with generalized modes X^(−1/2+iE). The monomial form does not establish normalizable eigenvectors, discrete spectrum or zero correspondence. The phase-space truncation can reproduce the smooth count, but closing the classical/quantum dynamics remains an explicitly unresolved problem (p261).

The Fourier transform of the even homogeneous mode produces gamma factors and a phase involving θ(E), equation(6.6), p262. Formal relations to the functional equation therefore have a concrete Mellin/Fourier source. On p262 the paper identifies the missing task as boundary conditions making a well-defined Hermitian operator with discrete eigenvalues. It also rejects the naive integer-dilation superposition as an immediate solution: integers do not form a group under multiplication, and a ζ-factor in a formal mode gives no reason to impose its vanishing. Equation(6.12), p263, is a functional identity, not a boundary condition selecting zeros.

## Context and dependencies

Prime explicit formulas → periodic-orbit heuristic → smooth density and GUE-statistical analogies → candidate XP dynamics → unresolved compactification and boundary domain. The candidate properties(a–j),p260, are diagnostic conjectural requirements, not jointly established theorems constructing H.

## Independently checked portion

On L²(R_+,dx), U f(y)=e^(y/2) f(e^y), y∈R, is unitary and UHU^(−1)=−i d/dy. Thus the natural complete half-line realization has continuous spectrum R. This is an elementary check, later treated explicitly by PAPER-S003; the paper does not assert that this bare realization solves RH.

## Obstacles and next step

A finite compact first-order graph fixes discrete spectrum but has only linear positive spectral count; PAPER-S003 makes this obstruction rigorous. Matching the leading smooth KlogK count through an energy-dependent phase-space cutoff is insufficient to define a single self-adjoint operator. Next inspect whether a proposed energy-dependent endpoint matrix has a self-adjoint auxiliary realization, and quantify the number of auxiliary states needed. See `proposals/independent_campaigns/spectral_counting_barrier.md` for an elementary finite-channel lower bound. No claim of novelty for that calculation.

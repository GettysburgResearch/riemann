# Spectral campaign: finite-channel counting curvature

Status: scoped independent review completed; see `audits/adversarial_reviews/graph_skeptic.md` and `audits/adversarial_reviews/director_adjudication.md`. No novelty claim. No implication that an RH proof has been found. Source papers: PAPER-S001, S002, S003; the independent calculation below sharpens the useful form of an established finite-graph obstruction. Execution: 2026-11-17.

## Mathematical goal

Determine how many channels a compact first-order Berry–Keating graph approximation needs to match the zero-counting function at several heights. A fixed compact graph is already excluded by linear versus T log T Weyl growth. Allowing the graph to grow with the height can conceal that elementary obstruction. We test the stronger requirement of reproducing the curvature of the counting function to additive o(T) accuracy.

## Model and exact assumptions

A graph consists of E finite edges [a_j,b_j], 0<a_j<b_j<∞. On the direct sum of L²(dx) spaces let H_j=−i(x d/dx+1/2), with any self-adjoint, energy-independent endpoint coupling. Put l_j=log(b_j/a_j)>0 and L=∑l_j. By y=log(x/a_j), g_j(y)=sqrt(x) f_j(x), the model is unitarily equivalent to −i d/dy on intervals [0,l_j]. Every self-adjoint endpoint coupling has the form g(0)=S g(l), S unitary. Consequently k is an eigenvalue iff det(I−S diag(e^{ik l_j}))=0, with eigenvalue multiplicity equal to the dimension of the kernel. This is Endres–Steiner Proposition9.1, equations(82)–(83), with the log-coordinate reduction explicit.

Only this fixed first-order model is considered. Energy-dependent couplings, noncompact graphs, growing internal Hilbert spaces, nonlocal perturbations and scattering resonances lie outside the proposition. The finite graph itself may depend on the target height K, but its S and lengths must be fixed when comparing K,2K,4K.

## Proposition S-C1 (uniform finite-channel count)

Let N_H(K) count eigenvalues in (0,K], with multiplicity, K>0. There is a real constant C and a function F:[0,∞)→[0,E) such that

    N_H(K) = LK/(2π) + C − F(K).

In particular |N_H(K)−LK/(2π)|<E, and

    |N_H(4K)−3N_H(2K)+2N_H(K)| < 3E.

Endpoint values use the floor convention so zero eigenvalues at k=0 are excluded and eigenvalues at K are included. The inequalities may safely be weakened to ≤ at degeneracies without changing any conclusion.

### Proof

Set U(k)=S exp(ikD), D=diag(l_j)>0. On each compact k interval choose continuous real lifts θ_j(k) of the E eigenphases, with relabeling through crossings. Finite-dimensional analytic perturbation gives piecewise analytic branches; at a simple eigenvalue U(k)v=e^{iθ}v,

    θ'(k) = v*D v > 0,

since U*U'=iD. At a multiple eigenvalue the possible one-sided phase derivatives are eigenvalues of the positive compression of D to the eigenspace, so all crossings of phase 0 mod2π are positive. Moreover

    ∑[θ_j(K)−θ_j(0)] = LK,

by det U(k)=det(S)e^{ikL}. Counting crossings, including multiplicity, gives

    N_H(K)=∑[floor(θ_j(K)/(2π))−floor(θ_j(0)/(2π))].

Therefore F(K)=∑ frac(θ_j(K)/(2π)) and C=F(0), establishing the representation and first bound. In the dyadic combination both C and the linear term cancel, leaving 3F(2K)−F(4K)−2F(K), strictly between −3E and3E. This argument concerns phase flow of a finite unitary matrix, not semiclassical quantization. ∎

An alternative route to audit is a finite-deficiency spectral-shift comparison with E decoupled periodic edges. That route gives a weaker sufficient O(E) remainder without relying on individual phase branch notation.

## Corollary S-C2 (three-height complexity barrier)

Let N_ζ(T) count nontrivial zeta zeros with 0<Imρ≤T, including multiplicity; RH is not assumed. Use the established Riemann–von Mangoldt formula

    N_ζ(T)=T/(2π) log(T/(2π))−T/(2π)+O(logT).

This is an external classical dependency (Endres–Steiner equation32 records it); its original proof has not been audited here. Direct subtraction gives

    N_ζ(4K)−3N_ζ(2K)+2N_ζ(K)=K log2/π+O(logK).

If a sequence of the finite graphs above, of E_K edges, satisfies

    max_{m∈{1,2,4}} |N_{H_K}(mK)−N_ζ(mK)| ≤ ε_K K,

then

    3E_K ≥ K log2/π − 6ε_K K − O(logK).

In particular ε_K→0 implies

    liminf E_K/K ≥ log2/(3π) ≈0.0735452.

This lower bound persists even when the total length L_K grows like logK and makes the leading K logK density agree. It is a lower bound for this model class and this strong absolute-count accuracy. It does not rule out weaker relative-error approximations, models whose scattering matrices depend on energy, or all spectral approaches to RH. It does not prove that the bound is sharp.

## Harmless scalar potentials do not evade the bound

For −i d/dy+V_j(y), with real V_j∈L∞([0,l_j]), the unitary gauge f_j(y)=exp(−i∫_0^y V_j)g_j(y) removes V_j and changes only the fixed endpoint unitary S. Thus the proposition remains true. A proposed potential modification must change more than a bounded real scalar first-order gauge term to evade this argument.

## Tests and negative knowledge

`experiments/code/spectral_counting_barrier.py` uses exact fractions to count spectra of three decoupled loops and checks the stronger 3E dyadic bound at five heights. It does not implement arbitrary coupled graphs or compute zeta zeros. Its floating RVM main-term column is illustrative only; the corollary is analytic. A leading-density match alone passed the initial intuition but failed the three-height accuracy test mathematically. The finite graph family cannot have sublinear channel count and o(K) counting accuracy at all three heights.

## What would make this publishable?

First perform a serious novelty search in quantum-graph spectral flow and counting discrepancy; this proposition is elementary enough to be known. Then seek a substantially sharper invariant involving the prime-side trace formula, or prove quantitative lower bounds for energy-dependent S(k) under causality/self-adjoint-realization constraints. A precise next question is: if S(k) arises by eliminating a self-adjoint auxiliary system of M degrees of freedom, can the dyadic curvature be bounded by O(E+M) plus a controlled scattering-phase term? Do not assume every unitary S(k) is the boundary data of a single self-adjoint operator.

## Adversarial review questions

1. Verify the orientation of boundary conditions and phase derivative.
2. Check phase labeling and crossing multiplicity through degeneracies.
3. Check endpoint floors, especially a zero eigenvalue at k=0.
4. Re-derive the3E bound without relying on a choice of phase branch.
5. Search known quantum graph counting results before any novelty statement.
6. Test a non-diagonal unitary S numerically; numerical agreement is supplementary only.

## Provenance search update

A primary-source search found the underlying phase-flow/counting-discrepancy mechanism already presented by Sven Gnutzmann and Uzy Smilansky, *Quantum Graphs: Applications to Quantum Chaos and Universal Spectral Statistics*, arXiv:nlin/0605028v2,§5.1,pp36–38, especially equations(5.5)–(5.11). The phase derivative bounds and bounded oscillatory count are therefore established quantum-graph machinery, independently reconstructed here. The three-height subtraction is an elementary consequence; its novelty has not been established and should not be advertised as a new theorem. Their standard quantum graph has2B directed channels, whereas our first-order model hasE channels; channel counting and positive/absolute spectral conventions must not be mixed. Primary corrected PDF: https://arxiv.org/pdf/nlin/0605028v2 .

## Complement: why the disconnected infinite butterfly escape loses local trace mass

PAPER-S006 supplies an explicit alternate regime: components with two equal directed lengths L_m=m logp for a fixed primep and arbitrarily largem. Each component has two eigenvalue grids k=(2πn−θ_j)/L_m, n∈Z, regardless of its unitary vertex eigenphasesθ_j. In any fixed open interval I of lengthδ>0, each grid contributes at leastδL_m/(2π)−1 points. Thus the component alone has

    N_m(I) ≥ δL_m/π−2 →∞.

Consequently the disconnected direct sum cannot have a locally finite counting measure. Every open interval contains infinitely many component eigenvalues, and its spectral trace on a nonzero nonnegative compactly supported test function is infinite (choose a subinterval where the function is bounded below). This is an elementary independent reconstruction of the source's stated infinite-density limitation, not a new criticism of that paper.

The finite and infinite obstructions have different hypotheses and cannot be conflated: the finite model has too little count curvature, whereas this particular infinite model has too much positive local spectral mass. A mean-subtracted oscillatory distribution may exist after renormalization without being the trace measure of an operator with compact resolvent. A candidate construction must specify which of these objects it claims to identify with the zeros.

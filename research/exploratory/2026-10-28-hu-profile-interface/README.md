# Common-profile and tail interface for the variable low-side calculation

**Status:** Elementary separation lemma plus a source-specific dependency audit. This is not an independent proof of Hu's reflection identity, its conductor ledger, or a zero-free region. It concerns the proposed [variable low-side calculation](../2026-10-28-hu-variable-low/README.md).

**Source:** Boyang Hu, [*A seven-eighths zero-free half-plane for unitary Weil L-functions*](https://hexagonmath.org/2610.00216v1), §§4 and 6.5, specifically Lemma 4.8, its coefficient-independence paragraph, kernel bound (4.24), tails, and (6.22). The exact source PDF hash is recorded in the linked candidate note. No claim is made that the elementary lemma below verifies every source hypothesis.

## Abstract common-profile lemma

Fix `n`, real exponents `a_1,...,a_n`, a compact box `I` in `R^n`, and a smooth cutoff `chi` supported in the interior of `I`. Suppose `K` is smooth on `(0,infinity)` and, for every integer `j>=0` and every `A>=0`,

    sup_(r>=1) r^A |(r d/dr)^j K(r)| <= C_(j,A).

For `R>=1`, define

    F_R(x) = chi(x) K(R exp(sum_i a_i x_i)).

Then there is an absolutely integrable Fourier density `Fhat_R` with

    F_R(x) = integral Fhat_R(xi) exp(i xi dot x) dxi,
    integral (1+|xi|)^m |Fhat_R(xi)| dxi <<_(I,chi,a,m,A) R^(-A)

for every `m,A>=0`. One proves this by applying `(1-Delta_x)^k` for a fixed integer `k` large enough to make `(1+|xi|)^m(1+|xi|^2)^(-k)` integrable. The compact support of `chi`, bounded `exp(sum a_i x_i)` on `I`, and the derivative hypothesis give an `L^1` bound of order `R^(-A)` for every derivative needed. Fourier inversion gives the representation. When `x_i=log(q_i/Q_i)`, each factor is `(q_i/Q_i)^(i xi_i)`, a product of independent unit-modulus norm phases.

If the variables consist of a row, a slot product, and dual squarefree/cube variables, this separation alone does not reorganize a coefficient: it only multiplies the already factorized row, slot, and dual factors by their respective norm phases. Thus it preserves a pre-existing statement that the slot coefficient is independent of row and dual variables, and that the dual coefficient is independent of row and slot variables. It does not create that statement when collisions or masks couple the variables.

If `R ~ Z^r` with `r>=tau>0`, where the implied scale constants are fixed, the Fourier density above has arbitrarily large power saving `Z^(-A tau)`. For a fixed finite number of slots, any independently proved polynomial-in-`Z` count of dyadic blocks or frozen terms can be absorbed by taking `A` sufficiently large. This absorption is uniform for all exponents in a fixed compact range, provided the constants in the derivative bounds are uniform in that range. The order `A`, number of slots, arithmetic data, and support factors are fixed before sending `Z` to infinity. A count whose exponent itself grows with `A`, or an unverified uniformity in a varying number of slots, is not covered.

## Matching what is available in Hu

Hu §4 explicitly fixes the field, a finite set of local characters, a representative modulo global norm twists, and compact profile supports. His arithmetic normalization absorbs finite-order background into the finite group and allows a genuinely infinite-order fixed unitary background. His proof of Lemma 4.8 freezes classes, extracts the local minima and the unrestricted cube, and states that the resulting slot coefficient is independent of the row and dual variables and the dual coefficient is independent of the row and slot variables. It handles active collision masks explicitly and sums inactive prime tuples before reflection. These are source **assertions**, not deductions newly checked here.

For the variable-geometry candidate with `0<=d<=ell<=1/5`, the exponents of `X',Y',M',ell'` remain in fixed bounded ranges, and the tests remain the same fixed compact profiles evaluated at different positive dyadic scales. The unitary target factors introduced by the finite compensation have absolute value one and are indexed by the prime tuple, so merely changing `b,ell,d` does not by itself create a row-dependent coefficient. Finitely many unit sectors and fixed local exclusions also do not depend on `Z`. This establishes a plausible source-level matching, subject to verifying that Hu's frozen decomposition and original zero extensions are literally the same after each rescaling.

Hu's proof describes the separated kernel factor (4.24) and a tail `C_A Z^Btail Z^(-(A-sigma)tau_ref/2)` for a positive fixed retention margin. If its stated derivative/seminorm and absolute-series hypotheses apply uniformly to the rescaled argument, the elementary lemma explains why changing the fixed geometry does not itself destroy the tail: all relevant scale exponents remain bounded, so a common tail order can be chosen for finitely many subsets. A fixed norm twist changes finitely many seminorm constants or polynomial height factors; the candidate must use a fixed target and choose height costs after the slot system, as in Hu. This paragraph is a conditional application of Hu's statement, not an independent derivation of his kernel estimates.

## Remaining load-bearing gap

The missing proof is a source-faithful map, for **every** rescaled subset and actual local annulus, from the marked physical coefficients in Hu (6.1), (6.9) to the frozen variables and masks in Lemma 4.8. It must establish the conductor comparisons `2A0<=O+o(1)` and `N0<=A0`, the correct completed and row exponents, and the retained dyad/tail conditions without replacing a shared coefficient by independent surrogate data. After that, verify the common profile and primitive ideal counting for the original unit-sector quotient and every marked exclusion, together with the fixed-target seminorm and height order. Hu establishes the fixed geometry; whether his proof provides all these assertions for variable geometry remains to be checked line by line. The algebraic [variable-energy lemma](../2026-10-28-variable-energy-lemma.md) starts only after these hypotheses are in hand.

**What was done:** proved the abstract Fourier-separation lemma and inspected the specified source statements; no numerical work, Lean build, or full replay of the theta/reflection argument. No high-side or new zero-free estimate follows from this note.

## Candidate puncture and support matching

A direct comparison of the physical summand (6.9) with Hu's definitions (6.1) and (3.20) gives a more specific, still source-dependent interface. For a fixed tuple and subset `J`, the marked completed row is `B_{m,psi;p_(J^c)}`: in (3.20) take the puncture `r=1`, and the marks to be the primes with indices in `J^c`. The character `psi` enters the completed coefficient `vartheta`; it is not the squarefree puncture `r`. Mark tuples meeting the row are zero on the primal side and are removed before reflection, exactly as Hu states. The subset `J` changes the scales and adds its outside tuple coefficient, but does not insert a second puncture into (6.1).

For a nonzero exterior row ideal, choose its canonical factorization `(m)=h d` with `h` powerful (all prime valuations at least two), `d` squarefree and `(h,d)=1`. Then Hu's frozen support `P0=supp(h) union supp(r)` is just `supp(h)`. His reflection label `f` is a squarefree product of primes of `P0`, so

    2 log_Z(Nf) <= log_Z(Nh).

This exact ideal inequality holds before taking dyadic logarithms; fixed annular endpoint constants add only `O(1/log Z)`. It supplies the comparison `2A0<=O+o(1)` **if** Hu's `A0` is identified with the length of this `f` and the row factorization is preserved through all unit sectors. The companion [variable-energy lemma](../2026-10-28-variable-energy-lemma.md) contains the corresponding abstract support inequality and keeps `N0<=A0` as a separately checkable local-table assertion.

This matching is an observation from displayed definitions, not yet an audit of every Fourier separation and row restriction. A complete proof must still show that no moving puncture is introduced in carrying the actual physical row to Lemma 4.8, that inactive mark exclusions remain precisely those of Hu's reflection, and that the `j=4` contribution counted in `N0` is a subproduct of the same frozen `f`. In particular these logical identifications cannot be supplied merely by calling the fixed-geometry (6.22).

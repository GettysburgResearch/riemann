# Director adjudication: first-generator membership and exact character transfer

17 November 2026. I derived the first-derivative/multiplicity argument independently and read the two independent zeta proofs (jump_generator63_single_member_skeptic.md and the updated proponent note), the two independent character proofs (jump_generator63_dirichlet_skeptic.md and jump_generator63_fixed_character_independent.md), and the primary antecedent map jump_generator63_antecedents.md. The proof is a specialization of established discrete Nyman–Beurling/Mellin closure reasoning. Balazard's Proposition11 supplies the general all-multiplicity holomorphy obstruction; Manzur–Noor supplies the explicit group. No publication-priority claim is made.

## 1. One explicit vector

For fixed k≥2 put f_k(x)=k floor(x/k)−floor x, and W=closed span{f_j:j≥2} in S=L²([1,∞),dx/x²) restricted to integer cells. The established integer-span criterion gives RH iff W=S. The exact statement is

    RH iff G f_k∈W, for every individually fixed k≥2.

The bounded periodic f_k lies in Dom G. The difference quotient is bounded coordinatewise by 2‖f_k‖∞ log n, whose square is summable against w_n. Write q=floor(n/k). Its generator has the entirely explicit cell value

    (Gf_k)_n=i[k log(q!)+kq log k−log(n!)].

For k=2, dropping the irrelevant scalar i gives the target log[4^q(q!)²/n!]. These are O(log n) sequences, not zero labels. The closure membership remains the unresolved assertion.

On Re s>1/2,

    s M f_k(s)=F_k(s)=ζ(s)(k^(1−s)−1),
    M(Gf_k)(s)=−i F'_k(s)/s.

The factor cancels the zeta pole at1. If an off-line zero ρ has order m, each of the continuous Mellin jets of orders0,…,m−1 annihilates W. Their norm bound is

    ‖L_(ρ,a)‖≤sqrt((2a)!)/(2Reρ−1)^(a+1/2).

The factor k^(1−ρ)−1 is nonzero for 1/2<Reρ<1. Hence

    L_(ρ,m−1)(Gf_k)=−i ζ^(m)(ρ)(k^(1−ρ)−1)/ρ≠0.

There is no extra factorial. This contradicts membership for every possible off-line multiplicity. The functional equation supplies a right-hand zero if needed. Conversely RH makes W=S. No zero-density theorem is used in this converse, unlike the fixed finite-time source criterion.

For a specified off-line zero this also gives the explicit distance lower bound in the independent proof. Since f_k∈W and J_t f_k=f_k+tGf_k+o(|t|),

    dist(J_t f_k,W)=|t|dist(Gf_k,W)+o(|t|).

The actual generator's integer spectrum supplies no zeta zero list. Critical-line evaluations are not continuous on S; this proof excludes off-line zeros and does not assert simplicity. The graph-domain topology must not silently replace the closure topology.

## 2. General Dirichlet characters need the correct space

For a fixed nonprincipal character χ, fχ(x)=Σ_(n≤x)χ(n) is bounded periodic. Let Xχ be the closed span of its integer dilates, with no zero-at-one anchor. The same argument, using M fχ=F/s and M Gfχ=−iF'/s, proves

    GRH for χ iff G fχ∈Xχ.

The forward density input is the established qualitative unrestricted p=2 character criterion, checked in Dimitrov–Oliveira; it needs no optimized rate. In the reverse, the(m−1)-jet detects every right-strip zero of order m. Real zeros are included. The same-character functional reflection and the classical boundary nonvanishing cover the rest of the nontrivial strip.

For a principal character the raw summatory seed grows linearly and is outside S. Use the bounded pole-cancelled gχ,k(x)=Sχ(x/k)−Sχ(x)/k and its anchored span Wχ. For every fixed k≥2,

    RH for its inducing zeta function iff G gχ,k∈Wχ.

For a nonprincipal character this anchored variant is instead always false: evaluation at1 annihilates Wχ but M(Ggχ,k)(1)=iF(1)log k/k≠0. This is the infinitesimal form of the already verified anchor obstruction. The unanchored nonprincipal and anchored principal statements have different admissible spaces for a mathematical reason.

## 3. Exact finite-Euler-factor transport of closures

Let U_d b(x)=b(x/d), with zero extension below1. Its norm on S is d^(−1/2). The finite Euler polynomial E(U) relating an induced character to its primitive inducer is boundedly invertible by commuting geometric Neumann series. The unrestricted character span is invariant under every U_d. The anchored span is also invariant, since U_d gχ,k=gχ,dk−gχ,d/k. Thus E(U) acts onto the same inducing closed span, proving unconditionally Xχ=Xχ* in the nonprincipal case and Wχ=Wχ* in both cases. For principal characters the finite inclusion–exclusion identity must be applied pointwise before anchoring the linearly growing raw seed.

The commutator is [G,U_d]=i log d U_d, so [G,E(U)] sends the relevant inducing seed to its own closed span. This proves exact first-generator membership transfer under induction. Added Euler-factor zeros lie on Re0 and do not change the argument. These are closure identities; the earlier finite-cutoff sandwich is still needed for approximation rates and polynomial lengths.

The known Balazard criterion, the source finite-time operator theorem, this infinitesimal specialization and the character transfer are recorded as related exact implications with different inputs. None furnishes a proof that its unresolved arithmetic membership holds.

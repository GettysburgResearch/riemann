# Weighted unrestricted-coefficient criteria and limit quantifiers

Independent source/mathematical audit, 2026-11-17. This is a reconstruction of standard Mellin–Hardy-space reasoning, with no novelty claim. It separates the valid unrestricted-coefficient weighted criterion from the prescribed Selberg-family issue documented in `audits/selberg_provenance_round2.md`.

## Definitions and conclusion

For a finite Dirichlet polynomial D(s)=Σ_{n≤N}a_n n^(−s) and an integer q≥1, write

d_q(D)²=(1/(2π))∫_R |1−ζ(1/2+it)D(1/2+it)|² dt/|1/2+it|^(2q).

The coefficient vector may be complex; the conclusions also hold if coefficients are restricted to real numbers. Let

δ_q(N)=inf_{a_1,…,a_N} d_q(D).

Then **RH is equivalent to δ_q(N)→0 for every fixed integer q≥1**. Equivalently one may use liminf_N δ_q(N)=0, since δ_q(N) is nonincreasing.

More quantitatively, every nontrivial zero ρ=β+iγ with β>1/2 gives the uniform lower bound

d_q(D) ≥ √(2β−1) |ρ−1| / |ρ|^(q+1),

for every finite D, independently of its length and coefficients. The constant is positive because ρ≠0,1. This proves the converse even for a subsequence of an arbitrary prescribed coefficient family.

The inner multiplier used below gives a stronger bound than the factor (s−1)/(s+1) initially considered: no extra norm constant is necessary.

## Primary-source grounding

1. Báez-Duarte, *A strengthening of the Nyman–Beurling criterion for the Riemann hypothesis, 2*, arXiv:math/0205003v1, Theorem1.1 printed pp.1–2 and proof pp.4–6, supplies the q=1 discrete closure criterion. Its shifted real Möbius arrays also show that real coefficients suffice under RH. Existing archive record: PAPER-E001.
2. Wei–Wu, *A characterization of the zero-free region of the Riemann zeta function and its applications*, *Expositiones Mathematicae*40(4) (2022),961–993, DOI [10.1016/j.exmath.2022.07.004](https://doi.org/10.1016/j.exmath.2022.07.004), institutional manuscript at https://bimsa.net/doc/publication/1424.pdf . Proposition2.14, printed p.12, states that the Mellin transform is an isometric isomorphism from L²(0,1] onto H²(Re(s)>1/2). Proposition2.3, printed p.8, supplies point-evaluation continuity; the exact evaluation constant used here is independently derived by Cauchy–Schwarz below. Its introduction, pp.3–4, already uses the pole-canceling factor (s−1)/s in connecting the classical norm to Hardy-space functions. Archive record: PAPER-C105.
3. Ehm, *On certain Gram matrices and their associated series*, arXiv:2405.06349v2, printed p.1 equations(1)–(2), says the unrestricted q=2 criterion follows from q=1. The proof below validates that statement. It does not validate the later fixed-array RH-alone reverse implication.

The proof below uses only the stated standard Mellin–Hardy facts and elementary identities; no RH-dependent zeta growth bound is used for Hardy-space membership. The full source papers are not newly counted as read by this scoped audit.

## 1. Integrability and an explicit Hardy-space representation

Put A=D(1)=Σa_n/n and define, for 0<x≤1,

h_D(x)=1+Σ_{n≤N}a_n {1/(nx)}.

This is bounded, hence belongs to L²(0,1). Let

H_D(s)=∫_0^1 h_D(x)x^(s−1)dx.

By Mellin–Paley–Wiener, H_D belongs to the Hardy space of the half-plane Re(s)>1/2, with norm

||H_D||²_H²=||h_D||²_L²(0,1),

where the Hardy norm uses boundary measure dt/(2π). The integral defines an analytic function for Re(s)>0.

The fractional-part Mellin identity, for 0<Re(s)<1, is

∫_0^∞ {1/(nx)}x^(s−1)dx=−ζ(s)n^(−s)/s.

For x>1, {1/(nx)}=1/(nx), so its tail integral is 1/[n(1−s)]. Subtracting the tail yields

∫_0^1 {1/(nx)}x^(s−1)dx=−ζ(s)n^(−s)/s+1/[n(s−1)].

Consequently,

H_D(s)=[1−ζ(s)D(s)]/s+A/(s−1).                 (W1)

The apparent singularity at s=1 in this expression cancels. Identity(W1), initially obtained in the strip, holds by analytic continuation throughout Re(s)>0, with that removable singularity understood.

This identity also shows directly that the full critical-line q=1 error is square-integrable: its boundary function is H_D(s)−A/(s−1), a sum of two L² boundary functions. Since |s|≥1/2 on the critical line, every q≥1 error integral is finite as well.

## 2. The correct pole-canceling inner function

Let

b(s)=(s−1)/s.

For Re(s)>1/2,

|s|²−|s−1|²=2Re(s)−1>0.

Thus b is analytic and bounded in modulus by1 there. On the boundary Re(s)=1/2, its modulus equals1. It is precisely the half-plane Blaschke factor for the point1. Multiplication by b is a bounded multiplier of H² and preserves the boundary L² norm.

For integer q≥1 define

F_(q,D)(s)=b(s)[1−ζ(s)D(s)]/s^q.

Using(W1),

F_(q,D)(s)=b(s)H_D(s)/s^(q−1)−A/s^q.          (W2)

Each term belongs to H²(Re(s)>1/2): b and s^(−q+1) are bounded analytic multipliers, while 1/s^q is itself a Hardy-space function. Explicitly, its vertical-line squared integral is a constant times σ^(1−2q), uniformly bounded for σ>1/2. Hence(W2) proves Hardy-space membership without inferring it merely from an L² boundary trace.

Because |b|=1 on the boundary,

||F_(q,D)||_H²=d_q(D).                       (W3)

There is no factor2 and no inequality loss in(W3).

## 3. Point evaluation and the off-line-zero lower bound

If F∈H²(Re(s)>1/2), Mellin–Paley–Wiener provides f∈L²(0,1) such that F(s)=∫_0^1 f(x)x^(s−1)dx and ||F||=||f||. For ρ=β+iγ with β>1/2, Cauchy–Schwarz gives

|F(ρ)|≤||f|| [∫_0^1 x^(2β−2)dx]^(1/2)
       =||F||/√(2β−1).                      (W4)

If ζ(ρ)=0, then directly from the analytic definition of F_(q,D),

F_(q,D)(ρ)=(ρ−1)/ρ^(q+1).

Combining(W3) and(W4) proves

d_q(D)≥√(2β−1)|ρ−1|/|ρ|^(q+1).              (W5)

This argument does not evaluate an arbitrary L² boundary function at a boundary zero. It evaluates a rigorously constructed Hardy-space function at an **interior** point β>1/2. The distinction prevents an invalid extension of(W5) to β=1/2. At a critical-line zero the displayed lower bound degenerates to0, as it should.

## 4. The weighted unrestricted-coefficient equivalence

On the critical line |s|≥1/2, so for every D,

d_q(D)≤2^(q−1)d_1(D).                       (W6)

Under RH, the established q=1 discrete criterion provides length-N approximants whose errors tend to0. Equation(W6) then implies δ_q(N)→0 for each fixed q≥1.

Conversely, if δ_q(N) has a subsequence tending to0, an off-line zero in Re(s)>1/2 would contradict the positive lower bound(W5), which holds for **every** D. By the functional equation, the absence of nontrivial zeros on the right of the critical line also excludes nontrivial zeros to its left. Thus RH follows.

Since the length-at-most-N spaces are nested, δ_q(N+1)≤δ_q(N). It is therefore immaterial whether the optimized criterion is written as a limit or a liminf. An infimum need not be attained for this argument: choose an approximant within an arbitrarily small positive error of it.

Real coefficients suffice in the forward implication because the established q=1 proof gives real coefficients. The converse lower bound applies even to complex coefficients.

## 5. Prescribed families and the quantifier boundary

Let D_N be any prescribed family, including the fixed logarithmic Selberg family. The sequence d_q(D_N) need not be monotone.

* If liminf_N d_q(D_N)=0, choose a subsequence tending to0. Equation(W5) proves RH.
* This does not follow from the optimized criterion in reverse: RH⇒δ_q(N)→0 does not choose D_N or bound its error.
* If the exact fixed first-order Selberg family satisfies d_1(D_N)→0 for the **full sequence**, Wei–Wu Proposition1.9 proves simplicity as well as RH. The separately reconstructed q≥1 extension follows by applying Hardy integration to the reciprocal fractional-part transform.
* That simplicity argument uses a global little-o estimate Ψ(x)=o(√x log x) derived from bounds at every sufficiently large integerN. A sparse convergent subsequence gives only Ψ(N_k)=o(√N_k log N_k). It does not give the global estimate used in the pole argument.

Accordingly, this audit establishes RH from liminf prescribed error0, but **does not establish simplicity from that liminf**. It also does not prove that such a simplicity implication is false; it records the exact missing uniformity. The inspected Wei–Wu statement assumes full convergence.

A precise optional strengthening illustrates the missing condition. If the prescribed Selberg error tends to0 along N_k and, additionally,

N_(k+1)−N_k=o(√N_k log N_k),

then the known small-interval bound gives Ψ(N_k)=o(√N_k log N_k). Since Ψ′(x)=M(x)/x almost everywhere and |M(x)|≤x, Ψ is1-Lipschitz on[1,∞). The stated mesh condition therefore extends the little-o bound to every realx, recovering simplicity through the same pole argument. This is an elementary conditional interpolation observation, not a claim about arbitrary sparse subsequences or a novelty claim.

## 6. A coefficient witness at the canceled pole

The same Hardy representation has F_(q,D)(1)=−D(1), because the residue of ζ at1 is1. Point evaluation at1 has norm1 under the stated normalization. Hence

d_q(D)≥|D(1)|, for every integerq≥1.

For the prescribed Selberg family, Ehm §7.1's unconditional reciprocal Möbius moments give D(1)∼1/log N. Therefore its error obeys d_q(D_N)≥(1+o(1))/log N for every fixed integerq≥1. Additional spectral downweighting alone cannot make this same prescribed family o(1/log N). This observation does not give a rate lower bound for the optimized infimum, because arbitrary coefficients can enforce D(1)=0. It is an elementary consequence of the pole-canceling Hardy representation, with no novelty claim.

## Findings and reuse

Classification: **correct weighted unrestricted criterion, but liable to be conflated with a prescribed-family convergence statement**. The H² membership and evaluation steps have explicit representations and constants. No mathematical error was found in Ehm's unrestricted q=2 criterion.

Reusable lemma: any pole-canceled boundary approximation admits the explicit Hardy representation(W2); an off-line zero then supplies the uniform coefficient-independent witness(W5). Repeated powers of1/s weaken the quantitative witness but do not change the zero-free conclusion for any fixed q≥1.

Concrete next step: include both optimized and prescribed-family nodes in the knowledge graph, with separate limit quantifiers and evidence. An archive must not add an RH→prescribed-convergence edge merely because an RH↔optimized-infimum edge exists.

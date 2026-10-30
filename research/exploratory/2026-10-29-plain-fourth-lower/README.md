# A lower bound for the unmarked plain fourth moment

**Status:** Proposed proof using elementary Eisenstein-lattice Poisson summation and prime ideal counting; independent review requested. It disproves an all-row moment replacement discussed in [the universal-selector note](../2026-10-29-universal-sixth-selector/README.md). It does **not** disprove a moment restricted to detector-zero witness fibers or the physical prime-only selected norm, and it does not prove a zero-free region. No priority claim is made.

Let `O=Z[ω]`, fix a finite set S of prime ideals containing those above 6, and let χ_n(u) be the zero-extended sextic residue character in the source convention, with n supported away from S. Let W be a fixed nonnegative smooth compactly supported function on `(0,∞)` that is not zero, and put

    S_L(u)=L^(−1/2) Σ_{n good} W(Nn/L) χ_n(u).

Fix `0<m<5/12`, let `L=U^m`, and sum over sixth-power-free nonzero element rows u of norm at most a fixed constant times U, additionally coprime to S. Then

    Σ_u |S_L(u)|⁴ ≫_{m,S,W} U/(log U)².                 (1)

Every ideal n is represented once in the inner sum using the source's fixed good generator convention. Row units are retained as distinct element rows; an analogous single ray/unit class requires an additional convention check and is not asserted here. The source's fixed background twist is chosen trivial and the profile has height zero. This specialization is permitted whenever an alleged all-row estimate is claimed uniformly for all such profiles and twists.

In particular, if a broad-slot selected moment estimate of the shape

    Σ_selected |S_L(u)|⁴ ≪ U^{max(2m,1−s+2ms)+ε}          (2)

were claimed uniformly on all selected row sets, then the [universal sixth-power selector](../2026-10-29-universal-sixth-selector/README.md) selects every row for any fixed `0<s<1/6`. Since `m<1/2`, the exponent in (2) is `1−s(1−2m)+ε<1` for small enough ε, contradicting (1). At the hypothetical return bottleneck, the critical plain length is `m=ℓ/2≈0.36639836<5/12`; the proposed power is approximately `U^0.99014870`, while the nonprincipal error in the lower-bound proof is `O(U^0.89946339+ε)`. This excludes the all-row version of the proposed plain-square replacement at that length. It does not exclude an estimate only for rows with an actual detector witness or zero-location condition.

## A uniform fixed-field character-sum bound

For any nonprincipal finite multiplicative character χ on `O` of original modulus q, with its natural zero extension, and any V>0,

    |Σ_{z∈O} χ(z) W₀(Nz/V)|
       ≪_{S,W₀,ε} (Nq)^(1/2+ε),                        (3)

for each fixed smooth compactly supported radial W₀ on `(0,∞)`. This bound is uniform in the modulus and V. It is a smooth sum over elements of the fixed planar lattice O, not a sharp ideal-norm Pólya–Vinogradov estimate; no such sharp estimate is used. To see it, induce χ from its primitive finite character of conductor f dividing q, and impose any extra zero masks at primes dividing q/f by inclusion–exclusion. The resulting divisor sum costs `(Nq)^ε` and does not increase the primitive conductor. Since O is a PID, choose a generator of f; the dual lattice for the quotient O/f is a rotated dilation of the fixed Eisenstein dual lattice. Poisson summation expresses the sum as `V/Nf` times complete additive Gauss sums and rapidly decaying Fourier transforms at scale `sqrt(V/Nf)`. The zero frequency vanishes for a nonprincipal character, and each primitive complete Gauss sum has modulus at most `(Nf)^(1/2)`. The sum of nonzero Fourier weights is `O(min(Nf/V,(Nf/V)^A))` for any fixed A>1 after increasing its implied constant. Multiplication yields `O((Nf)^(1/2))` uniformly for both `V≤Nf` and `V≥Nf`. The fixed S-row coprimality mask is incorporated by another fixed inclusion–exclusion. These are the standard finite-ring Gauss identity and Poisson summation; the argument is stated here to make the conductor and V uniformity explicit.

## Second-moment expansion

Choose W₀ nonnegative smooth supported in `[1,2]`, nonzero and bounded above by one. Let R_U be the S-good sixth-power-free element rows weighted by `W₀(Nu/U)`. Expanding gives

    Σ_u W₀(Nu/U) 1_sixfree(u) 1_(u,S)=1 |S_L(u)|²
      = L^(−1) Σ_{n₁,n₂ good} W(Nn₁/L)W(Nn₂/L) C(n₁,n₂),
    C(n₁,n₂)=Σ_u W₀(Nu/U)1_sixfree(u)1_(u,S)=1
                         χ_{n₁}(u) overline(χ_{n₂}(u)).  (4)

The row function in C is an ordinary finite Dirichlet character modulo a fixed bad modulus times `lcm(n₁,n₂)`, with the original zero masks. In particular, if it is principal, it is exactly one on coprime elements and zero otherwise. Because W is nonnegative and the background twist is trivial, **every principal-character term in (4) is a nonnegative real number**, even when the two indices differ. This is an exact statement about the ratio character; it does not discard a sextic reciprocity phase.

For the diagonal choose good prime ideals p with `W(Np/L)≥c>0`, which occur with number `≫L/log L` by the prime ideal theorem. For such p, the row factor is `1_(u,p)=1`. Standard lattice counting and sixth-power Möbius inversion give, uniformly in p,

    Σ_u W₀(Nu/U)1_sixfree(u)1_(u,S)=1 1_(u,p)=1 ≫ U.     (5)

For example, expand `1_sixfree(u)=Σ_{d^6|(u)} μ(d)`; lattice counting gives the positive Euler-product density, while the total boundary error is `O(U^(1/2))` because `Σ_d (Nd)^(−3)<∞`. The extra single prime mask changes the positive density by a uniformly bounded factor. Thus the diagonal terms alone contribute `≫U/log L` to (4).

For every nonprincipal ratio in (4), apply the same sixth-power inversion. If d^6 divides (u), write `u=α_d^6 v`, with a fixed generator α_d of d; the character factor at α_d^6 is a unit phase or zero. There are O(U^(1/6)) possible d, and (3), including the fixed S-mask, bounds the v-sum by `O_ε((Nn₁ Nn₂)^(1/2+ε))`. Since `Nn_i≪L`, there are O(L²) pairs, and the outer normalization is L^(−1), the combined absolute contribution of **all** nonprincipal pairs is

    O_ε(U^(1/6+ε) L²) = o(U/log L)                       (6)

when m<5/12 and ε is sufficiently small. Therefore the weighted second moment is `≫U/log U`. There are O(U) possible element rows in the fixed annulus. Weighted Cauchy–Schwarz now gives (1). □

The conclusion uses only this single trivial-twist, nonnegative-profile presentation. A detector-specific bound might avoid it by restricting rows using zero/witness conditions; the proof does not claim any of these rows possess such zeros. The all-row implication also requires the actual broad sixth-power slot support, which is absent from a physical prime-only slot dictionary.

**Independent review:** Three researchers checked the primitive/imprimitive character sums, principal-ratio positivity, sixth-power Möbius truncation, prime diagonal, fourth-moment Cauchy step, and the restriction to all rows with trivial twist and nonnegative profiles. The proof uses standard finite-ring Gauss and lattice Poisson identities as stated.

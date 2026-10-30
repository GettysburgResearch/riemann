# De Faveri's cubic symbols, ray sectors, and the full inverse

**Status:** Source matching and targeted literature search, not independent verification of the cited large-sieve theorem or the companion mean-square calculation. The source is Alexandre de Faveri, [*Optimal large sieve for fixed order characters*](https://arxiv.org/abs/2610.04045v1), version 1, §§2.2–2.5 and Proposition 8.1. In particular, this note corrects an earlier overbroad warning: the symbol with a primary index in the **numerator** does define the source Hecke character for every good index, not only indices in the principal ray sector.

## Exact source convention

De Faveri §2.3.4 constructs χ_a(b) for coprime good ideals a,b by a choice of representatives of the finite group R_c and n-th power residue symbols. It extends by zero when a,b share a prime or b meets the fixed bad modulus. By §2.5.1 this is a Hecke character in **b**, of order dividing n and trivial infinity type, with conductor c_a a*, where c_a divides fixed c and a* is the product of good primes whose exponents in a are not divisible by n. Choice of representatives matters; the family need not be described by a single naively chosen element over an arbitrary number field.

In the special normalization of Example 2.2, take K=Q(ω), n=3, S consisting of the prime above 3, c=(9), and choose primary generators a,b≡1 mod 3. The chosen representatives yield precisely

    χ_(a)(b) = (a/b)_3.

Thus **(g/q)_3**, with g primary and fixed, is the source Hecke character as a function of the ideal q even when g is not 1 mod 9. It is the opposite raw symbol **(q/g)_3**, viewed as a character of the ideal q using only primary generators, that may fail to descend to ideals without a fixed ray correction. For example π=4+3ω has Nπ=13 and π≡1 mod 3, but (ω/π)_3=ω≠1. This shows why the direction of the symbol is essential. Enlarging S in applications may be handled by restricting rows and columns of this S={3} model and deleting the corresponding Euler factors; a new FHL choice for larger S should not be silently identified with Example 2.2.

For a≠1 squarefree and good, the conductor contains a, so χ_a is nontrivial; the primitive character defines a cyclic cubic extension by class field theory. The full product ζ_K L(s,χ_a)L(s,barχ_a) is its Dedekind zeta function. At finitely many S primes, the S-deleted identity deletes factors at all extension primes above S. The original good-prime zero extension in χ_a(q) correctly encodes ramification at q|a.

## Reciprocity and the principal ray sector

Source (2.5) states, for coprime good ideals,

    χ_g(q) = α([g],[q]) χ_q(g),

where both classes lie in R_c and α depends only on those classes. Multiplicativity makes α a bicharacter; taking g=1 shows α(1,[q])=1. The original zero extensions on the two sides agree when gcd(g,q)≠1. For the source's Example 2.2, R_(9)=H_(9) and [g]=1 exactly when the ideal g has a generator g≡1 mod 9. In this sector,

    (g/q)_3 = χ_g(q) = χ_q(g) = (q/g)_3

with every denominator interpreted using the source's chosen primary generator. The congruence makes (q/g)_3 invariant under units q, so the last symbol really is a Hecke character of the q-ideal. Conversely, for a general fixed sector C=[g], α(C,[q]) is a fixed finite ray-class phase in q, which is harmless in any estimate allowing arbitrary squarefree-column coefficients. The ray restriction is useful for a particularly transparent identification; it is not needed to define χ_g.

## Precise use of Proposition 8.1

For squarefree q in a norm dyad Q and an arbitrary complex coefficient vector λ_q, Proposition 8.1 estimates

    Σ_(a∼A) Σ_(b∼B) |Σ_(q∼Q)^* λ_q χ_q(a b²)|²
      ≪ (ABQ)^ε [AB+M^(2/3)N^(1/3)Q+M^(1/3)N^(2/3)Q^(2/3)] Σ|λ_q|²,

where M=min(A,B), N=max(A,B), and * denotes squarefree q. Its outer sum is over all good ideals a,b. Taking A∼X, B=1 includes b=O and yields a bound for the outer g-sum of `|Σ_q λ_q χ_q(g)|²`. Restricting g to the principal ray sector only reduces this nonnegative sum; here χ_q(g)=χ_g(q). For any other single fixed sector C, replace λ_q by α(C,[q])λ_q and then similarly drop the sector restriction. These are direct applications for a **single sum over squarefree q**. The coefficients must be independent of g after fixing C; fixed profiles and fixed norm twists can be absorbed into λ, subject to the precise uniformity one needs.

This does **not** directly establish a moment estimate for the entire reciprocal extension zeta. Expanding the latter introduces χ_g(a)barχ_g(b)=χ_g(ab²) and a further common Möbius factor. Even when a,b are squarefree, ab² need not be squarefree; grouping by ab² does not satisfy Prop. 8.1's squarefree-column hypothesis. Nor may one discard the base factor or the nonprincipal cross-terms from the complete inverse without controlling their cancellation. Any such further application needs an explicit decomposition or a separate sieve inequality.

## Priority and logical scope

The [related literature benchmark](2026-10-29-full-inverse-prior-art.md) records Hu–Kaneko–Martin–Schildkraut's number-field Mertens Ω results, Gao–Zhao's GRH-conditional negative first moment for individual cubic Hecke L-functions over prime rows, and squarefree cubic mollified moments of David–de Faveri–Dunn–Stucky. Additional targeted searches for averaged inverse Dedekind zeta, family Möbius moments, and cubic extension Mertens functions did not identify a theorem matching the principal-ray squarefree-row full-inverse factor H_S/ζ_K together with a single fixed short test. Search terminology and scope are limited; this is not a priority claim.

The [full-inverse note](2026-10-29-cubic-full-inverse-mean/README.md) claims, conditional on its explicitly stated arithmetic average and a nonvanishing Mellin test W, the implication

    full-inverse second moment ≪_ε X^(1+ε) for all ε>0,
    one fixed 0<r<1/2 and all sufficiently large X
      ⇒ RH for ζ_K.

The family weights are fixed nonnegative V with positive mass, g is squarefree in the principal ray sector, D=X^r, and the S-deleted original masks are retained. This is a **one-way implication**, not an equivalence: RH for ζ_K by itself has not been shown to imply the full family second moment. The hypotheses and conclusion must remain conditional on the companion arithmetic estimates and the no-cancellation Mellin argument; neither this review nor the cited sources prove that moment bound or a new zero-free region.

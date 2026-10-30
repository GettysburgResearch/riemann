# Source-qualified density for a monomial GL₄ family

**Status.** This is a conditional consequence of [the natural-label density theorem](../reports/direct-nfree-density.md) and its explicitly listed FHL, de Faveri large-sieve and detector inputs. It is a density estimate for a specified family, not an individual zero-free region. The source proof and the imported analytic inputs have not been independently verified here. The prior comparison below is targeted, not exhaustive.

Let `K=Q(ζ₅)`, so `Gal(K/Q)≅C₄` and `|D_K|=125`. Fix the good-prime set and fifth-order FHL family `χ_u` used by the natural-label theorem, with ν=1. For every rational prime p splitting completely in K and outside the finite bad set, choose one of the four primes `𝔭|p` and set

    ρ_p=Ind_(W_K)^(W_Q) χ_𝔭,       π_p=AI_(K/Q)(χ_𝔭).

Here χ means its primitive finite-order inducing Hecke character. The FHL good-prime local data imply that χ_𝔭 has exact order 5, is tamely ramified with conductor exponent 1 at 𝔭, and is unramified at each other good prime; its bad conductor is uniformly bounded in the fixed source family. Its infinity type is trivial. The four Galois conjugates have different ramification primes, hence form a full orbit. By Mackey's criterion ρ_p is an irreducible finite-image degree-4 monomial Artin representation. Cyclic automorphic induction gives a cuspidal representation of `GL₄(A_Q)` with the corresponding local parameters. See [Henniart, *Induction automorphe globale pour les corps de nombres*](https://www.numdam.org/item/BSMF_2012__140_1_1_0/) for cyclic automorphic induction and its fibers; compatibility with Artin induction, including the local ramified factors, is also used here.

For the primitive inducing character, Artin formalism and its conductor formula give

    L_Q(s,π_p)=L_Q(s,ρ_p)=L_K(s,χ_𝔭),
    q(π_p)=q(ρ_p)=125·N_K/Q(f(χ_𝔭)) ≍_K p.                 (1)

The bad conductor can vary inside a fixed finite set, so `(1)` does not assert equality `q(π_p)=125p`. All Euler factors are those of the primitive representation, including ramified factors.

Choose one 𝔭 for each split p and let `F(X)` consist of the distinct π_p with `q(π_p)≤X`. The prime number theorem for split rational primes and (1) give

    #F(X) ≫ X/log X.                                           (2)

Indeed, sufficiently small `p≤cX` have conductor at most X. Representations from different rational primes are distinct: their restrictions to `W_K` have different good ramification supports (equivalently, their conductor ramification differs at the corresponding large rational prime). Standard automorphic induction identifies Galois-conjugate inducing characters; choosing one 𝔭 per p avoids relying on how many of those conjugates the FHL presentation contains.

For a fixed σ with `7/10<σ<1`, define `δ=2σ−1`, `h=1−δ`, and

    R₅(σ)=2/5 + 6(4/5−δ)/(5(3−δ)−7)  if δ≤4/5,
            10h/(4+5h)                   if δ≥4/5.              (3)

Then, under the natural-label source theorem, for each ε>0 a τ>0 exists such that

    #{π∈F(X): L(s,π)=0 for some Re s≥σ, |Im s|≤X^τ}
       ≪_ε X^(R₅(σ)+ε).                                       (4)

At `σ=4/5`, `R₅=16/25=0.64`. At `θ=4369347/5000000=0.8738694`, `R₅=5045224/10653265≈0.473584765`. The proof is a restriction of the source sum over all good fifth-free `Nu≤X/125` labels to these prime labels, using equality of L-functions. To absorb fixed conductor scaling in the height window, choose a slightly smaller τ than the source allows. The source count includes zero multiplicities, so it bounds the number of representations with at least one zero. Together with (2), (4) implies a power-saving exceptional fraction for sufficiently small ε. No uniform infinite-height conclusion follows.

## Named prior comparisons

[de Faveri, Corollary 1.5](https://arxiv.org/html/2610.04045v1), directly treats the untwisted fifth-free natural-index family and hence this prime subset. With `[K:Q]=4`, its printed bound includes `T^(1+4(1−σ)/(3−2σ)+ε)` and fixed-height label exponents `23/35≈0.657143` at `σ=4/5` and `4795079555137/9914648967955≈0.483635837` at θ. These exceed the respective numbers in (4); the strict comparisons persist for sufficiently small height powers. As in (4), transfer to GL₄ uses (1). This is a comparison to that named recent source, not a claim of priority among all monomial automorphic theorems.

[Blomer–Goldmakher–Louvel, Corollary 1.6](https://arxiv.org/html/1112.1650), is directly a squarefree ideal-label Hecke result, and its corresponding exponents are `8/11≈0.727273` at `4/5` and `≈0.542094803` at θ, with its stated height factor and FHL convention. [Khale–O’Kuhn–Panidapu–Sun–Zhang, Lemma 3.3](https://arxiv.org/abs/2008.09677v3), bounds the much larger finite-order conductor family over fixed Galois K; the fixed-height exponent is `1` at `4/5` and `≈0.577343` at θ. Apply its stated T-dependence before comparing polynomial heights. These are Hecke-family estimates transported to the induced representations; they do not establish a stronger direct GL₄ theorem.

[Liu](https://arxiv.org/abs/2610.26835v1) claims finite-order Hecke individual zero-freeness for `Re s>0.874886647…`; [Hu](https://hexagonmath.org/2610.00216v1) claims the unitary scope for `Re s>7/8`. Neither claimed boundary reaches θ; these recent claims have not been independently verified here. If valid, they supersede a positive-exception estimate strictly inside their respective all-height regions. Other specialized automorphic or prime-label zero-density results could be stronger and have not been exhaustively ruled out.

## Every fixed prime order p≥5

Fix a prime `p≥5` once and for all; constants, the allowed height exponent, the finite bad set and all source inputs may depend on p. Take `K=Q(ζ_p)` and the p-th order FHL family. For each rational prime `ℓ≠p` splitting completely in K and outside the fixed bad set, choose one `𝔭|ℓ` and define

    ρ_ℓ=Ind_(W_K)^(W_Q) χ_𝔭,
    π_ℓ=AI_(K/Q)(χ_𝔭) on GL_(p−1)(A_Q).

The good conductor support of `χ_𝔭` is exactly 𝔭. The p−1 conjugates have different supports, so they have a full `Gal(K/Q)` orbit; Mackey and cyclic automorphic induction give an irreducible Artin representation and a cuspidal automorphic representation. The fixed bad conductor is bounded, and the all-place conductor/L compatibility gives

    q(π_ℓ)=|D_K| N(f(χ_𝔭)) ≍_p ℓ,
    |D_K|=p^(p−2),        L_Q(s,π_ℓ)=L_K(s,χ_𝔭).            (5)

As above, different ℓ give different representations and the split-prime theorem gives `≫_p X/log X` of them of conductor at most X. Restricting the same conditional natural-index density theorem to these labels gives, for every fixed σ in `1/2+1/p<σ<1`, and every ε>0, a sufficiently small τ>0 and at most `O_(p,σ,ε)(X^(R_p(σ)+ε))` exceptions up to height `X^τ`, where R_p is the piecewise formula in the cited theorem. For the two requested σ both are in its middle branch, since p≥5:

    R_p(4/5) = (6p²−9p−25)/(p(12p−35)),
    R_p(θ) = (1891959p²−1914571p−12500000)
             /[7p(804379p−2500000)],  θ=4369347/5000000.      (6)

For example, p=5 gives `16/25` and `5045224/10653265`; p=7 gives `206/343≈0.600583` and `22267998/51133999≈0.435483`. Both exponents are below 1, so the bad proportion among this specified prime family tends to zero with a fixed power saving. The displayed limits as p→∞ are 1/2 and `1891959/5630653≈0.3360`, but they compare separate **fixed-p** theorems: no uniform estimate as p grows with X is asserted.

For an automorphic-source comparison, [Chen An, Theorem 1.1](https://arxiv.org/html/2004.14410v2), is stated for a family of cuspidal GL_n representations with bounded analytic conductor and cardinality, assuming Ramanujan and bounded archimedean parameters. Here `n=p−1`, finite image supplies the needed unramified Ramanujan bound, and the infinity type is fixed. Taking `A=1`, `d=1` and conductor parameter `q≍X` gives its displayed fixed-height exponent `(4p−1/2)(1−σ)` and height exponent `((p−1)/2+3)(1−σ)`; the representation count `≪X` follows from construction. At p=5 and σ=4/5 this gives 3.9, so this particular general automorphic bound does not beat even trivial family counting there. This comparison uses only An's Theorem 1.1; it does not rely on the separately problematic field-count asymptotic in the arXiv version's Theorem 1.2. General automorphic and more specialized monomial results may have different hypotheses or better exponents, and this search does not exclude them.

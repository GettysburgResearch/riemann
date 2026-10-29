# The full cubic inverse retains the base pole on average

**Status:** Proposed elementary conditional implication; independent review requested. This is not a proof that a full-inverse moment bound holds and not a zero-free theorem. It uses standard cubic reciprocity and finite-order Hecke analytic estimates in the Eisenstein field, with the original zero masks. No priority claim is made.

Let K=Q(√−3), O=Z[ω], and fix a finite set S containing primes above 6 and all fixed reciprocity moduli. Restrict g to good squarefree ideals in the principal ray class modulo (9); equivalently, each has a generator g≡1 mod 9. On good ideals q, define χ_g(q)=(g/q)₃ using the standard cubic residue symbol and keep its original zero extension. This is a trivial-infinity cubic Hecke character for every good primary g; we impose the principal mod-9 sector to make its fixed ray normalization and reciprocity bookkeeping transparent. The raw symbol in the opposite orientation is a different object and must not be identified without its finite-ray correction. Write

    1/[ζ_(K,S)(s)L_S(s,χ_g)L_S(s,barχ_g)]
        = Σ_{j good} c_g(j)/(Nj)^s,                   Re s>1,
    M_g(D)=D^(−1/2) Σ_{j good} c_g(j) W(Nj/D),

where W is a fixed smooth annular function. The product is the S-deleted ζ-function of the cyclic cubic extension for nontrivial χ_g; the finitely many trivial presentations can be removed at no relevant cost. Fix a nonnegative smooth annular V with `∫V(x)dx>0`, and average over all such good squarefree g in this fixed ray sector with weights V(Ng/X). Denote this normalized average by E_X.

Define the fixed multiplicative factor

    h(h₀)=∏_{p|h₀} Np/(Np+1),
    H_S(s)=∏_{p∉S} [1+(Np/(Np+1)) (Np)^(−2s)].

Then H_S converges absolutely and is nonzero for Re s>1/2. For every ε>0 and D,X≥2,

    E_X M_g(D)
      = D^(−1/2) Σ_{d,h good} μ_K(d) μ_K(h)² h(h)
            W(N(d h²)/D)
        + O_{S,V,W,ε}(X^(−1/2+ε) D^(1+ε)).          (1)

The main term has Mellin transform

    Ŵ(s) ζ_(K,S)(s)^(−1) H_S(s).                       (2)

This is the **full inverse**, not just the isolated μ_K summand. The H_S factor is nonzero throughout Re s>1/2, so it cannot remove a base ζ_K zero there.

Consequently, suppose ζ_K has a zero `ρ=β+iγ` with β>1/2. Choose once a nonnegative annular W with Ŵ(ρ)≠0. For any fixed `0<r<1/2` and `0<η<β−1/2`, there are arbitrarily large X such that, with D=X^r,

    Σ_{g squarefree good} V(Ng/X)|M_g(D)|²
       ≫ X^{1+r(2β−1−2η)}.                            (3)

Thus any uniform full-inverse moment bound `≪X^(1+ε)` for all ε>0, even only at one fixed inverse-length exponent `0<r<1/2` and all such fixed W, would itself imply the Riemann hypothesis for ζ_K. In particular, an argument proving such a bound without excluding the putative base zeros would be genuinely decisive; applying a general character-family bound to separate nonprincipal terms cannot make the common pole disappear. This is a conditional no-go theorem for the *proposed norm*, not a proof that RH is false, and not a full ζ_L zero-density estimate.

## Proof of the average

By Artin factorization and the primitive convention, for good indices

    c_g(j)=Σ_{d a b=j} μ(d)μ(a)μ(b)χ_g(a)barχ_g(b).   (4)

Take a,b squarefree (otherwise μ vanishes), set h=(a,b), a=h a₀, b=h b₀; h,a₀,b₀ are pairwise coprime. Then

    χ_g(a)barχ_g(b)=1_(g,h)=1 χ_g(a₀ b₀²).            (5)

This includes every original noncoprime zero. The term a₀=b₀=1 has row weight `1_(g,h)=1`; all other terms have a nontrivial cubic residue character of the element generator g. The product index `a₀b₀²` has a good prime with exponent 1 or 2, so even after multiplying by a fixed S-ray character its primitive conductor has a nontrivial good-prime factor; its conductor norm is `≪N(a₀b₀)≤C D`. The condition g≡1 mod 9 fixes a unique generator per ideal; its residue-class indicator is handled by finitely many characters modulo 9.

The following two standard fixed-field estimates, detailed below, hold uniformly for good h,q with `N(hq)≤D^O(1)`:

    Σ_{g good, squarefree, [g]=1 mod 9, (g,h)=1} V(Ng/X)
       = C_{S,V} X h(h) + O_ε(X^(1/2+ε)(Nh)^ε);     (6)
    Σ_{g good, squarefree, [g]=1 mod 9, (g,h)=1} V(Ng/X)χ_q(g)
       ≪_ε X^(1/2+ε) (N rad(q))^(1/2+ε)(Nh)^ε     (7)

for each nonprincipal cubic residue character in the g-variable, with the stated modulo-9 sector. The main density C_{S,V}>0 is the same for every h. The finite S-part of the character, common ray sectors, and all original zero masks are included in the constants or the displayed h-loss.

For (6), project to the principal ray class by the fixed finite ray-character orthogonality relation. The principal term has Dirichlet series

    ζ_(K,S)(s)/ζ_(K,S)(2s) · ∏_{p|h}(1+Np^(−s))^(−1).

Each nonprincipal fixed ray character ξ contributes `L_S(s,ξ)/L_S(2s,ξ²)` times the analogous finite h-factors and has no pole at s=1. Mellin inversion and a shift to `Re s=1/2+ε` yield the principal pole with factor h(h), divided by the fixed ray-class number; every reciprocal on the shifted line has an absolutely convergent Euler product. The h-local factor is `≪_ε (Nh)^ε` there. For (7), expand squarefreeness by `Σ_{k²|g}μ(k)` and the h-mask by divisor inclusion–exclusion. Write g=α_k² v using a chosen generator of the good ideal k. The condition g≡1 mod 9 becomes one invertible residue class for v mod 9, expanded into finitely many multiplicative characters of `(O/9)×`. The cubic symbol `(g/q)₃` is a finite residue character in the element g modulo rad(q), retaining its zero mask; after multiplication by a modulo-9 character it is still nonprincipal at every good prime dividing rad(q). Its primitive conductor norm is `≪N rad(q)`. A smoothed sum over Eisenstein elements for a nonprincipal primitive residue character of conductor Q is `≪_ε Q^(1/2+ε)` uniformly in its scale, by two-dimensional Poisson summation and the finite Gauss identity; imprimitive masks are split by divisor inclusion–exclusion. See [the detailed lattice argument](../2026-10-29-plain-fourth-lower/README.md). There are `O(X^(1/2))` k ideals, and h-mask divisors cost `(Nh)^ε`. This proves (7), including the row masks.

Applying (6)–(7) to (4), the unnormalized denominator is `C_{S,V}X+O(X^(1/2+ε))`. The diagonal a₀=b₀=1 gives the displayed main term in (1); the denominator correction costs at most `X^(−1/2+ε)D^(1/2+ε)`, already covered by the displayed error. For the off-diagonal, each character sum is `≪X^(1/2+ε)D^(1/2+ε)`, and the number of triples with `N(dab)≪D` is `≪D^(1+ε)` by the ideal divisor bound. Dividing by the family mass ≍X and the `D^(1/2)` normalization gives `O(X^(−1/2+ε)D^(1+ε))`. This proves (1).

## From a base zero to the lower bound

The Euler product in (2) is obtained by summing independently over d and squarefree h. Every factor `1+c_p Np^(−2s)` has `|c_p Np^(−2s)|<1` for Re s>1/2, and the product converges absolutely there, hence H_S is holomorphic and nonzero. If ζ_K(ρ)=0 and Ŵ(ρ)≠0, the Mellin transform of the unnormalized main sum has a pole at ρ. As in [the common-factor note](../2026-10-29-common-factor-lifting/README.md), it cannot be O(D^(β−η)), so the main term in (1) has size at least D^(β−1/2−η) along an unbounded sequence.

For any fixed r<1/2, choose ε small enough that the error in (1), with X=D^(1/r), tends to zero. Set X along this sequence. Since the main term grows by a positive fixed power of D, the average has the same lower order. Weighted Cauchy–Schwarz, `Σ_g V(Ng/X)≍X`, yields (3). □

The desired full-ζ lifting route therefore cannot obtain an `X^(1+ε)` full inverse mean-square estimate from the stated arithmetic inputs alone **unless it proves the base zero-free claim as part of that argument**. Stronger but genuinely structured estimates or a different zero-detection strategy may still be possible; no restriction on their existence is asserted.

**Independent review:** Two researchers checked the finite-ray nonprincipal character reduction, squarefree and h-mask averages, normalized error, H_S nonvanishing and Mellin/Jensen implication. The review remains conditional on the stated fixed-field reciprocity and uniform smooth Hecke estimates; it does not assert the desired full-inverse upper bound.

## One universal nonvanishing Mellin test

The final implication does not require a different W for each putative base zero. Replace the annular test by the fixed log-Gaussian

    W_*(x)=exp(−(log x)²),  x>0.

Its Mellin transform is the nowhere-zero entire function

    Ŵ_*(s)=√π exp(s²/4).                                (8)

For fixed `0<r<1/2` and D=X^r, the mean identity (1), with the same stated `X^(−1/2+ε)D^(1+ε)` error after renaming ε, remains valid for W_*. Indeed, truncate the j-sum to `D^(1−κ)≤Nj≤D^(1+κ)` for an arbitrarily small fixed κ>0. Outside that range `W_*(Nj/D)` is superpolynomially small in D. Uniformly in g, the inverse coefficients satisfy `|c_g(j)|≤d₃(j)` by the triple convolution. For the upper tail, combine the Gaussian decay with an arbitrary extra power of Nj/D and the convergence of `Σ_j d₃(j)/(Nj)^2`; for the lower tail, use ideal counting and the divisor bound. Both tails, including the corresponding diagonal main sum, are `O(D^(−B))` for every prescribed fixed B. Since D=X^r with fixed r>0, they are also `O(X^(−A))` for any prescribed fixed A after choosing B sufficiently large. The truncated range lies below `D^(1+κ)`, so repeating the character-sum and divisor argument in (1) only changes the D exponent by O(κ), absorbed in ε.

Mellin inversion applies to W_* because (8) decays as a Gaussian on every fixed vertical line. At **every** zero ρ of ζ_K with Re ρ>1/2, Ŵ_*(ρ) and H_S(ρ) are nonzero. The pole/Ω argument therefore yields (3) with this same W_* simultaneously as a theorem for each fixed putative zero. Consequently a single-test family bound

    Σ_g V(Ng/X)|M_g(X^r;W_*)|² ≪_ε X^(1+ε)

for one fixed `0<r<1/2` and every ε>0 would imply RH for ζ_K; its test function need not be selected after the zero. This remains a logical implication, not a proof of that moment bound or RH. The log-Gaussian truncation and the uniform arithmetic estimates require independent audit.

## A single compact annular test for all zeros

The preceding implication can use one **fixed nonnegative C∞ compact-annular** W with no truncation. Let U_j, j≥1, be independent uniform random variables on `[-2^(−j),2^(−j)]`, and let T=Σ_j U_j. The series converges almost surely and |T|≤1. Its characteristic function is

    φ(ξ)=∏_{j≥1} sin(2^(−j)ξ)/(2^(−j)ξ).                 (9)

For each fixed N, the first N factors give `|φ(ξ)|≪_N (1+|ξ|)^(−N)`; every remaining factor has modulus at most one. Fourier inversion therefore gives a C∞ density w for T. Its compact support lies in [−1,1], w≥0, and its integral is one. Set

    W(x)=w(log x),    supp W⊆[e^(−1),e].

The Mellin transform is the moment-generating function

    Ŵ(s)=∫w(t)e^(s t)dt
         =∏_{j≥1} sinh(2^(−j)s)/(2^(−j)s).              (10)

The product converges uniformly on compact subsets of C, because its factors are `1+O_K(4^(−j))`. It has no zeros for `Re s≠0`: each factor's only zeros lie on the imaginary axis, and the convergent product cannot acquire an additional zero where every factor is nonzero. Thus W is one fixed nonnegative smooth annular profile whose Mellin transform is nonzero at every zero of ζ_K in Re s>1/2.

Use this W directly in the already-proved annular average (1). For any fixed `0<r<1/2`, the full-inverse moment bound

    Σ_g V(Ng/X)|M_g(X^r;W)|² ≪_ε X^(1+ε)

for every ε>0 would imply RH for ζ_K by the same pole/Ω and Jensen argument. This single test is fixed **before** any hypothetical zero is chosen. The construction and the consequence need independent review; they do not establish the moment bound or RH.

**Independent test-function review:** A second researcher checked rapid decay of the sinc product, existence and smooth compact support of the density, local uniform convergence and zero-freeness of the Mellin product, and its use in the conditional Ω/Jensen implication.

**Independent compact-profile review:** The construction, Euler factor, pole/Ω argument, explicit error exponent, and fixed-test quantifiers were checked in [compact-annular-review.md](compact-annular-review.md). This remains conditional on the stated arithmetic inputs and assumes the moment bound rather than proving it.

## A conditional converse and an exact moment criterion

Fix `1/2≤θ<1`. Suppose ζ_K is zero-free in `Re s>θ`. For every η>0, standard fixed-field Borel–Carathéodory and vertical-strip bounds give polynomial growth of `1/ζ_(K,S)(s)` on `Re s≥θ+η`; the pole of ζ_K at 1 gives a **zero** of its reciprocal, not a pole. Mellin inversion then gives, uniformly for every fixed smooth annular W and Y>0,

    Σ_{d good} μ(d) W(Nd/Y) ≪_{K,S,W,η} Y^(θ+η).       (11)

Using the exact triple convolution (4), group `a=h a₀`, `b=h b₀` as before. For each index triple i=(h,a₀,b₀), the normalized coefficient after summing d satisfies

    |c_i| ≪ D^(θ−1/2+η) (Nh)^(−2θ−2η)
                    (N(a₀b₀))^(−θ−η),                   (12)

and its row factor is `1_(g,h)=1 χ_g(a₀b₀²)`. Here h,a₀,b₀ are squarefree and pairwise coprime. Retain the fixed modulo-9 sector and every zero mask. Since W is annular, only `N(h²a₀b₀)≪D` occur.

Expand the weighted row second moment. The ratio character attached to two indices i,i' is principal on the modulo-9 sector exactly when their good cubic exponent vectors agree, equivalently `a₀=a₀'` and `b₀=b₀'`: otherwise a good prime ramifies and fixed modulo-9 factors cannot cancel it. The principal ratio terms are bounded absolutely using O(X) rows and (12). Because `2θ+2η>1`, the sums of `(Nh)^(−2θ−2η)` and `(N(a₀b₀))^(−2θ−2η)` converge. Thus their total is

    ≪ X D^(2θ−1+2η).                                    (13)

For every nonprincipal ratio, the same squarefree-sector argument as (7), now with conductor norm `≪D²` and the h,h' zero masks, gives a weighted row sum `≪X^(1/2+ε) D^(1+ε)`. The total absolute mass of the normalized coefficients is `≪D^(1/2+ε)`: before the d-summation there are only `≪D^(1+ε)` divisor triples and each has size `O(D^(−1/2))`. Hence all nonprincipal pairs together contribute

    ≪ X^(1/2+ε) D^(2+ε).                               (14)

Combining (13)–(14), choosing η and auxiliary losses sufficiently small, and taking D=X^r yields, whenever

    0<r<1/[2(3−2θ)],

    Σ_g V(Ng/X)|M_g(X^r;W)|²
       ≪_{K,S,V,W,r,θ,ε} X^(1+ε) X^{r(2θ−1)}.          (15)

For θ=1/2 this is `O(X^(1+ε))` for every fixed r<1/4. Conversely, the fixed compact-annular W from (10) has Ŵ nonzero throughout Re s>0; if (15) held for every ε>0 and ζ_K had any zero β>θ, the lower bound (3), with η and ε sufficiently small, would contradict it. Consequently, for every fixed `1/2≤θ<1` and `0<r<1/[2(3−2θ)]`, the following are equivalent, conditional only on the standard fixed-field reciprocity, finite-ring character-sum and Mellin inputs used here:

* ζ_K has no zeros in Re s>θ;
* the single fixed compact-annular full-inverse moment in (15) holds for every ε>0.

In particular RH for ζ_K is equivalent to the `O(X^(1+ε))` single-test full-inverse moment at any fixed r<1/4. This is an exact reformulation, not a proof of either side. The principal-sector restriction is a convenient fixed-ray normalization for this proof, not a claim that De Faveri’s χ_g fails to be a trivial-infinity Hecke character outside it. The elementary converse and fixed-sector bookkeeping require independent review.

For `3/4≤θ<1`, one can alternatively replace the elementary off-diagonal estimate by the **dual** of De Faveri's cubic rectangular sieve. On each dyadic `Na₀≈A,Nb₀≈B`, fix h and apply the source norm to its row-independent coefficient vector; the factor `1_(g,h)=1` lies outside the inner (a₀,b₀)-sum and can be dropped in the row L² norm. Minkowski then sums the resulting norms over h, at the convergent cost `Σ_h (Nh)^(−2θ−2η)`. A bound `AB+sqrt(AB)X` for X≥D follows from its `AB+M^(2/3)N^(1/3)X+M^(1/3)N^(2/3)X^(2/3)` bracket: the third term is at most `sqrt(AB)X` since `(N/M)^(1/6)≤D^(1/6)≤X^(1/3)`. The coefficient squared mass is `≪D^(2θ−1+ε)(AB)^(1−2θ)`; the product is `≪X D^(2θ−1+ε)(AB)^(3/2−2θ)`, and the last factor is ≤1 for θ≥3/4. This yields the same moment bound for every fixed r<1/2, but relies on the preprint sieve and the fixed-h Minkowski separation. It is not needed for the elementary equivalence above.

## Exact asymptotic growth exponent

Let `Θ_K=sup{Re ρ: ζ_K(ρ)=0, 0<Re ρ<1}`. For every fixed `0<r<1/4`, the preceding estimates give the following identity using the stated classical fixed-field reciprocity and character-sum inputs, without an additional zero-free assumption

    limsup_{X→∞} [log(X^(−1) Σ_g V(Ng/X)|M_g(X^r;W)|²)]/log X
       = r(2Θ_K−1),                                      (16)

where W is the single fixed compact-annular profile in (10), and log 0 is interpreted as −∞ if necessary. The assertion remains conditional on the standard fixed-field reciprocity and uniform character-sum inputs already stated; it is not a numerical value for Θ_K or an RH proof.

For the upper bound, if Θ_K<1 apply (15) with any `θ>max(Θ_K,1/2)` and let θ decrease to `max(Θ_K,1/2)`, with ε subsequently decreasing to zero. The condition `r<1/[2(3−2θ)]` holds for every θ≥1/2 because r<1/4. If Θ_K=1, the elementary divisor bound `|M_g(D)|≪D^(1/2+ε)` gives limsup at most r, which is the desired value.

For the lower bound when Θ_K>1/2, choose zeros with real parts β arbitrarily close to the supremum. The main-term pole/Ω argument and Jensen give limsup at least `r(2β−1−2η)` for every sufficiently small η>0. Taking β to Θ_K and η to zero proves the lower bound even if the supremum is not attained.

When Θ_K=1/2, a base zero exactly on the critical line need not be chosen. Write

    H_S(s)=ζ_(K,S)(2s) G_S(s),
    G_S(s)=∏_{p∉S} (1+c_p Np^(−2s))(1−Np^(−2s)),
    c_p=Np/(Np+1).

The product for G_S converges absolutely and is nonzero for Re s>1/4: its local factors differ from 1 by `O(Np^(−1−2 Re s)+Np^(−4 Re s))`, and neither factor vanishes for Re s>0. At s=1/2, ζ_(K,S)(2s) has a pole, while ζ_(K,S)(s) is finite; if the latter vanishes there, its reciprocal adds a pole rather than cancelling it. Ŵ(1/2)>0 and G_S(1/2)≠0. Hence the diagonal main-term Mellin transform has a pole at s=1/2 regardless of whether ζ_K(1/2) vanishes. Its normalized main sum is Ω(D^(−η)) for every η>0. For r<1/4 the averaging error `X^(−1/2+ε)D^(1+ε)` is smaller along the Ω sequence after choosing η,ε small, giving limsup ≥0. This completes (16), subject to the stated analytic inputs. □

**Independent converse and growth review:** Three researchers checked the fixed principal-ray correction, grouped principal/nonprincipal covariance, η and r ranges, the critical-line Euler-product pole and the limsup quantifiers. The written [growth-identity review](GROWTH-IDENTITY-REVIEW.md) records the scope. These checks use, and do not independently establish, the cited cubic reciprocity and uniform finite-ring character sums.

For the staged Dirichlet candidate θ=4369351/5000000, the factorization `ζ_K=ζ·L(s,χ_{−3})` would give the zero-free hypothesis for ζ_K, subject to the candidate's cache and conventional-L-function interpretation qualifications. The cubic-sieve converse would then yield, for each fixed `0<r<1/2`, the source-dependent full-inverse bound

    Σ_g V(Ng/X)|M_g(X^r;W)|²
      ≪_ε X^(1+ε) (X^r)^(1869351/2500000)
      = X^(1+0.7477404 r+ε).

This is a power saving over the trivial `X^{1+r+ε}`. It inherits both the assumed Dirichlet boundary and De Faveri's cubic sieve, and is not a claim of an independent new zero-free region.

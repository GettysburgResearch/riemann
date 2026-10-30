# An averaged quadratic-sieve substitute for the angular strip

**Status.** This is a proposed partial theta-tail estimate, conditional on the October 5 source identities, common-profile completed-theta mean and pointwise derivative estimates, and the source-to-quadratic-Hecke reciprocity matching below. It needs independent verification. It does **not** give an individual zero-free region or control the remaining physical signed core.

## The angular coefficient and prior scope

Let E=Q(ω), let S be the fixed source bad set, and choose the unique generator of every good ideal congruent to 1 modulo 3. Such a generator exists and is unique because the six global units map bijectively to `(O_E/3)×`. The source factor `α(c)=c/|c|` is multiplicative on these representatives and defines a unitary Hecke character of angular type +1 and conductor dividing (3); its conjugate cube has angular type −3. [October 5, §1 Step 5 and equations (intro-cube-weight)–(intro-cube-inversion)](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex) give the cube-inversion coefficient `μ(c) ᾱ(c)^3 ξ(c)^3 χ_c(b)^3`, with primary generators, a fixed ray character ξ and literal zero masks.

For fixed b, sextic reciprocity identifies `χ_c(b)^3` with the corresponding quadratic Hecke character in c, multiplied by a fixed finite-ray phase, on `(b,c)=1`; the latter zero is retained. The phase is a character of the fixed ray group: the quotient of the two symbol families is multiplicative in c, and every fixed ray class has representatives coprime to b. Finite Fourier expansion is an alternative if this is used only sectorwise. Thus each constituent is angular type −3, with finite conductor `≪_S Nrad(b)`; an additional mask at f stays as an Euler deletion. Exact matching of the physical χ to this FHL presentation remains a source input.

[Hu, hexagon:2610.00216v1](https://hexagonmath.org/2610.00216v1), claims an all-height `Re s>7/8` zero-free half-plane for **all unitary Hecke characters**, so its scope includes this family if the result and the needed uniform reciprocal consequence are accepted. Its proof has not been independently verified here. The retuned finite-order Hecke and Dirichlet candidates do not cover ᾱ³: no finite-order or pure-norm twist removes its nonzero angular type. Automorphic induction gives a weight-four CM GL₂ family with infinite projective image, since its conjugate-ratio has nonzero angular type −6; finite Artin factorization therefore supplies no automatic transfer from finite-order Hecke nonvanishing. The [Rubinstein–Restrepo Borrero elliptic-curve claim](https://hexagonmath.org/2610.00220v1) treats a specific weight-two/type-one CM family; it is not a stated type-three general quadratic-twist theorem. No stronger directly applicable independently checked fixed half-plane was found in this targeted, nonexhaustive search.

## A quadratic prefix mean

Assume the Goldmakher–Louvel quadratic Hecke sieve for the relevant fixed E-family and finite ray sectors. For `B,T≥1`, define the common masked prefix

    A_b(T)=Σ_(Nc≤T) μ(c) ᾱ(c)^3 ξ(c)^3 χ_c(b)^3 1_(c,f)=1.

The coefficients are squarefree in c and have modulus at most one. Uniformly in f in fixed polynomial ranges, the expected source consequence is

    Σ_(Nb≤B, b good) |A_b(T)|²
       ≪_ε (BTF)^ε [B T+B^(1/2)T²],          F=Nf.              (1)

Indeed decompose `b=d v²` with d squarefree. The original quadratic symbol gives `χ_c(b)^3=χ_c(d)^3 1_(c,v)=1`. Fix v and finite reciprocity sectors; absorb `ᾱ(c)^3 ξ(c)^3 1_(c,vf)=1` into one common column vector. Its squared norm is `O(T)` and its support is squarefree. The quadratic sieve then gives `O((BT)^ε (B/(Nv)²+T)T)`. Summing good ideal v of norm ≲√B yields (1). If source rows include arbitrary bad S-parts, split them by S-valuations/residue classes and retain their finite masks before summing; the fixed number of bad primes costs only a subpower factor. No individual cancellation or zero-free region is used.

## Tail balance

Assume the completed source theta polynomials satisfy for a common smooth profile and its differentiated profile

    Σ_(Nb≤B)|T_b(Z;f)|² ≪ (BZF)^ε[B+B²F/Z],
    |T_b(Z;f)|+|∂_(log Z)T_b(Z;f)| ≪ Z^(1/2+ε).                (2)

All original phases/masks and the source's finite-profile seminorm dependence are retained. The source cube inversion reads

    P_b(D;f)=Σ_c μ(c) ᾱ(c)^3 Ψ_b(c)^3 T_b(D/(Nc)^3;f)/(Nc),
    Ψ_b(c)^3=ξ(c)^3 χ_c(b)^3 1_(c,f)=1.

For 1≤C≤D^(1/3), weighted Cauchy and the first line of (2) give the short-index squared mean `≪B+B²F C³/D`. For the long part, ideal-norm partial summation, Minkowski in ℓ²(b), (1), and the pointwise bound and logarithmic derivative in (2) yield

    ||P_{b,>C}(D;f)||_{ℓ²(b≤B)}
       ≪(BDF)^ε D^(1/2)[B^(1/2)C^(−2)+B^(1/4)C^(−3/2)].       (3)

Thus the long squared mean is `≪D[B C^(−4)+B^(1/2)C^(−3)]`. Choose

    C=max{1,(D²/(BF))^(1/7),(D²/(B^(3/2)F))^(1/6)},

capped at the effective maximal cube index `O(D^(1/3))`. If a cutoff exceeds this support, the long sum is empty; the short sum only improves. The resulting bound is

    Σ_(Nb≤B)|P_b(D;f)|² ≪ (BDF)^ε [
       B+B^(11/7)F^(4/7)D^(−1/7)+B^(5/4)F^(1/2)].      (4)

When BF>D², use the elementary global mean `BD` instead of the short/long split; it is at most the third displayed term because their ratio is `(BF/D²)^(4/7)≥1`. Otherwise the chosen C is at least 1 and the balancing applies. The endpoint and support constants are absorbed in the fixed smooth-profile losses. Formula (4) uses a family mean of reciprocal coefficients rather than Hu's **pointwise** prefix bound, and it can beat that conditional bound in some parameter ranges; it has not yet been inserted into the physical d,k,g divisor sum. In particular no claim is made for the final inverse target or for the large-core complement without that calculation and an independent review.

**Independent review.** High_match checked the quadratic prefix mean, square-row masks, ℓ² partial summation and balance conditional on the source identities, finite sectors and uniform pointwise theta derivative. They also checked the use of BD in the large-BF case. The physical e-divisor insertion remains a separate calculation.

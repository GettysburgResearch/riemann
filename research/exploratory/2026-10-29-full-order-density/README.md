# Conditional conductor-density bounds for full fixed-order Hecke families

**Status:** Source-dependent proof of a generalization of [the full quartic bound](../2026-10-29-full-quartic-density/README.md). It uses de Faveri's preprint through the generalized conjugate-pair sieve replay for every effective order m≥3, the Goldmakher–Louvel quadratic Hecke large sieve, and the fixed-field short-detector proof replay. The powered-character compatibility and the quadratic source normalization have been independently audited below; the general rectangular-sieve and detector extensions remain source replays. The imported preprints have not been independently validated. This is a family density result, not an individual zero-free region; no priority claim is made.

Fix n≥3, a fixed number field K containing μ_n, its fixed good-prime set S and source n-th-order character family χ_g, and one fixed unitary Hecke character ν whose finite conductor is supported on S. Write every good n-th-power-free ideal uniquely as

    g=∏_{j=1}^{n−1} a_j^j,

with squarefree pairwise-coprime good a_j. At every good prime p dividing any a_j, the local character of χ_g is nontrivial, even when its order is a proper divisor of n. The source conductor formula and fixed ν therefore give

    N cond(νχ_g)≤X  ⇒  ∏_j Na_j≤X,

while the primitive conductor and the original deleted Euler-factor radical are `O(X)`.

For each `1≤j<n/2`, the powered source family `ψ_q=χ_q^j` has effective order `m=n/gcd(n,j)`. The compatible-choice calculation below and the [general-order rectangular-sieve replay](../2026-10-29-conjugate-conductor-sieve/README.md) lead to

    Σ_{u≈A,v≈B} |Σ_{q≈Q, q sf} λ_q ψ_q(u)overline(ψ_q(v))|²
      ≪(ABQ)^ε [AB+M^(1−1/m)N^(1/m)Q
                     +M^(1/m)N^(1−1/m)Q^(2/m)]∑|λ_q|²,        (1)

where M=min(A,B), N=max(A,B). For even n, the quadratic powered family `χ_q^(n/2)` is covered by Goldmakher–Louvel's Corollary 1.2. Their §2 uses the same FHL S,c,E construction and passes to the primitive inducing characters; on good ideals the primitive and de Faveri original values agree, including zero at primes dividing squarefree q. The key source-facing point is **compatibility of powered n-order characters with the order-m family**, up to finitely many ray-class phases and an invertible m-th-root embedding; the good-prime conductor alone would not establish it. No pair has effective m=2: `j<n/2` rules out `gcd(n,j)=n/2`.

Under these explicit inputs and the fixed-field detector/profile inputs, for every fixed `σ>1−1/(n−1)`, `σ<1` and ε>0 there exists τ>0 such that, when n≥5,

    Σ_{g good n-free, N cond(νχ_g)≤X} N(σ,X^τ;νχ_g)
       ≪_{K,S,n,ν,σ,ε} X^{2−1/(n−1)−σ+ε}.                  (2)

Zeros of the primitive inducing character are counted with multiplicity. For n=4 the sharper piecewise result is in the quartic note; for n=3 the ordinary cubic argument is stronger. The family-size calculation below gives ≫X(log X)^{n−2} distinct primitive characters of conductor at most X, hence (2) gives density-one zero-free rectangles in the full n-free family. It is not an individual statement.

## Global squarefree-column moment

Fix a dyadic box with `Na_j≈A_j` and product `P=∏_j A_j≪X`. Let λ_q be one common coefficient vector on squarefree q≈Q. Partition the finite reciprocity ray class of g, and absorb its q-dependent phase into λ. For j<n/2, freeze all variables except the pair (a_j,a_{n−j}); the other variables contribute only row-independent q-coefficient factors of modulus ≤1. Put

    U_j=A_j A_{n−j},     M_j=min(A_j,A_{n−j}),
    N_j=max(A_j,A_{n−j}), m_j=n/gcd(n,j).

Because `χ_q^{n−j}=overline(χ_q^j)`, (1) and ideal counting for the frozen variables give, apart from small powers,

    P + (P/U_j) M_j^(1−1/m_j) N_j^(1/m_j) Q
      + (P/U_j) M_j^(1/m_j) N_j^(1−1/m_j) Q^(2/m_j)
    ≤ P + (P/√U_j)Q + P U_j^(−1/m_j)Q^(2/m_j).             (3)

The first inequality uses `M_j≤N_j`. Original coprimality conditions may be removed only after enlarging a nonnegative outer sum; the χ_q zero masks are retained.

For even n, freezing all variables except a_{n/2} and applying the quadratic Hecke large sieve gives

    ≪ P+(P/W)Q,  W=A_{n/2}.                                   (4)

Let h be the maximum of all √U_j and, if present, W. There are `(n−1)/2` pairs for n odd, and `(n−2)/2` pairs plus one singleton for n even. Hence

    P=(∏_j U_j)W ≤ h^(n−1),
    P/h ≤ P^(1−1/(n−1))≤X^(1−1/(n−1)).                        (5)

If the maximizing group is the singleton, (4) directly gives the desired estimate. If it is a pair, `U_j≥P^(2/(n−1))`, so the last term of (3) is at most

    P^(1−2/[m_j(n−1)])Q^(2/m_j)
       ≤ X^(1−2/m_j) [X^(1−1/(n−1))Q]^(2/m_j)
       ≪ X+X^(1−1/(n−1))Q,                                   (6)

by weighted arithmetic–geometric mean, since m_j≥3. We used the **actual box product P** to select h and only then enlarged P to X; no lower bound P≈X is needed. There are O((log X)^(n−1)) boxes and finitely many fixed ray classes, so their losses are subpowers.

Putting `c=1−1/(n−1)`, every common squarefree inverse coefficient vector of mass O(1) therefore obeys

    Σ_g |M_r(g)|² ≪ X^{E(r)+ε}, E(x)=max(1,c+x).               (7)

The ordinary qv² decomposition, the row multiplier `χ_g(v²)` of modulus ≤1, and Minkowski over v yield the same exponent `E(m)` for normalized ordinary blocks. The finite-dimensional Sobolev lemma transfers both estimates to the detector's row-dependent real part and common height at a fixed polynomial height cost. No coefficient vector is allowed to depend separately on g inside a sieve application.

## Detector optimization for n≥5

The short detector supplies witnesses with `r≤t+O(η)`, `m≤1/2+O(η)`, `r+m≥t−O(η)`, and both squared sizes at least `X^{δ_g r−η}` and `X^{δ_g m−η}`, where `δ_g≥δ−O(e)` and `δ=2σ−1`. It excludes the possible pure norm label g=1 separately. Let

    f(x)=max(1,c+x)−δx.

For n≥5, `c≥3/4`. The condition σ>c is equivalent to `δ>2c−1`, and

    R=c+1/2−δ/2=c+1−σ<1.

Choose t just above 1/2. At t=1/2, for x∈[1−c,1/2], `f(x)≤R`. If x<1−c and `f(x)>R`, then

    x<1/2+(1/2−c)/δ ≤1/4,

because c≥3/4 and δ<1. Thus both f(r),f(m)>R would imply r+m<1/2, contrary to the witness constraint. Taking t>1/2 and absorbing the fixed losses yields (2), with τ chosen small after all profile and height orders. The standard individual zero-count factor and finite/bin/dyadic costs are absorbed into ε.

This is also the exact scalar optimum from these moments and witness inequalities: for t≤1, the feasible point r=m=1/2 gives value R; for t≥1, r=t,m=0 gives `min(1,c+(1−δ)t)≥R`. These are feasible points of the relaxation, not assertions about actual zeros. The method gives no density saving from these inequalities when σ≤c.

## Source and novelty qualifications

At each good prime, taking a power of the n-th residue symbol gives the corresponding lower-order residue symbol, up to an invertible exponent on μ_m. The compatible-choice argument below also addresses the source's Hecke representatives, fixed S-unit factors and ray-class normalizations, and has had an independent paper-level review. Goldmakher–Louvel's §2, Remark 3 and Corollary 1.2 cover the quadratic singleton with the same FHL construction and good-prime masks. The general-order rectangular-sieve itself is a source-proof replay, not a theorem printed in the cited paper. The fixed-type detector and all classical large-sieve inputs remain source dependencies. No exhaustive comparison with existing full-family conductor-density results has been made.

For ν=1, the same density estimate applies to the subfamily of characters of **exact order n**: it is a restriction of a nonnegative sum, and this subfamily also has ≫X(log X)^{n−2} distinct primitive characters. For a general fixed unitary ν, the twist need not have finite order, so no analogous claim about its exact order is made.

To see the denominator, each squarefree good ideal a admits `(n−1)^ω(a)` choices of nonzero local exponent, all giving distinct primitive characters because the good tame local character records each exponent. Their Dirichlet series is

    ∏_{p∉S}[1+(n−1)(Np)^(−s)] = ζ_(K,S)(s)^(n−1) H_n(s),

where H_n is holomorphic for Re s>1/2 and H_n(1)>0. A positive-coefficient Tauberian theorem gives `∼C X(log X)^(n−2)` labels with `N rad(g)≤X`. The uniformly bounded bad conductor allows replacing X by X/C₀ to obtain the same lower order under the conductor cutoff. To have order strictly below n, every local exponent must be divisible by some prime ℓ|n; for each ℓ the corresponding Euler product has only `n/ℓ−1<n−1` choices per prime and thus lower logarithmic order. This removes a negligible number of labels. Fixed ν multiplication is injective on characters, even when ν itself is not of finite order.

At σ=4/5, the full quartic result in the companion note gives exponent `13/15`; formula (2) for n=5 gives `19/20`. These examples require the same source-dependent sieve and detector inputs and are not individual zero-free claims.

## A proposed compatible-choice reduction for the powered-family gate

The following gives a concrete derivation of powered-family compatibility rather than treating matching local conductors as sufficient. It uses the choices in de Faveri §2.3. A second researcher independently checked the reduction, coprimality adjustment, residue-symbol identity, and Goldmakher–Louvel quadratic-family normalization; see [the source review](POWERED-FAMILY-INDEPENDENT-REVIEW.md).

Write `n=d m` and `j=d k` with `(k,m)=1`. Retain the n-family's finite S and modulus c: its assumption that the local c-neighborhood consists of n-th powers implies the corresponding m-th-power condition. The natural map `R_(c,n)=H_c⊗Z/n → R_(c,m)=H_c⊗Z/m` is surjective. Reducing a chosen basis of R_(c,n) gives a generating set of the same cardinality for the free rank-fixed R_(c,m), hence a basis. Use the same good ideal representatives E_i and the same chosen S-integer generators m_(E_i) to construct the order-m family, reducing each representative exponent modulo m.

For fixed good coprime q,b, choose the source n-decomposition

    q=(x) E_t G^n,      x≡1 (mod c),      (G,b)=1,

where the vector t has coordinates in `[0,n−1]`. Write t=t₀+mℓ, with coordinates t₀ in `[0,m−1]`, and put `G'=G^d∏E_i^(ℓ_i)`. Then

    q=(x) E_(t₀) (G')^m,
    x m_(E_t) = (x m_(E_t₀)) (∏m_(E_i)^(ℓ_i))^m.             (9)

A nontrivial technical point is that G' need not be coprime to b. By weak approximation choose z∈K× with z≡1 (mod c) and `v_p(z)=−v_p(G')` at every p|b. Replacing G' by `(z)G'` and x by `x z^(−m)` gives a valid m-decomposition with its power ideal coprime to b. The two resulting symbol numerators are b-units and differ by the m-th power of a b-unit, so the power-residue identities give

    χ_q^(n)(b)^j = χ_q^(m)(b)^k                             (10)

for the compatible choices. Both sides vanish when (q,b)≠1. The exponent k is invertible modulo m; the source explicitly allows a fixed change of the complex embedding of μ_m, which realizes this k-th power throughout the family. For m=2, Goldmakher–Louvel Remark 3 and Corollary 1.2 directly cover the n/2-th powers of the same FHL family, as checked in the linked source review. This paper-level argument is not a Lean-certified lemma.

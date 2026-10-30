# A fixed-height prime-mark transfer for the cubic full inverse

**Status:** A source-qualified short-scale estimate over K=Q(√−3), not a long-inverse bound, zero-free region, or assertion that the relevant selected rows exist. It uses standard sextic/cubic reciprocity and finite-ray normalization, fixed-field Hecke analytic continuation, and, for the stronger optional exponent, [Han Wu's GL(1) subconvexity theorem](https://arxiv.org/abs/1604.08551). Independent review is requested. The original noncoprime masks are retained.

Fix a finite good-prime set S containing the primes above 6 and the fixed reciprocity moduli. Let g run over good squarefree ideals in one fixed principal ray sector ensuring a consistent primary generator and cubic Hecke character. Let V≥0 be a fixed smooth radial annular row weight, and write ρ_g(p) for the compatible sextic symbol at a good prime p and χ_g for the corresponding cubic character; on good coprime ideals `χ_g=ρ_g²`. Work with the S-deleted cubic product

    F_g(s)=ζ_(K,S)(s)L_S(s,χ_g)L_S(s,barχ_g).

For D,P≥2 define a fixed-profile normalized full inverse block and a fixed-coefficient prime slot

    M_D(g)=D^(−1/2) Σ_{j good} c_g(j) W(Nj/D),
    c_g(j)=Σ_{dab=j} μ(d)μ(a)μ(b) χ_g(a)barχ_g(b),
    Q_P(g)=Σ_{p good prime, Np≈P} λ_p ρ_g(p),
    Σ_p|λ_p|²≪1,     |λ_p|≪P^(−1/2).                       (1)

The phases and norm twists in W and λ are fixed across g; arbitrary fixed real norm-twist heights are allowed because all estimates below use only their absolute coefficient magnitudes. In particular `Σ_p|λ_p|²≪1/log P` for a standard normalized fixed smooth prime profile. Let

    E_M=Σ_g V(Ng/Y)|M_D(g)|²,
    E_mark=Σ_g V(Ng/Y)|Q_P(g)|²|M_D(g)|².

Then the elementary Hecke-convexity input gives

    E_mark ≤ (Σ_p|λ_p|²) E_M
              + O_ε(Y^(1/2+ε)(PD)^(3/2+ε)).                  (2)

Using Wu's theorem with the currently admissible GL(2) Ramanujan exponent 7/64 improves the error to

    O_ε(Y^(1/2+ε)(PD)^(359/256+ε)).                           (3)

The implied constants depend on the fixed field, sector, profiles and ε, but not the lengths or fixed common phases. For `P=Y^z`, `D=Y^r`, (2) has an `o(Y)` error when `r+z<1/3`, and (3) when `r+z<128/359`. The requested regime r<z may be imposed, but it is not needed for the off-diagonal nonprincipality below.

## Expansion and local nonprincipality

Expand the inverse block as its exact d,a,b convolution in (1), and expand the prime square. The p=q terms have `|ρ_g(p)|²=1_((g,p)=1)` and, since V≥0, are at most `(Σ|λ_p|²) E_M`. No row mask is replaced by one in the original polynomial.

For p≠q, expand also the two inverse convolutions. For fixed triple indices `(d,a,b)` and `(d',a',b')`, the row character has the form

    ρ_g(p) overline(ρ_g(q))
       χ_g(a)barχ_g(b) overline[χ_g(a')barχ_g(b')].             (4)

At the good slot prime p, the sextic slot contributes exponent +1 modulo 6. Every cubic factor contributes an even exponent modulo 6, so their sum is odd and cannot vanish modulo 6. Thus the induced Hecke character in g is nonprincipal and ramified at p; the same applies at q. This remains true even if an inverse index shares a slot prime. The customary P>D separation makes those overlaps absent, but the parity argument itself does not require it.

Finite-ray reciprocity expresses (4) on the fixed g sector as a finite linear combination of finite-order Hecke characters, with fixed ray phases and the original masks. Its primitive conductor Q is bounded by a fixed S factor times the radical of `p q a b a' b'`. Annular support gives `N(dab),N(d'a'b')≪D`, hence

    Q ≪ P² D².                                                   (5)

The exponent D² is essential: if a,a' are distinct good primes of norm ≍D and the other inverse factors are units, the row character is ramified at both, so its conductor can indeed be ≍P²D². Shared-prime cancellation can only reduce the primitive conductor; any remaining zero masks at such primes must still be deleted as Euler factors.

## Smooth row bound and summation

For a nonprincipal finite-order primitive Hecke character ξ of K of conductor norm Q, a fixed ray sector and finite deleted radical R, squarefree row restriction has Dirichlet series

    L(s,ξ)/L(2s,ξ²) × (fixed and deleted Euler factors).

On `Re s=1/2+η`, the reciprocal denominator is absolutely convergent; all deleted factors cost `R^ε`. The numerator obeys either the standard convexity bound `Q^(1/4+ε)` or Wu's source-qualified subconvex bound `Q^(103/512+ε)`, with a fixed polynomial in height. Mellin inversion of V yields, uniformly in the moving character and masks,

    Σ_{g sf, fixed sector} V(Ng/Y) ξ(g) masks
       ≪_ε Y^(1/2+ε) Q^(1/4+ε) R^ε,                         (6)

and the analogous estimate with 1/4 replaced by 103/512. The fixed sector is expanded into finitely many fixed ray characters; no such factor can cancel the good p-ramification in (4). The entire numerator is nonprincipal, so no pole is crossed. The rapid Mellin decay absorbs the polynomial vertical factor.

For the inverse convolution, the coefficient ℓ¹ mass is `≪D^(1/2+ε)` by the ideal triple-divisor bound. The prime-slot coefficient ℓ¹ mass is `≪P^(1/2)` by Cauchy or the pointwise bound. Squaring these masses and inserting (5)–(6) gives the off-diagonal contribution

    ≪Y^(1/2+ε) · (P D) · (P²D²)^(1/4+ε)
      =Y^(1/2+ε)(PD)^(3/2+ε),

or exponent `1+2·103/512=359/256` using Wu. This proves (2)–(3) under the stated source inputs. The error bounds are absolute bounds for the p≠q terms; they do not require cancellation between inverse terms.

If a selected row family satisfies `|Q_P(g)|²≥P^σ`, positivity and (2) give

    Σ_selected V(Ng/Y)|M_D(g)|²
      ≤ P^(−σ) [(Σ_p|λ_p|²)E_M
                    + O_ε(Y^(1/2+ε)(PD)^(3/2+ε))],             (7)

with the Wu exponent substituted if desired. The final selected error can already be O(Y) in the larger region `3(r+z)/2−σz<1/2`, or `359(r+z)/256−σz<1/2` under Wu; the stricter ranges stated after (3) make the **unscaled** off-diagonal o(Y). Equation (7) is conditional on the actual slot selection and says nothing by itself about the unrestricted full-inverse energy E_M, which can contain a common base-field zeta obstruction. Row-dependent heights require the separate finite-dimensional Sobolev argument and its height cost; no arbitrary rowwise coefficient vector is admitted here.

## Exact marked growth without ordering the lengths

Let λ be a fixed nonzero smooth prime profile normalized by P^(−1/2), so the prime ideal theorem in the chosen fixed sector gives

    Λ(P)=Σ_p |λ_p|² ≍ 1/log P.                                  (8)

Define `Θ_K=sup Re ρ` over nontrivial zeros of ζ_K, and take the fixed nonnegative annular inverse profile W from [the cubic full-inverse growth note](../2026-10-29-cubic-full-inverse-mean/README.md), whose Mellin transform is zero-free in `Re s>0`. Assume its source-qualified unmarked identity. If

    0<r<1/4,   z>0,   r+z<1/3,

then, with D=Y^r and P=Y^z,

    limsup_{Y→∞} log[Y^(−1) E_mark]/log Y
       = r(2Θ_K−1).                                            (9)

The same conclusion holds for `r+z<128/359` if the source-qualified Wu estimate is used. No condition r<z is required.

The key is the diagonal of the prime slot. For every g in the support of the row weight, Ng≪Y. The number of prime ideals p with `Np≈Y^z` dividing g is `O_z(1)`, and each `|λ_p|²≪1/P`. Hence uniformly in every such row,

    Λ(P)−O_z(P^(−1)) ≤ Σ_p|λ_p|²1_((g,p)=1) ≤ Λ(P).          (10)

Combining (10) with the signed p≠q error in (2),

    [Λ(P)−O_z(P^(−1))] E_M − Err ≤ E_mark ≤ Λ(P)E_M+Err,
    Err≪Y^{1−δ₀}                                                (11)

for some fixed δ₀>0 after choosing ε small; use (3) for the larger Wu range. Since Λ(P)≈1/log P, the diagonal factor is positive and subpower. The unmarked cubic identity states

    limsup log(Y^(−1)E_M)/log Y=r(2Θ_K−1)≥0.

For the upper side of (9), (11) and Err=o(Y) suffice. For the lower side, along an Ω subsequence E_M is at least `Y^{1+r(2Θ_K−1)−η}` for any fixed η>0; choose η<δ₀, and the error cannot cancel the diagonal. The same reasoning covers the endpoint Θ_K=1/2, where the cubic mean note proves a zero-exponent Ω using the pole of its ζ_K(2s) factor. This proves the equality of marked and unmarked logarithmic growth exponents, conditional on the arithmetic inputs. It is an exact transfer, not a proof that either energy is O(Y^{1+ε}) or that ζ_K is zero-free.

**Independent source-level review:** Amplified_opt checked that at each slot prime, the odd sextic exponent cannot be canceled by the even cubic inverse exponents even when their supports overlap. The fixed ray projection cannot remove this good-prime ramification; the primitive conductor bound, deleted Euler-factor masks, Wu/Mellin row estimate and ℓ¹ exponent arithmetic also check under the stated sources. The remaining classical/Hecke normalization and subconvex inputs are not formalized here.

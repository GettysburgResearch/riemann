# A fixed-profile frequency transfer on Eisenstein rows

**Status.** This is a conditional transfer from a marked full-relative-inverse moment to the base ζ_K zero boundary, using Montgomery–Vaughan's Dirichlet-polynomial mean value theorem, the prime number theorem in fixed progressions and the [cubic full-inverse lower mean](../2026-10-29-cubic-full-inverse-mean/README.md). It does not establish the marked bound or a zero-free region. Its row transport and frequency/height quantifiers must match the application; it is not a counterexample to a detector-specific cell.

Let K=Q(ω), fix a good set containing the primes over 6, choose a rational prime ℓ≡1 mod 12 and a fixed primary prime ξ with Nξ=ℓ. The auxiliary inverse source omits primes above 6ℓ. Let g vary over the squarefree good principal-ray rows `g≡1 mod 9` in a fixed positive-weight norm annulus `Ng≈Y`, with ξ∤g. Let `M_g(Y^r)` be the full inverse polynomial for the cubic extension ζ-function from the cited note, using its one fixed compact-annular W with zero-free Mellin transform. Write χ_p(g) for the source zero-extended sextic symbol.

Fix a nonzero nonnegative smooth annular profile U, put `P=Y^w` for fixed w>0, and define

    Q_{j,t}(g)=P^(−1/2) ∑_{p good} η(p)^j χ_p(g) U(Np/P)(Np/P)^(it),
    η(p)=χ_p(ξ³),       j=0,1.                                  (1)

The prime sum omits the fixed primes over 6ℓ. For `T=CP` with a sufficiently large fixed C,

    ∑_{j=0}^1 (1/T)∫₀ᵀ |Q_{j,t}(g)|² dt ≫ 1/log P             (2)

uniformly for all such rows g. To prove this, group the sum by integer norm n. Each rational prime r≡1 mod3 splits as p p̄ and gives a two-term fiber of norm r. For a positive density of split r in any fixed nonempty subinterval of the prime profile's support, `(ℓ/r)=−1`: use quadratic reciprocity and the prime number theorem in fixed arithmetic progressions. For those r,

    η(p)η(p̄)=χ_(r)(ξ³)=(ℓ/r)=−1.

At all such fibers with p,p̄∤g, both sextic symbols have modulus one, and the parallelogram identity gives

    |χ_p(g)+χ_p̄(g)|²+|η(p)χ_p(g)+η(p̄)χ_p̄(g)|²=4.

Only O_w(1) rational primes of the annulus divide Ng≪Y. Thus the sum of the squared norm-fiber coefficient masses in the two sums is ≫1/log P. The Montgomery–Vaughan mean-value theorem for integer-frequency Dirichlet polynomials gives the same lower bound after averaging over `[0,CP]`: its error is O(P) times the coefficient mass, and C is chosen larger than that absolute constant. No fourth moment or independent prime phases are needed.

## Removing the auxiliary twist by row transport

Put `g'=ξ³g`. Since ξ∤g and g is squarefree, g' is sixth-power-free, with `Ng'=ℓ³ Ng`. For slot primes p outside 6ℓ,

    χ_p(g')=η(p)χ_p(g),      Q_{0,t}(g')=Q_{1,t}(g).            (3)

The cubic characters relevant to the full relative inverse are the squares of the sextic symbols. Multiplication by ξ³ therefore changes them by a sixth power, equal to 1 on every inverse source ideal coprime to ξ; the original zero masks agree there. Hence

    M_{g'}(Y^r)=M_g(Y^r)                                        (4)

for the fixed inverse source deletion. The base ζ_K inverse factor and its ξ Euler deletion are unchanged. The source row family must allow the fixed factor ξ³ and the ray sector into which it moves g: excluding ξ from the **rows**, or insisting that g′ remain in the original principal mod-9 sector, would invalidate this transport, even though ξ is excluded from the inverse source and slot primes. In applications with a separate fixed physical bad set, choose ξ outside the physical row restrictions and enlarge only the auxiliary inverse/slot deletion set.

Suppose an all-row marked estimate is available uniformly for `0≤t≤CP`, for both original rows of scale ≍Y and transported sixth-free rows of scale ≍ℓ³Y, with the same inverse length up to this fixed rescaling:

    ∑_u V(Nu/Y₀)|M_u(Y^r)|² |Q_{0,t}(u)|²
       ≪_{ε,w} Y^(1+κ+ε) (1+|t|)^A,                           (5)

where V is a fixed nonnegative row weight that majorizes the original and transported annuli after choosing `Y₀=Y` or `Y₀=ℓ³Y`, and the constant is independent of t,Y. Integrating (5) for both row families and using (2)–(4) gives the unmarked cubic-extension full-inverse moment

    ∑_g V₀(Ng/Y)|M_g(Y^r)|² ≪_{ε,w} Y^(1+κ+Aw+ε).              (6)

The fixed-sector lower mean in the cubic note then forces

    Θ_K ≤ 1/2 + (κ+Aw)/(2r)                                   (7)

for `0<r<1/2`, subject to its standard character-sum and reciprocity inputs. In particular, κ=0 would imply RH for ζ_K if the same fixed r and A work for arbitrarily small fixed w, and the permitted height always contains `[0,CP]`. Constants may depend on w; the exponent A may not grow so fast that Aw fails to tend to zero.

This conditional statement uses a single fixed smooth slot profile and the permitted frequency family, but it requires both original and ξ³-transported sixth-free rows, inverse-source deletion at ξ, and a height window at least CP. It does not apply to a single fixed t, to a family that excludes ξ from its rows, or to detector bins not known to contain the transported rows. If the height allowance is selected after w and can be smaller than w, the w→0 conclusion does not follow.

## What frequency averaging can and cannot save

The Montgomery–Vaughan upper bound gives the matching inequality to (2), uniformly for these rows:

    ∑_{j=0}^1 (1/T)∫₀ᵀ |Q_{j,t}(g)|² dt ≪ 1/log P.             (8)

Indeed each norm fiber contains at most two prime ideals, so its squared coefficient mass is O(P^−1) times the number of prime ideals in the fixed annulus; the prime ideal theorem bounds that by O(1/log P). The mean-value error is O(P/T) times the same mass. Combining (2) and (8), and multiplying by the nonnegative row-dependent but frequency-independent `V₀(Ng/Y)|M_g(Y^r)|²`, gives the two-sided equivalence

    (1/T)∫₀ᵀ ∑_g V₀(Ng/Y)|M_g(Y^r)|²
                 (|Q_{0,t}(g)|²+|Q_{1,t}(g)|²) dt
       ≍ (1/log P) ∑_g V₀(Ng/Y)|M_g(Y^r)|².                   (9)

The implied constants depend on the fixed data and w, not on Y or g. By (3)–(4), the second marked term is the same untwisted profile evaluated on the ξ³-transported row. Thus a direct **average-frequency** estimate of size `Y^{1+κ+ε}` for these two row pieces is, up to logarithms, exactly as strong as the corresponding unmarked full-inverse moment. It would avoid a worst-case height loss, but for κ=0 and 0<r<1/2 it would still imply RH for ζ_K by the lower mean. Frequency averaging alone therefore cannot supply this estimate from generic Dirichlet-polynomial orthogonality: its diagonal retains the full base-zeta obstruction. The statement assumes M_g itself does not depend on t; a detector with a row- or frequency-dependent inverse requires a separate argument.

**Independent review:** Amplified_opt checked the split-prime norm-fiber identity, fixed progression density, source-mask matching, ξ³ row transport, common frequency and fixed-scale rescaling, subject to the stated admissibility hypotheses.

**Second independent review:** High_match checked the quadratic twist product, norm-fiber diagonal, original masks, Montgomery–Vaughan grouping, sixth-free row transport and ξ-deleted cubic inverse identity. The row-family, profile-rescaling and height assumptions remain conditional.

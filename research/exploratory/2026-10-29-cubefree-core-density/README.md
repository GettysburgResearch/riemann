# Cube-free core and natural-label density at 437/500

**Superseded as a numerical bound:** [the direct n-free four-face theorem](../2026-10-29-direct-nfree-density/README.md) applies the original n-free-row sieve directly and gives stronger exponents at the exact tracker boundary, without the moving-core or short-cutoff inputs. The present source-qualified calculations and covers remain documented as an independent decomposition approach.

**Status: source-qualified density implication, not a new individual zero-free theorem.** The rational certificate below is exact. The deduction assumes the cited de Faveri arbitrary-coefficient n-th-order sieve and FHL character identities, and the conductor-uniform Hecke detector, common-profile/height and short-cutoff replay described in [the moving-twist note](../2026-10-29-full-sixthfree-fourth-density/README.md). Those analytic inputs have not been independently established here. Comparisons are with one named source, not a complete priority claim.

Fix one integer n in the table, a fixed number field K containing μ_n, and fixed FHL data and bad set S. Assuming those inputs, for every ε>0 there is τ>0 such that

    Σ_{u good, n-free; Nu≤X} N(437/500,X^τ;χ_u) ≪ X^(R+ε).   (1)

Here zeros of the primitive inducing functions are counted with multiplicity; implied constants may depend on the fixed field, order, data and ε. The exact certificate gives:

    n      R          de Faveri Cor. 1.5         difference
    8      449/1000   478987/1061492              594273/265373000
    9      7/16       1291685/2899511             370383/46392176
    10     43/100     83626/189655                41487/3793100
    11     21/50      2100479/4803751             4145179/240187550
    15     2/5        856711/2003395              55353/2003395
    20     39/100     807269/1916740              149351/4791850
    30     37/100     959263/2312395              2073537/46247900

The comparator uses its middle branch at σ=437/500, for which

    D_n=1−δ[δn²−(6σ−2)n+3]/[δ(3−2σ)n²−4σn+2], δ=187/250.

Each strict fixed-height gap permits a sufficiently small positive height exponent after accounting for both statements' height losses. The source's broad n-free family is the same label ordering; no conductor-ordered comparison is asserted. Squarefree good labels already give ≫X distinct primitive characters, because their good conductor supports are their labels.

## Decomposition and moments

Write every good n-free ideal uniquely as `u=q b³`, with q cube-free; q and b need not be coprime. De Faveri §2.5.1, equation (2.4), gives `χ_u(a)=χ_q(a)χ_b(a)³` including the original zero extensions, also at shared primes. For a dyadic `Nb≈B=X^b`, set `Y=X/B³` and `U=X/B²`. The primitive conductor and deleted radical of χ_u are ≪_S Nrad(qb)≪U, with fixed infinity type. The detector is applied first to χ_u with this common upper conductor; only afterwards is b fixed, so χ_b³ becomes a bounded common coefficient in each column vector.

Because q is cube-free and n≥8, it is n-free; the available all-row form of de Faveri's order-n sieve, applied with n-free columns, gives

    Σ_{Nq≤Y}|Σ_a c_aχ_q(a)|²
      ≪ (YD)^ε [Y+Y^(1/n)D+Y^(1−1/n)D^(2/n)] Σ|c_a|², (2)

where Na≈D. The discarded `Y^(2/n)D^(1−1/n)` is bounded by the third term for D≤Y and by the second for D≥Y. The sieve can be applied to the larger all-row family and hence to q cube-free. The inverse columns are squarefree. For the ordinary second moment, decompose its unrestricted column as a=a₁v² with a₁ squarefree; for fixed v, χ_u(v²) is a row contraction of modulus at most one. For an ordinary fourth moment first convolve two ordinary blocks, then use the same squarefree decomposition. In both cases Minkowski, divisor bounds, and the fixed-v masks allow (2) after an X^ε loss. The moving χ_b³ and χ_u(v²) masks are retained; they are not assumed constant as q varies. Summing over b costs B^(1+ε).

With D=U^x and δ=187/250, dividing a second or fourth witness by its squared threshold yields the following X-exponent faces:

    f₀=(1−2b)(1−δx),
    f₁=b+(1−3b)/n+(1−δ)(1−2b)x,
    f₂=b+(1−3b)(1−1/n)+(2/n−δ)(1−2b)x.                 (3)

Write f=max(f₀,f₁,f₂). As in the source-qualified detector, the actual witnesses satisfy r≤t, m≤1/2 and r+m≥t up to arbitrarily small fixed losses. The inverse second moment yields f(r); ordinary second yields f(m), and ordinary fourth f(2m). The conductor U≥X^(1/3) and bounded t intervals permit a single sufficiently small global height power after all fixed profile and loss choices.

## Certificate and witnesses

[check_cover.py](check_cover.py) partitions 0≤b≤1/3 into 100 rational intervals. On each it chooses one rational t>1/2 and one of:

* inverse, checking f on `[t−1/2,t]`;
* second, checking f on `[t/2,t]`, using inverse when r≥t/2 and the actual m∈[t/2,1/2] otherwise;
* fourth, checking f on `[2t/3,max(t,1)]`, using inverse when r≥2t/3 and the actual `2m∈[2t/3,1]` otherwise;
* the trivial label count `B Y≤X^(1−2b)`.

Each face is affine separately in b and x, so checking the four corners of every interval rectangle is sufficient. All accepted checks use exact rational arithmetic; [cover.json](cover.json) records the chosen t, mode and maximal face. The partition, rational cutoff choices and resulting finite losses are fixed before X grows. Dyadic endpoints and individual zero counts are absorbed by X^ε. A t<1 selection depends explicitly on the cited short-cutoff detector replay; this certificate does not prove that analytic extension.

In particular, n=11 and K=Q(ζ₁₁) furnish a **conditional** natural-label density exponent 21/50 for the original order-11 characters at σ=.874. Passing to all conjugate powers and then to cyclic fields needs the source powered-family identification and finite-fiber argument in [the prime-family note](../2026-10-29-all-prime-natural-relative/README.md). The base ζ_K is a product of finite Dirichlet L-functions; the separate retuned Dirichlet candidate at .8738694, if admitted with its conventional semantics, would cover that base at σ=.874. Neither this certificate nor that conditional application proves a new half-plane on its own.

## All fixed orders n≥11 and cyclic prime-degree fields

The same source-qualified implication (1) holds for every fixed integer n≥11 with

    R_n=21/50  for 11≤n≤14,       R_n=2/5  for n≥15.         (4)

The independent exact checker [check_all_prime.py](check_all_prime.py) covers the two parameter rectangles `1/n∈[1/14,1/11]` and `1/n∈[0,1/15]`, each with the same 100 b-intervals. The faces are separately affine in b, h=1/n, and x, so their extrema occur at the eight rectangle corners. The endpoint h=0 only certifies a limiting inequality: n, its field and all source constants remain fixed. The recorded choices are in [all-prime-cover.json](all-prime-cover.json).

The source comparator D_n strictly decreases for n≥4, because

    dD_n/dn = −187(187n−500)(35343n−125000)
                /(58531n²−218500n+125000)² < 0.

At the relevant limiting points

    D_14−21/50 = 1013851/106725950 > 0,
    lim_{n→∞} D_n−2/5 = 4/1565 > 0.

Thus each fixed order in (4) gives a strict comparison with that source at fixed height; this does not assert uniformity as n or K varies.

Fix an odd prime p≥11 and let K=Q(ζ_p). Subject to (1), the stated source compatibility for the nonzero powers χ_u^j, j=1,…,p−1, and the standard Kummer/class-field and conductor-discriminant inputs, the corresponding full natural p-free label family satisfies

    # {nonunit labels Nu≤X with ζ_{L_u}(s) having a zero in
       Re(s)≥437/500, |Im(s)|≤X^τ} ≪ X^(R_p+ε).              (5)

Indeed, for each fixed j=1,…,p−1 use the compatible FHL family obtained by changing the root-of-unity embedding to its j-th power, on the same original ideal labels u; apply (1) separately to each such family. This preserves the norm cutoff Nu≤X, good support, zero masks and primitive conductors. Merely replacing each local exponent e by je mod p is not sufficient for the truncated count because that replacement can change Nu. Each nonunit label presents a degree-p cyclic extension L_u/K, a field has at most p−1 generating characters, and squarefree good labels provide ≫X distinct fields. For the base factor, ζ_K=ζ·∏_{χ nonprincipal mod p} L(s,χ), where the factors are primitive Dirichlet L-functions. The pole at s=1 is not counted as a zero. Its nonvanishing in Re(s)≥437/500 follows only **conditionally on admission and conventional analytic interpretation** of the separately fresh-kernel-replayed [Dirichlet candidate](../2026-10-29-return-retune-8738694/README.md), whose boundary is .8738694. This is a deduction from that candidate and the stated inputs, not a new proof of an individual zero-free region.

The conductor of χ_u is ≪rad(u), so the relative conductor-discriminant formula gives `|D_{L_u}|≪_{p,S} X^(p−1)`. Choosing X as a sufficiently small fixed multiple of `Y^(1/(p−1))` therefore produces a specified family of ≫`Y^(1/(p−1))` such fields with `|D_{L_u}|≤Y`, of which at most `O(Y^(R_p/(p−1)+ε))` fail the rectangle with a suitable small height power. This does **not** count all cyclic p-extensions of K with discriminant ≤Y; it is the family produced from the stated X-truncated natural labels. The p-independent display of R_p does not imply uniform constants or heights in p.

**Independent review.** Families checked the moving twist, source sieve and effective conductor, and independently reproduced the h-corner coverage. High_match checked the same source-qualified deduction, interval witnesses, conductor and full-field/discriminant conversion. Both reviews treat the cited detector and sieve statements as inputs rather than independently established theorems.

The same two all-order targets in (4) also pass at the rational boundary `σ=87387/100000=.87387`; [check_near_boundary.py](check_near_boundary.py) makes a fresh rational cutoff selection and records it in [all-prime-near-boundary-cover.json](all-prime-near-boundary-cover.json). Thus, conditional on the identical analytic inputs and the retuned Dirichlet candidate's admission and conventional semantics, the cyclic-prime-field consequence also holds in the rectangle `Re(s)≥.87387`. This boundary lies .0000006 to the right of the candidate's .8738694 and does not itself improve that individual boundary. At this σ, the named comparator remains strictly decreasing for n≥4: writing its denominator as `2340912231 n²−8738700000 n+5000000000`, its derivative is

    −37387(37387n−100000)(1414686693n−5000000000)
       /(2340912231n²−8738700000n+5000000000)².

The comparator gaps at n=14 and at the limiting endpoint are respectively `21001199963/2134231232975` and `904/313065`. Heights and constants can depend on the fixed p and the chosen separation from the candidate boundary.

The three finite-order certificates n=8,9,10 also hold at `.87387` with the same respective exponents `449/1000, 7/16, 43/100`; [check_near_boundary_finite.py](check_near_boundary_finite.py) and [near-boundary-finite-cover.json](near-boundary-finite-cover.json) verify the complete intervals with exact arithmetic. Their source comparator gaps are respectively `245511779/94764266500`, `15459283983/1855449451376`, and `1711713337/151704223100`. Together these give the source-qualified natural-label density implication at this boundary for every fixed n≥8. The assertion is for a sufficiently small polynomial-height rectangle; it supplies no all-height nonvanishing for the varying Hecke factors.

The certificates also hold at the **exact** retuned candidate boundary `θ=4369347/5000000=.8738694`: the independently regenerated [check_at_candidate.py](check_at_candidate.py) verifies both rectangles in [at-candidate-cover.json](at-candidate-cover.json), with δ=1869347/2500000. Under precisely the same source inputs, for each fixed odd prime p≥11 all but `O(X^(R_p+ε))` of the natural labels Nu≤X have **every nontrivial relative factor** L(s,χ_u^j) zero-free in the closed rectangle `Re(s)≥θ, |Im(s)|≤X^τ`. The powered-family estimates are applied separately on the same original labels, then united over the finitely many j. If the retuned Dirichlet candidate is admitted with its conventional analytic semantics, it supplies base-factor nonvanishing on the **open** half-plane `Re(s)>θ`; consequently the corresponding density-one cyclic degree-p field family has ζ_{L_u}(s) zero-free for `Re(s)>θ, |Im(s)|≤X^τ`. The pole at 1 is not a zero. The discriminant-truncated statement above applies with the same family and appropriately scaled positive height power. This is a conditional polynomial-height family-density statement, not an all-height result or a new individual zero-free boundary.

At θ, the fixed-height de Faveri comparison remains strict. The comparator D_n has derivative

    −1869347(1869347n−5000000)(3536727880773n−12500000000000)
       /(5852276793591n²−21846735000000n+12500000000000)² < 0

for n≥4. The relevant exact gaps are `D_14−21/50=52511352552743/5335574759648975` and `lim_{n→∞}D_n−2/5=45224/15653265`.

At the exact candidate boundary, the finite n=8,9,10 covers likewise hold with exponents `449/1000, 7/16, 43/100`. Their reproducible checker [check_at_candidate_finite.py](check_at_candidate_finite.py) uses a rational t-grid of step 1/500, with the chosen bins recorded in [at-candidate-finite-cover.json](at-candidate-finite-cover.json). The respective de Faveri gaps there are `2149571143879/829186854647750`, `38655637190463/4638620884493936` and `611412255151/54180047051300`. Families independently reproduced the two n≥11 exact-θ covers, source-comparison gaps and closed-relative/open-full-field interpretation.

## Fourth-free core for large orders

At the same exact θ and under the same analytic assumptions, the original decomposition may instead be `u=q₄ b⁴`, with q₄ fourth-free. For n≥30 this is a valid n-free row family, while `Y=X/B⁴` and the original-character conductor bound is `U=X/B³≥X^(1/4)`. The general all-row source sieve and exact common factor χ_b⁴ therefore give the same detector bound with faces

    f₀=(1−3b)(1−δx),
    f₁=b+(1−4b)/n+(1−δ)(1−3b)x,
    f₂=b+(1−4b)(1−1/n)+(2/n−δ)(1−3b)x,
    0≤b≤1/4,   δ=1869347/2500000.                            (6)

All shared-prime zero masks, ordinary-column decompositions and source/height qualifications are the same as for q₃. The exact rational h-corner checker [check_fourth_core.py](check_fourth_core.py), with its [cover](fourth-core-cover.json), proves the following stronger exponents for fixed n in the specified ranges:

    n≥30: R=37/100;  n≥50: R=9/25;
    n≥100: R=7/20;  n≥1000: R=17/50.                         (7)

The 100 rational b intervals, t choices and inverse/second/fourth/trivial witness modes are as above, with the trivial count `X^(1−3b)`; each h-rectangle is `[0,1/n₀]`. In particular the prime-degree field consequence at θ inherits these sharper exponents when p is in the corresponding range. The constants and allowable heights are still fixed-p quantities. Since the named de Faveri comparator decreases with n and has limit `1261306/3130653`, its gap over the last exponent is at least `9844199/156532650>0`. These are density bounds at polynomial height, not new individual or all-height zero-free regions.

# A proposed 49/78 density for all sixth-free Eisenstein labels

**Status.** A source-qualified conditional theorem. The uniform detector interface is reduced below to standard fixed-field Hecke estimates and the cited detector proof, while the source squarefree-column large sieve, its analytic proof, the `t<1` detector replay, and the common-profile/Sobolev/height transfers remain imported and not independently established here. It would improve a named sixth-order zero-density source, not prove an individual zero-free region. A theorem valid only for a fixed finite-ray twist is not enough for the growing twists below.

Let `K=ℚ(ω)`, fix the good-prime set S including primes above 6, and let χ_u be the source sextic FHL character for each good sixth-power-free primary u, with its original zero masks. Under the exact uniform inputs described below, for each ε>0 there is τ>0 such that

    Σ_(u good sixth-free, Nu≤X) N(4/5,X^τ; χ_u)
       ≪_ε X^(49/78+ε).                                    (1)

Here zeros belong to the primitive inducing L-functions and are counted with multiplicity; a possible principal presentation is handled separately. There are `≫X` distinct such primitive characters already among squarefree good u, because their good conductor is exactly `(u)` and squarefree ideal counting has positive density. Thus (1) would give a density-one zero-free rectangle within this natural-index family at sufficiently small power height. De Faveri Corollary 1.5 gives exponent `209/326` at the same real-part boundary and fixed/polylogarithmic height; the improvement in X exponent is `82/6357>0`, before the sources' height losses. It remains a conditional source comparison, not an exhaustive priority claim.

## Exact splitting and the needed uniform interface

Every good sixth-free ideal has the unique decomposition

    (u)=q b²,   q squarefree,                                  (2)

with no requirement that q and b be coprime. Choose primary generators and partition the finitely many necessary ray/unit classes. De Faveri §2.5.1, equation (2.4) and the immediately following sentence, explicitly give multiplicativity in the label for all integral good ideals even when the factors overlap; the original zero extensions make it valid at noncoprime column ideals. Thus on every good column ideal a

    χ_u(a)=χ_q(a) χ_b(a)².                                    (3)

For each fixed b, the second factor is a **common** bounded column multiplier, including its zeros; it may be multiplied into arbitrary inverse and ordinary sieve coefficients. It is not treated as an S-supported fixed ray character. Sixth-freeness of u ensures every good prime in rad(qb) has exponent 1–5 and is tamely ramified, so the primitive conductor of χ_u is `≪Nrad(qb)` up to the fixed S factor; the original-vs-primitive Euler masks have no extra growing good-prime deletions beyond that conductor.

For a norm dyad `Nb≈B=X^b`, `0≤b≤1/2`, put

    Y=X/B²=X^(1−2b),    U=Y B=X^(1−b).                       (4)

The q family has `Nq≪Y`, and all its χ_(qb²) have conductor `≪U`. The source's squarefree sextic large sieve, applied to χ_q with arbitrary common coefficients multiplied by χ_b², supplies

    Σ_(q good sf, Nq≪Y) |Σ_a c_a χ_(qb²)(a)|²
      ≪_ε (UY)^ε [Y+Y^(1/6)D+Y^(5/6)D^(1/3)] ||c||²       (5)

for squarefree columns of norm ≪D, with finite ray partitions and fixed bad-prime masks retained. The fourth generic sextic-sieve face `Y^(1/3)D^(5/6)` is absorbed by `Y^(5/6)D^(1/3)` when `D≤Y` and by `Y^(1/6)D` when `D≥Y`. The factor χ_b² costs no norm because `|χ_b²(a)|≤1`. Squaring an ordinary block and writing a column as `a=a₁v²` gives the analogous fourth moment by the divisor-bound/Minkowski argument of the [box note](../2026-10-29-fourth-moment-cyclic-box/README.md). This use of arbitrary coefficients is essential: a bound whose constants depend arbitrarily on the conductor of χ_b² would not suffice.

The other essential input is a **uniform detector** for all original χ_(qb²) of conductor `≪U`, not just a detector with b fixed and constants depending on b. It provides simultaneous inverse/plain witnesses at scale U with `r≤t+O(η)`, `m≤1/2+O(η)`, `r+m≥t−O(η)`, thresholds `U^((3/5)r−O(η))` and `U^((3/5)m−O(η))`, and common-coefficient/profile/Sobolev and polynomial-height controls uniformly for `0≤b≤1/2`. The derivation from the cited fixed-field detector and its listed standard Hecke inputs is given below. The third parameter range uses t=17/20<1 and therefore needs the cited short-cutoff **replay**. A finite b-mesh, with all small losses chosen before the height power, is needed for uniformity.

## Exact scalar calculation

There are `≪B^(1+ε)` choices of b per dyad. After summing them and using (5), define

    f₀(x)=(1−b)(1−3x/5),
    f₁(x)=(1+4b)/6+(2/5)(1−b)x,
    f₂(x)=(5−4b)/6−(4/15)(1−b)x,
    f(x)=max{f₀(x),f₁(x),f₂(x)}.                           (6)

The inverse second-moment and ordinary fourth-moment count exponents are respectively f(r) and f(2m). For actual witnesses the count is bounded by their minimum, with `r+m≥t` and the **entire** interval `m≤1/2`, not an assumed equality. The following choices give at most `49/78` throughout:

* For `0≤b≤2/17`, choose `t=15(1−2b)/[13(1−b)]≥1` and `L=2t/3`. The decreasing f₂ at L equals the increasing f₁ at t, both `(49−20b)/78`; f₀(L) is no larger. If r≥L use inverse; otherwise `2m≥L` and `2m≤1≤t`, so use ordinary fourth.
* For `2/17≤b≤3/13`, choose `t=1`, split at `L=2/3`, and note the maxima of f₀,f₁,f₂ on `[2/3,1]` are respectively `3(1−b)/5`, `(17+8b)/30`, `(59−44b)/90`; all are ≤49/78 in the stated interval.
* For `3/13≤b≤29/78`, choose `t=17/20`. The inverse witness alone has `r∈[7/20,17/20]`; f₀ and f₂ decrease and f₁ increases, and their worst endpoint values on this b interval are below 49/78. The narrowest exact margin is `49/78−7349/11700=1/11700`.
* For `29/78≤b≤1/2`, trivial counting gives at most `X^(1−b+ε)≤X^(49/78+ε)` labels, before the standard small-height zero-count factor.

The original primary label u=1 and zeros of any fixed exceptional presentation contribute at most `X^(O(τ)+ε)`. Sum the logarithmic ideal-norm dyads and take a finite b-mesh. For the first three ranges, choose the detector and bin losses smaller than the requested ε, then choose τ below the uniform height orders times the minimum scale exponent `1−b≥1/2`. In the last range choose τ small enough that the trivial individual zero-count cost is absorbed. This yields (1) subject to the cited source and analytic inputs. Endpoint powers and fixed unit/ray fibers cost at most X^ε.

## Uniform detector with a moving b

The following checks the interface against the [fixed-field buffered proof](../2026-10-29-cubic-short-detector-proof/README.md). It is a replay for the original sextic character family, conditional on the standard fixed-field Hecke facts, the source FHL conductor/mask formula and the source detector/profile steps; it is not an independent verification of those analytic inputs.

For each dyad set `U≈X/B`; fixed dyadic constants only change constants. For every retained `u=q b²`, sixth-freeness makes the exponent at every good prime dividing u nonzero modulo six. The primitive inducing character ξ_u therefore has conductor at every such good prime, with

    Nf(ξ_u) ≪_S N rad(qb) ≤ Nq·Nb ≪ U.                       (7)

The FHL source's trivial infinite type is the **same** for every u, and its possible bad-place conductor is bounded by a fixed S-dependent constant. The original character has the same good ramification support and fixed bad-prime zero extension, so the radical of its deleted Euler factors is also `≪_S U`. No fixed-b hypothesis is used here. Since a good prime with exponent 1–5 contributes a nontrivial tame local character, `u=1` is the only possible principal presentation; its individual zero count is treated separately.

The standard Hecke functional equation, fixed-field Euler product and fixed-strip bounds are uniform over all finite-order ξ_u with conductor (7): all archimedean gamma factors are those of the trivial infinity type, and the strip bound is a fixed power of `U(3+|t|)^[K:Q]`. The finite deleted-product estimates likewise depend only on the radical upper bound `≪U`. Apply the detector's nested-maxima construction separately to the finite collection `{ξ_u,bar ξ_u}` at the single global base U. With a fixed floor strictly between 1/2 and 4/5 and a fixed bin width e, the number of bins and every Borel–Carathéodory/three-circles constant depend on K,S,e, not on u or b. In its buffered rectangle both original reciprocal functions are `≪U^η`; the reflected plain L-function has the source bound `≪U^(a−1/2+12e+η)` times a fixed polynomial height factor, uniformly using (7). Smaller actual conductors only improve that upper bound.

The Gamma-convolution proof in the cited packet now applies to each selected zero with the **same** scale U. Its truncated inverse has length `U^t`, its auxiliary smoothing power and strip-growth order are fixed uniformly on the bounded t interval `[17/20,15/13]`, and all separated Fourier frequencies share one height allowance. After the common product profile is separated, saturation gives the simultaneous inverse/plain witnesses and inequalities quoted before (6). The use of t=17/20 is precisely the cited short-cutoff replay; no printed t≥1 result is silently extended. The selected primitive zero and its conjugate are treated as in the packet, with original masks and the one possible principal row retained separately.

For the moment step **fix b only after the detector has been formed**. Equation (3) then makes `χ_b(a)^2` a common column coefficient of modulus at most one. It may grow in conductor with b, but no arithmetic estimate is applied to it as a fixed Hecke twist: the squarefree-q sextic sieve accepts an arbitrary common vector and is uniform in its ℓ² norm. The same fixed-b multiplier is present after differentiating the common β/height profiles. For the ordinary fourth moment, square the block, write its column `a=a₁v²`, fix v and use `χ_u(v²)` as a row contraction; divisor-bounded coefficients and Minkowski preserve the `E(2m)` bound. A fixed finite number of Sobolev derivatives in β and height gives common vectors with the same mass estimates, and the O(U^τ₀) height-cover cost is absorbed by selecting τ₀ after the desired loss. The source's finite ray reciprocity classes are partitioned before applying the sieve; all constants are uniform in b.

Since `U=X^(1−b)` and `0≤b≤1/2`, one has U≥X^(1/2) up to fixed dyadic constants. Thus a fixed X-height `X^τ` lies inside every required U-height buffer after τ is chosen below half the available U-power and the fixed polynomial height losses. The individual zero count per primitive Hecke character costs only a logarithm times a fixed polynomial in `X^τ`, uniformly by (7), so the row count transfers to zeros with multiplicity. A finite mesh in b and t allows fixed source constants and loses an arbitrarily small power before the final height choice. This verifies the moving-b **quantifiers** within the cited source framework; it does not validate the general sextic sieve, the fixed-field analytic estimates or the short-t replay independently.

**Independent review.** High_match checked the source multiplicativity with overlapping q,b and all zero masks, the conductor bound U=YB, the absorbed fourth sieve face, and every scalar interval. The uniform detector quantifier replay remains conditional on the cited analytic/source inputs and the short-t extension.

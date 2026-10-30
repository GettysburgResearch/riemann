# A fixed-field saturated inverse witness at conductor scale

**Status:** Proposed source-based detector lemma and proof, for independent review. It is the generic analytic part needed by [the cubic conductor-density calculation](../2026-10-29-cubic-conductor-detector/README.md). It imports standard Hecke continuation, functional equations, strip growth and Euler products, and follows OpenAI Lemmas 4.9–4.10 and 8.1–8.3. The finite-seminorm and trace-tail details below must be checked before this is treated as a fully established theorem. It is not a zero-free statement.

## Statement

Fix a totally complex number field K, a finite set S, a fixed infinity-type orbit, and fixed positive strip and height ranges. Let a finite set of rows have scale U≥2. For each row choose a finite presentation set closed under conjugation, consisting of primitive unitary Hecke characters of those fixed types and their original imprimitive presentations. **Assume every primitive inducing L-function is entire**, excluding all pure norm characters, including the principal character. Assume their conductor norms and deleted Euler-factor radicals are O(U), uniformly over rows, and that all finite presentation choices have fixed cardinality. Let σ₀>1/2 be fixed.

For every requested loss ε>0 there are fixed positive e,τ and a finite set of smooth-profile derivative orders, such that for every sufficiently large U, each row with some presentation having a zero ρ with Re ρ≥σ₀ and |Im ρ|≤U^τ has a presentation, a bin endpoint a≥σ₀−e, a common dyadic inverse length U^r and a centrally normalized inverse polynomial

    M_r = U^(−r/2) Σ_(q outside S) μ_K(q) ψ(q) W(Nq/U^r)

with

    1/2−ε ≤ r ≤ 1+ε,     |M_r|² ≫ U^((2a−1)r−ε).          (1)

The profiles are annular, depend only on a fixed finite number of real parameters and a pure norm-twist frequency of size O(U^τ), and have uniformly bounded untwisted smooth seminorms. Their permitted derivative orders and the binning/height choices are uniform in the row. Grouping dyadic lengths and finite presentation labels costs only O((log U)^C). Any rowwise supremum over the remaining fixed-dimensional parameters may be controlled by Sobolev at those derivative orders, at a fixed polynomial cost in U^τ; applying an arithmetic moment after this step requires its uniformity for the differentiated **common** coefficient profiles. Pure norm presentations must be removed or treated separately. The claim is insensitive to multiplying U by a fixed factor.

Nonprincipal **alone** is insufficient: for real nonzero t₀ the pure norm character `psi(a)=(Na)^(it₀)` is nonprincipal and unitary, but `L(s,psi)=zeta_K(s−it₀)` has a pole at `1+it₀`. Such a pole can lie in a logarithmic-control disk and contributes an extra residue in the Gamma-integral shift below. The printed OpenAI argument concerns nonprincipal finite-order characters, for which no pure norm twist occurs. In the later fixed-background families `nu chi_g` with good cube-free labels and `cond(nu)` supported on S, every good prime dividing g is ramified in `chi_g` and cannot be canceled by ν. A pure norm character is unramified at every finite prime, so only the unit-ideal label g=1 can qualify. A finite presentation dictionary gives at most a fixed number of such labels. Their L-functions are fixed norm shifts of `zeta_K`; the standard individual zero count is `O((T+1) log(2+T))` for fixed K and shifts, and is absorbed by choosing the polynomial height exponent small enough. For other row parameterizations, bounded multiplicity must be established separately.

## Derivation from the standard analytic inputs

Use OpenAI's nested-height construction with T₁=U^τ and a finite number of intervals of heights 3jT₁. For each row, consider all presentations and conjugates at once, and include a sentinel floor σ_f=(σ₀+1/2)/2 in every maximum. These maxima lie in [σ_f,1], and the assumed zero makes the first at least σ₀. A pigeonhole index and grid rounding produce a bin a with a≥σ₀−e and no zeros on the enlarged rectangle Re s≥a+2e. The argument needs only the Euler-product upper boundary 1 and allows a zero on Re s=1.

On each disk centered at 2+it and lying inside the rectangle, the Euler product gives a uniform lower and upper bound at the center. Borel–Carathéodory and the three-circles theorem, using the fixed-field polynomial strip bound, give `|L|+|1/L|≪U^η(1+T₁)^A` on the smaller disk for every η>0. The fixed S and row-prime deleted products, with radical O(U), cost another U^η in positive real parts; on Re s≥−6e their upper bound is U^(6e+η). The primitive functional equation and fixed complex gamma types give the reflected bound `≪U^(a−1/2+12e+η)(1+T₁)^A`. See [the buffered-detector note](../2026-10-29-fixed-type-buffered-detector.md) for the source-qualified disk and deletion calculation. Conjugate presentations are included in the same buffer.

For centrally normalized smooth annular inverse and plain blocks, truncated Mellin shifts inside that buffer therefore give, for bounded nonnegative r,m,

    |M_r|² ≪ U^((2a−1)r+η),
    |S_m|² ≪ U^((2a−1) min(m,1−m)+η),                 (2)

provided τ is chosen after the finite height order. The remaining vertical tails stay on absolute lines; horizontal joins stay inside the buffer for reciprocal factors. Their external smooth-test orders can be chosen after τ, without increasing the internal moment-profile order. The functional equation supplies the second, reflected plain bound; the first comes from the right shift. These are the fixed-field analogues of OpenAI Lemma 8.2, with the conductor upper bound U used only once.

Now choose t=1 and D*=U. For a selected zero ρ in the bin, form a smoothly truncated inverse `C(ρ+z)` of length D* and integrate `Y*^z Γ(z)L(ρ+z)C(ρ+z)` on the line Re z=2. Its residue at z=0 vanishes because L(ρ)=0. Choose **Y*=U^B**, with B a sufficiently large fixed number depending on K, the fixed infinity type and the global strip-growth exponent. Moving to Re z=−1/4 then makes the new integral o(1); the primitive character is entire and all deleted factors are controlled there. This choice replaces the source's field-specific `U^20` and permits terminal block lengths in the fixed range [0,B+1].

Expanding on the absolute line, the Dirichlet convolution of the truncated Möbius inverse with L cancels every nonunit ideal of norm at most D*, leaving a unit contribution 1+o(1). The remaining tail therefore has size at least a positive constant. Apply a terminal cutoff above U^(B+1), partition both ideal variables dyadically, and separate the common product profile by logarithmic Fourier inversion. The fixed number of profile derivatives gives rapid Fourier tails; after choosing τ, discard frequencies outside a fixed share of T₁. Consequently, for one dyadic pair D=U^r,N=U^m and one common presentation and norm-twist height,

    r ≤ 1+O(1/log U),   r+m ≥ 1−O(1/log U),
    |M_r S_m|² ≫ U^((2a−1)(r+m)−η).                     (3)

The two witnesses use the same zero and the same separated frequency. The proof does not replace their joint product by two independently selected zeros.

Compare (3) with (2). Since 2a−1≥2σ₀−1−2e>0, m≤1/2+O(η), and hence r≥1/2−O(η). Dividing the product lower bound by the plain upper bound gives the inverse lower bound in (1), after reducing the preliminary η,e relative to ε. The finite presentation and dyadic groupings, common row-independent profiles, and Sobolev parameter step are as stated. □

## Review gates

The Gamma integral uses the simple pole of `Γ(z)` at zero; there is no extra division by z. Independent review should verify the fixed-type analytic bounds, all deleted factors, and the Sobolev parameter interval before the lemma is used as more than a proposed transfer. The lemma supplies no arithmetic large-sieve estimate by itself.

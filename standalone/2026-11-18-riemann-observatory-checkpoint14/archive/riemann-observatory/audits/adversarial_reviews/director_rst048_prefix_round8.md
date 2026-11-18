# Director adjudication: fixed logarithmic prefix, RST048 v2 Theorem 5

Date: 2026-11-17. Source credit: bramble_trace, PAPER-RST048 v2, Theorem 5, (79)–(89), and PAPER-RST047 v1 §§2–6. Both exact primary downloads and metadata are pinned. I read RST048 v2 in full and now also all of RST047 v1 §§1–8 and its references, including the causal-filter section. RST047 is therefore a complete substantive Level 1 reading; its whole proof has not received a Level 2/3 audit. The prior RST048 main-theorem adjudication and its fixed-Laurent localization qualification remain in force.

Accepted: for every fixed 0<b<1, under RH, the source fixed-prefix optimum has scaled squared limit

    C(b)=Σ_(distinct nontrivial ρ) c_(mρ)(b)/|ρ|²,
    c_m(b)=m²b+v* M^(-1)v,
    M_ij=(1−b^(i+j+1))/(i+j+1),
    v_j=−δ_(j0)+m b^(j+1)/(j+1),   0≤i,j<m.

The input A(s)=Σ_(n≤N) a_n n^(−s) is required to have a_n=μ(n)(1−log n/log N) for n≤N^b, including n=1. The unrestricted cost is ||1−ζA||_*². The anchored cost is ||1−ζ(A−A(1))||_*² for the same prefix-constrained input A. One must not impose that prefix on the coefficients of A−A(1). The tail coefficients are arbitrary complex numbers. N tends to infinity with b fixed. No moving-b uniform theorem, effective rate, prescribed full array, or RH conclusion is asserted. Source Theorem 6 (finite off-line extensions) remains unverified.

Independent complete reviews: audits/rstation48_fixed_prefix_lower_skeptic62.md and audits/adversarial_reviews/witness62_rstation48_theorem5.md. I independently reconstructed the following interfaces from the original texts rather than accepting the finite matrix calculation as an arithmetic proof.

## 1. Compact tests really control arbitrary suffix coefficients

For u in the first N integer generator span, finite Möbius inversion of the piecewise-constant jumps gives a coefficient ℓ1 bound N√(4N+1)||u||. This applies to a candidate with bounded residual, whose u has bounded norm. It does not assume an orthogonal affine projection or individually bounded coefficients.

Use k=ceil(log N), scale A=N, outer cutoff R=ceil(4N log N), and χ_k(z)=e^(−z)Σ_(j<k) z^j/j!, B_k(z)=e^(−z)z^k/Γ(k). The compact test uses 1−χ_k−B_k/s. Its zero Mellin moment eliminates the periodic means. The nonzero Fourier transform is the exact Pochhammer tail in RST047, not an estimate obtained by an unjustified sharp cutoff. For integer frequencies |ω|≥2π, its modulus is bounded by C k^(−σ)|ω|^σ(1+|ωN|²)^(−k/2). Bounded Fejér means justify the Fourier pairing before the absolutely convergent bound is taken.

After summing generators with the coefficient bound, the Fourier exponent is 3/2−σ−(1/2)log(1+4π²), negative near σ=1/2. The physical-cutoff gamma-tail exponent is 3/2−σ−(3−log4), also negative there. The same bounds hold analytically on fixed discs about each selected zero, so Cauchy estimates justify each fixed derivative jet. The ζ factor annihilates exactly the derivative indices below multiplicity. Thus the source total compact moments tend to δ_(j0)/ρ for every bounded-residual candidate sequence, with no hidden suffix-coefficient bound.

The compact-test Gram, divided by log N, tends to the confluent Hilbert blocks. The gamma bump has squared mass O(√log N); mixed terms are o(log N). The logarithmic-length O(loglog N) outer physical interval is also negligible after division by log N. These checks are essential for the arbitrary-coefficient lower bound.

## 2. Head moments, anchor and split projection

Set X=N^b and L=log N. For x≤X the exact divisor identity gives Σ a_n floor(x/n)=1+ψ(x)/L. The anchored residual therefore satisfies L e(x)=d_N floor x + floor x−ψ(x), where d_N=L A(1)−1. Under RH the integrated explicit formula

    J(X)=∫_1^X (x−ψ(x))/x dx
        =Σ_ρ mρ (X^ρ−1)/ρ²+O(log X)

is absolutely summable and O(√X). It can be integrated by parts against fixed powers; one must not substitute a conditionally convergent pointwise zero sum. Pairing with the drift gives |d_N|√X=O(√L), hence A(1)=O(1/L). Replacing floor x by x adds only the bounded term floor x−x in this integrated estimate; the exact residual identity retains floor x. The same-zero term supplies mρ L b^(j+1)/[ρ(j+1)], while off-zero terms are bounded by an absolutely summable expression involving 1/(|λ||λ−ρ|) for each fixed ρ. No uniform growing-gap bound is claimed.

For the unrestricted residual, the head is A(1)x−ψ(x)/L. Pair it directly with x to control A(1) first, then compare to the anchored residual. Their extended residuals differ by A(1){x}, of norm O(1/L). This order avoids a circular use of anchored estimates. The difference of squared costs is o(1/L) for bounded scaled cost.

The head Gram tends to bL for the single power at each zero, and its pairing is mρ b/ρ. Subtracting the head moments from the total compact jets gives the tail target −v/ρ, with tail Gram L M. Head and tail have disjoint support. Projection gives the cost mρ²b+v* M^(-1)v, divided by |ρ|². First select finitely many distinct zeros, take the N liminf, then exhaust the zeros. This is why a finite algebraic cost formula alone would not establish the theorem.

## 3. Integer upper construction preserves the prefix

For fixed b the delayed correction begins strictly after N^b. The mesh and contour parameters may depend on b. The source B_b=72((1+b)/(1−b))², a sufficiently small D, δ≤b/1000, H=N^(b/10), K=N^(3b/10) give strictly negative high, low and anchor exponents.

For each fixed zero, the optimal profile has its m-th derivative fixed to −m on the head and a polynomial projection on the tail. It need not be globally of the special form u^(m−1)q(u) in the earlier lemma. The correct arithmetic realization is the source direct bounded-variation quadrature (84) on [N^b,N]. Its error is O_(b,m)(L^(m−1)(1+|t|)N^(−b)); splitting at |t|=N^(b/2) yields negative squared exponents −5b/4 and −b/4, and the anchor costs O_(b,m)(L^(m−1)N^(−b/2)). Thus it is an actual ordinary integer polynomial with the original prefix unchanged. The optimal local cost is at most that of the older admissible profile, so the previous summable cluster-tail domination remains valid. Fixed finite replacements come first, N second, and exhaustion last; no growing inverse Gram is used.

Together these arguments establish the two limits stated above, with the previously recorded source qualification. For any b>0, c_1=1 and c_m>m² for m≥2. Consequently, under RH, C(b)=C(0) at even one fixed positive b is equivalent to all zeros being simple. This does not prove simplicity.

The next arithmetic target is a quantified endpoint estimate as b approaches 1. The current fixed-b proof does not provide it. Theorem 6 must have its separate off-line normalization, projection and uniformity audited before adoption.

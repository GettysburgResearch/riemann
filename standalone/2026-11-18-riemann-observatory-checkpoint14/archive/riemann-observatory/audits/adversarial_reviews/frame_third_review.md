# Independent third review: a weighted frame estimate for the E2 remainder

**Review date:** 2026-11-17. **Reviewer:** corpus agent, reassigned independently; no proposer proof was read. **Outcome:** the proposed E2 bound is valid under the explicitly stated uniform window assumptions and measurability of the weight. This is a self-contained auxiliary estimate, not validation of Proposition 5.2, the paper's other estimates, or its principal theorem. No literature novelty is asserted.

## Source and inspected scope

The inspected source is the locally supplied PDF `sources/analytic/2608.13637.pdf`, identified by the parent task as arXiv:2608.13637v2, printed pp. 8–9, Proposition 5.2, specifically the definition and bound for E2. Fourier normalization was checked in §1.7, printed p. 3; window conditions in §2.2, printed p. 4; weight bounds in (5.7), printed p. 8. This review does not independently establish the bibliographic author identity, the version history, or the status of any later corrections. Source URL: https://arxiv.org/abs/2608.13637v2 . PDF SHA-256: `6de3b156342e7b4a802c34f8ef40432567e9dabe006938da04233f19fc4ef444`.

The printed argument bounds E2 by a quantity of order `L^3 B^2 l log L`. Here `l=L`, and B² is of order T. Dividing this printed bound alone by the square of the matrix normalization, of order L⁴, gives an error of order `T log L`; it does not give the claimed `N log L/L²`, of order `T log L/L`. The estimate proved below supplies the missing saving for E2. E1 and every other part require their own checks.

## Precise auxiliary statement

Let T tend to infinity, L=log(T/(2π)), h=2π/L, d=floor(T/h), I=[T,2T], and αk=T+kh for 0≤k<d. Let φ be a real even function in C²(R), supported in [-L/2,L/2], with 0≤φ≤1 and

    ||φ'||₁ ≤ C1,       ||φ''||₁ ≤ C2,

where C1,C2 are independent of T. Set

    f(r)=hatφ(r)=∫R φ(x) exp(-irx) dx,
    v(τ)=(f(τ-αk))_{0≤k<d}.

Let ν be real and measurable and B≥1, with

    |ν(τ)| ≤ B + log⁺(|τ|/(4T))    (τ∈R).

This already implies |ν|≤B on |τ|≤4T. Define the positive semidefinite matrix and scalar

    H = ∫R |ν(τ)| v(τ)v(τ)* dτ,
    J = ∫R\I |ν(τ)| ||v(τ)||² dτ.

Then

    ||H||op = O(BL + L/T²),
    J = O(BL log L + L/T²).

Consequently, with K(τ,τ′)=v(τ)ᵀv(τ′), the real even window ensures K is real, and

    |∫(I×I)ᶜ K(τ,τ′)² ν(τ)ν(τ′) dτ dτ′|
       ≤ 2 ||H||op J
       = O(B² L² log L).

All constants depend only on C1,C2 and an absolute lower threshold for T. In particular B asymptotic to sqrt(T) satisfies these estimates. The displayed integrals are absolutely convergent by the bounds proved below.

## 1. Exact frame upper bound

For any c∈Cᵈ, Plancherel with the source normalization gives

    ∫R |∑k ck f(τ-αk)|² dτ
       = 2π ∫[-L/2,L/2] |φ(x)|² |∑k ck exp(iαk x)|² dx
       ≤ 2π ∫[-L/2,L/2] |∑k ck exp(2πikx/L)|² dx
       = 2πL ∑k |ck|².

The common factor exp(iTx) has modulus one, and the last identity is elementary orthogonality on an interval of exactly length L. No infinite-frame identity, Poisson summation, or interchange of a conditionally convergent series is needed. Therefore

    H0 := ∫R v(τ)v(τ)* dτ  satisfies  H0 ≤ 2πL Id.

Complex conjugating coefficients if necessary gives the same statement with the chosen column-vector convention. Since f is real here, no convention affects the estimate.

## 2. The logarithmic far-tail weight costs O(L/T²)

Compact C² support gives vanishing boundary terms in integrations by parts, hence

    |f(r)| ≤ min(L, C1/|r|, C2/|r|²)   for r≠0.

For every αk∈[T,2T] and |τ|>4T,

    |τ-αk| ≥ |τ|/2,
    ||v(τ)||² ≤ 16 C2² d |τ|⁻⁴.

Put w(τ)=log⁺(|τ|/(4T)). Direct integration gives

    ∫|τ|>4T log(|τ|/(4T)) |τ|⁻⁴ dτ
       = 1/(288 T³),

because ∫1∞ (log u)u⁻⁴ du=1/9. Thus

    tr Hw := ∫R w(τ)||v(τ)||² dτ ≤ C2² d/(18T³)
             = O(L/T²).

Hw is positive semidefinite, so ||Hw||op≤tr Hw. The weight inequality yields

    0≤H≤B H0+Hw,
    ||H||op≤2πBL+O(L/T²).

This step genuinely uses the second derivative estimate. Bounding the weight by its global supremum would be invalid, since that supremum is infinite.

## 3. Endpoint leakage has only a log L loss

For s≥0 define Q(s)=∫s∞ |f(r)|² dr. Reality and evenness of φ imply f is real and even, and Plancherel gives

    Q(0)=π||φ||²₂ ≤ πL.

For s>0, integration of the preceding pointwise bounds gives simultaneously

    Q(s) ≤ min(πL, C1²/s, C2²/(3s³)).

For the left endpoint, αk-T=kh. For the right endpoint write T/h=d+θ, 0≤θ<1. Then

    2T-αk = h(d+θ-k) ≥ h(d-k).

In particular the last included frequency is at least h from the right endpoint; the left endpoint includes α0=T and must be treated separately. Since Q is decreasing,

    J0 := ∫R\I ||v(τ)||² dτ
       = ∑k [Q(kh)+Q(2T-αk)]
       ≤ Q(0)+2∑j≥1 Q(jh).

For h≤1, put M=ceil(1/h). The first M terms are bounded by

    ∑1≤j≤M Q(jh) ≤ (C1²/h)∑1≤j≤M 1/j = O(L log L).

The remaining terms are bounded by

    ∑j>M Q(jh) ≤ (C2²/(3h³)) ∑j>M j⁻³
                  ≤ C2²/(6h³ M²) = O(L).

Therefore J0=O(L log L). There is **no log T factor**: the harmonic estimate is used only until distance jh reaches order 1, after which the second derivative gives a summable cubic tail. The number d≈TL of frequencies never enters this logarithm.

Finally

    J ≤ B J0 + ∫R w(τ)||v(τ)||² dτ
      = O(BL log L + L/T²).

## 4. The E2 matrix inequality

The complement of I×I is contained in ((R\I)×R)∪(R×(R\I)). Its nonnegative absolute-value integral is therefore at most twice that over the first set. Tonelli is legitimate, and subsequent finiteness follows from the preceding estimates. For fixed τ,

    ∫R |K(τ,τ′)|² |ν(τ′)| dτ′
      = v(τ)* H v(τ)
      ≤ ||H||op ||v(τ)||².

Consequently

    |E2| ≤ 2∫R\I |ν(τ)| v(τ)*H v(τ) dτ
          ≤ 2||H||op J
          = O(B²L² log L).

Absolute values are essential when ν changes sign. The estimate proves a bound for |E2|, stronger and less ambiguous than an unsigned upper bound.

## Adversarial checks and limitations

- The endpoint α0=T contributes O(L) and was retained. It cannot be discarded using a positive-distance bound.
- The floor in d places all included frequencies strictly below 2T and introduces no short-spacing issue; θ only increases the right-endpoint distance.
- Both derivative norms must be uniform in T. A C² claim without those uniform bounds would not imply the stated asymptotic constant.
- “C² supported in the interval” must mean global C² with compact support. A merely C² interior function abruptly extended by zero need not admit the integration-by-parts estimates.
- ν must be measurable for the integrals to be defined. This is an implicit definition-level condition, satisfied by the source's explicit νX.
- Evenness and reality make the source's unconjugated square compatible with the PSD matrix estimate. For a general complex window one must use the conjugated kernel and |K|² instead.
- No numerical evidence is needed: the estimate follows from finite-dimensional orthogonality, Plancherel, positive semidefinite order and absolutely convergent integrals.
- The bound repairs E2 only. A complete audit must separately verify E1, the explicit-formula applicability, the definition of the matrix, all subsequent evaluations, and the final theorem deductions.

**Classification:** independently checked with no issue found in this proposed E2 repair, under the stated assumptions. The source's printed E2 estimate alone is insufficient for its claimed normalization, but this review supplies a valid stronger auxiliary estimate. This is not a verified error in the principal theorem.

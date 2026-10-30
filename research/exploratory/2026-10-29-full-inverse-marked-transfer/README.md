# A marked full-inverse moment that would imply RH for the base zeta function

**Status.** An elementary random-phase transfer, combined with the [full-inverse spectral identity](../2026-10-29-cubic-full-inverse-mean/README.md) and its stated fixed-field character-sum and reciprocity inputs. It does not prove the marked moment, RH, or a new zero-free region. The implication below assumes uniformity over all bounded prime-slot coefficients; it does not apply automatically to a prescribed fixed physical phase profile.

Let K=Q(√−3), fix the bad set S and the principal ray sector and nonnegative row weight V from the cited cubic note. Let g run over its good squarefree rows of norm ≍X. Let W be the one fixed nonnegative C∞ annular inverse weight constructed there, whose Mellin transform has no zeros in Re s>0. Let `M_g(X^r)` be the centrally normalized smooth Dirichlet polynomial for the **full** inverse `1/ζ_(L_g)`, with its fixed S Euler deletions, as defined in that note. Fix `r>0` and `z>0`, let `P=X^z`, and choose a fixed nonnegative smooth annular prime profile U positive on a smaller annulus. For arbitrary complex phases `a_p` with `|a_p|≤1`, define

    Q_g(P;a)=P^(−1/2) Σ_{p good prime} a_p U(Np/P) χ_g(p),

retaining the original zero mask at p|g. Then uniformly in g in the row support,

    E_a |Q_g(P;a)|² ≍ 1/log P,                                  (1)

where the a_p are independent uniform unit phases. Expanding the square, mixed terms vanish and the diagonal is

    P^(−1) Σ_p |U(Np/P)|² 1_{p∤g}.

The fixed-field prime ideal theorem counts ≍P/log P supported primes; since `Ng≪X`, at most `O_z(1)` slot primes divide g. This proves (1) after X is large. Fixed finite ray restrictions are permitted when the slot primes retain positive density.

Consequently, if for every ε>0 one had the **uniform** estimate

    Σ_g V(Ng/X) |M_g(X^r) Q_g(P;a)|²
       ≪_{ε,r,z,V,W,U} X^{1+ε}                                  (2)

for all bounded coefficient vectors a, then averaging (2) over independent phases and using (1) gives

    Σ_g V(Ng/X) |M_g(X^r)|² ≪_ε X^{1+ε}.                      (3)

The logarithm in (1) is absorbed by shrinking the preliminary ε. The implied constant in (2) must be independent of the actual phases and of X; an estimate for only one chosen phase vector cannot be averaged in this way. All row, prime and Euler masks remain in place. A polynomial-height parameter may be included only when (2) is uniform over the chosen permitted value; setting it to zero suffices if zero is allowed.

The lower-bound direction of the cubic full-inverse mean proves, under its stated standard finite-ring character-sum, reciprocity and fixed-field analytic inputs, that (3) for every ε>0 and **one** fixed `0<r<1/2` implies RH for ζ_K. Indeed a zero with β>1/2 gives a mean Ω of `X^{r(β−1/2−η)}` and the averaging error is negligible for r<1/2. No cubic sieve is needed for this direction. Thus (2), for any fixed z>0 and one such r, would imply RH for ζ_K. This is an obstruction to a proposed coefficient-uniform marked estimate: it does not disprove such an estimate, produce a zero-free half-plane, or imply anything about a narrower fixed-phase prime slot without a separate argument.

## Direct implication for the Riemann zeta function

The same averaging argument applies to any row family with unit-modulus prime characters away from the original zero mask. In particular, use the positive odd squarefree integers d≡1 mod4 and the full inverse polynomials `M_d(X^r)` in [the quadratic growth identity](../2026-10-29-riemann-quadratic-inverse-growth/README.md). For rational primes p in a fixed annulus P=X^z define `Q_d(P;a)` with the same P^(−1/2) normalization and χ_d(p). Each d in the weighted family has only O_z(1) such prime divisors, so the analogue of (1) holds.

Suppose, for fixed `0<r<1/2`, `z>0` and `κ≥0`, that for every ε>0 the same coefficient-uniform marked sum is `≪X^{1+κ+ε}`. Averaging gives the unmarked full-inverse moment with the same exponent, up to an absorbed logarithm. The cited exact growth identity then forces

    Θ_ζ := sup{Re ρ : ζ(ρ)=0, 0<Re ρ<1}
          ≤ 1/2 + κ/(2r).                                     (4)

In particular, κ=0 would imply RH for the Riemann zeta function itself. The implication needs only the lower-mean direction of the quadratic note, using its stated reciprocity, Poisson, prime-count and reciprocal-ζ inputs; it does not require the quadratic large sieve used for the opposite direction of the full growth identity. It does not prove the marked hypothesis. For finitely many disjoint fixed-width prime slots, independent phase vectors give a product of `≍1/log P_i` in the diagonal expectation, and the same implication holds after absorbing finitely many logarithms. It still requires a constant uniform over all the allowed phase vectors and their source masks.

**Independent review.** High_match checked the row-uniform random-phase diagonal, the cubic lower-mean range r<1/2, the quadratic growth consequence, and the coefficient-uniform scope; no defect was found under the cited inputs.

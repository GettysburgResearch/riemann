# Exact separation of the moving Gaussian slot scale

**Status:** Elementary profile lemma, proposed for independent review. It isolates one literal rescaling in Hu's variable-length low-side problem; it is not a proof of his reflection estimate, the complete low bound, or a new zero-free region.

**Source:** In Hu, [*A seven-eighths zero-free half-plane for unitary Weil L-functions*](https://hexagonmath.org/2610.00216v1), equations (6.1) and (6.9), the marked completed row contains `P_G(N(c n^3)/(Z N(p_{J^c})))`, with

    P_G(t) = (2 sqrt(pi))^(-1) exp(-(log t)^2/4).

For fixed `J` the surviving marked slots are those indexed by `I=J^c`. Their windows force each `N(p_i)/P_i` into a fixed compact subinterval of `(0,infinity)`, with `P_i=Z^ell_i`. The target and Gauss factors are kept in the original coefficients; the calculation below touches only this Gaussian scale.

## Lemma

Fix a finite set `I`, fixed compact windows `W_i` on `(0,infinity)`, and a nonnegative smooth function `phi` supported in `[-2,2]` such that `sum_{j in Z} phi(x-j)=1`. Set `P=product_i P_i` and, for a completed-index ideal of norm `A>0`, let

    x = log(A/(ZP)),        y_i = log(N(p_i)/P_i).

Choose smooth compact cutoffs `chi_i` equal to 1 on the logarithmic supports of `W_i`. The `j`th annular contribution to the exact Gaussian satisfies

    phi(x-j) P_G(exp(x-sum_i y_i))
       = integral a_j(t,xi) Phi(x-j) exp(i t x) product_i exp(i xi_i y_i) dt dxi

on all physical slot supports, where `Phi` is any fixed compact smooth function equal to 1 on the support of `phi`. For every fixed `m>=0`, the densities can be chosen so that

    integral (1+|t|+sum_i |xi_i|)^m |a_j(t,xi)| dt dxi
       <= C_m exp(-c j^2)

for some fixed `c>0` and constants depending on `I`, the fixed windows, `phi` and `m`, but not on `Z`, the prime tuples, or `j`.

## Proof

For `x'=x-j`, define the compactly supported smooth function

    F_j(x',y) = phi(x') product_i chi_i(y_i)
                  P_G(exp(j+x'-sum_i y_i)).

On this fixed box the quantity `x'-sum_i y_i` is bounded. Every derivative of `F_j` is a finite sum of a polynomial in `j+x'-sum y_i` times `exp(-(j+x'-sum y_i)^2/4)` and bounded derivatives of the cutoffs. For each fixed derivative order its absolute value is therefore `O(exp(-c j^2))`, after reducing `c>0` and absorbing finitely many small `j` into the constant.

Fourier inversion gives an absolutely integrable transform. Applying sufficiently many powers of `1-Delta` before taking the transform yields the displayed weighted `L^1` bound. Replacing `x'` by `x-j` changes the density only by the unit phase `exp(-i t j)`. Since the integral equals a function supported where `phi(x-j)` is nonzero, multiplying it by `Phi(x-j)` leaves it unchanged while retaining an explicit annular row profile. On the slot supports every `chi_i=1`, proving the identity. The integral is independent of the ideal and prime tuples except through the displayed phases.

The completed-index factor is `(A/(ZP))^(it)` and each slot factor is `(N(p_i)/P_i)^(i xi_i)`. All have modulus one. Thus, if the original completed-row coefficient and the separate slot coefficients have the product form required by a row-energy theorem, this separation preserves that product form; it also leaves every mark, collision and zero-extension indicator exactly where it was. The fixed unitary factors `psi(p_i)` in (6.9) merely multiply their own slot coefficients. A Fourier phase changes fixed window seminorms at most polynomially in its frequency, which is integrable against the displayed weighted density.

## Dyadic scales and the remaining interface

On the `j`th annulus, the completed norm has scale

    A ~ Z P exp(j),   log_Z(A) = 1 + sum_(i in I) ell_i + j/log Z + O(1/log Z).

For `I=J^c`, `sum_(i in I) ell_i = ell-d`. Fix any `eta>0`; retaining `|j|<=eta log Z` makes the offset in Hu's completed length `theta_N` at most `eta+O(1/log Z)`. Outside that range, the Gaussian density is super-polynomially small in Z.

The completed-index part admits an elementary absolute majorant. For any `X>=1`, fixed-field ideal counting and partial summation give

    sum_(N(c) N(n)^3 <= X) (N(c) N(n))^(-1/2)
      << X^(1/2) sum_n N(n)^(-2) << X^(1/2).

The first sum may be enlarged from squarefree `c` to all ideals; the second converges. On Hu's physical row, the zero-extended residue symbols and marks have modulus at most one, the unitary target has modulus one, and the cited good-prime identity `gamma_2(p)^3=-Lambda(p)` gives `|gamma_2(c)|=1` for squarefree exterior `c`. Thus, before applying any cancellation, one completed row on annulus `j` has size at most a fixed power of `Z`, times `exp(|j|/2-cj^2)`, after summing the fixed finite number of prime slots using the crude count `#{p:N(p)<=x} <<_K x`. This bound is uniform in the additive row.

The remaining additive weights in Hu (6.3) also have a polynomial majorant for the proposed positive scales. To see it, write `X',Y'>=1` for the actual rescaled quantities and use Hu's positive norm section, whose finite components are 1 and whose complex components are `T^(1/[K:Q])`. A compact set of representatives for `T0/Gamma` has uniformly bounded finite valuations and archimedean components. Since `W0` has compact support in `K_S^times`, the nonzero terms in `W0(m/(t0 ell_(N(b)X')))` lie in a fixed fractional `O_K`-ideal and have archimedean absolute values `O((N(b) X')^(1/[K:Q]))`. The fixed Minkowski lattice therefore gives

    #{m in O_(K,S): W0(m/(t0 ell_(N(b)X'))) != 0}
       <<_K,S,W0 1 + N(b) X',

uniformly in the compact representative `t0`. The finite-place denominator bound is independent of `N(b)X'`, because the section's finite components are 1. On the fixed support of `W1`, `N(b) ~ Y'`; there are `O_K(Y')` exterior ideals there. The elementary bound `|g_b(-m)| <= N(b)` and the two displayed square-root factors in (6.3) therefore bound the absolute additive part, uniformly in `t0`, by

    O(X'^(-1/2) Y'^(3/2) (1+X'Y')).

The Haar measure of the compact quotient is finite. For the variable-geometry hypotheses of the linked low-side note, `X',Y'` remain between fixed positive powers of `Z` on every subset, so this is a fixed power of `Z`. The rescaled-slot prefactors and number of tuples are also polynomial for a fixed finite slot system. Consequently the full contribution of `|j|>eta log Z` is `O_A(Z^(-A))` for every fixed `A>0`. This absolute argument imports only the stated compact quotient, norm section and the fixed finite-sector calibration; it does not establish Hu's reflection identity or the required retained-dyad bounds.

For each fixed tuple of rescaled slots indexed by `J`, their product is absent from the surviving mark. Hu's additive-side estimate can then be applied at the actual scales `X'=X/N(p_J)` and `Y'=Y/N(p_J)`; the marked-slot separation above does not introduce dependence on the additive row into a slot coefficient. Bounds for those scales, including the normalizer and their uniform profile seminorms, remain separate source interfaces.

**What was checked:** Exact Gaussian normalization, Fourier construction, weighted decay, the scale identity, a completed-index ideal-count majorant, and the additive lattice/weight bound under Hu's stated compact quotient and norm-section calibration. An independent review checked the Gaussian tail argument. No finite Gauss sum, source calibration, unit-sector assertion, or Hu analytic theorem was independently replayed.

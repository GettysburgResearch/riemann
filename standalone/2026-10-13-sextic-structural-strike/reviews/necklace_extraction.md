# Mathematical review of the finite-horizon necklace representation

## 1. Frozen object and verdict

**Reviewed manuscript:**
`standalone/2026-10-13-sextic-structural-strike/HORIZON_NECKLACE_FACTORIZATION.md`,
20,252 bytes, SHA-256

`a6aa7ab8925eac3f1f514b6e4138baa87735e3902fa3c5a78679480c7cf925ab`.

**Reviewer:** extraction/resonance agent. I did not develop or write the
necklace factorization or its horizon application. I authored the
short-factor non-smallness and first-order Euler resonance components
that motivate this repair, and contributed to the early collision
analysis. This review is therefore independent of the proposed repair's
derivation, but not of every motivating result in the packet. It uses
the same underlying model as the other agents.

**Verdict:** the formal factorization, absolute coefficient convergence,
exact horizon transport and polynomial bound pass this reconstruction
at the stated hash. They hold for each finite slot number and each
finite degree \(J\), under the strict real-part condition displayed in
the manuscript. No load-bearing gap remains after the two corrections
described below. The statements about the full moment remain
conditional, as they should.

During review I identified two scope issues in earlier versions:

- The element-row bound with a factor \(H\) is specific to the
  two-dimensional Eisenstein lattice under the scaling
  \(u/\sqrt H\). The initial general-field wording would not have
  justified that factor. The final manuscript explicitly restricts all
  such row traces to the Eisenstein field, while retaining arbitrary
  fixed fields for the ideal-coefficient statements.
- A same-side pair has the cubic power of the sextic symbol together
  with the fixed \(\nu^2\) character. The complete product need not be
  cubic. The final Section 6 now states this exactly; the defining
  coefficient formula already retained that datum.

Both corrections were checked in a complete read of the final file.
No author file was edited by this reviewer.

## 2. Primary and repository source checks

I directly opened Pieter Moree,
[*The formal series Witt transform*, arXiv:math/0311194v2](https://arxiv.org/html/math/0311194v2),
Section 2. Its equations (1)--(3) and ensuing product identity give the
same primitive cyclic-word counts and multivariate product as the new
manuscript. The classical attribution is accurate. The free-Lie-algebra
interpretation is a connection, not an unmentioned analytic premise.

I also checked the preserved #911 source at commit
`2f8b6a3898a722d0602a91dea73bac344a3bb7dd`:

- `PRIME_SLOT_CANCELLATION.md`, particularly P3--P6 and P13--P15;
- `SHORT_POLYNOMIAL_COLLISION_TRANSPORT.md`, the exact finite factors,
  short coefficients and complete norm-filtered identity.

The degree-two specialization of the new remainder is precisely the
source's rational P4 factor. The new application changes which finite
Euler factors are shortened and uses the actual individual column
horizons. It does not import analytic continuation of reciprocal
\(L\)-functions into a conjectural zero-free region.

I did not conduct a complete priority search of all historical
repository branches. The scope of this review is validity of the
proposed representation and its stated analytic bounds, not a claim of
novelty for the classical identity or uniqueness of this repair.

## 3. Formal identity: independent derivation

For a content vector \(\alpha\), let \(N_\alpha\) be its multinomial
word count and let \(p_\alpha\) count primitive cyclic words. A word
whose primitive period has content \(\alpha/d\) belongs to a cyclic
class with exactly \(|\alpha|/d\) distinct linear words. Thus

\[
N_\alpha=\sum_{d\mid\gcd\alpha}\frac{|\alpha|}{d}p_{\alpha/d}.
\]

Setting \(q_\alpha=|\alpha|p_\alpha\), this is the divisor relation
\(N_\alpha=\sum_{d\mid\gcd\alpha}q_{\alpha/d}\). Möbius inversion
gives exactly (2.1). This both proves the formula and explains why its
value is a nonnegative integer.

The coefficient of \(\mathbf z^\beta\) in
\(-\log(1-\sum z_i)\) is \(N_\beta/|\beta|\). In

\[
\sum_{\alpha\ne0}p_\alpha
     \sum_{d\geq1}\frac{\mathbf z^{d\alpha}}d
\]

the same coefficient is
\(\sum_{d\mid\gcd\beta}p_{\beta/d}/d\), which is equal by the
preceding word-count relation. Formal exponentiation yields (2.2).
Every coefficient calculation uses only finitely many contents and
divisors, so there is no hidden infinite regrouping at this stage.

For example, the weights of \(e_i\), \(e_i+e_j\), and
\(2e_i+e_j\) are one; the weight of three different letters is two.
The weight of a pure multiple \(m e_i\) vanishes for \(m>1\).
Therefore degree two extracts exactly the distinct-slot pairs, and the
first remaining cubic terms have the signs and multiplicities of P4.

The integrality matters operationally. The later expression uses
ordinary powers of finite Möbius polynomials. It never needs to select
a branch of a fractional power of a possibly vanishing polynomial.

## 4. Absolute coefficient convergence and normal convergence

Write the Taylor expansion of the rational remainder as

\[
R_J(\mathbf z)=1+\sum_{|\beta|\geq J+1}c_\beta\mathbf z^\beta.
\]

Every coordinate exponent is nonnegative, but the coefficients are
not asserted to be nonnegative. Keeping these two statements distinct
is necessary for the subsequent horizon proof and analytic majorant.

Here is an explicit majorant underlying Lemma 3.1. Fix any
\(0<\rho<1\). The finitely many denominator factors have no zeros
on the closed polydisk \(|z_i|\leq\rho\), so its supremum there is
a finite number \(M_{r,J,\rho}\). Multivariate Cauchy bounds give

\[
|c_\beta|\leq M_{r,J,\rho}\rho^{-|\beta|}.
\]

There are \(\binom{m+r-1}{r-1}\) multi-indices of total degree
\(m\). Consequently, for \(0\leq t\leq\rho/2\),

\[
\sum_{|\beta|\geq J+1}|c_\beta|t^{|\beta|}
\leq C_{r,J,\rho}t^{J+1}.
\]

This estimate uses the exact cancellation of all low-degree
coefficients before taking absolute values. A majorant obtained by
taking absolute values in the unexpanded numerator and denominator
would not have the needed starting degree.

At a large prime, take \(t=(Np)^{-\sigma_*}\). The local absolute
coefficient norm is then at most

\[
1+C_{r,J}(Np)^{-(J+1)\sigma_*}.
\]

Its product over primes converges under
\((J+1)\sigma_*>1\); bounding by the sum over all integral ideals
already suffices. At each of the finitely many remaining primes, the
same rational Taylor series is absolutely convergent at the actual
polyradii \((Np)^{-\sigma_i}<1\). The finite cost is uniform in all
character phases and their zeros.

Multiplying these local absolute majorants proves the full weighted
absolute sum of multivariate ideal coefficients in (3.5). Different
prime ideals, even those with equal norm, have different ideal
exponent labels. The argument does not merge them. Multiplication
by the slot phases decreases this universal majorant, and deleting
a prime removes a factor whose absolute coefficient norm is at least
one. Thus uniformity in arbitrary moving deletion masks follows as
stated.

For normal convergence, any compact subset of the allowed tube lies
inside a tube with a slightly smaller minimum real part still
strictly greater than \(1/(J+1)\). The majorant just proved is
summable on that larger tube and uniform on the original compact
set. The Weierstrass criterion applies to the ideal series and the
Euler product. A finite local numerator can vanish; no argument here
requires the resulting function to be nonzero or a logarithm of it
to exist globally.

The constants may depend on \(r,J\) and the fixed distance from the
convergence boundary. Nothing has been shown uniformly as \(J\)
tends to infinity. The manuscript correctly does not use such a
limit.

## 5. Why shortening every copy preserves every physical coefficient

The clean algebraic interpretation is a quotient by the monomials
outside the column rectangle. A tuple \((n_i)\) is outside the
rectangle when \(Nn_i>Y_i\) for at least one coordinate. Multiplying
such a tuple by any tuple of integral ideals keeps it outside.
Thus the omitted monomials form an ideal in the formal
multivariate ideal-series algebra. Projection onto the retained
coefficients is compatible with multiplication in this quotient.

For a retained necklace factor \(\alpha\), an ideal \(n\) in its
Euler expansion puts the ideal \(n^{\alpha_i}\) in column \(i\).
It can belong to the rectangle only when

\[
Nn\leq\min_{\alpha_i>0}Y_i^{1/\alpha_i}=X_\alpha.
\]

Any term deleted by the proposed cutoff is therefore zero in the
rectangle quotient. This statement remains true after multiplying
by every other retained factor and by the remainder: all of them
have only nonnegative coordinate exponents. No signed cancellation
can bring an oversized monomial back to a smaller norm.

The cutoff must be applied to each of the \(w_\alpha\) copies.
For example, when \(w_\alpha=2\), one cannot infer that the product
of two individually allowed ideals stays within every horizon.
The theorem makes no such assertion. It preserves the rectangle
coefficients of their product; the final column tests still remove
all oversized products.

The anisotropic power is also necessary. For
\(\alpha=2e_i+e_j\), the correct cutoff is
\(\min(Y_i^{1/2},Y_j)\). Using only the smaller of \(Y_i,Y_j\)
would not implement the same coefficient argument. The manuscript
uses the correct exponent in every degree.

There are two legitimate ways of handling the prime horizon. Starting
with \(Np\leq Y_*\) gives an exact finite rational identity. Every
ideal of norm at most \(X_\alpha\leq Y_*\) already has its prime
support in that set. Hence the shortened factor is exactly the stated
Möbius polynomial. Replacing the finite remainder by its all-prime
version then adds no rectangle coefficient: any nonconstant term at
a new prime with \(Np>Y_*\) already violates some horizon. This
settles the potentially delicate infinite-remainder step.

These statements are coefficientwise in individual ideals, and each
fixed coefficient has only finitely many factorizations. Analytic
convergence is not needed to define this formal equality. The
absolute convergence from Section 4 makes it usable on the stated
contours.

Literal nonunit zeros are preserved as well. Every participating
slot in \(\eta_\alpha\) has a positive exponent. If its value is
zero, the local product is zero. A net sextic exponent divisible by
six does not turn that zero into one. The later principal pair
polynomials therefore retain the original masks.

## 6. Mellin transport and uniform bounds

On an admissible contour the remainder's weighted coefficient sum
is finite, and each polynomial factor has finite support. Their
product therefore has an absolutely convergent multivariate ideal
series. The smooth Mellin transforms decay faster than any fixed
power in each independent frequency. Termwise inversion is justified
by the product of the absolute coefficient majorant and the Mellin
integrals.

For every term selected by the original tests,
\(Nn_i\leq bD/Nc_i=Y_i\). The rectangle theorem therefore returns
its exact source coefficient. If some proposed allocation has a
subunit horizon, it is absent from the eligible source allocation
set; Theorem 4.1 itself assumes \(Y_i\geq1\). No new nonempty
range is manufactured at that endpoint.

For \(\lambda=\alpha\cdot\boldsymbol\sigma>0\), elementary ideal
counting bounds a short factor by a constant times
\(B_\lambda(X_\alpha)\). This has exactly the three forms in (5.1),
including the logarithm at \(\lambda=1\). Multiplying the finitely
many such estimates and using the remainder bound proves (5.2).
It is uniform in all imaginary parts because no step depends on
their values.

The Eisenstein lattice has real dimension two. For a fixed Schwartz
test and \(H\geq1\), a standard annular lattice count gives
\(\sum_{u\ne0}|\Phi(u/\sqrt H)|\ll H\). Together with
\(|\omega_{\mathbf q}(u)|\leq1\), this proves the corrected
row-trace statement (5.3) and justifies its use inside the full Mellin
integral. An analogous general-field statement would need its own
embedding and scaling convention, which is outside the final scope.

Replacing each hard cutoff by a fixed smooth cutoff equal to one
through the horizon also preserves every rectangle coefficient.
All changed terms lie beyond \(X_\alpha\), hence vanish in the
same quotient. A fixed extension to \(2X_\alpha\) changes the
absolute bound by only a fixed factor. This does not require an
unproved cancellation estimate for arbitrary cutoff coefficients.

## 7. Critical-line specialization and remaining arithmetic demand

For \(J=2\), the only retained contents are \(e_i\) and
\(e_i+e_j\). At \(\sigma_i=1/2\), the corresponding real parts
are \(1/2\) and one. The all-prime remainder has absolutely
convergent coefficients because its first possible total degree is
three. Thus (6.2) follows with the individual factors

\[
\prod_iY_i^{1/2}\prod_{i<j}\log(2\min(Y_i,Y_j)).
\]

This is a uniform polynomial bound, so it rules out the particular
superpolynomial instability of the old unfiltered representations
for this new representation. It gives no square-root cancellation
in the original column coefficients.

At equal horizons, the short factors contribute \(D^k\) and the
Mellin scale factors contribute another \(D^k\). The displayed
absolute argument therefore gives only \(HD^{2k}\), as the
manuscript states. The signed estimate (7.1) remains a separate,
substantial open premise.

I checked its conditional incidence bookkeeping against P14--P15.
A bound uniform in every original allocation gives the scale weight

\[
\prod_i(D/Nc_i)^{1/2}
=D^k\prod_I(Nq_I)^{-|I|/2}.
\]

The size-two incidences have harmonic ideal sums, while the larger
incidences have absolutely summable weights. There are finitely many
incidence types for fixed \(k\), and the powers of logarithms can
be absorbed in an arbitrarily small input loss. Therefore the claimed
implication to the full moment is correct if (7.1) is supplied with
its stated uniformity. This review supplies no such estimate.

The warning about old frequency-tube bounds is necessary and correct:
equality after complete Mellin filtering does not preserve the value
of an individual partial frequency integral under a representation
change. The old tube suppression cannot be transferred merely from
the exact coefficient identity.

## 8. Final review boundary

The final version passes a direct mathematical reconstruction of
all finite-degree representation claims and their analytic
majorants. No finite computation was used as evidence for an
infinite theorem in this review. The result needs only the stated
classical combinatorial identity, elementary ideal counting and
smooth Mellin inversion; it does not need a prime ideal theorem,
theta foundation or zero-free assumption.

This verdict does not prove the open trace bound, a diagonal native
moment, a zero-free half-plane or RH. It also does not assert that
the new open trace target has no other obstruction. It establishes
that the exhibited low-degree Euler instabilities are absent from
an exact horizon-respecting representation whose full independent-
frequency integrand has the stated polynomial majorant.

# Independent review: source polarization and the four-node residual

Verdict: **PASS in the stated analytic scope** for exact science
`e5e43625b157ecc5f602532e16a1197679594824`, parent/preregistration
`a15673eb301cc49ae055dcb9a0253e6ff750f0f8`, authoring base
`8f01064df805624c045877655893c324a220975d`. This review does not prove RH,
does not promote the six finite panels to global positivity, and does not
turn the prime expansion into a sum of separately closable operators.

The reviewed proof blob is `888c1e4713cb79a2abd205b8380f6f5e3e679b82`.
Its fixture-bound normalized-LF SHA256 is
`b9b550fc3c8836f1f4ba2d24ebadba6fbb3adc0b420636afd6efc4e740578f71`.
The science payload seal is
`ea3acbb318e168993244d24ec1eb614f1abcdd45613f6644515e68d31d6c211a`.
I independently checked all 11 commit/path/blob/LF primitive bindings.
Root is reviewing the finite producer separately; my additional finite check
was an independent `Fraction` implementation of 243 four-node cells and did
not import the author producer.

## Analytic reconstruction

1. Starting with the full-line density `Phi=2 phi0`, the variables
   `s=a+b`, `d=a-b` and the Jacobian give the Volterra formula in SP3.
   Since `partial_a+partial_b=2 partial_s`, differentiation of the lower
   endpoint gives exactly

       (partial_a+partial_b) A = -(a+b) Phi(a) Phi(b).

   Evenness pays the half-plane `s<0`; the two derivatives agree and vanish
   at `s=0`, so there is no hidden delta mass. Fourier integration by parts
   then gives `i(v-z) Ahat` on the left and the Wick numerator on the right.
   This reproduces SP5 with no `2 pi` factor and with its displayed sign.
   The Gaussian calibration independently gives
   `A(a,b)=exp(-alpha(a^2+b^2))/(2 alpha)`.

2. The superexponential source bounds make `A` Hilbert--Schmidt and give all
   exponential moments used by upper-half-plane Fourier features. Thus the
   truncation, boundary-limit, Riemann-sum and Fourier-density steps really
   identify positivity of `A` on `L2` with finite-packet positivity of
   `B_X`; pointwise positivity of the integrand is never substituted for
   positive semidefiniteness.

3. On `L2(0,infinity)`, the exponential core is dense and linearly
   independent. In Hardy coordinates the complete adjoint identity is

       L(T_0^* h) = F Lh.

   An off-axis Xi zero becomes a zero of `Y` in `Re z>0` after reflection if
   necessary. Its logarithmic derivative has a simple pole, even for a
   multiple zero. The adjoint domain must therefore lie in the kernel of
   the nonzero bounded evaluation at that zero and cannot be dense. This
   proves `closable => RH` without assuming a zero is simple.

4. Under RH, the paired genus-zero logarithmic derivative converges locally
   uniformly and has positive real part in the right half-plane. The maximal
   Hardy multiplier `M_F` is closed. The Schur multipliers
   `(1+epsilon F)^(-1)` map arbitrary `H2` vectors into its domain, are
   contractive, converge weakly by bounded evaluation and then strongly by
   the displayed norm inequality. Hence the multiplier domain is dense and
   `L overline(T_0) L^-1=M_F^*`. The accretivity/closability implication is
   also paid directly by expanding the form at `g_n+zv`; it is not an
   unsupported general operator assertion. SP13 and the restriction SP14
   therefore establish precisely the claimed RH equivalences.

5. Logarithmic differentiation of the literal completed Xi expression at
   `s=x+1/2` gives both resolvents, the digamma term, and
   `-sum Lambda(n)n^(-x-1/2)` with the signs in SP15. The prime-power series
   converges only on each fixed finite exponential-core vector, as stated.
   The sequence `(x_n-1/2)e_(x_n)` independently confirms that the minus
   resolvent piece is nonclosable; no piecewise functional calculus follows.

## Four-node algebra and source scope

For distinct positive `t_i`, both displayed determinant factors are
homogeneous irreducible quadratics in the `p_i`. On the dense zero locus of
the first, `p(t)=c+d/(t+s)`, giving a rank-one plus rank-two matrix. For the
second, `tp(t)` is fractional-linear; partial fractions give a `c/t` term
of rank one and a pole term of rank at most two. The factors are coprime.
Comparison of the `p_1^2 p_2^2` coefficient supplies exactly the product of
all six `(x_i+x_j)^2` denominators. This establishes SP16 polynomially,
including degenerate `p` values by continuation.

Newton reduction yields SP17 with the stated sign. In the confluent limit,
`D_f` is `(f''/2)^2-f'f'''/6`. Row multilinearity after multiplying row
`i` by `x_iY_i` gives both signed source integrals in SP18 exactly. These
formulas expose a source sign burden; they do not solve it.

Finally, the bordered determinant and `M adj(M)=delta I` give
`c^T H c=delta det(H)` without dividing by `delta`. This correctly preserves
the singular-anchor boundary: at `delta=0` the quadratic charge can vanish
without detecting a negative four-node determinant. The fixed-spectator
Volterra coefficient has determinant `-(u-v)^2`; it blocks only a pointwise
positive one-spectator factorization, not a global or arithmetic one.

## Exact limits of acceptance

- The analytic RH equivalence is a characterization, not progress on paying
  its premise.
- The six strict native quadruples are finite controls only.
- No strict three-node anchor is imported from the repaired size-three PSD
  theorem.
- No self-adjoint realization, operator-norm Euler expansion, positive prime
  decomposition, global sign for both four-node factors, or novelty claim is
  obtained.

Within these boundaries I found no material mathematical gap.

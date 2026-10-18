# Attempt to use the new square-root phase estimate on the native source

Status: **analytic transfer attempt; the required adapter remains OPEN.**
This records the actual phases and the cost of a simple attempted
conversion. It does not import a positive zeta moment as a reciprocal
estimate and does not infer a zero-free region.

The external candidate is de Faveri--Pandey,
[*The sixth moment of the Riemann zeta function*, arXiv:2610.01035v1,
Corollary 1.4](https://arxiv.org/html/2610.01035v1#S1.SS2). It bounds large
values of sums with bounded individual coefficients and phase
`w[sqrt(n/N)+eta(n/N)^(3/2)]`, in its specified ranges
`N<=W<=N^(4/3)` and `|eta|<=cW/N^2`. The coefficient hypothesis is
essential. The native source does not presently have this phase.

## 1. Exact Fourier frequency at an R-dilate

Write R(v)=H_floor(v)-log(v)-gamma. For v>=1, the elementary uniform
harmonic-number expansion gives

    R(v)=[1/2-{v}]/v+O(v^(-2)).

Indeed H_m=log(m)+gamma+1/(2m)+O(m^-2), and Taylor expansion at
m=v-{v} proves the displayed formula uniformly, including integer v.
Away from the jumps, the sawtooth has its usual symmetric Fourier
expansion

    1/2-{v}=sum_(h!=0) e(hv)/(2 pi i h).

At integer v this Fourier series gives zero, whereas the right-continuous
sawtooth equals 1/2. A proof for the actual integer native cells must
therefore retain the exact divisibility correction or use an integrated
form with all jumps accounted for. It cannot silently identify these
two values.

For a dyadic product d~D, the oscillatory phase is consequently `h k/d`.
For the alternative one-dimensional square-product source it is
`h k/r^2`. Neither is the square-root phase in Corollary 1.4.

## 2. What stationary phase would do, and why the coefficients matter

For a smooth unweighted sum in d, Poisson summation introduces an
integral with phase

    f(x)=h k/x + ell x.

When h k and ell are positive its stationary point is
`x0=sqrt(h k/ell)` and `f(x0)=2sqrt(h k ell)`. This explains a possible
square-root connection. It does not justify Poisson summation with the
original rough signed coefficient left unchanged. Here that coefficient
is the actual old Mobius convolution, or the exact masked alpha vector.
It is not a smooth amplitude with bounded derivatives.

For comparison, take any coefficient vector |a_n|<=1 on exactly L
consecutive integer sites, and its normalized discrete Fourier transform

    a_n=sum_(j mod L) a_hat(j)e(jn/L),
    a_hat(j)=L^(-1)sum_n a_n e(-jn/L).

Parseval and Cauchy give

    sum_j |a_hat(j)|<=sqrt(L).

Thus expanding the rough coefficient into smooth exponential modes and
then summing their estimates by the triangle inequality can cost a full
factor sqrt(L). Bounded coefficients alone cannot improve this uniform
bound: for odd prime L, a_n=e(n^2/L) has all normalized Fourier
coefficients of magnitude L^(-1/2), by the elementary complete quadratic
Gauss-sum identity. The loss is therefore real for the generic class.
This is not a lower bound for the ACTUAL Mobius vector; it identifies
what an arithmetic-specific adapter must save.

There is a different stationary phase for square products. The phase
`h k/x^2+ell x` has stationary point `(2h k/ell)^(1/3)` and stationary
value

    3*2^(-2/3)*(h k)^(1/3)*ell^(2/3).

The first Poisson step is a cubic-root/power-two-thirds phase, rather
than the cited square-root class. The jump boundaries `r=sqrt(k/h)`
alone do not convert the complete weighted source into that class.

## 3. Exact completion interface still needed

A useful adapter must simultaneously retain the complete original
annular mask, divisibility jumps, all shared-prime coefficients and
frequency tails, and convert the actual signed vector with a total
resource cost smaller than the saving delivered in the legal parameter
range of the external estimate. Neither the formal stationary point nor
a generic Fourier decomposition accomplishes this.

The compact-flux compression in `rational/MASKED_COMPRESSION.md` is an
unconditional way of changing the geometric support with subpower error.
Its explicit reference weights retain the original signed alpha vector;
the apparent reference Mobius signs are compensated by those weights.
Calling them fresh independent oscillations would not be a valid phase
adapter. The full signed compressed amplitude, with a quantitative
contraction budget, remains the target of this attempt.

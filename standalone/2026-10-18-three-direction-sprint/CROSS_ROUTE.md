# A same-profile Gauss-bias filter also removes the radial principal detector

Status: **PROPOSED elementary functional calculation, requiring independent
review. This is an obstruction for one identified radial construction.**

This note cross-checks the Eisenstein arithmetic-vector experiment against
the principal scalar in the pinned CT source. It does not rule out probes
in different variables, genuinely joint weights, or another detector.

The primary CT interface is Cureton--Thorner, Hexagon 2610.00200v2,
[`DedekindZeta.tex`](https://hexagonmath.org/api/v1/works/2610.00200v2/source?path=DedekindZeta.tex),
SHA256 `f54808ad0f967b5429c7ac30d7b27ff25671e02d7fb43cf753b2b826c9d35df4`.
Its general-field hypotheses require additional roots of unity; this note
does not assert that its entire theorem specializes directly to Q(omega).
The functional calculation below is local at one complex place, with its
radial hypothesis displayed explicitly.

## 1. The actual two functionals

In the cubic Gauss-vector calculation of de Faveri--Dunn--Hoffstein,
the polar contribution is proportional to the radial Mellin value

    Hhat(5/6),  Hhat(s)=integral_0^infinity H(v)v^(s-1)dv.

See [the primary paper, Section 2.1, equations (2.4)--(2.9)]
(https://arxiv.org/html/2607.07911v1). The truncated Gauss evaluation is
ultimately [Lemma 6.7 of the underlying primary paper]
(https://arxiv.org/html/2410.03048v2). Signed smooth compact profiles follow
by linearity, keeping the remainder of both fixed nonnegative profiles.

The CT principal calculation uses

    M(z)=integral_(C^times) What_0(y)|y|_C^z d^times y,
    c_0=(R_S^2/6) M(1/6) What_1(1).

The local norm is |y|_C=|y|^2. The source explicitly requires M(1/6)!=0.
The calculation below assumes the SAME radial profile

    W_0(x)=H(|x|^2), H in C_c^infinity((0,infinity)),

is used in both functionals. Fixed nonzero measure and auxiliary-place
normalizations multiply the answer by a nonzero scalar and do not affect
its vanishing. A construction in which the Gauss profile lives in a
different variable is outside this obstruction's scope.

## 2. Explicit Fourier--Mellin identity

Use Lebesgue area dA, d^times y=dA(y)/|y|^2, and

    What_0(y)=integral_C W_0(x) exp(-4 pi i Re(x y)) dA(x).

For 0<Re z<1 the exact identity is

    M(z)=pi^2 (2pi)^(-2z) Gamma(z)/Gamma(1-z) Hhat(1-z).    (1)

In particular the scalar at z=1/6 is strictly positive, so

                    M(1/6)=0  iff  Hhat(5/6)=0.           (2)

Proof. For 0<Re z<1,

    |y|^(2z-2)=1/Gamma(1-z)
       * integral_0^infinity t^(-z) exp(-t|y|^2)dt.

Pair this identity with the Schwartz function What_0. The integral is
absolutely convergent: the weight is integrable near zero, and What_0
decays faster than any power at infinity. Its Fourier Gaussian pairing is

    integral_C What_0(y) exp(-t|y|^2)dA(y)
       =(pi/t) integral_C W_0(x) exp(-4pi^2|x|^2/t)dA(x).

The x support is a compact annulus. Therefore the subsequent t integral
can also be interchanged absolutely, including for complex z in the
stated strip. Substitute u=4pi^2|x|^2/t to obtain

    integral_C What_0(y)|y|^(2z-2)dA(y)
       =pi(2pi)^(-2z) Gamma(z)/Gamma(1-z)
          * integral_C W_0(x)|x|^(-2z)dA(x).

Polar coordinates give the last integral as pi Hhat(1-z). This proves
(1), without importing a distributional normalization convention.

## 3. Consequence for the proposed filter

Let H=(v d/dv+5/6)H_0. Integration by parts, with zero compact-support
boundary terms, gives

    Hhat(s)=(5/6-s) Hhat_0(s).

This kills the cubic Gauss pole at s=5/6. Equation (2) shows that applying
the SAME radial filter to W_0 also kills its CT principal scalar. It cannot
be advertised as a principal-preserving CT improvement.

The arithmetic-vector estimate remains a meaningful separate result: it
demonstrates that the worst general cubic large-sieve norm need not be
attained by every Gauss-correlated coefficient vector. Connecting that
fact to the native reciprocal detector requires either another variable,
a joint profile with independently verified target response, or an
explicit cancellation scheme whose target row survives. The scalar
nonvanishing check must precede any claimed zero-free consequence.

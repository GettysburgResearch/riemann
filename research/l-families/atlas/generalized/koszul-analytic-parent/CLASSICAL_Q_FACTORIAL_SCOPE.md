# Classical multiple q-factorials and the scope of the source construction

The polynomial-growth R_n global cohomological completions in these
packets belong to a classical special-function family: they are finite
products and ratios
of multiple q-shifted factorials with arithmetic Frobenius parameters.
The source constructions, ramification adapters, operator domains and
source-count boundary proofs remain the substantive claims. Inventing
a new species of scalar special function is not a claim of the packet.

The primary reference is Narukawa,
[The modular properties and the integral representations of the multiple elliptic gamma functions](https://arxiv.org/abs/math/0306164),
section 2, page 4 of the arXiv PDF. It defines the multiple q-shifted
factorial as a product indexed by nonnegative integer tuples and gives
its absolute convergence when all base parameters have modulus below
one. We use that product only; no modular transformation at coincident
parameters is imported without checking its hypotheses.

## 1. Exact reduction from the source multiplicities

Let G be a finite group of exponent L, and retain the source
R_n=Sym^n(V) tensor Sym^n(W), with
D=dim V+dim W-1. Every eigenvalue of every input group element is
an L-th root of unity. The source character argument in the
[finite-group theorem](FINITE_GROUP_SOURCE_BOUNDARY.md) proves that
every multiplicity sequence m_{rho,n} has a rational generating series
whose poles are L-th roots of unity of order at most D. Thus

    sum_{n>=0} m_{rho,n} z^n=P_rho(z)/(1-z^L)^D,        (1.1)

where P_rho is a polynomial with integer coefficients. Integrality
follows from the integer multiplicities and the integer denominator.
The character generating functions are proper rational functions:
their coefficient formulas are finite sums of polynomials in n times
roots of unity to the n-th power. Hence deg P_rho<LD.

No infinite coefficient search is needed. The exact numerator is

    p_{rho,j}=sum_{k=0}^{floor(j/L)}
                   (-1)^k binom(D,k)m_{rho,j-kL},
    0<=j<LD.                                          (1.2)

Coefficients beyond that range vanish by the rational pole proof,
not by extrapolating a finite zero list. For the actual S3 source one
may take L=6,D=4; for S4, L=12,D=6. For a general even/odd
selection replace L by lcm(L,2) if necessary. The S3 and S4
periods are already even; in particular the S4 parity selections
in the coherent quadratic algebra have the same period bound 12.

For a fixed finite Frobenius matrix A define the matrix product

    B_D(X,A;q)=product_{k_1,...,k_D>=0}
                     det(1-X q^{k_1+...+k_D} A).

For |q|<1 this converges locally uniformly in X. It is equivalently
the product, over eigenvalues alpha of A with algebraic multiplicity,
of the classical multiple q-factorials with argument alpha*X and
D equal bases q. No diagonalizability is needed for determinants,
and no numerical eigenvalue fitting is used.

If m_n has the numerator P(z)=sum_j p_j z^j in (1.1), then

    product_{n>=0} det(1-Tz^n A)^{m_n}
       = product_{j=0}^{LD-1} B_D(Tz^j,A;z^L)^{p_j}.    (1.3)

Indeed the number of D-tuples with sum k is binom(k+D-1,D-1).
Expanding the right-hand exponents gives exactly (1.1). Alternatively,
in a neighbourhood of T=0 its logarithm is

    -sum_{m>=1} T^m tr(A^m) P(z^m)
                           /[m(1-z^{Lm})^D],

which is precisely the source-grade logarithm. Ordinary holomorphic
or meromorphic continuation in T proves (1.3) on the entire common
T-domain. Some p_j can be negative; any resulting apparent poles
cancel as dictated by the original source determinant.

## 2. Small exact calibrations

For the identity character of rank (2,3),

    F_e(z)=(1+2z)/(1-z)^4,

so the corresponding graded determinant is
B_4(T,A;z) times B_4(Tz,A;z)^2. Its first five exponents are

    (1,6,18,40,75),

since the coefficient at n is
binom(n+3,3)+2binom(n+2,3). These are exactly
dim(Sym^n C^2 tensor Sym^n C^3).

For the identity character of rank (3,4),

    F_e(z)=(1+6z+3z^2)/(1-z)^6,

giving B_6(T,A;z), B_6(Tz,A;z)^6 and B_6(Tz^2,A;z)^3.
The first five exponents are

    (1,12,60,200,525),

from binom(n+5,5)+6binom(n+4,5)+3binom(n+3,5).
These identities are exact coefficient checks, not an independently
constructed arithmetic Frobenius source. The actual S3/S4 completions
use the individual group multiplicity numerators and their already
constructed finite cohomology matrices.

## 3. What the identification does and does not establish

For the untwisted completion, apply (1.3) to each finite H^1 source
and inversely to the H^0 and H^2 sources. For the fixed quadratic
twist there are only H^1 factors. For the coherent graded algebra
apply it to the separate even untwisted and odd twisted multiplicity
series. This is a finite special-function expression for the same
ordinary cohomological Fredholm object on |z|<1.

The identification does not replace the source by a fitted scalar
function, prove a new RH theorem, or establish that a finite-field
cohomological construction is a number-field L-function. It also does
not apply to the exponential-growth Koszul Lie multiplicities, including
their later actual arithmetic cohomological completion: those are a
different source with a different convergence problem.
Nor does this reduction identify the nonlinear full place-Euler source
E_Segre(z) with the polynomial-growth product over finite cohomological
grades. The latter two are different source operations.

Narukawa also gives definitions in other regions of the base
parameters. Such exterior definitions do not create a meromorphic
continuation across the grading unit circle of the source germ studied
here. The proved dense root-of-unity obstructions still prevent that
continuation for the stated fixed positive T region. Any proposed
alternative completion, anisotropic refinement or modular identity
must specify its new domain and source compatibility; it cannot be
presented as the same ordinary determinant continued through this
natural boundary without addressing the obstruction.

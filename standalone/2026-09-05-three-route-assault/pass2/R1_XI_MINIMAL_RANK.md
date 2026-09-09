# Actual xi coefficient completions: minimal ranks 15 and 32

Status: PROPOSED UNCONDITIONAL FINITE THEOREMS; complete analytic proof and rational interval certificate supplied; independent review required.
Scope: first TWO and first THREE nonconstant Taylor coefficients of the actual invariant xi function. No zero data, RH assumption, floating-point acceptance, or all-order extrapolation.
Executable proof boundary: source_certificate.py recomputes the displayed strict signs from rational series and Euler--Maclaurin remainder bounds. The analytic identities and their remainder proofs below still require mathematical review; this is not Lean formalization.

## D1. The actual source power sums

Let f(u)=xi((1+sqrt(1+4u))/2)/xi(1), as in R1_COMPACTNESS.md, and define p_j by

    log f(u)=p_1 u-p_2 u^2/2+p_3 u^3/3+O(u^4).

Write gamma_j for the Stieltjes constants in

    zeta(1+h)=1/h+gamma_0-gamma_1 h+gamma_2 h^2/2+O(h^3).

Put

    C=1+gamma_0/2-log(4pi)/2,
    L1=-1+pi^2/8-2gamma_1-gamma_0^2,
    L2=2-7zeta(3)/4+3gamma_2+6gamma_0 gamma_1+2gamma_0^3.

Then exactly

    p_1=C,   p_2=2C-L1,   p_3=6C-3L1+L2/2.       (D1)

Indeed C,L1,L2 are the first three derivatives of log xi at s=1. The pole of zeta cancels the factor s-1; the remaining gamma derivatives use digamma(1/2)=-gamma_0-2log2, trigamma(1/2)=pi^2/2, and digamma''(1/2)=-14zeta(3). Substituting s=1+u-u^2+2u^3+O(u^4) proves D1.

These are source constants, NOT sums over a presumed real zero spectrum. Newton's identities say that matching p_1,...,p_k is equivalent to matching the first k determinant coefficients.

## D2. First two coefficients: minimal rank exactly 15

The rational certificate proves

    C>0, p_2>0,
    14p_2<C^2<15p_2.

For any positive semidefinite matrix K of rank r, Cauchy gives

    (tr K)^2 <= r tr(K^2).

Thus no rank at most 14 can match the first two nonconstant coefficients. The construction A5 in R1_COMPACTNESS.md with r=15 gives a positive matrix matching them exactly. Its spectrum has 14 copies of

    x=(C-sqrt((15p_2-C^2)/14))/15

and one copy of C-14x. Both values are strictly positive. Therefore rank 15 is attained and minimal.

## D3. A sharp cubic-moment obstruction for every rank at most r

Assume 0<p_2<C^2 and C^2<=r p_2. Define

    d_r=sqrt((r p_2-C^2)/(r-1)),
    x_r=(C-d_r)/r,
    y_r=(C+(r-1)d_r)/r.

For any r nonnegative numbers lambda_i with sum C and square sum p_2,

    sum_i lambda_i^3 <= (r-1)x_r^3+y_r^3.         (D3)

Proof: Cauchy on the r-1 remaining coordinates gives lambda_i<=y_r. Hence each (lambda_i-x_r)^2(lambda_i-y_r)<=0. Summing this cubic and using the prescribed first two moments gives D3; the bound is attained at r-1 copies of x_r and one y_r. Zero-padding includes every spectrum of rank less than r. This proof requires no unproved variational classification.

For the ACTUAL xi constants, the certificate proves

    p_3-[30x_31^3+y_31^3] > 2.0155627 * 10^(-9) >0.

Consequently no positive semidefinite matrix of rank at most 31 can match the first three nonconstant xi coefficients.

## D4. A rank-32 construction with no zero information

For x in the fixed rational interval (0.00056,0.00057), set

    S(x)=C-30x,
    D(x)=2(p_2-30x^2)-S(x)^2,
    P(x)=30x^3-S(x)^3/2+(3/2)S(x)(p_2-30x^2)-p_3.

The certificate proves

    P(0.00056)<0<P(0.00057),
    S(x)>0, D(x)>0, S(x)^2-D(x)>0,
    P'(x)>0

throughout the closed interval. The interval assertions follow from the endpoint checks: D is concave; S is decreasing; S^2-D is decreasing for x<C/31; and

    P'(x)=45[31*32*x^2-62Cx+C^2-p_2]

is decreasing for x<C/32 and positive at the upper endpoint. All those strict inequalities are certified.

Thus P has exactly one root x_* in this rational interval. Define

    lambda_+= [S(x_*)+sqrt(D(x_*))]/2,
    lambda_-= [S(x_*)-sqrt(D(x_*))]/2.

The diagonal matrix with 30 copies of x_* and the two positive values lambda_+,lambda_- has trace C, square trace p_2, and cube trace p_3. Its determinant therefore matches f through degree three EXACTLY. Together with D3 this proves:

    The minimal rank of an unmarked positive determinant completion
    through the first three nonconstant invariant-xi coefficients is 32.

The entries are defined by exact source constants and a unique real root, not rounded decimal eigenvalues. The rational endpoints locate the root; they are not substituted for it. This matrix is not claimed to approximate higher xi coefficients or to have the actual xi zeros.

## D5. Rational enclosure of the source constants

The code uses N=64 and m=4. Let L=log N, H_j=sum_(k<=j)1/k, H_j^(2)=sum_(k<=j)1/k^2, and c_k=B_(2k)/(2k N^(2k)), for k=1,...,m. Define

    G0=H_(N-1)-L+1/(2N)+sum c_k,
    G1=sum_(n<N)log(n)/n-L^2/2+L/(2N)
                         -sum c_k(H_(2k-1)-L),
    G2=sum_(n<N)log(n)^2/n-L^3/3+L^2/(2N)
                  +sum c_k[(H_(2k-1)-L)^2-H_(2k-1)^(2)].

The Euler--Maclaurin remainder is

    R(s)=-(s)_(2m)/(2m)! integral_N^infty B_(2m)({x}) x^(-s-2m)dx.

Using |B_(2m)({x})|<=|B_(2m)| and differentiating the absolutely convergent remainder near s=1 gives

    |gamma_0-G0|<=r0,
    |gamma_1-G1|<=r1,
    |gamma_2-G2|<=r2,
    r0=|B_(2m)|/[2m N^(2m)],
    A=H_(2m)+L,
    r1=r0[A+1/(2m)],
    r2=r0[A^2+H_(2m)^(2)+A/m+1/(2m^2)].

For R'' the derivative of the rising factorial contributes H_(2m)^2-H_(2m)^(2); the displayed plus sign gives a safe absolute bound. The log-moment integrals supply the last two terms. The signs of R or its derivatives are not assumed.

Likewise zeta(3) is enclosed by

    Z3=sum_(n<N)n^(-3)+1/(2N^2)+1/(2N^3)
         +sum_(k=1)^m B_(2k)(3)_(2k-1)/[(2k)! N^(2k+2)],
    |zeta(3)-Z3| <= |B_(2m)|(3)_(2m)
                      /[(2m)!(2m+2)N^(2m+2)].

Pi uses Machin's identity 16 atan(1/5)-4 atan(1/239), each arctangent enclosed by consecutive alternating partial sums. Logarithms use power-of-two reduction to 1<=x<=2 and

    log x=2 sum_(j=0)^(M-1) y^(2j+1)/(2j+1)+R_M,
    y=(x-1)/(x+1),
    0<=R_M<=2 y^(2M+1)/[(2M+1)(1-y^2)].

Here M=40. Every arithmetic operation is rational, rounded OUTWARD to denominator 10^40. Square-root endpoints are obtained by integer square roots; logarithm interval endpoints use monotonicity. No floating-point or special-function library participates in acceptance.

The stored JSON gives full endpoint intervals. Readable enclosures include

    0.02309570896612102 < C < 0.02309570896612105,
    0.00003710063643722 < p_2 < 0.00003710063643771,
    0.00000014367785825 < p_3 < 0.00000014367786233.

The rank-31 obstruction and the cubic endpoint signs have margins much larger than these interval widths.

## D6. Scope of the advance

This is an actual source-only finite positive construction and a minimal-rank theorem. It supplies a nontrivial starting object for A1, not the missing all-order sequence. The jump from minimal rank 15 at order two to 32 at order three is a finite fact; no rank-growth law or higher-order extrapolation is claimed. All three research routes remain active.

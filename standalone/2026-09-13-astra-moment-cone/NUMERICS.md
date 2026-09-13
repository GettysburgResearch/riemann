# Complete native integration and finite matrix contract

MCE26. The mathematical remainder arguments below are proposed for independent
review. Executing the checker is not a formal proof of those arguments.

## Primitive and dependence

`exact_interval.py` is a byte-identical copy of CCF26's 512-bit outward dyadic
primitive, supplied in the previous user archive and now published in #875.
SOURCES.json records both SHA256 and Git-blob identity. It uses integers and
Fraction only. Machin's identity with 128 alternating arctangent terms encloses
pi. Positive exponentials use range reduction to at most 1/8, 100 Taylor terms
and the complete geometric ratio remainder, followed by outward squaring.
Negative exponentials use reciprocals or a rigorous underflow interval.
Square roots use integer square roots. No floating arithmetic, zeta evaluator,
root table, or third-party special-function evaluator enters acceptance.
Ordinary and optimized execution are the SAME primitive implementation.

## 1. Literal centered gamma stage five

The rates are exactly (1,4,9,16,25), each with gamma shape two. With

    b_a=a^2 product_(d!=a)[d/(d-a)]^2,
    c_a=-2 sum_(d!=a)1/(d-a),
    f5(x)=sum_a b_a(x+c_a) exp(-a x), x>0,
    tau=pi^2/3-2 sum_a 1/a,

these are the finite rational partial fractions of product (a/(a+s))^2.
The half-line defining moments are

    I_k=int_0^L t^(2k) sqrt(f5(pi exp(2t)-tau)
                            f5(pi exp(-2t)-tau))dt,
    L=(1/2)log(pi/tau), f_k=I_k/[I_0 (2k)!].

The factor two from reflection cancels exactly. L is enclosed by exponential
comparisons between the terminating bounds

    1.07952912855616 < L < 1.07952912855618.

We integrate to B=1.0795291285 and retain the entire remaining endpoint tail.
No quadrature is performed outside the support.

### Gap-free complex Taylor cover

Recursively bisect [0,B]. A cell with center c, halfwidth d is accepted when
8d<=rho=min(1/64,(L_lower-c)/4). The resulting 964 rational cells are checked
for their endpoints, adjacency and these inequalities. On each complex disk
|t-c|<=rho the large argument x=pi exp(2t)-tau has Re x>13/5,
|Im x|<Re x and |x|<32. Its rate-one term dominates: the exact upper ratio

 sum_(a>1)(b_a/b_1) [2+|c_a|/(13/5)]/[1+c_1/(13/5)]
                              *2^(-floor((a-1)13/5))

is less than 1/4, as checked rationally. In obtaining it, |x+c_1| is bounded
below by Re x+c_1, not by an unproved modulus comparison. The complete large
density is bounded above by
sum_a b_a(32+|c_a|)2^(-floor(a13/5))<2^11.

The small argument y=pi exp(-2t)-tau has Re y>0. For r=L-c,
exp(2(r-rho))cos(2rho)>1 follows from rho<=r/4, rho<=1/64 and
cos(2rho)>=exp(-4rho^2). Moreover |Im y|<=4/31<pi/24 and |y|<4.
The simplex convolution formula is

    f5(y)=[(5!)^4/9!] y^9 E exp(-y R), 1<=R<=25.

Rotating the expectation by exp(13i Im y) makes its real part positive,
because |(R-13)Im y|<pi/2. Thus the density is nonzero on the entire disk,
and its analytic square root is fixed by the positive real center.
The coefficient (5!)^4/9! is less than 600; hence |f5(y)|<2^28.
These are analytic branch statements, not merely positivity at sample points.

We use the scaled Taylor variable v=(t-c)/rho. Exponential and square-root
recurrences retain all coefficients through degree 48. Multiplication by
(c+rho v)^2 generates moments through degree 28. Each even Taylor coefficient
is integrated with exactly 2d(d/rho)^k/(k+1).
The complete omitted Taylor tail over all cells is bounded by

    2 B M_j 8^(-49)/(1-1/8), M_j=2^21(11/10)^(2j).

Indeed |h|<sqrt(2^11*2^28)<2^20, |t|<11/10 on the disks, and the real cell
has |v|<=1/8. The extra factor two is spare. The program retains this error
for every moment, not just for the normalizer.

### Whole unintegrated endpoint

Put delta=L_upper-B. The checker establishes tau<2/5 and
(4/5)exp(1/50)<1. For 0<=v=L-t<=delta<1/100, the small argument obeys

    tau(exp(2v)-1)<v.

The large density is at most 4x exp(-x)<=4. The simplex small density is at
most 600 v^9. Thus h(L-v)<=50 v^(9/2), and the entire omitted moment is at
most 10 delta^(11/2)(11/10)^(2j). Integer square roots enclose delta^(1/2).
Both the Taylor and endpoint errors are included before normalizing by the
strictly positive I_0 interval. The stored coefficients are the full source
intervals; the scout's coefficients are never used.

## 2. Fresh full theta moments through degree thirty-two

Use the literal even theta source from PROOF.md, with n=1,...,20 on the grid
h=1/256, |t|<=3. The weight at zero is h and at each positive grid point is
2h, including the point t=3: these are the retained points of the whole-line
infinite trapezoid rule, not a finite-interval trapezoid with half endpoints.
The following three errors are paid. The test suite also freshly reconstructs
mesh 1/320 with the same primitive and complete remainder arguments.

### Infinite trapezoid alias

Jacobi inversion supplies the holomorphic even continuation throughout the strip |Im t|<=1/4.
On its boundary, writing x=Re t>=0, |t|^j<=j! exp(x+1/4),
pi cos(1/2)>5/2 and pi<4 give

    |t^j phi(t)| <= 2^8 j! sum_n n^4 exp(6x)
                                     exp[-(5/2)n^2 exp(2x)].

Substituting v=n^2 exp(2x) in the integral of each term and using
sum n^-2<2 proves a complete boundary L1 bound less than 2^16 j!.
The usual contour-shift proof of the Fourier-transform decay, followed by the
absolutely convergent Poisson sum, bounds the alias by

    2^17 j!/[exp(2pi(1/4)/h)-1].

At h=1/256, exp(128pi)>2^512: use pi>3 and exp(3/4)>2.
Therefore this error is less than j!2^-494. It is smaller at mesh 1/320.
The same bound applies for every j<=32; it is not an extrapolated quadrature
error inferred from two meshes agreeing.

### Entire spatial grid tail

For t>=3 the same termwise positive upper estimate, enlarged harmlessly,
gives 2^14 j! exp(6t-(5/2)exp(2t)). For example bound
sum n^4 exp(-n^2/2)<64 using n^4 exp(-n^2/4)<16 and the Gaussian integral.
At t=3 the exponent is <-982, since exp(6)>400, and its derivative is
<-1994 thereafter. The omitted geometric grid sum, with h=1/256 or 1/320,
is less than j!2^-900, including both signs of t.

### Entire index tail

For n>=21 and t>=0, exp(6t-3n^2 exp(2t)) decreases. Also n^4<=2^n and e>2.
The total weights of the retained grid on [-3,3] are less than 7. Thus the
entire missing-index contribution is at most

    616 j! sum_(n>=21)2^(n-3n^2)<j!2^-1290.

Adding all three bounds gives less than j!2^-490, the allowance added in
`theta`. Every floating printed decimal is only an orientation value.

## 3. Power sums, inertia, robustness and the permanent tube

The exact triangular logarithmic recurrence in PROOF (2) maps the full source
coefficient intervals to all required scaled p_k. Directed LDL elimination
certifies six positive pivots and one negative pivot for H7(F5). The same
elimination certifies both native theta matrices. No numerical eigenvalue
algorithm is used. The rational negative vector is stored separately and
applied to the entire interval matrix, then again to the full coordinate box
for E14(32)<=2^-72.

The permanent all-N tube is PROOF (9)--(13). Its only numerical inputs are the
fresh theta coefficient intervals, N^-3/4<=2^-144, the exact factorial and
power-of-three bounds, and the uniform normalizer 1/1600. Every coordinate
error, including normalization, is retained before evaluating the matrices.
The accepting program does not evaluate F_(2^192).

Finally, the rational Pade comparator uses rounded rational u_k as NEW MODEL
data. Its two rational matrices, rational solve, full denominator/numerator,
and all matched series identities are checked exactly. This rounding is not
used as a surrogate for a native theta integral or for the negative F5 form.

# Every fixed even order for the full hybrid Hecke family

Status: PROPOSED unconditional theorem with complete proof. This does NOT
prove the original near-linear physical-row moment without the extra Hecke
average. Its parameter-volume cost is D^k, not D. Constants may depend on k;
there is no growing-k uniformity claim. Definitions and field/class/twist
normalizations are those of THEOREMS.md.

## 1. The quantitative theorem

Let K be any fixed imaginary quadratic field. Use either the native ideal
Mobius coefficients with bounded completely multiplicative phases, or the
coupled 0/1/m coefficients (4), at ANY integer m>=2. All original row masks
and finite exclusions remain. Let nu have finite mass Z and be fixed at every
scale. Let <.>_R be the normalized class/angular/Mellin average, with both
Gaussian widths R>=1, centered at any fixed l0 in Z and t0 in R.

For every fixed integer k>=1 and X>=2,

    < integral |B_(psi,l,t)(X,u)|^(2k) dnu(u) >_R
       <= C_(K,c,k) Z [X^k+X^(2k)/R^2] log(3X)^(k^2-1). (17)

The constant is independent of m, phases, masks, exclusions, centers, X and R.
For the cumulative critical order-2k energy,

    E_k(D)=integral_0^D integral |B(X,u)|^(2k)dnu(u)dX/X^(k+1),

one consequently has, for D>=2,

    <E_k(D)>_R <= C_(K,c,k)Z[log(3D)^(k^2)
                        +(D^k/R^2)log(3D)^(k^2-1)].     (18)

At R=D^(k/2), (17) has the desired D^k power, up to logarithms, for this FULL
averaged family. Every ideal and all composite/collision contributions occur.
At k=2 the two widths are D, giving spectral area D^2. At k=1 they are sqrt(D).
This explicit cost is why (17) is not the native H=D^(1+theta) moment conjecture.

The Gaussian is exactly W_c of THEOREMS.md. The same fixed-scale conclusion
holds for a bounded compact norm test with support in (0,b], with constants
depending on b and the test bound. No contour continuation is used.

## 2. Positive tensor coefficients: uniformity in m without a k-dependent power

Let f_m be the positive multiplicative ideal majorant with

    f_m(p)=1-1/q,  f_m(p^m)=q^(m/2-1),
    f_m(p^e)=0 for other e>0,  f_m(1)=1.

For native coefficients use f(p)=1 and f(p^e)=0, e>=2. Define d=f_m^{*k} using
UNRESTRICTED Dirichlet convolution, including shared prime factors. Then

    sum_(Nn<=Y) d(n)^2 <= C_(K,k)Y log(3Y)^(k^2-1),       (19)

uniformly in m>=2.

Here is a direct proof of (19). At a prime ideal of norm q put v=q^-1/2 and
let D_e be the coefficient of x^e in

    [1+(1-1/q)x+q^(m/2-1)x^m]^k.

D_0=1 and D_1=k(1-1/q). Evaluated at x=v, every powerful choice has weight
q^(m/2-1)v^m=q^-1=v^2, independently of m. Grouping choices by whether their
total physical exponent is 0,1,or >=2 gives

    sum_(e>=2) D_e q^(-e/2) <= 3^k/q,
    sum_(e>=2) D_e^2 q^-e <= 9^k/q^2.                    (20)

For the first bound expand the k factors, bound each ordinary occupied
weight by v and each powerful one by v^2, and bound every term of degree
at least two by v^2 times its coefficient. Squaring the nonnegative sum
proves the second bound. Native coefficients satisfy the same bounds.

Consider the formal polynomial P_q(z)=sum_e D_e^2 q^-e z^e and multiply by
V_q(z)=(1-z/q)^(k^2), the inverse local factor of zeta_K(s)^(k^2) at weight
one. Its linear coefficient is -k^2/q. Thus the product has linear coefficient

    k^2[-2/q^2+1/q^3],                                  (21)

not zero (it is zero for the native majorant). Its remaining absolute
coefficient mass is O_k(q^-2). Explicitly, writing r=k^2, the entire
nonconstant mass is at most C_k/q^2, with

    C_k=2r+r^2+2^r(1+r+9^k).

To check this bound, write P=1+A z+P_2 and V=1-B z+V_2. Use A<=r/q,
B=r/q, |A-B|<=2r/q^2, ||P_2||_1<=9^k/q^2,
||V_2||_1<=2^r/q^2 and ||V||_1<=2^r. Expand the product and sum the five
bounds |A-B|, ||V_2||, AB, A||V_2||, and ||P_2||||V||.

Let h be the exact formal quotient of sum_n d(n)^2(Nn)^-s by zeta_K(s)^r.
These bounds prove sum_n |h(n)|/(Nn)<=C_(K,k), uniformly in m. No zero-free
claim is involved: the inverse local factors are polynomials. Coefficientwise
one has d(n)^2=(h*z_r)(n), where z_r counts ordered r-tuples of ideals.
Repeated ideal counting gives sum_(Nn<=Y)z_r(n)<=C_(K,k)Y log(3Y)^(r-1).
Convolving this positive bound with |h| proves (19). The formal coefficient
identities involve finite divisor sums before any infinite estimates. QED.

## 3. Finite source and multiplicative twisting

Let F be the source restricted to Nn<=Y with arbitrary additional weights of
modulus <=1. By multiplicativity of eta_(psi,l,t),

    F_(psi,l,t)^k = sum_j b_j eta_(psi,l,t)(j),
    |b_j|<=d(j),  Nj<=Y^k.

The same character orthogonality (8) and Schur estimate (10), now WITHOUT the
Gaussian energy kernel, give

    <|F|^(2k)>_R <= (1+C_K Y^k/R^2) sum_j |b_j|^2.

This follows from 2|b_i b_j|<=|b_i|^2+|b_j|^2 and the row sum in (10).
Use (19) at Y^k and absorb fixed powers of k into C_(K,k). The result is

    <|F|^(2k)>_R <= C_(K,k)[Y^k+Y^(2k)/R^2]log(3Y)^(k^2-1). (22)

The class average acts on the class of the WHOLE product ideal, not separately
on each column. Thus no false pairwise coprimality or independence is inserted.
All principal aliases are present in the product coefficient b_j.

## 4. The full Gaussian and critical scale integration

Partition every ideal into dyadic bands 2^j X<Nn<=2^(j+1)X, using a harmless
consistent endpoint convention. Empty bands below norm one vanish. Let

    w_j=sup_(2^j<=y<=2^(j+1)) |W_c(y)|.

For constants a>0 and C depending only on c, w_j<=C exp(-a j^2+C|j|).
Divide the coefficient weights of each band by w_j and apply (22). Minkowski
in the normalized class/angular/Mellin probability space gives, for X>=1,

    <|B(X)|^(2k)>_R^(1/(2k))
       <= C_(K,c,k) [X^(1/2)+X/R^(1/k)]
                           log(3X)^((k^2-1)/(2k)).       (23)

Indeed the dyadic root bound has Y^(1/2)+Y/R^(1/k), where Y=2^(j+1)X;
log(3Y)<=C[log(3X)+|j|] on nonempty bands. Both weighted sums in j converge
by the displayed Gaussian bound. This also justifies the full L^(2k) limit,
not just the finite ideal truncations. Raising (23) to 2k proves (17), then
summing over nu multiplies the uniform per-row bound by Z.

For 0<X<=1, the coefficient bound |c_m(n)|<=sqrt(Nn), uniform in m and masks,
and W_c(y)<=C_c y^-2 for y>=1 imply |B(X,u)|<=C_(K,c)X^2. This treats the
entire small-scale Gaussian tail uniformly in the twists. For X>=1 integrate
(17) with dX/X^(k+1). The two elementary integrals are bounded by
C_k log(3D)^(k^2) and C_k D^k log(3D)^(k^2-1)/R^2, respectively. This proves
(18). No same-height pointwise envelope or unknown native moment enters.

## 5. Limit and source credit

The theorem is an unconditional generalized moment result, but for a larger
archimedean Hecke family. Its area D^k at order 2k cannot be relabeled the
near-linear physical row height D^(1+theta). Recovering the principal angular
and Mellin member without that loss is not proved.

The local first-coefficient subtraction in Section 2 is the same classical
Euler-coefficient comparison used for the tensor-square norm budget in #954;
we apply it to IDEAL k-fold convolution coefficients, not rational norm fibers.
The geometric Schur estimate is proved in THEOREMS.md, with Huxley's classical
number-field large-sieve/Hecke-moment framework credited in SOURCES.md.
No claim is made that the general mean-value method is new in the literature.

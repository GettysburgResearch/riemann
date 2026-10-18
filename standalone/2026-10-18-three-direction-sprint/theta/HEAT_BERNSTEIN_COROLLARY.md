# Uniform all-order consequences of the positive actual heat kernel

**PROPOSED corollary of GLOBAL_HEAT_POSITIVITY.md.** These are all-order
scalar and factorial-scaled statements. They do not give complete
monotonicity of k or the unscaled Hamburger positivity required in#1003.
No novelty claim is made for the Bernstein/spectral interpretation.

Put `F(x)=xi(1/2+sqrt(x))/xi(1/2)` and `G=F'/F`, with the same actual
kernel k. Let gamma0 be the unique first positive zero height freshly
certified in[14.13,14.14]. The proof of the global heat theorem gives

    0<k(y)<(5/3)exp(-gamma0^2 y), y>=1/50.               (1)

Indeed its complete remaining-zero bound is less than two thirds of
the first positive term; the same triangle inequality supplies the upper
bound. At0 the literal arithmetic formula gives
`k(y)=O(y^(-1/2)(1+|log y|))`, as established in
ARITHMETIC_STIELTJES_KERNEL.md. Thus every polynomially weighted absolute
moment of k is finite. This is an explicit integrability argument,
not differentiation justified by mere L1 integrability alone.

For every integer m>=0 and every real x> -gamma0^2,

    (-1)^m G^(m)(x)=integral_0^infty y^m e^(-xy)k(y)dy>0. (2)

For x>1/4 this is differentiation of the exact arithmetic Laplace
formula. Equation(1) extends its integral holomorphically to
`Re x> -gamma0^2`. Classical paired factorization, the complete first20
census, and `|Re rho-1/2|<=1/2` show that G has no other pole in that
half-plane: every remaining squared zero has real part at most
`1/4-20^2<-gamma0^2`. Analytic continuation therefore proves(2) on the
stated whole real interval. Positivity is strict because k is strictly
positive on every positive y interval. This proves complete monotonicity
of **G**, simultaneously at every order; it does not prove complete
monotonicity of **k**.

In the physical Xi variable define the actual canonical coefficients by

    log[xi(1/2+iz)/xi(1/2)]
       =-v z^2/2-sum_(r>=2) A_r z^(2r)/r,
    A_1=v/2.

Taylor expansion in (2), with its proved absolute moments, gives

    A_r=1/(r-1)! integral_0^infty y^(r-1)k(y)dy>0,
                         EVERY integer r>=1.            (3)

Thus the signs of all individual actual canonical power sums are settled
at once by one global kernel inequality. No finite-moment induction or
extrapolation is involved. Standardized coefficients in#1003 are
`Q_r=A_r/v^r`, so they have the same strict scalar signs.

More precisely, for every N the factorial-scaled matrix

    [(i+j+1)! A_(i+j+2)]_(0<=i,j<=N)

is strictly positive definite: its quadratic form for a nonzero real
polynomial P is `integral_0^infty y k(y)P(y)^2dy>0`.
The unscaled matrix `[A_(i+j+2)]` is different. Dividing a moment
sequence by its varying factorial is not a positivity-preserving step.
For example the positive density `k0(y)=exp(-y^2)` gives

    A_2=1/2, A_3=sqrt(pi)/8, A_4=1/12,
    A_2 A_4-A_3^2=1/24-pi/64<0.

Consequently neither (2), (3), nor the strict scaled-matrix result
proves the actual canonical Hamburger tower. The remaining gate is
precisely the removal of this factorial obstruction, or a separate
all-order complete-monotonicity proof for the literal arithmetic k.

# A growing-prime sector: a uniform remainder and explicit subpower growth

Status: **PROPOSED analytic component theorem, requiring independent review.**
This extends Theorem F of PROOF.md while retaining the entire common-factor
sum and the actual Gaussian physical horizon. It gives no upper bound for
the full critical energy and no new zeta zero-free boundary.

Use a, beta, C_a, G, H_p, C_c, and the finite prime universe U_P exactly as
in PROOF.md. All ordered primitive ratios in U_P are retained, and their
common factor d is unrestricted. Put d_c=c-1/2 to distinguish the fixed
Gaussian shift c from the small constant kappa below.

## 1. A global harmonic remainder, including x below one

If a coefficient sequence h satisfies B_theta=sum_e |h(e)|e^(-theta)<infinity,
theta in [3/4,1), and b=1*h, then for ALL x>0

    sum_(n<=x)b(n)/n=C log x+D+O(B_theta/(1-theta) x^(theta-1)),   (1)
    C=sum_e h(e)/e,
    D=gamma C-sum_e h(e)log(e)/e.

The implicit constant is absolute over the displayed theta range. For x>=1,
write the left side as sum_(e<=x) h(e)H_floor(x/e)/e and use
H_floor(u)=log u+gamma+O(1/u). The finite remainder is <=B_theta x^(theta-1).
For the omitted e>x main term, put v=e/x and use

    sup_(v>=1) v^(-(1-theta))log v=1/(e(1-theta)).

For x<1 the left side is zero. Bound C, D and |log x| by the same norm
and the same elementary maximum. Thus (1) is a global bound, not an
asymptotic silently applied to below-output arguments.

For the primitive-ray sequence b(n)=a(rn)a(sn), (8) of PROOF.md gives

    B_theta <= |a(r)a(s)| G_theta product_(p|rs) L_p(theta),
    G_theta=sum_e |g(e)|e^(-theta)<=G_(3/4),
    L_p(theta)=1+(1-1/p)p^(-theta)/(1-(1-2/p)p^(-theta)).        (2)

Here g is the full non-zeta coefficient sequence of G, not a prime cutoff.
Its absolute norm includes all infinite primes and is finite. The constants
in (2) are uniform as theta tends to one.

The ray's two exact leading coefficients in (1) are

    C_(r,s)=C_a beta(r)beta(s),
    D_(r,s)=C_(r,s)[gamma+G'(1)/G(1)+sum_(p|rs) alpha_p],
    alpha_p=H'_p(1)/H_p(1)
           =p^2 log(p)/[(p^2-1)(p+2)].                    (3)

This follows by differentiating the absolutely convergent non-zeta
Dirichlet series at 1. It retains all shared primes between n and rs.

## 2. A uniform full-sector identity

Define, with absolutely convergent sums for fixed P,

    ell_P(sigma)=sum_(r,s in U_P,(r,s)=1)
          beta(r)beta(s)(rs)^(-sigma)exp(-log(r/s)^2/8),
    ell_P=ell_P(1/2),
    A_P=sum_(r,s in U_P,(r,s)=1)
          beta(r)beta(s)/sqrt(rs) exp(-log(r/s)^2/8)
                                             sum_(p|rs)alpha_p,
    Xi_theta(P)=product_(p<=P)
          [1+2L_p(theta)(p-1)/(p^(1+theta/2)-1)].          (4)

The complete sector E_P(T) satisfies, uniformly for T>0, P>=2 and
3/4<=theta<1,

    E_P(T)=C_a C_c [ell_P(log T+C_0)
                            +(1/2)ell'_P(1/2)+A_P]
              +O_c(T^(theta-1) Xi_theta(P)/(1-theta)),    (5)
    C_0=gamma+G'(1)/G(1)-2d_c.

Proof. Integrate (1) against the exact full Gaussian g_log(r/s)(y) in
the physical ray formula, at x=T exp(y)/sqrt(rs). The first y moment is
-2d_c times its mass. The error y integral is its mass times
exp[2d_c(1-theta)+(1-theta)^2/2]. Thus its absolute bound is a constant
times T^(theta-1)|a(r)a(s)|(rs)^(-theta/2)
product_(p|rs)L_p(theta)/(1-theta). Drop only the Gaussian <=1 at this
error step. Summing these positive resources over the coprime r,s in U_P
gives EXACTLY Xi_theta(P), including arbitrarily high prime powers. The
main log(rs) sum is -ell'_P(1/2), accounting for the plus sign in (5).
All interchanges are absolutely justified by the finite product of
convergent geometric series. No uniform-in-P conclusion is inferred from
a fixed-P big-O term.

## 3. Control of the constant terms relative to the positive mean

The positive Fourier Euler representation in PROOF.md applies to
ell_P(sigma) near sigma=1/2, with

    lambda_(p,sigma)(t)=1-2c_p Re[z/(1-z)],
    z=p^(-1-sigma)exp(i t log p), c_p=(p^2-1)/(p+2).

At sigma=1/2 every lambda is positive, uniformly away from zero for each
fixed p. Uniformly in real t and as p tends to infinity,

    |partial_sigma log lambda_(p,sigma)(t)|_(sigma=1/2)
         <=(2+o(1)) log(p)/sqrt(p).                     (6)

Indeed differentiate z/(1-z), use |z|=p^(-3/2), c_p<=p and
lambda=1+O(p^(-1/2)). The finitely many small primes have finite bounds
by their strictly positive minima in (24) of PROOF.md. Positivity permits
bounding the derivative of the Fourier integral RELATIVE TO that integral.
The prime number theorem, by partial summation, then yields

    |ell'_P(1/2)| <=(4+o(1))sqrt(P) ell_P.               (7)

The alpha_p weighted support indicator has the same Fourier integral with
the extra local sum

    sum_(p<=P) alpha_p (lambda_p(t)-1)/lambda_p(t).

Its absolute value is bounded uniformly in P,t: alpha_p=O(log(p)/p),
lambda_p-1=O(p^(-1/2)), and sum_p log(p)p^(-3/2)<infinity.
The finitely many small denominators again have positive minima. Hence

                         |A_P|<=C ell_P.                (8)

These bounds pay the entire constant term of (5), including its signs;
they do not replace signed prime coefficients by unrelated positive data.

## 4. A legal growing prime universe

**Theorem G.** Fix 0<kappa<1/(4e^2), and put

    P(T)=kappa (log T)^2.

For each fixed real Gaussian shift c, the complete signed sector defined
above is positive for all sufficiently large T, and

    log E_(P(T))(T) ~ 2sqrt(kappa) log T/log log T.       (9)

Thus it grows faster than every fixed power of log T, and slower than
every fixed positive power of T. This is a theorem about a specified signed
Gram sector, not the complete energy. The classical prime number theorem
is the only prime-distribution input.

Proof. Choose theta=1-2/log P, which lies in [3/4,1) eventually. In the
product Xi_theta(P), uniformly over this theta schedule,

    log Xi_theta(P) <=2 sum_(p<=P) p^(-theta/2)+O(P^(1/4))
                    =(4e+o(1))sqrt(P)/log P.             (10)

For the first inequality, expand each local factor; the error is
O(p^(-theta)), whose prime sum is at most the full integer sum
O(P^(1/4)) uniformly for theta>=3/4. For the second, partial summation
of the prime number theorem is uniform for exponents theta/2 in a compact
subset of (0,1); P^((1-theta)/2)=e.

The remainder in (5) is consequently

    exp[(-2+4e sqrt(kappa)+o(1))log T/log P],             (11)

up to an absorbed logarithmic prefactor. It tends to zero because of the
strict kappa hypothesis. Equations (7)--(8) bound the bracket in (5)
between

    ell_P[(1-2sqrt(kappa)+o(1))log T]
    and ell_P[(1+2sqrt(kappa)+o(1))log T].                (12)

The lower coefficient is positive since sqrt(kappa)<1/(2e)<1/2.
Theorem F gives log ell_P~4sqrt(P)/log P. The logarithm of the extra
factor log T in (12) is negligible on this scale. Substituting P(T)
proves (9), with the full physical horizon and all common factors intact.

The qualifier 'sector' is essential. The complete critical bound
E_psi(T)<<_epsilon T^epsilon, if true, permits the growth in (9). Neither
that bound nor its failure follows from this component result. This
calculation instead provides an explicit range in which the previously
nonuniform prime-universe completion CAN be made uniform, with its full
remainder resource displayed in (5).

# Literal cutoff indefiniteness and a signed prime-tail theorem

Status: PROPOSED COMPLETE COMPONENT PROOFS; independent mathematical review
required. The full arithmetic matrix inequality and RH remain UNPROVED.
Base: PR #790 at bce97be9727dea9968db7517738edc966d2cc86b.
Local labels: ASTRA-SC6-01 through 04. No external priority claim.
Scope: literal von Mangoldt weights, every finite integer cutoff X>=2,
explicit unbounded rational test orders, and one actual ten-dimensional
matrix certificate. None of the new analytic results uses a verified zero
prefix, a zero simplicity assumption, or the earlier high heat-derivative
positivity claims.

## 1. Fixed source and complete formula

Use the parent's definitions

    A=rho(1-rho), Im rho>0, all multiplicities;
    h(u)=X'(u)/X(u)=sum_A 1/(u+A),
    X(u)=xi(1/2+sqrt(u+1/4));
    Omega(y)=Re digamma(1/4+i y/2)-log pi.

The square root expression defines an entire X by reflection; the displayed
branch on u>0 is only a way to evaluate it. The Fourier convention is

    ghat(l)=integral_R g(y) exp(-i l y)dy.

For the even rational functions used below, the unconditional explicit
formula in the parent gives

    4pi sum_A g((rho-1/2)/i)
      =4pi g(i/2)+integral_R g(y)Omega(y)dy
                    -2 sum_(n>=2) Lambda(n)n^(-1/2)ghat(log n). (1)

Here g is even; each invariant A occurs once in the upper-ordinate list.
The factor 4pi accounts for the two signs in the full zero list. The
rational tests below have poles only at imaginary height sqrt(17)/2>1/2,
so they are analytic in a strip strictly wider than the critical strip.
They have adequate real-axis decay, and their transforms are an exponential
times a polynomial. All prime series at each fixed order converge absolutely.
The Guinand--Weil formula, not a conjectural positivity assertion, is imported.

One small source budget is sufficient. Let

    H=h(0)=1+gamma_E/2-log(4pi)/2.

For A=x+iy, the critical strip gives x>0, y^2<=x. Since each
Re(1/A)>=1/(x+1)>0, the product identity gives H>0. Elementary gamma_E<1,
pi>3 and e<3 give H<1/2. Exactly as in the parent,

    x>=x0=1/H-1>1,        sum_A 1/x<=C=H/(1-H)<1.             (2)

Indeed 1/(x+1)<=H gives the first inequality, and
1/x=(1+y^2/x^2)Re(1/A)<=(1+1/x)Re(1/A)
<=Re(1/A)/(1-H) gives the second after summation. These estimates import
no numerical zero data.

## 2. Finite cutoff is NOT a positive operator approximation

For an integer X>=2, put

    W_X(y)=Omega(y)-2 sum_(2<=n<=X) Lambda(n)n^(-1/2)cos(y log n),
    S_X(t)=1+(1/(2pi))integral_0^infinity
                    exp(-(y^2+1/4)t)W_X(y)dy.                (3)

This is exactly the finite-prime-power truncation of the parent's heat
explicit formula. All gamma terms are retained. W_X is not being asserted
to be the density of the FULL zeta spectrum; it is the density of this
finite-cutoff approximation.

For any fixed c>0 define the Hankel operator

    T_(X,c)(s,t)=exp(-c(s+t))S_X(s+t).                       (4)

It has the signed real spectral-measure representation

    mu_(X,c)=delta_c+
      W_X(sqrt(lambda-c-1/4))/(4pi sqrt(lambda-c-1/4))d lambda,
                        lambda>c+1/4.                      (5)

The integral of 1/lambda against |mu| is finite: near its lower endpoint
the density is O((lambda-c-1/4)^(-1/2)), and at infinity it is
O_X(log(lambda+2)/sqrt(lambda)). Hence

    T_(X,c)=integral |exp(-lambda t)><exp(-lambda t)|dmu(lambda)

converges in trace norm. This is a self-adjoint signed integral, not an
integral of positive operators against a positive measure.

The exact endpoint is

    W_X(0)=-gamma_E-pi/2-3log2-log pi
                         -2 sum_(2<=n<=X)Lambda(n)/sqrt(n)<0. (6)

This uses the classical digamma value at 1/4. Conversely W_X(y) is eventually
positive because Omega(y)=log(y/(2pi))+O(1/y), whereas the cutoff cosine sum
is bounded. Thus both signs occur on open intervals.

**ASTRA-SC6-01.** Every T_(X,c), for every finite X>=2 and every c>0,
has infinitely many strictly negative eigenvalues and infinitely many
strictly positive eigenvalues.

Proof. Write the form as integral |R(lambda)|^2 dmu(lambda), where R is the
Laplace transform of the test. Fix p>0, set z=1/(lambda+p), and let nu be
the finite positive measure obtained by pushing z^2 d|mu|(lambda) forward
to [0,1/(c+p)]. Every z P(z), with P a polynomial, is the Laplace transform
of an exponential polynomial exp(-pt) times a polynomial in t. Polynomials
are dense in L2(nu): continuous functions are dense for this finite Borel
measure on a compact interval, and Weierstrass approximates them uniformly.
For any k, choose k disjoint compact subintervals where mu has negative
continuous density. Their normalized indicator functions have a negative
definite form. Approximate each in L2(nu) by polynomials; boundedness of
the sign multiplier preserves negative definiteness for sufficiently close
simultaneous approximations. This realizes a k-dimensional negative subspace
of the original Hankel form. Repeat on positive intervals for the positive
index. The trace-class min-max principle proves the assertion for every k.
This proof is a standard signed-Laplace Hankel argument, given here in full
for the literal arithmetic cutoff. QED.

This does NOT prove that the full zeta operator is indefinite. A limit of
indefinite compact operators can be positive; there is no fixed spectral gap
in the preceding construction. Nor does it rule out a different, compensated
positive approximation scheme. It rules out proving that these literal
finite cutoffs are positive.

## 3. Explicit tests and an all-cutoff negative bound

Fix B=17/4. For N>=1 set

    g_N(y)=(y^2+1/4)^2/(y^2+B)^(2N+2),
    Q_(N,X)=(1/(4pi))[integral_R g_N Omega
                 -2 sum_(2<=n<=X)Lambda(n)n^(-1/2)ghat_N(log n)].

The endpoint term is zero: g_N(i/2)=0. Equivalently,

    Q_(N,X)=(1/(2pi))integral_0^infinity
             W_X(y)(y^2+1/4)^2/(B+y^2)^(2N+2)dy.           (7)

These tests really belong to the source Hankel framework. At c=p=2,

    R_N(lambda)=(lambda-2)/(lambda+2)^(N+1),
    f_N(t)=exp(-2t)[t^(N-1)/(N-1)!-4t^N/N!],

and R_N is the Laplace transform of f_N. The delta_2 atom is annihilated.
Substituting lambda=y^2+9/4 into R_N(lambda)^2 gives g_N(y).
Thus Q_(N,X)=<f_N,T_(X,2)f_N>.

Let L be the least integer with X<=2^L, so L>=1, and put

    delta=1/[4(L+1)], U=68(L+1)^2=B/delta^2,
    q=U/(U+1), C_X=8+4*2^L*L,
    N0(X)=4096(L+1)^3.                                    (8)

**ASTRA-SC6-02.** For every integer X>=2 and every N>=N0(X),

    Q_(N,X)< -(4/17)^(2N+2)/(384N).                         (9)

Proof of the uniform constants. The digamma partial-fraction series gives

    0<=Omega(y)-Omega(0)
       <=(y^2/4)sum_(j>=0)(j+1/4)^(-3)<=18y^2.

Here sum<=64+8=72 by a decreasing integral comparison. Formula (6) without
its prime part gives Omega(0)<-4, using gamma_E>0, pi>3, log2>1/2 and
log pi>1. For 0<=y<=delta<=1/8, Omega(y)<-2. Also
|y log n|<=L/[4(L+1)]<1/4 for n<=X; its cosine is positive. Hence

    W_X(y)<-2                 (0<=y<=delta).               (10)

For all y>=0, the same partial fractions give Omega(y)>=Omega(0)>-8.
The standard elementary digamma remainder |psi(z)-log z|<=1/Re z gives
Omega(y)<=4+log(1+y). Further,

    sum_(2<=n<=X)Lambda(n)/sqrt(n)<2sqrt(X)log X<=2*2^L*L.

Consequently |W_X(y)|<=C_X+log(1+y)<=C_X+y.

Assume N>=U. On 0<=y<=sqrt(B)/(2sqrt(N))<=delta/2,
(y^2+1/4)^2>=1/16 and
(1+y^2/B)^(2N+2)<=exp((2N+2)/(4N))<=e<3.
The magnitude of the negative core of (7), after multiplication by
B^(2N+2), is therefore at least

    sqrt(B)/(96pi sqrt(N)).                               (11)

All the rest of [0,delta] is also negative. On y>delta use
(y^2+1/4)^2<=(B+y^2)^2, split the power 2N into N+N, and N>=2. The
absolute exterior contribution, with the same normalization, is at most

    B^2 q^N/(2pi) integral_0^infinity
                      (C_X+y)(1+y^2/B)^(-2)dy
       <= B^3(C_X+1)q^N/(2pi).                             (12)

The last integration uses pi sqrt(B)/4 and B/2, with B>1 and pi<4.
The ratio of (12) to (11) is

    48B^3(C_X+1)sqrt(N)q^N/sqrt(B).

For N>=U, Nq^N is nonincreasing. Since (1+1/U)^U>=2,
q^U<=1/2. At N=N0, N0>=60U(L+1), and

    48B^3(C_X+1)N0 q^N0
      <2^(L+28)(L+1)^4 * 2^(-60(L+1))
      <=2^(-55L-32)<1/2.                                  (13)

We used 48B^3<2^12, C_X+1<=2^(L+4)(L+1), and L+1<=2^L.
Thus the exterior is less than half the negative core, simultaneously for
all N>=N0. Equation (11) gives
Q_(N,X)<-sqrt(B)B^(-2N-2)/(192pi sqrt(N))
<-B^(-2N-2)/(384N), using sqrt(B)>2 and pi<4. QED.

The degree bound is O((log X)^3), not an optimized threshold. It is an
all-X analytic statement, not a finite-prime numerical experiment.

## 4. A completed signed inequality for the omitted literal primes

For the full heat source, the corresponding original Gamma_0 test is
exp(-2t)f_N(t), not f_N(t) without the damping. Define its absolutely
convergent full form

    Q_N=sum_A A^2/(A+4)^(2N+2).

By (2), for every N>=1,

    |Q_N|<=sum_A 2x^2/(x+4)^(2N+2)
          <=2C(x0+4)^(-2N+1)<10*25^(-N).                   (14)

No sign of Q_N is assumed in this estimate. Its exponential smallness is
just the source-derived gap x>1; no off-line zero is being excluded here.
For N>=128, elementary rational arithmetic yields

    139008*N*(289/400)^N<1.

It suffices to check N=128; N*(289/400)^N decreases for N>=3. Since
768*10*B^2<139008, (14) implies

    |Q_N|<B^(-2N-2)/(768N),                N>=128.          (15)

Subtract the finite version of (1) from the full version. Exactly,

    sum_(n>X)Lambda(n)n^(-1/2)ghat_N(log n)
                          =2pi[Q_(N,X)-Q_N].              (16)

**ASTRA-SC6-03 (signed prime-tail theorem).** For every integer X>=2,
L=ceil(log_2 X), and every integer N>=4096(L+1)^3,

    sum_(n>X) Lambda(n)/sqrt(n) * ghat_N(log n)
          < -(1/(128N))*(4/17)^(2N+2) <0.                  (17)

Proof. N0>=32768>128. Insert (9) and (15) in (16), then use 2pi>6.
All constants in (17) are rational. The definition of the Fourier transform
and the full von Mangoldt weights, including every prime power, are fixed.
The theorem gives a SIGNED infinite prime-tail bound, not its absolute norm.
It uses neither RH, finite-height RH verification, nor PNT. QED.

This is not the unrestricted matrix inequality. These rational functions
concentrate near y=0, below the elementary source-derived invariant gap.
The proof controls that deliberately selected family. It does not orient
arbitrary cross terms between prescribed basis vectors. The fact that a
signed prime inequality is proved does not make it an RH-strength estimate.

### Exact fixed-cutoff asymptotic

For each fixed X, ordinary dominated scaling y=sqrt(B/N)z in (7) gives

    lim_(N->infinity) sqrt(N)B^(2N+2)Q_(N,X)
                        =W_X(0)sqrt(B)/(64sqrt(2pi)).       (18)

The density is continuous at zero and O_X(1+log(1+y)). To justify the full
integral rather than a formal saddle, note that for N>=N_1,
(1+z^2/N)^(-2N-2)<=(1+z^2/N_1)^(-2N_1), while the remaining polynomial
and logarithmic factors have an integrable common majorant when N_1 is
large enough. The limiting integral is integral_0^infinity exp(-2z^2)dz.
Equation (14) is exponentially smaller after this normalization. Thus

    lim sqrt(N)B^(2N+2) sum_(n>X)Lambda(n)n^(-1/2)ghat_N(log n)
                           =W_X(0)sqrt(pi B)/(32sqrt(2))<0. (19)

The same proof with no retained primes gives the complete prime sum
asymptotic, with W_X(0) replaced by Omega(0). It is a low-center arithmetic
cancellation law, not an estimate in the unresolved high-resolution regime
around an arbitrary invariant parameter.

## 5. The first complete prescribed dyadic matrix is positive

**ASTRA-SC6-04 (finite certificate).** In the original unshifted Gamma_0
of the parent, the entire space V_(1,4) has a strictly positive quadratic
form. This space has the ten basis vectors

    exp(-pt), t exp(-pt),             p=1,2,4,8,16.

`interval_source.py` reconstructs the literal source at those five p's
using rational outward arithmetic and analytic remainders. It does NOT
set an uncomputed prime or zeta tail to zero. Every entry of the raw Gram
form Q is enclosed; interval LDL yields ten positive pivots. The tenth is
in the rational interval

    [4.584342053795e-48, 4.584342053796e-48].                 (20)

All ten endpoint pairs, reconstruction parameters, and the complete
recomputed matrix/jet payload hash are in certificate.json. The raw basis
metric is G_((p,r),(q,s))=(r+s)!/(p+q)^(r+s+1). LDL positivity is a
congruence statement and does not require computing G^(-1/2). The pivots
are NOT eigenvalues of the orthogonal operator compression.

For p!=q write d=q-p and a=h(p)-h(q). The exact four entries are

    Q00=a/d,
    Q10=-h'(p)/d-a/d^2,
    Q01=h'(q)/d+a/d^2,
    Q11=-(h'(p)+h'(q))/d^2-2a/d^3.                         (21)

For equal nodes and r,s in {0,1}, with h_j=[z^j]h(p+z),

    Q_(r,s)=(-1)^(r+s+1)r!s! h_(r+s+1).                   (22)

These follow by differentiating the parent's divided-difference identity.
`CERTIFICATE.md` states every analytic and rounding bound used to enclose
h_0,...,h_3. The computation uses only Python integer/rational operations.
An independent ordinary high-precision differentiation is a diagnostic,
not an acceptance premise. Independent implementation/proof review remains
required; this is not a kernel-formalized result.

## 6. The attempted global completion and exact disposition

The direct attempt was to prove positivity of the full arithmetic matrix
by first establishing positive finite gamma-plus-prime cutoffs and passing
to the completed source. ASTRA-SC6-01/02 prove that this particular premise
is false for EVERY finite cutoff, on explicitly described admissible tests.
It cannot be repaired by increasing one fixed cutoff and keeping the test
order unbounded. ASTRA-SC6-03 shows the necessary compensating tail really
has a controlled negative sign for a nontrivial infinite family.

A second attempt was to extend the now-certified first full dyadic stage
by source-jet/Schur induction. The first stage is positive, but the next
Schur complement contains signed cross terms not controlled by (17).
No order-uniform lower bound for these complements was obtained. The
finite interval proof and the tail theorem are not substituted for it.

What is still needed remains the actual all-rank sign, or an estimate
forcing the negative trace of the original operator to zero. No such
estimate is proved here. This packet therefore DOES NOT complete RH.
It supplies a completed signed arithmetic theorem, a literal-cutoff
obstruction, and a finite source-positive stage, with their scopes separated.

# A finite sufficient inequality for the exact logistic detector

Status: proposed certified component, awaiting independent rational replay and
composition review. This is a real-parameter calculation, not a zero census.
Date: 2026-10-21. The analytic adapter and global minimum-zero argument are
separate dependencies. No claim about RH or the repository's fixed-width
boundary follows from this component alone.

## 1. Domain and imported kernel

Use the Heath-Brown function w in Bellotti--Trudgian--Yang,
https://arxiv.org/html/2603.21490v1, with theta=5669/5000. Write

    k=tan(theta), c=1/k, s=sec(theta)^2, U=2theta*c,
    w(v)=s[(s theta c-1-sv/2)cos(kv)+2theta c-2-v
                    +(2c-cot(2theta))sin(kv)], 0<=v<=U,

and w(v)=0 for v>U. Its Laplace transform is W. The imported
autocorrelation/positive Fourier transform representation gives
0<=w(v)<=w(0)<6, and the elementary formula gives w'(0)=0. The compact
zero extension is C2 and piecewise C3. The independently checked elementary
constant packet gives ||w''||_infinity<1000 and U<1.1. In particular

    |w(v)-w0| <= 500 v^2                  for every v>=0.       (1)

The statement for v>U follows by integrating the globally continuous
second derivative of the zero extension, not by extending a trigonometric
formula beyond its support.

The scalar certificate covers the larger closed rectangle

    0 <= A <= 25/121,       28 <= l <= 81.                       (2)

Define c_l=log(16+10^10 exp(-l)), mu=1/(1+c_l/l), eta=A/l,
sigma=1-A/(l+c_l), alpha=2sigma-1, z0=sigma-1,
z1=sigma-1+eta and z2=sigma-eta. Then sigma>.99, eta<.0075,
alpha>.98, z0+alpha>0, z1+alpha>0 and z2>0 throughout (2).
The needed theta and polynomial coefficients are exact rational inputs.
The physical kernel uses A>0; at A=0 only the sufficient expression (5)
is extended continuously. No division by eta occurs in that expression.

## 2. A lower bound using three elementary logistic integrals

Put

    J(z,alpha)=integral_0^infinity exp(-zu)/(1+exp(alpha u)) du,
    C(z)=eta integral_0^infinity
              exp(-zu)w(eta u)/(1+exp(alpha u)) du,
    F(z)=W(z/eta)-C(z).

By (1) and 1/(1+exp(alpha u))<=exp(-alpha u),

    |C(z)-eta w0 J(z,alpha)| <=1000 eta^3/(z+alpha)^3.          (3)

Similarly, directly from the integral defining F at z2>0,

    |F(z2)-eta w0[1/z2-J(z2,alpha)]|<=1000 eta^3/z2^3.         (4)

Consequently, with a1=865534/497079,

    a1[F(z1)+F(z2)]-F(z0) >=
      a1 W(1-mu)-W(-mu)
      +eta w0[a1/z2+J(z0,alpha)-a1 J(z1,alpha)-a1 J(z2,alpha)]
      -1000 eta^3[(z0+alpha)^(-3)
                      +a1(z1+alpha)^(-3)+a1 z2^(-3)].         (5)

No sign cancellation or point approximation of w is assumed in the error.
All three absolute errors have been subtracted in the unfavorable direction.

Let aP=2919857/828465. The certificate subtracts from (5)

    w0[A aP/4 -3.0126 eta/2]+10^(-7).                         (6)

The constant packet proves that the actual archimedean constant is at
most -3.0126 and E_f(sigma)<=10^(-10)eta. The adapter and global wrapper
must justify that this and the remaining pole/zero/gamma errors fit within
the displayed 10^(-7) budget. The resulting sufficient margin is strictly
positive on all of (2).

## 3. Finite evaluation of W and J

For real |z|<=1, use

    W(z)=sum_(n=0)^24 (-z)^n M_n/n! + remainder,
    M_n=integral_0^U v^n w(v)dv.

The error is at most

    6*1.1*exp(1.1)*1.1^25/25! <10^(-20).                     (7)

Compute M_n by inserting the displayed elementary w formula. To avoid
quadrature, let C_n=integral_0^U v^n exp(ikv)dv and use

    C_0=(exp(ikU)-1)/(ik),
    C_n=U^n exp(ikU)/(ik)-n C_(n-1)/(ik).

The scalar polynomial terms integrate exactly. The implementation uses
outward intervals for every elementary function and operation; recurrence
cancellation cannot invalidate its enclosure. It can only widen it.

For b=z+alpha>0 the identity

    1/(1+exp(-alpha u))
      =(1/2) sum_(n>=0) [(1-exp(-alpha u))/2]^n

and a beta integral give

    J(z,alpha)=sum_(n>=0) T_n,
    T_0=1/(2b), T_n=T_(n-1)*n alpha/[2(b+n alpha)].

All terms are positive and T_n<=1/(2^(n+1)b). Thus retaining indices
0 through 48 leaves an error in [0,2^(-49)/b]. This is the implemented
one-sided error, not an unverified convergence estimate.

## 4. Coverage and acceptance

The producer starts with (2) and repeatedly bisects a rational coordinate
of a nonaccepted rectangle. It accepts a rectangle only if the interval
lower bound of (5)-(6) is strictly positive. The complete accepted list
therefore covers (2); common boundaries are included. A depth limit causes
failure, never acceptance. No ordinary floating point enters an acceptance
comparison. The elapsed-time field in the output has no evidentiary role.

The initial run used mpmath 1.3.0's iv context at 70 decimal digits and
accepted 32 rectangles after 63 evaluations. Its smallest reported lower
bound was greater than 0.0001167. The JSON binds the producer source by
SHA256. An independently implemented exact-rational replay is planned;
until reviewed, this output is a proposed computation certificate.

Finally, log(3*10^12)>28 and exp(21.233*(25/121))<81 are checked with
directed intervals. Thus (2) contains the entire
rectangle required by the global minimum-zero wrapper for R=4.84.
The enlarged A range eliminates any numerical classical baseline from
the global argument; positivity of the minimizing B follows from the
standard strict critical strip for nontrivial zeros.

The smallest computational failure that could invalidate the component is
an underestimated interval or omitted part of the closed rectangle. The
smallest analytic failures are the imported kernel positivity/regularity,
the explicit formula adapter, or an incorrect global error budget. These
are independent review obligations and are not authenticated by a scalar
JSON file.

# End-to-end attempt: completed steps and the unpaid arithmetic step

Goal: prove the unbounded mixed inequalities of PR790 and hence RH.
Outcome: new complete regional proofs, not full closure.

## Attempt 1: differentiate the original heat argument

The factor A^m adds a phase m arg A and a polynomial weight. A split at
B=(123/100)/t, a weighted incomplete-gamma tail, and the fixed verified
prefix close all t and m<=27, with an explicit lower bound. This is not a
formal differentiation of S>0; it estimates each differentiated sum anew.

## Attempt 2: avoid the order loss by following the saddle

Separate A=w^2+1/4 and first control sum w^(2j)e^(-tw^2). At its saddle
r=sqrt(j/t), the phase's two linear terms cancel. Complete zero counts give
positive mass on a width t^-1/2 interval. A Gaussian band sum pays every
omitted zero. This closes all j and 0<t<=10^-8.

## Attempt 3: join this interval to the low-zero-dominated tail

The late-time argument works at every order, but begins at T_m(H). With
only H=100 it cannot join all orders to the small-time interval. With the
FULL published H=3*10^12 it joins all orders m<=10^15. The proof is a
uniform parameter comparison, not an enumeration. For unbounded m,
T_m(H) grows, and a genuine intermediate interval remains.

There is no justified analytic-continuation rule for derivative signs across
that interval. The heat is analytic there, but analyticity does not preserve
inequalities. A finite-order bound is not a cofinal limit.

## Attempt 4: compress all mixed signs into one source norm

Degree elevation makes total signed Bernstein-row variation nondecreasing.
A finite Vandermonde argument proves that its exact exponential growth rate
is R(v)=sup_A (v+|A|)/|v+A|. Therefore a source-side subexponential L2 bound
for the complete Laguerre integral would imply all the mixed inequalities
and RH. This preserves finite exceptional zeros quantitatively.

The direct absolute-value estimate gives R(v)^n, not exp(o(n)). Verified
height makes R(v)-1 tiny but does not make it zero. Letting v depend on n
changes the fixed-scale problem and is not a proof. The parent's positive
heat estimate alone cannot be inserted into an oscillatory Laguerre integral
as a sign-preserving lower bound.

## The remaining theorem, in one line

For one fixed v>0, prove FROM THE LITERAL ARITHMETIC SOURCE that

    || integral_0^infinity e^(-x) S(x/v)L_n((1-z)x) dx ||_L2(|z|=1)
                                                        = exp(o(n)).

No proof of this line is supplied. It is explicitly RH-equivalent, not
claimed weaker than RH. Its value is as a cancellation-sensitive norm target,
not as another claim that naming one missing theorem resolves it.

A successful next pass must control the intermediate time/large-order
arithmetic or construct a genuinely positive source representation. Neither
source positivity, finite verified height, nor the complete zero-count
asymptotic supplies that final structure by itself.

# Proper native theta quotients have off-central real zeros at large weight

This is an analytic corollary of accepted source and cusp-norm theorems,
not a new numerical search or an additional computational test module.
The source quotient is taken BEFORE Mellin observation. No assertion about
classical zeta RH, automorphic lifts, or external priority is made.

## Frozen parents

- Actual positive theta source and its completed quotient: science
  `fdd349dcf6ba1b104e27866ae66b4c89752d5f05`, independently reviewed at
  `8b2bb44f3b82059b6e3721aba9b2cff2a70fd7d0`;
  [MP proof](CUSP_MATRIX_PERIOD_POSITIVITY.md), Sections 1--2, especially
  MP1, MP5--MP12.
- Native fixed-depth cusp chart and Petersson norm: science
  `070751bf7e96c1dbd6d4b3cfbb05dc70f5a2aa22`, independently reviewed at
  `c29ae6f3d134e076fa41aef9ae39920478f16ac0`;
  [DL proof](CUSP_FLAG_FIXED_DEPTH_DIVISOR_LADDER.md), Section 2,
  DL5--DL10 and its concluding norm estimate.

Only the source completion and norm result are imported. The period-side
divisor clusters, Schur complements AFTER Mellin observation, and their
12j/k scales are NOT used to infer zeros of the different source quotient.

## 1. Literal source and assertion

Fix an integer j>=1. For even weights k with dim S_k>=j+1, use the actual
level-one cusp spaces and the fixed coefficient functional

    V_(k,j) = {f in S_k : [q]f=...=[q^(j-1)]f=0},
    ell_j(f) = [q^j]f,
    W_(k,j) = ker ell_j in V_(k,j).

Thus V_(k,j)/W_(k,j) is one-dimensional, and W_(k,j) is nonzero.
The quotient is genuinely proper. Its scalar coordinate is ell_j=1;
the Petersson form and the modular coordinate q=exp(2*pi*i*z) are not
renormalized after seeing the Mellin parameter.

Write G_Q for the positive scalar Petersson quotient norm and H_Q(t)
for the quotient of the actual source form

    H(t)[f] = integral_F y^k |f(z)|^2 Theta_z(t) dmu(z),
    Theta_z(t) = sum_(m,n in Z) exp[-pi*t*|m*z+n|^2/y],
    dmu=dx*dy/y^2.

Explicitly,

    G_Q    = min_(ell_j(f)=1, f in V_(k,j)) G[f],
    H_Q(t) = min_(ell_j(f)=1, f in V_(k,j)) H(t)[f],
    C_Q(t) = [H_Q(t)-G_Q]/2.

These are MP's intrinsic quotient forms. In particular C_Q(t)>0, and

    L_(k,j)(s) = G_Q/[2*s*(s-1)]
               + integral_1^infinity [t^(s-1)+t^(-s)] C_Q(t) dt.   (TQ1)

The integral term is entire. The only poles are the simple endpoint poles
with residues -G_Q/2 and +G_Q/2, and L(s)=L(1-s).
The pole-cleared function Z_(k,j)(s)=s(s-1)L_(k,j)(s) is entire.

**Theorem.** For every FIXED j, all sufficiently large even k have

    L_(k,j)(1/2)>0.

Consequently L_(k,j), and hence Z_(k,j), has a sign-changing real zero in
each of (0,1/2) and (1/2,1), with the two intervals related by reflection.
No simplicity, uniqueness, zero location asymptotic, or effective weight
threshold is asserted.

## 2. A source bound that survives the quotient minimum

The standard fundamental domain contains the full cusp rectangle
-1/2<=x<=1/2, y>=1. All summands in Theta_z(t) are positive. Retaining
only m=0 and applying one-dimensional Gaussian Poisson summation gives

    Theta_z(t) >= sum_(n in Z) exp(-pi*t*n^2/y)
                = sqrt(y/t) sum_(n in Z) exp(-pi*y*n^2/t)
                >= sqrt(y/t).                                  (TQ2)

This lower bound is independent of x. For EVERY admissible f, x-Parseval
on that full unit interval gives

    integral_(-1/2)^(1/2) |f(x+iy)|^2 dx
       = sum_(n>=j) |a_f(n)|^2 exp(-4*pi*n*y)
       >= exp(-4*pi*j*y),                                      (TQ3)

because a_f(j)=1. Positivity, TQ2 and TQ3 imply, for every t>0,

    H(t)[f] >= J_(k,j)/sqrt(t),
    J_(k,j) = integral_1^infinity y^(k-3/2) exp(-4*pi*j*y) dy
            = Gamma(k-1/2,4*pi*j)/(4*pi*j)^(k-1/2).              (TQ4)

The bound is uniform over the WHOLE admissible affine space. Therefore

    H_Q(t) >= J_(k,j)/sqrt(t).                                  (TQ5)

No minimizing lift is fixed across t. No interchange of a minimum with an
integral is used. This is why the estimate applies to the proper source
quotient, rather than only to a fixed one-dimensional restriction.

## 3. The central-value criterion

At s=1/2, TQ1 becomes

    L(1/2) = -2G_Q + 2 integral_1^infinity t^(-1/2) C_Q(t) dt.

For any finite B>1, discard the positive integral beyond B and use TQ5:

    L(1/2) >= -2G_Q
               + integral_1^B [J_(k,j)/t-G_Q/sqrt(t)] dt
            = J_(k,j) log B - 2sqrt(B) G_Q.                    (TQ6)

The possibly negative pointwise lower bound for C_Q causes no problem:
it is used only on the finite interval [1,B], while the discarded tail
uses the actual positivity of C_Q.

Put R=J_(k,j)/G_Q. If R>1, choosing B=R^2 in TQ6 yields

    L(1/2)/G_Q >= 2R(log R-1).                                (TQ7)

In particular R>e is a sufficient central-positivity criterion.
Equivalently, the fixed choice B=e^2 gives L(1/2)>=2J_(k,j)-2eG_Q.
This is an exact criterion, not a numerical test or a claim of necessity.

## 4. Native quotient norm and large-weight conclusion

Let

    A_j(k)=Gamma(k-1)/(4*pi*j)^(k-1).

The same cusp restriction and Parseval argument, now without theta, gives
for every admissible f and hence its quotient minimum

    G_Q >= integral_1^infinity y^(k-2) exp(-4*pi*j*y) dy
        = A_j(k) * Gamma(k-1,4*pi*j)/Gamma(k-1).                (TQ8)

For FIXED j, the final ratio tends to one as k tends to infinity.

DL Section 2 constructs an actual modular form h_j in V_(k,j), with
a_(h_j)(j)=1 and

    G[h_j]=A_j(k)(1+o(1)),

uniformly over the six allowed even-weight residue classes. It is not a
free Fourier vector or a truncated q-series. Since G_Q<=G[h_j], TQ8 proves

    G_Q/A_j(k) -> 1.                                          (TQ9)

The incomplete-Gamma factor in J_(k,j) likewise tends to the full Gamma
factor at every fixed j. The ordinary Gamma-ratio asymptotic therefore gives

    R = J_(k,j)/G_Q
      ~ Gamma(k-1/2)/[sqrt(4*pi*j)*Gamma(k-1)]
      ~ sqrt(k/(4*pi*j)) -> infinity.                         (TQ10)

For clarity, the omitted integral from zero to the fixed lower cutoff has
at most fixed-base exponential growth in k, while Gamma(k-c) has
factorial-scale growth. This proves the incomplete/full ratios used here.
The remaining ratio is the classical
[Gamma-ratio expansion](https://dlmf.nist.gov/5.11#iii).

Thus eventually R>e, so TQ7 proves L(1/2)>0 for every sufficiently large
even weight at each fixed depth j. No effective onset is extracted from
the asymptotic. In particular k>4*pi*j*e^2 by itself is NOT asserted to be
a valid numerical threshold.

## 5. Genuine real zeros and the precise limitation

TQ1 makes L real and analytic on (0,1). Its positive residue at one gives

    L(s) -> -infinity as s approaches 1 from below.

Together with L(1/2)>0, continuity forces a sign-changing zero in
(1/2,1). Reflection gives one in (0,1/2). The function is not identically
zero, so the zeros are isolated; at least one zero in each interval has
odd multiplicity. There are no denominator poles in these intervals
against which such a zero could cancel. Multiplication by s(s-1) does
not remove either zero.

These are genuine PROPER theta-source quotients at fixed depth and
sufficiently large weight. They retain actual modular origin, positive
Petersson vacuum, smooth strictly positive source excess, completed
reflection, the positive Mellin feature kernel and only endpoint poles.
Those properties therefore do not force all completed zeros to the
critical line even after quotienting at the source level.

This theorem does NOT settle the proper weight-24 quotient's zero
geometry, select Hecke-stable flags, give the old period-side 12j/k
location law for the new source quotient, or prove a uniform theorem
when j grows with k. It is not a new automorphic L-function or an RH/GRH
counterexample. It supplies a further source-exact selection obstruction.

The argument was discovered late in the six-hour pass from the accepted
theta and cusp-norm parents. It is a post-result analytic deduction, not a
preregistered computation. Acceptance requires a separate frozen-SHA
review; the computational panel counts do not increase for this note.

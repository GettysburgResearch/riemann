# A geometric reciprocal source and an elementary positive-measure lemma

**Status:** complete proposed deductions from the stated BV/Hecke period identity and elementary Mellin arguments, not a new zero-free estimate. Classical Mobius inversion and period formulas are credited, not claimed invented.

## 1. Strengthening an existence mechanism to a proportion

Let Omega be the probability space of all ideal classes and unit-scalings in BV Section 6 for a totally complex field of degree 2m. Write E(L)=Z_L(1/2), with the source's covolume-one normalization. Its approximate functional equation gives

    E(L) >= -4/m

because both theta integrals are nonnegative at the center. If lambda_1(L)<=r_m, where

    r_m=(1+(m+4) exp(pi)/4)^(-1/m),

BV Lemma 8 gives E(L)>=1. Let A be the mean of E and let p be the probability of lambda_1<=r_m. Integrating the two lower bounds yields

    A >= p - (4/m)(1-p).

Consequently

    Prob(lambda_1>r_m) >= (1-A)/(1+4/m).              (G1)

A negative right side is replaced by zero. Since A>=-4/m, it cannot exceed one. If |A|<=a<1, the right side is at least m(1-a)/(m+4). This argument uses only a LOWER bound for E, not a false assertion that all central Epstein values are positive.

In the CM subfamily remaining after BV's geometric reduction, their stated subconvex estimate makes A tend to zero. Formula (G1) then gives a proportion at least m/(m+4)-o(1), rather than merely existence. For |A|<=1/2 it gives m/[2(m+4)]. These assertions about decay are restricted to the source's regime, not all growing-discriminant fields with unrestricted real-subfield discriminant. Possible ineffectivity in residue bounds is not removed.

This is an elementary corollary of the imported floor and mean bounds. No literature-priority claim is made. It gives a useful geometric sampling guarantee, but not a bound for a reciprocal L-function or CT's fixed-field signed pairing.

## 2. The exact class/scaling average

Now fix any totally complex F of degree 2m, discriminant D, class number h, regulator R and number w of roots of unity. Let

    C_F(t) = mean_Omega [theta_L(t)-1],       t>0,
    c_F = w/(m h R).

The probability space is compact for each fixed F, modulo rotations. Shortest primal and dual vector lengths therefore have positive uniform lower bounds. Thus C_F is smooth, nonnegative, decays exponentially at infinity, and is O_F(t^(-m)) near zero.

For Re(s)>1, termwise integration gives

    integral_0^infinity C_F(t) t^(ms) dt/t
       = c_F D^(s/2) ((2pi)^(-s) Gamma(s))^m zeta_F(s).   (G2)

This is precisely the BV Proposition 9/Hecke formula, with the theta Mellin normalization shown. It averages ALL ideal classes and the full compact unit-scaling quotient. It is not an average over an infinite unbalanced element ball.

The right side contains zeta, not 1/zeta. Merely bounding this positive period does not turn its zeros into forbidden singularities.

## 3. Two Mobius convolutions create an actual reciprocal detector

Let mu_F denote the ideal Mobius function. For j=1 or 2 define

    G_j(t) = sum_{a_1,...,a_j} mu_F(a_1)...mu_F(a_j)
               C_F(t (N a_1 ... N a_j)^(1/m)),          (G3)

over all nonzero integral ideals, including the unit ideal. Fixed-t absolute convergence follows from exponential decay and polynomial ideal counting. The same argument after differentiation proves smoothness. For every real sigma>1, Tonelli applied to the absolute integrand bounds the absolute Mellin integral by the finite Mellin integral of C_F times zeta_F(sigma)^j. Hence Fubini is legitimate on that half-plane, without RH or cancellation assumptions.

Changing variables t -> t/(N a_1...N a_j)^(1/m) then proves

    Mellin_m(G_j)(s)
      = c_F D^(s/2) ((2pi)^(-s) Gamma(s))^m
                  zeta_F(s)^(1-j).                    (G4)

For j=1, the zeta factor cancels COMPLETELY: no reciprocal detector remains. For j=2, the transform is a nowhere-zero gamma/discriminant factor divided by zeta_F(s). This is an exact alternative reciprocal source, without sextic Poisson characters or the CT correction H.

If, for some 0<b<1 and every epsilon>0,

    G_2(t) = O_(F,epsilon)(t^(-m(b+epsilon))), t->0,     (OPEN-G)

then exponential decay at infinity and Mellin convergence make (G4) holomorphic for Re(s)>b. The numerator has no zeros or poles there. Thus zeta_F has no zero in that half-plane, away from its pole at one. Taking b<11/12 would outperform the present boundary. The bound OPEN-G is NOT supplied by this packet or by BV.

## 4. Explicit unfolding exposes the remaining difficulty

For x>0 let J_1(x)=exp(-x). For m>=2 set

    J_m(x) = integral_(R_+)^(m-1)
              exp[-u_1-...-u_(m-1)-x/(u_1...u_(m-1))]
              du_1/u_1 ... du_(m-1)/u_(m-1).

This is the multiplicative convolution of m copies of exp(-x). Euler's gamma integral and Tonelli give

    integral_0^infinity J_m(x) x^s dx/x = Gamma(s)^m,
                                                       Re(s)>0.

Put Q=(2pi)^m/sqrt(D). Mellin inversion on a line Re(s)>1, or uniqueness after the logarithmic change of variables, gives

    G_1(t)=c_F m J_m(Q t^m),
    G_2(t)=c_F m sum_a mu_F(a) J_m(Q t^m N a).          (G5)

The factor m is necessary: substituting x=Q t^m introduces dt/t=dx/(m x). This explicit formula proves that the geometric route still requires a smoothed ideal-Mobius cancellation estimate. It changes the realization and possible tools, not the arithmetic content for free.

The first identity in (G5) also explains the temptation to infer a positive-source breakthrough: one Mobius convolution can indeed produce a simple positive archimedean kernel, but it has eliminated the zero detector at the same time. The second convolution restores BOTH the reciprocal and the signed difficulty. At each prime the formal identities are

    (1-x)^(-1)(1-x)=1,
    (1-x)^(-1)(1-x)^2=1-x.

These local identities are included as finite negative-control tests; they are not substitutes for (G3)--(G4)'s absolute-convergence proof.

## 5. The triangle-inequality ceiling

For each sigma>1, smoothness and the two endpoint estimates imply C_F(t)<=C_(F,sigma)t^(-m sigma) for all t>0. Applying absolute values in (G3) then gives

    |G_2(t)| <= C_(F,sigma)t^(-m sigma) zeta_F(sigma)^2.

This is a bound arbitrarily close to exponent m from above, not below it. It only recovers the original absolute-convergence half-plane. BV's geometric period estimate and discriminant-aspect subconvexity do not control the signs in (G5) as t->0 for a fixed F.

This alternative is worth retaining because it has a clean geometric interpretation and no auxiliary sextic denominator family. It also rules out a misleading shortcut: neither a single class average nor one Mobius deconvolution gives an automatic improvement over 1/12. Genuine progress requires signed cancellation in OPEN-G, or a new structure relating that sum to an estimable period.

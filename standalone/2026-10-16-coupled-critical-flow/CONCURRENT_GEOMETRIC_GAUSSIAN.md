# Concurrent #950: exact overlap and the direct Gaussian geometric corollary

**Status:** post-freeze source comparison and proposed analytic corollary. No new arithmetic cancellation bound, zero-free exponent or RH proof. The original two mathematical files and finite checker are unchanged. This added corollary has a written proof, but no independent review or new dedicated finite-census test.

## 1. What was found after the initial source freeze

A final live check found #950, at `5a6418b021a35c95bbc2c80775353ee33506faee`, published while this packet was being prepared. Its three files were then read in full:

- [MATHEMATICS.md](https://github.com/GettysburgResearch/riemann/blob/5a6418b021a35c95bbc2c80775353ee33506faee/standalone/2026-10-16-critical-geometric-lift/MATHEMATICS.md)
- [PRE_POISSON.md](https://github.com/GettysburgResearch/riemann/blob/5a6418b021a35c95bbc2c80775353ee33506faee/standalone/2026-10-16-critical-geometric-lift/PRE_POISSON.md)
- [TEST_INTERFACE.md](https://github.com/GettysburgResearch/riemann/blob/5a6418b021a35c95bbc2c80775353ee33506faee/standalone/2026-10-16-critical-geometric-lift/TEST_INTERFACE.md)

The m=6 product called U here is EXACTLY #950's K product, up to the constant C_S convention. Therefore the 3/7 domain and constant critical correction cost are overlapping component results, not a second independent analytic gain and not first established by #951. #950 additionally gives a geometric arithmetic source, profile-dependent bounds, and an actual simultaneous pre-Poisson dilation. Those contributions are credited to #950.

The distinct calculations here are the general-m coefficient budget, the weaker norm-2-only gate for unit-profile below-critical nonvanishing, the sharp one-logarithm comparison for the DIFFERENT 0/1/m source, its direct two-way Gaussian comparison, and the two-channel occupancy flow including the infinite Gaussian. #950's compact-to-Gaussian theorem uses Baire under an all-compact-test hypothesis. The following direct two-way Gaussian comparison applies its summable kernel argument without that all-test premise.

## 2. Direct constant-cost Gaussian comparison for the geometric lift

Fix F, exclude prime ideals of norm below 7, and let m>=2. For each physical row u let |a_p(u)|,|b_p(u)|<=1, with both zero at a masked prime. Let pi be any probability law on measurable prime-support profiles |z_p|<=5/3. Independence of those profiles is NOT assumed. The same profile occurs on both sides of every convolution.

Define native and geometric local series, in x=q^(-s), by

    N_p(x)=1-z_p a_p x,
    L_p(x)=1-z_p(1-1/q)a_p x/[1-b_p q^(m/2-1)x^m].       (1)

The native source uses the coefficients of product N_p. The geometric source uses product L_p. In the sextic physical family take a_p=xi_u(p), b_p=eta_p xi_u(p)^6 and m=6. This preserves the radical and every literal nonunit zero. Its positive supported exponents are 1,7,13,...; it is NOT the 0/1/6 coupled source.

Use the same Gaussian W=w_(5/6) as in CRITICAL_FACTOR_AND_GAUSSIAN.md and the same finite nonnegative row measure w. Let A_z,u(X), C_z,u(X) be the complete, untruncated Gaussian sums. For p>=1 define the same-height root envelopes with the Lp norm over w times pi.

### Corollary G

For every D>0, p>=1 and m>=2,

    E_C,p(D)<=exp(10[F:Q]) E_A,p(D),
    E_A,p(D)<=exp(10[F:Q]) E_C,p(D).                      (2)

For z_p=1 the constant exp(4[F:Q]) suffices. These are constants for ROOT NORMS, not moments raised to 2k. Neither envelope is bounded at diagonal order by this comparison.

**Proof.** Write r=1/q, y=b_p q^(m/2-1)x^m. The exact local ratio and inverse are

    L_p/N_p=1+z_p a_p x(r-y)/[(1-z_p a_p x)(1-y)],
    N_p/L_p=1-z_p a_p x(r-y)/[1-y-z_p(1-r)a_p x].         (3)

Set R=5/3. Replace numerator coefficients by absolute values and denominators by their convergent geometric majorants. At t=q^(-1/2), q^(m/2-1)t^m=r. The two positive local majorants consequently have the SAME mass

    1+2R q^(-3/2)/[(1-r)(1-Rt)].                        (4)

Since q>=7, t<2/5 and 1-r>=6/7, this is at most 1+(35/3)q^(-3/2). The argument is exactly the local critical majorant in #950; the equality q^(m/2-1)t^m=r shows it holds uniformly in m. There are at most [F:Q] prime ideals with any one integer norm, and sum_(n>=7)n^(-3/2)<=2/sqrt(6)<5/6. Thus the two multiplicative positive coefficient majorants have total critical mass at most exp(175[F:Q]/18)<exp(10[F:Q]). For R=1 the same calculation gives exp(175[F:Q]/54)<exp(4[F:Q]).

For all configurations, both coefficient arrays have absolute size at most (Nn)^(3/2): each occupied prime costs at most 5/3, while the geometric prime-power coefficient is at most the square root of its norm. Thus the Gaussian sums converge absolutely and are flat at zero. Exact Dirichlet convolution gives C=j_z*A and A=h_z*C with the SAME profile and unrestricted common prime factors. Fubini is justified by a global bound W(t)<=C_M t^(-M), M sufficiently large, and the convergent coefficient majorants.

Apply Minkowski to the full infinite convolution, using its profile-independent majorant v(n). Since X/Nn<=D for every X<=D,

    X^(-1/2)||sum_n j_z(n) A_z(X/Nn)||_Lp(w times pi)
       <= E_A,p(D) sum_n v(n)/sqrt(Nn).

The entire sum on the right is finite. No Gaussian tail has to be cut off or paid separately, and there is no independence between kernel and source in this inequality. The inverse is identical. This proves (2). QED.

This is a direct extension of #950's compact-test kernel comparison to the actual Gaussian, with uniform m and correlated profiles. It is not an improvement of #950's random-profile kernel constant, nor a replacement for the arithmetic estimate in its OPEN-LIFT.

## 3. Infinite Gaussian restoration for the geometric source

Under Mammen prime-support randomization, the cofactor for (1) is

    V=-(1-1/q)a_p sum_(j>=0) b_p^j q^((m/2-1)j)
                          C^(p excluded)(X/q^(mj+1)).    (5)

The same random coordinate multiplies the ENTIRE expression (5). At critical root weight its absolute mass is exactly q^(-1/2) for unit phases:

    (1-1/q) sum_(j>=0) q^((m/2-1)j)q^(-(mj+1)/2)=q^(-1/2).

For the Gaussian, sums over prime powers and over restored primes are absolutely justified by the same M0 and M1 argument as Section 4 of COUPLED_PRIME_FLOW.md: the deterministic coefficient bound is (Nn)^(3/2), and the sum of prime-occupancy masses is bounded by sum_n omega(n)(Nn)^(3/2)|W(Nn/X)|. Therefore #950's exact compact-support restoration extends to the full Gaussian, retaining its full cofactor (5).

Its positive reference bound also extends directly: on Re(s)=sigma>1/2, the geometric occupied-prime mass is

    (1-1/q)q^(-sigma)/[1-q^(m/2-1-m sigma)]<=q^(-sigma).

Inserting the Gaussian Rankin majorant into the proof of Theorem 5 in COUPLED_PRIME_FLOW.md proves diagonal reference size at each fixed order, with no arithmetic assumption. As before, the final Gaussian native moment equals that reference plus the signed injection minus compensation. The terminal inequality is still OPEN. The coupled 0/1/6 compensation and the geometric compensation use DIFFERENT cofactors; they cannot be identified term by term.

## 4. What the pre-Poisson result adds, and what it leaves

#950's PRE_POISSON.md supplies a genuinely earlier-stage realization: simultaneously dilate the actual additive scale X and coefficient scale Z by (Nd)^6, holding Y fixed. Its monomial identity isolates (Nd)^(3-6xi) at every frequency. The physical sum is finite by its moving row support, while the principal Gaussian dilation is infinite and its tail is cancelled by the residual. This is precisely why a bound for the principal Euler product alone is insufficient.

The next estimate should use that joint physical dilation OR the full prime-support cofactor (5) before separating signs. A bound known only on the old fixed scale curve does not apply to these off-curve arguments. The direct comparison (2), the exact dilation, and the positive compensation do not estimate the total adverse signed pairing. No full-proof claim is made from composing their identities.

## 5. Source and verification receipt

This addendum was written after reading the three pinned #950 files. Its statements have not received independent mathematical review, and the #950 checker was not replayed. The original #951 finite checks remain unchanged at 46,878 predicates and do not purport to test this new infinite-Gaussian corollary. The coefficient proof above is an exact extension of an inspected local identity, with its convergence arguments supplied. No new numerical census is advertised.

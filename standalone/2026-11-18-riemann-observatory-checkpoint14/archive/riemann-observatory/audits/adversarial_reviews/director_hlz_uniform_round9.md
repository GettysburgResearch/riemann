# Director adjudication: uniform logarithmic prime blocks

17 November 2026. I read the complete source-based proofs finite_moment63_uniform_prime_blocks.md and adjacent63_uniform_prime_blocks_skeptic.md, the independent third reconstruction uniform64_hlz_third_review.md, and the relevant HLZ shifted-theorem dependencies. I independently checked the exact local quotient, four-sign cancellation, reduced-rational error, strict-tail normalization and matrix estimate. The following is a symmetric two-sided assertion; the optional one-sided complex extension is not needed for this adjudication. The underlying use of Siegel makes the cutoff ineffective.

Assume RH. Let T_Y(U,V)=sum_(|gamma|>Y)|zeta'(rho)|²U(rho)overline(V(rho))/|rho|², B_Y=T_Y(1,1), e_m(s)=m^(−s), and L=log Y. For every fixed D,B>0, uniformly for m,n<=L^D, g=gcd(m,n),

    mn T_Y(e_m,e_n)/B_Y
      = g + O_(D,B)( g log(mn/g²)/L + L^(−B) ).

The diagonal equals m exactly. Thus the normalized Fourier transform differs from g/sqrt(mn) by O_D(1/L) in absolute value, since log x/sqrt x<=2/e. This is not a relative O(1/L) estimate when the predicted coefficient is small. For factorial Q_k=k e_k−1 the unscaled covariance error is bounded by

    O_(D,B)([g log(kl/g²)+log k+log l]/L + L^(−B)).

For prime indices up to P<=L^D this is O_D(log(2P)/L). For all integer indices it is O_D(P/L), so P=o(L) is a sufficient uniform absolute range. If Z_p=Q_p/sqrt(p−1), the centered covariance matrix on primes p<=L^D differs from identity by O_D((log L)²/L) in operator norm. Actual-variance normalization has the same order. This is growing-dimensional second-moment convergence, not a full joint law for unrestricted tests on a growing torus.

The uniform proof does not insert a fixed-polynomial constant into a growing family. It declares source length T^(1/4), pads the divisor-closed support by a baseline 8 and unit signed monomials, and uses common coefficient bounds6..10 on support. Four signs cancel the padding in the entire shifted main term before any termwise bound. The real version extracts the symmetric monomial pair. Reflection supplies the full two-sided numerator.

For the small complex shifts use separated nested Cauchy circles. With U=p^(−u), V=p^(−v), z=p^(−1−b), the local factor quotient is exactly

    V^e + (U−1)(sum_(i=0)^(e−1)U^i V^(e−1−i))(1−Vz)/(1−z).

Its departure from1 is O(e log p/log T), uniformly for p^e<=log^D T. The product therefore differs from1 by O(log(mn/g²)/log T). Comparing against the exact untwisted kernel before the outer derivatives preserves the lcm weight and removes an unnecessary common normalization error.

For source remainders, common coefficient envelopes control the initial contour and continuous moment. The shifted convolution retains its harmless n^(O(1/log T)) bound rather than a global shift-independent divisor estimate. Ng's pointwise oscillatory integral lemma gives the needed uniform summation. In the nonprincipal part every conductor q is at most log^D T, so the large-conductor error vanishes after a larger polylog split. A narrow zero-free rectangle and Siegel with epsilon D<1/2 place any exceptional zero left of the contour even after the O(1/log T) shifts. No shifted exceptional residue needs an unsupported bound. Polynomial log factors are absorbed by exp(−c sqrt(log T)); this is uniform but ineffective. The third review records exact source pages and the explicit repair of these potential interpretation traps, without declaring a source theorem false.

After outer Cauchy, the difference from the untwisted derivative sum has error O(T(log T)^3 log(mn/g²)/lcm(m,n)+T(log T)^(2−M)). Choose M after D,B, integrate the strict tail for every t>=Y, and divide by B_Y~L^4/(12 pi Y). The displayed uniform formula follows. The matrix entry bound is dominated by a constant times u_p u_q, u_p=1/sqrt(p−1); even the elementary harmonic estimate sum_(p<=P)1/(p−1)=O(log(2P)) suffices for the stated norm. The mean outer product is smaller.

At each fixed Y, arbitrary close large prime ratios still force a normalized all-prime discrepancy at least1. The proved prescribed growing range and that obstruction have different quantifiers and are fully compatible. No numerical onset height, effective Siegel constant, new unconditional zero theorem or publication-priority claim is supplied.

# Verified partial cancellation in the single Mangoldt remainder

18 November 2026. The director read the fixed-factor Poisson and Hurwitz derivations, three independent strata reviews, both inverse-prime constructions and the quantitative kernel argument. Primary inputs were checked in Ghosh's actual thesis theorem page, Baker's publisher PDF, Blomer–Harcos–Michel's journal formula, Fouvry–Shparlinski's publisher PDF and Korolev's remote journal PDF. The results below are accepted scoped deductions with bounded priority checking. They leave a long-prime contribution open and prove no new complete fourth-moment formula.

## Common formulation and choice of smoothing

Retain the Round 13 sufficient signed sum for C_*=d_2*(Lambda log²), with T comparable to Y, outer coefficients c_k of D^4, y=Y^theta and 1/2<theta=4b<2/3. Every |c_k|≤24 and each prime factor of supported k exceeds Y^a. The cutoff w_T is compactly supported at comparable positive heights, with two monotone transitions of width H=T^kappa and derivative bounds O_j(H^(−j)). Let delta=H/T. The contour application uses RH; the estimates for the arithmetic sum in this note are unconditional.

The transition exponent is freely chosen sufficiently close to one for each prescribed set of strict exponent margins. It remains fixed below one. This choice is compatible with the smooth saddle and sharp-zero-endpoint comparison. An arbitrarily small T^epsilon loss is not claimed at every previously fixed kappa. All interval slices in an averaged prime estimate have common endpoints across moduli, or are inserted by the common smooth weight and derivative envelope specified below.

## Exact effective modulus and removal of several strata

Open C_* by its Mangoldt factor nu=p^j and divisor variable n. For g=gcd(k,nu), q=k/g and M=kT/nu, the signed divisor sum is

```text
R_(k,nu)=sum_n d_2(n) w_T(2π nu n/k)
 [e(−nu n/k)−average_(u unit mod k) e(u nu n/k)].
```

The unit-group reduction to q is surjective with equal fibers. Thus it is an exact additive divisor twist at modulus q minus its unit-numerator average; q=1 gives zero. No coprimality of n is imposed. Nonempty support implies M is bounded below by a positive constant. The original support has nu≪kT.

Two independent methods give

```text
|R_(k,nu)| ≪_B M log(2+M)
       (1+H gcd(k,nu)/sqrt(kT nu))^(−B),
|R_(k,nu)| ≪_B q delta^(−2) (q²/(M delta²))^B.
```

The first bound follows from a smooth divisor hyperbola, Poisson and the exact cancellation of the resonant case q|d. It gives arbitrary saving when nu/g²≤H²/(kT) times a fixed negative power of T, for every fixed kappa>(1+theta)/2. The second follows from exact unit-independent polar cancellation in the finite Hurwitz formula and its Fourier equation, including every gcd block. Together with the trivial M log(2+M) estimate it gives O_epsilon(qT^epsilon) after choosing kappa sufficiently close to one and then a small fixed left-line exponent B>0.

All powers p^j sharing a prime with k now contribute o(T): each supported k has at most four different prime factors, and the support bounds j by a constant depending on a,b. All genuine powers j≥3 also contribute o(T), since their count up to T is O(T^(1/3)log T) and their reciprocal tail above T is O(T^(−2/3)log T). The aggregate is O(y T^(1/3+epsilon)log^C T), which saves a power for theta<2/3. The statements keep the log³nu factor and the original c_k/k weight. Applying the same count to all squares would only give y sqrt(T), so a different argument is necessary.

[Independent Poisson proof](prime101_coprime_prime_strata.md) · [Separate Mellin proof and dual phases](weighted101_single_mangoldt_strata.md) · [Third adjudication and square endpoints](uniform105_strata_adjudication.md).

## Ghosh's primary quadratic estimate removes every square in a strict range

Ghosh's 1981 Nottingham thesis, Chapter 1 §1.1, printed p.4/PDF p.12, Theorem 2 with Theorem 1's hypotheses, gives the Mangoldt prefix bound

```text
|sum_(n≤X) Lambda(n)e(alpha n²)|
 ≪_epsilon X^(1+epsilon)(q^(−1)+X^(−1/2)+q X^(−2))^(1/4),
gcd(A,q)=1, |alpha−A/q|<q^(−2).
```

The constant depends only on epsilon. Exact reduced rational phases satisfy the approximation condition and there is no further relative-length restriction. The director inspected the rendered actual theorem page; the inaccessible separate journal PDF is not described as read. Ren's journal (1.4) corroborates the formula but is not substituted for this primary check.

On k≈K and p≈X, swap the square base p and the divisor variable n. For fixed k,n reduce its unit numerator to denominator q=k/gcd(k,n). The q=1 case cancels. The estimate applies to every remaining unit numerator and to its average. Removing proper prime-power base variables and primes dividing k costs less than the X^(7/8+epsilon) term. The actual square-factor coefficient is 4 log³p. Partial summation adds the remaining logs and a taper of bounded total variation, with no T/H loss.

Summing n≪KT/X² on its gcd classes gives the block bound

```text
T^epsilon (KT/X) [K^(−1/4)+X^(−1/8)+K^(1/4)X^(−1/2)].
```

Below X=T^(1−nu0)/K use the earlier pointwise divisor estimate and choose its epsilon loss below nu0. Above this cutoff all three displayed terms decrease in X. At the cutoff they have sizes K^(7/4)T^nu0, K^(17/8)T^(−1/8+9nu0/8), and K^(11/4)T^(−1/2+3nu0/2). Taking fixed small positive margins proves a power saving for the **entire prime-square stratum** when

```text
1/2<theta<9/17, equivalently 1/8<b<9/68.
```

The endpoint is not included. This is a partial estimate for a signed arithmetic remainder, not the full fourth moment. The separate coprime genuine-prime contribution remains.

[Square proof](weighted107_quadratic_and_inverse_prime_savings.md) · [Independent source and algebra checks](geometry108_ghosh_source_qa.md) · [Third arithmetic adjudication](analytic109_arithmetic_partial_adjudication.md).

## Divisor Voronoi and averaged inverse-prime bounds

Blomer–Harcos–Michel §2.3, journal pp.708–709, (2.25)–(2.27), applies at every integer modulus k and unit additive numerator. Freeze a coprime prime factor p. Its numerator-independent main integral cancels under the principal subtraction. The two remaining phases are e(±l inverse(p)/k). With x=(kT/p)u and U=KP/T, each weight, including both the outer 1/k and Voronoi's 1/k, is

```text
B_(k,l)(p)=(kT/p)/k² integral w_T(2πT u)
                   J^±(sqrt(l(kT/p)u)/k) du,
J^−(z)=−2πY_0(4πz), J^+(z)=4K_0(4πz).
```

Baker's Theorem 2 (journal pp.351–352) bounds the average over Q<q≤2Q of the maximal unit-numerator inverse-prime annular sum by (Q^(11/10)P^(4/5)+QP^(11/12))Q^epsilon for sqrt(Q)≤P≤2Q. Fouvry–Shparlinski Theorem 3.3 (journal p.301, definition p.296) gives (Q^(13/10)P^(3/5)+Q^(13/12)P^(5/6))Q^epsilon for 1≤P≤Q^(3/2). These are annular source statements. Prefix differences at each **common** endpoint follow by dyadic decomposition; the Baker bottom prefix of size Q^(3/2) is absorbed in its displayed budget.

A uniform Bessel envelope makes the dual length affordable. For a standard two-transition taper,

```text
sum_(l≥1) d_2(l) [sup_(k,p)|B_(k,l)(p)|
                         +P sup_(k,p)|partial_p B_(k,l)(p)|]
 ≪ T^epsilon delta^(−5/2),
```

uniformly in U>0 on the polynomial scales in question. The same statement with an extra divisor-count weight holds after a polynomial cutoff and negligible tail. The factor U^(−1) in the kernel cancels the density of dual indices. Small arguments have only an integrable logarithm; large arguments have a summable bound proportional to (l/U)^(1/4)(1+delta sqrt(l/U))^(−A). Thus no positive power of U is lost, including U<1. The independent ODE proof, which transfers the prime derivative to uW'(u), gives an even smaller taper loss and checks the tail without differentiating an uncontrolled remainder. The conservative displayed loss suffices after choosing kappa near one.

Nonunit dual indices are retained. For d=gcd(k,l) the phase reduces to unit numerator l/d at modulus q=k/d. For each fixed d|l the map k=dq is one-to-one into a dyadic q block. Source maxima over unit numerators and the common derivative envelope apply there. Extra excluded primes dividing k but not q cost O(log T) per modulus; the reduced Ramanujan average costs O(T^epsilon P). The case q=1 cancels exactly. The divisor count is absorbed in T^epsilon.

Consequently for K≈T^theta, P≈T^xi, 1/2<theta<2/3, the coprime-prime dyadic contribution saves a fixed power on either of these open regions:

```text
Baker: theta/2<xi<theta,
       (11/10)theta+(4/5)xi<1,
       theta+(11/12)xi<1.

Fouvry–Shparlinski: 0<xi<(3/2)theta,
       (13/10)theta+(3/5)xi<1,
       (13/12)theta+(5/6)xi<1.
```

Use Baker when the reduced modulus exceeds P, Fouvry–Shparlinski for reduced moduli between P^(2/3) and P, and a triangle bound below that. The fallback powers P^(23/12) in the Baker region and P^(5/3) in the second region save a power under the stated inequalities. There is no least-prime-factor restriction in this gcd-resolved estimate. Constants are uniform on compact subsets after choosing the taper for those margins.

For example theta=0.60 permits xi<0.425 in the relevant Baker interval, beyond the earlier short-factor exponent 0.40. At theta=0.51 the second region reaches xi<0.537 and includes P>K. The earlier narrow transition-band proof supplies a separately checked control case. The much longer prime portion, potentially up to P≪KT, is not bounded by these regions.

[Initial primary-source match and narrow-window proof](prime107_inverse_prime_voronoi.md) · [General envelope and gcd proof](prime113_uniform_voronoi_envelope.md) · [Independent kernel proof](uniform113_bessel_kernel_mass_review.md) · [Accepted independent general-gcd adjudication](uniform115_general_prime_window_qa.md). The director read the last review and independently checked its modulus partition, source domains, fallback exponents and common endpoint argument before accepting the strengthened window.

## An alternate inverse-prime input and an excluded shortcut

Korolev's 2018 English journal theorem on pp.652–653 bounds the homogeneous unit-numerator Mangoldt inverse prefix by X^(32/37)q^(7/74+epsilon), for q^(7/10+epsilon)≤X≤q. The director read that primary PDF through the remote reader; direct local byte retrieval returned 403, so no source checksum is claimed. The later inhomogeneous theorem requiring two unit coefficients cannot be used with its linear coefficient set to zero.

Using the exact Hurwitz transform with a common short dual cutoff gives an independent local prime band near X=T^(1−theta), for 1/2<theta<10/17. The exponent there is (64+17theta)/74<1, with fixed small margins. Prime partial summation costs an additional vertical factor 1+|t| and therefore delta^(−3−2B); this cost is retained. The result is weaker than the averaged general region in relevant overlaps, but supplies an independently sourced interface. [Derivation](weighted107_quadratic_and_inverse_prime_savings.md) · [Independent actual 2018 source and contour check](geometry114_korolev_primary_qa.md).

Finally, twisting the entire sequence C_* by a character produces L(s,chi)²(−L'/L)'' in its convergent half-plane. At a simple zero rho of L this has residue −2 L'(rho,chi)²; multiple zeros of order at least two introduce no pole there. Thus an ordinary divisor/Eisenstein functional equation for the entire C_* sequence would omit zero residues. Freezing the prime factor before applying divisor Voronoi avoids that invalid substitution. No Dirichlet GRH is assumed.

The precise next step is cancellation for prime scales outside the verified regions, or a joint estimate that handles them without absolute summation of the inverse phases. An estimate for the residual plus the proved pieces would give the sufficient C_* bound from Round 13. The present partial results do not.

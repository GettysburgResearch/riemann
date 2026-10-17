# Off-central numerator fourth moments

Status: PROPOSED source-qualified deductions, awaiting independent mathematical review. No RH, native inverse-Mobius moment, or critical signed-covariance hypothesis is assumed. The large-sieve and AFE inputs below are imported, not independently rebuilt. This first checkpoint does not yet announce a new zero-free region.

## 1. Exact input and scope

Fix the field F containing mu_6, the finite set S, permissible generator choices, and the finite list of S-supported finite-order twists psi from #965 and #968. Rows a are SIXTH-POWER-FREE integral exterior ideals, ordered by FULL ideal norm Na<=U. Characters retain their original zeros at nonunits. The inducing conductor is O(Na), not necessarily comparable to Na. Angular infinite-order characters are not covered.

Adopt the pinned de Faveri sieve contract S6 in #968, head 14f544fb4293ffb59942ff8d345ab9d6da67025c, NUMERATOR_MOMENTS.md:

    sum_{Na<=U}^{6-free} |sum_{Nc<=V}^{6-free} z_c chi_a(c)|^2
       <<_eta (UV)^eta K(U,V) sum_c |z_c|^2,
    K(U,V)=U+V+U^(5/6)V^(1/3)+U^(1/3)V^(5/6).

It is essential that BOTH indices are sixth-free, rather than merely squarefree. Fixed psi multiplies common column coefficients. Positive restrictions on the rows may be retained. This statement is ascribed to de Faveri, arXiv:2610.04045v1, Theorem 1.1; fresh primary-body retrieval failed in this pass. Its exact scope is adopted from the pinned repository contract, not represented as freshly verified.

Also use the standard complete approximate functional equation and functional equation for finite-order Hecke L-functions, including their dual term, conductor weights, gamma factors and rapidly decreasing tails. BGL, arXiv:1112.1650, pp. 18-19, was freshly read for the AFE/Mellin separation and zero-detector mechanism. Neither that read nor the rational checker validates S6 or the CT theta construction.

## 2. The new off-central bounds

For every eta>0,

    sum_{Na<=U}^{6-free} |L_F^S(7/12+it,psi chi_a)|^4
        <<_eta U^(1+eta)(2+|t|)^C,
    sum_{Na<=U}^{6-free} |L_F^S(5/12+it,psi chi_a)|^4
        <<_eta U^(4/3+eta)(2+|t|)^C.                    (1)

The height exponent C may be chosen fixed for eta in a bounded positive interval; constants may depend on eta and the fixed field data. These are moments of numerator L-values, not reciprocal L-values. The central fourth-moment exponent 7/6 is already in #966/#968 and is not claimed again as new.

### Proof

First split the rows by their actual conductor norm Q into dyadic ranges. This prevents an illegal replacement of a negative conductor power by a negative power of U. We always have 1<=Q<<U. A fixed polynomial factor in 2+|t| is suppressed below.

On a Q-range, the two AFE polynomials have length Q^(1/2) times an arbitrarily small U power and a fixed height power. Separate their smooth conductor-dependent weights by Mellin inversion on a small positive line. The resulting coefficient arrays are common across the rows; imaginary conductor powers are row phases of modulus one. All Mellin integrals have polynomially weighted integrable tails. Use |A+epsilon B|^4<=8(|A|^4+|B|^4), preserving both AFE pieces and their unit-modulus root numbers. Dyadic tail intervals beyond the main length are summed with arbitrarily rapid decay. Principal bounded-conductor rows, including any AFE polar terms, are handled separately by fixed-function bounds.

After squaring either polynomial and dividing the product ideal into a dyadic range Nn~V, its coefficients have size at most (Nn)^(-s0+eta) times a harmless divisor factor, where s0 is the real line of that AFE piece. All ordered products, shared primes and distinct ideals of equal norm remain.

Write n=c d^6 uniquely, with c sixth-free. Do NOT require (c,d)=1. Then

    chi_a(c d^6)=chi_a(c) 1_{(a,d)=1}.                 (2)

For fixed d, the coefficient square mass in this product dyad is

    << V^(1-2s0+eta) (Nd)^(-6).

Indeed all n have norm comparable to V, while the c-range has length V/(Nd)^6. Apply S6 to the c-polynomial, retaining the row indicator in (2). Minkowski across d costs the convergent sum (Nd)^(-3+eta). Since K is increasing in its second argument, the fourth-moment contribution of the dyad is therefore

    << U^eta V^(1-2s0) K(U,V),                         (3)

with the usual polynomial height factor. Empty subunit c-ranges vanish. Complete AFE tails, not just their formal main lengths, obey the same argument with their rapidly decaying weights.

For the first AFE piece at s0=7/12, (3) is V^(-1/6)K(U,V). For 1<=V<=U its four terms are

    U V^(-1/6), V^(5/6), U^(5/6)V^(1/6), U^(1/3)V^(2/3),

each at most U. Small U/height power enlargements of the interval are absorbed in eta and the fixed height factor. The dyadic sum loses only logarithms.

The dual AFE piece has s0=5/12 and an exterior factor Q^(-1/12). Its fourth power is Q^(-1/3). The resulting dyadic estimate is

    Q^(-1/3) V^(1/6) K(U,V), 1<=V<<Q.

The expression V^(1/6)K(U,V) is increasing in V. Its sum over dyadic V<=Q is bounded, up to logarithms, by Q^(1/6)K(U,Q). Thus the dual contribution is at most Q^(-1/6)K(U,Q), and the same four displayed inequalities with V=Q show that this is O(U). Small conductor ranges are included; no assumption Q~U was made. Summing conductor ranges proves the first line of (1).

The functional equation, with the fixed omitted Euler factors retained, gives

    |L_F^S(5/12+it,psi chi_a)|
       << Q^(1/12)(2+|t|)^C
                   |L_F^S(7/12-it,conjugate(psi chi_a))|.

Now the conductor exponent is positive, so Q^(1/3)<<U^(1/3) is a legitimate bound after taking fourth powers. Apply the first line of (1) to the conjugate family, which satisfies the conjugate S6 inequality. This proves the second line. All auxiliary losses may be chosen sufficiently small after the requested eta. QED.

## 3. Any zero-selected subset and the saved physical exponent

For ANY subset E of at most U^nu rows, Holder gives

    sum_{a in E}|L_F^S(5/12+it,psi chi_a)|
       << U^(3nu/4+1/3+eta)(2+|t|)^C.                  (4)

The subset may depend on denominator zeros. Reciprocal and correction suprema must be bounded BEFORE applying (4); no independence is assumed.

In the actual CT monomial X^(1/2-z) Z^(xi+z-1)Y^(w-1), put X=Y=Z^a and let the top Poisson norm be U=Z^(1-a), temporarily omitting positive contour buffers. With x=Re xi, the central fourth-moment estimate at Re w=1/2 has exponent

    x-1+(1-a)(3nu/4+7/24).

Using (4) at Re w=5/12 changes this to

    x-1-a/12+(1-a)(3nu/4+1/3).

The latter is SMALLER by exactly (3a-1)/24, independently of nu. At a=4/9 this is 1/72 in the Z exponent. This is the useful change: a slightly larger L-value moment is more than offset by the physical Y factor. The move is legal only when the complete correction domain, in particular 3x+Re w>5/2, is retained. At 5/12 this requires x>25/36. The good class near x=2/3 must therefore keep its second moment at w=1/2.

A separate complete contour certificate is required before this component is used to announce a new Dedekind boundary. An inequality at the numerator alone does not establish a theta estimate or RH.

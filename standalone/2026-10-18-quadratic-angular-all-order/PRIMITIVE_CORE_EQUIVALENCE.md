# A rational, zero-preserving primitive-core source

**Status:** exact Euler-factor and convolution theorem, and a classical-RH-equivalent square-root criterion. This is a reformulation, NOT a proof of the required cancellation. It removes the angular variable from the fixed principal problem and points to a very different arithmetic target. The primitive-core idea and Euler-product comparisons are elementary/classical; no literature-priority claim.

## 1. The principal ideal source becomes a squarefree rational integer sequence

Let K be a fixed imaginary quadratic field with fundamental discriminant d_K<0 and associated real primitive Dirichlet character chi=chi_(d_K). Fix a squarefree rational Q divisible by 6*rad(|d_K|). Exclude all prime ideals over p|Q. These exclusions guarantee that every unexcluded split rational prime satisfies p>=5. Finite removed Euler factors are harmless for zero exclusion in Re s>0.

Let

    a_K(n)=sum_(NI=n) mu_K^S(I),
    A(s)=sum_n a_K(n)/n^s = 1/zeta_K^S(s), Re s>1.

Let b_K(n) be the completely explicit rational-integer function

    b_K(n)=mu(n)*2^(omega(n))  if n squarefree AND every p|n
                                 is unexcluded and chi(p)=+1;
          =0                 otherwise.

Thus

    B(s)=sum_n b_K(n)/n^s
        =prod_(p∤Q,chi(p)=+1)(1-2p^(-s)),  Re s>1.      (1)

There is NO angular character, ideal representative, theta row, or averaging in (1). At a split rational prime p, the two available prime ideals each have Mobius sign -1; selecting neither or exactly one of them produces 1-2p^(-s). Thus B(s) is exactly the original signed squarefree primitive-ideal source aggregated by rational norm, not a positive surrogate.

For K=Q(sqrt(-3)) and Q=6 this reduces simply to

    b(n)=mu(n)2^(omega(n)) 1_(all p|n satisfy p≡1 mod 3). (2)

## 2. Two invertible corrections, both supported on prime powers >=2

Define V(s)=B(s)zeta_K^S(s), so B=A*V in the Dirichlet-series sense, and W(s)=1/V(s). For unexcluded split primes write x=p^(-s):

    A_p(x)=(1-x)^2,
    B_p(x)=1-2x,
    V_p(x)=(1-2x)/(1-x)^2 =1-sum_(m>=2)(m-1)x^m,
    W_p(x)=(1-x)^2/(1-2x) =1+sum_(m>=2)2^(m-2)x^m. (3)

At unexcluded inert p, with x=p^(-s),

    A_p(x)=1-x^2, B_p(x)=1,
    V_p(x)=(1-x^2)^(-1)=sum_(r>=0)x^(2r),
    W_p(x)=1-x^2.                                      (4)

All four local series equal 1 at p|Q. There is no ramified factor because all ramified rational primes divide Q. Equations (3)-(4) are exact formal-power-series identities, with ALL p^m factors present, not an unspecified O(p^(-2s)) fudge.

For each fixed sigma>1/2, V and W are absolutely convergent ideal/rational Euler products and each has a Dirichlet series with absolutely summable coefficients weighted by n^(-sigma). At unexcluded split p>=5, the denominator 1-2p^(-s) cannot vanish when Re s>1/2 because 2/sqrt(p)<1. The first nonconstant local coefficient occurs at p^2 and the local absolute norms are O_sigma(p^(-2sigma)); summing over p converges. The inert p factors have the same p^(-2sigma) property. Thus

    V(s) and 1/V(s) holomorphic, nonzero,
    and absolutely Dirichlet-summable on every Re s>1/2+delta.   (5)

In particular, an off-critical zero of zeta_K^S(s) would produce a nonremovable pole of B(s)=V(s)/zeta_K^S(s). It cannot disappear through an angular numerator zero or a correction Euler factor in the critical right half-plane.

## 3. Exact equivalence of the two critical arithmetic cancellation targets

Write V(s)=sum_n v(n)n^(-s) and W(s)=sum_n w(n)n^(-s). Their local coefficients in (3)-(4) give exact identities

    b_K=a_K*v,    a_K=b_K*w,     v*w=delta_1.            (6)

For any epsilon>0, choose 0<delta<epsilon. If

    sum_(n<=X)a_K(n) <<_delta X^(1/2+delta),

then by (6) and (5),

    |sum_(n<=X)b_K(n)|
       =|sum_(d<=X)v(d)sum_(m<=X/d)a_K(m)|
       <<_delta X^(1/2+delta) sum_d |v(d)|/d^(1/2+delta)
       <<_delta X^(1/2+delta).                           (7)

The reverse implication is identical with w replacing v. Hence the two all-epsilon square-root criteria are EQUIVALENT, not just one-way implications:

    sum_(n<=X) a_K(n) <<_epsilon X^(1/2+epsilon) for all epsilon>0
      iff
    sum_(n<=X) b_K(n) <<_epsilon X^(1/2+epsilon) for all epsilon>0. (8)

The standard fixed-field Mobius/RH criterion identifies the first property with RH for zeta_K. One direction is particularly transparent: (8)'s second property makes B(s) converge normally by Abel summation for Re s>1/2; by (5), B/V is holomorphic there and agrees with 1/zeta_K^S initially for Re s>1. Therefore no zero of zeta_K^S lies to the right of 1/2. The functional equation gives RH for zeta_K. For the converse, RH for fixed zeta_K implies the usual X^(1/2+epsilon) ideal Mobius estimate by classical zero-free contour/Littlewood bounds for fixed-degree Dedekind zeta functions; then (7) applies.

**Therefore:**

    RH for zeta_K
      iff  for every epsilon>0,
           sum_(n<=X, squarefree, all p|n split and p∤Q)
               mu(n)2^(omega(n)) <<_(K,Q,epsilon) X^(1/2+epsilon). (9)

For K=Q(sqrt(-3)), (9) would imply RH for the ordinary Riemann zeta function AND GRH for L(s,chi_-3), because zeta_K(s)=zeta(s)L(s,chi_-3). The converse of ordinary RH alone is NOT asserted; (9) is equivalent to the stronger fixed-K Dedekind RH.

This proof requires no all-moment inequality. Equations (3)-(8) show exactly how every discarded rational content contribution is restored by an invertible critical-weight convolution. Unlike a generic angular mean, the transform preserves EACH hypothetical off-critical zero.

## 4. Why this reduction matters and why it does not finish RH

The remaining problem is a one-dimensional, fixed, unaveraged arithmetic estimate for the rational sequence (2). That is a qualitatively different research program from raising theta or angular moments: the target is cancellation in split-prime squarefree weights with the exact factor 2^(omega(n)). It is also genuinely difficult: it is RH-equivalent. The Euler correction DOES NOT generate new cancellation, and the 2^(omega(n)) is not harmless to omit.

A possible technical direction is to investigate the signed correlations of b(n) directly under a split-prime Buchstab/Heath-Brown decomposition, keeping BOTH orientations of each split prime and the complete p^2 correction. Any use of existing Möbius/additive-uniformity theorems must prove that their hypotheses apply to this unbounded multiplicative coefficient, not simply replace |b(n)| by 1. An all-logarithmic-power saving would not prove (9).

## 5. Checkability and independent inputs

A finite exact rational-prime enumerator is included as check_primitive_euler.py. For K=Q(sqrt(-3)), Q=6, it verifies (6) at EVERY n<=3000, with 9000 exact integer predicates and ordinary/optimized matching output. Those finite identities do not certify the infinite Euler products or the classical RH-to-Mobius implication.

No use is made of the proposed quasi-RH results, Dedekind 11/12 refinements, or an unproved 2k-native moment. The only external number-theoretic standard input in (9)'s converse is the classical equivalence of a fixed Dedekind zeta RH with square-root ideal Mobius cancellation. This note is meant to reveal a zero-preserving arithmetic target, not announce a proof of it.


## 6. No-loss transfer of uniform additive and polynomial-phase bounds

The same inverse Euler correction yields a useful, **unconditional implication between estimates**, not only an RH criterion. Fix beta>1/2. Suppose for all epsilon>0,

    sup_(alpha in R) |sum_(n<=X)a_K(n)e(alpha*n)|
                          <<_(epsilon) X^(beta+epsilon).  (10)

Then b_K=a_K*v and (5), with any epsilon' smaller than epsilon but beta+epsilon'>1/2, give

    sum_(n<=X)b_K(n)e(alpha*n)
       =sum_(d<=X)v(d) sum_(m<=X/d)a_K(m)e(alpha*d*m)
       << X^(beta+epsilon') sum_d |v(d)|d^(-beta-epsilon')
       << X^(beta+epsilon'), uniformly in alpha.         (11)

The reverse implication is IDENTICAL using w, because a_K=b_K*w. Therefore (10) is equivalent to the corresponding bound for b_K, at every fixed exponent beta>1/2 with the usual arbitrary epsilon loss. No exponent deterioration is caused by adding or removing the prime-power correction.

More generally, the SAME implication and converse hold with e(P(n)) and the supremum over real polynomials of any fixed degree: for each d the phase P(dm) is another polynomial of that degree. This is a transfer conditional only on having the chosen uniform phase bound for one of the sequences. It does **not** manufacture that cancellation from the Euler identity.

In particular, if #972's proposed uniform additive theorem for a_K is validated, its \`15/16+epsilon\` exponent under the imported common Dirichlet \`7/8\` strip transfers to the simple rational b_K at **exactly 15/16+epsilon**. This statement inherits all qualifications of the imported source and is **not** an improved zero-free boundary. It gives a concrete bridge for source-faithful experiments and polynomial-phase comparisons without treating b_K as a one-bounded multiplicative function.

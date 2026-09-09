# A direct Euler-factor cancellation attack: exact drift, norm blow-up, and the stopped source

**Status:** PROPOSED COMPLETE COMPONENT PROOFS; independent mathematical review required. No RH proof or new zero-free region is obtained.
**Scope:** genuine finite Euler products with the ordinary Mobius signs, their causal Cauchy-weighted norms, and a horizon-faithful prime update. All local labels EP1--EP6 belong only to this packet.
**Read parent:** PR #793 at `c4fedfcebf5226915969610281c650f452844fd8`, especially the faithful-source compiler and both preserved fifth-pass packets.
**Actual attempted final step:** use multiplicativity, rather than a sign-blind diagonal estimate, to prove a contraction as prime factors are inserted. EP2 disproves the proposed local inequality using the actual primes 2,3,5. EP3 proves a stronger obstruction to any uniformly bounded unstopped version. EP5 states the exact surviving stopped ledger without asserting its required sign.

This is a failed proof mechanism with quantitative results, not a renamed RH completion. Classical Euler products, PNT, Hilbert-space shift algebra, Plancherel, and Laguerre estimates are credited in REVIEW_AND_SOURCES.md. No external priority claim is made for these deductions.

## 1. EP1: exact source and three energies that must not be conflated

Fix a finite set of primes S (possibly omitting q=67), let Q_S be their product, and put

    P_S(s)=product_(p in S)(1-p^-s)=sum_(d|Q_S) mu(d)d^-s,
    M_S(y)=sum_(d|Q_S, d<=y)mu(d), with M_S(y)=0 for y<1,
    F_(S,a)(x)=exp(-a x) M_S(exp x), x>=0, a>0.

For empty S, Q_S=1 and M_S(y)=1 for y>=1. For nonempty S, M_S vanishes for y>=Q_S. All functions F_(S,a) belong to L2(0,infinity), without any assertion about the full infinite-prime source.

Define the physical, causal energy

    K_S(a)=integral_0^infinity |F_(S,a)(x)|^2 dx.

Finite expansion, or the Laplace transform followed by Plancherel, gives

    K_S(a)=(1/(2pi)) integral_R |P_S(a+it)|^2/(a^2+t^2)dt
          =(1/(2a)) sum_(d,e|Q_S) mu(d)mu(e)/max(d,e)^(2a).       (EP1)

The normalization is 1/(2pi), not the normalized Cauchy probability measure. In particular K_empty(a)=1/(2a).

For completeness, the Laplace calculation is

    integral_0^infinity exp(-(a+it)x)M_S(exp x)dx=P_S(a+it)/(a+it).

Alternatively expand |M_S|^2 and integrate from log max(d,e) to infinity. Both routes give EP1 and justify all interchanges because the divisor set is finite.

The diagonal of the last expression is

    D_S(a)/(2a),  D_S(a)=sum_(d|Q_S)d^(-2a)=product_(p in S)(1+p^(-2a)). (EP2)

A different average is the independent-phase or long-time energy:

    E_theta |product_(p in S)(1-p^-a exp(i theta_p))|^2 = D_S(a),
    lim_(T->infinity) (1/(2T)) integral_(-T)^T |P_S(a+it)|^2dt = D_S(a). (EP3)

The first identity follows by independence and one-circle integration. The second follows by finite Dirichlet expansion: all distinct d,e have nonzero log(d/e), so their averaged exponential tends to zero. No estimate permits replacing the weighted physical integral in EP1 by either average in EP3.

## 2. EP2: the genuine three-prime obstruction to one-step contraction

Let U_l be the right-shift isometry on L2(0,infinity): (U_lF)(x)=F(x-l) for x>=l, and zero otherwise. For p not in S, multiplicativity gives the EXACT identity

    F_(S union {p},a)=F_(S,a)-p^-a U_(log p)F_(S,a).

Define C_S(p,a)=Re <F_(S,a), U_(log p)F_(S,a)>. Then

    K_(S union {p})(a)=(1+p^(-2a))K_S(a)-2p^-a C_S(p,a).        (EP4)

The attempted proof would have required C_S(p,a)>=0 (or a comparably strong summable collective control). The individual sign is false even for the actual increasing prime chain.

Take S={2,3}, p=5. In the physical integer variable,

    M_S(y)=1 on [1,2), 0 on [2,3), -1 on [3,6), and 0 on [6,infinity).

In the correlation at shift log 5, the only overlap is x in [log 5,log 6); one factor is negative and the other positive. Therefore for EVERY a>0,

    5^-a C_{2,3}(5,a)=-(5^(-2a)-6^(-2a))/(2a)<0,
    K_{2,3,5}(a)-(1+5^(-2a))K_{2,3}(a)
                     =(5^(-2a)-6^(-2a))/a>0.                  (EP5)

At a=1 this is completely rational:

    K_{2,3}(1)=5/12,
    5^-1 C_{2,3}(5,1)=-11/1800,
    K_{2,3,5}(1)=401/900,
    excess above the diagonal update =11/900.                  (EP6)

The analytic statement holds also throughout the RH-facing range 1/2<a<1; a=1 is merely an exact numerical check. The same witness survives a finite log horizon L>=log 30, since the previous block and its shift are then entirely contained in [0,L].

This is not a counterfeit coefficient sequence. It uses mu(1), mu(2), mu(3), mu(5), and all their genuine squarefree products. It disproves local monotone-energy insertion, NOT any global Mobius cancellation theorem.

## 3. EP3: a moving-frequency profile and a sharp logarithmic energy asymptotic

Now let S_X={p<=X: p prime, p!=67}, and write P_X, K_X, D_X for this family. Fix a in (1/2,1) throughout this section. Put

    A_X(a)=sum_(p in S_X)p^-a.

The ordinary PNT and partial summation give

    A_X(a) ~ X^(1-a)/[(1-a)log X].                           (EP7)

Indeed A_X=pi_q(X)X^-a+a int_2^X pi_q(t)t^(-a-1)dt, up to the harmless initial convention, where pi_q counts the same primes. Substitution of pi_q(t)~t/log t and one integration comparison gives EP7. Removing one fixed prime changes only a bounded term. In particular A_X tends to infinity and log log X=o(A_X).

Use the analytic logarithm

    Log P_X(s)=sum_(p in S_X) log(1-p^-s), Re s>0,

where each log is the power series at p^-s=0. This specifies a single branch and does not take the principal logarithm of the finished product. Since 2a>1,

    Log P_X(a+it)=-sum_(p in S_X)p^-a exp(-it log p)+O_a(1), (EP8)

uniformly for all real t and X. To prove the error, for |z|=p^-a use

    |log(1-z)+z| <= |z|^2/[2(1-|z|)],

and sum the convergent majorant over p. Thus all prime powers of order at least two are paid with an X-independent constant here.

### Full moving-frequency limit

For every fixed V<infinity,

    sup_(|v|<=V) | Log P_X(a+i v/log X)/A_X(a) + exp(-iv) |
                                                        ->0. (EP9)

Proof. For any fixed epsilon in (0,1), the weight of primes at most X^(1-epsilon), divided by A_X(a), tends to zero by EP7. On the remaining primes,

    |log p/log X -1|<=epsilon,
    |exp(-iv log p/log X)-exp(-iv)|<=V epsilon.

Hence the normalized discrepancy is at most an o(1) term plus V epsilon, uniformly for |v|<=V. First let X tend to infinity, then epsilon decrease to zero. Combine with EP8. QED.

Consequently log |P_X(a)|/A_X -> -1, whereas

    log |P_X(a+i pi/log X)|/A_X -> +1.                     (EP10)

Thus the same exact Mobius-sign Euler product has a very small value at t=0 and a very large value at a frequency tending to zero. No hypothetical zeta zero is used to create this spike.

### Logarithmic norm asymptotic

The complete Cauchy-weighted physical energy satisfies

    log K_X(a) ~ 2 A_X(a)
               ~ 2 X^(1-a)/[(1-a)log X].                  (EP11)

Upper bound: at every t,

    |P_X(a+it)|<=product_(p<=X,p!=67)(1+p^-a)<=exp(A_X(a)).

Integrating EP1 gives K_X(a)<=exp(2A_X(a))/(2a), hence limsup log K_X/(2A_X)<=1.

Lower bound: fix eta in (0,pi/2). For t in

    I_X=[(pi-eta)/log X,(pi+eta)/log X],

EP9 gives log |P_X(a+it)| >=(cos eta-o(1))A_X, uniformly on I_X. For all sufficiently large X this interval lies in (0,1), where (a^2+t^2)^-1>=(a^2+1)^-1. Thus

    K_X(a)>=[eta/(pi(a^2+1)log X)]
                exp(2(cos eta-o(1))A_X(a)).

The logarithm of the prefactor is o(A_X). Therefore the lower limit is at least cos eta. Let eta decrease to zero and combine with the upper bound to prove EP11. No interchange of a meromorphic integral with a divergent Taylor series is present: every P_X is a finite exponential polynomial.

### Bounded diagonal versus diverging literal signed energy

For this same a, EP2 gives

    D_X(a) -> zeta(2a)/[zeta(4a)(1+67^(-2a))] < infinity.  (EP12)

Therefore the exact physical/diagonal energy ratio has the SAME logarithmic growth EP11. In particular it exceeds every fixed power of X for sufficiently large X.

This disproves any prime-cutoff-independent physical-norm bound deduced solely by multiplying the local diagonal factors, EVEN ON THE GENUINE MOBIUS EULER VECTOR. It is stronger in source fidelity than changing mu to mu^2. It is still a result about finite prime-product approximants, not about the full Mertens function or full reciprocal zeta on Re s=a.

Finite Euler products in the critical strip are a classical subject. The elementary phase mechanism and EP11 are supplied with a proof for this particular norm; external novelty has not been established.

## 4. EP4: the unstable mass escapes past the observed arithmetic horizon

The finite prime product preserves the exact ordinary 67-free Mobius coefficient for EVERY integer n<=X. Its additional coefficients are mu(n) on squarefree X-smooth numbers, with no repeated prime powers, up to the primorial Q_(S_X). It is not the raw integer truncation n<=X.

For any L>=0 define the stopped norm

    K_X(a;L)=int_0^L exp(-2a x)|M_(S_X)(exp x)|^2 dx.

Since |M_(S_X)(exp x)|<=exp x,

    K_X(a;L) <= [exp((2-2a)L)-1]/(2-2a), 1/2<a<1.         (EP13)

Combining EP11 and EP13 shows that for ANY nonnegative horizons L_X=o(A_X(a)),

    K_X(a;L_X)/K_X(a) ->0.                                (EP14)

In particular L_X=log X is allowed. On precisely that horizon,

    M_(S_X)(exp x)=M_67(exp x), 0<=x<=log X,               (EP15)

where M_67(y)=sum_(n<=y,67 does not divide n)mu(n). Thus the diverging total norm is not evidence for huge actual Mertens energy in the range where the finite product represents the full source. Almost all of this approximant's normalized energy lies farther out, where the missing primes matter.

There is a clean functional-analytic consequence. The unit vectors

    F_(S_X,a)/sqrt(K_X(a))

converge weakly to zero in L2(0,infinity): their norm on every fixed compact time interval tends to zero by EP14, and compactly supported L2 test functions are dense. Their unstopped norms cannot be used as a uniformly bounded sequence realizing the full source. No assertion that F_(S_X,a) itself converges in L2 is made.

This pinpoints the approximation issue rather than concluding incorrectly that RH must fail from EP11.

## 5. EP5: the exact stopped Euler ledger, retaining both interference and boundary loss

Return to an arbitrary finite ordered prime set p_1,...,p_J and fixed L>=0. Work in L2(0,L), and let V_p be the truncated right shift by log p. Put

    F_j(x)=exp(-a x)M_{p_1,...,p_j}(exp x), 0<=x<=L,
    E_j=||F_j||^2,
    B_j=int_(max(0,L-log p_j))^L |F_(j-1)(x)|^2 dx,
    rho_j=p_j^-a Re <F_(j-1),V_(p_j)F_(j-1)>.

Then

    F_j=(I-p_j^-a V_(p_j))F_(j-1),
    E_j=(1+p_j^(-2a))E_(j-1)-p_j^(-2a)B_j-2rho_j.        (EP16)

Proof. ||V_p F||^2=||F||^2-B_j exactly, including when log p>L. Expand the square. This preserves the endpoint loss that a full-line isometry calculation would miss.

Let d_0=1 and d_j=product_(l<=j)(1+p_l^(-2a)). Dividing EP16 by d_j and summing gives

    E_J/d_J = (1-exp(-2aL))/(2a)
               -sum_(j=1)^J [p_j^(-2a)B_j+2rho_j]/d_j. (EP17)

At p_j=5 after {2,3}, with L>=log30, B_j=0 and rho_j is the strictly negative value EP5. The proposed termwise nonnegative ledger is therefore false inside the genuine stopped prime chain as well.

Choose now every prime p<=exp L except 67. The endpoint E_J is EXACTLY

    int_0^L exp(-2a x)|M_67(exp x)|^2dx.                  (EP18)

Since d_J is bounded above and below for a>1/2, a uniform lower bound in L for the ENTIRE signed sum in EP17 would imply boundedness of EP18. If this were proved for a predetermined sequence a decreasing to 1/2, it would prove RH.

For the last implication, a finite weighted L2 norm makes the causal Laplace transform of M_67(exp x) holomorphic in Re s>a by Cauchy--Schwarz. On Re s>1 it is

    1/[s zeta(s)(1-67^-s)].

Meromorphic uniqueness then excludes every zero with Re rho>a; the finite Euler factor is nonzero there. A sequence a down to 1/2 and reflection give RH. This is the classical Mellin/Mertens endpoint in the stopped prime coordinate, not a new weaker criterion.

**The uniform lower bound for the collective signed sum in EP17 has not been proved.** EP16--EP17 are bookkeeping identities, not cancellations. Replacing rho_j by its absolute value, discarding B_j, or bounding every rho_j below by zero does not supply the missing theorem.

## 6. EP6: a polynomial prime cutoff can still falsely pass the Laguerre endpoint

For P_X and the original Laguerre coordinate define

    a_tilde_n(X)=sum_(d|Q_(S_X))mu(d)d^-3/2 L_n(2log d).

This keeps ALL squarefree products of primes at most X, not merely integers at most X. More generally attach any prime phases eta_p with |eta_p|<=1 and use the induced coefficients product eta_p on those squarefree products. The classical Laguerre inequality |L_n(t)|<=exp(t/2) gives

    |a_tilde_n(X)|<=product_(p in S_X)(1+p^-1/2),
    sum_(n=0)^N |a_tilde_n(X)|^2
            <=(N+1) product_(p in S_X)(1+p^-1/2)^2.       (EP19)

PNT and partial summation give

    log product_(p in S_X)(1+p^-1/2)
                       ~2sqrt X/log X.                 (EP20)

The error from replacing log(1+p^-1/2) by p^-1/2 is O(sum_(p<=X)1/p)=O(log X), already negligible; no sharp Mertens theorem is needed for that error. Hence EVERY schedule with sqrt(X_N)/log X_N=o(N), for instance X_N=N^2, automatically satisfies the desired subexponential UPPER growth test for these finite coefficients, for every choice of prime phases.

This is stronger than retaining a short integer interval: the largest supported integer is the primorial, whose log is asymptotic to X_N. At X_N=N^2 the largest included integer is exp((1+o(1))N^2), far beyond 1728^N, yet many integers containing a prime greater than X_N are still omitted.

The failure is visible without any unknown zeta fact. Choose eta_p=+1. The infinite positive-squarefree coefficients have generating germ

    zeta(w(z))/[(1-z)zeta(2w(z))(1+67^-w(z))],
    w(z)=1/2+(1+z)/(1-z).

Its sole pole in the disk is z=-1/3, with principal part 2delta_67/(1+3z), where delta_67=1/[zeta(2)(1+1/67)]. The remaining function is holomorphic in the disk because Re(2w)>1. Cauchy's formula gives

    a_n^+=2delta_67(-3)^n+O_r(r^-n), 1/3<r<1.

By EP19--EP20, the polynomial-prime-cutoff approximation is exp(o(n)), so its omitted tail contains asymptotically the whole 2delta_67(-3)^n signal. This positive control is not reciprocal zeta. It shows why neither primewise multiplicativity nor very large supported integers verifies the full-source endpoint without a tail bound for the actual omitted set.

## 7. Outcome and nonclaims

The local contraction was the attempted direct signed proof, and it fails by EP5. The globally unstopped replacement also fails, with the explicit actual-sign growth EP11. The stopped ledger EP17 preserves the correct source but leaves its collective arithmetic bound open.

The meaningful proven content is the exact actual-prime counterexample, the uniform moving-frequency profile, the full logarithmic norm asymptotic with bounded diagonal, the escape-of-energy statement, and the prime-cutoff Laguerre warning. None improves a known zero-free region or proves a new Mobius cancellation estimate. Routes 1 and 3 are not abandoned, but no matrix positivity result is added in this pass.

The finite checker compares independent exact Gram and step-integral formulas, updates with and without the boundary term, complete telescoping ledgers, and actual Mobius coefficients at finite horizons. It does not prove PNT, Plancherel, the infinite norm asymptotic, or RH. Independent mathematical review is still required.

# PPD26: prime-sign dephasing without losing the native RH detector

**PROPOSED component proofs; independent review required. RH and the native
subpower upper bound remain OPEN.** This is a new attack on PR848's arithmetic
bottleneck, not a proof that the old crossing covariance is nonpositive.
Parent: `99101457b32b6f10f4eda88ca998048404b860ea`.

Classical ingredients are finite-group Parseval, Euler products, causal Young
bounds, conditional expectations, Chebyshev's prime estimates and the Mertens
criterion. No priority is claimed for those tools, prime sieving, or the general
strategy of averaging twists. The quantitative growing-bank comparison, sharp
generic threshold, and their exact-source composition are proposed here.

## 1. The energy and the genuinely native family

For real X>1 define

    E_a(X) = integral_1^X |sum_(n<=u) a(n)|^2 du/u^2.

When X=N+1 is integral, this is the ENTIRE physical energy of the finite
ordinary source a(1),...,a(N), followed by coefficient -sum_(n<=N)a(n) at X.
Its cumulative function is zero thereafter. This is the previous E_N, NOT F_N
or the Newton product diagonal. No uncharged future or reciprocal-zero
normalization is assumed. The complete finite kernel is

    E_a(X)=sum_(m,n<X) a(m) conjugate(a(n))
                              [1/max(m,n)-1/X].                  (1)

At integer endpoints the convention has no effect on the integral.
Let S be ANY finite set of primes. For a sign vector epsilon in {+1,-1}^S,
let chi_epsilon be completely multiplicative, equal to epsilon_p on S and
one on other primes. Put

    a_epsilon(n)=mu(n)chi_epsilon(n),
    R_S(u)=sum_(n<=u, (n,product S)=1) mu(n),
    E_rough,S(X)=integral_1^X R_S(u)^2 du/u^2,
    A_S(X)=2^(-|S|)sum_epsilon E_(a_epsilon)(X).                  (2)

These are exactly prescribed arithmetic sequences, not independent random
values of mu. All primes outside S keep their actual Mobius signs. Set energies
to zero when their argument is <=1. The notation A_S is unrelated to the
balanced-state A_Y in the older Newton packet.

## 2. PPD26-1: exact elimination of all different small-prime parts

Let P=product_(p in S)p. Every squarefree n factors uniquely as d*r with d|P
and (r,P)=1. Hence

    sum_(n<=u)a_epsilon(n)
       =sum_(d|P)mu(d)chi_epsilon(d)R_S(u/d).

The characters chi_epsilon(d) on the finite sign cube are orthonormal.
Integrating their EXACT Parseval identity, including the changed endpoint,
gives

    A_S(X)=sum_(d|P,d<X) (1/d) E_rough,S(X/d).                    (3)

In particular

    E_rough,S(X) <= A_S(X)
      <= product_(p in S)(1+1/p) E_rough,S(X).                   (4)

There is no missing factor 2^|S|. In the pair kernel (1), averaging removes
exactly those pairs whose squarefree S-parts differ. The surviving pairs are
(d*r,d*s), with the SAME d|P and both r,s prime-to-P. Nothing claims that
correlations between distinct rough r,s have vanished.

The pair diagonal remains

    D_0(X)=sum_(n<X)mu(n)^2(1/n-1/X) <= 1+log X.                 (5)

This is NOT the old coalesced Newton-product diagonal. No earlier finite
covariance value or diagonal bound is reassigned to this new object.

## 3. PPD26-2: a two-way causal comparison, uniform over every signature

Put T=log X, and work on L2(0,T) with zero extension to negative time. Let

    U_d f(t)=d^(-1/2) f(t-log d) 1_(t>=log d),  0<t<T.

Then ||U_d||<=d^(-1/2), U_d U_e=U_(de), and U_d=0 if d>=X.
For h_a(t)=exp(-t/2)sum_(n<=exp(t))a(n), its squared norm is E_a(X).
Arithmetic Dirichlet convolution becomes the corresponding sum of U_d.
All identities below hold on this finite time interval. They do NOT identify
the separately canceled completions after time T.

For a_epsilon the finite Euler quotient relative to mu is

    R_epsilon(s)=product_(p in S)(1-epsilon_p p^(-s))/(1-p^(-s)).

At p^k, k>=1, its local coefficient is 1-epsilon_p. The inverse quotient has
coefficient (epsilon_p-1)epsilon_p^(k-1). Their absolute local norm sums at
Re s=1/2 are bounded by

    1+2/(sqrt(p)-1)=(1+p^(-1/2))/(1-p^(-1/2)).

These geometric series converge absolutely for every finite S. Define

    B_S=product_(p in S)(1+p^(-1/2))/(1-p^(-1/2)).               (6)

Young's inequality and both Euler quotient identities give, for EVERY X,S
and EVERY signature, including signatures selected using the prefix,

    B_S^(-2) E_mu(X) <= E_(a_epsilon)(X) <= B_S^2 E_mu(X).       (7)

There is no averaging hypothesis in (7). The same bounds hold for E_rough,S:
its forward multiplier is product(1-p^(-s))^(-1), and its inverse is the finite
product(1-p^(-s)); their absolute norm sums are each <=B_S. Truncation is causal,
so composing the two truncated maps is still identity on (0,T).

### An elementary explicit critical-bank bound

For S consisting of any primes <=y, and y>=exp(16),

    log B_S <= 56 sqrt(y)/log y.                               (8)

Here is a self-contained conservative prime estimate. Write
vartheta(x)=sum_(p<=x)log p. The primes in (n,2n] divide binomial(2n,n), so
summing over dyadic intervals gives vartheta(x)<4(log2)x<3x. Consequently

    sum_(p<=y) log p/sqrt(p) < 6 sqrt(y).

Split the prime sum at sqrt(y). Below it, enlarge to integers to get at most
2 y^(1/4). Above it, 1/log p<=2/log y. Since log y<=y^(1/4) for y>=exp(16),

    sum_(p<=y)1/sqrt(p) <=14 sqrt(y)/log y.

Finally log((1+a)/(1-a))<=2a/(1-a^2)<=4a for a=p^(-1/2).
This proves (8) without PNT or a zeta-zero hypothesis.

In particular, for T>=exp(8) and ANY S contained in primes <=4T^2,

    B_S^2 <= exp(112 T/log T)=X^(112/log log X).                 (9)

The very large threshold is an analytic ceiling, not a numerical experiment.
For the natural cutoff y=T^2 the constant 112 improves to 56. The integer
schedule y=(floor(log_2 X))^2 is covered by (9).

Thus exponentially many signatures can be compared to the original source at
SUBPOWER cost. Elementary Chebyshev lower bounds imply that the full bank at
y=T^2 has |S| of order T^2/log T, so a cardinality factor 2^|S| would not be
subpower. The causal comparison, not division by the family size, avoids that
loss. In particular (7) remains true at the minimizing signature.

## 4. PPD26-3: the power two threshold is sharp for generic causal norms

This theorem concerns an OPERATOR CLASS, not the actual Mobius input.
For fixed a>0 let S_T contain all primes <=T^a and define on L2(0,T)

    V_(T,a)=sum_(d S_T-smooth) U_d.

Only d<exp(T) act. Then

    lim_(T->infinity) log ||V_(T,a)|| / T
           = max(0, 1/2-1/a).                                (10)

Thus universal no-power-loss prime deletion cannot be continued past the
exponent-two polylogarithmic bank using a better bound for this same norm.
This does NOT refute a source-specific improvement beyond that bank.

For the upper bound choose 1/2<sigma<1. Its absolute coefficient mass obeys

    ||V_(T,a)|| <= exp((sigma-1/2)T)
                        product_(p<=T^a)(1-p^(-sigma))^(-1),
    log product <= C_sigma T^(a(1-sigma)).                    (11)

The second line follows by enlarging primes to integers and a geometric log
bound. Choose sigma=1/2+epsilon if a<=2; if a>2 choose
sigma=1-1/a+epsilon<1. The product term is o(T). Let epsilon tend to zero.

For the lower bound when a>2 fix 0<theta<1 and take
r=floor(theta*T/(a log T)). There are binomial(pi(T^a),r) distinct squarefree
products of r allowed primes, all at most exp(theta*T). Chebyshev gives
pi(u)>=c*u/log u eventually. For completeness, Legendre's factorial formula
implies v_p(binomial(2n,n))<=floor(log_p(2n)), so
psi(2n)>=log binomial(2n,n)>=2n log2-log(2n+1). Since
psi(u)-vartheta(u)<=3sqrt(u)log_2(u), vartheta(u)>=c*u eventually, proving the
needed lower bound. Therefore

    log binomial(pi(T^a),r) >= theta*(1-1/a)T+o(T).

Test V on f=T^(-1/2)1_(0,T). Each selected shift has scalar product at least
(1-theta)exp(-theta*T/2). Their sum gives the lower exponent
theta(1/2-1/a). Let theta increase to one. For a<=2 the identity summand and
positivity give ||V||>=1. This completes (10).
No finite computation in this packet is called an evaluation of that norm.

## 5. PPD26-4: deterministic multiplicative signing with an exact work law

The family can be searched constructively without enumerating 2^|S| members.
Fix the prime order. After some signs are fixed, group the cumulative source
by its subset r of REMAINING small primes; write the resulting functions as
f_r in L2(0,T). Conditional mean energy is

    A_j=sum_r ||f_r||^2.

For the next prime p, pair each r not containing p with r union {p}. Set

    b_j=sum_(r not containing p) Re <f_r,f_(r union {p})>.

Assign epsilon_p=-sign(b_j), with +1 at a tie. The remaining conditional
mean becomes

    A_(j+1)=A_j-2|b_j|.

At the final step there is only one function, and hence EXACTLY

    E_greedy(X)=A_S(X)-2sum_j |b_j| <= A_S(X).                   (12)

Every coefficient still has the form mu(n)chi_epsilon(n); there is no free
choice of independent signs for different integer products. All b_j are
rational at integral X, computed with the complete kernel (1). A streaming
prefix implementation needs O(|S|X) group updates and at most O(X) groups.
This is an arithmetic-operation count, not a linear bit-complexity claim.
The method of conditional expectations is classical. Its role here is to
supply a finite exact selector compatible with the uniformly controlled Euler
quotient; its energy deficit is NOT known to be subpower.

Greedy signing is not guaranteed to improve the original signature. The exact
finite corpus includes X=256, y=64, where it has energy >1.8996 while the native
energy is <1.4076. At X=16, y=16, it improves 1.0996... to 0.6758... . These are
finite performance controls, not an asymptotic improvement or disproof.

## 6. PPD26-5: full RH consumer, with no average-to-member gap

Let X_j be ANY unbounded integer sequence. At each X choose ANY prime bank
S_X contained in primes <=4(log X)^2. Any ONE of the following subpower upper
bounds along X_j would imply RH:

    A_(S_X)(X)=X^o(1);
    E_rough,S_X(X)=X^o(1);
    min_epsilon E_(a_epsilon)(X)=X^o(1);
    E_greedy(X)=X^o(1).                                       (13)

Indeed (7)-(9) compare EVERY one of these quantities with E_mu up to X^o(1),
independently of family size and of how the signs are selected. No unproved
principal-member individualization is being used. The average may be evaluated
by (3), without sampling a single signature.

Here is the complete forward implication from E_mu to RH. For X=N+1 cancel
M(N) at X to obtain a finite source C with entire energy E_mu(X). Write
h_C(t)=exp(-t/2)sum_(n<=exp t)C(n). The causal factorial source

    d(t)=exp(-t/2)[floor(exp t)(1-t)+log(floor(exp t)!)],
    Ld(z)=(s-1)zeta(s)/s^2, s=z+1/2, ||d||_1<=6

has the stated norm by integral comparison for log(n!). Finite divisor
inversion makes d*h_C equal h_*(t)=exp(-t/2)(t-t^2/2) for t<log X.
Here ||h_*||=sqrt(2), Lh_*=(s-1)/s^3. If rho=beta+i gamma were a nontrivial
zero with alpha=beta-1/2>0, evaluating transforms at rho-1/2 and applying
Cauchy-Schwarz on the COMPLETE delayed error gives

    6sqrt(E_mu(X))+sqrt(2)
        >=sqrt(2alpha)*|rho-1|/|rho|^3 * X^alpha.               (14)

Thus even arbitrarily sparse subpower energies contradict every such zero.
The classical functional equation reflects left-of-line zeros. This is the
previous causal criterion, rederived, not a new proof of its antecedent.

When the parent's proposed common-exponent theorem is used, (7)-(9) transfer
its limit 2Theta-1 to ALL quantities in (13), even with moving banks and
adaptively chosen signatures. That optional numerical-exponent identification
retains the parent's review boundary; it is not needed for (13)->RH.

## 7. PPD26-6: a forced positive mean covariance, and the actual next target

Averaging has a genuine price even on the NATIVE Mobius family. Let S contain
all primes <=y. For 1<=u<=y^2 a rough squarefree integer other than 1 is a
single prime. Therefore, exactly,

    R_S(u)=1-[pi(u)-pi(y)] for y<=u<=y^2,
    R_S(u)=1 for 1<=u<=y.                                    (15)

Chebyshev's upper/lower prime bounds from Section 4 imply

    E_rough,S(y^2) is of order y^2/(log y)^2, y->infinity.      (16)

For the lower bound use u in [y^2/2,y^2]: pi(u)-pi(y)>=c*y^2/log y eventually.
For the upper bound use pi(u)<=C*u/log u on [y,y^2], paying the initial energy
by one. Both constants are absolute; no practical first y is computed.
At y=(log X)^2, eventually y^2<X. Equations (4)-(5),(16) give

    A_S(X)-D_0(X) >= c*(log X)^4/(log log X)^2-(1+log X)>0.     (17)

This is an all-height native counterexample to the TEMPTING NEW claim that
this dephased off-diagonal must be nonpositive. It is not the old Newton
crossing covariance C_Y, so it does not refute that candidate.
A finite example is X=64, S={2,3}: mean energy >4.8784, diagonal <2.9487.

The forced cost in (16) is itself subpower. It can be paid explicitly, leaving
only the genuine rough tail

    Remainder(X,y)=integral_(y^2)^X R_S(u)^2 du/u^2.             (18)

For y=(log X)^2, subpower growth of (18) is sufficient for RH by (13).
The exact native recursion to attack is

    R_y(u)=1-sum_(y<p<=u) R_p(u/p),                            (19)

where R_p keeps primes STRICTLY greater than p. It follows by assigning a
squarefree integer its least prime factor; squares and repeated factors are
excluded. This is a classical Buchstab-type decomposition, not an assertion
that different prime branches are orthogonal.

THE MISSING THEOREM remains a subpower bound in (13), equivalently for the
rough tail, or enough accumulated signing gain in (12). The averaging identity,
subpower transfer cost, and finite greedy decreases do NOT establish it.
The new construction removes all different-small-prime-part correlations
without losing the detector, but leaves correlations among the rough cofactors.
It does not renew a fresh distribution at each Newton step or use arbitrary
completion coefficients to erase an uncharged native energy.

## 8. Evidence and boundaries

The two finite implementations reconstruct the actual mu coefficients, all
372 members of 30 declared small sign ensembles, seven larger means and greedy
runs without enumerating their 38,046,272 member occurrences, exact finite
Euler inverses, rough-cutoff integrals at rational endpoints, and strict
least-prime recursion. Code agreement is not independent mathematical review.
Finite combinatorial products check the lower-bound counting interface; they
do not numerically evaluate any asymptotic operator norm or RH limit.
See VALIDATION.md for normal/optimized runs, corruptions and non-replays.

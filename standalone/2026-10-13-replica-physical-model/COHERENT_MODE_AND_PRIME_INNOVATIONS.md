# The exact coherent mode and orthogonal prime innovations

Status: PROPOSED, complete derivation, awaiting independent review.
Scope: the literal principal-replica divisibility model from #932.
Classical ingredient: expansion in products of independent centered Bernoulli
variables (the elementary Hoeffding/ANOVA decomposition). No novelty is claimed
for that probabilistic identity or for #932's mean inverse.
New work: its exact causal dilation realization, physical comparison, and the
explicit distinction from the invariant-free phase model in #931.

## 1. A causal normalization with no unknown arithmetic coefficients

Use the preceding note's notation. For q=Np let S_q F(x)=F(x/q), and put

    R_p = S_q/(I-S_q),        pi_p=1/q,
    M_Q = product_{p notin Q}(I+pi_p R_p).

All expressions are finite when applied at a fixed horizon to a function
vanishing below 1. Infinite operator products also converge in the weighted
supremum norm M_alpha for every alpha>0.

The product M_Q and its inverse are inherited exactly from #932:

    M_p = [I-(1-1/q)S_q]/[I-S_q],
    M_p^(-1)=I-(1/q) sum_{j>=1}(1-1/q)^(j-1) S_q^j.           (1.1)

Its local nonidentity coefficient norm is O_alpha(q^(-1-alpha)), so the
products and inverse products converge. This retains duplicate norms of split
prime ideals: the equal dilation operators occur with their distinct factors.

Define the normalized physical replica and its model counterpart by

    C_w^F = M_Q^(-1) T_w F,
    C_X^F = M_Q^(-1) T_X F.                                  (1.2)

Q is fixed throughout a given experiment and all of its shorter scales, even
when Q was selected from the terminal horizon D. A genuinely scale-varying
M_{Q(x)} inside the dilation recursion is NOT being used.

The mean in the independent model is exactly

    E_X C_X^F(x)=F(x).                                       (1.3)

Thus the normalization does not suppress the unknown ordinary-zeta source.
It isolates it as the coherent mean.

## 2. Exact finite orthogonal decomposition

Set

    L_p = R_p (I+pi_p R_p)^(-1)
        = S_q/[I-(1-pi_p)S_q],
    eta_p = X_p-pi_p.

For a squarefree ideal a prime to Q, write

    eta_a = product_{p|a} eta_p,
    L_a = product_{p|a} L_p,
    v(a) = product_{p|a} pi_p(1-pi_p).

Empty products are 1 or the identity.

### Theorem 2.1
For every causal F and every finite x,

    C_X^F(x)=sum_{a squarefree,(a,Q)=1} eta_a L_a F(x).        (2.1)

Only Na<=x contribute. The same algebraic identity holds for physical w on
replacing X_p by 1_{p|w}; it does not assume physical independence.

For complex F,G and x,y,

 E_X[C_X^F(x) conjugate(C_X^G(y))]
   = F(x) conjugate(G(y))
     +sum_{a!=1} v(a) L_aF(x) conjugate(L_aG(y)).              (2.2)

In particular,

 E_X|C_X^F(x)|^2
   = |F(x)|^2 + sum_{a!=1}v(a)|L_aF(x)|^2.                   (2.3)

Proof. For each prime the exact operator identity is

    (I+X_pR_p)/(I+pi_pR_p) = I+(X_p-pi_p)L_p.

Multiply over primes and expand. The minimal dilation in L_a has norm Na,
which proves finite-horizon truncation. Independence and centering give
E eta_a conjugate(eta_b)=0 for a!=b, while E|eta_a|^2=v(a).
The random variables here are real but F and G need not be. These identities
prove (2.2) and (2.3). QED.

This is a source-preserving decomposition: the coherent term is literally
F(x), not a scalar asserted to be small, and the prime innovations act on the
same F at smaller scales.

## 3. A quantitatively summable innovation energy

Let

    ell_p(alpha)=q^(-alpha)/[1-(1-1/q)q^(-alpha)],
    V_alpha(Q)=product_{p notin Q}[1+pi_p(1-pi_p)ell_p(alpha)^2]-1.

For each alpha>0 this product converges. At a finite horizon x,

 E_X|C_X^F(x)-F(x)|^2
 <= M_alpha(F;x)^2 x^(2alpha) V_alpha(Q).                    (3.1)

Proof. The positive dilation coefficients of L_p have weighted sum
ell_p(alpha). Apply the finite source envelope to each L_a and sum (2.3)
without its coherent term. The sum over squarefree a factorizes into the
stated product. QED.

When Q contains all prime ideals q<=P,

    V_alpha(Q) <= C_{K,alpha} P^(-2alpha)                    (3.2)

for P sufficiently large. This bound uses only A(x)<=C_Kx and partial
summation: the logarithm is O_alpha(sum_{q>P} q^(-1-2alpha)). The elementary
prime Chebyshev bound improves (3.2) to O(P^(-2alpha)/log P), but this
improvement is not needed for the comparison theorem.

At alpha=1/2 the noise energy is at most O(P^(-1)) times the squared past
critical envelope. At a critical past record, this is small relative to
|F(x)|^2, not an independent upper bound for |F(x)|^2.

## 4. The physical measure can be compared without assuming F is small

Since all dilation operators commute,

    C_w^F=T_w G,   C_X^F=T_X G,   G=M_Q^(-1)F.

The previous note therefore applies to C as well as to B. In particular,
for fixed Q and r=2, alpha=1/2,

 |E_{Y,Q}|C_w^F(D)|^2 - E_X|C_X^F(D)|^2|
 <= C_{K,Q}Y^(-1/2)[log(2D)]^2 M_{1/2}(F;D)^2D.             (4.1)

Combining this with (2.3) gives a PHYSICAL lower bound

 E_{Y,Q}|C_w^F(D)|^2
 >= |F(D)|^2
    - C_{K,Q}Y^(-1/2)[log(2D)]^2 M_{1/2}(F;D)^2D.            (4.2)

The exact remainder includes all failures of orthogonality in the short ideal
annulus; none is omitted or given a sign without proof.

For Q=Q(P), the inverse norm has the stronger bound

    ||M_Q^(-1)||_alpha <= exp(C_{K,alpha}P^(-alpha)),           (4.3)

by the positive coefficient majorant in (1.1). With P=(log D)^2 and alpha=1/2,
raising (4.3) to r=O(log D/log log D) costs exp(O(1/log log D)). Hence
Theorem 4.1 of the comparison note remains valid for the normalized replicas
with the same growing-order range and the same error D^(-eta+o(1)).

At a critical past record |F(D)|=M_{1/2}(F;D)sqrt(D), equation (4.2), or its
moving-Q version, shows that the physical mean square retains (1-o(1)) of the
squared coherent signal whenever Y is a fixed positive power of D.

## 5. Why invariant-free random-phase moments cannot be imported here

The relevant adjacent source is PR #931, c77671d71dcf22a08833a6d7f86a6f15a2eba84f,
`standalone/2026-10-13-signed-moment-reassessment/COMPACT_TEST_HAAR_MOMENTS.md`
(blob e025b01c2eae6c09ebc9c6181cd9bca77ff6fc2a), Theorem 1.1.
That theorem gives model moments for invariant-free finite-group determinant
coefficients; when an invariant subspace is present it retains the target
L-function hypothesis. Its original physical discrepancy is not proved there.

Our variables are instead Bernoulli PRIME-DIVISIBILITY masks for replicas of
an already fixed deterministic F. Equation (1.3) identifies an explicit
nonzero coherent component. These are not interchangeable probability models.

For every fixed r>=1, Jensen gives

    E_X|C_X^F(D)|^r >= |F(D)|^r.                              (5.1)

More precisely, for fixed Q, fixed alpha>0 and fixed r>=1, the following
all-scale assertions are equivalent:

 (a) F(D)=O(D^alpha);
 (b) E_X|C_X^F(D)|^r=O(D^(r alpha)).                          (5.2)

The implication (b)->(a) is (5.1). For the converse, G=M_Q^(-1)F has the same
power bound. The positive replica majorant gives

 |T_XG(D)| <= C D^alpha product_{p:X_p=1}(1-q^(-alpha))^(-1).

Its r-th moment is bounded by the convergent Euler product

 product_{p notin Q}
 [1+q^(-1){(1-q^(-alpha))^(-r)-1}],                           (5.3)

because the nonconstant term is O_{r,alpha}(q^(-1-alpha)).
Finite-horizon domination and monotone convergence justify this bound. This
proves (a)->(b) without any statement about zero locations. QED.

For the specific nonvanishing Mellin test inherited from #932, (a) excludes
ordinary-zeta zeros in Re s>alpha. The cofinal versions for every alpha>1/2
are ordinary-RH-strength by #932's converse. A single exact endpoint alpha=1/2
bound is not asserted to be equivalent to RH.

Thus an unconditional diagonal moment theorem for THIS normalized model would
already contain the missing arithmetic cancellation. The physical comparison
proved here does not import #931's invariant-free conclusion into a model that
has retained the coherent signal.

## 6. Moving roughness makes the replicas uniformly coherent

This elementary bound provides a second check independent of moment comparison.
Suppose Nw<=D^rho and every prime ideal dividing w has norm>P. For alpha>0,

 K_alpha(w) = product_{p|w}(1-q^(-alpha))^(-1)-1
 <= exp[2 rho log D/(P^alpha log P)]-1                       (6.1)

when P^(-alpha)<=1/2. Indeed the number of distinct prime ideals in w is at
most rho log D/log P, and -log(1-u)<=2u in this range. Repeated prime powers
in w only decrease the possible number of distinct primes. Split-prime ideals
of equal norm are counted separately as required.

The exact recurrence implies

 sup_{1<=x<=D} |T_wF(x)-F(x)|/x^alpha
 <= K_alpha(w) M_alpha(F;D).                                 (6.2)

For P=(log D)^2 and every fixed alpha>=1/2, the right multiplier tends to zero,
uniformly over ALL such w. At alpha=1/2 it is O_rho(1/log log D).
At a large normalized past record, every rough replica has the same sign as a
real F and almost its full magnitude. A collection of these replicas cannot
be treated as many independent opportunities for sign cancellation.

### Corollary 6.1 (a single signed witness in each direction)
Use specifically the fixed real universal test W_* from #932, not an arbitrary
locally bounded source. Fix alpha>=1/2, rho>0, C0>=0, and omega(X)->infinity.
On each dyadic [X,2X], freeze P_X=(log X)^2, Q=Q(P_X) with the fixed bad
primes, and Y_X=X^rho. Use the grid

    D_i=X exp(i log(2)/N_X),
    N_X=ceil((log X)^3 omega(X)),  0<=i<=N_X.

Suppose at EVERY node of EVERY sufficiently large dyadic interval there are
possibly different bases w_+,w_- in V_Q(Y_X) satisfying

    B_{w_+}(D_i) <= C0 D_i^alpha,
    B_{w_-}(D_i) >= -C0 D_i^alpha.                            (6.3)

Then F(D)=O(D^alpha). In particular the original zero-safe detector excludes
zeros in Re s>alpha. The inequalities (6.3) themselves are unproved.

Proof. The annulus is nonempty for all sufficiently large X by Lemma 2.1 and
R_Q=X^{o(1)}. Equation (6.1) makes K_alpha(w)<=1/2 for EVERY base in that
annulus, eventually. Suppose the normalized source is unbounded and choose
alpha-past records D_* with A=|F(D_*)| and A/D_*^alpha tending to infinity.
The positive recurrence gives each base the same record sign, magnitude at
least A/2 at D_*, and magnitude at most 3A/2 on the preceding interval.
The fixed-test Taylor-Markov lemma of #932 (Lemma 2.1) then gives error
o(A)+O(X^(-2)) from D_* to its nearest preceding grid node, uniformly over
all bases. Every base at that common node still has the record sign and
magnitude at least A/4. A positive record contradicts the first witness in
(6.3), and a negative record contradicts the second. This proves the endpoint
bound. The Mellin conclusion is the existing #932 detector implication. QED.

This is a corollary of the existing capture argument with a new explicit
moving roughness choice. It changes the observation count, not the source-bound
problem; it is not a way around the coherent-mode identity (1.3).

## 7. Result of the attempted combination

The intended combination was: use the exact ordinary-zeta bridge from #932,
then supply its statistical observations through the independent-prime moment
technology in #931. The comparison obstacle can be paid for the
principal-divisibility model, even at growing moment orders. However, the exact
normalization shows why the last step fails: the random model contains F as
its mean. Random prime innovations are not the sought-after cancellation of F.

A next RH-relevant estimate must control that coherent term using the literal
Möbius coefficients, or control the original norm-filtered signed covariance
in the NONPRINCIPAL phase family. Centering, sampling more replicas, or importing
an invariant-free model theorem does not establish either estimate.

No zero-free constant, full native fourth moment, generalized undamped moment
hierarchy, or zero-height shrinking band is proved in this packet.

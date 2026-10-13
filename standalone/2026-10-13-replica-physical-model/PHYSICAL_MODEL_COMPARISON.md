# Physical principal replicas: critical and growing-order moment comparison

Status: PROPOSED, with a complete written derivation; not independently reviewed.
Scope: ordinary-zeta principal replicas indexed by Eisenstein ideals, not the full sextic character family.
Exact source: PR #932, c63b5aaa5d53dd183abb20299cea4628f0ab57b7,
`standalone/2026-10-13-principal-zeta-bridge/PRINCIPAL_REPLICA_AVERAGES_AND_CONVERSE.md`
(blob 873769f256fe4025800f34eebbf0c21ca21d1517), especially (1.2) and Theorem 2.1.
New contribution: an r-linear comparison, the critical logarithmic cost, explicit dependence on a growing roughness set, and a comparison uniform in growing moment order.
Smallest remaining gap: an upper bound for the coherent ordinary Möbius source. None of the results below supplies it.

## 1. Source, measure, and finite horizons

Fix K=Q(sqrt(-3)). All lower-case Gothic prime indices denote PRIME IDEALS.
Distinct split prime ideals with the same rational norm are distinct throughout.
For an integral ideal a, write Na for its norm and rad(a) for its squarefree
prime-ideal radical.

The exact source identity from #932 is

    F(D) = sum_n mu(n) W(n/D),
    B_w(D) = T_w F(D) = sum_{rad(d)|w} F(D/Nd).

Here B_w is shorthand for the original row B_{w^6}, not B_w in the original
sextic notation. The fixed companion filter and finite Euler restoration have
already been applied. No additional character or nonunit mask is discarded.

For the arguments it is enough that F is any locally bounded complex function
which vanishes below a positive fixed scale. Rescale that scale to 1. Every
sum at a fixed horizon D is then finite. Compact smooth Möbius sources satisfy
these conditions. The theorems do not assume any asymptotic estimate for F.

For a finite prime-ideal set Q, define

    V_Q(Y) = {w : (w,Q)=1, Y/2 < Nw <= Y},
    J_Q^circ(Y) = |V_Q(Y)|,
    d_Q = product_{p in Q}(1 - 1/Np),
    e_Q = product_{p in Q}(1 + (Np)^(-1/2)),
    R_Q = e_Q/d_Q.

Empirical expectation E_{Y,Q} uses uniform measure on V_Q(Y). The independent
model has independent variables X_p in {0,1}, for p outside Q, with

    P(X_p=1) = 1/Np.

Set X_rad(d)=product_{p|d} X_p and

    T_X F(x) = sum_{(d,Q)=1} X_rad(d) F(x/Nd).

Only primes of norm at most x occur. There is no independent sextic root-of-unity
phase here: this is a PRIME-DIVISIBILITY model for principal replicas.

## 2. Uniform rough-annulus density, including growing Q

### Lemma 2.1
There are constants c,C depending only on K such that, whenever
Y >= C R_Q^2, the annulus is nonempty, J_Q^circ(Y) >= c d_Q Y, and for every
squarefree ideal a prime to Q,

    |P_{Y,Q}(a|w) - 1/Na| <= C R_Q Y^(-1/2) (Na)^(-1/2).       (2.1)

The assertion is uniform in a and Q. In particular it includes Na>Y, where
the physical probability is zero.

Proof. The elementary Eisenstein lattice count gives
A(x)=# {ideals w:Nw<=x}=kappa x+O_K(sqrt(x)) for all x>0, setting A(x)=0
for x<1. For x>=1 this follows by counting lattice points in a disk, using
class number one and dividing the six nonzero generators of each ideal.
For 0<x<1 the same error bound is immediate.

Finite inclusion-exclusion therefore gives, with an ABSOLUTE K-dependent error,

    A_Q(x)=kappa d_Q x + O_K(e_Q sqrt(x)).                       (2.2)

Consequently J_Q^circ(Y)=kappa d_Q Y/2+O_K(e_Q sqrt(Y)), giving the
denominator bound at the declared threshold. Multiplication by a is a bijection
onto bases divisible by a, since (a,Q)=1; it imposes no coprimality between a
and the remaining quotient. Thus the probability is exactly

    [A_Q(Y/Na)-A_Q(Y/(2Na))]/J_Q^circ(Y).

Subtract 1/Na and use (2.2). The two errors are bounded by a constant times
R_Q Y^(-1/2)[(Na)^(-1/2)+(Na)^(-1)], proving (2.1). Alternatively, for Na>Y,
1/Na <= Y^(-1/2)(Na)^(-1/2). QED.

This is the explicit-Q version of the fixed-Q density calculation already
in #932. That first-order calculation is not claimed as a new result.

## 3. Joint moments, not only the mean

For alpha>0 define the finite, possibly unknown, source norm

    M_alpha(F;x)=sup_{1<=t<=x} |F(t)|/t^alpha.

Let r>=1 be an integer, let x_j in [1,D], and allow arbitrary complex causal
F_j. Conjugation can be included by replacing a chosen F_j by its conjugate.
Define the positive coefficient sum

 S_{r,alpha,Q}(D) =
 sum_{Nd_j<=D, (d_j,Q)=1}
   [N rad(d_1 ... d_r)]^(-1/2) product_j (Nd_j)^(-alpha).        (3.1)

### Theorem 3.1 (finite r-linear comparison)
Under the threshold in Lemma 2.1,

 | E_{Y,Q} product_j T_w F_j(x_j)
       - E_X product_j T_X F_j(x_j) |
 <= C_K R_Q Y^(-1/2) S_{r,alpha,Q}(D)
        product_j [M_alpha(F_j;x_j) x_j^alpha].                (3.2)

Proof. Expand the finite product. A tuple (d_1,...,d_r) contributes the
indicator rad(d_1...d_r)|w. In the independent model its expectation is
1/N rad(d_1...d_r), since X_p is idempotent and its mean is 1/Np.
Use (2.1) and the defining bound on each F_j. This proves (3.2) without
interchanging infinite sums or assuming independence of physical bases. QED.

In particular, for r=2k this compares the actual nonnegative 2k-th moment of
principal replicas with the divisibility model. It does NOT compare the original
all-row sextic moment with a random multiplicative phase model.

### Theorem 3.2 (fixed orders above and at the critical exponent)
For fixed r and alpha>1/2,

    S_{r,alpha,Q}(D) <= C_{K,r,alpha},                         (3.3)

uniformly in D and Q. At alpha=1/2,

    S_{r,1/2,Q}(D) <= C_{K,r} [log(2D)]^r.                    (3.4)

Thus the comparison error is genuinely square-root in the replica-base height
Y; at the critical exponent it costs only a fixed power of log D, relative to
the finite critical source norms.

Proof. For (3.3), remove the finite horizons. The Euler product is

 product_{p notin Q}
 [1 + q^(-1/2){(1-q^(-alpha))^(-r)-1}], q=Np.

Its nonconstant local term is r q^(-alpha-1/2)+O_{r,alpha}(q^(-2alpha-1/2)).
The product converges for alpha>1/2 by the ideal counting bound A(x)<=C_K x.

For (3.4), insert epsilon=1/log(2D). Since product_j Nd_j<=D^r,
the finite sum is at most exp(r) times the same Euler product with each
alpha replaced by 1/2+epsilon. For fixed r, its local factor is
1+r q^(-1-epsilon)+O_r(q^(-3/2)). Dividing by the local factors of
zeta_K(1+epsilon)^r leaves a bounded product, uniformly in 0<epsilon<=1.
The finitely many small primes cause only a constant depending on r.
Finally zeta_K(1+epsilon)<=C_K/epsilon follows by partial summation from
A(x)<=C_K x. No RH, prime ideal theorem, or Mertens asymptotic is used. QED.

The appearance of M_{1/2}(F;D) in (3.2) is essential: for the actual Möbius
source this norm has NOT been bounded uniformly or by D^epsilon here.

## 4. An explicit high-order estimate

Let Q contain every prime ideal of norm at most P. Additional fixed bad primes
are harmless. Assume D>=2 and P>=(4r)^2. Then

 S_{r,1/2,Q}(D)
 <= [C_K log(2D)]^r exp(C_K r^2/sqrt(P)).                      (4.1)

All constants in this display are independent of r, D, P.

Proof. Use the preceding Rankin insertion. For q>P put z=q^(-1/2-epsilon).
Then rz<=1/4, and the elementary Taylor bound gives

    (1-z)^(-r) = 1+rz+O(r^2 z^2),

with an absolute implied constant for this range. The logarithm of the local
Euler factor is consequently at most

    r q^(-1-epsilon) + C r^2 q^(-3/2).

The first prime-ideal sum is at most log zeta_K(1+epsilon). The second is
O_K(P^(-1/2)) by ideal counting and partial summation. Absorb exp(r) from the
Rankin insertion into C_K^r. This proves (4.1). QED.

An elementary Chebyshev bound for rational primes also yields

    log R_{Q(P)} <= C_K sqrt(P)/log(2P)                       (4.2)

for P sufficiently large, with any fixed bad primes incorporated in C_K.
Indeed each rational prime produces at most two degree-one prime ideals, or a
degree-two prime ideal. Hence pi_K(t)<=C_K t/log(2t). Partial summation bounds
sum_{q<=P}q^(-1/2) by O(sqrt(P)/log P) and sum_{q<=P}q^(-1) by O(log log P).
Expand log(1+q^(-1/2))-log(1-q^(-1)). The latter O(log log P) is absorbed
into the displayed bound. The rational Chebyshev input and its binomial proof
are classical; a primary exposition is Terence Tao, 254A Notes 1 (2014),
https://terrytao.wordpress.com/2014/11/23/254a-notes-1-elementary-multiplicative-number-theory/ .

### Theorem 4.1 (growing-order critical comparison)
Fix rho>0 and eta with 0<eta<rho/2. Put

    Y=D^rho,  P=(log D)^2,
    Q=Q(P) together with the fixed bad-prime set.

Q is frozen throughout the experiment at this terminal D. Suppose

    1<=r <= (rho/2-eta) log D/log log D.                       (4.3)

For all sufficiently large D, uniformly in these integer orders and in the
functions/scales in Theorem 3.1,

 | E_{Y,Q} product_j T_w F_j(x_j)
      - E_X product_j T_X F_j(x_j) |
 <= D^(-eta+o(1)) product_j [M_{1/2}(F_j;x_j) sqrt(x_j)].      (4.4)

The o(1) is uniform in r under (4.3), for fixed rho,eta,K and fixed bad data.

Proof. We have r/sqrt(P)=O(1/log log D), so P>=(4r)^2 eventually.
Equation (4.2) gives R_Q=D^{o(1)}, so the annulus threshold holds.
The logarithm of the factor in (3.2), after applying (4.1), is at most

 -rho/2 log D + O(log D/log log D)
   + r log log(2D)+O(r)+O(r^2/log D).

By (4.3) this is at most -eta log D+o(log D), as claimed. QED.

For one source and r=2k,

 |E_{Y,Q}|T_wF(D)|^(2k)-E_X|T_XF(D)|^(2k)|
 <= D^(-eta+o(1)) M_{1/2}(F;D)^(2k) D^k.                    (4.5)

In the original replica parametrization H=D^h and Y=H^(1/6), rho=h/6.
The allowed TOTAL moment order is therefore

    2k <= (h/12-eta) log D/log log D.

This quantitative statement concerns principal-divisibility replicas only.
It does not give an undamped native sextic moment at growing k, an RH bound,
or a height-dependent band in the ordinate of a zero.

## 5. A useful sanity check and the unresolved mean

Take F(x)=x^beta for x>=1 and zero below 1, with beta>1/2. This causal source
has large critical source norm. The physical/model comparison remains valid.
Both models have a large coherent contribution; the comparison cannot make it
square-root-sized. Smoothly cutting off the same example near 1 gives the same
asymptotic test with smoothness.

For the Möbius source, no bound for M_{1/2}(F;D) is proved. The next note gives
an exact orthogonal decomposition identifying this coherent contribution.
The point of (4.5) is to isolate model error without falsely treating the
unknown source norm as a constant.

## 6. Evidence boundary

The finite diagnostic tests the exact r-linear density expansion, including
repeated ideal norms and high-radical tuples exceeding the physical row height.
It does not prove (2.2), a uniform big-O constant, the Euler estimates, or an
asymptotic moment theorem. Those claims rest on the written proofs above.
No independent reviewer, Lean build, or external acceptance is claimed.

# Arithmetic coercivity and a uniform shell-compactness route to RH

**Status: PROPOSED component theorems; independent mathematical review required.**
**The uniform compactness assertion Q-AC26 is OPEN. RH is not proved.**

This is a different attack from the signed-kernel mode calculation in PR837.
We impose every finite divisor equation and ask for a lower singular-value
estimate on one explicit integer matrix. The main connection is exact: the
full inverse operator costs at most a logarithmic factor beyond the literal
odd-Mobius energy. A sufficient scale-to-scale compactness estimate is then
isolated without discarding the coupling to the previous scales.

Arithmetic matrix approaches to RH are classical; in particular see
Bordelles--Cloitre (2009), Section 2.2. No priority claim is made for using
triangular integer matrices, incidence inversion, singular values, or compactness
arguments. The precise normalization, trace identity, ternary-shell contract,
and countermodel below are the proposed objects of this packet. Sources and
inspection levels are in SOURCES.json. All norms below are ordinary Euclidean
norms, and all matrices act on complex vectors unless otherwise stated.

## 0. Source, endpoint and norm conventions

Use the actual Mobius function, restricted to positive odd integers:

    M(x)=sum_(n<=x, n odd) mu(n),
    m(x)=sum_(n<=x, n odd) mu(n)/n,
    Q(x)=M(x)-x m(x),
    E(X)=integral_1^X m(t)^2 dt.

Set M,m,Q to zero below 1 and E(X)=0 for X<=1. An endpoint X in a finite
matrix is always an ODD integer at least 3. Its index set is

    O_X={1,3,...,X-2};       N_X=(X-1)/2.

Thus X is EXCLUDED from the vector; each included index is the left endpoint
of an interval of length two. This convention is essential for exact energy
and trace identities. No numerical zero data is used.

For v indexed by O_X, set v_(-1)=0 and define

    (Delta_X v)_d=v_d-v_(d-2),
    D_X=diag(d: d in O_X),
    Z_X(n,d)=1_(d divides n),
    B_X=Z_X D_X Delta_X.

Explicitly,

    (B_X v)_n=sum_(d|n) d(v_d-v_(d-2)).                  (0.1)

The symbol Z_X is a finite incidence matrix, not the zeta function. We use
Z_o(s)=(1-2^(-s))zeta(s) for the analytic odd Euler factor.

For example, at X=7,

             [ 1  0  0 ]
    B_7 =    [-2  3  0 ],
             [ 1 -5  5 ]

and B_7(1,2/3,7/15)^t=e_1. The matrix contains only divisor data; its solution
contains the Mobius harmonic sums. Eigenvalues and singular values are not
interchangeable in this nonnormal system.

## 1. AC26-1: exact finite inverse and complete trace

### Theorem

B_X is invertible, lower triangular, with diagonal d in O_X. Its inverse V_X
has entries

    V_X(n,d)=m(n/d)/d.                                  (1.1)

In particular B_X(m(n))_(n in O_X)=e_1, and

    E(X)=2 ||V_X e_1||_2^2,                             (1.2)
    2 ||V_X||_HS^2=sum_(d in O_X) E(X/d)/d.              (1.3)

Writing h_X=sum_(d in O_X)1/d and kappa(X)=||V_X||_op^2 gives

    E(X)/2 <= kappa(X) <= ||V_X||_HS^2 <= h_X E(X)/2.     (1.4)

All identities include the endpoint terms. In particular this is an
operator-norm comparison, not a claim that the first column maximizes the norm.

### Proof

Finite divisor inversion gives
Z_X^(-1)(n,d)=1_(d|n) mu(n/d). Solve B_X v=f in three steps:

    a_n=sum_(d|n)mu(n/d)f_d,
    v_n=sum_(k<=n, k odd) a_k/k
       =sum_(d<=n, d odd) (f_d/d) sum_(r<=n/d, r odd)mu(r)/r.

This proves (1.1) and the source equation. Lower triangularity also directly
gives det(B_X)=product_(d in O_X)d. All its eigenvalues are those same positive
integers; nothing here estimates its least singular value.

The function m(t) is constant on each [n,n+2), n odd, so (1.2) follows. For
fixed odd d, the jumps of m(t/d) occur at odd multiples of d and therefore
at points of the SAME grid. Consequently, exactly,

    2 sum_(n in O_X) m(n/d)^2/d^2
       =d^(-2) integral_1^X m(t/d)^2 dt
       =d^(-1) E(X/d).

The portion below t=d has zero integrand. Summing over d proves (1.3).
The first column lower-bounds the operator norm, the operator norm is bounded
by the Hilbert--Schmidt norm, and E(X/d)<=E(X), proving (1.4). QED.

### Finite Euler factorization

Let (S_p v)_n=1_(p|n)v_(n/p) for each odd prime p<X. These finite shifts commute
and are nilpotent. Unique prime factorization gives the exact identities

    Z_X=product_(p<X, p odd prime)(I-S_p)^(-1),
    Z_X^(-1)=product_(p<X, p odd prime)(I-S_p).

Every inverse is a finite geometric sum. No convergence of an infinite Euler
product in a critical half-plane is asserted or used. The computational
checker reconstructs Z_X both from divisibility and from these finite factors.

## 2. AC26-2: the full coercivity estimate is RH-equivalent

### Theorem

The following assertions are equivalent:

(a) RH;
(b) E(X)=O_epsilon(X^epsilon) for every epsilon>0;
(c) kappa(X)=O_epsilon(X^epsilon) for every epsilon>0, on odd X;
(d) for every epsilon>0 there is c_epsilon>0 such that, for ALL odd X>=3
    and ALL v in C^(N_X),

    ||B_X v||_2^2 >= c_epsilon X^(-epsilon) ||v||_2^2.    (2.1)

It is enough to establish (b), (c), or (d) on X=3^r. This is an exact
reformulation/bridge, NOT a proof of any of these global estimates.

### Proof of the analytic bridge

At each odd integer the jumps of M and x m cancel. Thus Q is continuous,
locally absolutely continuous, Q(1)=0, and Q'=-m almost everywhere. Expanding
M=Q+x m gives

    (Q(x)^2/x)'=m(x)^2-M(x)^2/x^2.

After integration,

    E(X)=integral_1^X M(t)^2/t^2 dt+Q(X)^2/X.            (2.2)

Hence (b) implies Q(X)=O_epsilon(X^(1/2+epsilon)). For Re(s)>1, absolute
convergence gives

    integral_1^infinity Q(x)x^(-s-1) dx
       =-1/[s(s-1)Z_o(s)].                              (2.3)

The growth just obtained makes the left side holomorphic for Re(s)>1/2.
Analytic continuation of (2.3) therefore precludes a zero of zeta there:
1-2^(-s) is nonzero in that half-plane, and s(s-1)Z_o(s) has the removable
pole at s=1 already canceled. Functional-equation reflection gives RH.

Conversely assume RH. The classical RH-to-Mertens implication gives
M_all(x)=O_delta(x^(1/2+delta)) for every delta>0. This is an explicitly
imported classical theorem, not a new result or a finite computation here.
Separating the even terms yields

    M(x)=sum_(2^j<=x) M_all(x/2^j)=O_delta(x^(1/2+delta)).

Partial summation shows that sum_(n odd)mu(n)/n converges; its value is zero
by taking the Abel limit of 1/Z_o(s) at s=1. Taking 0<delta<1/2 and summing
the tail gives m(x)=O_delta(x^(-1/2+delta)). Integration gives (b), after
choosing delta smaller than half the requested epsilon.

Now (1.4) and h_X<=1+log X identify (b) and (c), with the epsilon reduced
before absorbing the logarithm. The reciprocal of kappa(X) is the least
eigenvalue of B_X^*B_X, proving equivalence to (d).

Finally E is increasing and consecutive endpoints 3^r have ratio three.
A subpower bound on that cofinal sequence extends to all real X. This also
proves the stated cofinal versions via (1.4). QED.

The full-vector lower bound is not an accidentally stronger requirement with
an unproved source-to-operator adapter: (1.3) proves that adapter exactly.

## 3. AC26-3: exact elimination of a complete multiplicative shell

Let A=3^r, r>=1. Split O_(3A) into O_A and the A-element shell

    T_A={A,A+2,...,3A-2}.

Every proper divisor of an odd n<3A is at most n/3<A. Accordingly,

                [ B_A   0  ]
    B_(3A)=     [ C_A   K_A],                            (3.1)

where

    K_A=diag(n: n in T_A) Delta_shell,
    J_A:=K_A^(-1),  J_A(n,k)=1_(k<=n)/k.                (3.2)

The first shell difference uses zero at its artificial left boundary; the
actual term -A x_(A-2) belongs to C_A. Explicitly, for d in O_A,

    C_A(n,d)=sum_(e|n, e<A)e(1_(d=e)-1_(d=e-2))
                     -A 1_(n=A)1_(d=A-2),             (3.3)

with out-of-range Kronecker terms omitted. Put L_A=-J_A C_A. Exact inversion
of the lower block matrix gives

                [ V_A      0  ]
    V_(3A)=     [ L_A V_A  J_A].                        (3.4)

No Schur coupling or arithmetic source term is dropped. The new independent
forcing is uniformly stable:

    ||J_A||_op^2 <= ||J_A||_HS^2
      =sum_(j=0)^(A-1)(A-j)/(A+2j)^2
      <=(A+1)/(2A)<=2/3.                               (3.5)

The inequality follows by replacing every denominator by A^2 and summing
A+(A-1)+...+1. Equations (3.1)--(3.4) follow directly from (0.1) and triangular
inversion, so the result holds for EVERY r, not merely the tested shells.

### Uniform control of macroscopic forcing indices

For every fixed real q>=1, let P_(A,q) retain old forcing coordinates d>=A/q.
Then, unconditionally and uniformly in A,

    ||L_A V_A P_(A,q)||_op^2
       <=||L_A V_A P_(A,q)||_HS^2 < 2q^2.               (3.6)

To see this, first use |m(t)|<=2. An elementary proof starts from
sum_(n<=N)mu(n)floor(N/n)=1, which implies |sum_(n<=N)mu(n)/n|<=1 by taking
fractional parts. Separating even terms and iterating gives the odd sum bound
2. The inverse formula (1.1) gives every relevant entry as m(n/d)/d,
n in T_A. For d>=A/q its absolute value is at most 2q/A. There are A rows
and fewer than A/2 old columns, proving (3.6).

Thus arbitrary input supported at any fixed proportion of the previous
cutoff already has a uniform output bound. The unresolved part lies in
forcing indices d/A tending to zero. This does not discard those indices
or bound their interactions with one another.

## 4. AC26-4: a concrete compactness theorem would complete the proof

### Q-AC26 — uniform arithmetic shell compactness (OPEN)

For every eta>0, is there a finite C_eta, independent of r, such that

    ||L_A x||_2^2 <= eta ||x||_2^2+C_eta ||B_A x||_2^2  (4.1)

for A=3^r, every r>=1, and every complex vector x on O_A?

This has the shape of a compactness/Ehrling estimate, but no existing generic
compactness lemma is being invoked to prove it. Each FIXED dimension admits
some C_eta trivially. Independence from the cutoff is the mathematical target.
No claim is made that (4.1) is necessary for RH; its sufficiency is proved next.

### Conditional closing theorem

If Q-AC26 holds, then RH holds.

**Proof.** Given old and new forcing u,v, (3.4), (4.1), and (3.5) give

    ||V_(3A)(u,v)||^2
      =||V_Au||^2+||L_AV_Au+J_Av||^2
      <=[(1+2eta)kappa(A)+2C_eta]||u||^2+(4/3)||v||^2.

Therefore

    kappa(3A)<=max((1+2eta)kappa(A)+2C_eta,4/3).        (4.2)

Iteration from A=3 gives kappa(3^r)=O_eta((1+2eta)^r). For any desired
positive exponent epsilon choose eta so small that
log(1+2eta)/log3<epsilon. AC26-2 now gives RH. This excludes every off-critical
zero, not just a finite height range. QED, CONDITIONAL ON (4.1).

### Equivalent sequential version of the OPEN target

Assertion (4.1), with all eta>0, is equivalent to:

    Whenever A_j are powers of three, sup_j||x_j||<infinity,
    and ||B_(A_j)x_j|| -> 0, then ||L_(A_j)x_j|| -> 0.   (4.3)

The forward implication follows from (4.1), first letting j grow and then
eta decrease. Conversely, failure for eta_0>0 gives for each integer j a
vector satisfying ||Lx||^2>eta_0||x||^2+j||Bx||^2. Normalize by ||Lx||.
The new vectors have bounded norm, B-residual tending to zero, and L-norm
one, contradicting (4.3). Any such countersequence has an unbounded cutoff
subsequence, because each fixed B_A is invertible.

At each fixed coordinate, the triangular equations force x_j to tend to zero
when their residuals do. The challenge is therefore an actual no-concentration
statement at moving scales: prevent a bounded approximate null vector, which
has disappeared at every fixed coordinate, from generating a macroscopic
new-shell output. That is not established by coordinatewise convergence.

### Exact finite certificate interface

For given A, eta, C, (4.1) is equivalent to the Loewner inequality

    C I+eta V_A^*V_A-(L_A V_A)^*(L_A V_A) >= 0.          (4.4)

It is a test for ALL vectors in that dimension. The attached exact checks
prove strict positivity at A=3,9,27,81 for eta=1/10 and 1/100, C=1, by all
leading principal minors. The test computes the whole coupling, not only
the Mobius source column. Eight finite certificates do not prove (4.1)
or bound C_eta at larger cutoffs.

## 5. AC26-5: generic triangularity and stable new forcing do not suffice

The following is an exact CONTROL SYSTEM, not the zeta divisor source.
On odd integers define a nonnegative multiplicative kernel

    a(1)=1,  a(3^k)=3^(k-1) for k>=1,
    a(n)=0 for all other n.

Its Dirichlet inverse is

    b(1)=1,  b(3^k)=-2^(k-1) for k>=1,
    b(n)=0 otherwise.

Indeed their formal series in t=3^(-s) are (1-2t)/(1-3t) and its reciprocal.
The full divisor equations a*b=e_1 hold. In particular the inverse has actual
harmonic balance sum b(n)/n=0, with absolute convergence, and

    m_b(x)=sum_(n<=x)b(n)/n=(2/3)^k
                      for 3^k<=x<3^(k+1).

It follows exactly that

    E_b(3^r)=6((4/3)^r-1).                              (5.1)

Replace Z_X(n,d) by 1_(d|n)a(n/d), leaving D_X and Delta_X unchanged. The
resulting B_X^(a) has the SAME positive diagonal, eigenvalues and determinant
as the native matrix. Its high-shell block K_A and stable J_A are also the
same: a proper divisor still lies below A. But for x=(m_b(n))_(n in O_A),

    B_A^(a)x=e_1,
    ||x||^2=3((4/3)^r-1),
    ||L_A^(a)x||^2=(4/3)^r,       A=3^r.               (5.2)

The last identity holds because extending the exact source e_1 creates the
constant value (2/3)^r on the A entries in the new shell. Thus any constant
in the analog of (4.1) must obey

    C_eta >= (1-3eta)(4/3)^r+3eta.                      (5.3)

It diverges for eta<1/3. Equivalently the normalized x give bounded vectors
with vanishing forcing but new-shell squared norm tending to 1/3, violating
(4.3). This is a complete all-r counterexample to the GENERIC inference,
not a counterexample to the native compactness conjecture or to RH.

The inverse series (1-3^(1-s))/(1-2*3^(-s)) has a pole at log_3 2>1/2, in
accord with (5.1). It is not 1/Z_o(s). Its kernel coefficients and inverse
coefficients do not have the native bounds a(n)=1 and |mu(n)|<=1, and it
has no asserted zeta functional equation. Those source differences remain
load bearing. Positivity, multiplicativity, exact inversion, balance, the
known matrix spectrum, and new-shell stability alone do not give (4.1).

## 6. AC26-6: a fixed positive coercivity constant is impossible

Unconditionally,

    E(X) -> infinity,
    kappa(X) -> infinity,
    lambda_min(B_X^*B_X) -> 0.                          (6.1)

This uses the classical existence of a critical-line zeta zero, not RH,
zero simplicity, or numerical zero input. It is the familiar boundary-pole
argument also used in the repository's compact inverse work, not a novel
proof of Hardy's theorem.

Suppose E(infinity)<infinity. Then h(t)=e^(t/2)m(e^t) belongs to L2(0,infinity).
Its Laplace transform H(z) is holomorphic for Re(z)>0 and obeys

    |H(sigma+it)|<=||h||_2/sqrt(2sigma).

On Re(z)>1/2, absolute convergence gives the IMPORTANT shifted formula

    H(z)=1/[(z-1/2) Z_o(z+1/2)].                        (6.2)

The factor is z-1/2, not z+1/2. The pole of Z_o at z=1/2 is canceled by this
factor. Analytic continuation gives the identity throughout Re(z)>0 wherever
the right side is defined; multiplying by the holomorphic denominator also
excludes interior poles under the supposed L2 hypothesis.

Let 1/2+i gamma be any critical-line zero, with multiplicity m>=1. The
Euler factor is nonzero there and i gamma-1/2 is nonzero. Near z=i gamma,
(6.2) grows as a nonzero constant times sigma^(-m) when sigma decreases to
zero along z=sigma+i gamma. This contradicts the sigma^(-1/2) Laplace bound.
Thus E(infinity)=infinity. Equation (1.4) gives the remaining conclusions.

The checker proves B_X^*B_X > I/4 at its seven SPECIFIED small cutoffs.
Equation (6.1) proves that this finite observation cannot persist for all X.
The RH target allows deterioration slower than every power; it does not ask
for a fixed gap. This distinction must survive any numerical campaign.

## 7. Disposition and next theorem

The completed results are the exact source/operator comparison, the complete
shell decomposition, uniform new-forcing and macroscopic-forcing estimates,
the conditional compactness-to-RH theorem, and two explicit limitations.
The experiment supplies finite full-vector certificates, not the required
all-scale compactness proof.

The proposed attack is to prove (4.3) for the native divisor operator, using
its exact arithmetic and the simultaneous constraints at all smaller scales.
One must not replace that by a claim about arbitrary multiplicative kernels,
coordinatewise convergence, selected test vectors, or finite invertibility.
The unresolved small-divisor forcing sector is explicitly retained in (3.4).
No unconditional subpower bound for E or kappa is established in this packet.

This is a full-problem route with a precise unproved assertion, not a full
proof proposal with an RH-strength lemma silently assumed. See ATTACK_PLAN.md
for a bounded next investigation and VALIDATION.md for actual computations.

# Matching geometry and loss-free physical principal calibration

Status: PROPOSED component mathematics; complete proofs at the stated fixed-order
scope. No full native moment estimate, improved zero-free exponent, or RH proof.
The author also wrote the checker. Independent mathematical review is pending.

Base: PR #942, commit 377f548cab8759399aca80ed3188c495667d562a.
This note does not modify or certify its predecessor's proofs.

## 0. Classical credit and the actual increment

The logarithmic exponents (k-1)^2 and k(2k-3), and their relation to
multiplicative moment geometry, are classical. In particular, Harper--Nikeghbali--
Radziwill, arXiv:1505.01443v1, Theorems 3 and 4, give stronger asymptotics in
the ordinary-integer Steinhaus and Rademacher models. Heap--Lindqvist,
arXiv:1505.03378, independently obtain such asymptotics. Those results, not this
packet, establish the classical priority. We do not infer a physical sextic
moment from either random model.

Here an elementary graph count is adapted to the repository's ideal columns,
actual divisibility masks and sixth-power aliases. It gives sharp *orders* for
the complete principal reference and no-singleton absolute count. More usefully,
it removes D^epsilon from the physical principal comparison: its relative error
is O(H^(-1/2)) for sharp rows, or O(log(2H)^(k^2)/H) for a fixed smooth row
profile, uniformly as the column scale grows. Constants depend on fixed order;
no growing-k uniformity or leading constant is asserted.

The previous low-radical annihilation and the large-radical signed remainder
are unchanged. The new logarithmic estimates do NOT pay that remainder.

## 1. Set-up

K=Q(sqrt(-3)), O=Z[omega], omega^2+omega+1=0, v_K=sqrt(3)/2.
All multiplicative indices are integral IDEALS. Conjugate split ideals of equal
norm are distinct. S is a fixed finite set including the primes above 2 and 3.
Additional fixed exclusions can be incorporated into S. Upper bounds below
also permit arbitrary additional deletions of columns. The lower bounds do not
claim uniformity under growing exclusions that could remove all columns.

Fix k>=1 and a bounded nonzero nonnegative continuous W of compact support
[a,b] inside (0,infinity); for the lower argument take b=sup supp(W). Smooth W
is a special case. Let nu be any completely multiplicative ideal function with
|nu(p)|=1 outside S. The constants below can be chosen independently of these
unitary prime phases. The actual source is

    A_u(D)=sum_(n squarefree,(n,S)=1) mu_K(n)nu(n)chi_n(u)W(Nn/D).

The local sextic symbols have exact order six on residue-field units, and zero
at nonunits. For a 2k-tuple t=(n_1,...,n_k;m_1,...,m_k), put

    Q(t)=rad(product_i n_i m_i),
    e_p(t)=sum_i 1_(p|n_i)-sum_i 1_(p|m_i),
    c(t)=product_i [mu(n_i)nu(n_i)W(Nn_i/D)]
                   conjugate([mu(m_i)nu(m_i)W(Nm_i/D)]).

Call t principal when e_p(t)=0 modulo 6 at every prime. Define

    delta(Q)=product_(p|Q)(1-1/Np),
    B_(2k)(D)=sum_(t principal) c(t) delta(Q(t)),
    P_(2k)(D,H)=sum_(t principal) c(t) C_Q(H),
    C_Q(H)=#{u in O:0<Nu<=H,(u,Q)=1}.

B is a nonnegative real number. To see this, independently choose, at each
relevant prime, Z_p uniform on mu_6 and E_p in {0,1} with mean 1-1/Np.
Expanding E|sum_n mu(n)nu(n)W(Nn/D) product_(p|n) E_p Z_p|^(2k)
gives exactly B. This is an identity for the reference, NOT an assumption
about the physical rows. It preserves every principal nonunit mask.

For a fixed Schwartz function Phi on C, define C_Q^Phi(H) by weighting the same
nonzero rows with Phi(u/sqrt(H)); P^Phi is defined using this count. Put

    c_0=pi/v_K,              c_Phi=(integral_C Phi)/v_K,
    L=log(2+D),             d_k=(k-1)^2.

If Phi is nonnegative and nonzero, then c_Phi>0.

### Main theorem

For every fixed k and W as above, for all sufficiently large D,

    B_(2k)(D) asymp_(K,S,k,W) D^k L^d_k.                       (1.1)

For every H>=1, uniformly in D>=3 (with a changed constant on bounded D),

    P_(2k)(D,H)=c_0 H B_(2k)(D)
                 +O_(K,k,W)(sqrt(H) D^k L^d_k),              (1.2)

and for every fixed Schwartz Phi,

    P_(2k)^Phi(D,H)=c_Phi H B_(2k)(D)
                 +O_(K,k,W,Phi)(D^k L^d_k log(2H)^(k^2)).    (1.3)

Thus the relative errors, when c_Phi>0, are O(H^(-1/2)) and
O(log(2H)^(k^2)/H), independently of D. The constants are NOT uniform in k.
The exact band-limited identities in #942 remain stronger in their own
exact-support regimes.

## 2. A graph count with its logarithmic dimension visible

Let G be a fixed finite simple graph, with V vertices and E edges. B_G is its
UNSIGNED incidence matrix: each edge column has two entries equal to one.
Set

    r_G=rank_Q B_G,       d_G=E-r_G.

Equivalently r_G=V-b_G, where b_G counts bipartite connected components,
INCLUDING isolated vertices. Indeed a vector in the left kernel satisfies
x_v=-x_w along every edge. It is one-dimensional on a connected bipartite
component and zero on a connected component with an odd cycle.

For caps Y_v>=1, assign one ideal a_e to every edge, subject to

    product_(e incident to v) Na_e <= Y_v.                   (2.1)

The ideals here need not be squarefree or coprime. Fixed-field ideal counting
I(T)<=C_K T gives

    #{assignments} <= C_G product_v Y_v^(1/2)
                            (1+log(2 max_v Y_v))^d_G.       (2.2)

**Proof.** Put each Na_e in [2^j_e,2^(j_e+1)), j_e>=0. There are at most
C_K 2^j_e choices. Necessarily B_G j<=ell, where ell_v=floor(log_2 Y_v).
For an admissible vector put s=ell-B_G j. Then

    2 sum_e j_e=sum_v ell_v-sum_v s_v.                       (2.3)

Choose r_G linearly independent columns of B_G. For a fixed right side and
fixed values of the other d_G coordinates, the basis coordinates are uniquely
determined over Q, so there is at most one nonnegative integer solution.
Every free coordinate is at most ell_max. Hence each fiber has size at most
(1+ell_max)^d_G. Sum the factor 2^(-sum s_v/2) over all s_v>=0, allowing
inconsistent right sides. Its sum is (1-2^(-1/2))^(-V). This proves (2.2).
This proof is valid for disconnected graphs and isolated vertices. QED.

### Weighted version

For 0<theta<=1 define

    F_theta(a)=sum_(d|rad(a)) (Nd)^(-theta)
              =product_(p|a)(1+(Np)^(-theta)).

Opening the divisor sum gives, for T>=1,

    sum_(Na<=T) F_theta(a)
       <= C_K T sum_d (Nd)^(-1-theta)
       = C_K T zeta_K(1+theta).                            (2.4)

Thus weighting every assignment in (2.2) by product_e F_theta(a_e) multiplies
its bound by at most zeta_K(1+theta)^E (up to a fixed graph constant).
No uniform prime number theorem is used. Ideal counting also gives
zeta_K(1+theta)<=C_K(1+1/theta).

At exponent s>1,

    sum_a F_theta(a)/(Na)^s <= zeta_K(s)zeta_K(s+theta),      (2.5)

which is uniformly bounded for theta>=0 if s is fixed above one. At theta=0,
interpret F_0(a)=2^omega(a); the same bound at s>1 holds.

## 3. Upper bound for ALL principal aliases

At each prime of a principal tuple, let I and J be the sets of left and right
slots containing it. Match the first min(|I|,|J|) slots in increasing order.
Place that prime in the ideal a_ij for each matched pair (i,j). The remaining
slots, if any, are all on one side and their number is divisible by six.
Partition them, in increasing order, into groups of six and place the prime
in an ideal b_C for each such six-element group C.

This is deterministic. Its edge and six-slot ideals reconstruct the original
columns exactly. An ideal may share primes with another edge or group ideal;
NO extra coprimality is imposed. Conversely, allowing arbitrary independent
ideals on these indices only enlarges the count. Reconstruction ensures that
different original tuples cannot have the same entire collection of variables.

After fixing all b_C, the edge graph is K_(k,k). Its rank is 2k-1 and its
nullity is d_k=(k-1)^2. Its caps are

    Y_v=bD / product_(C containing v) Nb_C.

Caps below one have no solutions. The square root of their product is

    product_v Y_v^(1/2)=(bD)^k product_C (Nb_C)^(-3).         (3.1)

Use (2.2) and sum every b_C. Their sums converge at exponent three. We obtain

    sum_(t principal) |c(t)| <= C_(K,k,W) D^k L^d_k.         (3.2)

Since delta(Q)<=1, this proves the upper half of (1.1). It also proves the
same upper bound for the principal ABSOLUTE coefficient count, which can be
larger than B when the fixed twist has nontrivial sixth powers.

Since rad(Q) is the union of the primes in the edge and group ideals,

    F_theta(Q) <= product_e F_theta(a_e) product_C F_theta(b_C).

Equations (2.4)-(2.5) therefore give the stronger uniform bound

    sum_(t principal) |c(t)| F_theta(Q(t))
       <= C_(K,k,W) zeta_K(1+theta)^(k^2) D^k L^d_k,
                         0<theta<=1/2.                    (3.3)

The constant apart from the displayed zeta factor is independent of theta.
The six-slot sums are bounded uniformly using zeta_K(3)^2. This is where the
higher aliases are genuinely retained rather than declared absent. They first
occur for squarefree columns at k=6, and do not change the logarithmic exponent.

## 4. Lower bound: a positive density of alias-isolated matchings

We first supply the elementary counting input for the lower bound.

### Lemma 4.1: weighted coprime ideal boxes

Fix an integer m>=1, rho>1, and the finite exclusion S. For any real scales
T_1,...,T_m tending to infinity, the weighted number of tuples of pairwise
coprime squarefree ideals a_j, prime to S, with T_j<=Na_j<rho T_j, weighted by

    delta(product_j a_j),

is at least c_(K,m,rho,S) product_j T_j, once min T_j is sufficiently large.
The corresponding unweighted upper bound is C product_j T_j.

**Proof.** The elementary Eisenstein lattice count gives

    I(T)=kappa_K T+O_K(sqrt(T)),    kappa_K=pi/(6v_K).

For finitely many prescribed prime valuations, subtract counts of multiples
of fixed ideal powers. This gives the usual geometric distribution:
P(v_p(a)=0)=1-1/q and P(v_p(a)=1)=(1-1/q)/q, q=Np, with an error tending to
zero in each fixed box. For a prime outside S the allowed weighted local factor
(at most one variable contains p, and that variable contains it just once) is

    L_m(q)=(1-1/q)^m [1+m(1-1/q)/q]=1+O_m(q^(-2)).          (4.1)

It is strictly positive. The primes in S contribute (1-1/q)^m. The infinite
product of these factors converges to a positive constant because
sum_p q^(-2)<infinity.

For completeness the passage from finitely many primes to all primes is
uniform over the box scales. A square p^2 in any variable costs at most
C product T_j/q^2 by I(rho T_j/q^2)<=C rho T_j/q^2 (zero if the cap is <1).
A prime p in two variables has the same bound. Summing all such defects above
a fixed norm cutoff Y costs at most C product T_j sum_(Np>Y)q^(-2).
The missing density weight above Y costs the same: use
1-product_(p|Q,Np>Y)(1-1/q)<=sum_(p|Q,Np>Y)1/q
and count multiples of p in one variable. First choose Y making these tail
costs smaller than one quarter of the positive limiting local density. Then
let min T_j grow so the finite-prime count is within another quarter. This
proves the lower bound. Only fixed ideal counting, not a prime ideal theorem,
is used. QED.

### Lemma 4.2: logarithmically many matching boxes

Suppose G has 2k vertices and has a strictly positive fractional perfect
matching: there are w_e>0 with B_G w=1. For any fixed interval [c,c'] inside
(0,infinity), there are at least c_G (log D)^d_G disjoint edge boxes, each
contributing at least c'_(G,S) D^k pairwise-coprime squarefree assignments
(with the density weight), for which every vertex product lies in [cD,c'D].

**Proof.** Choose rho>1 so rho^(max degree G)<c'/c. Let h_1,...,h_d be linearly
independent integer vectors spanning ker_Q B_G, d=d_G. For integer parameters
t_l with |t_l|<=epsilon log D, put

    T_e=(cD)^(w_e) rho^(sum_l t_l h_l,e).

Choose epsilon>0 sufficiently small. Then every T_e>=D^eta for a fixed eta>0.
Since B_G h_l=0, all vertex products of the T_e equal cD. Since
sum_e w_e=k and sum_e h_l,e=0, product_e T_e=(cD)^k. The edge intervals
[T_e,rho T_e) thus put the vertex products in [cD,c'D]. Distinct integer
parameter vectors give disjoint boxes: at some edge their log_rho scales
differ by a nonzero integer. Lemma 4.1 supplies cD^k in each box, uniformly.
There are at least c(log D)^d boxes. For d=0 one box suffices. QED.

Apply this to K_(k,k), with w_e=1/k. All edge ideals are pairwise coprime and
squarefree, so each original column is squarefree, every prime occurs in one
left and one right column, and the product n=product_i n_i is squarefree.
The matrix is recovered uniquely by a_ij=gcd(n_i,m_j), so none of the resulting
ordered tuples is counted twice.

A subtlety is necessary for a general unitary twist. Other sixth-power aliases
in the same charge block could have negative real cross terms. We avoid this
by isolating the selected charge blocks, rather than discarding those terms.

Let q_* be the smallest prime-ideal norm outside S. Choose c<c'<b with
W>=w_*>0 on [c,c'] and

    c^k > b^k/q_*^6.                                       (4.2)

Such an interval exists: nonzero values of the continuous nonnegative W
approach b=sup supp W, and the inequality is strict below b. Every selected
product n is squarefree and Nn> (bD)^k/q_*^6. Any product m with the same
sixth charge must have the form m=n d^6. If d is nonunit, Nm>=Nn q_*^6>
(bD)^k, outside the full allowed product support. Thus this charge block has
exactly ONE product ideal n.

For each fixed pattern of the zero masks, its entire contribution to the
principal reference is the squared modulus of the sum of coefficients in
that block. All its k-fold factorizations have the common phase mu(n)nu(n),
so its density-averaged contribution is precisely

    delta(n) [sum_(n_1...n_k=n) product_i W(Nn_i/D)]^2.

All other charge blocks are nonnegative squared norms. Keeping just the
constructed tuples inside the isolated blocks therefore gives a legitimate
lower bound, at least c D^k L^d_k. This proves the lower half of (1.1), uniformly
in the arbitrary unitary prime phases of nu. It is not a termwise positivity
assertion for all principal aliases.

## 5. Physical masks with no D^epsilon loss

The elementary planar lattice estimate, extended to 0<Y<1, is

    R(Y):=#{u in O:0<Nu<=Y}=c_0 Y+O_K(sqrt(Y)), Y>0.         (5.1)

For an ideal d, multiplication by a generator rotates/scales the lattice, and
the number of nonzero rows divisible by d is exactly R(H/Nd). Inclusion--
exclusion therefore gives

    C_Q(H)=c_0 H delta(Q)+O_K(sqrt(H) F_(1/2)(Q)).            (5.2)

This is sharper for the aggregate problem than replacing the divisor weight
by tau(Q). Sum (5.2) with c(t) and use (3.3) at theta=1/2. This proves (1.2).
The argument retains ALL primes in Q, including neutral principal masks.

For a fixed Schwartz Phi, uniformly over lattice rotations gamma, define

    E_gamma(Y)=sum_(u!=0) Phi(gamma u/sqrt(Y))-c_Phi Y.

Poisson summation for Y>=1, with rapid Fourier decay on the rotated dual
lattice, shows |E_gamma(Y)|<=C_Phi. The subtraction of the zero row leaves
the constant -Phi(0), which must not be dropped. For 0<Y<=1, rapid spatial
decay on nonzero lattice points gives |E_gamma(Y)|<=C_Phi Y. Consequently

    |E_gamma(Y)| <= C_Phi min(1,Y) <= C_Phi Y^theta,
                         0<theta<=1/2.                    (5.3)

The first constant is independent of theta and gamma. The coset/rotation
normalization is the same Euclidean Fourier convention as #942. The usual
Poisson identity is classical; this small/large Y bound is supplied here.

Inclusion--exclusion using (5.3), followed by (3.3), now gives

    |P^Phi-c_Phi H B|
      <= C H^theta zeta_K(1+theta)^(k^2) D^k L^d_k.         (5.4)

Take theta=min(1/2,1/log(2H)). Then H^theta<=e and
zeta_K(1+theta)<=C_K log(2H). This proves (1.3). Unlike substituting theta=0
into a divergent estimate, this chooses a strictly positive exponent and
pays its full constant. Uniformity in D is genuine; uniformity in k is NOT
asserted. The entire Schwartz row sum is retained.

Together with (1.1) these prove the relative principal estimates stated at
the start. They are estimates for P, not for the full physical moment M.

## 6. A sharp-log no-singleton bound, including nonprincipal tuples

For a 2k-tuple of squarefree columns a singleton prime is one occurring in
exactly one slot. Given a graph G on these 2k slots, allow a prime of total
occurrence two only when its two slots form an edge of G; allow every
occurrence set of size at least three; forbid singletons.

The absolute tuple count, for all column norms <=X and coefficients of
modulus <=1, satisfies

    T_G(X) <= C_(K,k,G) X^k (log(2X))^d_G.                   (6.1)

Additional tuple selectors of modulus at most one and moving exclusions may
be imposed in this upper bound. Coefficients can depend on a fixed row; no
row-independent large sieve is being applied.

**Proof.** Let q_I be the product of primes with exact incidence set I. Keep
q_I for |I|>=3 fixed. Incidence sets of size two give one ideal per edge of G.
After dropping coprimality restrictions their vertex caps are
X/product_(I containing v)Nq_I. Formula (2.2) costs

    C X^k log(2X)^d_G product_(|I|>=3) (Nq_I)^(-|I|/2).

Every remaining ideal sum converges, since |I|/2>=3/2. QED.

If G has a strictly positive fractional perfect matching, Lemmas 4.1-4.2
show that (6.1) has the correct order for fixed nonnegative annular weights
on the columns, already using only incidence sets of size two. This is an
absolute-count lower bound; it is NOT a lower bound on a signed nonprincipal
physical contribution.

For the full no-singleton sector take G=K_(2k). For k>=2 it is connected and
nonbipartite, giving

    d_G=binom(2k,2)-2k=k(2k-3).                             (6.2)

For k=1 the graph is K_2 and d_G=0. Hence any physical nonnegative row measure
of mass O(H) gives the ACTUAL SIGNED no-singleton sector the upper bound

    |N_(2k)| <= C H X^k log(2X)^(k(2k-3)),  k>=2.            (6.3)

No positivity of N is assumed: first dominate it by the absolute count.
At orders 4,6,8 the logarithmic powers here are 2,9,20, whereas the principal
reference powers are 1,4,9. At every fixed order both are absorbed by X^epsilon,
but the distinctions matter for finite normalizations and growing-order work.

This is a SHARPER LOGARITHMIC ESTIMATE for a smaller sector than the smooth-
singleton sector of #940. It neither supersedes that larger controlled union
nor supplies the remaining singleton estimate.

## 7. Where the large-radical attack stopped

For the positive band-limited majorant of #942, low-radical nonprincipal tuples
still vanish exactly. Split the surviving remainder into no-singleton and
singleton tuples. The former is now paid at the explicit logarithmic cost
(6.3); #940 already pays a larger union at an X^epsilon cost.

The unresolved part contains genuinely large singleton prime products. In a
positive incidence count, a singleton ideal enters one vertex only. The graph
normalization then leaves its coefficient weight (Nq)^(-1/2), whose ideal sum
is not convergent. Allowing independent singleton ideals up to X restores a
power loss. The new graph geometry cannot remove that loss by itself.

The unproved arithmetic assertion remains a one-sided bound for the COMPLETE
native signed singleton remainder, not for individually selected prime faces.
The original target is still M_(2k)(D,D^(1+theta))<<D^(1+theta+k+epsilon),
with its full source quantifiers. None of (1.1)-(6.3) proves it or approaches
RH without a new signed estimate.

The Birkhoff/matching connection clarifies the correct principal benchmark
and improves the physical calibration error. It does not turn independent-
residue orthogonality into short-physical-row orthogonality.

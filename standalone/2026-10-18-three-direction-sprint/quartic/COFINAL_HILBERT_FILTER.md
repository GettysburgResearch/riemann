# A bounded fourth-power filter for quartic theta

**Supplementary late addendum, 18 October 2026.** This note supplements the frozen three-direction packet. It proves a normalized Hilbert-space construction and a particular local Fourier limit. It does not construct the square-selecting/angular automorphic adapter or bound its Eisenstein period, and it proves no new zero-free region.

## 1. Classical input and the function space

Use F=Q(i), O=Z[i], lambda=1+i and S={lambda}. Good primary elements represent ideals prime to S once. Write Nd for their norms. The classical quartic residues theta_(i1),theta_(i2) and their two-ray residue coefficients are normalized as in the companion `ALL_SQUARE_INDICES.md`. The primary sources are David--Dunn--Hamieh--Lin, [arXiv:2306.11875v2](https://arxiv.org/html/2306.11875v2), especially (4.34)--(4.38), and Suzuki, *The biquadratic theta series* (1983), Theorem 3, printed page 114, [primary scan](https://gdz.sub.uni-goettingen.de/content/PPN243919689_0340/1000/0/00000118.jpg). Suzuki's original theorem states FULL fourth-power periodicity without a coprimality restriction; DDHL quotes a narrower consequence. We use the full classical statement, not an iteration outside a coprime hypothesis.

Let V be the linear span of these two selected quartic residues, viewed as scalar functions on H^3. The proof below also applies to any other such function once the same Fourier periodicity and L2 hypotheses are supplied. Every theta in V has a base-cusp expansion

    theta(z,y)=C y^(3/4)+sum_(nu!=0) A_nu(y) echeck(nu z/lambda^4),
    A_nu(y)=c tau(nu)(Nnu)^(1/8)y K_(1/4)(pi|nu|y),
    tau(d^4 nu)=tau(nu)                              (1)

for every good primary d and every nu!=0. The last identity follows directly from Suzuki's full periodicity and DDHL (4.35) for these selected residues.

These residues are L2 automorphic functions with the finite-order unitary Kubota character kappa on Gamma=Gamma_1(lambda^4). At an essential cusp their only residual constant term is a multiple of y^(3/4); the incoming seed y^s has no pole. Its square is integrable against y^-3 dy. At a nonessential cusp the finite nontrivial stabilizer character shifts the Fourier lattice away from zero. Moderate growth excludes the growing I-Bessel radial solution, leaving exponential K-Bessel decay. This also verifies L2 directly at all cusps.

Put Gamma0=ker(kappa), a finite-index subgroup of Gamma. Treat theta as an ordinary invariant function on Gamma0\H^3. Form the inductive Hilbert space H over all finite-index subgroups H0 of Gamma0: pull a function to a common finite cover and use the norm

    ||f||^2 = [Gamma0:H0]^(-1) integral_(H0\H^3) |f|^2.

The quotient has a common completion. The choice includes all finite covers; no claim that ker(kappa) is a congruence subgroup is needed.

For g in SL2(F), define D_g f(w)=f(gw). It is unitary on this inductive space. Indeed g commensurates Gamma0, because Gamma0 has finite index in the arithmetic lattice Gamma. Compute on a common subgroup of Gamma0 and g^(-1)Gamma0 g. Change variables by g, which preserves hyperbolic measure. The two covering indices agree because conjugate lattices have the same covolume. The same argument works starting from any finite cover. These pullbacks compose in reverse group order; all unipotent operators used below commute.

## 2. Finite orthogonal projections and the exact dilation identity

Let H_per be the closed subspace fixed by all translations n(lambda^4 b), b in O, where n(t)w=(z+t,y). It contains V. For any good primary d define

    P_d = (Nd)^(-4) sum_(b mod d^4) D_(n(lambda^4 b/d^4)).

This is an orthogonal projection on H_per. It averages a finite unitary group: lambda^4 d^(-4)O/lambda^4 O. Inverses and products are well defined modulo the translations fixing this subspace. Its base Fourier multiplier is precisely 1_(d^4|nu), including the constant term.

Every two such projections commute, and

    P_d P_e=P_lcm(d,e),             P_1=I.               (2)

This follows by averaging the sum of their finite additive groups. At each prime the larger denominator supplies the sum, hence the least common multiple.

Set a_d=diag(d^2,d^(-2)), T_d=D_(a_d). In H^3,

    a_d(z,y)=(d^4 z,(Nd)^2 y).

The full Fourier identity (1), including its constant term, gives POINTWISE on all H^3

    P_d theta=(Nd)^(-3/2) T_d theta.                    (3)

For a nonzero mode nu=d^4 mu, its norm prefactor grows by (Nd)^(1/2), whereas the dilation's y factor grows by (Nd)^2. The scalar (Nd)^(-3/2) is therefore exact. The constant term also agrees because ((Nd)^2 y)^(3/4)=(Nd)^(3/2)y^(3/4).

Both sides represent functions on a common finite cover, so this pointwise identity is also a Hilbert-space identity. Unitarity of T_d gives

    ||P_d theta||^2=(Nd)^(-3)||theta||^2.               (4)

No all-cusp adelic right-translation identification is needed for this classical common-cover proof.

For completeness, the dilation orbit has an exact Gram matrix:

    <T_d theta,T_e theta>/||theta||^2
      = [N(gcd(d,e))^2/(Nd Ne)]^(3/2).                 (5)

Use (2), self-adjointness of P_d, and (3). The mixed inner product of P_d theta and P_e theta equals ||P_lcm(d,e)theta||^2. Formula (5) is a one-vector orbit statement, not a multiplication or period bound. Its local Toeplitz kernel q^(-3|j-k|/2) gives the optional synthesis bound

    ||sum_d b_d T_d theta||^2
      <= [zeta_F^S(3/2)^2/zeta_F^S(3)]
                           ||theta||^2 sum_d |b_d|^2

for finitely supported coefficients. The local bound follows by extending the sequence by zero to all integers and bounding convolution by the sum of its absolute kernel; multiply the convergent local bounds over the finite prime set supporting the coefficients, then bound by the full Euler product.

## 3. The hard filter has a nonzero strong limit

For a finite set P of good primes put

    Q_P=product_(p in P)(I-P_p).

These are commuting orthogonal projections. As P increases to all good primes, Q_P converges strongly to the projection Q onto the intersection of their ranges. For a fixed vector this follows directly from

    ||Q_P theta-Q_R theta||^2
      =||Q_P theta||^2-||Q_R theta||^2,   P subset R.

Inclusion--exclusion and (4) give the EXACT norm product

    ||Q_P theta||^2
      = product_(p in P)(1-(Np)^(-3)) ||theta||^2,
    ||Q theta||^2=zeta_F^S(3)^(-1)||theta||^2>0.        (6)

No pure-tensor hypothesis is used. The product is positive by absolute convergence at 3. If a fully elementary quantitative bound is desired, zeta(3)<5/4 and beta(3)<1 give zeta_F^S(3)=(7/8)zeta(3)beta(3)<35/32. Thus the retained squared norm exceeds (32/35)||theta||^2. The weaker union bound exceeds (29/32)||theta||^2 as well.

The finite filters have the expansion

    Q_P theta=sum_(d squarefree, p|d => p in P)
                          mu(d)(Nd)^(-3/2) T_d theta.

The full series converges absolutely in H, since sum_d (Nd)^(-3/2)<infinity. On a square index nu=nu_a m^2, with m prime to the fixed base nu_a, its Fourier mask removes exactly the nonsquarefree m. It does NOT select square indices from the complete Fourier expansion.

## 4. Positive valuation damping, with exact norms

For one good prime p, q=Np, write P_j=P_(p^j), j>=0, so P_j selects v_p(nu)>=4j. The differences P_j-P_(j+1) are orthogonal projections. For eta>0 define the bounded positive contraction

    D_p(eta)=sum_(j>=0) q^(-eta j)(P_j-P_(j+1)).

The operator series converges in norm; its omitted tail has norm at most q^(-eta J). On theta, the limiting intersection projection contributes zero since ||P_j theta||^2=q^(-3j)||theta||^2 tends to zero. The base Fourier multiplier for nu!=0 is

    q^(-eta floor(v_p(nu)/4)),

and its constant multiplier is 0. One may approximate by finite-level capped multipliers q^(-eta min(floor(v_p(nu)/4),J)), with constant multiplier q^(-eta J), before passing J to infinity.

The geometric block masses from (4) give

    ||D_p(eta)theta||^2/||theta||^2
      =(1-q^(-3))/(1-q^(-3-2eta)).                     (7)

Joint block masses factor for finitely many primes: the joint tail projection is P_d, and (4) is (Nd)^(-3). Therefore finite products over distinct primes have the product of (7), without assuming tensor factorization of the automorphic representation. The cofinal products converge strongly. Indeed the operators are commuting positive contractions, and for finite nested products A>=B>=0 one has (A-B)^2<=A^2-B^2; the norm differences are bounded by the decreasing squared-norm differences. Their exact limiting norm is

    ||D(eta)theta||^2/||theta||^2
       =zeta_F^S(3+2eta)/zeta_F^S(3)>0.                (8)

At eta=0 use the identity operator; (8) then equals 1. As eta tends to infinity, the hard-filter value (6) is recovered.

## 5. A specific local Fourier limit is available

There is an additional fact for THIS explicit sequence, even though evaluation on a fixed finite component is not a continuous functional on an arbitrary completed Hilbert space. Each finite hard filter multiplies the original nonzero Fourier coefficient by a number in {0,1}. Each capped or exact positive damping filter has a multiplier in [0,1]. These multipliers stabilize or converge for each fixed nonzero nu; every such nu has only finitely many good prime divisors. The constant terms vanish after the first hard prime, or converge to zero in the capped positive-damping limit.

The original Fourier series is an absolute C-infinity majorant on every compact subset of H^3. Here is a direct argument avoiding any unproved uniform coefficient theorem. Fix a compact set with y>=epsilon>0 and bounded y above. At height y0=epsilon/2, the original smooth periodic function is bounded. Its Fourier coefficient A_nu(y0) is therefore uniformly bounded. The positive real K_(1/4)(pi|nu|y0) and its standard large-argument estimates imply

    |tau(nu)|<=C_epsilon (1+|nu|)^(1/4)
                                      exp(pi|nu|y0).

At y>=epsilon, the K-Bessel decay leaves an exponentially decreasing factor exp(-pi|nu|epsilon/2), times a polynomial. Any fixed number of z,y derivatives introduces only another polynomial: the derivative recurrence for K shifts its order by finitely many integers. The Gaussian lattice has polynomial counting, so the full derivative majorants are summable. Dominated convergence proves C-infinity local convergence of the explicitly filtered base-cusp series. The hard limit retains exactly frequencies with v_p(nu)<4 for all good p. Positive damping retains the displayed valuation weights. These limits remain Laplace eigenfunctions locally.

For a nonzero theta in V the hard local limit is also nonzero. First some nonconstant coefficient exists: otherwise theta=C y^(3/4), incompatible with the lower lambda^4 unipotent unless C=0. Remove all good fourth-power factors from a nonzero coefficient's index using (1). The resulting index has the same nonzero tau and survives every hard filter.

This argument constructs a distinguished local limit of this sequence. It does not assert that the limit is invariant under one fixed finite-index group, or that arbitrary representatives of the Hilbert limit possess a canonical identity-component trace.

## 6. Two explicit continuity barriers

The base constant functional is actually unbounded on these finite covers. To see that the selected theta_(i1) has a nonzero base constant, use the constant-term double-coset formula DDHL (4.6). On the initial real line, gamma to gamma^(-1) swaps the two cusp indices, replaces the lower-left entry by its negative, and conjugates the unitary multiplier. All cusp widths in this displayed normalization have the same volume. Thus

    phi_(j,i)(s,0,0)=conjugate(phi_(i,j)(conjugate(s),0,0)).

Meromorphic continuation and the scalar K(0,s,0), real at real s, make the residue constant matrix Hermitian at 5/4. DDHL's displayed column entry phi_(infinity,i1) is a nonzero multiple of zeta_F^S(4s-4)/zeta_F^S(4s-3), with nonzero residue. Therefore the transposed entry phi_(i1,infinity) also has nonzero residue, and theta_(i1) has C!=0 at the base cusp. But P_(p^j)theta_(i1) has exactly the SAME base constant C for every j while its Hilbert norm is q^(-3j/2)||theta_(i1)||. Consequently this constant-term functional is not bounded by the unweighted Hilbert norm. This does not obstruct the special Fourier limit in Section 5; it explains why it required an independent majorant argument.

A separate radial scaling test records the missing period resource. Remove each base constant and let B_s(theta,phi) be the bilinear torus-constant radial integral of their nonzero-mode products, using y^(s-3)dy and torus Haar mass 1, wherever it converges. The same change of variables can be tested on matched finite Fourier truncations transported by the dilation; arbitrary fixed cutoffs do not preserve the periodicity relation. No global automorphic interpretation is asserted. Change y to q^(2j)y and use the measure-preserving torus endomorphism z to p^(4j)z. Equation (3) gives

    B_s(P_(p^j)theta,P_(p^j)phi)
        =q^(j(1-2s)) B_s(theta,phi).                    (9)

On an initial convergence domain this is an ordinary change of variables; it remains an identity under any consistent meromorphic continuation. In contrast the product of the two L2 norms is q^(-3j)||theta||||phi||. Whenever the base bilinear value is nonzero, the ratio is amplified by q^(j(4-2Re(s))). Hence a bilinear period bound on the whole unweighted Hilbert completion cannot simply be assumed. At Re(s)=7/8 the j=1 scalar term has size q^(-3/4), whose sum over good primes is not absolutely convergent. This is a failure of the proposed absolute majorant, not a proof that the complete signed period diverges; off-diagonal cancellation or a different justified adapter could change the complete calculation.

Any ordinary Eisenstein series on a newly chosen finite cover, or any actual genuine quadratic Eisenstein section, has its own cusp and scattering data. The Hilbert construction does not preserve an explicit arithmetic normalizer for such a new period. In particular an ordinary noncongruence-cover Eisenstein series cannot silently be identified with the original quadratic Kubota series.

## 7. Damping removes the arithmetic numerator-cancellation gate

This paragraph concerns the ALREADY SELECTED fixed squareclass of the companion `ALL_SQUARE_INDICES.md`, not the complete Fourier expansion. There a fixed nu_a with v_a=f(nu_a)!=0 is proved to exist, and one of the fixed bilinear matrices B=I or diag(1,-1) has C_B=Q_B(v_a)!=0. Put S_a=S union {primes dividing nu_a}, let xi_a(m)=(nu_a/m)_2 on ideals prime to S_a, and chi_a=epsilon xi_a delta_kappa. All m below are prime to S_a. Every norm and filter construction above applies with the fixed larger deleted set S_a; its Euler products are then zeta_F^(S_a).

For eta>0 apply D_p(eta/2) to EACH of the two quartic fields, for every p outside S_a. For a nonzero index nu define its coefficient multiplier

    w_(eta/2)(nu)=product_(p outside S_a)
                         (Np)^(-(eta/2)floor(v_p(nu)/4)).

This is a finite product for each nu. The corresponding damped residue coefficient vector is f_eta(nu)=w_(eta/2)(nu) f(nu). It is the distinguished local Fourier limit of the bounded Hilbert construction in Sections 4--5. Each field has squared-norm ratio

    zeta_F^(S_a)(3+eta)/zeta_F^(S_a)(3).

Write m=d^2 r with r squarefree, with shared primes between d and r still unrestricted. Since p does not divide nu_a,

    v_p(nu_a m^2)=4v_p(d)+2v_p(r),
    floor(v_p(nu_a m^2)/4)=v_p(d).

Thus the product of the two field multipliers is exactly (Nd)^(-eta), while the base coefficient at nu_a is unchanged. The companion's complete squareclass Euler identity becomes

    sum_(m primary, (m,S_a)=1)
        chi_a(m)(Nm)^(1/2-s) Q_B(f_eta(nu_a m^2))
       = C_B L_F^(S_a)(2s-1+eta,epsilon^2)
                                         /zeta_F^(S_a)(s),             (10)
    Re(s)>1.

The d sum supplies the shifted numerator; the squarefree r sum is unchanged. For eta>=1, a hypothetical ordinary-zeta zero rho with Re(rho)>1/2 has

    Re(2rho-1+eta)>1.

The numerator in (10) is therefore nonzero there by its absolutely convergent unitary Hecke Euler product. The fixed removed Euler factors are also nonzero. Since zeta_F=zeta L(s,chi_-4), every such ordinary-zeta zero is a zero of the denominator, with its multiplicity retained; C_B!=0. Consequently the meromorphic arithmetic target in (10) retains a pole at every such zero. The companion's extra radial factor (Nnu_a)^(.25-s/2) is entire and nonzero. The hard filter is the eta=infinity coefficient limit: only squarefree m survive, and the same identity has numerator 1.

This proves arithmetic zero retention for the selected piece, not its holomorphy or a bound in that region. The left-hand series is justified initially for Re(s)>1. The Hilbert/local Fourier construction does not continue a weighted global period across a hypothetical pole. Squareclass selection, the root angular realization, the fixed S_a valuation masks, and a complete global period estimate remain unconstructed. No ordinary-zeta zero is excluded by (10) alone.

## 8. Limits of the result

The infinite filter is a genuine nonzero Hilbert-space construction, and its explicitly defined base Fourier sequence has a nonzero local smooth limit. These conclusions remove a simple norm-divergence objection to filtering repeated square roots. They do not identify an automorphic square-selector, implement the root angular character, or control a weighted noncompact Eisenstein period of the limit. An unbounded period is not continuous merely because a sequence is bounded in L2 and converges locally. Multiplication of two Hilbert vectors is also not licensed by the one-vector Gram estimate.

In particular, deleting nonsquarefree m inside the square-index piece would remove its replica L numerator arithmetically, but applying that observation to a complete regularized or absolutely unfolded period requires the missing global adapter and period bound. No estimate for 1/zeta in a new region follows here.

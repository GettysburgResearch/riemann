# GCP26: the exact cost of grounding the arithmetic coherent mode

Date: 2026-09-08. Status: proposed component theorems with complete paper proofs;
independent mathematical review pending. This is NOT an RH proof.
Base: PR825, e4a486d3fd4009e3722e9e93f35710b834fbd195.
Cross-source: PR826, 3a82b80da82edbcd65d4538418a3d51d6030f058,
standalone/2026-09-08-astra-divisor-poincare/PROOF.md, Section 3.

The general spectral/capacity method is classical. We reconstruct the needed
calculation at the literal prime-power graph and prove the growing-prime
asymptotics. No priority claim is made. No PNT, RH, zero census, or numerical
zeta evaluation is used. The elementary Euler product for zeta at real s>1
appears in a return kernel, NOT in a spectral identification with zeta zeros.

## 1. Two exact arithmetic reservoirs, and three different constants

Let P>=2 and let Pset be ALL ordinary primes at most P. We treat:

* sf: S consists of all squarefree divisors of product_{p<=P} p;
* geo: S consists of all positive integers supported on Pset, with no bound
  on prime exponents. P is finite, so its harmonic mass is finite.

Put Z=sum_{n in S}1/n, mu(n)=1/(Zn). Work in l2(S,mu), not an unspecified
prime-phase measure. The normalized Dirichlet form is

  E(f)=(1/Z) sum_{jp^k in S} (log p)/(jp^k) |f(jp^k)-f(j)|^2.       (1)

Every allowed prime-power edge is retained. The scalar theorem extends by
orthogonal coordinate expansion to complex Hilbert-valued functions. The
closed form in the geo case is the finite-prime form of ADG26; its diagonal
construction is also given in Section 2 below. We use its finite-energy domain.

Define the centered variance, root contrast, and anchored constant by

  Var(f)=||f-mean_mu f||^2,
  G_P=sup_{E(f)>0} |f(1)-mean_mu f|^2/E(f),
  C_P=sup_{E(f)>0} ||f-f(1)||^2/E(f).                            (2)

Multiplying both norm and form by Z gives precisely the unnormalized harmonic
metric of PR825. G_P is a squared functional norm on the mean-zero energy
space. C_P is the optimal constant in the stronger ANCHORED inequality.
Neither is automatically the inverse of the mean-zero spectral gap.

For p in Pset put

             sf                         geo
  b_p =      1/p                        1/(p-1)
  a_p =      (1+1/p)log p                p log p/(p-1).

For a nonempty subset D of Pset set b_D=product_{p in D} b_p and
lambda_D=sum_{p in D} a_p. Empty products have value 1.

**GCP26.T1 (exact root contrast and anchored inverse).**

  G_P = sum_{empty!=D subset Pset} b_D/lambda_D
      = integral_0^infinity [ product_{p<=P}(1+b_p exp(-a_p t))-1 ]dt. (3)

The centered spectral gap is exactly

  g_sf=(3/2)log 2;                 g_geo=2log 2.                  (4)

C_P is the unique c>1/g satisfying

  sum_{empty!=D subset Pset} b_D/(c lambda_D-1)=1.                (5)

In particular

  G_P <= C_P <= G_P+1/g.                                       (6)

**GCP26.T2 (sharp growing-prime asymptotics).** As P tends to infinity,

  G_sf(P)=(1/zeta(2))log log P+O(1),
  G_geo(P)=log log P+O(1),                                    (7)
  C_P-G_P=O(1/log log P).

All O constants in (7) are absolute for the indicated reservoir. They are
not numerical certification constants. Thus grounding f(1)=0 has lowest
Dirichlet eigenvalue asymptotic to zeta(2)/log log P in sf, and to
1/log log P in geo, although the CENTERED gaps (4) stay fixed.

Already the finite squarefree sets show that the O(log log P) order in
ADG26's ANCHORED inequality cannot be replaced by an absolute constant.
This does NOT establish optimality of ADG26's CENTERED inequality for arbitrary
divisor-closed sets. On the two product reservoirs its centered bound can
indeed be replaced by (4). No assertion for n<=N follows by tensorization.

## 2. Reconstructing the complete spectral calculation

For a prime p, use the coordinate e=v_p(n). At finite depth m its unnormalized
weight is p^{-e}, e=0,...,m, and the generator divided by log p is

  L_p f(e)=sum_{j<e}[f(e)-f(j)]
                +sum_{j>e}p^{-(j-e)}[f(e)-f(j)].                 (8)

This is obtained directly from (1), with both orientations and detailed
balance included. For 1<=j<=m put A_j=sum_{l=1}^{m-j+1}p^{-l} and

  u_j(e)=0 (e<j-1),   -A_j (e=j-1),   1 (e>=j).

The vectors have weighted mean zero, are mutually orthogonal, and substitution
in (8) gives eigenvalue (j+A_j)log p. Along with the constant they form a basis.
In sf, m=1: the normalized mean-zero vector has root value -sqrt(b_p) and
positive eigenvalue a_p.

At unbounded depth A_j=1/(p-1). The same step functions have eigenvalues
(j+1/(p-1))log p. They are complete: constants plus the first m step functions
span the functions arbitrary on 0,...,m-1 and constant thereafter; these spaces
are dense in geometric l2. In unweighted coordinates the operator is the
number operator times log p plus a bounded self-adjoint Toeplitz term, because
sum_{k>=1}p^{-k/2}<infinity. It is self-adjoint on the number-operator domain
and has compact resolvent. This also identifies the closed form.

The product of finitely many coordinate probability measures is EXACTLY
mu(n)=1/(Zn). Consequently the full generator is a tensor sum, not a claimed
independent model for primes sampled by a Cauchy frequency. Finite tensor
products of these bases are complete, and their eigenvalues add.

At the root e=0, ALL j>=2 step functions vanish. Only the constant and the
j=1 vector are visible. Therefore the root functional, on mean-zero functions,
has one visible spectral coefficient of squared magnitude b_D at lambda_D
for each nonempty subset D. Different subsets with equal eigenvalues remain
separate orthogonal vectors; their positive weights add. No independence of
logarithms is assumed or needed.

Cauchy--Schwarz in spectral coordinates proves (3), and equality is attained
by the finite spectral vector with coefficient e_D(1)/lambda_D in a real
orthonormal convention. The integral follows by integrating exp(-lambda_D t).
The monotonicity of (1+1/p)log p and p log p/(p-1) for real p>=2 proves (4).
For the second monotonicity use p-1-log p>0; the first is equally elementary.

For completeness let xi=1_{n=1}/mu(1), so <xi,f>=f(1), and its constant
spectral coefficient is 1. Its other nonzero coefficient squares are b_D.
For 0<ell<g, the equation

  <xi,(L-ell I)^{-1}xi>=-1/ell+sum_D b_D/(lambda_D-ell)=0          (9)

has exactly one solution: the left side is strictly increasing from -infinity
to +infinity. The vector (L-ell I)^{-1}xi is orthogonal to xi, hence has root
zero, and is a Dirichlet eigenvector on that codimension-one subspace.
By min-max there is at most one eigenvalue below g; compact resolvent in geo
and finite dimension in sf justify the lowest eigenvalue statement. Thus this
solution is the lowest Dirichlet eigenvalue. Its inverse c gives (5).

Alternatively, Var(f)<=E(f)/g and the root contrast inequality give the upper
side of (6); the lower side follows by the equality vector for G_P. The anchored
constant is the Dirichlet inverse because subtracting f(1) changes neither the
energy nor the constraint class, and maps every f to a root-zero function.

## 3. Elementary prime inputs; no prime number theorem

We record sufficient bounds with loose constants. Let theta(x)=sum_{p<=x}log p,
psi(x)=sum_{p^k<=x}log p, M(x)=sum_{p^k<=x}(log p)/p^k.
Central binomial valuations and dyadic summation give psi(x)<3x. The factorial
identity sum_{d<=x}Lambda(d)floor(x/d)=log(floor(x)!) then gives
M(x)<=log x+3. These hold for x>=1, with empty sums as usual.

Splitting primes at sqrt x gives

  pi(x)<=sqrt x+2theta(x)/log x <8x/log x,              x>=2,    (10)

using log x/sqrt x<1. Also

  B(P):=sum_{p<=P}log p/(p-1) <=log P+5.                       (11)

Indeed its log p/p portion is at most M(P); the difference is bounded by
sum_{n>=2}log n/[n(n-1)]<2. The latter follows by telescoping to
log2+sum_{n>=2}log(1+1/n)/n and then using log(1+1/n)<=1/n.

Normalize 1/n over ALL P-smooth integers. Its mean log n is B(P). Markov gives
at least half the mass below exp(2B(P)); a harmonic-sum bound gives

  Z_geo(P)<=2+4B(P)<=22+4log P<40log P.                         (12)

If B=0 the assertion is direct; here P>=2 so B>0. Also Z_sf(P)<=Z_geo(P).
Every geometric exponent tail is included in this proof.

For 0<t<=1, partial summation of (10) yields

  sum_{p>P}p^{-1-t} <=8(1+t)E1(t log P),
  E1(u)=integral_u^infinity exp(-v)dv/v <= exp(-u)/u.            (13)

The negative lower endpoint may be dropped for this upper bound. We will use
only positive sums and integrals. No conditional convergence is involved.

## 4. The infinite return product and its exact zeta factor

Define for t>0 the convergent positive product

  K_infinity(t)=product_p(1+b_p exp(-a_p t)).                   (14)

Convergence follows from b_p<=2/p and a_p>=log p. Factor the elementary Euler
product for zeta(1+t):

  K_infinity(t)=zeta(1+t) H(t),
  H(t)=product_p [(1+b_p exp(-a_p t))(1-p^{-1-t})].              (15)

These are identities of convergent positive products for REAL t>0. No
meromorphic continuation or nontrivial zeta zero enters them.

### 4.1 Squarefree case

Write l=log p, q=p^{-1-t}. The local factor is

  H_p(t)=(1+q exp(-t l/p))(1-q).

It lies in (0,1], is at least 1-q>=1/2, and H_p(0)=1-p^{-2}.
Using 1-exp(-r)<=r, for t>=0,

  |H_p(t)-H_p(0)| <=3t(log p)/p^2.

Therefore, for 0<t<=1,

  |log H(t)-log(product_p(1-p^{-2}))|
                       <=6t sum_p(log p)/p^2=O(t).             (16)

The convergent sum is bounded by the corresponding integer sum. The Euler
product at 2 makes the product in (16) exactly 1/zeta(2). Hence

  H_sf(t)=1/zeta(2)+O(t),
  K_infinity,sf(t)=1/[zeta(2)t]+O(1),           t down to 0.     (17)

For the last estimate the integral comparison 1/t<=zeta(1+t)<=1+1/t suffices.

### 4.2 Unbounded-exponent case

Now delta_p=l/(p-1), b_p=1/(p-1), a_p=l+delta_p. Put

  r_p(t)=[p/(p-1)] exp(-delta_p t)(1-q).

Then r_p(0)=1 and

  (log r_p)'=-delta_p+l q/(1-q)<=0.

The local factor is H_p(t)=1-q[1-r_p(t)], so 0<H_p(t)<=1, H_p(t)>=1-q>=1/2.
Moreover 0<=-log r_p(t)<=delta_p t, giving

  0<=1-H_p(t)<=t(log p)/[p(p-1)].

Thus |log H(t)|<=4t sum_p(log p)/p^2=O(t), and

  H_geo(t)=1+O(t),
  K_infinity,geo(t)=1/t+O(1),                 t down to 0.      (18)

Both cases satisfy the useful global upper bound

  1<=K_infinity(t)<=zeta(1+t), t>0.                           (19)

This factorization explains the logarithmic divergence below. It is the pole
at the SAFE real argument 1, not information about the critical zero set.

## 5. Matching the full growing-prime asymptotic

Let K_P(t)=product_{p<=P}(1+b_p exp(-a_p t)) and assume P>=e. Set L=log P>=1.
By (12), the integral of K_P-1 on [0,1/L] is O(1), uniformly in P. By (19),
its integral on [1,infinity) is bounded by

  integral_1^infinity [zeta(1+t)-1]dt
    =sum_{n>=2} 1/[n^2 log n]<infinity.                       (20)

On [1/L,1], (13) bounds the omitted primes:

  0<=log(K_infinity/K_P)<=32 E1(t L).

Since 1-exp(-x)<=min(1,x), (19) gives

  0<=K_infinity(t)-K_P(t)<=(1+1/t)min(1,32E1(t L)).             (21)

After u=tL, its integral is bounded by
32 integral_1^infinity (1+1/u) E1(u)du, independently of P; use (13) for
convergence. Equations (17)-(18) therefore give

  integral_{1/L}^1 [K_P(t)-1]dt = c log L+O(1),
  c=1/zeta(2) in sf; c=1 in geo.

Together with the nonnegative small-time part and (20), this proves the first
two assertions of (7). In particular both G_P tend to infinity.

Also the second spectral moment is uniformly bounded:

  H_P:=sum_D b_D/lambda_D^2
      =integral_0^infinity t[K_P(t)-1]dt <=H_*<infinity,         (22)

where (19), the integral comparison near zero, and exponential decay of
zeta(1+t)-1 at infinity prove finiteness. No inverse-zero-derivative sum occurs.
From (5), writing ell=1/C_P, obtain

  C_P-G_P=ell sum_D b_D/[lambda_D(lambda_D-ell)].                (23)

Once G_P>=2/g, (6) gives ell<=1/G_P<=g/2, so (23) is at most 2H_*/G_P.
This proves the final assertion of (7), including the stated grounded-gap
asymptotics. Every limit is over all real cutoffs P tending to infinity.

## 6. The root is a genuine slow channel, not a small centered eigenvalue

For normalized mean-zero f, (3) states the exact inequality

  |f(1)|^2<=G_P E(f).

Equality is attained by the finite visible spectral sum described in Section 2.
Thus the logarithmic growth is not an artifact of discarding signs or of a
numerical near-singularity. For a prescribed mean/root contrast a, the minimum
energy is exactly |a|^2/G_P. This is a capacity statement in the native harmonic
metric; it neither evaluates nor bounds the BSY entropy defect of actual xi.

For the stationary reversible chain generated by -L, G_P also equals the mean
hitting time of state 1. Indeed its return probability satisfies
P_t(1,1)/mu(1)=K_P(t), and integrating the centered return probability gives
(3). The same formula follows by solving the Poisson equation with forcing
xi-1 and imposing zero at 1. This interpretation is classical; the exact
arithmetic product and asymptotics above are the application proved here.

The usable conclusion is to KEEP the harmonic mean channel in a Schur
calculation, rather than treat fixing f(1) as a uniform way to eliminate it.
The centered inverse on these reservoirs remains bounded by 1/g. If grounding
is genuinely required, (3) and (5) price it exactly and allow directed finite
certification without forming the exponentially large graph matrix.

## 6.1 An exact coherent-channel Schur test

Let H0 be the mean-zero energy space and ell(f)=f(1)-mean_mu f. For any real
c and complex tau consider the COMPLETE specified block form

  Q(a,f)=c|a|^2+2 Re(conj(a) tau ell(f))+E(f), a in C, f in H0.

Let g_P be the root Green vector from Section 2, so ell(g_P)=E(g_P)=G_P
and the energy pairing of g_P with f equals ell(f). Exact completion gives

  Q(a,f)=E(f+conj(tau)a g_P)+(c-|tau|^2 G_P)|a|^2.              (24)

Consequently this entire block is nonnegative if and only if

  c >= |tau|^2 G_P.                                          (25)

No estimate of an unknown inverse remains in (25). If the inequality fails,
f=-conj(tau)a g_P is an explicit negative test. Thus fixed positive c and
nonzero fixed tau do NOT give positivity uniformly in P, despite the uniform
centered gap. The same statement for operator-valued retained data uses the
exact root-coupling B and its full adjoint; it is not inferred for an unrelated
source. We make no identification of c,tau with actual xi's missing mean terms.

## 7. Boundary of the attempted RH composition

Neither L nor its grounded resolvent is the critical xi operator. The full
Weil gamma/continuum/mean terms and their mixed couplings have not been
identified with the graph diagonal. The physical residual norm of PR803 is
also NOT the harmonic graph norm or its period mean. A positive constant
centered gap does not prove the retained Schur complement nonnegative.

The review/synthesis file states the missing source equality and signed bound
for each attempted composition. No member of (3)-(23) sets an unevaluated
RH-equivalent energy or intrinsic defect to zero. No new zero-free region,
prime-discrepancy exponent, or unconditional RH proof is claimed.

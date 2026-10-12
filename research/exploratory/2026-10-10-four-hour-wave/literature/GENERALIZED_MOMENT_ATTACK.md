# Generalized inverse moments: endpoint correction and the unpaid joint estimate

Date: 2026-10-10. Status: a new proved finite-support correction lemma and
conditional lower-moment lifting adapter, with a source-faithful open
estimate. No generalized moment, improved zero boundary or RH is proved.
This note extends a specific strict-exponent interface in PR915; it does
not relabel the partial results in PR913–915 as a full moment theorem.

## G1. Exact pinned sources and the remaining estimate

The independently read snapshots are outside the checkout:

| Packet | Exact Git commit | Load-bearing documents |
| --- | --- | --- |
| PR913 | `6498d6cc2eded03159c7332b25fd224ad07f89c1` | `GENERAL_MOMENT_ATTACK.md`, `FOURTH_MOMENT_ATTACK.md` |
| PR914 | `0cc0428fedbbfc340044c7451b3d392c1da9a103` | `CONDUCTOR_SECTORS.md`, `A2_COMPLETION.md`, `INTERACTION_GRAPH.md` |
| PR915 | `9959364671f89b86f3992ec5ed5e19f804eb607b` | `ANISOTROPIC_SINGLETON_CORES.md`, `COUPLED_THETA_COMPLETION.md`, `REUNITED_RAMANUJAN_EULER_PRODUCT.md` |

The literal local paths start at
`/workspace/.riemann-research/moment-sources/PR/standalone/`, with `PR`
replaced by its number. The exact checker binds the seven documents used
below by SHA256. The source papers and earlier checkers are unchanged.

Fix K=Q(sqrt(-3)), a fixed finite bad-prime set S, primary generators, a
fixed finite-order character nu and fixed compact smooth norm profiles.
Keep the literal nonunit zeros in chi_n(u)=(u/n)_6. The desired input is

    sum_(0<Nu<=H) |A_u(D)|^(2k) << H D^(k+epsilon),
    H=D^(1+theta),  theta>0 fixed,
    A_u(D)=sum_(n,S)=1 mu_K(n) nu(n) chi_n(u) W(Nn/D).        (G1)

Every row is retained, including sixth powers. Constants can depend on
each fixed k, theta, nu, S and finitely many profile seminorms. Arithmetic
H is neither imaginary zero height nor reflected dual row norm.

PR914 already controls all Hermitian tuples without singleton primes.
For the others, write g1 for the product of primes occurring exactly once
in the full 2k tuple, and g2 for the product of nonprincipal primes
occurring exactly twice. Its completed absolute accounting also controls
the region (Ng1)*sqrt(Ng2)<=H. Consequently the genuinely unpaid quantity
is the real signed remainder

    R_k^Phi = sum_(g1!=1, (Ng1)*sqrt(Ng2)>H)
                c(tuple) S_tuple^Phi(H),                    (G2)

and the full smooth moment is R_k^Phi+O(H D^(k+epsilon)). This is the
literal PR914 Section10 identity, not a selected sharp sector enlarged by
positivity. The sufficient new estimate is R_k^Phi<<H D^(k+epsilon).
The exact surviving Möbius sign is mu_K(f1*f3*f5), with fj the residual
conductor primes of exponent j mod6. Taking an arbitrary positive
coefficient envelope discards this sign. The principal masks do not supply
an additional hidden Möbius sign.

## G2. A useful extension at the critical Euler exponent

PR915's forward correction for a pairwise-coprime singleton core is

    B_(C,u)(X_1,...,X_k)
      = sum_d e_C(d) eta_u(d_1...d_k)
                    product_i A_u(X_i/Nd_i;W_i),             (G3)

where eta_u=nu*chi_u and C is a moving squarefree exclusion. At a good
prime outside C its local correction is

    E_p(z)=(1-sum_i z_i)/product_i(1-z_i).

For a nonconstant monomial z^e its coefficient is
1-|supp e|. At a prime of C the coefficient is one. At a prime of S there
is no correction. In particular outside C there are no single-axis terms.
Equation G3 is finite: a contributing d_i has Nd_i<=b_i X_i, where b_i is
the fixed upper support endpoint of W_i. Multiplication by eta_u(d_1...d_k)
is a contraction in the full row norm, including its exact zeros.

The earlier infinite absolute seminorm assumes alpha_i+alpha_j>1. For
the actual finite correction, the endpoint is available.

**Finite-support endpoint lemma.** Fix k and alpha_i>=1/2. Put
Z=max(2,max_i b_i X_i). For every eta>0,

    sum_(Nd_i<=b_i X_i) |e_C(d)| product_i Nd_i^(-alpha_i)
       <<_(k,alpha,S,eta) Z^eta (NC)^eta.                    (G4)

The implied constant is independent of C, X and the row. Thus several
axes may simultaneously have exponent exactly 1/2. This does not assert
convergence of the unrestricted infinite seminorm at that endpoint.

**Proof.** Drop the coupled support bounds and enlarge to the positive
Euler product over primes of norm at most Z. At an unmasked prime put
t_i=(Np)^(-alpha_i). Its full local absolute sum is exactly

    1 + sum_(I subset [k], |I|>=2) (|I|-1)
                          product_(i in I) t_i/(1-t_i).       (G5)

For sufficiently large Np, uniformly with alpha_i>=1/2 this is
1+O_k((Np)^(-1)); terms of support at least three are
O_k((Np)^(-3/2)). The finitely many smaller primes give a fixed positive
constant. To bound the truncated critical product without an unproved
prime estimate, let delta=1/log Z. For Np<=Z,

    (Np)^(-1) <= e (Np)^(-1-delta).

Elementary ideal counting gives zeta_K(1+delta)<<_K 1+1/delta. The Euler
product implies sum_p (Np)^(-1-delta)<=log zeta_K(1+delta).
Consequently the unmasked product is at most a fixed power of log(2Z),
hence <<_eta Z^eta. For a masked prime its local absolute sum is
product_i(1-(Np)^(-alpha_i))^(-1). Their product over p|C is
<<_(k,eta) (NC)^eta: above a fixed norm threshold each factor is at most
(Np)^eta, and the remaining primes contribute a fixed constant. The
unmasked product is at least one, so replacing its factors at C by the
masked ones has at most this cost. This proves G4. If an axis has a
bounded nonempty scale below one, its fixed support bound is included in
Z and the same proof applies. Empty rectangles contribute zero. QED.

The critical terms in G5 are precisely pair incidences between axes with
alpha_i=alpha_j=1/2. Their leading coefficient is one per pair. This
matches, rather than removes, the harmonic pair-overlap cost in PR913.

## G3. Lift a paid lower moment to several long singleton axes

Fix 1<=r<=k and assume, for each of the fixed profiles needed here and
every nonempty smaller scale 1/b_i<=Y<=D,

    sum_(0<Nu<=H) |A_u(Y;W_i)|^(2r)
       << D^epsilon H Y^r.                                 (OPEN/PAID-r)

For r=1 this is the imported second-moment adapter in PR913. For r>=2,
it is an additional input unless a source-qualified lower-moment theorem
has separately supplied it. Uniformity over the smaller scales, all rows
and the fixed profile family is essential; a bound only at Y=D does not
license the following convolution.

Also assume the conductor-uniform pointwise estimate

    |A_u(Y;W_i)| << D^epsilon Y^b,  1/2<=b<=1,              (G6)

throughout the same scales and row range. At b=1 this is elementary
counting. A smaller b requires a named analytic input with uniform row
conductor constants.

Let J be any r-axis set and let NC<=D^C0 with C0 fixed. Then

    ||B_(C,.) (X)||_2^2
      << D^epsilon H product_(i in J) X_i
                          product_(i not in J) X_i^(2b).     (G7)

**Proof.** At each smaller rectangle Y retain the same set J. Hölder
over the full row set gives

    sum_u product_(i in J) |A_u(Y_i)|^2
       <= product_(i in J) (sum_u |A_u(Y_i)|^(2r))^(1/r)
       << D^epsilon H product_(i in J) Y_i.

Apply G6 on the remaining axes. Take square roots, then use Minkowski in
the finite identity G3. The exact d weights are alpha_i=1/2 on J and b
elsewhere. G4 is valid at these endpoints. Taking its eta sufficiently
small absorbs both Z<=O(D) and NC<=D^C0 into the requested D^epsilon,
after squaring and assigning smaller preliminary losses. No derivative
of a changed test is introduced: each original W_i is kept at a shifted
scale. This proves G7. QED.

Ordering X_(1)>=...>=X_(k), choose the r largest axes for J. If
P=product_i X_i and Q_r=product_(i>r) X_(i), this reads

    ||B_C(X)||_2^2 << D^epsilon H P Q_r^(2b-1).              (G8)

For r=1 it recovers PR915's theorem, and G4 additionally permits the
endpoint b=1/2 if that pointwise premise is actually available. For r>=2
it gives a precise further range paid by the lower 2r moment. It does
not infer that premise from the second moment.

## G4. Retain all incidence interference

Use the exact PR913 expansion A_u(D)^k=sum_c z_c(u)B_C(X), with
|z_c(u)|<=1 and X_i=D/product_(I contains i,|I|>=2) Nc_I. For Q0>=1 let
F_(r,Q0) be exactly its portion with Q_r<=Q0. The fixed-order harmonic
pair-incidence sum and convergent higher-incidence sums give

    ||F_(r,Q0)||_2^2 << D^epsilon H D^k Q0^(2b-1).           (G9)

Indeed take square roots in G8, keep Q_r^(b-1/2)<=Q0^(b-1/2), and sum
the remaining weights product_(|I|>=2)(Nc_I)^(-|I|/2).
Pairs cost a fixed logarithmic power and subsets of size at least three
give convergent ideal sums. Squaring absorbs that fixed logarithmic
loss. This uses the norm of the entire selected polynomial, including
interference among its configurations.

A concrete new conditional range at k=3,r=2 has
c_{13},c_{23} each of norm about sqrt D, all other shared factors one,
and these two ideals coprime. Then X is about (sqrt D,sqrt D,1), P about
D and Q_2 about one. It lies outside the previous short-product range
P<=H^(1/2) and outside the growing common-gcd tail, and Q_1 about sqrt D
is outside PR915's subpower peripheral range. G9 controls it if the
uniform fourth moment at its two smaller scales is paid. This example
respects the incidence constraints; the superficially convenient tuple
(D,D,1) does not.

The full balanced core c_I=1 has X_i=D. For every fixed r<k its Q_r is
D^(k-r). Therefore this lifting adapter alone leaves a power loss
D^((k-r)(2b-1)). Setting r=k would assume the requested moment itself.
The new endpoint lemma removes a technical correction obstruction, not
the balanced-core analytic obligation.

## G5. Price the reflected joint estimate before attempting a contour shift

PR915's coupled reflection exposes a genuine angular character and an
exact quadratic cross-symbol. Its all-negative allocation still has
mean-square bound Hdual/A + Hdual^2 A^2/B. At A=B=D the initial fourth
moment needs Hdual about D^(3-theta), while that second term is
D^(7-2theta), far above the required D^2 canonical scale. Improved cube
and squarefree-divisibility components do not suppress this term.

The reunited Ramanujan product at fixed theta index n is exactly

    F_(k,n)(w,r) = L(r,chi+) L(v,kappa_k)/L(w,chi-)
                     * E_(k,n)(w,v),  v=w+r-1,

with infinity types +3 and -3, respectively. Its proved Euler remainder
region is Re w>0, Re v>1/2, Re(w+v)>1. But after summing the actual
Gauss-theta n coefficients the sufficient absolute-convergence region
still forces Re v>5/2. The possible finite-order pole is at v=1 and
the outer ratio is A^(v-1)*(Nk^2/(cAB))^t. A useful shift therefore
requires a **joint** continuation and mean-square theorem for the
deformed Gauss series, reciprocal angular factor, moving k Euler masks
and polar divisor. A fixed-n Euler identity is not such a theorem.

PR915's `PRIMARY_SOURCE_MATCH.md`, Section4, already isolates the divisor
deformation and its Gauss CRT moving twist. At an n-prime its exact
additional local ratio is

    (1+(q-1)x_p)/(1-x_p+z_p),
    x_p=chi-(p)q^(-w), z_p=kappa_k(p)q^(-v).

This formula is used only where its denominator is nonzero. It should
not define the global object by dividing by a potentially vanishing
factor: the original local numerators and the holomorphic remainder
definition in PR915 remain authoritative. Its divisor expansion would
produce the literal Gauss CRT auxiliary twist chi_(n')(d)^4. This is the
same moving twist as the source theta completion, so it is a plausible
joint representation rather than an arbitrary coefficient insertion.
The analytic summation, possible polar cancellation and contour bound
are OPEN. A further attack must pay this summation jointly, rather than
claim the divisor reorganization as a new estimate. The finite endpoint
correction G4 cannot be substituted for
them because their coefficient amplitude contains q^(1-Re w).

## G6. What this pass establishes

The new proof is G4 and its conditional consequences G7–G9. The exact
checker covers critical local coefficients, the finite correction with
all masks, source sign bookkeeping, scale and incidence controls; it
does not authenticate an asymptotic moment estimate. The inherited
controlled regions and full generalized hierarchy remain distinct.
In particular no additional mixed fourth moment or signed remainder
bound has been paid in this pass. The strongest useful remaining target
is the actual signed G2 estimate, or a joint reflected theorem strong
enough to imply it, with all source conductors and profiles retained.

The coordinator independently read and accepts G4 and G7–G9 at their
displayed conditional scope. Normal and optimized exact checker replays
are byte-identical. The later companion `OPPOSITE_THETA_DERIVATIVE.md`
pays a precisely specified completed standard-cusp negative allocation;
it does not supply the full signed G2 estimate.

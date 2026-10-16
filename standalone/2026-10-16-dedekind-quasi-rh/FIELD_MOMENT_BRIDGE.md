# Native moments over a general field: a mask-preserving extraction theorem

Status: PROPOSED CONDITIONAL component theorem. The implication is proved
below; its full native-moment hypothesis is NOT proved. No new 17/24 theorem.
Credit: sixth-power extraction and Mellin detection are classical within the
imported architecture (Cureton--Thorner v2 Section 2.2, crediting OpenAI's
shorter proof). The formula 1/2+5h/(12k)+e/(2k) already appears in this repo,
including PR #946 Section 7. We do not claim that formula as new. This note
supplies a self-contained balanced-box general-field implementation and an
explicit recursive treatment of the moving prime mask.

## 1. Exact field, rows, coefficients and quantifiers

Fix a number field F containing mu_6, d=[F:Q], a finite prime set S containing
primes above 6, and a fixed finite-order Hecke character psi whose conductor
is supported on S. For ideals prime to S let chi_a(u)=(u/a)_6, defined
primewise by the residue-field sixth-power character and extended
multiplicatively. It is zero if u and a share a prime. This definition does
not require choosing a generator for every ideal.

For W in C_c^infinity(0,infinity), set

    A_u(D;W,psi)=sum_(a prime to S) mu_F(a)psi(a)chi_a(u)W(Na/D),
    M(D;W,psi)=A_1(D;W,psi).                               (1)

Choose a sufficiently large constant C_F once, and define a finite set

    R_H={0!=u in O_F : |sigma(u)|<=C_F H^(1/d)
                           for every archimedean embedding sigma}. (2)

There are O_F(H) such elements for H>=1 by lattice counting. In a general
field with positive unit rank, the set {u:0<|N(u)|<=H} is infinite; it must
NOT be substituted for (2). This is a new precisely specified row hypothesis,
not a claim that the paper's adelic measure has already been identified with it.

**Classical replica input.** For large H, (2) contains at least
c_F H^(1/6)/log(2H) distinct elements pi^6, with (pi)=p a prime ideal outside
S and Np comparable to H^(1/6). To see this, use the prime ideal theorem in
the principal ideal class in a fixed norm annulus. For each principal prime,
choose an integral generator. The logarithms of units form a full lattice in
the norm-zero archimedean hyperplane (Dirichlet's unit theorem). Multiplying
by a unit brings the normalized logarithmic sizes into one bounded
fundamental parallelepiped. Hence |sigma(pi)|<=C'_F (Np)^(1/d) at every
embedding, and pi^6 belongs to (2) after fixing C_F large enough. Different
prime ideals give different sixth powers. These are fixed-field classical
inputs; no uniformity in discriminant or degree, and no GRH, is invoked.
A fixed principal ray class can be used instead when fixed local congruences
are imposed; its finite-index unit subgroup gives the same conclusion.

## 2. Conditional theorem

Fix k>=1, 0<h<6 and e>=0, and write

    lambda=1/2+5h/(12k)+e/(2k).                             (3)

Assume that for EVERY fixed compact smooth test W and every epsilon>0,

    sum_(u in R_(D^h)) |A_u(D;W,psi)|^(2k)
          <= C_(F,S,psi,W,k,h,e,epsilon) D^(h+k+e+epsilon)  (4)

for all D>=2. No moment estimate for a moving conductor or prime exclusion
is part of this hypothesis. The assertion is interesting when lambda<1.

**Theorem.** Under (4), for every fixed W and every epsilon>0,

    |M(D;W,psi)| << D^(lambda+epsilon).                     (5)

Consequently L(s,psi,F) has no zero in Re(s)>lambda (away from the pole at
one for the principal character). If lambda>=1 the same conclusion follows
already from the elementary bound M(D)<<D and absolute convergence.

### Proof: first extract a masked scalar

On u=pi^6, the character is exactly 1_(p not dividing a). Define

    M_p(D)=sum_(p not dividing a) mu_F(a)psi(a)W(Na/D).

The fixed exclusions S remain throughout. By the replica count and (4),
for each sufficiently large D at least one such p, with q=Np comparable to
D^(h/6), satisfies

    |M_p(D)| << D^(lambda+delta)                            (6)

for any fixed delta>0; absorb the logarithm into delta. The prime can depend
on D. No claim of a bound for every replica is needed.

### Proof: remove the moving mask by a scalar bootstrap

Unique factorization of ideals and the Mobius value at a repeated prime give

    M(D)=M_p(D)-psi(p)M_p(D/q),
    M_p(D)=sum_(j>=0) psi(p)^j M(D/q^j).                   (7)

The second sum is finite, because W has compact support bounded away from
zero and M(T)=0 for all sufficiently small T. There is no new coprimality
condition on the recursive scalar M.

Suppose |M(T)|<=C_B T^B for all T>0, with B>0. Elementary ideal counting
starts this at B=1. From (7), uniformly over p,

    |M_p(D)-M(D)| <= C_B sum_(j>=1)(D/q^j)^B
        <= C_B D^B q^(-B)/(1-q^(-B))
        << D^(B(1-h/6)).                                  (8)

Constants in q comparable to D^(h/6) are fixed and are absorbed here.
Combining (6) and (8) improves the scalar exponent from B to

    max(lambda+delta, (1-h/6)B).                            (9)

Choose delta smaller than the requested epsilon. Since 0<1-h/6<1, finitely
many iterations starting from B=1 reach lambda+delta. Every step uses the
same W and psi, (4) at the same class of all scales D, and scalar bounds
already proved at shorter arguments. Constants may grow with the finite
number of steps; that does not affect (5). Bounded D is absorbed separately.
This proves (5).

This recursion matters: retaining only the original crude error D/q would
leave a floor 1-h/6, and would not justify the cofinal high-moment conclusion.
No disappearing prime-divisibility mask has been assumed.

### Proof: exclude denominator zeros

In Re(s)>1, direct Mellin integration gives

    integral_0^infinity M(D)D^(-s) dD/D = W_hat(s)/L^S(s,psi,F). (10)

The integral is holomorphic on Re(s)>lambda by (5), with uniform dominated
convergence on each compact subset. At a hypothetical zero rho there,
choose W(y)=y^(-rho)phi(y), with phi>=0 nonzero compact smooth. Then
W_hat(rho)=integral phi(y)dy/y>0, so the right side would have a pole, a
contradiction. The omitted finite Euler factors have no zeros in Re(s)>0.
This proves the theorem. QED.

## 3. Exact consequences, all conditional on the ORIGINAL full moments

With e=0 and admissible h arbitrarily close to 1 from above, (3) gives

|Moment order 2k|Limiting zero-free boundary|
|---:|---:|
|2|11/12|
|4|17/24|
|6|23/36|
|12|41/72|
|2k|1/2+5/(12k)|

To deduce any strict zero-free half-plane, choose h and epsilon sufficiently
close to their limits; no estimate ON the boundary is asserted.

A cofinal sequence k_j -> infinity with 0<h_j<6 and e_j=o(k_j), satisfying
(4) at those orders for every W, implies no zeros with Re(s)>1/2. No uniform
constant in k_j is needed for that qualitative statement: fix a hypothetical
zero first, then choose ONE sufficiently large order. For psi principal,
the functional equation then gives RH for zeta_F. Finite-order Hecke
characters are handled one at a time; the conjugate-character functional
equation gives the corresponding critical-line conclusion.

If such moment theorems were available over every F containing mu_12, then
for arbitrary K one could take F=K(mu_12). This extension is abelian;
zeta_F is zeta_K times entire nonprincipal Hecke factors, so a zero of
zeta_K away from one cannot be canceled. This is the same classical descent
used by the imported paper, not a new result of changing fields.

## 4. What the new general-field paper does NOT supply

Its reflected theta second mean (Proposition 9.1) concerns a completed,
transformed family B_m, followed by an additive average. It is not (4) for
all k, or even a statement that the full Eisenstein native mean-square
argument of its Section 2.2 has been transported into (2) without new work.
One must track the actual row measure, cube removal, full composite
cofactors, test functions, and prime zeros to make that bridge.

The immediate theoretical target is the native FOURTH moment (4), first for
one fixed field beyond Q(omega), or for the original field with the full
signed remainder restored. The more ambitious target is a cofinal hierarchy
with e_k=o(k). A diagonal random model, a principal-only reference, or a
bound after deleting long-singleton tuples is not (4).

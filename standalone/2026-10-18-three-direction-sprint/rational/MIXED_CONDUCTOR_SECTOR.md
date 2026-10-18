# The complete small-conductor sector of the mixed inverse/plain mean

**PROPOSED.** The estimate below is unconditional over the Eisenstein field
in the fixed primary conventions of the pinned OpenAI source. It pays the
entire primitive-conductor-at-most-U part of the actual mixed mean, including
shared powers and all nonunit zeros. It does not estimate the remaining
large-conductor correlations or improve a zeta zero-free boundary.

The proof uses elementary ideal counting, the primitive finite-field Gauss
identity, and planar Poisson summation. It does not assume an improved
arbitrary-coefficient sextic large sieve or a cancellation theorem for
Möbius sums. The final question concerns the actual remaining signed sum,
not a selectable or frozen subvector.

## 1. The actual coefficient and the order of majorization

Work in E=Q(omega), O=Z[omega], with the fixed good-primary and fixed-S
conventions of `../eisenstein/_source-original-quasi.tex`. Every ideal has
only boundedly many relevant primary/unit presentations. Write q_a=Na.
At one fixed choice of the detector parameters put

    M_u=D^(-1/2) sum_d mu(d) nu(d) chi_d(u)^epsilon W_M(q_d/D),
    S_u=N^(-1/2) sum_n       nu(n) chi_n(u)^epsilon W_S(q_n/N),
    L=DN,   epsilon in {-1,+1}.

Both profiles have fixed annular support and bounded absolute size. The
same finite character nu and orientation occur in both factors, and their
height is synchronized as in the source. No coprimality condition between
d and n is imposed. Let

    c_A=L^(-1/2) nu(A)
          sum_(dn=A) mu(d) W_M(q_d/D) W_S(q_n/N).        (1)

Thus `M_u S_u=sum_A c_A chi_A(u)^epsilon`, exactly, including every
shared-prime zero. Its support lies in `cL<=q_A<=CL`, with fixed positive
constants, and

    |c_A| <= C L^(-1/2) tau(A).                         (2)

The powers x^(-sigma-i omega) in the actual synchronized profiles respect
this bound uniformly in their common height; sigma ranges over a fixed
compact interval. Rowwise parameter choices must first be treated by the
source's common Sobolev separation. They are not choices of c_A after the
row sum has been opened.

Choose a fixed nonnegative smooth planar annular majorant Phi of the
original row box. Enlarge the POSITIVE mean over sixth-power-free physical
rows to

    T(U)=sum_(u in O) Phi(u/sqrt(U))
                     |sum_A c_A chi_A(u)^epsilon|^2.    (3)

The fixed row exclusions at S remain as a zero mask. Fixed unit/ray
subdivisions may be retained as finitely many such expressions. This
positive enlargement occurs before expansion. Once (3) is expanded, its
conductor sectors have signed kernels; they must not individually be
enlarged from sixth-power-free rows.

For the radial notation `Phi(Nu/U)` used by the source, (3) has the same
meaning. A fixed compact-shape planar profile is equally admissible.

## 2. Exact conductors and the masked row kernel

For a pair A,B and every good prime P let

    e_P = v_P(A)-v_P(B) modulo 6,
    C(A,B) = product_(e_P != 0) P,
    R(A,B) = product_(e_P = 0, P|AB) P.

The complete row character is

    chi_A(u)^epsilon conjugate(chi_B(u)^epsilon)
        = theta_C(u) 1_((u,R)=1),                     (4)

where theta_C is primitive with conductor C if C is not the unit ideal.
Its local exponent is epsilon*e_P. It is nonprincipal at every P|C;
raw sextic symbols at good primes have exact order six. The primes in R
are zero-only masks and cannot be erased. Fixed S masks may be multiplied
into R, at a fixed cost. A fixed finite residue subdivision can instead
be completed separately; its number and its modulus are fixed.

Let K_U(A,B) be the row sum in (3) of (4). Then

    |K_U(A,B)| <= C_Phi (NC)^(1/2) tau(R)       if C != 1,
    |K_U(A,B)| <= C_Phi U                       if C = 1. (5)

Here and below U>=1. We prove the nonprincipal estimate including the
imprimitive masks. Expand `1_((u,R)=1)=sum_(b|R,b|u) mu(b)`. For each b,
primitive Poisson summation and the Gauss-root modulus one give, up to a
fixed harmless field normalization,

    U/(Nb sqrt(NC)) Gamma(theta_C) theta_C(b)
       sum_h conjugate(theta_C(h))
           Phihat(sqrt(U) h/(sqrt(Nb) c)),             (6)

where `|c|^2=NC`. The precise dual ideal and fixed different change only
the field constant. The h=0 term vanishes because C is nonprincipal.
Planar lattice counting and Schwartz decay give, for every lambda>0,

    sum_(h != 0) (1+lambda Nh)^(-A) <= C_A/lambda,
        A>1.                                          (7)

For lambda<=1 this is ordinary lattice counting. For lambda>=1 use
`lambda^(-A) sum_(h!=0)(Nh)^(-A) <= C_A/lambda`.
Taking `lambda=U/(Nb NC)` in (7) cancels the factor U/Nb in (6),
and each b costs at most `C sqrt(NC)`. Summing b|R proves (5).
The C=1 bound follows by counting the original rows, with its complete
zero mask still present. In particular no false nonprincipal Gauss
formula is used for the principal diagonal.

## 3. A complete pair-counting estimate

For every Q>=1,

    sum_(A,B on the support, 1<NC(A,B)<=Q)
       |c_A c_B| sqrt(NC(A,B))
             <<_epsilon L^epsilon Q^(1+epsilon),      (8)

and

    sum_(A,B on the support, C(A,B)=1)
       |c_A c_B| <<_epsilon L^epsilon.                (9)

These bounds already include every old product in (1). They also hold
for any coefficient vector obeying (2); there is no Möbius cancellation
hidden in their proof.

To prove them, factor `g=gcd(A,B)`. The two remaining ideals are coprime.
Extract their sixth powers uniquely:

    A=g*a*m^6,   B=g*b*n^6,

where a,b are sixth-power-free and coprime, and

    C(A,B)=rad(ab).

There are further coprimality conditions on m,n,a,b. Discarding them is
legal in this nonnegative upper bound. For each fixed a,b,m,n, ideal
counting bounds the possible g by

    C L/max(Na*(Nm)^6, Nb*(Nn)^6).

If the displayed quotient is below one there are no g, so this formula
does not omit a lattice boundary term. The elementary inequality

    1/max(x,y) <= 1/sqrt(x*y)

and convergence of the ideal zeta series at 3 show

    sum_(m,n) 1/max(Na*(Nm)^6, Nb*(Nn)^6)
                  <= C/sqrt(Na Nb).                  (10)

Every divisor factor in (2), and tau(R) when needed in (5), is at most
`C_epsilon L^epsilon` because q_A,q_B≈L. For a fixed squarefree C,
each prime P|C is assigned to exactly one of a,b, with exponent
j in {1,...,5}. Therefore

    sqrt(NC) sum_(rad(ab)=C,(a,b)=1) 1/sqrt(Na Nb)
      = product_(P|C) [2 sum_(j=1)^5 (NP)^((1-j)/2)]
      <= C_epsilon (NC)^epsilon.                    (11)

The last inequality is the usual fixed-divisor-power bound: the local
factor is bounded and tends to 2, and any fixed bounded local factor
over squarefree primes is O_epsilon((NC)^epsilon). Sum (11) over
`NC<=Q`; there are O(Q) ideals. The pair count supplies L, which is
canceled by the L^(-1) in |c_A c_B|. This proves (8). When C=1,
`a=b=1`; the convergent double sum in (10) directly proves (9).

The same argument proves a useful general fact. For fixed order k>=3,
replace sixth powers by kth powers and the exponent set by {1,...,k-1}.
The m,n series is at k/2>1, hence converges. No squarefree-column
assumption is needed. We use k=6 here because it is the actual source.

## 4. The paid sector and the precise remainder

Expanding (3), write T=T_small(Q)+T_large(Q), where the first term
contains exactly `NC(A,B)<=Q`, including C=1. From (5), (8), and (9),

    |T_small(Q)| <<_epsilon (U+Q) L^epsilon Q^epsilon. (12)

For D=U, N=U^(1/2), take Q=U. Since L=U^(3/2), the COMPLETE
small-conductor contribution is `O_epsilon(U^(1+epsilon))`. Thus the
actual improving mixed target is reduced to estimating the signed sum

    T_large(U)=sum_(A,B, NC(A,B)>U)
                    c_A conjugate(c_B) K_U(A,B).       (13)

All sixth-power-free physical rows were already included before this
partition, all shared powers enter C,R exactly, and every product in
(1) remains. A bound `T_large(U)<<U^(1+epsilon)` from above would prove
the same bound for (3); an absolute-value bound is sufficient but is
not required. We do not know that estimate. The individual sectors of
(13) can have either sign.

There is a second elementary source-specific support restriction. Here
`squarefree_kernel(a)=product_(v_P(a) odd) P` is the odd-exponent core.
Since d is squarefree, at every prime lost from that kernel of dn,
n contains that prime. Consequently

    N(squarefree_kernel(dn)) >= Nd/Nn,

so the corner coefficient (1) is supported on squarefree kernels
`>>D/N≈U^(1/2)`. Separately, if dn is a kth power for any integer k>=2,
squarefreeness of d forces n to contain d^(k-1), so Nn>=Nd^(k-1).
Thus there are no perfect-power products when the two annuli are strictly
separated with Nd>Nn. This does not remove
the known Gauss bias, whose bad vectors can already be squarefree.

Finally, `mu*1=delta` is an exact low-product identity for a COMPLETED
prefix convolution. The source zero detector uses that identity before
selecting its dyadic witnesses. The particular corner D=U,N=U^(1/2)
has products of size U^(3/2); it contains no small products on which
the literal delta identity could annihilate (1).

## Source and review scope

The synchronized witness and profiles are the pinned source's
Proposition `detector-witness`, in
`../eisenstein/_source-original-quasi.tex`, around lines 4510--4680;
the normalization is its equations `old-eq:1.1` and `old-eq:1.1a`.
The conductor decomposition is the primitive local power-residue identity,
and (6) is ordinary primitive planar Poisson with its full R mask.
The Eisenstein teammate independently checked the proposed small-conductor
count and the nonprincipal Poisson scaling before this draft. This is
internal first-read feedback, not final-SHA review or external acceptance.

For a different number field, the pair-counting proof remains valid for
ideals. Applying (12) there additionally requires its uniform smooth
primitive-character bound (5) in the actual compact-shape row convention;
that interface is not silently inferred from the planar argument above.

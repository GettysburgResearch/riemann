# Exact signed Fourier transport of the short norm-ball measure

Status: **Root-reviewed finite-source component identities C-F1--C-F5.**
Every displayed short weight is the actual lattice norm-ball count.
No short-row moment upper bound or new zero-free region is proved.
The conditional statement C-F5 retains the root packet's full-family
analytic input and its essential unit-frequency restriction.

## C-F1. Fourier transport retains the unpaid weight

Let G=O_K/Q, q=|G|, and let t be the unit CRT translator in
`correlations/MOBIUS_CRT_TRANSLATION.md`: chi_p(t)=-1 at every source
prime. For a finite unsigned profile C and integer k>=1, put

    f(v)=|C(v)|^(2k),
    L_H(v)=#{u != 0: Nu<=H and u mod Q=v}, R_H=sum_v L_H(v).

For additive characters e_lambda of G use unnormalized transforms

    hat(g)(lambda)=sum_v g(v) conjugate(e_lambda(v)).

Let t*lambda be the character v -> e_lambda(tv). The exact Möbius
translation A(u)=C(tu) and finite Fourier orthogonality give

    S_mu(H)=sum_v f(v)L_H(t^-1 v)
           =(1/q)sum_lambda hat(f)(lambda)hat(L_H)(-t*lambda).

In particular,

    S_mu(H)-S_plus(H)
      =(1/q)sum_(lambda!=0) hat(f)(lambda)
                    [hat(L_H)(-t*lambda)-hat(L_H)(-lambda)].       (C-F1)

To check the inverse direction, substitute v=tu in the weighted sum.
The transform of v -> L_H(t^-1 v) is hat(L_H)(t*lambda), because
substitution v=tw in that transform gives e_lambda(tw). The zero
frequency in C-F1 cancels exactly. Replacing the remaining weight by
its mean would discard the entire difference being investigated.

## C-F2. Exact local Gauss signs and every zero mask

Identify the additive dual of each residue field F_p with that field
by a fixed nontrivial additive character psi_p. At a source prime with
at least one occurrence in a moment tuple, write d=r-s modulo six,
where r,s count left and right occurrences. Its local factor is
g_d(u)=chi_p(u)^d for u!=0 and g_d(0)=0, including d=0. Its transform is

    d=0: hat(g_d)(0)=Np-1, hat(g_d)(b)=-1 if b!=0;
    d!=0: hat(g_d)(0)=0,
           hat(g_d)(b)=chi_p(b)^(-d) tau_d if b!=0,
    tau_d=sum_(u!=0)chi_p(u)^d psi_p(-u), |tau_d|^2=Np.          (C-F2)

The nonprincipal formula follows from changing variables u to b^-1 u.
For its squared norm, write u=zv in the double sum. The v-sum is Np-1
when z=1 and -1 otherwise; the nontrivial multiplicative character has
sum zero, so the result is Np. The principal values are additive
orthogonality with its zero residue removed.

If a prime is absent from the entire tuple, its factor is instead the
constant one: its transform is Np at b=0 and zero off zero. That inactive
factor must not be confused with the active principal coprimality mask.

Since chi_p(t)=-1, multiplication of b by the local t changes an active
nonprincipal transform by (-1)^d. It preserves every principal mask and
inactive delta. The tuple's Möbius sign is also exactly

    product_p(-1)^(r_p+s_p)=product_p(-1)^(r_p-s_p).

Thus the signed dual expansion retains the same parity pattern as the
literal Möbius source, with its local Gauss phases. It is not a positive
sum over generic unsigned correlations. Arbitrary fixed coefficient
characters remain in the tuple coefficients; the sign calculation is
unchanged. Taking absolute values term by term erases this parity.

## C-F3. A source-blind Parseval bound and its cost

The zero mode is R_H times the complete-residue mean E_G f. Cauchy--
Schwarz and Parseval give the exact generic discrepancy bound

    |S_mu(H)-R_H E_G f|
      <=sqrt[(sum_v f(v)^2-q(E_G f)^2)
                      (sum_v L_H(v)^2-R_H^2/q)].                (C-F3)

The same right side applies to the unsigned source: multiplication by
t merely permutes its Fourier coefficients. All unweighted Fourier
l^p norms are likewise equal. A distinction between these sources must
therefore retain their relation to the lattice-weight frequencies or
another source-specific structure.

If NQ>4H, the norm-ball points have distinct residues. Indeed two
different points in that ball have difference norm at most 4H, while
a nonzero element of the ideal Q has norm at least NQ. Thus L_H is a
zero-one function and the right side becomes

    sqrt(q R_H-R_H^2) sqrt(E_G f^2-(E_G f)^2).

For a large CRT modulus this generic estimate pays a square root of
q rather than a short-row cancellation gain. This explains the cost
of discarding the signed frequency/weight correlation; it is not an
impossibility theorem for a future sharper argument.

## C-F4. Actual finite norm-ball controls

`check_crt_short_fourier.py` uses actual split ideals of norms 7,13,
the translator 34 modulo 91, and the unsigned hypercube
C=(1+chi_7)(1+chi_13). It enumerates complete Eisenstein norm balls at
H=16,32,64, retaining every nonzero lattice row and any repeated residue.
For k=2 its exact signed and unsigned fourth sums are:

| H | Rows | Maximum residue multiplicity | Signed sum | Unsigned sum |
|---:|---:|---:|---:|---:|
| 16 | 60 | 1 | 1734 | 1878 |
| 32 | 120 | 2 | 3666 | 3522 |
| 64 | 240 | 3 | 7134 | 6894 |

The difference can have either sign. The checker verifies C-F1 by exact
cyclotomic polynomial Fourier arithmetic, rather than numerical complex
evaluation, and verifies the local C-F2 masks/Gauss identities at every
frequency of the two split fields. The source is a finite hypercube,
not the native sharp-band profile; these controls certify only the stated
finite identities. The root's native finite probes are a separate input.

## C-F5. Conditional unit-frequency nonreturn, with its guard

Suppose the coherent-translator conclusion T-M3 of the root packet holds
for fixed smooth nonnegative native profile W and its active source prime
set P_D: for every fixed P>0, every row w with chi_p(w)=-1 at every
p in P_D has Nw>D^P for all sufficiently large D. This conclusion is
conditional on the exact uniform full-family B<1 input stated there.

Let t_D be any such translator. Fix A,B>0. For sufficiently large D,
there are no elements b,v satisfying all three conditions

    b is a unit modulo Q_D, Nb<=D^A,
    v == t_D b modulo Q_D, Nv<=D^B.                         (C-F5)

Otherwise w=v b^5 is nonzero, has Nw<=D^(B+5A), and satisfies
chi_p(w)=chi_p(t_D)chi_p(b)^6=-1 at every active prime, contradicting
T-M3 with P=B+5A. No assertion that b^6 is the unit residue is needed;
only its sixth-residue character is one.

This forbids polynomially small returns of coherent multiplication on
the unit part of the additive dual, under the stated analytic input.
The unit hypothesis is essential to that proof. Native moment tuple
transforms have zero coordinates at primes outside their tuple union,
by the inactive delta in C-F2. They are often nonunits in the entire
source residue ring. C-F5 consequently does not control those masked
frequencies and supplies no full short-row upper moment. A new argument
must still pay their signed, incomplete lattice correlation.

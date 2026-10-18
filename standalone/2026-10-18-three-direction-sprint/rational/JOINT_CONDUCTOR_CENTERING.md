# A legal simultaneous row-conductor filter and pair-conductor centering

**PROPOSED complete source-qualified sector estimate.** The remaining
centered form is OPEN. This note repairs a possible interaction gap:
the unfiltered sixth-power-free pair kernel must not be reused after
an arbitrary arithmetic row restriction. The new smooth radical filter
is retained inside its own complete kernel estimate below.

Use the full actual synchronized corner D=U,N=sqrt(U), common fixed
profiles and height, complete good sixth-power-free physical rows Nu≈U,
all inverse and plain input powers and every original nonunit zero.
The only deep moment import is the pinned source inverse amplification
at e(1)=1. The plain reflection and primitive planar Poisson inputs
are those used in `ROW_CONDUCTOR_FILTER.md` and
`MIXED_CONDUCTOR_SECTOR.md`. Common profile parameters must be separated
by the source's common Sobolev argument BEFORE opening the family.

Let R(u)=N(rad u), so the primitive row conductor is comparable to R(u)
with fixed constants. Choose a fixed smooth function tau:[0,infty)->[0,1]
equal to zero on [0,1] and one on [2,infty). Put

    rho_hi(u)=tau(R(u)/Q0),    rho_lo(u)=1-rho_hi(u).     (1)

The weights in (1) partition the ORIGINAL positive mixed mean exactly.
They are not projections of a signed pair-conductor expansion.

## 1. The complete low-radical row contribution

The pointwise primitive plain reflection gives
`|S_u(N)|^2<<R(u)/N*(1+T)^A`. Therefore the source inverse second
moment proves

    E_lo=sum_u w_u rho_lo(u)|M_u S_u|^2
        <<_epsilon U^(1+epsilon) Q0/N*(1+T)^A.          (2)

All rho_lo rows have R(u)<=2Q0. No squarefree row presentation is
assumed. This is the complete row-sector estimate, with every column
and shared input prime retained.

## 2. The actual high-radical pair kernel

Let theta be a nonprincipal primitive good character of pair conductor
C, with any original zero-only row mask B. The kernel to be estimated is

    K_hi(theta;B)=sum_(u sixth-power-free)
       theta(u)1_((u,B)=1) w(Nu/U)tau(R(u)/Q0).          (3)

Fixed original primary rays and supported local sectors remain in (3).
We claim, uniformly in Q0 and all polynomially bounded masks,

    |K_hi(theta;B)|
        <<_epsilon U^(1/2+epsilon)(NC)^(1/4+epsilon)
                         (NB)^epsilon.                (4)

Uniquely write u=v z, where v is the squarefree product of primes of
valuation ONE in u, and z is the powerful part, with prime valuations
in {2,3,4,5}. Then `(v,z)=1`,

    Nv≈U/Nz=:V,       R(u)=Nv*N(rad z).

For each fixed z the summation in v has the smooth radial profile

    w(Nv/V)*tau(Nv*N(rad z)/Q0),                        (5)

and the original coprimality mask Bz. On its fixed annulus the Euler
derivatives of (5) are uniformly bounded: when the tau factor varies,
its argument lies in [1,2]; outside that region it is constant. The
possible ray of v is one of a fixed finite list inherited from z.
The outside theta(z) has modulus at most one, retaining all its zeros.

Primitive Poisson and the exact squarefree divisor expansion give
the uniform v-kernel bound

    <<_epsilon (V NC NB Nz)^epsilon V^(1/2)(NC)^(1/4).  (6)

This is the squarefree kernel reconstructed in
`../eisenstein/GROWING_GAUSS_GRAM.md`, Section 1. Its elementary proof
uses `sum_a min(V/(Na)^2,sqrt(NC))`; if NC>V^2 the trivial O(V)
bound is already no larger than (6). Thus no lost conductor range
appears when z is large.

Summing (6) over EVERY powerful z is legal because

    sum_(Nz<=C U,z powerful)(Nz)^(-1/2)
                          <<_epsilon U^epsilon.        (7)

For example multiply the summand by U^epsilon/(Nz)^epsilon and
extend to infinity. The local Euler factors at exponent
1/2+epsilon are `1+sum_(e>=2)(Np)^(-e(1/2+epsilon))`, whose product
converges absolutely. Equations (5)--(7) prove (4). Every powerful
row part and its shared-prime zero conditions have been included.

The stronger UNFILTERED sixth-power-free kernel cannot simply be
substituted for (4). The squarefree decomposition is the explicit
price paid for the actual radical filter.

## 3. Complete small-pair-conductor cost under this filter

For A_i=d_i n_i, the primitive pair conductor C is the radical of
the nonzero exponent differences modulo six; primes with zero
differences retain their original zero-only mask. The exact
gcd/sixth-power count in `MIXED_CONDUCTOR_SECTOR.md` gives, at each
fixed C, complete absolute coefficient-pair mass

    <<_epsilon U^epsilon (NC)^(-1/2+epsilon).           (8)

This estimate also holds after the additional fixed restrictions
d1!=d2,n1!=n2. The restricted expanded coefficient need not factor
as c_(A1)bar c_(A2), but its absolute value is bounded by the SAME
divisor majorant `tau(A1)tau(A2)/(DN)` used to prove (8).

The principal C=1 part costs O(U^(1+epsilon)) by absolute counting.
For 1<NC<=Q1, (4) and (8), summed over ideals C, give

    |C_diff,hi,NC<=Q1|
       <<_epsilon [U+U^(1/2)Q1^(3/4)]
                               U^epsilon(1+T)^A.       (9)

This is a bound for the actual filtered signed sector. No positive
enlargement is performed after separating pair conductors.

## 4. Exact centering and a single complete open form

The full d1=d2 and n1=n2 strips of E_hi each cost U^(1+epsilon),
by `ACTUAL_RECTANGULAR_CENTERING.md`: inserting rho_hi<=1 preserves
their positive upper bounds. Their overlap is nonnegative O(U).
Consequently exact inclusion-exclusion and (2), (9) yield

    E = C_diff,hi,NC>Q1
        +O_epsilon([U+U Q0/N+U^(1/2)Q1^(3/4)]
                                  U^epsilon(1+T)^A).  (10)

The term on the right is the ENTIRE actual both-different covariance,
on the SAME original rows with smooth weight rho_hi, retaining every
pair conductor NC>Q1, every shared prime and the complete profiles.
It is real by conjugate pairing and need not be nonnegative.

For the corner, take Q0=U^(7/10),Q1=U^(9/10). The paid terms in (10)
cost at most U^(6/5+epsilon); the small-pair-conductor term alone has
exponent 47/40=1.175. One may reduce Q0 by any fixed small power if
a strict margin below 6/5 is wanted for that component.

A full upper bound U^(6/5+epsilon) for the remaining signed term
would therefore prove that corner mean bound. It is OPEN. The
unfiltered larger cutoff Q1=U^(9/8) from
`ACTUAL_SIXTHFREE_SECTOR.md` is deliberately NOT retained here:
it belongs to a different kernel estimate.

The squarefree-COLUMN adapter is another exact full-vector tool, but
its outer Minkowski decomposition does not preserve the original
both-different restriction term by term. Combining it with (10)
requires an explicit new centering argument in its own variables.
Other witness lengths still require their full native consumer.
No new zero-free region follows from the paid terms alone.

## 5. Alternative: retain the stronger unfiltered kernel by counting removed rows

There is a second legal estimate for the SAME small-pair-conductor
sector. It exchanges the two cutoffs differently. For good sixth-free
rows in the original compact physical annulus,

    #{u:rho_lo(u)!=0} <<_epsilon Q0 U^epsilon.          (11)

Indeed every radical ideal r has norm at most 2Q0. There are at most
`5^omega(r)` choices for its prime valuations in {1,...,5}. This is
`O_epsilon((Nr)^epsilon)` by the divisor bound. The fixed compact
shape and unit conventions give only bounded multiplicity per ideal.
Counting EVERY such radical by the fixed-field ideal count proves
(11); imposing the physical norm annulus can only reduce this count.

Write the exact low-radical, both-different covariance expanded in its
original d1,n1,d2,n2 variables. At each fixed pair conductor C its
absolute coefficient mass is (8), and the low-row kernel is at most
(11) by absolute counting. Therefore

    |C_diff,lo,NC<=Q1|
        <<_epsilon Q0 Q1^(1/2) U^epsilon(1+T)^A.        (12)

This step takes the absolute value of an already expanded signed sector;
it does not enlarge a positive square after selecting its conductors.
The principal C=1 term is included. All actual shared primes and both
index inequalities remain under the same coefficient majorant.

Now use the exact identity

    C_diff,hi,NC<=Q1
       =C_diff,all,NC<=Q1-C_diff,lo,NC<=Q1.

The first term has the complete UNFILTERED sixth-free estimate of
`ACTUAL_SIXTHFREE_SECTOR.md`; (12) pays the second term. Inserting this
identity in the original positive row partition and strip centering
gives the distinct complete reduction

    E=C_diff,hi,NC>Q1
       +O_epsilon([U+U Q0/N+U^(1/6)Q1^(11/12)
                         +Q0 Q1^(1/2)]U^epsilon(1+T)^A). (13)

One may choose the better of (10) and (13) for any prescribed cutoffs.
For example, at the synchronized corner

    Q0=U^(51/80),    Q1=U^(9/8),

the four exponents in (13) are respectively

    1, 91/80, 115/96, 6/5.

Thus this choice also pays at most `U^(6/5+epsilon)`, retaining a larger
pair-conductor cutoff in exchange for a smaller row-conductor cutoff.
The complete remaining signed form is still OPEN. Neither alternative
estimates it or proves an improved zeta boundary.

# Actual future-scale probes: native column removal and its cofinal cost

**PROPOSED component results.** Every probe below is an explicit finite
combination of the original B_m, with the actual Gauss phases and all
shared-prime/nonunit terms. No improved zeta boundary is established.
The single-prime and finite-inverse cancellations are exact identities,
not observations about an arbitrary coefficient vector.

## 1. Fix the final S before choosing the primes

Use the CT-admissible field F=Q(zeta_12), the FINAL excluded set S of the
pinned source, and its allowed generators. Call a prime ideal P good if
it has an allowed generator p whose image in every F_v^*/F_v^{*6}, v in S,
is trivial. In the source's finite class group this is [p]=1. A sufficiently
deep fixed principal congruence p=1 mod m implies this condition by Hensel's
lemma. Good primes of arbitrarily large norm exist by the prime theorem
for the trivial ray class; for example [Sutherland, Proposition 28.10]
(https://math.mit.edu/classes/18.785/2021fa/LectureNotes28.pdf).
Only this fixed-field existence statement is imported, not a least-prime
bound, a claim about a particular prime polynomial, or uniformity in S.

Put Q=NP, psi=vartheta^3, kappa=vartheta^6, and

    lambda(P)=gamma_2(P)/vartheta(P).

This is an actual unit Gauss phase. For good P, all finite row-unit and
frequency-unit symbols chi_P(epsilon) are one by the source's unit-symbol
identity. Its reflected c=P coefficient is therefore lambda(P)/sqrt Q
in EVERY unit slice of the clean h=f=1 sector. The c=P and c=1 terms
have the SAME combined profile, because [p]=1. This class condition is
essential; a norm dilation alone would not align general class profiles.

Define the legal future-scale operation

    F_P B_m(Z)=B_m(Z)-lambda(P)/sqrt Q chi_P(m)^3 B_m(QZ). (1)

Only the Gaussian scale inside B changes. The physical outer X,Y and the
row set stay fixed. One must not replace them by the scale-dependent
values associated with QZ when computing a principal response.

## 2. Exact cancellation of a native reflected column

In the exact clean reflected expansion, write a column by the IDEAL

    ell=n c k^3,

where n is the selected future-filter ideal, c is the original squarefree
reflected ideal, and k is the unrestricted reflected cube. The original
profile is Phi(Nell Z/(Nd)^2). For ell=P there are exactly two terms:

    n=1,c=P,k=1:    lambda(P)/sqrt Q chi_d(p)^3 Phi(QZ/(Nd)^2),
    n=P,c=1,k=1:   -lambda(P)/sqrt Q chi_d(p)^3 Phi(QZ/(Nd)^2).

They cancel identically, including when P divides d: then BOTH vanish.
All row phases are common and the profiles agree by section 1. This is
the full ell=P column, since a nontrivial cube cannot divide a prime.

The operation also creates or changes other columns. In particular
n=P,c=P,k=1 gives

    -lambda(P)^2/Q 1_(P does not divide d) Phi(Q^2 Z/(Nd)^2). (2)

It has quadratic core one and is not deleted. For other c the full
coefficient contains the actual cubic Gauss reciprocity interaction.
Formula (1), rather than an omission of those columns, is the definition
of the observable.

For a finite set Pset of good primes, the commuting product of (1) is

    B_m^prime(Z)=sum_(n squarefree, supp n subset Pset)
       mu_F(n) product_(P|n)lambda(P)/(sqrt(Nn))
                            chi_n(m)^3 B_m(Z Nn).       (3)

It cancels every selected prime column. It does not cancel all smooth
squarefree columns. For ell=P R, its coefficient is

    [lambda(P R)-lambda(P)lambda(R)]/sqrt(Q_P Q_R).      (4)

The exact Gauss CRT identity and allowed-generator reciprocity give

    lambda(P R)=lambda(P)lambda(R)chi_P(r)^4.           (5)

Thus (4) is often nonzero. The interactions in (5), not independent random
phases and not ordinary multiplicativity, determine the next cancellation.

## 3. The complete principal multiplier really is zero safe

The local cube deformation in CUBE_TILT.md, with t=Q^(-v), gives

    H_t/H_1=(A-Tt^2/Q)(1-T)/[(1-Tt^2)(A-T/Q)],
    A=1-(1-Q^(-1))Q^(-s), T=kappa(P)Q^(3-6s).          (6)

Its exact original-probe expansion is

    H_t/H_1=1+(t-1) sum_(j>=1)(psi(P)/Q)^j D_j(s)t^(j-1),

where D_j is the principal response of chi_(P^j)(m)^3 B_m(Z/Q^(3j)).
Comparing the power series in t on an initial absolute region gives

    D_1=(Q/psi(P)) T(A-1/Q)/(A-T/Q).                   (7)

This uses the full Poisson shell calculation; no bare Gauss-vector mean
has been substituted. The response of the future probe B_m(QZ) instead
is Q^(4(s-5/6))D_1, because its Gaussian scale is Q^4 times that of the
probe in (7), with physical X,Y fixed. Hence (1)'s principal multiplier is

    1-z_P(s),
    z_P(s)=lambda(P)psi(P)Q^(1/6-2s)
       (1-Q^(-1))(1-Q^(-s))
       /[1-(1-Q^(-1))Q^(-s)-kappa(P)Q^(2-6s)].         (8)

For Re s>1/2 and Q>=13, the denominator is bounded below by
`1-Q^(-1/2)-Q^(-1)>1/2`, while the numerator is bounded above by
`(1+Q^(-1/2))Q^(-5/6)`. Consequently

    |z_P(s)|<=2 Q^(-5/6)<1.                           (9)

For clarity, the factor 2 follows directly from the slightly sharper
denominator retaining `(1-Q^-1)Q^-1/2`: at Q=13 and beyond,
`1+Q^-1/2 <=2[1-(1-Q^-1)Q^-1/2-Q^-1]`.
Thus no finite product of (1) loses a principal target pole in Re s>1/2.
Its extra multiplier is not the same radial functional as the CT scalar
c0, so the same-W0 obstruction does not apply.

The product over ALL good primes Q>=13 converges normally and is nowhere
zero on Re s>7/12, since the general bound is O(Q^(1/6-2Re s)). On any
fixed closed half-plane Re s>=theta>7/12, the complete multiplier and
its inverse have finite absolute Dirichlet-norm bounds after the local
denominators from H_FACTOR.md are expanded. Native H itself is nonzero
for Re s>2/3. Therefore this additional filter retains every ordinary
zeta zero that the original principal detector sees; in particular it
does not lose a hypothetical zero beyond an intermediate target such
as 5/6. It does not cure any pre-existing cancellation by native H below
2/3. The separate v>=1/2 construction remains the fully zero-safe detector.

For an increasing prime universe this identifies the normal limit of the
finite PRINCIPAL components. A uniform bound for the complete nonprincipal
Poisson terms is still a separate requirement. Neither convergence of the
principal Euler factors nor the native moment below silently supplies that
additional contour/remainder comparison.

## 4. The cofinal prime filter keeps the native moment, but saves no power

There is a better bound than the L1 future-operator triangle cost
`product(1+Q^-1/2)`. Collapse the actual coefficients BEFORE applying the
quadratic sieve. In a frozen reflected tuple, n and c in (3) are both
squarefree. Write

    e=gcd(n,c), n=e u, c=e v, ell_0=u v,

with e,u,v pairwise coprime squarefree. Retain the exact row mask
`1_((e,d)=1)`. The quadratic character is chi_d(ell_0)^3 and the profile
depends on `(Ne)^2 Nell_0`, with the unchanged native cube k^3 and frozen
factors. The column coefficient has magnitude at most

    tau(ell_0)/(Ne sqrt(Nell_0)).                     (10)

All actual Gauss phases, n/h common-prime zeros and finite class slices
remain in this coefficient. Every selected n has class one, so the class
of c is determined by ell_0 and e; its original profile slice is retained.
No independent profile is assigned after the sum.

On Nell_0 approximately C its square mass is
`O_epsilon(C^epsilon/(Ne)^2)`. The quadratic sieve gives

    O_epsilon((CD)^epsilon)[D/(Ne)^2+C/(Ne)^2].

The effective C is L/(Ne)^2, where L is the SAME original reflected
length `D^2P/Z`, with its frozen a_f,k,f factors. Minkowski over e costs
only a harmonic ideal sum in the D root and a convergent inverse-square
ideal sum in the L root. Both are paid exactly as the native reflection
argument. Higher native cubes have the original k^(-5/2) dual resource;
the a_f and f sums are unchanged. This proves, uniformly in the selected
finite prime set,

    sum_(m in a P,D native dyad)|B_m^prime(Z)|^2
          <<_epsilon Z^epsilon P^(1/2)[D+D^2P/Z].     (11)

The full tail is also uniform. After collapsing n,c, the coefficient
Dirichlet majorant has only divisor powers; at every fixed exponent
sigma>1/2 it is bounded by a fixed power of zeta_F(sigma+1/2), independent
of the selected prime universe. Apply the source's rapid profile envelope
to `Q0=(Ne)^2 Nell_0 (Nk)^3` beyond its usual common cutoff
`Z^delta D^2P/Z`, then sum that complete positive majorant. Choosing the
profile power after delta and the row-box exponent gives any prescribed
negative-power row-square tail. No filter-index population is dropped.

The same absolute majorant proves convergence at every fixed nonzero m,Z
when the prime universe increases to all good primes. Thus (11) extends
to the actual cofinal all-prime filter by Fatou (or uniform tail plus finite
convergence). Its full native row exponent remains 2M-1 for M>1.

This is a complete arithmetic sector removal with no exponent penalty.
It is NOT a saving in that exponent. Semiprime interactions (4), all
higher cores, every shared-prime column (2), and powerful-row sectors
remain. Killing only the prime columns cannot be substituted for a
stronger signed estimate for this remaining vector.

## 5. Exact finite inverse for every smooth squarefree column

For a fixed good prime set indexed by 1,...,k put

    b(S)=product_({i,j} subset S) eta_ij,
    eta_ij=chi_(P_i)(p_j)^4 in mu_3.

The actual Gauss coefficient is
`lambda(product_(i in S)P_i)=product lambda(P_i) b(S)`.
There is a unique squarefree incidence inverse x(empty)=1,

    sum_(T subset S) x(T)b(S\T)=1_(S empty).           (12)

Use coefficient `x(S)product lambda(P_i)/sqrt(NP_S)` and future scale
`Z NP_S` in place of the coefficients in (3). Then EVERY nonempty
squarefree ell supported on these primes cancels in the complete clean
reflected sector, with no finite-profile mismatch and no omission of
other products. The principal multiplier is exactly

    M_x(s)=sum_(S subset {1,...,k}) x(S)product_(i in S) z_(P_i)(s).

If `sum_(S nonempty)|x(S)|product 2Q_i^(-5/6)<1`, (9) proves it is nonzero
throughout Re s>1/2. This is quantitative separation of the actual
principal response from the canceled native columns.

The inverse has the exact partition formula

    x(S)=sum_(partitions pi of S) (-1)^|pi| |pi|!
                               product_(B in pi)b(B). (13)

Its universal bound is `|x(S)|<=|S|! 2^(|S|-1)` for nonempty S: ordered
partitions are counted by ordering elements and then choosing cut points;
this overcounts and therefore supplies the displayed bound. Consequently
any fixed k can have arbitrarily small raw and principal perturbation
resources by choosing sufficiently large good primes. This gives genuine
finite arithmetic cancellation without target loss for every final S.

It does not yet give the cofinal inverse norm. In contrast to (3), the
coefficients x(S) in (13) are not bounded by one or by a fixed divisor
power uniformly in |S|. All shared-prime columns remain; for ell=P_S^2
the unique n=c=P_S,k_native=1 term is

    x(S) b(S) product_(i in S)lambda(P_i)^2/(NP_S)
                        1_((P_S,d)=1) Phi((NP_S)^2Z/(Nd)^2). (14)

This exact surviving diagonal is one reason that squarefree-column
cancellation alone does not imply a cheaper complete moment.

The actual new analytic task is to control the complete inverse vector,
including (14), uniformly for a growing prime set. A bound based solely
on (13)'s absolute factorial bound does not supply an improving power.

## 6. Actual finite F12 interaction check and its precise legality boundary

`prime_probe_check.py` uses twelve principal prime ideals generated by
`1+216k zeta_12`. Their prime norms are exactly `t^4-t^2+1`, t=216k,
authenticated by FLINT primality at norms below 2^64. The residue embedding
is zeta_12=-1/t mod p. It checks all 132 actual ordered sextic residues
and their reciprocity; no Gauss phase is replaced by a random variable.
Individual unit Gauss phases factor by the proved identity (5).

The exact mu_3 algebra inverse verifies all 4096 equations (12).
The naive prime-product filter leaves 37 of the 66 semiprime columns
nonzero. The true finite inverse has coordinate L1 as large as 211243751,
yet its complete finite raw root resource is below 1.00001, the dual root
resource below 1.000000001, and its principal perturbation below 10^-6.
The large prime norms, not a cofinal cancellation theorem, pay that cost.

These displayed generators are sixth powers at every place over 2,3:
v(alpha-1)>=6>2v(6)=4, so strong Hensel applies. At complex places roots
exist automatically. They authenticate the arithmetic minimal-S graph.
The final imported CT S may contain ADDITIONAL exceptional places. The
script does NOT certify sixth-power class one at those unknown places.
For final-source use choose the general good primes of section 1, or
replace 216 by a modulus deep at EVERY final S place and certify the
chosen generators. No infinitude of prime values of t^4-t^2+1 is assumed.
The general cancellation theorem is legal for the final S independently
of whether these particular numerical generators meet that larger modulus.

# Four different convergence domains of one coherent arithmetic source

Use the actual S3 times C2 cover and coherent algebra from
[the quadratic place-Euler theorem](COHERENT_QUADRATIC_PLACE_EULER.md).
The field has cardinality Q and characteristic greater than three.
Let U be the base with all six geometric branch points removed: the
four old finite branch points, zero, and infinity. Let E_chi be the
full place-Euler source and let G_chi be its good-place part over U.
The finite bad-place product is denoted B_chi, so E_chi=B_chi G_chi
as germs near zero. This is a decomposition of the specified source,
not a choice of correction designed after observing its zeros.

There are four exact centered domains:

| Operation | Exact radius | Meaning |
| --- | --- | --- |
| Absolute local-factor convergence | Q^(-1) | Sum_v abs(F_v(z^deg(v))-1) is finite. Finite zero factors are allowed in this tail criterion. |
| Good-place logarithms grouped by closed degree | Q^(-1/2) | A normally convergent sum of finite degree blocks, using the local logarithm at zero. The finite bad factors remain outside this logarithm. |
| Taylor series of the full E_chi | Q^(-1/4) | Its first poles are exactly those of P_E(z^2), with the noncancellation proved in the preceding source theorem. |
| Meromorphic continuation of the full source germ | 1 | It is single valued inside the unit disk and has a meromorphic natural boundary there. |

The last two statements are imported from the preceding exact theorem;
the first two are proved below, including their sharpness. This table
does not enlarge the ordinary exponential Lie operator's trace-class
disk abs(z)<1/2. That is a different operator condition, not one of the
four source-series radii.

## 1. The absolute Euler threshold is exact

For a good source class (h,epsilon) the factor is F_h(epsilon t), with

    F_e(t)=(1+2t)/(1-t)^4,
    F_s(t)=(1-t^2)^(-2), F_c(t)=(1-t^3)^(-1).

There are at most Q^d/d good closed places of degree d. The finitely
many local series have F_h(epsilon t)=1+O(t) uniformly near zero.
Thus the factor-difference series converges for abs(z)<1/Q. This is
the usual absolute Euler convergence criterion even when a finite bad
factor happens to vanish: the criterion is about the tail, and does
not assert that the final product is nonzero.

Conversely, the actual geometrically connected joint cover has

    pi_split(d)=Q^d/(12d)+O(Q^(d/2))

completely split good places of every sufficiently large degree. At
each of those places the factor is F_e(z^d), and

    F_e(w)-1=6w+O(w^2).

For all sufficiently small complex w this gives
abs(F_e(w)-1)>=3 abs(w), uniformly in its argument. Fix z with
1/Q<=abs(z)<1. For all sufficiently large d, the contribution of
the split degree-d places to the absolute criterion is therefore at
least a positive constant times

    (Q abs(z))^d/d.

Its sum diverges, including the harmonic endpoint Q abs(z)=1.
This proves the exact threshold throughout the meromorphic unit disk.
It does not claim that every ordering of a conditionally convergent
product has the same value.

## 2. A source-defined degree grouping of the good logarithms

For abs(w)<1/2 let ell_(h,epsilon)(w) be the holomorphic logarithm of
F_h(epsilon w) with value zero at w=0. No local good factor has a zero
or pole in that disk. Define the finite degree block

    D_d(z)=sum_(v in U, deg(v)=d) ell_(h_v,epsilon_v)(z^d).

This grouping is specified by closed-point degree. It is not an
arbitrary rearrangement of individual Euler factors. Its linear term
is A_d z^d, where

    A_d=sum_(v in U, deg(v)=d) tr(Fr_v | M_1 tensor chi).

The actual first Lie source M_1 is the regular S3 representation, and
M_1 tensor chi is the six-dimensional anti-regular joint source. The
proper H^1 has rank twelve, with Weil weight one; H^0 and H^2 vanish.
At each of the four old geometric finite branch points its invariant
stalk has dimension three. The new zero and infinity stalks vanish.
The localization sequence consequently gives

    dim H_c^1(U,M_1 tensor chi)=12+12=24,
    H_c^0=H_c^2=0.

The extra twelve boundary eigenvalues have modulus one, while the
proper twelve have modulus sqrt(Q). Hence the genuine compact trace
sum S_m over U(F_(Q^m)) satisfies

    abs(S_m)<=12 Q^(m/2)+12.                            (2.1)

Every closed point of degree e dividing m contributes its full
Frobenius power, not just its first trace:

    S_m=sum_(e|m) e sum_(deg(v)=e)
                    tr(Fr_v^(m/e) | M_1 tensor chi).

All such traces have absolute value at most six. Removing the proper
degree contributions therefore bounds

    abs(A_m)
      <= [12 Q^(m/2)+12+6 sum_(1<=e<=floor(m/2)) Q^e]/m
      <= 32 Q^(m/2)/m.                                 (2.2)

For the last inequality use Q>=5 and
sum_(e<=m/2)Q^e<=Q^(m/2)Q/(Q-1). The intentionally loose constant32
also covers m=1. No inference from small-field patterns replaces this
all-degree trace argument.

For abs(w)<=r<1/2, the explicit three local logarithms give

    abs(ell_(h,epsilon)(w)-tr(M_1 tensor chi)(h,epsilon) w)
       <= C(r) abs(w)^2,
    C(r)=2/(1-2r)+2/(1-r).                             (2.3)

Indeed the identity coefficients in degree k>=2 have absolute value
at most (2^k+4)/k, and summing their bounds with 1/k<=1/2 gives
(2.3). The transposition and cycle series have smaller bounds. The
quadratic sign does not change these absolute estimates.

Combining (2.2)--(2.3), for r<Q^(-1/2),

    abs(D_d(z))
      <= 32 (sqrt(Q)r)^d/d + C(r)(Qr^2)^d/d
      for abs(z)<=r.                                   (2.4)

The sum of this bound converges. Thus sum_d D_d(z) converges normally
on abs(z)<Q^(-1/2) to a holomorphic function L_U(z). On the smaller
absolute-Euler disk it is the original good Euler logarithm; hence

    G_chi(z)=exp(L_U(z))

throughout this larger disk. In particular this good-place product
has no zeros there. The full product B_chi(z) G_chi(z) can have zeros
there because of its finitely many bad factors.

The explicit certified tail after degree N is

    32 (sqrt(Q)r)^(N+1)/[(N+1)(1-sqrt(Q)r)]
      + C(r)(Qr^2)^(N+1)/[(N+1)(1-Qr^2)].              (2.5)

This estimates complete degree blocks, not individual absolute Euler
factors. Replacing the square root by any proved rational upper bound
preserves a rational certificate.

## 3. Why the good-log radius stops at the Weil circle

Use finite Koszul extraction through grade two. Apart from compact
boundary determinants with zeros and poles only on abs(z)=1, the
two proper finite factors are

    P_-(z) (1-z^2)(1-Qz^2)/P_E(z^2),                  (3.1)

where P_- has degree twelve and all reciprocal roots have modulus
sqrt(Q). The good-place residual starts in local degree three, so
its product converges normally on abs(z)<Q^(-1/3). This is strictly
beyond Q^(-1/2), but still before the elliptic denominator circle
Q^(-1/4).

At abs(z)=Q^(-1/2), every good local numerator is nonzero: its only
possible zero has local argument +1/2 or -1/2, whereas
abs(z^d)<=Q^(-1/2)<1/2. The finite extraction denominator is nonzero
inside the unit disk. The large-degree tail is normally convergent
and nonzero after the usual finite separation; all separated factors
are also nonzero at the point in question. No bad-place factor is
being included in this good-product assertion.

Consequently the first zeros of the continued good product are exactly
the zeros of

    P_-(z)(1-Qz^2),                                   (3.2)

on the Weil circle, with their full algebraic multiplicities. There
are fourteen counting multiplicity; overlap or repeated eigenvalues
is allowed. There are no zeros in the smaller disk by Section2.

If L_U extended holomorphically to a centered disk of larger radius,
its exponential would be a nonzero continuation of G_chi through
these zeros, a contradiction. In particular the displayed sum of
good degree-log blocks cannot converge normally on a larger centered
disk. This is an exact centered-domain statement. It does not assert
that the degree series diverges at every individual exterior point,
nor that no conditional product limit exists at a selected boundary
point.

## 4. Finite bad factors must not be hidden inside that logarithm

The new zero place gives a concrete warning. When its old S3 Frobenius
is identity, its full even source is

    (1+14s+9s^2)/(1-s)^4, s=z^2.

The smaller numerator root is negative with absolute value strictly
between1/16 and1/9: the polynomial 1-14x+9x^2 is positive at x=1/16
and negative at x=1/9. Thus this factor has zeros with abs(z) between
1/4 and1/3. This is an exact invariant-source factor calculation.
Whenever this old Frobenius class occurs and the resulting root lies
inside the good-log disk, it gives a zero of the full source there,
because G_chi is nonzero there. No assertion that every parameter has
this particular bad zero is needed or made.

This formal source control introduces no new parameter or field count.
It explains why the good-place logarithm and the full Taylor function
must be kept distinct. The finite bad numerator does not create a Taylor
singularity there; the full source remains holomorphic until its
first actual elliptic poles at Q^(-1/4).

## 5. Exact small-field provenance and the scope of the replay

The first two primitive extension histograms determine the rational
and degree-two old branch places with their actual quadratic signs.
If all four old branch points form one degree-four orbit, its sign
is also determined without constructing F_(Q^4). The branch equation is

    -27u^4+54B u^2-(4A^3+27B^2)=0.

The norm of a root in that orbit is (4A^3+27B^2)/27. For every nonzero
element a of F_(Q^f),

    chi_(Q^f)(a)=chi_Q(Norm_(Q^f/Q)(a)),

by the elementary finite-field exponent formula. Thus its quadratic
sign can be computed in the base field. At an old branch point the
anti-regular invariant space has dimension three, with scalar
Frobenius chi_v. The complete compact first-grade polynomial is

    L_U(M_1 tensor chi,z)
       =P_-(z) product_(old branch v) (1-chi_v z^deg(v))^3.             (5.1)

Its degree is24, consistent with the exact localization sequence.
The replay checks (5.1), the first two actual compact trace sums,
the Frobenius-square correction in A_2, and rational versions of
the bound (2.5). It also checks the exact identity-class even source
and the small bad-root enclosure above. Every new primitive
field has order at most49.

The source weights, split places in all sufficiently large degrees,
normal-convergence proof and sharp centered log obstruction remain
theorems, not conclusions from sampling the bounded controls. The
companion arithmetic-divisor note, when included in this packet,
addresses the exact interior cohomological orders separately from
these convergence-order distinctions.

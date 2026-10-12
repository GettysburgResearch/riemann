# Independent moment-norm and sextic absorption audit

Date: 2026-10-10. Read-only checkout/Git. Scoped PASS for the complete
moment-norm lemma and conditional sextic auxiliary-base mechanism.
No new native slab, parameter-family certificate or RH result is
established. The exploratory K=6905 probe is not independently bound
by this proof audit.

Final proof files reviewed:

- MOMENT_NORM_TRANSPORT.md SHA256
  9279440530af0efc1f4c19b3dd9aca608ec9a5d6afde278687dc098b010967c4.
- SEXTIC_ABSORPTION.md SHA256
  9d6a56bf4ea5553419d710ce96848122316886d0abbf4e8b490f46aca8d1f5e5.

The initial files were 5eaaa458... and 11f396b9.... This review requested
two elementary clarifications, which the owner applied: R>0/A>=0 in
the general norm lemma, and P_R(0)=1 as the normalized finite product
in the sextic note. Without the positive-cutoff premise the argument
bound in MN3 would not follow from its stated MN2 alone. The normalized
P_R convention now explicitly differs from C1's product that includes
Xi(0), avoiding a stray Xi(0) factor. Actual R=8192 and the intended
native construction were already in the corrected scope.

## Complete norm transport

For rho=gamma+i*eta with gamma>R>0 and |eta|<=A, its argument lies
in the claimed interval. Under 2k*atan(A/R)<pi/2, the real projection
of rho^(-2k) is at least c_k*|rho|^(-2k). The product's inverse-square
summability implies absolute convergence for every k>=1, so complete
conjugate grouping and multiplicity-preserving summation are valid.
The t_k are real and strictly positive for a nonempty tail; all unknown
nonreal blocks remain included. Thus S_2k<=t_k/c_k is correct.

The higher-norm inequality follows termwise from |rho|>R and loses
no coefficient class or zero supply. All three exact rational c_k
forms are correct. The sufficient R>2kA guard is valid, including A=0.
An upper interval endpoint for the actual t_k gives a safe complete
absolute norm budget. Merely selected candidate roots cannot provide it.

MN7 has the correct factor -k: the complete paired logarithmic series
coefficient of z^(2k) is -(1/k)sum m*rho^(-2k). Subtracting the complete
simple real census removes exactly its contribution once per opposite
pair; nonreal conjugate representatives are both retained in the tail.
The source coefficient and complete census remain declared dependencies.
No ordinary floating-point or unreviewed jet is promoted into a bound.

## Two positive fake pairs and exact three-moment cancellation

The strict interval t2^3/(2t3^2)<K<t2^3/t3^2 is exactly necessary and
sufficient for the unique unordered distinct positive u,v with the two
power-sum equations. With p=u+v, uv=(p^2-s2)/2 is positive and the
discriminant 2s2-p^2 is positive on the stated open interval. The cubic
sum has derivative (3/2)(s2-p^2)<0 there, with the two claimed endpoint
values. The Gaussian guard a1>sqrt(2K*t2) ensures a=a1-Kp>0.
K is a fixed positive integer; feasibility is an extra source hypothesis,
not a consequence of positive moments or a numerical fit.

The radius bounds and V4<=t2^2/K are correct and include the entire K
multiplicity for both pairs. The normalized P_R convention makes G(0)=Xi(0).
On B<R with B^2*max(u,v)<1, Xi/G is an analytic nonzero multiplier:
the common census factors cancel even at their actual real zeros,
the complete tail has no zero in the disk, and all artificial factors
are nonzero there. Its unique log with value zero at zero cancels the
z^2,z^4,z^6 coefficients exactly. No higher tail moment is discarded.

## Full residual derivative budgets

The complete derivative identity SA9 is correct: the actual residual
is -2*z^7*sum m/[rho^6*(rho^2-z^2)], and both fake residuals have the
opposite sign and the full u^4/v^4 numerators. Every actual contribution
is charged to S8, every fake contribution to V4. The actual denominator
bound uses 1-d with d=B^2/R^2; the fake one uses 1-w. The proposed
U8=t3_upper/(c3*R^2) follows directly from the complete norm lemma.

Differentiating each summand gives the envelope
7/(1-x)+2x/(1-x)^2=(7-5x)/(1-x)^2. Its derivative
(9-5x)/(1-x)^3 is positive on [0,1), so the shared d/w bounds in J2
are valid. Both J1 and J2 are full-disk bounds, not bounds at isolated
points. The identity q''/q=h''+(h')^2 gives the final J1^2+J2 bound.
Using whole interval upper bounds for V4 and w is safe only while the
same strict w<1 guard remains protected, as the note requires.

## Artificial multiplicities and the protected companion

The real-rooted Gaussian-polynomial approximants apply in the open
lower half-plane even though the two fake roots have multiplicity K.
Their complete companion polynomial has no lower zeros. The positive
imaginary-axis Gaussian/product power-series anchors prevent an
identically zero limit and give strict harmonic sector positivity.
This argument does not misuse the order-below-two positive Fourier
source theorem for an order-two Gaussian base.

Multiple fake roots can make the companions vanish on the real line
at those roots. SA6 correctly excludes them from the entire protected
disk. Within its real interval, each census zero is simple. Away from
zeros of G, write
G'/G=-2a*x+sum_alpha multiplicity(alpha)/(x-alpha).
Its derivative is -2a-sum_alpha multiplicity(alpha)/(x-alpha)^2<0.
Thus any zero of G' there is simple, G and G' never share a zero there,
and G' and G'' never share a zero there. Both companions are nonzero
on the protected real boundary. The strict real Laguerre numerator is
G^2*(2a+sum multiplicity/(x-alpha)^2)>0 off census zeros, and G'^2>0
at their simple zeros. This supplies the boundary step despite the
multiple artificial zeros outside the domain.

Consequently a compact joint source-bound parameter family satisfying
all strict guards has positive companion/derivative margins by
continuity. This statement gives existence, not effective margins.
A real finite checker must still cover that entire family, all target
boxes and the stated multiplier predicate. With tau=a0/M, the protected
bounds imply tau<=1, and SA11 gives |n|<1, |d|<1 and the exact quotient
error less than tau. It is the reviewed C14-C17 transport criterion,
not a new all-lambda/all-domain inference from one parameter point.

## Independent controls and limits

/tmp/review_moment_sextic_oracle.py independently checks ten exact
symbolic identities, twelve complete higher-norm inequalities for a
finite source containing a nonreal conjugate pair with multiplicities,
and three distinct positive fake-pair configurations. Normal/-O
outputs are byte-identical at
/tmp/review-moment-sextic-{normal,optimized}.json. No K=6905 source
primitive, larger domain or complete family certificate is replayed.

No remaining mathematical gap found at the final hashes. The two
lemmas are valid tools for a subsequent source-bound directed family
certificate. They do not themselves improve any accepted finite
column or claim a cofinal/RH result.

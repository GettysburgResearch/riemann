# The complete arithmetic inverse: shared squares, signed prime cost, and spin

**PROPOSED.** This is an audit and a collection of exact partial results.
It proves no improvement in the ordinary zeta zero-free boundary. The
notation and final-S good-prime convention are those of FUTURE_PROBES.md.

## 1. A shared-square column survives every squarefree incidence inverse

Write lambda_P=gamma_2(P)/vartheta(P), Q_P=NP and
eta_PQ=chi_P(q)^4=chi_Q(p)^4 in mu_3 for distinct good primes.
The clean reflected coefficient at a squarefree c is lambda(c)/sqrt(Nc).
The squarefree incidence inverse has x(P)=-1 and x(PQ)=2-eta_PQ.

At the column ell=P^2 Q, native cube index one, exactly two terms occur:
the future-filter index n=P with c=PQ, and n=PQ with c=P. Their sum is

    2 lambda_P^2 lambda_Q (1-eta_PQ)/(Q_P sqrt(Q_Q))
       1_(P does not divide d) chi_d(Q)^3
       Phi(Q_P^2 Q_Q Z/(Nd)^2).                         (1)

Indeed their scalar multipliers are respectively -eta_PQ and 2-eta_PQ.
The quadratic phases both reduce to chi_d(Q)^3 and both vanish when P|d.
Good-prime class one makes the complete profile and its unit/cusp labels
identical. No later good prime can change this column, since its filter
index would have to divide ell. Thus (1) survives the cofinal squarefree
incidence inverse. It is not legitimate to retain only squarefree ell.

For fixed P, a nontrivial eta_PQ has positive Dirichlet density among good
Q. To see this, use the cubic Kummer extension F(p^(1/3))/F. It ramifies
at P because v_P(p)=1. Its intersection with the fixed S-ray field is F:
the degree-three extension has no proper intermediate field, and the
S-ray field is unramified at P. Chebotarev therefore gives each cubic
Frobenius class with positive density even subject to the fixed good-ray
condition. On a nontrivial class |1-eta|^2=3. Consequently the sum of
the squares of the scalar coefficients in (1) diverges, since it equals
12/Q_P^2 times a positive-density prime harmonic sum.

This is a statement about this actual complete column resource. It is
NOT a lower bound for the whole row moment: correlations with other
columns and other square parts may cancel it. In particular it does not
justify taking absolute values before those correlations are examined.

## 2. The full inverse must contain prime squares

An inverse that cancels every nonempty column, instead of only squarefree
columns, must have the future-filter coefficient

    a(P^2)=lambda_P^2/Q_P.                              (2)

This follows directly from the ell=P^2 column: the native squarefree
c coefficient vanishes, the n=P,c=P term is -lambda_P^2/Q_P, and the
n=P^2,c=1 term is the only remaining contribution. The row character
of (2) is the nontrivial mask 1_(P does not divide m); it must be kept.

The exact principal response of (2), relative to the original principal
term, is

    lambda_P^2 Q_P^(2s-8/3)
        (1-Q_P^-1)(1-Q_P^-s)
        /[1-(1-Q_P^-1)Q_P^-s-kappa(P)Q_P^(2-6s)].       (3)

It is obtained by the same local cube-resolvent computation as equation
(7) of FUTURE_PROBES.md, now at future dilation Q_P^2 and quadratic
character chi_(P^2)^3. For Re s>1/2 the denominator is nonzero. On each
closed substrip of Re s>1/2 its ratio after the leading power equals
1+O(Q_P^-min(Re s,6 Re s-2,1)).

Thus the leading prime series has absolute exponent 8/3-2 Re s.
The absolute prime budget diverges at and above Re s=5/6. This is only
an ABSOLUTE-budget obstruction. The lambda_P^2 phases are arithmetic,
and must not be discarded when evaluating the actual signed budget.

If, for the specified final ray class and field, one proves

    sum_(NP<=X) lambda_P^2 = O(X^(theta+epsilon)),       (4)

then Abel summation makes the leading part of (3) converge locally
uniformly wherever Re s<(8/3-theta)/2. The rational corrections in (3)
are absolutely summable near the working boundary Re s approximately
0.875; this follows because their extra exponent exceeds 1/12 there.
This conditional signed statement concerns one repeated-prime diagonal.
It does not bound the full inverse, its cross-prime partition coefficients,
its complete reflected moment, or its physical Poisson error.

## 3. What the Eisenstein angular first moment would pay

On E=Q(omega), the exact Gauss correction identities give

    lambda_P^2=-Lambda(P)^3 G(P)^2 conjugate(gamma_2(P)).

Here Lambda has nonzero angular infinity type, and G is the fixed finite
correction. The pinned OpenAI fixed-angular prime theorem supplies
exponent theta=5/6 for this type of nonzero angular Gauss sum, in its
stated coefficient class. IF the required final fixed-ray restriction
and finite twist are supplied by a legal extension of that theorem,
the threshold in (4) is Re s<11/12. This would pay the signed p^2
series (3) near 0.875, despite its divergent absolute mass.

The conditional qualification is essential. The native CT interface used
in this packet requires mu_12 in F and is not an interface over E.
Neither a fixed-ray extension nor a base-change extension is inferred
merely from the published untwisted angular theorem.

## 4. The F12 base-change factor is a cubic spin

Let F=E(i), tau the nontrivial element of Gal(F/E). Let an exterior
degree-one prime q=(pi) of E split as P tau(P). Choose alpha generating P,
and put pi=alpha tau(alpha), after recording any fixed primary unit.
At these degree-one local fields the standard trace additive characters
of F and E agree. Their Gauss denominators are alpha and pi. The finite
Gauss scaling identity therefore gives exactly

    gamma_(2,F)(P)=chi_P(tau(alpha))^-2 gamma_(2,E)(q), (5)

provided the displayed generators and additive characters are used.
If either convention is changed, the corresponding explicit unit or
fixed local additive scaling must be inserted; (5) is not a license to
erase that factor. Its cube is consistent with the source's norm pullback
Lambda_F(P)=Lambda_E(q).

Writing alpha=r+is, r,s in E, gives tau(alpha)=2r modulo P. Thus the
cubic factor in (5) is the cubic residuacity of the variable relative
trace 2r. It need not be a fixed finite ray character. For good P and
tau(P), cubic reciprocity and tau fixing mu_3 give the SAME spin factor
at both primes, so summing the conjugate pair does not remove it.

This is the same relative-trace spin phenomenon studied by Merikoski,
arXiv:2012.05675v2, equation (1.2). His precise spin is [s/r]_3, for a
primary alpha=r+is, and equation (1.2) identifies it with [r/pi]_3^2.
Fixed factors at 2 and primary units must still be matched before
identifying it literally with the phase in (5). His Theorem 1 proves
the UNWEIGHTED spin prime sum O(X^(1-1/143)). That theorem alone does not
bound the product of spin with an Eisenstein cubic Gauss coefficient.
Moreover 1-1/143 is larger than the exponent 8/3-2 Re s required by
(4) near Re s=0.875, even before the joint coefficient issue is addressed.

The exact missing import is therefore a JOINT spin-times-angular-Gauss
prime estimate in the final fixed ray classes, not just equidistribution
of spin, and not just the Eisenstein angular Gauss first moment. This
records an actual arithmetic obstacle to a casual field specialization;
it does not assert that the joint estimate is false.

## 5. Why random phase intuition is insufficient for the inverse

For a squarefree selected prime set S the exact inverse is

    x(S)=sum_(partitions pi of S) (-1)^|pi| |pi|!
                           product_(B in pi) product_(i<j in B) eta_ij.

As a diagnostic only, take independent uniform eta_ij in mu_3. Distinct
set partitions have distinct internal-edge incidence sets. Orthogonality
then gives the EXACT model identity

    E |x(S)|^2 = sum_(r=1)^|S| Stirling2(|S|,r) (r!)^2. (6)

Thus even random independent local phases do not imply uniformly small
inverse coefficients; inversion sums many partitions coherently. This
probabilistic identity is not a theorem that arithmetic phase graphs are
random, and is not a norm lower bound in the ideal-norm aspect. An actual
cofinal inverse bound must combine the partition sum with the arithmetic
distribution of its prime norms and shared-prime phases.

## Sources read and the remaining target

The algebra in sections 1--2 uses the pinned CT/OpenAI local identities
listed in NOTES.md and FUTURE_PROBES.md. Section 3 uses only the stated
scope of the pinned OpenAI fixed-angular appendix. The primary classical
spin source is [Merikoski, arXiv:2012.05675v2](https://arxiv.org/pdf/2012.05675v2),
Theorem 1 and equation (1.2), read directly. No spin estimate is assumed
for the joint coefficient (5).

A full improving result still requires a bound for the complete signed
inverse vector or an alternative physical marked detector. Paying one
prime-square series does not pay that vector. Conversely, divergence of
its absolute resource does not refute a signed correlated approach.

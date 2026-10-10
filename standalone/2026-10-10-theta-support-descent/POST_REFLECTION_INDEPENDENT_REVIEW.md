# Independent review of the post-reflection Euler continuation

Review date: 10 October 2026.

Reviewer: moment_arithmetic. The reviewer did not author
POST_REFLECTION_EULER_CONTINUATION.md. The reviewer authored its
earlier divisor-conditioning dependency, which is subject to a
separate independent review by joint_series_review; this report
does not purport to independently review that earlier dependency.

Reviewed object:
[POST_REFLECTION_EULER_CONTINUATION.md](POST_REFLECTION_EULER_CONTINUATION.md).

Reviewed SHA256:
7ddcaf96aba2f109fb5696880ed9098e435712e2075613e72474b76fc00a3072.

Primary source: the October 5 paper2.tex imported from OpenAI/math
commit adc7f1241b42e322a6451854ab7e4b4c146bf78a. Relevant interfaces
were checked in the actual local source, especially its Gauss–Jacobi
identities, normalized CRT, reduced cusp denominators,
eq:ray-local-transform, eq:ray-multiplier, eq:ray-additive-crt,
eq:theta-mellin-functional-equation, and dual cusp Mellin series.

**Verdict: PASS at the explicitly stated source-conditional scope.**
The complete standard-face object has the claimed meromorphic
continuation and, with the specified finite-order zero-free input,
the stated pole-controlled refinement and polynomial vertical bound.
The possible residue is specified by a normally convergent formula;
its nonvanishing and its identification with a moment diagonal are
not proved or claimed.

## 1. The phase cancellation was independently reconstructed

The exact source definitions are
sigma_p=lambda squared times c/p and
epsilon_p=minus lambda to the -5 times (c/p) to the -2.
At a prime of k, the exponent-3 local scalar has exponents -2 on
chi_p(-1), 21 on chi_p(lambda), and 8 on chi_p(c/p).
The identity chi_p(-1) squared equals one removes the exponent -2;
the other two exponents reduce modulo six to 3 and 2. This verifies
the final precision sentence after (2.4) and gives its first line.
The source identities

\[
\gamma_1(p)\gamma_2(p)
 =-\alpha(p)\chi_p(4)^{-1}\gamma_3(p),\qquad
\gamma_1(p)\gamma_5(p)=\chi_p(-1)
\]

then give its second line with the sign shown in the reviewed file.
Normalized squarefree CRT gives exactly its row scalar
Gamma_(c0)(k), including mu(k) and alpha(k).

At the primes of d, normalized CRT combines the local gamma_4(p)
and the ordered d–d cross-symbols to
gamma_4(d) chi_d(lambda squared times c0 k) to the -2.
The k–d factors are chi_k(d) squared and chi_d(k) to the -2;
cubic reciprocity cancels them. The remaining alpha(d) squared
from the plus derivative cancels the outer alpha(d) to the -2.
The source identity gamma_2(d) gamma_4(d)=1 cancels the remaining
Gauss coefficient. Thus the d coefficient after reflection is
finite order, exactly as in (2.12).

The supplemental simplification using vartheta is also correct:
vartheta(d) chi_d(lambda squared times c0) to the -2 equals
chi_d(c0) to the -2 on the retained good ideals. The remaining
residue-class restriction still has to be expanded. Equations
(3.1)–(3.3) do so explicitly with a fixed finite group; no angular
factor is assigned to that group.

The retained dual row factor is the sextic character
chi_k(lambda to the fourth times ell), since B_(p,3) has exponent
-5, congruent to +1 modulo six. It is not silently reused as a
quadratic character.

## 2. Mellin normalization and exact reflected object

For the plus derivative, the primal Mellin factor is the negative
of the positive scalar in the source's minus-derivative formula.
The coordinate functional equation contributes another minus sign.
The dual minus-derivative Mellin series contributes i divided by
4 times (2 pi) to the power 2-2s. Combining these three facts gives
the positive i in H(s), with exactly 27 to the -s and
(2 pi) to the 4s-2. The gamma ratio in (3.3) therefore has the
correct sign, arguments, and scale.

The d norm exponent was checked independently:

\[
-(w+s-1)+(1-2s)-\tfrac12
 =-v,\qquad v=w+3s-\tfrac32.
\]

All k and d primes are active, so c=c0kd has precisely the norm
factor used. The finite cusp labels, additive phases and normalizing
units vary through fixed finite sets after the stated residue split.
Thus (3.5) is the actual source reflection of the conditioned object,
initially in Re(s)<0, Re(v)>1. The earlier normally convergent
divisor representation supplies a nonempty overlap, so this is a
continuation of the same function.

## 3. Euler product and infinite cusp summation

For a good prime, let D=1-x+z and u=zeta(p)q to the -v. The two
local signed factors are 1-u/D and 1+(q-1)u/D. Dividing each by
1-u gives exactly (4.2), and subtraction of one in the first case
gives u(-x+z)/(D(1-u)). The error exponents are therefore w+v
and 2v, with their actual signs.

In the claimed domain Re(v)>1/2 and
Re(s)<min(0,Re(v)-1), one has Re(w)>2. The quantitative bound
|x|+|z|<2 to the -2 plus 2 to the -1/2 is less than one.
It prevents division through a zero of D. The factors 1-u are
nonzero as well. The normally convergent remainder is consequently
holomorphic, including its finitely many ell-prime factors.
Their norm bound preserves all repeated prime factors and all k
exclusions.

The theta support and coefficient bound yield an absolutely
convergent three-cusp majorant for Dirichlet exponent greater than
one. Applying the ell-prime bound therefore gives the sufficient
condition

\[
1-\Re(s)-\max(0,1-\Re(v))>1.
\]

This is exactly the claimed domain. Its strict margin absorbs the
small divisor-count loss and justifies normal convergence, the
uniform row bound, and holomorphic dependence in both variables.
No limiting claim is inferred from finite examples.

The finite reciprocals are placed outside those normally convergent
cusp sums. Ordinary meromorphic continuation then gives precisely
the possible polar divisors stated in Theorem 1.1. The moving Euler
factors at k cannot vanish in this domain; they remain in every
displayed L-function.

## 4. Vertical bounds, residue, and limits of the theorem

The fixed-character zero-free refinement is sufficient for the
logarithm argument in Section 4.1. In the principal case
(v-1)L(v)/(v+1) is holomorphic and nonzero on the relevant half-plane,
including its removable value at one. The disk-centered Euler
bound, upper bound for the real part of the logarithm, and
Borel–Caratheodory give a polynomial reciprocal bound. The family
is finite. Its moving k Euler factors cost only Q to an arbitrarily
small positive power, uniformly in the vertical variables.
The remainder and cusp-series majorants are also uniform in those
variables. Stirling gives the stated polynomial growth of H(s).
This verifies (4.15), including the factor v-1 when needed.

For Re(s)<0, a neighborhood of v=1 lies strictly inside the cusp
summability domain. Taking the limit through (4.12) is therefore
legal and gives (5.2). A principal reflected character has analytic
reciprocal value zero at one. Nonprincipal components can cancel
each other. The reviewed file correctly makes no nonvanishing claim.
The special local simplification when zeta equals kappa was also
checked: the full good-prime factors are 1-x and 1-x+qz.

The conductor factor Q to the 1-2Re(s) cancels the corresponding
Mellin scalar power. On the new side Re(v)<=1, the remaining
balanced scale exponent satisfies Re(v)-2Re(s)>2-Re(v)>=1.
This supplies continuation across the old boundary without a
moment saving. The full generalized moment, a favorable averaged
row estimate, and a diagonal identification remain outside this
theorem.

What was actually done: complete reading of the reviewed file;
direct comparison with the named primary-source formulas; independent
reconstruction of its good-prime scalar, CRT and Mellin identities;
checking all convergence inequalities, pole locations, zero masks,
and vertical-growth dependencies; and exact SHA256 identification
after the author's minor notation corrections. No theta-automorphy
proof replay, zero computation, or numerical experiment was used.

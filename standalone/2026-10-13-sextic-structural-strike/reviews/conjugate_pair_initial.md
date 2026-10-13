# Independent mathematical review of the conjugate-pair conductor argument

## 1. Frozen object, scope and verdict

**Reviewed manuscript:** `pass3_bilinear_attack.md`, 21,258 bytes, SHA-256

`0dd707c8181160a8347cafd9b1cadec962755001981ce32a9e0da2a09563d0e6`.

**Reviewer:** extraction/resonance agent. I did not develop or write this
bilinear argument. I did independently develop the short-polynomial
non-smallness and finite-Euler resonance arguments in the same research
session; neither argument is used in this manuscript's proof. This is a
fresh reconstruction by another agent using the same underlying model,
not a certification of the external large-sieve theorem.

**Verdict:** no load-bearing mathematical gap found in Theorems 3.1, 4.1
or 5.1 under the fixed standard-family assumptions and the source's
compact smooth row test. The order-six conclusion is a source-qualified
deduction from de Faveri's stated general-order sieve and structural
lemmas. The proof correctly restricts its conclusion to the conjugate
pair of conductor exponents and to positive native tuple accounting.
It does not prove the full generalized moment.

Two short clarifications would make the proof easier to audit, without
changing an exponent or requiring a new analytic input:

1. After Mellin separation in Section 3, explicitly apply
   Cauchy--Schwarz to the two coefficient vectors before referring to a
   nonnegative square. A complex Mellin parameter need not preserve a
   literal square at the preceding stage. The primary proof makes this
   Cauchy step, and it gives exactly the claimed bound.
2. In Section 4, take the background character to mean its primitive
   associate before writing its zero extension on the good index. The
   theorem is naturally stated in terms of its intrinsic conductor;
   an arbitrarily enlarged imprimitive modulus must not add coefficient
   zeros that the primitive product does not have.

For standalone clarity, also state explicitly that the fixed radial
majorant in Section 5 is the compact smooth majorant of the cited native
source. Mere smoothness and domination of a ball, without decay, would
not define the asserted row sum.

## 2. Exact source checks

I directly opened the primary text, rather than relying only on the new
manuscript's account:

- Alexandre de Faveri, [*Optimal large sieve for fixed order characters*,
  arXiv:2610.04045v1](https://arxiv.org/html/2610.04045v1), Theorem 1.1,
  Section 2.5, Lemmas 2.4, 3.1 and 3.3, and the full Poisson reduction in
  Proposition 8.1.
- PR #929, commit `97bf40329489992e9384c34d7595af6d01a40774`,
  `standalone/2026-10-10-conductor-averages/CUBIC_CONDUCTOR_AVERAGE.md`,
  especially the uniform AFE construction and the unit correction in
  Sections 2--4; also `EXPLORATION_SINGLETON_SIEVE.md` for the displayed
  old one-sign comparison.

The crucial primary facts have the necessary quantifiers. Theorem 1.1
is for every fixed order at least three. Lemma 2.4 supplies the exact
good conductor of a coprime pair in the same refined ray class. Lemma
3.1 applies to its nontrivial primitive character. In Lemma 3.3 the
mixed root-number factors involve each column's part beyond its
squarefree kernel. They equal one for squarefree columns. The remaining
scalar is fixed after the indicated ray partition. Proposition 8.1
uses this squarefree simplification before introducing the cubic
all-row estimate.

These are imported inputs, not foundations re-proved in this review.
The rest of the review reconstructs their composition in the proposed
generalization.

## 3. The all-row reduction is valid

Write an arbitrary good ideal uniquely as

\[
x=e^n x_0,
\]

where every prime exponent of \(x_0\) is less than \(n\). No
coprimality between \(e\) and \(x_0\) is needed or generally true.
For squarefree column \(q\), the value of \(\chi_q(e^n)\) is precisely
\(\mathbf 1_{(e,q)=1}\). Thus each fixed \(e\) only deletes entries of
the column vector. It does not increase its squared norm.

The four terms of the fixed-order sieve at row length
\(U/(Ne)^n\) sum to

\[
U\sum_e(Ne)^{-n},\quad O(U^{1/n}V),\quad
U^{1-1/n}V^{2/n}\sum_e(Ne)^{-(n-1)},\quad
U^{2/n}V^{1-1/n}\sum_e(Ne)^{-2}.
\]

All three infinite sums converge for \(n\geq3\); the second term uses
ordinary ideal counting. The arbitrarily small powers from the sieve
and the finite reciprocity partition fit in the final epsilon. This
establishes (2.1) with the literal nonunit mask, including ideals with
overlapping \(e\) and \(x_0\).

## 4. Independent reconstruction of the Poisson step

Assume \(A\leq B\), using conjugation for the other ordering. Partition
the column ideals by a fixed refined ray class and write an opened pair
as

\[
q_1=d h_1,\qquad q_2=d h_2.
\]

Because the original columns are squarefree, these three ideals are
pairwise coprime and squarefree. Both \(h_i\) lie in the same ray class.
The common column contributes exactly
\(\mathbf 1_{(a,d)=1}\mathbf 1_{(b,d)=1}\). It must not be suppressed
inside the signed opened expression.

Away from the bounded \(Nh_i\asymp1\) ranges, the residual pair is
nontrivial and primitive of conductor \(h_1h_2\). The bounded ranges
give \(AB\|\lambda\|_2^2\) with a divisor loss: the relevant \(d\)'s
are of scale \(Q\), and each original column is counted by only a
bounded number of residual short ideals and a divisor number of masks.

Removing \((b,\mathfrak c d)=1\) by a divisor \(r\), Poisson on the
conjugate character has prefactor

\[
\frac{B}{Nr\sqrt{N(h_1h_2)}}
\]

and dual ideal length \(N(h_1h_2)Nr/B\). Both quantities are independent
of the residue order. The source root-number formula has no mixed
factor here: \(h_i^\sharp=1\), while
\([h_i^\star]=[h_i]\) is already fixed. Its remaining factors are one
bounded coefficient attached to \(h_1\), its conjugate attached to
\(h_2\), and a fixed class scalar.

Write the dual ideal as \(s e\), where \(s\) has only bad-prime factors
and \(e\) is good. The good character on the reflected ideal has the
same orientation as the surviving character on \(a\). It is therefore
\(\chi_h(ae)\), including a zero when \(h\) meets either factor.
Nothing in this identity uses \(n=3\).

Here is a precise completion of the manuscript's abbreviated
Mellin-to-square step. After fixing a Mellin parameter, the factor
\(N(h_1h_2)^{-1/2+z}\) can produce two different column vectors.
Apply Cauchy--Schwarz to the product of their sums over \(a,e\).
Both vectors have the same modulus, up to the common real Mellin
power already charged to the epsilon. Apply the same all-row operator
bound to each resulting square. Thus this step has exactly the cost
of one all-row bound, with no extra power of a length.

Remove \((h_1,h_2)=1\) by its exact divisor \(g\), writing \(h_i=g f_i\).
The new coefficients keep \((f_i,g)=1\), the ray conditions and all
prior column masks. They are independent of \(a,e\). The common
\(g\)-factor is a row mask and may be dropped after the Cauchy step.
The factorization count for \(u=ae\) is at most an ideal divisor
function.

One can see directly why the \(g\)-sum is harmless. In either energy
sum its weight has the form

\[
\sum_g\sum_{f\sim Q/N(dg)}
\frac{|\lambda'_{gf}|^2}{N(rfg)}.
\]

Writing \(h=gf\), the number of representations is bounded by
\(\tau(h)\), while the denominator is \(Nr\,Nh\). The shorter column
length \(Q/N(dg)\) is at most \(Q/Nd\). The subsequent \(d\)-sum is
another divisor count of the original column. The \(r\)-sum is over
divisors of \(\mathfrak c d\), and the truncated \(s\)-sum has only
fixed prime generators. Their collective cost is an arbitrarily small
power.

For \(Nd\asymp\Delta\) and \(Nr\asymp P\), this gives exactly

\[
\frac{B\Delta}{QP}\,
\mathcal C_n\left(\frac{AQ^2P}{B\Delta^2},\frac Q\Delta\right)
\]

up to the final epsilon and \(\|\lambda\|_2^2\). The dual cutoff has
the manuscript's extra factor \(1/Ns\), which can be discarded for
this upper bound. Empty dual ranges contribute nothing. Fixed support
constants and the small power in the cutoff can be kept until the end;
they do not require turning an empty range into a new row contribution.

With \(U=AQ^2P/(B\Delta^2)\), \(V=Q/\Delta\), a monomial
\(U^xV^y\) becomes

\[
A^xB^{1-x}Q^{2x+y-1}\Delta^{1-2x-y}P^{x-1}.
\]

Substitution of the four all-row terms gives (3.10) exactly. Every
\(\Delta,P\) exponent is nonpositive for \(n\geq3\). The term
\(AQ\) is absorbed by \(A^{1-1/n}B^{1/n}Q\) since \(A\leq B\).
This establishes Theorem 3.1. At \(n=3\), the third and fourth terms
coincide; at \(n=6\) they are distinct. The extra sixth-order term
has not been silently deleted.

## 5. Moving background, primitive values and the AFE

Interpret \(\psi\) as its primitive associate. Since its good
conductor \(\mathfrak r\) is disjoint from squarefree \(ab\), each
good prime of \(\mathfrak r ab\) carries a nontrivial local
component of the product. Consequently the good conductor is exactly
\(\mathfrak r ab\). Possible cancellation at the fixed bad primes
changes only their fixed finite conductor data. It does not justify
replacing their primitive values by an imprimitive product.

The common AFE length is therefore
\((RAB)^{1/2+\eta}(2+|t|)^{C_\eta}\). On a Mellin line with real part
\(\eta>0\), the dependence of the conductor weight on \(a,b\) is a
bounded real factor times a unit-modulus phase outside that row's
Dirichlet polynomial. The gamma factor is fixed because the infinity
type and the field are fixed. Direct and dual pieces are separated
before averaging, so no uniform average of the moving root number is
asserted. The conjugate coefficient family in the dual piece has the
same bound after conjugation and exchange of the outer labels.

For the index factorization \(m=s q r_0^2\), the equality is unique
without requiring \((q,r_0)=1\). Weighted Cauchy uses the convergent
sum

\[
\sum_{s\mid S^\infty}\sum_{r_0\in I(S)}
(N(s r_0^2))^{-1/2-\eta}.
\]

The \(s,r_0\) character multiplier can depend on \(a,b\), but it is
independent of \(q\) and has modulus at most one. After the square
is formed it can be bounded by one. At \(S\), this multiplier is
the actual primitive product value. On good \(q\), the remaining
coefficient is the fixed background value times the displayed norm
weight. Its moving conductor exclusion is already a zero in that
coefficient. Its squared norm on a dyad is bounded uniformly in the
background character.

After fixing the reciprocity classes of \(a,b,q\), the remaining
kernel is precisely the conjugate-pair kernel of Section 3. Any class
scalar depending on \(a,b\) lies outside its own square; the scalar
depending on the \(q\)-class is part of that class's coefficient vector.
Dropping squarefreeness, coprimality or background exclusions from the
outer sum occurs only after it is nonnegative.

The four substitutions at \(Q=(RAB)^{1/2}\), divided by \(AB\), give
the four ratios in (4.1). I also checked the general formula (4.6).
Its last ratio is at most \(R^{1/2}\): use
\(N_0^{-1/(2n)}\leq M^{-1/(2n)}\) to bound its size by
\(R^{3/(2n)}M^{3/n-1}\), and both exponents are suitable for
\(n\geq3\). The other ratios have the same required bound. This
verifies that no background dependence is hidden in a source constant.

## 6. Native unit correction and the tuple count

The fixed ray partition is essential. The raw singleton element
character need not be trivial on the six units, so it cannot by itself
be treated as an ideal Hecke character. In the complete radial sum,
the tuple's total character is first averaged over the unit group.
Nontrivial unit characters vanish exactly.

For a surviving tuple, fix all nonsingleton conductors and their
residual exponents, then fix the two singleton ray classes. The
standard character \(\chi_{a_+a_-^5}\) has exactly the singleton good
local components of the tuple. Their discrepancy is a character at
the fixed bad modulus, determined by those ray classes. Dividing the
total ideal character by the standard singleton character thus leaves
a background whose good conductor is exactly

\[
g_2\prod_{m\geq3}g_m.
\]

It is independent of the varying singleton ideals within those
classes. Class number one excludes an additional unramified ambiguity.
This is the same quotient argument as the cubic source adapter; no
step depends on using the double-prime rather than the singleton
exponents. The final product uses its primitive extension at the bad
primes, as required in Section 4.

The Mellin expression for a nonprincipal complete radial tuple kernel
then has no crossed pole. Its principal-prime mask produces the exact
finite Euler product; taking absolute values costs at most
\((Nq_0)^\eta\). This operation does not discard a character zero in
the underlying identity.

The physical norm budget bounds \(Nq_0\) by

\[
D^kL^{-1/2}G^{-1}\prod_{m\geq3}(Ng_m)^{-m/2}
\]

up to fixed support constants. Ideal counting and prime-position
assignments give (5.6) with a divisor loss. One must freeze the
background residual exponents before using the family mean; the
manuscript does this. Cauchy in the singleton pair contributes
\(L\) times the square root of each second-mean ratio. The sum over
\(g_2\asymp G\) cancels its counting denominator, while every higher
multiplicity sum converges with exponent at least \(5/4\).
The decay of the Mellin transform absorbs the AFE's vertical
polynomial. This proves (5.2), including arbitrary bounded original
column phases and arbitrary tuple selectors.

The allowance of tuple selectors does not allow an arbitrary subset
of the row sum: the complete smooth radial kernel is needed for both
unit averaging and the Mellin identity. The manuscript preserves that
distinction.

## 7. Exponent and scope checks

I independently recalculated the generic monomial substitution above
and the numerical fixture, also running a separate short calculation
with exact rational arithmetic. I did not treat the author's finite
checker as proof of the analytic steps.

The four new excesses in the feasible fixture are

\[
-1/20,\quad -1/20,\quad -1/24,\quad -23/480.
\]

The old one-sign profile gives
\(-1/20,-1/10,1/480,-11/480\). The stated classical and balanced
comparison excesses are \(3/20\) and \(23/60\). Direct substitution
in the old anisotropic cubic profile gives the three numbers in
(6.7); the Wu comparison uses the older profile explicitly displayed
in the cited source. Each original column in (6.1) has exponent one,
and \(Nq_0\) has exponent \(41/40\), consistent with the physical
budget. The claimed new positive region is a real enlargement over
those particular comparison branches.

Clearing denominators in the four inequalities obtained by requiring
each term of (5.2) to be at most \(HD^{k+\epsilon}\) gives (5.7)
exactly. The powers of \(G,M,N_0\) in its fourth inequality are all
needed.

Finally, the manuscript correctly leaves the leading long-singleton
core open. At \(X=Y=D^k\) and \(G=1\), the first accounting term is
\(H^{1/2}D^{2k+\epsilon}\). Improving the displayed absolute
conductor mean to its ideal size does not remove that term from this
counting argument. This is an obstruction to this chain of upper
bounds, not a lower bound on the signed native core. No RH or full
moment consequence is established by this review.

## 8. Review disposition

The frozen manuscript passes this scoped mathematical reconstruction,
with the short clarifications listed in Section 1. Any subsequent
edit needs a new hash binding; this verdict does not automatically
apply to a later document or to extra corollaries not present at the
reviewed hash. The general-order external sieve remains an explicit
import. Publication should retain that qualification and the
long-singleton limitation.

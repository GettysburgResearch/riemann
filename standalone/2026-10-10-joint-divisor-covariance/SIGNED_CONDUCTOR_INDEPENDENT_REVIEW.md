# Independent review of the signed conductor progress

**Reviewer:** /root/moving_auxiliary_attack.

**Reviewed object:** the complete SIGNED_CONDUCTOR_PROGRESS.md,
22,968 bytes, SHA-256
d973468a0e0a893f43327e6f3a4ac706076952ec44a2a3114423ea515bdc4e4a.

**Verdict:** pass at its stated source-qualified scope. The paper proves
additional bounds for complete smooth character kernels and for actual
signed moment sectors by positive accounting of those kernels. The
unit projection, sixfold element-to-ideal normalization, moving
principal-mask adapter, conductor-divisor choice, all-order incidence
count, controlled domains, feasible scale fixtures, and exact residual
replacement are valid. The full remaining signed covariance and the
generalized moment hypothesis remain unproved.

I did not author or edit the reviewed proof. The new conductor argument
does not use my mixed theta adapter. This is an independent review of
the written deductions, not a reconstruction of the published
subconvexity proofs, external peer review, or a proof-assistant
certificate.

## 1. External theorem interfaces checked directly

I opened [Han Wu's primary manuscript, arXiv:1604.08551v6](https://arxiv.org/html/1604.08551v6).
Theorem 1.1 has exactly the analytic-conductor exponent used here.
The convention in Section 1.3 makes Hecke characters unitary. The
formula immediately preceding Theorem 1.1 states the Söhne estimate
with an arbitrary ideal divisor of the finite conductor. Thus the
reviewed WU and SO inputs match their expressly identified source.

I also opened the [published Blomer–Brumley paper](https://annals.math.princeton.edu/wp-content/uploads/annals-v174-n1-p18-p.pdf).
Its Definition 1 quantifies over every number field and every place;
Theorem 1 gives the stated \(7/64\) value for \(n=2\). It therefore
supplies the admissible parameter for Wu's theorem here.

The original Söhne proof was not inspected. The reviewed paper
explicitly uses the formula quoted by Wu and discloses that source
boundary. I approve that accurately described interface, not an
unperformed verification of the 1997 proof.

For the internal comparison and residual identities I read PR #914's
CONDUCTOR_SECTORS.md, Sections 3–8, at
0cc0428fedbbfc340044c7451b3d392c1da9a103, and PR #919's
SMALL_GCD_CONDUCTOR_REDUCTION.md at
9b04a887e171b3104a66cf57296ce5b0b2920d78, especially its signed
inequality, lower bound, cutoff, and averaged extraction statement.
The new incidence count is also proved in the reviewed note, so the
new bound does not depend merely on a descriptive citation.

## 2. The exact character and unit projection

The residual conductor is

\[
f=\prod_{p:\ r_p-s_p\not\equiv0\ (6)}p.
\]

At each such good prime, a nonzero power modulo six is a nontrivial
character of the prime residue field. It remains primitive at that
prime even when its order falls from six to three or two. The
complementary radical \(q_0\) consists of the residual-zero primes,
whose original nonunit zeros are retained as the separate mask.
Thus reviewed (1.3) is valid at nonunits as well as on units.

In particular the analytic conductor in the new estimates is
\(Nf=\prod_m Ng_m\). It is not the older incidence complexity
\(Ng_1\sqrt{Ng_2}\). The latter is only a summary of the counting
cost. The proof keeps these quantities distinct.

The complete row test is radial. Multiplication by any Eisenstein
unit preserves its norm and every principal mask. If the residual
character is nontrivial on this six-element group, its whole smooth
row sum is zero. Otherwise it is constant on the generators of each
nonzero ideal. Since this field is a PID and each nonzero ideal has
exactly six generators, the surviving element sum is exactly six
times the ideal sum. There is no replacement by a primary-row or
squarefree-row average.

The resulting ideal character has trivial infinity type. Its
primitivity is preserved: if it descended to a proper finite
conductor, its values on generators prime to \(f\) would make the
original residue character descend as well. Nonprincipality follows
by choosing a nonzero residue where the primitive character is
nontrivial and representing it by an element prime to \(f\).
The zero row contributes zero when \(f\ne1\).

## 3. Mellin inversion, masks, and the two row estimates

Smooth radiality gives \(\Phi(z)=\phi(|z|^2)\) with
\(\phi\in C_c^\infty([0,\infty))\). A nonzero value at zero causes
no difficulty on the line used in the proof. Its Mellin transform is
holomorphic for positive real part. Repeated integration by parts
gives arbitrary polynomial decay on vertical strips bounded away
from zero. No Mellin pole is crossed in moving the contour from a
fixed line right of one to real part \(1/2\).

Before any estimate, the moving principal mask is the exact Euler
polynomial

\[
\prod_{p\mid q_0}(1-\widetilde\psi(p)(Np)^{-s}).
\]

On the new line, its absolute value is bounded by
\(\prod_{p\mid q_0}(1+(Np)^{-1/2})\), which is subpower in \(Nq_0\)
uniformly over squarefree \(q_0\). Only finitely many small primes
need a fixed constant; the logarithm of every sufficiently large
factor is at most a chosen positive multiple of \(\log Np\).

The primitive nonprincipal Hecke \(L\)-function is entire, and the
contour uses \(L\), not its reciprocal. Its zeros require no
zero-free premise. The norm twist by \(it\) has analytic conductor
comparable, for this fixed imaginary quadratic field and trivial
infinity type, to \(Nf(2+|t|)^2\). The rapid Mellin decay integrates
the polynomial vertical factors in both external estimates.
This proves the displayed \(H^{1/2}\) row bounds uniformly in the
conductor and principal mask.

I independently computed

\[
\frac14-\frac{1-2(7/64)}{16}=\frac{103}{512}.
\]

For the divisor-sensitive bound, the chosen divisor really divides
the actual conductor. With \(P=\max_{p\mid f}Np\), a first-crossing
product of conductor primes gives

\[
F^{1/3}P^{-2/3}\le Nd\le F^{1/3}P^{1/3}.
\]

If the lower endpoint is at most one, the unit divisor works.
Otherwise the final prime multiplies the previous product by at
most \(P\). Both non-leading terms of SO are consequently at most
\((FP)^{1/6}\), as is its \(F^{1/6}\) term. The argument does not
assert a balanced divisor for every conductor. When a divisor
comparable to \(F^{1/3}\) is separately stipulated, the stronger
\(F^{1/6}\) bound follows with its fixed comparison constant.

## 4. All-order incidence counting and selected domains

Every prime of \(q_0\) appears in at least two tuple positions.
For fixed nonprincipal multiplicity ideals \(g_m\), the complete
support condition therefore gives

\[
Nq_0\le (BD)^k\prod_m(Ng_m)^{-m/2}.
\]

There are at most a constant times this upper cutoff possible
principal-mask ideals when it is at least one; if it is smaller,
there are no tuples. At fixed total radical, assigning each prime
to its incidence pattern costs at most
\((2^{2k}-1)^{\omega(q)}\), a subpower on the actual polynomial
support for every fixed order \(k\).

Multiplying by the WU row estimate leaves the powers
\((Ng_m)^{103/512-m/2}\). Summing \(g_1,g_2\) in their indicated
dyadic blocks gives exactly

\[
L^{359/512}G^{103/512}.
\]

All sums for \(m\ge3\) converge absolutely; the first denominator
exponent is \(3/2-103/512=665/512>1\). Replacing \(103/512\) by
\(1/6\) gives \(L^{2/3}G^{1/6}\) and again strictly convergent
higher-multiplicity sums. The largest-prime branch has the one
additional factor \(Y^{1/6}\). Every discarded restriction is
discarded only in these nonnegative counting bounds.

The classical branches apply to the same positive accounting
quantity, so taking the minimum is legitimate. An additional tuple
selector can be imposed before these bounds; this does not allow
a selector inside the complete row character sum itself.

Squaring the WU block inequality yields the diagonal-size condition

\[
(Ng_1)^{359/256}(Ng_2)^{103/256}\le H.
\]

Raising the prime-factor inequality to its sixth power gives
\(Y(Ng_1)^4Ng_2\le H^3\). Dyadic partition of the actual largest
prime makes the replacement by \(P(f)\) valid with only a fixed
factor and one additional logarithmic count. The balanced-divisor
subfamily similarly gives \((Ng_1)^4Ng_2\le H^3\).

The numbers of nonempty dyadic blocks are logarithmic in \(D\)
at fixed \(k\), because every conductor prime divides a tuple of
bounded column norm. Taking the literal union of controlled regions,
and counting overlaps once, therefore gives a total
\(O(HD^{k+\epsilon})\) bound. The no-singleton and principal portions
remain covered by the old counting result. There is no all-order
uniform-constant claim hidden in these fixed-order sums.

## 5. The two fourth-moment fixtures

I checked the incidence pattern directly. In

\[
(cea_1,\;cf_0a_2;\;deb_1,\;df_0b_2),
\]

the same-side double product is \(cd\), the singleton product is
\(a_1a_2b_1b_2\), and the principal mask is \(ef_0\). The side
gcds are exactly \(c,d\); matched cross gcds are \(e,f_0\), and
the unmatched cross gcds are units. All these statements use the
stipulated pairwise coprimality of the eight labels.

The independent rational checks are:

| Quantity | Fixture 5.1 | Fixture 5.2 |
|---|---:|---:|
| Row exponent \(h\) | \(101/100\) | \(21/20\) |
| Singleton exponent | \(5/16\) | \(2/5\) |
| Double exponent | \(7/5\) | \(7/5\) |
| Side gcd exponent | \(7/10\) | \(7/10\) |
| Small-gcd cutoff exponent | \(499/700\) | \(99/140\) |
| Old completion excess over \(HD^2\) | \(1/400\) | \(1/20\) |
| General WU excess | \(-869/204800\) | \(19/512\) |
| Largest-prime branch excess with exponent \(1/10\) | not imposed | \(-1/120\) |
| Balanced-divisor branch excess | not imposed | \(-1/40\) |

Each original column has total norm exponent one. Both side gcds
are strictly below their small-gcd cutoffs. The positive matched
cross-separation exponents are respectively \(249/320\) and \(4/5\),
so these configurations are outside subpower cross-gcd sectors.
Both old branches fail to yield a diagonal-size bound for the
specified collections, while the claimed new branches do yield it.

The second fixture's factorization is feasible: fourteen distinct
residual primes occur in \(c,d\), and four more occur as singleton
labels, all at exponent \(1/10\). If all eighteen lie in a fixed
relative interval, six form a divisor comparable to \(F^{1/3}\),
with a fixed comparison constant. The claim is one of scale
feasibility and an upper bound on a complete incidence collection;
neither the proof nor this review asserts a lower bound on the
character kernel or on the actual signed contribution. Unit
projection can only reduce these upper bounds.

## 6. The exact signed residual replacement

The new selected union is invariant under interchange of the two
Hermitian sides. Its signed contribution is real, and its absolute
value is controlled by the new positive accounting bounds even
after the two old side-gcd restrictions are retained.

Write \(U=V+E\), where \(U\) is precisely the pinned old remainder
and \(E\) is the newly controlled signed portion. Since
\(|E|\ll HD^{2+\epsilon}\), substitution in both old inequalities

\[
M_4\le K HD^{2+\epsilon}+2U,\qquad
U\ge-K HD^{2+\epsilon}
\]

gives reviewed (6.3) after enlarging the constant. The lower bound
for \(V\) follows from the same absolute estimate on \(E\). No
monotonicity of a signed sum under restriction is assumed.

The conditional averaged criterion remains an additional
unproved hypothesis. Integrating the controlled difference is
harmless, and the stated boundary
\(1/2+5h/24+e/4\) is the existing PR #919 extraction with that
replacement. The new component bound does not prove its premise.
The higher-order statement likewise constructs an exact smaller
signed complement; it does not infer cancellation on that complement.

## 7. Correction history, validation, and remaining boundary

The initial review identified one overbroad sentence in Section 7:
failure to reach diagonal size at \(H=D^{1+\theta}\) needs the
intended near-critical range. The author repaired it before this
review hash, explicitly taking \(0<\theta\le1/10\) and \(k\ge1\).
The actual top-scale singleton calculation then does fail to reach
diagonal size for every stated \(k\). For comparison, its displayed
WU bound would allow diagonal size only once \(h\ge359k/128\);
the balanced-divisor bound would require \(h\ge8k/3\). These are far
outside the repaired range.

I independently ran exact rational checks of the subconvex exponent,
higher-incidence convergence, both original-column balances, the two
gcd cutoff comparisons, both old excesses, and all three new fixture
gains. The reviewed proof passed a scan for unintended control
characters. Those checks do not replay primitive character sums or
certify the external analytic theorems.

The smallest new mathematical dependency is the uniform application
of WU, and of the expressly quoted SO formula for its additional
branch, to the unit-invariant primitive residual Hecke characters.
The proof establishes that adapter with the correct conductor and
every principal mask. The remaining missing assertion is still
the signed averaged bound for the new far-separated remainder,
or a stronger estimate implying it. The file makes no unsupported
zero-free or generalized moment conclusion.

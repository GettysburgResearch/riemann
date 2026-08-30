# Universal coefficient-power Euler obstruction and trace-coordinate repair

Status: proposed local algebraic theorem packet for issue #764; not an
integrated or independently reviewed result.

Scope: finite-dimensional complex algebraic representations of
\(\mathrm{GL}_n\), finite virtual differences, and nonnegative integer
coefficient powers. No global prime-indexed family is built.

Exact sources: the stable notes pinned at commit
02e53055b6bdff73fa136ff28cced239d1627f80 in
universal_coefficient_power_euler_obstruction.sources.json.

What is replayed: exact identity coefficients, finite-difference
numerators, independently counted multiset descents, positive
second-coefficient defects, balanced tensor weights, and bounded formal
exponential/determinant coefficients. The universal statements are proved
below, not inferred from the finite rectangle.

Smallest remaining review burden: the identity specialization and the
stable-sort bijection in Section 4. Neither uses an unproved analytic or
global hypothesis.

## 1. The question and its quantifiers

Let \(V=\mathbb C^n\), \(n\geq1\), with the standard action of
\(\mathrm{GL}_n(\mathbb C)\). Define

\[
 \det(I-AT)^{-1}
 =\sum_{r\geq0}h_r(A)T^r,\qquad
 h_r(A)=\operatorname{Tr}(\operatorname{Sym}^r A).
 \tag{1.1}
\]

For an integer \(k\geq0\), the coefficientwise power is

\[
 F_{n,k}(A,T)=\sum_{r\geq0}h_r(A)^kT^r.
 \tag{1.2}
\]

At \(k=0\) this means the polynomial operation \(x^0=1\), including at
\(x=0\), not a limiting convention for a complex logarithm.

A finite virtual representation is a fixed class
\(R=[R_+]-[R_-]\), with \(R_\pm\) finite-dimensional algebraic
representations of \(\mathrm{GL}_n\). Its Euler factor is

\[
 L_R(A,T)
 =\frac{\det(I-T\rho_-(A))}{\det(I-T\rho_+(A))}.
 \tag{1.3}
\]

The class may depend on \(n,k\), but not on the particular matrix \(A\).
The question is whether some such class satisfies
\(F_{n,k}(A,T)=L_R(A,T)\) for every \(A\), or on a Zariski-dense
generic set. Any finite representation-ring construction applied
universally to the standard representation has an output of this form.

The authenticated NONINTEGRAL_LOCAL_POWER_RATIONALITY.md, Section 3,
already warns that integer Hadamard powers usually have a nontrivial
numerator, even when their denominator has symmetric-power weights.
The present claim is stronger: no alternative finite virtual
representation repairs that universal Euler-factor identification.
It does not deny the genuine matrix-coefficient parent of
TRANSFER_MATRIX_SYMMETRIC_PARENT.md. Section 5 gives a constructive
alternative using power traces instead of complete symmetric coefficients.

## 2. Identity and pole-order obstruction

### Theorem GLO764.UNIVERSAL_VIRTUAL_REPRESENTATION_POWER_OBSTRUCTION

Fix integers \(n\geq2\), \(k\geq2\). No finite virtual algebraic
representation \(R\) of \(\mathrm{GL}_n(\mathbb C)\) satisfies

\[
 F_{n,k}(A,T)=L_R(A,T)
 \tag{2.1}
\]

as formal series for every \(A\), or for a Zariski-dense set of \(A\)'s.
In fact, (2.1) cannot hold even at \(A=I_n\).

### Proof

Every representation sends the identity to the identity. If
\(D=\dim R_+-\dim R_-\in\mathbb Z\), then

\[
 L_R(I_n,T)=(1-T)^{-D}.
 \tag{2.2}
\]

On the other hand,

\[
 h_r(I_n)=\binom{n+r-1}{n-1},\qquad
 F_{n,k}(I_n,T)=
 \sum_{r\geq0}\binom{n+r-1}{n-1}^{k}T^r.
 \tag{2.3}
\]

Comparing coefficients of \(T\) forces

\[
 D=n^k>0.
 \tag{2.4}
\]

The coefficient in (2.3) is a polynomial in \(r\) of exact degree
\(e=k(n-1)\) and leading coefficient \(((n-1)!)^{-k}\).
For any polynomial \(p(r)\) of exact degree \(e\) with leading
coefficient \(c\neq0\), its series has an exact pole of order \(e+1\)
at \(T=1\). Indeed expand \(p\) in the basis \(\binom rj\); its top
coefficient is \(ce!\), and

\[
 \sum_{r\geq0}\binom rjT^r
 =\frac{T^j}{(1-T)^{j+1}}.
 \tag{2.5}
\]

Thus (2.3) has exact pole order

\[
 d=k(n-1)+1.
 \tag{2.6}
\]

But the positive binomial terms of degrees at least two give

\[
 n^k=(1+(n-1))^k>1+k(n-1)=d
 \qquad(n,k\geq2),
 \tag{2.7}
\]

contradicting (2.2), (2.4), and (2.6).

For the generic version, every formal coefficient of (1.2) and (1.3)
is a regular function on \(\mathrm{GL}_n\). Determinant inverses are
regular on this group as well. Coefficientwise equality on a
Zariski-dense set therefore extends to the identity. \(\square\)

Negative virtual multiplicities are allowed in this proof. At the
identity the numerator and denominator only cancel powers of \(1-T\);
the resulting expression is still (2.2).

## 3. A positive obstruction in the second coefficient

### Theorem GLO764.IDENTITY_SECOND_COEFFICIENT_OBSTRUCTION

For \(n,k\geq2\), put \(a=\binom{n+1}{2}\), \(b=\binom n2\).
After matching the first coefficient, the second coefficient forced by
(2.2) exceeds the target by

\[
 \boxed{
 \Delta_{n,k}
 =\binom{n^k+1}{2}-\binom{n+1}{2}^{k}
 =\sum_{\substack{2\leq j\leq k\\j\ {\rm even}}}
   \binom kj a^{k-j}b^j
 >0.}
 \tag{3.1}
\]

### Proof

Since \(a+b=n^2\), \(a-b=n\), the even binomial terms sum to

\[
 \sum_{\substack{0\leq j\leq k\\j\ {\rm even}}}
 \binom kj a^{k-j}b^j
 =\frac{(a+b)^k+(a-b)^k}{2}
 =\frac{n^{2k}+n^k}{2}
 =\binom{n^k+1}{2}.
 \tag{3.2}
\]

Remove the \(j=0\) term \(a^k=h_2(I_n)^k\). The \(j=2\) term
remaining in (3.1) is strictly positive. \(\square\)

The smallest example is \(n=k=2\):

\[
 F_{2,2}(I_2,T)=1+4T+9T^2+\cdots,\qquad
 (1-T)^{-4}=1+4T+10T^2+\cdots.
 \tag{3.3}
\]

This two-coefficient contradiction alone proves the no-go theorem.

The natural representation with first character
\((\operatorname{Tr}A)^k\) is \(V^{\otimes k}\). Regrouping its squared
tensor power identifies the total flip with the tensor product of the
factor flips, so

\[
 \operatorname{Sym}^2(V^{\otimes k})
 \cong
 \bigoplus_{\substack{S\subseteq\{1,\ldots,k\}\\|S|\ {\rm even}}}
 \left(\bigotimes_{j\in S}\Lambda^2 V\right)
 \otimes
 \left(\bigotimes_{j\notin S}\operatorname{Sym}^2 V\right).
 \tag{3.4}
\]

Indeed \(V\otimes V=\operatorname{Sym}^2V\oplus\Lambda^2V\) is the
split into the \(+1,-1\) flip eigenspaces, and a total plus sign requires
an even number of minus signs. The target coefficient \(h_2(A)^k\)
is the character of the empty-\(S\) summand only. Dimensions of the
omitted summands give (3.1). This explanation does not assume that every
virtual candidate is the tensor power: the identity proof already
excludes all candidates.

## 4. The identity numerator counts multiset descents

Put \(a=n-1\), \(e=ka\), \(d=e+1\).
Let \(\mathcal W_{a,k}\) be the words on the ordered alphabet
\(\{1,\ldots,k\}\) with exactly \(a\) copies of each letter. An empty
alphabet or zero multiplicity gives one empty word. Define

\[
 \operatorname{des}(w)=
 |\{i:1\leq i<e,\ w_i>w_{i+1}\}|.
 \tag{4.1}
\]

### Theorem GLO764.IDENTITY_POWER_SEGRE_EULERIAN_NUMERATOR

For all integers \(n\geq1,\ k\geq0\),

\[
 \boxed{
 F_{n,k}(I_n,T)
 =\frac{H_{n,k}(T)}{(1-T)^{k(n-1)+1}},\qquad
 H_{n,k}(T)
 =\sum_{w\in\mathcal W_{n-1,k}}T^{\operatorname{des}(w)}.}
 \tag{4.2}
\]

The numerator has nonnegative integer coefficients, with

\[
 H_{n,k}(0)=1,\qquad
 H_{n,k}(1)=\frac{(k(n-1))!}{((n-1)!)^k}>0,\qquad
 [T]H_{n,k}=n^k-k(n-1)-1.
 \tag{4.3}
\]

For \(n\geq2,k\geq1\),

\[
 \deg H_{n,k}=(k-1)(n-1).
 \tag{4.4}
\]

For \(n=1\) or \(k=0\), \(H_{n,k}=1\).
For \(k\geq1\), (4.2) is also the Hilbert series of the
diagonal-graded Segre algebra

\[
 \mathcal S_{n,k}
 =\bigoplus_{r\geq0}
 \bigotimes_{j=1}^k\mathbb C[x_{j,1},\ldots,x_{j,n}]_r,
 \tag{4.5}
\]

the homogeneous coordinate algebra of the Segre embedding of
\((\mathbb P^{n-1})^k\). The grading in (4.5) uses degree \(r\) in
each factor, not total tensor-product degree \(r\).

### Proof by stable sorting

The integer \(\binom{r+a}{a}^k\) counts \(k\) weakly increasing lists,
one per letter, each of length \(a\), with entries in
\(\{0,\ldots,r\}\). Merge them by increasing entry, breaking ties by
increasing letter. This gives a word \(w\in\mathcal W_{a,k}\)
and a weakly increasing value sequence
\(0\leq t_1\leq\cdots\leq t_e\leq r\). The value must increase strictly
at every descent of \(w\).

Conversely, such a word and value sequence recover the lists. Within an
equal-value block the word cannot descend, so it is ordered by letter;
merging recovers exactly the same pair. This is a bijection.

For a fixed word with \(b\) descents, subtract from \(t_i\) the number of
descents before position \(i\). The result is an arbitrary weakly
increasing length-\(e\) list in \(\{0,\ldots,r-b\}\). Its count is
\(\binom{r-b+e}{e}\) when \(r\geq b\), and zero otherwise. Therefore

\[
 \binom{r+a}{a}^k
 =\sum_{w\in\mathcal W_{a,k}}
   \binom{r-\operatorname{des}(w)+e}{e},
 \tag{4.6}
\]

with that zero convention, and

\[
 \sum_{r\geq b}\binom{r-b+e}{e}T^r
 =\frac{T^b}{(1-T)^{e+1}}.
 \tag{4.7}
\]

Summation proves (4.2), including empty words. There is exactly one
word with no descents and \(e!/(a!)^k\) multiset words in total,
proving the first two parts of (4.3). Multiplication by \((1-T)^d\)
and comparison of coefficients of \(T\) proves its last part.

For (4.4), split a word into maximal strictly decreasing consecutive
runs. Each run contains any fixed letter at most once, so \(a\) copies
of that letter require at least \(a\) runs. A length-\(e\) word with
\(q\) such runs has \(e-q\) descents, at most \(e-a\).
Concatenating \(a\) copies of \(k,k-1,\ldots,1\) attains
\(a(k-1)=e-a\), proving the exact degree.

Finally, monomial bases show that the degree-\(r\) piece of (4.5)
has dimension \(\binom{n+r-1}{n-1}^k\). Its degree-one monomials are
the Segre coordinates. Each diagonal degree-\(r\) monomial is a product
of \(r\) such coordinates, by putting each factor's variables into \(r\)
slots. This proves the algebra and Hilbert-series interpretation.
\(\square\)

For \(n=2\), each letter occurs once, so the numerator is the ordinary
Eulerian descent polynomial of permutations of \(k\) letters:

\[
 H_{2,2}=1+T,\quad
 H_{2,3}=1+4T+T^2,\quad
 H_{2,4}=1+11T+11T^2+T^3.
 \tag{4.8}
\]

Further controls are

\[
 H_{3,2}=1+4T+T^2,\qquad
 H_{3,3}=1+20T+48T^2+20T^3+T^4.
 \tag{4.9}
\]

The Segre and multiset-Eulerian identification is established mathematics,
not a priority claim. See Marcel Morales,
[Segre embeddings, Hilbert series and Newcomb's problem](https://arxiv.org/abs/1306.6910v2),
and Danai Deligeorgaki, Bin Han, and Liam Solus,
[Colored Multiset Eulerian Polynomials](https://arxiv.org/abs/2407.12076v2).
These are literature boundaries, not machine-authenticated dependencies.
The native stable-sort proof above suffices for this packet.

## 5. Constructive repair in power-trace coordinates

### Theorem GLO764.BALANCED_TRACE_EXPONENTIAL_EULER_REPAIR

Let \(n\geq1,m\geq1\), let \(A\in\mathrm{GL}_n(\mathbb C)\), and put
\(p_r(A)=\operatorname{Tr}(A^r)\). Define the genuine representation

\[
 W_m=V^{\otimes m}\otimes(V^\vee)^{\otimes m}
 \cong\operatorname{End}(V)^{\otimes m},\qquad N=\dim W_m=n^{2m}.
 \tag{5.1}
\]

Then

\[
 \operatorname{Tr}(\rho_{W_m}(A)^r)
 =p_r(A)^m p_r(A^{-1})^m.
 \tag{5.2}
\]

If \(A\) is unitary, this is \(|p_r(A)|^{2m}\), and the formal
exponential of power traces is the honest Euler factor

\[
 \boxed{
 \exp\left(\sum_{r\geq1}\frac{|p_r(A)|^{2m}}rT^r\right)
 =\det(I-T\rho_{W_m}(A))^{-1}.}
 \tag{5.3}
\]

Without unitarity, (5.3) holds after replacing \(|p_r(A)|^{2m}\)
by the algebraic expression in (5.2). This is the explicitly defined
power-trace, or plethystic-exponential, operation; it is not exponentiation
of the ordinary generating function (1.2).

The representation \(W_m\) is self-dual, has determinant identically one,
and is unchanged by every scalar twist \(A\mapsto cA\), \(c\neq0\).
For diagonal \(A\) with eigenvalues \(z_1,\ldots,z_n\), its Euler factor is

\[
 \prod_v(1-z^vT)^{-C_v},\qquad
 C_v=\sum_{\substack{\alpha-\beta=v\\|\alpha|=|\beta|=m}}
        \binom m\alpha\binom m\beta.
 \tag{5.4}
\]

Its denominator has degree \(\sum_vC_v=N=n^{2m}\), even when eigenvalues
collide. This differs from the scalar recurrence degree for
\(|p_r(A)|^{2m}\), which, along a dense full or determinant-one compact unitary torus
orbit with \(n\geq2\), counts distinct supported characters,

\[
 d_n(m)=
 |\{v\in\mathbb Z^n:\ \sum_i v_i=0,\ \sum_i|v_i|\leq2m\}|.
 \tag{5.5}
\]

### Proof

The contragredient matrix is \((A^{-1})^{\mathsf T}\), and trace is
multiplicative on tensor products, proving (5.2). For unitary \(A\),
\(p_r(A^{-1})=\overline{p_r(A)}\).
For any invertible finite matrix \(B\), triangularization and the scalar
formal identity \(-\log(1-x)=\sum_{r\geq1}x^r/r\) give

\[
 -\log\det(I-TB)=\sum_{r\geq1}\operatorname{Tr}(B^r)T^r/r.
 \tag{5.6}
\]

This proves (5.3), with constant term one and no analytic branch choice.
The nondegenerate pairing \((X,Y)\mapsto\operatorname{Tr}(XY)\) on
\(\operatorname{End}(V)\) is invariant under conjugation, so its tensor
power gives self-duality. The determinant of conjugation by \(A\) is
\((\det A)^n(\det A^{-1})^n=1\); determinants of tensor products then
give \(\det\rho_{W_m}(A)=1\). Scalar twists cancel on
\(V\otimes V^\vee\).

Expanding \((\sum_i z_i)^m(\sum_i z_i^{-1})^m\) gives (5.4), with
positive integer coefficients, total mass \(n^{2m}\), and
\(C_v=C_{-v}\). The support is exactly (5.5): write
\(v=v^+-v^-\), with \(|v^+|=|v^-|=s\leq m\), and append the same
nonnegative vector of mass \(m-s\) to both parts. Conversely any
\(\alpha-\beta\) in (5.4) satisfies those bounds.

The exact scalar recurrence assertion is the authenticated dense-torus
theorem: density separates the supported characters, positivity prevents
cancellation, and restriction to determinant one cannot identify two
sum-zero exponent vectors. Its denominator has each surviving character
once. The Euler factor (5.4) instead retains every multiplicity.
Since \(A\) and \(\rho_{W_m}(A)\) are invertible, no factor in the
determinant has zero eigenvalue; its degree is always \(N\), and its
numerator is one. \(\square\)

At \(A=I_n\), these two series are visibly different:

\[
 \sum_{r\geq0}|p_r(I_n)|^{2m}T^r=\frac{n^{2m}}{1-T},
 \qquad
 \exp\left(\sum_{r\geq1}\frac{n^{2m}}rT^r\right)
 =(1-T)^{-n^{2m}}.
 \tag{5.7}
\]

Thus the construction preserves representation multiplicities rather
than confusing them with the degree of a minimal scalar recurrence.
For \(m=1\), this is the classical \(V\otimes V^\vee\) tensor-dual
local algebra of Rankin--Selberg factors, not a new automorphic lift.
See Jacquet, Piatetskii-Shapiro, and Shalika,
[Rankin-Selberg Convolutions](https://www.math.columbia.edu/~hj/Rankin%20Selberg%20convolutions.pdf).
No global automorphy assertion follows merely from (5.3).

## 6. Exceptions and state-space boundaries

The excluded integer cases genuinely admit universal representations:

- \(k=0\): \(F_{n,0}=(1-T)^{-1}\), the trivial representation.
- \(k=1\): \(F_{n,1}=\det(I-AT)^{-1}\), the standard representation.
- \(n=1\): \(F_{1,k}(z,T)=(1-z^kT)^{-1}\), the character \(z\mapsto z^k\).

Negative and nonintegral coefficient powers are outside the statement.
Their domains and branches require separate definitions.

If a sequence has a finite matrix-coefficient parent
\(u_r=\ell(B^rv)\), then

\[
 u_r^k=(\ell^{\otimes k})((B^{\otimes k})^r v^{\otimes k}),
 \tag{6.1}
\]

with vectors in the symmetric tensor subspace. Its series is a resolvent
matrix coefficient, generally with a numerator, not necessarily a
representation determinant inverse.
At \(A=I_n\), the scalar sequence \(h_r(I_n)=\binom{r+n-1}{n-1}\)
is nonconstant for \(n\geq2\); a transfer matrix realizing it need not
become the identity with the input. The no-go theorem uses precisely
the identity requirement on a group representation.

The theorem excludes finite virtual representation-ring outputs,
including generic regular representation identities. It does not
classify arbitrary nonfunctorial matrices, maps singular at the identity,
extra Artin/Frobenius data, regularized determinants, or infinite-dimensional
and complex-rank categories. No motive, functional equation, automorphy,
or RH/GRH consequence is asserted.

## 7. Exact replay and refusal contract

The producer and tests use standard-library exact integer and rational
arithmetic. The arithmetic class is `MIXED`, comprising
`CERTIFIED_INTEGER_COVERAGE` for the declared finite combinatorial rows and
`EXACT_RATIONAL` for trace/determinant coefficients, with no rounding.
The default identity rectangle is
\(1\leq n\leq4,\ 0\leq k\leq4\), with hard maxima \(n,k\leq5\).
Two independent constructions are compared:

1. Finite differences multiply the identity coefficient series by
   \((1-T)^d\), with a bounded tail checked beyond the allowed degree.
2. A memoized state of remaining multiplicities and last letter counts
   descents without using the binomial coefficient sequence.

The replay checks equality of the resulting vectors, positivity,
\(H(0),H(1)\), exact degree, first numerator coefficient, both second-jet
defects, and strict pole-order gap in the \(n,k\geq2\) chamber.
Independent bounded word enumeration and held-out ranks/powers appear
in the tests.

The constructive controls use \(2\leq n\leq\min(4,\text{max-n})\),
\(1\leq m\leq\min(2,\text{max-k})\), comparing multinomial weight
expansion to repeated convolution of the End weights. They check
inversion symmetry, scalar-twist blindness, zero determinant exponent,
and multiplicity mass. At an explicitly labeled rational diagonal
specialization they compare four coefficients from the formal
exponential recursion to the independently multiplied determinant
factors. That specialization checks the algebraic (5.2), not a numerical
absolute value of a nonunitary matrix.

Preflight bounds count the named primary algebraic loops:
dynamic-program coefficient additions, finite-difference summands, and
finite weight/exponential operations. They do not count every diagnostic,
hashing operation, or bit operation. Total declared work must be strictly below 10,000,000;
each identity row must be strictly below 2,000,000. These are
combinatorial bounds, not wall-clock or RAM measurements. Hard parameter
maxima also apply to direct helper calls. No float operations, random
samples, external symbolic calls, or range escalation occur.

More precisely, an identity-row state has at most \(n^k(k+1)\)
possible remaining-multiplicity/last-letter combinations, at most \(k\)
transitions, and at most \(e+1\) coefficient additions per transition.
The empty-alphabet bound uses \(\max(k,1)\). The finite-difference
summand count through index \(2d+3\) is recorded exactly.
For a constructive row put \(M=\binom{m+n-1}{n-1}^2\) and
\(L=\text{cutoff}+1=5\). The declared bound is

\[
 M+\sum_{j=1}^m n^{2j}+(2n+2L^2)M+L^2+2nL.
 \tag{7.1}
\]

Here \(M\) bounds the expansion pairs and supported weights;
\(\sum n^{2j}\) bounds the End-convolution updates; the remaining
terms bound the named weight evaluations and finite trace, exponential,
and determinant-factor summands. Individual constructive rows have
an additional strict cap of 20,000.

The manifest is pinned by an expected LF-normalized SHA-256. For each
primitive note the producer authenticates its Git object at the source
commit, reads the blob bytes, and compares their normalized SHA-256
and the working-tree file to the manifest. Source drift, a missing
Git object, stale fixture content, or a reached resource cap fails closed.
Producer, note, test, and payload hashes bind the delivered local bytes;
they do not certify a proof or external literature.

Run from the repository root:

~~~powershell
python research/l-families/atlas/generalized/universal_coefficient_power_euler_obstruction.py --check
python -O research/l-families/atlas/generalized/universal_coefficient_power_euler_obstruction.py --check
python -m unittest discover -s tests -p test_universal_coefficient_power_euler_obstruction.py
python -O -m unittest discover -s tests -p test_universal_coefficient_power_euler_obstruction.py
~~~

Finite replay does not machine-prove the universal representation
quantifier, extension from a Zariski-dense set, the unbounded stable-sort
bijection, or a global \(L\)-function. Those are explicit proof or scope
obligations, not conclusions extrapolated from finite rows.

An independent audit of the original packet at
`330c6f8b85fa1923f2d4914ce3ab1775b0e56c75`, with release-only repairs and
additional exact controls, is recorded in
[the audit report](UNIVERSAL_COEFFICIENT_POWER_EULER_OBSTRUCTION_AUDIT_330C6F8B.md).
The compact-unitary qualifier above makes the imported scalar recurrence
hypothesis explicit; the algebraic trace-pair repair still applies to every
invertible complex matrix.

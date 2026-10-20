# Quadratic large-sieve input in the primary Eisenstein convention

20 October 2026. Status: source and convention audit for the new coupled
quadratic/sextic mean. This note verifies the imported quadratic sieve
input; it does not assert that the coupled absorption has been proved.

## 1. Exact primary source

Goldmakher--Louvel, *A quadratic large sieve inequality over number fields*,
[arXiv:1112.1642v2](https://arxiv.org/html/1112.1642v2), 31 May 2012,
Definition 1, Theorem 1.1, and Corollary 1.2; PDF pages 1--2.
The downloaded HTML has SHA256
`a9ce3eb6cbc267812e4f2889852a14ac9f05cb54d137a88af87dd15f9031766e`.

Theorem 1.1 bounds the squared row norm for arbitrary complex coefficients
and a quadratic Hecke family. Both indices are squarefree ideals coprime
to a fixed modulus. Its large-sieve factor is
\((MN)^\epsilon(M+N)\), and its constant depends on the field, fixed
modulus, and epsilon. Definition 1 supplies the finite-class reciprocity
and primitive-product hypotheses. Section 2 constructs the needed
families. Corollary 1.2 also applies to the quadratic powers of an even
order Hecke family; in particular one may use the cubes of a sextic
family. These are imported theorems, not consequences of the present
packet's finite checkers.

## 2. Direct bridge to the native denominator symbol

Here is the convention check for \(E=\mathbb Q(\omega)\). All ideals
and primary generators below are prime to a fixed sufficiently deep
modulus \(\mathfrak c\), supported at the bad places and including
the primes above 2 and 3. Make \(\mathfrak c\) divisible by \((3)\).
The Eisenstein ring has class number one, and each ideal prime to 3 has
a unique generator congruent to one modulo 3. These primary generators
are multiplicative, including for fractional ideals prime to 3.

In the source Section 2 construction for \(n=2\), choose the generators
of its finite ray-class representatives to be primary. Write its ideal
decomposition as
\[
                  \mathfrak a=(x)\mathfrak e\mathfrak g^2,
                  \qquad x\equiv1\pmod{\mathfrak c}.
\]
If \(a,e,g\) denote the primary generators, then
\(a=xeg^2\) exactly: the possible unit is primary and therefore one.
Choose the source representative element \(m_{\mathfrak e}=e\).
Its Kummer parameter is then
\[
                         m_{\mathfrak a}=xe=a/g^2.
\]
The source construction chooses \(\mathfrak g\) coprime to the ideal
at which the character is evaluated. Hence its quadratic character is
\[
                \chi_{\mathfrak a}(\mathfrak b)=(a/b)_2
\]
for coprime inputs. This equality is a check of the chosen normalization,
not an assumption that an arbitrary element symbol automatically defines
the source family.

The theorem is displayed with kernel
\(\chi_{\mathfrak b}(\mathfrak a)\). Thus, taking row
\(\mathfrak a=(S)\) and column \(\mathfrak b=(c)\), it is already
the desired native kernel
\[
                  \xi_S(c)=(c/S)_2=\chi_6(c/S)^3.
\]
No transposition or loss in the exponents is necessary. For completeness,
finite-class reciprocity or Hilbert-space duality gives the opposite
orientation with the same bound as well.

Consequently, for arbitrary squarefree-supported coefficients \(a_c\),
\[
 \boxed{\quad
 \sum_{\substack{S\ \text{squarefree}\\ NS\le H\\(S,\mathfrak c)=1}}
 \left|\sum_{\substack{c\ \text{squarefree}\\ Nc\le Y\\
                       (c,\mathfrak c)=1}}a_c\xi_S(c)\right|^2
 \ll_{E,\mathfrak c,\epsilon}
       (HY)^\epsilon(H+Y)\sum_c|a_c|^2 .
 \quad}                                                        \tag{2.1}
\]
Dyadic intervals follow by inserting zeros in the coefficients and
restricting the nonnegative outer sum.

## 3. Conductors, filters, and natural zeros

At an odd moving prime dividing squarefree \(S\), the local quadratic
character is nontrivial and tame, so its conductor contains that prime
to the first power. The possible conductor contributions at the fixed
bad places range over a finite set. Their dependence is absorbed into
the fixed modulus and, when necessary, a finite partition into ray
classes. This does not introduce a factor growing with \(NS\).

The character is zero when \((S,c)\ne1\); these are precisely the
natural shared-prime zeros required by the mean. They may be retained
throughout (2.1). Additional fixed row restrictions are restrictions of
a positive sum. Additional column restrictions are coefficient zeros.
Fixed ray conditions on both variables can be imposed in this way or
by a finite class partition.

If a different primitive quadratic convention is used at the bad places,
split into the finite list of those conventions first. A fixed character
of the column can be absorbed into \(a_c\). For quadratic characters
with the same squarefree odd conductor, any remaining ratio is
unramified away from the fixed bad places, so this is a finite correction
over the fixed field; it is not an arbitrary growing family of twists.

For a fixed cube variable \(d\), the completion contributes
\(\xi_S(d)^3=\xi_S(d)\). Remove that row phase only after fixing
\(d\), retaining the positive restriction \((S,d)=1\); then (2.1)
applies to the remaining squarefree column. Minkowski in \(d\) is a
separate step requiring the displayed completion weights to be summable.
This observation does not license replacing the full cube completion
by its first term.

## 4. Application boundary

The bound permits a fixed cubic-row twist, angular factor, or fixed
ramified profile inside the column coefficients, provided that
coefficient sequence is independent of the quadratic row \(S\).
If a cusp profile depends on a finite residue class of \(S\), split
those finitely many classes before applying the theorem.

It does **not** give (2.1) for the sextic partner
\(\xi_S(c)\chi_{3,S}(c)^2\) by declaring its extra cubic symbol an
arbitrary coefficient: that factor depends on \(S\). A coupled
argument must estimate that partner with its own applicable sieve
and carry the actual reflection between the two components. This is
the analytic interface which the proposed asymmetric absorption must
still justify.

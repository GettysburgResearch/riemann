# The retained angular phase in a coherent cubic label sum

20 October 2026. Status: exact free-inner-series algebra and a scoped
research interface. There is no proved Type-III prime saving here.
In particular, a diagonal upper bound is not a lower bound on the
actual trilinear sum.

The exact local algebra uses DUAL_RESUMMATION.md, SHA256
d8dae0a17a85b466ba9d9d5b762ee532ce92b0a45de7236ffe5b3bb8256dbef2,
and the source-normalized reflection in FINITE_PROFILE_CLOSURE.md,
SHA256 a4a1798f304fd9a551c35b2a161ef2f7b82644d62d9f0eae986df2afb7100dad.
The latter is used as an exact finite-component identity, not only
through its norm consequence.

Primary source: Dunn--Radziwill, arXiv:2109.07463v3, (2.3),
(5.60), (5.70)--(5.74); pinned HTML SHA256
3949e0f0ae87808d84fe02c12a3b68c5b66aa8d967d8ecb5e1605f1d985b956d.
The prime transition described below is the independent-prime
decomposition in the Ope September angular-Gauss source, as audited
separately by the boundary agent.

## 1. A phase which norm estimates legitimately discard

Write \(\alpha(r)=r/|r|\), using primary generators. The source
(5.60) contains the factor

\[
 (\overline r/r)^\ell=\alpha(r)^{-2\ell}.
\]

Solving for the original Mellin transform reverses that exponent.
The displayed source equation (5.71) consequently has
\(\alpha(r)^{2\ell}\), not its inverse. The complete finite Fourier
transform (5.70) supplies \(\overline{g(r)}c_r(u)\).
After normalizing the Gauss sum, the moving factor is therefore

\[
 \alpha(r)^{2\ell}\overline{\widetilde g(r)}
 (Nr)^{1/2-2s},
\tag{T1}
\]

times the exact common gamma quotient and the fixed ramified
coefficient matrices. All those additional factors are retained.
The gamma quotient is the one in ANGULAR_UNIFORMITY.md (U4).

The factor \(\alpha(r)^{2\ell}\) has modulus one but is not periodic
in ell. The periodicity assertions in the finite-profile and
uniformity notes concern the conversion between ramified cusp
coefficients; they do not assert periodicity of (T1).
Discarding (T1) is harmless for their norm inequalities and loses
information in a coherent signed label sum.

## 2. Exact complementary-prime factors

Consider first a complete, free-inner theta series \(Q_r(s;\ell)\),
and an outer coefficient of the coherent form

\[
                  a_r\,\widetilde g(r)\alpha(r)^\ell.
\tag{T2}
\]

Rows r are squarefree, primary, and prime to 3. The Gauss factors
in (T1)--(T2) cancel exactly. For one reflected finite profile
\(\kappa\), the remaining outer angular phase is
\(\alpha(r)^{3\ell}\). Put \(w=1-s\). The exact divisor identity
(D5) contributes

\[
 \sum_{k\mid r}\widetilde g(k)\kappa(k)\alpha(k)^{-\ell}
       (Nk)^s Q_{k,\kappa}(w;-\ell)
 \prod_{\mathfrak p\mid r/k}(qz_{\mathfrak p}-1),
\quad
 z_{\mathfrak p}=\kappa(\mathfrak p)^3
       \alpha(\mathfrak p)^{-3\ell}q^{1/2-3w}.
\tag{T3}
\]

Every profile in the realized four-component family is cubic, so
\(\kappa(\mathfrak p)^3=1\). Split \(r=km\), with \((k,m)=1\).
For each complementary prime the exact simplification is

\[
 \boxed{\quad
 \alpha(\mathfrak p)^{3\ell}(qz_{\mathfrak p}-1)
          =q^{3s-3/2}-\alpha(\mathfrak p)^{3\ell}.
 \quad}
\tag{T4}
\]

Thus, including the norm in (T1), the contribution of a fixed divisor
k has the arithmetic form

\[
 \widetilde g(k)\kappa(k)\alpha(k)^{2\ell}
 (Nk)^{1/2-s}Q_{k,\kappa}(1-s;-\ell)
 \sum_{\substack{m\\(m,k)=1}}
 a_{km}(Nm)^{1/2-2s}
 \prod_{\mathfrak p\mid m}
       \{q^{3s-3/2}-\alpha(\mathfrak p)^{3\ell}\}.
\tag{T5}
\]

This formula describes each reflected finite component; it does not
replace the full finite matrix by a scalar. Its dependence on
r modulo 9 can be expanded into the finitely many primary ray
characters. This only inserts fixed characters into the displayed
prime factors and retains all common-prime zeros. The fixed
ramified matrices and gamma scalar must still be multiplied back.

For a row made from two independently weighted prime variables,
proper divisors k leave one or two complementary prime factors in
(T5). Coprimality retains the original prime exclusion. In contrast,
the full divisor k=r leaves no prime factor of the form (T4).
That term is

\[
 a_r\,\widetilde g(r)\kappa(r)\alpha(r)^{2\ell}
      (Nr)^{1/2-s}Q_{r,\kappa}(1-s;-\ell).
\tag{T6}
\]

It is still a coherent Gauss/Dirichlet-series expression, not an
ordinary Hecke prime sum. In particular nonzero ell does not
annihilate it coefficientwise.

## 3. What a common Hecke half-plane gives in the proper terms

Assume the common all-unitary Hecke half-plane with boundary beta,
and its conductor-uniform prime-sum consequence proved in the
separate uniform packet. For a fixed smooth radial prime weight
on \(N\mathfrak p\asymp P\), fixed ray filters, and a nonzero ell,
the second term in (T4) is a nonresonant angular Hecke sum:
its size is \(O(P^{\beta+\epsilon}(1+|\ell|+|t|)^\epsilon)\),
with the usual weighted-log normalization or a harmless logarithm.
The finite-character factor from the cusp decomposition does not
make the nonzero angular type a common norm character.

On \(s=1/2-\delta+it\), the first term in (T4) has absolute size
\(q^{-3\delta}\). Its prime sum is bounded by
\(O(P^{1-3\delta+\epsilon})\), whether or not its finite-character
twist is principal. A complementary prime sum consequently admits
the bound

\[
 O\!\left(P^\epsilon
    \{P^{1-3\delta}+P^\beta(1+|\ell|+|t|)^\epsilon\}\right).
\tag{T7}
\]

This is a saving in that complementary factor relative to its
absolute P scale. It is not a bound for the full reflected sum:
the common norm powers, k-sum, gamma factors, and the full-divisor
term (T6) remain. Arbitrary complex prime coefficients are not
allowed in this Hecke cancellation claim; they could cancel the
angular character by design. The weights must have the actual
radial/ray structure just stated.

The damped term in (T4) is an actual zero-angular contribution.
It must not be omitted by saying that ell is nonzero. Thus there
are two separate issues: the damped principal contribution within
proper-divisor terms, and the surviving full-divisor expression.

## 4. The actual three-prime transition

At balanced prime scales \(N\pi_i\asymp N\), \(X=N^3\), twisted
multiplicativity gives, for pairwise distinct primes,

\[
 \widetilde g(pqr)=
 \widetilde g(p)\widetilde g(q)\widetilde g(r)
 \overline{(p/q)_3}\,
 \overline{(p/r)_3}\,
 \overline{(q/r)_3}.
\tag{T8}
\]

Cubic reciprocity makes the three residue factors symmetric.
The angular phase is \(\alpha(pqr)^\ell\). The source transition
has independent smooth prime weights, possibly with the explicitly
retained interval/order restrictions, and a common smooth product
envelope. It does not have an unrestricted inner variable.

This last fact is a substantive obstruction to applying (T3)
directly. The theta functional equation is an identity for the
complete coefficient series. Replacing that series by its
prime-restricted subseries is not licensed. One must first open a
valid prime-detection identity and retain its Möbius factors,
common-prime zeros, and all new summation ranges. Formula (T7)
cannot bypass that step.

For comparison, the source positive diagonal estimate for two
primes on the A side and one on the B side, \(A\asymp N^2\),
\(B\asymp N\), is of size \(A\sqrt B=N^{5/2}=X^{5/6}\),
up to the explicit logarithmic density savings. It is not a
lower bound for the coherent triple-prime sum.

Another exact formulation is the trace of a product of three
weighted cubic-residue matrices. If
\(C_{p,q}=\overline{(p/q)_3}\), with zero on a common prime,
then (T8) is the kernel of
\(\operatorname{tr}(D_1 C D_2 C D_3 C)\), after separating a
smooth product envelope by Mellin inversion. The ordinary cubic
large sieve gives \(\|C\|_{\mathrm{op}}\ll N^{2/3+\epsilon}\);
the Hilbert--Schmidt trace estimate is then \(N^{8/3+\epsilon}\),
which is weaker than the source diagonal bound. Repeated Cauchy
alone does not supply the missing signed correlation.

The new exact information is (T1)--(T5), including the ordinary
angular character in every complementary prime and the full
zero-angular term in (T4). A strict Type-III power saving would
need additional control of the prime projection and of (T6),
or a coherent transformation which combines them before taking
absolute values. No such estimate is established here.

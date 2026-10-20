# Independent review of the small-prime consequence

**Reviewed file:** `work/hecke_small_prime_consequence.md`.
**SHA-256 reviewed:** `978862e9932f9dfcbbacb084f45ab30aca42ae5fa2f35dffb1c7a5093b78daa6`.
**Review scope:** The implication from the stated Hecke zero-free hypothesis
\(H_B\) to character-detecting degree-one primes and ray-class subgroup
generators. This review does not certify Liu's upstream analytic theorem or
claim worldwide novelty.
**Verdict:** No substantive mathematical gap found in the reviewed version.

## 1. Field-uniform smoothed explicit formula

The archimedean normalization is correct. For a primitive finite-order Hecke
character, the gamma factors can be written with nonnegative multiplicities
\(a,b\), \(a+b=n\), in the displayed digamma formula. Complex places
contribute to both multiplicities; real-place signs change their allocation.
There is no omitted archimedean parameter whose size could destroy uniformity.

I independently opened the published primary PDF of Benjamin Wesolowski,
*Generating subgroups of ray class groups with small prime ideals*,
[DOI 10.2140/obs.2019.2.461](https://msp.org/obs/2019/2-1/obs-v2-n1-p28-s.pdf).
Its Section 2, equations (2-2) and (2-3), agree with the gamma normalization
and real-part logarithmic-derivative identity used in the note. Table 1
agrees with the residue contribution at zero, including the principal case.

At \(s=2\), the right side of the identity is bounded by
\(O(\log Q+n)\) with an absolute constant. The prime-by-prime estimate
\(-\zeta'_K/\zeta_K(2)\le n[-\zeta'/\zeta(2)]\) is valid; using
\(\sum_{\mathfrak p\mid p}f_{\mathfrak p}\le n\) is enough. The comparison
between \(1/(1+\gamma^2)\) and the positive summands
\(\Re(2-\rho)^{-1}\) is correct. It follows that

\[
\sum_\rho(1+\gamma^2)^{-1}\ll\log Q+n.
\]

The specified annular weight has integral one and supremum \(15/4\).
It and its first derivative vanish at both endpoints, so its Mellin transform
has the stated \(t^{-2}\) decay uniformly in the fixed vertical strip.
This makes the zero contribution absolutely summable without a factor of
\(n\log X\).

The shift to \(\Re s=-1/2\) crosses only nontrivial zeros, the principal
pole at one, and a possible trivial zero at zero. The order at zero lies
between zero and \(n\), so its contribution is harmless. The functional
equation reflects the left-line logarithmic derivative to absolute
convergence at \(\Re(1-s)=3/2\), and the gamma factors stay away from
their poles. The resulting bound is uniform in the field and character.

A sequence of horizontal heights avoiding zeros can depend on the fixed
field and character when establishing the exact contour identity. This
does not create a field-dependent constant in the final estimate: the final
zero sum and left-line integral have the explicit uniform bounds just
described. Thus

\[
S_\chi(X)=\delta_\chi X+O_f(X^B(\log Q+n))
\]

is supported by the proof. It needs only the location bound supplied by
\(H_B\), not quantitative constants from Liu's proof.

## 2. Incomplete characters and degree-one restriction

Removing Euler factors at the larger modulus costs at most
\(O_f(\omega(\mathfrak m_0)\log X)\), which is correctly absorbed into
\(O_f(X^B\log N\mathfrak m_0)\) for \(B\ge1/2\). The finite conductor
divides the finite ray modulus, and the infinite-place cost is retained by
the \(n\) term.

The degree-one removal estimate is also correct. After first powers of the
permitted degree-one prime ideals are removed, all remaining terms lie at
rational prime powers \(p^j\) with \(j\ge2\). This includes first powers
of higher-residue-degree prime ideals and higher powers of degree-one primes.
It also includes powers of primes whose classes are outside \(H\) but whose
higher powers enter \(H\); those terms must not be silently discarded, and
the displayed estimate does retain them.

For each rational prime and exponent, the sum of residue degrees of the
contributing prime ideals is at most \(n\). Chebyshev's estimate therefore
gives the required uniform total \(O_f(n\sqrt X)\). The finitely many
higher-power terms are bounded by
\(O(X^{1/3}\log X)=O(\sqrt X)\), uniformly for \(X\ge2\).

## 3. Subgroup projection and exponent

The annihilator \(H^\perp\) has size \(i=[G:H]\). Exactly one term in
the first projected sum is principal, and none in the translated sum is
principal when \(\chi|_H\) is nontrivial. The projection therefore has
main term \(X/i\), while averaging the \(2i\) uniform error bounds and
dividing by \(i\) leaves error \(O_f(X^B A)\), with
\(A=\log(DN\mathfrak m_0)+n\). There is no extra factor of \(i\) in that
error before solving for \(X\).

Under the absence of a detecting degree-one prime, the remaining sum is
\(O_f(n\sqrt X)\), so

\[
X^{1-B}\ll_f iA.
\]

This yields the claimed exponent \(1/(1-B)\). The subsequent generation
argument is valid because a character of a subgroup of a finite abelian
group extends to the whole group.

I independently checked the exact polynomial substitution
\(B=1-1/p\): the ascending coefficients after multiplying by \(p^4\)
are

\[
[133488,-157356,55674,-5691,116],
\]

as stated. The exact theorem uses \(p=1/(1-B_\flat)\); the decimal is
only explanatory.

## 4. Scope and optional sharpening

The conclusion is a classical explicit-formula corollary with a new imported
zero-free input. The reviewed note correctly avoids identifying a detecting
prime with a prime in every prescribed ray class, and it does not import
Wesolowski's numerical ERH constants unchanged.

For a fixed field \(K\), the proof only needs \(H_B\) for finite-order
Hecke characters of that field. The hypothesis over every number field is
appropriate for the uniformly quantified global conclusion, but it is
stronger than necessary for each individual fixed-field application. This is
an optional clarification, not a defect in the reviewed theorem.

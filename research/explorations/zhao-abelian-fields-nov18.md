# The abelian fields in Zhao's spectral condition

Assume GRH for the Dedekind zeta functions under consideration. Exactly **229 abelian extensions of the rational field**, counting the rational field itself, satisfy the strict sufficient condition \(B_K<2\) in Zhao's §8(3). Here \(B_K=\sum_\gamma(1/4+\gamma^2)^{-1}\) counts both signs and all multiplicities. The inventory identifies each field by its group of primitive Dirichlet characters, with conductor and Conrey identifier. It also gives the absolute discriminant and signature. [Inventory](zhao-abelian-fields-nov18.json) · [Python/Arb certificate](../../scripts/check_zhao_abelian_fields_nov18.py) · [Source question](https://doi.org/10.1007/s40993-025-00640-y)

| Degree | Fields | Totally real |
|---:|---:|---:|
| 1 | 1 | 1 |
| 2 | 168 | 116 |
| 3 | 7 | 7 |
| 4 | 47 | 16 |
| 5 | 1 | 1 |
| 6 | 4 | 2 |
| 8 | 1 | 0 |

The unique octic example is the full fifteenth cyclotomic field. These are the fields passing the strict spectral bound. The sign behavior for the remaining fields is a separate question.

## Bounding the individual characters

By Kronecker–Weber and the abelian factorization of the Dedekind zeta function, the field corresponds to a finite group \(G\) of Dirichlet characters identified with their primitive forms. The nontrivial characters contribute nonnegative weights
\[
 b(\chi)=\log(q/\pi)+\psi((1+a)/2)+2\Re(L'/L)(1,\chi),
\]
where \(q\) is the conductor and \(a\) the parity. The completed logarithmic derivative gives this identity by summing over ordinates on the critical line. It applies also to nonreal characters, whose zeros reflect across the critical line by the functional equation and conjugation. Conjugate characters have the same weight. A field passes the test exactly when \(\sum_{1\ne\chi\in G} b(\chi)<T=2-B_\zeta\). Under the same assumption the [general degree bound](zhao-number-fields-nov18.md) gives \(|G|\le15\).

Real primitive members must lie in the already checked list of 168 quadratic discriminants. For a nonreal character the field contains its inverse, so \(b(\chi)<T/2\). At \(s=7/4\), use
\[
 \tfrac12\log(q/\pi)+\tfrac12\psi((s+a)/2)+\Re(L'/L)(s,\chi)
 \le (s-1/2)b(\chi),\qquad \Re(L'/L)(s,\chi)\ge\zeta'/\zeta(s).
\]
Consequently \(q<463\) for even and \(q<226\) for odd nonreal members, by a 96-bit ball evaluation. The program enumerates all primitive Conrey labels at these moduli with order at most 15. It evaluates one representative of each of the 1,841 nonreal conjugate pairs at 1 by the first two Taylor coefficients of its Dirichlet L-function. Every comparison uses strict disjoint Arb intervals and aborts for an unresolved boundary. This also checks the quadratic weights afresh on the supplied list.

## Closing under multiplication

To identify products having possibly different conductors, fix generators of the local unit groups. At an odd prime choose a primitive root modulo its square, which remains a generator at every positive exponent. At 2 use \(-1,5\), allowing redundant identity generators at small exponents. Evaluate a character on each generator by lifting to a unit equal to 1 on the other prime components. Each phase is an exact integer multiple of \(1/\operatorname{lcm}(1,\ldots,15)\) turns. The resulting finite tuple of nonzero local phases determines the primitive character uniquely and multiplies by componentwise addition. Thus the program computes the partial multiplication table of all eligible candidates, including inverse and identity checks.

Starting from the trivial group, adjoin each candidate and enumerate successive cosets until the identity coset is reached. Reject an extension at the first missing product or excess degree. For each new closed group test its total spectral weight by interval arithmetic. Nonnegative weights imply all subgroups of a passing group pass, so induction on the number of generators proves exhaustion. The conductor is the least common multiple of the character conductors, the absolute field discriminant is their product by the conductor–discriminant formula, and all characters are even precisely for totally real fields. Different subgroups yield distinct fields up to rational isomorphism since the extensions are normal.

# Independent review of the full common-D root-return extension

**Reviewer:** the coherent-identity agent, separately from the author
of `COMMON_D_TRIANGLE_EXTENSION.md`. **Verdict:** pass for the full
three-edge raw rooted-return class with unchanged shared prime sets,
including different initial and final lists. The continuous bound is
exact at its stated scope; the conservative arithmetic corollary
imports the explicitly retained Appendix A.5 premise.

## 1. Frozen objects and replay

| Object | SHA256 | Git blob |
|---|---|---|
| `COMMON_D_TRIANGLE_EXTENSION.md` | `67769f6a6f2a9c6c8beca1aad4c94f7150d71b4d11253515e355df84c3ff7bc9` | `1ec8c0f0444c2d4353454ac2d7a7fce31fd9143f` |
| `check_common_d_triangle_extension.py` | `1e449d9aa11395fc9cf6dd76f86cb49ac3a26bf6dd897b079f16217408cfb400` | `1bdc7ba47731f803739955c40a2dbb4d23150c0f` |

I read the complete note, inspected the checker, and independently ran
the checker under `python -O`. It passed. The original source
normalization and Appendix A.5 were independently checked in my
`REVIEW_CLOSED_TRIANGLE_SOURCE.md`; the present review checks the
new endpoint, prime-pattern and four-product arguments rather than
assuming that the earlier list-diagonal result extends automatically.

## 2. The prime collision exclusions are exact

The chronological products are Db,Da,Dc,Dd at relative vertices
z_0,z_1,z_2,z_3, with z_0=z_3=(1,0). Their determinants are
\(D(b-a),D(a-c),D(c-d)\). Adjacent legal replacements already
exclude b_i=a_i, a_i=c_i and c_i=d_i.

If b_i=c_i=p, a nonzero active-line indicator would require z_0
and z_2 to be on the same projective line modulo p. But their
determinant is the negative of the last edge determinant, which is
nonzero modulo p because the legal last replacement has p not
dividing Dd. This is impossible. Likewise a_i=d_i would equate
the lines of z_1 and z_0, contradicting the nonzero first edge
determinant modulo that prime.

Consequently each group either has b_i=d_i with three distinct
unshared primes, or has four distinct unshared primes. These exhaust
the possible equality patterns. Primitivity is essential and is
retained: it guarantees that each projective reduction exists.

## 3. Different endpoint lists have the claimed original weight

Let I be the returning groups and t the product of their repeated
primes. Unique factorization and the disjoint groups give
\(t=\gcd(b,d)\), with b=tb' and d=td'. The active union is
the squarefree product Dactb'd'. Each active prime has one specified
line, including a returning prime that appears at both copies of
the identical root. Thus its once-only line average is at most

\[
       \frac1{Dactb'd'}=\frac{t}{Dabcd}.
\]

The note correctly avoids carrying over the earlier assertion that
all inactive damping is one. In particular, a prime active at the
first root remains incident at the identical final position even
when it is absent from the final active list. Its extra damping can
be less than one. The proof retains it as a factor at most one and
then drops it only in an upper bound.

The two unordered root states can differ, but the actual root vector
is one on every such state. Both orthonormal coordinates are
\(\sqrt{((J+1)!)^K\prod_iV_i^{-(J+1)}}\). Their product is
therefore the same constant as in the list-diagonal calculation.
The three original symmetrized edge factors are unchanged as well.
After the shared-list sum the prefactor is exactly

\[
                         (J+1)^{-2K}\prod_iV_i^{-4}.
\]

There is no trace restriction, no independent endpoint assumption,
and no second draw of a returning prime. The six eta factors and
three raw d_0/D factors have the stated bounds. All numerical label
enlargements occur after the genuine prime-level weight is obtained.

## 4. Closed solvability cancels the gcd in the new count

Put h=b-a, k=c-d and g=gcd(|h|,|k|). The closed-position
linear equations give one congruence class for the first position
coefficient if and only if g divides a-c. The exact multiplicity
mean is then Wg/|h|, with W=255/16.

For proper I, a is coprime to t, so h and therefore g are
coprime to t. The identity

\[
                    a-c=t(b'-d')-(h+k)
\]

shows that solvability is equivalent to g dividing b'-d'. This
restriction is needed before summing g; the note retains it.

I checked the lower bound B=Y/t at least one. Proper I makes b',d'
distinct odd integers greater than one. Their larger member is at
least five, while both are at most 4Y/t. Hence t at most 4Y/5.
The odd-prime hypothesis supplies this fact; it would not follow
merely from t being a divisor of b at most 4Y.

On the original ranges, the scalar weight is at most t/Y^4.
After taking that bound, fix signed nonzero h,k of size at most
H=floor(3Y). For each b' in [B,4B], the number of **different**
d' in the same residue class modulo g is at most
2 floor(3B/g). There are at most 4B possible b', proving the
24B^2/g bound. Each pair determines a,c uniquely. Thus the
unweighted ratio sum is at most

\[
 24B^2(2H)\left(2\sum_{n\le H}\frac1n\right)
       \le288\frac{Y^3}{t^2}(1+\log(3Y)).
\]

Multiplication by t/Y^4 proves the stated 288/(tY) logarithmic
bound. The exclusion b'=d' is crucial: the diagonal would not obey
this inverse-g pair count and is handled separately by the earlier
three-product theorem.

The sum over actual return products t is at most
\(\prod_{i\in I}V_i\). No factorization multiplicity is missing.
Summing proper I therefore gives exactly
\(\prod_i(1+V_i)-\prod_iV_i\). Adding the all-returning case
proves the full bracket in equation (11).

## 5. Conservative discrete-root budget and scope

For fixed J,K, the maximum used-prime modulus and number of label
families are each bounded by \(x^{(J+4)\beta}\). The first
position window allows \(O(x^{(J+1)\beta})\) integer position
coefficients per family. Each fixes at most one second vertex.
The active lines of every primitive retained candidate are
prescribed, so there is no additional line-choice sum.

Applying the unchanged Appendix A.5 discrepancy to the single root
interval for each candidate gives

\[
 (J+4)\beta+(J+1)\beta+5(J+4)\beta-\delta/100
                   =(7J+25)\beta-\delta/100.
\]

No reciprocal-prime discount is attached to this error. The fixed
lower bound for V_i suffices for the main-term constants: every
positive V_i power in the subset sum is paired with V_i to power
minus four. The example's error exponent is exactly -17/10000.

This proves the stated conservative source-dependent arithmetic
corollary, without relying on the later root-count refinement. It
still concerns a finite-depth parameter variant. Changing shared
sets, immediate two-edge contractions, comparison-kernel terms,
arbitrary attached history, and the native inverse transfer remain
outside the result. The note states these limitations correctly.

## 6. Finite verification

The optimized replay passed 1,892 literal active-line averages,
28 excluded cross-collision paths, 305 surviving primitive paths,
27 partial-return gcd reductions, 210 reduced-endpoint pair counts,
162,826 weighted four-product terms at 15 scales, 94 soluble and
20 insoluble label families, six subset normalizers, seven
discrepancy budgets, and both negative controls.

Those computations verify finite instances and normalizers. The
analytic sum and the conditional arithmetic transfer are justified
by the proofs above and the stated source premise, respectively.
The enlarged common-D rooted raw class is approved at that scope.

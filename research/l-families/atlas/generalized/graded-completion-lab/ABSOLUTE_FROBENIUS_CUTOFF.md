# A grading genus coherent with constant-field Frobenius powers

Status: separate proof draft and operation-law target, before implementation.
This uses the same F7 Frobenius and actual even-grade multiplicities as
`GRADING_GENUS_COMPLETION.md`, frozen at
`32c4a249d188612729f093815b4a445b796893a0`, proof blob
`d133bba85a2f335b9f795fb041df4b4d204de27b`.
No new curve, field count, operator, or recovery of the native source
normalization is supplied.

The previous linear policy has a changed-slope norm law. A different declared
policy can instead be coherent across all constant-field powers of one fixed
Frobenius. The key is to cut off the exponent of the original Frobenius, not
the exponent measured anew after each extension. This makes a positive
coherence statement without asserting uniqueness of the cutoff choice.

## 1. A fixed absolute cutoff

Let C_n be positive integers for the even source grades n≥4. For the extension
Q=7^e, define

    p_(e,n)=ceil(C_n/e).

Keep lambda=i sqrt(7), the source multiplicity a_n, and the canonical factor
E_(p-1) of the grading-genus theorem. Define

    A_(e,C)(z;xi)=product_(even n≥4,epsilon=±1)
       E_(p_(e,n)-1)(xi (epsilon lambda)^e z^n)^(a_n).    (1.1)

For a small zero-free disk the logarithm of a grade-n block is exactly

    -a_n sum_(h≥1, e h≥C_n)
           xi^h tr(Frob_7^(e h)) z^(nh)/h.              (1.2)

Indeed h≥ceil(C_n/e) is equivalent to e h≥C_n. Equation (1.2) is a
definition by actual canonical factors, not permission to use its full
power series beyond its local domain.

For every fixed e the policy p_(e,n) tends to infinity if and only if C_n
does. The preceding grading-genus theorem therefore proves that (1.1)
converges normally on the unit disk for every fixed e at xi=1 exactly when
C_n→∞. Under that condition it is jointly holomorphic in z and xi on |z|<1
and xi in C. At **xi=1**, each such choice gives the same source zero divisor
and a meromorphic unit-circle natural boundary. No such zero-divisor or
natural-boundary assertion is made here for arbitrary xi; at xi=0 the product
is identically one. These are global regularized scalar frames, not the
unchanged native scalar germs.

## 2. The same-policy norm law

For every positive integer d,

    A_(ed,C)(z^d;xi^d)
      = product_(omega^d=1) A_(e,C)(z;omega xi).          (2.1)

The sequence C is unchanged on the two sides. To prove (2.1), use (1.2)
near zero and sum over omega. Only h=d*l survives, with sum omega^h=d.
Its cutoff is

    e d l≥C_n,

which is exactly the left cutoff. Its coefficient d/(d*l)=1/l, its phase
is (xi^d)^l, and its grading is z^(ndl). Thus every individual source
block satisfies the identity. Equivalently, the elementary canonical-factor
formula uses the integer equality

    ceil(ceil(C_n/e)/d)=ceil(C_n/(ed)).

This proves the finite block identity, not only equality of a fitted total
series. Normal convergence and the identity theorem extend it to the whole
unit disk, including at zeros. No quotient of zero values is used.

For odd e the two eigenvalues are opposite, so A_(e,C)(z;-xi) equals
A_(e,C)(z;xi). In particular

    A_(2e,C)(z^2;1)=A_(e,C)(z;1)^2  (e odd).             (2.2)

Unlike the fixed linear slope convention, this is one family with the same
absolute cutoff C. It concerns the regularized cohomological multiplier.
It does not assert a scalar substitution law for the full place-Euler source
or interchange extension and inertia invariants.

## 3. What the norm law determines at a single grade

There are two useful precision levels. The actual-block classification and
threshold-distinctness statements in this section are at xi=1; they are not
inferred from the degenerate zero-phase product.

**Literal cutoff rules.** Suppose integer thresholds p_(e,n) are required to
commute with the cyclic sieve before imposing any trace identity. The condition
is p_(ed,n)=ceil(p_(e,n)/d). Taking e=1 shows that all such systems are exactly

    p_(e,n)=ceil(C_n/e),  C_n=p_(1,n).

Thus the absolute-cutoff form classifies this declared class of rules. It does
not select the sequence C_n.

**Actual source blocks.** The F7 source has zero odd power traces, so literal
thresholds can differ while defining the same block. For a threshold p at
extension e, the first surviving trace order is

    q_e(p)=p if e is even, and 2 ceil(p/2) if e is odd.

The canonical block depends only on q_e(p); increasing p past an omitted odd
trace changes no counterterm. Conversely, two different surviving thresholds
give different blocks, since the coefficient at the first crossed trace order
is nonzero. This conclusion is made at one grade before summing grades.

Suppose the actual grade-n blocks, rather than only their full products, obey
the unmodified norm law for all e,d. From the norm with e=1 and d arbitrary,
their surviving threshold is forced by p_(1,n). Put

    C_n^eff=2 ceil(p_(1,n)/2).

If d is even, ceil(p_(1,n)/d)=ceil(C_n^eff/d), since the two numerators
either coincide or are consecutive odd/even numbers. If d is odd, taking
the first even surviving order gives

    2 ceil(p_(1,n)/(2d))=2 ceil(C_n^eff/(2d)).

Consequently the blocks are exactly those of the absolute-cutoff family
C_n^eff. Conversely every such family satisfies (2.1). This classifies
blockwise norm-compatible policies up to the actual zero-trace ambiguity.
It does not classify identities created accidentally after combining different
grades, and it supplies no uniqueness theorem for arbitrary sheaf sources.

## 4. Choice dependence and the original normalization

Two divergent absolute-cutoff sequences C and D give products whose quotient
is a global holomorphic unit. At extension e define U as the normalized
logarithm of A_(e,D)/A_(e,C), so its explicit sign convention is

    U_(e;C,D)(z;xi)=sum_n a_n
       sum_(ceil(C_n/e)≤h<ceil(D_n/e))
                  xi^h tr(Frob_7^(eh)) z^(nh)/h,         (4.1)

with the oriented-sum convention when the bounds reverse. The grading-genus
tail estimate proves normal convergence, after retaining the finite polynomial
head. The same cyclic sieve proves the additive norm law for U. Thus not only
the products but their changes of frame are coherent with (2.1).

The choice remains real: C_n=n and D_n=2n already give different e=1 products,
with first difference in degree16. Adjacent cutoffs crossing only odd original
Frobenius powers can agree; the effective even cutoff in section3 records that
ambiguity. Neither coherence nor the source grading singles out C_n=n.

For C_n=n, the first extension has the previously proved expansion

    A_(1,C)(z;1)=1-49 z^16+(686/3)z^24+O(z^32).

At e=2, p_(2,n)=n/2 on every even grade, and

    A_(2,C)(z;1)=1-98 z^8+(1372/3)z^12+O(z^16).         (4.2)

These are consistent with (2.2); they are not the products obtained by keeping
the extension-relative slope one at e=2. They also differ from the native
integral Frobenius multipliers. Multiplication by the actual integral H2 still
has the previously stated nonintegral coefficient at e=1. The construction
therefore repairs a base-change coherence law by a declared scalar
regularization, while retaining its normalization cost.

The reference Frobenius Frob_7 and its powers are part of this family. No
reference-free extension to arbitrary arithmetic objects, archimedean factors,
or all ramification operations has been proved. Those would require additional
source functors and compatibility maps.

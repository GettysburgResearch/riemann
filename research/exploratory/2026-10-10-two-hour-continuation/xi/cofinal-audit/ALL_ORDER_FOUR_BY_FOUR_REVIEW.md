# Independent review of actual all-order size-four Hankel positivity

Verdict: ACCEPT F4.1–F4.11 at
`../../operators/ALL_ORDER_FOUR_BY_FOUR_HANKEL.md`, SHA
`5be9809ae8521de1cc1cb42a44f65d279c72c778a06d0f4195e2d2991f73fa97`,
and its checker SHA
`4e3ad96d34d74ca898e6e891626a023013e6b413266d9cdf032e0b0f7357147e`.
I independently read the complete source, mathematical argument and code,
then directly ran its exact rational guards normally and under -O. Own
preserved `four_by_four_hankel_normal.json` and optimized receipts are
byte-identical to the owner, SHA
`484d15709dbb2826436e79b9d4c472ec2a36acdab822e7850c25843ffd13a214`.
No native root, moment, jet or heat computation was performed by this replay.

The theorem concerns the COMPLETE actual Xi source. At fixed t1 and c3/4,
with `b_n=c^n C_(n+1)(1)`, it establishes

\[
 (b_{n+i+j})_{0\le i,j\le3}
  \succeq\frac{I}{30000000000000000000\,1250^{n+1}}
                  \quad\hbox{for EVERY integer }n\ge0.
\]

All complex coefficient vectors, unknown complex occurrences, real tail
terms and positive integer multiplicities remain in this statement.
The matrix sum at complex nodes is bilinear with a transpose, rather
than a positive Hermitian Gram sum.

I checked the actual four anchor intervals and each of their six pairwise
node gaps. The full Lagrange coefficient bound controls the inverse
Vandermonde matrix uniformly over the intervals, rather than inverting
their midpoints. Its Frobenius price is exactly16044560000000000000,
strictly below20000000000000000000. Weighting the resulting real Gram
bound by the minimum node1/1250 and factor1/c gives the complete real-head
gap for every n. All other complete real-head terms are positive.

For n>=5 the previous full-source tail norm remains valid in four
dimensions because the polynomial factor norms are bounded by the finite
geometric sum, hence by `1/(1-alpha²)`. The exact tail/head ratio is below
1/2 at n5 and decreases at every later integer index. Its complete count
input is the sharper theta/Jensen N(x)<x log(x), and both Stieltjes
endpoints have already been paid in that imported tail theorem.

For n0,...,4, I independently derived the full conjugate-pair formula
`u(|R_a|²-|I_a|²)-2v Re(R_a*conj(I_a))`. Completing its complex-coefficient
square gives the exact negative price `|w|²/u*|I_a|²`. The strip bounds
give `|(n+1)arg(z)|<5/R` and hence u>|w|/2. The telescoping imaginary-part
identity and Cauchy–Schwarz bound the cubic coefficient contribution by
2y² times the full coefficient norm. After counting BOTH conjugates,
the per-occurrence price is `4c^(n+2) gamma^(-2n-8)`.

The complete upper count gives, for every p>=8,
`sum m gamma^-p < (512/49)R^(1-p)`. I checked its antiderivative and
the exact coefficient `(8/7)(9+1/7)=512/49`. Thus the entire low-order
negative tail has the stated price2048c²/(49R⁷) times(c/R²)^n. Its exact
ratio to the head is below1/2 at n0 and decreases, covering all five low
indices. No negative complex block is discarded. Real unknown nodes are
positive and may safely be omitted from a lower bound.

Current direct and inherited hashes, the full size-two and small-shift
adapter chains, and the original native census's source table were checked
against frozen files. The complete actual real5419 head and first four
strict native-root intervals are explicit accepted imports; no historical
count or all-height root-location assumption is used. The finite checker
authenticates the source contracts and rational constants, while the full
analytic proof establishes the infinite order range.

Every principal size-three and size-two submatrix is therefore positive,
but the universal Hankel criterion requires unbounded matrix size. The
new theorem supplies no such passage, no universal mixed signs, no
complete heat monotonicity, no simplicity or cofinal success, and no RH.

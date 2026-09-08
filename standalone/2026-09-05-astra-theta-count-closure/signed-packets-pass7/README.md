# Signed-packet continuation: unbounded-rank prime tails and actual full blocks

**RH and the full all-width matrix inequality remain UNPROVED.** This packet
contains complete proposed component proofs and finite validation, not an
independently reviewed theorem or a claimed RH completion.

Base: PR #790 at f0584f7a49550540eaed005868422a83cb3e1011.
The prime-cutoff packet was imported unchanged by another agent at that head,
alongside the independent signed-tail-pass6 packet. All earlier files are
preserved. This continuation adds only signed-packets-pass7/.

## Main advances

### 1. Arbitrary-coefficient signed prime-tail matrices, in unbounded dimension

For d>=0, define the (d+1)-dimensional packet

    E_(m,d)=span{u_m,...,u_(m+d)},
    Laplace(u_j)(A)=A/(A+1)^j.

Equivalently every transform is R=A/(A+1)^m p((A-1/4)/(A+1)), deg p<=d.
Let g(x)=R(x^2+1/4)^2 and I=int_R g(x)dx. For integer cutoff X>=2, put
D=ceil(log_2(d+2)), L=ceil(log_2 X). Then

    m >= (d+2)max{256(D+1),40(17+L^2)}

implies, for EVERY nonzero real coefficient vector,

    sum_(n>X) Lambda(n)/sqrt(n) ghat(log n) < -(3/2)I <0.

Thus the entire omitted-tail matrix is strictly below -(3/2) times its
specified positive real-frequency Gram matrix. Every cross term is retained;
this is not an entrywise assertion or a nonnegative coefficient cone.
The order cost is O((d+2)[log(d+2)+log^2 X]).

The proof combines a signed-polynomial Jacobi energy estimate, a complex
Legendre evaluation bound, and the full source constant sum_A 1/Re A<1.
It requires no PNT, zero-prefix verification, simplicity, or prime scan.

**The omitted tail is not the full form.** The latter satisfies the strong
but sign-insensitive estimate

    |Q| <= 2592 m(d+1)^4(8m)^(2d)(25/64)^m I,

which is <exp(-m/4)I in the stated degree range. Its residual sign is not
thereby determined. See SIGNED_TAIL_MATRICES.md, SP7-1 through SP7-3.

### 2. Actual full positivity on every consecutive three-dimensional block

For EVERY integer m>=5, the literal xi matrix

    [sum_A A^2/(A+1)^(2m+i+j)]_(0<=i,j<=2)

is strictly positive definite. This covers all real signed coefficients
in E_(m,2), not only its generators or individual entries.

The proof bounds the complete unverified zero tail against three real
reservoir nodes. It uses the published critical-line verification through
height 100 and a separate directed sign certificate in (14,15), (21,22),
(25,26). Multiplicities need not be one. V100 is imported, not rerun; the
six endpoint signs are independently recomputed in this packet with an
explicit eta tail and the stated interval-Gamma software dependency.

### 3. Fixed-width negative directions cannot be removed by shifting

For any finite leading cluster of DISTINCT invariant parameters separated
in |A+1| from the rest, the corresponding shifted finite form eventually
has exactly the cluster's number of nonreal conjugate pairs as its negative
index. If RH fails, one FIXED finite width therefore remains indefinite at
every sufficiently large shift. This includes the shift ranges where the
new omitted-tail theorem holds.

The exact synthetic control 4,8+i,8-i has positive heat and the same strip
inequality, but an explicitly interpolated rational polynomial in every
E_(m,2) has full form -2. It is not xi and does not have its Euler product.

Read ACTUAL_BLOCKS.md, SP7-4 through SP7-6, for both the actual positive
result and the full proof of this scope boundary.

## Replay and review

    python verify.py --check checks.json
    python -O verify.py --check checks.json
    python verify_low_zeros.py --check low_zeros.json
    python -O verify_low_zeros.py --check low_zeros.json
    sha256sum -c SHA256SUMS

verify.py uses only the standard library and performs exact rational and
Gaussian-rational algebra. verify_low_zeros.py requires mpmath==1.3.0 and
makes its interval-Gamma trust boundary explicit. Neither checker proves
the infinite analytic arguments. See VALIDATION.md for what actually ran.

Read SOURCES_AND_REVIEW.md for exact sources, changes from both pass-6
packets, novelty boundaries, and review priorities. No parent test suite,
Lean build, remote CI run, all-height zero verification, or broad prime sum
is asserted in this continuation.

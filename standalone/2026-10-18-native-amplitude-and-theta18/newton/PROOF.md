# A power-small low-product amplitude sector in the native Newton identity

Status: **proposed unconditional component theorem, awaiting independent
mathematical review.** This estimates part of the retained native amplitude;
it is not another estimate for the within-block compression error. It does
not prove the remaining coarse-energy recurrence or RH.

Scope: the complete strict Newton square step, with the literal rational
Mobius source and every product of old-prefix indices retained before the
decomposition. The kernel estimate is valid for arbitrary complex
coefficients bounded by the two-fold divisor function. Its application
uses the native inverse identity. No new Mobius-sign cancellation theorem,
zero-free strip, short-interval estimate, or improved large sieve is assumed.

Exact inherited source: NRC32, PR #905 at
`0f82df3bf1d0bc669a1bbca09f8404b77c6fecde`,
`standalone/2026-09-21-native-covariance-compression/PROOF.md`.
The strict finite inverse identity and the quadratic coordinates are
reproduced below. The projection consequence applies in particular to the
partition of PR #974 at `89c37b6707cb77fc5a86143ea98d8756759fdcbc`.
That packet is unchanged.

## 1. Statement: remove a complete input-product range with a power error

For an integer Y>=1 put b=Y+1, N=b^2-1, and

    m(k)=sum_(n<=k) mu(n)/n,
    g_Y(n)=mu(n) 1_(n<=Y),
    z_Y=g_Y*g_Y,
    F_K=sum_(1<=k<=K) m(k)^2.

Dirichlet convolution is meant. In particular, |z_Y(d)|<=d_2(d), and its
support is d<=Y^2. Define two exact old-prefix balance coordinates

    M_Y=m(Y),
    B_Y=1+sum_(n<=Y) mu(n)log(n)/n
                      -(log Y+gamma/2) M_Y,                 (1.1)

where gamma is Euler's constant. The second coordinate can equivalently
be written

    B_Y=1-integral_1^Y m(floor t) dt/t-(gamma/2)M_Y.

These are finite expressions. No infinite sum identity or unestimated
tail is used to define them. The constant 1 is the actual mu(1).

For t>0 let

    R(t)=H_floor(t)-log t-gamma,       H_0=0.                (1.2)

Fix a real rho with 1/2<rho<2/3. Partition the square step into the dyadic
annuli X_j=2^j b<b^2, with cells

    J_j=[X_j,min(2X_j,b^2)) intersect Z,
    D_j=floor(X_j^rho).

For k in J_j define the filtered amplitude

    P_(Y,rho)(k)
       =2 M_Y B_Y+M_Y^2 log(Y^2/k)
           -sum_(D_j<d<=Y^2) z_Y(d) R(k/d)/d.              (1.3)

**Theorem 1 (complete low-product amplitude bound).** There is an explicit
constant depending only on rho such that

    sum_(b<=k<b^2) |m(k)-P_(Y,rho)(k)|^2
       <= C_rho b^(-(2-3rho)) (1+log b)^8.                (1.4)

For example one may take

    C_rho=10752/(1-2^(-(2-3rho))).

Thus this complete amplitude error is a negative power of Y, up to the
displayed logarithm. The theorem removes ALL coefficients with product
d<=D_j on each annulus, after retaining the two explicit balance
coordinates. On an annulus it in particular removes every ordered pair
(a,c), a,c<=Y, for which min(a,c)<=floor(D_j/Y).

At the concrete choice rho=5/8, the squared amplitude error is
O(Y^(-1/8)(1+log Y)^8). On the final annulus X_j is comparable to Y^2,
so the low-product threshold is of order Y^(5/4), and all interactions
with one old-prefix index up to a constant times Y^(1/4) are in the
controlled sector. No claim about the remaining larger products follows
from their number alone.

Every value in (1.3) is an explicit quadratic form in the old prefix.
Products d>k MUST still be retained there: although their original
H_floor(k/d) is zero, their renormalized remainder is -log(k/d)-gamma.
Those terms cancel the corresponding logarithmic balance terms. This
is still a finite sum, not an infinite continuation of the short source.

## 2. Exact native balance, before taking any estimates

Let 1(n)=1 and let delta be the Dirichlet-convolution identity. Set

    v=2g_Y-1*g_Y*g_Y.

The literal relation mu*1=delta gives

    mu-v=mu*(delta-1*g_Y)*(delta-1*g_Y).

The last two factors vanish below b, so v(n)=mu(n) for EVERY n<b^2.
There is no assertion at the first possible error coefficient b^2.
Taking weighted partial sums gives, for b<=k<b^2,

    m(k)=2M_Y-sum_(d<=Y^2) z_Y(d)H_floor(k/d)/d.          (2.1)

The finite convolution identities are

    sum_d z_Y(d)/d=M_Y^2,
    sum_d z_Y(d)log(d)/d
           =2M_Y sum_(n<=Y)mu(n)log(n)/n.

Insert (1.2) into (2.1), with the sum still over every d<=Y^2. This gives
the exact identity

    m(k)=2M_Y B_Y+M_Y^2 log(Y^2/k)
                      -sum_(d<=Y^2)z_Y(d)R(k/d)/d.       (2.2)

Subtracting (1.3) now gives

    m(k)-P_(Y,rho)(k)
                 =-sum_(d<=D_j)z_Y(d)R(k/d)/d.          (2.3)

There has been no unsigned replacement in (2.2) or (2.3). The next lemma
will bound (2.3) for a larger coefficient class; its power gain comes
from periodic oscillation of the exact harmonic kernel.

## 3. An elementary harmonic remainder estimate

For t>=1 put psi(t)=1/2-{t}, with the value 1/2 at each integer. Then

    R(t)=psi(t)/t+e(t),       |e(t)|<=3/t^2.              (3.1)

Here is a proof sufficient for the stated constant. For f(x)=1/x the
trapezoidal error on [n,n+1] is nonnegative and at most
sup_[n,n+1] f''/12<=1/(6n^3). Telescoping these errors, using the
definition of gamma, gives

    |H_m-log m-gamma-1/(2m)|<=1/(4m^2),       m>=1.

Indeed sum_(n>=m)n^(-3)<=m^(-3)+(2m^2)^(-1)<=3/(2m^2).
For m=floor t, v={t}, put u=v/t. We have m>=t/2 and 0<=u<=1/2.
Expanding log(m/t)=log(1-u), the three errors are bounded by

    |log(1-u)+u|<=u^2/[2(1-u)]<=1/t^2,
    |1/(2m)-1/(2t)|<=1/t^2,
    1/(4m^2)<=1/t^2.

Their sum proves (3.1). The integer values of the sawtooth are essential;
no almost-everywhere convention may replace them on these integer cells.

## 4. Complete rational-frequency control of the low-product sector

**Lemma 2 (kernel amplitude bound).** Let K,D be positive integers with
1<=D<=K. For any complex coefficients c(d) satisfying |c(d)|<=d_2(d),
put

    T(k)=sum_(d<=D) c(d)R(k/d)/d.

Then

    sum_(K<=k<2K)|T(k)|^2
       <=21(1+log D)^8 [D/K+D^3/K^2].                   (4.1)

The estimate also bounds any subset of those output cells. It is uniform
in the coefficients and includes their complete off-diagonal covariance.

### 4.1 The mean and every reduced denominator

For integers d>=1 define

    u_d(k)=(d-1)/(2d)-(k mod d)/d.

Its mean on a complete period is zero, and

    psi(k/d)=1/(2d)+u_d(k).                              (4.2)

The exact finite Fourier expansion is

    u_d(k)=sum_(1<=a<d)
                e(ak/d)/[d(1-e(-a/d))],                (4.3)

where e(x)=exp(2pi i x). This follows by summing the finite geometric
progression and its derivative. The sum is empty for d=1.

For each q<=D put

    Z_q=sum_(d<=D,q|d)c(d)/d.

Grouping equal frequencies in (4.3), rather than treating different
representations of one rational number as separated, gives exactly

    P(k):=sum_(d<=D)c(d)psi(k/d)
       =Z_1/2+sum_(2<=q<=D) Z_q
          sum_(1<=a<q,(a,q)=1)e(ak/q)/(1-e(-a/q)).       (4.4)

Thus the original diagonal and every denominator coincidence have been
retained. The coefficient of frequency zero is Z_1/2, not zero.

Write L=1+log D. By submultiplicativity of d_2 and repeated harmonic
summation,

    |Z_q|<=d_2(q)L^2/q,
    sum_(q<=D)d_2(q)^2<=sum_(q<=D)d_4(q)<=D L^3.

For the pointwise divisor inequality, each pair of two-part weak
compositions of a prime exponent is realized by at least one 2-by-2
nonnegative integer matrix with those margins. Counting these matrices
and multiplying over primes gives d_2(n)^2<=d_4(n).

Also |1-e(a/q)|>=4 min(a,q-a)/q. Consequently

    sum_(1<=a<q,(a,q)=1)|1-e(a/q)|^(-2)<=q^2/4.

For example the bound follows by summing 1/j^2<=2 over each half.
The squared mass of ALL Fourier coefficients in (4.4), including zero,
is therefore at most

    |Z_1|^2/4+(1/4)sum_(q<=D)q^2|Z_q|^2
                       <=(1/2)D L^7.                  (4.5)

### 4.2 Finite spacing, without an imported large-sieve theorem

Distinct reduced fractions with denominators at most D, including zero,
have circular distance at least D^(-2). There are at most D^2 of them.
For two such frequencies alpha,beta, geometric summation gives

    |sum_(K<=k<2K)e(k(alpha-beta))|
                  <=min(K,1/[2||alpha-beta||]).

Order the other frequencies along the two semicircles from a fixed one.
The j-th on either side is at distance at least j/D^2. Summing reciprocals
of these distances shows that every absolute row sum of this Gram matrix
is at most

    K+D^2(1+2log D)<=K+2D^2 L.

Schur's elementary inequality and (4.5) yield

    sum_(K<=k<2K)|P(k)|^2
                      <=(1/2)(K+2D^2 L)D L^7.           (4.6)

The location of the interval does not alter this estimate. No average
over a family of sources or arithmetic shifts has been inserted.

### 4.3 Restore the harmonic remainder

Since k/d>=1, equation (3.1) gives

    T(k)=P(k)/k+E(k),
    |E(k)|<=3k^(-2)sum_(d<=D)d|c(d)|
                         <=3D^2 L/K^2.

Therefore (a+b)^2<=2a^2+2b^2 and (4.6) give the more informative bound

    sum_(K<=k<2K)|T(k)|^2
       <= D L^7/K + 2D^3 L^8/K^2 +18D^4 L^2/K^3.

Because D<=K and L>=1, this is bounded by the right side of (4.1).
This proves Lemma 2, including every output cell and all coefficient
cross terms.

## 5. Complete square-step summation

Apply Lemma 2 on J_j with K=X_j, D=D_j and c=z_Y. These coefficients
are the original truncated convolution; the bound d_2 is uniform in Y.
The shortened final annulus is paid by the full positive sum in (4.1).

Put alpha=2-3rho>0. Since rho>1/2,

    D_j/X_j<=X_j^(rho-1)<=X_j^(-alpha),
    D_j^3/X_j^2<=X_j^(-alpha).

Thus each annular error is at most
42(1+log X_j)^8 X_j^(-alpha). On the strict square step X_j<b^2,
so 1+log X_j<=2(1+log b). Sum the convergent geometric series in
X_j=2^j b to obtain (1.4) with its displayed constant. No annulus,
endpoint strip, or large-product tail is omitted.

The pair-sector assertion follows from a,c<=Y: if
min(a,c)<=floor(D_j/Y), then ac<=D_j. This is an exact inclusion of
ordered native tuples, including ties, shared primes and repeated products.

## 6. Transfer to the retained coarse amplitudes

Let Pi be orthogonal projection onto block-constant vectors for ANY
partition of the complete square-step cells. Put

    S_Y=||Pi m||_2^2,
    S_Y^high=||Pi P_(Y,rho)||_2^2,
    E_Y=C_rho b^(-(2-3rho))(1+log b)^8.

Projection is contractive, so Theorem 1 gives the actual coarse-amplitude
comparison

    |sqrt(S_Y)-sqrt(S_Y^high)|<=sqrt(E_Y).                (6.1)

In particular, for any fixed eta>0,

    S_Y<=(1+eta)S_Y^high+(1+eta^(-1))E_Y.               (6.2)

The same norm comparison applies without projection to the complete
native annular energy F_N-F_Y. It would be incorrect to assert an additive
energy error E_Y alone: the mixed term with the remaining amplitude has
not been proved to vanish. Equations (6.1)--(6.2) retain its full cost.

For the annulus-respecting blocks of #974, every filtered mean is explicit.
If I=[a,a+h) lies in J_j, put

    A_d(t)=t H_floor((t-1)/d)-d floor((t-1)/d),
    L_I=(1/h)log[(a+h-1)!/(a-1)!].

Then the mean of R(k/d) over I is exactly

    [A_d(a+h)-A_d(a)]/h-L_I+log d-gamma.

Insert this expression into (1.3). It involves only old-prefix quadratic
coefficients, the two balance coordinates and products d>D_j. No future
Mobius coefficient is needed to generate these amplitudes.

## 7. Mathematical gain and remaining limit

The new result controls a complete low-product range INSIDE the arithmetic
amplitude, with a power-small complete L2 error. Its ordered-pair count is
still an asymptotically small fraction of the Y^2 input pairs. The prior compression theorem
controlled variation around block means; it did not estimate a sector of
those means. The two results can be used together through (6.1).

The quantitative gain over the elementary absolute estimate is explicit.
Since R(k/d)=O(d/k) for d<=k, summing its absolute value gives

    sum_(X<=k<2X) |sum_(d<=D)c(d)R(k/d)/d|^2
                         << D^2(1+log D)^2/X.

At D=X^rho this has a negative power only for rho<1/2. The complete
covariance estimate in Lemma 2 extends the power-small range to every
rho<2/3. It uses periodic cancellation in the kernel while retaining
the arbitrary allowed coefficients and all of their cross terms.

The kernel lemma itself does not exploit Mobius signs. It also holds for
c(d)=d_2(d). Its role is to show that the low-product oscillatory sector
is harmless once the exact native logarithmic balances have been kept.
The native inverse identity is needed to identify the output being
approximated; a general bounded-increment sequence has no such identity.

Neither B_Y nor the remaining high-product quadratic form has been
bounded here with a subquadratic power of F_Y. The required new arithmetic
cancellation therefore remains visible in (1.3); the theorem does not
infer it from a smaller list of terms. It supplies no RH conclusion.

The 2/3 cutoff comes from the elementary D^2 rational-frequency spacing
cost in (4.6). Improving it for the actual z_Y, or bounding the retained
high-product sector by a smaller native state, would require additional
arithmetic input. No such improvement is claimed. The finite Fourier and
spacing methods are classical; no general large-sieve or priority claim
is made for them.

## 8. Exact finite validation boundary

The companion checker authenticates the strict native coefficient identity,
both balance identities and the filtered reconstruction on every declared
finite cell using rational coefficients of formal logarithms and gamma.
It separately checks the periodic decomposition by rational Möbius inversion,
complete-period means and covariances, reduced-denominator grouping, and
the source tuple inclusion. Native prefixes and the comparison Möbius
array have separate constructions. Negative controls retain the zero
frequency, the logarithmic balance, the above-output products and the
strict square endpoint as mandatory gates.

These finite checks verify exact algebra and coverage. They do not prove
the infinite harmonic remainder bound or the asymptotic spacing estimate;
those have complete written proofs above. No sampled Fourier grid,
floating-point log evaluation, independent transcendental backend, full
repository audit or remote CI claim is made.

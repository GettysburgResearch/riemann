# Sparse-sign feedback: any fixed power saving suffices

Date: 2026-09-07.
Status: PROPOSED COMPLETE COMPONENT PROOFS; independent review required.
RH, any native power saving for the failure count, and unbounded-window
positivity are NOT proved. No new positive range or zero verification is claimed.
Parent: PR #803 at cdbe96a71523c81a7f50c8fe990f0f702ab49c82.
Labels SSB1--SSB7 are local, not canonical claim IDs.

## 0. What changes, and what does not

The earlier curvature argument showed that a zero of real part beta>1/2
forces a failure-count exponent at least beta. It consequently proposed a
square-root upper bound for the count. The new observation is that the
amplitude envelope can be fed back after using the count. One does NOT have
to reach the square-root counting exponent in the first place.

For the SAME actual annular scalar D and every fixed h>=0, write

  F_(r,h)(K) = #{integers k: 2<=k<=K and D(k^r)<-h}, r=1 or 2.

**SSB1.** For either r, and any fixed h>=0,

  RH  <=>  there exist delta in (0,1], C>0 such that
            F_(r,h)(K) <= C K^(1-delta) for all K>=2.       (S1)

Finite initial exceptions can be absorbed into C. In particular ANY one
fixed exponent strictly below one suffices. It need not be close to 1/2.
For r=2 these are original prime scales X=k^4, not X=k^2.

**SSB2 (dichotomy).** If RH is false, then, for both r and every fixed h>=0,

  limsup_(K->infinity) log(1+F_(r,h)(K))/log K = 1.         (S2)

There is no assumption of a rightmost zero. In contrast, if RH is true,
F_(r,h) is identically zero by the source-specific margin proved below.

A concrete, weaker-looking terminal premise is therefore

  exists delta>0,C>0: for all K>=2,
  #{2<=k<=K: B(k^2)<(135/2)k^8-240k^6} <= C K^(1-delta).  (S3)

Here B is the unchanged finite prime-power sum; (S3) counts only D(k^2)<-1.
It allows shallow failures, ignores all non-grid scales, and asks for only
one unspecified power saving. It remains RH-equivalent, not established.

The argument is an application of classical Landau positivity and
measure-theoretic oscillation ideas, combined with the actual source's
absolutely summable spectral expansion and complete sampling error. Related
supremum-of-zero-real-parts arguments already occur in Mahatab--Mukhopadhyay
[MM18, section 3.3.2]. No external novelty or priority is claimed. Our
contribution here is the source-specific feedback, sparse-grid conclusion,
and explicit separation of the hypotheses that make the feedback legitimate.

## 1. The unchanged arithmetic source

Let Lambda(p^k)=log p for all prime powers, and zero otherwise. Set a0=45/128
and, with zero endpoint values,

  w(u)=u/3-1/(192u^2),        1/4<u<=1,
       1/(3u^2)-u/192,        1<u<4,
       0,                    otherwise.

It is continuous, nonnegative, integral w=a0, and w(1/u)=u*w(u). Define

  P(X)=X^(-1/2) sum_n Lambda(n)w(n/X),
  D(m)=P(m^2)-a0*m+1/4,                 m>=2,
  B(m)=192m^3 P(m^2).                                   (1.1)

Every sum is finite, over m^2/4<n<4m^2. At the center both formulas agree.
All arithmetic includes prime powers, not primes alone. Explicitly,

  B(m)=sum_(m^2/4<n<=m^2)(64n-m^6/n^2)Lambda(n)
       +sum_(m^2<n<=4m^2)(64m^6/n^2-n)Lambda(n).

D(m)<-h is exactly B(m)<(135/2)m^4-(48+192h)m^3.
This proves the normalization of (S3).

### 1.1 The all-scale sampling bounds

These are PC1/PC2 in the locked curvature source. We repeat the essential
calculation so that its strength and limitations are visible.

The elementary prime-power Chebyshev bound psi(x)<3x follows from central
binomial prime valuations and dyadic summation. For m away from the knots,

  D'(m)=m^-2 sum_n Lambda(n)v(n/m^2)-a0,
  v(u)=-u-1/(64u^2) on (1/4,1),
       u/64+1/u^2 on (1,4),

and v is zero outside. Since |v|<=65/64, |D'|<13. Local absolute
continuity gives, for every real m,n>=2,

  |D(m)-D(n)| <= 13|m-n|.                                (1.2)

For one term f_n(m)=w(n/m^2)/m, its derivative jumps at sqrt(n)/2,
sqrt(n),2sqrt(n) are 1/(2n), -65/(32n),1/(8n). Its ordinary second
derivative is m^-3 r(n/m^2), where

  r(u)=4u-1/(32u^2) on (1/4,1),
       2/u^2-u/16 on (1,4),              |r|<=4.

After multiplication by Lambda(n), these are ALL distributional terms;
there is no delta-prime because f_n is continuous. The regular part has
absolute value <=48/m. For 2<=A<B<=2A, the entry, center and exit knot
counts on [A,B] are at most 12A(B-A)+1, 3A(B-A)+1, and
3A(B-A)/4+1, respectively. Their respective weights, before Lambda, are
at most 1/(8A^2),65/(32A^2),1/(2A^2). With ell=log(4B^2)>2 this yields

  |D''|([A,B]) <= ell[32(B-A)/A+3/A^2].                   (1.3)

Thus endpoint atoms and coincidences are paid; no convexity is assumed.
The Dirichlet Green kernel on [A,B] is nonnegative, at most (B-A)/4,
and -partial_m^2 G(m,t)=delta_t. Hence, with l the linear interpolation,

  |D(m)-l(m)| <= log(4B^2)[8(B-A)^2/A+3(B-A)/(4A^2)].      (1.4)

For A=k^2, B=(k+1)^2, integer k>=3, this implies

  D(m)>=min(D(k^2),D((k+1)^2))-45log(4(k+1)^4).            (1.5)

The same estimate bounds the error on the other side. The constants follow
from B/A<2, B-A<=7k/3, and 8*49/9+(3/4)*7/81<45. In particular, on
that cell 45log(4(k+1)^4)<=45log(64m^2).

These statements are unconditional. They give no sign, count saving,
or permission to discard a prime-power knot.

## 2. A matched spectral envelope and Mellin pole set

Let Theta=sup Re(rho), over all nontrivial zeta zeros, and set

  alpha=2Theta-1,                  0<=alpha<=1.             (2.1)

Reflection implies |Re(rho)-1/2|<=alpha/2. The supremum need not be
attained. RH is equivalent to alpha=0. Alpha is an unknown feature of
the actual spectrum, not a numerical input or a zero-free hypothesis.

Put b=3/2, d=log4, c=1/8, and

  A(z)=(1-c exp(dz))(1-c exp(-dz)),
  J(s)=integral_(1/4)^4 w(u)u^(s-1)du
      =A(s-1/2)/(9/4-(s-1/2)^2).                          (2.2)

The integral defines an entire function. The two apparent poles of the
quotient at s=-1,2 are removable. Direct integration gives the equality;
also J(1)=45/128 and J(1/2)=49/144. The factors of A show that its zeros
lie on Re(z)=+/-3/2. Consequently J(rho)!=0 for every nontrivial zeta zero.

### 2.1 Unconditional spectral representation, not a real-zero replacement

For completeness recall the exact source adapter from the annular and
height-transfer packets. Define S(x)=sum_(j>=1)exp(-(2j+1/2)x)/
((2j+1/2)^2-b^2) on x>=0, C_b=(1-gamma_E-log(2pi))/3 and
P2=-zeta'(2)/zeta(2). The even arithmetic W, on x>=0, is

  W(x)=exp(x/2)/2+C_b exp(-bx)+S(x)-(P2/b)cosh(bx)
       +(1/b)sum_(2<=n<=exp x) Lambda(n)/sqrt(n)
                                      sinh(b(x-log n)).

The fixed filter V(x)=(1+c^2)W(x)-cW(x-d)-cW(x+d) cancels P2 and
all prime powers outside the compact annulus. With

  E(X)=c S(log(X/4))+c S(log(4X))-(1+c^2)S(log X), X>=4,

one has exactly

  D(m)=1/4-E(m^2)-V(2log m),        0<=E(X)<1/10, E(X)->0. (2.3)

The prime-cusp cancellation can be checked on its four activation intervals:
(1+c^2)sinh(bu)1_(u>=0)-c sinh(b(u-d))1_(u>=d)
-c sinh(b(u+d))1_(u>=-d)=-c sinh(b(d-|u|))1_(|u|<d).
For each exponent in S, A(2j+1/2)<0, proving E>=0. The upper bound follows
from S(0)=1/6+log2/3<2/5, after dropping the negative term.

The exact Laplace adapter is

  LW(r)=[H(r)-(r/b)H(b)]/(b^2-r^2),
  H(r)=xi'(1/2+r)/xi(1/2+r),              Re r>1/2.         (2.4)

It follows termwise from the Euler-safe logarithmic derivative and digamma
partial fractions, first sufficiently far right, with the full tail P2
retained. Locally uniform source convergence and analytic continuation give
(2.4) on the stated half-plane. The apparent pole at r=b is removable.
This is the source identity proved in the locked parents, not an assertion
about an arbitrary kernel called W.

Write z_rho=rho-1/2, listing all upper-half-plane zeros with multiplicity.
The classical even Hadamard product gives

  H(r)=sum_(Im rho>0) 2r/(r^2-z_rho^2).

Indeed opposite zeros cancel their genus-one linear exponentials, and evenness
removes the remaining linear exponential. N(T)=O(T log(T+2)) implies normal
convergence. Inserting this into (2.4), taking the elementary Laplace
inverse, and then applying the fixed filter yields

  V(t)=sum_(Im rho>0) 2A(z_rho)cosh(z_rho*t)/(b^2-z_rho^2). (2.5)

This is an unconditional sum over ALL zeros, not only critical-line zeros.
An off-line quartet supplies both reflected upper zeros. On bounded t
intervals it is absolutely and uniformly convergent: |A(z_rho)|<=85/64
and |b^2-z_rho^2|>=gamma^2+2. Termwise Laplace transformation is legitimate
on Re r>1/2; uniqueness fixes equality to the arithmetic W above.
No simplicity or finite-height verification is used in (2.5).

Define the finite constant

  C_*=(85/32)sum_(Im rho>0)(gamma^2+2)^-1.

The actual value need not be known. Equations (2.1),(2.3),(2.5) imply

  |D(m)| <= 7/20+C_* m^alpha,                    m>=2.     (2.6)

More generally, if all zero real parts are at most (1+u)/2, 0<=u<=1,
then the SAME argument gives |D(m)|<=7/20+C_*m^u. Reflection is necessary
here to bound the absolute value of both horizontal deviations. This
feedback is absent from a purely local curvature argument.

### 2.2 Every positive-real-part pole survives in the arithmetic Mellin transform

For Re z>1 let F(z)=integral_2^infinity D(m)m^(-z-1)dm. Direct interchange
in the finite arithmetic source, followed by the absolutely convergent
von Mangoldt series, gives

  F(z)=-(1/2)J((z+1)/2) (zeta'/zeta)((z+1)/2) - K(z)
       -a0*2^(1-z)/(z-1)+2^(-z)/(4z),                    (2.7)

  K(z)=integral_0^2 P(m^2)m^(-z-1)dm.

K is entire, since P(m^2)=0 for m<sqrt(2)/2 and has only finitely many
terms on this compact range. It is NOT discarded. At z=1 the residue of
the first term is a0, canceled by the third term. For other positive real
z the zeta argument exceeds 1/2 and is not a zero: the alternating eta
series proves nonvanishing below one and the Euler product above one.
Thus F is meromorphic and holomorphic in a neighborhood of every real z>0.

At every nontrivial zero rho with beta>1/2, (2.7) has the genuine pole

  z_rho^*=2rho-1,
  Res_(z=z_rho^*) F(z)=-m_rho J(rho)!=0.                  (2.8)

The factor 1/2 in (2.7) and the affine derivative 1/2 cancel in this residue.
Every analytic multiplicity is retained. Consequently, if alpha>0, the
supremum of the real parts of these poles is EXACTLY alpha. There may be
no pole on the boundary line Re z=alpha. The proof below allows that case.

## 3. SSB3: Landau transfer for a sparse negative part

We use the following elementary lemma. Let f be locally integrable on
[x0,infinity), of finite polynomial growth. Suppose its Mellin transform
has a meromorphic continuation holomorphic near every real s>s0. If the
Mellin transform of f_-:=max(-f,0) converges absolutely for Re s>s0,
then the Mellin transform of f itself converges absolutely and is
holomorphic for Re s>s0.

Proof. Initially Mf_+=Mf+Mf_- sufficiently far right. The transform of the
nonnegative f_+ therefore has an analytic continuation near every real
s>s0. If its real convergence abscissa lambda were greater than s0,
Landau's theorem would make lambda a real singularity, a contradiction.
Its abscissa is finite above, or -infinity, because f has finite polynomial
growth. Thus both nonnegative parts converge on Re s>s0. Their difference
there is the continuation of Mf, proving the lemma.

Here is the Landau step, so no analytic positivity premise is hidden.
A nonnegative Mellin density becomes a nonnegative Laplace density after
x=exp t. If its finite real abscissa lambda were regular, the right half-plane
and a small disk about lambda would contain a disk centered at lambda+e
with radius greater than e. Differentiation under the integral and evaluation
of its Taylor series toward the left give a sum of NONNEGATIVE integrals.
Tonelli identifies that sum with the Laplace integral at a real point below
lambda, contradicting the definition of the abscissa. Compact initial pieces
have entire transforms and do not affect the argument. This also explains
why holomorphic continuation is not being equated with a divergent integral.

## 4. SSB4: the count lowers the possible pole boundary

Assume |D(m)|<=C_u m^u for some 0<=u<=1. Suppose for one r in {1,2},
one fixed h>=0 and some delta in (0,1],

  F_(r,h)(K)<=C K^(1-delta),                     all K>=2. (4.1)

We prove that F(z) has no pole in

  Re z > max(0,u-delta/r).                                (4.2)

### 4.1 All integer m-nodes (r=1)

Set f(m)=D(m)+h+13. If D(j)>=-h at the left integer endpoint of
[j,j+1], (1.2) gives f>=0 throughout the cell. Hence f_- is supported
in the union of cells whose left endpoints are counted by F_(1,h).
Also f_-<=D_-<=C_u m^u. On a dyadic block [T,2T], T an integer,

  integral_T^(2T) f_-(m) dm <= C' T^(u+1-delta).           (4.3)

Boundary cells change only the harmless constant. Multiplying by m^(-sigma-1)
and summing dyadic blocks proves absolute convergence for sigma>u-delta.
Extra powers of log m are summable for every strict inequality, so the
transform is holomorphic there. Its addition to F is the elementary
Mellin transform of h+13, with its only possible positive-boundary singularity
at z=0. Apply section 3 with s0=max(0,u-delta). This proves (4.2).

It is important to shift by 13: negative values can occur between successful
integer samples. The shift makes those shallow unsampled values harmless,
without canceling ANY positive-real-part pole of (2.7).

### 4.2 Square m-nodes (r=2, original prime scale X=k^4)

Start at m=9, and set

  f(m)=D(m)+h+45log(64m^2).

On [k^2,(k+1)^2], if both endpoint values are >=-h, (1.5) gives f>=0.
Its negative part is therefore supported in cells adjacent to a failing
node. On [T,2T], T>=16, each relevant cell has length at most 5sqrt(T),
and each failing node touches at most two cells. The relevant nodes satisfy
k<=2sqrt(T). Consequently the total bad-cell length is at most

  12sqrt(T) F_(2,h)(2sqrt(T)) = O(T^(1-delta/2)).           (4.4)

As before f_-<=D_-<=C_u m^u. Thus

  integral_T^(2T) f_-(m)dm = O(T^(u+1-delta/2)),            (4.5)

and its Mellin transform is holomorphic for Re z>u-delta/2.
The added logarithmic function has Mellin poles only at zero; changing the
lower limit from 2 to 9 adds an entire term. Section 3 proves (4.2) again.
The bad-cell length is not equated with the number of bad nodes: the
sqrt(T) factor in (4.4) is essential.

## 5. Closing the feedback -- not proving its counting hypothesis

By (2.8), (4.2) excludes every zero with

  Re rho > [1+max(0,u-delta/r)]/2.

The unconditional expansion (2.5), with reflection, now returns the improved
amplitude bound

  D(m)=O(m^(max(0,u-delta/r))).                            (5.1)

This implication is the feedback step. Start with u0=1 from the critical
strip. The SAME assumed count (4.1), not a sequence of new counting
hypotheses, can be used repeatedly:

  u_(n+1)=max(0,u_n-delta/r),
  u_n=max(0,1-n delta/r).                                 (5.2)

After at most ceil(r/delta) steps all zeros have real part <=1/2.
Reflection proves RH. For example a bound F_(1,0)(K)=O(K^(99/100))
suffices after 100 applications; the analogous F_(2,1) bound takes at
most 200 applications. These are finite logical deductions from an
UNPROVED counting premise, not computed zero-free strips.

There is a shorter proof that avoids even naming those steps. Suppose
alpha>0 in (2.1). Use the actual envelope u=alpha in section 4. It would
exclude all poles with real part greater than max(0,alpha-delta/r),
strictly below alpha. This contradicts their supremum alpha. No rightmost
zero is selected. This proves the forward part of SSB1.

If RH is false and the limsup in (S2) were less than one, choose a fixed
nu strictly between that limsup and one. Then F_(r,h)(K)=O(K^nu), absorbing
the finite initial segment. The just-proved implication yields a
contradiction. Since always F_(r,h)(K)<=K, its limsup exponent is exactly
one. This proves SSB2 without an arithmetic power-saving assertion.

### 5.1 The RH-side margin, and exactly which scalar check is used

Under RH, (2.5) is a positive cosine series with total mass C0=V(0).
Thus |V(t)|<=C0. Its exact source value is

  C0=47/64-(21/64)(gamma_E+log pi)+(115/96)log2
              -(641/1728)log3-(65/192)log5.

Our fresh elementary rational enclosure proves 1/25<C0<1/20. The checker
uses a Machin alternating series for pi, range-reduced atanh series for
logs, and H_1024-log1024-1/1024 < gamma_E < H_1024-log1024.
These latter bounds follow by integral comparison of the harmonic tail;
no special-function or zero oracle is imported.

With 0<=E<1/10, (2.3) gives D>1/4-1/20-1/10=1/10 for all real m>=2.
In particular F_(r,h)=0 under RH for h>=0. This completes SSB1 and the
stated dichotomy. It is conditional positivity, not a new unconditional
positive range. The analytic source adapter and the classical zeta
properties remain paper-proof dependencies, not consequences of the
scalar interval check.

## 6. SSB5: even power-sized negative excursions have full count exponent

Assume alpha>0, and fix 0<=q<alpha. Count the nodes at which
D(k^r)<-(k^r)^q. Their upper power-growth exponent in K is again one.

Proof. If their count were O(K^(1-delta)), replace the backgrounds in
section 4 by C_q m^q+13 for r=1, or C_q m^q+45log(64m^2) for r=2.
One can take C_q=4^q, since the largest endpoint in either relevant cell
is at most 4m. Good endpoints therefore imply nonnegativity of the shifted
function throughout that cell. Its negative part is still bounded by
D_-<=C m^alpha. The background has its only additional real Mellin pole
at q. The sparse-negative-part lemma now excludes poles to the right of
max(q,alpha-delta/r,0), again strictly below alpha. Contradiction.

This is stronger than the earlier count exponent >=beta from the local
negative-run estimate. It does NOT guarantee a long consecutive run at
every scale, a positive lower density, or a computable first failure.
The predecessor's run theorem remains separately useful and unchanged.

## 7. SSB6: stronger density when the spectral edge is actually attained

Here the extra hypothesis is essential to the proof. Suppose alpha>0 and
some zero has Re rho=(1+alpha)/2. Then for either r=1,2 and every fixed
h>=0 there are constants c_-,c_+>0 such that, for all sufficiently large K,

  #{2<=k<=K:D(k^r)<-h} >= c_- K,
  #{2<=k<=K:D(k^r)> h} >= c_+ K.                           (7.1)

Proof. Put t=log m and divide (2.3),(2.5) by m^alpha. Reflection and
conjugation show that the terms on the attained right edge tend to the
real trigonometric series

  g(t)=-2 Re sum_(beta=(1+alpha)/2, gamma>0)
            m_rho J(rho) exp(2i gamma t).                  (7.2)

Every other exponential has a strictly smaller real exponent and tends to
zero. The full coefficients are absolutely summable, so dominated
convergence gives

  m^-alpha D(m)-g(log m) -> 0.                             (7.3)

This is valid even if non-edge zeros approach the edge arbitrarily closely;
no spectral gap or convergence rate is asserted. The multiplicities in
(7.2) are retained. Its distinct nonzero-frequency coefficients are nonzero
because J(rho)!=0. Averaging against one such frequency recovers its
coefficient by absolute convergence, so g is not identically zero. Its
ordinary time mean is zero, by the same argument without modulation.

The series is uniformly almost periodic. Here is the needed recurrence
fact without assuming independence of ordinates. Approximate it uniformly
by a finite trigonometric sum. The orbit of its phase vector has compact
closure in a finite torus. Translates of any neighborhood of the identity
cover that closure; compactness selects finitely many orbit translates.
It follows that return times to that neighborhood are relatively dense.
Those return times are uniformly small translation errors for the finite
sum, and hence for g after paying the absolute tail.

A nonzero, nonnegative uniformly almost-periodic function cannot have
mean zero: a positive interval recurs with bounded gaps, forcing a positive
mean. The same holds for a nonpositive function. Thus g has a positive
interval and a negative interval, with fixed strict margins, and both
kinds recur with bounded gaps in t.

For each sufficiently large K, choose a negative interval of length l>0
within [r log K-T,r log K] where T is a fixed sufficiently large recurrence
length. Its exponential image under k=exp(t/r) lies below K and contains
at least c K integers for a fixed c>0. Equation (7.3) makes D(k^r)<-h
on it once K is large. The positive interval works in the same way.
This proves (7.1). Constants depend on the full edge series and are not
numerically certified. No simplicity or linear independence was used.

Without an attained edge the dominated limit in (7.3) is zero, and this
proof does NOT give (7.1). The unconditional false-RH conclusion is (S2),
not a lower density or a lower count exponent.

## 8. Why this does not complete the requested arithmetic estimate

The old fixed even moments include harmless critical-line oscillations and
can grow at full exponent one even under RH. This result does not estimate
those moments. It uses only the negative part after a harmless background
shift, and feeds its support information into the actual spectral envelope.

Neither positivity of w, psi(x)<3x, the full divisor identity, nor the
successful finite range proves F_(r,h)=O(K^(1-delta)). Our direct attempt
to sum the centered deficit over its unknown failing set produces the
same signed prime correlations, with a source-dependent selector. Taking
absolute values still loses the needed cancellation. No new unconditional
sublinear count upper bound was obtained in this pass.

A bound K/log K, or an arbitrary density-one success assertion, has exponent
one and does not satisfy (S1). We do not claim such information can never
suffice with additional source structure. Small counts on an arbitrarily
sparse subsequence also do not give the all-K power envelope in (S1).

The precise new first open theorem can be (S3), with ANY one fixed delta>0.
For example exponent 999/1000 would suffice; that exponent is an example
of the allowed hypothesis, not a proved estimate. The completed arguments
remove the unnecessary square-root target and shallow failures; they do
not create a power saving or establish RH.

## 9. Dependencies and checking boundary

The bound and meromorphic poles are properties of the same actual source.
One cannot replace (2.5) by a positive surrogate, normalize using a
hypothetical rightmost zero, or use the false-RH conclusion (S2) as an
unconditional failure-count bound. All sums include analytic multiplicity.

Source SHA/path bindings are in SOURCE_LOCK.json. The three imported
manuscripts are authenticated as bytes and their used analytic identities
are reconstructed above. This is an author continuation, not an independent
acceptance of the parent proofs or this one. No parent numerical suite is
rerun. The fresh scalar enclosure and bounded exact tests check constants,
finite identities, residue normalization, sparse-cell geometry and iteration
arithmetic only. They cannot machine-prove Landau's theorem, the infinite
Hadamard expansion, the unknown spectral edge, or (S1)'s missing premise.

See SOURCES_AND_SYNTHESIS.md for primary-source prior art and the exact
external reading boundary, and VALIDATION.md for what was actually executed.

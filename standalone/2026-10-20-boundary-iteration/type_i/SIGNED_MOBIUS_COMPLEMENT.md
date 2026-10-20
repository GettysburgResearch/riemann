# An exact signed Möbius-complement factorization

20 October 2026. **Status: conditional proper-complement estimate.**
This note preserves the signs in the exact reflected expression.
It does not bound its surviving full-divisor term or solve the
prime-restricted Type-III problem.

The arithmetic interface is COHERENT_TYPE_III_INTERFACE.md,
SHA256 07f5ae784686e8ee74d6b3253a5a4a9fa55f492cd7917e1d952e23fdd1f96bd9,
especially (T4)--(T6). The analytic premise and conductor-uniform
reciprocal theorem are those of
../uniform/UNIFORM_INVERSE_AND_STRIPPING.md,
SHA256 fcee7547018c62c5a54c273501b7f2032a93b3633b5b04b3cdce90fdc1015c12.

## 1. The actual signed complementary coefficients

Take the outer coefficient \(a_r=\mu_E(r)\) in (T5). For squarefree
\(r=km\), with \((k,m)=1\), it factors as \(\mu_E(k)\mu_E(m)\).
After separating a fixed primary ray character \(\varphi\) from
the finite reflection matrix, the complementary sum is
\[
 \mathcal C_{k,\varphi}(M;s,\ell)
 =\sum_{\substack{m\ {\rm primary}\\(m,3k)=1}}
   \mu_E(m)\varphi(m)(Nm)^{1/2-2s}
   \prod_{\mathfrak p\mid m}
     \{q^{3s-3/2}-\alpha(\mathfrak p)^{3\ell}\}
                         W(Nm/M).
\tag{MC1}
\]
Here \(W\) is fixed, smooth, and compactly supported in
\((0,\infty)\), \(\ell\ne0\), and \(M\ge1\).
The squarefree support is supplied by \(\mu_E\).
All primes excluded by the fixed ray character or the original
source conventions are also omitted.

At a prime the signed coefficient, including its norm weight, is
\[
 \varphi(\mathfrak p)\alpha(\mathfrak p)^{3\ell}q^{1/2-2s}
                    -\varphi(\mathfrak p)q^{s-1}.
\tag{MC2}
\]
Consequently its Dirichlet series in \(w\) has exact local factor
\(1+x-y\), where
\[
 a=w+2s-\tfrac12,\qquad b=w+1-s,\qquad
 x=(\varphi\alpha^{3\ell})(\mathfrak p)q^{-a},
 \quad y=\varphi(\mathfrak p)q^{-b}.
\tag{MC3}
\]

## 2. A factorization extending past the absolute square threshold

Use the elementary identity
\[
 1+x-y=(1+x)(1-y)
             \left(1+\frac{xy}{(1+x)(1-y)}\right).
\tag{MC4}
\]
Writing a superscript \((k)\) for the retained common-prime
deletions, the exact Euler product is
\[
 \boxed{\displaystyle
 \mathcal F_{k,\varphi}(w;s,\ell)
 =
 \frac{L_E^{(k)}(a,\varphi\alpha^{3\ell})}
 {L_E^{(k)}(2a,\varphi^2\alpha^{6\ell})
  L_E^{(k)}(b,\varphi)}
              \mathcal E_{k,\varphi}(w;s,\ell).}
\tag{MC5}
\]
The local factors of \(\mathcal E\) are those in parentheses
in (MC4). They converge absolutely and locally uniformly whenever
\[
          \Re a>0,\qquad \Re b>0,\qquad \Re(a+b)>1.
\tag{MC6}
\]
Indeed \(|1+x|\ge1-q^{-\Re a}\) and
\(|1-y|\ge1-q^{-\Re b}\), while the numerator of the error has
magnitude \(q^{-\Re(a+b)}\).
This convergence does not require \(2\Re a>1\).
The reciprocal of \(L(2a,\varphi^2\alpha^{6\ell})\) keeps the
square term that would otherwise obstruct that continuation.

Define \(\mathcal E\) directly over primes not dividing \(k\).
Its bound on compact substrips of (MC6) is uniform in \(k\).
The deleted Euler factors of the three Hecke functions cost
\((Nk)^\epsilon\) for any \(\epsilon>0\).
There is no division by \(1+x-y\), which could vanish.
Both factors \(1+x\) and \(1-y\) are nonzero in (MC6).

## 3. Smooth cancellation from the common unitary premise

Assume a common zero-free half-plane
\[
          L_E(z,\chi)\ne0\qquad(\Re z>\beta),
             \qquad \tfrac12\le\beta<1,
\tag{MC7}
\]
for the actual unitary Hecke characters in (MC5), including
\(\varphi^2\alpha^{6\ell}\) and \(\varphi\).
The full unitary family premise is sufficient.
Put
\[
 s=\tfrac12-\delta+it,\qquad 0<\delta<\tfrac14.
\]
The numerator in (MC5) has nonzero angular degree and hence no
principal or translated principal pole. Conditions (MC6)--(MC7)
permit Mellin contour shifting to any fixed line
\[
 \Re w>\tau_\beta(\delta),\qquad
 \tau_\beta(\delta)=
 \max\left\{
      \frac{\beta}{2}-\frac12+2\delta,\
      \beta-\frac12-\delta,\
      \frac{\delta}{2}\right\}.
\tag{MC8}
\]
The first condition makes \(2\Re a>\beta\), the second
\(\Re b>\beta\), and the third \(\Re(a+b)>1\).
Moreover \(\Re a>0\) follows since
\(\Re a>\tfrac12-\tfrac32\delta>1/8\); \(\Re b>0\)
also follows.

Apply the uniform reciprocal estimates to the two denominators,
and the ordinary Hecke polynomial strip bound to the numerator.
All finite conductors here are fixed apart from the deleted
primes; their archimedean conductors are polynomial in
\(1+|\ell|+|t|+|\Im w|\).
Rapid Mellin decay of \(W\), using a fixed number of derivatives,
then gives
\[
 \boxed{\displaystyle
 |\mathcal C_{k,\varphi}(M;\tfrac12-\delta+it,\ell)|
 \ll_{\delta,\beta,\epsilon,W}
   (Nk)^\epsilon(1+|\ell|+|t|)^C
                     M^{\tau_\beta(\delta)+\epsilon}.}
\tag{MC9}
\]
Here \(C\) is a fixed finite degree depending on the indicated
strip; no subpower numerator bound is asserted.
All contour gaps are chosen positive before fixing constants.
The original Mellin integral starts far enough right for
absolute convergence, so (MC5) continues the actual signed sum.

Fixed powers of \(\log Nm\) or \(\log Nk\) can be included by
Mellin differentiation and expanding the logarithm of \(N(km)\).
Cauchy estimates on a slightly wider permitted strip handle
those fixed derivatives. An arbitrary coefficient sequence
depending on \(m\) cannot be inserted into (MC9).

For comparison, summing (MC2) in absolute value gives at best the
scale \(M^{1/2+2\delta+\epsilon}\).
Every exponent in (MC8) is strictly smaller than
\(1/2+2\delta\) for \(\beta<1\) and \(0<\delta<1/4\).
Thus (MC9) is a strict gain for this particular smooth signed
complementary factor.

## 4. Optimizing this isolated exponent and its exact limitation

For \(2/3\le\beta<1\), the first two affine expressions in (MC8)
meet at \(\delta=\beta/6\). There the third is no larger, and
\[
             \min_{0<\delta<1/4}\tau_\beta(\delta)
                         =\frac{5\beta}{6}-\frac12.
\tag{MC10}
\]
For \(1/2<\beta\le2/3\), the second and third expressions meet at
\(\delta=(2\beta-1)/3\); the first is then no larger, and
\[
             \min_{0<\delta<1/4}\tau_\beta(\delta)
                         =\frac{2\beta-1}{6}.
\tag{MC11}
\]
At \(\beta=1/2\) the corresponding infimum is zero, approached
as \(\delta\) tends to zero from the right.
These are elementary optimizations of this isolated factor,
not of the full reflected bilinear form.

At the candidate \(\beta=B_\flat\), (MC10) is approximately
\(0.229072205866637\), with
\(\delta\approx0.145814441173327\).
This substitution remains conditional on (MC7).

The full expression (T5) still contains the \(k\)-sum, its
Gauss coefficient, the reflected completed series, gamma factors,
and exact finite matrices. In particular \(k=r\) means \(m=1\);
then (MC1) has no long complementary sum and (MC9) supplies no
cancellation. The surviving term (T6) is unchanged.
Furthermore an actual three-prime restriction must be opened
through a valid prime-detection identity before these complete
theta reflections apply. Neither issue is resolved by (MC5).
No strict Type-III exponent, numerical zero-free improvement,
or RH assertion follows from this note alone.

## 5. A coherent free-inner transformed-tail consequence

Combining the preceding factorization with the cubic mean gives
one additional, explicitly restricted consumer. This consequence
was derived jointly within the current research packet.
Consider the complete free-inner expression
\[
 \mathcal F_s(R)=\sum_{r\ {\rm primary}}^{*}
    \mu_E(r)\widetilde g(r)\alpha(r)^\ell
                       f(Nr/R)Q_r(s;\ell),
\tag{MC12}
\]
where \(f\) is fixed smooth and supported on a compact annulus.
This is a completed theta expression, not a prime-restricted
inner series. Apply the exact reflection and retain all finite
profile components and their common gamma factors.
In one reflected dyad \(Nk\asymp K\), \(Nm\asymp M\), with
\(KM\asymp R\), (T5) and (MC9) give
\[
 \begin{split}
 |\text{dyad}|
 &\ll R^\epsilon(1+|\ell|+|t|)^C
          K^\delta M^{\tau_\beta(\delta)+\epsilon}
               \sum_{Nk\asymp K}^{*}
                       |Q_{k,\kappa}(1/2+\delta-it;-\ell)|\\
 &\ll R^\epsilon(1+|\ell|+|t|)^C
          K^{1+\delta}M^{\tau_\beta(\delta)}.
 \end{split}
\tag{MC13}
\]
The last step is Cauchy--Schwarz and the new pure cubic mean.
The angular and height factors, including the gamma quotient, are
absorbed into the displayed fixed polynomial. Each finite ray
factor separates across \(r=km\). For each fixed \(k\), the weight
\(f(NkNm/R)\) is a smooth weight at scale \(R/Nk\) with uniformly
bounded normalized seminorms. A smooth dyadic partition in \(m\)
therefore satisfies exactly the hypotheses of (MC9).

Define the transformed tail to consist of the exact reflected
terms with complementary dyads \(M\ge M_0\ge2\).
Since \(\tau_\beta(\delta)<1+\delta\), summing (MC13) yields
\[
 |\text{transformed tail with }M\ge M_0|
 \ll R^{1+\delta+\epsilon}(1+|\ell|+|t|)^C
                   M_0^{-(1+\delta-\tau_\beta(\delta))}.
\tag{MC14}
\]
For \(\beta\ge2/3\) and \(\delta=\beta/6\), its saving exponent is
\[
       1+\delta-\tau_\beta(\delta)
                         =\frac32-\frac{2\beta}{3}.
\tag{MC15}
\]
The unsaved \(m=1\) term and the bounded-\(m\) terms still remain
in (MC12). The direct Cauchy bound for the full expression has
scale \(R^{1+\delta+\epsilon}\), so (MC14) is a strict estimate
for a proper part of its reflected decomposition.

The cutoff in (MC14) is imposed after exact reflection as a
smooth dyadic restriction on the complementary variable.
A new roughness restriction on the original row \(r\), or an
arbitrary prime-detection coefficient replacing \(\mu_E(r)\),
does not automatically preserve (MC9). Such a restriction changes
the complementary Euler product, and its additional conductor
or truncated-prime costs require a separate argument.

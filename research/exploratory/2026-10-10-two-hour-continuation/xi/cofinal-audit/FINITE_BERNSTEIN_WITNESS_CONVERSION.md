# Explicit finite conversion from a negative Hankel form to a mixed moment

Status: complete proposed analytic finite-witness conversion. No actual-Xi
negative form or mixed witness is supplied.
Scope: the complete shifted native moment functional; an explicit finite
diagonal of mixed Hausdorff differences, with an order bound depending on
the negative quadratic margin and the rational polynomial coefficients.
Exact dependencies: the complete shifted normalization in
[HAUSDORFF_LOG_MOMENT_CRITERION.md](HAUSDORFF_LOG_MOMENT_CRITERION.md), SHA256
`4f72ef0b7685bd0346f9c0d61b54819a2c7462de78d9620473cf07383ec9c54f`,
and the elementary binomial factorial-moment identity proved below.
The off-real application additionally uses the complete shifted finite
filter in [CONSTRUCTIVE_FINITE_HANKEL_WITNESS.md](CONSTRUCTIVE_FINITE_HANKEL_WITNESS.md),
SHA256 `396f428d865c5bda2a67c141673700b29c48b08d776e7e3ea4f46e0d2f336513`.
What was actually run: analytic derivation only; no coefficient enumeration.
Smallest remaining gap for RH: establish actual complete positivity, rather
than assume a negative witness or infer all orders from a finite positive set.

## BC1. Exact normalized complete functional

Fix `t>A>=0`, put `L=1/(t^2-A^2)`, and retain all positive-real-part source
occurrences with multiplicity. Write

\[
 \lambda_\rho=(\rho^2+t^2)^{-1},\qquad s_\rho=\lambda_\rho/L,
 \qquad b_n=\sum_\rho m_\rho\lambda_\rho s_\rho^n,
 \qquad \mathcal B(Q)=\sum_\rho m_\rho\lambda_\rho Q(s_\rho).
 \tag{BC1}
\]

Complete summability and `|s_rho|<=1` make every displayed polynomial sum
absolutely convergent. Conjugate grouping makes it real for real Q. Define

\[
 D_{n,j}=\sum_{h=0}^j(-1)^h{j\choose h}b_{n+h}
       =\mathcal B(s^n(1-s)^j).
 \tag{BC2}
\]

Let P be any real polynomial of degree d such that

\[
                 \mathcal B(P^2)=-\eta<0.
 \tag{BC3}
\]

This is a contraction of the finite complete normalized Hankel matrix
`(b_(i+j))_(0<=i,j<=d)`. It retains all unknown source occurrences. Choose
any `epsilon>0` satisfying

\[
        \epsilon\le\frac{\eta}{2(1+|b_0|)},
 \qquad Q(s)=P(s)^2+\epsilon=\sum_{i=0}^{2d}q_i s^i.
 \tag{BC4}
\]

Then Q is at least epsilon on the REAL interval `[0,1]`, and
`B(Q)=-eta+epsilon b_0<-eta/2`. No positivity of b0 is assumed. If a native
negative contraction has strict lower margin eta0 and a finite upper bound
B0 for `|b0|`, a rational `0<epsilon<=eta0/(2(1+B0))` suffices.

## BC2. Exact nonnegative Bernstein coefficients at a finite degree

For an integer `N>=2d`, put

\[
 c_\ell^{(N)}=\sum_{i=0}^{2d}q_i
                         \frac{(\ell)_i}{(N)_i},\qquad 0\le\ell\le N,
 \quad (a)_i=a(a-1)\cdots(a-i+1),\quad(a)_0=1.
 \tag{BC5}
\]

The ratio is zero when `ell<i`. The binomial factorial identity is

\[
 s^i=\sum_{\ell=0}^N\frac{(\ell)_i}{(N)_i}
                       {N\choose\ell}s^\ell(1-s)^{N-\ell}.
 \tag{BC6}
\]

To prove it, use
`(ell)_i binom(N,ell)=(N)_i binom(N-i,ell-i)`, factor out `s^i`, and apply
the binomial theorem. BC6 is a POLYNOMIAL identity on the whole complex
plane, not an approximation that requires the source nodes to be real.
Thus

\[
 Q(s)=\sum_{\ell=0}^N c_\ell^{(N)}{N\choose\ell}
                                      s^\ell(1-s)^{N-\ell}.
 \tag{BC7}
\]

Sampling i times with and without replacement from N items, ell of which
are marked, gives the elementary uniform coupling bound

\[
 \left|\frac{(\ell)_i}{(N)_i}-(\ell/N)^i\right|
                  \le\frac{i(i-1)}{2N}.
 \tag{BC8}
\]

The two experiments agree unless at least two draws coincide; the union
bound pays the right side. It is valid for every ell, including ell<i.
For i=0 and i=1 the difference is exactly zero. Define the finite exact
coefficient price

\[
                  C_Q=\sum_{i=2}^{2d}|q_i|\frac{i(i-1)}2.
 \tag{BC9}
\]

Choose an integer

\[
            N\ge\max\{1,2d,\lceil2C_Q/\epsilon\rceil\}.
 \tag{BC10}
\]

Equations BC8–BC10 imply
`|c_ell^(N)-Q(ell/N)|<=C_Q/N<=epsilon/2`, and hence

\[
                        c_\ell^{(N)}\ge\epsilon/2>0
                         \quad(0\le\ell\le N).
 \tag{BC11}
\]

This is complete finite coefficient coverage by a uniform theorem. It does
not require an enumeration of N+1 coefficients and does not use convergence
of Bernstein approximations at complex nodes. The representation is exact.

## BC3. Some mixed difference on one explicit finite diagonal is negative

Apply the complete functional to the exact polynomial identity BC7:

\[
 \mathcal B(Q)=\sum_{\ell=0}^N c_\ell^{(N)}{N\choose\ell}
                                      D_{\ell,N-\ell}<-\eta/2.
 \tag{BC12}
\]

Every coefficient of this finite combination is strictly positive by BC11.
Therefore at least one complete mixed moment on the single finite diagonal
`n+j=N` is strictly negative. More quantitatively, evaluating BC7 at 1/2
gives the sum of the positive weights,

\[
 W=\sum_{\ell=0}^N c_\ell^{(N)}{N\choose\ell}
            =2^N Q(1/2)>0,
 \qquad \min_{0\le\ell\le N}D_{\ell,N-\ell}
                   <-\frac\eta{2W}.
 \tag{BC13}
\]

If P and epsilon have rational coefficients then N, all c coefficients
and W are exact finite rational data. An authenticated negative native
Hankel contraction consequently gives an explicit finite search diagonal
and a strict witness margin. The sufficient N can be very large, and the
margin may be exponentially small in N. No efficiency claim is made.

## BC4. Source and quantifier boundaries

The shifted finite-filter theorem supplies BC3 whenever an off-real source
node exists. Scaling its real polynomial by `lambda=L*s` produces precisely
the normalized functional BC1. Rational approximation preserves its strict
negative margin, so BC10 gives a concrete finite mixed-witness order once
that finite contraction is authenticated. This strengthens the existential
Hausdorff refutation statement without asserting an actual negative source
coefficient.

All complete mixed inequalities nonnegative would contradict BC12 for any
negative Hankel form. Conversely, a real spectrum makes every normalized
node belong to `(0,1)` and every weight positive, so both the Hankel and
mixed inequalities hold. With the complete strip, product summability and
imaginary-axis exclusion, the all-order Hankel and Hausdorff criteria are
therefore equivalent real-location conditions, allowing multiplicities.

The native 528 mixed tests and finite analytic rectangles supply only finite
subsets of the required mixed family. BC10 does not bound a hypothetical
negative witness solely from the census height: it also requires a negative
polynomial, its margin and coefficient price. The positive-Fourier
countermodel with arbitrarily late off-real roots shows why those missing
data cannot be inferred from finite head information alone.

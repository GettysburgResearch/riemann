# Prefix truncation moves the rough-source frontier to \(y=(\log X)^{2+o(1)}\)

Status: **exact prefix-truncated conditioning, a sharp Rankin--PNT
subpower frontier at \(y\le (\log X)^{2+o(1)}\), and an enlarged
rough-critical-lattice RH equivalence; no rough-source cancellation,
Möbius estimate, RH, or GRH theorem**

Bounded replay:
[ffps_prefix_truncated_rough_rankin_frontier.py](ffps_prefix_truncated_rough_rankin_frontier.py).
Canonical summary:
[ffps_prefix_truncated_rough_rankin_frontier.json](ffps_prefix_truncated_rough_rankin_frontier.json).

Frozen predecessor: commit
`1e0c42aaf3f35a90af52380a32bbf7d8da0d5be5`, document blob
`7f909b9a474ef3418ef79ecf98170c8bdc7f7f90`, and producer blob
`2c9b40bc95dd090682449124c2873af9bcfebdbf`.

One classical analytic input is used: the prime number theorem and partial
summation.  In particular, \(\pi(y)\sim y/\log y\), and uniformly for
\(a\) in compact subintervals of \((0,1)\),

\[
 \sum_{p\le y}p^{-a}
 \ll {y^{1-a}\over(1-a)\log y}.
\tag{0.1}
\]

These inputs are not proved by the bounded replay.

## 0. Outcome

The predecessor bounded the rough-source scale transforms by the complete
Euler products

\[
 \prod_{p\le y}(1+p^{-1/2}),
 \qquad
 \prod_{p\le y}(1-p^{-1/2})^{-1}.
\tag{0.2}
\]

Those products include dilations which cannot occur at a prefix \(Y\le X\).
Every actual forward term has \(d\le Y\), and every inverse term has the
same restriction.  Retaining it gives the smaller coefficient masses

\[
\begin{aligned}
 C_{\rm sf}(X,y)
 &=\sum_{\substack{d\le X\\d\mid P(y)}}d^{-1/2},\\
 C_{\rm sm}(X,y)
 &=\sum_{\substack{d\le X\\P^+(d)\le y}}d^{-1/2},
\end{aligned}
\tag{0.3}
\]

where \(P(y)=\prod_{p\le y}p\), \(P^+(1)=1\), `sf` means squarefree
\(y\)-smooth, and `sm` means unrestricted \(y\)-smooth.

For every positive Fourier measure \(\nu\), the exact maximal-prefix
conditioning improves to

\[
\boxed{
 C_{\rm sm}(X,y)^{-1}\mathfrak A_{y,\nu}(X)
 \le \mathfrak M_\nu(X)
 \le C_{\rm sf}(X,y)\mathfrak A_{y,\nu}(X).}
\tag{0.4}
\]

For the literal duplicate-\(67\) source \(D\),

\[
\boxed{
 (1-67^{-1/2})C_{\rm sm}(X,y)^{-1}\mathfrak A_{y,\nu}(X)
 \le \mathfrak D_\nu(X)
 \le (1+67^{-1/2})C_{\rm sf}(X,y)\mathfrak A_{y,\nu}(X).}
\tag{0.5}
\]

For every \(0<\sigma<1/2\), Rankin's trick gives

\[
\boxed{
\begin{aligned}
 C_{\rm sf}(X,y)
 &\le X^\sigma\prod_{p\le y}(1+p^{-1/2-\sigma}),\\
 C_{\rm sm}(X,y)
 &\le X^\sigma\prod_{p\le y}(1-p^{-1/2-\sigma})^{-1}.
\end{aligned}}
\tag{0.6}
\]

Combining (0.1) and (0.6) yields the common logarithmic envelope

\[
 \log C_{\bullet}(X,y)
 \le \sigma\log X
 +O\!\left(
 {y^{1/2-\sigma}\over(1/2-\sigma)\log y}
 +\log\log y
 \right),
\tag{0.7}
\]

where \(C_\bullet\) denotes either mass.

The exact new frontier (with \(y(X)\to\infty\)) is

\[
\boxed{
 \log y(X)\le(2+o(1))\log\log X.}
\tag{0.8}
\]

Equivalently, \(y(X)\le(\log X)^{2+o(1)}\).  In this whole range one can
choose \(\sigma=o(1)\) in (0.7), and therefore

\[
\boxed{C_{\rm sf}(X,y),\ C_{\rm sm}(X,y)=X^{o(1)}.}
\tag{0.9}
\]

Conversely, if (0.8) fails, the squarefree mass alone has a fixed positive
power along a subsequence.  Thus

\[
\boxed{
 C_{\rm sf}(X,y),\ C_{\rm sm}(X,y)=X^{o(1)}
 \quad\Longleftrightarrow\quad
 \log y\le(2+o(1))\log\log X.}
\tag{0.9a}
\]

Consequently, for the retained critical Fourier lattice \(\lambda_X\) of
the frozen predecessor,

\[
\boxed{
 \mathrm {RH}
 \Longleftrightarrow
 \sup_{1\le Y\le X}
 \|A_{y(X),Y}\|_{L^2(\lambda_X)}^2=X^{o(1)}}
\tag{0.10}
\]

throughout (0.8).

This strictly enlarges the earlier absolute-Neumann range.  In particular,
for every fixed real \(B\),

\[
 y=(\log X)^2(\log\log X)^B
\tag{0.11}
\]

is now admissible.  The predecessor reached only \(B<2\) by discarding the
prefix cutoff; when \(B=2\), its complete Euler products cost
\(X^{1+o(1)}\) in norm and \(X^{2+o(1)}\) after squaring.  The actual
prefix-truncated masses remain subpower for every fixed \(B\).

For comparison, if \(y=(\log X)^A\) with fixed \(A>2\), matching Rankin
upper and squarefree-binomial lower bounds give

\[
 \boxed{
 C_{\rm sf}(X,y),\ C_{\rm sm}(X,y)
 =X^{1/2-1/A+o(1)}.}
\tag{0.12}
\]

This is an asymptotic for the two positive coefficient masses.  It is not
a lower bound for a signed operator and not a no-go for cancellation in the
native scale transform.

## 1. Exact prefix-truncated conditioning

Write \(s=1/2+it\) and use the frozen prefixes

\[
\begin{aligned}
 M_Y(t)&=\sum_{n\le Y}{\mu(n)\over n^s},\\
 D_Y(t)&=\sum_{n\le Y}{\beta(n)\over n^s},\\
 A_{y,Y}(t)&=
 \sum_{\substack{n\le Y\\(n,P(y))=1}}{\mu(n)\over n^s}.
\end{aligned}
\tag{1.1}
\]

The exact scale identities are

\[
\begin{aligned}
 M_Y(t)
 &=\sum_{\substack{d\mid P(y)\\d\le Y}}
 {\mu(d)\over d^s}A_{y,Y/d}(t),\\
 A_{y,Y}(t)
 &=\sum_{\substack{d\le Y\\P^+(d)\le y}}
 {1\over d^s}M_{Y/d}(t),\\
 D_Y(t)&=M_Y(t)-67^{-s}M_{Y/67}(t),\\
 M_Y(t)&=\sum_{\substack{j\ge0\\67^j\le Y}}
 67^{-js}D_{Y/67^j}(t).
\end{aligned}
\tag{1.2}
\]

Every sum is finite at the displayed prefix.  Let

\[
 \mathfrak F_\nu(X)=
 \sup_{1\le Y\le X}\|F_Y\|_{L^2(\nu)}.
\tag{1.3}
\]

Minkowski and \(|d^{-it}|=1\) give

\[
 \mathfrak M_\nu(X)
 \le C_{\rm sf}(X,y)\mathfrak A_{y,\nu}(X),
 \qquad
 \mathfrak A_{y,\nu}(X)
 \le C_{\rm sm}(X,y)\mathfrak M_\nu(X).
\tag{1.4}
\]

The two duplicate-\(67\) identities similarly give

\[
 \mathfrak D_\nu(X)
 \le(1+67^{-1/2})\mathfrak M_\nu(X),
 \qquad
 \mathfrak M_\nu(X)
 \le(1-67^{-1/2})^{-1}\mathfrak D_\nu(X).
\tag{1.5}
\]

Combining (1.4)--(1.5) proves (0.4)--(0.5).  No positivity of the source
coefficients is used.  Positivity is required only of the measure so that
\(L^2(\nu)\) is a norm and Minkowski applies.

The cutoff \(d\le X\) is load-bearing.  Replacing the two sums in (0.3) by
their complete Euler products recovers the predecessor's weaker constants.

## 2. Rankin envelope

For \(d\le X\) and \(\sigma>0\),

\[
 1\le(X/d)^\sigma.
\tag{2.1}
\]

Inserting (2.1), then completing the nonnegative sums, proves (0.6).  Put
\(a=1/2+\sigma\).  The squarefree product satisfies

\[
 \log\prod_{p\le y}(1+p^{-a})
 \le\sum_{p\le y}p^{-a}.
\tag{2.2}
\]

For the smooth product,

\[
 -\log(1-p^{-a})
 =p^{-a}+O(p^{-2a}),
\tag{2.3}
\]

uniformly for \(a\ge1/2\).  The accumulated remainder is
\(O(\log\log y)\).  Applying (0.1) to the first-order term gives (0.7).

### The \((\log X)^{2+o(1)}\) choice

Put \(L=\log X\), \(\ell=\log L\), and

\[
 \eta=\log y-2\ell.
\tag{2.4}
\]

Under (0.8), \(\eta_+=o(\ell)\).  Choose

\[
 \sigma_X=
 \max\left(0,{\eta/2+2\log\ell\over\log y}\right).
\tag{2.5}
\]

Then \(\sigma_X=o(1)\).  If the maximum is positive,

\[
 y^{1/2-\sigma_X}={L\over\ell^2};
\tag{2.6}
\]

if it is zero, the left side is at most the same quantity.  Hence both
terms on the right of (0.7) are \(o(L)\), proving (0.9).

Formula (2.5) is a proof device, not a new detector parameter.  The rough
source and the critical bandpass kernel remain exactly those of the frozen
predecessor.

### Sharpness of the exponent-two frontier

Suppose (0.8) fails.  Along a subsequence there is an \(\epsilon>0\) such
that, with \(V=\log y\),

\[
 V\ge(2+\epsilon)\ell.
\tag{2.7}
\]

First assume \(V=o(L)\), and put \(k=\lfloor L/V\rfloor\) and
\(N=\pi(y)\).  Every product of \(k\) distinct primes at most \(y\) is at
most \(y^k\le X\), so all of them occur in the squarefree mass.  Each has
weight at least \(X^{-1/2}\).  The PNT and the elementary binomial estimate
therefore give

\[
\begin{aligned}
 \log C_{\rm sf}(X,y)
 &\ge \log {N\choose k}-{L\over2}\\
 &=L\left({1\over2}-{\ell\over V}\right)+o(L).
\end{aligned}
\tag{2.8}
\]

Under (2.7), the coefficient is at least
\(\epsilon/(2(2+\epsilon))+o(1)\).  If \(V\) is not \(o(L)\), choose a
fixed \(\theta>0\) along a subsequence with \(X^\theta\le y\).  The
one-prime terms alone give

\[
 C_{\rm sf}(X,y)
 \ge\sum_{p\le X^\theta}p^{-1/2}
 =X^{\theta/2+o(1)}.
\tag{2.9}
\]

Since \(C_{\rm sm}\ge C_{\rm sf}\), this proves the reverse implication in
(0.9a).  It also shows that the frontier is a property of the positive
coefficient mass itself, not merely a weakness of the Rankin upper bound.

### Fixed polylogarithmic powers beyond two

Let \(y=L^A\), \(A>2\) fixed.  Choosing

\[
 \sigma=
 {1\over2}-{1\over A}
 +{2\log\ell\over A\ell}
\tag{2.10}
\]

makes \(y^{1/2-\sigma}=L/\ell^2\), so (0.7) proves the upper bound in
(0.12).  Formula (2.8), now with \(V=A\ell\), gives the matching lower
bound for \(C_{\rm sf}\), and \(C_{\rm sm}\ge C_{\rm sf}\).  This proves
(0.12).  It still says nothing about cancellation in (1.2).

## 3. Enlarged RH-equivalent rough target

The frozen predecessor proves

\[
 \mathrm {RH}
 \Longleftrightarrow
 \mathfrak D_{\lambda_X}(X)^2=X^{o(1)}.
\tag{3.1}
\]

Equations (0.5) and (0.9) show that, in the range (0.8),

\[
 \mathfrak D_{\lambda_X}(X)=X^{o(1)}
 \Longleftrightarrow
 \mathfrak A_{y(X),\lambda_X}(X)=X^{o(1)}.
\tag{3.2}
\]

Squaring preserves subpower size, proving (0.10).

The maximal prefix remains essential: the exact inverse calls
\(D_{Y/(67^jd)}\) or \(M_{Y/d}\) at many smaller endpoints.  No claim is
made that the isolated endpoint \(A_{y(X),X}\) is RH-equivalent.

The theorem is a coordinate change, not an estimate for the new
coordinates.  It removes all primes through \((\log X)^{2+o(1)}\) at
subpower conditioning cost, but it proves no cancellation between the
remaining rough Möbius phases.

## 4. What changed, and what did not

The improvement is not a new large-sieve theorem.  It is the recovery of
support information already present in the finite prefix algebra:

~~~text
complete Euler product
  -> charges every formal dilation
prefix-truncated coefficient mass
  -> charges only d <= X
Rankin optimization
  -> pushes the subpower roughness range to y <= (log X)^(2+o(1))
~~~

This closes one false boundary from the predecessor: the scale
\((\log X)^2(\log\log X)^2\) is not an intrinsic obstruction.  What remains
open begins beyond the exponent-two polylogarithmic frontier, or inside the
rough-source sum itself.

Possible ways past (0.8) would have to use at least one of:

* cancellation among the signed smooth dilates;
* a nonmaximal inversion which avoids paying every smaller prefix;
* a source-adapted norm rather than coefficient-mass domination;
* a direct estimate for the rough spectral witnesses.

None is supplied here.

## 5. Claim ledger

| statement | grade |
|---|---|
| finite prefix identities (1.2) | **IMPORTED EXACT FROM FROZEN PREDECESSOR** |
| truncated maximal conditioning (0.4)--(0.5) | **PROVED EXACT FOR EVERY POSITIVE FOURIER MEASURE** |
| Rankin product bounds (0.6) | **PROVED EXACT** |
| logarithmic envelope (0.7) | **PROVED USING THE LABELLED PNT INPUT** |
| sharp iff frontier (0.9a) | **PROVED BY RANKIN UPPER AND SQUAREFREE-BINOMIAL LOWER BOUNDS** |
| fixed-\(A>2\) mass exponent (0.12) | **PROVED WITH MATCHING UPPER AND LOWER BOUNDS** |
| enlarged rough-lattice equivalence (0.10) | **PROVED CONDITIONAL EQUIVALENCE TO RH** |
| rough-source cancellation or estimate | **OPEN** |
| RH or GRH | **NOT PROVED** |

## 6. Bounded replay

The replay enumerates integers only through \(840\) and primes only through
\(13\).  It checks the exact forward and inverse prefix identities, the
truncated coefficient masses, their domination by both the Rankin products
and the complete Euler products, and the strict savings caused by the
prefix cutoff.  It computes no zeta zero, finite-field element, modulus,
curve, point, or \(L\)-function.

~~~text
python -B research/l-families/atlas/function_field/ffps_prefix_truncated_rough_rankin_frontier.py --check
python -B -O research/l-families/atlas/function_field/ffps_prefix_truncated_rough_rankin_frontier.py --check
python -B -m unittest tests.test_ffps_prefix_truncated_rough_rankin_frontier
python -B -O -m unittest tests.test_ffps_prefix_truncated_rough_rankin_frontier
python -B -m ruff check research/l-families/atlas/function_field/ffps_prefix_truncated_rough_rankin_frontier.py tests/test_ffps_prefix_truncated_rough_rankin_frontier.py
python -B -m ruff format --check research/l-families/atlas/function_field/ffps_prefix_truncated_rough_rankin_frontier.py tests/test_ffps_prefix_truncated_rough_rankin_frontier.py
~~~

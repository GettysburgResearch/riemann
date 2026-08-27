# One guarded harmonic is the sharp maximal rough-Mobius RH normal form

Status: **exact synthesis of the sharp prefix-truncated rough coordinate
change and maximal phase transport; one fixed nonzero guarded harmonic of
the maximal rough Mobius prefix is RH-equivalent throughout the complete
subpower coefficient-mass range; no rough-prefix estimate, endpoint-only
compression, RH, or GRH theorem**

Bounded replay:
[ffps_sharp_rough_single_harmonic_normal_form.py](ffps_sharp_rough_single_harmonic_normal_form.py).
Canonical summary:
[ffps_sharp_rough_single_harmonic_normal_form.json](ffps_sharp_rough_single_harmonic_normal_form.json).

Frozen inputs:

* sharp truncated rough frontier, commit
  `d1af013130ae4004c629b916950e34545b0a65f1`;
* single-harmonic maximal phase transport, commit
  `31c0e730ffe80683798d9cc830c26e9d451a8759`.

The first input uses the prime number theorem and partial summation.  The
second imports the classical Mertens criterion for RH and the pinned
low-frequency expansion of the critical band-pass kernel.  Those classical
and frozen inputs are not reproved by the bounded replay.

Throughout, \(X,N\) are positive integers and \(X\to\infty\).  A real
roughness cutoff \(y_X\ge2\) is chosen once at the **outer** horizon \(X\)
and frozen across every prefix \(1\le N\le X\).  This quantifier is
load-bearing.  Write

\[
 P_X=\prod_{p\le y_X}p.
\tag{0.1}
\]

Real prefix endpoints may be reduced to their floors, but every displayed
Abel identity below uses integer endpoints.  Prefixes with endpoint zero
are defined to be zero.  As in the frozen inputs, \(F(X)=X^{o(1)}\) means
the subpower upper bound \(F(X)\ll_\epsilon X^\epsilon\) for every
\(\epsilon>0\).

## 0. Outcome

Define the unweighted and critical rough prefixes

\[
\begin{aligned}
 Q_{X,N}
 &=\sum_{\substack{n\le N\\(n,P_X)=1}}\mu(n),\\
 A_{X,N}(t)
 &=\sum_{\substack{n\le N\\(n,P_X)=1}}
 {\mu(n)\over n^{1/2+it}},
\end{aligned}
\tag{0.2}
\]

and their maximal forms

\[
 \mathfrak A_{X,t}=\max_{1\le N\le X}|A_{X,N}(t)|,
 \qquad
 \mathfrak Q_X=
 \max_{1\le N\le X}{|Q_{X,N}|\over\sqrt N}.
\tag{0.3}
\]

Fix a kernel order \(r\ge1\) and an integer \(h\ne0\), independently of
\(X\), and put

\[
 L_X=\log X+S_{r,\infty}+\delta,
 \qquad
 t_{h,X}={2\pi h\over L_X},
 \qquad
 w_{h,X}={|\widehat B_{r,\infty}(t_{h,X})|^2\over L_X}.
\tag{0.4}
\]

For fixed \(h\), this guarded coordinate is retained for every sufficiently
large \(X\).

Assume \(y_X\to\infty\) and

\[
 \limsup_{X\to\infty}{\log y_X\over\log\log X}\le2,
 \qquad\text{equivalently}\qquad
 y_X\le(\log X)^{2+o(1)}.
\tag{0.5}
\]

Then the synthesis theorem is

\[
\boxed{
\begin{aligned}
 \mathrm {RH}
 &\Longleftrightarrow \mathfrak A_{X,0}=X^{o(1)}\\
 &\Longleftrightarrow \mathfrak Q_X=X^{o(1)}\\
 &\Longleftrightarrow \mathfrak A_{X,t_{h,X}}=X^{o(1)}\\
 &\Longleftrightarrow \mathfrak A_{X,t_{h,X}}^2=X^{o(1)}\\
 &\Longleftrightarrow
 w_{h,X}\mathfrak A_{X,t_{h,X}}^2=X^{o(1)}.
\end{aligned}}
\tag{0.6}
\]

Thus one fixed nonzero guarded harmonic of the maximal \(y_X\)-rough
Möbius prefix is a complete RH normal form, both before and after the
literal critical-lattice weight is retained.  The result is an equivalence,
not an estimate for that harmonic.

The exact comparison behind (0.6) is useful in its own right.  Put

\[
\begin{aligned}
 C_{\rm sf}(X,y_X)
 &=\sum_{\substack{d\le X\\d\mid P_X}}d^{-1/2},\\
 C_{\rm sm}(X,y_X)
 &=\sum_{\substack{d\le X\\P^+(d)\le y_X}}d^{-1/2},\\
 H_{h,X}&=1+|t_{h,X}|\log X<1+2\pi|h|.
\end{aligned}
\tag{0.7}
\]

If

\[
 \mathfrak M_t(X)=
 \max_{1\le N\le X}
 \left|\sum_{n\le N}{\mu(n)\over n^{1/2+it}}\right|,
\tag{0.8}
\]

then, with no asymptotic assumption on \(y_X\),

\[
\boxed{
 {\mathfrak M_0(X)\over H_{h,X}C_{\rm sf}(X,y_X)}
 \le \mathfrak A_{X,t_{h,X}}
 \le H_{h,X}C_{\rm sm}(X,y_X)\mathfrak M_0(X).}
\tag{0.9}
\]

The literal duplicate-\(67\) beta source can also be kept.  For

\[
 \beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67),
 \qquad
 \mathfrak D_t(X)=
 \max_{N\le X}
 \left|\sum_{n\le N}{\beta(n)\over n^{1/2+it}}\right|,
\tag{0.10}
\]

and \(a=67^{-1/2}\), the exact source-faithful comparison is

\[
\boxed{
 {1-a\over C_{\rm sm}(X,y_X)}\mathfrak A_{X,t}
 \le \mathfrak D_t(X)
 \le(1+a)C_{\rm sf}(X,y_X)\mathfrak A_{X,t}}
\tag{0.11}
\]

for every real \(t\).  There is no special case at \(y_X=67\): rough-prime
deletion and the duplicate-\(67\) source filter are distinct exact
coordinate changes.

## 1. Exact rough scale transport

At \(s=1/2+it\), set

\[
 M_N(t)=\sum_{n\le N}{\mu(n)\over n^s}.
\tag{1.1}
\]

With \(y_X\) frozen, the finite identities are

\[
\begin{aligned}
 M_N(t)
 &=\sum_{\substack{d\mid P_X\\d\le N}}
 {\mu(d)\over d^s}A_{X,\lfloor N/d\rfloor}(t),\\
 A_{X,N}(t)
 &=\sum_{\substack{d\le N\\P^+(d)\le y_X}}
 {1\over d^s}M_{\lfloor N/d\rfloor}(t).
\end{aligned}
\tag{1.2}
\]

The floors are displayed to make the prefix scope literal.  Minkowski for
the scalar absolute value gives, for every real \(t\),

\[
\boxed{
 C_{\rm sm}(X,y_X)^{-1}\mathfrak A_{X,t}
 \le\mathfrak M_t(X)
 \le C_{\rm sf}(X,y_X)\mathfrak A_{X,t}.}
\tag{1.3}
\]

The duplicate source identities

\[
\begin{aligned}
 D_N(t)&=M_N(t)-67^{-1/2-it}M_{\lfloor N/67\rfloor}(t),\\
 M_N(t)&=\sum_{\substack{j\ge0\\67^j\le N}}
 67^{-j(1/2+it)}D_{\lfloor N/67^j\rfloor}(t)
\end{aligned}
\tag{1.4}
\]

cost respectively \(1+a\) and \((1-a)^{-1}\) in maximal norm.  Combining
(1.3) and (1.4) proves (0.11).

## 2. Exact phase transport collapses the spectrum

For arbitrary complex coefficients \(c_n\), define

\[
 F_N(t)=\sum_{n\le N}c_nn^{-it},
 \qquad
 \mathfrak F_t(X)=\max_{N\le X}|F_N(t)|.
\tag{2.1}
\]

Discrete Abel summation, followed once by demodulation, gives the exact
two-sided maximal inequality

\[
\boxed{
 {1\over1+|t|\log X}\mathfrak F_0(X)
 \le\mathfrak F_t(X)
 \le(1+|t|\log X)\mathfrak F_0(X).}
\tag{2.2}
\]

Apply this first to \(c_n=\mu(n)n^{-1/2}\), then to

\[
 c_n=\mathbf1_{(n,P_X)=1}\mu(n)n^{-1/2}.
\tag{2.3}
\]

The latter is one fixed coefficient sequence for the entire prefix family
because \(y_X\) was frozen before taking the maximum.  Hence

\[
 H_{h,X}^{-1}\mathfrak A_{X,0}
 \le\mathfrak A_{X,t_{h,X}}
 \le H_{h,X}\mathfrak A_{X,0},
\tag{2.4}
\]

and the same comparison holds for \(\mathfrak M_{t_{h,X}}\) and
\(\mathfrak M_0\).  Combining either route with (1.3) proves (0.9).

The common frequency is load-bearing: every prefix is evaluated at
\(t_{h,X}\).  A family using \(t_{h,N}\) at prefix \(N\) is not covered by
the reverse Abel argument.

## 3. Zero frequency and the valid unweighted rough-Mertens form

Partial summation is valid for the outer-\(X\) coefficient sequence

\[
 q_{X,n}=\mathbf1_{(n,P_X)=1}\mu(n).
\tag{3.1}
\]

Inside the integrals below, \(Q_{X,u}=Q_{X,\lfloor u\rfloor}\) and
\(A_{X,u}(0)=A_{X,\lfloor u\rfloor}(0)\).

It gives, for every integer \(N\le X\),

\[
\begin{aligned}
 A_{X,N}(0)
 &=N^{-1/2}Q_{X,N}
 +{1\over2}\int_1^N Q_{X,u}u^{-3/2}\,du,\\
 Q_{X,N}
 &=N^{1/2}A_{X,N}(0)
 -{1\over2}\int_1^N A_{X,u}(0)u^{-1/2}\,du.
\end{aligned}
\tag{3.2}
\]

Consequently,

\[
\boxed{
 {1\over1+\tfrac12\log X}\mathfrak A_{X,0}
 \le\mathfrak Q_X
 \le2\mathfrak A_{X,0}.}
\tag{3.3}
\]

This proves the unweighted equivalence in (0.6).  The normalization
\(N^{-1/2}\) inside the maximum is essential for this moving outer cutoff.
The weaker-looking assertion

\[
 \max_{N\le X}|Q_{X,N}|=X^{1/2+o(1)}
\tag{3.4}
\]

is **not** claimed equivalent: at a smaller outer horizon \(u\), its
hypothesis would involve \(y_u\), whereas (3.2) still contains the cutoff
\(y_X\).  There is no scale-local bound to insert into the integral.

For the ordinary, \(X\)-independent Möbius sequence, the same two partial
summations recover the classical chain

\[
 \mathrm {RH}
 \Longleftrightarrow
 \max_{N\le X}\left|\sum_{n\le N}\mu(n)\right|
 =X^{1/2+o(1)}
 \Longleftrightarrow
 \mathfrak M_0(X)=X^{o(1)}.
\tag{3.5}
\]

Together with the subpower conditioning in the next section, (3.5),
(1.3), (2.4), and (3.3) prove (0.6).

## 4. The sharp positive-mass boundary

The frozen rough-frontier theorem proves

\[
\boxed{
 C_{\rm sf}(X,y_X),\ C_{\rm sm}(X,y_X)=X^{o(1)}
 \Longleftrightarrow
 \limsup_{X\to\infty}{\log y_X\over\log\log X}\le2,}
\tag{4.1}
\]

under \(y_X\to\infty\).  Its upper bound uses Rankin's trick and the PNT;
its lower bound uses squarefree products of distinct primes.  Therefore
(0.5) is the largest complete range in which the positive coefficient
masses make (0.9) a subpower isomorphism.

Every fixed \(B\in\mathbb R\) is allowed in

\[
 y_X=(\log X)^2(\log\log X)^B.
\tag{4.2}
\]

For comparison, if \(y_X=(\log X)^A\) with fixed \(A>2\), then

\[
 C_{\rm sf}(X,y_X),\ C_{\rm sm}(X,y_X)
 =X^{1/2-1/A+o(1)}.
\tag{4.3}
\]

Equations (4.1)--(4.3) concern the **positive conditioning masses**.  They
do not prove that the signed rough coordinate ceases to be RH-equivalent
beyond the frontier, and they are not a no-go for cancellation in the
native scale transforms.

## 5. Restoring the literal lattice weight

For fixed \(r\ge1\) and fixed \(h\ne0\), the pinned low-frequency theorem
is

\[
\boxed{
 w_{h,X}\sim
 K_0^2(2\pi|h|)^{2r}L_X^{-(2r+1)},
 \qquad
 K_0=3(1-\sqrt2)^2(\log2)^2\ne0.}
\tag{5.1}
\]

Thus \(w_{h,X}\) and \(w_{h,X}^{-1}\) are both \(X^{o(1)}\), proving the
last equivalence in (0.6).  The harmonic must remain nonzero in the
weighted statement: the band-pass kernel is exactly notched at \(h=0\).
The raw zero-frequency rough prefix remains RH-equivalent by (0.6).

Within the positive kernel-weighted retained lattice, one nonzero
coordinate is therefore cardinality-minimal.  This is not a universal
information-theoretic minimality statement about unweighted coordinates.

## 6. Quantifier and scope fences

The following replacements are not proved:

* \(y_X\) may not be replaced by \(y_N\) inside the prefix maximum.  The
  inverses in (1.2) call smaller endpoints while retaining \(P_X\).
* One does not impose \(y_X\le N\) for every prefix.  If \(N<y_X\), the
  rough sum simply contains only its \(n=1\) term.
* The endpoint \(A_{X,X}(t_{h,X})\) is not known to replace the maximal
  prefix.
* Dyadic endpoints are not known to replace all prefixes.
* Reperiodized frequencies \(t_{h,N}\) are not covered.
* Moving \(h\), moving \(r\), or \(h=0\) in the weighted theorem is not
  covered.
* No cancellation estimate for \(A_{X,N}(t)\), RH, or GRH is proved.

The theorem is a particularly small target, but it is still exactly of RH
strength:

~~~text
ordinary weighted Mertens maximal prefix
  -- sharp truncated rough scale isomorphism -->
maximal y_X-rough critical prefix at zero frequency
  -- bounded common-period phase transport -->
one fixed nonzero guarded harmonic
  -- polylogarithmic nonzero lattice weight -->
one weighted spectral coordinate.
~~~

## 7. Claim ledger

| statement | grade |
|---|---|
| finite rough scale identities (1.2) | **IMPORTED EXACT AND REPLAYED** |
| scalar maximal conditioning (1.3), beta comparison (0.11) | **PROVED EXACT** |
| arbitrary-coefficient phase transport (2.2) | **IMPORTED EXACT AND REPLAYED** |
| normalized unweighted rough comparison (3.3) | **PROVED EXACT BY PARTIAL SUMMATION** |
| sharp coefficient-mass frontier (4.1) | **IMPORTED PROVED SHARP** |
| raw rough single-harmonic criterion (0.6) | **PROVED RH-EQUIVALENT** |
| weighted rough single-harmonic criterion (0.6) | **PROVED RH-EQUIVALENT FOR FIXED \(r,h\ne0\)** |
| endpoint-only or dyadic compression | **OPEN / NOT CLAIMED** |
| rough-prefix estimate, RH, or GRH | **NOT PROVED** |

## 8. Bounded replay

The replay uses integers only through \(840\), primes only through \(13\),
and one fixed low frequency.  It checks the two finite rough scale
identities, forward and reverse maximal phase inequalities for the literal
rough critical coefficients, the normalized partial-summation comparison,
and the composed normal-form constants.  It computes no zeta zero,
finite-field element, curve, point count, or large matrix.

~~~text
python -B research/l-families/atlas/function_field/ffps_sharp_rough_single_harmonic_normal_form.py --check
python -B -O research/l-families/atlas/function_field/ffps_sharp_rough_single_harmonic_normal_form.py --check
python -B -m unittest tests.test_ffps_sharp_rough_single_harmonic_normal_form
python -B -O -m unittest tests.test_ffps_sharp_rough_single_harmonic_normal_form
python -B -m ruff check research/l-families/atlas/function_field/ffps_sharp_rough_single_harmonic_normal_form.py tests/test_ffps_sharp_rough_single_harmonic_normal_form.py
python -B -m ruff format --check research/l-families/atlas/function_field/ffps_sharp_rough_single_harmonic_normal_form.py tests/test_ffps_sharp_rough_single_harmonic_normal_form.py
~~~

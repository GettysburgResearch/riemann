# Small-prime removal is an exact rough-source coordinate change up to the absolute-Neumann frontier

Status: **exact commuting prefix-scale factorization, terminating inverse,
positive-measure maximal conditioning, and moving-\(y\) critical-lattice RH
equivalence; no rough-source estimate, cancellation theorem, RH, or GRH is
proved**

Bounded exact replay:
[ffps_small_prime_rough_critical_lattice_preconditioner.py](ffps_small_prime_rough_critical_lattice_preconditioner.py).
Canonical summary:
[ffps_small_prime_rough_critical_lattice_preconditioner.json](ffps_small_prime_rough_critical_lattice_preconditioner.json).

Frozen predecessor: \(8192514ed68f50b8e2a9cff9e1bedab2478bb5c1\).
The replay pins the complete duplicate-\(67\) scale-filter and critical
Fourier-lattice theorem quartets at that commit.

One classical external analytic input is used and labelled explicitly:
the prime number theorem and partial summation give
\[
 \sum_{p\le y}p^{-1/2}
 =\left(2+o(1)\right){\sqrt y\over\log y}.
\tag{0.1}
\]
This input is not reproved or numerically simulated by the bounded replay.

## 0. Outcome

Put \(s=1/2+it\), let
\[
 P(y)=\prod_{p\le y}p,
\tag{0.2}
\]
and define the ordinary Möbius, duplicate-\(67\), and \(y\)-rough prefixes
\[
\begin{aligned}
 M_X(t)&=\sum_{n\le X}{\mu(n)\over n^s},\\
 D_X(t)&=\sum_{n\le X}{\beta(n)\over n^s},
 \qquad
 \beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67),\\
 A_{y,X}(t)&=
 \sum_{\substack{n\le X\\(n,P(y))=1}}{\mu(n)\over n^s}.
\end{aligned}
\tag{0.3}
\]
Every prefix below one is zero.

For each prime \(p\), set
\[
 \omega_p(t)=p^{-s},
 \qquad
 (\mathsf S_pF)_X(t)=F_{X/p}(t),
 \qquad
 \mathsf T_p=I-\omega_p\mathsf S_p.
\tag{0.4}
\]
The multiplication and prefix-dilation operators commute for distinct
primes.  The exact finite factorization is
\[
\boxed{
 M=\prod_{p\le y}\mathsf T_p A_y,
 \qquad
 D=\mathsf T_{67}\prod_{p\le y}\mathsf T_p A_y.}
\tag{0.5}
\]
If \(67\le y\), the second formula contains
\(\mathsf T_{67}^2\).  That is not double counting: one factor is the
ordinary Möbius Euler state and the other is the literal duplicate-\(67\)
source orientation.

Every inverse terminates at every prefix:
\[
\boxed{
 \mathsf T_p^{-1}F_X
 =\sum_{j\ge0}\omega_p^jF_{X/p^j}.}
\tag{0.6}
\]
Consequently, if \(\mathcal S(y)\) denotes the positive integers all of
whose prime factors are at most \(y\), then
\[
\boxed{
 A_{y,X}(t)
 =\sum_{\substack{d\in\mathcal S(y)\\d\le X}}
 d^{-s}M_{X/d}(t).}
\tag{0.7}
\]
There is also the source-faithful beta inverse
\[
\boxed{
 A_{y,X}(t)
 =\sum_{\substack{j\ge0,\ d\in\mathcal S(y)\\67^jd\le X}}
 67^{-js}d^{-s}D_{X/(67^jd)}(t).}
\tag{0.8}
\]

Let \(\nu\) be any positive Fourier measure for which these finite prefixes
belong to \(L^2(\nu)\), and define
\[
 \mathfrak F_\nu(X)=
 \sup_{1\le Y\le X}\|F_Y\|_{L^2(\nu)}.
\tag{0.9}
\]
Put
\[
 C_+(y)=\prod_{p\le y}(1+p^{-1/2}),
 \qquad
 C_-(y)=\prod_{p\le y}(1-p^{-1/2})^{-1}.
\tag{0.10}
\]
Then
\[
\boxed{
 C_-(y)^{-1}\mathfrak A_{y,\nu}(X)
 \le\mathfrak M_\nu(X)
 \le C_+(y)\mathfrak A_{y,\nu}(X)}
\tag{0.11}
\]
and
\[
\boxed{
\begin{aligned}
 &(1-67^{-1/2})C_-(y)^{-1}\mathfrak A_{y,\nu}(X)\\
 &\qquad\le\mathfrak D_\nu(X)
 \le(1+67^{-1/2})C_+(y)\mathfrak A_{y,\nu}(X).
\end{aligned}}
\tag{0.12}
\]
These inequalities hold for every positive measure, including the
continuous critical window and the retained critical Fourier lattice.

For the lattice, keep the predecessor notation
\[
 L_X=\log X+S+\delta,\qquad
 t_k={2\pi k\over L_X},\qquad
 K_*(X)=\left\lceil {L_Xe^{\sqrt{(\log2)(\log X)}}\over2\pi}\right\rceil,
\tag{0.13}
\]
and define
\[
 \lambda_X={1\over L_X}
 \sum_{|k|\le K_*(X)}
 |\widehat B(t_k)|^2\delta_{t_k}.
\tag{0.14}
\]
If \(y=y(X)\to\infty\) satisfies
\[
\boxed{
 {\sqrt{y(X)}\over\log y(X)}=o(\log X),}
\tag{0.15}
\]
then
\[
\boxed{
\mathrm{RH}\Longleftrightarrow
\sup_{1\le Y\le X}
\|A_{y(X),Y}\|_{L^2(\lambda_X)}^2=X^{o(1)}.}
\tag{0.16}
\]

The absolute-Neumann frontier is explicit.  For every fixed
\(\delta_0>0\),
\[
 y=(\log X)^2(\log\log X)^{2-\delta_0}
\tag{0.17}
\]
has
\[
\boxed{
\log C_\pm(y)
=\left(1+o(1)\right)
{\log X\over(\log\log X)^{\delta_0/2}}
=o(\log X).}
\tag{0.18}
\]
Thus (0.16) applies.  In contrast, for fixed \(c>0\),
\[
 y=c(\log X)^2(\log\log X)^2
\tag{0.19}
\]
has
\[
\boxed{
 C_+(y)=C_-(y)=X^{\sqrt c+o(1)},
 \qquad
 C_+(y)C_-(y)=X^{2\sqrt c+o(1)}.}
\tag{0.20}
\]
At this scale absolute inversion loses a genuine power.  Equation (0.20)
is stated for norms; after squaring, either one-way maximal-energy
comparison may cost \(X^{2\sqrt c+o(1)}\).  It does not prove that every
signed inversion or every arithmetic norm must lose that power.

## 1. Exact commuting prefix algebra

Every squarefree integer has a unique factorization \(n=dm\), where all
prime factors of \(d\) are at most \(y\), \(m\) is \(y\)-rough, and
\((d,m)=1\).  Therefore
\[
\begin{aligned}
\prod_{p\le y}\mathsf T_p A_{y,X}(t)
&=\sum_{d\mid P(y)}{\mu(d)\over d^s}A_{y,X/d}(t)\\
&=\sum_{n\le X}{\mu(n)\over n^s}
=M_X(t).
\end{aligned}
\tag{1.1}
\]
This proves the first identity in (0.5); applying the literal
duplicate-\(67\) difference proves the second.

For \(p\ne q\),
\[
 \mathsf S_p\mathsf S_qF_X
 =F_{X/(pq)}
 =\mathsf S_q\mathsf S_pF_X,
\tag{1.2}
\]
and the scalar multipliers commute.  Hence every \(\mathsf T_p\) and every
terminating inverse commute.

Iterating one scale equation gives
\[
 \mathsf T_p^{-1}F_X
 =F_X+\omega_pF_{X/p}+\cdots+
 \omega_p^{\lfloor\log_pX\rfloor}F_{X/p^{\lfloor\log_pX\rfloor}},
\tag{1.3}
\]
because the next prefix is below one.  Multiplying (1.3) over all
\(p\le y\) gives (0.7).  Composing with the duplicate-\(67\) inverse gives
(0.8).  No limiting Euler product, PNT estimate, or Möbius cancellation is
used in these identities.

Coefficientwise, (0.7) says
\[
 \mathbf1_{(n,P(y))=1}\mu(n)
 =
 \sum_{\substack{d\mid n\\d\in\mathcal S(y)}}\mu(n/d).
\tag{1.4}
\]
The bounded replay checks both (1.1) and (1.4) through \(n=420\), including
prime powers and nonsquarefree inputs.

## 2. Maximal conditioning for every positive measure

For one prime, Minkowski gives
\[
 \|\mathsf T_pF_Y\|_{L^2(\nu)}
 \le\|F_Y\|_{L^2(\nu)}
 p^{-1/2}\|F_{Y/p}\|_{L^2(\nu)}.
\tag{2.1}
\]
Taking the prefix supremum yields
\[
 \mathfrak T_{p,\nu}(X)
 \le(1+p^{-1/2})\mathfrak F_\nu(X).
\tag{2.2}
\]
The terminating inverse and another application of Minkowski give
\[
 \mathfrak F_\nu(X)
 \le\sum_{j\ge0}p^{-j/2}\mathfrak T_{p,\nu}(X)
 ={1\over1-p^{-1/2}}\mathfrak T_{p,\nu}(X).
\tag{2.3}
\]
Multiplication over the commuting primes proves (0.11).  The
duplicate-\(67\) one-prime inequality
\[
 (1-67^{-1/2})\mathfrak M_\nu(X)
 \le\mathfrak D_\nu(X)
 \le(1+67^{-1/2})\mathfrak M_\nu(X)
\tag{2.4}
\]
then proves (0.12).

The measure may depend on \(X\) and may be atomic.  The proof uses only
positivity, Minkowski, \(|\omega_p(t)|=p^{-1/2}\), and the maximal prefix
envelope.  It neither estimates individual Fourier coordinates nor
asserts an operator-norm approximation for the discarded lattice tail.

## 3. Why the moving-\(y\) lattice target is RH-equivalent

First, the beta maximal retained-lattice criterion is itself RH-equivalent:
\[
\boxed{
\mathrm{RH}\Longleftrightarrow
\mathfrak D_{\lambda_X}(X)^2=X^{o(1)}.}
\tag{3.1}
\]

For the forward implication, assume RH.  Use the period \(L_X\) not only
for \(H_X\), but for every \(H_Y\) with \(Y\le X\).  Its support lies in
\([0,\log Y+S]\subset[0,\log X+S]\), so the same guard gives exact Parseval:
\[
 \mathcal E(Y)
 ={1\over L_X}\sum_{k\in\mathbf Z}
 |\widehat B(t_k)|^2|D_Y(t_k)|^2.
\tag{3.2}
\]
The retained sum is at most \(\mathcal E(Y)\).  The fixed-kernel criterion
gives \(\mathcal E(Y)=Y^{o(1)}\), and the standard finite-small-prefix
argument gives
\[
 \sup_{1\le Y\le X}\mathcal E(Y)=X^{o(1)}.
\tag{3.3}
\]
This proves the forward half of (3.1).

Conversely, the maximal retained norm contains its \(Y=X\) endpoint.  The
pinned critical-lattice theorem says that this endpoint is \(X^{o(1)}\)
if and only if RH.  This proves (3.1).

By the PNT estimate in Section 4, condition (0.15) is precisely enough for
\[
 C_+(y(X))=C_-(y(X))=X^{o(1)}.
\tag{3.4}
\]
Apply (0.12) with \(\nu=\lambda_X\), square the inequalities, and combine
with (3.1).  This proves (0.16).

The maximal prefix is load-bearing.  Formulae (0.7)--(0.8) call the
smaller prefixes \(X/d\) for all \(y\)-smooth \(d\), so an isolated rough
endpoint is not supplied by this absolute inverse.

## 4. Imported PNT asymptotics and the frontier

The only non-algebraic input specific to the moving cutoff is the
classical estimate (0.1).  It follows from
\(\pi(u)\sim u/\log u\) by partial summation.  Also,
\[
 \sum_{p\le y}{1\over p}=O(\log\log y).
\tag{4.1}
\]
Taylor expansion, with the finitely many smallest primes absorbed into
the error, gives
\[
\begin{aligned}
\log C_+(y)
&=\sum_{p\le y}\log(1+p^{-1/2})
=\sum_{p\le y}p^{-1/2}+O(\log\log y),\\
\log C_-(y)
&=-\sum_{p\le y}\log(1-p^{-1/2})
=\sum_{p\le y}p^{-1/2}+O(\log\log y).
\end{aligned}
\tag{4.2}
\]
Thus
\[
\boxed{
\log C_\pm(y)
=\left(2+o(1)\right){\sqrt y\over\log y},
\qquad
\log(C_+(y)C_-(y))
=\left(4+o(1)\right){\sqrt y\over\log y}.}
\tag{4.3}
\]

For (0.17),
\[
 \sqrt y=\log X\,(\log\log X)^{1-\delta_0/2},
\qquad
 \log y=2\log\log X+O(\log\log\log X),
\tag{4.4}
\]
which proves (0.18).  For (0.19),
\[
 \sqrt y=\sqrt c\,\log X\log\log X,
\qquad
 \log y=2\log\log X+O(\log\log\log X),
\tag{4.5}
\]
which proves (0.20).

Chebyshev two-sided bounds alone already locate the transition up to
constant powers.  The PNT normalization supplies the displayed
\(\sqrt c\) exponent.

## 5. What remains after rough preconditioning

Inside the subfrontier, the RH burden has become
\[
\boxed{
\sup_{1\le Y\le X}{1\over L_X}
\sum_{|k|\le K_*(X)}
|\widehat B(t_k)|^2
\left|
\sum_{\substack{n\le Y\\p\mid n\Rightarrow p>y(X)}}
{\mu(n)\over n^{1/2+it_k}}
\right|^2
=X^{o(1)}.}
\tag{5.1}
\]
The inner source is squarefree and \(y(X)\)-rough.  All small-prime Euler
states have been removed exactly, but no cancellation among the remaining
rough phases has been produced.

The theorem therefore does three things, and only three:

1. it exhibits a commuting multiscale coordinate system;
2. it proves that removing primes through (0.17) costs only \(X^{o(1)}\)
   under absolute inversion;
3. it identifies the power-loss boundary of that absolute argument.

It does not show that the rough source is smaller, more random, or easier
in the required norm.  At and beyond (0.19), signed cancellation among
smooth dilates, a nonmaximal inversion, or a source-adapted norm could in
principle outperform \(C_-(y)\); none is supplied here.

## 6. Claim ledger

| statement | grade |
|---|---|
| commuting factorization (0.5) | **PROVED EXACT FOR EVERY FINITE \(y,X\)** |
| terminating inverses (0.6)--(0.8) | **PROVED EXACT** |
| maximal conditioning (0.11)--(0.12) | **PROVED FOR EVERY POSITIVE FOURIER MEASURE** |
| beta maximal retained-lattice criterion (3.1) | **PROVED FROM GUARDED PARSEVAL AND THE PINNED ENDPOINT CRITERION** |
| moving-\(y\) equivalence (0.16) | **PROVED WHEN (0.15) HOLDS** |
| PNT conditioning asymptotic (4.3) | **IMPORTED CLASSICAL PNT PLUS PARTIAL SUMMATION** |
| subfrontier and critical exponents | **PROVED FROM (4.3)** |
| rough-prefix estimate (5.1) | **OPEN / RH-EQUIVALENT IN THE STATED RANGE** |
| cancellation, RH, or GRH | **NOT PROVED** |

## 7. Bounded replay

~~~text
python -B research/l-families/atlas/function_field/ffps_small_prime_rough_critical_lattice_preconditioner.py --check
python -B -O research/l-families/atlas/function_field/ffps_small_prime_rough_critical_lattice_preconditioner.py --check
python -B -m unittest tests.test_ffps_small_prime_rough_critical_lattice_preconditioner
python -B -O -m unittest tests.test_ffps_small_prime_rough_critical_lattice_preconditioner
python -B -m ruff check research/l-families/atlas/function_field/ffps_small_prime_rough_critical_lattice_preconditioner.py tests/test_ffps_small_prime_rough_critical_lattice_preconditioner.py
python -B -m ruff format --check research/l-families/atlas/function_field/ffps_small_prime_rough_critical_lattice_preconditioner.py tests/test_ffps_small_prime_rough_critical_lattice_preconditioner.py
~~~

The replay uses integer coefficient convolution and rational finite prefix
filters.  It checks 420 coefficients and four commuting scale operators on
96 prefixes.  It performs no floating-point asymptotic fit, zeta-zero
enumeration, large matrix calculation, or finite-field enumeration.  Its
preconditioning prime set is exactly \(\{2,3,5,7\}\).

# A sharper unmarking theorem: the exact minimum-degree projection

Status: **The finite probability-space theorem below is proved.** Its
application to the fixed-parameter marked correlations is source-qualified.
The separate growing-parameter audit is in `UNIFORM_HLC_AUDIT.md`; do not infer
a quantitative theorem from fixed-parameter estimates alone.

Scope: exact finite CRT algebra, an optimal approximation theorem, and an
explicit correlation transfer inequality. This does not prove RH or a new
zero-free region.

Exact sources: Lü–Wang–Wu, arXiv:2610.20242v1, equations (2.12)–(2.19),
Propositions 3.1, 4.2 and 5.3, and the fixed-parameter proof of Theorem 1.
The supplied PDF and its digest are identified in the parent `SOURCES.md`.
The first-pass `MARK_VARIANCE.md` supplies the finite single-band moments;
they are rederived here where used.

What is new in this packet: the paper averages a number of normalized block
marks and incurs an inverse-square-root error. Here every admissible marked
product is used together. The best possible error in their linear span is an
explicit lower tail of a sum of independent Bernoulli variables. This gives
exponential decay in the number of individual bands, with a fixed minimum
degree. It is not another form of the preceding block average.

## 1. Exact theorem on a product probability space

Let \(U_1,\ldots,U_N\) be independent real random variables with

\[
 \mathbb E U_i=1,\qquad \mathbb E U_i^2=R_i>1,
 \qquad q_i=R_i^{-1},\quad a_i=1-q_i.
\]

Only these first two moments are required. Fix integers \(1\le k\le N\).
For a subset \(S\subseteq\{1,\ldots,N\}\), put
\(U_S=\prod_{i\in S}U_i\) and \(q_S=\prod_{i\in S}q_i\), with empty
products equal to one. Define the finite-dimensional subspace

\[
 \mathcal V_{N,k}=
 \operatorname{span}\{U_S: |S|\ge k\}\subset L^2.
\]

**Theorem 1.** The orthogonal projection of the constant function one onto
\(\mathcal V_{N,k}\) is

\[
 \boxed{
 P_{N,k}=
 \sum_{\substack{S\subseteq[N]\\|S|\ge k}}
 (-1)^{|S|-k}\binom{|S|-1}{k-1}q_SU_S.}
 \tag{1}
\]

Its exact squared error is

\[
 \boxed{
 \|1-P_{N,k}\|_2^2
 =\sum_{\substack{T\subseteq[N]\\|T|<k}}
       \prod_{i\in T}q_i\prod_{i\notin T}(1-q_i)
 =\Pr\{B_1+\cdots+B_N<k\},}
 \tag{2}
\]

where the \(B_i\) in the last expression are independent Bernoulli variables
of probabilities \(q_i\). No independence between these auxiliary Bernoulli
variables and the \(U_i\) is needed: (2) is a formula for a number.

If \(R_i=R\), this number is

\[
 \sum_{j=0}^{k-1}\binom Nj R^{-j}(1-R^{-1})^{N-j}.
 \tag{3}
\]

The projection, not just its norm, is determined. In particular, no other
linear combination of the admitted squarefree products has smaller
\(L^2\) error.

### Proof

Set \(V_i=1-q_iU_i\). Directly from the moments,

\[
 \mathbb E(U_iV_i)=0,\qquad
 \mathbb E V_i^2=1-q_i,\qquad
 1=V_i+q_iU_i.
\]

For \(T\subseteq[N]\) put

\[
 H_T=\prod_{i\in T}U_i\prod_{i\notin T}V_i.
\]

These functions are pairwise orthogonal: two distinct index sets differ in
some coordinate, whose expectation contributes \(\mathbb E U_iV_i=0\).
Their norms are positive, so they are linearly independent. Expanding
\(1=\prod_i(V_i+q_iU_i)\) gives

\[
 1=\sum_{T\subseteq[N]}q_TH_T.                 \tag{4}
\]

Also

\[
 U_S=\sum_{T\supseteq S}q_{T\setminus S}H_T.
 \tag{5}
\]

The transformation in (5), ordered by decreasing cardinality, is triangular
with diagonal one. Consequently

\[
 \mathcal V_{N,k}=\operatorname{span}\{H_T:|T|\ge k\}.
\]

Thus the desired projection is the sum in (4) with \(|T|\ge k\).
Expanding the remaining \(V_i=1-q_iU_i\), the coefficient of \(U_S\)
for \(|S|=j\ge k\) is

\[
 q_S\sum_{r=k}^{j}(-1)^{j-r}\binom jr
 =q_S(-1)^{j-k}\binom{j-1}{k-1}.
\]

This proves (1). By orthogonality, the squared norm of the omitted terms is

\[
 \sum_{|T|<k}q_T^2
       \prod_{i\in T}R_i\prod_{i\notin T}(1-q_i),
\]

which is (2). Orthogonal projection minimizes the distance to a subspace,
proving optimality. All sums are finite. \(\square\)

## 2. Exact finite CRT realization for the source marks

Let \(\mathcal P_1,\ldots,\mathcal P_N\) be nonempty, finite, disjoint
sets of odd primes. Let \(P\) be the product of every prime in their union,
and choose \(a\) uniformly from the reduced residue classes modulo \(P\).
For \(p>2\), precisely one of the \(p-1\) nonzero residue classes satisfies
\(p\mid a+2\). Hence the indicators \(1_{p\mid a+2}\) are independent
Bernoulli variables with probabilities \(\theta_p=1/(p-1)\).

Write

\[
 N_i=\sum_{p\in\mathcal P_i}1_{p\mid a+2},\qquad
 F_i(z)=\prod_{p\in\mathcal P_i}(1+\theta_p(z-1)).
\]

For any fixed \(0<\rho<1\), define

\[
 U_i=\frac{N_i\rho^{N_i-1}}{F_i'(\rho)},
\]

where the numerator is zero when \(N_i=0\). Since
\(\mathbb E z^{N_i}=F_i(z)\), differentiation gives

\[
 \mathbb E U_i=1,\qquad
 R_i=
 \frac{F_i'(\rho^2)+\rho^2F_i''(\rho^2)}{F_i'(\rho)^2}.
 \tag{6}
\]

The variables \(U_i\) are independent by CRT. Each has positive probability
of being zero and positive mean, so \(R_i>1\). Theorem 1 therefore applies
without an asymptotic limit or a conjecture about primes.

For a nonempty subset \(S\), the product \(U_S\) is exactly a nonzero
scalar multiple of the source's mark (2.13) formed from the bands in \(S\):

\[
 U_S=
 \prod_{i\in S}\frac{V_i^{\rm src}}{F_i'(\rho)}
 \prod_{i\in S}\frac{N_i\rho^{N_i-1}}{V_i^{\rm src}},
 \qquad V_i^{\rm src}=\sum_{p\in\mathcal P_i}p^{-1}.
 \tag{7}
\]

The damping counts in (7) involve only the selected bands. There is no
unselected-band damping, repeated band, or replacement of the original
Möbius coefficient. This is why the degree restriction in Theorem 1 is
useful: if the source requires at least \(k\) bands, every term of (1)
is admissible.

## 3. A correlation transfer with every cost explicit

Let \(\nu\) be any probability measure on a space on which the same
functions \(U_i\) are defined, and let \(|f|\le1\). For the coefficients
\(c_S=(-1)^{|S|-k}\binom{|S|-1}{k-1}q_S\), the exact identity
\(1=P_{N,k}+(1-P_{N,k})\) and Cauchy–Schwarz give

\[
 \left|\int f\,d\nu\right|
 \le \sum_{|S|\ge k}|c_S|
                  \left|\int fU_S\,d\nu\right|
       +\left(\int|1-P_{N,k}|^2\,d\nu\right)^{1/2}.
 \tag{8}
\]

No distributional assumption on \(\nu\) was used in (8). If the last
integral differs from the CRT quantity (2) by at most \(\delta\ge0\), and
every admitted correlation has magnitude at most \(\varepsilon\), then

\[
 \left|\int f\,d\nu\right|
 \le \varepsilon A_{N,k}(q)
       +\sqrt{\Pr(\sum B_i<k)+\delta},          \tag{9}
\]

where

\[
 A_{N,k}(q)=\sum_{|S|\ge k}\binom{|S|-1}{k-1}q_S
 \le \frac{N^{k-1}}{(k-1)!}\prod_{i=1}^N(1+q_i)
 \le \frac{N^{k-1}2^N}{(k-1)!}.               \tag{10}
\]

The first inequality uses \(\binom{j-1}{k-1}\le N^{k-1}/(k-1)!\).
Thus (9) includes both amplification of the marked errors and the exact
unmarking cost. Exponential decay cannot be quoted while omitting the
coefficient cost or the discrepancy \(\delta\).

For fixed \(R>1\) and fixed \(k\), (3) gives

\[
 \|1-P_{N,k}\|_2
 \ll_{k,R}N^{(k-1)/2}(1-R^{-1})^{N/2}.        \tag{11}
\]

For comparison, averaging \(b\) independent normalized blocks, each of
\(k\) bands and second moment \(R^k\), has squared error
\((R^k-1)/b\). A blockwise product correction gives error
\((1-R^{-k})^{b/2}\), which still has the poor rate \(R^{-k}\).
The full minimum-degree projection (11), using \(N=bk\) individual bands,
avoids that loss. These are comparisons of rigorously defined approximation
spaces, not a claim that their arithmetic correlation estimates are equal.

## 4. The paper's fixed-band asymptotic

For the source bands
\(\mathcal P_i=(\exp(L^{a_i}),\exp(2L^{a_i})]\cap\mathbb P\),
with \(L=\log x\) and fixed distinct \(a_i\in(0.1,0.2)\), the
single-band distributions tend to Poisson with mean \(\lambda=\log2\).
Consequently (6) tends to

\[
 R=r(\rho)=\left(\rho^2+\frac1\lambda\right)
                \exp\{\lambda(\rho-1)^2\}.  \tag{12}
\]

The fixed-dimensional joint convergence for shifted primes follows by the
same divisor expansion and Bombieri–Vinogradov input as source Proposition
2.3. For the finitely many second moments needed here, one also applies it
to \(N_i^2\rho^{2N_i-2}\); this is a bounded function of \(N_i\), and its
divisor expansion is obtained by twice differentiating the generating
polynomial. One can instead use fixed mixed factorial moments and their
Poisson limit, as in the parent `MARK_VARIANCE.md`.

For each fixed \(N,k\), take \(\nu_x\) to give each prime
\(x<p\le2x\) mass \(\log p/\sum_{x<q\le2x}\log q\), and set
\(f(p)=\mu(p+2)\). Then the last term of (8) tends to the square root of
(3) with \(R=r(\rho)\). If the source's marked-correlation conclusion is
available for every selected cardinality \(k,\ldots,N\), each first term
tends to zero. Thus

\[
 \limsup_{x\to\infty}
 \left|\int\mu(p+2)\,d\nu_x(p)\right|
 \le
 \left[\sum_{j=0}^{k-1}\binom Njr(\rho)^{-j}
                  (1-r(\rho)^{-1})^{N-j}\right]^{1/2}.
 \tag{13}
\]

This is an exponential-in-\(N\) improvement of the source's fixed-parameter
unmarking inequality. It still takes the \(x\)-limit with \(N,k\) fixed.
Equation (13) alone gives no prescribed rate in \(x\).

## 5. What this does and does not retain

I also tested retaining both \(\mu(m)\) and \(\mu(h)\) in the Type II
equation \(mn+2=ah\). The source's determinant square is the norm after
the \(h\)-sign is discarded. Reinserting \(\mu(h)\) into both endpoints
produces \(\mu(h)^2\), not a second independent signed saving. Reinserting
it at one endpoint creates a coupled coefficient depending on the quotient
\((mn+2)/a\), outside the separable major-arc calculation. No new bound
for that coupled coefficient is proved here.

The positive result of this note is instead an exact repair of one
quantitative loss that occurs after the source's Type II estimate. It does
not supply a power of \(x\), does not establish the native inverse-moment
estimate, and does not delete the Mertens main term in the shift bridge.

## 6. Verification

`check_optimal_unmarking.py` enumerates complete reduced residue systems for
finite prime-band examples and checks (1), (2), and orthogonality against
every admitted product using exact rational arithmetic. It also verifies
the Pythagorean optimality identity for a nonzero perturbation of the
projection and rejects a deliberately changed coefficient. These checks
authenticate finite identities; the proof above supplies the arbitrary-size
theorem. They do not certify any growing-parameter analytic estimate.

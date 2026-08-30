# Canonical Boolean principal diagonal: an arithmetic candidate, not a native resolution

Status: PROVED BOUNDED-SCOPE DIAGONAL ESTIMATE; native masked bilateral identification OPEN.
Programme: #763, carried earlier signed-source work. No RH assumption or consequence.
Base context: 08187bdfae119f66c8c82baca2d1c1068e48ff40.
Arithmetic: MIXED (EXACT_RATIONAL and CERTIFIED_INTEGER_COVERAGE).
The producer checks finite algebra only; the all-horizon proof is below.

## 1. What is and is not being compared

The canonical equal-pair Boolean source has an exact arithmetic coefficient
before the retained bilateral observations are imposed. This note bounds the
principal diagonal of that candidate using the ORIGINAL principal weights
and ORIGINAL Mellin measure. It does not identify this candidate with a
resolution of the fully labelled T-106140 source.

Write the full principal moments and their diagonals as
\(P_{\rm nat},D_{\rm lit}\) and \(P_B,D_B\), respectively. Then
\[
 P_{\rm nat}^{\circ}-P_B^{\circ}
   =(P_{\rm nat}-P_B)+(D_B-D_{\rm lit}).                 \tag{CBPD1}
\]
The source estimate for \(D_{\rm lit}\), together with our estimate for \(D_B\),
bounds the SECOND difference by their sum. The FIRST difference is unpaid.
Equality of unobserved product sources is not intertwining of pair-dependent
masks. No diagonal comparison in this note establishes a sign, cancellation,
full-fibre estimate, new admissible native coefficient vector, WCADD, WCKUM,
WCEQ, or RH.

The following theorem EXCLUDES the exceptional prime 67 completely. Its
primes are ordinary distinct physical primes, not two labelled copies of 67.
There is no claimed extension to that exceptional chart. It is elementary
Boolean/divisor algebra applied to this normalization, not a novelty claim
for the underlying majorants.

## 2. Canonical coefficient and the unit-core edge case

On squarefree integers use disjoint-support Boolean convolution \(\star\).
For an integer \(U\ge1\), let
\[
 \mu_U(a)=\mu(a)1_{a\le U},\qquad
 a_U=\epsilon-\mu_U\star1_{\rm sf},\qquad
 b_U=a_U\star a_U\star\mu_{\rm sf}.
\]
Since \(1_{\rm sf}\star\mu_{\rm sf}=\epsilon\), the literal Vaughan expansion is
\[
 b_U=\mu_{\rm sf}-2\mu_U+
             \mu_U\star\mu_U\star1_{\rm sf}.             \tag{CBPD2}
\]
This is the coefficient source of L-106080. L-106133.9--.11 gives the
canonical owner-pair share
\[
 B_U(a)=\frac{b_U(a)}{\binom{\omega(a)+2}{2}}.            \tag{CBPD3}
\]
There is no added selector weight in this definition. The factor follows
independently from \(2\int_0^1(1-\theta)\theta^h\,d\theta
=2/((h+1)(h+2))\), with \(h=\omega(a)\).

At \(a=1\), \(b_U(1)=1-2+1=0\), so \(B_U(1)=0\).
For \(h\ge1\), \(|\mu(a)-2\mu_U(a)|=1\) and the last convolution
has at most \(3^h\) signed summands. Thus
\[
 |B_U(a)|\le \frac{1+3^h}{\binom{h+2}{2}}\le 3^h.       \tag{CBPD4}
\]
This holds uniformly in the cutoff, without any asymptotic estimate.
In particular the usual \(U=\lfloor Y^{1/6}\rfloor\) is allowed.

## 3. Exact chart, measure, and theorem

Fix real \(Y\ge1\) and \(T=\lfloor16Y\rfloor\). A canonical atom is the
EXACT arithmetic tuple
\[
 {\mathfrak a}=(P,Q,g,c,d).
\]
Here \(g,c,d\) are squarefree, mutually coprime and 67-free; \(c,d>1\);
\(P,Q\) are products of two distinct owner primes, with all four owner
primes distinct and disjoint from \(gcd\). These conditions are the clean
ordinary-prime chart; discarding them in a nonnegative upper bound is allowed.
Set \(\ell=P^-(c)\), \(\rho=P^-(d)\), so \(\ell\ne\rho\).
The physical products are
\[
 N=Pg^2c^2,\qquad M=Qg^2d^2,\qquad N,M\le16Y.            \tag{CBPD5}
\]
Any of the narrower original windows, least-prime classes, ratio conditions,
or support selectors can be retained as masks \(m_{\mathfrak a}(t)\) with
\(|m_{\mathfrak a}(t)|\le1\). Class labels determined by the tuple do not
introduce an extra multiplicity. There is ONE atom per exact arithmetic
tuple: repeated carrier, shell, endpoint, amplitude, or history labels are
not covered by this convention and cannot be silently appended and summed.

The scalar Fourier realization of the unobserved canonical source is
\[
 A^B_{P,a}(t)=B_U(a)a^{-1-2it}P^{-1/2-it},\qquad
 z^B_{\mathfrak a}(t)=
 \frac{B_U(gc)B_U(gd)}{g^2cd\sqrt{PQ}}\,
 \exp\!\left(it\log\frac{Pc^2}{Qd^2}\right).             \tag{CBPD6}
\]
Indeed \(z^B=\overline{A^B_{P,gc}}A^B_{Q,gd}\): the common \(g\)-phase
cancels. All powers here use the real logarithm of positive integers.

Put \(c_q=(q+1)/(q-1)\), \(\kappa(u)=K(e^u)\) and
\(\widehat\kappa(t)=\int_{\mathbb R}\kappa(u)e^{-itu}\,du\).
The original measure and original principal diagonal are
\[
 d\mu(t)=|\widehat\kappa(t)|^2\,dt/(2\pi),\qquad
 D_B(Y)=\sum_{\mathfrak a}g^2\ell\rho c_\ell c_\rho
                 \int_{\mathbb R}|m_{\mathfrak a}(t)z^B_{\mathfrak a}(t)|^2d\mu(t).
                                                               \tag{CBPD7}
\]
Equivalently, \(\widetilde z=g\ell\rho z\) has principal weight
\(c_\ell c_\rho/(\ell\rho)\). These weights are NOT the complete additive
weights, which carry the additional conductor factors.

**Theorem.** For every such set of tuples, every \(U\ge1\), and every
measurable collection of masks of modulus at most one,
\[
 \boxed{D_B(Y)\le6C_\kappa\,\zeta(2)^{81}H_{\lfloor16Y\rfloor}^{22}
                  =Y^{o(1)},\quad
 C_\kappa=128(3+\sqrt2)\log2-288.}                        \tag{CBPD8}
\]
More precisely, for every \(\varepsilon>0\) the right side is at most
\(C_\varepsilon Y^\varepsilon\) for all \(Y\ge1\); constants are independent
of \(U\), the masks and any subset of the chart. Prime 2 is included in
this scalar diagonal estimate. This is not a claim about a characteristic-2
Kummer frame or about the excluded prime-67 chart.

## 4. The actual kernel constant, without numerical integration

The frozen L-102880.2 kernel, also used in L-106026, is
\[
 K(y)=
 \begin{cases}
 8-4\sqrt y,&1\le y<2,\\
 -8(1+\sqrt2)+4\sqrt2\sqrt y,&2\le y<4,\\
 8\sqrt2-2\sqrt y,&4\le y<8,\\
 0,&\text{otherwise}.
 \end{cases}                                           \tag{CBPD9}
\]
Plancherel and \(du=dy/y\) give
\[
 \int_{\mathbb R}d\mu=\int_1^8 K(y)^2\,dy/y=C_\kappa.
\]
For each piece \(A+B\sqrt y\), an exact integral on \([a,b]\) is
\[
 A^2\log(b/a)+4AB(\sqrt b-\sqrt a)+B^2(b-a).             \tag{CBPD10}
\]
All three ratios \(b/a\) equal 2. Summing in
\(\mathbb Q(\sqrt2)+\mathbb Q(\sqrt2)\log2\) yields log coefficient
\(384+128\sqrt2\) and constant \(-288\).
Positivity follows from the nonzero squared kernel, not decimal evaluation.

## 5. Proof of the global diagonal bound

By (CBPD4) and coprimality,
\[
 |B_U(gc)B_U(gd)|^2
       \le81^{\omega(g)}9^{\omega(c)}9^{\omega(d)}.
\]
The maximum of \(c_\ell c_\rho\) over DISTINCT primes is
\(c_2c_3=6\); also \(\ell\le c\) and \(\rho\le d\). Therefore the
principal-weighted pointwise squared amplitude is at most
\[
 6\,\frac{81^{\omega(g)}}{g^2}
       \frac{9^{\omega(c)}}c\frac{9^{\omega(d)}}d\frac1P\frac1Q.  \tag{CBPD11}
\]
Masks do not increase it. Integrating costs exactly \(C_\kappa\).
Every variable in (CBPD5) is at most \(T\). Dropping all incidence, window,
ordering and coprimality restrictions gives a product of nonnegative sums.

For the common square-core,
\[
 \sum_{g\ {\rm sf}}\frac{81^{\omega(g)}}{g^2}
   =\prod_p(1+81/p^2)\le\prod_p(1-p^{-2})^{-81}
   =\zeta(2)^{81}.                                      \tag{CBPD12}
\]
For squarefree \(n\), \(d_9(n)=9^{\omega(n)}\), and for every positive
integer \(r\)
\[
 \sum_{n\le T}\frac{d_r(n)}n
 =\sum_{n_1\cdots n_r\le T}\frac1{n_1\cdots n_r}\le H_T^r.
\]
Thus each of \(c,d\) costs \(H_T^9\). Each owner-product sum costs at most
\(H_T^2\): discard its distinct-prime and unordered-pair restrictions
and sum \(1/(uv)\) over positive integers \(u,v\le T\).
The total harmonic exponent is \(9+9+2+2=22\).
This proves (CBPD8). All infinite sums have nonnegative terms; monotone
limits justify their factorization. \(H_T\le1+\log T\) proves the stated
uniform subpower conclusion.

## 6. Precise remaining native map

The frozen principal estimate is L-106121.9 and T-106140.9--.10.
It bounds the fully labelled \(D_{\rm lit}\), not a diagonal chosen after
arbitrary labels have been forgotten. Signed-history recombination at the
base context pays its own history-only correction and retains other labels.

A proposed native identification still needs, at each retained tuple and
with all original windows and source coordinates, an identity of the form
\[
 \sum_{\lambda,\nu}M_{\mathfrak a}(\lambda,\nu;t)\,
       \overline{A_{{\mathfrak a}_L,\lambda}(t)}
       B_{{\mathfrak a}_R,\nu}(t)
       =m_{\mathfrak a}(t)z^B_{\mathfrak a}(t),\quad |m_{\mathfrak a}(t)|\le1.
                                                               \tag{CBPD13}
\]
The left labels mean actual retained carrier/endpoint/selector/shell/amplitude
coordinates, not invented coefficient freedom. A nontrivial aggregation may
fail to produce a bounded mask, or may require further coordinates and
multiplicities absent from the right. Neither failure is repaired by this
diagonal theorem.

L-102901's unobserved complementary-factor product identity does not prove
(CBPD13). L-106093 retains anchors and masks; L-106120 retains the bilateral
conditions; L-102963 explicitly warns about pair-dependent selectors.
We have not proved mask intertwining, nor equality of the corresponding
uncentered moments. The useful outcome is a candidate diagonal budget and
a precise unpaid \(P_{\rm nat}-P_B\), not a resolution-change or sign theorem.

## 7. Frozen sources and replay contract

The adjacent typed manifest pins eleven scientific blobs at
86cac1d64364015ec2cc0f8fbb6fc75dc041c12b and
ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc, plus one contextual blob at the
base commit. Each has its Git blob identity and LF-normalized SHA-256.
The producer reauthenticates all primitives and hashes this note, itself,
the test, and manifest. CRLF checkout conversion does not change those hashes.

The finite replay independently reconstructs (CBPD2) by three-part Boolean
allocation and the original convolution, checks the Beta/binomial share
including the empty support, compares original and rescaled principal
weights on two arithmetic controls, integrates (CBPD10) exactly, and checks
finite divisor-convolution/Euler majorants. These controls do not constitute
a numerical proof of Plancherel, an infinite Euler product, a Mellin integral,
a subpower limit, or the missing native mask identity.

Public numeric inputs are strict bounded integers/rationals; Boolean integers,
floats, non-primes, prime 67, repeated primes/tuples, excess support, bad
physical windows, and masks of modulus exceeding one fail closed. Source
roles, schemas, duplicate JSON keys, nonfinite JSON constants, byte/work caps,
artifact hashes and the canonical payload digest are checked. The symbolic
\(\log2\) constant is not rounded. Reproduction: run the adjacent producer
with --check and the corresponding unittest file, normally and with Python -O.

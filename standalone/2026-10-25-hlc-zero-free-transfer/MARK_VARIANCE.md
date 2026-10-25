# The exact cost of removing the auxiliary prime marks

Status: native finite identity and fixed-parameter asymptotic deduction.
Scope: the marks in Lü--Wang--Wu, arXiv:2610.20242v1, Section 2.3.
Dependencies: the classical prime number theorem, Mertens' prime estimate,
and Bombieri--Vinogradov, in the same ranges as the paper's Proposition 2.3.
What was actually run: exact rational CRT checks described in CHECKS.md.
Smallest remaining gap: no signed estimate for the mark-removal remainder
is supplied here. A variance identity is not a zero-free theorem.

This note makes the cost of the paper's final Cauchy--Schwarz step explicit.
It does not contradict its qualitative theorem and is not an impossibility
result for other methods.

## 1. A finite identity before taking any limit

Let \(\mathcal P_1,\ldots,\mathcal P_K\) be disjoint nonempty finite sets of odd
primes, and set

\[
 P=\prod_{i=1}^K\prod_{p\in\mathcal P_i}p,\qquad
 V_i=\sum_{p\in\mathcal P_i}\frac1p,\qquad
 N_i(a)=\#\{p\in\mathcal P_i:p\mid a+2\}.
\]

Take \(a\) uniformly among the reduced residue classes modulo \(P\).
The Chinese remainder theorem makes the events \(p\mid a+2\) independent,
with probability

\[
 \vartheta_p=\frac1{p-1}.
\]

The prime 2 is excluded: its local probability is different. Define

\[
 F_i(z)=\mathbb E z^{N_i}
       =\prod_{p\in\mathcal P_i}(1+\vartheta_p(z-1)).
 \tag{1}
\]

Fix \(0<\rho<1\). With \(0\rho^{-1}\) interpreted as zero, put

\[
 W(a+2)=\prod_{i=1}^K\frac{N_i(a)\rho^{N_i(a)-1}}{V_i}.
\]

Differentiating the finite polynomial (1) gives the exact identities

\[
 m=\mathbb EW=\prod_i\frac{F_i'(\rho)}{V_i},
 \qquad
 \mathbb E\left(\frac Wm\right)^2=\prod_i r_i,
 \quad
 r_i=\frac{F_i'(\rho^2)+\rho^2F_i''(\rho^2)}
                 {F_i'(\rho)^2}.
 \tag{2}
\]

Indeed \(F_i'(t)+tF_i''(t)=\mathbb E[N_i^2t^{N_i-1}]\);
take \(t=\rho^2\). No probabilistic approximation occurs in (1)--(2).

For \(b\) groups of \(K\) prime sets, all disjoint across groups, let
\(U_j=W_j/m_j\). Independence and \(\mathbb EU_j=1\) give

\[
 \boxed{\quad
 \mathbb E\left|\frac1b\sum_{j=1}^bU_j-1\right|^2
       =\frac1{b^2}\sum_{j=1}^b
                    \left(\prod_{i=1}^K r_{j,i}-1\right).
 \quad}                                                    \tag{3}
\]

This is an exact finite CRT-residue formula.

There is also a bound independent of the damping formula. Any normalized
nonnegative mark \(U\) supported on \(N_i\ge1\) for all \(i\) satisfies

\[
 \mathbb EU^2\ge
       \frac1{\mathbb P(N_1\ge1,\ldots,N_K\ge1)}
       =\prod_i(1-F_i(0))^{-1}.                            \tag{4}
\]

This follows from \(1=(\mathbb EU)^2\le
\mathbb P(U>0)\mathbb EU^2\). Thus the sparsity of the marks itself
forces a variance cost.

## 2. The limiting constant for the paper's bands

Write \(L=\log x\). The paper chooses

\[
 \mathcal P_i(x)=\{p:\exp(L^{a_i})<p\le\exp(2L^{a_i})\},
 \qquad 1/10<a_i<1/5,
 \tag{5}
\]

with all parameters fixed before \(x\) tends to infinity. Let
\(\lambda=\log2\). Mertens' estimate and the fact that the least
prime tends to infinity give

\[
 \sum_{p\in\mathcal P_i}\vartheta_p\longrightarrow\lambda,
 \qquad
 \sum_{p\in\mathcal P_i}\vartheta_p^2\longrightarrow0.
\]

Consequently \(F_i(z)\to\exp(\lambda(z-1))\) locally uniformly in
the complex plane, together with every fixed derivative. Inserting this
in (2) yields

\[
 \frac{F_i'(\rho)}{V_i}\longrightarrow e^{\lambda(\rho-1)},
 \qquad
 r_i\longrightarrow
 r(\rho)=\left(\rho^2+\frac1\lambda\right)
                         e^{\lambda(\rho-1)^2}.
 \tag{6}
\]

For fixed \(b,K,\rho\), equation (3) therefore tends to

\[
 \boxed{\qquad \frac{r(\rho)^K-1}{b}. \qquad}                \tag{7}
\]

Since \(1-F_i(0)\to1-e^{-\lambda}=1/2\), equation (4) also gives
\(r(\rho)^K\ge2^K\). The cost is at least
\((2^K-1)/b\), not a constant independent of the number of prime bands.

## 3. The same fixed-parameter limit along shifted primes

The limit (7) also holds for the weighted prime average

\[
 \frac1x\sum_{x<p\le2x}\log p\,
       \left|\frac1b\sum_j\frac{W_j(p+2)}{m_j}-1\right|^2.
 \tag{8}
\]

Here \(b,K,\rho\), and all the exponents in (5), remain fixed.
The following gives a justification without assuming that residue
equidistribution holds for the enormous product \(P\).

For any fixed collection of nonnegative integers \(r_i\), expand
\(\prod_i\binom{N_i(p)}{r_i}\) as a sum over distinct selected primes
in each band. The condition is a single reduced class
\(p\equiv-2\pmod d\), with

\[
 d\le\exp\!\left(2\sum_i r_i L^{1/5}\right)=x^{o(1)}.
\]

The coefficients of the expansion are bounded by a constant depending
only on the fixed orders. Bombieri--Vinogradov therefore supplies the
main term \(1/\varphi(d)\), with total error tending to zero after
division by \(x\). The resulting mixed factorial moments are
\(\prod_i\lambda^{r_i}/r_i!\), the moments of independent
Poisson variables of mean \(\lambda\).

The usual fixed-dimensional moment argument applies: higher fixed
factorial moments give uniform integrability of each moment, and the
Poisson distribution is determined by its moments (its moment generating
function is finite near zero). Thus the joint counts converge in
distribution to these independent Poisson variables. For fixed
\(0<\rho<1\), both \(j\rho^{j-1}\) and its square are bounded on
the nonnegative integers. The first and second moments of every mark
therefore converge. The normalizers \(m_j\) tend to positive constants.
Equation (8) has the limit (7).

This is also obtainable by carrying the paper's truncated divisor
expansion through \(W_j^2\). We do not infer any uniformity for growing
\(b\) or \(K\) from this fixed-parameter argument.

## 4. How many independent bands are available?

If the real intervals defining all \(bK\) bands in (5) are disjoint,
list their starting logarithms as \(t_1<\cdots<t_{bK}\).
Disjointness requires \(t_{j+1}\ge2t_j\), while
\(L^{1/10}<t_j<L^{1/5}\). Hence

\[
 bK\le1+\frac{\log L}{10\log2}.                            \tag{9}
\]

If only the sets of primes are disjoint, rather than the real
intervals, use harmonic mass instead. All primes lie between
\(\exp(L^{1/10})\) and \(\exp(2L^{1/5})\), whose total reciprocal
prime mass is

\[
 \frac1{10}\log L+\log2+o(1).
\]

Each band has mass \(\log2+o(1)\), uniformly over the allowed endpoints.
This still bounds the number of disjoint bands by \(O(\log L)\).

Even an additional uniform version of the present Cauchy--Schwarz
unmarking estimate would therefore give at best a logarithmic-scale
gain from the number of independent bands. In the fixed-parameter
statement actually proved in the source, no prescribed quantitative
choice \(b=b(x)\) is justified. A sufficiently slow diagonal choice can
exist without giving a specified rate.

The conclusion is about this estimate: a bound for the correlation by
the full \(L^2\) norm in (8) does not deliver an \(x^{-\eta}\) factor.
The actual correlation with the signed Möbius sequence can be much
smaller than that norm. Proving that smaller signed remainder would
be a different and potentially useful theorem.

## 5. What this suggests changing

A transfer toward RH has to retain the sign in

\[
 \sum_{x<p\le2x}\mu(p+2)\log p
       \left(1-\frac1b\sum_jU_j(p+2)\right),
\]

or use a different reconstruction. Making the existing \(K\) or \(b\)
larger while keeping the same absolute Cauchy--Schwarz estimate does not
supply the missing power saving. Likewise, the source's theorem for a
fixed nonzero additive shift does not supply the multiplicative,
conductor-uniform correlation in NATIVE_AFFINE_REDUCTION.md.

This isolates a concrete analytic task. It is not a claim that the
paper's theorem is false, that all possible mark designs have this
cost, or that no stronger shifted-correlation theorem can be proved.

# Exact second moment and the sharp two-moment sign floor

**Status:** exact consequence theorem for every odd prime power \(q\).
The packet closes the previously open second moment of the genus-two toy
minor. It also proves an optimality firewall: support and the first two
moments alone cannot improve its Cantelli sign bound.

**Exact dependencies:** the separately proved all-\(q\) formulas for
\(\mathbb E[K_D]\), \(\mathbb E[a_D^4]\),
\(\mathbb E[a_D^2b_D^2]\), and \(\mathbb E[b_D^4]\), together with the
exact \(USp(4)\) support range \([-20,4/3]\). Their fixtures are
source-locked by canonical and LF-normalized SHA-256. The locked
\(q=3,5,7\) histograms are used only as held-out controls.

**What was run:** 384 guarded Laurent-algebra updates, 226 exact
translation-coefficient accumulations, and 89 atoms from the already-frozen
\(q=3,5,7\) histograms as held-out falsification controls. The theorem replay
enumerates no finite field, quintic, curve, or family.

**Smallest remaining gap:** a better unconditional negative-density theorem
must use at least a third moment, constrain the zero atom, or import genuine
arithmetic/geometric structure. Re-optimizing a quadratic inequality cannot
do it.

## 1. The exact second moment

For all monic squarefree quintics \(D\in\mathbf F_q[T]\), put

\[
 K_D=q a_D^2-b_D^2,\qquad Z_D=\frac{K_D}{q^2}.
\]

The exact reduction

\[
 \mathbb E[K_D^2]
 =q^2\mathbb E[a_D^4]
  -2q\mathbb E[a_D^2b_D^2]
  +\mathbb E[b_D^4]
\tag{1}
\]

now has all three inputs proved. Exact substitution and collection gives

\[
\boxed{
 \mathbb E[K_D^2]
 =
 \frac{
  3q^7-8q^6+6q^5+8q^4-9q^3-19q^2-4q-1
 }{q^3}.}
\tag{2}
\]

Equivalently,

\[
\boxed{
 \mathbb E[Z_D^2]
 =
 \frac{
  3q^7-8q^6+6q^5+8q^4-9q^3-19q^2-4q-1
 }{q^7}
 \longrightarrow 3.}
\tag{3}
\]

Combining (2) with

\[
 \mathbb E[K_D]=-(q-1)^2+\frac{q+1}{q^3}
\]

also gives

\[
\boxed{
 \operatorname{Var}(K_D)
 =
 \frac{q+1}{q^6}
 \left(
 2q^9-6q^8+6q^7+6q^6-14q^5-7q^4+q^3-q-1
 \right).}
\tag{4}
\]

Thus \(\operatorname{Var}(Z_D)\to2\). These limits agree with the relevant
\(USp(4)\) Haar moments, but this packet does not infer equidistribution from
that agreement.

## 2. An exact all-\(q\) density floor

Write

\[
\begin{aligned}
 P(q)&=q^5-2q^4+q^3-q-1,\\
 N(q)&=3q^7-8q^6+6q^5+8q^4-9q^3-19q^2-4q-1.
\end{aligned}
\]

Then

\[
 \mathbb E[Z_D]=-\frac{P(q)}{q^5},
 \qquad
 \mathbb E[Z_D^2]=\frac{N(q)}{q^7}.
\]

Cantelli's one-sided variance inequality, applied at the threshold \(0\),
therefore proves

\[
\boxed{
 \Pr(K_D<0)
 \geq
 C(q):=\frac{P(q)^2}{q^3N(q)}.}
\tag{5}
\]

There is no asymptotic or equidistribution input in (5). The producer proves
positivity by translating every controlling polynomial to \(q=t+3\), where
all coefficients are strictly positive.

The bound is strictly increasing for every real \(q\geq3\). Indeed,

\[
 C'(q)=\frac{P(q)D(q)}{q^4N(q)^2},
\]

where

\[
\begin{aligned}
D(q)={}&4q^{11}-16q^{10}+48q^9-40q^8-93q^7+54q^6\\
      &+94q^5+22q^4-114q^3-103q^2-17q-3,
\end{aligned}
\]

and every coefficient of \(D(t+3)\) is positive. Consequently

\[
\boxed{
 \frac{1352}{8127}=C(3)
 \leq \Pr(K_D<0),
 \qquad
 \lim_{q\to\infty}C(q)=\frac13.}
\tag{6}
\]

Moreover \(C(q)<1/3\) for finite \(q\geq3\), again by a coefficientwise
positive translated numerator. Its first asymptotic terms are

\[
 C(q)=\frac13-\frac{4}{9q}+\frac{4}{27q^2}+O(q^{-3}).
\tag{7}
\]

The previous range-only argument gave

\[
 \Pr(K_D<0)\geq\frac{P(q)}{20q^5},
\]

with limit \(1/20\). Exact subtraction shows

\[
 C(q)-\frac{P(q)}{20q^5}
 =
 \frac{P(q)G(q)}{20q^5N(q)}>0
\tag{8}
\]

for every \(q\geq3\), because

\[
G(q)=17q^7-32q^6+14q^5-8q^4-11q^3-q^2+4q+1
\]

also has strictly positive coefficients after \(q=t+3\).

## 3. Why the two-moment method is now exhausted

The exact compact-group range already gives

\[
             -20\leq Z_D\leq \frac43.
\tag{9}
\]

One might hope that optimizing a different quadratic minorant of
\(\mathbf1_{\{z<0\}}\) on this finite interval improves (5). It cannot.

Define

\[
 x_q=\frac{\mathbb E[Z_D^2]}{\mathbb E[Z_D]}
     =-\frac{N(q)}{q^2P(q)}.
\tag{10}
\]

The same translated-positivity certificate used in (8) proves

\[
 20q^2P(q)-N(q)=G(q)>0.
\]

Hence

\[
                  -20<x_q<0.
\tag{11}
\]

Now put mass

\[
 \rho_q=\frac{\mathbb E[Z_D]^2}{\mathbb E[Z_D^2]}=C(q)
\]

at \(x_q\), and the remaining mass at \(0\). This two-point probability law
lies inside the known support (9), has exactly the same first and second
moments as \(Z_D\), and has negative mass exactly \(C(q)\).

Therefore:

\[
\boxed{\text{The bound (5) is optimal among all deductions using only
support, mean, and second moment.}}
\tag{12}
\]

The saturating two-point law is an information-theoretic witness, not a claim
about the arithmetic family. Its role is to identify the next genuine
theorem gate: another moment, a zero-atom theorem, or geometric stratification
is logically necessary.

## 4. Held-out checks and claim boundary

The \(q=3,5,7\) joint histograms were not used to derive (2). After the
formula was fixed, their exact \(K_D^2\) sums were checked:

| \(q\) | members | \(\sum_DK_D^2\) | \(\mathbb E[K_D^2]\) |
|---:|---:|---:|---:|
| 3 | 162 | 14,448 | \(2408/27\) |
| 5 | 2,500 | 2,630,080 | \(131504/125\) |
| 7 | 14,406 | 69,108,480 | \(1645440/343\) |

This packet proves no limiting sign law, memberwise sign, equidistribution,
RH, or GRH result. \(K_D\) remains a toy reciprocal-coefficient minor, not
canonical XD, HCNC, or a Pick/Loewner detector.

## 5. Replay

From the repository root:

    python -B research/l-families/atlas/function_field/genus2_toy_minor_second_moment.py --check
    python -B -O research/l-families/atlas/function_field/genus2_toy_minor_second_moment.py --check
    python -B -m unittest tests.test_genus2_toy_minor_second_moment -v
    python -B -O -m unittest tests.test_genus2_toy_minor_second_moment -v

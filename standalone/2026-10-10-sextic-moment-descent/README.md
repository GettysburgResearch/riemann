# Sextic inverse moments: proved partial ranges and the remaining \(17/24\) problem

**Status: proposed research with complete component proofs and scoped independent review. The full fourth moment, the \(17/24\) zero-free boundary, the unbounded moment hierarchy, and RH remain unproved here.**

This packet continues [PR #910](https://github.com/GettysburgResearch/riemann/pull/910) at commit 670a76c1a3a8f325c43c1755b1cfc24d313a3e3c. Its purpose is to attack the actual fourth moment and general \(2k\)-th moments identified in the [preceding packet](../2026-10-10-quasi-riemann-height-descent/README.md). The previous packet and the complete source import are preserved.

The main new analytic result is an all-row sextic sieve:

\[
\boxed{
\sum_{0<Nu\le H}\left|
\sum_{\substack{n\ {\rm squarefree},\ (n,S)=1\\Nn\le L}}z_n\chi_n(u)
\right|^2
\ll_{S,\epsilon}(HL)^\epsilon
\left[H+(HL)^{2/3}+H^{1/6}L\right]\sum_n|z_n|^2.
}
\]

It retains every nonzero element row and every nonunit zero of the character. It applies to arbitrary complex squarefree-column coefficients, including moving coprimality masks fixed before the row average. It is a deduction from classical character sieves and elementary ideal arithmetic, independent of the imported quasi-RH conclusion. No claim of external novelty is made.

This estimate improves the first all-row argument's \(H^{1/2}L\) loss to \(H^{1/6}L\). It proves the desired moment scale for specified portions of every fixed moment, and enlarges the controlled common-divisor range of the sixth and higher moments. The long product columns with little overlap remain unresolved.

## What to read

| Component | Complete proof | Scope |
|---|---|---|
| Stronger all-row sextic sieve | [Refined sieve](REFINED_ALL_ROW_SIEVE.md), Theorem 3.4 | Classical inputs; no quasi-RH or new moment assumption |
| Exact decomposition and proved parts of every moment | [General moments](GENERAL_MOMENT_ATTACK.md), Sections 1–4 | All rows, all shared-prime patterns, explicit uniform exclusions |
| A coupled correlation estimate using another OpenAI paper | [Sextic Gram estimate](SEXTIC_GRAM_BOUND.md) | Direct off-diagonal character correlation; its moment consequence is limited |
| Closure of balanced divisor weights under the two-Poisson transfer | [Structured transfer](FOURTH_MOMENT_ATTACK.md), Sections 3–4 | Conditional on the named imported arithmetic/Poisson interfaces; completion and initialization remain open |
| A weaker full \(2k\)-moment with conductor uniformity proved | [Weaker moments](FOURTH_MOMENT_ATTACK.md), Section 8 | Uses the imported second moment and a common zero-free half-plane |
| Exact exceptional-row and bootstrap analysis | [Obstructions and hierarchy](MOMENT_OBSTRUCTIONS.md) | Complete identities, a rectangular-moment qualification, and an RH-level equivalence |
| Positive-density extraction with no prime-counting logarithm | [Extraction](GENERAL_MOMENT_ATTACK.md), Section 6 | Conditional on the stated input moment; preserves its exact exponent |
| Initial simpler large-gcd proof | [Initial sieve and fourth-moment tail](ALL_ROW_SIEVE_AND_GCD_TAIL.md) | Valid earlier deduction, improved quantitatively by the refined sieve |
| Independent review, checks, and source hashes | [Review](INDEPENDENT_MOMENT_REVIEW.md), [validation](VALIDATION.md), [provenance](PROVENANCE.json) | AI-agent source review and finite arithmetic checks; no Lean build |

## 1. The target and its exact significance

Work over \(K=\mathbb Q(\sqrt{-3})\). Fix a finite-order Hecke character \(\nu\), a finite bad-prime set \(S\) containing the primes above 6 and those dividing the conductor of \(\nu\), and a fixed smooth compactly supported test \(W\). With the original primary-generator and zero-extension conventions, set

\[
A_u(D;W)=\sum_{(n,S)=1}\mu_K(n)\nu(n)\chi_n(u)W(Nn/D),
\qquad \chi_n(u)=(u/n)_6.
\]

The target is

\[
\mathcal M_{2k}(D,H)=\sum_{0<Nu\le H}|A_u(D;W)|^{2k}
\ll D^{k+\epsilon}H,
\qquad H=D^{1+\theta}.
\tag{T}
\]

For the limiting constants below, \((T)\) must hold for arbitrarily small fixed \(\theta>0\), all sufficiently large scales, all rows, and every fixed smooth test needed by Mellin continuation. A numerical sample or a statement with the sixth-power rows removed does not supply these quantifiers.

The exact sixth-power extraction then gives

\[
|A_1(D;W)|\ll D^{\,1/2+5(1+\theta)/(12k)+\epsilon}.
\]

Thus the limiting consequences of the **unproved full moments** are:

| Full input moment | Resulting limiting zero-free boundary |
|---|---:|
| Fourth, \(k=2\) | \(17/24=0.708333\ldots\) |
| Sixth, \(k=3\) | \(23/36=0.638888\ldots\) |
| Eighth, \(k=4\) | \(29/48=0.604166\ldots\) |
| General fixed \(k\) | \(1/2+5/(12k)\) |

The unbounded hierarchy would settle an RH-level statement outright. [Theorem 10.1](MOMENT_OBSTRUCTIONS.md) proves that, at any one fixed polynomial row scale \(H=D^h\), diagonal moments for unbounded fixed orders and every fixed smooth test are equivalent to GRH for the entire associated sextic row-twist family. With \(\nu=1\), that includes ordinary RH through \(\zeta_K=\zeta L(\chi_{-3})\). The converse requires GRH for that whole family.

Here \(H\) measures the norm range of an auxiliary arithmetic row. It is separate from the imaginary height \(T=\operatorname{Im}s\) in the preceding packet's height-local detector. No new shrinking band in \(T\) is proved in this pass.

## 2. How the stronger sieve works

Every row has an exact valuation decomposition

\[
u=\varepsilon\,v^6a_1a_2^2a_3^3a_4^4a_5^5,
\]

where the \(a_j\) are squarefree and pairwise coprime. The ideal \(v\) may share primes with them. Its character contribution is exactly the mask \(\mathbf1_{(n,v)=1}\), which stays in the column coefficient.

On a dyadic block take lower endpoints \(A_j\le Na_j<2A_j\) and \(V\le Nv<2V\), and write \(P_0=\prod_j A_j\), \(B=VP_0\), and \(M=\max_j A_j\). The exact norm constraint then implies \(V^6\prod_j A_j^j\le H\).

There are two complementary estimates for the same block. Varying the largest squarefree factor gives a cost bounded by

\[
B+\frac{BL}{M}+\frac{BL^{2/3}}{M^{1/3}}.
\]

Alternatively, after fixing \(v\), the entire remaining core defines a primitive character whose good-prime conductor has norm comparable to \(P_0\). The local character recovers each exponent \(j\); multiplicity from units and bad primes is bounded. The ordinary primitive-character sieve gives

\[
V(L+P_0^2).
\]

The key exact inequality is

\[
\left(\frac{BL}{M}\right)^2(VP_0^2)\le H^2L^2.
\]

Consequently the smaller of these two troublesome terms is at most \((HL)^{2/3}\). Also \(B\le H\), \(B/M^{1/3}\le H^{2/3}\), and \(V\le H^{1/6}\). Summing the logarithmically many blocks gives the displayed refined sieve. The proof keeps the conductor distinction and the sixth-power masks throughout.

The classical sources are Blomer–Goldmakher–Louvel's [higher-order sieve](https://arxiv.org/abs/1112.1650), Goldmakher–Louvel's [quadratic sieve](https://arxiv.org/abs/1112.1642), and the planar additive sieve. The ordinary primitive-character step is proved from Gauss sums, character orthogonality and planar spacing in the note.

## 3. What is now proved inside the actual moments

Expand the ordinary \(k\)-th power before taking its absolute square. A prime dividing precisely the factors with indices in \(I\subseteq\{1,\ldots,k\}\) belongs to one shared ideal \(c_I\). This assignment is unique. After fixing the shared ideals with \(|I|\ge2\), the remaining singleton factors have product scale

\[
P(\mathbf c)=D^k\prod_{|I|\ge2}(Nc_I)^{-|I|}.
\]

The remaining squarefree column has the exact \(k\)-factor divisor weight. Its coefficient square norm is \(O(D^\epsilon P)\). The refined sieve therefore proves

\[
\|B_{C,\cdot}(\mathbf X)\|_2^2
\ll D^\epsilon
\left[HP+H^{1/6}P^2+H^{2/3}P^{5/3}\right].
\]

The normalized summation over shared ideals costs only logarithms for pair overlaps; incidences of size at least three have convergent sums. This proves the target \(HD^{k+\epsilon}\) for the full specified part with \(P(\mathbf c)\le H^{1/2}\).

A second proved range is the common-gcd tail. Let \(G_{\ge C}^{(k)}\) be exactly the part of \(A_u(D)^k\) whose original tuple has common-divisor norm at least \(C\). Then

\[
\boxed{
\|G_{\ge C}^{(k)}\|_2^2
\ll D^\epsilon
\left[
HD^k+H^{1/6}D^{2k}C^{2-2k}
+H^{2/3}D^{5k/3}C^{2-5k/3}
\right].
}
\]

It has the target size when

\[
C\ge\max\left\{
1,\,
(D^k/H^{5/6})^{1/(2k-2)},\,
(D^{2k}/H)^{1/(5k-6)}
\right\}.
\]

For \(H=D^{1+\theta}\), \(0<\theta\le1/10\):

| Moment | Common-divisor range now controlled at the target size |
|---|---|
| Fourth | \(C\ge D^{(3-\theta)/4}\) |
| Sixth | \(C\ge D^{(5-\theta)/9}\) |
| Eighth | \(C\ge D^{(19-5\theta)/36}\) |

These exponents describe common-divisor cutoffs. The sixth-moment cutoff improved from \(D^{(5-\theta)/8}\) in the first argument to \(D^{(5-\theta)/9}\). The fourth-moment cutoff did not change because its mixed sieve term is still limiting.

These are bounds for actual portions of the expanded polynomial, including all their interference. They are not estimates for the entire moment. In particular, the fourth-moment remainder still contains \(c=1\), where two coprime factors each have norm about \(D\), and the product column has length about \(D^2\). Large common divisors represent a restricted portion of the tuples; controlling them does not control the dominant nearly coprime range.

## 4. The connection to OpenAI's cubic Gauss-sum work

The source import also points to a useful argument in family 023, *An unconditional first moment for cubic Gauss sums*. Adapting its Poisson correlation argument to sextic characters gives the following new component proof. For fixed squarefree primary \(p\) of norm about \(P\), define

\[
T_{p,p'}(Z)=\sum_{n\equiv1\ (3)}
W(Nn/Z)\chi_p(n)\overline{\chi_{p'}(n)}.
\]

Here \(n\) is unrestricted apart from the primary condition; \(W\) is a fixed smooth radial test, and the squarefree moduli are outside the fixed bad-prime set. Then

\[
\boxed{\sum_{\substack{Np'\asymp P\\p'\ {\rm squarefree},\ (p',S)=1\\p'\ne p}}
|T_{p,p'}(Z)|^2
\ll(PZ)^\epsilon\left[PZ+P^2Z^{1/3}\right].}
\]

The proof removes the common-prime mask exactly, applies lattice Poisson summation, and separates the smooth modulus dependence before the character sieve. A bounded-coefficient extension to unrestricted inner frequencies provides the saving. The sextic Gauss phase is retained as a row scalar; the cubic simplification of that phase is not used. The note proves the required extension and the normalized large-values corollary.

This controls signed off-diagonal correlations. Its direct use still falls short at the main fourth-moment product scale \(P\asymp D^2\), \(Z\asymp H=D^{1+\theta}\). For example, its second term improves on the elementary bound \(PZ^2\) only when \(Z>P^{3/5}\), whereas the small-\(\theta\) target has \(Z\asymp P^{(1+\theta)/2}\). A further use of the actual balanced Möbius coefficients is required. The complete adapted proof and exact pinned source paths are in [SEXTIC_GRAM_BOUND.md](SEXTIC_GRAM_BOUND.md). A separate [direct-composition proof](GRAM_MOMENT_COMPOSITION.md) shows that the resulting arbitrary-coefficient moment estimate adds no range beyond the refined sieve; it records the exact all-row adapter and the recovered fourth-moment gcd cutoff.

## 5. What the imported machinery now supplies, and where it stops

The balanced divisor weights form a closed class under the source's two-Poisson transfer. The exact residual coefficient becomes \(v(rf'n)\), identically across the signed preimages. Allocating its primes among factor axes, separating the coupled smooth kernel before Cauchy, and removing exclusions afterward preserves the source normalizer and child-scale inequalities. This extends to every fixed number of factor axes.

Two further estimates are still needed for a fourth-moment proof by this route. The original completed cubic-theta reflection has not been extended to the balanced divisor coefficient. Separately, the initial fourth-moment Poisson formula has dual row scale \(D^{3-\theta}\) and product-column scale \(D^2\). Their ratio is \(D^{1-\theta}\), while the available canonical theorem needs a power smaller than one. Extending the transfer class alone does not change this ratio.

There is also a genuine weaker full moment. From a common zero-free boundary \(\beta>1/2\) and the imported second moment, the packet proves

\[
\mathcal M_{2k}(D,H)\ll H D^{1+2(k-1)\beta+\epsilon}.
\]

Its proof supplies uniform conductor dependence, so it applies to the moving rows. At the preceding packet's conditional \(\beta=139999/160000\), the fourth moment becomes

\[
\mathcal M_4(D,H)\ll H D^{2.7499875+\epsilon}.
\]

The target exponent is \(2\). Extracting from the weaker general bound gives \(\beta+(11/6-2\beta)/(2k)\), which approaches the existing \(\beta\) from above. It cannot lower that boundary. Likewise, deleting exceptional rows and restoring them using the existing \(\beta\) returns \(\beta\) unchanged.

**No further improvement to the zero-free boundary is established in this packet.** The retained boundary is the preceding conditional \(139999/160000\), with its original upstream verification limits.

## 6. Computation and the next analytic obligation

The diagnostic implements the actual sextic residue symbols over split and inert prime ideals, not a model of random phases. It includes every element row in eight finite norm balls, at \(D=64,\ldots,8192\), with \(H=\lceil D^{1.1}\rceil\), \(\nu=1\), and the fixed smooth bump in [the program](checks/sextic_moment_probe.py). Moments through order twelve are recorded.

The largest panel has 73,140 rows and 1,145 nonzero-weight squarefree ideal columns. The symbol arithmetic and independent norm-coefficient checks are exact. The bump, complex sums and moments use ordinary binary64 arithmetic. The [validation report](VALIDATION.md) states the coverage and reproduction commands. No finite panel is used as proof of a uniform moment estimate.

The remaining analytic obligation is cancellation in the long balanced cores, with every row retained. The most concrete available paths are a coupled theta completion together with control of the adverse initial dual range, or a direct signed four-column estimate that uses the literal Möbius/divisor coefficients. The new Gram estimate supplies a checked character-correlation component for the latter direction. Its smooth unweighted correlation bound still needs a justified connection to the inverse-moment coefficients.

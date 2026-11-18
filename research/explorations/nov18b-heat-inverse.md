# The Dirichlet inverse of the positive heat coefficients

**Proposed lemma.** For \(u\ge0\) put \(a_u(n)=\exp(u\log^2 n)\), the coefficient in the positive-time heat Dirichlet wave. Let \(b_u\) be its algebraic Dirichlet inverse, so \(a_u*b_u=\mathbf 1_{n=1}\). Then
\[
                      |b_u(n)|\le a_u(n)\quad(n\ge1).
\]
This includes integers with repeated prime factors. In particular the exact inverse on a prefix is available without any loss from counting ordered factorizations. No convergence for the full positive-time Dirichlet series is assumed. These are the weights in Polymath15's finite Riemann–Siegel expansion. [Polymath15, Theorem 1.3](https://arxiv.org/abs/1904.12438)

## A finite random graph gives the coefficient exactly

Label the \(e_p\) occurrences of each prime in \(n=\prod p^{e_p}\). Independently connect each pair of labels carrying primes \(p,q\) by an edge with probability \(1-e^{-2u\log p\log q}\), including pairs carrying the same prime. Independently choose a uniform permutation of the labels within each equal-prime group. Adjoin edges joining all labels belonging to a common cycle of these permutations. Let \(C\) count the connected components of the resulting graph. Then
\[
                       b_u(n)/a_u(n)=\mathbb E(-1)^C.         \tag{1}
\]

For \(n>1\), expand the Dirichlet inverse as the finite alternating sum over ordered factorizations into \(j\ge1\) factors exceeding one. For a fixed labelled ordered partition into corresponding nonempty blocks, the product of the \(a_u\) values divided by \(a_u(n)\) equals the probability that no random edge crosses a block boundary, by expanding the square of the sum of the logarithms. Ordered factorizations are the orbits of these labelled ordered partitions under the product of the equal-prime symmetric groups. Averaging their invariant weight over fixed points of a uniform group element counts each orbit's weight once, by the orbit–stabilizer theorem. A partition fixed by the group element must also keep every permutation cycle in a single block. Therefore the expectation that remains is the signed count of all ordered partitions of the connected components of the augmented graph. For any fixed number \(k\) of components the signed count is \(\sum_{j=0}^k(-1)^j j!\,{k\brace j}=(-1)^k\), by evaluating the falling-factorial expansion of \(x^k\) at \(x=-1\). This proves (1); the empty graph handles \(n=1\).

At \(u=0\) the formula reduces to the usual Möbius coefficient. Coupling the permutations at times zero and \(u\) bounds the normalized perturbation from \(\mu(n)\) by twice the probability of at least one random edge, hence
\[
 \big|b_u(n)/a_u(n)-\mu(n)\big|
 \le 2\left[1-e^{-u(\log^2 n-\sum_{p^e\parallel n}e\log^2p)}\right].
\]
In particular \(b_u(p)=-a_u(p)\) for every prime, at every time.

## Positive connected coefficients in the formal Euler logarithm

There is a further exact identity. Let \(\ell_u(1)=0\), and let \(\ell_u\) be the formal Dirichlet logarithm of \(a_u\), computed coefficientwise from \(\log(1+v)\) with \(v=a_u-\mathbf 1_{n=1}\). For every \(n>1\),
\[
 \ell_u(n)=a_u(n)\Pr(C=1).
\]
Indeed the same ordered-partition proof now weights \(j\) blocks by \((-1)^{j-1}/j\). For fixed \(k\) components,
\(\sum_{j=1}^k(-1)^{j-1}(j-1)!\,{k\brace j}=\mathbf 1_{k=1}\), as follows by comparing the coefficients in \(\log(e^x)=x\). Thus every coefficient of the formal logarithm is nonnegative. At time zero, only single cycles on identical prime labels contribute, giving \(\ell_0(p^k)=1/k\) and zero at other integers.

More generally, for every complex \(z\), the formal Dirichlet power \(a_u^{*z}=\exp_*(z\ell_u)\) satisfies
\[
                     a_u^{*z}(n)=a_u(n)\mathbb E z^C .
\]
The expansion for \((1+v)^z\) weights an ordered partition into \(j\) blocks by \(\binom zj\), so the sum conditional on \(C=k\) is the falling-factorial expansion of \(z^k\). Consequently \(|a_u^{*z}(n)|\le a_u(n)\) throughout the closed unit disk. These are finite coefficient identities for the heat deformation.

## A consequence for an arithmetic mollifier

For \(1\le K\le N\), use exactly \(\sum_{d\le K}b_u(d)d^{-s}\) on \(\sum_{n\le N}a_u(n)n^{-s}\). The product has constant 1 and all its coefficients on \(2\le n\le K\) vanish. At \(n>K\) the absolute residual coefficient is bounded by
\[
 a_u(n)\sum_{d\mid n,\ d\le K,\ n/d\le N}
               e^{-2u\log d\log(n/d)}.
\]
For \(n\le N\), the inverse identity allows use of the complementary sum over \(d>K\) instead whenever smaller. The coefficientwise estimate applies to the actual positive-time deformation at a finite cutoff, including every phase. It does not give cancellation of the residual beyond \(K\) by itself.

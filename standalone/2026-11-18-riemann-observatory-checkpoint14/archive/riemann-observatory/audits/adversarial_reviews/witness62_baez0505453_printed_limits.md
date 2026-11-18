# Báez-Duarte, arXiv:math/0505453v1, printed limits in §2

I inspected rendered pp. 4 and 6 of the pinned first version. The statements below concern that manifestation. [Primary PDF](https://arxiv.org/pdf/math/0505453v1)

The inspected PDF has SHA-256 digest `ae798c555cdb8a503ed09ffb396b954a1da1786cd9d662ddf03f7d37b4118d70`.

## Lemma 2.1 and its proof

Page 4 prints the conclusion with lower integration limit \(0\). For the admissible smooth \(f(t)=e^{-t}\), even the \(n=1\) integral \(\int_0^1 e^{-x}dx/x\) is infinite. Indeed for any nonzero \(f\) modulo null sets, Tonelli and invariance under \(u=nx\) give the same strictly positive, possibly infinite integral for every \(n\) over the full positive ray. The proof instead starts from a fixed \(\varepsilon>0\) and proves the valid claim
\[
 \int_\varepsilon^\infty\sum_{n\ge1}|f(nx)|\frac{dx}{x}
 =\int_\varepsilon^\infty \lfloor u/\varepsilon\rfloor |f(u)|\frac{du}{u}
 \le\varepsilon^{-1}\int_\varepsilon^\infty |f(u)|du.
\]
Taking a countable exhaustion by positive lower endpoints gives the almost everywhere existence used later. The original attribution in the preprint is to Burnol. This check does not assign the typo to Burnol's original.

## Proposition 2.2, equations (2.8)–(2.9)

The two limits on p. 6 are printed without their minus signs. The exact finite formulas are
\[
 \int_0^T t f'(t)dt=T f(T)-\int_0^T f(t)dt
 \quad\text{and}\quad
 \int_0^T \sum_{n\ge1}\chi(nx/t)f'(t)dt
 =\lfloor T/x\rfloor f(T)-\sum_{n\le T/x}f(nx).
\]
For each finite \(T\) and \(x>0\) the second sum is finite, so no monotone convergence for complex \(f'\) is needed there. Under the good-kernel hypotheses, \(T f(T)\to0\). The sum of \(|f(nx)|\) converges for almost every \(x>0\) by the correctly truncated lemma. For such \(x\), the two limits are \(-\int_0^\infty f(t)dt\) and \(-\sum_{n\ge1}f(nx)\), respectively. The same smooth \(e^{-t}\) gives a strictly negative limit in each formula where the printed one is positive. Combining the corrected limits in the order of (2.7) gives
\[
 \int_0^\infty \rho(t/x)f'(t)dt
 =\sum_{n\ge1}f(nx)-x^{-1}\int_0^\infty f(t)dt
 =Pf(x).
\]
Thus the conclusion of Proposition 2.2 and the sign in identity (2.5) remain valid. The Mellin calculation has the corresponding cancellation of the two minus signs in \(-\zeta(s)/s\) and \(\int t^sf'(t)dt=-s\widehat f(s)\). The two directions of Theorem 1.2 use the repaired convolution and Mellin identities without a change to their hypotheses or conclusions.

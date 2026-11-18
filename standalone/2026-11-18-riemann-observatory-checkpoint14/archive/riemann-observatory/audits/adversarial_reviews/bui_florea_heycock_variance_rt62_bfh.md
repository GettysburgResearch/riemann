# Variance checkpoint challenge in Bui–Florea–Heycock v1

Independent reviewer rt_repair_62, PAPER-LATEST62-003. Source [arXiv:2610.27591v1](https://arxiv.org/pdf/2610.27591v1), local PDF SHA256 471eef2f839d4e67f9018c58d8a7fd529dc7bd10271c4b008bfba541d046d555. I compared rendered pp. 15–16, 27–28 and 41 with extracted Lemma 2.3, §§4–6, and the stated §7–8 dependencies. The review concerns the literal variance comparison and its uses in the preprint's small-shift tail argument, conditional on its other localization and tail inputs.

## Parameters and variance

Let \(h=\log\log T\), \(A=\alpha\log T\), and \(B=\log(1/\alpha)=h-\log A\). Equation (4.1) means \(M_0\le A\le M_1 B^{12+\varepsilon}\) for fixed \(M_0,M_1>0\). Under (4.2), \(\beta_1=h^{-30}\), \(\beta_j=r^{j-1}\beta_1\), \(T_j=T^{\beta_j}\), \(r>1\) is fixed, and \(\theta/r<\beta_K\le\theta\) for fixed sufficiently small \(\theta\). Set \(z_\ell=-\log\beta_\ell\) and \(c_\ell=e^{z_\ell/90}\). Here \(\ell\) is the upper prime checkpoint and \(j\ge\ell\) determines the coefficients, so a large \(j\) does not make the prime sum reach \(T_j\).

Consider \(A=h\), \(\ell=2\), and \(j=K\). One has \(B=h-\log h\), so (4.1) holds for all sufficiently large \(T\), and \(K\ge2\). The hypotheses of Lemma 2.3 hold: \(T_2\to\infty\), \(T_2\le T^{1/4-\epsilon_0}\) for any fixed \(0<\epsilon_0<1/4\) eventually, \(\alpha\ge T_K^{-1}\) as \(\beta_K\) is bounded below, and \(0<\alpha<1\). Also \(\alpha\log T_K=h\beta_K\to\infty\). By the first case of Lemma 2.3 and equation (4.4),
\[
 \sigma_{2,K}^2=\tfrac12(h-30\log h+\log r)+O(1).
\]
The difference from \(B/2\) is \(-\tfrac{29}{2}\log h+O(1)\), unbounded in absolute value. The use on p. 27 can itself access \((2,K)\) by taking the Lemma 6.1 event checkpoint \(\ell=3\), which uses \(\sigma_{\ell-1,j}\), or in Lemma 6.2 directly at \(\ell=2\). Neither choosing smaller fixed \(\theta\) nor imposing \(r\) close to one changes this limit. The \(1/2\) is already the factor in the real polynomial's second moment (2.3). Subtracting the mean squared cannot eliminate the divergence: the mean has size \(o(1)\) by integrating each nonconstant frequency (giving \(O((T\log n)^{-1})\)) and bounding the sum of absolute coefficients using Lemma 2.2 and \(T_2^2=T^{o(1)}\). Thus the two displayed estimates (4.4) and uniform (6.4) are incompatible in this admissible regime.

## Replacement and barrier accounting

Equation (4.4) gives the uniform estimate
\[
 \sigma_{\ell,j}^2=B/2+O(1+z_\ell^2).
\]
Indeed \(B-t_\ell=\max(0,z_\ell-\log A)=O(1+z_\ell)\), and (4.4) supplies the rest. As \(z_\ell\le30\log h\) and \(B=h+O(\log h)\), all variances are comparable to \(B\). For \(|u|\ll B\),
\[
 \frac1{\sigma_{\ell,j}}\ll B^{-1/2},\qquad
 -\frac{u^2}{2\sigma_{\ell,j}^2}
 \le -\frac{u^2}{B}+O(1+z_\ell^2).
\]
This is the same comparison as (6.18), with \(1\) included in the bound. A fixed choice of small enough \(\theta\) makes \(z_K\) large and \(z_\ell\ge z_K\). Thus for any fixed \(C,b>0\), \(C(1+z_\ell^2)+\log(Cc_\ell(1+z_\ell))\le b c_\ell\) uniformly after reducing \(\theta\). Also \(K-\ell+1=O_r(1+z_\ell)\) and \(z_{\ell-1}=z_\ell+\log r\). These facts give the following substitution at each explicit use.

- **Lemma 6.1, p. 27.** Retain the displayed factorial ratio with \(q=\lfloor\delta c_\ell\rfloor\). Stirling bounds it by \((C q z_\ell^2/c_\ell^2)^q\le\exp(-b c_\ell z_\ell)\) for large \(z_K\), since \(q\asymp_\delta c_\ell\). The lower barrier \(L_{\ell-1}=V-(V/h)z_{\ell-1}-c_{\ell-1}\) is positive and differs from \(V\) by \(O(c_\ell+z_\ell)\), with \(c_{\ell-1}=r^{1/90}c_\ell\). Applying the corrected variance comparison at \(L_{\ell-1}\) therefore costs \(O(c_\ell+1+z_\ell^2)\) in the exponent. This cost, the displayed \(O(z_\ell^2)\), and the counting factor \((K-\ell+1)c_{\ell-1}\) are absorbed by reducing the constant in \(-b c_\ell z_\ell\). This gives the stated prefactor \(B^{-1/2}\) and \(\exp(-V^2/B)\).
- **Lemma 6.2, pp. 27–28.** The upper barrier satisfies \(U_\ell=V-(V/h)z_\ell+c_\ell\ge V+c_\ell/2\) for large \(z_K\), since \(V=\kappa B\) and \(c_\ell\) dominates \(z_\ell\). Consequently \(-U_\ell^2/B\le -V^2/B-\kappa_0 c_\ell\) for \(\kappa\ge\kappa_0>0\). The variance and counting costs are \(O(1+z_\ell^2)+\log(O(c_\ell(1+z_\ell)))\), and a fixed fraction of the \(\kappa_0 c_\ell\) saving absorbs them. The local range \(|u|\ll B\) holds since \(c_1=h^{1/3}\) and \(c_\ell\le c_1\).
- **Lemma 6.3, p. 28.** In the case \(D\log(V-u)/(V-u)>\beta_K\), the positive lower bound \(\beta_K>\theta/r\) implies \(V-u=O(1)\) with constants depending on fixed \(\theta,D\). The bound \(V-u\ge c_\ell\) then gives \(c_\ell,z_\ell=O(1)\). In this case the uniform-in-\(T\) \(O(1)\) variance substitution is justified. The Gaussian estimate also implies the other exponential form by \(-V^2/B\le-\rho V+\rho^2 B/4\). In the other case the source proof on pp. 30–31 already uses (6.18) and the positive margin \(\tfrac12(a/(rD)-\rho)(V-u)\), with \(V-u\ge c_\ell\) and \(a>\rho rD\). This absorbs the \(O(1+z_\ell^2)\) loss and the count. For (6.7) the source also retains \((\rho-2\kappa_1)(V-u)>0\).

The first-level upper crossing in Lemma 6.4 uses the same gain as Lemma 6.2. Its more generous \(O(h)\) window count costs only \(O(\log h)=O(z_1)\) in the exponent and is still absorbed by \(c_1=h^{1/3}\). The first-level lower-crossing calculation already keeps the \(O(z_1^2)\) exponent loss on p. 33. The terminal Lemma 6.5 has \(z_K=O(1)\), bounded \(c_K\), and \(u=V+O(1)\), so its \(O(1)\) variance substitution holds. Finally, \(c_\ell=c_K r^{(K-\ell)/90}\) implies
\[
 \sum_{\ell=1}^K e^{-b c_\ell}\le
 \frac{e^{-b c_K}}{1-e^{-b c_K(r^{1/90}-1)}}
\]
using \(r^{m/90}\ge1+m(r^{1/90}-1)\). The \(c_\ell z_\ell\) savings are at least as summable. Thus the correction preserves the rates used in the (4.5) decomposition and the small-shift Gaussian and tilted bounds, at the variance-substitution steps considered here.

## First reciprocal moment and scope

The first Mertens contour in §8.1, pp. 40–41, takes \(T_j=2^{j-1}x_0\) and \(\alpha_j=C/(\log T_j\log\log T_j)\). Hence \(\alpha_j\log T_j=C/\log\log T_j\to0\), outside (4.1), and the cited input is Theorem 1.2 in range (1.4) at \(\varepsilon=1/3\). The proof on p. 39 splits the layer cake at \((\log T_j)^{1/3}\), bounds the lower part trivially, and invokes the separate Lemma 7.2 above this threshold with the pointwise cap from (7.3). Neither (6.4) nor the Gaussian tail is an input to this first reciprocal moment. The first contour uses its own pointwise bounds for the other pieces. For higher integer reciprocal powers §8.2 instead cites Theorem 1.3, whose invocation of Theorem 1.7 uses its larger-shift proof. The small-shift part of Theorem 1.1 does depend on the small-shift Gaussian and tilted tails.

The audit supports the reported variance discrepancy for this primary v1 and the specified local repair. It does not reprove Propositions 5.1–5.2, Lemma 7.2, the contour connectors, or the full Gaussian theorem. No statement is made about revisions after the inspected version.

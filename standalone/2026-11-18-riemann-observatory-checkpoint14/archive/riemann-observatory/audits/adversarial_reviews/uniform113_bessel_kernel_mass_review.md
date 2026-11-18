# Independent check of the modulus-uniform Bessel weight mass

18 November 2026. The proposed bound with no power loss in \(U=KP/T\) holds for a standard two-transition taper. The derivative can be transferred exactly onto the taper before estimating the Bessel integral. The resulting loss is \(\Delta^{-3/2}\) up to logs, where \(\Delta=H/T\). This permits a larger local inverse-prime bridge under explicit strict margin conditions. It does not settle the remaining long-prime estimate. [Previous local Baker bridge](prime107_inverse_prime_voronoi.md) · [Baker endpoint check](uniform108_baker_bridge_qa.md)

## Shared weight and its prime derivative

Let \(k\asymp K\) and \(p\in[P,2P]\). Put \(U_{k,p}=kp/T\asymp U\), \(R=\sqrt{l/U_{k,p}}\), and \(W(u)=w_T(2\pi T u)\). Keep \(W\) on a fixed compact subinterval of \((0,\infty)\), with two transition intervals of length \(O(\Delta)\), and \(\|W^{(r)}\|_\infty\ll_r\Delta^{-r}\). In the divisor Voronoi formula, after \(x=(kT/p)u\) and after including the outer \(1/k\), the dual weight is
\[
 B_{k,l}^{\pm}(p)=U_{k,p}^{-1}\int W(u)J^\pm(R\sqrt u)\,du.
\]
Here \(J^-=-2\pi Y_0(4\pi\cdot)\) and \(J^+=4K_0(4\pi\cdot)\). Since \(p\partial_p U_{k,p}=U_{k,p}\) and \(p\partial_p R=-R/2\), ordinary differentiation and integration by parts give exactly
\[
 p\partial_p B_{k,l}^{\pm}(p)
 =-U_{k,p}^{-1}\int \left(Wf+uW\partial_u f\right)du
 =U_{k,p}^{-1}\int uW'(u)f(u)\,du,
 \qquad f(u)=J^\pm(R\sqrt u).
\]
There is no boundary term. Both amplitudes \(W\) and \(uW'\) have bounded \(L^1\) norm. Their derivatives of order \(r\) have \(L^1\) norm \(O_r(\Delta^{-r})\), because \(W'\) and all its derivatives are on the transition intervals. This derivative conclusion uses the two-transition hypothesis. With only global derivative sup norms, the argument loses another \(\Delta^{-1}\), which is still a fixed power loss.

When \(R\le1\), the order-zero kernels are \(O(1+|\log R|)\) on the support. When \(R\ge1\), they are \(O(R^{-1/2})\). To get rapid decay at large \(\Delta R\), set \(D=\partial_u(u\partial_u)\). The order-zero Bessel equation gives \(Df=-(2\pi R)^2 f\) for \(Y_0\) and \(Df=(2\pi R)^2 f\) for \(K_0\). Transfer \(D^j\) onto either amplitude by integrating by parts. Its \(L^1\) norm is \(O_j(\Delta^{-2j})\), so either integral is at most
\[
 C_j R^{-1/2}\min\{1,(\Delta R)^{-2j}\}.
\]
The argument uses the exact Bessel equation and needs no derivative estimate for an asymptotic remainder. Replacing \(U_{k,p}\) by the common \(U\) costs only fixed dyadic constants. Thus the same bounds apply to the supremum of \(|B_{k,l}^{\pm}|+P|\partial_p B_{k,l}^{\pm}|\) over the entire block. The extra \(\log^3p\) weight and its scaled derivative introduce only fixed log powers. [Primary divisor Voronoi formula, (2.25)–(2.27)](https://www.numdam.org/item/10.1016/j.ansens.2007.05.003.pdf)

## Summation over dual indices, including small \(U\)

Use \(\sum_{l\le X}d_2(l)\ll X\log(2X)\) for \(X\ge1\), which follows by a harmonic divisor count. The small-argument portion \(l\ll U\) costs \(O(\log(2+U))\), by dyadic summation of \(U^{-1}(1+\log(U/l))\). In the region \(U\lesssim l\le U\Delta^{-2}\), sum \(U^{-3/4}d_2(l)l^{-1/4}\). Provided the range meets the positive integers, its cost is \(O(\Delta^{-3/2}\log(2+U\Delta^{-2}))\). The tail above \(X=U\Delta^{-2}\) has an additional factor \((l/X)^{-j}\). For \(X\ge1\), dyadic summation gives the same bound. If \(X<1\), all indices satisfy \(l\ge1>X\). The entire sum is then bounded by \(O_j(U^{-3/4}X^j)=O_j(\Delta^{-3/2}X^{j-3/4})\) for fixed \(j>1\). Therefore, uniformly even for \(U<1\),
\[
 \sum_{l\ge1}d_2(l)\sup_{k,p}
 \bigl(|B_{k,l}^{\pm}(p)|+P|\partial_pB_{k,l}^{\pm}(p)|\bigr)
 \ll \Delta^{-3/2}\log(2+U\Delta^{-2}).
\]
A lower bound \(U\ge T^{-\epsilon}\) is unnecessary for this mass estimate.

For the common cutoff \(l\le\lfloor U T^\omega\rfloor\), let \(\gamma=1-\kappa\) so that \(\Delta=T^{-\gamma}\), and impose \(\omega>2\gamma\). Above the cutoff, \(\Delta R\gg T^{\omega/2-\gamma}\). Reserve some integrations by parts for a factor \(T^{-A}\), and use the remaining ones for the displayed mass sum. This yields arbitrary fixed power decay for the full discarded part, also when the cutoff falls below 1. This cutoff is common, independent of the varying \(k,p\). Fixed polynomial outer counting losses and the log weights are absorbed by increasing the derivative order.

## Range of the consequence and quantifiers

Take a fixed modulus scale \(K\asymp T^\theta\), prime scale \(P\asymp T^\xi\), and assume supported moduli are products of four band primes exceeding \(Y^a\). Impose
\[
 \theta/2<\xi<\theta,\qquad
 \tfrac{11}{10}\theta+\tfrac45\xi<1,\qquad
 \theta+\tfrac{11}{12}\xi<1,\qquad
 \theta+\xi-1<a.
\]
First choose a fixed \(\omega>0\) with \(\theta+\xi-1+\omega<a\), and then \(\gamma>0\) small enough that \(2\gamma<\omega\). This ensures every retained \(l\) is a unit against every supported \(k\). The source Baker theorem uses a common prime annulus. Common fixed prefixes follow by dyadic telescoping and the absorbed bottom prefix, and common-interval partial summation applies each prefix estimate separately. The weight derivative is controlled **pointwise across all moduli** at that integration endpoint by the mass bound above. Neither a maximum over variable endpoints inside the modulus average nor a sharp modulus-dependent cutoff is used. The two phases \(e(\pm l\bar p/k)\) both have unit numerators. The dual Ramanujan subtraction is \(\mu(k)/\varphi(k)\), which is \(O(1/k)\) on the supported moduli. Its cost after summing \(k\) is at most \(O(P)\) times the same weight mass.

Consequently the dyadic block estimate is
\[
 \ll_\epsilon \Delta^{-3/2}T^\epsilon
 (K^{11/10}P^{4/5}+KP^{11/12}+P)+O_A(T^{-A}),
\]
absorbing fixed logs. Choose \(\gamma\) and Baker's \(\epsilon\) sufficiently small in the strict exponent gaps. This gives a power saving, uniformly over exponents in compact subsets of the displayed open region. The \(T^\epsilon\) form without a separate \(\Delta\)-factor is available only by choosing \(\kappa\) close enough to 1 after the desired loss is specified. It is not uniform for every previously fixed \(\kappa\) bounded away from 1.

For \(1/2<\theta<2/3\) there is room above \(\xi=1-\theta\). At that value the first two cost exponents are \(4/5+3\theta/10\) and \(11/12+\theta/12\), both strictly below 1, and both Baker endpoint margins are strict. Thus this kernel bound covers part of the genuine dual range at positive \(U\)-exponent and retains the cutoff constraint \(\theta+\xi-1<a\). No claim follows for longer primes outside these inequalities, where at least one of the exponent budget, source modulus range or all-unit dual cutoff needs another argument. No canonical record was changed.

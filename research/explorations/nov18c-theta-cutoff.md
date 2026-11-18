# Every sufficiently late hard cutoff of the Riemann theta kernel introduces off-line zeros

**Proposed theorem.** Take any proper subset $A$ of the positive integers. Write $q=\min(\mathbb N_{>0}\setminus A)$, $z=s-1/2$, and $b(x)=(4\pi^2x^4-6\pi x^2)e^{-\pi x^2}$. Form the entire symmetric transform
\[
 U_A(s)=\int_0^\infty e^{u/2}\sum_{n\in A} b(ne^u)
                   (e^{zu}+e^{-zu})\,du.
\]
With every term included this is exactly $\xi(s)$, by the classical theta integral (apply $D_u^2-1/4$ to $e^{u/2}\theta(e^{2u})$). The transforms converge locally uniformly to $\xi$ as $q\to\infty$. For every sufficiently large $q$, **every such transform** has $\gg (\log T)^{5/4}$ zeros, counting multiplicity, in
\[
 1-(\log T)^{-3/4}<\Re s<1,\qquad \Im s=T+O(\log T),\qquad T=4q^2.
                                                                    \tag{1}
\]
The constants are independent of $A$. This whole rectangle is inside the classical Vinogradov–Korobov zero-free region of the actual zeta function for sufficiently large $q$. The result allows arbitrary choices after the first missing integer, including restoration of every later term. It concerns the specified hard cutoff with even reflection in log coordinates; it imposes no conclusion on other approximations to the theta kernel.

## The first omission sets the transition height

Let $E_A=\xi-U_A$. Uniformly for $|\Re z|\le5/4$ and $|\Im z|\le 2T$, one has
\[
 E_A(s)=8\pi^2q^4e^{-\pi q^2}
             \frac{2\pi q^2}{(2\pi q^2)^2-z^2}+O(e^{-\pi q^2}).     \tag{2}
\]
Indeed, after dividing the $q$th integrand before its two exponential tests by $4\pi^2q^4 e^{-\pi q^2}$, the result is
\[
 e^{9u/2}\big(1-3e^{-2u}/(2\pi q^2)\big)
                     \exp[-\pi q^2(e^{2u}-1)].
\]
On $0\le u\le1$ its difference from $e^{-2\pi q^2u}$ is $O((u+q^{-2}+q^2u^2)e^{-c q^2u})$ for an absolute $c>0$. Beyond one both tails decay exponentially in $q^2u$, even with the test weight $e^{5u/4}$. The integrated error is $O(q^{-4})$ in this normalization. Integrating the two exponentials against $e^{-2\pi q^2u}$ gives the leading term in (2). Every later summand, integrated against both tests, costs $O(n^2e^{-\pi n^2})$, so even their total is $O(q^2e^{-\pi(q+1)^2})$. The same estimates on fixed wider real strips prove local uniform convergence and justify the defining entire functions.

For $t=\Im s=T+O(\log T)$, (2) has magnitude comparable to $T e^{-\pi T/4}$ and argument $o(1)$ uniformly on the stated real strip. This estimate identifies the actual sign and size required in the zero count.

## A rectangle in which the original and omitted terms exchange dominance

Write $L=\log T$, $\eta=L^{-3/4}$. Take boundary heights from opposite ends of the band
\[
 t=T+(4/\pi)aL,\qquad 1-\eta/4\le a\le1-\eta/8 .
\]
Choose heights a positive fixed fraction of the band apart and away from the zero ordinates of $U_A$. Each sufficiently large $q$ gives a nonzero $U_A$ since its kernel at real $s$ is positive. On $\sigma=1-\eta$, Stirling's formula and the classical bound $|\zeta(\sigma+it)|\ll t^{C(1-\sigma)^{3/2}}(\log t)^C$ give
\[
 \frac{|\xi(1-\eta+it)|}{T e^{-\pi T/4}}
 \ll L^C\exp\big((1-\eta/2-a+C\eta^{3/2})L\big)=o(1).
\]
On $\sigma=1$, the classical reciprocal bound $1/|\zeta(1+it)|\ll(\log t)^C$ gives $|\xi(1+it)|/(Te^{-\pi T/4})\gg L^{-C}\exp((1-a)L)\to\infty$. Thus $U_A$ on the left stays in a sector about the negative real axis, while on the right its argument differs from that of $\xi$ by $o(1)$ with continuous choices. Along the right edge gamma supplies a positive increment $(t_2-t_1)\log(T/(2\pi))/2+O(L)\gg L^{5/4}$. One may bound the two endpoint values of the continuous Euler branch of $\arg\zeta(1+it)$ by $O(L)$ using the usual horizontal argument estimate; the line-one estimates and the same count are detailed in the [Euler-product contour proof](nov18c-euler-contour.md). [Ford's bound in the strip](https://doi.org/10.1112/S0024611502013655)

For completeness each horizontal argument variation costs $O(L)$. At a chosen height $t$, take $\theta=\arg U_A(1+it)$ and apply Jensen's formula about $w=1$ to
\[
 \tfrac12\big(e^{-i\theta}U_A(w+it)
              +e^{i\theta}\overline{U_A(\bar w+it)}\big).
\]
Its value at one is $|U_A(1+it)|\gg Te^{-\pi T/4}$, and on $|w-1|\le3/4$ its supremum is $\ll T^C e^{-\pi T/4}$ by (2), Stirling and polynomial growth of zeta on fixed strips. Jensen bounds the number of its zeros on $|w-1|\le1/2$ by $O(L)$. On each intervening real segment the rotated real part has constant sign, bounding that segment's net argument variation by $\pi$. This proves the horizontal bound. The positively oriented argument principle now gives (1). Finally $L^{-3/4}=o(L^{-2/3}(\log L)^{-1/3})$, so the Vinogradov–Korobov theorem proves that these zeros are absent from the limiting function at these locations. [Classical zero-free region](https://www.ford126.web.illinois.edu/wwwpapers/zetabd.pdf)

## The sign of the omission at all heights

There is also a global inequality: when $q\ge2$, $\Re(\xi(s)-U_A(s))>0$ throughout $0\le\Re s\le1$. For $a=\Re z$ the real part of a summand is the cosine transform of the sum of two functions of the form
\[
 g(u)=e^{du}(4v^2-6v)e^{-v},\qquad d=1/2\pm a\in[0,1],\quad
 v=\pi n^2 e^{2u}\ge4\pi .
\]
They are positive and strictly convex on $u\ge0$. Indeed $(\log g)'=d+4+6/(2v-3)-2v\le-v$ and $(\log g)''=-4v-24v/(2v-3)^2$, giving $g''>0$. For $t\ne0$, two integrations by parts express the cosine transform as $t^{-2}\int_0^\infty g''(u)(1-\cos(tu))\,du>0$. At zero use $g>0$. Absolute convergence permits summation over all omitted indices. Thus the hard truncation even obeys a strict one-sided comparison throughout the full strip; (1) still forces its extra zeros.

This also tests a possible proof by interlacing with a fixed cutoff. For every proper $A$ containing one, the real-axis function $t\mapsto U_A(1/2+it)$ is strictly negative for all sufficiently large $t$. Indeed write the sum of the omitted kernels before the cosine test as $k(u)=e^{u/2}\sum_{n\notin A}b(ne^u)$. The derivative computation just made gives $k'(0)<0$. Its second derivative is integrable by Gaussian decay. Two integrations by parts and the Riemann–Lebesgue lemma yield $\xi(1/2+it)-U_A(1/2+it)=(-2k'(0)+o(1))/t^2$, whereas $\xi$ decays exponentially times a polynomial there. Consequently the real meromorphic quotient $V(t)=\xi(1/2+it)/U_A(1/2+it)$ is regular for all large real $t$ and vanishes at infinitely many of them by Hardy's theorem. Its imaginary part cannot keep one sign immediately above this whole real tail. Such a sign would force $V'(t)$ to keep one weak sign by the Cauchy–Riemann equations, making $V$ monotone and hence identically zero between successive zeros. This excludes a proof based on assigning this particular quotient a Pick-function sign.

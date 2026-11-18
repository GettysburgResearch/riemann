# A finite all-shift Jensen hyperbolicity bound from the zero-free region

For every shift $n\ge0$ the classical Jensen polynomial of the even coefficients of $\xi$ is hyperbolic at every integer degree
$$
 1\le d\le 9\,230\,808\,759\,835\,755\,081\,505\,020 .
$$
This is a direct numerical refinement of the Chasse–Griffin–Ono–Rolen–Thorner–Tripp–Wagner sector argument. For comparison, the verified height $H=3\,000\,175\,332\,800$ alone gives $H^2=9\,001\,052\,027\,541\,590\,755\,840\,000$. The degree ratio is $1.0255255\ldots$.

Indeed let $R=5.558691$. Platt–Trudgian's verified height in Johnston–Yang Lemma 2.1 and Mossinghoff–Trudgian–Yang Theorem 1.3 imply that for every zero of $\xi$ with $|\gamma|>H$,
$$
 \frac{|\beta-1/2|}{|\gamma|}
 \le \frac{1/2-1/(R\log|\gamma|)}{|\gamma|}
 \le a=\frac{1/2-1/(R\log H)}{H}.
$$
The right-hand function is decreasing there by differentiation, since $(1/\log t+1/\log^2t)/R<1/2$. At all remaining zeros the numerator vanishes. Thus the zeros of $F(w)=\xi(1/2+\sqrt w)$, which has genus zero, lie in the convex sector of half-angle $\delta=2\arctan a$ around the negative real axis. Partial products and Gauss–Lucas place every derivative in the same sector class. Lemma 5.2 of Griffin et al. applies to every shift and gives hyperbolicity through $d\le\csc^2\delta$. The exact expression and a 200-bit Arb enclosure are
$$
 \csc^2\delta=\left(\frac{1+a^2}{2a}\right)^2
 =9\,230\,808\,759\,835\,755\,081\,505\,020.60327939810983059\ldots .
$$
For reproducibility, use the following with python-flint:

~~~python
from flint import arb, ctx
ctx.prec = 200
height = arb(3000175332800)
r = arb(5558691) / 1000000
a = (arb(1) / 2 - 1 / (r * height.log())) / height
bound = ((1 + a*a) / (2*a))**2
assert bound > 9230808759835755081505020
assert bound < 9230808759835755081505021
~~~

[Griffin–Ono–Rolen–Thorner–Tripp–Wagner, §5](https://arxiv.org/abs/1910.01227) · [Johnston–Yang, Lemma 2.1](https://arxiv.org/abs/2204.01980) · [Mossinghoff–Trudgian–Yang, Theorem 1.3](https://arxiv.org/abs/2212.06867)

## Comparison with the large-degree literature

In October 2026, Ono proved that for each sufficiently large $d$, the unshifted polynomial has at least $d-O(\sqrt{d\log d})$ distinct negative real zeros, and located these roots by a uniform real-axis two-saddle asymptotic. His Remark 18 places the interval of counted roots between scales $-d/\log^2d$ and $-1/\log d$. With the coordinate $x=-z^2/d$ in the [heat comparison](jensen-heat-nov18.md), this spans real frequencies of order $\sqrt{d/\log d}$ through $d/\log d$ up to constants. A count of $O(\sqrt d\log d)$ or $O(d^{3/5})$ real zeros in the interior would therefore give no improvement on the total count. The local heat comparison supplies a comparison on complex boxes, simplicity and exclusion of additional nonreal zeros there, and identifies their phases with those of the backwards heat flow. A uniform real-axis error estimate alone allows extra complex pairs and does not assert simplicity of every zero.

For the symmetric unshifted results see [Ono, Theorem 1, Corollary 16 and Remark 18](https://arxiv.org/abs/2610.38870). The distinct large-shift hyperbolicity criterion of Kim–Lee covers $n\gg_\epsilon d^{1/2+\epsilon}$. [Kim–Lee](https://doi.org/10.4134/JKMS.j210622)

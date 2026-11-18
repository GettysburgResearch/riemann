# Positive-time heat approximation for the unshifted even Jensen polynomial

**Status.** Proposed unconditional local theorem, with absolute unevaluated constants. Put $\Xi(z)=\xi(1/2+iz)=\sum a_{2k}z^{2k}$ and
$$
P_d(z)=\sum_{k=0}^d(d)_{\underline k}a_{2k}z^{2k}/d^k .
$$
All zeros of $P_d$ with $|\Im z|\le1$, sufficiently large $T=\Re z$, and $C/\log T\le T^2/(2d)\le1/2$ are real and simple. Thus this concerns growing degrees at coefficient shift zero. It controls one region of the complex plane.

## A traveling-wave representation

Use the usual even bilateral theta density $\Phi$ with Fourier transform $\Xi$. Set $n=2d$, $R=\chi_{n+1}/\sqrt n$, and $A(y)=e^{-y^2/(2n)}\mathbb E e^{yR}$. Completing the square in the full Gaussian moment of degree $2d$ gives
$$
[A(y)+A(-y)]/2=\sum_{k=0}^d(d)_{\underline k}y^{2k}/(d^k(2k)!).
$$
Consequently $P_d(z)=\int_\mathbb R\Phi(u)A(izu)\,du$.

For $n\gg T^2$ (here and below this means a constant lower bound on $n/T^2$), and $|y|\le C_0\sqrt n\log T$,
$$
A(y)=\exp(y-y^2/(4n))(1+O_{C_0}((\log T)^3/\sqrt n)).
$$
Indeed in the chi integral substitute $v=r-\sqrt n$, $b=y/(2\sqrt n)$. After factoring out $\exp(y-y^2/(4n))$, the numerator is proportional to the integral of $e^{-(v-b)^2}G(v)$, where $G(v)=(1+v/\sqrt n)^n\exp(-\sqrt n v+v^2/2)$. The denominator is the same integral at $b=0$. Shift to $v=s+b$, $-\sqrt n\le s<\infty$. The endpoint connector is $O(e^{-n})$ since its polynomial factor is at most $(O(\log T)/\sqrt n)^n$ and the remaining factors are $e^{O(n)}$. For $|s|\le C_1\log T$ the Taylor expansion of $\log G$ gives $G=1+O((\log T)^3/\sqrt n)$. For $C_1\log T<|s|\le c\sqrt n$ choose $C_1$ large, $c$ small, obtaining $|G-1|\ll (|s|+|b|)^3e^{s^2/2}/\sqrt n$ from the cubic Taylor bound and $|e^w-1|\le |w|e^{|w|}$. For $|s|>c\sqrt n$, $s\ge-\sqrt n$, use $|1+(s+b)/\sqrt n|\le1+(s+|b|)/\sqrt n$ and $\log(1+h)\le h$. The integrand is then $\ll\exp(-s^2/2+O((\sqrt n+|s|)|b|+|b|^2))$ and has exponentially small integral. The same real Gaussian bound before shifting gives the global crude estimate $|A(y)|\ll\exp(\Re y+C|y|^2/n)$, using a fixed neighborhood of $v=0$ to lower-bound the denominator.

## Uniform comparison on a unit box

Freeze $\tau=T^2/(8d)\le1/8$, put $X=\tfrac12\log(T/(2\pi))$, and let $|\Re z-T|,|\Im z|\le1$, $b=|\Im z|$. In Polymath's normalization the backwards heat transform $\mathcal H_\tau(z)=\int\Phi(u)e^{izu+\tau u^2}\,du$ equals $8H_{4\tau}(2z)$. Then
$$
 |P_d(z)-\mathcal H_\tau(z)|
 \ll T^{-1/4}(\log T)^3 e^{-\pi T/4}T^{7/4+b/2}e^{\tau X^2}.
 \tag{1}
$$
Shift the contour to $u=x+i(\pi/4-h)$ with $(T/2)\sin(2h)=B=3+\tau X$. On $|x|\le2\log T$ the preceding approximation gives $A(izu)=e^{izu+\tau u^2}(1+O((\log T)^3/T))$, since $z^2/(8d)-\tau=O(1/T)$. The global crude bound and the theta series give negligible tails beyond this interval, even after factoring out $e^{-\pi T/4}$, because the exponent from the theta sum is at most $-c e^{2|x|}/T$.

For clarity the absolute integral of the comparison weight on the shifted line is $\ll e^{-\pi T/4}T^{5/2+b/2}e^{\tau X^2}$. By evenness and conjugation it suffices to bound the theta density for $x\ge0$ by a constant times $\sum_{k\ge1} k^4e^{9x/2}\exp(-\pi k^2e^{2x}\sin(2h))$. Write $v=x-X+\log k$, $a=9/2+b$. Then $\sum_{k\le e^{X+v}}k^{4-a}\ll e^{(X+v)/2}$, and $x^2\le(X+v)^2$. Since $Th=B+o(1)$, the remaining dimensionless integral after taking out $e^{(a+1/2)X+\tau X^2}$ has exponent
$$
 (a+1/2)v+B(1-e^{2v})+2\tau Xv+\tau v^2,\qquad v\ge-X .
$$
For $v\ge0$, $1-e^{2v}\le-2v-2v^2$ gives Gaussian decay. For $-1\le v\le0$, $1-e^{2v}+2v\le0$ suffices. For $-X\le v\le-1$, use $1-e^{2v}+2v+v^2/X\le1+v\le0$, leaving an integrable bound $\exp(3+(a+1/2)v)$. This proves (1).

## Reality and simplicity

Fix $T,d$, let $t=4\tau$ for the entire box, and assume $t\log T\ge C$. D. H. J. Polymath's Proposition 9.1(i), Lemma 9.2 and equations (102)–(104) compare $H_t(2z)$ to two nonvanishing leading terms on this box. The larger term has modulus comparable to the amplitude $e^{-\pi T/4}T^{7/4+b/2}e^{\tau X^2}$ in (1), by Stirling in their definitions of $M_0$, $\alpha$ and $M_t=M_0\exp(t\alpha^2/4)$. For $b\ge c_1/\log T$ their modulus ratio is $\ll\exp(-b\log T)$ for the smaller divided by the larger, by (102). Choose $c_1$ large. The two approximation errors, $O(T^{-ct})$ and $O(T^{-1/4}\log^3T)$ relative to the larger term, leave this region zero-free.

For $b\le c_1/\log T$ take the closest real reference point $x_j$ in Polymath's coordinate to $2\Re z$. Consecutive $x_j$ have spacing $(4\pi+o(1))/\log T$. Taking the common holomorphic factor $\exp(-\pi(2z-x_j)/8)$ directly from (102), the expansion used in (104) gives a nonvanishing holomorphic factor comparable in modulus to the preceding amplitude, times $\sin((2z-x_j)\log(x_j/(4\pi))/4)+O(T^{-ct}+(\log T)/T+1/\log T)$ (the factor arising from the imaginary part of the phase in (102) is $1+O(1/\log T)$). The sine is bounded below in modulus by a positive constant outside disks $|2z-x_j|<c_2/\log T$, for any sufficiently small fixed $c_2>0$, and on their boundaries. Increasing $C$ and the lower threshold on $T$ makes both comparison errors smaller than that constant. Rouché gives precisely one zero counted with multiplicity inside each disk contained in the local box. Real coefficients force that zero to be real. For an individual candidate zero take $T=\Re z$ so its relevant disk is contained in the frozen box.

Source: D. H. J. Polymath, *Effective approximation of heat flow evolution of the Riemann ξ function, and a new upper bound for the de Bruijn–Newman constant*, §9, especially the proof of Theorem 1.5. [arXiv:1904.12438](https://arxiv.org/abs/1904.12438).

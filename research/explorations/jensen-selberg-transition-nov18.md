# Removing the logarithmic loss at the Jensen transition

**Proposed theorem.** The classical unshifted Jensen polynomial of the Riemann $\xi$ function has at least
$$
 d-O(\sqrt d)
 \tag{1}
$$
distinct negative real roots for all sufficiently large $d$. Constants here are unevaluated. We combine the previous [bulk and phase matching](jensen-mean-transition-nov18.md) and [Möbius estimate](jensen-mollified-transition-nov18.md) with the full positive-half heat integral and a Selberg mollifier. The [positive wave and moving-shift twisted moment](jensen-positive-wave-nov18.md) give the analytic input.

Keep $U\asymp\sqrt{d/\log d}$, $L=\log U$, and write $y\in I=[Y,2Y]$ for a transition band. Let $s=1/2+iy$, $G(s)=\xi(s)/\zeta(s)$ as the explicit elementary gamma factor, $\alpha=G'/G$, $\tau=y^2/(8d)$, and
$$
 c(y)=2\tau\Re\alpha(s),\quad h=\min_I c(y),\quad D=hL\asymp Y^2 L^2/d.
$$
Relative to Polymath’s convention used in the companion note, Stirling gives $G/(8M_0)=1+O(1/Y)$ and $(\log G)'-(\log M_0)'=O(Y^{-2})$, with each further derivative gaining $Y^{-1}$. The positive-wave reduction also follows directly with exact $G$ by Taylor expanding $G(s+v)/G(s)$. Only $C\le D\le C_0\log L$ requires a new argument. In particular $h=o(1)$, $c(y)\asymp h$, and $\tau\asymp h/L$. Fixed enlargements of $I$ inside $[Y/2,3Y]$ have the same estimates with absolute changes of constants; use the minimum on the enlarged support in choosing $h$ if necessary.

## A positive comparison for Selberg coefficients

Set $q_0=1+h/8$, $K=\lfloor Y^{1/100}\rfloor$. Select primes independently with probabilities $p^{-q_0}$ and let $\mathcal D$ be their product, finite almost surely. Write $P=\Pr(\mathcal D\le K)$ and
$$
 b_m=\mu(m)m^{q_0}\Pr(m\mid\mathcal D\mid\mathcal D\le K),
 \qquad B(s)=\sum_{m\le K} b_m m^{-s}.
$$
Here the inner notation denotes the conditional probability of $m\mid\mathcal D$, given $\mathcal D\le K$. These real coefficients have $b_1=1$, $|b_m|\le P^{-1}$ and $1-P\ll e^{-cD}$. Indeed apply Markov with exponent $h/16$ and use
$$
 \mathbb E\mathcal D^{h/16}
 =\prod_p(1-p^{-q_0}+p^{-q_0+h/16})\ll1;
$$
the logarithm is $\ll\sum_p(p^{-1-h/16}-p^{-1-h/8})=O(1)$ by the Euler product for $\zeta$. Increase the lower constant in $D\ge C$ to ensure $P\ge1/2$.

For a fixed $y$ abbreviate $c=c(y)$, and take $0<\delta\le1/4$. In the ordinary Dirichlet-coefficient square sum of $\zeta(1/2+\delta+i\,\cdot)\,B(1/2+c+i\,\cdot)$ (the diagonal), represent the mollifier by the conditional expectation above and use two independent copies of $\mathcal D$. For prescribed copies $D_1,D_2$ the sum factors as $\zeta(1+2\delta)$ times a product over primes. A prime in neither copy contributes 1, a prime in exactly one contributes $1-a$, and a prime in both contributes $1-2a+b$, with
$$
 a=p^{q_0-1-c-\delta},\qquad b=p^{2q_0-1-2c}=p^{1+2\delta}a^2 .
$$
These factors are nonnegative. Removing the two restrictions $D_j\le K$ therefore bounds the conditional diagonal by $P^{-2}$ times the unrestricted diagonal. Averaging over unrestricted copies recovers the full reciprocal zeta coefficients $\mu(m)$, and gives the exact nonnegative Euler expression
$$
 H(\delta,c)=
 \prod_p\left(1+\frac{(p^{-\delta}-p^{-c})^2}{p(1-p^{-1-2\delta})}\right).
 \tag{2}
$$
All interchanges can first be performed with finitely many selected primes. The local products converge for positive $c,\delta$; the conditional sums involve only $m\le K$.

If $|\delta-c|\le c/2$ then $\log H\ll(\delta-c)^2/c^2$, by $\sum_p(\log p)^2p^{-1-c}\ll c^{-2}$. Generally, expanding the logarithm to first order, with the uniformly summable $O(p^{-2})$ remainder, gives
$$
 H(\delta,c)\ll \frac{\zeta(1+2\delta)\zeta(1+2c)}{\zeta(1+c+\delta)^2}
 \ll\frac{(c+\delta)^2}{c\delta}.
 \tag{3}
$$
The short twisted second moment for full $\zeta$, as used below, is bounded above by the integral of this diagonal plus a negligible error. Its reflected term has the nonpositive factor $\zeta(1-2\delta)$ times a positive semidefinite gcd matrix. The first moment of the product is $1+O(Y^{-c_1})$ under normalized smooth averaging. Consequently the norm of the product minus 1 has the *subtracted* diagonal bound $P^{-2}H(\delta,c)-1$ for its **square**, plus negligible error. These moment statements allow smooth moving shifts such as $\delta=xc(y)$, where $x>0$ is held fixed under integration in $y$.

## The positive heat wave after mollification

The positive half of the exact heat convolution has gamma factor $G(s)e^{\tau\alpha(s)^2}$ and normalized to a complex amplitude $W(y)$ whose real oscillation gives $P_d(y)=J_d(-y^2/d)$ up to an absolute error $O(Y^{-c_1})$ after division by the gamma amplitude. In detail the amplitude, up to such an error, is
$$
 W(y)=e^{\tau(\Im\alpha)^2}\int_0^\infty
 \frac{c(y)}{\sqrt{4\pi\tau}}
 \exp\left(-\frac{c(y)^2(x-1)^2}{4\tau}\right)
 e^{i\Im\alpha\,c(y)(x-1)}
 \zeta(1/2+xc(y)+iy)\,dx .
 \tag{4}
$$
For the integral with $\zeta$ replaced by $1$, extending $x$ to the whole real line gives exactly 1 by the Gaussian characteristic function. The missing negative tail costs $O(e^{-c_2D})$. In the stated range the range $xc(y)>1/4$ may be discarded at a superpolynomial saving in $Y$ by a common cutoff $x\asymp1/\max_I c(y)$ with a sufficiently small constant; all omitted real shifts are bounded below by a fixed positive constant and the Gaussian decays like $\exp(-c/\tau)$ there. Multiplication by $B$ preserves this saving.

Put $\mathcal B(y)=B(1/2+c(y)+iy)$. With $\|\cdot\|_2$ normalized on $I$, (2)–(4) imply
$$
 \|W\mathcal B-1\|_2\ll D^{-1/2}.
 \tag{5}
$$
Indeed the kernel is bounded by $C\sqrt D e^{-c_2D(x-1)^2}$, uniformly in $y$. Use Minkowski *before* integrating $x$. On $|x-1|\le1/2$ the product-minus-one norm is $O(|x-1|+e^{-c_2D}+Y^{-c_1})$ by (2). Outside that interval its norm is $O(1+\sqrt x+x^{-1/2})$ by (3), integrable against the tail of the Gaussian even at zero. Smooth nonnegative majorants of $1_I$, with integral $O(Y)$, give the same bounds for interval norms by applying the squared centered estimate before majorizing. This proves (5).

## Relative phase derivatives

Put $S(y)=\zeta(1/2+c(y)+iy)$. Needed bounds, in addition to $\|\mathcal B\|_2\ll h^{-1/2}$, are
$$
 \|S\mathcal B-1\|_2+h\|(S\mathcal B)'\|_2\ll e^{-c_2D}+Y^{-c_1},
 \qquad \|S\mathcal B'\|_2\ll h^{-1}.
 \tag{6}
$$
The first estimate without derivatives is (2) with matching shifts. For the derivative use Cauchy's formula on a circle $|w|=h/8$ applied to $\zeta(s+c+w)B(s+c+w)-1$. The real parts still satisfy the same Selberg comparison with equal shifts, and the common fixed imaginary offset simply translates the twist variable. The derivative in $y$ introduces only the bounded factor $c'(y)+i$. Decrease $c_1$ to absorb powers of $\log Y$ as necessary.

For the final estimate in (6) apply Cauchy to $\zeta(s+c)B(s+c+w)$. Here only the mollifier is offset, and we claim the noncentered diagonal is $O(1)$ for $|w|\le h/8$. Write $v=\Re w$, $\theta_p=\Im w\log p$, and $a=p^{q_0-1-2c-v}$. With independent copies of the same Bernoulli model the local factors for singles are $1-ae^{\pm i\theta_p}$, and for both the real nonnegative factor is $1-2a\cos\theta_p+p^{1+2c}a^2$. Majorize absolute values and drop both restrictions $D_j\le K$ as above. Compare the unrestricted product of these absolute local expectations with its value at $\Im w=0$. If $r=p^{-q_0}$, the latter local expectation is at least $(1-r)^2\ge1/4$. Its additive increase is at most $C r a |\theta_p|$, using $|1-ae^{i\theta}|-(1-a)\le a|\theta|$ and $1-\cos\theta\le |\theta|$. Summing these relative increases costs a bounded factor because
$$
 \sum_p r a|\theta_p|\ll |\Im w|\sum_p(\log p)p^{-1-2c-v}\ll1.
$$
At $\Im w=0$ the unrestricted diagonal is $H(c,c+v)\ll1$. This proves the claim. The reflected part of the full twisted second moment remains nonpositive also for the complex mollifier coefficients. Cauchy now gives the required $O(1/h)$ norm. The bound for $\mathcal B$ alone follows from short Dirichlet mean value and $|b_m|\le2$.

## Summing the local loss

Use the sign argument of the [mollified transition](jensen-mollified-transition-nov18.md) on chunks of length $\ell=(h^2/L)^{1/3}$. The fraction of chunks on which $|S\mathcal B-1|>1/2$ somewhere, measured by their total length, is
$$
 O\big(\|S\mathcal B-1\|_2^2+\ell^2\|(S\mathcal B)'\|_2^2\big)\ll e^{-c_2D}
$$
since $\ell/h=D^{-1/3}$. On the others, the variation of $\arg\mathcal B$ costs at most a fraction $O(\ell^2/h^2)=O(D^{-2/3})$, by $|(\arg\mathcal B)'|\le2|S\mathcal B'|$. Freeze this phase and count consecutive gamma extrema. Chunk boundaries remove at most a fraction $O((\ell L)^{-1})=O(D^{-2/3})$. The arcs where the real part fails to have the predicted sign cost $O(D^{-1})$ by (5) and the harmless $O(Y^{-c_1}|\mathcal B|)$ comparison error. As in the previous note the result is at least $YL/(2\pi)-O(YLD^{-2/3}+Y\log L+1)$ distinct real zeros on $I$.

The previous Möbius argument already gives precisely this bound on all upper bands $D\ge C_0\log L$. Sum over dyadic $I$ down to $Y_0\asymp \sqrt d/L$ at which $D$ becomes a fixed large constant. The untested lower interval costs $O(Y_0 L)=O(\sqrt d)$ expected oscillations. The sum of $YLD^{-2/3}$ is $O(d^{2/3}L^{-1/3}Y_0^{-1/3})=O(\sqrt d)$. As before, $O(U\log L)$ and both phase-matching endpoint errors are smaller. This proves (1). The argument does not resolve reality of the remaining roots.

## Every coefficient shift

The number of distinct negative zeros of $J^{d,n}$ is at least $d-O(\sqrt d)$ uniformly for all nonnegative shifts $n$. Indeed
$$
 (J^{d+n,0})^{(n)}=(d+n)!\,J^{d,n}/d!.
$$
Rolle gives at least $d-O(\sqrt{d+n})$ distinct negative roots. This suffices for $n\le d$. In the complementary range, first differentiate $\lfloor n/2\rfloor$ times. The resulting polynomial of degree $d+\lceil n/2\rceil$ is hyperbolic by the [Kim–Lee large-shift theorem](https://doi.org/10.4134/JKMS.j210622) when $d+n$ is sufficiently large, since the current shift is a positive fraction of its degree. All roots are strictly negative by positivity of coefficients, and Rolle gives at most $O(\sqrt{d+n})$ multiplicities in excess of one. Each derivative of a hyperbolic polynomial has one simple new root between consecutive distinct roots, and otherwise retains each repeated root at multiplicity one less. Taking the remaining $\lceil n/2\rceil$ derivatives therefore makes all roots simple. The same argument gives simplicity throughout the Kim–Lee range $n\ge C_\epsilon d^{1/2+\epsilon}$ for sufficiently large degrees after increasing $C_\epsilon$ (use any smaller exponent $\epsilon'>0$ at the halfway shift).

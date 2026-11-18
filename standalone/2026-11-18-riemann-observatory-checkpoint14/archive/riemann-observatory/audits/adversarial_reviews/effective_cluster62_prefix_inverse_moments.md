# Inverting the finite prefix-cost sum

This note concerns the aggregate of the established finite polynomial costs. It makes no assertion about the arithmetic prefix theorem. Let $W_m\ge0$ be the sum of $|\rho|^{-2}$ over distinct critical-line zeros of multiplicity $m$, or more generally a nonnegative sequence with the stated moment bounds. Let
$$
 C(b)=\sum_{m\ge1}W_m c_m(b),\qquad
 \mu_m=m(m-1),\qquad
 \nu=\sum_{m\ge2}W_m\mu_m^2\delta_{\mu_m}.
$$
The analytic germ of $C$ at 0 determines every $W_m$. For the zeta critical-line zero set, classical unconditional logarithmic counts suffice for that germ and its determinacy. Under RH, the stronger fixed-window count gives a holomorphic representative on $\mathbb C\setminus\{1\}$. [Finite cost formula](director_prefix_cost_round6.md)

## 1. Taylor coefficients and moments

The finite Gram formula in the director’s review reads
$$
 c_m(b)=m^2+\int_0^{b/(1-b)}G_m(s)^2\,ds,\qquad
 G_m(s)=2P_{m-1}'(1+2s).
$$
For $m\ge2$, the exact Taylor coefficients can be written as
$$
 G_m(s)=\mu_m\sum_{j\ge0}
 \frac{s^j}{j!(j+1)!}
 \prod_{\ell=1}^j\bigl(\mu_m-\ell(\ell+1)\bigr).
 \tag{1}
$$
The first vanishing factor occurs at $\ell=m-1$, so the sum terminates at $j=m-2$. For example, this follows by expanding the exact coefficient
$m(m-1)\binom{m-2}{j}\binom{m+j}{j}/(j+1)$ and pairing $(m-1-\ell)(m+\ell)=\mu_m-\ell(\ell+1)$. At $m=1$ the cost is identically 1.

Squaring (1) and integrating shows that the coefficient of $s^k$ in $c_m-m^2$ is $\mu_m^2$ times the degree-$k-1$ polynomial
$$
 q_{k-1}(X)=\frac1k\sum_{i+j=k-1}
 \frac{\prod_{\ell=1}^i(X-\ell(\ell+1))\prod_{\ell=1}^j(X-\ell(\ell+1))}
 {i!(i+1)!j!(j+1)!}.
$$
Terms whose products vanish remain valid polynomial identities when evaluated at $\mu_m$. Since $s=b/(1-b)=b+O(b^2)$, the coefficient of $b^k$ equals $\mu_m^2 p_{k-1}(\mu_m)$, where $p_{k-1}$ differs from $q_{k-1}$ by lower-degree terms. In more detail, the contribution of $s^j$ to $[b^k]$ is $\binom{k-1}{j-1}$ for $1\le j\le k$. Vandermonde’s convolution gives
$$
 [X^{k-1}]p_{k-1}
 =\frac1k\sum_{i+j=k-1}\frac1{i!(i+1)!j!(j+1)!}
 =\frac{\binom{2k}{k}}{k!(k+1)!}.
$$
Indeed multiplying the middle sum by $k!(k+1)!$ gives $\sum_i\binom{k-1}{i}\binom{k+1}{k-i}$. Thus the coefficients $[b^k]C$ for $k\ge1$ determine the successive moments $M_j=\int X^j\,d\nu(X)$ by triangular inversion, with a nonzero diagonal. The first two examples are $[b]C=M_0$ and $[b^2]C=M_1/2$.

## 2. Unconditional local convergence and RH continuation

For the zeta critical-line zeros use the classical bound $O(\log(2+T))$ for the total zero multiplicity in each unit window at ordinate modulus $T$. It is unconditional and in particular bounds each individual multiplicity by $K\log(2+|\gamma|)$ for some $K$. Thus there is an $a>0$ with
$$
 \sum_{m\ge1} W_m(1+\mu_m^2)e^{a\sqrt{\mu_m}}<\infty.
 \tag{2}
$$
For example take $aK<1$: a far unit window at height modulus $j$ contributes at most $O((2+j)^{-2+aK}\log^5(2+j))$, using $\sqrt{\mu_m}\le m$, $\mu_m^2\le m^4$, and the unit count. The same bound handles either sign. The finitely many low zeros contribute finitely.

For complex $s$ the products in (1) have nonnegative factors up to termination and are bounded by $\mu_m^j$. Consequently,
$$
 |G_m(s)|\le \mu_m e^{2\sqrt{\mu_m|s|}},
 \qquad
 |c_m(b)-m^2|\le |s|\mu_m^2 e^{4\sqrt{\mu_m|s|}},
 \quad s=\frac b{1-b}.
 \tag{3}
$$
For the first inequality, drop $j+1$ from $(j+1)!$ and bound $\sum_j x^j/(j!)^2$ by $(\sum_j x^{j/2}/j!)^2$. Integrate along the straight segment from 0 to $s$ for the second. Thus the aggregate is normally convergent on compact subsets with $4\sqrt{|b/(1-b)|}<a$. In particular it has a neighborhood of holomorphy at 0, allowing termwise Taylor extraction in §1.

Under RH, the fixed short-window count is at most $(h/\pi+o_h(1))\log T$ for any fixed half-width $h>0$. Place a window at the zero and then take $h$ arbitrarily small after the height limit. This gives $m=o(\log(2+|\gamma|))$. Therefore (2) holds for every $a>0$ by the same comparison, after absorbing finitely many low exceptions. Every compact subset of $\mathbb C\setminus\{1\}$ has bounded $|b/(1-b)|$. Equation (3) gives normal convergence there. If at least one $W_m>0$ for $m\ge2$, then $C(b)\to+\infty$ as $b\uparrow1$ because that summand has a positive leading pole. Its Taylor radius at 0 is then exactly 1 under RH. If the multiple support is finite with largest index $m_*$, the singularity is a pole of order $2m_*-3$ by the degree of the cost polynomial in $s$. If the support is infinite, the normally convergent aggregate in $s$ is an entire nonpolynomial function, since its nonnegative Taylor coefficients have arbitrarily high nonzero degrees. Hence $b=1$ is an essential singularity. When all weights above multiplicity one vanish, the aggregate is constant.

## 3. Determinacy from the local germ

The exponential moment of $\sqrt X$ in (2) suffices for Stieltjes determinacy. To prove this, symmetrically push $\nu$ to the real line under $X\mapsto\pm\sqrt X$ with equal halves. This yields a finite symmetric measure $\sigma$. Its even moments are $M_j$ and all odd moments vanish. For any other nonnegative measure on $[0,\infty)$ with the same moments, its corresponding symmetric pushforward has the same integrals of every partial sum of $\cosh(a'x)$ for $0<a'<a$. Monotone convergence gives a finite integral of $\cosh(a'x)$ for both, and hence a finite exponential moment in $|x|$ for both.

Their moment-generating functions are holomorphic in $|\Re z|<a'$. All derivatives at zero agree, so they agree on this strip and in particular on the entire imaginary axis. Uniqueness of Fourier transforms of finite measures gives equality of the symmetric measures. Pushing forward by $x\mapsto x^2$ gives equality of the original measures. This argument proves uniqueness among all finite nonnegative competitors with the same moments, even if an exponential bound was not assumed for the competitor beforehand.

The atoms $\mu_m$ are distinct for $m\ge2$, and $W_m=\nu(\{\mu_m\})/\mu_m^2$. Finally $W_1=C(0)-\sum_{m\ge2}m^2W_m$. The germ therefore determines the weighted multiplicity distribution, including its simple component. Since $W_m$ sums weights over zeros, this inverse result gives no individual ordinates.

## 4. Exact radius from the exponential tail

Assume $\sum_m m^2W_m<\infty$ and at least one multiple weight is positive, and put $\Lambda=\limsup_{m\to\infty}W_m^{1/m}\in[0,1]$, with zeros allowed in the sequence. For fixed real $0<b<1$, set $a_b=(1+b)/(1-b)$ and $R_b=a_b+\sqrt{a_b^2-1}=(1+\sqrt b)/(1-\sqrt b)$. Then
$$
 \lim_{m\to\infty}c_m(b)^{1/m}=R_b^2 .
$$
This follows directly from the positive Legendre integral. For fixed $x>1$, it gives $\lim_{n\to\infty}P_n(x)^{1/n}=x+\sqrt{x^2-1}$ by upper bounding the integrand by its maximum and lower bounding on any small interval near its maximum. Since the Taylor coefficients of $P_n$ at 1 are nonnegative, $P_n'(x)\ge(P_n(x)-1)/(x-1)$ and $P_n'$ is increasing for $x\ge1$. Thus the cost integral on any fixed interval ending at $a_b$ bounds the root-growth limit inferior below by the square of the root-growth rate at its lower endpoint. Move that endpoint towards $a_b$. Conversely $P_n'(a_b)\le[P_n(a_b+\varepsilon)-P_n(a_b)]/\varepsilon\le P_n(a_b+\varepsilon)/\varepsilon$. Use this on the entire cost integral and let $\varepsilon\downarrow0$ for the matching upper bound.

For real $b$, the root test now gives convergence if $\Lambda R_b^2<1$ and divergence if $\Lambda R_b^2>1$. Moreover, the $b$-Taylor coefficients are nonnegative for each $m$, since the surviving coefficients of (1) are nonnegative and $s=b/(1-b)$ has nonnegative Taylor coefficients. Their aggregate positive Taylor series therefore has the same convergence test, by Tonelli. For $0<\Lambda<1$ its radius is exactly
$$
 r_*=\left(\frac{1-\sqrt{\Lambda}}{1+\sqrt{\Lambda}}\right)^2.
$$
The equality case at the radius need not be decided by this root test. If $\Lambda=0$, the radius is 1 by the same convergence argument and the pole lower bound on the real axis. If $\Lambda=1$, the radius is zero, with the possibility of infinite coefficient sums in the absence of polynomial moment bounds. The special case of no multiple weight is the constant aggregate.

For a synthetic zero-count model, place one point at ordinate $\gamma_m=e^{\alpha m/2}$ of multiplicity $m$, $m\ge2$, with $\alpha>0$. These points lie on the line, have unit-window total multiplicity $O(\log(2+|\gamma|))$, and satisfy $W_m=(1/4+e^{\alpha m})^{-1}$. They give $\Lambda=e^{-\alpha}$ and radius strictly less than 1. Thus logarithmic multiplicity and counting bounds alone ensure local convergence, while leaving room for a smaller radius. This construction is a count model and makes no claim about the actual zero sequence.

## 5. Formal moments alone can fail on this exact lattice

One can remove the exponential input and build two nonnegative measures with all polynomial moments equal on the same lattice. Fix $0<\beta<1$ and let $a_m$ be the real Taylor coefficients of
$$
 f(z)=z^2\exp\bigl(-(1-z)^{-\beta}\bigr),\qquad |z|<1,
$$
using the principal branch. The function extends smoothly to the unit circle and is flat at $z=1$. Indeed $1-z$ has argument in $[-\pi/2,\pi/2]$ for $|z|\le1$, $z\ne1$, so $\Re(1-z)^{-\beta}\ge\cos(\pi\beta/2)|1-z|^{-\beta}$. Every differentiated factor loses only powers of $|1-z|$, absorbed by the exponential. Integration by parts of the boundary Fourier coefficients gives $a_m=O_A(m^{-A})$ for every $A$. Also $a_0=a_1=0$ and $f$ is nonzero. Termwise differentiation at 1 shows $\sum_{m\ge2}a_m m^j=0$ for every $j$ by ordinary powers expressed through falling factorials.

Assign positive and negative coefficient parts to the atoms $\mu_m=m(m-1)$. This gives distinct finite nonnegative measures $\nu_+,\nu_-$ with all their $\mu$-moments equal, since every power of $\mu_m$ is a polynomial in $m$. Set corresponding $W_m^\pm=\nu_\pm(\{\mu_m\})/\mu_m^2$ for $m\ge2$. The multiplicity-one masses can be chosen nonnegative to make the two $C(0)$ values equal, by increasing the smaller side. All formal Taylor coefficients of the aggregates now coincide. These are not equal analytic germs: any analytic neighborhood with positive coefficients would imply an exponential weight tail by §4 and restore determinacy. This demonstrates exactly where the exponential input bars an ambiguity of formal moments.

## 6. Finite and approximate data

The inverse theorem is an exact recovery result for the weighted masses $W_m$, which aggregate all ordinates at each multiplicity. It gives neither individual zero locations nor a stable inversion from finitely many Taylor coefficients.

For each integer $K\ge1$, choose $K+1$ distinct lattice points $\xi_i=m_i(m_i-1)$ with $2\le m_1<\cdots<m_{K+1}$. Put
$$
 \lambda_i=\frac1{\prod_{j\ne i}(\xi_i-\xi_j)}.
$$
Lagrange interpolation for a polynomial $p$ of degree at most $K-1$, followed by extraction of the coefficient of $X^K$, gives $\sum_i\lambda_i p(\xi_i)=0$. The signs of the $\lambda_i$ alternate. Therefore
$$
 \nu_+=\sum_{\lambda_i>0}\lambda_i\delta_{\xi_i},
 \qquad
 \nu_-=\sum_{\lambda_i<0}(-\lambda_i)\delta_{\xi_i}
$$
are two nonzero finite positive measures with identical moments of degrees $0,\ldots,K-1$. Their largest support points differ, since $\xi_{K+1}$ belongs to just one side. Convert each measure to weights by dividing its atom at $\mu_m$ by $\mu_m^2$, then add a suitable nonnegative $W_1$ on each side so that both $C(0)$ equal a chosen common constant above the two baseline sums. By §1, these give identical Taylor jets through order $K$ and different multiple weights and maximum multiplicities. For $K=0$ the same conclusion follows by choosing two different single multiple masses and adjusting $W_1$. This is an existential obstruction at every finite order. In particular it leaves the boundary case $C'(0)=0$ fully identifiable: that equality is $\sum_{m\ge2}W_m\mu_m^2=0$, which forces all multiple weights to vanish.

Approximate data on a compact prefix range also have no general ability to exclude a high multiplicity. Fix $C_0>0$, $0<r<1$, a tolerance $\delta>0$, and any desired $M\ge2$. Start with the constant aggregate $C_0$. Add a mass $W_M=w>0$ with
$$
 w\le \min\!\left\{\frac{C_0}{2M^2},
                    \frac{\delta}{c_M(r)-M^2}\right\}
$$
and set $W_1=C_0-wM^2$. The new aggregate still has $C(0)=C_0$, has maximum multiplicity $M$, and differs from the constant by $w(c_M(b)-M^2)$ of modulus at most $\delta$ on $[0,r]$. Here $c_M(r)>M^2$ and monotonicity follow from the integral of the positive coefficient square. The same conclusion for $|b|\le r$ follows from nonnegativity of the Taylor coefficients of $c_M(b)-M^2$. These constructions are synthetic feasible weights. They do not assert the existence of a multiple zeta zero.

## 7. A limiting singularity test and finite-cutoff caution

Under RH, the exact $b=1$ singularity described in §2 is a pole of order $2M-3$ exactly when the multiple support is nonempty and finite with maximal multiplicity $M$. Infinite multiple support gives an essential singularity, while purely simple support gives a constant. A weaker test needs just the positivity in (1). For every $m\ge2$ and $0<b<1$,
$$
 c_m(b)-m^2\ge \mu_m^2\frac{b}{1-b}.
$$
Hence if the limiting aggregate satisfies $C(b)=o((1-b)^{-1})$ as $b\uparrow1$ along the real axis, then every positive multiple weight is excluded. Conversely all-simple support gives a constant and hence that little-oh bound. This suggests a precise question for an arithmetic upper estimate on the limiting profile, conditional on a rigorously established identification with the finite-cost aggregate. It supplies no such arithmetic estimate.

At fixed integer cutoff $N\ge2$, the prescribed prefix set $\{n:n\le N^b\}$ changes only at the finitely many breakpoints $\log n/\log N$. When the definition depends on $b$ only through this set, its finite-cutoff optimal distance and any fixed rescaling in $N$ are piecewise constant functions of $b$. Their classical derivatives vanish on each open interval between breakpoints. Consequently these derivatives cannot generally substitute for derivatives of an analytic limiting profile. The elementary model
$$
 C_J(b)=C\!\left(\frac{\lfloor Jb\rfloor}{J}\right)
$$
for integer $J\ge1$ converges uniformly to $C$ on each $[0,r]$, $r<1$, by uniform continuity. Each $C_J$ has derivative zero almost everywhere, even if $C$ is nonconstant. This is a control for the invalid differentiation step and does not assume that any actual zeta multiplicity exceeds one.

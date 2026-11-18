# An explicit prime-variance threshold for RH and simple zeros

Proposed consequence of the compact isolation and classical explicit formula. Let $V(X)$ be the distance of $\pi(y)-\int_2^y du/\log u$ to the constants in $L^2([X,2X],dy/y)$. For $L=\log2$, define the continuous average
$$
 J(Y)=Y^{-1}\int_L^Y t^2 e^{-t} V(e^t)^2\,dt .
$$
The limit exists in $[0,\infty]$. It is infinite if RH fails. Under RH it is finite, and it equals a specified constant $C_*$ if and only if all nontrivial zeros are simple. Consequently RH and simplicity together are equivalent to $\liminf J(Y)\le C_*$. The constant is approximately $0.05554151$ and can be defined entirely without zero data. No corresponding upper bound of this precision is established for the primes.

**Under RH.** Let $m_\rho$ denote multiplicity, group equal zeros, and put
$$
 d_\rho=1-\frac{|2^\rho-1|^2}{L|\rho|^2},\qquad
 d_0=1-4(\sqrt2-1)^2/L .
$$
Here $d_0$ denotes the variance of $e^{u/2}$ on $0\le u\le L$, without dividing by $L$. By the uniform block expansion, the normalized profile projected off constants is the uniform-in-$t$, block-$L^2$ limit, up to $o_{t\to\infty}(1)$, of the similarly projected functions
$$
 -e^{u/2}-\sum_{|\gamma|\le K}\frac{m_\rho}{\rho} e^{it\gamma}e^{\rho u},\qquad \rho=1/2+i\gamma .
$$
The sum here and below with explicit $m_\rho$ runs over distinct zeros. Distinct real rotation frequencies are orthogonal after continuous averaging as $Y\to\infty$, including the zero frequency of the square-prime term. Uniform convergence in block norm and uniform boundedness justify taking $K\to\infty$ after the mean for the squared norms. Projection of $e^{\rho u}$ has squared norm $d_\rho>0$ since the exponential is nonconstant. This proves
$$
 \lim_{Y\to\infty}J(Y)=d_0+\sum_\rho \frac{m_\rho^2}{|\rho|^2}d_\rho.
$$
If RH fails, the every-octave lower exponent in the [critical-norm argument](causal-critical-nov18.md) gives divergence to infinity.

**Eliminating zero data from the baseline.** With zeros now counted with multiplicity, put $F(x)=\sum_\rho x^\rho/[\rho^2(1-\rho)^2]$. The sum converges locally uniformly for positive $x$. Under RH the expression with multiplicity counted once, in place of its square above, is
$$
 C_*=d_0+2+\gamma_E-\log(4\pi)-[3F(1)-2F(2)]/L.
$$
Indeed the Hadamard product gives $\sum 1/[\rho(1-\rho)]=2+\gamma_E-\log(4\pi)$, and conjugation on the critical line gives $|2^\rho-1|^2=3-2^\rho-2^{1-\rho}$. The baseline is independent of the simplicity hypothesis. Under RH the excess above it is the sum of $m_\rho(m_\rho-1)d_\rho/|\rho|^2$ over distinct zeros. Every summand is nonnegative and each multiple zero makes a strictly positive contribution.

For a direct evaluation set $g=\gamma_E$ and $l=\log(2\pi)$. Then
$$
 3F(1)-2F(2)=-2L^2+4Lg+2Ll+8L-\pi^2/12-2g-2l-3
 -\sum_{k\ge1}\frac{3-2\cdot4^{-k}}{4k^2(1+2k)^2}.
$$
Here is a residue calculation to fix the constants. Integrate $H(s)x^s/[s^2(1-s)^2]$, $H=-\zeta'/\zeta$, upwards on $\Re s=2$, divided by $2\pi i$. Perron inversion gives $\sum_{n\le x}\Lambda(n)[(1+x/n)\log(x/n)+2(1-x/n)]$, since the inverse rational kernel has precisely the displayed residues at 0 and 1, and vanishes below 1. This sum vanishes for $1<x\le2$. Moving the contour to the left gives residues $-F(x)$ from the nontrivial zeros and $-\sum_{k\ge1}x^{-2k}/[4k^2(1+2k)^2]$ from the trivial zeros. One may first use rectangles with horizontal edges at good heights (local partial fractions give $O(\log^2 |t|)$ on fixed strips) and then send the left edge through negative odd integers to minus infinity, using the functional equation and $x>1$. The resulting identity extends to $x=1$ by convergence.

Writing $v=\log x$ and $d=g^2+2\gamma_1$ with the usual Stieltjes constant convention, the combined residues at 1 and 0 are
$$
 x[v^2/2-2v+3-g(v-2)+d]+d-\pi^2/12-(v+2)l .
$$
This uses $H(1+h)=1/h-g+dh+O(h^2)$, $H(0)=-l$ and $H'(0)=d-\pi^2/12$ by the functional equation. Substitution of $x=1,2$ cancels $d$ and proves the asserted formula. The positive-series tail for the numerical baseline after $k=K$ is bounded by $1/(16K^3)$ before division by $L$, from comparison with $3/(16k^4)$. The proposed threshold is an exact real constant; the displayed decimal is for orientation.

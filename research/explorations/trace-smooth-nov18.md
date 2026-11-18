# A tuned smooth-number cutoff in the native odd Möbius trace

**Status.** Proposed source-specific signed cancellation theorem. All terms below belong to the odd trace of [#866, TC26 §3](https://github.com/GettysburgResearch/riemann/blob/a27285abe428835ac0171fe9eb8cbbc97a64a33a/standalone/2026-09-13-astra-trace-covariance/PROOF.md). The polynomial-degree upper bound needed for RH remains open.

Let $l=2j+1$, $\phi_j=\sqrt{2l+1}P_l$ and $\psi_j(x)=\int_x^1\phi_j(u)\,du/u$ for $0\le x\le1$, extended by zero above one. Write $b_j=\psi_j(0)$ and $c_y(n)=\mu(n)$ for odd integers with every prime factor $\le y$, zero elsewhere. Put
$$
 P(y)=\sum_{n\ge1}c_y(n)/n=\prod_{3\le p\le y}(1-1/p),\qquad
 U_{j,y}(t)=\sum_{n\ge1}\frac{c_y(n)}n\psi_j(t/n),\quad 1<t<3 .
$$
The smooth sum has finite support since $\mu$ vanishes on nonsquarefree integers. Its complementary nonsmooth vector $W_{j,y}$ uses the same formula with $\mu_{\rm odd}-c_y$ and the native increasing source cutoff. The sum $U+W$ is the negative of the TC26 column, a sign common to both sectors. Our results concern their literal unbalanced splitting in this representation.

## The smooth column and its optimal boundary layer

Suppose $\log N/\log y$ stays in a fixed compact subinterval of $(1,2)$. Uniformly for $N\le j<2N$, writing $L_j=\log j$,
$$
 U_{j,y}(t)=b_j\left[P(y)-\frac2{L_j}+\frac{2\log t}{L_j^2}\right]
                    +O_{L^2(1,3)}((\log N)^{-3}).
\tag{1}
$$
Moreover $U_{j,y}+W_{j,y}=O_{A,L^2}((\log N)^{-A})$ for every fixed $A$. When $y=N^{1/u}$ with fixed $1<u<2$, the first-order coefficient of $U$ is $2b_j(ue^{-\gamma}-1)/\log N$. It vanishes at $u=e^\gamma$. A more precise cutoff $y=e^\lambda N^{e^{-\gamma}}$, with fixed real $\lambda$, gives
$$
 \sum_{j=N}^{2N-1}\|U_{j,y}\|_2^2
 \sim\sum_{j=N}^{2N-1}\|W_{j,y}\|_2^2
 \sim-\sum_{j=N}^{2N-1}\langle U_{j,y},W_{j,y}\rangle
 \sim \frac{4\pi N}{(\log N)^4}
 \int_1^2\int_1^3 (\log(zt)-e^\gamma\lambda)^2\,dt\,dz .
\tag{2}
$$
The minimizer in $\lambda$ is $e^{-\gamma}(2\log2+\tfrac32\log3-2)$. Even at this choice the integral is strictly positive. Thus tuning a single smoothness cutoff suppresses the leading vector but leaves a macroscopic degree-block energy whose cancellation requires the signed companion. No comparison with the size of the unknown true block below inverse-log precision is used.

## Arithmetic input on the central scale

Put $m_c(x)=\sum_{n\le x}c_y(n)/n$. Uniformly with $\log x/\log y$ in a fixed compact subset of $(1,2)$ it has, to every fixed integer order $h\ge2$, an expansion
$$
 m_c(x)=-\sum_{i=1}^h\frac{D_i}{i(\log x)^i}
          +O_h((\log x)^{-h-1}),\quad
 D_i=(-1)^i\left(\frac{d}{ds}\right)^i\!
       \left[\frac1{(1-2^{-s})\zeta(s)}\right]_{s=1}.
\tag{3}
$$
Constants can depend on the compact set. This is the odd-source version of the finite Newton large-prime calculation in [the companion note](newton-nov18.md). Indeed $x<y^2$ ensures that at most one prime $p>y$ divides an input contributing to $m_{\rm odd}(x)-m_c(x)$. The exact difference is
$$
 -\sum_{a\le x/y,\,a\text{ odd}}\frac{\mu(a)}a
                  \sum_{y<p\le x/a}\frac1p.
$$
Replace the prime sum by $\log(\log(x/a)/\log y)+O_K((\log y)^{-K})$ using the classical zero-free-region prime number theorem and partial summation. The absolute loss from the remainder is $O(\log x)$. The ordinary Möbius sum has arbitrarily strong inverse-log PNT bounds, also valid for odd integers by the powers-of-two convolution. With $L=\log x$, the tail $a>\exp\sqrt L$ against the smooth reciprocal-prime logarithm costs $O_K(L^{-K})$ by partial summation; the multiplier including $1/a$ has size $O(1/a)$ and derivative $O(1/a^2)$ throughout. Below that cutoff expand $\log(1-\log a/L)$ to sufficiently high fixed order. The weighted log moments converge to $D_i$ with arbitrary inverse-log truncation error by the same PNT estimates. The zeroth moment vanishes, and the full odd reciprocal sum $m_{\rm odd}(x)$ itself costs $O_K(L^{-K})$. This proves (3). The Laurent expansion at one gives $D_1=-2$ and $D_2=-4(\gamma+\log2)$. In particular the displayed smooth main term begins as $2/L+2(\gamma+\log2)/L^2$.

## Centering the integrated column

Set $C_j(t,x)=\psi_j(t/x)-b_j\,\mathbf1_{x>j}$. The identity
$$
 U_{j,y}=b_j(P(y)-m_c(j)) +\sum_{n\ge1}\frac{c_y(n)}n C_j(t,n)
\tag{4}
$$
uses the strict threshold in both terms. Choose $\eta>0$ small enough that $x\in[V,Z]=[N^{1-\eta},N^{1+\eta}]$ remains in the uniform range of (3). The contribution of $n\le V$ to the sum with $C_j$ is $O_{L^2}(V/N)$. For $n\ge7$ this follows from $|\psi_j(t/n)|\ll n/N$ on this range by (10) of [the ratio note](trace-nov18.md). For $n=3,5$, use TC26 (2) away from zero to get $O_{L^2}(N^{-1})$, and $n=1$ vanishes. The contribution from $n>Z$ is $O(N/Z)$ since $|\phi_j(u)|\ll ju$ in the interior and hence $|C_j(t,n)|\ll j/n$ there. These bounds apply to any coefficients bounded by one in modulus.

On $[V,Z]$ use partial summation in (4) and replace $m_c(x)$ by the differentiable log polynomial $g(x)$ in (3) with $h=5$. Endpoints and the jump at $j$ are included. The replacement costs $O((\log N)^{-5})$ by (3) and the total variation $O(\log N)$ of $C_j$ there, from $\int_0^{1/2}|\phi_j(u)|\,du/u\ll\log(2j)$ and $|b_j|\ll1$. The strict convention at the integer jump changes a Stieltjes endpoint convention by at most $O(1/j)$, also absorbed. The remaining integral has weight
$$
 g'(x)=-\frac2{xL_j^2}
         +O\left(\frac{1+|\log(x/j)|}{x(\log N)^3}\right).
$$
The integral of $|C_j(t,x)|(1+|\log(x/j)|)\,dx/x$ on $[V,Z]$ is uniformly bounded: below $j$ the column is $O(x/j)$, and above $j$ the centered column is $O(j/x)$. Extending the main integral $\int C_j\,dx/x$ to $(0,\infty)$ has cost $O(V/N+N/Z)$. For $x\le6$ use $z=t/x$ and TC26 (2) on $z\ge1/6$; this part is $O(N^{-1})$. We have shown
$$
 \sum_{n\ge1}\frac{c_y(n)}n C_j(t,n)
 =-\frac2{L_j^2}\int_0^\infty C_j(t,x)\frac{dx}{x}
            +O_{L^2}((\log N)^{-3}).
\tag{5}
$$
The same argument with the full odd Möbius source, $P=0$ and $g=0$ gives $U+W=O_{A,L^2}((\log N)^{-A})$. The centered tail converges absolutely and the discarded constant has the PNT-ordered sum zero.

The main integral in (5) is exactly $b_j(\log j-\log t-H_{2j+1})$. Indeed, substituting $z=t/x$ and starting at $z=\epsilon$, reversing the finite integrals and letting $\epsilon\downarrow0$ yields $\int_0^1\phi_j(z)\log z\,dz/z-b_j\log(t/j)$. The elementary Mellin moment is the rational function
$$
 \int_0^1 \phi_j(z) z^{s-1}\,dz
   =\sqrt{4j+3}\frac{\prod_{k=1}^j(s-2k)}
                         {\prod_{k=0}^j(s+2k+1)},\quad \Re s>-1 .
$$
To see this, integrate the odd polynomial termwise. It yields a rational function with the indicated denominator and numerator degree at most $j$. The numerator vanishes at $2,4,\ldots,2j$ by Legendre orthogonality to lower odd powers. Its top coefficient is $\phi_j(1)=\sqrt{4j+3}$ from the limit of $s$ times the integral as $s\to+\infty$. The logarithmic derivative at $s=0$ is $-H_{2j+1}$. Now $H_{2j+1}=\log j+\log2+\gamma+O(j^{-1})$. Equations (3)–(5) cancel the $\gamma+\log2$ terms and give (1).

Finally the classical Mertens product with zero-free-region remainder is $P(y)=(2e^{-\gamma}/\log y)(1+O_A((\log y)^{-A}))$ for each fixed $A$. Here the factor two removes the prime two. Expanding at the specified $y=e^\lambda N^{e^{-\gamma}}$ gives $U_{j,y}=2b_j[\log(jt/N)-e^\gamma\lambda]/(\log N)^2+O_{L^2}((\log N)^{-3})$. From the factorial expression in TC26 (3), $b_j^2=\pi+O(1/j)$. Squaring and taking the Riemann sum in $j/N$ gives (2). Minimizing the integral amounts to centering $\log(zt)$ at its mean for uniform $z,t$ on $[1,2]\times[1,3]$.

**Verification scope.** This argument imports classical PNT and Mertens estimates and TC26's column normalization. The estimates concern the full source limit on the stated sectors, followed by a degree-block limit. The incomplete scope is the lack of a power saving on the recombined vector.

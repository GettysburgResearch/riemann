# A finite prime-ideal exclusion test without GRH

Let $D(s)$ be the logarithmic derivative of $s(s-1)\Lambda_K(s)$, and put $B^*=2D(1)$ for an arbitrary number field $K$. The [positive Hadamard sum](zhao-number-fields-nov18.md) gives $B^*=\sum_\rho \Re(1/[\rho(1-\rho)])$, unconditionally. If $B^*\le2$ then every nontrivial zero has $|\Im\rho|\ge\sqrt{3}/2$. Indeed a real zero alone is impossible by positivity and the functional equation. A nonreal pair on the critical line contributes $2/(1/4+\gamma^2)$. A nonreal off-line quartet with $\beta>1/2$ contributes at least $4\beta/(\beta^2+\gamma^2)$, which forces $\gamma^2\ge 2\beta-\beta^2\ge3/4$.

Take $s=5/2$ and the following exact rational coefficients in order of ascending derivative:
$$
 (b_0,\ldots,b_7)=(0.882,-0.764,-0.336,0.345,0.802,0.023,-1.64,1.1011).
$$
Form the real statistic
$$
 T=b_0D(s)+\sum_{k=1}^7 b_k\frac{(-1)^{k-1}}{k!}D^{(k)}(s).
$$
Under the sole supposition $B^*\le2$ it obeys $T\le1.0005B^*$. To verify this, pair each zero $z$ with $1-\bar z$. The symmetrized zero summand is the real part of $b_0/(s-z)-\sum_{k\ge1}b_k/(s-z)^{k+1}$ averaged at the two points. Subtract this from $1.0005\Re(1/[z(1-z)])$. This function is harmonic, symmetric in the strip and tends uniformly to zero at imaginary infinity. Its nonnegativity on the half-strip $0\le\Re z\le1$, $\Im z\ge\sqrt{3}/2$, follows by the minimum principle once verified on its boundary. Along the edge $\Re z=0$ clear denominators to obtain a degree-17 polynomial in $x=(\Im z)^2\ge3/4$. On the bottom edge the degree-34 polynomial is in $\Re z\in[0,1/2]$ and the remainder of that edge follows by symmetry. Both have positive left endpoint and zero roots on the stated intervals by the exact Sturm computation in the [replay script](../../scripts/check_zhao_unconditional_weight_nov18.py).

The same script checks the sign of $b(y)=-b_0+\sum_{k\ge1}b_k y^k/k!$ on $[4,\infty)$ by Sturm's theorem. Each prime ideal of norm $q$ contributes $\log q\sum_{j\ge1}q^{-js}b(j\log q)$ in $T$. Thus dropping all terms with $q^j>55$ gives a lower bound on $T$. A strict truncated lower bound above $2.001$ proves $B^*>2$ unconditionally. The cutoff can be increased and still gives a lower bound. At cutoff 55 only local factorizations at the 16 rational primes $p\le53$ are required.

The archimedean contribution of each real gamma factor $\Gamma_{\mathbb R}(s+a)$ is
$$
 \tfrac12 b_0(\psi((s+a)/2)-\log\pi)
 +\sum_{k\ge1}b_k 2^{-k-1}\zeta(k+1,(s+a)/2).
$$
Use $r_1+r_2$ copies with $a=0$ and $r_2$ copies with $a=1$. Add $b_0\log|\Delta_K|/2$ and the rational pole terms $b_0(1/s+1/(s-1))-\sum_{k\ge1}b_k(s^{-k-1}+(s-1)^{-k-1})$. The numerical helpers use Arb intervals; the finite rational-function checks use SymPy's rational Sturm implementation.

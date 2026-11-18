# A near-quadratic degree bound for detecting an off-line zero with a Jensen polynomial

**Status.** Proposed quantitative converse for the ordinary Jensen polynomials of $\Xi$ and the classical even-coefficient Jensen polynomials at shift index zero. Constants are absolute and unevaluated. The argument requires no isolation, simplicity, or restriction on other zeros. It does not prove an equivalence with the de Bruijn–Newman flow.

## Statement

Put $\Xi(z)=\xi(1/2+iz)=\sum_{j\ge0}a_jz^j$ and use the falling factorial $(D)_{\underline j}=D(D-1)\cdots(D-j+1)$. Define
$$
 J_D(z)=\sum_{j=0}^D (D)_{\underline j}a_j z^j/D^j .
$$
Suppose $\Xi(w)=0$, $\Re w=T\ge100$, $0<|\Im w|=\delta<1/2$. For every integer
$$
 D\ \ge\ C\,T^2\delta^{-2}(\log T)^2(\log\log T)^2,
 \tag{1}
$$
$J_D$ has a nonreal zero in the disk $|z-w|<\delta/2$.

Equivalently for the even coefficients, in the sense of the additional implication proved in §4, write $\Xi(z)=\sum_{k\ge0}(-1)^k\gamma_k z^{2k}/k!$. For every $d$ with $2d$ satisfying (1), the classical even-coefficient polynomial $\sum_{k=0}^d\binom dk\gamma_k x^k$ is nonhyperbolic. Thus hyperbolicity at that single degree excludes any defect satisfying (1). Scaling all $\gamma_k$ by the same positive constant does not affect the statement.

The earlier finite implication from verified critical-line zeros to hyperbolicity has the reverse direction. The bound above loses logarithmic factors and includes a displacement parameter. [Griffin–Ono–Rolen–Thorner–Tripp–Wagner](https://arxiv.org/abs/1910.01227) · [Observatory C1](https://github.com/GettysburgResearch/riemann/blob/2dbadaef2014cbebd1881b5ce261575e14f4edb7/research/exploratory/riemann-observatory/proposals/independent_campaigns/C1-detection-horizons/FINAL.md)

## 1. A contour supporting relative derivative estimates

Use the finite Blaschke product on a disk about $2+iT$ from the [cluster contour proof, §1](weil-contour-nov18.md). In the $s$ plane that disk has radius strictly between 4 and 5 and contains $N\ll\log T$ zeros, with multiplicities. Choose $r\in[\delta/4,\delta/2]$ so that on the circle $|z-w|=r$ the following two bounds hold:
$$
 |\Xi(z)|\ge e^{-\pi T/4-C_1 H},\qquad
 \sum_a |s-a|^{-1}\ll {\log T\,\log\log T\over\delta},
 \quad H=(1+\log(1/\delta))\log T,\quad s=1/2+iz.
 \tag{2}
$$
Here $a$ runs over the finite Blaschke zeros. For details let $d_a=|a-(1/2+iw)|$ and discard radii within $h=\delta/[100(N+1)]$ of any $d_a$, which costs at most $\delta/50$. On what remains, the integral of $|r-d_a|^{-1}$ is $O(1+\log(N+1))$ for each $a$, by truncating the logarithmic integral at $h$ over an interval of length $\delta/4$. The average of $\log^+(1/|r-d_a|)$ is $O(1+\log(1/\delta))$ as in the contour proof. Markov's inequality with a sufficiently large fixed factor provides a remaining radius satisfying both sum bounds. Since $|s-a|\ge|r-d_a|$, the reciprocal sum follows, and the Blaschke lower modulus, Stirling, and the log sum give (2).

There is an absolute sufficiently large $C_2$ such that, with $Q=C_2(\log T)\log\log T/\delta$, on this same circle
$$
 {|\Xi(z+v)|\over|\Xi(z)|}\le e^{Q|v|}\qquad (|v|\le1/8).
 \tag{3}
$$
Indeed the zero-free quotient by the finite Blaschke factors has harmonic log modulus bounded in absolute value by $O(\log T)$ on the concentric radius-3 disk, by the maximum principle and Harnack argument already given. Its log-modulus gradient on the radius-$5/2$ disk is $O(\log T)$ by the interior gradient estimate. Both old and new points and their connecting segment lie there. The Blaschke denominators have logarithmic gradients $O(1)$ each. Each numerator incurs a factor at most $1+|v|/|s-a|\le\exp(|v|/|s-a|)$. This argument allows a zero between the two points. The elementary prefactors and the gamma factor have logarithmic gradients $O(\log T)$ there by Stirling. Multiplication proves (3).

Fix an integer $K=\lceil C_3 H\rceil$, with $C_3$ sufficiently large for §3. Enlarge $C_2$ after this choice so that $K/Q\le1/8$ for all the allowed parameters; $\delta(1+\log(1/\delta))$ is bounded. Cauchy's formula on the circle of radius $k/Q$ and (3) give, for $1\le k\le K$,
$$
 {|\Xi^{(k)}(z)|\over|\Xi(z)|}
 \le k!\,e^k(Q/k)^k \ll\sqrt{k}\,Q^k .
 \tag{4}
$$

## 2. Jensen multiplier relative to translation

The even theta kernel $\Phi$ of [the cardinal reconstruction](../../reviews/D-pass3/PROOFS_AND_REPAIRS.md) has Fourier transform $\Xi$ with the convention $e^{izu}$. Termwise integration gives
$$ J_D(z)=\int_{\mathbb R}\Phi(u)(1+izu/D)^D\,du .$$
Write $B_D(y)=e^{-y}(1+y/D)^D=\sum_{k\ge0}c_{k,D}y^k$. The elementary estimate $|1+b|\le\exp(\Re b+|b|^2/2)$ implies $|B_D(y)|\le\exp(|y|^2/(2D))$ for all complex $y$. Thus $c_{0,D}=1$, $c_{1,D}=0$, and Cauchy's estimate on radius $\sqrt{kD}$ gives
$$ |c_{k,D}|\le (e/(kD))^{k/2}\quad(k\ge1).$$
By (4), for $z$ on the selected circle and $D\ge C_4 T^2Q^2$, choosing $C_4$ large makes
$$
 \sum_{k=2}^{K-1}|c_{k,D} z^k\Xi^{(k)}(z)|\le\tfrac14|\Xi(z)|.
 \tag{5}
$$
Indeed $|z|\le 2T$ and the resulting series is bounded by an absolute constant times $\sum_{k\ge2}\sqrt{k}\,[2\sqrt e\,TQ/\sqrt{kD}]^k$.

## 3. Uniform high-order remainder on the actual source

Set $\theta=\pi/4-1/T$ and translate the $u$ path to $u=x+i\theta$ in the Jensen integral and the finitely many derivative integrals. The integrands are analytic on this substrip and decay at both ends by the theta series. On the translated line,
$$
 |\Phi(x+i\theta)|\le C_5 T^{C_6} e^{C_6|x|}
                         \exp(-c_5 e^{2|x|}/T),
 \quad
 |e^{izu}|\le C_5e^{-\pi T/4}e^{|x|}.
$$
The first estimate follows as in the [tilted theta argument](weil-contour-nov18.md) by extracting the first theta exponential and summing the remaining Gaussian terms, with $\cos(2\theta)\asymp1/T$. The second uses $\Re z=T+O(1)$ and $|\Im z|\le3/4$.

The Taylor tail of $B_D$ starting at $k=K$ is bounded by $2^{1-K}\exp(2|y|^2/D)$, by Cauchy's estimate on the circle of radius $2|y|$ and summation of the geometric series (at zero the tail vanishes). With $y=izu$ and $D\gg T^2(\log T)^2$ this makes the integrated absolute remainder at most
$$
 2^{-K}e^{-\pi T/4}T^{C_7}.
 \tag{6}
$$
Indeed the extra quadratic exponential is $\le\exp[C(1+|x|)^2/(\log T)^2]$. Integrate first over $|x|\le 2\log T$, where this factor is bounded by an absolute constant; on the rest the negative exponential in $e^{2|x|}/T$ absorbs both this quadratic and the linear exponential, leaving a bounded integral. All constants are independent of $\delta,D,K$. Choose $C_3$ so (6) is smaller than $|\Xi(z)|/4$ by (2). Combining the truncated expansion with (5) gives $|J_D(z)-\Xi(z)|<|\Xi(z)|$ all around the circle. Rouché's theorem proves the local zero assertion with multiplicity. The circle and its interior avoid the real axis.

## 4. Transfer to the even-coefficient Jensen polynomial

Write $D=2d$ and $P(x)=\sum_{k=0}^d(d)_{\underline k}a_{2k}x^k/d^k$, a rescaling of the even-coefficient Jensen polynomial with sign reversal of the variable. Its coefficients alternate strictly, by the positive theta moments. If the even Jensen polynomial is hyperbolic, $P$ has all roots positive. Direct factorial duplication gives
$$
 J_{2d}(z)=\sum_{k=0}^d [x^k]P(x)\,{(d-\tfrac12)_{\underline k}\over d^k}\,z^{2k}.
$$
The diagonal multiplier $(d-1/2)_{\underline k}$ preserves real-rootedness on degree at most $d$. Indeed its finite symbol is
$$
 \sum_{k=0}^d {d\choose k}(d-\tfrac12)_{\underline k}\,x^k
 =d!\,x^d L_d^{(-1/2)}(-1/x),
$$
whose zeros are all negative since the Laguerre parameter exceeds $-1$. The finite Schur–Szegő composition theorem therefore applies. The additional factor $d^{-k}$ just rescales the variable. The output coefficients continue to alternate, so its roots in $z^2$ are positive and $J_{2d}$ is hyperbolic. Contraposition gives the stated even-coefficient conclusion.

**Remaining gap.** A finite hyperbolicity check excludes displacements only at its degree-dependent resolution. The proof neither establishes hyperbolicity at unbounded degrees nor identifies a sharp first failure degree.

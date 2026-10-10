# Note L (lead): what a uniform half-plane means at different heights and aspects, and what it does not do for moments

```text
Status: PROPOSED (classical deductions from the IMPORTED half-plane; each is a one-paragraph argument, not repository-reviewed)
Scope: global in t and q; conditional only on the imported 7/8 (or 0.874957) theorem
Exact sources: qrh_main.txt Theorem 1.1, Cor. 1.2; qrh_1112.txt Cor. 1.2; Titchmarsh Ch. 14 (Theorem 14.2-type growth bounds); Soundararajan (2009) Prop. 1; notes/D_repo_consequences.md (C1)–(C5)
What was actually run: nothing (derivations only)
Smallest remaining gap: the uniform-in-q Borel–Carathéodory bound for 1/L(s,chi) is standard but not written out here
```

Write $\Theta\le7/8$ for the supremum of real parts of zeros of all Dirichlet $L$-functions.

## 1. The t-aspect: a Lindelöf-type half-plane

Classically a zero-free half-plane $\Re s>\Theta$ gives, by Borel–Carathéodory and Hadamard three circles applied to $\log\zeta$ on disks inside the zero-free region, $\log\zeta(\sigma+it)\ll(\log t)^{(1-\sigma)/(1-\Theta)+\epsilon}$ uniformly for $\sigma\ge\Theta+\delta$, hence
$$\zeta(\sigma+it)\ll_{\delta,\epsilon}t^{\epsilon},\qquad 1/\zeta(\sigma+it)\ll_{\delta,\epsilon}t^{\epsilon}\qquad(\sigma\ge7/8+\delta).$$
So the Lindelöf function satisfies $\mu(\sigma)=0$ for every $\sigma>7/8$. This is new unconditionally: convexity from Bourgain's $\mu(1/2)\le13/84$ gives only $\mu(7/8)\le13/336$, and exponent-pair bounds near $\sigma=1$ are positive at $7/8$. Consequences at every height: (i) $\int_0^T|\zeta(\sigma+it)|^{2k}dt\ll_{k,\epsilon}T^{1+\epsilon}$ for all $k>0$ and $\sigma>7/8$ — **every $2k$-th moment is Lindelöf-trivial on the half-plane**; (ii) $N(\sigma,T)=0$ for $\sigma>7/8$ (within the range $\sigma\ge25/32$ where the density hypothesis was already known, so no new density consequence); (iii) the same with $(q(|t|+2))^\epsilon$ for Dirichlet $L$-functions uniformly in $q$, by the identical argument with $\log(q(|t|+2))$ in place of $\log t$.

For small heights nothing changes: the classical Vinogradov–Korobov region $\sigma>1-c(\log t)^{-2/3}(\log\log t)^{-1/3}$ is wider than $\sigma>7/8$ for $t<\exp((8c)^{3/2}\cdot)$, roughly $t\lesssim e^{10^3}$ for the explicit constants, and numerical verification covers $|t|\le3\times10^{12}$ anyway. The uniform half-plane matters at *large* heights and, more importantly, in the conductor aspect.

## 2. The q-aspect: effective uniformity Siegel–Walfisz never had

From the explicit formula with all zeros in $1/8\le\Re\rho\le7/8$ (note D, (C4)):
$$\psi(x;q,a)=\frac{x}{\varphi(q)}+O(x^{7/8}\log^2x)\quad\text{uniformly for }1\le q\le x,\ (a,q)=1,$$
with an absolute, effective constant. Hence $\psi(x;q,a)\sim x/\varphi(q)$ uniformly for $q\le x^{1/8-\epsilon}$. Siegel–Walfisz gives this only for $q\le(\log x)^A$ and ineffectively; GRH would give $q\le x^{1/2-\epsilon}$; Bombieri–Vinogradov gives $q\le x^{1/2-\epsilon}$ only on average over $q$. The exclusion of Landau–Siegel zeros is the $q$-aspect face of the same statement (note D, Observation 0.1: $c=(\log3)/8$). Linnik's constant: the pointwise bound gives $p(q,a)\ll q^{8+\epsilon}$, weaker than Xylouris' $L=5$ obtained from zero-density and repulsion; so the half-plane does not improve Linnik, but it makes the weaker bound effective and elementary.

## 3. The critical line: why the half-plane gives nothing for $2k$-th moments of $\zeta(1/2+it)$

The RH-conditional moment bounds (Soundararajan, Harper) rest on the inequality $\log|\zeta(\tfrac12+it)|\le\Re\sum_{n\le x}\frac{\Lambda(n)}{n^{1/2+\lambda/\log x+it}\log n}\frac{\log(x/n)}{\log x}+\frac{1+\lambda}{2}\frac{\log t}{\log x}+O(1/\log x)$, whose proof uses that every term $(\sigma-\Re\rho)/|s-\rho|^2$ in the Hadamard product has a fixed sign for $\sigma>1/2$ when all $\Re\rho=1/2$. A zero-free half-plane $\Re s>7/8$ leaves the zeros free in $1/8\le\Re\rho\le7/8$, so the sign fails exactly for the zeros that matter (those within $1/\log x$ of the point $1/2+\lambda/\log x+it$). Zero-density estimates bound the number of offending zeros by $T^{1-c\eta}$ for $\Re\rho>1/2+\eta$, but $\eta\asymp\lambda/\log x$ is far too small for that to control an exceptional set against the trivial bound $|\zeta|^{2k}\ll T^{k/6+\epsilon}$. So, unconditionally, the state remains: sharp upper bounds for $0\le k\le2$ (Heap–Radziwiłł–Soundararajan), lower bounds for all $k$ (Heap–Soundararajan), and $k>2$ only under RH. The half-plane changes the moment problem only off the critical line (Section 1).

## 4. The family aspect (where the proof actually lives)

The theorem is proved for the sextic Kummer family $\{\psi_u\}$ over $\mathbb Q(\sqrt{-3})$ and transferred to Dirichlet $L$-functions by $L(s,\chi\circ N)=L(s,\chi)L(s,\chi\chi_{-3})$. Everything about "heights" inside the proof is uniform: the detector works in bounded-height rectangles $|\Im\rho|\le2T_1$ with $T_1=Z^\tau$, $\tau$ tiny, and all constants depending on the target are allowed. The one place where a height parameter is structurally important is the *row* height $U=Z^d$ (the conductor of the twist), not $\Im s$: the whole exponent system is a function of $d$, and the binding constraints sit at $d=h$ (notes A, E). In this sense the "height level" that matters for improving the bound is the conductor level $d$ of the nonprincipal rows, and the obstruction is a zero-density/absolute-value problem at conductor $U=Z^{13/16}$ and real part $\approx0.69$.

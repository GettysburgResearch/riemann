# The large-prime part of a native Newton step

**Status.** Proposed unconditional obstruction for the literal Möbius source. The scale-to-scale upper bound and RH remain open. This application uses classical prime number theorem estimates. No priority is claimed for smooth-number asymptotics.

**Scope and dependencies.** BNR26, §§0–4 of [the original proof](https://github.com/GettysburgResearch/riemann/blob/a1b4625f9775df1fdbd431b5198309a2fce9b038/standalone/2026-09-10-astra-balanced-newton/PROOF.md), supplies the identification of its output with the ordinary Möbius coefficients through the strict square endpoint. At [the later #848 head](https://github.com/GettysburgResearch/riemann/tree/7de75c02417d5d8db7eafb1ceba364380e72d16a/standalone/2026-09-19-newton-rough-core), RCB26 groups the *products inside the harmonic kernel*. Here the split acts on the *reconstructed output coefficients*. An obstruction for this split leaves the RCB26 estimates intact.

## Statement

Let integers $b\to\infty$, $Y=b-1$, $B=b^2-1$. Split $\mu=r+s$ on $1\le n\le B$, where $r(n)=\mu(n)$ if $n$ has a prime factor greater than $b$, and $r(n)=0$ otherwise. For a real sequence $a$ put

$$
 M_a(x)=\sum_{n\le x}a(n),\quad m_a(x)=\sum_{n\le x}a(n)/n,\quad
 u_a(N)=m_a(N)-M_a(N)/(N+1).
$$

The BNR26 norm squared and its associated inner product at an integer endpoint $N$ are

$$
 A_N(a)=\sum_{k=1}^N\frac{M_a(k)^2}{k(k+1)}+2(N+1)u_a(N)^2,\qquad
 \langle r,s\rangle_N=\tfrac12(A_N(r+s)-A_N(r)-A_N(s)).
$$

For every fixed $0<\delta<1$, uniformly over $b^{1+\delta}\le x\le B$, with $L=\log x$,

$$
 M_r(x)=\frac{x}{L^2}+O_\delta(x/L^3),\qquad
 m_r(x)=-\frac{1}{L}+O_\delta(L^{-2}).                         \tag{1}
$$

Both corresponding smooth-source values have the opposite main term. In particular

$$
 A_B(r)\sim A_B(s)\sim-\langle r,s\rangle_B\sim\frac{2B}{(\log B)^2}. \tag{2}
$$

The negative covariance already appears in the cumulative energy. On the terminal window $B/2\le k\le B$ the two separate squared norms before the balancing fee are each asymptotic to $B/(2\log^4 B)$, and the signed cross inner product on that window is asymptotic to its negative.

For every fixed $p\le2$ and $C>0$, both $A_B(r)$ and $A_B(s)$ eventually exceed $C(1+A_Y(\mu))^p$. Thus termwise bounds on these two actual output sectors cannot even give the quadratic recurrence. The exact signed interaction is indispensable at orders much larger than the entire desired output. This holds on every sufficiently large Newton stage.

## Proof

Use the classical zero-free-region consequences $M_\mu(t)\ll_K t/(\log(2t))^K$ and
$\pi(t)=\operatorname{li}(t)+O_K(t/(\log(2t))^K)$ for every fixed $K>0$ and $t\ge2$. For each fixed $j\ge0$,

$$
 D_j=\sum_{n\ge1}\frac{\mu(n)(\log n)^j}{n}
 =(-1)^j(1/\zeta)^{(j)}(1).
$$

The truncation error at $H\ge2$ is $O_{j,K}((\log H)^{-K})$ by partial summation with the bound on $M_\mu$. These convergent series have the asserted values by taking a real limit from $\sigma>1$ in the differentiated Dirichlet series. In particular $D_0=0$, $D_1=-1$, and $m_\mu(t)\ll_K(\log(2t))^{-K}$.

There is at most one prime factor $p>b$ of any $n\le B$, and $m=n/p<b<p$. Thus $\mu(pm)=-\mu(m)$, including squareful cofactors. With $T=x/b$,

$$
 M_r(x)=-\sum_{m\le T}\mu(m)[\pi(x/m)-\pi(b)],\qquad
 m_r(x)=-\sum_{m\le T}\frac{\mu(m)}m
                  \sum_{b<p\le x/m}\frac1p.                            \tag{3}
$$

The factor $\pi(b)M_\mu(T)$ is $O_{K,\delta}(xL^{-K})$ since $T\ge b^\delta$. Partial summation of the prime number theorem gives
$\sum_{b<p\le v}p^{-1}=\log(\log v/\log b)+O_K((\log b)^{-K})$ uniformly for $b\le v\le b^2$. Summing its error absolutely in (3) costs at most $1+\log T$. The same absolute loss handles the remainder in
$\pi(x/m)=(x/m)\sum_{i=1}^{J}(i-1)!/(\log(x/m))^i+O_J((x/m)L^{-J-1})$.
Here $\log(x/m)\ge\log b\ge L/2$.

All expansion and truncation operations below admit arbitrary fixed inverse-log precision. Set $H=\exp(\sqrt L)$, which is below $T$ eventually. For $H<m\le T$, each smooth multiplier just displayed, after dividing the first expression by $x$, has magnitude $O_J(1/m)$ and derivative $O_J(1/m^2)$ as a function of $m$. The reciprocal-prime logarithm is bounded because $\log(x/m)/\log b\in[1,2]$. Partial summation with the arbitrarily strong logarithmic bound on $M_\mu$ makes these tails $O_{K,J}(L^{-K})$ for each fixed $K$. On $m\le H$, expand in $v=\log m/L\le L^{-1/2}$. Taylor expansion through degree $h$ costs $O_{h,J}((1+\log H)L^{-(h+1)/2})$ after summation with weight $1/m$. Taking $h$ and $J$ sufficiently large relative to the requested order justifies replacing all resulting log moments by $D_j$.

Specifically, the terms through order $L^{-2}$ of $M_r(x)/x$ are
$-D_0/L-(D_1+D_0)/L^2$.
For $m_r(x)$, the multiplier inside the negative sum is
$\log(L/\log b)+\log(1-v)$, so its constant term disappears and its first surviving term gives $D_1/L$. This proves (1), and subtraction from the bounds on $M_\mu,m_\mu$ gives the smooth component.

For the total cumulative energy of $r$, indices $k<b^{3/2}$ contribute $O(b^{3/2})$ by $|M_r(k)|\le k$, and the rest contribute $O(B/\log^4 B)$ by (1). The same bounds hold for $s$. At $B$, (1) gives $u_r(B)=-1/\log B+O(1/\log^2 B)$ and $u_s(B)=+1/\log B+O(1/\log^2 B)$. Consequently the balancing fee supplies the leading term in (2). Polarization gives the covariance since the native source satisfies $A_N(\mu)\ll_K N/(\log(2N))^K$ for every fixed $K$ (split its energy sum at $\sqrt N$). The terminal-window statements follow directly by summing (1), using $\log k=\log B+O(1)$. The recurrence obstruction now follows from (2) and the same bound for the native input at $Y$, already at $p=2$.

## How far deterministic inverse-log subtraction goes

For each fixed integer $h\ge1$, the same expansion proves

$$
 m_r(x)=\sum_{j=1}^{h}\frac{D_j}{j L^j}+O_{h,\delta}(L^{-h-1}).       \tag{4}
$$

Infinitely many $D_j$ are nonzero. Otherwise the Taylor series of $1/\zeta(s)$ at $1$ would terminate and agree with a polynomial throughout $\Re s>1$ by the identity theorem. Its limit along the positive real axis is one, forcing that polynomial to be constant, contrary to $D_1=-1$. After subtracting any fixed truncation of (4), let $j$ be the first omitted nonzero order. Summing the squared reciprocal residual on $[B/2,B]$ still costs asymptotically $B D_j^2/(2j^2\log^{2j} B)$. All of these fixed truncations therefore leave an above-subpower cost on this source sector. This conclusion concerns the isolated reciprocal component and allows an exact paired compensation or an order increasing with the cutoff.

**Verification.** The displayed errors and endpoint conventions are derived analytically above. The remaining RH-facing problem is to estimate the joint compensated source to subquadratic precision. These asymptotics quantify one mandatory cancellation without establishing that estimate.

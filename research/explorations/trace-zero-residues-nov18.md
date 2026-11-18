# Critical-zero residues give an all-degree lower bound for the odd trace

**Status.** Proposed unconditional variational estimates. The zero hypotheses in each summand concern its location and multiplicity. The proof gives no new zero location and no upper bound for the native trace.

**Source.** Use the finite odd-polynomial operators $A,E,K_N$, their domains and the exact identity $Ep=K_NAp$ from [#866, DG26 §§0–1](https://github.com/GettysburgResearch/riemann/blob/a27285abe428835ac0171fe9eb8cbbc97a64a33a/standalone/2026-09-12-astra-polynomial-degree-growth/PROOF.md). The high-order Fourier approximation in §2 below is the construction of [#869, arithmetic Lemma 1](https://github.com/GettysburgResearch/riemann/blob/5e559c9cbf5aee84ff7ed78dc91b55df744aef56/standalone/2026-09-12-three-route-completion/arithmetic/PROOF.md), which used it for near-sharp off-line power exponents. DG26 §6 gives $\|K_N\|^2\gg\log N$ from one critical zero. Here a logarithmic Fourier multiplier, simultaneous trials and a degree-resolving cutoff give multiplicity dependence and explicit residue coefficients. No general priority claim for spectral zero obstructions or variational lower bounds is made.

Write $Z(s)=(1-2^{-s})\zeta(s)$, $a(s)=(s-1)Z(s)$, $S_N=\operatorname{tr}(K_NK_N^*)$, and $v_\rho(t)=t^{\rho-1}$ on $(1,3)$. For an integer $m\ge1$ and any finite set $F$ of distinct zeros $\rho=1/2+i\gamma$ of exact order $m$, put $a_m(\rho)=a^{(m)}(\rho)/m!$ and $c_m=(2m-1)((m-1)!)^2$. Then
$$
 \liminf_{N\to\infty}\frac{S_N}{(\log N)^{2m-1}}
 \ge \frac{\log3}{c_m}\sum_{\rho\in F}\frac1{|a_m(\rho)|^2}.
\tag{1}
$$
The bound holds for the sum over *all* such zeros by taking suprema of finite sums; an infinite right side means that the normalized trace tends to infinity. In particular, the simple zeros contribute $\log3\sum_\rho |(\rho-1)(1-2^{-\rho})\zeta'(\rho)|^{-2}$ at scale $\log N$. Conjugate zeros may both be included.

A stronger conclusion bounds every fixed output quadratic form from below. For $g\in L^2(1,3)$ the lower limit of $\|K_N^*g\|^2/(\log N)^{2m-1}$ is at least $c_m^{-1}\sum_{\rho\in F}|\langle g,v_\rho\rangle/a_m(\rho)|^2$. The proof also gives the same bound in the variational sense for each of the first $|F|$ eigenvalues, compared with the corresponding eigenvalue of $c_m^{-1}\sum_{\rho\in F}|a_m(\rho)|^{-2}v_\rho\otimes v_\rho^*$. These finite-set conclusions keep all interactions in the output space.

## 1. A logarithmic operator on a compact smooth envelope

For $w\in C_c^\infty(\mathbb R)$ with $w(0)=1$ and $w=0$ on $[1,\infty)$, take $R>1$ and
$$
 f(t)=t^{\rho-1}w_R(-\log t),\quad w_R(x)=w(x/R).
$$
This is smooth and zero near $t=0$. Extend the definition over all positive $t$. For $x=-\log t$ and a compact smooth function $h$, set
$$
 (T_\rho h)(x)=\sum_{n\ge1,\ n\text{ odd}} n^{-\rho}
   [(\rho-1)h-h'](x+\log n).
$$
The sum is pointwise finite, and direct differentiation gives $Af(t)=t^{\rho-1}T_\rho w_R(x)$. Let $D(y)=\lfloor(e^y+1)/2\rfloor-e^y/2$, so $D$ is bounded on $y\ge0$ and equals $-e^y/2$ on $y<0$. In logarithmic coordinates the odd-integer counting measure is $e^y\,dy/2+dD(y)$. On the whole real line its continuous part in $T_\rho h$ integrates to zero: the integrand is minus a constant multiple of $(e^{(1-\rho)y}h(x+y))'$. Integration by parts in the discrepancy gives
$$
 T_\rho h(x)=\int_{\mathbb R} e^{-\rho y}D(y)
 [\rho(\rho-1)h-(2\rho-1)h'+h''](x+y)\,dy .
\tag{2}
$$
The kernel is integrable with exponential tails. For $0<\Re s<1$ the standard Euler summation identity is $Z(s)=s\int e^{-sy}D(y)\,dy$; this is also DG26 (4.2)'s discrepancy identity. Thus with the Fourier convention $e^{-i\xi x}$ the exact multiplier in (2) is $a(\rho-i\xi)$. It has polynomial growth $O_\rho((1+|\xi|)^2)$ on the real frequency axis by (2). Its zero at frequency zero has order $m$.

It follows by Plancherel that
$$
 R^m (T_\rho w_R)(Rv)\ \longrightarrow             (-1)^m a_m(\rho) w^{(m)}(v)
 \quad\text{in }L^2(\mathbb R,dv).
\tag{3}
$$
Indeed $R^ma(\rho-i\eta/R)\widehat w(\eta)$ has the required pointwise limit. For $|\eta|/R\le1$, Taylor's theorem bounds the prefactor by $C|\eta|^m$. For $|\eta|/R>1$, it is bounded by $C(1+|\eta|)^{m+2}$. The Fourier transform of $w$ decays faster than either polynomial. On $0<t<1$, $|t^{\rho-1}|^2\,dt$ becomes $dx$ on $x>0$. The *half*-line restriction of (3) therefore gives
$$
 R^{2m-1}\|Af\|_2^2\ \longrightarrow |a_m(\rho)|^2 I_w,\qquad I_w=\int_0^1|w^{(m)}(v)|^2\,dv .
\tag{4}
$$
For distinct zeros of order $m$, the corresponding normalized input inner product tends to zero. In the $v$ variable it contains the factor $e^{i(\gamma'-\gamma)Rv}$; the two remaining factors converge in $L^2(0,\infty)$ by (3), and their product converges in $L^1$. Apply the Riemann–Lebesgue lemma to the limiting product.

For the output, write $Q_f(t)=\sum_{n\text{ odd}}f(t/n)/n$. Splitting by the same counting measure gives $Q_f(t)$ as a constant independent of $t$ plus
$$
 t^{\rho-1}\int_{\mathbb R} e^{-\rho y}D(y)
             [\rho w_R-w_R'](x+y)\,dy .
$$
Indeed the continuous term is $\tfrac12\int e^{(1-\rho)z}w_R(z)\,dz$ after the change $z=x+y$. The integral in the display tends uniformly to $w(0) Z(\rho)=0$ for bounded $x$, by dominated convergence and the exponential kernel. Since $Ef=f(t)+Q_f(1)-Q_f(t)$ on $(1,3)$, the potentially large constant cancels exactly and $Ef\to v_\rho$ in $L^2(1,3)$.

## 2. Realizing almost the full degree scale

Fix $0<\epsilon<1$, set $R=(1-\epsilon)\log N$, and extend $f$ oddly to $[-1,1]$. It vanishes on $|t|\le e^{-R}$. For any fixed integer $d\ge2$, differentiating its even derivative $g=f'$ through order $d$ gives
$$
 \max_{0\le k\le d}\|g^{(k)}\|_\infty\le C_{d,\rho,w}e^{(d+3/2)R}.
$$
Negative powers of $R$ created by derivatives of $w$ are bounded. The $2\pi$-periodic function $g(\cos\theta)$ has the same type of $d$th derivative bound. Integrating its Fourier coefficients by parts $d$ times shows that truncating to frequencies $|k|\le 2N-2$ gives uniform error $O_{d,\rho,w}(N^{1-d}e^{(d+3/2)R})$. The truncation is an even polynomial in $t$ of degree at most $2N-2$: there are only cosine terms by reflection in $\theta$, and only even frequencies since $g$ is even. For any fixed requested $B>0$ take $d$ large relative to $B,\epsilon$ and integrate this polynomial from zero. This yields an odd $p_{\rho,N}$ of degree at most $2N-1$ with $\|p'-f'\|_\infty=O(N^{-B})$. The derivative-to-$A,E$ bounds from DG26 (4.6) or direct absolute dilation summation therefore give errors $O(N^{-B})$ in both outputs. The polynomial lies in the actual input space of DG26, and $Ep_{\rho,N}=K_N(Ap_{\rho,N})$ exactly.

## 3. Simultaneous trial and cutoff optimization

Use the columns $h_{\rho,N}=Ap_{\rho,N}$, $\rho\in F$, and let $H_N$ be the matrix mapping their coefficient vectors to the input space. By (4) and the oscillatory cross estimate, $R^{2m-1} H_N^*H_N$ tends to the positive diagonal matrix with entries $|a_m(\rho)|^2 I_w$. The columns of $K_N H_N$ tend to $v_\rho$. The orthogonal projection onto the trial span gives the positive operator lower bound
$$
 K_NK_N^*\ \succeq\
 (K_NH_N)(H_N^*H_N)^{-1}(K_NH_N)^*
$$
for every sufficiently large $N$. After division by $R^{2m-1}$, the finite-rank right side converges in trace norm to $I_w^{-1}\sum |a_m(\rho)|^{-2}v_\rho\otimes v_\rho^*$. In particular it preserves nonorthogonality of the outputs. Their squared norms are $\log 3$.

For real $w$ as above, the infimum of $I_w$ is $c_m$. Repeated integration from the vanishing endpoint gives
$$
 1=w(0)=\frac{(-1)^m}{(m-1)!}\int_0^1 u^{m-1}w^{(m)}(u)\,du .
$$
Cauchy–Schwarz gives $I_w\ge c_m$. For the reverse inequality take smooth cutoffs of $u^{m-1}$ in $C_c^\infty(0,1)$ approaching it in $L^2$, multiply by constants of the indicated sign to enforce the displayed normalization, and integrate $m$ times from the right endpoint. The resulting $w$ is polynomial near zero and can be extended smoothly with compact support to negative arguments. Its right-half energy tends to $c_m$. Letting first $N\to\infty$, then $I_w\downarrow c_m$ and $\epsilon\downarrow0$, proves (1) and the asserted operator bounds. The constant is optimized for this trial family; equality for the native trace is open.

**Remaining gap.** These variational lower bounds measure the obstruction from actual boundary zeros. A matching upper bound would be a substantially stronger input than any component proved here. The Mellin multiplier, polynomial approximation and Gram calculation are analytic and do not use a finite zero table.

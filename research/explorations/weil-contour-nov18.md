# A height bound for detecting an arbitrary off-line zero in a Weil window

**Status.** Proposed analytic theorem for review. The hypothesis is the existence of an off-line zeta zero. All other zeros may occur with their actual positions and multiplicities. Constants below are absolute but unevaluated.

**Sources.** Use $\Xi(z)=\xi(1/2+iz)$, $\widehat f(z)=\int_{\mathbb R}f(u)e^{izu}\,du$, and $\Gamma$ the multiset of zeros of $\Xi$. The Weil form on complex smooth compactly supported tests is
$$W(f)=\sum_{z\in\Gamma}\widehat f(z)\overline{\widehat f(\bar z)}.$$
The integrated cardinal construction captures a specified pair with adaptable compact support. Observatory C4 asks for a quantitative window and addresses the contribution of other defects. The argument below encloses a cluster, avoiding a reciprocal derivative at an individual zero. [Cardinal reconstruction R16](../../reviews/D-pass3/PROOFS_AND_REPAIRS.md) · [C4 final report at its frozen head](https://github.com/GettysburgResearch/riemann/blob/2dbadaef2014cbebd1881b5ce261575e14f4edb7/research/exploratory/riemann-observatory/proposals/independent_campaigns/C4-weil-window-locality/FINAL.md)

## Statement

Suppose $\Xi$ vanishes at $w$ with $\Re w=T\ge100$ and $0<|\Im w|=\delta<1/2$. Set $H=\log T(1+\log(1/\delta))$. There exists an absolute $C$ and a complex $f\in C_c^\infty(-L,L)$ with $W(f)<0$ for
$$
 L={1\over2}\log\!\left[{T\over2\pi}+C(T^{1/3}H^{2/3}+H)\right].
$$
In particular, along any sequence of such defects with $\log(1/\delta)=o(T/\log T)$, the infimum of detectable window radii is at most $\tfrac12\log(T/(2\pi))+o(1)$. The proof first gives the bound with $T/4+CH$ inside the logarithm, then improves the leading constant by translating the theta kernel in its strip of analyticity.

## 1. A small contour with controlled reciprocal

Take $s_*=1/2+iw$ and $s_c=2+iT$. On $|s-s_c|\le 6$, the zeta function is analytic and $|\zeta(s)|\le T^{C_1}$ for some absolute $C_1$. This uses the classical polynomial growth in a fixed vertical strip away from the pole. The absolutely convergent reciprocal Euler series gives $|\zeta(s_c)|\ge1/\zeta(2)$. Jensen's formula on the disk of radius 6 bounds the number of zeros in the disk of radius 5 by $C_2\log T$. Take any $R\in(4,5)$ whose circle meets no zero and divide zeta by the finite disk Blaschke product for its zeros $a$ in $|a-s_c|<R$. Each factor has modulus one on the boundary, at most one in the disk, and at least $c\min(1,|s-a|)$ on the disk of radius 3 about $s_c$ for an absolute $c>0$. These bounds follow from the factor $R(s-a)/(R^2-\overline{(a-s_c)}(s-s_c))$. Write $G$ for the resulting zero-free quotient. The maximum principle gives $\log|G|\le C_1\log T$, and $\log|G(s_c)|\ge-\log\zeta(2)$. Harnack's inequality applied to $C_1\log T+1-\log|G|$ gives $\log|G|\ge -C_3\log T$ on the concentric radius-3 disk, uniformly in $R$.

Choose $r$ in $I=[\delta/4,\delta/2]$. For each $a$, writing $d_a=|a-s_*|$,
$$
 |I|^{-1}\int_I\log^+(1/|r-d_a|)\,dr\le \log(1/\delta)+C_4.
$$
Translate and scale the interval to length one and integrate the logarithmic singularity to obtain this uniform bound. Averaging the sum over $a$ gives one $r$ for which the sum of these logarithms is at most $C_2\log T(\log(1/\delta)+C_4)$. In particular the circle is disjoint from the zeros. Its minimum distance to each $a$ is $|r-d_a|$. Combining the factor bounds with Harnack gives $|\zeta(s)|\ge \exp[-C_5\log T(1+\log(1/\delta))]$ all around this circle. It lies in the radius-3 disk.

Map the circle to the $v$ plane, where its center is $w$. Let $\mathcal C$ be its positively oriented boundary and $\overline{\mathcal C}$ the positively oriented boundary of the conjugate disk. Write $H=\log T(1+\log(1/\delta))$. The completed-xi normalization and uniform Stirling bounds in this fixed real-part strip give
$$
 \max_{v\in\mathcal C\cup\overline{\mathcal C}} |\Xi(v)|^{-1}
 \le \exp(\pi T/4+C_6 H).
$$
Indeed the gamma factor has modulus comparable to an explicit power of $T$ times $\exp(-\pi(T+O(1))/4)$ and the other prefactors are polynomially bounded above and below. Conjugation preserves the modulus. Each disk lies entirely on one side of the real $v$ axis and the two disks are disjoint.

## 2. Exact projection onto all zeros in the disk

Let $\Phi$ be the even real theta source in R16 with $\widehat\Phi=\Xi$. Define
$$
 K_v(u)=\begin{cases}
 i\int_0^\infty \Phi(u+t)e^{ivt}\,dt,&u>0,\\
 -i\int_{-\infty}^0\Phi(u+t)e^{ivt}\,dt,&u<0.
 \end{cases}
$$
Its two expressions extended to all $u$ differ by $i e^{-ivu}\Xi(v)$. Its jump at zero is $i\Xi(v)$. Differentiating away from zero and adding this jump gives $(i\,d/du-v)K_v=\Phi-\Xi(v)\delta_0$ in distributions, hence
$$\widehat K_v(z)={\Xi(z)-\Xi(v)\over z-v}.$$
The removable value is understood. The rapid decay at both ends justifies the entire Fourier transform.

For a circle $D$ in the preceding pair set
$$
 f_D(u)={1\over 2\pi i}\int_D {K_v(u)\over\Xi(v)}\,dv.
$$
The difference between its two extended expressions is a contour integral of $i e^{-ivu}$ and vanishes. Thus $f_D$ is smooth on the whole line. For each zero $z\in\Gamma$ its transform is the contour integral of $1/(v-z)$ divided by $2\pi i$, and therefore equals one inside the disk and zero outside. Fubini is justified by the fixed contour and the tail bounds below. Consequently $f_\infty=f_{\mathcal C}-f_{\overline{\mathcal C}}$ has transform equal to $+1$ and $-1$ on the two clusters, respectively, and zero at every other zero. If the first disk contains $m$ zeros counted with multiplicity, the Weil sum for this rapidly decaying function is exactly $-2m$.

## 3. Truncation with all background zeros included

From the R16 theta series on $u\ge0$ and evenness, there are absolute $c_j,C_j$ such that for $j=0,1,2$ and $x\ge1$,
$$|\Phi^{(j)}(\pm x)|\le C_j \exp(c_j x-\pi e^{2x}).$$
Indeed differentiation gives polynomial factors in $n$ and $e^x$ times $\exp(-\pi n^2 e^{2x})$, and division by the $n=1$ exponential leaves a uniformly summable series. On the two circles $|\Im v|\le3/4$. Moving $u$ derivatives under the $K_v$ integral gives, for sufficiently large $x=|u|$,
$$
 |f_\infty^{(j)}(u)|\le C_7\exp(\pi T/4+C_6H+C_8x-\pi e^{2x}).
$$
Here $|e^{ivt}|\le e^{3|t|/4}$, the contour lengths are bounded by an absolute constant, and $e^{2(x+t)}\ge e^{2x}(1+2t)$ for $t\ge0$ controls the integral on each tail.

Let $S=T/4+CH$, $L=(\log S)/2$, and multiply $f_\infty$ by a smooth cutoff equal to one for $|u|\le L-2/S$ and zero for $|u|\ge L-1/S$, using a fixed smooth transition rescaled by $S$. Call the product $f$. For $e=f-f_\infty$ the preceding estimates imply
$$
 \sum_{j=0}^2 \int_{\mathbb R} e^{|u|/2}|e^{(j)}(u)|\,du
 \le C_9(1+S)^{C_{10}}
 \exp(\pi T/4+C_6 H-\pi S).
$$
Indeed $e^{2(L-2/S)}=S e^{-4/S}\ge S-4$, and derivatives of the cutoff cost $O(S^j)$. The remaining integration has the same exponential by $e^{2(x+t)}\ge e^{2x}(1+2t)$. Increase $C$ if needed to accommodate the fixed lower tail threshold. Since $H\gg\log T$ and $\log(1+S)=O(\log(1+C)+H)$, the right side can be made less than any chosen absolute positive constant by one sufficiently large absolute $C$.

For every zeta ordinate, integration by parts twice and $|\Im z|<1/2$ now give $|\widehat e(z)|\le \varepsilon/(1+|z|^2)$ for arbitrary prescribed absolute $\varepsilon>0$ by the same choice of $C$. Riemann–von Mangoldt counting implies $\sum_{\Gamma}(1+|z|^2)^{-2}<\infty$. Choose $\varepsilon$ so that $\|\widehat e\|_{\ell^2(\Gamma)}\le1/4$. Conjugation of the multiset is a unitary permutation; Cauchy–Schwarz therefore yields
$$
 W(f)\le -2m+2\sqrt{2m}/4+1/16<0
$$
for every $m\ge1$. This proves the theorem.

## 4. Translate the source toward the edge of the theta strip

For $0\le\theta<\pi/4$ put $\Phi_\theta(u)=\Phi(u+i\theta)$ and $F_\theta(z)=e^{\theta z}\Xi(z)$. The theta series defines an analytic function in $|\Im u|<\pi/4$ since $\Re e^{2u}>0$. The evenness identity extends there by analytic continuation. On each fixed closed substrip the double-exponential tail in both real directions justifies translating the Fourier integration contour, which gives $\widehat{\Phi_\theta}=F_\theta$. The multiplier is entire and zero-free, so the same contour formula selects the same clusters.

Let $\eta=\pi/4-\theta=\min(1/4,(H/T)^{1/3})$. The reciprocal estimate becomes $\exp(\eta T+C_6'H)$ because $\Re v=T+O(1)$ on both circles. There are absolute constants $c_j',C_j'$ such that for $j\le2$, $x\ge1$ and $\sin(2\eta)e^{2x}\ge1$,
$$
 |\Phi_\theta^{(j)}(\pm x)|\le C'_j \exp(c'_j x-\pi\sin(2\eta)e^{2x}).
$$
For positive real part this follows from the same differentiated series, since $\Re e^{2(x+i\theta)}=\sin(2\eta)e^{2x}$. After extracting the $n=1$ exponential, the residual terms are bounded by a polynomial in $n$ times $\exp(-\pi(n^2-1))$. Evenness gives the bound on the other side. There is no loss in the constants as $\eta$ decreases under the stated tail condition.

Take $D=T^{1/3}H^{2/3}+H$, $S=T/(2\pi)+CD$, and $L=(\log S)/2$. Throughout $x\ge L-2/S$ we have $\sin(2\eta)e^{2x}\gg\eta S$, and $\eta S$ can be made larger than any required fixed constant by increasing $C$, because $\eta D\gg H$. Repeat the truncation in §3 with these tilted sources. The upper bound there is now
$$
 C_9'(1+S)^{C_{10}'}\exp(\eta T+C_6'H-\pi\sin(2\eta)S).
$$
All polynomial factors and constants are uniform: integrating each tail uses $\sin(2\eta)e^{2x}\gg1$, and replacing $S$ by $Se^{-4/S}$ in the exponent costs at most $4\pi$. The excess at the leading term satisfies
$$
 \eta T-\tfrac12T\sin(2\eta)\ll T\eta^3\le H.
$$
Moreover $\sin(2\eta)D\gg \eta D\gg H$ in either branch of the definition of $\eta$. Since $\log(1+S)=O(\log(1+C)+H)$, increasing $C$ provides the same arbitrarily small evaluation error as before. The sign argument now proves the displayed theorem with its stated $L$.

**Remaining burden.** The theorem locates a test detecting an assumed defect. Proving positivity of the actual arithmetic Weil form on the resulting unbounded set of windows remains open. No numerical inputs or zero separation assumptions are used.

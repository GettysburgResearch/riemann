# An upper bound on the wait for the two quadratic bias witnesses

Let \(L=\log(3Q)\). For the discriminants outside the exceptional set in the [fixed-moment theorem](zhao-bias-moments-nov18.md), both signs, with normalized magnitudes at least \(c_A\sqrt L/2\), occur in every interval
\[
 [X,X^{\exp(C_A L^{3/2})}],\qquad \log X\ge L^3 .
\]
For the [stretched-exponential exceptional set](zhao-bias-blocks-nov18.md) the analogous statement has amplitude \(c'L^{1/4}/2\) and waiting exponent \(\exp(C L^{7/4})\). Both statements hold for sufficiently large \(Q\) under quadratic GRH. In particular they provide finite witness ranges for each conductor covered by the respective family theorems. The proof uses coarse phase precision for higher zeros.

## Uniform approximation by the zero profile

Write \(J_D(t)=-2/3-K_D(t)\) in the [prime-tail normalization](zhao-bias-kernel-nov18.md). Uniformly on \(Q<|D|\le2Q\), under GRH,
\[
 I_D(e^v)=J_D(v)+O(L/v+e^{-c\sqrt v}+v^2e^{-v/6}+(L+v)e^{-v/2}) \qquad(v\ge1).
\]
Here is one derivation of the conductor dependence. In the once-integrated Perron formula for \(-L'/L(s,\chi_D)Y^{s+1}/(s(s+1))\), shift the contour to \(\Re s=-1/2\). On this line the functional equation and absolute convergence at \(3/2\) give \(O(L+\log(2+|\Im s|))\) for the logarithmic derivative. The residue at zero costs \(O(Y(L+\log Y))\), by the functional equation and \(L'/L(1,\chi_D)\ll\log\log(3Q)\); the latter follows by GRH truncation at \((\log(3Q))^6\). One can take the contour heights tending to infinity a distance \(\gg1/\log(2Q(2+T))\) from all neighboring ordinates, by the usual local zero count and partial fraction expansion. The nontrivial-zero sum is absolutely convergent. Thus the primitive of \(\psi(t,\chi_D)\) equals \(-Y^{3/2}K_D(\log Y)+O(Y(L+\log(2Y)))\). The prime squares contribute \((2/3)Y^{3/2}+O(Y^{3/2}e^{-c\sqrt{\log Y}}+YL)\) by the classical prime number theorem and \(\sum_{p\mid D}\log p\le\log |D|\). Higher powers cost \(O(Y^{4/3}\log^2(2Y))\). The primitive of \(\theta(t,\chi_D)\) is \(O(LY^{3/2})\) for \(Y\ge2\), since the absolute zero coefficient mass is \(O(L)\). The partial summation in the prime-tail note now costs \(O(L/\log Y)\) after normalization. This proves the displayed estimate.

## Recurrence with a variable mesh

Suppose \(1\le h\le\sqrt L\) and at phases \(|u_\pm|\le L\) the profile \(J_D\) exceeds \(h\) and falls below \(-h\), respectively. Put \(T=C_0L/h\), with a sufficiently large absolute \(C_0\). The zero count per interval of length one is \(O(L+\log(2+|\gamma|))\). The absolute mass of ordinates \(|\gamma|>T\) is consequently \(O((L+\log(2+T))/T)\), at most \(h/16\) by the choice of \(C_0\). For each remaining distinct positive ordinate divide the circle \(\mathbb R/\mathbb Z\) into
\[
 m_\gamma=\left\lceil\frac{C_2 T^2}{1+\gamma^2}\right\rceil
\]
equal intervals. The product of these bin counts is at most \(\exp(C L T)\): on each unit ordinate interval there are \(O(L)\) coordinates, and \(\sum_{k\le T}[1+\log(T/(1+k))]\ll T\), with a bounded endpoint adjustment. Fix \(V=\log X\ge L^3\). By the pigeonhole principle two of the first \(1+\prod m_\gamma\) vectors \((j\cdot 2V\gamma/(2\pi))_\gamma\bmod 1\) occupy the same box. Their index difference \(k\) lies in \([1,\exp(CLT)]\), and the resulting phase multiplier differs from one at ordinate \(\gamma\) by at most \(2\pi/m_\gamma\). Including multiplicities and conjugates, the error incurred in the zero profile for these ordinates is
\[
 \ll\sum_{|\gamma|\le T}\frac{1}{(1+\gamma^2)m_{|\gamma|}}\ll\frac{LT}{C_2 T^2},
\]
where the central ordinate has zero error and is omitted. Choose \(C_2\) sufficiently large. Together with the tail error this gives \(\sup_t|J_D(t+2kV)-J_D(t)|\le h/4\). The phases \(v_\pm=2kV+u_\pm\) both lie between \(V\) and \(V\exp(C'L^2/h)\). At those phases the uniform approximation error tends to zero for \(Q\to\infty\). Hence \(I_D(e^{v_\pm})\) has the respective signs with magnitude at least \(h/2\).

Both family arguments produce their witnesses at \(u=-\log x\) with \(0\le\log x\le L\); their margins absorb replacing \(\log Q\) by \(L\). Applying the recurrence estimate at the two stated amplitudes proves the claims.

# A deterministic exclusion for Zhao's integrated quadratic prime bias

Assume GRH for the primitive quadratic character $\chi$ of conductor $D$. In the notation of the [prime-tail proof](zhao-bias-kernel-nov18.md), let $I_\chi(Y)$ be the normalized integrated prime bias and $K_\chi$ its absolutely convergent zero series. As $D\to\infty$, uniformly for those characters satisfying $L(1/2,\chi)\ne0$,
$$
 \limsup_{Y\to\infty} I_\chi(Y)\ \ge\ \frac23-O((\log\log D)^{-2}). \tag{1}
$$
For every primitive quadratic character, including those with central vanishing,
$$
 \liminf_{Y\to\infty} I_\chi(Y)\ \le\ -\frac{2}{3\sqrt3}\log D+O(\log\log D). \tag{2}
$$
Thus all sufficiently large conductors where the central value is nonzero fall outside the set in Zhao's question 2. The assertions are about each individual character under its own GRH.

## A low zero

Set $R=\tfrac13\log\log D$ and use the real even entire test function
$$
 h_R(t)=(1-R^2t^2)\left(\frac{\sin(Rt)}{Rt}\right)^4.
$$
It is nonpositive for $|t|\ge1/R$. Its inverse Fourier transform $g_R(u)=(2\pi)^{-1}\int h_R(t)e^{itu}dt$ has support in $[-4R,4R]$, has supremum norm $O(1/R)$, and $g_R(0)=1/(12R)$. The last equality follows from $\int_{\mathbb R}(\sin v/v)^4dv=2\pi/3$ by Plancherel, and $\int_{\mathbb R}\sin^4(v)/v^2\,dv=\pi/2$ by the cosine difference integral. Compact support follows from the fourfold convolution of intervals and its second derivative.

Apply the Dirichlet explicit formula to $h_R$. The prime term in absolute value is $O(R^{-1}\sum_{n\le e^{4R}}\Lambda(n)/\sqrt n)=O(e^{2R}/R)$ by Chebyshev's bound. The archimedean integral is $O(1/R)$ by the uniform real-axis digamma bound $O(\log(2+|t|))$ for both parities and $h_R(t)\ll(1+R^2 t^2)^{-1}$. Hence the sum of $h_R(\gamma)$ over all ordinates equals $(\log(D/\pi))/(12R)+O(e^{2R}/R)>0$ for large $D$. By GRH there is a zero with $|\gamma|<1/R$. Central nonvanishing forces such a zero to be nonreal.

## The Fourier coefficient of a nonnegative function

For $\gamma\ne0$ of multiplicity $m_\gamma$ write $c_\gamma=m_\gamma/[(1/2+i\gamma)(3/2+i\gamma)]$. The Bohr mean of $K_\chi$ is $4m_0/3$ where $m_0$ is the central multiplicity. The nonnegative uniformly almost periodic function $K_\chi-\inf K_\chi$ has coefficient $c_\gamma$ and mean $4m_0/3-\inf K_\chi$. The triangle inequality for its long-interval means gives
$$
 -\inf K_\chi\ge |c_\gamma|-4m_0/3.
$$
This step uses no assumption on relations among the ordinates. When $m_0=0$ the low zero above has $|c_\gamma|\ge 4/3-O(R^{-2})$. Almost-periodic recurrence gives $\limsup I_\chi=-2/3-\inf K_\chi$, proving (1). At an individual conductor the same argument gives a computable strict witness whenever $|c_\gamma|>(2+4m_0)/3$.

## An opposite excursion for every character

Evaluate the explicit formula for $K_\chi(t)$ at $t=\log 3$ using $g(u)=k(u+t)$, where $k(v)=(e^{-v/2}-e^{-3v/2})\mathbf1_{v>0}$. The conductor term is $g(0)\log(D/\pi)$ with $g(0)=2/(3\sqrt3)$. The digamma integral is absolutely convergent and $O(1)$ for this fixed $t$, since the transform decays quadratically. The reflected prime term $g(-\log n)$ has support $n<3$ and is $O(1)$. The remaining prime term is a fixed linear combination of $\sum\Lambda(n)\chi(n)/n$ and $\sum\Lambda(n)\chi(n)/n^2$. The second sum is absolutely bounded. Truncate the first at $L=(\log D)^6$. Its initial portion is $O(\log L)$ by Chebyshev and its tail is $O(L^{-1/2}\log^2(2DL))$ by partial summation and the GRH bound for $\psi(x,\chi)$. Damping the shifted kernel by $e^{-\epsilon(u+t)}$ on its support justifies the formula by Abel convergence. Thus $K_\chi(\log3)= 2\log D/(3\sqrt3)+O(\log\log D)$. Positive-time recurrence gives (2).

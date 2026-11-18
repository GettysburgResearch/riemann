# Arithmetic second moment at the Nyquist radius

**Status.** Proposed unconditional arithmetic estimate. On average over the carrier center, at least $3/4-o(1)$ of the eigenvalues in a growing block of critical Fourier modes are strictly positive. For four consecutive modes a positive fraction of centers have a positive definite matrix. The estimates use the signed von Mangoldt phases, without a local census of zeros.

## Statement and normalization

Take $Y=X/(2\pi)$, $U=\log Y$, $L=U/2$, and let $\omega$ be uniformly distributed on $[X,2X]$. Use $D$ consecutive integer modes $j$ with $\max |j|\pi/L\le X/4$, including any consecutive block near zero of polylogarithmic size. Let $0\le\chi\le1$ be a smooth real cutoff supported in $(-L,L)$ and equal to one on $[-L+2,L-2]$, with $\|\chi'\|_1=O(1)$. These assumptions allow transitions narrower than unit width and include the convolution tapers used in the [local matrix](weil-bandwidth-nov18.md). Set
\[
  g_j(u)=\chi(u)e^{-i(\omega+j\pi/L)u}/\sqrt{2L},\qquad
  A_\omega=(W(g_k,g_j))_{jk}.
\]
The radius is fixed over the dyadic averaging interval and equals the Nyquist radius at its left endpoint. All estimates below also apply if $Y\asymp X$ with $U=\log Y$, by exactly the same proof. The modulations here slide continuously, instead of restricting $\omega$ itself to one lattice. Write $n_{\le0}$ for the count of nonpositive eigenvalues.

For fixed $D$, put
\[
      V_D=D/6+\sum_{l=1}^{D-1}(D-l)/(\pi^2l^2).
\]
Then
\[
 \mathbb E\,n_{\le0}(A_\omega)\le {D V_D\over D+V_D}+o(1).
\]
This also bounds the proportion of centers with any nonpositive eigenvalue. At $D=1$ it gives strict positivity for at least $6/7-o(1)$ of centers. At $D=4$ the lower bound on the proportion with positive definite matrix is $1-4V_4/(4+V_4)-o(1)>0.17-o(1)$.

For any $D=D(X)\to\infty$ in the stated frequency range,
\[
     D^{-1}\mathbb E\, n_{\le0}(A_\omega)\le 1/4+o(1).
\]
This averaged eigenvalue count allows a negative eigenvalue at every center in a large block.

## The arithmetic mean and second moment

Write $e_j(u)=(2L)^{-1/2}1_{[-L,L]}(u)e^{-ij\pi u/L}$. For $0\le s\le U$ let $C_s$ denote the matrix of the translated cutoff overlaps $\int(\chi e_k)(u+s)\overline{(\chi e_j)(u)}du$. It is the compression of a translation with two contraction multipliers, so $\|C_s\|_{\rm op}\le1$. The full Hermitian prime part to subtract is
\[
 P_\omega=Z_\omega+Z_\omega^*,\qquad
 Z_\omega=\sum_{n\le Y}\Lambda(n)n^{-1/2}e^{-i\omega\log n} C_{\log n}.
\]
In particular $\|\mathbb EP_\omega\|_{\rm op}\ll X^{-1}\sum_{n\le Y}\Lambda(n)/\sqrt n=O(X^{-1/2})$ by oscillatory integration and Chebyshev.

The Montgomery–Vaughan mean value inequality, applied to each matrix entry, and the bound $\|C_s\|_{\rm HS}^2\le D$, give
\[
 \mathbb E\operatorname{tr}(P_\omega^2)
 =2\sum_{n\le Y}{\Lambda(n)^2\over n}\|C_{\log n}\|_{\rm HS}^2+O(D\log X).
\]
Indeed the weighted mean-value error in $\mathbb E\|Z_\omega\|_{\rm HS}^2$ costs at most $D X^{-1}\sum_{n\le Y}\Lambda(n)^2\ll D\log X$. The same-sign terms $\mathbb E\operatorname{tr}(Z_\omega^2)$ and their conjugates cost $O(DX^{-1}(\sum_{n\le Y}\Lambda(n)/\sqrt n)^2)=O(D)$ since $\log(nm)\ge\log4$ and $|\operatorname{tr}(C_s C_r)|\le D$. These estimates include every prime power.

Replacing the taper by the full box changes each $\|C_s\|_{\rm HS}^2$ by $O(D/\sqrt L)$ uniformly: the Hilbert–Schmidt norm of multiplication by $1-\chi$ on the uncut basis is at most $O(\sqrt{D/L})$ on the interval, and each of the two difference terms has the other factors contractive. For the box put $y=s/U$. Direct integration over the overlap gives diagonal entry magnitude $1-y$ and off-diagonal entry magnitude $|\sin(\pi l y)|/(\pi|l|)$ at index difference $l$. Hence its squared Hilbert–Schmidt norm divided by $D$ is
\[
 H_D(y)=(1-y)^2+2\sum_{l=1}^{D-1}(1-l/D)\frac{\sin^2(\pi l y)}{\pi^2l^2}.
\]
As $D\to\infty$, $H_D(y)\to1-y$ uniformly on $[0,1]$ by Parseval for an interval indicator and the summable Fourier-square tail (the uniform error is $O((1+\log D)/D)$).

The prime number theorem and partial summation give $\sum_{n\le e^u}\Lambda(n)^2/n\sim u^2/2$, so the measures $U^{-2}\sum_{n\le Y}\Lambda(n)^2 n^{-1}\delta_{\log n/U}$ converge weakly to $y\,dy$. Thus for fixed $D$ the limit of $U^{-2}\mathbb E\operatorname{tr}P_\omega^2$ is $2D\int_0^1 y H_D(y)dy=V_D$. Here $\int y(1-y)^2dy=1/12$ and $\int y\sin^2(\pi ly)dy=1/4$ over $[0,1]$. For growing $D$, uniform convergence gives the limit $1/3$ after dividing additionally by $D$, since $2\int_0^1y(1-y)dy=1/3$.

## Positive gamma reserve in all but a negligible fraction of directions

The unnormalized gamma term is $G_{jk}=(2\pi)^{-1}\int \mu(t)\widehat g_k(t)\overline{\widehat g_j(t)}dt$ with $\mu(t)=\Re\psi(1/4+it/2)-\log\pi$. Let $Q$ be the Gram matrix of the cutoff modes. Then $0\le Q\le I$, and $\operatorname{tr}(I-Q)=O(D/L)$ from the width of the transition region. Uniformly for $\omega\in[X,2X]$,
\[
              \|G-UQ\|_{\rm tr}=O(D).
\]
Indeed integrate $|\mu(t)-U|\sum_j|\widehat g_j(t)|^2/(2\pi)$. It is $O(D)$ on $[X/4,4X]$ by Stirling and Plancherel. Off that interval use $|\widehat g_j(t)|\ll L^{-1/2}|t-\omega-j\pi/L|^{-1}$ by integration by parts, whose squared integral against $O(\log(2+|t|)+U)$ is $O(1)$ per mode. The two pole matrices have combined trace norm $O(D e^L/(L X^2))$ by the same integration by parts at $\pm i/2$. The explicit formula consequently reads
\[
                  A_\omega=U I-P_\omega+R_\omega,
       \qquad \|R_\omega\|_{\rm tr}=O(D).
\]
The bound includes $U(I-Q)$. No lower frame bound for the cutoff basis is required.

## Counting signs

Put $\epsilon=U^{-1/2}$. At most $O(D/(\epsilon U))$ singular values of $R_\omega$ exceed $\epsilon U$. Min–max bounds $n_{\le0}(A_\omega)$ by this count plus $\#\{\lambda(P_\omega)\ge(1-\epsilon)U\}$. For every $a\ge0$ the latter is at most $\operatorname{tr}(P_\omega/U+aI)^2/(1-\epsilon+a)^2$. Using the signed first moment and the second moment above, take $a=V_D/D$ for fixed $D$, and $a=1/3$ for growing $D$. This proves both assertions. All phase cancellation used here takes place on the arithmetic side of the explicit formula.

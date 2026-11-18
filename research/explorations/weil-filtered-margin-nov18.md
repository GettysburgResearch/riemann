# Compact translation filters for a conditioned Weil witness

**Status.** Proposed theorem, conditional on an actual off-line zero. This construction complements the [pole-free comparison](weil-prime-margin-nov18.md). A change of tilt and finite physical translations avoid its exponentially small relative margin, with a slightly wider support. No arithmetic sign is assumed.

Let $T,\delta,H=\log T(1+\log(1/\delta))$ be as in the [contour construction](weil-contour-nov18.md). Along any defect sequence with $H=o(T)$ there is a pole-free smooth test $g$ with support radius
\[
 L_g\le \tfrac12\log(T/(2\pi))+
 O\left(\sqrt{(H/T)(1+\log(T/H))}\right)
\]
for which, using the same signed prime autocorrelation $P$ and gamma integral $G$ as in the pole-free comparison,
\[
 T^{-2}\ll G(g)\le e^{CH},\qquad
 c m\le P(g)-G(g)\le C m .
\]
Here $m\ge1$ is the multiplicity count in the target disk. In particular the relative excess over the full gamma integral is at least $e^{-C'H}$, an inverse power of $T$ for fixed $\delta$. These bounds describe the tests attached to existing defects. Establishing a prime-side inequality that excludes such tests is still open.

## Pointwise size before filtering

Put $M=1+\log(T/H)$, $\eta=\sqrt{H/(TM)}$, and use the contour projector with $F(z)=e^{(\pi/4-\eta)z}\Xi(z)$. Eventually $0<\eta<1/4$ and $\eta T/H\to\infty$. The truncation in the companion with $e^{2L}=(\eta T+C H)/(\pi\sin(2\eta))$ makes both the uniform Fourier error $|\widehat f-\widehat f_\infty|\le\varepsilon/(1+|z|^2)$ on the full zero strip and its zero-sample $\ell^2$ norm at most any prescribed absolute bounds of this form. This gives $L\le \tfrac12\log(T/(2\pi))+O(\eta^2+H/(\eta T))$.

For real $t$, which is exterior to both contours, the exact projector satisfies
\[
 |\widehat f_\infty(t)|\le (1+|t|)^C\exp(\eta T+C H-\eta|t|).
\]
Indeed divide the contour formula by $F(t)$. It becomes the signed integral of $1/[F(v)(t-v)]$, since the term with no $1/F(v)$ has zero integral. The contour radius divided by its distance to the real axis is at most one. The reciprocal bound from the companion and the real-axis Stirling bound on $F(t)$ give the result, including its stronger decay for $t<0$. For $|t|\ge T$ this already gives
\[
 \int_{|t|\ge T}(1+\log(2+|t|))|\widehat f_\infty(t)|^2dt\le e^{C'H}.
\]
To see this, shift $|t|=T+u$. The residual polynomial moments of $e^{-2\eta u}$ are polynomial in $T$ and $1/\eta$, both absorbed into $e^{O(H)}$.

## The translation filter on the remaining frequencies

Write $\Delta=H/\eta$ and $d_j=2^j\Delta$ for $j=0,\dots,J$ with $J$ the least nonnegative integer such that $2d_J\ge2T$. Set
\[
 s_j=\pi/(4d_j),\qquad k_j=\lceil 4\eta d_j/\log 2\rceil,\qquad
 B(z)=\prod_{j=0}^J \cos(s_j(z-T))^{k_j}.
\]
On the real line $|B|\le1$. For $d=|t-T|\in[d_j,2d_j]$ the $j$th cosine has modulus at most $1/\sqrt2$, so $|B(t)|\le e^{-2\eta d_j}\le e^{-\eta d}$. For $d<\Delta$ the unfiltered envelope loss is at most $e^{\eta d}\le e^H$. These two observations and $T-|t|\le d$ bound $|B(t)\widehat f_\infty(t)|$ by $e^{C H}$ on $[-T,T]$. Combining with the preceding tail bound gives a logarithmically weighted real-axis squared norm at most $e^{C'H}$, also after truncation because the absolute cutoff error has finite weighted norm.

Each cosine is a linear combination of two translations. The total additional radius obeys
\[
 \sum_j k_j s_j\ll \eta(1+\log(T/\Delta))+1/\Delta
       \ll \sqrt{HM/T}.
\]
Moreover $\sum_j k_j s_j^2\ll\eta/\Delta+1/\Delta^2=o(1)$. The inequalities $|\cos(s_j(z-T))|\le\cosh(s_j/2)$ for $|\Im z|\le1/2$ and $\log\cosh y\le y^2/2$ give $|B|\le1+o(1)$ throughout the strip. Taylor expansion gives $B(z)=1+o(1)$ uniformly when $|z-T|\le1$. Thus the filter preserves the cluster samples while keeping the error on the full zero multiset bounded in $\ell^2$.

## Pole-free arithmetic comparison

Let $\tau=\pi/(2T)$. Postmultiply $B\widehat f$ by
\[
 b(z)=\sin(\tau z)^k[\cos(\tau z)-\cosh(\tau/2)],
 \qquad k=\lceil C_0 H/\log T\rceil
\]
for a sufficiently large absolute $C_0$, and denote the resulting transform by $\widehat g$. The added radius $O((k+1)/T)$ is within the stated allowance. As before $b(\pm i/2)=0$, $|b|\le5$ on the zero strip, and $b=-1+o(1)$ on both disks since $k=o(T)$. With an initially sufficiently small $\varepsilon$, the full zero sum is therefore $-\Theta(m)$ by the same conjugation and Cauchy–Schwarz calculation as in the pole-free comparison. The pointwise sample at the specified defect has modulus at least $1/2$.

Stirling gives fixed $R$ such that the gamma density $\mu(t)\ge1$ for $|t|\ge R$, and $|\mu(t)|\ll1+\log(2+|t|)$ everywhere. On $|t|\le R$ the sine factor is bounded by $(C_R/T)^k$ after taking the power. The preceding $e^{CH}$ norm bound and the choice of $C_0$ make the squared norm on this band $O(T^{-4})$. On the other hand, the sample at $w$ and Cauchy–Schwarz give
\[
 \tfrac12\le |\widehat g(w)|\le (2L_g)^{1/2}e^{L_g/2}\|g\|_2.
\]
Since $L_g\le\log T$ eventually, Plancherel gives total squared Fourier norm $\gg 1/(T\log T)$. Its mass outside the fixed band dominates the negative gamma part therefrom, proving $G(g)\gg T^{-2}$. The logarithmically weighted norm gives the upper bound for $G$. The pole-free explicit formula now yields $P(g)-G(g)=-W(g)=\Theta(m)$ as claimed. The argument controls the actual signed sum; it does not bound it term by term.

# Sharp logarithmic norm scale for the xi-weighted translations

Reviewer rt_repair_62. This is a quantitative follow-up to the [RH-conditional spectral audit](xi_weighted_semigroup_rt62_xi_semigroup.md) of \(W_\tau f=F(w)f(w+\tau)/F(w+\tau)\), where \(F(w)=\xi(1/2+w)\) and the numerator \(f(w+\tau)\) is multiplied by \(F(w)\). In particular, the weight is \(H_\tau(w)=F(w)/F(w+\tau)\). The conclusion is
\[
 \log\|W_\tau\|=-\frac{\tau}{2}\log\tau+
      \frac{\tau}{2}(1+\log(2\pi))+O(\log\tau).
\]

Write \(s=r+1/2+it\). For \(r\ge2\), the logarithmic derivative is
\[
 G(r+it)=1/s+1/(s-1)-\tfrac12\log\pi
       +\tfrac12\psi(s/2)+\zeta'(s)/\zeta(s).
\]
The rational terms are \(O(1/r)\) uniformly in \(t\). The absolutely convergent von Mangoldt series gives \(|\zeta'(s)/\zeta(s)|\le2^{-(\Re s-2)}\sum_{n\ge2}\Lambda(n)n^{-2}=O(2^{-r})\). The digamma expansion \(\psi(u)=\operatorname{Log}u+O(1/|u|)\) holds uniformly in the closed sector \(|\arg u|\le\pi/2\) at large \(|u|\), and a compact bounded region with \(\Re u\ge5/4\) can be included by increasing the constant. Thus
\[
 \Re G(r+it)=\frac12\log\frac{|r+1/2+it|}{2\pi}+O(1/r)
 \quad(r\ge2,\ t\in\mathbb R).
\]
No critical-line estimate enters this approximation.

On RH, the weight \(H_2\) is Schur by the paired Hadamard product. For \(\tau\ge2\),
\[
 |H_\tau(it)|=|H_2(it)|\exp\!\left(-\int_2^\tau\Re G(r+it)\,dr\right)
 \le\exp\!\left(-\frac12\int_2^\tau\log\frac{r}{2\pi}\,dr+O(\log\tau)\right).
\]
The product factorization applies even at a boundary zero, where \(H_2(it)=0\); taking its logarithm separately would not be legitimate at those points. The upper bound is uniform in \(t\). The boundary multiplication norm and contractivity of horizontal translation give the upper estimate for \(\log\|W_\tau\|\), with linear coefficient \((1+\log(2\pi))/2\).

For the lower bound, denote the unnormalized evaluation vector at fixed \(x>0\) by \(K_x\), with norm \((2x)^{-1/2}\) for boundary normalization \(dt/(2\pi)\). The adjoint identity \(W_\tau^*K_x=\overline{H_\tau(x)}K_{x+\tau}\) yields
\[
 \log\|W_\tau\|\ge \log|F(x)|-\log|F(x+\tau)|
                 +\tfrac12\log(x/(x+\tau)).
\]
The complete xi expression and real Stirling give
\(\log|F(x+\tau)|=(\tau/2)\log\tau-(\tau/2)(1+\log(2\pi))+O_x(\log\tau)\); the rational prefactor contributes \(O_x(\log\tau)\), and \(\zeta(1/2+x+\tau)=1+o(1)\). The kernel norm ratio costs only \(O_x(\log\tau)\), so this proves the matching lower bound. The uniform upper estimate and single-kernel lower estimate fix the linear coefficient independently of boundary singularities. Scope is this specific RH-conditional semigroup. Priority is unassessed.

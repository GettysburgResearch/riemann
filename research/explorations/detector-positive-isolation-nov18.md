# A hypothetical off-line zero forces both signs in every fixed-ratio window of sufficient width

Status — Proposed analytic theorem for the original 5:3 arithmetic detector. The imported arithmetic estimate is the classical Ingham zero-density bound. No numerical zero data or residue-summability hypothesis enters this argument.

Let \(W(X)=5c_X(2)+3c_X(3)\). If \(\rho_0=1/2+a+i\gamma_0\) is an actual zeta zero with \(a>0\) and multiplicity \(m\), there exist constants \(B>1,\ c>0,\ Y_0\), depending on that zero and the actual spectrum, such that for every \(Y\ge Y_0\),
\[
 \min\left\{\int_{Y/B}^Y W(X)_+\,\frac{dX}{X},\
             \int_{Y/B}^Y W(X)_-\,\frac{dX}{X}\right\}
 \ \ge cY^a(\log Y)^{m-1}.
 \tag{1}
\]
The target may lie to the left of other zeros. In particular, if an unbounded sequence \(Y_j\) satisfies
\[
 \int_1^{Y_j} W(X)_-\,\frac{dX}{X}=Y_j^{o(1)}
 \quad\text{in the sense of upper bounds,}
 \tag{2}
\]
then RH follows. There is no restriction on gaps between the \(Y_j\). The same holds with the integral restricted to \([Y_j/B_j,Y_j]\) whenever \(B_j\to\infty\), \(1\le B_j\le Y_j\). Under RH the classical Mertens bound gives the subpower upper bound on all horizons. Whether (2) holds for the arithmetic source remains open.

## 1. The Mellin transform and the sparse set to remove

Extend \(w(u)=W(e^u)\) by zero for \(u<0\). Its Laplace transform on \(\Re s>1/2\) is
\[
 F(s)=\frac1{s^2}\left(6+\frac{P(1/2+s)}{\zeta(1/2+s)}\right),\qquad
 P(z)=-3(2^{-z}-1)(2^{-z}-2).
\]
The fixed numerator is nonzero throughout the critical strip. The [original primitive arithmetic sum](https://github.com/GettysburgResearch/riemann/blob/433fd3662f7b2e4ba384ce64f196380e88624090/claims/lemmas/L-99261-five-three-row-zero-free-mellin-witness.md) is continuous in \(u\) and grows at most \(O(e^u)\); its transform is integrable on \(\Re s=1\). We may take \(\gamma_0>0\) by conjugation and put \(s_0=a+i\gamma_0\).

Choose \(0<\alpha_0<\alpha<a\). The choice of \(\alpha\) can and will ensure
\[
 |\alpha-(\Re\rho-1/2)|\ge c_0(1+|\Im\rho|)^{-3}
 \tag{3}
\]
for every nontrivial zeta zero. Indeed the sum of these radii is finite by the Riemann–von Mangoldt count. Starting with any fixed closed interval of positive length inside \((\alpha_0,a)\), choose \(c_0\) sufficiently small to leave positive measure after exclusion.

For fixed \(\sigma=1/2+\alpha_0>1/2\), Ingham's bound
\(N(\sigma,T)\ll T^{3(1-\sigma)/(2-\sigma)}(\log T)^5\)
implies \(N(\sigma,T)=O(T^k)\) for some \(k<1\). This count includes multiplicities. Partial summation gives
\[
 \sum_{\substack{\Re\rho>1/2+\alpha\\ \Im\rho>0}}
                \frac{m_\rho}{\Im\rho}<\infty ,
 \tag{4}
\]
where the summation in (4) is over distinct zeros. This summability pays for finite support of a positive measure which removes every competing pole at once.

## 2. A compact positive measure that preserves the selected conjugate pair

Consider each competing shifted zero \(s_1=b+i\gamma\), \(b>\alpha,\gamma>0\), distinct from \(s_0\). Choose an integer \(r\ge2\). Normally use \(r=2\). In the exceptional case \(b=a\) and \(\gamma_0/\gamma\) an odd integer \(j\ge3\), use \(r=j\). With \(h=2\pi/(r\gamma)\), form the probability measure
\[
 \mu_1=\frac{\sum_{\ell=0}^{r-1}e^{b\ell h}\delta_{\ell h}}
                  {\sum_{\ell=0}^{r-1}e^{b\ell h}} .
\]
Its Laplace transform vanishes at \(s_1\) because the numerator becomes a sum of all \(r\)-th roots of unity. It also vanishes at \(\overline{s_1}\). Every zero of this finite geometric sum has real part \(b\), and on this line a frequency \(t\) is killed precisely when \(t/\gamma\) is an integer which is not divisible by \(r\). Thus the chosen \(r\) preserves \(s_0,\overline{s_0}\). The ratio one with \(b=a\) is the target itself and was omitted.

Convolve \(m_{\rho_1}\) copies of \(\mu_1\) for each competing zero. Each copy has support in \([0,2\pi/\gamma]\). By (4), the infinite convolution exists as a probability distribution supported in \([0,D_0]\) for finite \(D_0\). For example it is the law of the sum of independent bounded variables whose deterministic support lengths sum to \(D_0\). Its transform is the locally uniformly convergent product of the factor transforms. For \(s\) in a compact set, a factor differs from 1 by \(O_s(1/\gamma)\), uniformly for large \(\gamma\), by integrating \(e^{-sx}-1\) over its support. Consequently the product at \(s_0\) is nonzero. At each unwanted pole it vanishes at least to the required multiplicity, since its finite corresponding factors can be separated from the remaining probability convolution.

## 3. A smooth positive kernel and a contour estimate

Convolve this measure with the distribution of \(\sum_{j\ge1}U_j\), for independent \(U_j\) uniform on \([-j^{-2},j^{-2}]\). Its support is compact and its transform is
\[
 J(s)=\prod_{j\ge1}\frac{\sinh(j^{-2}s)}{j^{-2}s}.
\]
Each factor is nonzero for \(\Re s>0\), and the product converges to a nonzero value at \(s_0\) because its tail deviations are \(O_{s_0}(j^{-4})\). On any fixed bounded vertical strip,
\[
 |J(s)|\le C e^{-c\sqrt{|s|}}\quad(|s|\ge2).
\]
Indeed each factor is bounded by \(e^{j^{-2}|\Re s|}\min(1,j^2/|s|)\) by its integral representation and the elementary bound on \(|\sinh|\). For \(j\le\sqrt{|s|/2}\), the second factor is at most \(1/2\). Fourier inversion now shows the resulting probability convolution has a bounded smooth density \(K\ge0\), supported in a fixed interval \([L,R]\). Write \(Q(s)=\int K(x)e^{-sx}dx\). The first probability convolution has bounded transform on every bounded vertical strip. Thus \(Q\) inherits the stated decay and \(Q(s_0)\ne0\).

On \(\Re s=\alpha\), (3) gives
\[
 \left|1/\zeta(1/2+s)\right|\le \exp(C\log^2(2+|\Im s|)).
 \tag{5}
\]
For the details, the classical local partial fraction formula for \(\zeta'/\zeta(v+it)\) in \(1/2\le v\le2\) subtracts the sum of \(1/(v+it-\rho)\) over \(|\Im\rho-t|\le1\) with error \(O(\log(2+|t|))\) at large height. Integrate its real part horizontally from \(2+it\), with the corresponding local logarithms of distances subtracted first. The bound extends through intermediate zero ordinates by continuity at nonzero endpoints. There are \(O(\log(2+|t|))\) local terms, and (3) bounds the endpoint distance below by a constant times \((2+|t|)^{-3}\). The Euler product bounds the starting reciprocal, proving (5). The same bound holds along cofinal horizontal lines from \(\alpha\) to 1 at heights a distance \(\gg1/\log(2+|t|)\) from every zero ordinate. Such heights in successive unit intervals exist by the local count. For bounded heights use compactness away from zeros.

Fourier inversion initially on \(\Re s=1\) expresses
\((K*w)(u)\) as the inverse integral of \(Q(s)F(s)e^{su}\); compact support and absolute integrability on that line justify the product rule. Shift to \(\Re s=\alpha\) along the heights just described. Every pole between the lines except \(s_0,\overline{s_0}\) is canceled, the point corresponding to the pole of zeta is regular, and zero lies left of the contour. The decay \(e^{-c\sqrt{|t|}}\) dominates (5), giving absolute convergence on the left and vanishing horizontal integrals for each fixed \(u\). The new vertical integral is \(O(e^{\alpha u})\), with a fixed constant uniform in \(u\ge0\). Thus
\[
 (K*w)(u)=2e^{au}\Re\!\left(e^{i\gamma_0u}p(u)\right)+O(e^{\alpha u})
 \tag{6}
\]
for a polynomial \(p\) of degree exactly \(m-1\). Its leading coefficient is
\[
 c_*=\frac{Q(s_0)}{(m-1)!}
            \frac{m!P(\rho_0)}{s_0^2\zeta^{(m)}(\rho_0)}\ne0 .
\]

## 4. One-sided mass in every sufficiently large window

There are two arithmetic progressions of centers, each with spacing \(T_0=2\pi/\gamma_0\), for which \(e^{i\gamma_0u}c_*\) equals \(+|c_*|\) or \(-|c_*|\). Equation (6) therefore gives \((K*w)(u)_\pm\ge c_1 e^{au}u^{m-1}\) for every sufficiently large center of the corresponding progression. Positivity and compact support yield
\[
 (K*w)(u)_\pm\le \|K\|_\infty\int_{u-R}^{u-L}w(v)_\pm\,dv .
\]
Given \(T=\log Y\), choose one center from each progression in \([T+L-T_0,T+L]\). Its integration interval belongs to \([T-(R-L+T_0),T]\). Since \(u=T+O(1)\), taking \(B=\exp(R-L+T_0)\) proves (1). This step requires a nonnegative physical kernel. A signed annihilating test controls absolute mass but does not yield the two separate inequalities.

If (2) holds, (1) excludes all zeros with \(\Re\rho>1/2\), and the functional equation gives RH. Conversely the classical RH estimate \(\sum_{n\le x}\mu(n)=O_\epsilon(x^{1/2+\epsilon})\), followed by partial summation in the finite dilates defining the primitive row, gives \(w(\log X)=O_\epsilon(X^\epsilon)\). Integrating with a smaller exponent yields the required cumulative bound. Both implications use a single fixed arithmetic row throughout. The kernel in the proof of necessity can depend on a hypothetical zero because it tests the mass of that already fixed row.

An arithmetic proof of subpower negative mass even on one unbounded sequence would resolve the criterion. The constants in (1) are existential, since the product uses the actual complete set of off-line poles in the selected half-plane.

# A local prime-power inequality at polynomial precision

**Status.** Proposed direct arithmetic consequence of the [bandwidth theorem](weil-bandwidth-nov18.md). Fix once and for all the displacement resolution $d\in(0,1/2)$ and an allowed additive radius excess $\tau>0$. Use $B=K_\tau H$, $H=(1+\log(1/d))\log X$ and the trial functions of that theorem. Its constants, including $C_0$, can depend on the fixed $d,\tau$ in the assertions below.

Normalize coefficient vectors by $\sum|a_k|^2=1$ and put $g=\sum a_k g_k$. Let $\mathscr D=i\,d/dx$, whose Fourier multiplier with the chosen positive-exponential transform is $t$. Define
$$
 M(t)=\Re\psi(1/4+it/2)-\log\pi,\qquad
 Q_{r,X}(t)=\sum_{j=0}^r {M^{(j)}(X)\over j!}(t-X)^j.
$$
Here $\psi=\Gamma'/\Gamma$. Define the finite signed prime-power contribution
$$
 P(g)=2\Re\sum_{2\le n<S}{\Lambda(n)\over\sqrt n}
           \int_{\mathbb R} g(x+\log n)\overline{g(x)}\,dx .
$$
The sign is immaterial to the orientation of the translation because the real part is taken.

**Proposition.** For every fixed $A>0$ there exists a fixed nonnegative integer $r$ such that for all sufficiently large $X$, uniformly over the trial vectors,
$$
 \left|W(g)-\big(\langle Q_{r,X}(\mathscr D)g,g\rangle-P(g)\big)\right|
 \le X^{-A}.
$$
Here the scalar product is linear in the first argument. Consequently, proving
$$
 P(g)\le\langle Q_{r,X}(\mathscr D)g,g\rangle + X^{-A}
$$
at every sufficiently large center and all its vectors, with $A>C_0(1+\log(1/d))+1$ and $r$ as above, excludes all sufficiently high zeros with displacement $\ge d$. The differential order, number of terms per entry outside the prime sum, and required inverse-polynomial precision exponent are fixed for this strip. The number of coefficients is $O_{d,\tau}((\log X)^2)$.

## Proof

The classical explicit formula in this Fourier normalization reads
$$
 W(g)=2\Re(\widehat g(i/2)\overline{\widehat g(-i/2)})
 +{1\over2\pi}\int_{\mathbb R}M(t)|\widehat g(t)|^2\,dt-P(g).
$$
The prime sum truncates at $S$ by support. The archimedean multiplier follows from the two factors $\Gamma_{\mathbb R}(s)=\pi^{-s/2}\Gamma(s/2)$ on the critical line.

We spell out the required localization, since small absolute errors matter in this comparison. The box-convolved cutoff has $m=\lceil H\rceil$ factors, transition width $H/B$, and Fourier estimate from the [exterior lemma](weil-local-complement-nov18.md). For each fixed $A'>0$ and fixed $r$, there is a constant $D_{A',r}>C'$ such that
$$
 |\widehat g(i/2)|+|\widehat g(-i/2)|\ll X^{-A'},\qquad
 \int_{|t-X|>D_{A',r}B}
     (1+|t|+\log X)^{r+2}|\widehat g(t)|^2dt\ll X^{-A'} .
$$
Indeed each mode carries a factor $(c B/|t-X|)^m$ when $|t-X|>2C'B$, or $(cB/X)^m$ at the poles. The prefactors consist of powers of $X$ for fixed $r$. On the real tails retain $r+4$ powers for integrability, and use the other $m-r-4$ to beat the desired fixed polynomial by increasing $D_{A',r}$. Cauchy–Schwarz sums at most $O((\log X)^2)$ modes. The estimates apply to the fixed cutoff independent of $A',r$.

Uniform differentiated Stirling on $|t-X|\le D_{A',r}B$ gives $|M^{(j)}(t)|\ll_j X^{-j}$ for fixed $j\ge1$. For instance, the real-analytic continuation there is the half sum of $\psi(1/4\pm iz/2)-\log\pi$ (with the constant subtracted once); their Stirling expansions on disks of radius $cX$ and Cauchy bounds give the derivative estimates. Thus $|M(t)-Q_{r,X}(t)|\ll_{r,D}(B/X)^{r+1}$ on this band. Globally $|M(t)|\ll\log(2+|t|)$ and $|Q_{r,X}(t)|\ll_r(1+|t|+\log X)^{r+1}$. The cutoff contraction gives $\|g\|_2\le1$. Use the local bound, the exterior estimates, Plancherel and the two pole bounds in the explicit formula. Since $B\asymp_{d,\tau}\log X$, choosing $r>A+1$ and $A'>A+1$ proves the asserted accuracy once $X$ is large. The arithmetic consequence follows by the negative margin in the bandwidth theorem.

**Remaining arithmetic burden.** The signed translation bound above has not been proved. Pointwise control of the unsmoothed Dirichlet polynomial is stronger than the required control of its quadratic averages, since each test is constrained in physical support and modulation bandwidth.

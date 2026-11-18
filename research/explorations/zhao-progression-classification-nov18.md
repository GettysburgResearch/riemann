# Classification of integrated prime biases in reduced residue classes with independent ordinates

Assume GRH for the Dirichlet functions modulo \(q\), including RH for the zeta function, and no central zeros. For necessity assume also that the positive ordinates in the full family of primitive inducing functions are rationally linearly independent and unshared between functions. Pair each zero with the reflected zero of the conjugate character at the **negative** ordinate. This forced pairing introduces one real phase per positive ordinate. Multiplicities within a function can be counted in its coefficient. Then
\[
 \int_2^X(\pi(t;q,a)-\operatorname{li}(t)/\varphi(q))\,dt<0
 \quad\hbox{for all sufficiently large }X
\]
holds exactly for the square reduced residue classes at the moduli
\[
 1,2,3,4,5,6,8,10,12,15,20,24,30 .
\]
The indicated persistent signs use only GRH. The converse in this all-modulus classification uses the ordinate assumptions.

### Exact spectral threshold

With the \(\varphi(q)\log X/X^{3/2}\) normalization in the [coset argument](zhao-progression-cosets-nov18.md), the constant is \(-2r_a/3\), where \(r_a\) counts the square roots of \(a\) in the group of units. Indeed subtract all prime squares from the prime-power explicit formula; each square-root class contributes \(\sqrt x/\varphi(q)\) before integration. Induced local corrections and higher powers contribute \(o(1)\) after normalization. Character orthogonality gives a Fourier series with coefficients \(-\overline{\chi}(a)/[\rho(\rho+1)]\), summed over the zeros of the primitive character inducing \(\chi\), including the principal zeta zeros. The once-integrated pole term is removed by the logarithmic integral; the standard partial summation and absolute convergence are as in the [quadratic calculation](zhao-bias-kernel-nov18.md). The limiting supremum therefore equals
\[
 -2r_a/3+S_q,\qquad
 S_q=\sum_{\chi\bmod q}\sum_{\rho_{\chi^*}}\frac1{|\rho(\rho+1)|},
\]
by Kronecker approximation. If \(a\) is nonsquare, \(r_a=0\), so its bias changes signs. If \(a\) is square, \(r_a=r(q)\) is the size of the kernel of squaring on the units. Without independence the triangle inequality still gives \(\limsup\le -2r_a/3+S_q\), enough for strict negativity when the right side is negative.

### Uniform finite reduction

Write \(f_\chi\) for the conductor of the inducing primitive character and \(M_\chi(c)=\sum_\rho(c^2+\gamma^2)^{-1}\). As in the [quadratic norm criterion](zhao-bias-classification-nov18.md), \(S_q\) is the sum of the monotone integral averages of \(M_\chi(\sqrt{1/4+2\sin^2\theta})\), and is at least \(\sum M_\chi(3/2)\). For the complex characters take the real part of the completed log derivative, pairing conjugate characters. Their real linear Hadamard terms cancel under the functional equation, or equivalently apply the real paired product. For the principal zeta factor the pole removal contributes \(1/s+1/(s-1)=3/2\) to the completed log derivative at \(s=2\). As \(\Re(L'/L)(2,\chi)\ge -0.57\), the conductor-discriminant formula for the cyclotomic field gives
\[
 3S_q\ge \varphi(q)\left[\log(q/\pi)-\sum_{p\mid q}\frac{\log p}{p-1}
                           -\gamma_E-1.14\right]+3 .
\]
Here \(\prod_{\chi\bmod q} f_\chi=|\operatorname{disc}(\mathbb Q(\zeta_q))|
=q^{\varphi(q)}\prod_{p\mid q}p^{-\varphi(q)/(p-1)}\), also valid for \(q\equiv2\pmod4\). For \(q\ge2000\) the average log conductor exceeds \(\log 130\): bound the sum by \((\log q+3\log2+\log3)/4\), separating primes 2 and 3. Since \(r(q)\le\varphi(q)\), the displayed bound exceeds \(2r(q)\). Apply the same displayed test to all smaller integer moduli. Only 52 require norm evaluation, all at most 120.

For these 52, group the inducing primitive characters by conductor. Compute the derivative and value of their Dirichlet series from deflated Hurwitz zeta jets at positive real arguments, with the pole canceled by summing over the period. The zeta term uses its own pole-removed expression, with \(M_\zeta(1/2)=2+\gamma_E-\log(4\pi)\). Equally spaced lower and upper rectangle sums of the monotone resolvent rigorously separate every modulus from its threshold. The [Arb code](../../experiments/X-nov18-quadratic-bias/classify_progressions.py) and [directed intervals](../../experiments/X-nov18-quadratic-bias/progression-norms.tsv) give the displayed classification.

### Unconditional counterexamples at the class one

For each \(q\in\{11,21,22,28,36,40,42,48,60,84,120\}\), the class \(a=1\) has positive excursions arbitrarily late without any independence or zero assumption. These entries occur in [Zhao's Table 1](https://link.springer.com/article/10.1007/s40993-025-00640-y/tables/1). On GRH, at logarithmic phase zero the coefficient sum before its minus sign equals \(\sum_\chi[M_\chi(1/2)-3M_\chi(3/2)]/2\) by the completed product and functional equation for the aggregate. It is strictly below \(-2r(q)/3\) for each of the displayed moduli, e.g. below \(-2.9848\) at \(q=11\) versus \(-4/3\). The [interval check](../../experiments/X-nov18-quadratic-bias/classify_progressions.py) and almost-periodicity prove the positive excursions in this case.

If an inducing function has an off-line zero, by the functional equations some function has one at \(\Re\rho>1/2\). Since \(a=1\), all multiplicities in the logarithm of the collective Euler product add. Its Mellin transform for the integrated count thus has a logarithmic singularity there, with the pole of zeta at one removed by the logarithmic integral. The [signed Landau argument](zhao-bias-unconditional-nov18.md) gives both signs beyond any fixed normalized amplitude: all nontrivial real zeros to the right of \(1/2\) are excluded at these small conductors by [Platt's rigorous verification](https://doi.org/10.1090/mcom/3077), and zeta has no real zero in that interval. This establishes the counterexamples for the actual prime counts.

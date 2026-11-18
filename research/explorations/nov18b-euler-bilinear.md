# Removing the Type I terms from the reflected prime interaction

Use \(A,k,J,w\) and \(g_N\) from the [reflected integer-comb theorem](nov18b-euler-reflection.md). Define the linear functional on arithmetic coefficient sequences
\[
 \mathcal T_N(f)=\frac1{N^2w}\sum_{m,n} A(m/N)A(n/N)
 \sum_r\frac{f(r)}{\sqrt r}J\!\left(\frac{\log(r/(mn))}{w}\right).
\]
The actual cross form is \(-\mathcal T_N(\Lambda)+O(1/N)\). We give two unconditional arithmetic estimates on this same functional. All constants may depend on the fixed templates.

## Arbitrary short divisors

For any fixed \(\eta>0\), any divisor-bounded \(c_d\) with \(d\le Y\le N^{1-\eta}\), and \(j=0,1\),
\[
 \mathcal T_N\big(c*(\log)^j\big)=O_{B,\eta}(N^{-B})\quad\text{for every }B>0.
 \tag{1}
\]
Here \((\log)^0(n)=1\), and divisor-bounded means \(|c_d|\ll_\epsilon d^\epsilon\) for every \(\epsilon>0\), uniformly across the family considered. In particular these terms have been removed before applying an absolute value to the load-bearing interaction.

For each \(m,n\asymp N\), let \(F(x)=x^{-1/2}(\log(x/d))^j J(\log(x/(mn))/w)\). Its support has length \(O(N)\) at \(x\asymp N^2\), with derivatives \(F^{(r)}\ll_r N^{-1-r}(1+\log N)^j\). Poisson summation at spacing \(d\) gives
\[
 \sum_\ell F(d\ell)=d^{-1}\int F(x)dx+
 O_R\big(d^{-1}(1+\log N)^j(d/N)^R\big)
\]
for each integer \(R\ge2\). The main integral is
\[
 w\sqrt{mn}\int e^{ws/2}J(s)\big(\log(mn/d)+ws\big)^j ds .
\]
Its sum in \(m,n\) is negligible to arbitrary order. Indeed \(N^{-1}\sum A(n/N)(n/N)^{1/2}(\log(n/N))^i\) for \(i=0,1\) has zero integral by the specified double Mellin zero and arbitrarily small discretization error by smooth Poisson summation. The powers of \(N\) and logarithms before these moment sums are harmless. The summed error term in (1) costs \(\ll_{R,\epsilon}N^{1+\epsilon}(Y/N)^R\). Taking \(R\) sufficiently large proves (1).

For any \(U,V\ge1\) with \(UV\le N^{1-\eta}\), define \(c=\mu_{>U}*1=\delta_1-\mu_{\le U}*1\). Then the exact Vaughan identity and (1) give
\[
 \mathcal T_N(\Lambda)=\mathcal T_N(c*\Lambda_{>V})+O_{B,\eta}(N^{-B}).       \tag{2}
\]
Indeed the remaining terms are \(\mu_{\le U}*\log\), \(-\mu_{\le U}*\Lambda_{\le V}*1\), and \(\Lambda_{\le V}\); the last has support too short to intersect \(r\asymp N^2\). In (2) the first factor vanishes for \(a\le U\) and its absolute value is at most \(\tau(a)\). Taking \(U=V=N^{(1-\eta)/2}\) removes every configuration with a shorter factor in this particular split.

## Arithmetic fluctuations for two balanced factors

Let \(\alpha\) and \(\beta\) be arbitrary complex sequences on dyadic intervals \([D,2D]\) and \([E,2E]\) with \(DE\asymp N^2\). Put \(L_\alpha^2=\sum|\alpha_a|^2/a\), \(L_\beta^2=\sum|\beta_b|^2/b\). Let
\[
 \Psi_N(y)= y\int_0^1 k(v)e^{-wv}A(ye^{-wv})dv.
\]
This fixed-width smooth envelope, evaluated at \(e^u/N\), is the zero-frequency Poisson term for \(g_N(u)\). Define the continuous comparison
\[
 \mathcal T_N^0(\alpha,\beta)
 =\sum_{a,b}\frac{\alpha_a\beta_b}{\sqrt{ab}}\int_0^\infty
          \Psi_N(ax/N)\Psi_N(b/(Nx))\,\frac{dx}{x}.
\]
Uniformly in the coefficients and for all contributing \(D,E\),
\[
 \big|\mathcal T_N(\alpha*\beta)-\mathcal T_N^0(\alpha,\beta)\big|
 \ll \sqrt{(1+D/N)(1+E/N)}\,L_\alpha L_\beta
       +O_j(N^{-j})L_\alpha L_\beta .                                  \tag{3}
\]
For \(D,E\asymp N\) the bound is \(O(L_\alpha L_\beta)\), in particular \(O_\epsilon(N^\epsilon)\) for divisor-bounded inputs. This removes these balanced sampling fluctuations without any cancellation hypothesis on the factors. The continuous term itself remains.

To prove (3), the original functional factors exactly as the integral, in \(dx/x\), of
\[
 \left(\sum_a\alpha_a a^{-1/2} g_N(\log(ax))\right)
 \left(\sum_b\beta_b b^{-1/2}g_N(\log(b/x))\right).
\]
Poisson summation over the comb labels expresses \(g_N(\log t)\) as
\[
 \sum_{h\in\mathbb Z} e(ht)\,\Psi_{h,N}(t/N),\qquad
 \Psi_{h,N}(y)=y\int k(v)e^{-wv} A(ye^{-wv})
         e\!\left(hNy(e^{-wv}-1)\right)dv ,
\]
where \(e(t)=e^{2\pi it}\). This uses \(n=t e^{-wv}\) in each Poisson integral; the sign convention for \(h\) is immaterial. The functions have fixed compact support in \(y>0\), their fixed-order derivatives are \(O_{r,j}((1+|h|)^{-j})\) by integration by parts in \(v\), and \(\Psi_{0,N}=\Psi_N\). The derivative of the phase in \(v\) has size comparable to \(|h|\omega\) there.

In the integral put \(x=(N/D)t\), so \(t\) remains in a fixed compact subinterval of \((0,\infty)\). At fixed \(h\ne0\) the first factor is a smooth combination of the exponentials \(e(h a (N/D)t)\), whose distinct frequencies are separated by \(|h|N/D\). Its \(L^2(dt)\) norm is
\[
 \ll_j (1+|h|)^{-j}\sqrt{1+D/(|h|N)}\, L_\alpha.
\]
For detail, insert a fixed smooth cutoff equal to one on the interaction range. Extend \(\Psi_{h,N}((a/D)t)\) smoothly as a function of \(a/D\in[1,2]\) and expand this variable in a Fourier series on a larger fixed interval. Its coefficients have sup norms \(\ll_{j,R}(1+|h|)^{-j}(1+|l|)^{-R}\), uniformly on the bounded \(t\) range. For each Fourier mode the factors depending on \(a\) have modulus one, and the usual separated-frequency estimate follows by integrating against a smooth majorant and summing its rapidly decreasing Fourier transform along the frequency differences. The estimate for the second factor follows after replacing \(t\) by \(1/t\), with \(D\) replaced by \(E\) up to fixed constants. Cauchy–Schwarz and the summable bounds on the nonzero modes give the first term in (3) for the product of two nonzero-mode parts.

Products with exactly one nonzero mode are negligible to every power. For a fixed \(a,b\) their phase in the scaled variable is either \(h a(N/D)t\) or \(h b(D/N)/t\), with first derivative \(\gg |h|N\). The smooth amplitudes including the cutoff have bounded derivatives of arbitrary fixed order with sufficient decay in \(h\). Integration by parts, followed by \(\sum |\alpha_a|/\sqrt a\le \sqrt{2D}L_\alpha\) and the corresponding bound for \(\beta\), proves the claimed negligible error. The product of the two zero-mode parts is exactly \(\mathcal T_N^0\). This proves (3).

The zero-frequency term samples the original multiplicative convolution smoothly at product scale \(N^2\). Bound (3) does not estimate its signed value. The other outstanding contributions are the nonzero-mode products when one factor in (2) substantially exceeds \(N\).

## Complete suppression when the prime factor is balanced

For the actual coefficient \(c=\mu_{>U}*1\) in (2), the continuous term in (3) also disappears when \(a\asymp D\) is longer than its divisor cutoff. More precisely, restrict the second factor by an arbitrary mask to \(b\in[E,2E]\) and leave the first factor at full length. Set \(D=N^2/E\), suppose \(D\ge U N^\eta\) for fixed \(\eta>0\) and \(D\gg1\), and write \(\beta\) for the masked second factor. Then
\[
 |\mathcal T_N(c*\beta)|\ll_{\eta,\epsilon}
 N^\epsilon\sqrt{(1+D/N)(1+E/N)}\ L_\beta .                      \tag{4}
\]
In particular every \(E\asymp N\) component satisfies the RH-scale bound \(O_\epsilon(N^\epsilon)\) for arbitrary divisor-bounded masks and \(U\le N^{1-\eta}\). The same estimate holds for all individual \(b\) in a balanced dyad summed with arbitrary bounded coefficients: by duality this bounds the sum of the absolute values of their separate signed first-factor contributions there.

Indeed both the exact comb term and its smooth comparison have \(ab\asymp N^2\) on their support. For (3) one may therefore restrict \(c\) to a fixed larger dyadic band of size \(D\) at cost \(O_\epsilon(N^\epsilon)\) in its weighted norm; subdivide the band into a bounded number of dyads. When estimating the resulting continuous part, restore all \(a\) because its own smooth envelope vanishes outside the same band. There \(c(a)=-\sum_{d\mid a,\,d\le U}\mu(d)\). In the integral for \(\mathcal T_N^0\), \(\Psi_N(b/(Nx))\) forces \(x\asymp E/N\). For each such \(x\),
\[
 \int_0^\infty y^{-1/2}\Psi_N(yx/N)\,dy=0
\]
by \(B(1/2)=0\), changing variables inside its defining integral. For each \(d\le U\), the function under the last integral has support \(y\asymp D\), derivatives of order \(r\) bounded by \(O_r(D^{-1/2-r})\). Thus its sum over multiples of \(d\) is \(O_R(D^{1/2}d^{-1}(d/D)^R)\) by Poisson, since its integral vanishes. Summing over \(d\le U\), the continuous first factor is negligible to every power of \(N\), uniformly in \(x\). This completes (4). The remaining configurations in (2) either have unbalanced sampling frequencies or occur near the end of the truncated divisor range, where this particular zero-moment argument no longer suppresses the continuous term.

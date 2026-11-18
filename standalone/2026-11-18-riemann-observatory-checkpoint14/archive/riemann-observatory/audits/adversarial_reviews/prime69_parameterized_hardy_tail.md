# Parameter tuning for the global Hardy tail bound

18 November 2026. This is a refinement of the global Hardy variation proof, using the already certified complete derivative sum through \(10000\). There was no new zero census. All claims about the true critical-line derivative series are unconditional. The identification with the full tapered prime-array limit retains the RH hypothesis. The change is a practical improvement to a still-wide numerical enclosure. [Global variation proof and its original parameters](prime67_global_hardy_tail.md)

## Parameter constraints and remainder

Let \(Y\) be the finite cutoff, \(w>0\) the transition width, \(T_0=Y-w>0\), \(r>1\) the block ratio, \(d>0\) the Euler truncation proportion, \(M=\lceil dT\rceil\) on a block at \(T\), and \(a=\max(a_1,a_2)\) the largest positive Cauchy radius. The checks require \(a_1,a_2<1/2\), \(\log T_0>5\), \(dT_0\ge34\), \(Y\le rT_0\), \(d^2T_0>1\), and \(1/T_0+\pi/4<1\). Thus the main blocks and the transition have endpoint \(U\le rT\). For the latter block the remainder uses its actual ratio \(U/T\). The code also checks
\[
 \frac{r+a/T_0}{d}<2\pi,\quad r+a/T_0<2\pi,\quad
 \log\frac{2\pi}{1-a/T_0}+\frac{\pi}{T_0-a}+\frac{1}{2(T_0-a)^2}<1.86 .
\]
These remain valid at all later \(T\). The first ensures nonstationarity for the positive Fourier modes, the second bounds the sign of \(\log(v/(2\pi T))\) for \(T-a\le v\le U+a\), and the last is the multiplier estimate with the actual maximal disk radius.

For \(s=\sigma+iv\) in these disk strips put \(\lambda=U/T\) and
\[
 C_+=\frac{\lambda+a/T}{d},\qquad
 C_-=\frac{1-a/T}{d+1/T},\qquad
 C_A=C_++\frac{(1/2+a)^2}{2dT(T-a)} .
\]
One has \(C_-\le v/M\le C_+\) and \(|s|/M\le C_A\), the latter by \(\sqrt{v^2+\sigma^2}\le v+\sigma^2/(2v)\). The same monotone-amplitude integration by parts as in the earlier proof now keeps both signs and the first eight frequencies:
\[
 \begin{split}
 |\zeta(s)-P(s)| &\le C(T,\lambda)M^{-\sigma},\\
 C(T,\lambda)&=\frac{d+1/T}{1-a/T}+\frac12+\frac{C_A}{\pi}
 \left[\sum_{n=1}^{8}\left(\frac1{n(2\pi n-C_+)}
                        +\frac1{n(2\pi n+C_-)}\right)\right.\\
 &\hspace{40mm}\left.
 +\left(\frac{\pi^2}6-\sum_{n=1}^8n^{-2}\right)
     \left(\frac1{2\pi-C_+/9}+\frac1{2\pi}\right)\right].
 \end{split}
\]
For \(n\ge9\), \(2\pi n-C_+\ge n(2\pi-C_+/9)\), and \(2\pi n+C_-\ge2\pi n\). The pole term uses \(M/v\le(d+1/T)/(1-a/T)\). The circle maximum, Cauchy derivative bound, and product rule with \(q=Q_2(1/2+it)\) now proceed as in the original proof, except with \(C(T,\lambda)\) and \(a_0=0,a_1,a_2\) in place of the original constants. The Hardy gamma-factor comparison uses imaginary modulus \(v/2\) and real parts in \((0,1/2)\), so the real-part error from the digamma comparison is at most \(\pi/v+1/(2v^2)\).

For \(\lambda=r\), the remainder coefficient \(C(T,r)\) decreases with \(T\), since \(C_+\) and \(C_A\) decrease and \(C_-\) increases. The normalized coefficients for the infinite blocks used in the previous proof therefore still decrease. For the centered polynomial moment envelope, the code checks \(\sqrt r\le 2\pi\) and \( (2(d+1/T_0))^2\,2\pi/\sqrt r<e^2\). These imply \(b\le\log T/2\) and \(\log(2M)-b\le(\log T+2)/2\) at every geometric block, with \(b=\tfrac12\log(\sqrt r T/(2\pi))\). The exact parity adjustment, trapezoid majorants, and summable infinite geometric remainder are as in the original proof.

## Cubic cutoff identities

Let \(H=G/t\), \(f=\varphi H\), with \(\varphi\) the cubic lower transition from the earlier proof. The first-derivative identity is
\[
 \|f'\|_2^2=\int\varphi^2|H'|^2-\int\varphi\varphi''|H|^2 .
\]
This follows by integrating \(\varphi\varphi'(|H|^2)'\), whose boundary coefficient vanishes at both ends of the transition. For the second derivative, all terms involving derivatives of \(\varphi\) are integrated on \([T_0,Y]\), taking the cubic's one-sided derivatives at \(Y\). Expansion and integration of the \(H''\overline{H'}\) and \(H''\overline H\) cross terms leaves a coefficient \(2\varphi'^2-4\varphi\varphi''\) multiplying \(|H'|^2\), plus the terms
\[
 \int_{T_0}^Y \varphi''^2|H|^2
 +\int_{T_0}^Y(\varphi'\varphi''-\varphi\varphi''')(|H|^2)'
 -\frac{12}{w^2}\Re(H'(Y)\overline{H(Y)}).
\]
On the transition \((\varphi'\varphi''-\varphi\varphi''')'=\varphi''^2\), and its endpoint values are \(0,12/w^3\). Thus
\[
 \|f''\|_2^2=\int\varphi^2|H''|^2+
 \int_{T_0}^Y(2\varphi'^2-4\varphi\varphi'')|H'|^2
 +\frac{12}{w^3}|H(Y)|^2-\frac{12}{w^2}\Re(H'(Y)\overline{H(Y)}).
\]
With \(x=(t-T_0)/w\) the coefficient in the transition is \(24x^3(2-x)/w^2\le24/w^2\). The first-derivative correction has \(-\varphi\varphi''\le6/w^2\). Let \(A_j\) be the global and \(B_j\) the transition norm majorant for \(G^{(j)}/t\). Consequently the squared bounds are
\[
 \begin{split}
 \|f'\|_2^2 &\le (A_1+A_0/T_0)^2+6B_0^2/w^2,\\
 \|f''\|_2^2 &\le (A_2+2A_1/T_0+2A_0/T_0^2)^2
   +24(B_1+B_0/T_0)^2/w^2
   +12|H(Y)|^2/w^3-12\Re(H'(Y)\overline{H(Y)})/w^2.
 \end{split}
\]
The last two terms are evaluated with their signs by Arb at the exact endpoint. For \(L(t)=q(t)\zeta(1/2+it)/t\), one has \(H=e^{i\theta}L\), so \(|H|=|L|\) and \(\Re(H'\overline H)=\Re(L'\overline L)\). The linear Taylor coefficient of \(\zeta(1/2+iY+iz)\) supplies its derivative along the critical line in \(L'\). There is no gamma-phase computation at the endpoint and no assumption about \(\zeta(1/2+iY)\) being nonzero.

## Numerical search and exact replay

The Python search uses SciPy Powell from two starting points. Each trial is rounded to rational thousandths for \(r,d,a_1,a_2\) and a whole number for \(w\). A 96-bit intermediate estimate drives the search using enough blocks to span a ratio of at least \(3\cdot10^6\). The search does not certify parameter optimality. It records all distinct trials and why inadmissible ones were dropped, including a potential stationary positive Fourier mode, an overly wide transition compared to the candidate ratio, and a radius reaching the strip boundary. The reported inequality uses a separate 128-bit replay with 64 blocks and the rational parameters recorded there. [Search code](../../scripts/prime69_hardy_tail_search.py) · [Search log](../../experiments/results/prime69_hardy_tail_search_10000.json) · [Verification code](../../scripts/prime69_parameterized_hardy_tail_checks.py)

The search evaluated 313 distinct proposals, including five rejected ones. One Powell run reached its evaluation budget, and the other terminated successfully. The selected exact parameters were \(r=1607/1000\), \(d=143/500\), \(w=22\), \(a_1=219/1000\), and \(a_2=433/1000\). The 64-block replay gives
\[
 \mathcal T(10000)<0.45906151,\qquad
 0.61649875288731141829<C_2<1.075561.
\]
The unrounded upper expression is \(0.4590615084631102969276294270\ldots\). The rounded analytic tail is about 5.3 percent smaller than the previous \(0.48494\) bound. The lower bound still comes from the complete certified finite sum through \(10000\). [Height-10000 replay](../../experiments/results/prime69_parameterized_hardy_tail_10000.json) · [Complete finite sum](prime64_q2_partial_tail_observation.md)

With the same parameters and 64 blocks at \(Y=2.8\cdot10^6\), the certificate gives \(\mathcal T(Y)<0.00591413\). A complete finite sum through that height of width below \(0.00025\) would therefore suffice for an enclosure narrower than one percent of the existing certified lower bound. That finite sum was not computed. [Height-2800000 replay](../../experiments/results/prime69_parameterized_hardy_tail_2800000.json)

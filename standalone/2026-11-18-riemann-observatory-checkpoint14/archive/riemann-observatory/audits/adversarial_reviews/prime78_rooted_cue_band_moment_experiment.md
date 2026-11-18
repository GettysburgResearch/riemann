# Deterministic finite-\(N\) experiment for a rooted CUE Fourier band

18 November 2026. This experiment evaluates the actual finite-\(N\) mean, variance, and third cumulant of the cosine band in the globally derivative-square tilted, rooted CUE of order \(N\). It uses exact finite-dimensional trace identities and floating evaluation of the two-mode correction. A second implementation computes a small case with dense matrices over the rationals. It does not sample eigenvalues or compute zeta zeros. The finite numbers corroborate the previously established limiting mean, variance, and cubic cumulant. They are not used as evidence for the weak limit proof or for an arithmetic distributional transfer. [Rooted CUE limit](prime77_rooted_cue_band_limit.md) · [Second-moment comparison](prime71_hlz_band_covariance.md) · [Independent CUE cubic derivation](weighted73_rooted_cue_band_match.md)

## Data

The band is \(a=1/20,\ b=1/10\), lower endpoint excluded. The three exact limiting expressions are
\[
 \log 2-\frac{2393}{12000},\qquad
 \frac{\log 2}{2}-\frac{1414849}{144000000},\qquad
 -\frac{818904257}{864000000000}.
\]
Selected finite values and the independently derived limits are shown rounded.

| \(N\) | Mean | Variance | Third cumulant |
| ---: | ---: | ---: | ---: |
| 20 | 0.310173160173 | 0.241145733776 | −0.000799470887 |
| 40 | 0.388879210221 | 0.282352036938 | −0.000868482663 |
| 160 | 0.464729453316 | 0.321743419291 | −0.000926896871 |
| 640 | 0.486299791162 | 0.332906060914 | −0.000942507019 |
| 2000 | 0.491339563439 | 0.335512134874 | −0.000946104954 |
| Limit | 0.493730513893 | 0.336748250002 | −0.000947805853 |

Each of the eight recorded finite sizes uses a multiple of 20, so endpoint floors do not vary relative to the prescribed rational band. At \(N=2000\) the signed errors are approximately \(-2.39\cdot10^{-3},-1.24\cdot10^{-3},1.70\cdot10^{-6}\). These are observations for the tested sizes and do not assert a convergence rate. The independent dense rational calculation at \(N=20\) gives
\[
 \frac{1433}{4620},\quad \frac{5147111}{21344400},\quad
 -\frac{39418363}{49305564000}.
\]
All three double-precision outputs are within \(3\cdot10^{-16}\) of the rounded exact values. The recorded source and complete JSON provide the replay. [Numerical output and exact check](../../experiments/results/prime78_rooted_cue_band_moments.json)

## Finite trace formulas

Let \(E\) be projection onto Fourier degrees \(0,\ldots,N\) and work in this \((N+1)\)-dimensional space. The two columns of \(U\) are the normalized vectors \(1\) and \(j-N/2\), and \(P=I-UU^*\) is the free-eigenvalue projection for the globally rooted tilt. Put
\[
 f(\theta)=-\sum_{aN<k\le bN}\cos(k\theta)/k,\qquad F_j=E M_{f^j}E .
\]
Here \(F_2,F_3\) are compressions of \(f^2,f^3\), distinct from powers of the compressed \(F_1\). From the finite-rank determinantal generating function on \(\operatorname{Ran}P\), expand \(\log\det(I+P(E M_{e^{tf}}E-I)P)\) through degree three. For the free sum the cumulants are
\[
 {\rm Tr}(PF_1),\quad {\rm Tr}(PF_2)-{\rm Tr}(PF_1PF_1),\quad
 {\rm Tr}(PF_3)-3{\rm Tr}(PF_1PF_2)+2{\rm Tr}(PF_1PF_1PF_1).
\]
The deterministic root adds \(f(0)=-\sum_{aN<k\le bN}1/k\) only to the mean.

At \(P=I\) the first trace is zero and the second cumulant is \(\frac12\sum 1/k\). Indeed each signed Fourier coefficient \(-1/(2k)\) at \(\pm k\) contributes \(k/(4k^2)\) from the boundary of the degree interval. The third base cumulant vanishes. To verify this algebraically, set \(n=N+1\) and let \(c_r\) denote Fourier coefficients of \(f\). Restrict to triples \(r+s+t=0\). In \({\rm Tr}F_3,{\rm Tr}F_1F_2,{\rm Tr}F_1^3\), their respective trace counts are \(n,n-|r|,n-\operatorname{span}(0,r,r+s)\), since the shifted indices must stay in the Fourier interval wherever a compression is inserted. The last span is \(\max(|r|,|s|,|t|)\), which equals \((|r|+|s|+|t|)/2\). These counts need no positive-part correction because \(3\lfloor bN\rfloor<n\) here. Summing over ordered triples symmetrizes the middle count in \(r,s,t\); the linear combination with coefficients \(1,-3,2\) then vanishes. For this particular band there are in fact no signed frequency triples summing to zero, since two positive band frequencies already sum to more than the upper endpoint.

Write \(M_j=U^*F_j U\), \(R=U^*F_1^2U\). Substitution of \(P=I-UU^*\) and cyclicity of trace give corrections to the base cumulants
\[
 \begin{split}
 &-\operatorname{Tr} M_1,\\
 &-\operatorname{Tr} M_2+2\operatorname{Tr} R-\operatorname{Tr}(M_1^2),\\
 &-\operatorname{Tr} M_3
  +3\operatorname{Tr}\big(U^*(F_1F_2+F_2F_1)U\big)
  -3\operatorname{Tr}(M_1M_2)
  -6\operatorname{Tr}(U^*F_1^3 U)
  +6\operatorname{Tr}(M_1R)-2\operatorname{Tr}(M_1^3).
 \end{split}
\]
In the last line the contributions with one, two, and three removed projections in the cubic trace have coefficients \(-6,+6,-2\). The correction matrices are all \(2\times2\).

The program forms the scalar Fourier coefficient vector of \(f\), with entries \(-1/(2k)\) at \(\pm k\), and uses its second and third ordinary convolutions for \(f^2,f^3\). Each compressed \(F_j\) acts by Toeplitz convolution followed by slicing back to degrees \(0,\ldots,N\). The low-rank calculations need only its action on the two columns of \(U\) and one extra application of \(F_1\) to \(F_1U\). They require no dense \(N\times N\) matrix. The direct convolutions cost \(O(N K)\) arithmetic operations for upper frequency \(K=\lfloor bN\rfloor\), including the \(O(K^2)\) coefficient convolutions since \(K\le N\). The exact small-size replay instead constructs \(P\) from its rational entries, forms dense Toeplitz matrices, and evaluates the original projections in the cumulant traces. In that calculation the two basis vectors can be left unnormalized, dividing each outer product by its integer squared norm. Thus it checks the low-rank expansion separately from floating-point orthonormalization.

Replay from the repository root with Python and NumPy.

```sh
python scripts/prime78_rooted_cue_band_moments.py
python scripts/prime78_rooted_cue_band_moments.py --sizes 20 40 --exact-size 40
```

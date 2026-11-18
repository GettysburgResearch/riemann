# Reducing the higher-degree field test to published complete tables

Assume GRH for each tested Dedekind zeta function. In degrees 5 through 8 the following strict discriminant upper bounds hold whenever \(B_K\le2\). Columns are indexed by the number \(r_2\) of complex places. An empty signature is impossible. [Interval certificate](../../scripts/check_zhao_field_cuts_nov18.py)

| Degree | 0 | 1 | 2 | 3 | 4 |
|---:|---:|---:|---:|---:|---:|
|5|1,012,301|736,477|535,318|||
|6|2,147,891|1,810,909|1,526,797|1,230,968||
|7|4,076,234|3,525,724|2,980,866|2,534,799||
|8|excluded|excluded|excluded|4,921,482|4,145,046|

The sharper signature exclusions in the [degree proof](zhao-number-fields-nov18.md) also apply. All unexcluded upper endpoints lie inside the published complete ranges of the LMFDB catalogue, including the septic and octic cases. This gives a finite source of candidate fields in every degree. [LMFDB, completeness of number field data](https://www.lmfdb.org/NumberField/Completeness)

To prove the caps, let \(D(s)\) denote the logarithmic derivative of the entire completed field zeta function, and let \(\mathcal TD(7/2)\) be the three-derivative linear form in the [degree proof](zhao-number-fields-nov18.md). For \(s>1,t\ge0\),
\[
 D(s)+t\mathcal TD(7/2)\le(s-1/2+t)B_K.
\]
This follows separately for each ordinate from the two rational kernel bounds. The unmodified derivative contributes \((\log|\Delta|)/2\), the two poles, the real gamma factors, and \(\zeta'_K/\zeta_K\). The part of \(\mathcal TD\) from the gamma factors and poles is bounded below by
\[
 G=(n-r_2)\sum_{j\ge0}f(7/2+2j)+r_2\sum_{j\ge0} f(9/2+2j)-f(7/2)-f(5/2)
\]
with \(f(z)=z^{-2}+3z^{-3}+16z^{-4}\) (in fact there is equality for this part). At \(m=p^k\), writing \(v=\log m\), the absolute coefficient of the prime logarithmic derivative, before division by \(p^{ks}\), is at most \(n\log p\) by the local residue degrees. In the *combined* lower bound it therefore costs at most
\[
 n\log p\;\max\{0,e^{-sv}-t(v+3v^2/2+8v^3/3)e^{-7v/2}\}.
\]
Denote the sum of these upper allowances by \(C\). Keeping the positive part after combining is important because one is estimating the contribution of the *same* ideal at the two evaluation points. Substitution and rearrangement give
\[
 \log |\Delta|\le 4(s-1/2)-2/s-2/(s-1)+ n\log\pi
 -(n-r_2)\psi(s/2)-r_2\psi((s+1)/2)+2t(2-G)+2C.
\]
The certificate uses specified rational \(s,t\) per signature, the first 64 terms and a lower integral tail for each sum in \(G\), and exact prime powers through 5,000 in \(C\). Above that cutoff it bounds the positive part by the sum of \(n(\log m)m^{-s}\) over all integers, with the decreasing integral bound. Every printed cap is an outward integer ceiling. For the three octic exclusions \(G>2\) suffices by itself.

## A separate interval evaluation at the threshold

The [Dedekind contour checker](../../scripts/check_zhao_dedekind_contour_nov18.py) evaluates \(B_K\) from the field polynomial even when compact prime sums straddle the threshold. It uses only the continuation and functional equation of the Dedekind zeta function, and the assumption that its zero ordinates are real. No Artin holomorphy is needed. Write \(c=\sqrt{|\Delta|}/\pi^{n/2}\). Up to a positive constant the entire symmetric function used is
\[
 H(w)=w(w-1)c^w\Gamma(w/2)^{n-r_2}\Gamma((w+1)/2)^{r_2}
       \zeta_K(w)\exp((w-1/2)^2/36).
\]
The functional equation gives \(H(w)=H(1-w)\) and its value at 1 is positive by the residue theorem for Dedekind zeta functions. Under GRH \(B_K=2(H'(1)/H(1)-1/36)\). Shifting the two sides of Cauchy's integral to \(\Re w=8,-7\) and reflecting the left line gives the value and derivative at 1 by integrating the common factor \(H(w)/(w(w-1))\) on the right line times respectively \(2w-1\) and \((2w-1)/(w(w-1))\), with measure \(dw/(2\pi i)\). The intermediate horizontal contours vanish since completed Dedekind zeta has at most polynomial growth after its archimedean exponential decay on each fixed vertical strip, and the inserted Gaussian dominates.

For explicit quadrature error let
\[
 C(\sigma)=c^\sigma\Gamma(\sigma/2)^{n-r_2}\Gamma((\sigma+1)/2)^{r_2}
   \exp((\sigma-1/2)^2/36)\zeta(\sigma)^n.
\]
On vertical lines \(\sigma=2,8,14\), both integrands before normalization have modulus at most \(C(\sigma)(2\sigma+2|t|)e^{-t^2/36}\). This uses the Euler integral for the gamma factor and \(|\zeta_K(\sigma+it)|\le\zeta(\sigma)^n\). The infinite trapezoidal rule of mesh \(h=1/4\) costs at most
\[
 \frac{\sum_{\sigma=2,14}(12\sigma\sqrt\pi+72)C(\sigma)}
      {2\pi(\exp(12\pi/h)-1)} .
\]
Indeed Fourier transforms on the two strip boundaries bound the nonzero sampling aliases by the geometric series, or one can integrate the cotangent kernel. Beyond \(T=320h\) use the decreasing positive tail and integrate the Gaussian to bound both omitted sides by \(72C(8)(1+8/T)e^{-T^2/36}/(2\pi)\).

At each sampled ordinate the logarithmic Euler series is truncated at rational prime powers \(p^k\le P\), using \(\sum_{f\mid k}f\,\#\{\mathfrak p\mid p:f_{\mathfrak p}=f\}/k\) as coefficient. Its omitted magnitude is at most \(n/(7P^7)\) by summation over all integers past \(P\). After exponentiation, the aggregate absolute quadrature error is at most the discrete Gaussian majorant times \(\exp(n/(7P^7))-1\). For the discrete majorant use its full integral plus \(4h(16+12)\) before multiplication by \(C(8)/(2\pi)\): on each positive or negative half-line the majorant is unimodal and its supremum is at most \(16+12\). The checker adapts \(P\) and verifies the *actual* error against the requested tolerance before it accepts any evaluation.

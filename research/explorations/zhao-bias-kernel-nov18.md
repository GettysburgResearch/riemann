# A prime-tail witness for the integrated quadratic prime bias

Let χ be a primitive nonprincipal quadratic character of conductor Q and parity a in {0,1}. Assume GRH for its L-function. Count all its nontrivial zeros ρ=1/2+iγ with multiplicity, including both ordinates of each conjugate pair. Define
$$
 K_χ(t)=\sum_ρ {e^{iγt}\over ρ(ρ+1)},\qquad
 k(v)=(e^{-v/2}-e^{-3v/2})\mathbf1_{v>0}.
$$
For every real X≥1 we have the exact identity
$$
 K_χ(-\log X)=-\sqrt X\sum_{n>X}{Λ(n)χ(n)\over n}(1-X/n)
 -\int_{\log X}^{\infty}{e^{-(1/2+a)y} k(y-\log X)\over1-e^{-2y}}\,dy. \tag{1}
$$
The series is taken in increasing n. Partial summation with the GRH estimate for ψ(u,χ) proves convergence. The archimedean term is nonpositive and has absolute value O(X^{-1/2-a}) uniformly for X≥1, by translating y and bounding the denominator from below by its value at y−log X. At X=1 the apparent singularity is removable. Equality at an integer endpoint is immaterial because k(0)=0. A central zero of multiplicity m contributes exactly 4m/3 on the left.

To justify (1), use the explicit formula for a primitive Dirichlet L-function in the convention h(t)=∫g(v)exp(−itv)dv. Take g(v)=k(v−log X). Its transform is X^{-it}/[(1/2+it)(3/2+it)]. The conductor term is g(0)log(Q/π)=0. The prime term is −ΣΛ(n)χ(n)[g(log n)+g(−log n)]/√n, giving (1). The gamma term is (2π)^{-1}∫h(t) Re ψ₀((1/2+a+it)/2)dt, where ψ₀ is the digamma function. Its integral representation gives
$$
 -\int_0^\infty {e^{-(1/2+a)y}\over1-e^{-2y}}[g(y)+g(-y)]\,dy,
$$
since g(0)=0. There is no pole term for a nonprincipal character. Formally one may first multiply g(v) by exp(−εv) on its support, making the prime sum absolutely convergent and moving the Fourier transform poles outside the closed critical strip in the ordinate variable. The explicit formula applies to this piecewise smooth kernel by convolution with smooth compactly supported approximate identities, or directly by contour integration. As ε decreases to zero the zero sum converges by domination by C_X/(1+γ²), the gamma term by absolute convergence, and the prime term by Abel convergence from its ordinary convergence.

For the connection to Zhao's §8(2), put π(x,χ)=Σ_{p≤x}χ(p). For fixed χ the normalized mean satisfies
$$
 {\log Y\over Y^{3/2}}\int_2^Y π(x,χ)\,dx
 =-2/3-K_χ(\log Y)+o(1). \tag{2}
$$
Indeed integration of the explicit formula for ψ(x,χ) gives −ΣY^{ρ+1}/[ρ(ρ+1)] plus O_χ(Y log²Y), by the usual once-integrated Perron formula; zeros at zero in the integrand contribute only to this error. Prime squares contribute θ(√x)−Σ_{p|Q, p≤√x}log p∼√x, and higher powers give O(x^{1/3}log²x), so integration for θ(x,χ) gives the extra −2/3. Finally the primitive of θ(x,χ) is O_χ(x^{3/2}) by absolute convergence of the integrated formula. Two partial summations now replace log p by log Y in the integrated sum with error O_χ(Y^{3/2}/log²Y) before the normalization in (2). Explicitly, if B(Y)=∫₂^Y θ(x,χ)dx, then ∫₂^Y π(x,χ)dx=∫₂^Y θ(x,χ)[1/log x+(Y−x)/(x log²x)]dx. Integrating by parts against B produces B(Y)/log Y. The derivative of the bracket is O(Y/(x² log²x)), giving the claimed error.

Absolute convergence makes K uniformly almost periodic, so each value K(−log X) is approached along ordinates t→+∞. In particular any X≥1 with K(−log X)<−2/3 gives positive normalized means along an unbounded sequence. Repeating at all negative times yields the exact strict witness criterion for a positive limiting supremum. The boundary inf K=−2/3 leaves the sign of lower-order terms open.

At X=1 the digamma difference evaluates to log 2 for even characters and 1−log 2 for odd ones. Thus K(0)=(L′/L)(1,χ)−(L′/L)(2,χ)−A, with A the indicated positive constant. This evaluation uses only four convergent periodic Dirichlet series. Truncate at a whole conductor multiple N and put B=maxₖ|Σ_{j≤k}χ(j)| over one period. Each tail for L(s) or L′(s) costs at most B N^{-s} or B(log N)N^{-s}, respectively, by monotonicity beyond N. The [standalone certificate](../../scripts/check_zhao_bias_witness_nov18.py) proves the following upper bounds, rounded upward.

| d | K(0) upper bound |
|---:|---:|
| 2221 | −1.306 |
| 2237 | −1.014 |
| 2269 | −1.388 |
| −2207 | −1.163 |
| −2239 | −1.287 |
| −2287 | −1.252 |

Each therefore fails eventual negativity under GRH. These six witnesses use only ordinary convergent series for individual characters. They establish no assertion about the proportion of discriminants.

The [classification and exhaustive small-conductor norm bounds](zhao-bias-classification-nov18.md) use this formula together with rigorous arithmetic sign witnesses. The [unconditional dichotomy](zhao-bias-unconditional-nov18.md) removes GRH in the individual exclusions with verified nonvanishing on the positive real segment.

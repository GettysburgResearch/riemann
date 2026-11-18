# One-sided critical negative-log packet estimate

Let \(q>0\), \(0<A<q\), \(T\ge T_0\), and \(w=T^{-1}(\log T)^A\). Fix smooth cutoffs \(\eta\) and \(\chi\) such that \(\eta(x)=0\) for \(x\le1\), \(\eta(x)=1\) for \(x\ge2\), and \(\chi(x)=1\) for \(0\le x\le1/2\) with \(\chi(x)=0\) for \(x\ge C\), where \(C>1/2\) is fixed. Only their values on the support of \(\eta(Tv)\) matter. Set \(b_T(v)=\chi(v/w)\eta(Tv)\sin(Tv)\) and extend by zero below \(v=0\). With the convention \(\widehat g(t)=\int g(v)e^{itv}dv\), uniformly for \(\beta\) in a fixed compact real interval,
\[
\int_{\mathbb R}\frac{\sqrt{1+t^2}}{\log^q(e+|t|)}
         \left|\widehat{e^{\beta v}b_T(v)}(t)\right|^2dt
\ll (\log T)^{A-q}+(\log T)^{-q}.
\]
In particular the squared tilted norm is \(O((\log T)^{A-q})\).

## Frequency proof

Write \(a_T(v)=e^{\beta v}\chi(v/w)\eta(Tv)\). Its support is contained in \([1/T,Cw]\), and the tilt and its first two derivatives are uniformly bounded there. Thus \(\|a_T\|_2^2\ll w\). Differentiating the cutoffs supplies
\[
\|a_T''\|_1\ll w+1+w^{-1}+T\ll T.
\]
For the upper cutoff, the first and second derivative \(L^1\) sizes are \(O(1)\) and \(O(w^{-1})\), respectively. For the lower cutoff they are \(O(1)\) and \(O(T)\), since the derivative support lies in \([1/T,2/T]\). The mixed derivative vanishes for large \(T\), since \(\chi'\) then vanishes on \([1/(Tw),2/(Tw)]\). Even without this eventual separation it is \(O(w^{-1})\) in \(L^1\). The estimate is uniform in the tilt. Two integrations by parts now give \(|\widehat a_T(\xi)|\ll T/|\xi|^2\) for \(\xi\ne0\), and modulation gives
\[
\widehat{e^{\beta v}b_T}(t)
    =(\widehat a_T(t+T)-\widehat a_T(t-T))/(2i).
\]

On \(T/2\le |t|\le2T\), the multiplier weight is \(O(T/(\log T)^q)\). Plancherel bounds the weighted integral there by \(O(Tw/(\log T)^q)=O((\log T)^{A-q})\). On the complement both shifted arguments have size \(\gg T+|t|\). The pointwise bound there is \(O(T/(T+|t|)^2)\). Below \(T/2\), its squared weighted integral is
\[
\ll T^{-2}\left(\int_0^{\sqrt T}(1+t)\,dt+(\log T)^{-q}\int_{\sqrt T}^{T/2}(1+t)\,dt\right)
\ll T^{-1}+(\log T)^{-q}.
\]
Above \(2T\), it is
\[
\ll T^2(\log T)^{-q}\int_{2T}^\infty t^{-3}\,dt\ll(\log T)^{-q}.
\]
The low-frequency and large-frequency bounds explicitly include leakage from the derivative of the \(T^{-1}\)-scale lower cutoff.

## Sharp inverse at packet origin

For cutoff \(U>0\), the symmetric inverse integral at zero equals
\[
J_\beta(U)=\frac1{2\pi}\int_{-U}^U\widehat{e^{\beta v}b_T}(t)dt
=\frac1{\pi}\int_{1/T}^{Cw}e^{\beta v}b_T(v)\frac{\sin(Uv)}v\,dv.
\]
Fubini is valid for every finite \(U\) by compact support. At \(U=T\), the effect of replacing the tilt by 1 is \(O(w)\), since \(|e^{\beta v}-1|\ll v\). The lower transition interval \([1/T,2/T]\) contributes \(O(1)\), and the upper transition \([w/2,Cw]\) contributes \(O(1)\), each by integrating \(dv/v\) over a fixed-ratio interval. Therefore
\[
J_\beta(T)=\frac1\pi\int_2^{Tw/2}\frac{\sin^2 y}{y}\,dy+O(1)
=\frac{1}{2\pi}\log(Tw)+O(1).
\]
For the last equality, \(\sin^2y=(1-\cos(2y))/2\) and the cosine integral over \([2,X]\) is bounded uniformly in \(X\) by integration by parts. The main term is \(A\log\log T/(2\pi)\). For \(|U-T|\le B\) with \(B\) fixed, the mean-value estimate for sine gives \(|J_\beta(U)-J_\beta(T)|\ll |U-T|w\). The same bound in fact holds for all \(U>0\), though it is informative only for offsets small relative to \(1/w\).

This establishes the packet estimates. For a packet translated to \(v_0\), evaluating the inverse at \(v_0\) removes the Fourier translation phase and inserts the scalar \(e^{\beta v_0}\) in the tilted estimate. A global prime-side or raw zero-sum construction requires separate control of all other sampling locations and packets.

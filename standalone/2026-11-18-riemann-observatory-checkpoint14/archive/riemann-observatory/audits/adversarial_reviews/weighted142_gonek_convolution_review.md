# Independent check of an explicit \((1,1)\) divisor-convolution bound

Gonek's Lemma 7 on printed pp. 133–134, at \(\mu=\nu=1\), has \(A_n(1,1)=\sum_{dr=n}\log d\,\log r\) and leading sum \(z(\log z)^3/6\). I checked these in the rendered original journal pages. The proposed all-\(z\) coefficient \(5/2\) is valid. Centering the integer-counting discrepancy gives the modest strengthening \(9/4\). [Pinned Gonek PDF](../../sources/classical63_lfunctions/gonek1984.pdf) · [Earlier source reconstruction](geometry88_gonek_whole_advocate.md)

Let \(z>1\) and \(L=\log z\). Define \(S(q)=\sum_{r\le q}\log r\) for \(q\ge1\), with endpoint included, and put \(q_0=\lfloor q\rfloor\). The upper bound \(S(q)\le q\log q\) follows term by term. Monotonicity gives \(S(q)\ge\int_1^{q_0}\log t\,dt\). Hence
\[
 0\le q\log q-S(q)
 \le q-1+\int_{q_0}^q\log t\,dt
 \le q-1+\log q\le2q .
\]
This also holds at \(q=1\) and integer \(q\).

For \(d\ge3\), \(t\in[d-1,d]\) gives \(2\log t\ge\log d\) since \((d-1)^2\ge d\), and \(1/t\ge1/d\). Thus \(\log d/d\le2\int_{d-1}^d(\log t)/t\,dt\). At \(d=2\), the same integrated inequality follows from \(\log2\ge1/2\). The \(d=1\) term vanishes. Summing the inequalities, with an empty sum if \(1<z<2\), gives
\[
 \sum_{d\le z}\frac{\log d}{d}\le(\log\lfloor z\rfloor)^2\le L^2 .
\]
Open the convolution in \(d\) and use the bound on \(S(z/d)\). All outer weights \(\log d\) are nonnegative, so
\[
 \left|\sum_{dr\le z}\log d\log r
      -z\sum_{d\le z}\frac{\log d\,\log(z/d)}{d}\right|
 \le2zL^2 .
\]

For the last sum, let \(g(t)=(\log t)(L-\log t)/t\) on \([1,z]\). In the variable \(v=\log t\), this is \(v(L-v)e^{-v}\). Its log derivative \(1/v-1/(L-v)-1\) is strictly decreasing on \((0,L)\), from \(+\infty\) to \(-\infty\). Thus \(g\) increases and then decreases, is zero at both endpoints, and has maximum at most \(L^2/4\). In particular its total variation is at most \(L^2/2\).

Stieltjes summation on \((1,z]\) gives, using the vanishing of \(g(1),g(z)\),
\[
 \sum_{d\le z}g(d)-\int_1^z g(t)\,dt
   =-\int_1^z(\lfloor t\rfloor-t)g'(t)\,dt
   =-\int_1^z(\lfloor t\rfloor-t+1/2)g'(t)\,dt.
\]
The last step uses \(\int_1^z g'=0\). The centered discrepancy is bounded in absolute value by \(1/2\), so the error is at most \(L^2/4\). Without centering it is at most \(L^2/2\). At integer \(z\) the upper counting jump is included and its weight \(g(z)\) is zero. The lower weight is zero as well. Finally,
\[
 \int_1^z g(t)\,dt=\int_0^L v(L-v)\,dv=\frac{L^3}{6}.
\]
Therefore uniformly for every real \(z>1\),
\[
 \left|\sum_{dr\le z}\log d\log r-\frac{zL^3}{6}\right|
 \le\frac94 zL^2\le\frac52 zL^2.
\]
At \(z=1\) the same inequality extends with both sides zero. For \(1<z<4\) the convolution itself is zero and the proof above still applies. It includes \(d=r=2\) at \(z=4\).

This is a finite-sum estimate for the particular derivative orders \((1,1)\), requiring no RH. The coefficient is a bound, without any assertion of optimality. It does not by itself give an explicit bound for the full derivative-tail asymptotic. No canonical change was made.

## Comparison with the parallel proof

I then checked [Prime142](prime142_gonek_convolution_constant.md). Its simpler harmonic comparison \(\sum_{d\le z}(\log d)/d\le L\sum_{2\le d\le z}1/d\le L^2\) is valid, including the empty range. Its derivative quadratic has exactly one root in \((0,L)\), and its uncentered variation estimate gives the stated \(5/2\). Its application to Lemma 8 uses the correct sign and the right endpoint convention.

With the centered improvement and the already verified Abel constants, the displayed two contributions can be sharpened at this single coefficient step. The \((1,1)\) outer divisor error is bounded by \((9/4)x\sum_{d\le x}\Lambda(d)d^{-1}\log^2(x/d)\). The upper Stieltjes boundary is identically zero for the two positive powers in question. Thus the sharper Abel form gives
\[
 \sum_{d\le x}\frac{\Lambda(d)}d\log^2(x/d)
       \le L_x^3/3+21L_x^2+40L_x,\qquad
 |A_3(x,\delta)|\le24L_x^3+60L_x^2
 \quad (|\delta|\le1/2,\ \delta\in\mathbb R).
\]
The first uses \(\delta=0\), and the second uses \(1+10\sqrt5<24\). Writing \(L_x=\log x\) and \(\mathcal I_3(x,\delta)=\int_1^x u^{i\delta-1}\log^3(x/u)\,du\), one obtains
\[
 \left|\sum_{n\le x} B_n(1,1,\delta)
                +\frac{x}{6}\mathcal I_3(x,\delta)\right|
 \le x\left(\frac{19}{4}L_x^3+\frac{229}{4}L_x^2+90L_x\right).
\]
This combines only the finite divisor and Abel steps. [Sharper Abel bound for positive powers](weighted134_explicit_abel_review.md)

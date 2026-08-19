# L-99101 — The factor-67 Harnack defect squares one Euler factor

Claim ID: `L-99101`  
Status: **PROVED EXACT**  
Depends on: `L-99000`  
RH status: **unproved**

Let

\[
 b_{67}(n)=a(n)-\mathbf1_{67\mid n}a(n/67).
\]

Then finite reindexing gives

\[
 \boxed{
 H_{67}(t)=C(t)-67^{-1/2}C(t/67)
 =\sum_{n\le t}\frac{b_{67}(n)}{\sqrt n}.}
\]

For `Re z>1`, T-99000 gives

\[
 \sum_{n\ge1}\frac{a(n)}{n^z}
 =6-\frac{3(1-2^{-z})(2-2^{-z})}{\zeta(z)}.
\]

Multiplication by `1-67^{-z}` therefore yields

\[
\boxed{
\begin{aligned}
 \sum_{n\ge1}\frac{b_{67}(n)}{n^z}
 ={}&6(1-67^{-z})\\
 &-3(1-2^{-z})^2(2-2^{-z})(1-67^{-z})^2
   \prod_{\substack{p\ {\rm odd}\\p\ne67}}(1-p^{-z}).
\end{aligned}}
\]

The new causal factor is not an arbitrary smoothing: it **squares the already
present local factor at 67**.

## Sparse coefficient formula

Write

\[
 n=2^e67^fm,\qquad (m,134)=1.
\]

Put

\[
 c_2(0,1,2,3)=(2,-5,4,-1),
 \qquad
 c_{67}(0,1,2)=(1,-2,1),
\]

and set either coefficient to zero outside the displayed range.  Then

\[
\boxed{
 b_{67}(n)
 =6\mathbf1_{n=1}-6\mathbf1_{n=67}
  -3c_2(e)c_{67}(f)\mu(m).}
\]

This is the formula used by the segmented exact scanner.  It is also the
source-side reason the renormalized target remains sparse and replayable.

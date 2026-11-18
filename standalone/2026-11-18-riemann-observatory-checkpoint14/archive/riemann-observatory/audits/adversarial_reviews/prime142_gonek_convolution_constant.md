# An explicit convolution error for Gonek's Lemma 7 at \((1,1)\)

18 November 2026. The coefficient form of Gonek's Lemma 7, equation (40), on journal pp. 133–134 gives an unspecified error constant in the sum of the coefficients of \(\zeta'(s)^2\). For this pair of derivative orders an elementary floor and variation argument gives, for every real \(z>1\),
\[
 \left|
 \sum_{d r\le z}\log d\,\log r-\frac{z(\log z)^3}{6}
 \right|\le \frac52\,z(\log z)^2 .
\]
The identity of the coefficients follows by multiplying the two absolutely convergent Dirichlet series for \(\zeta'\) in \(\Re s>1\). This note allocates only the \((1,1)\) convolution constant, with no new numerical derivative-tail estimate. [Gonek, Lemmas 7–8, journal pp. 133–135](../../sources/classical63_lfunctions/gonek1984.pdf)

## Inner logarithm sum

Write \(S(t)=\sum_{r\le t}\log r\) and \(n=\lfloor t\rfloor\) for any real \(t\ge1\). Since \(\log\) is nonnegative and increasing on \([1,\infty)\),
\[
 \int_1^n\log v\,dv\le S(t)\le t\log t.
\]
The lower bound holds by comparing the integral on each interval \([r-1,r]\) to its right endpoint. The loss relative to \(t\log t\) is at most
\[
 t\log t-n\log n+n-1
 =\int_n^t(1+\log v)\,dv+n-1
 \le t+\log t\le2t .
\]
Consequently \(|S(t)-t\log t|\le2t\), uniformly including \(t=1\), \(1<t<2\), or \(t\) exactly integral. The expression \(S(t)\) always includes the integer at an integral cutoff.

Apply this with \(t=z/d\) and put \(L=\log z\). Then
\[
 \sum_{dr\le z}\log d\,\log r
 =z\sum_{d\le z}\frac{\log d\,\log(z/d)}{d}+\mathcal E_1,\qquad
 |\mathcal E_1|\le2z\sum_{d\le z}\frac{\log d}{d}\le2zL^2 .
\]
The final bound uses \(\log d\le L\) and
\(\sum_{d=2}^{\lfloor z\rfloor}1/d\le\log\lfloor z\rfloor\le L\), from comparison with the right endpoint of the integral of \(1/v\) on \([d-1,d]\). If \(1<z<2\) the harmonic sum over \(d\ge2\) is empty.

## Main integral and variation

Put \(f(v)=v^{-1}\log v\,\log(z/v)\) for \(1\le v\le z\). It vanishes at both endpoints and is nonnegative between them. In the variable \(u=\log v\), the derivative of \(e^{-u}u(L-u)\) is \(e^{-u}(u^2-(L+2)u+L)\). This quadratic is positive at \(u=0\) and negative at \(u=L\), and opens upward. It has exactly one root in \((0,L)\), so \(f\) is unimodal. Since \(f(v)\le u(L-u)\le L^2/4\), its total variation is at most \(L^2/2\).

Use \(d\lfloor v\rfloor\) for integer counting on \((1,z]\). The omitted atom at 1 has weight zero. For the right-continuous error \(\lfloor v\rfloor-v\), bounded in modulus by 1, integration by parts gives
\[
 \left|\sum_{d\le z}f(d)-\int_1^z f(v)\,dv\right|
 =\left|-\int_1^z(\lfloor v\rfloor-v)f'(v)\,dv\right|
 \le L^2/2,
\]
because both boundary terms vanish. For integer \(z\), the formula includes the jump at \(z\) and \(f(z)=0\). For \(1<z<2\) it remains valid without interior atoms. The integral is exactly
\[
 \int_1^z f(v)\,dv=\int_0^L u(L-u)\,du=L^3/6.
\]
Multiplying the variation error by \(z\) and adding the inner error gives \(5zL^2/2\). For \(1<z<2\) the original double sum is zero, and the same bound also follows directly from \(L/6<5/2\). At \(z=1\) both sides of the comparison vanish.

## Its place in Lemma 8

In Gonek's notation the von Mangoldt factor contributes \(-\Lambda(d)d^{i\delta}\), so the \((1,1)\) divisor-convolution remainder before equation (36) is bounded, for real \(\delta\), by
\[
 \frac52\,x\sum_{d\le x}\frac{\Lambda(d)}d\log^2(x/d).
\]
The explicit Abel substitution with \(m=2,\delta=0\) bounds the sum by \(L_x^3/3+31L_x^2+40L_x\), \(L_x=\log x\). The main weighted prime sum has \(m=3\) and prefactor \(x/6\), so the subsequent Abel error on \(|\delta|\le1/2\) is at most \(x(31L_x^3+60L_x^2)/6\). Both bounds refer to this one coefficient step. No gamma-factor, contour or zero-tail constant is inferred. [Explicit Abel proof](prime126_explicit_abel_constant.md) · [Abel QA and source scope](prime140_director_abel_qa.md)

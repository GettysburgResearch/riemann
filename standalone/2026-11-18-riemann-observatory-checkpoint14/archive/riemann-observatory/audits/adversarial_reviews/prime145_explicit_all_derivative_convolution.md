# Explicit divisor-convolution constants for two positive derivative orders

18 November 2026. For all integers \(\mu,\nu\ge1\) and all real \(z>1\), put \(L=\log z\). Then
\[
\left|
\sum_{dr\le z}(\log d)^\mu(\log r)^\nu
-\frac{\mu!\nu!}{(\mu+\nu+1)!}\,zL^{\mu+\nu+1}
\right|
\le
\left(\min(\mu,\nu)+1+\frac{\mu^\mu\nu^\nu}{(\mu+\nu)^{\mu+\nu}}\right)
zL^{\mu+\nu}.
\]
This supplies an explicit constant for the two-positive-order part of Gonek's Lemma 7, equation (40). The signed coefficient convention for \(\zeta^{(\mu)}\zeta^{(\nu)}\) multiplies the main term and the sum by \((-1)^{\mu+\nu}\), leaving the error bound the same. For \((\mu,\nu)=(1,1)\) the constant is \(9/4\). [Gonek journal PDF, pp. 133–134](../../sources/classical63_lfunctions/gonek1984.pdf) · [Earlier \((1,1)\) calculation](prime142_gonek_convolution_constant.md)

## Uniform one-variable bound

For an integer \(j\ge1\), write \(S_j(t)=\sum_{n\le t}(\log n)^j\), \(t\ge1\). The function \(g(u)=(\log u)^j\) is continuously differentiable on \([1,t]\), with \(g(1)=0\). At \(j=1\), the derivative is \(1/u\) including at \(u=1\). Right-continuous Stieltjes partial summation gives
\[
 t(\log t)^j-S_j(t)
 =\{t\}(\log t)^j
  +j\int_1^t\frac{\lfloor u\rfloor}{u}(\log u)^{j-1}\,du .
\]
The two terms on the right are nonnegative. Using \(\{t\}\le1\), \(\lfloor u\rfloor\le u\), \(\log u\le\log t\), and \(\log t\le t\) yields
\[
 0\le t(\log t)^j-S_j(t)
 \le(\log t)^j+j(t-1)(\log t)^{j-1}
 \le(j+1)t(\log t)^{j-1}.
\]
For \(j=1\), the zeroth power of the logarithm is 1, including at \(t=1\). At \(t=1\) the exact left side is zero. If \(1<t<2\) the sum likewise vanishes, and the same identity and bound hold. At an integer cutoff the fractional term vanishes and the sum includes the integer itself.

## Outer sum and the centered floor error

Apply the one-variable bound at \(t=z/d\) and \(j=\nu\). Extracting the inner main term gives
\[
 \sum_{dr\le z}(\log d)^\mu(\log r)^\nu
 =z\sum_{d\le z}
     \frac{(\log d)^\mu(\log(z/d))^\nu}{d}+\mathcal E_1
\]
with
\[
 |\mathcal E_1|
 \le(\nu+1)zL^{\nu-1}\sum_{d\le z}\frac{(\log d)^\mu}{d}
 \le(\nu+1)zL^{\mu+\nu}.
\]
For the last inequality the \(d=1\) term vanishes because \(\mu\ge1\). The elementary harmonic comparison gives
\[
 \sum_{d=2}^{\lfloor z\rfloor}\frac{(\log d)^\mu}{d}
 \le L^\mu\sum_{d=2}^{\lfloor z\rfloor}\frac1d
 \le L^\mu\log\lfloor z\rfloor\le L^{\mu+1}.
\]
If \(1<z<2\) the sum on the left is empty. This use of the inner bound also allows \(z/d=1\), with the zeroth-power convention for \(\nu=1\).

Set \(f(v)=v^{-1}(\log v)^\mu(\log(z/v))^\nu\) on \([1,z]\). It vanishes at both endpoints and is positive in the interior. With \(u=\log v\), the logarithmic derivative of \(e^{-u}u^\mu(L-u)^\nu\) is
\[
 -1+\frac{\mu}{u}-\frac{\nu}{L-u}.
\]
It is strictly decreasing on \((0,L)\), with one positive-to-negative crossing. Thus \(f\) is unimodal, and its total variation is twice its maximum. Ignoring \(e^{-u}\le1\), the maximum is bounded by the elementary beta-polynomial maximum,
\[
 \max f
 \le \max_{0\le u\le L}u^\mu(L-u)^\nu
 =\frac{\mu^\mu\nu^\nu}{(\mu+\nu)^{\mu+\nu}}\,L^{\mu+\nu}.
\]

Both endpoints have zero weight, so the counting-measure comparison is exactly
\[
 \sum_{d\le z}f(d)-\int_1^z f(v)\,dv
 =-\int_1^z\left(\lfloor v\rfloor-v+\tfrac12\right)f'(v)\,dv .
\]
Centering by \(1/2\) leaves the integral unchanged because \(\int_1^z f'(v)\,dv=0\), and the centered floor error is bounded in absolute value by \(1/2\). Hence the error is at most half the total variation, which is \(\max f\). The equality uses right-continuous counting and includes the upper integer jump when present. At an integer \(z\), the weight of that atom is zero. The same formula holds without interior atoms for \(1<z<2\).

Finally,
\[
 \int_1^z f(v)\,dv
 =\int_0^L u^\mu(L-u)^\nu\,du
 =\frac{\mu!\nu!}{(\mu+\nu+1)!}L^{\mu+\nu+1}.
\]
The kernel error and the inner error give the stated estimate with \(\nu+1\) in place of \(\min(\mu,\nu)+1\). Exchange \(d,r\) and the two exponents and take the better of the two bounds. The beta main term and the kernel constant are symmetric, so this gives the exact claimed coefficient. At \(z=1\) both sides of the comparison vanish separately.

The proof relies on both endpoint values of \(f\) vanishing and assumes \(\mu,\nu\ge1\). Zero derivative orders need a separate endpoint calculation. This is a coefficient-level bound. Numerical constants in the subsequent contour and derivative-tail arguments remain separate.

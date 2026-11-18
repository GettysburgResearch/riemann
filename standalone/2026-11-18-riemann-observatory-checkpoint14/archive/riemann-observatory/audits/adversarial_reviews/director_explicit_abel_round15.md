# An explicit prime-to-integral substitution with complex shifts

18 November 2026. The director checked the unconditional primary-source bound, both independent Abel calculations, the endpoint convention, and the finite-interval order of the complex-shift estimate. This gives an explicit reusable constant for one step in Gonek's Lemma 8. It does not make the entire derivative-moment argument numerically effective.

## Sources and scope

Andrew Fiori and Mikko Jaskari, *Explicit bounds for the prime number theorem*, arXiv:2609.23222v2, 50 pages, SHA-256 `77d12f382218e5d63e1c3b6de0f96a7bb9dfe23538f1ecf0221d28d1f840c8db`. The inspected passages are Theorem 1.1 and its table, PDF p.4, Theorem 5.2, p.44, and the absolute-error conclusion in §5.1, p.45. The introductory signed notation alone would not justify an absolute bound; the proof conclusion does. The conditional quasi-RH transfer in Theorems 1.4 and 5.3 is not used. This is a targeted source reading, not an audit of all 50 pages or a replay of the upstream numerical optimization. [Primary preprint](https://arxiv.org/abs/2609.23222v2).

S. M. Gonek, *Mean values of the Riemann zeta-function and its derivatives*, Inventiones Mathematicae 75 (1984), 123–141, pinned journal scan SHA-256 `dfdd2444a2f62f1947c897e87101080225714dbf1f21db8ca19096d2a6e80fc3`. The application is the von Mangoldt convolution in Lemma 8. [Whole-work reconstruction](director_gonek_whole_round15.md).

Independent derivations: [prime126](prime126_explicit_abel_constant.md) and [weighted134](weighted134_explicit_abel_review.md). The result below is original archive analysis assembled from these inputs; publication novelty has not been established.

## A finite absolute error integral

Let \(E(u)=\psi(u)-u\), \(r(u)=|E(u)|/u\), for \(u\ge1\). The unconditional source bound with \(x_0=e^3\) has leading constant 0.2390 and exponent coefficient

\[
D=\frac52(5/3)^{1/5}(2000/161967)^{3/5}>0.198.
\]

The last comparison can be certified by raising positive rational quantities to the fifth power. For \(v=\log u\ge3\), its logarithmic correction is at least one, and \(\log v\le\sqrt v\). Thus

\[
r(e^v)\le0.239e^{-0.198\sqrt v}.
\]

For \(0\le v\le3\), the elementary estimate \(\psi(e^v)\le e^v v\) gives \(r(e^v)\le1+v\). Consequently \(r(u)\le4\) and

\[
\int_1^\infty r(u)\frac{du}{u}
\le\frac{15}{2}+\frac{0.478}{0.198^2}
=\frac{386015}{19602}<20.
\]

Extending the exponential integral down to zero only enlarges it. No RH assumption occurs here.

## Uniform Abel estimate

For real \(x>1\), integer \(m\ge0\), and complex \(\delta\), set \(L=\log x\), \(K=|\Im\delta|L\), and

\[
A_m(x,\delta)=\sum_{n\le x}\Lambda(n)n^{i\delta-1}\log^m(x/n)
-\int_1^x u^{i\delta-1}\log^m(x/u)\,du.
\]

All positive powers use the real logarithm, and the zeroth log power is one, including at the upper endpoint. Then

\[
|A_m|\le L^m+4e^K\mathbf1_{m=0}
+20e^K|i\delta-1|L^m+20m e^K L^{m-1},
\]

where the final term is **omitted** when \(m=0\). In particular a convenient common bound is

\[
|A_m|\le[1+e^K(4+20|i\delta-1|)]L^m+20m e^K L^{m-1}.
\]

For real \(|\delta|\le1/2\), this gives

\[
\boxed{|A_m|\le31L^m+20m L^{m-1}}.
\]

The same omitted-term convention applies. The constants are conservative. One may replace \(K\) by \(\max(0,-\Im\delta)L\).

To prove the estimate, put \(f_x(u)=u^{i\delta-1}\log^m(x/u)\). Right-continuous Stieltjes integration over \((1,x]\) gives

\[
A_m=E(x)f_x(x)-E(1)f_x(1)-\int_1^x E(u)f_x'(u)\,du.
\]

Here \(E(1)=-1\); the upper term is zero for \(m>0\) and at most \(4e^K\) for \(m=0\). A prime-power jump at \(x\) is included exactly. On this **finite** interval, \(|u^{i\delta}|\le e^K\), and

\[
|f_x'(u)|\le e^K u^{-2}
\bigl(|i\delta-1|\log^m(x/u)+m\log^{m-1}(x/u)\bigr).
\]

Bound the log powers by the corresponding powers of \(L\), then use the integral less than 20. Taking the finite-interval factor \(e^K\) out before extending the remaining nonnegative integral is essential: extending an integrand containing \(u^{-\Im\delta}\) to infinity would not justify the assertion for negative imaginary shifts. For real shifts, \(5+10\sqrt5<31\) supplies the stated common coefficient. There is no singular \(0\cdot L^{-1}\) term at \(m=0\).

## Application and remaining work

In Gonek's Lemma 8, \(m=\mu+\kappa+1\ge1\). The integral becomes the required beta integral after the substitution \(v=\log u/L\). The estimate is uniform on the real shift range used there, and on any fixed microscopic complex disk \(|\delta|L\le C\) with its displayed dependence on \(C\).

The divisor-convolution remainder, contour estimates, derivative gamma factors, and final weighted-zero tail still need their own numerical constants. Neither the coefficient 31 nor the upstream PNT theorem supplies a full derivative-tail onset or an improved enclosure for its normalized constant. The next meaningful task is to allocate constants through those remaining steps and compare the resulting onset with direct certified zero data; improving 31 in isolation has little value.

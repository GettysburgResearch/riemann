# Explicit divisor convolution for every fixed pair of derivative orders

For integers \(\mu,\nu\ge1\), the proposed coefficient \(\min(\mu,\nu)+1+\mu^\mu\nu^\nu/(\mu+\nu)^{\mu+\nu}\) is valid uniformly for all real \(z>1\). A slightly sharper additive constant follows from the same proof. Zero derivative orders can also be handled directly, with no negative logarithmic powers. [Gonek, Lemma 7, printed pp. 133–134](../../sources/classical63_lfunctions/gonek1984.pdf) · [Earlier \((1,1)\) calculation](weighted142_gonek_convolution_review.md)

## Positive orders

Write \(L=\log z\), \(M=\mu+\nu\) and \(S_\nu(q)=\sum_{r\le q}(\log r)^\nu\) for \(q\ge1\), with the integer endpoint included. Let \(q_0=\lfloor q\rfloor\). Termwise comparison and monotonicity give
\[
 \int_1^{q_0}(\log t)^\nu\,dt\le S_\nu(q)\le q(\log q)^\nu .
\]
Integration by parts on \([1,q]\), followed by an estimate over its last fractional subinterval, gives
\[
\begin{aligned}
 0\le q(\log q)^\nu-S_\nu(q)
 &\le \nu\int_1^q(\log t)^{\nu-1}\,dt
           +\int_{q_0}^q(\log t)^\nu\,dt\\
 &\le \nu q(\log q)^{\nu-1}+(\log q)^\nu
 \le (\nu+e^{-1})q(\log q)^{\nu-1}.
\end{aligned}
\]
The final inequality uses \(\sup_{q\ge1}(\log q)/q=e^{-1}\). At \(q=1\) the original error vanishes, and the zeroth power for \(\nu=1\) is taken as one. Replacing \(e^{-1}\) by 1 gives the proposed constant.

Open the convolution in \(d\) and take \(q=z/d\). The inner error is at most
\[
 (\nu+e^{-1})z
  \sum_{2\le d\le z}\frac{(\log d)^\mu}{d}
                       (\log(z/d))^{\nu-1}
 \le(\nu+e^{-1})zL^M,
\]
since each of the two log powers is bounded by its value at \(L\), and \(\sum_{2\le d\le z}1/d\le\log\lfloor z\rfloor\le L\). The \(d=1\) term was zero since \(\mu\ge1\). If \(1<z<2\), the outer sum in this bound is empty.

The resulting main sum uses
\[
 g(t)=\frac{(\log t)^\mu(L-\log t)^\nu}{t},
 \qquad 1\le t\le z .
\]
After \(v=\log t\), this is \(e^{-v}v^\mu(L-v)^\nu\), and its log derivative is \(-1+\mu/v-\nu/(L-v)\). That derivative strictly decreases from \(+\infty\) to \(-\infty\), so \(g\) has one interior maximum. It is zero at both endpoints and has total variation \(2\max g\). Ignoring \(e^{-v}\le1\), the algebraic maximum is at \(v=\mu L/M\), giving
\[
 \max g\le L^M\frac{\mu^\mu\nu^\nu}{M^M}.
\]
Integrate against the right-continuous floor counting function on \((1,z]\) and subtract Lebesgue measure. The endpoint weights vanish, so centering \(\lfloor t\rfloor-t\) at \(-1/2\) does not change the integral. The discrepancy is then bounded by half the total variation, at most \(\max g\). The main integral is
\[
 \int_1^z g(t)\,dt
 = \int_0^L v^\mu(L-v)^\nu\,dv
 = \frac{\mu!\nu!}{(M+1)!}L^{M+1}.
\]
It follows that
\[
 \left|\sum_{dr\le z}(\log d)^\mu(\log r)^\nu
                    -\frac{\mu!\nu!}{(M+1)!}zL^{M+1}\right|
 \le \left(\min(\mu,\nu)+e^{-1}
                 +\frac{\mu^\mu\nu^\nu}{M^M}\right)zL^M .
\]
The minimum comes from interchanging \(d,r\) before applying the inner estimate. This implies the proposed \(+1\) in place of \(+e^{-1}\) with the exact same domain. There is no need for a cutoff away from \(z=1\), or for avoiding integers. At integer \(z\) all original convolution terms at equality are included. The main-sum Stieltjes formula also includes the upper atom, whose weight is \(g(z)=0\).

## Zero orders

If one order is zero, put it on the inner variable and use the convention \((\log r)^0=1\) at every \(r\), including 1. For the other order \(m\ge1\), \(S_0(q)=\lfloor q\rfloor\) differs from \(q\) by at most one. The inner error after summation is at most \(\sum_{d\le z}(\log d)^m\le zL^m\). The main-sum kernel is now \(g(t)=(\log t)^m/t\), which is zero at 1 and is unimodal on the finite interval, allowing its maximum at \(z\). Because the upper endpoint need not vanish, write \(D_c(t)=\lfloor t\rfloor-t+1/2\) and retain its boundary contribution \(D_c(z)g(z)\). Then the summation discrepancy is at most \((g(z)+\operatorname{TV}(g))/2=\max g\le L^m\). The integral is \(L^{m+1}/(m+1)\). Hence
\[
 \left|\sum_{dr\le z}(\log d)^m-\frac{zL^{m+1}}{m+1}\right|
 \le 2zL^m.
\]
It includes the upper atom whether or not the kernel vanishes there.

If both orders are zero, put \(n=\lfloor z\rfloor\) and \(H_n=\sum_{d\le n}1/d\). Then \(\sum_{dr\le z}1=zH_n-\sum_{d\le n}\{z/d\}\). The inequalities \(\log(n+1)\le H_n\le1+\log n\) give \(0\le H_n-\log z\le1\). The fractional part sum also lies between 0 and \(z\), so \(\left|\sum_{dr\le z}1-z\log z\right|\le z\). These cases keep all powers at nonnegative orders.

All bounds are elementary, with no RH premise and no optimality claim. The coefficient of \(\zeta^{(\mu)}\zeta^{(\nu)}\) has the additional sign \((-1)^{\mu+\nu}\), which changes neither error estimate after putting it on both the coefficient sum and main term. No contour or numerical full-tail bound follows from these finite estimates alone. No canonical file was changed.

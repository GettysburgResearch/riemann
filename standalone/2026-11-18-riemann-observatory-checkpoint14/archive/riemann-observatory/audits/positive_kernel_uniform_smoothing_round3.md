# Finite uniform smoothing: polynomial vertical bounds, and a precise Dirichlet obstruction

2026-11-17; independent reconstruction by `/root/li_skeptic`. Root supplied the proposed smoothing and elementary convolution/Cesàro lemmas; all factors and proofs below were independently reconstructed. Earlier Bessel kernel facts and their classical Pólya1926 provenance are documented in `audits/adversarial_reviews/positive_kernel_bessel_skeptic_round3.md`. The original strict-log-concavity polynomial certificate is under separate third review; any use of that property here is conditional on its successful independent replay. No RH or novelty claim.

## Exact construction and hypotheses

Take `delta=1/100`, `a=1/4`, a fixed `T>=32`, and

\[
 c=2\pi e^{4\delta}=2\pi e^{1/25},\quad
 S_\delta(w)=\frac{\sinh(\delta w)}{\delta w},\quad
 Q_T(w)=((w-a)^2+T^2)((w+a)^2+T^2).
\]

The removable value of `S_delta` at zero is one. Let

\[
 A_T=\big[K_{1/4}(c)S_\delta(1/2)^2Q_T(1/2)\big]^{-1}>0,
\]
\[
 F_T(s)=A_T K_{(s-1/2)/2}(c)
              S_\delta(s-1/2)^2Q_T(s-1/2).
\]

The finite elementary bound `e^(1/25)<25/24` and `3<pi<22/7` give
`6<c<(44/7)(25/24)=275/42<7`. Thus the earlier positivity and log-concavity certificate's exact parameter interval `6<=c<=7` is preserved. One must not retune `c` by an arbitrary amount and silently reuse that certificate.

`F_T` is real entire, symmetric under `s -> 1-s`, normalized by `F_T(0)=F_T(1)=1`, of order one and infinite exponential type, and strictly positive on the real axis. Its centered bilateral Laplace kernel is the earlier positive smooth Bessel/quartet kernel convolved **twice** with the uniform probability density on `[-delta,delta]`. It remains smooth and everywhere positive, with double exponential tails after a bounded translation. Normalization multiplies it by a positive constant.

This is a distinct package from the unsmoothed model. The two equal uniform factors introduce **double** line zeros. No assertion that all line zeros are simple survives this operation; coincidence with a Bessel zero may increase a line multiplicity further. There remain exactly four off-line zeros, `s=1/2 +/-1/4 +/-iT`.

## Retuning the RVM smooth count exactly

For general positive `c`, Pólya1926's theorem (equivalently the independently reconstructed gamma-phase count) gives

\[
 N_{K,c}(X)=\frac X{2\pi}\log\frac Xc-\frac X{2\pi}+O(1).
\]

Each `S_delta` contributes `floor(delta X/pi)` positive-ordinate zeros. The quartet contributes two once `X>=T`. Counts add with multiplicity even at coincidences. Hence

\[
 N_{F_T}(X)=N_{K,c}(X)
       +2\lfloor\delta X/\pi\rfloor+2\mathbf1_{X\ge T}.
\]

The shift of the Bessel linear coefficient is
`-X log(c/(2pi))/(2pi)`, whereas the uniform factors contribute `2delta X/pi+O(1)`. They cancel precisely when `log(c/(2pi))=4delta`, as chosen. Thus

\[
 N_{F_T}(X)=\frac X{2\pi}\log\frac X{2\pi}
              -\frac X{2\pi}+O(1).
\]

The bounded error can be chosen uniformly over the quartet location `T`, since its count contribution is at most two; constants in later vertical bounds are allowed to depend on the fixed constructed function, including `T`.

## Elementary preservation of strict second logarithmic derivative

Here is a complete proof of the supplied convolution lemma. Let `g=e^{-V}>0` be `C^2` on `R`, with `V''>0` everywhere, and put

\[
 h(x)=\int_{x-d}^{x+d}g(v)\,dv,\quad d>0.
\]

At fixed `x`, write `b=x+d`, `a=x-d` and expectation under the positive density `g(v)/h(x)` on `[a,b]`. Let `m=E V'`. Differentiation of the translated integral gives

\[
 (\log h)''=\operatorname{Var}(V')-E V''.
\]

Integrating the derivative of `(V'-m)g` over this finite interval gives

\[
 \operatorname{Var}(V')-E V''
 =-\frac{(V'(b)-m)g(b)-(V'(a)-m)g(a)}{h(x)}<0.
\]

The last inequality is strict because `V'` is strictly increasing, so `V'(a)<m<V'(b)`, and both endpoint values of `g` are positive. No boundary-at-infinity step or external Prékopa equality theorem is needed. Dividing `h` by `2d` does not change this derivative. The convolved function is again positive and smooth, and the same argument applies a second time. Conditional on the earlier exact strict-concavity certificate, the twice-smoothed kernel therefore has `(log k)''<0` everywhere and is strictly decreasing for positive arguments by evenness.

## Uniform complex-order estimate, including the critical edge

The needed bound cannot be inferred just from a large *real* order asymptotic. Write `s=sigma+it`, `nu=(s-1/2)/2=alpha+i tau`, so `alpha=(sigma-1/2)/2`, `tau=t/2`. Fix an arbitrary finite real strip `A<=sigma<=B`, and a fixed `c>0`.

From DLMF10.25.2,

\[
 I_\nu(c)=\frac{(c/2)^\nu}{\Gamma(1+\nu)}P_\nu,\quad
 P_\nu=\sum_{k=0}^\infty
       \frac{(c^2/4)^k}{k!\prod_{m=1}^k(m+\nu)}.
\]

For `|tau|>=1`, every denominator factor has modulus at least `|tau|`. Consequently `|P_nu|<=exp(c^2/(4|tau|))`, uniformly in the fixed real strip; the same holds for `P_{-nu}`. Stirling uniformly in fixed real strips gives

\[
 |I_\nu(c)|\ll |\tau|^{-\alpha-1/2}e^{\pi|\tau|/2},\quad
 |I_{-\nu}(c)|\ll |\tau|^{\alpha-1/2}e^{\pi|\tau|/2}.
\]

Here `(c/2)^nu` uses the real logarithm of the positive number `c/2`; its modulus has no imaginary-order exponential. DLMF10.27.4 and
`|sin(pi nu)|>=sinh(pi|tau|)` now imply

\[
 |K_\nu(c)|\ll e^{-\pi|\tau|/2}
       \big(|\tau|^{\alpha-1/2}+|\tau|^{-\alpha-1/2}\big)
 \ll e^{-\pi|t|/4}|t|^{|\sigma-1/2|/2-1/2}.
\]

All constants are uniform on the chosen strip. At `sigma=1/2` both terms have the same size; cancellation can only improve this upper bound. We never divide by their difference, so there is no edge failure.

For `w=s-1/2` on the same strip,

\[
 |S_\delta(w)|\le\frac{\cosh(\delta\Re w)}{\delta|w|}
       \ll |t|^{-1},\qquad |Q_T(w)|\ll_T|t|^4.
\]

The sinc bound uses `|sinh(x+iy)|^2=sinh^2x+sin^2y<=cosh^2x`. Hence the two factors genuinely remove two powers uniformly on fixed strips.

## Gamma normalization and standard polynomial bounds

Define the meromorphic function

\[
 Z_T(s)=\frac{\pi^{s/2}F_T(s)}{s(s-1)\Gamma(s/2)}.
\]

This choice corresponds to `F=2xi` for the actual zeta function, so there is no missing factor of two. Stirling yields uniformly in any fixed real strip

\[
 |Z_T(\sigma+it)|\ll
 |t|^{E(\sigma)},\qquad
 E(\sigma)=\frac{|\sigma-1/2|-\sigma}{2}
 =\begin{cases}1/4-\sigma,&\sigma\le1/2,\\-1/4,&\sigma\ge1/2.
 \end{cases}
\]

The exponent bookkeeping is: Bessel `|sigma-1/2|/2-1/2`, quartet `+4`, two sinc factors `-2`, `s(s-1)` `-2`, reciprocal gamma `-sigma/2+1/2`; the exponential factors cancel exactly. In particular `Z_T(sigma+it)=O(|t|^{-1/4})` on each fixed right-hand strip. On `0<=sigma<=1` this is stronger than the standard convexity-shaped upper bound `O(|t|^{(1-sigma)/2+epsilon})`. Thus ordinary polynomial vertical bounds alone do not repair the countermodel.

There are further exact normalization facts. `Z_T` has only a simple pole at `s=1`, of residue one; the apparent pole at zero is removable, with `Z_T(0)=-1/2`. At every negative even integer it has an exactly simple zero, because reciprocal gamma has a simple zero there and `F_T` is positive on the entire real axis. Finally

\[
 \pi^{-s/2}\Gamma(s/2)Z_T(s)=\frac{F_T(s)}{s(s-1)}
\]

is invariant under `s -> 1-s`. This is exactly the usual completed functional equation, interpreted meromorphically. These statements do not make `Z_T` the Riemann zeta function.

## A rigorous obstruction to an ordinary Dirichlet series

Suppose for contradiction that, on some right half-plane, `Z_T(s)=sum_{n>=1}a_n n^{-s}` and the series is absolutely convergent at a real `sigma_0`. At any fixed `sigma>max(sigma_0,1)`, termwise integration and domination by `sum|a_n|n^{-sigma}` give for each positive integer `m`

\[
 \lim_{H\to\infty}\frac1{2H}\int_{-H}^H
 Z_T(\sigma+it)e^{it\log m}\,dt=a_m m^{-\sigma}.
\]

For `n!=m` the elementary integral is `sin(H log(m/n))/(H log(m/n))`, tending to zero; the diagonal integral is one. Absolute convergence justifies passing the limit through the series. But the proved vertical decay makes the absolute Cesàro average of `Z_T` tend to zero. Therefore every `a_m=0`, contradicting that `Z_T` is nonzero. No Euler product assumption is needed. This excludes every ordinary Dirichlet series with a half-plane of absolute convergence. Any ordinary series convergent somewhere has a sufficiently far right half-plane of absolute convergence, so it also excludes a nonempty ordinary half-plane of convergence.

This is the exact remaining obstruction: the constructed analytic normalization passes the listed gamma/functional-equation/growth/pole/trivial-zero tests but cannot have a discrete arithmetic Dirichlet expansion.

## An independent real-axis witness and its exact constant

For `nu>1` an exact change of variables in the bilateral Bessel integral gives

\[
 K_\nu(c)=\tfrac12(c/2)^{-\nu}\Gamma(\nu)
    E\exp[-(c^2/4)/X_\nu],\quad X_\nu\sim\operatorname{Gamma}(\nu,1).
\]

Since `0<=1-e^{-z/x}<=z/x`, the relative deviation of the expectation from one is at most `(c^2/4)/(nu-1)`. Thus its fixed-`c` large-real-order asymptotic is established directly, without a guessed continuation of an imaginary-order formula.

For real `sigma` tending to infinity, put `w=sigma-1/2`, `nu=sigma/2-1/4`. Use `Q_T(w)~w^4`,
`S_delta(w)^2~e^{2delta w}/(4delta^2 w^2)`, and
`Gamma(sigma/2-1/4)/Gamma(sigma/2)~(sigma/2)^{-1/4}`. Exact retuning cancels every real exponential. The surviving constant is

\[
 Z_T(\sigma)\sim C_T\sigma^{-1/4},\qquad
 C_T=\frac{A_T(2\pi)^{1/4}}{8\delta^2}>0.
\]

For a nonzero absolutely convergent ordinary Dirichlet series let `n_0` be its least nonzero coefficient. Absolute convergence and dominated convergence imply its real-axis asymptotic is `a_{n_0}n_0^{-sigma}(1+o(1))`, either a nonzero constant or exponential decay. It cannot have this strictly positive algebraic decay. This is a second, independent Dirichlet obstruction.

The same exponent calculation for `r` finite uniform factors of positive widths `delta_j`, with retuning `c=2pi exp(2 sum delta_j)`, yields `Z(sigma)~C sigma^{7/4-r}` for a positive constant `C`. Since no integer `r` equals `7/4`, finite uniform smoothing cannot remove this real-axis mismatch. Shape-certificate reuse still requires keeping the retuned `c` in its verified interval; no arbitrary-width conclusion is made.

## Finite Li prefix and limitations

With the quartet omitted, the Bessel and uniform factors have only line zeros. Their paired products have no hidden exponential factor (evenness and order one), and their reciprocal squared ordinates sum. Each fixed Li coefficient is strictly positive, since the Bessel factor alone supplies a positive line-pair contribution. The quartet contributes at most `4n/T(1+1/T)^{n-1}` in absolute value. Therefore each fixed finite prefix stays positive for sufficiently large fixed `T`, exactly as in the unsmoothed proof. The uniform widths and retuned `c` are held fixed when `T` tends to infinity.

The model has no ordinary Dirichlet expansion; no Euler product or prime explicit formula is asserted. It does not match individual zeta zeros or multiplicities, and equal smoothing widths deliberately add double line zeros. Prescribed finite Li positivity has the quantifier `for every N there exists T`; no all-coefficient positivity is claimed. The assembly's priority remains unassessed. The count and base all-imaginary-zero results are classical Pólya1926 mathematics; the archive independently reconstructs their use and records precisely which additional hypotheses do real work.

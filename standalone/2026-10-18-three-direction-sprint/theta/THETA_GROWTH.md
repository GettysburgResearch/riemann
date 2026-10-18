# A complete-source Gaussian growth bound and quantitative complex approximation

Status: **PROPOSED native analytic lemmas.** Independent review is required.
No zero-location theorem for xi is assumed or concluded by the growth bound.
The cofinal strip-model feasibility hypothesis remains open.

## 1. Full theta kernel strong log concavity

Use the original positive theta kernel `Phi` and its normalization from
PROOF22.md. On the whole real line,

\[
 \boxed{-(\log\Phi)''(t)\ge88/5.}
 \tag{1}
\]

Here all theta indices are retained. The bound is deliberately elementary
and is not claimed optimal.

First, the classical Jacobi theta transformation guarantees smooth evenness,
including at zero. To make that input explicit, write
`Theta(u)=sum_(n in Z) exp(-pi*n^2*u)` and
`r(t)=exp(t/2)Theta(exp(2t))`. Jacobi's identity
`Theta(u)=u^(-1/2)Theta(1/u)` gives `r(t)=r(-t)`. Direct differentiation of
the normally convergent series gives

\[
 2\Phi(t)=r''(t)-\tfrac14r(t).
\]

Thus the positive half-line source extends to the same smooth even kernel.
It suffices to prove (1) for `t>=0`.

Let `g_n(t)` denote the nth positive summand of `Phi(t)`. Put

\[
 x=2\pi e^{2t}>6,\qquad N=n^2,\quad b=(N-1)/2,
 \quad R(t)=\sum_{n\ge2}g_n(t)/g_1(t).
\]

The exact ratio is

\[
 \frac{g_n}{g_1}
 =N\frac{Nx-3}{x-3}e^{-bx}
 =\left(N^2+\frac{3N(N-1)}{x-3}\right)e^{-bx}.
 \tag{2}
\]

For the first theta term,

\[
 - (\log g_1)''=2x+\frac{12x}{(x-3)^2}>19\qquad(x\ge6).
 \tag{3}
\]

After multiplying the inequality by `(x-3)^2`, its numerator is
`2x^3-31x^2+144x-171`. Set `y=x-7>=-1`; the numerator becomes
`2y^3+11y^2+4y+4`. It is positive for `y>=0`. For `-1<=y<=0`, put
`u=-y in[0,1]` and bound it below by
`9u^2-4u+4=9(u-2/9)^2+32/9>0`. This proves (3).

For the ratios (2), differentiation is with `D_t=2xD_x`. Since `x>=6`,

\[
 D_t^2e^{-bx}\le4b^2x^2e^{-bx},
\]

and, dropping only the negative first-derivative part,

\[
 D_t^2\frac{e^{-bx}}{x-3}
 \le e^{-bx}\left(8b^2x+32b+\frac{64}{x}\right).
\]

The latter follows from
`1/(x-3)<=2/x`, `1/(x-3)^2<=4/x^2`, and
`1/(x-3)^3<=8/x^3`. Each positive function
`x^2e^-bx`, `xe^-bx`, `e^-bx`, and `x^-1e^-bx` decreases for `x>=6`, because
`b>=3/2`. Consequently

\[
 \left(\frac{g_n}{g_1}\right)''
 \le C_Ne^{-3(N-1)},
\]

where the exact polynomial upper coefficient is

\[
 C_N=36N^2(N-1)^2+
 3N(N-1)\left(12(N-1)^2+16(N-1)+\tfrac{32}{3}\right).
 \tag{4}
\]

In particular `C_4=11184`. Also `C_N<87N^4` for `N>=4`: the first term is
at most `36N^4`, and the second at most `50N^4` using `N>=4`.
The exact rational Taylor sum for `exp(3)` through degree8 exceeds20. Hence

\[
 R''(t)<\frac{11184}{20^3}
       +\sum_{n\ge3}\frac{87n^8}{20^{n^2-1}}<\frac75.
 \tag{5}
\]

For completeness, the ratio of consecutive displayed tail bounds is below
`(4/3)^8/20^7<1/2`, so the complete tail is below
`2*87*3^8/20^8<1/1000`. Adding that to `11184/8000=1.398` gives less than1.4.
All derivative series are absolutely normally convergent by these same
polynomial-times-exponential index bounds, so termwise differentiation and
summation are justified.

Finally,

\[
 (\log\Phi)''=(\log g_1)''+
 \frac{R''}{1+R}-\frac{(R')^2}{(1+R)^2}
 <-19+\frac75=-\frac{88}{5}.
\]

Here `R>=0`; the positive upper bound in (5) controls `R''/(1+R)` even if
`R''` happens to be negative. Smooth evenness transfers the bound to negative
`t` and to zero. This proves (1) with no discarded theta index or time tail.

## 2. Exponential tilts give the actual xi growth bound

The following elementary deduction avoids an imported concentration theorem.
If an even density has potential `V=-log density` with `V''>=c>0` and the
decay needed for integration by parts, every real exponential tilt has
variance at most `1/c`.

Indeed let `X` have tilted density proportional to `exp(sx-V(x))`, with mean
`m`. Integration by parts gives

\[
 1=\mathbb E[(X-m)(V'(X)-s)]
  =\mathbb E[(X-m)(V'(X)-V'(m))]\ge c\operatorname{Var}(X).
\]

The boundary terms vanish for the original superexponentially decaying
theta kernel and every real tilt. If `K(s)=log E exp(sT)`, then
`K''(s)=Var_s(T)<=1/c`. Evenness gives `K(0)=K'(0)=0`. Integrating twice,
with `c=88/5` from (1), yields the unconditional source bound

\[
 \boxed{\mathbb Ee^{sT}\le e^{5s^2/176}\quad(s\in\mathbb R),
 \qquad
 |\xi(1/2+iz)/\xi(1/2)|\le e^{5|z|^2/176}.}
 \tag{6}
\]

For the standardized theta variable `Y=T/sqrt(v)`, this gives

\[
 |F_Y(z)|\le e^{B|z|^2},\qquad B=\frac5{176v}.
 \tag{7}
\]

The exact variance enclosure is reconstructed from the full source. The
coefficient `B` is about0.615. This is an entire growth bound; it supplies
neither the reality of zeros nor a factorization of xi with real zeros.

## 3. A quantitative consumer on growing complex disks

Let `f` and `F` be even entire functions with
`|f(z)|<=exp(A|z|^2)` and `|F(z)|<=exp(B|z|^2)`, where `D=max(A,B)>0`.
Suppose their Taylor coefficients agree through degree `2n` and put `m=n+1`.
For every `R>=0` with `DR^2<m`,

\[
 \boxed{\sup_{|z|\le R}|f(z)-F(z)|
 \le\frac{2(eDR^2/m)^m}{1-DR^2/m}.}
 \tag{8}
\]

Apply Cauchy's coefficient estimate on radius `L>R`. Every difference of
degree `2r` coefficients is at most `2exp(DL^2)/L^(2r)`. Sum the resulting
geometric tail beginning with `r=m`, then choose `L^2=m/D`.
This proves (8). At `R=0` the bound is read by continuity.

If there are finite coefficient errors instead of equality, add the explicit
polynomial error sum
`sum_(r=0)^n |mu_f,2r-mu_F,2r| R^(2r)/(2r)!` to the right side, with the
same full tail estimate. No numerical residual is silently treated as zero.

For strip-confined approximants, the value of `A` can be supplied by the
one-point theorem or the variance/zero-gap theorem in PROOF.md. Equation(7)
supplies an independent actual-theta value of `B`, so this consumer does not
deduce a target bound from the desired approximation. If `D` stays bounded
and `R^2<=eta*m/(eD)` for fixed `eta<1`, the right side decays geometrically
in `m`. This gives certified growing complex domains **conditional on actual
finite moment feasibility**, rather than merely a count of matched moments.

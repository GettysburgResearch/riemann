# All derivative companions have a positive sector outside the complete strip

Status: proposed source-bound analytic theorem, with a complete proof.
Scope: global in the real coordinate, for every fixed derivative order and
every fixed positive companion parameter, on the open outer half-plane.
No conclusion in the remaining closed strip is asserted.
Native proof: the polynomial companion argument, limiting strictness, source
moment anchors, and quantitative adapters below.
Imported inputs: Hadamard factorization for entire functions of order below
one, differentiated local convergence, Gauss--Lucas, Hurwitz, the strong
harmonic minimum principle, and Schwarz--Pick. For actual Xi, its entire
order, complete classical zero strip, Jacobi inversion and the completed-xi
Mellin identity are also imported. A local zero census cannot replace the
complete strip hypothesis.

## 1. General theorem with explicit hypotheses

Let `mu` be a finite positive Borel measure on `[0,infinity)` such that

\[
\mu((0,\infty))>0,
\qquad \int_0^\infty e^{cu}\,d\mu(u)<\infty
\quad\text{for every }c\ge0.
\tag{O1}
\]

Define its even Fourier transform

\[
F(z)=\int_0^\infty(e^{izu}+e^{-izu})\,d\mu(u).
\tag{O2}
\]

Assume additionally that `F` has entire order strictly below two, and that its
**complete, multiplicity-preserving** zero multiset satisfies

\[
|\operatorname{Im}\rho|\le A,\qquad A\ge0.
\tag{O3}
\]

The order hypothesis is separate from (O1); exponential moment finiteness
alone does not give it. Fix any integer `r>=0` and real `lambda>0`, and put

\[
H_r=F^{(r)},\qquad
E_{r,\lambda}=H_r-i\lambda H_r'.
\tag{O4}
\]

**Theorem.** On the entire connected half-plane
`D_A={z:Im z<-A}`,

\[
H_r\ne0,\quad
\operatorname{Im}(H_r'/H_r)>0,
\quad E_{r,\lambda}\ne0,
\quad E_{r,\lambda}'\ne0,
\tag{O5}
\]

\[
\operatorname{Im}\frac{E_{r,\lambda}'}{E_{r,\lambda}}>0,
\qquad
\operatorname{Re}W_{r,\lambda}>0,
\qquad
W_{r,\lambda}:=\frac{iE_{r,\lambda}}{E_{r,\lambda}'}.
\tag{O6}
\]

Thus for **all real `T`**, the lower ray `z=T-iy` has the asserted sector
whenever `y>A`, independent of `r`. The same fixed `lambda` is used in
`E` and `E'`; in particular `E'_(r,lambda)=E_(r+1,lambda)` exactly. These are
pointwise global assertions, not a positive uniform margin as `|T|` grows or
`y` decreases to `A`.

For completeness the assertions about `H_r` and its logarithmic derivative
also hold when the companion parameter is zero. The positive-parameter
statement is the one used in source transport.

## 2. Complete paired products and all fixed derivatives

Equation (O1) permits differentiation under the integral at every fixed
order, locally uniformly in `z`. For example, a compact set with
`|Im z|<=M` is dominated at order `j` by `2u^j e^{Mu}`, which is integrable
by the moment with exponent `M+1` and an elementary bound on `u^j e^{-u}`.
Consequently `F` is even real entire and `F(0)=2mu([0,infinity))>0`.

Evenness supplies an entire function `J` with `F(z)=J(z^2)`. The equality of
maximum moduli

\[
M_J(R)=M_F(\sqrt R)
\tag{O7}
\]

shows that the order of `J` is half the order of `F`, hence below one.
Hadamard's theorem gives the genus-zero factorization

\[
F(z)=F(0)\prod_{\{\rho,-\rho\}}
                 (1-z^2/\rho^2)^{m_\rho},
\qquad \sum_{\{\rho,-\rho\}}m_\rho|\rho|^{-2}<\infty.
\tag{O8}
\]

There is no zero factor at zero and no nonconstant exponential multiplier.
Each opposite pair appears once with its analytic multiplicity. Choose an
increasing exhaustion by finite sets of pairs closed under conjugation, and
let `P_n` denote their complete finite products times `F(0)`. Every zero of
every `P_n` satisfies (O3). Absolute genus-zero convergence yields local
uniform convergence `P_n->F`; Cauchy's integral formula then yields

\[
P_n^{(j)}\longrightarrow F^{(j)}
\quad\text{locally uniformly, for every fixed }j.
\tag{O9}
\]

The degrees tend to infinity. Indeed, positivity gives numbers `v>0` and
`m>0` with `mu([v,infinity))>=m`. Therefore `F(-iy)>=m e^{vy}` for `y>0`,
so `F` is not a polynomial. A finite product (O8) would be a polynomial.
For any fixed `r`, discard the finite initial segment until
`deg P_n>=r+1`; every `H_n=P_n^(r)` in the remaining tail has positive degree.

## 3. The complete polynomial argument

The closed strip in (O3) is convex. Repeated Gauss--Lucas places every zero
`alpha_j` of `H_n=P_n^(r)` in that same strip, with its multiplicity `nu_j`.
For `z in D_A`,

\[
\frac{H_n'}{H_n}(z)=\sum_j\frac{\nu_j}{z-\alpha_j},
\qquad
\operatorname{Im}\frac1{z-\alpha_j}
 =\frac{\operatorname{Im}\alpha_j-\operatorname{Im}z}
        {|z-\alpha_j|^2}>0.
\tag{O10}
\]

Since `H_n` has positive degree, this logarithmic derivative has strictly
positive imaginary part. Therefore

\[
\operatorname{Re}\frac{H_n-i\lambda H_n'}{H_n}
 =1+\lambda\operatorname{Im}(H_n'/H_n)>1.
\tag{O11}
\]

It follows that `E_n=H_n-i lambda H_n'` has no zero in `D_A`. Its degree is
exactly `deg H_n`, since the derivative cannot cancel the highest term.
Every zero `eta_j` of the **complete** companion polynomial consequently
satisfies `Im eta_j>=-A`. Its full logarithmic derivative gives

\[
\operatorname{Im}\frac{E_n'}{E_n}(z)
 =\sum_j\frac{m_j(\operatorname{Im}\eta_j-\operatorname{Im}z)}
                   {|z-\eta_j|^2}>0
\quad(z\in D_A).
\tag{O12}
\]

No upper bound on the companion zeros is needed. No selected zero packet,
numerical root search, or asymptotic tail substitutes for either complete
polynomial sum.

## 4. Positive source moments make the limiting signs strict

For `y>0` and `j>=0`, define

\[
A_j(y)=\int_0^\infty u^j
       [e^{yu}+(-1)^j e^{-yu}]\,d\mu(u)>0.
\tag{O13}
\]

At `j=0` use the usual convention `u^0=1`, including a possible atom at zero.
For even `j` the bracket is twice `cosh(yu)`; for odd `j` it is twice
`sinh(yu)`. The positive mass on `(0,infinity)` makes every integral strictly
positive. Direct differentiation of the same source gives

\[
F^{(j)}(-iy)=i^jA_j(y),
\tag{O14}
\]

\[
E_{r,\lambda}(-iy)=i^r[A_r(y)+\lambda A_{r+1}(y)],
\quad
E_{r,\lambda}'(-iy)=i^{r+1}[A_{r+1}(y)+\lambda A_{r+2}(y)].
\tag{O15}
\]

By (O9), `H_n->H_r` and `E_n->E_(r,lambda)` locally uniformly. Hurwitz on
`D_A` says each limit is either nowhere zero or identically zero there.
Choose any `y>A`; (O14)--(O15) exclude the identically-zero alternatives.
Thus both limits are nowhere zero on `D_A`. Their logarithmic derivatives
are the locally uniform limits of the corresponding polynomial quotients.
Equations (O10) and (O12) give nonnegative limiting imaginary parts.

Each imaginary part is harmonic. At `z=-iy`, (O14)--(O15) give respectively

\[
\operatorname{Im}(H_r'/H_r)=A_{r+1}/A_r>0,
\qquad
\operatorname{Im}(E'/E)
 =\frac{A_{r+1}+\lambda A_{r+2}}{A_r+\lambda A_{r+1}}>0.
\tag{O16}
\]

The strong harmonic minimum principle on the connected domain now makes
both inequalities strict everywhere on `D_A`. In particular `E'` is nowhere
zero. If `q=E'/E`, then

\[
\operatorname{Re}(i/q)=\frac{\operatorname{Im}q}{|q|^2}>0,
\tag{O17}
\]

which proves (O5)--(O6). Strictness is supplied by the source and the minimum
principle, not by an invalid passage of strict inequalities through a limit.

## 5. Exact quantitative anchor in the shifted half-plane

Fix `y_0>A`, put `z_0=-iy_0`, and define the positive exact source ratio

\[
m_0=\frac{A_{r+1}(y_0)+\lambda A_{r+2}(y_0)}
           {A_r(y_0)+\lambda A_{r+1}(y_0)}>0.
\tag{O18}
\]

Then `q(z_0)=i m_0` and `W(z_0)=1/m_0`. For `z=T-iy in D_A`, set

\[
\rho(z)=\left|\frac{z-z_0}{z-\overline{z_0}+2iA}\right|
 =\sqrt{\frac{T^2+(y-y_0)^2}{T^2+(y+y_0-2A)^2}}<1,
\quad K(z)=\frac{1+\rho(z)}{1-\rho(z)}.
\tag{O19}
\]

The denominator is the distance to the reflection of `z_0` across
`Im z=-A`; the displayed sign of `2iA` follows from that reflection.
Schwarz--Pick, after mapping `D_A` and the upper half-plane to disks, gives

\[
\left|\frac{q(z)-im_0}{q(z)+im_0}\right|\le\rho(z).
\tag{O20}
\]

Applying the same disk argument to the right-half-plane function `W` gives

\[
\operatorname{Im}q(z)\ge\frac{m_0}{K(z)},\qquad
|q(z)|\le m_0K(z),\qquad
\operatorname{Re}W(z)\ge\frac1{m_0K(z)},\qquad
|W(z)|\le\frac{K(z)}{m_0}.
\tag{O21}
\]

For example, the inverse disk map for `W` is
`W=(1/m_0)(1+h)/(1-h)` with `|h|<=rho`; its real part is
`(1/m_0)(1-|h|^2)/|1-h|^2`, proving the stated lower bound.
These are analytic bounds in exact source moments. A numerical value for a
moment would need its own rigorous integral and tail enclosure.

## 6. Actual Xi, inherited hypotheses, and sharpness

Use the real-ordinate normalization

\[
\Xi(z)=\xi(1/2+iz)=2\int_0^\infty\Phi_\theta(u)\cos(zu)\,du,
\tag{O22}
\]

\[
\Phi_\theta(u)=\sum_{n\ge1}
 [4\pi^2n^4e^{9u/2}-6\pi n^2e^{5u/2}]
 e^{-\pi n^2e^{2u}},\qquad u\ge0.
\tag{O23}
\]

The corrected source identity and even extension are in
[R16](../../../../../reviews/D-pass3/PROOFS_AND_REPAIRS.md#r16-xi-cardinal-domain-and-complete-background-capture-s01).
Every summand is strictly positive: writing `t=pi n^2 e^(2u)>=pi`, its
prefactor is `2pi n^2 e^(5u/2)(2t-3)>0`. The double-exponential tail gives
all exponential moments and the required differentiated convergence.
Actual Xi has classical entire order one, so the order hypothesis holds.

Its zeros correspond exactly, with multiplicity, to the nontrivial zeta
zeros. The classical strip `0<Re s<1` supplies the complete hypothesis with
`A=1/2`. An independently established complete strip
`1-B<=Re s<=B`, `B>=1/2`, supplies `A=B-1/2`. This theorem proves neither
an improved `B` nor RH. Supplying `A=0` for actual Xi would already supply RH.

The boundary is sharp for the general class. For `A>0`, the polynomial
`z^2+A^2` has boundary zeros and an order-zero companion zero at

\[
z=-iy_\lambda,\qquad
y_\lambda=\sqrt{A^2+\lambda^2}-\lambda<A,
\qquad y_\lambda\to A\quad(\lambda\downarrow0).
\tag{O24}
\]

This is a control for strip information alone; it is not a positive Fourier
source. Within the actual theorem's positive-source class,
[DERIVATIVE_COUNTEREXAMPLE.md](../DERIVATIVE_COUNTEREXAMPLE.md) gives
`F_delta(z)=cos z+epsilon cos(2z)`,
`epsilon=cosh(delta)/cosh(2delta)`, `0<delta<=log 2`. Its complete strip is
`|Im z|<=delta`. On `z=pi-iy`, write
`f(y)=-cosh y+epsilon cosh(2y)`. Its companion has the unique zero
`f(y_lambda)+lambda f'(y_lambda)=0` with `0<y_lambda<delta`.
Since `f(delta)=0` and `f'(delta)>0`, the implicit function theorem at
`(y,lambda)=(delta,0)` gives

\[
y_\lambda=\delta-\lambda+O(\lambda^2).
\tag{O25}
\]

Thus no smaller universal entry height follows even from positive complete
source, order one, and the complete strip. For any prescribed `A>0`, replace
`F_delta(z)` by `F_delta((delta/A)z)`; its strip width is exactly `A`, and
its positive-parameter companion zeros again approach `A` from below.
The counterexample is not the native arithmetic theta source.

For actual Xi the remaining unconditional region is `0<y<=1/2`. The theorem
does not continue a strict sign across the strip boundary, control the real
boundary, or price the low-order wrong extrema, poles and winding. The
quantitative bounds in (O21) degenerate when `rho->1`, which includes
approach to the strip boundary and escape in the real direction.

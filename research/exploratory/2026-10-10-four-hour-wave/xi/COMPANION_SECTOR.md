# A quantitative positive-source companion certificate

Status: proposed analytic lemma with a complete moment proof.
Scope: a source-to-adjacent-companion estimate, conditional on explicit moment
and tilted-variance bounds. No RH-bearing low-order estimate is asserted.

Let `Phi>=0` on `(0,infinity)` and

\[
F(z)=\int_0^\infty\Phi(u)(e^{izu}+e^{-izu})\,du.
\]

Assume M_0 is finite and the exponentially tilted moments through order r+3
needed below are finite, with domination in a neighborhood of each point.
The r+3 moment supplies the variance of the (1+u/mu)-weighted measure.
Thus the Fourier integrals and their first derivatives are holomorphic at the
points under consideration. Fix an integer `r>=0` with finite nonzero moments

\[
M_j=\int u^j\Phi(u)\,du,\quad
\mu=M_{r+1}/M_r>0,\quad
\sigma^2=M_{r+2}/M_r-\mu^2,\quad
\eta=\sigma/\mu,\quad\lambda=1/\mu.
\]

At `z=T-iy`, `y>=0`, define

\[
\begin{aligned}
P&=\int u^r\Phi(u)(1+u/\mu)e^{yu+iTu}\,du,&
P_1&=\int u^{r+1}\Phi(u)(1+u/\mu)e^{yu+iTu}\,du,\\
N&=\int u^r\Phi(u)(1-u/\mu)e^{-yu-iTu}\,du,&
N_1&=\int u^{r+1}\Phi(u)(1-u/\mu)e^{-yu-iTu}\,du.
\end{aligned}
\]

The reflection terms can have either sign; they remain in every formula.
Let `A` be the mass of the positive measure defining P, and let `m>0` and
`v>=0` be its normalized mean and variance. Set

\[
\kappa=T^2v/2,
\quad
\alpha=\frac{\eta}{2(1-\kappa)},
\quad
\beta=\frac{|T|v/m}{1-\kappa}
       +\frac{\eta\sqrt{1+\eta^2}}{2(1-\kappa)}.       \tag{S1}
\]

If `kappa<1` and `beta<1`, then `E'_(r,lambda)` is nonzero and

\[
\left|m\frac{iE_{r,\lambda}}{E'_{r,\lambda}}-1\right|
 \le\frac{\alpha+\beta}{1-\beta}.                    \tag{S2}
\]

If additionally `alpha+2 beta<1`, the right side is less than one; hence
`E_(r,lambda)` is also nonzero and
`Re(i E_(r,lambda)/E'_(r,lambda))>0`.
Uniform bounds in y give the same certificate on the complete lower ray.
The quotient stays in the open right half-plane, so its continuous argument
cannot accumulate an unobserved winding.

## Proof

Center the positive tilted measure at m. The inequality
`cos t>=1-t^2/2` gives

\[
|P|\ge A(1-\kappa).
\]

Using its centered first moment zero and `|exp(it)-1|<=|t|`,

\[
|P_1-mP|
 = A|\mathbb E[(U-m)(e^{iT(U-m)}-1)]|
 \le A|T|v.                                        \tag{S3}
\]

Because `e^-yu<=1`, Cauchy–Schwarz for the untilted r-moment measure gives

\[
|N|\le M_r\sigma/\mu,
\qquad
|N_1|\le M_r\sigma\sqrt{\mu^2+\sigma^2}/\mu.         \tag{S4}
\]

Positivity and y>=0 give the essential normalizations

\[
A\ge2M_r,
\qquad
mA\ge M_{r+1}+M_{r+2}/\mu\ge2M_r\mu.               \tag{S5}
\]

For `s=(-1)^r`, differentiating the same frozen lambda yields

\[
E_{r,\lambda}=i^r(P+sN),\quad
E'_{r,\lambda}=i^{r+1}(P_1-sN_1).
\]

Thus, with `n=sN/P` and
`d=(P_1-mP)/(mP)-sN_1/(mP)`, the exact quotient is

\[
m\frac{iE_{r,\lambda}}{E'_{r,\lambda}}
 =\frac{1+n}{1+d},\qquad |n|\le\alpha,\quad|d|\le\beta.
\]

The denominator has modulus at least `1-beta`; subtract one to obtain (S2).
Every sign and both reflected terms have been retained.

An explicit sufficient version is

\[
T^2v/2\le1/4,\qquad\eta\le1/8,
\qquad |T|v/m\le1/16.                               \tag{S6}
\]

Then `alpha<=8/96`, `beta<17/96` (use `sqrt(65)<9`), and the error is
strictly less than `25/79`. This is a finite quantitative implication, not an
asymptotic claim that its inputs hold at low order.

## Exact adjacent-parameter drift

For the moment-dependent parameters `mu_r=M_(r+1)/M_r`,
`lambda_r=1/mu_r`, `eta_r^2=Var_(r)(U)/mu_r^2`,

\[
\mu_{r+1}=\mu_r(1+\eta_r^2),\quad
\lambda_{r+1}=\frac{\lambda_r}{1+\eta_r^2},\quad
\frac{\lambda_r-\lambda_{r+1}}{\lambda_{r+1}}=\eta_r^2. \tag{S7}
\]

Consequently

\[
\frac{\lambda_a}{\lambda_b}
 =\frac{\mu_b}{\mu_a}
 =\prod_{r=a}^{b-1}(1+\eta_r^2),\qquad
\sum_{r=a}^{b-1}\eta_r^2\ge\log(\mu_b/\mu_a).       \tag{S8}
\]

If `eta_r^2<=q` on the band, the reverse bound
`sum eta_r^2 <=(1+q)log(mu_b/mu_a)` follows from
`log(1+x)>=x/(1+q)`.

For a theta-tail source, the reviewed saddle asymptotic `mu_r~(log r)/2`
therefore forces the accumulated relative parameter drift from any fixed
order to r to be at least `log log r-O(1)`. It cannot be described as a
uniformly summable error. A constant-fraction high-order band is different:
the ratio of its endpoint means tends to one. These are precise statements
about parameter drift, not a proof that every possible descent method fails;
a valid method may account for that drift explicitly.

Indeed

\[
E'_{r,\lambda_r}-E_{r+1,\lambda_{r+1}}
 =-i(\lambda_r-\lambda_{r+1})F^{(r+2)}.               \tag{S9}
\]

Keeping lambda fixed removes (S9) exactly, but it does not remove the signed
lower-order obstruction proved in `DERIVATIVE_COUNTEREXAMPLE.md`.

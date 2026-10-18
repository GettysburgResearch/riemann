# A growth-controlled infinite star, and a strict global-tilt obstruction

**Status: PROPOSED complete analytic construction and obstruction.** The
infinite star below has a rigorous entire limit and real Fourier zeros.
The simple global-cosh-tilt subclass cannot equal the actual theta law,
even after any finite change of its fair-spin head. A varying coupling
profile can repair the first asymptotic mismatch; no exact theta
representation or improved zeta zero-free region is established.

Subsequent packet results sharpen the scope: HARMONIC_LATTICE_OBSTRUCTION.md
excludes the exact harmonic analytic-profile class even with an observed
hub and arbitrary fixed head changes. ANALYTIC_TAIL_OBSTRUCTION.md extends
this to analytic harmonic-type weights and uniformly regular compact-head
cofinal schemes. The surviving classes described at the end of this file
are therefore candidates only outside those stronger analytic premises.

This architecture was proposed jointly with the root research track after
the user redirected work from higher finite moment orders to actual
cofinal completion. The calculations use complete functions, not fitted
moments or sampled zeros.

## 1. The infinite construction and its automatic growth budget

Fix `a>0` and put `w_n=1/[2(n+a)]`, `n=0,1,...`. More generally allow
finitely many weights to be changed, deleted or added. Let `J_n>=0`,
`eta_n=tanh(J_n)`, and assume

\[
 \sum_n w_n^2<\infty,\qquad m:=\sum_n w_n\eta_n<\infty. \tag{1}
\]

Given a fair hub `S`, let the leaf spins be independent with
`E(sigma_n|S)=S eta_n`. The partial observables `X_N=sum_(n<=N)w_n sigma_n`
are precisely finite zero-field ferromagnetic stars. Conditional on the
hub, their means converge and their centered independent sums converge in
L2 (and almost surely by the elementary independent-series convergence
criterion). Thus they define a symmetric limit `X` with

\[
 \operatorname{Var}X=\sum_n w_n^2(1-\eta_n^2)+m^2=:V<\infty. \tag{2}
\]

There is also a direct uniform exponential-moment proof. For a single leaf,
the second derivative of its conditional log MGF is a tilted two-point
variance, at most `w_n^2`. Its centered log MGF is therefore at most
`t^2w_n^2/2`. Conditional independence gives

\[
 E e^{tX_N}\le\exp\left(|t|m+\tfrac12t^2\sum_nw_n^2\right). \tag{3}
\]

The corresponding complex bound uses `t=|Im z|` and gives local uniform
boundedness on the whole plane. The limit of the finite characteristic
functions is entire by Montel and agrees with the probability limit on
the real line. Finite Lee--Yang plus Hurwitz puts all its zeros on the
real axis. Thus (1) is a genuine growth-controlled infinite construction,
not the uncontrolled wall encoding of COFINAL_WALL_CONSTRUCTION.md.

Its complete characteristic function and MGF are

\[
 f(z)=\tfrac12\prod_n[\cos(w_nz)+i\eta_n\sin(w_nz)]
     +\tfrac12\prod_n[\cos(w_nz)-i\eta_n\sin(w_nz)], \tag{4}
\]
\[
 Ee^{tX}=\tfrac12 e^{L_J(t)}+\tfrac12 e^{L_{-J}(t)},\qquad
 L_J(t)=\sum_n\log\frac{\cosh(tw_n+J_n)}{\cosh J_n}. \tag{5}
\]

Products converge locally uniformly because their logarithms have linear
terms controlled by (1) and quadratic remainders controlled by sum w_n^2.
Individual permanent cosine factors need not occur when all eta_n>0.
The open completion question is equality of this entire law with the
actual theta law, not compactness of the candidate class.

## 2. The fair harmonic product has no inverse-power asymptotic terms

Let

\[
 L(t)=\sum_{n=0}^{\infty}\log\cosh\frac{t}{2(n+a)}.
\]

For every integer `N`, there are constants `C_a,D_a` such that, as
`t` tends to positive infinity,

\[
 L(t)=\tfrac12t\log t+C_at+D_a+O_N(t^{-N}). \tag{6}
\]

Here is a full reason the inverse powers are absent. Termwise twice
differentiation is justified by sum w_n^2, and

\[
 L''(t)=t^{-2}\sum_{n=0}^{\infty}F((n+a)/t),\quad
 F(x)=\frac1{4x^2}\operatorname{sech}^2\frac1{2x}. \tag{7}
\]

Extend F by zero at zero. It is smooth and flat there; at infinity its
k-th derivative is O(x^(-2-k)). Every derivative is integrable. The
shifted Euler--Maclaurin formula therefore has zero boundary terms of
every order. Its remainder at order 2k is bounded by
`C_(a,k) t^(-2k-1) integral_0^infinity |F^(2k)(x)| dx`.
If a>1, reduce its fractional part and remove finitely many terms; these
removed values are exponentially small as t grows. Finally

\[
 \int_0^\infty F(x)\,dx
  =\tfrac12\int_0^\infty\operatorname{sech}^2u\,du=\tfrac12.
\]

Consequently `L''(t)=1/(2t)+O_N(t^(-N))` for every N. Integrating its
integrable remainder twice proves (6), with potentially different fixed
constants. Any finite alteration of positive fair-spin weights adds only
a linear term, a constant and exponentially small terms; (6) remains true.

## 3. Global cosh tilt fails the actual theta asymptotic

Choose `J_n=h w_n`, with `h>=0`. This is exactly the cosh(hX)-tilt of
the fair harmonic series. Its symmetric MGF is

\[
 M_h(t)=\frac{e^{L(t+h)}+e^{L(t-h)}}{2e^{L(h)}}. \tag{8}
\]

For h>0, (6) gives

\[
 \log M_h(t)=\tfrac12t\log t+C_at+\tfrac h2\log t+D_{a,h}
       +\frac{h^2}{4t}+O(t^{-2})+O(t^{-h}). \tag{9}
\]

Indeed the ratio of the second branch to the first is
`exp[-h log t-2h(C_a+1/2)+O(t^(-2))]`. For h=0 the log t coefficient
is zero and (6) applies directly.

The actual normalized original theta MGF is
`M_theta(t)=xi(1/2+t)/xi(1/2)`. The elementary Stirling expansion gives

\[
 \boxed{\log M_\theta(t)
 =\tfrac12t\log t-\tfrac12[1+\log(2\pi)]t
       +\tfrac74\log t+D_\theta-\frac1{48t}+O(t^{-2}).} \tag{10}
\]

To pin every term: write
`xi(s)=s(s-1) pi^(-s/2) Gamma(s/2) zeta(s)/2`, `s=t+1/2`.
The factor s(s-1)=t^2-1/4 contributes `2 log t+O(t^(-2))`.
For Gamma use z=t/2 and shift 1/4. Its log t coefficient is -1/4,
and its inverse-t coefficient is
`B_2(1/4)/t=-1/(48t)`, since B_2(x)=x^2-x+1/6.
The zeta factor has exponentially small logarithm as t grows.

Equality with (9) would force `h=7/2`. The second branch is then
O(t^(-7/2)), smaller than 1/t, whereas (9) predicts

\[
 \frac{h^2}4=\frac{49}{16}>0
 \quad\hbox{in place of}\quad -\frac1{48}<0. \tag{11}
\]

This is a strict contradiction. It is independent of a, finite fair-head
changes, the constants C,D, or numerical moment fits.

The same sign obstruction holds for a finite positive mixture of fixed
global shifts `sum_j c_j exp L(t+h_j)`, `c_j>0`: the largest shift
determines the logarithmic coefficient, its own 1/t correction is
positive, and all lower-shift contributions are nonnegative. Such a
mixture cannot create the negative 1/t term in (10). An independent
finite-support head changes only the leading linear term and constant.

## 4. A nonconstant positive profile repairs the first mismatch

The obstruction does not exclude general J_n. For example, choose

\[
 J_n=h w_n+k w_n^2,\qquad h>1,\ k\ge0. \tag{12}
\]

This obeys (1) and keeps every star edge positive. Direct summation gives

\[
 L_J(t)=\tfrac12t\log t+C_at+\tfrac h2\log t+D_{a,h,k}
 +\frac{h^2/4-(k/2)\log2}{t}+O(t^{-2}). \tag{13}
\]

For completeness, expand log cosh(tw+J) about tw. The h-linear term is
h L'(t), and the k-linear term is k sum w_n^2 tanh(tw_n).
Applying the same shifted summation to the smooth flat function
`(1-tanh(1/(2x)))/(4x^2)` gives

\[
 \sum_n w_n^2[1-\tanh(tw_n)]
       =\frac{\log2}{2t}+O_N(t^{-N}). \tag{14}
\]

Its integral is `(1/2) integral_0^infinity(1-tanh u)du=(log2)/2`.
The quadratic h^2 term is `(h^2/2)L''(t)=h^2/(4t)+O_N(t^(-N))`.
The remaining quadratic cross terms and cubic remainder are O(t^(-2)):
after deleting finitely many head terms, their absolute values are
bounded by constants times sums `w_n^3 exp(-c t w_n)`, which are O(t^(-2))
by comparison with the corresponding scaled integral. Deleted terms are
exponentially small; their limiting constants were already included in D.
The opposite hub branch has relative size O(t^(-h)), as before.

With h=7/2, the exact positive choice

\[
 \boxed{k=\frac{h^2/2+1/24}{\log2}
          =\frac{37}{6\log2}} \tag{15}
\]

changes the inverse-t coefficient in (13) to -1/48, agreeing with the
actual theta value. This is an actual analytic repair of one asymptotic
coefficient inside a growth-controlled real-zero class. It establishes
neither full-function equality nor the remaining infinitely many
coefficients, constants or arithmetic remainder. Those are the precise
completion tasks, rather than another list of finite moments.

## 5. Every smooth integer-power profile with an unobserved hub is obstructed

There is a second, stronger obstruction. Assume the unobserved fair hub
in (4)--(5) still has observable weight zero. Suppose, for some h>0,
the coupling sequence has a complete integer-power asymptotic expansion

\[
 J_n=h w_n+j_2w_n^2+j_3w_n^3+\cdots,
 \tag{16}
\]

meaning that for every m its remainder after degree m is O(w_n^(m+1)).
Every function J(w) smooth at zero with J(0)=0 and J'(0)=h meets this
condition. Arbitrary finite changes of weights or couplings are allowed.
Then this infinite-star law **cannot equal the actual theta law**.

Here is the full asymptotic justification. For either sign of J,
Taylor-expand log cosh(tw+J) about tw. Its linear term splits as

\[
 hL'(t)+\sum_n(J_n-hw_n)
       -\sum_n(J_n-hw_n)[1-\tanh(tw_n)]. \tag{17}
\]

The middle sum converges. Expand the last sum with (16). At higher
Taylor orders m>=2, expand J_n^m in integer powers of w_n. Each resulting
nonconstant summand has the form `w_n^r g(tw_n)`, r>=2, where g is a
derivative of log cosh of order at least two, or g=1-tanh. These g decay
exponentially at positive infinity. Shifted summation gives

\[
 \sum_nw_n^r g(tw_n)
 =\frac{t^{1-r}}2\int_0^\infty u^{r-2}g(u)\,du+O_N(t^{-N}). \tag{18}
\]

The scaled summand is smooth and flat at its zero endpoint, and all its
derivatives are integrable; this is the same Euler--Maclaurin argument
as (7). For a specified finite target order, Taylor remainders are
bounded by sums `C w_n^r exp(-c t w_n)=O(t^(1-r))`. Finitely many head
terms contribute constants and exponentially small terms only. Thus for
every fixed m,

\[
 L_{\pm J}(t)=\tfrac12t\log t+C_at
       \mathbin{\pm}\tfrac h2\log t+D_\pm
       +\sum_{r=1}^{m}c_r^\pm t^{-r}+O(t^{-m-1}). \tag{19}
\]

In particular

\[
 e^{L_{-J}(t)-L_J(t)}
   =A t^{-h}(1+O(t^{-1})),\qquad A=e^{D_--D_+}>0. \tag{20}
\]

Matching the actual log t coefficient still forces h=7/2. Expanding the
logarithm of the sum in (5), through order strictly below four, then gives

\[
 \log Ee^{tX}
 =\tfrac12t\log t+C_at+\tfrac74\log t+D
       +c_1t^{-1}+c_2t^{-2}+c_3t^{-3}
       +A t^{-7/2}+O(t^{-4}),\quad A>0. \tag{21}
\]

The actual xi Stirling expansion has only integer inverse powers, with
remainder O(t^(-4)) after its inverse-cubic term. If any coefficient in
(21) disagrees, equality already fails. If all displayed integer
coefficients agree, multiplying the remaining difference by t^(7/2)
gives A>0, whereas the target gives zero. This proves the obstruction.
It does not rely on the size, sign or computability of j_2,j_3,... .

The integer coefficients by themselves do not supply the obstruction:
they are formally flexible. A new j_r, r>=2, first changes the
t^(1-r) coefficient by

\[
 -\frac{j_r}{2}I_r,\qquad
 I_r=\int_0^\infty u^{r-2}(1-\tanh u)\,du>0. \tag{22}
\]

All its nonlinear interactions enter later inverse powers. Therefore
these coefficients can be chosen recursively to match any prescribed
finite list of integer Stirling coefficients. I_2=log2; for r>2,
`I_r=2^(2-r)(1-2^(2-r)) Gamma(r-1) zeta(r-1)`. Formula (21), rather
than failure of an integer-coefficient fit, is the decisive obstruction.

## 6. What an escape must change

There are two explicit ways outside the last theorem; neither has been
completed for the actual theta law.

First, a coupling profile containing a term of order w^(9/2) produces a
term of order t^(-7/2) in its dominant branch by (22), with the integral
defined at r=9/2. It could cancel the opposite-branch term in (21).
Such a profile is outside the smooth integer-jet premise. Positivity
near zero does not forbid this correction, since h w dominates it.
Further fractional orders and the exact whole-function remainder would
still need control.

Second, give the hub a fixed positive observable weight B. Formula (5)
becomes

\[
 Ee^{tX_B}=\tfrac12e^{Bt+L_J(t)}
              +\tfrac12e^{-Bt+L_{-J}(t)}. \tag{23}
\]

This is still a symmetric zero-field ferromagnetic star observable. Its
entire convergence and growth follow from (3), with m replaced by m+B.
The ratio (20) now has the extra factor exp(-2Bt), so the troublesome
fractional term disappears beyond every integer inverse-power order.
The hub adds no independent Gaussian factor and does not produce a
permanent independent cosine factor. Its variance becomes
`sum w_n^2(1-eta_n^2)+(m+B)^2`.

This identifies a precise surviving class: a harmonic tail with a
nonconstant positive coupling profile and an observed hub, or a
noninteger profile with zero hub weight. Proving an identity with the
actual theta MGF, including its constants and complete arithmetic
remainder, remains open. Matching the leading tail or every formal
inverse-power coefficient alone would not prove such an identity.

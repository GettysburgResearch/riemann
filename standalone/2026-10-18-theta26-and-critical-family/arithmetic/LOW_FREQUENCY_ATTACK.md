# The retained zeta multiplier passes a quadratic logarithmic packet

## Result and scope

This focused continuation asks whether the actual zeta multiplier, its causal
singular support, physical square-step restriction, and exact removal of the
two smooth balance coordinates can themselves turn the native quadratic
energy cost into a subquadratic one.

**The answer for that information alone is no.** The theorem below constructs
bounded, squarefree-supported old coefficients with both balance coordinates
exactly zero, prescribed old energy of size `Y^kappa`, and retained physical
output of size `Y^(2 kappa)` in squared norm. It retains the actual multiplier
`zeta(s)/(s-1)`, every product in the old convolution, and the exact physical
window. The conclusion holds for every growing input-frequency cutoff,
including the proved native cutoff `Y^(84/71)`.

These coefficients are not the Möbius coefficients. In particular they do
not satisfy the exact old-prefix convolution identity `1*mu=delta`. The result
is an obstruction to upper estimates that use only the stated spectral,
support, size, energy, and balance information. It is **not** an impossibility
theorem for an arithmetic estimate of the actual Möbius input, and it does not
assert the native Newton identity for the constructed coefficients.

The point is to locate the missing use of arithmetic precisely. The earliest
singular component of the actual zeta multiplier preserves this packet rather
than cancelling it. Additional cancellation must use more than the inputs
retained by this construction.

## 1. Exact operator and theorem

Let `a_Y(n)` be real coefficients supported on `1<=n<=Y`, and define

\[
 m_{a,Y}(x)=\sum_{n\le x}\frac{a_Y(n)}n,\qquad
 E_Y(a)=\sum_{k\le Y}|m_{a,Y}(k)|^2,
 \qquad D_{a,Y}(s)=\sum_{n\le Y}a_Y(n)n^{-s}.
\]

Set `M_Y(a)=m_(a,Y)(Y)` and

\[
 B_Y(a)=1+\sum_{n\le Y}\frac{a_Y(n)\log n}{n}
                -(\log Y+\gamma/2)M_Y(a).
\]

The convolution coefficients are `z_a=a_Y*a_Y`. With the same full kernel
as the native source,

\[
 R(x)=H_{\lfloor x\rfloor}-\log x-\gamma,\qquad
 A_a(u)=e^{u/2}\sum_{d\le Y^2}\frac{z_a(d)}dR(e^u/d),
\]

the exact Mellin identity is

\[
 \widehat A_a(t)=\Phi_a(t)
 =\frac{\zeta(1/2+it)D_{a,Y}(1/2+it)^2}{-1/2+it}.       \tag{1.1}
\]

This identity holds for every finite input; it uses no Möbius inversion. In
particular no product with `d>e^u` is deleted. Fourier conventions are
`fhat(t)=int f(u) exp(-itu)du`, with inverse factor `1/(2 pi)`.

For `T>0`, let

\[
 A_{a,\le T}=\mathcal F^{-1}[\mathbf1_{[-T,T]}\Phi_a],
 \qquad W_Y=\mathbf1_{[\log(Y+1),\,2\log(Y+1))}.
\]

### Theorem L: a sharp retained-window packet

Fix `0<kappa<1`. There are coefficient arrays `a_Y`, for all sufficiently
large integer `Y`, satisfying

\[
 a_Y(1)=1,\qquad |a_Y(n)|\le1,\qquad
 a_Y(n)=0\ \text{if }n\text{ is not squarefree},
 \qquad M_Y(a)=B_Y(a)=0,                               \tag{1.2}
\]

and positive constants `c_E,c_A` such that

\[
 E_Y(a)\sim c_EY^\kappa,
 \qquad
 \|W_YA_{a,\le T_Y}\|_2^2\sim c_AY^{2\kappa}            \tag{1.3}
\]

for **every** sequence `T_Y->infinity`. The same conclusion holds with no
frequency truncation. The coefficients also have `m_(a,Y)(Y-1)=0`.

For each fixed `T>0`, a separate positive constant `c_(A,T)` gives

\[
 \|W_YA_{a,\le T}\|_2^2\sim c_{A,T}Y^{2\kappa}.         \tag{1.4}
\]

Consequently a uniform upper estimate for this class of the form

\[
 \|W_YA_{a,\le T_Y}\|_2^2
       \ll_\varepsilon Y^{\alpha+\varepsilon}
                              (1+E_Y(a))^p             \tag{1.5}
\]

requires `alpha >= (2-p) kappa`. In particular `p=3/2, alpha=1/3` fails for
every chosen `kappa>2/3`. This applies to the spectral estimate (1.5), not to
a recurrence for the true Möbius energy.

## 2. A smooth logarithmic packet with squarefree support

Choose constants `0<c<d<1` with

\[
                 2\log(d/c)<\log2;                   \tag{2.1}
\]

for example `c=1/4, d=1/3`. Let `f` be a fixed nonnegative, nonzero smooth
function compactly supported in `(log c,log d)`. Put

\[
 L=\log Y,\qquad A=Y^{\kappa/2},\qquad
 h_Y(x)=A x^{-1/2}f(\log(x/Y)),                         \tag{2.2}
\]

extended by zero outside its indicated support. On its support and a small
surrounding interval,

\[
 |h_Y(x)|\ll A Y^{-1/2},\qquad
 |h_Y'(x)|\ll A Y^{-3/2}.                              \tag{2.3}
\]

Here is a deterministic interpolation that preserves squarefree support.
Let `H=ceil(100 sqrt(Y))` and partition the integer prefix into full blocks
`(jH,(j+1)H]`, followed by a possible final incomplete block. On a full block
`I_j=(n_(j-1),n_j]`, set

\[
 S_j=\sum_{n\in I_j}\frac{\mu(n)^2}{n},\qquad
 u_j=\frac{h_Y(n_j)-h_Y(n_{j-1})}{S_j},\qquad
 a_Y^{\rm pkt}(n)=u_j\mu(n)^2.                         \tag{2.4}
\]

If both target endpoints vanish and `S_j=0`, set `u_j=0`. Set coefficients
in the final incomplete block to zero. For large `Y` it is disjoint from
the support of `h_Y`.

The elementary squarefree count is

\[
 \sum_{n\le x}\mu(n)^2=\frac6{\pi^2}x+O(\sqrt x).      \tag{2.5}
\]

For clarity, it follows by expanding
`mu(n)^2=sum_(r^2|n)mu(r)`, replacing each floor by its argument, and bounding
both the floor errors and the tail of `sum mu(r)/r^2` absolutely. One can
take an error at most `3 sqrt(x)` for `x>=4`. Thus each relevant full block
contains at least `H/2-6 sqrt(Y)>=0.44 H` squarefree integers. In particular

\[
 S_j\gg H/Y,
 \qquad |u_j|\ll A Y^{-1/2}=Y^{(\kappa-1)/2}.          \tag{2.6}
\]

The last expression tends to zero, so these coefficients are bounded by one.
This construction uses the squarefree support but leaves its signs free.

Let `m_Y^pkt(n)=sum_(r<=n)a_Y^pkt(r)/r`. At every full-block endpoint it
equals `h_Y(n_j)`, exactly. Inside a block it is a convex interpolation of
the endpoint values with positive weights `mu(n)^2/n`. By (2.3),

\[
 \sup_{x\ge1}|m_Y^{\rm pkt}(x)-h_Y(x)|\ll A/Y,         \tag{2.7}
\]

where the step function on the left uses the ordinary floor convention.
Its support lies in `[cY-H,dY+H]`. It is nonnegative, and is zero at both
`Y` and `Y-1` for large `Y`.

Define

\[
 f_Y(v)=A^{-1}e^{(L+v)/2}m_Y^{\rm pkt}(e^{L+v}).
\]

These functions have support in one fixed compact interval, and (2.7) gives

\[
 \|f_Y-f\|_1+\|f_Y-f\|_2+\|f_Y-f\|_\infty
                         \ll Y^{-1/2}.                \tag{2.8}
\]

In particular their Fourier transforms differ by `O(Y^(-1/2))` uniformly
on the entire real frequency line. Changing variables gives the exact packet
energy relation

\[
 A^{-2}\sum_{k\le Y}|m_Y^{\rm pkt}(k)|^2
 =\|f_Y\|_2^2\longrightarrow\|f\|_2^2>0.             \tag{2.9}
\]

The equality uses unit cells; the packet is zero near the upper endpoint.

## 3. Kill both smooth balance coordinates exactly

The packet already has `M_Y=0`. Let

\[
 L_Y^{\rm pkt}=\sum_{n\le Y}
                    \frac{a_Y^{\rm pkt}(n)\log n}{n}.
\]

Discrete partial summation and the zero endpoint give

\[
 L_Y^{\rm pkt}
 =-\sum_{n<Y}m_Y^{\rm pkt}(n)\log(1+1/n)
 =O(A Y^{-1/2}),\qquad L_Y^{\rm pkt}\le0.              \tag{3.1}
\]

Use two fixed small prefixes, both normalized to have first coefficient one
and supported on squarefree integers. The first is

\[
 a^-(1)=1,\quad a^-(2)=a^-(3)=-1,\quad a^-(5)=-\frac56.
\]

It has zero reciprocal sum and logarithmic moment `-J_-`, where

\[
 J_- =\frac{\log2}{2}+\frac{\log3}{3}+\frac{\log5}{6}
     =\frac{\log360}{6}<1.
\]

For example `e>27/10` from its positive series and `(27/10)^6>360`
verify the strict inequality with rational arithmetic.

The second prefix is

\[
 a^+(1)=1,\quad a^+(n)=-1\quad(n=3,5,6,7,10),\quad
 a^+(11)=-\frac{22}{35}.
\]

Its reciprocal weights satisfy

\[
 \frac13+\frac15+\frac16+\frac17+\frac1{10}+\frac2{35}=1.
\]

Thus it also has zero reciprocal sum. Its logarithmic moment is `-J_+`, where

\[
 J_+=\frac{\log3}{3}+\frac{\log5}{5}+\frac{\log6}{6}
   +\frac{\log7}{7}+\frac{\log10}{10}+\frac{2\log11}{35}>1.
\]

The inequality holds because the positive reciprocal weights sum to one and
all their logarithms exceed one. For large `Y`, (3.1) gives
`J_-<1+L_Y^pkt<J_+`. Define the convex mixture

\[
 \tau_Y=\frac{1+L_Y^{\rm pkt}-J_-}{J_+-J_-}\in(0,1),
 \qquad a_Y^{\rm base}=(1-\tau_Y)a^-+\tau_Ya^+.        \tag{3.2}
\]

It has first coefficient one, all coefficient magnitudes at most one,
squarefree support, zero reciprocal sum, and logarithmic moment
`-(1+L_Y^pkt)`.

The base and packet supports are disjoint. Set
`a_Y=a_Y^base+a_Y^pkt`. Every coefficient has size at most one and squarefree
support, and

\[
 M_Y(a)=0,\qquad
 B_Y(a)=1-(1+L_Y^{\rm pkt})+L_Y^{\rm pkt}=0.           \tag{3.3}
\]

exactly. The fixed prefix adds only `O(1)` to the old energy, so (2.9)
proves the first asymptotic in (1.3), with `c_E=||f||_2^2`.

This also removes the native-looking smooth term
`2 M_Y B_Y+M_Y^2 log(Y^2/x)` identically. No estimate of that term can
remove the output constructed below.

## 4. The precise limiting spectral amplitude

At `s=1/2+it`, partial summation with the zero packet endpoint gives

\[
 D_Y^{\rm pkt}(s)
  =(s-1)\int_1^Y m_Y^{\rm pkt}(x)x^{-s}\,dx
  =A e^{-itL}(s-1)\widehat f_Y(t).                    \tag{4.1}
\]

Its normalized quadratic spectral amplitude is therefore

\[
 A^{-2}e^{2itL}\Phi_Y^{\rm pkt}(t)
       =\zeta(s)(s-1)\widehat f_Y(t)^2.
\]

The expected limit is the actual, signed multiplier

\[
                \Psi_f(t)=\zeta(s)(s-1)\widehat f(t)^2. \tag{4.2}
\]

On every fixed compact frequency interval, convergence follows at once from
(2.8). The next section proves full `L^2` convergence; this is necessary to
exclude cancellation by the other retained frequencies after physical
restriction.

## 5. Full spectral convergence, including all growing cutoffs

Use the published `theta=13/84` bound for `zeta(1/2+it)` and the elementary
finite-polynomial moments already proved in
[NATIVE_FREQUENCY_TAIL.md](NATIVE_FREQUENCY_TAIL.md), Sections 2--3. Their
proof uses only coefficient size. If `|a(n)|<=eta`, homogeneity gives

\[
 \int_{|t|>K}
 \left|\frac{\zeta(s)D_Y(s)^2}{s-1}\right|^2dt
 \ll_\varepsilon \eta^4(YK)^\varepsilon
                         K^{-71/42}(K+Y^2).            \tag{5.1}
\]

For the packet, (2.6) allows `eta<<A/sqrt(Y)`. Dividing (5.1) by `A^4`
therefore gives

\[
 \int_{|t|>K}|A^{-2}\Phi_Y^{\rm pkt}(t)|^2dt
 \ll_\varepsilon(YK)^\varepsilon K^{-71/42}(1+K/Y^2).
                                                               \tag{5.2}
\]

Take `K=Y^(1/4)` and assign a sufficiently small preliminary epsilon.
The right side tends to zero.

On `|t|<=K`, write `fhat_Y=fhat+e_Y`, with
`|e_Y(t)|<<Y^(-1/2)`. The transform of the fixed smooth function decays
faster than every power. The squared norm of the term linear in `e_Y` is
`O(Y^(-1))`, since
`int |zeta(s)(s-1) fhat(t)|^2 dt` is finite. The term quadratic in `e_Y`
has squared norm

\[
 \ll_\varepsilon Y^{-2}K^{3+2\theta+\varepsilon}
 =Y^{-197/168+o(1)}\longrightarrow0.                  \tag{5.3}
\]

The target (4.2) has a vanishing `L^2` tail as `K` increases. Equations
(5.2)--(5.3) prove

\[
 A^{-2}e^{2itL}\Phi_Y^{\rm pkt}\longrightarrow\Psi_f
                                      \quad\text{in }L^2(\mathbb R).
                                                               \tag{5.4}
\]

The fixed base does not affect this limit. Indeed its Dirichlet polynomial
is bounded by a constant on the entire critical line. For the cross term,
the `j=1` polynomial moment, with the same coefficient factor `eta`, gives

\[
 \int_\mathbb R
       \frac{|\zeta(s)|^2|D_Y^{\rm pkt}(s)|^2}{|s-1|^2}\,dt
                 \ll_\varepsilon \eta^2Y^{1+\varepsilon}
                 \ll_\varepsilon A^2Y^\varepsilon.    \tag{5.5}
\]

To verify this directly, bound a dyad `U<|t|<=2U`, `U>=1`, by
`eta^2(YU)^epsilon U^(-71/42)(U+Y)` and sum the two convergent geometric
series. The compact interval is bounded using the same moment estimate.
After normalization by `A^4`, (5.5) tends to zero when epsilon is chosen
below kappa. The pure base term has bounded squared norm because
`2 theta-2<-1`; division by `A^4` again makes it vanish.

Consequently (5.4) holds with the full `Phi_a`. For any `T_Y->infinity`,
it also holds after multiplying the left side by `1_(|t|<=T_Y)`:
orthogonal projection is contractive and the corresponding tail of the
fixed limit tends to zero. No unsupported passage from a fixed frequency
sector to the full physical output is used.

## 6. The causal singular support does not cancel the first packet

Let `g=f*f`, and write

\[
                         k_f=\mathcal F^{-1}\Psi_f.
\]

The limiting kernel is especially transparent in physical coordinates.
Define `r(u)=e^(u/2)R(e^u)`, so that
`rhat(t)=zeta(s)/(s-1)`. The differential operator `D-1/2`, where
`D=d/du`, has Fourier multiplier `s-1`. Thus, as distributions,

\[
 (D-\tfrac12)^2r
   =\sum_{n\ge1}n^{-1/2}
           [\delta'(u-\log n)-\tfrac12\delta(u-\log n)].
                                                               \tag{6.1}
\]

This can be checked locally without manipulating a divergent series.
Writing `r=e^(u/2)[H_(floor(e^u))-u-gamma]`, two applications of `D-1/2`
differentiate the bracket twice. The first derivative of its staircase
is `sum_n (1/n) delta(u-log n)`; the second derivative and multiplication
by `e^(u/2)` give (6.1). The sum is locally finite and identifies the
distribution globally with the derivatives of `r`, which is in `L^2`.
The displayed series is first interpreted in `D'` against compactly
supported test functions. Its tempered distribution and Fourier meaning
come from the left side; a termwise sum against arbitrary Schwartz test
functions is not asserted and can fail to converge.

Convolving with the compact smooth `g` gives the exact expression

\[
 k_f(v)=\sum_{n\ge1}n^{-1/2}
          [g'(v-\log n)-\tfrac12g(v-\log n)].          \tag{6.2}
\]

For each finite `v` this is a finite sum. Since `g` is supported in
`(2 log c,2 log d)`, the separation condition (2.1) ensures that no term
with `n>=2` contributes anywhere on that interval. It is entirely negative,
and there

\[
                         k_f(v)=g'(v)-\tfrac12g(v).
\]

Therefore

\[
 \int_{-\infty}^0|k_f(v)|^2\,dv
 \ge\int_{2\log c}^{2\log d}|g'(v)-\tfrac12g(v)|^2\,dv
 =\|g'\|_2^2+\tfrac14\|g\|_2^2>0.                   \tag{6.3}
\]

The mixed integral is zero by integration by parts. The actual zeta
multiplier has preserved a nonzero first component. It has not been
replaced by an absolute-value majorant in this argument.

## 7. The literal physical window and final asymptotics

Plancherel applied to (5.4) gives

\[
 A^{-2}A_{a,\le T_Y}(2\log Y+v)
                         \longrightarrow k_f(v)
                         \quad\text{in }L^2(\mathbb R).
                                                               \tag{7.1}
\]

After the same translation, the physical square-step window is

\[
 [-\log Y+\log(1+1/Y),\,2\log(1+1/Y)).
\]

Its indicators tend pointwise to `1_(-infinity,0)`. Since multiplication
by any such indicator is an `L^2` contraction, (7.1) and dominated
convergence imply

\[
 A^{-4}\|W_YA_{a,\le T_Y}\|_2^2
       \longrightarrow\int_{-\infty}^0|k_f(v)|^2\,dv>0.
                                                               \tag{7.2}
\]

This proves (1.3), including its growing-cutoff assertion. For fixed `T`,
the limit is instead the inverse transform of `1_[-T,T] Psi_f`. This is
a nonzero bandlimited entire function: `fhat` and the zeta factor cannot
vanish identically on that interval. It cannot vanish on the whole negative
half-line without being identically zero. Its retained squared norm is
therefore positive, proving (1.4).

Finally, comparing the powers in (1.3) with (1.5), and then taking epsilon
arbitrarily small, proves `alpha >= (2-p) kappa`.

## 8. Consequence for the arithmetic attack

The theorem has kept the actual zeta multiplier, its signed initial impulse,
all old products, squarefree support, a vanishing endpoint, the second
balance equation, the full physical window, and the other retained
frequencies. Those facts permit a coherent packet with exactly quadratic
energy growth. Removing the smooth component does not change it.

The construction deliberately leaves free the signs and magnitudes on the
squarefree support. It fails the complete Möbius identities

\[
                    \sum_{d\mid n}a_Y(d)=\mathbf1_{n=1}
                    \qquad(n\le Y).
\]

Those identities uniquely force the actual old prefix. A useful next
arithmetic estimate must exploit their effect on this coherent spectral
configuration, or exploit another property equally specific to the target.
The present counterexample does not decide whether that extra structure
gives a contraction. It proves that the spectral and balancing mechanisms
examined in this pass do not supply one by themselves.

# Stationary horizontal minima and critical-value conservation

Date: 2026-08-23  
Programme: Xi reverse Rolle, fixed-order `Xi''' -> Xi''`  
Controlling theorem: `T-104580`  
RH status: **unproved**

## 1. Radical change of target

The modular routes `MSINE104570` and `ACDM104570` seek the global inequality

\[
\mathcal L_2(t)=\Xi'''(t)^2-\Xi''(t)\Xi''''(t)\ge0
\quad(t\in\mathbb R).
\]

The fixed-order Conrey descent does not require a sign at every ordinate.  It
requires the sign only at the real zeros of `Xi'''` supplied by the known
third-derivative theorem.

The complete positive source is

\[
g(u)=u^2\Phi(u),
\qquad
\mathscr Z(z)=\int_{\mathbb R}g(u)e^{zu}\,du.
\]

Then

\[
\mathscr Z(it)=-\Xi''(t)
\]

and

\[
\mathscr Z\mathscr Z''-(\mathscr Z')^2
\big|_{z=it}
=\mathcal L_2(t).
\]

For

\[
Q_t(h)=|\mathscr Z(h+it)|^2=|\Xi''(t-ih)|^2,
\]

one has

\[
Q_t''(0)=2\mathcal L_2(t).
\]

Thus a real zero `c` of `Xi'''` is Rolle-generating for `Xi''` exactly when
`h=0` is a horizontal modulus minimum of `Xi''(c-ih)`.

This converts a global positive-definiteness problem into a critical-set
sampling problem in the same horizontal-shift coordinate used by
Levinson--Conrey mollifiers.

## 2. Exact partition-function facts

On the real exponential-family axis,

\[
\mathscr Z(x)\mathscr Z''(x)-\mathscr Z'(x)^2
=\mathscr Z(x)^2\operatorname{Var}_{\mu_x}(U)>0.
\]

More strongly, if `W` has nonnegative Fourier transform, then for every real
`h`,

\[
\int W(t)
\left[
 |\mathscr Z(h+it)|^2-|\mathscr Z(it)|^2
\right]dt\ge0.
\]

The proof is a coefficient-one source identity:

\[
\iint g(u)g(v)
[\cosh(h(u+v))-1]
\widehat W(u-v)\,du\,dv\ge0.
\]

This retains the full finite horizontal shift before taking an infinitesimal
limit.

The exact positive atom source

\[
\mathscr Z(z)=\cosh z+\frac12\cosh2z
\]

shows the missing interface.  Its real-axis variance is positive, but at the
stationary imaginary point `z=i pi`,

\[
\mathscr Z=-\frac12,
\quad
\mathscr Z'=0,
\quad
\mathscr Z''=1,
\]

so the determinant equals `-1/2`.  Real-axis log-convexity and bulk positive
averages do not automatically sample individual critical points.

## 3. Exact fixed-order conversion

If a lower density `q` of the real `Xi'''` zeros is horizontally minimizing,
then exact factor-two reverse Rolle gives

\[
\alpha_2\ge(2q-1)\alpha_3.
\]

Using Conrey's `alpha_3>0.9873`:

```text
q >= 3/4   -> alpha_2 > 0.49365;
q >= 9/10  -> alpha_2 > 0.78984;
q = 1      -> alpha_2 >= alpha_3 > 0.9873.
```

No independent `alpha_2` theorem enters these implications.

The finite-shift version is fail-closed: for each fixed height one first sends
`h` to zero.  A simultaneous `h(T)` requires uniform Taylor control and a
small-curvature sparsity theorem.

## 4. Unconditional critical-value weighted majority

For an arbitrary real `C^2` function, monotone-interval variation gives

\[
\sum_{f'(c)=0}-f(c)\operatorname{sgn}f''(c)
={1\over2}
\left[
 \int|f'|+\text{two explicit endpoint terms}
\right].
\]

For `f=Xi''`, the endpoints vanish at infinity and therefore

\[
\sum_{\rm good}|\Xi''(c)|
-
\sum_{\rm wrong}|\Xi''(c)|
={1\over2}\int_{\mathbb R}|\Xi'''(t)|dt>0.
\]

This proves unconditionally that the good extrema carry strictly more than
half of the complete critical-value amplitude mass.  A layer-cake argument
also gives at least one amplitude threshold on which good critical points
outnumber wrong ones.

The theorem is weighted; the selected threshold need not yet contain a
positive density of Conrey's line zeros.

## 5. Exact amplitude-to-count conversion

Let `rho_T` be the normalized signed amplitude bias and let `v_T` be the
coefficient of variation of the amplitudes `|Xi''(c)|` at the real zeros of
`Xi'''`.  Cauchy--Schwarz gives

\[
{G_T\over R_3(T)}
\ge {1\over2}+{\rho_T-v_T\over2}.
\]

Thus

\[
\liminf(\rho_T-v_T)\ge\eta>0
\quad\Longrightarrow\quad
\alpha_2\ge\eta\alpha_3>0.9873\eta.
\]

This is a two-moment target on actual critical values.  It is independent of
the inverse-curvature residue-coherence target `RCMV104530`.

## 6. Correct remaining routes

```text
SHMIN104580
  Prove a horizontally minimizing density q>1/2 directly, using shifted
  derivative moments at real Xi''' zeros.

CSAMP104580
  Transfer the complete positive-Fourier bulk finite-shift theorem to the
  critical-point measure with loss <1/2.

AMPREG104580
  Prove liminf(rho_T-v_T)>0 for the critical values |Xi''(c)|.
```

Any one of `SHMIN104580` or `AMPREG104580` gives a direct positive `Xi''`
proportion from Conrey's `Xi'''` theorem.  `CSAMP104580` is a structural route
to `SHMIN104580`.

## 7. Scientific boundary

```text
partition-function determinant             proved exact
bulk finite-shift positivity                proved exact
critical horizontal-minimum conversion      proved exact
critical-value weighted majority            proved unconditionally
amplitude-to-count algebra                  proved exact
stationary sampling                         open
critical-value amplitude regularity         open
alpha_2 from alpha_3                        not yet established
Riemann Hypothesis                          unproved
```

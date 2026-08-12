# L-91406 — The Green-removal density has a monotone ballistic energy

Claim ID: `L-91406`  
Status: **EXACT DYNAMICAL NORMAL FORM AND SLOPE-WITNESS THEOREM**  
Created: 2026-08-12  
Depends on: PR #396 notation and positivity of the all-Green discrepancy `E_{s,0}`  
RH status: **unproved**

## 1. Arithmetic kicks and free flight

Fix `a>0`, put

\[
 s=2a,
 \qquad
 c=c_s=\zeta(1+s)^{-1},
 \qquad
 \kappa=\sqrt{275/14},
\]

and

\[
 f_n=\frac{F_s(n)}n,
 \qquad
 F_s(n)=\prod_{p\mid n}(1-p^{-s}).
\]

Let

\[
 E_0(t)=\sum_{\log n\le t}f_n-ct,
\]

\[
 E_1(t)=\sum_{\log n\le t}f_n(t-\log n)-\frac{ct^2}{2},
\]

and retain the final Green-removal density

\[
 \boxed{
 B(t)=-c+\kappa aE_0(t)+4a^2E_1(t).
 }
 \tag{L-91406.1}
\]

On every open knot interval,

\[
 E_0'=-c,
 \qquad
 E_1'=E_0,
\]

and therefore

\[
 \boxed{
 B'=-\kappa ac+4a^2E_0,
 \qquad
 B''=-4a^2c.
 }
 \tag{L-91406.2}
\]

At `t=log n`,

\[
 \Delta E_0=f_n,
 \qquad
 \Delta B=\kappa af_n,
 \qquad
 \Delta B'=4a^2f_n.
 \tag{L-91406.3}
\]

Thus the density is exactly the position of a particle with constant negative acceleration between logarithmic knots and positive coupled position/velocity kicks at the knots.

## 2. Exact discrete recurrence

Let

\[
 t_n=\log n,
 \qquad
 h_n=t_{n+1}-t_n=\log(1+1/n),
\]

and use post-knot states

\[
 e_n=E_0(t_n+),
 \qquad
 b_n=B(t_n+),
 \qquad
 v_n=B'(t_n+).
\]

Then

\[
 \boxed{
 \begin{aligned}
 e_{n+1}
 &=e_n-ch_n+f_{n+1},\\
 v_{n+1}
 &=v_n-4a^2ch_n+4a^2f_{n+1},\\
 b_{n+1}
 &=b_n+v_nh_n-2a^2ch_n^2+\kappa af_{n+1}.
 \end{aligned}}
 \tag{L-91406.4}
\]

The pre-knot value is

\[
 \boxed{
 B(t_{n+1}-)
 =b_n+v_nh_n-2a^2ch_n^2.
 }
 \tag{L-91406.5}
\]

This is an exact two-state arithmetic recurrence; no continuum approximation is present.

## 3. Ballistic energy

Define

\[
 \boxed{
 \mathscr K(t)
 =B(t)+\frac{B'(t)^2}{8a^2c}.
 }
 \tag{L-91406.6}
\]

### Free-flight invariance

If an interval has length `h`, equations (L-91406.2) give

\[
 v_{\rm out}=v_{\rm in}-4a^2ch,
\]

\[
 b_{\rm out}=b_{\rm in}+v_{\rm in}h-2a^2ch^2.
\]

Hence

\[
 \boxed{
 b_{\rm out}+\frac{v_{\rm out}^2}{8a^2c}
 =b_{\rm in}+\frac{v_{\rm in}^2}{8a^2c}.
 }
 \tag{L-91406.7}
\]

### Positive jump increment

Let `e^-` be the pre-knot value of `E_0` and let the knot mass be `f>=0`. Using

\[
 v^-=-\kappa ac+4a^2e^-,
\]

the jump in `mathscr K` is

\[
\begin{aligned}
 \Delta\mathscr K
 &=\kappa af
 +\frac{(v^-+4a^2f)^2-(v^-)^2}{8a^2c}\\
 &=\frac{4a^2}{c}e^-f+\frac{2a^2}{c}f^2\\
 &=\frac{2a^2}{c}\left[(e^-+f)^2-(e^-)^2\right].
\end{aligned}
\]

The all-Green theorem gives `e^->=0`. Therefore

\[
 \boxed{
 \Delta\mathscr K\ge0.
 }
 \tag{L-91406.8}
\]

Combining free-flight invariance and the jump law:

\[
 \boxed{
 \mathscr K(t)\text{ is nondecreasing on }[0,\infty).
 }
 \tag{L-91406.9}
\]

## 4. Exact initial reserve

Immediately after the unit atom at `t=0`,

\[
 E_0(0+)=1,
 \qquad
 B(0+)=-c+\kappa a,
 \qquad
 B'(0+)=-\kappa ac+4a^2.
\]

Thus

\[
 \boxed{
 \mathscr K_0
 =-c+\kappa a
 +\frac{(4a^2-\kappa ac)^2}{8a^2c}>0.
 }
 \tag{L-91406.10}
\]

The strict sign follows from `c<2a` and `kappa>2`.

More explicitly,

\[
 \boxed{
 \mathscr K(t)
 =\mathscr K_0
 +\frac{2a^2}{c}
 \sum_{2\le n\le e^t}
 \left[E_0(\log n+)^2-E_0(\log n-)^2\right].
 }
 \tag{L-91406.11}
\]

Every summand is nonnegative.

## 5. A negative density forces a large slope

If `B(t)<0`, then (L-91406.9)--(L-91406.10) imply

\[
 \frac{B'(t)^2}{8a^2c}
 =\mathscr K(t)-B(t)
 >\mathscr K_0.
\]

Consequently

\[
 \boxed{
 B(t)<0
 \Longrightarrow
 |B'(t)|>\sqrt{8a^2c\,\mathscr K_0}.
 }
 \tag{L-91406.12}
\]

Since

\[
 B'=4a^2\left(E_0-\frac{\kappa c}{4a}\right),
\]

this is equivalently

\[
 \boxed{
 B(t)<0
 \Longrightarrow
 \left|E_0(t)-\frac{\kappa c}{4a}\right|
 >\sqrt{\frac{c\mathscr K_0}{2a^2}}.
 }
 \tag{L-91406.13}
\]

Thus the compact Green-density theorem is reduced further: it is enough to keep the one-Green discrepancy inside one explicit interval. Any counterexample to the desired density sign must first create a quantitatively large one-Green slope excursion.

## 6. Significance and boundary

The Green-removal problem is not an unrelated collection of pre-knot inequalities. It is a positively kicked ballistic system with a monotone exact energy. This structure retains the contact term and both Green orders simultaneously, so it avoids the one-sided-FKG loss isolated in `R-91401`.

It does not yet rule out the slope excursion in (L-91406.13). A conclusion-producing continuation may use:

```text
an explicit upper/lower corridor for E_0;
a source-specific martingale transport for the arithmetic kicks;
a polarized Hardy square controlling B';
or a finite interval certificate on the remaining compact (a,t) set.
```

```text
exact knot recurrence                         EXACT
free-flight energy invariance                 EXACT
positive arithmetic energy kicks             EXACT
monotone ballistic energy                     EXACT
negative density -> explicit slope witness    EXACT
uniform exclusion of the slope witness        OPEN
full Green-removal density sign               OPEN / RH-BEARING
Riemann Hypothesis                            UNPROVED
```

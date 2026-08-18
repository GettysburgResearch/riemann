# Zero-marginal Lorenz collapse, target-prefix no-go, and the target-root route

Date: 2026-08-18  
Branch: `research/gpt56-pro/98000-zero-marginal-lorenz-collapse`  
Frozen base: PR #596 at `40bfd7e70521f4205e95d3960812a6cef6073c05`  
Scientific status: **new unconditional structure and exact refutations; RH remains unproved**

## Executive result

This pass removes the continuous Lorenz geometry as a source of ambiguity.

The canonical unsieved `5:3` marginal ratio

\[
\vartheta(Y)=Q_*(Y)/(4\sqrt Y-3)
\]

is strictly increasing from `0` to `6`. Consequently every Lorenz threshold is one cutoff in the native source index.

For any finite source, the complete Lorenz dual is minimized at `lambda=0` exactly when

\[
T_E^+\le T_O\le T_E.
\]

Thus the nonzero hinges collapse to the native scalar under one explicit target sandwich.

The first proposed pointwise continuation was then attacked and refuted. At the actual `P_61` source,

\[
X=600,\qquad Y=100,
\]

gives a negative one-switch target prefix. Therefore a proof must retain cumulative signed area in the Lorenz parameter; an instantaneous positive cone in the two prefix moments is impossible.

Finally, the upper half of the zero-marginal target sandwich is proved asymptotically from PNT and squarefree density. The sole remaining target condition is positivity of

\[
\mathcal T_X
=4\sqrt X\sum_{n\le X}{\mu(n)\over n}
-3\sum_{n\le X}{\mu(n)\over\sqrt n}.
\]

This target root has the zero-safe transform

\[
{s+3/2\over s(s-1/2)\zeta(s+1/2)}.
\]

Eventual nonnegativity therefore implies RH by Landau. It is a genuine RH-bearing producer, not a routine Hall auxiliary.

## I. Ordered marginal theorem

On every activation cell,

\[
Q_*(Y)=A_N\log Y-B_N.
\]

The derivative of `vartheta` is positive exactly when

\[
B_N/A_N>\log Y-2+3/(2\sqrt Y).
\]

The proof introduces the increasing function

\[
g_y(x)=x^{-1/2}(\log x-c(y)),
\qquad y=N+1,
\]

and obtains the exact Riemann-sum lower bound

\[
\sum_{n=1}^N g_y(n)
\ge
\log y-1-{1\over2\sqrt y}+{3\over2y}>0.
\]

The exceptional dictionary correction at `1,2,4` is also strictly positive. This proves global order without a numerical tail.

## II. Zero-marginal convex collapse

For

\[
D^+(\lambda)
=\lambda T_O+
\sum_Ea_i(r_i-\lambda t_i)_+-R_O,
\]

the one-sided derivatives are

\[
D'_-(0)=T_O-T_E,
\qquad
D'_+(0)=T_O-T_E^+.
\]

Convexity gives

\[
0\text{ is the global minimizer}
\iff
T_E^+\le T_O\le T_E.
\]

For the canonical source, `r_X(k)>0` exactly when `k<X/2`. The sandwich is equivalently

\[
0\le\mathcal T_X\le\mathcal Z_X,
\]

where `mathcal Z_X` is the even target in `X/2<=k<=X`.

## III. One-switch layer cake

For `0<=lambda<6`, let `Y_lambda` be the unique marginal threshold. Then

\[
(Q_*(Y)-\lambda T(Y))_+
=\int_\lambda^6 T(Y)1_{Y>Y_u}\,du.
\]

After a finite Euler projection,

\[
\mathcal C_P(X,\lambda)
=\int_\lambda^6\mathcal T_P(X;Y_u)\,du,
\]

with

\[
\mathcal T_P(X;Y)
=4\sqrt X\sum_{d<X/Y}{\mu(d)\over d}
-3\sum_{d<X/Y}{\mu(d)\over\sqrt d}.
\]

Thus each finite failure is a one-switch separator with only two prefix moments.

## IV. Exact pointwise no-go

At `P=P_61`, `X=600`, `Y=100`, the strict cutoff is `d<6`, so only `1,2,3,5` occur. Exact rational radical bounds give

\[
\mathcal T_{P_{61}}(600;100)<-14/15.
\]

Hence the derivative of the cumulative hinge may be negative. The open sign is the area

\[
\mathcal C_P(X,\lambda)\ge0,
\]

not pointwise positivity of its derivative.

The minimal future-prime search state must therefore retain accumulated area in addition to the two instantaneous moments.

## V. Upper zero-marginal sandwich is unconditional

PNT gives

\[
\mathcal T_X=o(\sqrt X).
\]

On `[X/2,3X/4]`, the scalar is zero and the target is bounded below by a positive constant times `X^{-1/2}`. Positive squarefree parity has density `3/pi^2`, up to `o(1)`, so

\[
\mathcal Z_X\gg\sqrt X.
\]

Therefore `mathcal T_X<=mathcal Z_X` eventually. The only remaining sandwich condition is `mathcal T_X>=0`.

## VI. Target-root Mellin and Volterra forms

The exact Mellin transform is

\[
\int_1^\infty\mathcal T_X X^{-s-1}dX
={s+3/2\over s(s-1/2)\zeta(s+1/2)}.
\]

The zeta pole at `s=1/2` is removable, while every hypothetical zero with real part greater than one half survives. Landau therefore gives

\[
\mathrm{TRP67}\Longrightarrow\mathrm{RH}.
\]

Abel summation further gives, with `A(x)=sum_{n<=x}mu(n)/n`,

\[
\mathcal T_x
=\sqrt x A(x)+{3\over2}\int_1^xA(t)t^{-1/2}dt.
\]

Equivalently,

\[
\mathcal T_x
=x^{-1/2}{d\over dx}
\left[x^{3/2}\int_1^xA(t)t^{-1/2}dt\right].
\]

The target route is one Volterra storage monotonicity theorem for the reciprocal Mertens prefix.

## VII. Correct strategic verdict

The following shortcut is dead:

```text
ordered marginals
-> every target prefix positive
-> all hinges positive.
```

The corrected possibilities are:

```text
A. prove the native root scalar GPC67 / RBLPTE67 directly;
B. prove TRP67, which independently implies RH;
C. prove the cumulative one-switch area profile with an area-plus-slope Bellman state;
D. prove the target sandwich and root scalar, thereby recovering full CPSL67.
```

Route A remains minimal. Route B is algebraically simpler and deserves an independent attack. Route C is the correct continuation of the Lorenz-Bellman programme after the pointwise no-go.

## VIII. Immediate assignments

1. Run the target-root one-sided endpoint scanner to a large certified range and search for its first finite negative state.
2. Construct exact interval arithmetic for
   \[
   4\sqrt N A_N-3B_N
   \]
   at both activation sides.
3. Search area-plus-slope barriers in the state
   \[
   (\mathcal C,U,V,\text{future quotient profile}).
   \]
4. Attempt a literal bridge from the negative derivative sectors to PR #590's one-sided balanced Type-II packet.
5. Treat every pointwise `(U,V)` cone as refuted unless it stores the missing cumulative area.

## Boundary

```text
marginal order                                  PROVED
zero-marginal convex criterion                  PROVED
one-switch layer cake                           PROVED
pointwise target-prefix positivity              REFUTED
upper zero-marginal target inequality           PROVED EVENTUALLY
TRP67 Mellin-Landau implication                 PROVED CONDITIONAL
TRP67 arithmetic sign                           OPEN / RH-BEARING
cumulative one-switch positivity                OPEN
GPC67 / RBLPTE67                                OPEN / RH-BEARING
Riemann Hypothesis                              UNPROVEN
```

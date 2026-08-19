# L-99250 — The SHARP row kernel has an exact Radon–Nikodym common parent

Claim ID: `L-99250`  
Status: **PROVED EXACT, RELATIVE ONLY TO THE POSITIVE KERNEL THEOREM `L-99240`**  
Created: 2026-08-19  
Frozen parent: PR #642 at `07aa0d4838458a1b2d3af9e5bc96616baa6b4767`  
RH status: **not assumed**

## 1. Positive row source

Put

\[
T(y)=(4\sqrt y-3)\mathbf 1_{y\ge1}.
\]

For a fixed integer row `j>=2`, `L-99240` proves

\[
Q_Y(j)=\int_1^YT(Y/t)\kappa_j(t)\,\frac{dt}{t},
\qquad \kappa_j(t)>0\quad(t\ge j).
\tag{L-99250.1}
\]

Define the finite positive measure

\[
dM_Y^{(j)}(t)
:=\mathbf 1_{t\le Y}T(Y/t)\kappa_j(t)\frac{dt}{t}.
\tag{L-99250.2}
\]

Its total mass is exactly `Q_Y(j)`.

## 2. The exact child map

Let `1<=Z<=Y`. On the support of `M_Y^(j)`, set

\[
R_{Z\mid Y}(t)
:=\mathbf 1_{t\le Z}\frac{T(Z/t)}{T(Y/t)}.
\tag{L-99250.3}
\]

Because `T` is positive and increasing on `[1,infinity)`,

\[
0\le R_{Z\mid Y}(t)\le1.
\]

Moreover

\[
\boxed{
dM_Z^{(j)}(t)=R_{Z\mid Y}(t)dM_Y^{(j)}(t).
}
\tag{L-99250.4}
\]

Thus a same-index smaller-endpoint child is a literal Radon–Nikodym thinning
of one parent source. It is not merely a compatible marginal and it is not a
raw support cutoff.

## 3. The normalized profile is source-monotone

Define

\[
dN_Y^{(j)}(t):=\frac{dM_Y^{(j)}(t)}{T(Y)}.
\tag{L-99250.5}
\]

For fixed `t>=1` and `Y>=t`, write `z=sqrt(Y)` and `a=t^{-1/2}`. Then

\[
\frac{T(Y/t)}{T(Y)}=\frac{4az-3}{4z-3}
\]

and

\[
\frac{\partial}{\partial Y}
\frac{T(Y/t)}{T(Y)}
=
\frac{6(1-t^{-1/2})}
     {\sqrt Y(4\sqrt Y-3)^2}
\ge0.
\tag{L-99250.6}
\]

The supports are nested, so

\[
\boxed{N_{Y_1}^{(j)}\le N_{Y_2}^{(j)}
\quad(1\le Y_1\le Y_2)}
\tag{L-99250.7}
\]

as measures. Taking total masses gives the normalized component-profile
monotonicity

\[
\boxed{
\frac{Q_{Y_1}(j)}{T(Y_1)}
\le
\frac{Q_{Y_2}(j)}{T(Y_2)}.
}
\tag{L-99250.8}
\]

This reconstructs the load-bearing profile arrow of `L-99020` directly from
the new SHARP kernel, without a separate directed tail campaign.

## 4. Literal compact Hall source

Fix `1<=x<67`. For a positive compact occurrence `e` and a negative occurrence
`o`, let

\[
Y_e=x/e,\qquad Y_o=x/o,
\]

and let `t_x(o,e)` be the exact target Hall flow of `L-99020`, supported on
`e<=o`. Then `Y_e>=Y_o`, and (L-99250.7) gives the positive matched source

\[
t_x(o,e)\bigl(N_{Y_e}^{(j)}-N_{Y_o}^{(j)}\bigr)\ge0.
\tag{L-99250.9}
\]

Its total row mass is precisely

\[
t_x(o,e)
\left[
\frac{Q_{Y_e}(j)}{T(Y_e)}
-
\frac{Q_{Y_o}(j)}{T(Y_o)}
\right].
\]

The unused target interval `u_x(e)` carries `u_x(e)N_{Y_e}^{(j)}`. Hence the
compact Hall bonus and the residual row are two disjoint observations of one
divisible positive target source. The bonus is current-owned and has no child
coordinate.

## 5. All factor-67 children from one key

Let a positive residual parent have endpoint `Y`, child endpoints `Z_i<=Y`,
and exact causal coefficients

\[
\alpha_i=r_i\lambda_i,\qquad
\sum_i\alpha_i<67^{-1/2}<1/8.
\]

On `M_Y^(j) x [0,1]`, put

\[
f_i(t)=\alpha_iR_{Z_i\mid Y}(t),
\qquad
F_i(t)=\sum_{h\le i}f_h(t).
\]

Since `0<=R<=1`,

\[
\sum_i f_i(t)<1/8.
\]

The disjoint cylinders

\[
E_i=\{(t,u):F_{i-1}(t)\le u<F_i(t)\}
\tag{L-99250.10}
\]

have marginals

\[
\boxed{\alpha_iM_{Z_i}^{(j)}}.
\tag{L-99250.11}
\]

The complement has marginal

\[
M_Y^{(j)}-\sum_i\alpha_iM_{Z_i}^{(j)}\ge0.
\tag{L-99250.12}
\]

Using `s_k+sum_i lambda_i=1` and `alpha_i=r_i lambda_i`, its total row is
exactly

\[
\boxed{
Q_Y(j)-\sum_i\alpha_iQ_{Z_i}(j)
=s_kQ_Y(j)+
\sum_i\lambda_i\bigl(Q_Y(j)-r_iQ_{Z_i}(j)\bigr).
}
\tag{L-99250.13}
\]

Thus the factor-67 current and every child are one samplewise feasible
partition of the same positive row source.

## 6. Binding interface correction

The phrase “restrict the kernel source to `t<=Z`” is insufficient if it means
raw support restriction. Indeed, with `Y=16`, `Z=4`, `t=4`,

\[
T(Y/t)=T(4)=5,
\qquad
T(Z/t)=T(1)=1.
\]

The raw parent cutoff carries density `5 kappa_j(4)`, while the child carries
`kappa_j(4)`. The exact multiplier is `R_(4|16)(4)=1/5`.

Equation (L-99250.4), not a bare indicator, is the source-faithful child map.

## 7. Scope

This lemma closes the following interfaces at exact fixed-row scope:

```text
normalized Hall profile monotonicity    exact from the SHARP kernel;
matched Hall row bonus                   one positive source difference;
same-index child domination              exact Radon–Nikodym derivative;
all children plus current                 one random-key parent partition;
raw endpoint cutoff                       rejected and repaired.
```

It does not prove the global signed SHARP state nonnegative. The conclusion
route in `T-99250` removes that remaining global source-tree question by
reducing it to one scalar factor-67 Harnack tail.

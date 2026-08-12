# L-91502 — Plastic-cutoff normalization isolates the negative long-jump Hankel channel

Claim ID: `L-91502`  
Status: **EXACT QUASI-LÉVY NORMALIZATION AND HARDY-BLOCK THEOREM**  
Created: 2026-08-12  
Depends on: Nakamura source lock; `L-91402`, `L-91410`  
RH status: **unproved**

## 1. Completed signed source

For

\[
\sigma=a+\frac12>1,
\]

Nakamura's signed quasi-Lévy measure may be written

\[
d\nu_\sigma=d\mathsf N_\sigma+q_\sigma(u)\,du,
\]

where

\[
q_\sigma(u)
=\frac{e^{-\sigma u}}u
\left[\frac1{1-e^{-2u}}-(1+e^u)\right].
\tag{L-91502.1}
\]

Let `varpi>1` be the plastic constant,

\[
\varpi^3-\varpi-1=0,
\qquad
\kappa=\log\varpi.
\]

Since

\[
\frac1{1-e^{-2u}}-(1+e^u)
=\frac{1+e^u-e^{3u}}{e^{2u}-1},
\]

one has

\[
q_\sigma(u)>0\quad(0<u<\kappa),
\qquad
q_\sigma(u)<0\quad(u>\kappa).
\tag{L-91502.2}
\]

Thus

\[
d\nu_\sigma^-(u)
=-q_\sigma(u)\mathbf1_{u>\kappa}\,du
\tag{L-91502.3}
\]

is the complete negative continuous channel.

## 2. Move the Lévy truncation to the sign boundary

The conventional representation uses

\[
F_t^{(1/2)}(u)
=e^{itu}-1-itu\mathbf1_{u\le1/2}.
\]

Replace it by

\[
\boxed{
F_t^{(\kappa)}(u)
=e^{itu}-1-itu\mathbf1_{u\le\kappa}.
}
\tag{L-91502.4}
\]

This changes only the deterministic drift.  If `lambda_sigma^(1/2)` is the old
drift, put

\[
\boxed{
\lambda_\sigma^{(\kappa)}
=\lambda_\sigma^{(1/2)}
-\int_{\kappa<u\le1/2}u\,d\nu_\sigma(u).
}
\tag{L-91502.5}
\]

Then

\[
it\lambda_\sigma^{(1/2)}
+\int F_t^{(1/2)}d\nu_\sigma
=
it\lambda_\sigma^{(\kappa)}
+\int F_t^{(\kappa)}d\nu_\sigma.
\tag{L-91502.6}
\]

The analytic completed characteristic function is unchanged.

The gain is structural: the negative source is supported in `u>kappa`, so its
phase difference has no compensation term:

\[
\boxed{
F_t^{(\kappa)}(u)-F_{-t}^{(\kappa)}(u)
=2i\sin(tu)
\qquad(u\in\operatorname{supp}\nu_\sigma^-).
}
\tag{L-91502.7}
\]

All negative infinite-dimensional source energy is therefore a genuine
oscillatory Hardy channel.  The complete compensation ambiguity has moved into
the one deterministic drift coordinate (L-91502.5).

## 3. Negative score measure and tail-Hankel block

Define the positive radial-score measure

\[
\boxed{
d\lambda_a^-(u)=a u\,d\nu_{a+1/2}^-(u).
}
\tag{L-91502.8}
\]

After the standard Hardy reflection, the positive-frequency block of the
negative completed channel is the tail-Hankel operator

\[
\boxed{
(\mathsf H_{\lambda_a^-}g)(t)
=\int_{u>t}g(u-t)\,d\lambda_a^-(u).
}
\tag{L-91502.9}
\]

For every finite positive measure `mu`, Minkowski's inequality gives

\[
\boxed{
\|\mathsf H_\mu\|
\le \mu((0,\infty)).
}
\tag{L-91502.10}
\]

Indeed,

\[
\begin{aligned}
\|\mathsf H_\mu g\|_2
&\le\int
\left(\int_0^u|g(u-t)|^2dt\right)^{1/2}d\mu(u)\\
&\le\mu((0,\infty))\|g\|_2.
\end{aligned}
\]

The bound is fully polarized: it applies to any common superposition of
carriers or compressed-delay resident inputs before a norm is taken.

## 4. Exact mass formula

Put

\[
n_a=\lambda_a^-((0,\infty)).
\]

Using

\[
\frac1{e^{2u}-1}=\sum_{m\ge1}e^{-2mu},
\]

one obtains

\[
\boxed{
\begin{aligned}
n_a
={}&\frac{a}{a-1/2}e^{-(a-1/2)\kappa}\\
&-a\sum_{m\ge1}
\frac{e^{-(a+1/2+2m)\kappa}}
     {a+1/2+2m}.
\end{aligned}}
\tag{L-91502.11}
\]

This is an alternating-reserve formula: the first elementary exponential is
strictly reduced by a positive series.

At the fixed safe scale `a=4`, put

\[
x=e^{-\kappa/2}=\varpi^{-1/2}.
\]

Then

\[
x^6+x^4=1
\tag{L-91502.12}
\]

and

\[
\boxed{
n_4
=\frac87x^7
-8\sum_{m\ge1}\frac{x^{9+4m}}{9+4m}.
}
\tag{L-91502.13}
\]

## 5. Directed rational bound

The exact rational inequalities

\[
\frac{86883}{100000}<x<\frac{86884}{100000}
\tag{L-91502.14}
\]

follow by substituting both endpoints in the increasing polynomial
`X^6+X^4-1`.

Discarding the negative tail after six terms and directing the powers gives

\[
\begin{aligned}
n_4
<&\frac87\left(\frac{86884}{100000}\right)^7\\
&-8\sum_{m=1}^{6}
\frac1{9+4m}
\left(\frac{86883}{100000}\right)^{9+4m}\\
<&\frac14.
\end{aligned}
\tag{L-91502.15}

The last comparison is an exact `Fraction` computation in the resident replay.
Thus

\[
\boxed{\|\mathsf H_{\lambda_4^-}\|<\frac14.}
\tag{L-91502.16}
\]

## 6. Scope

Closed here:

```text
plastic-boundary Lévy normalization;
all negative oscillatory mass in one positive tail-Hankel channel;
all compensation moved to one deterministic connection;
exact long-jump mass series;
directed rational bound n_4<1/4;
fully polarized operator-norm bound.
```

Not closed here:

```text
identification of the shifted deterministic drift with the completed bridge;
the signed completed source lock to the delayed screw Gram;
absorption of the long channel by a declared positive reserve;
RH.
```

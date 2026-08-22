# T-102790 — Outer-ray resolvent and the first-order critical-current frontier

Claim ID: `T-102790`  
Status: **MAJOR UNCONDITIONAL DIFFERENTIAL REDUCTION; RH UNPROVED**  
Created: 2026-08-22  
Base: PR #719  
RH status: **unproved**

The filtered completion programme has successively reduced its final scalar to:

```text
one filtered SHARP disk;
one centered radial SDP;
one fixed outer ray w=-8.
```

`L-102738--L-102740` now give the exact final analytic normal form.

## 1. Radial SDP solved

The radial gauge is both:

```text
one real primal minimization;
one compact SDP dual over fixed linear source functionals.
```

The distinguished rank-one dual extreme is the fixed ray `w=-8`.

## 2. Lorentz current equals outer-ray increment

For the filtered polynomial

\[
P(w)=C+2Bw+Aw^2,
\]

\[
\boxed{
5P_2a_\tau-G_\tau
=4A-B
=\frac{P(-8)-P(0)}{16}.
}
\]

The three-ray formula is exactly the degree-two interpolation of this outer
value.

## 3. The second-order current has a positive stable resolvent

For any fixed source `sigma`, let `H_sigma` be its common-mother observation and
put

\[
Y_\sigma=(D-1)H_\sigma.
\]

Then

\[
\boxed{
5P_2a_\sigma-G_\sigma
=
\frac52(D+3/10)Y_\sigma.
}
\]

The causal inverse has positive kernel,

\[
Y_\sigma(u)
=
\frac25\int_{-\infty}^{u}
 e^{-3(u-v)/10}
[5P_2a_\sigma-G_\sigma](v)\,dv,
\]

and therefore

\[
\boxed{
\int_{-\infty}^{U}(Y_\sigma)_-
\le
\frac43
\int_{-\infty}^{U}(5P_2a_\sigma-G_\sigma)_-.
}
\]

Thus the outer-ray estimate implies the first-order critical scale-variation
estimate with a fixed loss only.

## 4. Exact boundary

The converse is false for arbitrary smooth functions: high-frequency scale
oscillations can have bounded first-order negative mass and arbitrarily large
outer-current negative mass.  Hence the remaining reverse estimate must use
the literal native completion-defect source.

The conclusion graph is now

\[
\mathrm{OER}_{102780}
\Longrightarrow
\text{critical first-order variation}
\Longrightarrow
\mathrm{RH}.
\]

Equivalently, one may attack the source-specific converse and close through the
already-audited critical-variation consumer.

```text
radial primal/dual solution               PROVED EXACT
outer-ray interpretation                  PROVED EXACT
sharp inner-disk countermodel             PROVED EXACT
outer multiplier factorization            PROVED EXACT
positive causal resolvent                 PROVED EXACT
source-free converse                      FALSE
OER102780                                 OPEN / RH-BEARING
Riemann Hypothesis                        UNPROVED
```
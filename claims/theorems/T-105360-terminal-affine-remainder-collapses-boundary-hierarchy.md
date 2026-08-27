# T-105360 — A terminal affine boundary remainder collapses the all-window Stieltjes hierarchy

Claim ID: `T-105360`  
Status: **MAJOR EXACT EXHAUSTION REDUCTION; TWO SOURCE-SPECIFIC GATES OPEN**  
Created: 2026-08-23  
Depends on: `L-105328`, `L-105351`, `L-105360`, `T-105350`  
RH status: **unproved**

## 1. The remaining window quantifier

`T-105350` reduces the boundary half of the low-order Xi problem to the
all-order origin Stieltjes hierarchy `OASH105350` in every regular symmetric
window. `L-105360` now removes the remaining **window-by-window** repetition.

Let

\[
\Omega_1\Subset\Omega_2\Subset\cdots
\]

be the exact regular symmetric exhaustion for the last defective derivative

\[
F=\Xi^{(k)}.
\]

Let `H_N=H_(F,Omega_N)` be its boundary Cauchy function.

## 2. Terminal affine remainder gate

Define:

```text
TAIR105360:
  there exists a real a>=0 such that

      H_N(z) -> a z

  locally uniformly in one fixed complex neighborhood of the origin along the
  exact regular exhaustion.
```

By Cauchy's formula this is equivalent to the complete terminal origin-moment
statement

\[
\boxed{
\beta_0(F;\Omega_N)\longrightarrow a\ge0,
\qquad
\beta_n(F;\Omega_N)\longrightarrow0
\quad(n\ge1),
}
\tag{T-105360.1}
\]

with uniform analytic bounds on one fixed disk. The higher-moment vanishing is
load bearing; `R-105360` proves that a positive terminal slope alone is
insufficient.

## 3. Exact reconstruction of every inner boundary measure

Assume `CRVH105330` on the simple noncommon stratum. Then every critical point
crossed by the symmetric exhaustion is real and occurs in a pair `+-c` with

\[
\rho_c={F(c)\over F''(c)}\le0.
\]

For `m<N`, `L-105360` gives

\[
H_m(z)
=H_N(z)
+z\sum_{\substack{c>0\\c\in\Omega_N\setminus\Omega_m}}
 {-2\rho_c/c^2\over1-z^2/c^2}.
\tag{T-105360.2}
\]

Put

\[
w_c={-2\rho_c\over c^2}\ge0,
\qquad
s_c={1\over c^2}.
\]

Taking the coefficient of `z` in (T-105360.2) gives

\[
\sum_{\substack{c>0\\c\notin\Omega_m}}w_c
=eta_0(F;\Omega_m)-a<\infty.
\tag{T-105360.3}
\]

Thus the exterior atomic weights are summable. Passing to the limit on a
smaller fixed disk yields

\[
\boxed{
H_m(z)
=z\int_0^\infty{d\nu_m(s)\over1-sz^2},
}
\tag{T-105360.4}
\]

where

\[
\boxed{
\nu_m
=a\delta_0
+
\sum_{\substack{c>0\\c\notin\Omega_m}}
 {-2\rho_c\over c^2}\,\delta_{1/c^2}.
}
\tag{T-105360.5}
\]

The measure is finite and positive. Its support is compact because the omitted
critical points lie outside the fixed inner window, so `1/c^2` lies in one
bounded interval accumulating only at zero.

Consequently every inner boundary function satisfies the complete origin
Stieltjes hierarchy:

\[
\boxed{
\mathrm{CRVH105330}
\ \wedge\
\mathrm{TAIR105360}
\Longrightarrow
\mathrm{OASH105350}.
}
\tag{T-105360.6}
\]

## 4. Sharpened conclusion graph

The parent exact implications are

\[
\mathrm{CRVH105330}
\Longrightarrow
\mathrm{PRES105220}
+
\text{absence of the nonreal critical correction},
\]

and

\[
\mathrm{OASH105350}
\Longleftrightarrow
\text{the all-packet PSD component of }\mathrm{BRP105220}.
\]

Combining these with (T-105360.6) gives

\[
\boxed{
\mathrm{CRVH105330}
\ \wedge\
\mathrm{TAIR105360}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-105360.7}
\]

Neither antecedent is proved for the last defective low-order Xi derivative.

The boundary programme has nevertheless been reduced from

```text
every packet in every window
```

to

```text
one terminal affine-germ theorem,
provided the sharp critical-residue hierarchy holds along the exhaustion.
```

## 5. Terminal contour-moment form

`TAIR105360` is equivalently the source-specific contour statement

\[
\boxed{
{1\over2\pi i}\int_{\partial\Omega_N}
 {F(\zeta)/F'(\zeta)\over\zeta^2}\,d\zeta
\longrightarrow a\ge0,
}
\tag{T-105360.8}
\]

and, for every `n>=1`,

\[
\boxed{
{1\over2\pi i}\int_{\partial\Omega_N}
 {F(\zeta)/F'(\zeta)\over\zeta^{2n+2}}\,d\zeta
\longrightarrow0,
}
\tag{T-105360.9}
\]

with one fixed-disk normal-family bound. These are the exact far-boundary
quantities a source calculation must estimate.

## 6. Polynomial calibration

For a definite-parity real polynomial `p` of degree `n`, an outer contour
containing every critical point gives

\[
H_{p,\Omega_N}(z)={z\over n}.
\]

Thus

\[
a={1\over n},
\]

and (T-105360.5) reduces exactly to the exterior-residue measure of
`L-105351`. The theorem is therefore the entire-function analogue of the
classical polynomial terminal affine remainder.

## 7. What remains genuinely open

```text
finite nested-window Stieltjes atom transport       PROVED EXACT
all-window OASH from CRVH plus one terminal measure PROVED EXACT
positive terminal slope alone                       REFUTED AS SUFFICIENT
CRVH105330 for fixed low-order Xi                    OPEN / SHARP RH-BEARING
TAIR105360 for fixed low-order Xi                    OPEN / SHARP RH-BEARING
moving-saddle global dominance                      OPEN / PROPOSED
Riemann Hypothesis                                   UNPROVEN
```

The theorem does not derive `TAIR105360` from the moving saddle, justify
common/multiple critical events, or estimate the far-boundary contours. Those
are explicit next obligations rather than hidden passages.

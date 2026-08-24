# T-105600 — Phase variance, backward Poisson descent and height-shell energy form one closure frontier

Claim ID: `T-105600`  
Status: **MAJOR EXACT SYNTHESIS; SOURCE-SPECIFIC TRANSFER OPEN**  
Created: 2026-08-24  
Depends on: `T-105444--T-105451`, `L-105600--L-105603`, PR #731 `L-105281`  
RH status: **unproved**

## 1. One source, three coordinates

For the Xi derivative ratio

\[
m_r={\Xi^{(r)}\over\Xi^{(r+1)}
\]

the conclusion-facing differential field is

\[
\mathcal C_{r,b}(a,h)
={1\over2}
\left[
 h\Re m_r'(a+i(b+h))
-
 \Im m_r(a+i(b+h))
\right].
\tag{T-105600.1}
\]

At an extremal base `beta_r`, the shifted ratio is Pick. The exact work of
`L-105600--L-105603` proves that the same defect has three forms.

### Phase variance

For the normalized Herglotz phase law,

\[
\boxed{
\mathcal C
=-{\Im f\over4}
\mathbb E|\omega-1|^2.
}
\tag{T-105600.2}
\]

### Backward Poisson evolution

A downward base displacement `delta` acts by

\[
\boxed{
\mathcal C_h^{[\delta]}
=e^{\delta|D|}\mathcal C_h^{[0]}
}
\tag{T-105600.3}
\]

when the Xi affine Herglotz coefficient vanishes.

### Reciprocal-source Hardy multiplier

In the reflected safe-line coordinate,

\[
\boxed{
-2\mathcal C_{r,b}(a,h)
=
\Re\left[q_r(s)-h q_r'(s)\right],
\qquad
q_r={\xi^{(r)}\over\xi^{(r+1)}}.
}
\tag{T-105600.4}
\]

In the frozen rung-zero Dirichlet model,

\[
q_L-hq_L'
=
\sum_{n\ge1}
 b_L(n)(1+h\log n)n^{-s},
\qquad b_L(n)\ge0.
\tag{T-105600.5}
\]

The spatial frequency is `log n`, and lowering the base multiplies it by
`n^delta=e^(delta log n)`, exactly as in (T-105600.3).

The phase-barycenter, six-dimensional Newton, backward-Poisson and one-sided
Hardy programmes are therefore different transforms of one positive
reciprocal-source coefficient family.

## 2. Exact contact rigidity

Let `delta=beta_r-b>0`, put `y=h-delta`, and assume `h>delta`. A nonnegative
lower-base contact implies

\[
\boxed{
\mathbb E|\omega-1|^2
\le {2\delta\over y+\delta}.
}
\tag{T-105600.6}
\]

For every fixed `R>0`, its normalized Herglotz measure obeys

\[
\boxed{
\mathbb P\{|t-a|\le Ry\}
\le {1+R^2\over2}{\delta\over y+\delta}.
}
\tag{T-105600.7}
\]

Thus shallow contacts with `delta/y -> 0` force complete local measure
evacuation and a Schwarz--Pick equality blow-up:

\[
\boxed{
{f(a+y\zeta)-\Re f(a+iy)
 \over\Im f(a+iy)}
\longrightarrow\zeta.
}
\tag{T-105600.8}
\]

Spatial escape is no longer an arbitrary sequence at infinity. It is an
asymptotically affine local limit in which every source phase aligns.

## 3. Exact local-hole form

The downward-shift kernel is

\[
\boxed{
{1\over2y}
{\lambda s^2-(2+\lambda)
 \over(1+s^2)^2},
\qquad
\lambda={\delta\over y},
\quad
s={a-t\over y}.
}
\tag{T-105600.9]
\]

Its integral is always `-pi/2`, but it has a positive remote tail. Every
nonnegative contact necessarily satisfies

\[
\boxed{
\mu([a-y,a+y])
\le
2\delta y
\int_{|t-a|>y}{d\mu(t)\over(t-a)^2}.
}
\tag{T-105600.10}
\]

This is the exact source condition which a physical proof must contradict.

The finite-model firewall `R-105600` shows that compactly supported positive
measures actually develop the wrong sign at large spatial centre after every
downward shift. Therefore no finite polynomial or fixed truncation can close
this theorem without an explicit infinite-tail estimate.

## 4. Height-shell all-pass alternative

For a real polynomial or regular finite entire-function rectangle, define the
height-shell all-pass map

\[
\mathcal S_{F;h_1,h_2}(x)
=
{F(x+ih_2)F(x-ih_1)
 \over
 F(x-ih_2)F(x+ih_1)}.
\tag{T-105600.11}
\]

Its winding is minus the number of zeros in the horizontal shell. For the
derivative ladder, adjacent shell quotients telescope. If the terminal rung is
shell-free, then the base shell count is bounded by

\[
\boxed{
M_{F_0}
\le
\sum_{k<R}\mathcal E_-(\mathcal U_k)
+
(\mathsf v_{F_0}-\mathsf v_{F_R})_+,
}
\tag{T-105600.12}
\]

where `E_-` is the negative `H^(1/2)` energy and the final term is the single
surviving vertical endpoint correction.

Because the shell count is even,

\[
\boxed{
\sum_{k<R}\mathcal E_-(\mathcal U_k)
+
(\mathsf v_{F_0}-\mathsf v_{F_R})_+
<2
\Longrightarrow
M_{F_0}=0.
}
\tag{T-105600.13}
\]

This is `HSHE105602`. It is the integrated/topological counterpart of the
pointwise phase variance (T-105600.2).

## 5. Two coupled closure routes

The synthesis yields two routes which share one producer.

### Pointwise phase-variance route

```text
DMPXFER105603:
  physical one-sided-Hardy reserve exceeds every carrier/error term

-> C_(0,b)(a,h)<=0 for every base, centre and scale
-> beta_0=0
-> RH.
```

### Integrated shell-energy route

```text
HSHE105602:
  total adjacent negative H^(1/2) shell energy
  plus the telescoped endpoint correction is <2

-> every positive-height shell is empty
-> RH.
```

The same reciprocal coefficients `b_L(n)(1+h log n)` feed both routes.
The pointwise route seeks a local phase-variance lower bound; the integrated
route permits local slips but prices their integer winding by half a derivative.
A future proof may combine them: use the one-sided phase gap on diffuse regions
and reserve the all-pass energy only for concentrated near-zero phase slips.

## 6. Exact remaining implication matrix

```text
positive reciprocal Dirichlet source                 PROVED EXACT / FROZEN
one-sided pre-collapse phase reserve                  PROVED EXACT
phase barycenter = differential microscope            PROVED EXACT
base descent = backward Poisson                       PROVED EXACT
height shell = all-pass winding                       PROVED EXACT
negative winding <= H^(1/2) energy                    PROVED EXACT
finite-model global descent                           REFUTED
DMPXFER105603 physical pointwise transfer             OPEN / RH-BEARING
HSHE105602 physical shell-energy transfer              OPEN / RH-BEARING
Riemann Hypothesis                                    UNPROVEN
```

## 7. Scope

No physical transfer estimate is proved here. The moving-saddle terminal
endpoint remains subject to hostile review. The theorem neither excludes Xi
spatial escape nor proves the shell energy below two. It identifies the exact
shared producer and gives both the local and topological consumers without
claiming RH.

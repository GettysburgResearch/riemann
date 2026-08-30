# L-107102 — Spectral concentration forces Laguerre positivity and real zero localization

Claim ID: `L-107102`  
Status: **PROVED GENERAL FOURIER-CONCENTRATION THEOREM**  
Created: 2026-08-30  
Depends on: `L-107100`  
RH status: **not assumed**

Let `nu` be a probability measure supported in

\[
[u_0-\delta,u_0+\delta]
\subset(0,\infty),
\qquad
\eta={\delta\over u_0}\le{1\over32}.
\]

For `theta in {0,pi/2}`, define the real entire function

\[
F_{\nu,\theta}(z)
=
\int\cos(uz-\theta)\,d\nu(u).
\tag{L-107102.1}
\]

The choices `theta=0` and `theta=pi/2` are the cosine and sine cases.

## 1. Uniform Laguerre reserve

For real `t`, put

\[
\mathcal L_{\nu,\theta}(t)
=
F'_{\nu,\theta}(t)^2
-
F_{\nu,\theta}(t)F''_{\nu,\theta}(t).
\]

If

\[
|t|\delta\le{1\over32},
\]

then

\[
\boxed{
\mathcal L_{\nu,\theta}(t)
\ge {u_0^2\over2}>0.
}
\tag{L-107102.2}
\]

### Proof

Write

\[
A=\mathbb E\cos(tU-\theta),
\quad
B=\mathbb E[U\sin(tU-\theta)],
\quad
C=\mathbb E[U^2\cos(tU-\theta)].
\]

Then `L=B^2+AC`. For the point mass at `u_0`,

\[
B_0^2+A_0C_0=u_0^2.
\]

Put `q=|t|delta`. Elementary Lipschitz bounds give

\[
|A-A_0|\le q,
\]

\[
{|B-B_0|\over u_0}\le\eta+q,
\]

\[
{|C-C_0|\over u_0^2}\le3\eta+q.
\]

Also `|B|/u_0<=2` and `|C|/u_0^2<=4`. Therefore

\[
{|\mathcal L-u_0^2|\over u_0^2}
\le6\eta+8q
\le{14\over32}<{1\over2},
\]

which proves (L-107102.2).

Thus a sufficiently concentrated Fourier measure has no simple wrong-sign extrema in the entire interval `|t|<=1/(32 delta)`.

## 2. Complex zero localization

Let

\[
G_\theta(z)=\cos(u_0z-\theta)
\]

and let `z_j` be its real zeros. There is an absolute constant `c_0>0` with the following property.

Fix `T,H>0` and assume

\[
\boxed{
\delta(T+H+u_0^{-1})e^{\delta H}\le c_0.
}
\tag{L-107102.3}
\]

For every `j` with `|z_j|<=T+1/(4u_0)`, put

\[
D_j=\{z:|z-z_j|<1/(4u_0)\}.
\]

Then:

1. every `D_j` contains exactly one zero of `F_(nu,theta)`, counted with multiplicity;
2. that zero is real and simple;
3. `F_(nu,theta)` has no other zero in
   `|Re z|<=T`, `|Im z|<=H`.

### Proof sketch with explicit comparison

For `|U-u_0|<=delta`, the exponential representation of cosine gives

\[
|\cos(Uz-\theta)-\cos(u_0z-\theta)|
\le
C\delta|z|e^{\delta|\Im z|}
\left(|G_\theta(z)|+1\right)
\tag{L-107102.4}
\]

with an absolute `C`. On `partial D_j`,

\[
|G_\theta(z)|
=|\sin(u_0(z-z_j))|
\ge {1\over8}.
\]

Outside the union of the disks, either the real phase stays at least `1/4` from a cosine zero or the hyperbolic part supplies the same lower bound. Under (L-107102.3), (L-107102.4) is strictly smaller than `|G_theta|` on every relevant boundary. Rouché gives one zero in each disk and none elsewhere. Real conjugation plus uniqueness in a disk centred on the real axis forces that zero to be real; multiplicity one follows from the Rouché count.

## 3. Exponentially small tails

The compact-support assumption may be replaced by an explicit weighted tail. Let `nu_I` be the restriction to `[u_0-delta,u_0+delta]`, normalized to mass one, and suppose

\[
\mathfrak T_H
=
\int_{|u-u_0|>\delta}
\left(1+{u^2\over u_0^2}\right)
 e^{H|u-u_0|}\,d\nu(u)
\]

is smaller than a sufficiently small absolute multiple of the margins in (L-107102.2) and (L-107102.3). The tail changes `F,F',F''` by at most the corresponding weighted exponential moment, so the same conclusions hold with `u_0^2/2` replaced by `u_0^2/3` and with a smaller `c_0`.

## Scope

This theorem is source-independent but hypothesis-rich: concentration of the Fourier measure is the whole input. For Xi derivatives, proving the required concentration uniformly in derivative order is a separate analytic task.
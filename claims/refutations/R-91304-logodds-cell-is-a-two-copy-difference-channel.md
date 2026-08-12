# R-91304 — The log-odds Sturm–Liouville cell is a two-copy difference channel, not by itself the one-copy Xi impedance

Claim ID: `R-91304`  
Status: **EXACT COORDINATE CORRECTION / REQUIRED CORRECTION TO `L-91310`**  
Created: 2026-08-12  
RH status: **unproved**

## 1. One-copy BPY coordinate

Let one half-size-biased BPY copy be represented by

\[
 Z=\frac12\log\Sigma+C,
 \tag{R-91304.1}
\]

where `C` is the fixed normalizing constant and

\[
 \mathbb E e^{rZ}
 =\frac{\xi(\frac12+r)}{\xi(\frac12)}.
 \tag{R-91304.2}
\]

The Xi impedance is the one-copy ratio

\[
 \ell_a(r)
 =\frac{\mathbb E[e^{rZ}\sinh(aZ)]}
        {\mathbb E[e^{rZ}\cosh(aZ)]}.
 \tag{R-91304.3}
\]

## 2. Exact two-copy Gamma–Beta coordinates

Take two independent un-tilted Gamma-sum copies and pair their Gamma(2)
coordinates mode by mode. In the notation of the Brownian–theta branch,

\[
 \Sigma^+=A+D,
 \qquad
 \Sigma^-=A-D,
 \qquad |D|<A.
 \tag{R-91304.4}
\]

Define

\[
 Z_+=\frac12\log(A+D)+C,
 \qquad
 Z_-=\frac12\log(A-D)+C,
 \tag{R-91304.5}
\]

and the sum/difference coordinates

\[
 S=Z_++Z_- ,
 \qquad
 \Delta=Z_+-Z_-.
 \tag{R-91304.6}
\]

Then exactly

\[
 \boxed{
 \Delta
 =\frac12\log\frac{A+D}{A-D}
 =\operatorname{artanh}\frac DA,
 }
 \tag{R-91304.7}
\]

whereas

\[
 \boxed{
 S
 =\frac12\log(A^2-D^2)+2C
 =\log A+\frac12\log\left(1-\frac{D^2}{A^2}\right)+2C.
 }
 \tag{R-91304.8}
\]

The two-copy half-size bias is

\[
 (\Sigma^+\Sigma^-)^{1/4}
 =(A^2-D^2)^{1/4}
 =e^{S/2-C}.
 \tag{R-91304.9}
\]

## 3. What the exact local cell realizes

Put

\[
 v=\frac DA,
 \qquad
 \Delta=\operatorname{artanh}v.
 \tag{R-91304.10}
\]

The exact local functions from `L-91310`,

\[
 u_{a,\pm}(v)
 =\left(\frac{1+v}{1-v}\right)^{\pm a/2},
 \tag{R-91304.11}
\]

are therefore

\[
 \boxed{
 u_{a,\pm}(v)=e^{\pm a\Delta}.
 }
 \tag{R-91304.12}
\]

They solve the positive Sturm–Liouville equation

\[
 -\partial_v((1-v^2)\partial_vu)
 +\frac{a^2}{1-v^2}u=0,
 \tag{R-91304.13}
\]

and their odd/even ratio is

\[
 \frac{u_{a,+}-u_{a,-}}{u_{a,+}+u_{a,-}}
 =\tanh(a\Delta).
 \tag{R-91304.14}
\]

Thus the local cell realizes the **two-copy difference coordinate** `Delta`.
It does not directly realize `tanh(aZ)` for the one-copy variable in
(R-91304.1), and it does not by itself identify the Weyl function with the
one-copy impedance (R-91304.3).

The equality `Z=artanh(D/A)` in the first version of `L-91310` conflated these
two coordinates and is false as written.

## 4. The complete Brownian reflection form uses both coordinates

For an exponential polynomial `F`, the exact two-copy reflection form is

\[
 \boxed{
 \mathcal R_a(F)
 =\mathbb E\left[
  \sinh(aS)
  \int_{-S/2}^{S/2}
   \overline{F(x+\Delta/2)}
   F(x-\Delta/2)\,dx
 \right].
 }
 \tag{R-91304.15}
\]

Both `S` and `Delta` are load-bearing:

- `Delta` controls the relative translation of the two copies;
- `S` controls the oriented integration interval and the factor `sinh(aS)`;
- the half-size tilt is itself an explicit function of `S` by (R-91304.9).

A one-dimensional positive cell in `Delta` cannot decide the sign of
(R-91304.15) without a coupled treatment of the `S` channel.

## 5. Corrected route-III target

The conclusion-producing Brownian theorem is the following two-coordinate
identity.

> **Sum–Difference DtN Identity (`SDDI_a`).**  
> Construct a closed positive form on the exact Gamma–Beta reservoir, with
> boundary variables `(S,Delta)`, such that for every exponential polynomial
> `F`
> \[
> \boxed{
> \mathcal R_a(F)=\|\mathcal J_aF\|^2
> }
> \tag{R-91304.16}
> \]
> or, equivalently, such that its Weyl kernel is the Xi positive-real kernel.

The local Sturm–Liouville equation (R-91304.13) is a genuine component of this
construction, but only the `Delta` component. The radial/Gamma variable `A`, the
sum coordinate `S`, the exact tilt, and the theta/Poisson/`p=2` reserves must be
retained in the global Green identity.

## 6. Corrected status

```text
log-odds Sturm–Liouville equation                 EXACT
cell transfer = tanh(a Delta)                     EXACT
Delta = artanh(D/A)                               EXACT
one-copy Z = artanh(D/A)                          FALSE
cell alone realizes Xi impedance                  NOT ESTABLISHED
coupled S–Delta positive boundary identity        OPEN / RH-BEARING
Riemann Hypothesis                                UNPROVED
```

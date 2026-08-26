# L-105463 — Corrected reflection-Hodge variation and bounded-detector transfer

Claim ID: `L-105463`

Status: **CORRECTED: REFLECTION SIGNATURE RETAINED; DIRECT IDENTIFICATION WITH BOUNDED \(K_L\) WITHDRAWN**

Corrected: 2026-08-26

Depends on: `L-105462`, `L-105490--L-105491`, `L-106134--L-106135`

RH status: **unproved**

Let \(J_U\) be the ordinary completed same-half-source convolution, and put

\[
\mathcal D_{\rm out}
=
\frac12D(D-1)(5D+\tfrac32)(2D-1).
\]

## 1. Exact reflection geometry retained

With the reflection projectors \(E_x,O_x\), define the Beta-averaged energies

\[
\mathcal E_U(x)=\int_0^1(1-\theta)\|E_xf_\theta\|_2^2d\theta,
\qquad
\mathcal O_U(x)=\int_0^1(1-\theta)\|O_xf_\theta\|_2^2d\theta.
\]

Then

\[
\boxed{
J_U=\mathcal E_U-\mathcal O_U,
\qquad
\mathcal E_U+\mathcal O_U=\mathcal N_U,
}
\tag{L-105463.1}
\]

where \(\mathcal N_U\) is independent of \(x\). Hence

\[
\boxed{
\mathcal D_{\rm out}J_U
=
2\mathcal D_{\rm out}\mathcal E_U
=
-2\mathcal D_{\rm out}\mathcal O_U.
}
\tag{L-105463.2}
\]

The signed compact measure

\[
\nu_U=\mathcal D_{\rm out}\mathcal O_U
\]

has total mass zero. Therefore

\[
\nu_U^+(\mathbb R)=\nu_U^-(\mathbb R)
=\frac12\|\nu_U\|_{\rm TV}.
\tag{L-105463.3}
\]

The four exponential moments at
\(0,1,-3/10,1/2\) also remain zero.

Thus

\[
\boxed{
\mathrm{F1VAR}_{105460}
\Longleftrightarrow
\mathrm{REFSIG}_{106150}
\Longleftrightarrow
\mathrm{SFSC}_{106150}
}
\tag{L-105463.4}
\]

as statements about the differential reflection current.

## 2. Binding multiplier correction

Let \(H_K\) be the bounded derivative-outer observation of the same exact
Boolean source. It is not equal to \(\mathcal D_{\rm out}J_U\).
Instead `L-105490` gives

\[
\boxed{
(5D+\tfrac32)(I-\sqrt2\,\mathsf S)H_K
=
4\mathcal D_{\rm out}J_U
+
H_{\rm closed}.
}
\tag{L-105463.5}
\]

The closed term is inherited from repeated-label contractions and has
subpower logarithmic total variation.

By the stable resolvents of `L-105491`,

\[
\boxed{
\|H_K\|_{L^1(dX/X)}
\ll
\|\mathcal D_{\rm out}J_U\|_{\rm TV}
+
Y^{o(1)}.
}
\tag{L-105463.6}
\]

Therefore `F1VAR105460` remains a sufficient route to the bounded-detector
Hardy criterion and RH. The reverse implication is not established.

## Disposition

```text
reflection even/odd decomposition             PROVED EXACT
zero mass and Jordan-mass equality             PROVED EXACT
four primitive moments                         PROVED EXACT
F1VAR = REFSIG = SFSC for differential current PROVED EXACT
differential current = bounded K_L current      WITHDRAWN
stable one-way transfer to bounded K_L          PROVED
bounded K_L -> differential variation           OPEN / NOT CLAIMED
Riemann Hypothesis                              UNPROVED
```

# L-105418 — The positive Xi Fourier kernel orients every derivative ratio on the imaginary axis

Claim ID: `L-105418`  
Status: **PROVED UNCONDITIONALLY**  
Created: 2026-08-24  
Depends on: the positive Xi Fourier representation; `L-105417`  
RH status: **not assumed**

## 1. Positive Fourier representation

Use

\[
\Xi(z)=\int_0^\infty\Phi(u)\cos(zu)\,du,
\qquad
\Phi(u)>0.
\tag{L-105418.1}
\]

Put

\[
F_r(z)=\Xi^{(r)}(z),
\qquad
m_r(z)={F_r(z)\over F_r'(z)}
={\Xi^{(r)}(z)\over\Xi^{(r+1)}(z)}.
\tag{L-105418.2}
\]

All differentiations below are justified by the superexponential decay of the
explicit Xi kernel.

## 2. Even derivative orders

Let `r=2ell`. Up to the common sign `(-1)^ell`,

\[
F_r(z)=\int_0^\infty u^r\Phi(u)\cos(zu)\,du,
\]

while

\[
F_r'(z)=-\int_0^\infty u^{r+1}\Phi(u)\sin(zu)\,du.
\]

At `z=iy`, `y>0`, this gives

\[
F_r(iy)=(-1)^\ell
\int_0^\infty u^r\Phi(u)\cosh(yu)\,du,
\]

\[
F_r'(iy)=(-1)^\ell(-i)
\int_0^\infty u^{r+1}\Phi(u)\sinh(yu)\,du.
\]

Therefore

\[
\boxed{
 m_r(iy)
=i
{\displaystyle\int_0^\infty
u^r\Phi(u)\cosh(yu)\,du
 \over
 \displaystyle\int_0^\infty
u^{r+1}\Phi(u)\sinh(yu)\,du}
\in i(0,\infty).
}
\tag{L-105418.3}
\]

Here the displayed powers are the literal integration-variable powers `u^r`
and `u^(r+1)`.

## 3. Odd derivative orders

Let `r=2ell+1`. Up to the common sign `(-1)^(ell+1)`,

\[
F_r(z)=\int_0^\infty u^r\Phi(u)\sin(zu)\,du,
\]

and

\[
F_r'(z)=\int_0^\infty u^{r+1}\Phi(u)\cos(zu)\,du.
\]

Thus

\[
\boxed{
 m_r(iy)
=i
{\displaystyle\int_0^\infty
u^r\Phi(u)\sinh(yu)\,du
 \over
 \displaystyle\int_0^\infty
u^{r+1}\Phi(u)\cosh(yu)\,du}
\in i(0,\infty).
}
\tag{L-105418.4}
\]

Again the powers are `u^r` and `u^(r+1)`, and both integrals are strictly
positive.

## 4. Exact phase orientation

For every derivative order and every `y>0`,

\[
\boxed{
\operatorname{Im}
{\Xi^{(r)}(iy)\over\Xi^{(r+1)}(iy)}>0.
}
\tag{L-105418.5}
\]

Consequently the unregularized oriented shifted ratio satisfies

\[
\boxed{
\left.\partial_\alpha
\arg
{F_r'(iy)-\alpha F_r(iy)
 \over
 F_r'(iy)+\alpha F_r(iy)}
\right|_{\alpha=0}
<0.
}
\tag{L-105418.6}
\]

No saddle approximation, zero-location theorem or RH input is used.

## 5. Reduction of the outer-phase gate

Assume the signed-real-critical-pole hypothesis of `L-105417`. In the first
quadrant:

```text
positive real axis:       Im m_r = 0 away from poles;
small critical detours:   Im m_r >= 0;
positive imaginary axis:  Im m_r > 0 by this theorem.
```

Parity and reflection give the second quadrant. Therefore the cofinal
maximum-principle gate `OPG105417` requires a sign estimate only on the remote
quarter-circle, or on an equivalent folded safe-line outer edge.

Define the reduced source-specific gate

```text
QOPG105418 — quarter-arc outer phase

Along one cofinal first-quadrant exhaustion,

    max(0,-inf_(outer quarter arc) Im m_r) -> 0.
```

Then

\[
\boxed{
\mathrm{CRVH105330}
\wedge
\mathrm{QOPG105418}
\Longrightarrow
\mathrm{OPG105417}
\Longrightarrow
\mathrm{BRP105220}.
}
\tag{L-105418.7}
\]

## 6. Scope

The theorem pays the complete imaginary-axis edge, not the remote quarter arc.
It does not prove `QOPG105418`, the low-order critical sign, reverse-Rolle
descent or RH. Its contribution is to remove one full boundary edge from the
source-owned phase problem unconditionally.
# L-104539 — Positive-Fourier weighted horizontal-modulus defect is nonnegative

Claim ID: `L-104539`  
Status: **PROVED EXACT**  
Created: 2026-08-23  
Depends on: `L-104537`  
RH status: **not assumed**

Let `W` be a real even integrable function whose Fourier transform

\[
\widehat W(\xi)=\int_{\mathbb R}W(t)e^{it\xi}\,dt
\]

is pointwise nonnegative.  For real `h`, define

\[
\mathfrak H_W(h)
=\int_{\mathbb R}W(t)
\left(
 |\mathscr Z(h+it)|^2-|\mathscr Z(it)|^2
\right)dt.
\tag{L-104539.1}
\]

The complete source representation of `L-104537` gives

\[
\begin{aligned}
\mathfrak H_W(h)
={}&\iint_{\mathbb R^2}g(u)g(v)
\left[e^{h(u+v)}-1\right]
\widehat W(u-v)\,du\,dv.
\end{aligned}
\tag{L-104539.2}
\]

Applying the symmetry `(u,v)->(-u,-v)` and averaging yields

\[
\boxed{
\mathfrak H_W(h)
=
\iint_{\mathbb R^2}g(u)g(v)
\left[\cosh(h(u+v))-1\right]
\widehat W(u-v)\,du\,dv
\ge0.
}
\tag{L-104539.3}
\]

Thus the complete Riemann source is unconditionally horizontally
minimum-seeking after every positive-Fourier averaging, at every finite shift
`h`.

Expanding at `h=0` and using `L-104537.9`,

\[
\boxed{
\int_{\mathbb R}W(t)\mathcal L_2(t)\,dt
={1\over2}
\iint g(u)g(v)(u+v)^2\widehat W(u-v)\,du\,dv
\ge0.
}
\tag{L-104539.4}
\]

Equation (L-104539.4) recovers positive-definiteness of the Laguerre profile;
(L-104539.3) is its nonlinear finite-shift strengthening.

## What remains

Translation of `W` by an arbitrary ordinate multiplies `widehat W` by a
complex phase and destroys the pointwise source positivity used above.
Therefore (L-104539.3) does not itself control the defect at an individual zero
of `Xi'''`.

The exact missing interface is a source-qualified sampling theorem:

```text
CSAMP104580:
  transfer the proved positive-Fourier bulk horizontal defect to a density
  strictly greater than one half of the real Xi''' critical points.
```

Together with `L-104538`, any such density theorem gives a nonzero fixed-order
reverse-Rolle descent from Conrey's `Xi'''` result.

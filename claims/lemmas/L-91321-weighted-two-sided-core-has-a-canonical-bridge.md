# L-91321 — The weighted two-sided mean-zero core has a canonical one-dimensional bridge

Claim ID: `L-91321`  
Status: **PROVED EXACT ORTHOGONAL BRIDGE DECOMPOSITION**  
Created: 2026-08-13  
Depends on: `L-91320`, `L-91034`  
Upgrades: the unspecified bridge in `L-91034.13`  
RH status: **unproved**

## 1. Weighted half-line spaces

Fix `eta>0` and put

\[
 \mathcal H_{\eta,+}
 =L^2((0,\infty),e^{\eta t}dt),
 \qquad
 \mathcal H_{\eta,-}
 =L^2(( -\infty,0),e^{-\eta t}dt).
 \tag{L-91321.1}
\]

Let

\[
 \ell_+(f)=\int_0^\infty f(t)dt,
 \qquad
 \ell_-(f)=\int_{-\infty}^0 f(t)dt.
 \tag{L-91321.2}
\]

Their Riesz vectors are

\[
 q_+(t)=e^{-\eta t}\mathbf1_{t>0},
 \qquad
 q_-(t)=e^{\eta t}\mathbf1_{t<0},
 \tag{L-91321.3}
\]

and

\[
 \|q_+\|^2=\|q_-\|^2=\eta^{-1}.
 \tag{L-91321.4}
\]

Define the global weighted mean-zero space

\[
 \mathcal H_{\eta,0}
 =\left\{
 (f_+,f_-)\in\mathcal H_{\eta,+}\oplus\mathcal H_{\eta,-}:
 \ell_+(f_+)+\ell_-(f_-)=0
 \right\}.
 \tag{L-91321.5}
\]

## 2. Canonical bridge

Set

\[
 \boxed{
 b_\eta(t)
 =\eta e^{-\eta t}\mathbf1_{t>0}
 -\eta e^{\eta t}\mathbf1_{t<0}.
 }
 \tag{L-91321.6}
\]

Then

\[
 \ell_+(b_\eta)=1,
 \qquad
 \ell_-(b_\eta)=-1,
 \qquad
 \int_\mathbb R b_\eta(t)dt=0,
 \tag{L-91321.7}
\]

and

\[
 \boxed{\|b_\eta\|^2=2\eta.}
 \tag{L-91321.8}
\]

This fixes the scale, sign and norm of the bridge; no arbitrary auxiliary test
is needed.

## 3. Exact orthogonal decomposition

Let

\[
 \mathcal H_{\eta,+,0}=\ker\ell_+,
 \qquad
 \mathcal H_{\eta,-,0}=\ker\ell_-.
 \tag{L-91321.9}
\]

Since `q_+` and `q_-` are the Riesz vectors of the two defects,

\[
 \mathcal H_{\eta,+}
 =\mathcal H_{\eta,+,0}\oplus\mathbb Cq_+,
 \qquad
 \mathcal H_{\eta,-}
 =\mathcal H_{\eta,-,0}\oplus\mathbb Cq_-.
 \tag{L-91321.10}
\]

For `(f_+,f_-) in H_(eta,0)`, write

\[
 f_+=f_{+,0}+\eta\ell_+(f_+)q_+,
 \qquad
 f_-=f_{-,0}+\eta\ell_-(f_-)q_-.
\]

The global constraint gives

\[
 \ell_-(f_-)=-\ell_+(f_+),
\]

so the two Riesz components combine into a scalar multiple of `b_eta`.
Therefore

\[
 \boxed{
 \mathcal H_{\eta,0}
 =
 \mathcal H_{\eta,+,0}
 \ \widehat\oplus\
 \mathcal H_{\eta,-,0}
 \ \widehat\oplus\
 \mathbb C b_\eta,
 }
 \tag{L-91321.11}
\]

where every sum is orthogonal.

Combining this with `L-91320` proves the global delayed two-sided-plus-bridge
form-core statement intended in `L-91034.13`.

## 4. Explicit boundary transform

With the Fourier convention

\[
 \widehat f(u)=\int_\mathbb R f(t)e^{-iut}dt,
\]

the bridge has the rational transform

\[
 \boxed{
 \widehat b_\eta(u)
 =\frac{\eta}{\eta+iu}-\frac{\eta}{\eta-iu}
 =-\frac{2i\eta u}{\eta^2+u^2}.
 }
 \tag{L-91321.12}
\]

It is an odd Cauchy bridge with one vanishing moment.  Thus the bridge is no
longer a normalization placeholder: its boundary transform is explicit.  The
actual bridge row and column of the screw matrix still require the same
weighted-form continuity, Guinand--Weil admissibility, and exact gamma/pole
normalization declared by the parent route.

## 5. What this closes and what it does not

The theorem closes the Hilbert-space geometry of the one-dimensional bridge.
It does not sign the bridge row and column of the arithmetic screw Gram.  Those
entries must still be transported through the completed source comparison,
with their exact gamma/pole normalization retained.

## 6. Exact boundary

```text
half-line integral Riesz vectors                 EXACT
canonical bridge and norm                        EXACT
global orthogonal mean-zero decomposition        EXACT
delayed two-sided-plus-bridge form core           PROVED with L-91320
explicit rational bridge transform               EXACT
bridge row/column arithmetic positivity          OPEN
Riemann Hypothesis                               UNPROVED
```

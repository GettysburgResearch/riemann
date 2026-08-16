# L-93304 — The cubic scale-four wavelet has an exact First-Hermite heat-carrier decomposition

Claim ID: `L-93304`  
Status: **UNCONDITIONAL EXACT HEAT-WAVELET BRIDGE**  
Created: 2026-08-16  
Depends on: `L-93302`; the Fourier transform of a Gaussian  
RH status: **unproved**

## 1. First-Hermite kernel

For \(q>0\), let

\[
 h_q(u)
 =
 \left(1-\frac{u^2}{2q}\right)e^{-u^2/(4q)}.
 \tag{L-93304.1}
\]

Use the Fourier convention

\[
 \widehat f(t)=\int_{\mathbb R}f(u)e^{-itu}\,du.
\]

Differentiating the Gaussian transform gives

\[
 \boxed{
 \widehat h_q(t)
 =4\sqrt\pi\,q^{3/2}t^2e^{-qt^2}\ge0.
 }
 \tag{L-93304.2}
\]

Thus the first-Hermite kernel is exactly a positive heat derivative in carrier
space.

Put

\[
 \kappa_q(u)
 =\frac{h_q(u)}{4\sqrt\pi\,q^{3/2}}.
\]

Then

\[
 \widehat\kappa_q(t)=t^2e^{-qt^2}.
 \tag{L-93304.3}
\]

## 2. Logarithmic cubic wavelet

Define

\[
 G(u)=e^{-u}F(e^{-u})\mathbf1_{u\ge0}.
 \tag{L-93304.4}
\]

Its Fourier transform is the Mellin transform on the line \(\Re s=1\):

\[
 \boxed{
 \widehat G(t)=\widehat F(1+it).
 }
 \tag{L-93304.5}
\]

The two Mellin moments of `L-93302` give

\[
 \widehat G(0)=0,
 \qquad
 \widehat G'(0)=0.
 \tag{L-93304.6}
\]

## 3. Calderón reproducing formula

For \(t\ne0\),

\[
 \int_0^\infty t^2e^{-qt^2}\,dq=1.
\]

Since \(\widehat G(0)=0\), Plancherel and dominated convergence give the exact
\(L^2(\mathbb R)\) identity

\[
 \boxed{
 G
 =
 \int_0^\infty \kappa_q*G\,dq.
 }
 \tag{L-93304.7}
\]

Equivalently, the cubic scale-four wavelet is a continuous superposition of
First-Hermite heat derivatives.  This is a reproducing formula, not a heuristic
similarity of kernels.

## 4. Prime-carrier representation

Because

\[
 F(n/N)
 =\frac Nn\,G(\log(N/n)),
\]

the von Mangoldt wavelet satisfies

\[
 \boxed{
 S_F(N)
 =
 N\sum_{n\le N}\frac{\Lambda(n)}n
 G(\log(N/n)).
 }
 \tag{L-93304.8}
\]

Inserting (L-93304.7),

\[
 \boxed{
 S_F(N)
 =
 N\int_0^\infty
 \sum_{n\le N}\frac{\Lambda(n)}n
 (\kappa_q*G)(\log(N/n))\,dq.
 }
 \tag{L-93304.9}
\]

In carrier coordinates this is

\[
 \boxed{
 S_F(N)
 =
 \frac N{2\pi}
 \int_{\mathbb R}
 \widehat F(1+it)N^{it}
 \left(
 \sum_{n\le N}\frac{\Lambda(n)}{n^{1+it}}
 \right)dt.
 }
 \tag{L-93304.10}
\]

The compact support in \(G(\log(N/n))\) enforces \(n\le N\).

Equation (L-93304.9) is the exact structural bridge between the Q4 cubic
wavelet and First-Hermite carrier phases.

## 5. Relation to the frozen First-Hermite route

The frozen First-Hermite polynomial uses the critical normalization
\(\Lambda(n)n^{-1/2}\) and one prescribed carrier.  Equation (L-93304.9) uses
the absolutely normalized line \(\Re s=1\) and integrates all heat scales.
Therefore it does not silently import the still-open First-Hermite
one-carrier exclusion.

A valid cross-route closure would need an additional theorem transferring
arithmetic cancellation from the critical First-Hermite carrier family to the
line-one Calderón integral, or a direct critical-line version with its
low-carrier component explicitly controlled.

Block count and common-half-plane alignment do not provide such a transfer;
`R-93254` and `R-93300` remain binding.

## 6. Boundary

```text
First-Hermite Fourier transform                  exact
positive heat-derivative multiplier              exact
cubic log-wavelet Calderon formula               exact
prime carrier integral                           exact
critical First-Hermite one-carrier exclusion     not imported
carrier-to-balanced-dispersion estimate          open
Riemann Hypothesis                               unproved
```

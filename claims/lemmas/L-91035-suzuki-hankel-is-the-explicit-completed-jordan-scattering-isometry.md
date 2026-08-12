# L-91035 — Suzuki's Hankel transform is the explicit completed Jordan scattering isometry

Claim ID: `L-91035`  
Status: **IMPORTED PRIMARY-SOURCE THEOREM PLUS LOCAL SOURCE IDENTIFICATION — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-12  
Primary source: Masatoshi Suzuki, *A canonical system of differential equations arising from the Riemann zeta-function*, arXiv:1204.1827v2  
Depends on: main `L-91014`, branch `L-91030`, Suzuki Proposition 2.1 and Lemma 4.1  
RH status: **unproved**

## 1. The same positive Jordan coefficients occur in Suzuki's kernel

For `a>0`, define

\[
 q_a(n)=\prod_{p\mid n}(1-p^{-2a})>0
 \tag{L-91035.1}
\]

and

\[
 \boxed{
 c_a(n)=n^a q_a(n)
 =n^a\sum_{d\mid n}\frac{\mu(d)}{d^{2a}}.
 }
 \tag{L-91035.2}
\]

These are exactly Suzuki's coefficients `c_omega(n)` with `omega=a`.  Thus the
arithmetic channel in his completed Hankel kernel is the same generalized-
Jordan source used throughout `L-91014`--`L-91033`, not an analogous but
different sequence.

Its Dirichlet series is

\[
 \boxed{
 \sum_{n\ge1}\frac{c_a(n)}{n^s}
 =\frac{\zeta(s-a)}{\zeta(s+a)}
 }
 \tag{L-91035.3}
\]

in its absolute half-plane.

## 2. The explicit archimedean kernel

Suzuki defines, for `0<x<1`,

\[
\begin{aligned}
 g_a(x)
 =\frac{(2\pi)^a}{\Gamma(a)}\Bigg[
 &x^{2-a}(1-x^2)^{a-1}\\
 &-a x^{a-1}
  \int_{x^2}^1
   t^{1/2-a}(1-t)^{a-1}dt
 \Bigg],
\end{aligned}
\tag{L-91035.4}
\]

and `g_a(x)=0` for `x>1`.  Its Mellin transform is the completed gamma/pole
ratio appearing in the xi functional equation.

The completed arithmetic--archimedean impulse is

\[
 \boxed{
 h_a(x)
 =\frac1x\sum_{n\le x}c_a(n)g_a(n/x)
 \quad(x>1),
 \qquad
 h_a(x)=0\quad(0<x<1).
 }
 \tag{L-91035.5}
\]

This is an exact multiplicative co-Poisson synthesis:

```text
positive Jordan coefficients c_a(n)
  shifted through the local gamma kernel g_a
  and recombined before taking a norm.
```

No termwise analytic continuation of the positive Dirichlet series is used.

## 3. Exact completed scattering multiplier

Put

\[
 \Theta_a(z)
 =\frac{\xi(1/2-a-iz)}{\xi(1/2+a-iz)}.
 \tag{L-91035.6}
\]

Suzuki's Mellin identity is

\[
 \boxed{
 \int_0^\infty
 h_a(x)x^{1/2+iz}\frac{dx}{x}
 =\Theta_a(z)
 }
 \tag{L-91035.7}
\]

initially in the absolute half-plane and then by the stated analytic
continuation.

For real `z`, the functional equation gives

\[
 |\Theta_a(z)|=1,
 \qquad
 \Theta_a(z)\Theta_a(-z)=1.
 \tag{L-91035.8}
\]

For every

\[
 a>\frac12,
\]

`Theta_a` is a meromorphic inner function in the upper half-plane
unconditionally.

## 4. The completed multiplicative Hankel isometry

Define

\[
 \boxed{
 (\mathsf H_af)(x)
 =\int_0^\infty h_a(xy)f(y)dy.
 }
 \tag{L-91035.9}
\]

Suzuki proves that, for `a>1/2`, this extends to an isometry on
`L^2((0,infinity),dx)`.  If `M_(1/2)` denotes the shifted Mellin transform, then

\[
 \boxed{
 (\mathcal M_{1/2}\mathsf H_af)(z)
 =\Theta_a(z)(\mathcal M_{1/2}f)(-z).
 }
 \tag{L-91035.10}
\]

Because of `(L-91035.8)`, the extension is a unitary involution:

\[
 \boxed{
 \mathsf H_a^*=\mathsf H_a,
 \qquad
 \mathsf H_a^2=I.
 }
 \tag{L-91035.11}
\]

In spectral coordinates it is simply

\[
 \mathsf S_a=M_{\Theta_a}\mathsf R,
 \qquad
 (\mathsf RF)(z)=F(-z).
 \tag{L-91035.12}
\]

This is an explicit positive-metric two-sided Hardy scattering realization.

## 5. Relation to the bosonic product system

`L-91030` proves that

\[
 Q_a(s+\bar t)
 =\left\langle
  \operatorname{Exp}(v_{a,s}),
  \operatorname{Exp}(v_{a,t})
 \right\rangle
 \tag{L-91035.13}
\]

in the prime-power bosonic Fock space.  Equations `(L-91035.2)` and
`(L-91035.5)` show that Suzuki's physical impulse is built from the coefficient
sequence of that same coherent kernel.  The gamma kernel `g_a` is the local
archimedean completion, and `(L-91035.10)` is the resulting global scattering
isometry.

Thus the previously informal arrow

```text
positive generalized-Jordan source
  + completed gamma/pole factor
  -> two-sided unitary xi scattering
```

has a resident explicit operator:

\[
 \boxed{\mathsf H_a.}
\]

## 6. What this does and does not complete

This theorem **does complete the amplitude-level source/scattering
intertwiner**.  It gives:

```text
an explicit arithmetic kernel h_a;
a positive-metric unitary involution H_a;
exact causal/anti-causal Hardy transport;
exact incorporation of the gamma and pole factors;
no hidden signed auxiliary state.
```

It does **not** prove the screw/Weil Gram positive.  The target of main
`T-91006` and corrected `T-91008` is not the scattering amplitude `Theta_a`; it
is a logarithmic-derivative/radial-curvature form built from that amplitude.
Unitarity of a family of scattering matrices does not sign its Wigner--Smith
curvature.  This distinction is isolated in `L-91037`.

Nor does `(L-91035.13)` by itself define an isometry from the entire bosonic
Fock space onto `L^2((0,infinity))`.  It identifies the coherent kernel and the
vacuum transfer amplitude.  Claiming a full Fock-vector embedding from these
matrix coefficients alone would be another polarization error.

## 7. Strategic consequence

The final task should no longer be phrased as constructing the completed
source-to-Hardy **amplitude** embedding; Suzuki already constructed it for every
safe `a>1/2`.

The actual open theorem is the tangent lift:

```text
lift the first Poisson chaos / logarithmic derivative of H_a
into the delayed two-sided Hardy reserve with positive metric,
while preserving the completed gamma/pole channel.
```

That tangent lift is RH-bearing.

## 8. Source boundary

Imported directly from Suzuki:

```text
c_a(n), g_a, h_a;
Mellin identity for Theta_a;
innerness for a>1/2;
Hankel isometry and Mellin intertwining.
```

Local identification:

```text
c_a=n^a q_a uses the repository Jordan source;
Q_a is the repository Fock coherent kernel;
H_a is the explicit completed amplitude colligation;
the remaining CJHI is a tangent/curvature lift, not an amplitude lift.
```

## 9. Exact boundary

```text
positive Jordan coefficient identity                 EXACT
Suzuki completed Hankel scattering isometry           IMPORTED PROVED
amplitude-level source/gamma/Hardy embedding           CLOSED
full Fock-vector-to-Hardy isometry                     NOT IMPLIED
Wigner--Smith / screw tangent positivity               OPEN / RH-EQUIVALENT
Riemann Hypothesis                                     UNPROVED
```

# L-105351 — In a symmetric Xi window the boundary gate is one origin Stieltjes moment sequence

Claim ID: `L-105351`  
Status: **PROVED EXACT FINITE-WINDOW REDUCTION — XI SIGN OPEN**  
Created: 2026-08-23  
Depends on: `L-105214`, `L-105217`, `L-105329`, `L-105350`; the classical Stieltjes moment theorem  
RH status: **not assumed**

## 1. Boundary Cauchy function and fixed anchor

Let `F` be entire, real on the real axis, and of definite parity. Let `Omega`
be a bounded regular domain invariant under both conjugation and `z -> -z`,
and assume that a real interval `I` containing `0` lies in `Omega`. Put

\[
H(z)=H_{F,\Omega}(z)
={1\over2\pi i}\int_{\partial\Omega}
{F(\zeta)/F'(\zeta)\over\zeta-z}\,d\zeta.
\tag{L-105351.1}
\]

Because `F/F'` is odd and the interior critical-pole sum is odd, `H` is odd:

\[
H(-z)=-H(z).
\tag{L-105351.2}
\]

The source-owned anchor is therefore fixed at `x_*=0`.

## 2. One even moment sequence

Define

\[
\boxed{
\beta_n
={H^{(2n+1)}(0)\over(2n+1)!}
={1\over2\pi i}\int_{\partial\Omega}
{F(\zeta)/F'(\zeta)\over\zeta^{2n+2}}\,d\zeta,
\qquad n\ge0.
}
\tag{L-105351.3}
\]

Oddness makes all intervening Hamburger moments vanish. After reordering even
and odd monomials, the anchor matrix of `L-105350` splits into the two Hankel
families

\[
\boxed{
\mathsf E_k=[\beta_{r+s}]_{r,s=0}^{k-1},
\qquad
\mathsf O_k=[\beta_{r+s+1}]_{r,s=0}^{k-1}.
}
\tag{L-105351.4}
\]

Consequently,

\[
\boxed{
\mathscr L_H\succeq0\text{ on every finite real packet in }I
\Longleftrightarrow
\mathsf E_k\succeq0\text{ and }\mathsf O_k\succeq0
\quad(k\ge1).
}
\tag{L-105351.5}

This is the Stieltjes moment criterion for the single sequence `beta_n`.

## 3. Positive Stieltjes representation

Equivalently, there is a finite positive compactly supported measure `nu` on
`[0,infinity)` such that

\[
\boxed{
\beta_n=\int_0^\infty s^n\,d\nu(s)
}
\tag{L-105351.6}
\]

and

\[
\boxed{
H(z)=z\int_0^\infty{d\nu(s)\over1-sz^2}
}
\tag{L-105351.7}
\]

throughout the upper-half-plane continuation. Indeed, the Hamburger measure
of `L-105350` is symmetric and `nu` is its pushforward under `t -> t^2`.
Conversely, splitting each `s>0` atom equally between `t=+-sqrt(s)` recovers a
positive symmetric Hamburger measure.

Thus the complete boundary gate in a parity-symmetric Xi window is the claim
that one explicit contour sequence is Stieltjes.

## 4. Safe-axis scalar

For real `y` with `iy in Omega`, oddness gives the exact identity

\[
\boxed{
{H(iy)\over iy}
={1\over2\pi i}\int_{\partial\Omega}
{F(\zeta)/F'(\zeta)\over\zeta^2+y^2}\,d\zeta.
}
\tag{L-105351.8}
\]

Under the equivalent boundary gate,

\[
\boxed{
{H(iy)\over iy}
=\int_0^\infty{d\nu(s)\over1+s y^2}.
}
\tag{L-105351.9}
\]

Hence the boundary Cauchy function is encoded by one literal safe-axis
Stieltjes transform. This is the precise coordinate that a future import from
safe-axis Xi positivity must match. Positivity of the raw `Xi` Pick coordinate
is not silently identified with (L-105351.9).

## 5. Fixed-anchor contour squares

For a real polynomial `Q(u)=sum_(r=0)^(k-1) q_r u^r`,

\[
\boxed{
\begin{aligned}
q^T\mathsf L_k(0)q
={1\over2\pi i}\int_{\partial\Omega}
{F(\zeta)\over F'(\zeta)}
\left(
\sum_{r=0}^{k-1}{q_r\over\zeta^{r+1}}
\right)^2d\zeta.
\end{aligned}
}
\tag{L-105351.10}
\]

Therefore arbitrary separated Cauchy packets in `BCVH105330` may be replaced,
without loss, by all Laurent-polynomial squares at the single anchor zero.
The replacement is exact only because all orders and analyticity are retained.

## 6. Polynomial exterior-residue calibration

Let `p` be a centered real polynomial of degree `n`, and let a symmetric inner
window contain some but not all simple critical points. For the exterior
positive critical points `c>0`, the exact nested-window decomposition gives

\[
H_{p,\Omega}(z)
={z\over n}
+\sum_{\substack{p'(c)=0\\c>0,\ c\notin\Omega}}
\rho_c\left({1\over z-c}+{1\over z+c}\right).
\tag{L-105351.11}
\]

Hence

\[
\boxed{
H_{p,\Omega}(z)
=z\left[
{1\over n}
+\sum_{c>0,\ c\notin\Omega}
{-2\rho_c/c^2\over1-z^2/c^2}
\right].
}
\tag{L-105351.12}
\]

The Stieltjes measure is therefore exactly

\[
\boxed{
\nu={1\over n}\delta_0
+\sum_{c>0,\ c\notin\Omega}
{-2\rho_c\over c^2}\,\delta_{1/c^2}.
}
\tag{L-105351.13}
\]

If every crossed exterior residue is nonpositive, this measure is positive and
the inner boundary kernel is PSD. This is the one-anchor moment form of the
nested-window transport theorem `L-105217`.

## 7. New boundary gate

Define

```text
OASH105350:
  in every regular symmetric window of the exact Xi exhaustion, the two
  origin Hankel families E_k and O_k in (L-105351.4) are PSD for every k.
```

Then, window by window,

\[
\boxed{
\mathrm{OASH105350}
\Longleftrightarrow
\mathrm{BCVH105330}
\Longleftrightarrow
\text{the all-packet PSD component of BRP105220}.
}
\tag{L-105351.14}
\]

`OASH105350` is not proved for the last defective Xi derivative.

## 8. Scope

The theorem does not estimate `beta_n`, establish a Stieltjes representation
for the actual Xi boundary function, or control the critical/nonreal part of
the parent decomposition. The hierarchy is infinite; bounded derivative data
are insufficient. RH remains unproved.

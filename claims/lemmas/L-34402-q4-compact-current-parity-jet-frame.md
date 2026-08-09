# L-34402 — Uniform parity jet-frame domination of the compact Q=4 current

Claim ID: `L-34402`  
Title: On the complete critical line, the compact Q=4 current is bounded with coefficient one half by the two parity currents plus their bare source energies  
Status: **PROPOSED COMPLETE EXACT FINITE-TRIGONOMETRIC THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: PR #263 parity polynomial; PR #342 compact Q=4 innovation source  
Scope: exact critical-line jet-frame inequality and its finite-delay Hilbert consequence; no final Selberg/recurrence composition or RH conclusion

## 1. The three source polynomials

Put

\[
L=\log2,
\qquad z=2^{-s}.
\]

On the critical line `Re(s)=1/2`,

\[
|z|=2^{-1/2}.
\tag{L-34402.1}
\]

Retain

\[
p(z)=(1-z)(1-2z)(1-\sqrt2 z)^2
\tag{L-34402.2}
\]

and the parity pair

\[
B_+(s)=p(z)F(s),
\qquad
B_-(s)=p(-z)F(s),
\tag{L-34402.3}
\]

for an arbitrary differentiable complex carrier `F`.

The compact Q=4 source polynomial is

\[
T(z)=(1-z)(1-4z^2),
\qquad
B_\circ(s)=T(z)F(s).
\tag{L-34402.4}
\]

Define the three currents by differentiation in `s`:

\[
q_+=B_+',
\qquad q_-=B_-',
\qquad q_\circ=B_\circ'.
\tag{L-34402.5}
\]

No arithmetic property of `F` is used in the theorem.

## 2. Two-dimensional jet form

Put

\[
u=F'(s),
\qquad v=L F(s).
\]

Since `z'=-Lz`, one has exactly

\[
q_+
=p(z)u-zp'(z)v,
\tag{L-34402.6}
\]

\[
q_-
=p(-z)u+zp'(-z)v,
\tag{L-34402.7}
\]

and

\[
q_\circ
=T(z)u-zT'(z)v.
\tag{L-34402.8}
\]

Moreover

\[
|B_+|^2+|B_-|^2
={|p(z)|^2+|p(-z)|^2\over L^2}|v|^2.
\tag{L-34402.9}
\]

The elementary inequality `log 2<7/10` gives

\[
L^2<{1\over2},
\qquad {1\over L^2}>2.
\tag{L-34402.10}
\]

Therefore it is enough to prove the stronger algebraic inequality

\[
\boxed{
2|T(z)u-zT'(z)v|^2
\le
|p(z)u-zp'(z)v|^2
+|p(-z)u+zp'(-z)v|^2
+2\bigl(|p(z)|^2+|p(-z)|^2\bigr)|v|^2.
}
\tag{L-34402.11}
\]

## 3. Hermitian matrix

Let

\[
A(z)=
\begin{pmatrix}
 p(z)&-zp'(z)\\
 p(-z)&zp'(-z)
\end{pmatrix},
\qquad
 t(z)=\begin{pmatrix}T(z)&-zT'(z)\end{pmatrix}.
\]

Equation (L-34402.11) is equivalent to

\[
\boxed{M(z)\succeq0,}
\tag{L-34402.12}
\]

where

\[
M(z)=A(z)^*A(z)
+2\begin{pmatrix}0&0\\0&|p(z)|^2+|p(-z)|^2\end{pmatrix}
-2t(z)^*t(z).
\tag{L-34402.13}
\]

On the circle (L-34402.1), write

\[
z=2^{-1/2}e^{i\theta},
\qquad x=\cos\theta\in[-1,1].
\]

Direct exact expansion gives the first principal minor

\[
\boxed{
\begin{aligned}
Q_1(x)={}&32x^4-16\sqrt2 x^3
 +(92+96\sqrt2)x^2\\
&+18\sqrt2 x+9,
\end{aligned}}
\tag{L-34402.14}
\]

and

\[
\boxed{\det M(z)=8Q_2(x),}
\tag{L-34402.15}
\]

with

\[
\boxed{
\begin{aligned}
Q_2(x)={}&256x^8-128\sqrt2 x^7
 +(976+1344\sqrt2)x^6\\
&-(960+224\sqrt2)x^5
 +(7912+4776\sqrt2)x^4\\
&+(1560+552\sqrt2)x^3
 +(-420+78\sqrt2)x^2\\
&+(-216+72\sqrt2)x
 +(117+54\sqrt2).
\end{aligned}}
\tag{L-34402.16}
\]

Thus the theorem is reduced to two finite real-polynomial positivity statements on `[-1,1]`.

## 4. Exact Bernstein certificate

For a degree-`d` polynomial `Q`, its Bernstein representation on an interval `[a,b]` is

\[
Q(a+(b-a)t)=
\sum_{r=0}^d c_r\binom dr t^r(1-t)^{d-r}.
\]

If every `c_r` is positive, then `Q>0` throughout the interval.

### 4.1 First principal minor

On each of

\[
[-1,0],\qquad[0,1],
\]

the degree-four Bernstein coefficients of `Q_1` are all positive.

For `[-1,0]` they are

\[
\begin{aligned}
&133+94\sqrt2,
&&55+{77\sqrt2\over2},
&&{73\over3}+7\sqrt2,\\
&9-{9\sqrt2\over2},
&&9.
\end{aligned}
\tag{L-34402.17}
\]

For `[0,1]` they are

\[
\begin{aligned}
&9,
&&9+{9\sqrt2\over2},
&&{73\over3}+25\sqrt2,\\
&55+{115\sqrt2\over2},
&&133+98\sqrt2.
\end{aligned}
\tag{L-34402.18}
\]

The only coefficient not manifestly a sum of positive terms is

\[
9-{9\sqrt2\over2}>0
\]

because `sqrt(2)<2`. Hence

\[
\boxed{Q_1(x)>0\quad(-1\le x\le1).}
\tag{L-34402.19}
\]

### 4.2 Determinant

Split `[-1,1]` into

\[
[-1,-1/2],\ [-1/2,0],\ [0,1/2],\ [1/2,1].
\tag{L-34402.20}
\]

The degree-eight Bernstein coefficients of `Q_2` on **each** of these four intervals are all strictly positive elements of `Q(sqrt(2))`.

The full 36-coefficient exact table is generated and retained by

```text
experiments/X-34401-q4-compact-parity-synthesis/verify_jet_frame.py
```

and no floating calculation enters the certificate. For orientation, the smallest exact coefficient on each interval is respectively

\[
{1863\over4}+296\sqrt2,
\qquad
117+54\sqrt2,
\tag{L-34402.21}
\]

\[
{3849\over56}+{1983\sqrt2\over28},
\qquad
{2319\over4}+490\sqrt2,
\tag{L-34402.22}
\]

all manifestly positive. Consequently

\[
\boxed{Q_2(x)>0\quad(-1\le x\le1).}
\tag{L-34402.23}
\]

Equations (L-34402.19) and (L-34402.23) imply `M(z)` is positive definite on the complete critical circle.

## 5. Critical-line jet-frame theorem

Substituting the stronger algebraic inequality (L-34402.11) into (L-34402.9)--(L-34402.10) yields

\[
\boxed{
2|q_\circ(s)|^2
\le
|q_+(s)|^2+|q_-(s)|^2
+|B_+(s)|^2+|B_-(s)|^2
}
\tag{L-34402.24}
\]

for every

\[
\Re s={1\over2}
\]

at which the displayed functions are defined.

The inequality is uniform in the vertical frequency and in the carrier `F`.

This is materially stronger than a finite synthesis coefficient estimate: it uses the **joint current/bare-source jet geometry**, so derivative-filter gauges are already inside the right-hand side rather than emitted as a separate current-scale state.

## 6. Finite-delay Hilbert consequence

All entries of `A(z)` and `t(z)` are finite polynomials in `z`. Therefore (L-34402.12) is a positive matrix trigonometric-polynomial symbol on the critical circle.

By Fourier/Toeplitz compression, its convolution quadratic form is nonnegative on every finitely supported block sequence. Equivalently, after partitioning logarithmic physical time into cells of length `log 2`, (L-34402.24) holds for the corresponding full finite-support `L^2` block sums.

For a causal prefix, zero extension changes only a fixed number of terminal cells determined by the polynomial degrees. Hence the same estimate holds on every finite prefix with one explicit fixed-width collar.

This conclusion is purely finite-filter Hilbert algebra. It does not invoke RH, PNT, or a source asymptotic.

## 7. Relation to the live Q=4 frontier

For the actual odd Euler carrier

\[
F(s)=\mathcal O(s),
\]

the left side is the compact Q=4 current of PR #342.

The right side consists exactly of

```text
paired parity current energy
+
paired parity bare-source energy.
```

These are the two source species already present in the PR #334/#337 reflected Selberg–Kummer ledger. Thus the balanced compact innovation no longer requires a new current-space transference theorem: it is uniformly embedded into the existing parity **jet** frame with coefficient one half.

What remains is the global no-double-spend composition with the positive paired Selberg forcing, reconstructed Möbius boundary, neutral Q=4 principal state, and fixed endpoint collar.

## 8. Proof boundary

Closed exactly here:

1. complete critical-line two-jet formulas;
2. explicit Hermitian matrix reduction;
3. exact principal-minor polynomial;
4. exact determinant polynomial;
5. finite Bernstein positivity certificate;
6. uniform pointwise jet-frame inequality (L-34402.24);
7. finite-filter Hilbert/Toeplitz consequence up to a fixed causal collar.

Still open:

1. final source-convolved reflected reserve accounting without double spending;
2. composition with PR #341's neutral terminal-state ledger into one coefficient-one recurrence;
3. RH.

The reviewer receives the complete polynomial certificate; no positivity step is left as an exercise.

# L-16228 — Explicit rational phase partition and Airy transition ledger

Claim ID: `L-16228`  
Status: **PROVED EXACT PHASE GEOMETRY**  
Authoring agent: `gpt56-pro-12`  
Created: 2026-08-01  
Depends on: the CCM scale `gamma=2 pi lambda^2`; the Dunster radial phase in `L-16212`  
Scope: outward-rounded phase constants for the directed CCM radial replay

## 1. Purpose

The asymptotic radial arguments in `L-16212`, `L-16223`, `L-16226`, and
`L-16227` used compact phase partitions and an Airy neighborhood without
publishing one exact rational partition. This lemma supplies that ledger.

It does not bound the amplitude error between a PSWF and its Dunster template.
That is a separate interval-ODE primitive in `L-16229`.

## 2. Radial frequency map

For

\[
 0\leq s=\sigma^2\leq\frac18,
\]

define

\[
 \omega_s(z)
 =z\sqrt{\frac{z^2-s}{z^2-1}},
 \qquad z>1.                                      \tag{L-16228.1}
\]

This is the logarithmic derivative of the Dunster radial action:

\[
 \frac{d}{dt}\xi_\sigma(e^t)=\omega_s(e^t).       \tag{L-16228.2}
\]

Put \(y=z^2\). The fold is determined by

\[
 y_f=1+\sqrt{1-s},
 \qquad
 \omega_f=1+\sqrt{1-s}.                           \tag{L-16228.3}
\]

Hence

\[
 \frac{15}{8}<y_f\leq2,
 \qquad
 \frac{15}{8}<\omega_f\leq2.                      \tag{L-16228.4}
\]

## 3. One exact stationary-frequency window

Take

\[
 \boxed{J=\left[\frac{17}{8},\frac94\right].}      \tag{L-16228.5}
\]

For every \(\omega\in J\), the first Poisson sample has exactly two stationary
points. Their squared radial coordinates are

\[
 y_\pm
 =
 \frac{s+\omega^2
 \pm\sqrt{(s+\omega^2)^2-4\omega^2}}2.             \tag{L-16228.6}
\]

The following rational containments are valid:

\[
 1<y_-<\frac32,
 \qquad
 3<y_+<4.                                         \tag{L-16228.7}
\]

For example, the quadratic

\[
 p(y)=y^2-(s+\omega^2)y+\omega^2
\]

satisfies \(p(1)=1-s>0\), its vertex lies above \(1\), and

\[
 p(4)
 \geq
 16-\frac12-\frac{243}{16}
 =\frac5{16}>0.                                   \tag{L-16228.8}
\]

The remaining endpoint signs locate the two roots in the stated intervals.

## 4. Exact nondegeneracy moat

At a stationary point, with

\[
 \Delta=(s+\omega^2)^2-4\omega^2,
\]

the phase second derivative in logarithmic position is

\[
 \left|\phi_{tt}\right|
 =
 \frac{y\sqrt{\Delta}}{(y-1)\omega}.               \tag{L-16228.9}
\]

Uniformly on the declared box,

\[
 \frac{\Delta}{\omega^2}
 \geq
 \omega^2-4
 \geq
 \frac{33}{64}
 >
 \left(\frac{11}{16}\right)^2.                    \tag{L-16228.10}
\]

Both roots lie in \(1<y<4\), so \(y/(y-1)\geq4/3\). Therefore

\[
 \boxed{\left|\phi_{tt}\right|\geq\frac{11}{12}.}  \tag{L-16228.11}
\]

This is the stationary-phase denominator used by the directed replay.

## 5. Higher-alias gap

For the \(k\)-th Poisson alias, \(k\geq2\), the radial argument is \(kz\).
The frequency map is increasing once its argument exceeds the fold. Therefore
the least possible higher-alias frequency occurs at \(k=2,z=1\):

\[
 \omega_s(2)^2=\frac{4(4-s)}3.                     \tag{L-16228.12}
\]

The exact comparison

\[
 \frac{4(4-\frac18)}3
 -
 \left(\frac94+\frac1{50}\right)^2
 =
 \frac{413}{30000}>0                              \tag{L-16228.13}
\]

gives the rational derivative moat

\[
 \boxed{
 \left|\partial_t\phi_{k,\pm}\right|
 \geq\frac1{50},
 \qquad k\geq2,\quad\omega\in J.}                  \tag{L-16228.14}
\]

Thus every higher alias is nonstationary on \(J\).

## 6. Fold cubic coefficient

Let

\[
 a=\sqrt{1-s}.
\]

At the fold,

\[
 \phi'''(t_f)
 =
 \frac{d^2}{dt^2}\omega_s(e^t)\bigg|_{t=t_f}
 =
 4+\frac4a.                                       \tag{L-16228.15}
\]

Since \(7/8<a\leq1\),

\[
 \boxed{
 8\leq\phi'''(t_f)\leq\frac{60}{7}.}               \tag{L-16228.16}
\]

The fold is uniformly nondegenerate.

## 7. Directed Airy radius

Let \(R\geq16^3\), and let the exact integer \(q\) satisfy

\[
 q^3\leq R<(q+1)^3.                                \tag{L-16228.17}
\]

Use the logarithmic Airy box

\[
 \boxed{|t-t_f|\leq q^{-1}}                        \tag{L-16228.18}
\]

and the frequency box

\[
 \boxed{|\omega-\omega_f|\leq9q^{-2}.}             \tag{L-16228.19}
\]

Because \(q\geq16\),

\[
 e^{-1/8}>\frac78,\qquad e^{1/8}<\frac87.
\]

Together with (L-16228.4), the Airy box is contained in the rational rectangle

\[
 \frac{105}{64}\leq y=e^{2t}\leq\frac{16}{7},
 \qquad
 0\leq s\leq\frac18.                               \tag{L-16228.20}
\]

On this rectangle,

\[
 \omega_{tt}
 =
 \sqrt{\frac{y(y-s)}{y-1}}\,
 \frac{
  2s^2y+s^2-2sy^3+2sy^2-6sy+y^4-2y^3+4y^2
 }{
  (y-s)^2(y-1)^2
 }.                                                 \tag{L-16228.21}
\]

An exact rational interval evaluation on the fixed \(64\times32\) partition of
(L-16228.20) proves

\[
 \boxed{5\leq\omega_{tt}\leq18.}                   \tag{L-16228.22}
\]

No floating-point evaluation enters this step. The checker in `X-16204`
reconstructs all 2,048 boxes using `fractions.Fraction`; it proves the squared
bounds \(25\leq\omega_{tt}^2\leq324\).

Taylor's theorem and (L-16228.22) imply (L-16228.19) from (L-16228.18).
The chosen radii are deliberately wider than the canonical Airy scales.

## 8. Finite directed partition

For each fixed mode and retained alias, the proof producer uses:

1. the Airy box (L-16228.18);
2. the two first-alias stationary branches over \(J\), with moat
   \(11/12\);
3. the higher-alias nonstationary pieces, with moat \(1/50\);
4. compact tails separated at exact rational radial coordinates;
5. the endpoint channels and infinite alias remainder of `L-16221`.

All phase derivatives and endpoint locations are evaluated into outward rational
intervals. A piece is accepted only if one of the declared moats remains
strict.

## 9. Production certificate fields

One phase certificate contains:

```text
sigma_squared_upper       <= 1/8
omega_window              [17/8,9/4]
stationary_second_moat    <= 11/12
higher_alias_gap          <= 1/50
fold_third_interval       [8,60/7]
R and exact cube-root q
Airy t-radius             >= 1/q
Airy frequency radius     >= 9/q^2
SHA-256 of the interval phase ledger
```

`X-16204` checks every rational inequality and independently reconstructs the
Airy-grid enclosure.

## 10. Proof boundary

This lemma closes the phase geometry and Airy radius. It does not provide a
numerical coefficient in Dunster's hidden \(O(\gamma^{-1})\) envelope.
The production route obtains that coefficient from the interval-ODE
a-posteriori certificate of `L-16229`.

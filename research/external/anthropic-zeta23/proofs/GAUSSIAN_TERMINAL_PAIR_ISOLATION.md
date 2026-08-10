# Gaussian terminal-pair isolation removes the Gram-collapse escape

Status: **PROPOSED COMPLETE ZERO-SIDE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Scope: complete zero-side geometry and admissible Weil-test construction; no arithmetic lower floor and no RH claim  
Depends on: `OFFLINE_PAIR_SPECTRUM.md`, `FINITE_OFFLINE_ISOLATION.md`, the Riemann–von Mangoldt zero count, and the standard Weil explicit-formula test class

## 1. Centered zero coordinates

Write a nontrivial zero as

\[
\rho=\frac12+y+ix,
\qquad -\frac12<y<\frac12,
\]

and encode it by the centered coordinate

\[
z=x+iy.
\]

The functional-equation reflection is

\[
z^\sharp=x-iy.
\]

Let `Z+` denote the distinct centered zero coordinates with `y>0`, one representative from each reflected off-line pair, and retain the zero multiplicity `m_z`.

PRs #363–#364 show that a reflected pair contributes the exact indefinite block whose antisymmetric target values

\[
F(z)=1,
\qquad F(z^\sharp)=-1
\]

have Weil value `-2m_z`.

The exact-cardinal construction of PR #364 kills finitely many nuisance evaluations but can have a very large inverse-Gram cost. The theorem below shows that exact cardinalization is unnecessary: one can always choose an off-line pair for which a two-section Gaussian antisymmetric test has vanishing norm and vanishing complete nuisance leakage.

## 2. Gaussian evaluation kernel

For `sigma>0`, put

\[
v_\sigma(u)=e^{-u^2/(2\sigma^2)}
\]

and define the evaluation kernel

\[
\boxed{
K_\sigma(z,w)
=\int_{\mathbb R}v_\sigma(u)e^{i(z-\overline w)u}\,du
=\sqrt{2\pi}\,\sigma
 e^{-\sigma^2(z-\overline w)^2/2}.
}
\tag{GTP.1}
\]

Its normalized correlation has the exact Euclidean form

\[
\boxed{
\frac{|K_\sigma(z,w)|}
{\sqrt{K_\sigma(z,z)K_\sigma(w,w)}}
=e^{-\sigma^2|z-w|^2/2}.
}
\tag{GTP.2}
\]

Indeed, if `z=x+iy` and `w=x'+id`, then

\[
K_\sigma(z,z)=\sqrt{2\pi}\sigma e^{2\sigma^2y^2}
\]

and taking real parts of `(z-conj(w))^2` gives (GTP.2).

Consequently every fixed finite packet of distinct zero coordinates becomes asymptotically orthogonal as `sigma->infinity`. In particular, there is no intrinsic finite-packet Gram collapse in the Gaussian frame.

## 3. The raw antisymmetric pair interpolant

Fix one off-line coordinate

\[
z=x+iy,
\qquad y>0.
\]

Put

\[
A_\sigma=K_\sigma(z,z)
=\sqrt{2\pi}\sigma e^{2\sigma^2y^2},
\]

\[
C_\sigma=K_\sigma(z,z^\sharp)
=\sqrt{2\pi}\sigma.
\]

Define

\[
\boxed{
F_{\sigma,z}(w)
=\frac{K_\sigma(w,z)-K_\sigma(w,z^\sharp)}
{A_\sigma-C_\sigma}.
}
\tag{GTP.3}
\]

Then exactly

\[
\boxed{
F_{\sigma,z}(z)=1,
\qquad
F_{\sigma,z}(z^\sharp)=-1.
}
\tag{GTP.4}
\]

The function satisfies the reflection symmetry

\[
\boxed{
F_{\sigma,z}(w^\sharp)
=-\overline{F_{\sigma,z}(w)}.
}
\tag{GTP.5}
\]

Its Gaussian-frame norm is

\[
\boxed{
\|F_{\sigma,z}\|_\sigma^2
=\frac{2}{A_\sigma-C_\sigma}
=\frac{2}{\sqrt{2\pi}\sigma
 (e^{2\sigma^2y^2}-1)}
\longrightarrow0.
}
\tag{GTP.6}
\]

Thus the target pair keeps the fixed Weil moat `-2m_z` while the test norm tends to zero.

## 4. Exact nuisance exponent and the threat relation

Let

\[
w=x'+id,
\qquad d\ge0,
\]

be another right-side or on-line zero coordinate. From (GTP.1)–(GTP.3),

\[
|F_{\sigma,z}(w)|
\le
\frac{2}{1-e^{-2\sigma^2y^2}}
\exp\left(\frac{\sigma^2}{2}\Phi_z(w)\right),
\tag{GTP.7}
\]

where

\[
\boxed{
\Phi_z(w)
=(d-y)(d+3y)-(x'-x)^2.
}
\tag{GTP.8}
\]

If `d<=y`, then `Phi_z(w)<0` for every distinct coordinate `w`. Therefore only a **strictly deeper** off-line zero can obstruct Gaussian isolation.

Define a directed threat edge

\[
\boxed{
z\longrightarrow w}
\]

when

\[
\boxed{
d>y,
\qquad
(x'-x)^2\le(d-y)(d+3y).
}
\tag{GTP.9}
\]

Since `0<d,y<1/2`, every threat edge obeys

\[
\boxed{
(x'-x)^2<2(d-y).
}
\tag{GTP.10}
\]

A coordinate with no outgoing threat edge will be called **terminal**.

## 5. A terminal off-line pair always exists

Assume RH is false, so `Z+` is nonempty.

Suppose, for contradiction, that no coordinate in `Z+` is terminal. Starting from any `z_0=x_0+iy_0`, choose recursively an outgoing threat

\[
z_n\to z_{n+1}.
\]

Write `z_n=x_n+iy_n`. The depths increase strictly:

\[
y_0<y_1<y_2<\cdots<\frac12.
\]

By (GTP.10), for every `N`,

\[
\sum_{n=0}^{N-1}(x_{n+1}-x_n)^2
<2\sum_{n=0}^{N-1}(y_{n+1}-y_n)
=2(y_N-y_0)<1.
\tag{GTP.11}
\]

Cauchy–Schwarz gives

\[
\boxed{
|x_n-x_0|<\sqrt n.
}
\tag{GTP.12}
\]

Hence the first `N` distinct zero coordinates in the chain all have ordinates in an interval of length less than `2sqrt(N)`.

The Riemann–von Mangoldt formula gives, with multiplicity,

\[
N_\zeta(T)=O(T\log(2+T)).
\]

Applied to the interval in (GTP.12), it permits only

\[
O(\sqrt N\log(2+N))
\]

zero coordinates there. This is smaller than `N` for all sufficiently large `N`, contradicting the existence of the chain.

Therefore:

\[
\boxed{
\text{If RH is false, at least one off-line reflected pair is terminal.}
}
\tag{GTP.13}
\]

This conclusion uses only the global zero count. It does not require zero separation, simplicity, or the Anthropic positive-proportion theorem.

## 6. Complete nuisance leakage vanishes for a terminal pair

Fix a terminal pair `z=x+iy`.

For every distinct zero coordinate `w` with nonnegative depth,

\[
\Phi_z(w)<0.
\]

Moreover

\[
(d-y)(d+3y)\le\frac13
\tag{GTP.14}
\]

for `0<=d,y<=1/2`. Thus, whenever `|x'-x|>=1`,

\[
\Phi_z(w)
\le-\frac23|x'-x|^2.
\tag{GTP.15}
\]

There are only finitely many zero coordinates in `|x'-x|<1`. Terminality gives a strict negative maximum on that finite nuisance set. Equations (GTP.7), (GTP.15), and the unit-interval zero count

\[
N_\zeta(T+1)-N_\zeta(T)=O(\log(2+T))
\]

therefore imply

\[
\boxed{
\sum_{w\ne z}m_w
 |F_{\sigma,z}(w)|^2
\longrightarrow0.
}
\tag{GTP.16}
\]

The reflected values have the same modulus by (GTP.5). Hence the complete contribution of every nuisance on-line zero and every nuisance off-line pair is `o(1)` in the zero-side Weil form.

## 7. The complete Weil value is negative

The target reflected pair contributes exactly

\[
-2m_z
\]

by (GTP.4) and the pair block of `OFFLINE_PAIR_SPECTRUM.md`.

For a nuisance reflected pair, its absolute Weil contribution is bounded by a constant times

\[
m_w|F_{\sigma,z}(w)|^2,
\]

and on-line contributions obey the same square bound. Therefore (GTP.16) yields

\[
\boxed{
\mathcal W(F_{\sigma,z},F_{\sigma,z})
=-2m_z+o(1).
}
\tag{GTP.17}
\]

In particular, for all sufficiently large `sigma`,

\[
\boxed{
\mathcal W(F_{\sigma,z},F_{\sigma,z})< -m_z<0.
}
\tag{GTP.18}
\]

Together with (GTP.6),

\[
\boxed{
\frac{\mathcal W(F_{\sigma,z},F_{\sigma,z})}
{\|F_{\sigma,z}\|_\sigma^2}
\longrightarrow-\infty.
}
\tag{GTP.19}
\]

Thus an off-line zero cannot survive by hiding behind asymptotic singularity of exact nuisance-cardinal interpolation. Approximate two-section Gaussian isolation is enough.

## 8. Admissibility and compact approximation

The physical Gaussian sections underlying (GTP.3) are Schwartz functions. The classical Weil explicit formula is valid on this rapidly decreasing test class.

If a particular finite-kernel implementation insists on compactly supported smooth physical tests, multiply the two Gaussian sections by an even cutoff `chi_R` equal to one on `[-R,R]`. At fixed sufficiently large `sigma`, the cut tests converge to (GTP.3) in every required weighted Schwartz seminorm as `R->infinity`. The explicit formula and all finitely separated target evaluations are continuous in those seminorms, while the Gaussian zero tail is summable by (GTP.15). Therefore the strict negative margin in (GTP.18) survives for all sufficiently large `R`.

No non-admissible formal cardinal function is required.

## 9. Consequence for PR #364 and the complete-kernel route

PR #364 ended with the dichotomy

```text
persistent negative corrected kernel
or
asymptotically singular zero-interpolation metric.
```

The present theorem removes the second alternative at the level of the complete Weil test space:

\[
\boxed{
\text{false RH}
\Longrightarrow
\text{a terminal pair with a vanishing-norm Gaussian negative direction}.
}
\tag{GTP.20}
\]

Equivalently, the inverse-Gram blow-up observed under exact finite cardinal constraints is a coordinate artifact, not a fundamental zero-geometric escape.

What remains is the arithmetic side:

> prove a nonnegative, or asymptotically nonnegative, lower floor for the complete admissible Gaussian/compact-approximation family.

PR #199 shows that such a complete corrected-kernel floor is itself RH-bearing. The present theorem does not prove that floor and therefore does not prove RH.

## 10. Review and rejection tests

A review should check, in order:

1. the Gaussian kernel and normalized correlation (GTP.1)–(GTP.2);
2. exact target interpolation and norm (GTP.3)–(GTP.6);
3. the nuisance exponent (GTP.7)–(GTP.8);
4. the strict-depth threat relation;
5. the telescoping square-increment argument (GTP.11);
6. the Riemann–von Mangoldt contradiction;
7. summability of the far Gaussian zero tail;
8. reflection symmetry and the complete zero-side estimate;
9. admissible compact approximation.

Reject any use of this theorem as an RH proof unless an independent arithmetic lower-floor theorem is supplied.

## Exact boundary

```text
Gaussian normalized correlation                 PROPOSED COMPLETE EXACT
raw reflected-pair interpolant                   PROPOSED COMPLETE EXACT
threat exponent and strict-depth graph           PROPOSED COMPLETE EXACT
existence of a terminal off-line pair             PROPOSED COMPLETE
complete nuisance leakage -> 0                    PROPOSED COMPLETE
negative complete Weil test under false RH        PROPOSED COMPLETE
exact-cardinal Gram-collapse escape               REMOVED
arithmetic lower floor for these tests            OPEN / RH-BEARING
Riemann Hypothesis                                UNPROVED
```

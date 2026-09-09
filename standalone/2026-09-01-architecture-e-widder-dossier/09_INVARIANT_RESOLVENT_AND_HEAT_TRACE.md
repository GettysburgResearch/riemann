# Invariant Widder resolvent, terminal annulus, and fixed-center zero heat

Status: **PROPOSED EXACT THEOREMS AND SOURCE IDENTITIES; INDEPENDENT REVIEW REQUIRED; THE ALL-ORDER E–WIDDER INEQUALITY AND RH REMAIN UNPROVED.**

This note extracts two pieces of leverage that are invisible in the raw
high-derivative formulation.

1. The complete Widder-order sequence at one invariant scale has an exact
   ordinary generating function.  It is a radial phase derivative of the
   single entire function `mathfrak X`, and every off-line zero creates a
   noncancellable negative-residue pole on the real interval `(1/2,1)`.
2. The inverse Laplace transform of the safe invariant logarithmic derivative
   is exactly the centered zeta-zero heat trace at the single centre `x=0`,
   with the universal factor `exp(-t/4)`.  The E–Widder hierarchy is therefore
   equivalent to complete monotonicity in heat time of one fixed-centre trace.

The first result resums all Widder orders.  The second identifies the all-order
source with the existing First-Hermite programme, but trades all real centres
and one heat derivative for one invariant centre and every heat derivative.
Neither identity proves the remaining source sign.

## 1. Normalized invariant moments

Retain

\[
 q(u)=2\frac{\mathfrak X'(u)}{\mathfrak X(u)},
 \qquad
 \mathfrak X(s(s-1))=\xi_{\rm R}(s),
 \qquad u>0.
\]

For `k>=1`, put

\[
 \mathcal W_k(u)=(-1)^{k-1}D_u^{2k-1}[u^kq(u)]
\]

and normalize

\[
 \boxed{
 C_k(u)=\frac{(4u)^k}{2(2k-1)!}\mathcal W_k(u).
 }
 \tag{1.1}
\]

Let

\[
 a_\rho=-\rho(\rho-1)
\]

and choose one invariant parameter for each functional-equation orbit, with
multiplicity; conjugation closes the multiset.  The genus-zero logarithmic
derivative and the one-atom Widder identity give, without assuming RH,

\[
 \boxed{
 C_k(u)=\sum_a \lambda_u(a)^k,
 \qquad
 \lambda_u(a)=\frac{4ua}{(u+a)^2}.
 }
 \tag{1.2}
\]

If

\[
 a=re^{i\alpha},\qquad u=re^v,
\]

then

\[
 \boxed{
 \lambda_u(a)
 =\operatorname{sech}^2\left(\frac{v-i\alpha}{2}\right).
 }
 \tag{1.3}
\]

Indeed

\[
 e^v+e^{i\alpha}
 =2e^{(v+i\alpha)/2}
 \cosh\left(\frac{v-i\alpha}{2}\right).
\]

Thus each invariant zero is one translated `sech^(2k)` profile in logarithmic
scale.  For a critical zero `alpha=0`, the profile is real and lies in
`(0,1]`.  At the canonical matching scale `u=|a|=r`,

\[
 \boxed{
 \lambda_r(a)=\sec^2(\alpha/2).
 }
 \tag{1.4}
\]

Hence a nonreal invariant zero produces a real transformed atom strictly
larger than one at its matching scale.  This is the invariant analogue of an
interior Hausdorff pole.

## 2. Exact order-generating function

For fixed `u>0`, define initially near `w=0`

\[
 \boxed{
 \mathscr R_u(w)
 =\sum_{k\ge1}C_k(u)w^{k-1}.
 }
 \tag{2.1}
\]

The zero expansion gives the locally normally convergent meromorphic sum

\[
 \boxed{
 \mathscr R_u(w)
 =\sum_a\frac{\lambda_u(a)}{1-w\lambda_u(a)}.
 }
 \tag{2.2}
\]

Introduce a nonzero parameter `zeta` by

\[
 \boxed{
 \zeta+\zeta^{-1}=2(1-2w).
 }
 \tag{2.3}
\]

Then

\[
 (u+a)^2-4uwa
 =(a+u\zeta)(a+u\zeta^{-1}).
 \tag{2.4}
\]

A one-line partial fraction calculation followed by
`q(z)=2 sum_a 1/(z+a)` yields

\[
 \boxed{
 \mathscr R_u(w)
 =\frac{2u}{\zeta-\zeta^{-1}}
 \left[
  \zeta q(u\zeta)-\zeta^{-1}q(u\zeta^{-1})
 \right].
 }
 \tag{2.5}
\]

This is the exact closed form of the full Widder-order generating function.
It is independent of any truncation or zero enumeration.

For real `0<w<1`, write

\[
 w=\sin^2(\theta/2),
 \qquad
 \zeta=e^{i\theta},
 \qquad 0<\theta<\pi.
\]

Conjugation symmetry gives

\[
 \boxed{
 \mathscr R_u(w)
 =\frac{2u}{\sin\theta}
 \Im\left[e^{i\theta}q(ue^{i\theta})\right].
 }
 \tag{2.6}
\]

Since `q=2 mathfrak X'/mathfrak X`, this is also

\[
 \boxed{
 \mathscr R_u(w)
 =\frac{4u}{\sin\theta}
 \frac d{du}\arg\mathfrak X(ue^{i\theta}).
 }
 \tag{2.7}
\]

Thus all Widder orders are one radial argument-variation law.

Equivalently, for `z=ue^{i theta}` and `F=mathfrak X`,

\[
 \boxed{
 \mathscr R_u(w)
 =4u\,
 \frac{
 zF'(z)\overline{F(z)}
 -\bar zF(z)\overline{F'(z)}
 }{
 (z-\bar z)|F(z)|^2
 }.
 }
 \tag{2.8}
\]

This is a radial Euler--Bezout diagonal.  It is a resummation identity, not a
positivity theorem.

## 3. Exact contribution of one nonreal invariant pair

Let

\[
 a=A+iB=re^{i\alpha},
 \qquad A>0,
 \qquad c=1-2w.
\]

The conjugate pair contribution to (2.2) is

\[
 P_a(u,w)
 =2\Re\frac{\lambda_u(a)}{1-w\lambda_u(a)}.
\]

Direct expansion gives

\[
 \boxed{
 P_a(u,w)
 =\frac{
 8u\,[A(r^2+u^2)+2ucr^2]
 }{
 |a^2+2uca+u^2|^2
 }.
 }
 \tag{3.1}
\]

Because

\[
 \frac{r^2+u^2}{2ur}\ge1,
\]

the pair is strictly positive for every `u>0` precisely on the side

\[
 c>-\cos\alpha.
\]

Equivalently,

\[
 \boxed{
 P_a(u,w)>0\quad\text{for every }u>0
 \quad\Longleftrightarrow\quad
 w<\cos^2(\alpha/2).
 }
 \tag{3.2}
\]

At the boundary

\[
 w_a=\cos^2(\alpha/2)
\]

and the matching scale `u=r`, formula (1.4) gives

\[
 1-w_a\lambda_r(a)=0.
\]

Each atom has residue `-1` as a function of `w`.  Therefore a conjugate pair
of multiplicity `m` gives

\[
 \boxed{
 \operatorname*{Res}_{w=w_a}\mathscr R_r(w)=-2m.
 }
 \tag{3.3}
\]

All invariant zeros with the same pole add residues with the same negative
sign.  No cancellation is possible.  Immediately to the right of the pole,

\[
 \mathscr R_r(w)\longrightarrow-\infty.
\]

For a nontrivial zeta zero in the critical strip, `Re a>0`; hence

\[
 |\alpha|<\frac\pi2,
 \qquad
 \frac12<w_a<1
\]

when the zero is off the critical line.  A critical invariant zero has
`alpha=0` and places its matching pole only at the boundary `w=1`.

## 4. Resummed RH criteria

The preceding calculation gives two exact criteria.

### Theorem 4.1 -- unit-disc holomorphy

\[
 \boxed{
 \mathrm{RH}
 \iff
 \mathscr R_u(w)\text{ is holomorphic for }|w|<1
 \quad\text{for every }u>0.
 }
 \tag{4.1}
\]

Under RH, every `a` is positive real, so `0<lambda_u(a)<=1` and (2.2) is
holomorphic in the unit disk.  Conversely, an off-line orbit gives the real
interior pole (3.3) at `u=|a|`.

### Theorem 4.2 -- real-ray positivity

\[
 \boxed{
 \mathrm{RH}
 \iff
 \mathscr R_u(w)\ge0
 \quad(u>0,\ 0<w<1),
 }
 \tag{4.2}
\]

with the statement interpreted away from poles.  Under RH it is termwise.
If RH is false, choose an off-line orbit and its matching scale.  Just to the
right of its first coincident pole, the negative residue dominates all terms
that are regular there, while coincident residues add negatively.

These are equivalent resummations of the all-order Widder hierarchy.  They do
not supply the source-side proof of (4.2).

## 5. Unconditional positive half-ray

The critical strip alone gives

\[
 \Re a=\gamma^2+\beta(1-\beta)>0,
\]
so every invariant zero satisfies `|alpha|<pi/2`.  By (3.2), every conjugate
pair is therefore positive on

\[
 0\le w\le\frac12.
\]

Consequently

\[
 \boxed{
 \mathscr R_u(w)>0
 \qquad(u>0,\ 0\le w\le1/2)
 }
 \tag{5.1}
\]

unconditionally.  This is a continuum, all-orders-resummed theorem, not a
finite-order statement.

## 6. The same half-ray is exactly the uniform Euler-safe ray

For `w=sin^2(theta/2)` define

\[
 z=ue^{i\theta},
 \qquad
 x_\theta=\sqrt{\frac14+z},
 \qquad
 s_\theta=\frac12+x_\theta,
\]

using the branch continued from positive `u`.

If `0<theta<=pi/2`, then `Re z>=0`.  Writing `x_theta=p+iq`,

\[
 p^2
 =\frac{|1/4+z|+\Re(1/4+z)}2
 >\frac14,
\]

and hence

\[
 \Re s_\theta>1.
\]

Thus every term in the Euler formula for `q(z)` is absolutely convergent on
this complete ray.  If `theta>pi/2`, then for sufficiently small `u`,

\[
 \sqrt{1/4+ue^{i\theta}}
 =\frac12+ue^{i\theta}+O(u^2),
\]

so `Re s_theta<1`.  Therefore the uniform direct-Euler threshold

\[
 \boxed{w=1/2}
 \tag{6.1}
\]

is sharp in the invariant generator.

On `0<w<=1/2`, the pole contribution `2/z` cancels from (2.6), since
`e^{i theta}2/(ue^{i theta})=2/u` is real.  The exact source formula is

\[
 \boxed{
 \mathscr R_u(w)
 =\mathscr G_u(w)
 -\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
  \mathscr L_u(w,\log n),
 }
 \tag{6.2}
\]

where

\[
 \boxed{
 \mathscr G_u(w)
 =\frac{2u}{\sin\theta}
 \Im\left[
  \frac{e^{i\theta}}{2x_\theta}
  \left(\psi(s_\theta/2)-\log\pi\right)
 \right]
 }
 \tag{6.3}
\]

and

\[
 \boxed{
 \mathscr L_u(w,\ell)
 =\frac{2u}{\sin\theta}
 \Im\left[
  \frac{e^{i\theta}}{x_\theta}e^{-\ell x_\theta}
 \right].
 }
 \tag{6.4}
\]

The prime series converges absolutely and locally uniformly on the stated
open ray.  Combining (5.1) and (6.2) proves the all-orders-resummed source
inequality

\[
 \boxed{
 \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 \mathscr L_u(w,\log n)
 <\mathscr G_u(w)
 \quad(u>0,\ 0<w\le1/2).
 }
 \tag{6.5}
\]

This is not coefficientwise E–Widder positivity, but it is a genuine
continuum source theorem containing every order in one generating sum.

## 7. Verified height confines all possible failure to a terminal annulus

Assume every zero through height `H` is critical.  For an unverified off-line
zero,

\[
 |\arg a|<\alpha_H:=\arctan(1/H).
\]

By (3.2), every invariant pair is positive on the larger interval

\[
 0\le w\le w_H,
 \qquad
 \boxed{
 w_H=\cos^2(\alpha_H/2)
 =\frac12\left(1+\frac{H}{\sqrt{H^2+1}}\right).
 }
 \tag{7.1}
\]

Hence

\[
 \boxed{
 \mathscr R_u(w)>0
 \qquad(u>0,\ 0\le w\le w_H).
 }
 \tag{7.2}
\]

For the published verification height `H=3*10^12`,

\[
 1-w_H
 =\frac12\left(1-\frac{H}{\sqrt{H^2+1}}\right)
 <\frac1{4H^2}
 <2.78\cdot10^{-26}.
 \tag{7.3}
\]

Thus every possible real-ray failure of the resummed E–Widder generator is
confined to an explicit terminal annulus of width below `2.78e-26` adjacent
to `w=1`.  The external zero verification is imported through the existing
repository source lock and is not rerun here.

This terminal-annulus theorem is stronger as a resummed statement than the
linear finite-order cone in the preceding note.  It does not imply
coefficientwise positivity at unbounded order.

## 8. Fixed-centre invariant zero heat

Define

\[
 \boxed{
 K(t)=2\sum_a e^{-at},
 \qquad t>0.
 }
 \tag{8.1}
\]

The Gaussian zero count and `Re a>0` give absolute and locally uniform
convergence.  For `Re u>0`, Tonelli/local normal convergence gives

\[
 \boxed{
 q(u)=\int_0^\infty e^{-ut}K(t)\,dt.
 }
 \tag{8.2}
\]

For the centred zero coordinate

\[
 \gamma_\rho=\frac{\rho-1/2}{i},
\]

we have

\[
 a_\rho=\frac14+\gamma_\rho^2.
\]

The full zero multiset counts both centred signs for each invariant orbit,
so the centred heat trace

\[
 \mathcal H_\zeta(t,0)=\sum_\rho e^{-t\gamma_\rho^2}
\]

satisfies the exact identity

\[
 \boxed{
 K(t)=e^{-t/4}\mathcal H_\zeta(t,0).
 }
 \tag{8.3}
\]

There is no missing factor two: the full centred zero trace contains two
points for each invariant parameter.

### Theorem 8.1 -- fixed-centre heat criterion

\[
 \boxed{
 \mathrm{RH}
 \iff
 K\text{ is completely monotone on }(0,\infty).
 }
 \tag{8.4}
\]

Under RH, every `a` is positive real and (8.1) is termwise completely
monotone.  Conversely, Bernstein's theorem gives

\[
 K(t)=\int_{[0,\infty)}e^{-rt}\,d\mu(r)
\]

with `mu>=0`.  Substitution into (8.2) yields the Stieltjes representation

\[
 q(u)=\int_{[0,\infty)}\frac{d\mu(r)}{u+r},
\]

which implies RH by the invariant Stieltjes theorem in the parent dossier.

Thus the existing first-Hermite reality criterion and E–Widder are two
sections of the same zero heat object:

```text
First-Hermite:  every real centre, first heat derivative;
E–Widder:       one invariant centre, every heat derivative.
```

## 9. Widder-to-heat integral bridge

Differentiating (8.1), or first checking one exponential and then summing,
gives

\[
 \boxed{
 \mathcal W_k(u)
 =\int_0^\infty
 t^{2k-1}e^{-ut}(-1)^kK^{(k)}(t)\,dt.
 }
 \tag{9.1}
\]

Indeed one atom contributes

\[
 2a^k\int_0^\infty t^{2k-1}e^{-(u+a)t}\,dt
 =2(2k-1)!\frac{a^k}{(u+a)^{2k}}.
\]

This formula moves all high-order differentiation away from the Euler-safe
variable `u` and into heat time.  It shows that the stronger source theorem

\[
 (-1)^kK^{(k)}(t)\ge0
 \quad(k\ge0,\ t>0)
\]

would imply every E–Widder inequality by one positive Laplace moment.

## 10. Explicit heat-source formula

Apply the standard Guinand--Weil formula to

\[
 h_t(z)=e^{-tz^2}
\]

at centre zero, in the normalization already used by the integrated
First-Hermite packet.  Multiplying the resulting centred zero heat by
`e^(-t/4)` gives

\[
 \boxed{
 \begin{aligned}
 K(t)={}&2\\
 &+\frac{e^{-t/4}}{2\pi}
 \int_{\mathbb R}e^{-t\tau^2}
 \left[
  \Re\psi\left(\frac14+\frac{i\tau}{2}\right)-\log\pi
 \right]d\tau\\
 &-\frac{e^{-t/4}}{\sqrt{\pi t}}
 \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 e^{-(\log n)^2/(4t)}.
 \end{aligned}
 }
 \tag{10.1}
\]

Every term is absolutely convergent for `t>0`.  The same formula follows by
inverse Laplace transformation of the Euler-safe expression for `q`, using

\[
 \mathcal L^{-1}\left[
  \frac{e^{-\ell\sqrt{u+1/4}}}{\sqrt{u+1/4}}
 \right](t)
 =\frac{e^{-t/4-\ell^2/(4t)}}{\sqrt{\pi t}}.
 \tag{10.2}
\]

The rational pole term `2/u` becomes the constant `2`.

The all-order E–Widder burden can therefore be replaced exactly by the
fixed-centre heat inequalities

\[
 \boxed{
 (-1)^mD_t^m K(t)\ge0
 \qquad(m\ge0,\ t>0).
 }
 \tag{10.3}
\]

After differentiation, the prime side remains a single nonoscillatory
Gaussian sum in `log n`; the cosine phase present at a moving First-Hermite
centre has disappeared.  The resulting generalized Hermite/Laguerre weights
still change sign, so (10.3) is not termwise.

## 11. Exact recurrence in logarithmic invariant scale

Let `x=log u`.  Combining the differential recurrence for `W_k` with (1.1)
gives

\[
 \boxed{
 C_{k+1}(u)
 =\frac{2}{k(2k+1)}
 \left[k^2C_k(u)-uC_k'(u)-u^2C_k''(u)\right].
 }
 \tag{11.1}
\]

Equivalently,

\[
 \boxed{
 C_{k+1}(e^x)
 =\frac{2}{k(2k+1)}
 \left(k^2-\partial_x^2\right)C_k(e^x).
 }
 \tag{11.2}
\]

The `sech^(2k)` profile (1.3) is the exact atomic solution of this
Pöschl--Teller-type ladder.  The operator is not positivity preserving on
arbitrary functions; a successful induction must use the literal source or a
source-defined invariant cone.

## 12. New proof frontier

The new formulation removes two distractions.

- There is no need to attack one derivative order after another: all orders
  are the single radial phase function `R_u(w)`.
- There is no need to carry a movable Fourier centre: all E–Widder signs are
  positive Laplace moments of derivatives of the fixed-centre heat trace
  `K(t)`.

The remaining theorem may be stated in either of two genuinely source-local
forms.

### Terminal-annulus form

Prove the source expression (2.6)/(6.2) is nonnegative for

\[
 w_H<w<1,
\]

where the only possible obstruction has already been confined to a terminal
annulus of width below `2.78e-26`.

### Fixed-centre heat form

Prove complete monotonicity of the explicit source (10.1):

\[
 (-1)^mK^{(m)}(t)\ge0
 \quad(m\ge0,t>0).
\]

The second formulation is stronger pointwise in heat time and immediately
implies every coefficientwise E–Widder inequality through (9.1).  It exposes
a nonoscillatory prime source and is the recommended next attack.

Neither target is discharged here.

## 13. Review priorities

Independent review should check:

1. the normalization in (1.1)--(1.2);
2. the `sech` identity (1.3);
3. the quadratic factorization and partial fractions in (2.4)--(2.5);
4. the radial phase and Euler--Bezout formulas;
5. the pair numerator (3.1), threshold (3.2), and residue (3.3);
6. the holomorphy and real-ray equivalences;
7. the sharp uniform Euler threshold `w=1/2`;
8. the verified-height terminal-annulus estimate;
9. the factor in `K=e^(-t/4)H_zeta(t,0)`;
10. the Bernstein/Stieltjes converse in (8.4);
11. the moment factor in (9.1);
12. the Guinand--Weil normalization in (10.1);
13. the recurrence coefficient in (11.1).

## 14. Exact boundary

```text
normalized sech-profile identity                 PROPOSED EXACT / REVIEW
closed Widder-order resolvent                     PROPOSED EXACT / REVIEW
off-line matching-scale real pole                 PROPOSED EXACT / REVIEW
unconditional resummed positivity on w<=1/2       PROPOSED EXACT / REVIEW
verified-height terminal annulus                  PROPOSED EXACT / REVIEW
fixed-centre zero-heat identity                    PROPOSED EXACT / REVIEW
RH <=> complete monotonicity of K                  PROPOSED EXACT / REVIEW
explicit nonoscillatory heat source                PROPOSED EXACT / REVIEW
terminal-annulus source sign                       OPEN / RH-EQUIVALENT
complete monotonicity of K                         OPEN / RH-EQUIVALENT
all-order E-Widder source inequality               OPEN / RH-EQUIVALENT
Riemann Hypothesis                                 UNPROVED
```

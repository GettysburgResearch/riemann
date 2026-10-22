# Hardy flowers and real phase tomography

## Status

This packet contains a first bounded execution pass on two related research
questions:

1. Can the visible flower/petal geometry of the critical-line zeta image be
   converted into exact kinematic and counting identities?
2. Can the off-critical displacement of zeros be represented by an entirely
   real signal extracted from a phase field in the safe half-plane?

The packet proves several exact identities and finite-zero theorems.  It does
**not** prove the Riemann hypothesis, does not improve an unconditional zero
proportion, and does not certify an off-line zero.

The strongest project-specific synthesis is:

```text
Hardy critical-line flower
    -> signed radial kinematics and petal area
centered-Xi phase velocity above the zero strip
    -> safe right-half-plane xi'/xi
    -> absolutely convergent real prime cosine series
inverse Poisson transform
    -> real exponential/trigonometric zero response
weighted response energy
    -> exact maximal off-axis height for every finite real zero model.
```

The component ingredients are classical: Hardy's real function, the
functional equation, the Fourier transform of the Poisson kernel, Hadamard
factorization, and the explicit formula.  External novelty or priority for the
combined normal form has **not** been established and is not claimed.

---

## 1. The Hardy flower is a signed radial curve

Write

\[
Z(t)=e^{i\vartheta(t)}\zeta\!\left(\frac12+it\right)\in\mathbb R
\]

for Hardy's function and the Riemann--Siegel phase.  The image of the critical
line is

\[
\Gamma(t)=\zeta\!\left(\frac12+it\right)
         =e^{-i\vartheta(t)}Z(t).
\]

The following theorem is stated for arbitrary real functions.  Its value is
that it identifies exactly which parts of the visible flower are universal
kinematics and which parts can contain zeta-specific information.

### PFR-T1 — Hardy-flower kinematic theorem

Let `theta,Z` be real `C^2` functions on an interval and put

\[
\Gamma(t)=e^{-i\theta(t)}Z(t).
\]

Then

\[
\Gamma'(t)=e^{-i\theta(t)}
           \bigl(Z'(t)-i\theta'(t)Z(t)\bigr),
\tag{1.1}
\]

and hence

\[
|\Gamma'(t)|^2=Z'(t)^2+\theta'(t)^2Z(t)^2.
\tag{1.2}
\]

The signed areal velocity is

\[
\boxed{
\frac12\operatorname{Im}\bigl(\overline{\Gamma(t)}\Gamma'(t)\bigr)
=-\frac12\theta'(t)Z(t)^2.
}
\tag{1.3}
\]

If `a<b`, `Z(a)=Z(b)=0`, and `theta'>0`, the image is a closed curve based at
the origin.  Its algebraic area is

\[
\boxed{
\mathcal A[a,b]
=-\frac12\int_a^b\theta'(t)Z(t)^2\,dt.
}
\tag{1.4}
\]

If `a,b` are consecutive zeros of `Z`, this is the exact signed area of one
Hardy petal, counted with winding multiplicity if the petal self-intersects.
Every such petal has the same orientation wherever `theta'>0`.

#### Angular normal form

When `theta'>0`, use `phi=theta(t)` and put

\[
r(\phi)=Z(t(\phi)).
\]

Then

\[
\Gamma(\phi)=r(\phi)e^{-i\phi}.
\tag{1.5}
\]

Thus the elaborate picture is exactly a real signed-radius function in a
monotonically rotating frame.  At regular points its signed curvature is

\[
\boxed{
\kappa(\phi)=
\frac{r r''-r^2-2(r')^2}
     {(r^2+(r')^2)^{3/2}}.
}
\tag{1.6}
\]

The flower is therefore completely encoded by the real function `r`; the
complex plane records the rotating presentation of that real data.

#### Petal uncertainty inequality

If `Z(a)=Z(b)=0`, the ordinary Wirtinger inequality in the angular coordinate
gives

\[
\boxed{
\int_a^b\theta' Z^2\,dt
\le
\left(\frac{\theta(b)-\theta(a)}{\pi}\right)^2
\int_a^b\frac{(Z')^2}{\theta'}\,dt.
}
\tag{1.7}
\]

Equivalently, petal area is bounded by radial derivative energy:

\[
2|\mathcal A[a,b]|
\le
\left(\frac{\Delta\theta}{\pi}\right)^2
\int_a^b\frac{(Z')^2}{\theta'}\,dt.
\tag{1.8}
\]

This is exact and unconditional; it does not itself force a new zero.

#### Flower participation count

Let

\[
\gamma_0<\gamma_1<\cdots<\gamma_M
\]

be consecutive critical-line zeros in a window on which `theta'>0`, and define
positive petal masses

\[
A_j=\frac12\int_{\gamma_j}^{\gamma_{j+1}}
          \theta'(t)Z(t)^2\,dt.
\]

Cauchy--Schwarz gives the exact participation bound

\[
\boxed{
M\ge \frac{(\sum_j A_j)^2}{\sum_j A_j^2}.
}
\tag{1.9}
\]

If

\[
L_{\max}=
\max_j\bigl(\theta(\gamma_{j+1})-\theta(\gamma_j)\bigr),
\]

then a second Cauchy--Schwarz estimate in angular coordinates gives

\[
\boxed{
M\ge
\frac{\left(\int_{\gamma_0}^{\gamma_M}\theta'Z^2\,dt\right)^2}
     {L_{\max}
      \int_{\gamma_0}^{\gamma_M}\theta'Z^4\,dt}.
}
\tag{1.10}
\]

This is a precise form of the proposed “enough petals from flower mass” route.
To approach the full zero count it would require sharp control of petal-area
concentration or of `L_max`; ordinary second and fourth moments alone are not
expected to supply the missing all-zero theorem.

### Proof

Equations (1.1)--(1.3) follow by one differentiation.  Green's area formula
then gives (1.4).  Formula (1.6) follows by differentiating
`r exp(-i phi)` twice and using

\[
\operatorname{Im}(\overline{\Gamma'}\Gamma'')
=r r''-r^2-2(r')^2.
\]

Equation (1.7) is the Dirichlet Wirtinger inequality after the change of
variable `phi=theta(t)`.  Equation (1.9) is Cauchy--Schwarz for the positive
numbers `A_j`.  Finally,

\[
A_j^2
\le \frac14\Delta\theta_j
        \int_{\theta(\gamma_j)}^{\theta(\gamma_{j+1})}r^4\,d\phi
\]

and summation gives (1.10).

### Boundary of the result

The local shape around a zero is universal.  The exact area identity is not a
zero-count theorem unless one also controls concentration across petals.  A
future proof must add an arithmetic, spectral, or trace mechanism rather than
infer RH from attractive geometry alone.

---

## 2. A real phase field above the zero strip

Define the centered completed function

\[
\mathcal X(z)=\xi\!\left(\frac12+iz\right).
\]

Its zeros lie in the horizontal strip `|Im z|<1/2`; RH says that all of them
lie on the real axis.

For `y>1/2`, define the upper phase-velocity field

\[
\mathcal V_y(x)
=-\partial_x\arg\mathcal X(x+iy)
=-\operatorname{Im}
  \frac{\mathcal X'}{\mathcal X}(x+iy).
\tag{2.1}
\]

This is a completely real function of the real variable `x`.

### PFR-T2 — safe-line prime transducer

For every real `x` and `y>1/2`, put

\[
s=\frac12+y+ix.
\]

Then

\[
\boxed{
\mathcal V_y(x)=
\operatorname{Re}\frac{\xi'}{\xi}(s).
}
\tag{2.2}
\]

Consequently,

\[
\boxed{
\begin{aligned}
\mathcal V_y(x)
={}&\operatorname{Re}\left[
 {1\over s}+{1\over s-1}
 -{1\over2}\log\pi
 +{1\over2}\psi(s/2)
 \right]\\
&-\sum_{n\ge2}
 {\Lambda(n)\over n^{1/2+y}}
 \cos(x\log n).
\end{aligned}
}
\tag{2.3}
\]

The prime series is absolutely convergent.  Thus the phase motion of the
centered Xi flower on a line *above the whole zero strip* is exactly a real
cosine signal of the prime powers, plus an explicit archimedean field.

### Proof

At `z=x+iy`, let `s_-=1/2-y+ix`.  Since

\[
{\mathcal X'\over\mathcal X}(z)
=i{\xi'\over\xi}(s_-),
\]

(2.1) equals `-Re xi'/xi(s_-)`.  The functional equation gives

\[
{\xi'\over\xi}(s)=-{\xi'\over\xi}(1-s),
\]

and conjugation moves `1/2+y-ix` to `1/2+y+ix` without changing the real
part.  This proves (2.2).  Logarithmic differentiation of

\[
\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)
\]

and the absolutely convergent identity

\[
{\zeta'\over\zeta}(s)
=-\sum_{n\ge2}{\Lambda(n)\over n^s}
\qquad(\operatorname{Re}s>1)
\]

give (2.3).

### Relation to existing passivity work

Issue #39 studies the sign of `Re xi'/xi` and its Pick matrices as a finite RH
witness.  PFR-T2 does not replace that criterion.  Its new role in this packet
is to interpret the same safe-line field simultaneously as:

1. flower phase velocity on the opposite centered line;
2. a Poisson smoothing of zero data;
3. an absolutely convergent real prime signal whose inverse smoothing exposes
   critical `Lambda(n)/sqrt(n)` weights.

---

## 3. Finite inverse-Poisson phase tomography

The next result is exact for every finite polynomial and requires no zeta
input.

Let

\[
P(z)=C\prod_{j=1}^N(z-\lambda_j),
\qquad
\lambda_j=a_j+ib_j,
\]

and choose `y>B`, where

\[
B=\max_j b_j.
\]

Define

\[
V_{P,y}(x)
=-\operatorname{Im}{P'\over P}(x+iy)
=\sum_j {y-b_j\over (x-a_j)^2+(y-b_j)^2}.
\tag{3.1}
\]

Use the Fourier convention

\[
\widehat f(t)=\int_{\mathbb R}f(x)e^{-itx}\,dx.
\]

### PFR-T3 — phase-to-resonance theorem

For every real `t`,

\[
\boxed{
\widehat V_{P,y}(t)
=\pi e^{-y|t|}R_P(t),
\qquad
R_P(t)=\sum_j e^{b_j|t|}e^{-ia_jt}.
}
\tag{3.2}
\]

Therefore

\[
\boxed{
R_P(t)={e^{y|t|}\over\pi}\widehat V_{P,y}(t)
}
\tag{3.3}
\]

is independent of the observation height `y`.  It is the exact backward
Poisson, or de-Poissonized, response of the phase field.

If `P` has real coefficients, let

\[
B_{\mathbb R}(P)=\max_j|\operatorname{Im}\lambda_j|.
\]

Then the weighted real energy

\[
\mathcal E_P(\sigma)
=\int_0^\infty e^{-2\sigma t}|R_P(t)|^2\,dt
\tag{3.4}
\]

converges **if and only if**

\[
\boxed{\sigma>B_{\mathbb R}(P).}
\tag{3.5}
\]

For `sigma>B_R(P)` it has the exact Cauchy--Gram form

\[
\boxed{
\mathcal E_P(\sigma)
=\sum_{j,k}
{1\over
 2\sigma-b_j-b_k+i(a_j-a_k)}.
}
\tag{3.6}
\]

In particular,

\[
\boxed{
B_{\mathbb R}(P)
=\inf\{\sigma:\mathcal E_P(\sigma)<\infty\}.
}
\tag{3.7}
\]

This turns vertical zero displacement into an ordinary real convergence
abscissa.

### Real-rootedness equivalences

For a nonconstant real polynomial,

\[
\boxed{
\begin{aligned}
P\text{ has only real zeros}
\quad\Longleftrightarrow\quad& B_{\mathbb R}(P)=0\\
\Longleftrightarrow\quad& R_P\text{ is bounded on }\mathbb R\\
\Longleftrightarrow\quad& R_P\text{ is positive definite}\\
\Longleftrightarrow\quad&
\mathcal E_P(\sigma)<\infty\text{ for every }\sigma>0.
\end{aligned}
}
\tag{3.8}
\]

Thus a complex-zero statement has become a real harmonic-analysis statement.

### Proof

The Fourier transform

\[
\int_{\mathbb R}
{c\over(x-a)^2+c^2}e^{-itx}\,dx
=\pi e^{-c|t|}e^{-iat}
\qquad(c>0)
\]

gives (3.2).  Squaring the finite sum and integrating term by term gives
(3.6).

For the convergence boundary, group the zeros of maximal upper height `B`.
Their contribution is

\[
e^{Bt}Q(t),
\]

where `Q` is a nonzero trigonometric polynomial.  Its mean square is positive,
so exponential damping of rate at most `B` cannot be integrable.  The converse
is immediate from the finite sum.  Real coefficients provide conjugate zeros,
so the maximal upper height equals the maximal absolute height.

If all zeros are real, `R_P` is the Fourier transform of the positive atomic
measure `sum delta_{a_j}` and is positive definite.  Conversely, any continuous
positive-definite function satisfies `|R(t)|<=R(0)`, while a nonreal conjugate
pair forces exponential growth by the preceding maximal-height argument.
This proves (3.8).

### Interpretation

The ordinary phase field `V_{P,y}` is benign and positive above all zeros.
The off-axis information is hidden in the ill-conditioned inverse Poisson
operation `exp(y|D|)`.  The theorem therefore does not make real-rootedness
easy: it identifies precisely where analytic continuation stores the vertical
zero coordinate.

---

## 4. One symmetric quartet: explicit witness and a Speiser firewall

Let

\[
Q_{a,b}(z)=((z-a)^2+b^2)((z+a)^2+b^2),
\qquad a>0,
b>0.
\tag{4.1}
\]

Its zeros are the Xi-symmetric quartet

\[
\pm a\pm ib.
\]

The real response is

\[
\boxed{R_{a,b}(t)=4\cos(at)\cosh(b|t|).}
\tag{4.2}
\]

At

\[
\tau={2\pi\over a},
\]

the two-point positive-definiteness matrix is

\[
\begin{pmatrix}
4&4\cosh(2\pi b/a)\\
4\cosh(2\pi b/a)&4
\end{pmatrix}.
\]

Its smaller eigenvalue is

\[
\boxed{4-4\cosh(2\pi b/a)<0.}
\tag{4.3}
\]

So one off-axis quartet has an explicit two-point, entirely real witness after
de-Poissonization.

The response energy has the closed form, for `sigma>b`,

\[
\begin{aligned}
\mathcal E_{a,b}(\sigma)=4\Bigg[&{1\over2\sigma}
+{2\sigma\over(2\sigma)^2+4a^2}
+{2\sigma\over(2\sigma)^2-4b^2}\\
&+\frac12\left(
 {2\sigma-2b\over(2\sigma-2b)^2+4a^2}
+{2\sigma+2b\over(2\sigma+2b)^2+4a^2}
\right)\Bigg].
\end{aligned}
\tag{4.4}
\]

It diverges at the exact boundary `sigma=b`.

### PFR-R1 — local Speiser assignment is false in symmetric models

Direct differentiation gives

\[
\boxed{
Q'_{a,b}(z)=4z(z^2-a^2+b^2).
}
\tag{4.5}
\]

If `a>b`, every critical point of `Q_{a,b}` is real:

\[
0,\qquad \pm\sqrt{a^2-b^2},
\]

although all four zeros of `Q_{a,b}` are nonreal.

Therefore no generic local law of the form

```text
one off-axis symmetric zero quartet
    -> one nonreal derivative critical point
```

can underlie Speiser's theorem.  Speiser geometry is global and
zeta-specific; local flower topology alone is insufficient.  This is a useful
firewall for the proposed phase-flow programme.

---

## 5. De-Poissonization is the critical explicit formula

For the centered Xi phase field, Hadamard factorization gives a zero-side
Poisson representation.  PFR-T2 gives the prime-side representation.  Their
Fourier transforms meet at the square-root normalization.

### PFR-T4 — distributional phase/explicit-formula identity

Let `g` be smooth and compactly supported in `(0,infinity)`.  Then

\[
\boxed{
\begin{aligned}
\sum_\rho\int_0^\infty
 g(t)e^{(\rho-1/2)t}\,dt
={}&\int_0^\infty g(t)
\left[
 e^{t/2}+e^{-t/2}
 -{e^{-t/2}\over1-e^{-2t}}
\right]dt\\
&-\sum_{n\ge2}{\Lambda(n)\over\sqrt n}\,g(\log n).
\end{aligned}
}
\tag{5.1}
\]

The zero sum is over all nontrivial zeros with multiplicity and is understood
symmetrically.  For the stated test functions it is absolutely convergent
after integrating by parts in `t`; the prime sum is finite.

Equivalently, on positive frequencies,

\[
\boxed{
{e^{y t}\over\pi}\widehat{\mathcal V_y}(t)
=\sum_\rho e^{(\rho-1/2)t}
}
\tag{5.2}
\]

as a test-function distribution, independently of `y>1/2`.  The right side is
real because the zero set is closed under conjugation.

On the prime side, multiplication by `e^{yt}` cancels the safe-line damping:

\[
e^{yt}n^{-1/2-y}\big|_{t=\log n}=n^{-1/2}.
\tag{5.3}
\]

Thus the inverse-Poisson transform of the harmless absolutely convergent phase
field exposes exactly the critical prime weights `Lambda(n)/sqrt(n)`.

For a quartet

\[
\rho=\frac12\pm\delta\pm i\gamma,
\]

its zero-side contribution is

\[
\boxed{4\cosh(\delta t)\cos(\gamma t).}
\tag{5.4}
\]

This is the sought real-only description:

```text
horizontal coordinate gamma      -> real oscillation frequency;
off-line distance delta          -> hyperbolic growth exponent.
```

Under RH every hyperbolic factor collapses to `1`.

### Proof outline

For `s=1/2+y+ix`, Fourier transformation in `x` gives, at positive frequency
`t`:

\[
\widehat{\operatorname{Re}(1/s)}
=\pi e^{-(y+1/2)t},
\]

\[
\widehat{\operatorname{Re}(1/(s-1))}
=\pi e^{-(y-1/2)t},
\]

and the standard integral representation of the digamma function gives

\[
\widehat{\tfrac12\operatorname{Re}\psi(s/2)}
=-\pi{e^{-(y+1/2)t}\over1-e^{-2t}}.
\]

The prime cosine series contributes

\[
-\pi\sum_{n\ge2}{\Lambda(n)\over n^{1/2+y}}
\delta(t-\log n).
\]

Multiplying by `e^{yt}/pi` gives the right side of (5.1).  Fourier transforming
the Poisson kernels associated with the zeros gives the left side.  Pairing
against `g` avoids the singular distribution at frequency zero.

### Novelty boundary

Equation (5.1) is a standard explicit formula written in a phase-flow /
inverse-Poisson normal form.  The packet does not claim discovery of the
explicit formula.  The research contribution being tested is whether this
normal form, together with the finite energy theorem and petal geometry,
produces a new controllable invariant.

---

## 6. What has genuinely advanced

The pass narrows the two proposed approaches to concrete mathematical burdens.

### Flower route

The visible petals have an exact real kinematic content:

```text
petal area       = weighted Hardy-Z second mass;
radial roughness = weighted Z' energy;
petal count      >= area participation ratio.
```

A successful flower proof must control **concentration of petal area**, not
merely total area or local winding.

### Real-only route

The zero set has an exact real signal:

```text
safe phase field
  --inverse Poisson--> sum exp(delta t) cos(gamma t).
```

For every finite symmetric model the maximal `delta` is exactly an energy
abscissa, and real-rootedness is exactly positive definiteness of the response.
For Xi, the same inverse transform is the critical explicit-formula
distribution.

### Negative structural result

A symmetric off-axis quartet need not create a nonreal derivative critical
point.  Therefore a proof cannot assign Speiser defects locally, one flower at
a time.  It must use the global zeta map, its pole/boundary structure, or its
arithmetic source.

---

## 7. Open theorem targets

### PFR-G1 — windowed actual-Xi response energy

Construct a source-defined, height-windowed version of

\[
\sum_\rho e^{(\rho-1/2)t}
\]

whose weighted energy has abscissa

\[
\sup_{\rho\ \text{in the window}}
\left|\operatorname{Re}\rho-\frac12\right|,
\]

and express it through a finite or controlled prime-side quadratic form without
first inserting the zeros.

This would be the actual-Xi analogue of PFR-T3 and would provide a quantitative
real-only zero sensor distinct from the beta detector in PR #762.

### PFR-G2 — petal-area concentration theorem

Bound

\[
\sum_j A_j^2
\]

sharply enough, using zeta-specific arithmetic or phase-flow structure, that
(1.9) approaches the complete Riemann--von Mangoldt zero count rather than a
mere positive proportion.

### PFR-G3 — global phase/Speiser adapter

Relate the inverse-Poisson growth defect to the actual zeros of `zeta'` left of
the critical line, with all pole, completion, boundary, and endpoint terms.
PFR-R1 proves that such an adapter cannot be a generic local quartet theorem.

### PFR-G4 — prime-side positive-definiteness or temperedness

Use (5.1) to formulate and prove a prime-side condition ensuring that the
inverse-Poisson response is a positive-definite tempered distribution.  For
finite models this is equivalent to real-rootedness.  For Xi it is expected to
be close to Weil positivity and must be audited against known equivalences
rather than advertised as automatically new.

### PFR-G5 — certified phase graph

Build an interval-certified finite-window phase/separatrix graph containing:

- critical-line petals;
- zeros of `zeta` and `zeta'`;
- phase and Newton-flow edges;
- boundary winding;
- the petal-area and inverse-Poisson fields.

Test every proposed invariant against the quartet firewall and against
zeta-like functions known to violate their RH analogue.

---

## 8. RH status

```text
Hardy-flower kinematics                         PROVED EXACT
petal-area participation inequalities           PROVED EXACT
safe-line phase = real prime cosine field        PROVED EXACT
finite inverse-Poisson zero-height theorem       PROVED EXACT
finite response positive-definiteness criterion PROVED EXACT
symmetric-quartet local Speiser firewall         PROVED EXACT
critical distributional explicit formula         STANDARD IDENTITY / RECAST
actual-Xi source-defined response energy          OPEN
petal concentration at full zero-count strength  OPEN
new RH implication                               NONE
Riemann Hypothesis                               UNPROVED
```

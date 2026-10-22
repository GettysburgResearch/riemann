# Phase-flow / real-transducer continuation: symmetric positivity and Speiser screening

## Status

Claim namespace: `PFR-T10`, `PFR-T11`, `PFR-R4`  
Status: **AUTHOR-PROVED EXACT ANALYTIC THEOREMS / REVIEW PENDING / EXTERNAL NOVELTY UNESTABLISHED**  
Parent: branch head `16d9c586d2f7439187e756066410622fd51c6d56`  
RH status: **unproved**

This continuation advances both live directions.

```text
real-only response:
  one-sided Gamma spline PFR-T5/PFR-T7
      -> symmetric Green resolvent
      -> positive-definite time kernel under RH
      -> positive-real / Pick kernel under RH
      -> the same prime knots and the same zero-displacement abscissa;

flower / Speiser geometry:
  positive flower curvature = positive variation of arg zeta'
      -> finite harmonic screening identity
      -> exact zeta-prime rectangle Gauss law
      -> every left-of-line zeta' zero is paid by curvature or boundary flux.
```

No new zero, zero proportion, RH theorem, or external priority claim is made.
The positive-definite formulation is deliberately compared with Weil and
Suzuki screw-function positivity rather than advertised as a new field.

---

## 1. PFR-T10 — a symmetric positive-definite prime-knot resolvent

Let

\[
E(z)=\xi\!\left(\frac12+z\right),
\qquad
F(z)=\frac{E'(z)}{E(z)}
=\frac{\xi'}{\xi}\!\left(\frac12+z\right).
\tag{1.1}
\]

The functional equation makes `E` even and `F` odd.  Write the centered
nontrivial zeros as

\[
\lambda_\rho=\rho-\frac12.
\tag{1.2}
\]

They are invariant, with multiplicity, under

\[
\lambda\mapsto-\lambda,
\qquad
\lambda\mapsto\overline\lambda.
\tag{1.3}
\]

Fix

\[
a>\frac12,
\qquad
m\ge2,
\tag{1.4}
\]

and define the symmetric resolvent response

\[
\boxed{
\mathcal S_{a,m}(t)
=
\sum_\rho
\frac{e^{\lambda_\rho t}}
     {(a^2-\lambda_\rho^2)^m},
\qquad t\in\mathbb R.
}
\tag{1.5}
\]

The estimate `N(T)=O(T log T)` shows that the coefficients are absolutely
summable.  The series converges locally uniformly, is real-valued and even,
and belongs to `C^(2m-2)(R)` away from the special behavior at the origin
coming from the completed explicit formula.

Put

\[
B_\xi
=
\sup_\rho\operatorname{Re}\lambda_\rho
=
\Theta-\frac12.
\tag{1.6}
\]

The second equality uses the reflection symmetry.  RH is exactly `B_xi=0`.

### 1.1 Two-point Hermite source formula

Let `H_(a,m-1)F` be the unique polynomial of degree at most `2m-1` satisfying

\[
\left(H_{a,m-1}F\right)^{(j)}(\pm a)=F^{(j)}(\pm a),
\qquad 0\le j<m.
\tag{1.7}
\]

Define

\[
\boxed{
\mathcal M_{a,m}(z)
=
\frac{F(z)-H_{a,m-1}F(z)}{(a^2-z^2)^m}.
}
\tag{1.8}
\]

The apparent singularities at `z=+/-a` are removable.

#### Theorem 1.1 — exact Hermite remainder identity

For every `z` away from the centered zeros,

\[
\boxed{
\mathcal M_{a,m}(z)
=
\sum_\rho
\frac{1}
{(a^2-\lambda_\rho^2)^m(z-\lambda_\rho)}.
}
\tag{1.9}
\]

The series is normally convergent on compact sets away from its poles.

#### Proof

For one complex number `lambda`, let `h_lambda` be the two-point Hermite
interpolant of `z -> 1/(z-lambda)` at `+/-a`, with multiplicity `m` at each
node.  The exact rational remainder is

\[
\frac1{z-\lambda}-h_\lambda(z)
=
\frac{(a^2-z^2)^m}
     {(a^2-\lambda^2)^m(z-\lambda)}.
\tag{1.10}
\]

Both sides have the same pole and residue at `lambda`, and their difference is
a polynomial of degree at most `2m-1` with `2m` Hermite zero conditions, hence
vanishes.

Apply the linear remainder operator `I-H_(a,m-1)` to the genus-one Hadamard
logarithmic derivative of `E`.  It annihilates the regularization constants.
The remainder for one zero is `O(|lambda|^(-2m-1))`, so the transformed zero
series is absolutely and normally convergent.  Division by `(a^2-z^2)^m`
gives (1.9).

### 1.2 Why this is source-defined

For `Re z>1/2`, put `s=1/2+z`.  Then

\[
F(z)
=
\frac1s+\frac1{s-1}
-\frac12\log\pi
+\frac12\psi(s/2)
-
\sum_{n\ge2}\frac{\Lambda(n)}{n^s}.
\tag{1.11}
\]

The prime-power series and all of its `z`-derivatives converge absolutely.
The Hermite jets at `-a` are obtained from the oddness of `F`, so all data in
(1.8) are available from the single safe point `1/2+a>1` and the safe vertical
line `Re z>1/2`.

For `Re z>B_xi`, termwise Laplace transformation gives

\[
\boxed{
\int_0^\infty e^{-zt}\mathcal S_{a,m}(t)\,dt
=
\mathcal M_{a,m}(z).
}
\tag{1.12}
\]

Conversely, a Bromwich integral on any line `Re z=c>1/2` reconstructs
`S_(a,m)` from (1.8).  If desired, subtract `S_(a,m)(0)/z` first; for `m>=2`
the remaining transform is `O(|z|^-2)` and the inverse integral is ordinary.
Thus (1.8), not the zero sum, is the admissible source definition.

### 1.3 Symmetric Green equation and prime knots

Let `D=d/dt` and let `mathscr Z` be the positive-frequency explicit-formula
distribution of `PFR-T4`:

\[
\mathscr Z(t)
=
A(t)
-
\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}\,\delta_{\log n}(t),
\qquad t>0.
\tag{1.13}
\]

Modewise application of the symmetric differential operator gives

\[
\boxed{
(a^2-D^2)^m\mathcal S_{a,m}=\mathscr Z
\quad\hbox{on }(0,\infty)
}
\tag{1.14}
\]

in the distributional sense.

Consequently `S_(a,m)` is real analytic between logarithms of prime powers,
and at every prime power `n=p^r`,

\[
\boxed{
\mathcal S_{a,m}^{(2m-1)}((\log n)^+)
-
\mathcal S_{a,m}^{(2m-1)}((\log n)^-)
=
(-1)^{m+1}\frac{\Lambda(n)}{\sqrt n}.
}
\tag{1.15}
\]

All derivatives through order `2m-2` are continuous there.  The highest term
of `(a^2-D^2)^m` is `(-1)^m D^(2m)`, so the jump in (1.15) is exactly the
coefficient required to create the negative prime atom in (1.13).

The parameter ladder is

\[
\boxed{
\partial_a\mathcal S_{a,m}
=-2ma\,\mathcal S_{a,m+1}.
}
\tag{1.16}
\]

There is also a finite bridge back to the one-sided Gamma responses.  The
partial fraction identity

\[
\frac1{(a^2-z^2)^m}
=
\sum_{k=1}^m c_{m,k}(a)
\left[
\frac1{(a-z)^k}+\frac1{(a+z)^k}
\right]
\tag{1.17}
\]

has

\[
\boxed{
 c_{m,k}(a)
=2^{k-2m}
\binom{2m-k-1}{m-k}
 a^{k-2m}.
}
\tag{1.18}
\]

Hence, with the `k=1` terms interpreted distributionally,

\[
\mathcal S_{a,m}(t)
=
\sum_{k=1}^m c_{m,k}(a)
\left[
\mathcal R_{a,k}(t)+\mathcal R_{a,k}(-t)
\right].
\tag{1.19}
\]

The new response is therefore the symmetric completion of the existing
one-sided ladder, not an unrelated fitted detector.

### 1.4 Exact growth and Hardy-space abscissa

The coefficients in (1.5) are nonzero and absolutely summable.  The
Laplace-pole argument of `PFR-R3` applies without change and gives

\[
\boxed{
\limsup_{t\to\infty}
\frac1t\log|\mathcal S_{a,m}(t)|
=B_\xi.
}
\tag{1.20}
\]

For

\[
\mathcal E^{\rm sym}_{a,m}(\sigma)
=
\int_0^\infty
 e^{-2\sigma t}|\mathcal S_{a,m}(t)|^2dt,
\tag{1.21}
\]

one has

\[
\boxed{
B_\xi
=
\inf\left\{
\sigma:\mathcal E^{\rm sym}_{a,m}(\sigma)<\infty
\right\}.
}
\tag{1.22}
\]

For `sigma>B_xi`,

\[
\boxed{
\mathcal E^{\rm sym}_{a,m}(\sigma)
=
\sum_{\rho,\rho'}
\frac{
 (a^2-\lambda_\rho^2)^{-m}
 (a^2-\overline{\lambda_{\rho'}}^{\,2})^{-m}
}
{2\sigma-\lambda_\rho-\overline{\lambda_{\rho'}}}.
}
\tag{1.23}
\]

Equivalently, `M_(a,m)` belongs to the Hardy space of the half-plane
`Re z>sigma` precisely when that half-plane contains no surviving zero pole,
and

\[
\sup_{x>\sigma}
\frac1{2\pi}
\int_{-\infty}^{\infty}
|\mathcal M_{a,m}(x+iy)|^2dy
=
\mathcal E^{\rm sym}_{a,m}(\sigma).
\tag{1.24}
\]

### 1.5 Positive-definite and positive-real RH equivalences

Assume RH.  Every centered zero is `lambda=i gamma`, and

\[
\mathcal S_{a,m}(t)
=
\sum_\gamma
\frac{e^{i\gamma t}}{(a^2+\gamma^2)^m}.
\tag{1.25}
\]

This is the Fourier transform of the finite positive measure

\[
\mu_{a,m}
=
\sum_\gamma
\frac{1}{(a^2+\gamma^2)^m}\,\delta_\gamma.
\tag{1.26}
\]

Therefore `S_(a,m)` is positive definite.  Its Laplace transform is

\[
\mathcal M_{a,m}(z)
=
\int_\mathbb R\frac{d\mu_{a,m}(\gamma)}{z-i\gamma},
\qquad \operatorname{Re}z>0,
\tag{1.27}
\]

so it is positive real:

\[
\operatorname{Re}\mathcal M_{a,m}(z)>0.
\tag{1.28}
\]

Moreover the half-plane Pick kernel is

\[
\boxed{
\mathcal K_{a,m}(z,w)
=
\frac{
\mathcal M_{a,m}(z)+\overline{\mathcal M_{a,m}(w)}
}{z+\overline w}
=
\int_\mathbb R
\frac{d\mu_{a,m}(\gamma)}
{(z-i\gamma)(\overline w+i\gamma)}.
}
\tag{1.29}
\]

It is positive semidefinite.

Conversely, if RH fails, reflection supplies a centered zero `lambda_0` with
`Re lambda_0>0`.  Equation (1.9) has a nonremovable pole there with residue

\[
\frac{m_{\lambda_0}}
{(a^2-\lambda_0^2)^m}\ne0.
\tag{1.30}
\]

The real part of a nonzero simple principal part changes sign around an
interior pole.  Hence positive-realness fails.  Also (1.20) makes
`S_(a,m)` unbounded; every continuous positive-definite function obeys
`|S(t)|<=S(0)`, so positive definiteness fails and a finite Toeplitz witness
exists.

We obtain the exact equivalence stack

\[
\boxed{
\begin{aligned}
\mathrm{RH}
\quad\Longleftrightarrow\quad&
B_\xi=0\\
\Longleftrightarrow\quad&
\mathcal S_{a,m}\text{ is bounded}\\
\Longleftrightarrow\quad&
\mathcal S_{a,m}\text{ is positive definite}\\
\Longleftrightarrow\quad&
\mathcal M_{a,m}\text{ is positive real on }\operatorname{Re}z>0\\
\Longleftrightarrow\quad&
[\mathcal K_{a,m}(z_j,z_k)]_{j,k}\succeq0
\text{ for every finite safe set}\\
\Longleftrightarrow\quad&
\mathcal M_{a,m}\in H^2(\operatorname{Re}z>\sigma)
\text{ for every }\sigma>0.
\end{aligned}
}
\tag{1.31}
\]

This adds an independently motivated positive structure to the real response:
the same source-defined object is simultaneously a prime-knot spline, a
Bochner kernel, a positive-real transfer function, and a Pick Gram kernel.
It still does not prove any of those positive properties from the prime side.

### Literature and non-overlap boundary

Bochner positivity, Herglotz/Caratheodory functions, the Weil criterion, and
Suzuki's screw functions already provide deep positivity formulations of RH.
`PFR-T10` is not claimed to supersede them or to establish external novelty.
Its project-specific content is the exact symmetric completion of
`PFR-T5/PFR-T7`, the safe two-point Hermite source formula, and the simultaneous
prime-knot / growth / Toeplitz / Pick readouts.

---

## 2. PFR-T11 — flower--Speiser Gauss law and harmonic screening

`PFR-T8` identified the open Hardy-flower positive turn as

\[
\int
\left(
\operatorname{Re}
\frac{\zeta''}{\zeta'}
\left(\frac12+it\right)
\right)_+dt.
\tag{2.1}
\]

The next question is whether this positive variation literally counts
left-of-line zeros of `zeta'`.  The answer contains an exact screening term.

### 2.1 Finite polynomial screening theorem

Let `P` be a polynomial and let the observation line `Re s=sigma_0` contain no
zero of `P'`.  Write the critical points as

\[
c_k=\alpha_k+i\beta_k.
\tag{2.2}
\]

Define the nonnegative left and right boundary fields

\[
L(t)
=
\sum_{\alpha_k<\sigma_0}
\frac{\sigma_0-\alpha_k}
{(\sigma_0-\alpha_k)^2+(t-\beta_k)^2},
\tag{2.3}
\]

\[
R(t)
=
\sum_{\alpha_k>\sigma_0}
\frac{\alpha_k-\sigma_0}
{(\alpha_k-\sigma_0)^2+(t-\beta_k)^2}.
\tag{2.4}
\]

Then

\[
\operatorname{Re}\frac{P''}{P'}(\sigma_0+it)
=L(t)-R(t).
\tag{2.5}
\]

Let `N_L,N_R` be the corresponding critical-point counts and put

\[
\mathscr O
=
\int_{-\infty}^{\infty}\min(L(t),R(t))\,dt.
\tag{2.6}
\]

#### Theorem 2.1 — exact harmonic screening ledger

The positive and negative phase-variation masses are

\[
\boxed{
\int_\mathbb R(L-R)_+dt
=
\pi N_L-\mathscr O,
}
\tag{2.7}
\]

\[
\boxed{
\int_\mathbb R(R-L)_+dt
=
\pi N_R-\mathscr O.
}
\tag{2.8}
\]

Hence

\[
\int_\mathbb R(L-R)dt
=
\pi(N_L-N_R),
\tag{2.9}
\]

and

\[
\int_\mathbb R|L-R|dt
=
\pi(N_L+N_R)-2\mathscr O.
\tag{2.10}
\]

#### Proof

Each Poisson kernel has integral `pi`, so `int L=pi N_L` and
`int R=pi N_R`.  Pointwise,

\[
(L-R)_+=L-\min(L,R),
\qquad
(R-L)_+=R-\min(L,R).
\]

Integration gives the result.

The theorem identifies the precise obstruction to counting Speiser defects
from unsigned flower curvature: right-side critical points can screen the
harmonic measure of left-side critical points on the observation line.

### 2.2 PFR-R4 — perfect mirror screening firewall

Take one critical point at

\[
\sigma_0-d+i\beta
\]

and one at

\[
\sigma_0+d+i\beta,
\qquad d>0.
\]

Their two boundary Poisson kernels agree identically and cancel:

\[
\boxed{
\operatorname{Re}\frac{P''}{P'}(\sigma_0+it)=0
\quad\hbox{for every }t,
}
\tag{2.11}
\]

although there is one critical point to the left of the line.  Such a
polynomial exists: take

\[
P'(s)
=C\left(s-(\sigma_0-d+i\beta)\right)
 \left(s-(\sigma_0+d+i\beta)\right)
\]

and integrate once.

Therefore no unsigned or positive-part curvature rule can count left
critical points without a theorem controlling right-side and background
screening.  This is a structural firewall, not a zeta counterexample.

### 2.3 Exact finite-rectangle Gauss law for actual `zeta'`

The pole of `zeta'` is removed by

\[
G(s)=(s-1)^2\zeta'(s).
\tag{2.12}
\]

This is entire and nonzero at `s=1`.  Let

\[
\Omega
=
\{\sigma+it:
\sigma_0<\sigma<1/2,
\ T_0<t<T_1\},
\tag{2.13}
\]

and assume `G` is nonzero on the boundary.  Let `N_G(Omega)` count its zeros
inside, with multiplicity; these are exactly the zeros of `zeta'` in the
rectangle.

Define

\[
J_L
=
\int_{T_0}^{T_1}
\operatorname{Re}\frac{G'}G(\sigma_0+it)dt,
\tag{2.14}
\]

\[
H_T
=
\int_{\sigma_0}^{1/2}
\operatorname{Im}\frac{G'}G(\sigma+iT)d\sigma.
\tag{2.15}
\]

The argument principle, read as a two-dimensional Gauss law for
`log|G|`, gives

\[
\boxed{
\int_{T_0}^{T_1}
\operatorname{Re}\frac{G'}G\left(\frac12+it\right)dt
=
2\pi N_G(\Omega)
+J_L+H_{T_1}-H_{T_0}.
}
\tag{2.16}
\]

Since

\[
\frac{G'}G(s)
=
\frac{\zeta''}{\zeta'}(s)+\frac2{s-1},
\tag{2.17}
\]

and

\[
\operatorname{Re}\frac2{-1/2+it}
=-\frac1{t^2+1/4},
\tag{2.18}
\]

put

\[
f(t)
=
\operatorname{Re}
\frac{\zeta''}{\zeta'}\left(\frac12+it\right),
\tag{2.19}
\]

\[
Q(T_0,T_1)
=
\int_{T_0}^{T_1}\frac{dt}{t^2+1/4}
=
2\arctan(2T_1)-2\arctan(2T_0).
\tag{2.20}
\]

Then

\[
\boxed{
\int_{T_0}^{T_1}f(t)dt
=
2\pi N_G(\Omega)
+Q(T_0,T_1)
+J_L+H_{T_1}-H_{T_0}.
}
\tag{2.21}
\]

Writing

\[
P_{1/2}
=
\int_{T_0}^{T_1}f(t)_+dt,
\qquad
N_{1/2}
=
\int_{T_0}^{T_1}f(t)_-dt,
\tag{2.22}
\]

one obtains the exact screening/flux ledger

\[
\boxed{
P_{1/2}
=
2\pi N_G(\Omega)
+Q(T_0,T_1)
+J_L+H_{T_1}-H_{T_0}
+N_{1/2}.
}
\tag{2.23}
\]

In particular,

\[
\boxed{
2\pi N_G(\Omega)
\le
P_{1/2}
+|J_L|
+|H_{T_1}-H_{T_0}|.
}
\tag{2.24}
\]

Every left-of-critical-line `zeta'` zero must therefore be paid either by
positive flower curvature on the critical line or by explicit flux through
the other three sides.  Positive curvature is not itself the count; it is one
boundary component of the exact count.

### Proof

Traverse the rectangle counterclockwise.  On a horizontal segment,
`d arg G/d sigma=Im G'/G`; on a vertical segment,
`d arg G/dt=Re G'/G`.  Therefore

\[
H_{T_0}
+
\int_{T_0}^{T_1}\operatorname{Re}\frac{G'}G(1/2+it)dt
-
H_{T_1}
-
J_L
=
2\pi N_G(\Omega).
\]

This is (2.16).  Equations (2.17)--(2.23) are algebra, and (2.24) follows by
dropping the nonnegative terms `Q` and `N_(1/2)` and taking absolute values of
the remaining boundary flux.

### 2.4 Combined petal--Speiser conservation inequality

Suppose the critical-line interval is partitioned by simple zeros

\[
\gamma_0<\cdots<\gamma_M,
\qquad
T_0=\gamma_0,
\quad
T_1=\gamma_M,
\tag{2.25}
\]

and the hypotheses of `PFR-T6` hold.  Put

\[
C_{\rm corner}
=
\sum_{j=0}^{M-1}
\left(
\vartheta(\gamma_{j+1})-
\vartheta(\gamma_j)-\pi
\right)_+.
\tag{2.26}
\]

`PFR-T6` gives

\[
M
\ge
\frac{\vartheta(\gamma_M)-\vartheta(\gamma_0)}\pi
-
\frac{P_{1/2}+C_{\rm corner}}\pi.
\tag{2.27}
\]

Substituting (2.23) yields

\[
\boxed{
\begin{aligned}
M+2N_G(\Omega)
\ge{}&
\frac{\vartheta(\gamma_M)-\vartheta(\gamma_0)}\pi\\
&-
\frac{
Q+J_L+H_{T_1}-H_{T_0}
+N_{1/2}+C_{\rm corner}
}{\pi}.
\end{aligned}
}
\tag{2.28}
\]

This is the exact finite-window conservation law suggested by the flower
picture: critical-line petals and left-side derivative zeros share one phase
budget, while negative variation, the pole correction, and endpoint/side flux
form the screening remainder.

It is not yet a new zero-count theorem.  A useful consequence requires bounds
on the signed boundary and screening terms that are not supplied by the
argument principle itself.

### Literature and non-overlap boundary

The argument principle, Speiser's theorem, and the relation between curvature
and `Re(zeta''/zeta')` are classical or published.  `PFR-T11` claims only the
project synthesis: the exact harmonic-overlap term, the finite rectangle flux
ledger in the normalization used by the flower packet, and its insertion into
the `PFR-T6` petal-count inequality.

---

## 3. What this pass changes

### Real-only lane

The earlier response was an RH-equivalent growth sensor with a prime-knot
source.  The symmetric completion now supplies the structural positivity that
was missing:

```text
prime source
  -> symmetric Green spline
  -> local Lambda(n)/sqrt(n) jumps
  -> global zero-displacement abscissa
  -> under RH, one positive spectral measure
  -> Toeplitz positivity + positive-real transfer + Pick Gram positivity.
```

The exact remaining theorem is to prove any one of these positive properties
directly from the safe prime/Hermite source.  That remains RH-strength.

### Flower lane

The earlier packet identified the positive curvature defect.  The new Gauss
law shows exactly how it interacts with Speiser zeros:

```text
left zeta' zeros
  -> interior logarithmic charges
  -> critical-line positive phase flux
     plus left/horizontal boundary flux
     minus harmonic screening.
```

The exact remaining theorem is a source or global-geometry estimate preventing
right-side/background screening and controlling the finite-window flux.

---

## 4. Result ledger

```text
PFR-T10 symmetric Xi resolvent convergence/reality          PROVED EXACT
PFR-T10 safe two-point Hermite source formula                PROVED EXACT
PFR-T10 symmetric Green equation and prime-knot jumps        PROVED EXACT
PFR-T10 growth / L2 / Hardy abscissa = Theta-1/2             PROVED EXACT
PFR-T10 RH <-> Toeplitz / positive-real / Pick positivity    PROVED EXACT
PFR-T11 finite harmonic screening identity                   PROVED EXACT
PFR-R4 perfect mirror screening firewall                     PROVED EXACT
PFR-T11 actual-zeta-prime rectangle Gauss law                PROVED EXACT
PFR-T11 combined petal--Speiser conservation inequality      PROVED EXACT
prime-side proof of symmetric positivity                     OPEN / RH-STRENGTH
screening and boundary-flux estimate                         OPEN / RH-BEARING
new critical-line zero proportion                            NONE
Riemann Hypothesis                                           UNPROVEN
```

---

## 5. Replay boundary

The accompanying verifier checks:

- the finite two-point Hermite identity;
- the partial-fraction bridge to the one-sided ladder;
- positive Toeplitz behavior for a real-zero model;
- a negative two-point witness for one off-axis quartet;
- the finite weighted-energy boundary;
- the `m=2` symmetric prime-knot jump normalization;
- the finite harmonic screening identity;
- the perfect mirror-screening firewall;
- the finite rectangle Gauss ledger;
- one high-precision actual-Xi safe-Hermite / verified-zero-prefix regression.

The actual-Xi comparison is `NON_DIRECTED_HIGH_PRECISION`.  The verifier does
not machine-prove the analytic arguments or certify external novelty.

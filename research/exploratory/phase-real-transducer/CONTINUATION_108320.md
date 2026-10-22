# Phase-flow / real-transducer continuation: prime knots, curvature--Speiser flow, and finite-horizon localization

## Status

Claim namespace: `PFR-T7`, `PFR-T8`, `PFR-R3`, `PFR-T9`  
Status: **EXACT ANALYTIC CONTINUATION / PROJECT SYNTHESIS / ONE NEW NO-GO**  
Parent: `PFR-T5`, `PFR-T6`, `PFR-R2` at branch head
`4a78ba3ca89dcb63fcccf50d6738f01e28c80c64`  
RH status: **unproved**

This pass continues both live directions without introducing another RH
criterion by renaming:

```text
real-only response:
  actual-Xi Gamma resolvent
      -> a real prime-knot spline
      -> local derivative jumps recover Lambda(n)/sqrt(n)
      -> global growth still recovers the zero displacement;

flower/flow geometry:
  Hardy petal curvature defect
      -> phase acceleration of zeta'
      -> a signed Poisson field of derivative critical points in finite models;

height localization:
  hard holomorphic window is impossible
      -> nonvanishing filters preserve the infinite-time abscissa
      -> complex Gamma filters give quantitative soft localization
         on every finite real-time horizon.
```

No external priority is claimed.  In particular, the basic curvature identity

\[
\operatorname{sign}\kappa_{\zeta(\sigma+i\cdot)}(t)
=
\operatorname{sign}\operatorname{Re}
\frac{\zeta''}{\zeta'}(\sigma+it)
\]

is known and is discussed explicitly by Sourmelidis--Steuding, building on
Gonek--Montgomery and Yildirim; see Sourmelidis--Steuding, *Spirals of
Riemann's Zeta-Function---Curvature, Denseness, and Universality*,
Math. Proc. Cambridge Philos. Soc. (2023), DOI
`10.1017/S0305004123000543`, arXiv `2306.00460`.  The new project
contribution in `PFR-T8` is
the exact identification of the `PFR-T6` curvature-defect budget with the
positive variation of this derivative phase, together with the finite
critical-point Poisson transducer used as a Speiser-compatible model.

---

## 1. PFR-T7 — the actual-Xi resolvent is a real prime-knot spline

Recall the `PFR-T5` response.  Put

\[
\lambda_\rho=\rho-\frac12,
\qquad a>\frac12,
\qquad m\ge2,
\]

and define

\[
\mathcal R_{a,m}(t)
=
\sum_\rho
\frac{e^{\lambda_\rho t}}{(a-\lambda_\rho)^m},
\qquad t\ge0.
\tag{1.1}
\]

The response has the source-only expression

\[
\boxed{
\begin{aligned}
\mathcal R_{a,m}(t)
={}&
\frac{e^{t/2}}{(a-1/2)^m}
+
\frac{e^{-t/2}}{(a+1/2)^m}\\
&-
\sum_{k\ge0}
\frac{e^{-(2k+1/2)t}}{(a+2k+1/2)^m}\\
&-
\frac{e^{at}}{(m-1)!}
\sum_{n\ge2}
\frac{\Lambda(n)}{n^{a+1/2}}
(\log n-t)_+^{m-1}.
\end{aligned}
}
\tag{1.2}
\]

### Theorem 1.1 — prime-knot regularity and universal jumps

The function `R_(a,m)` is real-valued and belongs to

\[
C^{m-2}((0,\infty)).
\]

It is real analytic on every component of

\[
(0,\infty)
\setminus
\{\log n:\Lambda(n)\ne0\}.
\]

At every prime power `n=p^r`, its derivative of order `m-1` has the exact jump

\[
\boxed{
\mathcal R_{a,m}^{(m-1)}((\log n)^+)
-
\mathcal R_{a,m}^{(m-1)}((\log n)^-)
=
(-1)^{m+1}\frac{\Lambda(n)}{\sqrt n}.
}
\tag{1.3}
\]

The jump is independent of the safe parameter `a`.  At integers which are not
prime powers, the jump is zero.

Thus the same one-dimensional real function has two exact and very different
readouts:

```text
local singularity data:
  knots at log(p^r), jump size Lambda(p^r)/sqrt(p^r);

global large-t data:
  limsup log|R_(a,m)(t)|/t = Theta-1/2.
```

### Proof

Only one summand can lose smoothness at a fixed knot.  Write `tau=log n`.  The
prime-power term in (1.2) is

\[
F_n(t)
=-
\frac{\Lambda(n)n^{-a-1/2}}{(m-1)!}
 e^{at}(\tau-t)_+^{m-1}.
\tag{1.4}
\]

All derivatives through order `m-2` vanish at `t=tau` from the left and are
zero from the right.  In the derivative of order `m-1`, every Leibniz term in
which a derivative hits `e^(at)` still contains a positive power of
`tau-t` and vanishes at the knot.  The sole surviving left limit is

\[
-
\frac{\Lambda(n)n^{-a-1/2}}{(m-1)!}
 e^{a\tau}
 (-1)^{m-1}(m-1)!
=
(-1)^m\frac{\Lambda(n)}{\sqrt n}.
\]

The right limit is zero, giving (1.3).  Uniform convergence of the differentiated
source series on compact knot-free intervals follows from
`a+1/2>1`; arbitrary logarithmic powers remain summable against
`n^(-a-1/2)`.  The completion terms are analytic.

### Theorem 1.2 — resolvent differential ladder

Let `D=d/dt`, and let `mathscr Z` denote the positive-frequency explicit-formula
distribution from `PFR-T4`:

\[
\mathscr Z(t)
=
A(t)
-
\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\,\delta_{\log n}(t),
\tag{1.5}
\]

where

\[
A(t)
=e^{t/2}+e^{-t/2}
-
\frac{e^{-t/2}}{1-e^{-2t}}
\qquad(t>0).
\]

Then, distributionally,

\[
\boxed{
(a-D)^m\mathcal R_{a,m}=\mathscr Z.
}
\tag{1.6}
\]

More generally,

\[
(a-D)\mathcal R_{a,m}=\mathcal R_{a,m-1}
\tag{1.7}
\]

whenever the lower rung is interpreted distributionally, and

\[
\boxed{
\partial_a\mathcal R_{a,m}
=-m\mathcal R_{a,m+1}.
}
\tag{1.8}
\]

### Proof

Each exponential mode satisfies

\[
(a-D)^m
\frac{e^{\lambda t}}{(a-\lambda)^m}
=e^{\lambda t}.
\]

Normal convergence from `PFR-T5` permits the operation distributionally.
Equation (1.8) follows by differentiating the normally convergent zero series;
it also follows directly from the Gamma-resolvent kernel.

### Consequence

`PFR-T5` may now be read as a source-defined real spectral transducer rather
than only an RH-equivalent bound:

\[
\boxed{
\begin{array}{c}
\text{prime-power measure}\cr
\displaystyle\sum \Lambda(n)n^{-1/2}\delta_{\log n}
\end{array}
\quad\xleftrightarrow{\ (a-D)^{-m}\ }
\quad
\mathcal R_{a,m}
\quad\xrightarrow{\ \text{growth / }L^2\text{ abscissa}\ }
\quad
\Theta-\frac12.
}
\tag{1.9}
\]

The operator does not prove boundedness.  It displays, in one real object,
where the prime data enter locally and where the zero displacement appears
globally.

---

## 2. PFR-T8 — Hardy curvature is the phase acceleration of `zeta'`

Let

\[
s=\frac12+it,
\qquad
\Gamma(t)=\zeta(s)=e^{-i\vartheta(t)}Z(t),
\]

and retain the `PFR-T6` fields

\[
D_H(t)=\vartheta'(t)^2Z(t)^2+Z'(t)^2,
\tag{2.1}
\]

\[
\mathfrak C_H(t)
=
\vartheta'(t)^2 Z(t)^2
+2Z'(t)^2
-Z(t)Z''(t)
+
\frac{\vartheta''(t)}{\vartheta'(t)}Z(t)Z'(t).
\tag{2.2}
\]

On an open petal, `Z` is nonzero and `vartheta'>0`, so `zeta'(s)` cannot
vanish: from

\[
\Gamma'(t)
=e^{-i\vartheta(t)}
\bigl(Z'(t)-i\vartheta'(t)Z(t)\bigr)
=i\zeta'(s),
\]

its imaginary radial component is nonzero.

### Theorem 2.1 — exact curvature--derivative bridge

On every open Hardy petal,

\[
\boxed{D_H(t)=|\zeta'(s)|^2,}
\tag{2.3}
\]

\[
\boxed{
-\vartheta'(t)\mathfrak C_H(t)
=
\operatorname{Re}
\bigl(\overline{\zeta'(s)}\,\zeta''(s)\bigr),
}
\tag{2.4}
\]

and hence

\[
\boxed{
-\frac{\vartheta'(t)\mathfrak C_H(t)}{D_H(t)}
=
\operatorname{Re}\frac{\zeta''}{\zeta'}(s)
=
\frac{d}{dt}\arg\zeta'(s).
}
\tag{2.5}
\]

Equivalently, clockwise flower curvature is horizontal decay of `|zeta'|`:

\[
\boxed{
\mathfrak C_H(t)\ge0
\quad\Longleftrightarrow\quad
\left.
\partial_\sigma |\zeta'(\sigma+it)|^2
\right|_{\sigma=1/2}
\le0.
}
\tag{2.6}
\]

The sign relation in (2.5) is classical.  Equations (2.3)--(2.6) identify its
literal place inside the `PFR-T6` defect ledger.

### Proof

The first equality follows by taking the modulus of `Gamma'=i zeta'`.
Moreover,

\[
\Gamma''(t)=-\zeta''(s),
\]

so

\[
\operatorname{Im}
(\overline{\Gamma'(t)}\Gamma''(t))
=
\operatorname{Re}
(\overline{\zeta'(s)}\zeta''(s)).
\tag{2.7}
\]

Under the change of variable `phi=vartheta(t)`, the same curvature numerator
is

\[
\vartheta'(t)^3
\bigl(rr''-r^2-2r'^2\bigr)
=-\vartheta'(t)\mathfrak C_H(t),
\]

which proves (2.4).  Division by (2.3) gives (2.5).  Finally,

\[
\partial_\sigma|\zeta'(\sigma+it)|^2
=2\operatorname{Re}(\overline{\zeta'}\zeta'')
\]

gives (2.6).

### Corollary 2.2 — the flower defect is positive derivative-phase variation

For a simple petal `[gamma_j,gamma_(j+1)]`, the open positive-turn mass of
`PFR-T6` is exactly

\[
\boxed{
P_{\mathrm{open},j}
=
\int_{\gamma_j}^{\gamma_{j+1}}
\left(
\operatorname{Re}
\frac{\zeta''}{\zeta'}
\left(\frac12+it\right)
\right)_+dt.
}
\tag{2.8}
\]

Thus the total petal defect is

\[
\boxed{
\mathcal D_j
=
\int_{\gamma_j}^{\gamma_{j+1}}
\left(
\operatorname{Re}
\frac{\zeta''}{\zeta'}
\left(\frac12+it\right)
\right)_+dt
+
(\Delta\vartheta_j-\pi)_+.
}
\tag{2.9}
\]

The curvature-defect zero-count inequality becomes

\[
\boxed{
M
\ge
\frac{\vartheta(\gamma_M)-\vartheta(\gamma_0)}{\pi}
-
\frac1\pi
\sum_{j=0}^{M-1}
\left[
\int_{\gamma_j}^{\gamma_{j+1}}
\left(\operatorname{Re}\frac{\zeta''}{\zeta'}\right)_+dt
+
(\Delta\vartheta_j-\pi)_+
\right].
}
\tag{2.10}
\]

This does not control the positive variation.  It identifies the exact
Speiser-facing quantity that a flower proof must pay.

### Theorem 2.3 — finite critical-point Poisson transducer

Let `P` be a polynomial, let `sigma_0` be a vertical observation line containing
no zero of `P'`, and let

\[
\Gamma_P(t)=P(\sigma_0+it).
\]

If the critical points of `P` are

\[
c_k=\alpha_k+i\beta_k
\]

with multiplicity, then

\[
\boxed{
\frac{d}{dt}\arg\Gamma_P'(t)
=
\operatorname{Re}\frac{P''}{P'}(\sigma_0+it)
=
\sum_k
\frac{\sigma_0-\alpha_k}
{(\sigma_0-\alpha_k)^2+(t-\beta_k)^2}.
}
\tag{2.11}
\]

Critical points to the left of the line generate positive Poisson kernels;
critical points to the right generate negative ones.  Over the complete real
line,

\[
\boxed{
\frac1\pi
\int_{-\infty}^{\infty}
\operatorname{Re}\frac{P''}{P'}(\sigma_0+it)\,dt
=
N_L-N_R,
}
\tag{2.12}
\]

where `N_L,N_R` count critical points to the left and right of the line.
In particular, if all critical points lie strictly to the right, the image
curve has nonpositive signed curvature everywhere.

### Proof

Factor

\[
P'(s)=C\prod_k(s-c_k).
\]

Then `P''/P'=sum 1/(s-c_k)`, and taking real parts on the line gives
(2.11).  Each kernel integrates to `pi sign(sigma_0-alpha_k)`, proving
(2.12).

### Boundary

For actual `zeta'`, a canonical-product decomposition also contains the pole,
trivial/background, and regularization terms.  `PFR-T8` does not identify the
positive part in (2.8) with a bare count of left-of-line `zeta'` zeros.  The
finite theorem explains the correct signed-Poisson mechanism; the global zeta
adapter still requires the full Speiser ledger.

---

## 3. PFR-R3 — nonvanishing filters cannot localize the infinite-time abscissa

The hard-window obstruction `PFR-R2` rules out a holomorphic multiplier that is
zero on one open ordinate band and nonzero on another.  The next result shows
that merely making the unwanted modes very small also cannot change the
infinite-time convergence boundary.

### Theorem 3.1 — filtered exponential abscissa

Let `Lambda` be a locally finite set of distinct complex exponents with

\[
B=\sup_{\lambda\in\Lambda}\operatorname{Re}\lambda<\infty.
\]

Repeated exponents, including zero multiplicities, are first grouped into a
single aggregate coefficient.  Assume the resulting family is nonempty.  Let
coefficients `c_lambda` satisfy

\[
\sum_{\lambda}|c_\lambda|<\infty
\]

and suppose the meromorphic series

\[
M(z)=\sum_\lambda\frac{c_\lambda}{z-\lambda}
\]

converges normally away from its poles.  Put

\[
R(t)=\sum_\lambda c_\lambda e^{\lambda t}.
\]

Let

\[
B_c=\sup\{\operatorname{Re}\lambda:c_\lambda\ne0\}.
\]

Then

\[
\boxed{
\limsup_{t\to\infty}\frac1t\log|R(t)|=B_c,
}
\tag{3.1}
\]

and

\[
\boxed{
\inf\left\{\sigma:
\int_0^\infty e^{-2\sigma t}|R(t)|^2dt<\infty
\right\}
=B_c.
}
\tag{3.2}
\]

The proof is the Laplace-pole argument of `PFR-T5`: any smaller exponential or
`L2` boundary would analytically continue `M` across a pole whose residue is
the nonzero aggregated coefficient at that distinct exponent.

### Corollary 3.2 — Gamma filters preserve the global Xi abscissa

Let

\[
q=a+iT,
\qquad a>\frac12,
\qquad m\ge2,
\]

and define

\[
\mathcal R_{q,m}(t)
=
\sum_\rho
\frac{e^{(\rho-1/2)t}}
{(q-(\rho-1/2))^m}.
\tag{3.3}
\]

The multiplier has no zeros.  Hence

\[
\boxed{
\limsup_{t\to\infty}
\frac1t\log|\mathcal R_{q,m}(t)|
=
\Theta-\frac12,
}
\tag{3.4}
\]

and its infinite-time weighted-energy abscissa is again `Theta-1/2`, no matter
where the ordinate center `T` is placed.

Therefore an exact local-height abscissa cannot be obtained by a
zero-independent nonvanishing holomorphic filter.  To alter the asymptotic
abscissa the filter must annihilate every unwanted extremal mode, which is
zero-location-dependent; `PFR-R2` rules out achieving this by an open-band
holomorphic cutoff.

---

## 4. PFR-T9 — complex Gamma filters give finite-horizon soft localization

Although a nonvanishing filter cannot alter the infinite-time exponent, it can
suppress remote ordinates by an arbitrarily high algebraic order before that
asymptotic leakage takes over.

### Theorem 4.1 — complex source formula

For `q=a+iT`, `a>1/2`, and integer `m>=2`, the response (3.3) has the
zero-free source representation

\[
\boxed{
\begin{aligned}
\mathcal R_{q,m}(t)
={}&
\frac{e^{t/2}}{(q-1/2)^m}
+
\frac{e^{-t/2}}{(q+1/2)^m}\\
&-
\sum_{k\ge0}
\frac{e^{-(2k+1/2)t}}{(q+2k+1/2)^m}\\
&-
\frac{e^{qt}}{(m-1)!}
\sum_{n\ge2}
\frac{\Lambda(n)}{n^{q+1/2}}
(\log n-t)_+^{m-1}.
\end{aligned}
}
\tag{4.1}
\]

Both source series converge absolutely.  Its real and imaginary parts are two
entirely real prime/archimedean channels.

### Proof

Use the complex Gamma resolvent

\[
(\mathsf G_{q,m}F)(t)
=
\frac1{(m-1)!}
\int_0^\infty u^{m-1}e^{-qu}F(t+u)\,du.
\]

Since `Re(q)>1/2`, it is integrable against every centered zero mode and every
completion mode.  On `e^(lambda t)` its multiplier is `(q-lambda)^(-m)`.
Applying it to `PFR-T4`, with cutoff and dominated convergence, gives (4.1).

### Theorem 4.2 — coefficientwise soft band separation

Fix a target half-width `w` and guard width `W` with

\[
0\le w<W.
\]

For centered zeros `lambda=delta+i gamma`, define

\[
D_{\rm in}
=
\sqrt{(a+1/2)^2+w^2},
\qquad
D_{\rm out}
=
\sqrt{(a-1/2)^2+W^2}.
\tag{4.2}
\]

Assume `D_out>D_in`, and normalize

\[
H_{m,T}(\lambda)
=
\left(
\frac{D_{\rm in}}{a+iT-\lambda}
\right)^m.
\tag{4.3}
\]

Then every zero in the target band `|gamma-T|<=w` obeys

\[
\boxed{|H_{m,T}(\lambda)|\ge1,}
\tag{4.4}
\]

whereas every zero outside the guard band `|gamma-T|>=W` obeys

\[
\boxed{
|H_{m,T}(\lambda)|
\le
\eta^m,
\qquad
\eta=\frac{D_{\rm in}}{D_{\rm out}}<1.
}
\tag{4.5}
\]

This is an exact, zero-independent soft ordinate filter.

### Theorem 4.3 — finite-horizon leakage bound

Let `R_out` be the part of the normalized response coming from zeros outside
the guard band, and put

\[
C_{\rm out}
=
\sum_{|\gamma-T|\ge W}|H_{m,T}(\lambda_\rho)|.
\tag{4.6}
\]

The sum is finite.  For every horizon `L>0` and real damping `sigma`,

\[
\boxed{
\left\|e^{-\sigma t}R_{\rm out}(t)\right\|_{L^2(0,L)}
\le
C_{\rm out}\,
\Phi\!\left(\frac12-\sigma,L\right),
}
\tag{4.7}
\]

where

\[
\Phi(x,L)
=
\left(\int_0^L e^{2xt}\,dt\right)^{1/2}
=
\begin{cases}
\left((e^{2xL}-1)/(2x)\right)^{1/2},&x\ne0,\\
\sqrt L,&x=0.
\end{cases}
\tag{4.8}
\]

If `R_full=R_in+R_transition+R_out`, Minkowski gives the corresponding norm
error after the transition band is accounted for:

\[
\left|
\|e^{-\sigma t}R_{\rm full}\|_2
-
\|e^{-\sigma t}(R_{\rm in}+R_{\rm transition})\|_2
\right|
\le C_{\rm out}\Phi(1/2-\sigma,L).
\tag{4.9}
\]

Using `N(U+1)-N(U)=O(log(U+2))`, one also has, for `W>=2`,

\[
C_{\rm out}
\ll
D_{\rm in}^m
\sum_{k\ge W-1}
\frac{\log(3+|T|+k)}
{((a-1/2)^2+k^2)^{m/2}},
\tag{4.10}
\]

and hence

\[
C_{\rm out}
\ll_{a,m}
D_{\rm in}^m
W^{1-m}\log(3+|T|+W).
\tag{4.11}
\]

### Proof

For a centered zero,

\[
|a+iT-\lambda|^2
=(a-\delta)^2+(T-\gamma)^2.
\]

Since `|delta|<1/2`, the target and exterior bounds give (4.4)--(4.5).
For `t>=0`, every zero mode is bounded by `e^(t/2)`, so

\[
|R_{\rm out}(t)|
\le C_{\rm out}e^{t/2},
\]

which proves (4.7).  The zero-count estimate in unit ordinate intervals gives
(4.10), and integral comparison gives (4.11).

### Interpretation and exact remaining burden

`PFR-R2`, `PFR-R3`, and `PFR-T9` together give a sharp design boundary:

```text
hard holomorphic band                  impossible;
nonvanishing filter, infinite horizon  global abscissa unchanged;
soft Gamma band, finite horizon         explicit leakage control available.
```

The next nontrivial theorem is not another filter.  It is a **source-defined
in-band lower frame bound** strong enough to distinguish a true target-band
mode from cancellation among the transition and in-band modes.  Without that
lower bound, (4.7) is a leakage certificate rather than a local zero theorem.

---

## 5. Result ledger

```text
PFR-T7 prime-knot regularity and universal jump law       PROVED EXACT
PFR-T7 resolvent differential/parameter ladder            PROVED EXACT
PFR-T8 Hardy curvature = zeta' phase acceleration          KNOWN IDENTITY / EXACT PROJECT ADAPTER
PFR-T8 finite critical-point signed Poisson field          PROVED EXACT FINITE MODEL
PFR-R3 nonvanishing-filter abscissa invariance             PROVED EXACT
PFR-T9 complex Gamma source formula                        PROVED EXACT
PFR-T9 soft-band coefficient separation                    PROVED EXACT
PFR-T9 finite-horizon leakage bound                        PROVED EXACT
source-defined in-band lower frame bound                   OPEN
full zeta-prime Speiser/background decomposition           OPEN
prime-side boundedness of the global real spline           OPEN / RH-STRENGTH
Riemann Hypothesis                                         UNPROVEN
```

## 6. Novelty and scope firewall

This continuation does **not** claim:

- priority for the curvature identity `sign(kappa)=sign Re(zeta''/zeta')`;
- an unconditional curvature sign on the critical line;
- a count of left-of-line `zeta'` zeros from the positive curvature part alone;
- an exact height-localized asymptotic abscissa;
- a lower frame bound for the selected band;
- boundedness of `R_(a,m)`;
- RH or GRH.

The mathematical advances are the prime-knot/differential structure of the
actual-Xi resolvent, the exact insertion of derivative-phase variation into
the flower count ledger, and the hard/infinite-time/finite-horizon trichotomy
for ordinate localization.

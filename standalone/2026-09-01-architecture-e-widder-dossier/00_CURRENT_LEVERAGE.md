# Current leading state: four exact source gates for Architecture E

Status: **PROPOSED PROOF-ORIENTED SYNTHESIS; INDEPENDENT REVIEW REQUIRED; THE RIEMANN HYPOTHESIS REMAINS UNPROVED.**

This is the current front door for PR #785.  The branch has moved beyond a
finite Widder-order campaign.  The invariant formulation now supplies four
exact, mutually compatible source gates:

1. one positive-coefficient count law and one quasi-free determinant gate;
2. one all-orders radial resolvent with a canonical pole for every off-line
   invariant zero;
3. one fixed-centre zero heat trace whose complete monotonicity is equivalent
   to RH;
4. one continuous Cauchy–Binet formula isolating every positive-index
   Toeplitz minor in a theta–Darboux exterior current paired with a strictly
   totally-positive Pascal/Bessel kernel.

None of the four final source signs is proved.  Their value is that the
remaining burden is no longer a vague request for positivity and no longer an
order-by-order derivative problem.

## 1. The invariant function and count law

Let

\[
 \mathfrak X(s(s-1))=\xi_{\rm R}(s),
 \qquad
 \mathfrak X(u)=\sum_{n\ge0}c_nu^n.
\]

The actual positive theta source gives

\[
 \boxed{c_n>0\quad(n\ge0).}
\]

For every `v>0`,

\[
 P_v(z)=\frac{\mathfrak X(vz)}{\mathfrak X(v)}
\]

is therefore the probability-generating function of an integer-valued count
`N_v`.

The one-scale Aissen–Schoenberg–Whitney–Edrei criterion gives

\[
 \boxed{
 \mathrm{RH}
 \iff (c_nv^n/\mathfrak X(v))_{n\ge0}\text{ is }PF_\infty
 \iff N_v\text{ is Poisson-binomial}
 }
\]

for one, equivalently every, `v>0`.  Equivalently, RH asks for one positive
trace-class contraction `K_v` with

\[
 \boxed{
 P_v(z)=\det(I-K_v+zK_v).
 }
 \tag{TQF}
\]

The theta source gives an explicit positive mixture of quasi-free Bernoulli
fibres, including the vacuum atom, the latent scale `tau`, a forced
occupation, and the half-integer modes.  The missing theorem is not fibre
positivity; it is removal of the common latent selector while preserving all
exterior powers simultaneously.

Read
[`09_INVARIANT_ORDER_PRODUCT_AND_COUNT_LAW.md`](09_INVARIANT_ORDER_PRODUCT_AND_COUNT_LAW.md)
and
[`10_THETA_FOCK_MIXTURE_AND_QUASIFREE_GATE.md`](10_THETA_FOCK_MIXTURE_AND_QUASIFREE_GATE.md).

## 2. All Widder orders are one radial resolvent

Define

\[
 q(u)=2\frac{\mathfrak X'(u)}{\mathfrak X(u)},
 \qquad
 \mathcal W_k(u)=(-1)^{k-1}D_u^{2k-1}[u^kq(u)]
\]

and

\[
 C_k(u)=\frac{(4u)^k}{2(2k-1)!}\mathcal W_k(u).
\]

For one invariant zero parameter

\[
 a=-\rho(\rho-1),
\]

put

\[
 \lambda_u(a)=\frac{4ua}{(u+a)^2}.
\]

Then, without assuming RH,

\[
 \boxed{C_k(u)=\sum_a\lambda_u(a)^k.}
\]

If `a=re^(i alpha)` and `u=re^v`,

\[
 \lambda_u(a)
 =\operatorname{sech}^2\left(\frac{v-i\alpha}{2}\right).
\]

At the canonical scale `u=|a|`, a nonreal invariant atom becomes the real
number

\[
 \lambda_{|a|}(a)=\sec^2(\alpha/2)>1.
\]

The complete order-generating function is

\[
 \boxed{
 \mathscr R_u(w)
 =\sum_{k\ge1}C_k(u)w^{k-1}
 =\frac{2u}{\zeta-\zeta^{-1}}
 \left[
  \zeta q(u\zeta)-\zeta^{-1}q(u\zeta^{-1})
 \right],
 }
\]

where

\[
 \zeta+\zeta^{-1}=2(1-2w).
\]

For `w=sin^2(theta/2)`,

\[
 \boxed{
 \mathscr R_u(w)
 =\frac{2u}{\sin\theta}
 \Im(e^{i\theta}q(ue^{i\theta}))
 =\frac{4u}{\sin\theta}\frac d{du}
  \arg\mathfrak X(ue^{i\theta}).
 }
\]

A nonreal invariant pair has the exact positivity threshold

\[
 w<\cos^2(\alpha/2)
\]

and creates, at `u=|a|`, a noncancellable pole of residue `-2m` at

\[
 w_a=\cos^2(\alpha/2)\in(1/2,1).
\]

Hence

\[
 \boxed{
 \mathrm{RH}
 \iff \mathscr R_u\text{ is holomorphic in }|w|<1\text{ for every }u>0
 }
\]

and also

\[
 \boxed{
 \mathrm{RH}
 \iff \mathscr R_u(w)\ge0
 \quad(u>0,\ 0<w<1).
 }
\]

The critical strip alone proves the complete resummed inequality

\[
 \boxed{
 \mathscr R_u(w)>0
 \quad(u>0,\ 0\le w\le1/2)
 }
\]

unconditionally.  This same half-ray is the sharp interval on which the
radial formula remains uniformly in the absolutely-convergent Euler
half-plane.

The published RH verification through `H=3*10^12` expands the positive ray to

\[
 0\le w\le
 \frac12\left(1+\frac{H}{\sqrt{H^2+1}}\right).
\]

Thus every possible real-ray failure is confined to a terminal annulus of
width

\[
 \boxed{<2.78\cdot10^{-26}}
\]

adjacent to `w=1`.  The external verification is imported through the
existing repository lock and was not rerun.

Read
[`09_INVARIANT_RESOLVENT_AND_HEAT_TRACE.md`](09_INVARIANT_RESOLVENT_AND_HEAT_TRACE.md).

## 3. One fixed-centre heat trace contains every Widder sign

Define

\[
 \boxed{
 K(t)=2\sum_a e^{-at}.
 }
\]

For the centred zero coordinate

\[
 \gamma_\rho=(\rho-1/2)/i,
\]

we have

\[
 \boxed{
 K(t)=e^{-t/4}\sum_\rho e^{-t\gamma_\rho^2}.
 }
\]

Moreover

\[
 q(u)=\int_0^\infty e^{-ut}K(t)\,dt
\]

and

\[
 \boxed{
 \mathcal W_k(u)
 =\int_0^\infty
 t^{2k-1}e^{-ut}(-1)^kK^{(k)}(t)\,dt.
 }
\]

Consequently

\[
 \boxed{
 \mathrm{RH}
 \iff K\text{ is completely monotone on }(0,\infty).
 }
 \tag{HCM}
\]

This identifies Architecture E with the fixed-centre section of the existing
zero-heat programme:

```text
First-Hermite criterion: every real centre, first heat derivative;
E–Widder criterion:      one invariant centre, every heat derivative.
```

The explicit Guinand–Weil source is

\[
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
\]

The movable Fourier-centre cosine has disappeared.  The all-order problem is
now complete monotonicity of one nonoscillatory gamma-plus-prime heat source.

## 4. Every positive-index Toeplitz minor has one source exterior integral

Define

\[
 b_n(\tau)
 =[u^n]\cosh\left(\tau\sqrt{u+\frac14}\right)
\]

and

\[
 L=D_\tau^2-\frac14.
\]

Then

\[
 c_n=2\int_0^\infty\Phi(\tau)b_n(\tau)d\tau,
 \qquad
 Lb_n=b_{n-1}.
\]

The coefficient kernel has the exact Pascal composition

\[
 b_n(\tau)
 =\sum_{m\ge n}
 \binom mn4^{-(m-n)}\frac{\tau^{2m}}{(2m)!},
\]

which proves that

\[
 \boxed{(\tau,n)\longmapsto b_n(\tau)}
\]

is strictly totally positive of infinite order.

Let `I=(i_1<...<i_r)` and `J=(j_1<...<j_r)` satisfy `j_1>=i_r`, so every
Toeplitz entry has nonnegative coefficient index.  Put

\[
 h_p=i_p-i_1,
 \qquad n_q=j_q-i_1.
\]

Repeated self-adjoint transport of `L`, followed by Andreief, gives

\[
 \boxed{
 \begin{aligned}
 \det[c_{j_q-i_p}]
 ={}&2^r\int_{0<\tau_1<\cdots<\tau_r}
 \det[(L^{h_p}\Phi)(\tau_\ell)]_{p,\ell}\\
 &\qquad\qquad\cdot
 \det[b_{n_q}(\tau_\ell)]_{q,\ell}
 \,d\boldsymbol\tau.
 \end{aligned}
 }
 \tag{TDA}
\]

The second determinant is strictly positive.  Every arithmetic sign is
isolated in one actual theta–Darboux exterior current.

This is the continuous Cauchy–Binet form of the latent-selector gate.  It does
not replace a mixture of determinants by a determinant of an average.  It
keeps the common theta scale until the exterior pairing is complete.

Read
[`13_THETA_DARBOUX_ANDREIEF_GATE.md`](13_THETA_DARBOUX_ANDREIEF_GATE.md).

## 5. Imported coefficient regions and exact duality

The dossier also retains:

- the verified-height Toeplitz sector through order
  `9,419,999,999,999` at every shift;
- the imported centred cubic wedge `k>=10^18 r^3`;
- the exact reciprocal rectangle identity exchanging Toeplitz order and
  shift;
- the finite-height E–Widder cone through order
  `4,710,000,000,000`.

These are large unconditional regions, but they do not cover the broad
central cone in which both exterior rank and coefficient shift grow.

Read
[`11_TOEPLITZ_SECTOR_AND_RECIPROCAL_DUALITY.md`](11_TOEPLITZ_SECTOR_AND_RECIPROCAL_DUALITY.md)
and
[`08_FINITE_HEIGHT_WIDDER_CONE.md`](08_FINITE_HEIGHT_WIDDER_CONE.md).

## 6. The four equivalent constructive gates

The present proof frontier can be stated in four source languages.

### Quasi-free gate

Construct one positive trace-class contraction satisfying `(TQF)`.

### Radial terminal-annulus gate

Prove the source radial current is nonnegative on the remaining interval

\[
 w_H<w<1.
\]

### Fixed-centre heat gate

Prove `(HCM)` directly from the explicit nonoscillatory heat source.

### Theta–Darboux gate

Prove the weighted exterior integrals `(TDA)` are nonnegative for every index
packet, using strict total positivity of the coefficient propagator and
source-specific sign variation of the theta current.

Any complete gate proves the one-scale `PF_infinity` count theorem, the
Stieltjes/Widder inequalities, and RH.  None is discharged here.

## 7. Recommended next proof attack

The most concrete next synthesis is:

1. derive sign-variation bounds for the ordered theta–Darboux determinant;
2. use variation diminution of the strictly TP `b_n` kernel to prove the
   weighted signs `(TDA)` rather than an unnecessarily strong pointwise sign;
3. construct an intertwiner from the theta–Darboux ladder to the fixed-centre
   heat derivatives of `K`;
4. use the reciprocal rectangle identity to complete minors crossing the
   one-sided coefficient boundary;
5. recover one positive contraction from the projectively consistent exterior
   characters.

This is an end-to-end source programme.  It is not a proposal to inspect the
next unproved derivative order.

## 8. Exact status

```text
positive invariant coefficients and count law             PROPOSED EXACT / REVIEW
one-scale PF_infinity / Poisson-binomial criterion          PROPOSED EXACT / REVIEW
theta mixture of quasi-free fibres                          PROPOSED EXACT / REVIEW
radial order product and phase current                      PROPOSED EXACT / REVIEW
off-line matching pole in (1/2,1)                          PROPOSED EXACT / REVIEW
resummed positivity through terminal annulus cutoff         PROPOSED EXACT / REVIEW
fixed-centre zero heat identity                             PROPOSED EXACT / REVIEW
strict TP of invariant Pascal/Bessel kernel                 PROPOSED COMPLETE / REVIEW
theta–Darboux/Andreief minor factorization                  PROPOSED EXACT / REVIEW
quasi-free / radial / heat / theta-Darboux completion       OPEN / RH-EQUIVALENT
all-order E–Widder source inequality                        OPEN / RH-EQUIVALENT
Riemann Hypothesis                                          UNPROVED
```

## 9. Reading order

1. this file;
2. [`09_INVARIANT_ORDER_PRODUCT_AND_COUNT_LAW.md`](09_INVARIANT_ORDER_PRODUCT_AND_COUNT_LAW.md);
3. [`09_INVARIANT_RESOLVENT_AND_HEAT_TRACE.md`](09_INVARIANT_RESOLVENT_AND_HEAT_TRACE.md);
4. [`10_THETA_FOCK_MIXTURE_AND_QUASIFREE_GATE.md`](10_THETA_FOCK_MIXTURE_AND_QUASIFREE_GATE.md);
5. [`13_THETA_DARBOUX_ANDREIEF_GATE.md`](13_THETA_DARBOUX_ANDREIEF_GATE.md);
6. [`11_TOEPLITZ_SECTOR_AND_RECIPROCAL_DUALITY.md`](11_TOEPLITZ_SECTOR_AND_RECIPROCAL_DUALITY.md);
7. [`02_SOURCE_HERMITE_STIELTJES_CLOSURE.md`](02_SOURCE_HERMITE_STIELTJES_CLOSURE.md);
8. [`03_E_WIDDER_SCALAR_ENDPOINT.md`](03_E_WIDDER_SCALAR_ENDPOINT.md);
9. [`08_FINITE_HEIGHT_WIDDER_CONE.md`](08_FINITE_HEIGHT_WIDDER_CONE.md);
10. [`04_FIREWALLS_AND_SCOPE.md`](04_FIREWALLS_AND_SCOPE.md);
11. [`05_IMPORTED_VS_NEW_CLAIM_LEDGER.md`](05_IMPORTED_VS_NEW_CLAIM_LEDGER.md);
12. [`06_NEXT_ATTACK.md`](06_NEXT_ATTACK.md);
13. [`VALIDATION.md`](VALIDATION.md).

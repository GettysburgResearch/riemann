# Four-gate continuation — repaired radial packet, energy angle, and growing exact-radical frame

Agent: `gpt56-pro-12`  
Date: 2026-07-31  
Issue: #162  
PR: #164  
Status: substantial reduction; **RH not proved**

## Executive result

The four requested gates do not survive independent reconstruction as four
separate problems.

1. The raw four-mode profile gate is ill-posed: individual positive prolate
   modes do not satisfy the two source cancellations, and their Poisson tails
   contain non-`L2(d*u)` power terms.
2. The correct profile packet is the two-dimensional exact-radical space inside
   modes `0,4,8,12`.
3. Gates 2 and 4 are consequences of one strict source/background energy angle;
   the original absolute coupling little-o is unnecessary.
4. At generic support, the complete finite Fourier space is the projected exact
   arithmetic-source range. There is no algebraically independent background;
   gate 3 is a quantitative growing source-frame problem.
5. A consecutive-triple exact-radical basis gives an explicit banded right
   inverse with only polynomial cutoff conditioning, assuming uniform adjacent
   defect separation.
6. The exact Xi source needs only `N_lambda=O((log lambda)^2)` Fourier modes in
   the moving Hardy norm, while the radial scale is `R_lambda=2pi lambda^2`.
7. A complete relative scalarization theorem on this growing frame would imply
   the global floor, complete complement gap, and cross stability at once.

The route is now reduced to two nested analytic statements:

```text
A. fixed repaired two-profile radial theorem;
B. polylog-dimensional growing exact-radical frame scalarization theorem.
```

## I. Scope failure in the original gate 1

For an even source and the additive Fourier convention,

```text
E(f)(u)
 =E(Ff)(u^-1)
  +(1/2)[u^-1/2 integral f-u^1/2 f(0)].                  (1)
```

For one positive prolate mode `e_n`,

```text
q_n=e_n(0),
ell_n=integral e_n=chi_n q_n
```

are nonzero. Its lower multiplicative tail therefore contains

```text
(1/2)[u^-1/2 ell_n-u^1/2q_n],                            (2)
```

and the first term is not in `L2(d*u)` at zero.

Thus the individual objects

```text
T_(n,lambda), n=0,4,8,12,
```

cannot satisfy the declared ordinary tail-profile theorem. `R-16202` records
this exact refutation.

The correction is to impose

```text
sum c_nq_n=0,
sum c_nell_n=0.                                          (3)
```

The kernel of these two rows inside four modes is two dimensional. It contains
the repaired target of `T-16201` and one independent repaired complement.
Only these two exact-radical combinations have cancellation-free Poisson tails.

## II. Corrected fixed profile theorem

Let `T_(1,lambda),T_(2,lambda)` be the two repaired omitted tails, with natural
scales

```text
delta_1=Theta(d_4),
delta_2=Theta(d_8).
```

The corrected gate is

```text
widehat(T_j)(s)
 =sqrt(delta_j/R_lambda)
  exp(-isx_lambda)Phi_(j,lambda)(s/R_lambda),
 j=1,2,                                                    (4)
```

with positive profile Gram and fold-admissible regularity budgets.

`L-16210` proves that a uniform pointwise derivative bound is unnecessary. If
`H=Phi^*Phi` has a uniform Gram floor, bounded logarithmic moment, and weighted
matrix variation/horizontal-shift budgets

```text
V_lambda+U_lambda=o(R_lambda),                            (5)
```

then the zero-side matrix satisfies

```text
A_R=(log R)D_R+O(1)+o(log R),                             (6)
```

without RH. Its generalized spectral diameter relative to `D_R` tends to zero.
An Airy fold with variation `O(R^(1/3)polylog R)` is harmless.

## III. Radial geometry now identified

Dunster's fixed-mode radial phase gives, on compact `z>1`,

```text
gamma xi_n(z)
 =gamma sqrt(z^2-1)
  -(2n+1)/2 arccos(1/z)
  +O(gamma^-1).                                          (7)
```

With `z=exp t`, the normalized logarithmic frequency is

```text
omega(z)=z^2/sqrt(z^2-1).                                (8)
```

It has one fold, at

```text
z=sqrt(2), omega=2.                                      (9)
```

The `k`-th arithmetic alias begins at `z=k`, whose threshold is

```text
omega_(k,min)=k^2/sqrt(k^2-1).                           (10)
```

Hence

```text
J subset (2,4/sqrt(3))                                   (11)
```

is a single-stationary-alias window.

The mode-8/mode-4 relative phase is

```text
-4 arccos(1/z)+O(gamma^-1),                              (12)
```

which is nonconstant. Once the exact CCM/Dunster leakage normalization and
uniform error are inserted, stationary phase makes the two local profiles
linearly independent on `J`, giving a strict repaired-profile Gram floor.

A self-audit retained the nonstationary endpoint terms: higher aliases are
`O(gamma^-1)` before endpoint subtraction, not `O(gamma^-M)` wholesale. They are
still smaller than the first-alias stationary contribution `Theta(gamma^-1/2)`
on `J`.

The remaining fixed-profile obligations are now scalar:

```text
- exact finite-Fourier/radial normalization relative to sqrt(d_n);
- summation of every Poisson endpoint term;
- one Airy-fold variation estimate;
- the horizontal-strip derivative budget.
```

The natural scale is

```text
R_lambda=gamma=2pi lambda^2.                             (13)
```

## IV. Gates 2 and 4 collapse to one energy angle

After whitening by the production Gram, write

```text
A-sigma I=[S_0 X; X^* B_0],
S_0,B_0>=0.                                              (14)
```

If

```text
X=S_0^(1/2) C B_0^(1/2),
||C||<=kappa<1,                                          (15)
```

then

```text
A-sigma I>=(1-kappa)(S_0 direct_sum B_0)>=0.             (16)
```

Thus `L=sigma` is a global floor. For a target `p` in the source block,

```text
mu_A-L<=mu_S.                                            (17)
```

If the source and background diagonal gaps are `g_S,g_B`, the complete target
complement has gap

```text
g_full>=min{
 (1-kappa)g_S-kappa mu_S,
 (1-kappa)g_B-mu_S}.                                     (18)
```

Therefore

```text
mu_S=O(ad_4),
g_S,g_B>=cad_8,
kappa<=kappa_0<1                                         (19)
```

imply

```text
mu_A-L=O(ad_4),
g_full>=c_*ad_8.                                         (20)
```

The target/background dual correction also obeys

```text
||B_0^-1/2X^*p||^2<=kappa^2mu_S.                         (21)
```

The absolute condition `eta^2=o(g_Sg_B)` is sufficient but not necessary. The
relative energy angle is the correct Feshbach invariant.

## V. The algebraic background disappears generically

Connes--Consani's zeta-cycle theorem identifies the orthogonal complement of the
arithmetic source range on a circle of length `L` with critical-line zero
frequencies. If

```text
zeta(1/2+i2pi k/L)!=0 for every nonzero integer k,        (22)
```

then the source range is dense. Projecting onto any finite Fourier space gives
exact surjectivity:

```text
P_N Sigma_mu E(S_0^ev)=E_N.                              (23)
```

The exceptional lengths are countable. Even at an exceptional length, finite
surjectivity holds when no obstructing character lies inside the cutoff.

Thus there is no mysterious non-source finite sector at generic support. The
old background is the high part of one complete source frame. The missing gate
is conditioning, not algebraic reachability.

## VI. Constructive consecutive-triple source frame

Let the positive-mode defects and point values be

```text
d_0<...<d_(M+1),
q_0,...,q_(M+1)!=0.                                      (24)
```

In coordinates `x_j=q_jc_j`, radicality is

```text
sum x_j=0,
sum d_jx_j=0.                                           (25)
```

For each consecutive triple define

```text
w_j=(1-r_j)e_j-e_(j+1)+r_je_(j+2),

r_j=(d_(j+1)-d_j)/(d_(j+2)-d_j).                         (26)
```

These vectors satisfy both constraints exactly and form a basis of the entire
codimension-two space.

Let `B_0` be the first-difference frame with columns `e_j-e_(j+1)`. Then

```text
B=B_0+E,
||E||<=2r_*,                                             (27)
```

and

```text
s_min(B)
 >=2sin(pi/[2(M+1)])-2r_*,

s_max(B)<=2+2r_*.                                        (28)
```

If

```text
Mr_*->0                                                  (29)
```

and the point-value ratio is polynomial in `M`, the exact-radical frame has
only polynomial condition number. Its local direction `w_j` has defect energy
`Theta(d_(j+1))` under strong adjacent separation.

This avoids the catastrophic repair coefficient `d_n/d_4` produced by using
modes 0 and 4 to repair every high mode globally.

The finite theorem is exact. The missing prolate input is a uniform adjacent
ratio bound for the growing schedule.

## VII. The cutoff is only quadratic-logarithmic

For the exact global Xi source in logarithmic coordinates,

```text
Fourier(K)=Xi.
```

Gamma-factor decay gives

```text
|Xi(x+iy)|<=C(1+|x|)^Aexp(-pi|x|/4)                     (30)
```

on fixed closed substrips. If `L=log lambda`, the centered Fourier tail satisfies

```text
||(I-P_(L,N))K||_(L,tau)^2
 <=CL^C exp[2tau L-pi^2N/(2L)]+negligible.               (31)
```

Therefore

```text
N_L=ceil(cL^2), c>2/pi^2                                 (32)
```

is sufficient even when `tau->1/2`. In particular `N_L=ceil(L^2)` works.

Hence

```text
m_lambda=O((log lambda)^2),
R_lambda=2pi lambda^2,                                   (33)
```

and every fixed power of the frame dimension is `o(R_lambda)`. This leaves a
large margin for dimension factors in the radial/local-Weyl estimates.

## VIII. One complete-frame theorem implies gates 2--4

Let `D_lambda` be the complete exact-radical omitted-tail Gram and `A_lambda`
its exact zero-side Weil matrix. Suppose

```text
D-mu_DG>=c_Dd_8G on p^perp                               (34)
```

and

```text
||D^-1/2(A-aD)D^-1/2||<=epsilon_lambda a,
epsilon_lambda->0.                                       (35)
```

Then

```text
A>=0,
mu_A=O(ad_4),
g_complete>=c ad_8.                                     (36)
```

For any `D`-invariant low/high split, the energy angle is at most

```text
kappa<=epsilon/(1-epsilon)->0.                           (37)
```

Thus the global floor, complete background gap, and cross stability are all
consequences of one growing-frame scalarization theorem.

The Rayleigh-floor ratio is then

```text
(mu_A-L_A)/g_complete=O(d_4/d_8)=O(lambda^-8).            (38)
```

## IX. Exact remaining theorem

The honest remaining positive-route statement is:

```text
Choose a cofinal generic support schedule and N_lambda=O((log lambda)^2).
Construct the consecutive-triple exact-radical source frame and prove:

A. uniform growing-mode defect separation and point-value control;
B. a uniformly controlled arithmetic-image/tail frame;
C. fold-admissible normalized radial profiles at R_lambda=2pi lambda^2;
D. complete relative zero-side scalarization in the tail metric.
```

Items A--D imply every original gate, but none is silently claimed here.

## X. Exact controls

`X-16202` now contains:

```text
8/8 repaired-packet/energy-angle/scalarization tests;
6/6 consecutive-triple frame tests.
```

The exact local-frame control certifies a frame lower bound `1/100` and positive
defect-energy Gram for a five-defect synthetic ladder. These are finite rational
regressions only.

## Status

No RH proof is claimed. The work has corrected one invalid profile formulation,
proved the block mechanisms behind gates 2 and 4, eliminated an algebraic
background at generic support, supplied a constructive growing radical frame,
and reduced the remaining global problem to a polylog-dimensional normalized
profile/frame theorem.

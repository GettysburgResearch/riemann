# L-91327 — The delayed Cauchy tangent reduces exactly to finite pole jets and logarithmic-phase Toeplitz resolvents

Claim ID: `L-91327`  
Status: **PROVED EXACT FINITE-JET REDUCTION OF EVERY PHYSICAL DELAY PACKET**  
Created: 2026-08-13  
Depends on: `R-91008`, `L-91323`, `L-91326`, the exact model-space tangent identity in `L-91301`  
Sharpens: the structured observability endpoint of `L-91325`  
RH status: **unproved**

## 1. Ordinary Hardy pole jets

Let `H2=H2(C_+)`. For `w in C_+`, use the unnormalized Hardy kernel and its
first confluent jet

\[
 \kappa_w(u)=\frac1{u-\overline w},
 \qquad
 \kappa_w^{[1]}(u)=\frac1{(u-\overline w)^2}
 =\partial_{\overline w}\kappa_w(u).
 \tag{L-91327.1}
\]

For a finite node set `W subset C_+`, put

\[
 \mathcal R_W
 =\operatorname{span}\{
  \kappa_w,\kappa_w^{[1]}:w\in W
 \}.
 \tag{L-91327.2}
\]

Let

\[
 S_\tau^*f=P_+(e^{-i\tau\,\cdot}f),
 \qquad \tau\ge0,
 \tag{L-91327.3}
\]

be the backward upper-Hardy shift of `L-91322`. The reproducing-kernel
eigenvector identity gives

\[
 \boxed{
 S_\tau^*\kappa_w
 =e^{-i\overline w\tau}\kappa_w.
 }
 \tag{L-91327.4}
\]

Differentiating with respect to `bar w` gives

\[
 \boxed{
 S_\tau^*\kappa_w^{[1]}
 =e^{-i\overline w\tau}
  \left(\kappa_w^{[1]}-i\tau\kappa_w\right).
 }
 \tag{L-91327.5}
\]

Thus

\[
 \boxed{S_\tau^*\mathcal R_W\subseteq\mathcal R_W}
 \tag{L-91327.6}
\]

for every delay. In the ordered basis `(kappa_w,kappa_w^[1])`, the coefficient
column transforms by the exact triangular block

\[
 \boxed{
 D_w(\tau)
 =e^{-i\overline w\tau}
  \begin{pmatrix}
   1&-i\tau\\
   0&1
  \end{pmatrix}.
 }
 \tag{L-91327.7}
\]

The arbitrary continuous delay fibre therefore creates no new pole or jet
order.

## 2. Every delayed rational Cauchy input is a six-dimensional jet packet

Fix the safe Cauchy scale `a>1/2` and a carrier `x in R`. Put

\[
 w_{x,r}=x+ira,
 \qquad r\in\{1,2,4\},
 \tag{L-91327.8}
\]

and

\[
 W_{a,x}=\{w_{x,1},w_{x,2},w_{x,4}\}.
\]

The exact partial fraction identity `R-91008.3`, after scale covariance and the
fixed Fourier/Laplace change of convention, says

\[
 \boxed{
 F_{a,x}=\Psi_a(\,\cdot-x)\in\mathcal R_{W_{a,x}}.
 }
 \tag{L-91327.9}
\]

More precisely, only five of the six displayed basis vectors have nonzero
coefficients, but retaining the full first-jet block is invariant under every
delay and is the canonical confluent coordinate space.

Equations (L-91327.4)--(L-91327.7) imply

\[
 \boxed{
 S_\tau^*F_{a,x}\in\mathcal R_{W_{a,x}}
 \qquad(\tau\ge0).
 }
 \tag{L-91327.10}
\]

Hence every finite carrier-delay packet belongs to

\[
 \mathcal R_W,
 \qquad
 W=\bigcup_jW_{a,x_j},
 \qquad
 \dim\mathcal R_W\le6N
 \tag{L-91327.11}
\]

for `N` carriers, before coincidences are removed.

## 3. Model projection preserves the finite confluent coordinate count

Fix the Suzuki inner function `Theta=Theta_a` and write

\[
 k_w^\Theta=P_{K_\Theta}\kappa_w,
 \qquad
 k_w^{\Theta,[1]}=P_{K_\Theta}\kappa_w^{[1]}.
 \tag{L-91327.12}
\]

The explicit formulas already used in `L-91323` are

\[
 k_w^\Theta(u)
 =\frac{1-\overline{\Theta(w)}\Theta(u)}
        {u-\overline w},
 \tag{L-91327.13}
\]

and

\[
 k_w^{\Theta,[1]}(u)
 =\frac{1-\overline{\Theta(w)}\Theta(u)}
        {(u-\overline w)^2}
 -\frac{\overline{\Theta'(w)}\Theta(u)}
        {u-\overline w}.
 \tag{L-91327.14}
\]

Define

\[
 \mathcal K_W^{(1)}
 =P_{K_\Theta}\mathcal R_W
 =\operatorname{span}\{
   k_w^\Theta,k_w^{\Theta,[1]}:w\in W
  \}.
 \tag{L-91327.15}
\]

The forced resident vector of `L-91323` can equivalently be written

\[
 r_{a,x,\tau}
 =P_{K_\Theta}S_\tau^*F_{a,x}.
 \tag{L-91327.16}
\]

Indeed, projecting the raw delay directly or first taking its positive-Hardy
part gives the same model component. Therefore

\[
 \boxed{
 r_{a,x,\tau}\in\mathcal K_{W_{a,x}}^{(1)},
 }
 \tag{L-91327.17}
\]

and every finite resident carrier-delay packet lies in the finite confluent
space `K_W^(1)`. The model/amplitude forcing term of `L-91323` is encoded
exactly in the triangular coefficient transformation (L-91327.7) followed by
`P_(K_Theta)`; it has not been discarded.

## 4. Exact tangent columns on model kernels

Use logarithmic radius and put

\[
 \dot\Theta=a\partial_a\Theta_a,
 \qquad
 \ell=\overline\Theta\,\dot\Theta
      =a\partial_a\log\Theta_a.
 \tag{L-91327.18}
\]

On the physical domain proved in `L-91326`, define the logarithmic-phase
Toeplitz operator

\[
 T_\ell f=P_+(\ell f).
 \tag{L-91327.19}
\]

Since `ell(t)=O(log(2+|t|))`, both `kappa_w` and `kappa_w^[1]` lie in its
maximal boundary domain.

Let

\[
 \mathcal A_\Theta=M_{\dot\Theta}^*P_{K_\Theta},
 \qquad
 \mathcal J_a=\sqrt2\,\mathcal A_\Theta.
 \tag{L-91327.20}
\]

The ordinary kernel eigenvector identity gives

\[
 M_{\dot\Theta}^*\kappa_w
 =\overline{\dot\Theta(w)}\kappa_w.
 \tag{L-91327.21}
\]

Differentiating the isometry identity
`M_Theta^*M_Theta=I` gives

\[
 M_{\dot\Theta}^*M_\Theta
 =-M_\Theta^*M_{\dot\Theta}
 =-T_\ell.
 \tag{L-91327.22}
\]

Substitution into (L-91327.13) yields the exact first tangent column

\[
 \boxed{
 \mathcal A_\Theta k_w^\Theta
 =\overline{\dot\Theta(w)}\kappa_w
  +\overline{\Theta(w)}T_\ell\kappa_w.
 }
 \tag{L-91327.23}
\]

Differentiating in `bar w` yields the confluent tangent column

\[
\boxed{
\begin{aligned}
 \mathcal A_\Theta k_w^{\Theta,[1]}
 ={}&\overline{\dot\Theta'(w)}\kappa_w
 +\overline{\dot\Theta(w)}\kappa_w^{[1]}\\
 &+\overline{\Theta'(w)}T_\ell\kappa_w
 +\overline{\Theta(w)}T_\ell\kappa_w^{[1]}.
\end{aligned}}
 \tag{L-91327.24}
\]

Equations (L-91327.23)--(L-91327.24) are valid on the logarithmic weighted core
of `L-91326`; they do not use the refuted normalized Fisher-Hankel operator of
`L-91316`.

## 5. Every physical tangent Gram is a finite resolvent block

For a finite node set `W`, enumerate the confluent basis

\[
 e_{w,0}=k_w^\Theta,
 \qquad
 e_{w,1}=k_w^{\Theta,[1]}.
 \tag{L-91327.25}
\]

Define the output matrix

\[
 \boxed{
 G_a^{\rm out}(W)_{(w,m),(v,n)}
 =2\left\langle
  \mathcal A_\Theta e_{v,n},
  \mathcal A_\Theta e_{w,m}
 \right\rangle_{H^2}.
 }
 \tag{L-91327.26}
\]

By (L-91327.23)--(L-91327.24), every entry is an explicit inner product among
the finite collection

```text
kappa_w, kappa_w^[1],
T_ell kappa_w, T_ell kappa_w^[1]
        (w in W),
```

with coefficients given by the finite safe-line data

```text
Theta(w), Theta'(w), dotTheta(w), dotTheta'(w).
```

If `c(a,x,tau)` is the coefficient column obtained from the five exact Cauchy
partial-fraction coefficients and the triangular delay blocks (L-91327.7), then

\[
 \boxed{
 \|\mathcal J_ar_{a,x,\tau}\|^2
 =c(a,x,\tau)^*G_a^{\rm out}(W_{a,x})
  c(a,x,\tau).
 }
 \tag{L-91327.27}
\]

The same statement, with the block matrix over the union of nodes, holds for
every polarized multi-carrier, multi-delay packet.

Thus the continuous delay fibre is now finite algebra. What remains infinite
is not delay bookkeeping but the logarithmic-phase Toeplitz resolvent
`T_ell`, equivalently the reciprocal-completed-amplitude leg isolated in
`L-91325`.

## 6. Correct finite-matrix endgame

Let `G_a^src(W)` denote the complete Jordan plus gamma/pole first-chaos source
form evaluated on the same confluent resident basis. For each physical packet,
the desired domination is exactly

\[
 \boxed{
 c^*\left(G_a^{\rm src}(W)-G_a^{\rm out}(W)\right)c\ge0.
 }
 \tag{L-91327.28}
\]

Consequently the same-orientation Cauchy endpoint can be organized as a family
of finite confluent Pick/Loewner-type blocks, one for every finite carrier set,
provided the source entries are retained with their exact gamma/pole
normalization.

This does **not** reduce the theorem to the finite scalar values of `Theta` and
its derivatives. The columns `T_ell kappa_w` and
`T_ell kappa_w^[1]` contain the global boundary logarithmic phase and remain
load bearing. Replacing them by point evaluations would repeat the scalar
Wigner--Smith error of `R-91010`.

The reflected orientation has the conjugate finite-jet description. The mixed
orientation and the canonical bridge require adjoining their exact finite rows
and columns to (L-91327.28).

## 7. Exact boundary

```text
backward delays preserve each simple/double-pole block       EXACT
one Cauchy carrier uses at most six confluent coordinates    EXACT
all finite carrier-delay resident packets are finite jets    EXACT
model-space tangent on each jet                              EXACT
physical tangent Gram as a finite Toeplitz-resolvent block   EXACT
continuous delay bookkeeping                                CLOSED
finite scalar Theta-jet data alone                           INSUFFICIENT FOR THE DISPLAYED FORMULA
global logarithmic-phase Toeplitz columns                    LOAD BEARING
source-minus-output finite block positivity                  OPEN / RH-BEARING
mixed orientation and canonical bridge arithmetic block      OPEN
Riemann Hypothesis                                           UNPROVED
```

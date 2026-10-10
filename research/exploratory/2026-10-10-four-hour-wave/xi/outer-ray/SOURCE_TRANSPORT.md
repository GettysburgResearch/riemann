# Explicit source-error budgets on protected outer regions

Status: proposed analytic consequences of [THEOREM.md](THEOREM.md).
Scope: forward source transport on compact subsets of `Im z<-A`, for each
fixed derivative order and companion parameter. The bounds do not provide
transport into the remaining strip.
Dependencies: all hypotheses and inputs of the outer-strip theorem; elementary
holomorphic integration, complete absolute Fourier-source bounds, and Leibniz's
rule. No numerical theta integral is asserted to have been certified here.

## 1. A compact region and explicit denominator lower bounds

Keep `F`, its complete strip width `A`, and fixed `r,lambda` from the theorem.
Write `E=F^(r)-i lambda F^(r+1)`, `q_E=E'/E`, and `W=iE/E'`.
Choose a closed rectangle

\[
\mathcal D=\{T-iy:|T|\le X,\ Y_-\le y\le Y_+\},
\qquad A<Y_-\le y_0\le Y_+,
\tag{T1}
\]

so that the imaginary-axis anchor `z_0=-iy_0` and every straight segment from
that anchor to a point of `D` lie in `D`. From the complete source define

\[
B_0=A_r(y_0)+\lambda A_{r+1}(y_0)>0,
\qquad
m_0=\frac{A_{r+1}(y_0)+\lambda A_{r+2}(y_0)}{B_0}>0.
\tag{T2}
\]

Choose bounds `rho_*<1` and `L_*` such that

\[
\rho(z)\le\rho_*\quad(z\in\mathcal D),
\qquad |z-z_0|\le L_*\quad(z\in\mathcal D),
\qquad K_*=(1+\rho_*)/(1-\rho_*).
\tag{T3}
\]

For example, valid sharp geometric choices are

\[
\rho_*^2=
\max_{Y\in\{Y_-,Y_+\}}
\frac{X^2+(Y-y_0)^2}{X^2+(Y+y_0-2A)^2},
\qquad
L_*^2=X^2+\max_{Y\in\{Y_-,Y_+\}}(Y-y_0)^2.
\tag{T4}
\]

For (T4), the ratio increases in `T^2`. After putting `t=y-A` and
`t_0=y_0-A`, maximizing it in `t` is minimizing
`t/[X^2+(t+t_0)^2]`; this function has a single interior maximum, so its
minimum on a compact interval is at an endpoint. A rational upper bound on
`rho_*` is also sufficient.

The theorem gives `|q_E|<=m_0 K_*` throughout `D`. Since `E` is nowhere zero
on the simply connected outer half-plane, integrate its logarithmic
derivative along the straight segment:

\[
\left|\log\frac{|E(z)|}{|E(z_0)|}\right|
\le m_0K_*|z-z_0|.
\tag{T5}
\]

With

\[
C_*=B_0e^{-m_0K_*L_*}>0,
\tag{T6}
\]

this supplies explicit complete-source denominator protection,

\[
|E(z)|\ge C_*,\qquad
|E'(z)|\ge\frac{m_0}{K_*}C_*,\qquad
\operatorname{Re}W(z)\ge\frac1{m_0K_*},\qquad
|W(z)|\le\frac{K_*}{m_0}
\quad(z\in\mathcal D).
\tag{T7}
\]

The derivative bound follows from `|q_E|>=Im q_E>=m_0/K_*`. Unlike a local
perturbation lemma that merely assumes protected companion denominators,
(T7) derives them on this region from the complete strip and source moments.
The constants are coarse, but strictly positive and fully specified.

## 2. Full additive source transport at every fixed order

Let `G=F+Delta F` have the same Fourier normalization, with source difference
`nu` a signed measure on `[0,infinity)` and with the absolute exponential
moments required through order `r+2` and in a neighborhood of `D`. Put

\[
D_j=\int_0^\infty u^j
       (e^{Y_+u}+e^{-Y_+u})\,d|\nu|(u),
\quad 0\le j\le r+2.
\tag{T8}
\]

These are **complete** source errors, including both reflected terms and the
entire tail. For every point of `D`,

\[
|(G-F)^{(j)}|\le D_j.
\tag{T9}
\]

The same conclusion applies to complex source errors using total variation.
The sufficient transport result does not require the perturbed source itself
to be positive or its zero strip to be known.

Define

\[
\alpha=\frac{D_r+\lambda D_{r+1}}{C_*},
\qquad
\beta=\frac{K_*(D_{r+1}+\lambda D_{r+2})}{m_0 C_*}.
\tag{T10}
\]

Write the modified companions exactly as
`E[G]=E[F](1+n)` and `E'[G]=E'[F](1+d)`.
Equations (T7)--(T9) give `|n|<=alpha`, `|d|<=beta`. If `beta<1`, then

\[
E'[G]\ne0,\qquad
\left|\frac{W[G]}{W[F]}-1\right|
\le\frac{\alpha+\beta}{1-\beta}.
\tag{T11}
\]

In particular the explicit sufficient condition

\[
K_*^2\alpha+(K_*^2+1)\beta<1
\tag{T12}
\]

implies `alpha<1`, `beta<1`, and
`(alpha+beta)/(1-beta)<1/K_*^2`. Consequently both modified companions are
nonzero and

\[
\operatorname{Re}W[G]
\ge \frac1{m_0K_*}
     -\frac{K_*}{m_0}\frac{\alpha+\beta}{1-\beta}>0
\quad\text{throughout }\mathcal D.
\tag{T13}
\]

Proof of the relative estimate is the exact identity
`W[G]/W[F]=(1+n)/(1+d)`. No pole, reflected source term or endpoint is
dropped. A practical implementation of (T12) needs rigorous enclosures of
the actual moments in (T2) and complete errors in (T8); ordinary high
precision or finite source sampling does not provide them.

## 3. A cheaper multiplier budget for a single companion base

Let `H=F^(r)` and let `p` be holomorphic and nowhere zero near `D`. Define
the perturbed base to be `pH`. This is a source modification of `F` itself
when `r=0`. When `r>0`, this section concerns the base `pF^(r)`, which is
generally different from `(pF)^(r)`. The latter is treated in section 4.

Exact differentiation gives

\[
E[pH]=pE-i\lambda p'H,
\qquad
E'[pH]=pE'+p'(H-2i\lambda H')-i\lambda p''H.
\tag{T14}
\]

There is useful extra protection here. By the theorem,
`Im(H'/H)>0`, so with `w=H/E`,

\[
\operatorname{Re}(1/w)
 =1+\lambda\operatorname{Im}(H'/H)>1.
\tag{T15}
\]

Equivalently `|w-1/2|<1/2`; hence `|w|<1` and `|2-w|<2`. Since
`H-2i lambda H'=2E-H`, it follows that

\[
|H/E|<1,\qquad
|H/E'|\le |W|,\qquad
|(H-2i\lambda H')/E'|\le2|W|.
\tag{T16}
\]

If `|p'/p|<=L_1`, `|p''/p|<=L_2` throughout `D`, (T14)--(T16) yield

\[
\alpha_p=\lambda L_1,
\qquad
\beta_p=\frac{K_*}{m_0}(2L_1+\lambda L_2).
\tag{T17}
\]

Condition (T12) with these constants therefore guarantees the complete
modified sector on `D`. No smallness of `p-1` itself is required, beyond
nonvanishing of `p`; it is the logarithmic derivatives that enter the ratio.

## 4. Multiplying the original source, with every Leibniz term retained

For the actual modification `G=pF` and fixed derivative order `r`, let

\[
U_j=\int_0^\infty u^j
        (e^{Y_+u}+e^{-Y_+u})\,d\mu(u),
\qquad
L_k\ge\sup_{z\in\mathcal D}|p^{(k)}(z)/p(z)|
\quad(1\le k\le r+2).
\tag{T18}
\]

Then `|F^(j)|<=U_j`. Define `S_0=0` and

\[
S_j=\sum_{k=1}^j\binom jk L_kU_{j-k}
\quad(1\le j\le r+2).
\tag{T19}
\]

Leibniz's rule is the exact identity

\[
G^{(j)}=pF^{(j)}+R_j,
\qquad
R_j=\sum_{k=1}^j\binom jk p^{(k)}F^{(j-k)},
\qquad |R_j/p|\le S_j.
\tag{T20}
\]

Therefore

\[
E_r[G]=pE_r[F]+R_r-i\lambda R_{r+1},
\quad
E_r'[G]=pE_r'[F]+R_{r+1}-i\lambda R_{r+2}.
\tag{T21}
\]

The same argument proves a sufficient budget (T12), now with

\[
\alpha_r=\frac{S_r+\lambda S_{r+1}}{C_*},
\qquad
\beta_r=\frac{K_*(S_{r+1}+\lambda S_{r+2})}{m_0C_*}.
\tag{T22}
\]

This supplies a genuine all-fixed-order forward multiplier estimate. Using
only the single-base formula (T14) for derivatives of `pF` would miss the
Leibniz terms and is not authorized by this theorem.

For example, for the quartet multiplier from
[MODULAR_BINDING_AND_TRANSPORT.md](../MODULAR_BINDING_AND_TRANSPORT.md),
`p=Q_(R,d)/Q_(R,d)(i/2)`, on `|z|<=B` with `R>=10`, `0<d<1/2`, put

\[
\varepsilon_B=
\frac{(B^2+1/4)(B^2+1/4+2R^2)}{R^4}<1.
\tag{T23}
\]

The complete multiplier bound gives `|p|>=1-epsilon_B`. Literal polynomial
differentiation then gives valid choices

\[
L_1=\frac{4B(B^2+R^2)}{R^4(1-\varepsilon_B)},\quad
L_2=\frac{12B^2+4R^2}{R^4(1-\varepsilon_B)},\quad
L_3=\frac{24B}{R^4(1-\varepsilon_B)},\quad
L_4=\frac{24}{R^4(1-\varepsilon_B)},\quad
L_k=0\ (k>4).
\tag{T24}
\]

For each **fixed** `D,r,lambda`, these constants tend to zero as `R` tends
to infinity. Thus (T12) eventually certifies the modified sector on that
entire protected outer compact region. Yet the modified source retains its
added off-real quartet inside the classical actual-xi strip `|Im z|<1/2`.
Preservation of a chosen narrower imported strip additionally requires
`d<A`; compact transport itself does not require that preservation. This
confirms the exact
scope: successful compact outer transport is compatible with the slab
obstruction and does not extract the native arithmetic member from its
source class.

## 5. The continuation attempt stops at a specified estimate

Sections 1--4 remove an unspecified denominator premise outside the complete
strip. They do not remove that premise inside the strip. As a protected
rectangle approaches `y=A`, `rho_*` can approach one and (T6), (T10), and
(T12) become weak. Widening the rectangle without bound in the real coordinate
has the same effect. No uniform nonzero error allowance on either limit is
proved here.

To continue toward `0<y<=A`, one needs new actual-source information: a
protected companion denominator and a signed sector margin there, or a
complete signed residue/winding transport law that permits and prices their
failures. The generic positive-source counterexample gives companion zeros
arbitrarily close to `y=A` from below for small `lambda`. The theta-derived
quartet also preserves the bare Jacobi reflection and xi endpoint values;
those identities alone cannot supply the missing continuation estimate.

The actual constant-coefficient lattice Gaussian source or its exact
Mellin--Euler binding remains a possible distinguishing input. No estimate
from that binding controlling the complete low-order companion denominator
or signed ledger is established by this packet.

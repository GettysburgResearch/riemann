# T-21903 — Canonical Xi shift-quotient Pick criterion

Claim ID: `T-21903`  
Title: Pick positivity of the canonical Mellin–gamma shift quotient, equivalently one-separated Laguerre–Pólya geometry of its interpolant, implies the Riemann Hypothesis  
Status: **PROPOSED EXACT CONDITIONAL THEOREM PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-07  
Dependencies: `L-21910`; Konstantopoulos–Patie–Sarkar Theorem 23; the standard Pick/complete-Bernstein characterization  
Scope: full deduction to RH from one explicit upper-half-plane positivity theorem

## 1. Canonical objects

Let `C_Xi` be the entire function of `L-21910` and put

\[
 \phi_\Xi(z)=\frac{C_\Xi(z-1)}{C_\Xi(z)},
 \qquad
 \Psi_\Xi(u)=u\phi_\Xi(u).
 \tag{T-21903.1}
\]

The exact coefficient identity already proved there is

\[
 \boxed{\mathcal J_{\Psi_\Xi}(t)=\Xi(t).}
 \tag{T-21903.2}
\]

## 2. Pick-shift hypothesis

Assume the following explicit statement.

> **PX.** The meromorphic function `phi_Xi` has no cancellation between a zero
> of `C_Xi(z)` and a zero of `C_Xi(z-1)`, is nonnegative on `(0,infinity)`, and
> maps the upper half-plane holomorphically into its closure:
> \[
>  \operatorname{Im}\phi_\Xi(z)\ge0
>  \qquad(\operatorname{Im}z>0).
>  \tag{T-21903.3}
> \]

Equivalently, every finite Pick matrix

\[
 \boxed{
 \left[
 \frac{
  \phi_\Xi(z_j)-\overline{\phi_\Xi(z_k)}
 }{z_j-\overline{z_k}}
 \right]_{j,k=1}^m
 \succeq0}
 \tag{T-21903.4}
\]

for points `z_1,...,z_m` in the upper half-plane.

The noncancellation clause may be replaced by the stronger zero-geometric
condition in Section 5.

## 3. Bernstein and one-separation consequences

A Pick function which is nonnegative on the positive half-line and has all its
singularities on the negative real axis is a complete Bernstein function. In
particular,

\[
 \phi_\Xi\in\mathds B
 \quad\text{and is a Bernstein Pick function.}
 \tag{T-21903.5}
\]

Because `phi_Xi` is meromorphic, its real zeros and poles are simple and
interlace. Let `rho_k` be a pole. By (T-21903.1) and noncancellation,

\[
 C_\Xi(\rho_k)=0
 \quad\Longrightarrow\quad
 z_k:=\rho_k+1
 \text{ is a zero of }\phi_\Xi.
 \tag{T-21903.6}
\]

Conversely every zero of `phi_Xi` arises by shifting a zero of `C_Xi` one unit
to the right. Order the negative zeros and poles from right to left. The Pick
interlacing gives

\[
 z_k>\rho_k>z_{k+1}.
 \tag{T-21903.7}
\]

Together with `rho_k=z_k-1`, this is exactly

\[
 \boxed{
 \rho_k=z_k-1>z_{k+1}.}
 \tag{T-21903.8}
\]

Thus `phi_Xi` has the one-separation property and

\[
 \boxed{\phi_\Xi\in\mathds B_{P_1}.}
 \tag{T-21903.9}
\]

## 4. Completion through the van Dantzig theorem

Theorem 23 of Konstantopoulos–Patie–Sarkar states that

\[
 \phi\in\mathds B_{P_1}
 \quad\Longrightarrow\quad
 \Psi(u)=u\phi(u)\in\mathds N_{\mathds D}
 \quad\text{and}\quad
 \mathcal J_\Psi\in\mathds D_L\cap\mathds D_P.
 \tag{T-21903.10}
\]

Apply it to `phi_Xi`. Equations (T-21903.2), (T-21903.9), and
(T-21903.10) give

\[
 \boxed{\Xi\in\mathds D_L.}
 \tag{T-21903.11}
\]

The class `D_L` consists of even characteristic functions in the
Laguerre–Pólya class. Hence every zero of `Xi` is real. In the centered variable
this is precisely the assertion that every nontrivial zeta zero has real part
`1/2`. Therefore

\[
 \boxed{\mathrm{RH}.}
 \tag{T-21903.12}
\]

## 5. Equivalent sufficient zero geometry

A standard meromorphic Pick interlacing criterion gives a second, entirely
real-entire interface.

Assume:

1. `C_Xi` belongs to the Laguerre–Pólya type-I class;
2. every zero `lambda_k` of `C_Xi` is simple and satisfies
   \[
    \lambda_1<-1,
    \qquad
    \lambda_{k+1}<\lambda_k-1;
    \tag{T-21903.13}
   \]
3. `C_Xi(x)>0` for `x>=0`, with the natural positive normalization at infinity.

Then the zeros of the quotient are `lambda_k+1`, its poles are `lambda_k`, and
(T-21903.13) gives the alternating order

\[
 \lambda_k+1>\lambda_k>\lambda_{k+1}+1.
 \tag{T-21903.14}
\]

The corresponding canonical-product quotient is a nonnegative meromorphic Pick
function. Hence `PX` holds and RH follows.

Accordingly, either boxed statement is a sufficient final theorem:

\[
 \boxed{
 \phi_\Xi(z)=C_\Xi(z-1)/C_\Xi(z)
 \text{ is nonnegative Pick}}
 \tag{T-21903.15}
\]

or

\[
 \boxed{
 C_\Xi\text{ is Laguerre–Pólya type I with simple negative zeros
 separated by more than one}.}
 \tag{T-21903.16}
\]

## 6. Why ordinary Bernstein interpolation is insufficient

The cited paper proves that its larger class `D_P` is not contained in `D_L`:
some Bernstein-generated functions have nonreal zeros. Therefore the following
weaker statements do not close RH:

- monotonicity or concavity of the integer sequence `phi_Xi(n)`;
- complete alternation only on the integers;
- existence of some Bernstein interpolation;
- membership of `Xi` in `D_P` without the Pick one-separation property.

The upper-half-plane condition and the shift interlacing are load bearing.

## 7. Exact remaining obstruction

The proof is complete after `PX`. The smallest analytic target is the Loewner
kernel positivity

\[
 \boxed{
 \frac{
  C_\Xi(z-1)\overline{C_\Xi(w)}
  -C_\Xi(z)\overline{C_\Xi(w-1)}
 }{
  (z-\overline w)C_\Xi(z)\overline{C_\Xi(w)}
 }
 \succeq0
 \quad(z,w\in\mathbb H).}
 \tag{T-21903.17}
\]

No proof of (T-21903.17), (T-21903.15), or (T-21903.16) is supplied here.
They are one explicit final component, not a family of unspecified convergence
claims.

## 8. Status boundary

Closed:

- exact construction of `C_Xi`;
- exact moment interpolation;
- exact identity `J_(u phi_Xi)=Xi`;
- Pick plus shift implies one-separation;
- Theorem-23 deduction to the Laguerre–Pólya class and RH.

Open:

- the Pick kernel (T-21903.17), equivalently the stated separated
  Laguerre–Pólya geometry;
- RH.

This file is a complete conditional theorem, not an unconditional proof.
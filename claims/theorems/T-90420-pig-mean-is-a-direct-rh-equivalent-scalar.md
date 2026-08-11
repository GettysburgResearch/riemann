# T-90420 — The sole PIG mean mode is directly equivalent to RH

Claim ID: `T-90420`  
Title: The compact-Q4 mean carry coordinate has critical growth if and only if the Riemann Hypothesis holds; this direct Mellin/Landau consumer bypasses the disputed global PIG-to-pole assembly  
Status: **PROPOSED COMPLETE RH-EQUIVALENT CRITERION — INDEPENDENT REVIEW REQUIRED; RH UNPROVED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Dependencies: `L-90413`, `L-90419`; classical von Koch consequence of RH; elementary Mellin continuation and the zeta functional equation  
Scope: the scalar mean mode; no unconditional critical-growth proof

## 1. Definition

Retain the compact-Q4 prefix coefficient

\[
 c_\circ(m)
 =\Lambda(m)
 -4\mathbf1_{4\mid m}\Lambda(m/4)
 +3(\log4)\sum_{r\ge1}\mathbf1_{m=4^r}.
\tag{T-90420.1}
\]

Define

\[
 \boxed{
 M_\circ(X)
 =\sum_{m\le X}c_\circ(m)
  \left(\frac{2m}{X}-1\right),
 \qquad X\ge1.
 }
\tag{T-90420.2}
\]

This is exactly the zeroth Fourier coefficient and Haar scaling coefficient of the compact innovation carry field.

## 2. Mellin transform

`L-90413` proves, initially in the half-plane of absolute convergence,

\[
 \boxed{
 \begin{aligned}
 \int_1^\infty M_\circ(X)X^{-z-1}dX
 ={}&\frac{z-1}{z(z+1)}
 \Bigg[
 (1-4^{1-z})
 \left(-\frac{\zeta'}{\zeta}(z)\right)\\
 &\qquad\qquad
 +3(\log4)\frac{4^{-z}}{1-4^{-z}}
 \Bigg].
 \end{aligned}
 }
\tag{T-90420.3}
\]

At every nontrivial zeta zero `rho` with

\[
 0<\Re\rho<1,
\]

the elementary factors satisfy

\[
 \rho\ne0,-1,1,
 \qquad
 1-4^{1-\rho}\ne0,
 \qquad
 1-4^{-\rho}\ne0.
\tag{T-90420.4}
\]

Indeed equality in either exponential factor would force the wrong real part. The four-adic term is holomorphic at `rho`. Therefore every open-strip zero survives as a pole of the right side, with its full multiplicity.

## 3. RH implies the critical bound

Assume RH. The classical von Koch estimate gives

\[
 \psi(x)-x
 \ll\sqrt x\log^2(2x).
\tag{T-90420.5}
\]

Write

\[
 H(X)=\sum_{m\le X}\Lambda(m)
       \left(\frac{2m}{X}-1\right).
\]

Partial summation, or direct insertion of `psi(x)=x+E(x)`, gives

\[
 H(X)\ll\sqrt X\log^2(2X).
\tag{T-90420.6}
\]

Equation (T-90420.1) gives

\[
 M_\circ(X)=H(X)-4H(X/4)+O(\log^2(2X)),
\tag{T-90420.7}
\]

where the last term is the explicit four-adic atom. Hence

\[
 \boxed{
 \mathrm{RH}
 \Longrightarrow
 M_\circ(X)
 \ll\sqrt X\log^2(2X).
 }
\tag{T-90420.8}

## 4. Critical growth excludes every right-half zero

Assume that for every `epsilon>0`,

\[
 \boxed{
 M_\circ(X)=O_\epsilon(X^{1/2+\epsilon}).
 }
\tag{T-90420.9}

Then the Mellin integral in (T-90420.3) converges locally uniformly and defines a holomorphic function in

\[
 \Re z>\frac12.
\]

If `zeta(rho)=0` for one `rho` in that half-plane, (T-90420.3)--(T-90420.4) force a pole there, contradiction. Therefore

\[
 \zeta(s)\ne0
 \qquad(\Re s>1/2).
\]

The functional equation and symmetry of nontrivial zeros give

\[
 \boxed{\mathrm{RH}.}
\tag{T-90420.10}
\]

Thus

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 M_\circ(X)=O_\epsilon(X^{1/2+\epsilon})
 \text{ for every }\epsilon>0.
 }
\tag{T-90420.11}

The stronger logarithmic form in (T-90420.8) is also equivalent.

## 5. Relation to endpoint PIG

`L-90419` proves unconditionally

\[
 \frac1N\int_0^1|Q_{c_\circ,N}(\theta)|^2d\theta
 =\frac{|M_\circ(N)|^2}{N}
 +O(\log^4(2N)).
\tag{T-90420.12}

Therefore endpoint deterministic PIG is equivalent to the single scalar criterion (T-90420.9), modulo an already-closed unconditional error.

This equivalence is **independent** of PR #357's disputed complete block recurrence and PR #371's unresolved global adapter. The mean scalar has its own direct Mellin consumer.

## 6. Equivalent arithmetic coordinates

By `L-90418`, the same scalar is

\[
 M_\circ(N)
 =\frac{N+1}{N}
   \sum_{d\le N}i_\circ(d)\beta_{N,d}
 +\frac1N C_\circ(N).
\tag{T-90420.13}

Thus (T-90420.11) is also a critical-growth theorem for one inclusive uniform-Pascal current row. On the top annulus its source kernel is the linear ramp `2d/N-1`.

## 7. Proof boundary

Closed, subject to independent review:

1. exact mean scalar and Mellin transform;
2. open-strip zero safety;
3. `RH => sqrt(X) log^2 X` mean bound;
4. critical mean growth `=> RH`;
5. direct equivalence of endpoint PIG and the mean criterion after `L-90419`;
6. independence from the unresolved global QIDR adapter.

Open:

1. an unconditional proof of the mean bound;
2. RH.

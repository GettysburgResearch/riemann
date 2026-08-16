# L-91881 — Bulk Hall incidences and anchored Target-Lorenz leaves form the live arithmetic coupling

Claim ID: `L-91881`  
Status: **PROPOSED COMPLETE ARITHMETIC INCIDENCE THEOREM ON FROZEN AVLT INPUTS — REVIEW REQUIRED**  
Created: 2026-08-16  
Depends on: `L-91761`, `L-92920`, `L-91860`, PR #508 `L-93783--L-93784`  
RH status: **unproved**

## 1. Bulk rank-one Hall incidences

Fix a bulk point `(n,u)` and put `s=n+u`, `x=X/s`. For active colours define

\[
a_k=\ell_x(k),
\qquad
P_+=\sum_{\mu(e)=1}a_e,
\qquad
P_-=\sum_{\mu(o)=-1}a_o.
\]

On `1<x<67`, the frozen directed theorem gives `L(x)=P_+-P_->0`.
Define

\[
\boxed{
 d\Pi_B(s,o,e)
 =\frac2s\frac{a_oa_e}{P_+}\,du
}
\tag{L-91881.1}
\]

and

\[
\boxed{
 dR_B(s,e)
 =\frac2s a_e\frac{P_+-P_-}{P_+}\,du.
}
\tag{L-91881.2}
\]

Their exact incidence marginals are

\[
(\Pi_B)_-=\Sigma_{X,B}^-,
\qquad
(\Pi_B)_+ + R_B=\Sigma_{X,B}^+.
\tag{L-91881.3}
\]

Every colour multiplies the same packet `p_s`. Hence every bulk edge cancels
exactly in target, declared score, literal score, every component row, ordinary
`q`, ordinary `4q`, detail formed afterward, and every additive boundary
coordinate. The sole physical bulk output is the positive residual

\[
\boxed{
 d\Gamma_B^0(s,e,dt)
=dR_B(s,e)\,P_s(dt),
}
\tag{L-91881.4}
\]

where `P_s` is the direct endpoint-state placement of `p_s`.

No causal operator is applied to `p_s`; `R-91880` makes that type error
fail-closed.

## 2. Anchored stopped-leaf incidences

Apply the paired stopping line to each anchored native occurrence. Let
`omega` be a terminal path label and `a_X(omega)` its exact coefficient from
`L-91880.4`. At the leaf let `E_omega` and `O_omega` be the even and odd finite-Q
source packets, retaining their actual parity orientation.

PR #508 supplies one leftmost Target-Lorenz coefficient vector

\[
0\le u_{\omega,e}\le1,
\qquad
\sum_eu_{\omega,e}T_{\omega,e}=T(O_\omega),
\tag{L-91881.5}
\]

and proves, in the complete directed AVLT,

\[
S(U_\omega)\le S(O_\omega),
\qquad
B_\omega:=R(U_\omega)-R(O_\omega)\ge0
\tag{L-91881.6}
\]

in every component row. The same `u_(omega,e)` is used in target, score and
all rows.

To expose both marginals, define the explicit target-incidence coupling

\[
\boxed{
\Pi_\omega(o,e)
=\frac{T_{\omega,o}\,u_{\omega,e}T_{\omega,e}}
       {T(O_\omega)}
}
\tag{L-91881.7}
\]

when `T(O_omega)>0`; the zero-demand case is empty. Then

\[
(\Pi_\omega)_-=O_\omega,
\qquad
(\Pi_\omega)_+=U_\omega.
\tag{L-91881.8}
\]

Put

\[
\nu_\omega=E_\omega-U_\omega\ge0,
\qquad
\sigma_\omega=S(O_\omega)-S(U_\omega)\ge0.
\tag{L-91881.9}
\]

The exact typed leaf identity is

\[
\boxed{
\begin{aligned}
T(\nu_\omega)&=T(E_\omega)-T(O_\omega),\\
S(\nu_\omega)&=S(E_\omega)-S(O_\omega)+\sigma_\omega,\\
R(\nu_\omega)+B_\omega&=R(E_\omega)-R(O_\omega).
\end{aligned}}
\tag{L-91881.10}
\]

The row bonus `B_omega` is current-only, has one leaf owner and zero source
target. It is never sent through a rough split or to a child.

## 3. Avoiding the PR #503 counterexample

At `(p,y,s,j)=(67,15,1005,14)` the Volterra infinitesimal difference is
negative by `R-91880.1`. The coupling never constructs it.

The anchored leaf uses complete finite-Q packets. The replay proves

\[
Q_{1005}(14)-67^{-1/2}Q_{15}(14)>1,
\tag{L-91881.11}
\]

and reconstructs the actual Target-Lorenz leaf at `(p,y)=(67,15)`:

```text
cutoff even divisor: 133;
cutoff fraction:      0.1561057606...;
score surplus:        >2.88;
row-14 bonus:         >0.13;
minimum diagnostic row bonus over 2..66: >0.0095.
```

Only the first two inequalities and the row-14 moat are promoted by the
lightweight directed witness; the complete all-row statement remains the
frozen directed theorem of PR #508.

## 4. Exact owner and coefficient signature

For every anchored output define the signature

\[
\kappa(\omega,e)
=\tau_K a_X(\omega)\times
\begin{cases}
1-u_{\omega,e},&\text{residual source},\\
1,&\text{leaf row bonus owner}.
\end{cases}
\tag{L-91881.12}
\]

with the bonus itself carrying its edge coefficients (L-91881.7). The same
path coefficient `a_X(omega)`, the same Lorenz vector `u`, and the same physical
placement occur in target, declared score, every component row, ordinary `q`,
ordinary `4q`, and every additive boundary coordinate. The score surplus is
recorded explicitly rather than forcing false exact equality.

## 5. The live pre-quantization coupling

Let `T_X^anc` be the disjoint finite target containing every placed `nu_omega`
and `B_omega`, and let `T_X^bulk` be the tagged complete-cell endpoint target.
The positive pre-quantization coupling is

\[
\boxed{
\Gamma_X^0
=\Gamma_A^0\oplus\Gamma_B^0
}
\tag{L-91881.13}
\]

with

\[
\Gamma_A^0
=\sum_\omega a_X(\omega)
 \left[
  \sum_e(1-u_{\omega,e})E_{\omega,e}^{\rm phys}
  +B_\omega^{\rm phys}
 \right].
\tag{L-91881.14}
\]

Equations (L-91881.3), (L-91881.8), and the stopping-line path partition prove
that every finite or Volterra native occurrence is counted exactly once in its
appropriate incidence marginal. Every rough monomial has one first owner.
Every child coefficient occurs once in `a_X(omega)` and is not re-applied by
placement or quantization.

```text
bulk negative incidence                   exhausted exactly
bulk positive incidence                   edge plus residual exactly
anchored odd incidence                    exhausted exactly
anchored even incidence                   selected plus residual exactly
least rough owner                         unique
Volterra infinitesimal causal split       absent
finite-Q Target-Lorenz leaf               explicit
```

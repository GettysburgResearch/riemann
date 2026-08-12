# R-91403 — Stepwise SHARP-preserving two-state completions do not preserve the multiprime SHARP cascade

Claim ID: `R-91403`  
Status: **EXACT TWO-FACTOR REFUTATION**  
Created: 2026-08-12  
Refutes: the statement that `w_Psi N_p=w_Psi M_p` survives arbitrary products in PR #399 `L-91325.13`  
RH status: **unproved**

## 1. One-factor matrices

For `r=p^(-1/2)`, the exact rough Euler action is

\[
 M_r=(1-r)
 \begin{pmatrix}
  1+2r&-2r\\
  r&1-r
 \end{pmatrix},
\]

while the positive two-state completion is

\[
 N_r=(1-r)
 \begin{pmatrix}
  1+2r&0\\
  r&1-2r
 \end{pmatrix}.
\]

Let

\[
 w_\Psi=(1,2).
\]

Then, exactly,

\[
 w_\Psi N_r=w_\Psi M_r.
\tag{R-91403.1}
\]

Thus one isolated factor preserves the observed SHARP scalar.

## 2. Two factors

Take distinct parameters `r,s in (0,1/2)`. Since

\[
 N_r-M_r
 =r(1-r)
 \begin{pmatrix}
 0&2\\0&-1
 \end{pmatrix},
\]

and `w_Psi N_s=w_Psi M_s`,

\[
\begin{aligned}
 w_\Psi N_sN_r-w_\Psi M_sM_r
 &=w_\Psi M_s(N_r-M_r)\\
 &=\bigl(0,12rs(1-r)(1-s)\bigr).
\end{aligned}
\tag{R-91403.2}
\]

Therefore, on every input state `(L,R)` with `R>0`,

\[
 \boxed{
 w_\Psi N_sN_r\binom LR
 -w_\Psi M_sM_r\binom LR
 =12rs(1-r)(1-s)R>0.
 }
\tag{R-91403.3}
\]

The completed two-state cascade does not reproduce the arithmetic cascade.

## 3. Structural reason

The correction `Delta_r=N_r-M_r` lies in `ker w_Psi`, but this kernel is not invariant under the next exact Euler factor:

\[
 w_\Psi M_s\Delta_r\ne0.
\]

A one-step output-preserving completion composes only when the correction space is invariant under every subsequent factor, equivalently when the observation is a common left eigenvector. Here

\[
 w_\Psi M_s=(1-s)(1+4s,2-4s)
\]

is not proportional to `w_Psi`.

## 4. Correct repair

The fixed positive three-state and four-state dilations of PR #399 `L-91323/L-91327` do compose because they satisfy an exact intertwining identity

\[
 J\widetilde M_r=M_rJ.
\]

However the physical SHARP output then contains the auxiliary port, for example

\[
 \Psi=u+2v-4z
\]

in the three-state realization. That port must be retained and paid at the reset boundary. It cannot be erased after every prime by replacing `M_p` with `N_p`.

Consequently a source partition based on repeated two-state completions is not an exact proof of the multiprime reset. The correct factor-54 certificate must use the composable dilation and include its auxiliary port in the signed-detail/capacity ledger.

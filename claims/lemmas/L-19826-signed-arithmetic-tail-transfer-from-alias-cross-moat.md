# L-19826 — A collective alias cross moat transfers the signed `d_4,d_6` hierarchy

Claim ID: `L-19826`  
Status: **PROVED OPERATOR TRANSFER THEOREM; PSWF CROSS-MOAT INPUT SUPPLIED SEPARATELY BY L-19827**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-07  
Dependencies: exact first-alias normalization; pure signed hierarchy `L-19823/L-19824`  
Scope: the signed arithmetic-tail hierarchy requested in the review

## 1. Purpose

The complete arithmetic tail is not the first prolate leakage alone. Write it as

\[
 T_R=F_R+H_R,
 \tag{L-19826.1}
\]

where `F_R` is the exact normalized first Poisson alias and `H_R` is the sum of
all remaining aliases and endpoint channels.

The positive matrix `H_R^*H_R` need not be small. The only lower-bound danger is
the first-versus-rest cross operator

\[
 F_R^*H_R+H_R^*F_R.
\]

This lemma proves that a relative cross moat and a sufficiently mild upper
alias budget transfer the pure signed prolate scales

```text
target scale              d_4,
complete next scale       d_6
```

to the actual arithmetic omitted-tail Gram.

## 2. Abstract setup

Let `S_R` be the complete finite two-constraint signed prolate source space,
equipped with a positive metric `G_R`. Let

\[
 \Delta_R\succeq0
\]

be the exact diagonal positive-ray prolate leakage form compressed to `S_R`.
The first alias satisfies the exact identity

\[
 \boxed{F_R^*F_R=\Delta_R.}
 \tag{L-19826.2}
\]

The complete arithmetic omitted-tail Gram is

\[
 \begin{aligned}
 D_R
 &=T_R^*T_R\\
 &=\Delta_R+C_R+P_R,
 \end{aligned}
 \tag{L-19826.3}
\]

where

\[
 C_R=F_R^*H_R+H_R^*F_R,
 \qquad
 P_R=H_R^*H_R\succeq0.
 \tag{L-19826.4}
\]

All adjoints are taken in the physical tail Hilbert space and pulled back to the
same source coordinates.

## 3. Hypotheses

Assume the collective cross operator obeys

\[
 \boxed{
 \left\|
 \langle C_Rx,x\rangle
 \right|
 \le\varepsilon_R\langle\Delta_Rx,x\rangle
 \quad\hbox{for every }x\in S_R,}
 \tag{L-19826.5}
\]

with

\[
 \varepsilon_R\longrightarrow0.
 \tag{L-19826.6}
\]

Equivalently, on the support of `Delta_R`,

\[
 \|\Delta_R^{-1/2}C_R\Delta_R^{-1/2}\|\le\varepsilon_R.
 \tag{L-19826.7}
\]

Assume also an upper alias budget

\[
 \boxed{
 P_R\preceq B_R\Delta_R}
 \tag{L-19826.8}
\]

for some `B_R>=0`. A uniform or polylogarithmic `B_R` is more than sufficient;
the exact condition needed below is

\[
 B_R{d_4(R)\over d_6(R)}\longrightarrow0.
 \tag{L-19826.9}
\]

Finally, assume the pure signed hierarchy has an `G_R`-normalized target `p_R`
with

\[
 \mu_\Delta(R)
 :=\langle\Delta_Rp_R,p_R\rangle
 \le C_4d_4(R),
 \tag{L-19826.10}
\]

and, for every `x perpendicular_(G_R) p_R`,

\[
 \boxed{
 \langle\Delta_Rx,x\rangle
 -\mu_\Delta(R)\langle G_Rx,x\rangle
 \ge c_6d_6(R)\langle G_Rx,x\rangle.}
 \tag{L-19826.11}
\]

`L-19823/L-19824` supply (L-19826.10)--(L-19826.11) in the pure prolate model.

## 4. Complete lower and upper Loewner bounds

Since `P_R>=0`, equations (L-19826.3)--(L-19826.7) give

\[
 \boxed{
 D_R\succeq(1-\varepsilon_R)\Delta_R.}
 \tag{L-19826.12}
\]

Likewise, (L-19826.8) gives

\[
 \boxed{
 D_R\preceq(1+\varepsilon_R+B_R)\Delta_R.}
 \tag{L-19826.13}
\]

The lower bound uses no smallness of the higher-alias self-Gram. Its positivity
is retained rather than discarded.

## 5. Arithmetic target scale

Put

\[
 \mu_D(R)=\langle D_Rp_R,p_R\rangle.
\]

Equations (L-19826.10) and (L-19826.13) give

\[
 \boxed{
 \mu_D(R)
 \le(1+\varepsilon_R+B_R)C_4d_4(R).}
 \tag{L-19826.14}
\]

Thus the arithmetic target remains at scale `d_4` whenever

\[
 B_Rd_4(R)=o(d_6(R)),
\]

and in particular for every polylogarithmic `B_R`.

## 6. Complete arithmetic complement gap

Let `x perpendicular_(G_R) p_R`. From (L-19826.11)--(L-19826.12),

\[
\begin{aligned}
 \langle D_Rx,x\rangle
 &\ge(1-\varepsilon_R)
 \left[
 \mu_\Delta(R)+c_6d_6(R)
 \right]
 \langle G_Rx,x\rangle.
\end{aligned}
 \tag{L-19826.15}
\]

Subtracting the target upper bound (L-19826.14),

\[
\begin{aligned}
 &\langle D_Rx,x\rangle
 -\mu_D(R)\langle G_Rx,x\rangle\\
 &\quad\ge
 \Bigl[
 (1-\varepsilon_R)c_6d_6(R)
 -(B_R+2\varepsilon_R)C_4d_4(R)
 \Bigr]
 \langle G_Rx,x\rangle.
\end{aligned}
 \tag{L-19826.16}
\]

By (L-19826.6), (L-19826.9), and `d_4/d_6->0`, the bracket is at least
`c_6d_6/2` for all sufficiently large `R`. Therefore

\[
 \boxed{
 D_R-\mu_D(R)G_R
 \succeq {c_6\over2}d_6(R)G_R
 \quad\hbox{on }p_R^{\perp_{G_R}}.}
 \tag{L-19826.17}
\]

This is the requested complete signed arithmetic-tail hierarchy.

## 7. Sectorwise formulation

Suppose the source space is represented as

\[
 S_R=S_{R,+}\oplus S_{R,-}
\]

and the target lies in `S_(R,+)`. It is enough to prove

\[
 \Delta_{R,+}-\mu_\Delta G_{R,+}
 \succeq c_8d_8G_{R,+}
\]

on the positive target complement and

\[
 \Delta_{R,-}\succeq c_6d_6G_{R,-}.
\]

The direct-sum complete gap is `min(c_6d_6,c_8d_8)=Theta(d_6)`. A cross-sector
source-constraint repair of size `O(d_4/d_6)` changes the target energy only by
`O(d_4^2/d_6)=o(d_4)` and is absorbed by the preceding proof.

## 8. How the analytic alias theorem feeds this lemma

A sufficient analytic package is

\[
 \|\Delta_R^{-1/2}C_R\Delta_R^{-1/2}\|
 \ll R^{-1/3}(\log R)^A
 \tag{L-19826.18}
\]

and

\[
 P_R\preceq(\log R)^A\Delta_R.
 \tag{L-19826.19}
\]

Because `d_4/d_6=Theta(R^-2)`, (L-19826.18)--(L-19826.19) satisfy every
hypothesis. `L-19827` derives precisely this package from the holomorphic radial
branch, fold, and collective endpoint ledgers.

## 9. Proof boundary

- The operator transfer and the `d_6` arithmetic conclusion are exact.
- The theorem does not independently prove the PSWF cross moat or upper alias
  budget; these are analytic inputs proved/proposed in `L-19827`.
- No RH conclusion follows from the tail hierarchy alone.

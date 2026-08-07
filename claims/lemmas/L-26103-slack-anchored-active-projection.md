# L-26103 — Source-specific active projection on a fixed annulus

Claim ID: `L-26103`  
Title: Exact active minimum-norm corrections and the complete-period prime-power frame model  
Status: **CORRECTED PROPOSED EXACT ALGEBRA — UNIFORM HALF-STEP LEAKAGE CONTRACTION WITHDRAWN**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Corrected: 2026-08-08  
Issue: #261  
Depends on: `L-26101`, `L-26102`, `L-26104`, `L-26105`, `L-26106`; PR #254 `L-25301`  
Scope: exact active-set construction and frame model; not the final arithmetic theorem

## 1. Fixed annular source

Fix

\[
 \alpha=\frac9{20},
 \qquad
 \beta=\frac45,
\]

and let

\[
 I_X=[\lceil\alpha X\rceil,\lfloor\beta X\rfloor].
\]

For prime powers `q<=X` and `j in I_X`, put

\[
 A_X(q,j)
 =2\mathbf1_{q\mid j}
 -\mathbf1_{q\mid j-1}
 -\mathbf1_{q\mid j+1}.
 \tag{L-26103.1}
\]

The exact parabolic residual is

\[
 r_q=v_q(b_X^{(0)})-q^{-1/2}\log(X/q).
 \tag{L-26103.2}
\]

The annular repair problem is

\[
 A_XF\ge r.
 \tag{L-26103.3}
\]

## 2. Exact row compression

Two prime powers are equivalent at level `X` when they induce the same row on `I_X`:

\[
 q\sim_Xq'
 \iff A_X(q,\cdot)=A_X(q',\cdot).
 \tag{L-26103.4}
\]

For one equivalence class `C`, the complete family of inequalities is exactly equivalent to

\[
 A_X(C,\cdot)F\ge\max_{q\in C}r_q.
 \tag{L-26103.5}
\]

Thus duplicate rows may be compressed only after retaining the largest residual.

## 3. Exact active minimum-norm correction

Suppose a residual vector `r^(n)` has been produced. Compress identical rows and let

\[
 S_n=\{C:r_C^{(n)}>0\}.
\]

When

\[
 H_n=A_{S_n}A_{S_n}^*
\]

is invertible, define

\[
\boxed{
 u_n=A_{S_n}^*H_n^{-1}r_{S_n}^{(n)}.
}
\tag{L-26103.6}

For `0<eta<1`, set

\[
 F^{(n+1)}=F^{(n)}+\eta u_n,
\]

\[
 r^{(n+1)}=r^{(n)}-\eta A_Xu_n.
 \tag{L-26103.7}

The currently active rows decrease exactly:

\[
\boxed{
 r_{S_n}^{(n+1)}=(1-\eta)r_{S_n}^{(n)}.
}
\tag{L-26103.8}

The increment has the exact energy identity

\[
\boxed{
 \|u_n\|_2^2
 =\langle r_{S_n}^{(n)},H_n^{-1}r_{S_n}^{(n)}\rangle.
}
\tag{L-26103.9}

This is a useful finite producer and diagnostic for the active frame.

## 4. Complete-period prime-power model

For different prime bases `p!=r`, the rows `A_(p^a)` and `A_(r^b)` are orthogonal over every complete common period. Each row has mean zero, and the residue coordinates separate through the Chinese remainder theorem.

For one odd prime `p` and `a<=b`,

\[
\boxed{
 \mathbb M[A_{p^a}A_{p^b}]=\frac6{p^b}.
}
\tag{L-26103.10}

For `p=2`, the same formula holds once `a>=2`, while

\[
 \mathbb M[A_2^2]=4,
 \qquad
 \mathbb M[A_2A_{2^b}]=\frac8{2^b}\quad(b>=2).
 \tag{L-26103.11}

After diagonal normalization, an odd-prime chain has correlation

\[
 R_p(a,b)=p^{-|a-b|/2}
\]

and the finite Toeplitz floor

\[
\boxed{
 R_p\succeq
 \frac{1-p^{-1/2}}{1+p^{-1/2}}I.
}
\tag{L-26103.12}

Thus one complete prime-power chain is uniformly conditioned after normalization. The difficult arithmetic lies in finite-annulus boundaries, different-prime couplings, and the logarithmic near-null mode.

## 5. Closed initial source budget

`L-26104` proves

\[
 (r_q)_+
 \ll\frac{1+\log(X/q)}{\sqrt q}
\]

and therefore

\[
\boxed{
 \|r_+\|_2\ll\log^{3/2}(2X).
}
\tag{L-26103.13}

This part of the earlier `SAF` package is complete.

## 6. Withdrawal of the uniform half-step contraction

The exact identity (L-26103.8) controls only the rows active before the step. Leakage can activate previously negative rows.

Floating runs on the actual parabolic source contain individual half-steps for which

\[
 \|(r^{(n+1)})_+\|_2>\|(r^{(n)})_+\|_2.
\]

Therefore the formerly proposed per-step invariant

\[
 \|(r^{(n+1)})_+\|_2
 \le\rho\|(r^{(n)})_+\|_2,
 \qquad\rho<1,
\]

is withdrawn. It should not be sent to review as a theorem.

The correct globally monotone recursion is the projected-dual ascent of `L-26106`. Its Lyapunov function is the concave Hilbert--Farkas dual energy, not the positive-residual norm.

## 7. Current role of active frames

Generated active Gram floors remain useful evidence and may contribute to a proof of the Annular Dual Frame inequality, but no active-set frame bound is now an independent hypothesis in the final theorem.

The exact acceptance statement is `ADF` from `L-26105`, equivalently

\[
 \inf\{\|F\|_2:A_XF\ge r\}=X^{o(1)}.
\]

The active half-step and the projected-dual iteration are primal producers for this finite optimum.

## 8. Proof boundary

Exact:

- row compression;
- active minimum-norm correction;
- active-row reduction;
- projection energy identity;
- complete-period prime-base orthogonality and same-base covariance;
- polylogarithmic initial residual budget.

Withdrawn:

- uniform contraction of the complete positive-residual norm at every active half-step.

Open:

- `ADF`;
- a subpower annular repair;
- RH.
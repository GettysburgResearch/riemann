# L-20302 — Finite line-zero framing turns the complete kernel into a graph, then Möbius synthesis is exact

Claim ID: `L-20302`  
Title: After finitely many simple critical-line evaluations, every zero-invisible direction is a graph repair of the old radical packet and admits an explicit exact radical extension  
Status: `PROPOSED — COMPLETE FINITE PROOF; QUANTITATIVE FRAME/TAIL MOAT SEPARATE`  
Authoring agent: `gpt56-03-p`  
Created: 2026-08-01  
Dependencies: `L-18507`; `L-20301`; exact finite-dimensional metric algebra  
Scope: the enlarged selected-real-zero kernel of PRs #192 and #199  
Related counterexample candidates: none

## 1. Complete finite packet

Fix one support level. Let \(U\) be the actual complete finite packet after
ambient deficit augmentation, with positive metric \(G\). Let

\[
R\subset U
\]

be the old repaired radical-like packet and define

\[
W=R^{\perp_G}\cap U.
\tag{L-20302.1}
\]

Then

\[
U=R\oplus_G W.
\tag{L-20302.2}
\]

Assume every vector in \(U\) is represented by a function supported in one
compact multiplicative interval \([a,b]\).

## 2. Finite simple-line frame

`L-18507` proves that the simple critical-line zeta zeros form a uniqueness set
for the finite transformed space \(W\). Therefore one may choose exactly

\[
m=\dim W
\]

proof-grade simple critical-line ordinates

\[
Z=\{\gamma_1,\ldots,\gamma_m\}
\tag{L-20302.3}
\]

such that the evaluation map

\[
V_W:W\longrightarrow\mathbb C^m,
\qquad
V_Ww=
\bigl(\widehat w(\gamma_1),\ldots,\widehat w(\gamma_m)\bigr)
\tag{L-20302.4}
\]

is invertible.

Let

\[
V_R=V|_R.
\tag{L-20302.5}
\]

No quantitative lower bound is assumed yet.

## 3. Exact graph kernel

The selected-real-zero kernel inside the complete finite packet is

\[
K=U\cap\ker V.
\tag{L-20302.6}
\]

For \(r\in R\), define

\[
\boxed{
\mathcal G_Zr
=
r-V_W^{-1}V_Rr.
}
\tag{L-20302.7}
\]

Here the second term lies in \(W\). Then

\[
V\mathcal G_Zr
=
V_Rr-V_WV_W^{-1}V_Rr
=0.
\tag{L-20302.8}
\]

Conversely, if \(r+w\in K\), then

\[
V_Ww=-V_Rr
\]

and invertibility gives

\[
w=-V_W^{-1}V_Rr.
\]

Hence

\[
\boxed{
K=\operatorname{Ran}\mathcal G_Z,
\qquad
\dim K=\dim R.
}
\tag{L-20302.9}
\]

There are no independent zero-invisible augmentation directions after the
finite line frame is installed. The complete kernel is an exact graph over the
old radical coordinates.

## 4. Quantitative graph angle

Suppose

\[
V_W^*V_W\succeq\sigma^2G_W,
\qquad
\sigma>0,
\tag{L-20302.10}
\]

and

\[
V_R^*V_R\preceq\epsilon G_R.
\tag{L-20302.11}
\]

For \(w=-V_W^{-1}V_Rr\),

\[
\begin{aligned}
\sigma^2\|w\|_{G_W}^2
&\le
\|V_Ww\|_2^2\\
&=
\|V_Rr\|_2^2\\
&\le
\epsilon\|r\|_{G_R}^2.
\end{aligned}
\]

Therefore

\[
\boxed{
\|\mathcal G_Zr-r\|_{G_W}
\le
\frac{\sqrt\epsilon}{\sigma}\|r\|_{G_R}.
}
\tag{L-20302.12}
\]

The principal-angle estimate is an output of the exact graph formula. The
cofinal issue is the ratio \(\epsilon/\sigma^2\), not algebraic capture.

## 5. Exact global-radical synthesis of the graph kernel

Choose a basis map

\[
J_K:\mathbb C^{\dim R}\to K.
\tag{L-20302.13}
\]

Every vector \(J_Kc\) is compactly supported in \([a,b]\). Apply `L-20301`
coordinatewise with any integer \(N\) satisfying

\[
Na>b.
\tag{L-20302.14}
\]

This constructs an explicit source map

\[
F_N:\mathbb C^{\dim R}\to S_0^{\rm ev}
\tag{L-20302.15}
\]

and a global-radical synthesis

\[
\mathcal R_N=E F_N
\tag{L-20302.16}
\]

such that

\[
\boxed{
\mathcal R_Nc=J_Kc+T_Nc,
\qquad
\operatorname{supp}T_Nc\subset(0,a).
}
\tag{L-20302.17}
\]

The source is given explicitly by truncated Möbius dilations plus one
source-integral correction below \(a\). Thus existence of a radical synthesis
map for the **complete enlarged kernel** is unconditional.

## 6. Corrected kernel identity

Let the positive ambient complement be \(C\succ0\) and let \(Z_K\) be the
kernel-to-complement cross map. The Schur-corrected form is

\[
S_K=B_K-Z_K^*C^{-1}Z_K.
\tag{L-20302.18}
\]

Since \(\mathcal R_Nc\) is a global radical, `L-20301` gives

\[
Q_W(J_Kc,J_Kd)
=
Q_W(T_Nc,T_Nd).
\tag{L-20302.19}
\]

Therefore

\[
\boxed{
\begin{aligned}
\langle S_KJ_Kc,J_Kc\rangle
={}&Q_W(T_Nc,T_Nc)\\
&-\|C^{-1/2}Z_KJ_Kc\|^2.
\end{aligned}
}
\tag{L-20302.20}
\]

The complete kernel problem has now been reduced to one explicit lower-tail
operator and one explicit Schur cross norm.

## 7. Sufficient cofinal moat

If

\[
|Q_W(T_Nc,T_Nc)|
+
\|C^{-1/2}Z_KJ_Kc\|^2
\le
\eta\|J_Kc\|_G^2
\tag{L-20302.21}
\]

for every \(c\), then

\[
\boxed{
S_K\succeq-\eta G_K.
}
\tag{L-20302.22}
\]

Along a cofinal sequence, \(\eta_j\to0\) is exactly the final lower-floor
estimate.

A useful sufficient decomposition is

\[
\eta_j
\le
\eta^{\rm oldrad}_j
+
C_j\frac{\epsilon_j}{\sigma_j^2}
+
\eta^{\rm Mobius}_j
+
\eta^{\rm cross}_j,
\tag{L-20302.23}
\]

provided all four terms are proved in the same metric. The equation is a
scheduler, not an assertion that any term is already small.

## 8. What has been removed from the frontier

This theorem closes three previously distinct qualitative questions.

1. **Finite zero visibility:** finitely many simple line zeros frame the actual
   finite complement.
2. **Kernel dimension:** the complete kernel has exactly the old radical rank.
3. **Radical synthesis existence:** every graph-kernel vector has an explicit
   exact global-radical extension.

The only remaining issue is quantitative:

\[
\boxed{
\text{the explicit Möbius lower-tail plus Schur cross must be }o(1)
\text{ in the complete kernel metric.}
}
\tag{L-20302.24}
\]

## 9. False-RH obstruction

At any nontrivial zero parameter \(z_\rho\), `L-20301` gives

\[
\widehat{T_Nc}(z_\rho)
=
-\widehat{J_Kc}(z_\rho).
\tag{L-20302.25}
\]

If the hierarchy captures an off-line Xi-cardinal difference, its right side is
nonzero and fixed. Therefore no evaluation-controlling form norm can make the
complete Möbius tail vanish. This agrees with `L-19701/T-19701`: the
quantitative tail moat is RH-bearing.

## 10. Proof boundary

- Finite line-zero extraction is inherited from `L-18507`.
- The graph formula and dimension statement are exact.
- Exact local radical synthesis is supplied by `L-20301`.
- No lower bound uniform in support is proved for \(\sigma_j\).
- No cofinal Weil-form bound is proved for the explicit divisor tail.
- The theorem removes qualitative capture and synthesis-existence blockers; it
  does not prove RH.

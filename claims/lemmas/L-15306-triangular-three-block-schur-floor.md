# L-15306 — Triangular three-block Schur floor

Claim ID: `L-15306`  
Title: Eliminate the ambient complement first and charge the radical row only once  
Status: `PROPOSED`  
Authoring agent: `gpt56-03-k`  
Created: 2026-07-31  
Dependencies: completion of squares; positive-metric Schur complements; `L-14308`; radical-tail identity `L-14309`; visible-block floor `L-15305`  
Scope: exact finite algebra for the radical/visible/ambient decomposition

## 1. Setup

Let `R`, `V`, and `E` be finite-dimensional real or complex Hilbert spaces. Let

\[
G_R\succ0,\qquad G_V\succ0,\qquad M\succ0
\]

be declared metrics, and let

\[
\mathcal H=
\begin{pmatrix}
 B_R&X^*&Y^*\\
 X&B_V&Z^*\\
 Y&Z&C
\end{pmatrix}
\tag{L-15306.1}
\]

be Hermitian on `R direct-sum V direct-sum E`. The maps have the orientations

\[
X:R\to V,\qquad Y:R\to E,\qquad Z:V\to E.
\]

Assume that, for real numbers

\[
e\ge0,\qquad h>0,\qquad \beta>0,
\]

one has

\[
\boxed{B_R\succeq-eG_R,}
\tag{L-15306.2}
\]

\[
\boxed{C\succeq hM,}
\tag{L-15306.3}
\]

and the **visible Schur floor**

\[
\boxed{
S_V:=B_V-h^{-1}Z^*M^{-1}Z\succeq\beta G_V.}
\tag{L-15306.4}
\]

Define the complement-corrected radical-visible cross map

\[
\boxed{
\widetilde X:=X-h^{-1}Z^*M^{-1}Y}
\tag{L-15306.5}
\]

and the complete radical correction

\[
\boxed{
K_R:=h^{-1}Y^*M^{-1}Y
+\beta^{-1}\widetilde X^*G_V^{-1}\widetilde X.}
\tag{L-15306.6}
\]

## 2. Main theorem

If, for some `kappa>=0`,

\[
\boxed{K_R\preceq\kappa G_R,}
\tag{L-15306.7}
\]

then

\[
\boxed{
\mathcal H\succeq
-(e+\kappa)\operatorname{diag}(G_R,0,0).}
\tag{L-15306.8}
\]

In particular, relative to the complete metric

\[
\mathcal G=\operatorname{diag}(G_R,G_V,M),
\]

one has

\[
\boxed{
\lambda_{\min}(\mathcal H,\mathcal G)\ge-(e+\kappa).}
\tag{L-15306.9}
\]

If the represented matrix differs from the exact form by a lower-floor assembly
radius `delta>=0`, then

\[
\boxed{
\lambda_{\min}(\mathcal H_{\rm exact},\mathcal G)
\ge-(e+\kappa+\delta).}
\tag{L-15306.10}
\]

This is the exact finite three-block estimate requested by the positive route.

## 3. Proof by ordered completion of squares

For `r in R`, `v in V`, and `w in E`, write the quadratic form of
`mathcal H`. From (L-15306.3),

\[
\begin{aligned}
q(r,v,w)\ge{}&
\langle B_Rr,r\rangle
+2\operatorname{Re}\langle Xr,v\rangle
+2\operatorname{Re}\langle Yr,w\rangle\\
&+\langle B_Vv,v\rangle
+2\operatorname{Re}\langle Zv,w\rangle
+h\langle Mw,w\rangle.
\end{aligned}
\]

Complete the `E` square with the **combined** source `Yr+Zv`:

\[
\begin{aligned}
h\langle Mw,w\rangle
+2\operatorname{Re}\langle Yr+Zv,w\rangle
={}&h\left\|M^{1/2}w+h^{-1}M^{-1/2}(Yr+Zv)\right\|^2\\
&-h^{-1}\langle M^{-1}(Yr+Zv),Yr+Zv\rangle.
\end{aligned}
\tag{L-15306.11}
\]

After expansion, the remaining `V` block is `S_V`, the remaining cross map is
exactly `widetilde X`, and the radical diagonal has lost
`h^-1 Y^*M^-1Y`. Using (L-15306.4), complete the `V` square:

\[
\begin{aligned}
\beta\langle G_Vv,v\rangle
+2\operatorname{Re}\langle\widetilde Xr,v\rangle
={}&\beta\left\|G_V^{1/2}v+
\beta^{-1}G_V^{-1/2}\widetilde Xr\right\|^2\\
&-\beta^{-1}
\langle G_V^{-1}\widetilde Xr,\widetilde Xr\rangle.
\end{aligned}
\tag{L-15306.12}
\]

Discarding the two nonnegative squares gives

\[
q(r,v,w)\ge\langle(B_R-K_R)r,r\rangle.
\tag{L-15306.13}
\]

Equations (L-15306.2) and (L-15306.7) prove (L-15306.8). Since
`r^*G_Rr <= (r,v,w)^*mathcal G(r,v,w)`, (L-15306.9) follows. A robust assembly
loss gives (L-15306.10). QED.

## 4. Why the naive four-term budget is unnecessarily expensive

A direct triangle estimate suggests charging

\[
\frac{\|X\|^2}{\beta}
+\frac{\|Y\|^2+\|Z\|^2}{h}.
\tag{L-15306.14}
\]

That is not the correct three-block geometry.

1. `Z` is not a radical loss. It is absorbed into the visible Schur floor
   `B_V-h^-1Z^*M^-1Z`.
2. The relevant radical-visible cross is not `X`; it is
   `X-h^-1Z^*M^-1Y`.
3. Cancellation between the direct `R--V` path and the indirect
   `R--E--V` path is exact and must be retained before norms are taken.

Thus the sharp proof-facing error is the single positive matrix `K_R`, not a sum
of independently widened channels.

## 5. Combined-positive-block interpretation

Define the triangular lower model on `V direct-sum E`

\[
D_0=
\begin{pmatrix}
\beta G_V+h^{-1}Z^*M^{-1}Z&Z^*\\
Z&hM
\end{pmatrix}.
\tag{L-15306.15}
\]

It is positive definite and

\[
\langle D_0(v,w),(v,w)\rangle
=\beta\|v\|_{G_V}^2
+h\|w+h^{-1}M^{-1}Zv\|_M^2.
\tag{L-15306.16}
\]

With `L=(X,Y)^T`, one has the exact identity

\[
\boxed{L^*D_0^{-1}L=K_R.}
\tag{L-15306.17}
\]

Consequently `K_R` is the squared dual norm of the **complete radical row** in
the already Schur-corrected positive metric on `V direct-sum E`.

This gives the most economical analytic interface. It is enough to prove

\[
|\langle Xr,v\rangle+\langle Yr,w\rangle|
\le \eta\|r\|_{G_R}\|(v,w)\|_{D_0}
\tag{L-15306.18}
\]

for all vectors. Then

\[
\boxed{K_R\preceq\eta^2G_R,}
\tag{L-15306.19}
\]

so one may take `kappa=eta^2`.

## 6. Exact radical-tail specialization

Suppose the `R` packet consists of localized truncations `k_r` of exact global
radical vectors `r_r=k_r+t_r`. Radicality gives

\[
Q(k_r,g)=-Q(t_r,g),
\qquad
Q(k_r,k_s)=Q(t_r,t_s).
\tag{L-15306.20}
\]

Therefore:

- `B_R` is the tail-tail Gram;
- `(X,Y)` is minus one and the same tail functional restricted to the visible
  and ambient sectors;
- `K_R` is precisely its squared dual norm in the triangular positive metric
  (L-15306.16).

The whole radical row is consequently controlled by one form-topology tail
estimate. There is no need to bound `X` and `Y` independently or to demand
`Z->0`.

## 7. Relative visible-coupling corollary

A convenient way to prove (L-15306.4) is to begin with

\[
B_V\succeq\beta_0G_V
\tag{L-15306.21}
\]

and certify, for one fixed `0<=theta<1`,

\[
Z^*M^{-1}Z\preceq\theta\,\beta_0h\,G_V.
\tag{L-15306.22}
\]

Then

\[
\boxed{S_V\succeq(1-\theta)\beta_0G_V.}
\tag{L-15306.23}
\]

Hence `Z` may be large in absolute norm. Only its size relative to the visible
and ambient floors matters.

## 8. Directed finite certificate

A proof object should bind:

1. positive metric Grams `G_R,G_V,M`;
2. exact or directed blocks `B_R,B_V,C,X,Y,Z` in those coordinates;
3. a lower complement LMI `C-hM>=0`;
4. the complete visible Schur LMI (L-15306.4);
5. the corrected cross map (L-15306.5), recomputed rather than trusted;
6. the radical correction LMI (L-15306.7);
7. the radical diagonal loss (L-15306.2);
8. one separately derived assembly radius.

`X-15304` implements this interface with exact rational arithmetic and rejects
mutations of every load-bearing gate.

## 9. Proof boundary

- The block theorem is exact finite algebra.
- It does not construct the radical/visible split.
- It does not prove `L-15305`'s visible floor at production levels.
- It does not supply a uniform growing-packet tail estimate.
- It does not audit the Suzuki/CCM form normalization.
- The cofinal rates are isolated in `T-15302`; RH is not claimed here.

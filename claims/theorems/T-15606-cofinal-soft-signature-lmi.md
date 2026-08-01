# T-15606 — Cofinal soft-signature LMI from complete-frame support averaging

Claim ID: `T-15606`  
Title: Exporting the actual profile-soft packet after support selection gives a Schur negative part of order `a_T^(3/4)`  
Status: `PROVED CONDITIONAL COMPOSITION; PRODUCTION FULL-BLOCK PHASE LEDGER AND NORMALIZATION AUDIT OPEN`  
Authoring agent: `gpt56-08`  
Created: 2026-08-01  
Dependencies: `L-15630`, `L-15631`, `L-15632`, `L-16220`, `L-16226`, `L-18512`; the exact Weil explicit-formula normalization  
Scope: the finite profile-soft sector left after complete source-frame conditioning  
Related counterexample candidates: none

## 1. Purpose

`L-15630` constructs a complete exact source frame and proves sub-square-root
conditioning in a regularized profile metric. It leaves a finite profile-soft
sector because small ordinary tail mass alone does not control a signed Weil
form.

The missing observation is that the soft projector must be formed **after** a
support has been selected at which the complete actual Weil block is close to
its positive line-centered comparator. The comparison is made on the whole
low-plus-harmonic block. `L-15632` then passes that full-block moat through the
harmonic Schur complement.

The terminal-prime, polar, archimedean, local, and harmonic terms remain in one
matrix throughout.

## 2. Complete frame on a support block

Let

\[
 T\le R\le2T,
 \qquad T\to\infty.
 \tag{T-15606.1}
\]

Let `U_R` be the actual finite low/source packet, with production metric
`G_R`, and let

\[
 F_R:U_R\to\mathcal S_R,
 \qquad
 \mathcal L_RF_R=I_{U_R},
 \tag{T-15606.2}
\]

be the complete exact source frame of `L-15630/L-15631`.

Let

\[
 \mathcal T_R:U_R\to\mathcal X_R
 \tag{T-15606.3}
\]

be its actual omitted-tail/profile map and put

\[
 D_R=\mathcal T_R^*\mathcal T_R\succeq0.
 \tag{T-15606.4}
\]

Let `K_R` be the Gram of every amplitude and logarithmic support-derivative
channel entering the complete Hilbert-valued support large sieve. Assume the
block-uniform LMI

\[
 \boxed{K_R\preceq\mathfrak M_T^2G_R}
 \qquad(T\le R\le2T).
 \tag{T-15606.5}
\]

The exact smooth Mellin-cardinal construction gives the proposed production
rate

\[
 \mathfrak M_T=T^{1/4+o(1)}.
 \tag{T-15606.6}
\]

The theorem only needs

\[
 \boxed{
 \mathfrak a_T
 :=
 {\mathfrak M_T^2(\log T)^2\over T}
 \longrightarrow0.
 }
 \tag{T-15606.7}
\]

## 3. Regularized metric and optimal balancing

Set

\[
 \boxed{
 \tau_T={\mathfrak M_T\over\sqrt T}
 ={\sqrt{\mathfrak a_T}\over\log T}.
 }
 \tag{T-15606.8}
\]

For every support in the block define

\[
 \widehat D_R=D_R+\tau_TG_R.
 \tag{T-15606.9}
\]

Then

\[
 K_R
 \preceq
 B_T^2\widehat D_R,
 \qquad
 B_T^2={\mathfrak M_T^2\over\tau_T}
 =\mathfrak M_T\sqrt T.
 \tag{T-15606.10}
\]

The normalized large-sieve envelope is

\[
 \boxed{
 {B_T\over\sqrt{T/\log T}}
 =\mathfrak a_T^{1/4}
 \longrightarrow0.
 }
 \tag{T-15606.11}
\]

Also

\[
 \boxed{
 \tau_T\log T=\sqrt{\mathfrak a_T}\longrightarrow0.
 }
 \tag{T-15606.12}
\]

This balancing is exactly what is needed simultaneously for the hard-frame
large sieve and the soft-signature estimate.

## 4. Actual and line-centered full blocks

Let `E_R` denote the positive harmonic/form-core sector used in the direct
shorting theorem of PR #191, with metric `M_R`. On

\[
 U_R\oplus E_R
\]

let

\[
 \mathcal H_R
 =
 \begin{pmatrix}
 B_R&Z_R^*\\
 Z_R&C_R
 \end{pmatrix}
 \tag{T-15606.13}
\]

be the exact actual Suzuki block. It is assembled from:

1. the complete archimedean and local terms;
2. every prime power in the exact support;
3. the complete polar channel, with the terminal-prime pole cancellation
   performed before taking bounds;
4. the low--harmonic cross and harmonic block.

Let

\[
 \mathcal H_R^0
 =
 \begin{pmatrix}
 B_R^0&(Z_R^0)^*\\
 Z_R^0&C_R^0
 \end{pmatrix}
 \tag{T-15606.14}
\]

be the zero-side comparator obtained by replacing every centered zero parameter
by its real ordinate.

Because every line-centered zero contributes a positive rank-one square,

\[
 \boxed{\mathcal H_R^0\succeq0.}
 \tag{T-15606.15}
\]

The dimension-free local-Weyl and ambient-floor estimates supply fixed
constants `c,C>0` such that

\[
 \boxed{
 C_R^0\succeq c(\log T)M_R,
 }
 \tag{T-15606.16}
\]

and

\[
 \boxed{
 B_R^0\preceq C(\log T)\widehat D_R
 }
 \tag{T-15606.17}
\]

throughout the block, after the directed finite radial/local errors have been
inserted.

## 5. Full-block support averaging

Put

\[
 \widehat{\mathcal G}_R
 =\widehat D_R\oplus M_R.
 \tag{T-15606.18}
\]

The difference

\[
 \mathcal E_R=\mathcal H_R-\mathcal H_R^0
 \tag{T-15606.19}
\]

is exactly the complete horizontal-displacement block. The Hilbert-valued
support large sieve of `L-16226`, applied to the complete exact source and
harmonic profile frame, gives

\[
 {1\over T}
 \int_T^{2T}
 \left\|
 \widehat{\mathcal G}_R^{-1/2}
 \mathcal E_R
 \widehat{\mathcal G}_R^{-1/2}
 \right\|^2dR
 \le
 C_1{B_T^2(\log T)^3\over T}
 +o((\log T)^2).
 \tag{T-15606.20}
\]

Using (T-15606.10), the main right side is

\[
 C_1\mathfrak a_T^{1/2}(\log T)^2.
 \tag{T-15606.21}
\]

Therefore there is a support

\[
 R_T\in[T,2T]
 \tag{T-15606.22}
\]

outside every declared exceptional or zeta-cycle length such that

\[
 \boxed{
 \left\|
 \widehat{\mathcal G}_{R_T}^{-1/2}
 \mathcal E_{R_T}
 \widehat{\mathcal G}_{R_T}^{-1/2}
 \right\|
 \le
 \varepsilon_T,
 }
 \tag{T-15606.23}
\]

where, after the finite directed remainders are placed below the same scale,

\[
 \boxed{
 \varepsilon_T
 =O(\mathfrak a_T^{1/4}\log T)
 =o(\log T).
 }
 \tag{T-15606.24}
\]

All support averaging occurs before a soft spectral projector is formed. No
moving projector is differentiated.

## 6. Export of the actual soft packet

At the selected support `R_T`, whiten the actual profile Gram:

\[
 \widetilde D_T
 =G_{R_T}^{-1/2}D_{R_T}G_{R_T}^{-1/2}.
 \tag{T-15606.25}
\]

Define the mathematical soft projector

\[
 \boxed{
 P_T^{\rm soft}
 =\mathbf1_{[0,\tau_T]}(\widetilde D_T).
 }
 \tag{T-15606.26}
\]

and let

\[
 S_T=\operatorname{Ran}P_T^{\rm soft}.
 \tag{T-15606.27}
\]

On `S_T`,

\[
 D_{R_T}\preceq\tau_TG_{R_T}
 \tag{T-15606.28}
\]

and hence

\[
 \boxed{
 \widehat D_{R_T}|_{S_T}
 \preceq2\tau_TG_{R_T}|_{S_T}.
 }
 \tag{T-15606.29}
\]

A production exporter may use a buffered split. Put every generalized
eigenvalue whose directed enclosure meets `[tau_T,2tau_T]` into the soft
packet. Then (T-15606.29) becomes `3tau_T G`, while the complementary hard
packet has `D>=tau_T G`. This fails closed and needs no floating eigenspace.

The exporter records:

```text
selected support and block provenance;
G_R, D_R, K_R and the threshold tau_T;
a directed generalized spectral projector or buffered rational basis;
soft and hard Gram LMIs;
all source, prime-power, radial and normalization digests.
```

## 7. Harmonic Schur estimate on the soft packet

Restrict the actual and line-centered blocks to

\[
 S_T\oplus E_{R_T}.
\]

Apply `L-15632` with

\[
 D=\widehat D_{R_T}|_{S_T},
 \qquad
 h=c\log T,
 \qquad
 \ell=C\log T,
 \qquad
 \varepsilon=\varepsilon_T.
 \tag{T-15606.30}
\]

The ratios `ell/h` remain bounded and

\[
 \varepsilon_T/h=O(\mathfrak a_T^{1/4})\to0.
 \tag{T-15606.31}
\]

Thus the coefficient `eta_T` of `L-15632` satisfies

\[
 \eta_T
 =O(\mathfrak a_T^{1/4}\log T).
 \tag{T-15606.32}
\]

Let

\[
 \mathscr S_T^{\rm soft}
 =B_T^{\rm soft}
 -(Z_T^{\rm soft})^*C_{R_T}^{-1}Z_T^{\rm soft}
 \tag{T-15606.33}
\]

be the actual harmonic Schur block. Equations (T-15606.29) and
(L-15632.12) give

\[
\begin{aligned}
 \left\|
 \left[
 G_{S,T}^{-1/2}
 \mathscr S_T^{\rm soft}
 G_{S,T}^{-1/2}
 \right]_{-}
 \right\|
 &\le2\tau_T\eta_T\\
 &=O(\mathfrak a_T^{3/4}).
\end{aligned}
 \tag{T-15606.34}
\]

Therefore

\[
 \boxed{
 \left\|
 \left[
 G_{S,T}^{-1/2}
 \mathscr S_T^{\rm soft}
 G_{S,T}^{-1/2}
 \right]_{-}
 \right\|
 \longrightarrow0.
 }
 \tag{T-15606.35}
\]

The buffered export changes only the fixed constant.

## 8. Direct PR #191 production matrix

For a finite line-centered harmonic solve `X_T`, the proof-facing matrix is

\[
\boxed{
\begin{aligned}
 \mathscr D_T^{\rm soft}
 ={}&P_{T,S}+E_{T,S}\\
 &-(Z_{T,S})^*X_T-X_T^*Z_{T,S}+X_T^*C_TX_T\\
 &-h_T^{-1}
 \mathscr R_T^*M_T^{-1}\mathscr R_T,
\end{aligned}}
 \tag{T-15606.36}
\]

with

\[
 \mathscr R_T=Z_{T,S}-C_TX_T.
 \tag{T-15606.37}
\]

Here `P_(T,S)` contains the complete finite/local, archimedean, and exactly
pole-cancelled endpoint terms, and `E_(T,S)` is the complete centered
terminal-prime matrix. Every prime power is included.

A directed producer may either:

1. verify (T-15606.34) through the line-centered perturbation ledger; or
2. prove directly
   \[
   \mathscr D_T^{\rm soft}\succeq-\rho_TG_{S,T}
   \]
   with `rho_T` no larger than the analytic bound.

The line-centered Galerkin residual and directed assembly radius are chosen,
at each finite support, to be `o(a_T^(3/4))`. Form-core density and arbitrary
precision make this a proof-production refinement, not a new asymptotic gate.

## 9. Cofinal sequence

Choose any sequence of dyadic blocks

\[
 [T_j,2T_j],
 \qquad T_j\to\infty,
 \tag{T-15606.38}
\]

for which the complete-frame graph LMI and phase ledger hold and

\[
 \mathfrak a_{T_j}\to0.
 \tag{T-15606.39}
\]

Select one support `R_j` from each block by Section 5 and export the packet by
Section 6. Then

\[
 R_j\to\infty
 \tag{T-15606.40}
\]

and

\[
 \boxed{
 \left\|
 \left[
 G_{S,j}^{-1/2}
 \mathscr S_j^{\rm soft}
 G_{S,j}^{-1/2}
 \right]_{-}
 \right\|
 =O(\mathfrak a_{T_j}^{3/4})+o(1)
 \longrightarrow0.
 }
 \tag{T-15606.41}
\]

This is the requested cofinal soft-signature theorem.

## 10. Composition with the hard complement

On the hard packet, `D>=tau_TG`, so the same complete-frame envelope gives

\[
 \mathfrak B_T^{\rm hard}
 \le{\mathfrak M_T\over\sqrt{\tau_T}}
 =B_T
 =o\!\left(\sqrt{T/\log T}\right).
 \tag{T-15606.42}
\]

Therefore `L-15627` supplies the positive hard-complement compression floor,
while (T-15606.41) closes the only finite profile-soft signature block. The
previously proved radical-row and assembly rates may then be inserted into the
three-block lower-envelope theorem.

## 11. Exact proof boundary

The finite Schur perturbation theorem and the rate calculation are exact. The
zeta-specific cofinal conclusion depends on the following already-declared
production interfaces:

1. the exact full-block Weil normalization equating the prime/polar/
   archimedean assembly with the zero-side matrix;
2. the smooth exact source-frame graph LMI (T-15606.5), including the local
   zeta-product and multiplicative norm transport audits of `L-15631`;
3. the complete low-plus-harmonic phase and endpoint ledger needed to apply
   `L-16226` in the block metric;
4. directed local-Weyl upper and ambient-floor constants in
   (T-15606.16)--(T-15606.17).

No production packet satisfying all four interfaces has yet been emitted.
Accordingly, this theorem completes the symbolic conditioning-to-soft-LMI
composition but does not, by itself, constitute a verified proof of RH.

# L-91882 — The live arithmetic `Gamma_X` is one explicit finite/Volterra coupling

Claim ID: `L-91882`  
Status: **CANDIDATE-COMPLETE LIVE COUPLING ON FROZEN ARITHMETIC INPUTS — REVIEW REQUIRED**  
Created: 2026-08-16  
Inputs: `L-91880`, `L-91881`, `L-91850`, `L-91110`  
RH status: **unproved**

Let `Q_X^B(dt,dj)` be the frozen martingale B-spline kernel on the tagged bulk target. Let `I_A` be the identity kernel on finite anchored rows.

## 1. Bulk incidences and output

For `s` in a retained complete cell, put `x=X/s`, and let

\[
a_k=\ell_x(k),\quad P_+(x)=\sum_{\mu(e)=1}a_e,\quad P_-(x)=\sum_{\mu(o)=-1}a_o.
\]

Define the exact complete-graph Hall incidence

\[
\pi_s(o,e)=\frac{a_oa_e}{P_+(x)}
\]

and residual

\[
r_s(e)=a_e\frac{P_+(x)-P_-(x)}{P_+(x)}.
\]

Then

\[
\sum_e\pi_s(o,e)=a_o,\qquad \sum_o\pi_s(o,e)+r_s(e)=a_e.
\tag{L-91882.1}
\]

Every colour multiplies the same complete packet `p_s`, so every matched edge cancels in target, score, every row, ordinary `q`, ordinary `4q`, detail and intrinsic boundary coordinates.

The positive bulk output coupling is

\[
\boxed{d\Gamma_{X,B}(s,e,t,j)=\tau_K\frac2s r_s(e)E_s(dt)Q_X^B(t,dj)\,ds.}
\tag{L-91882.2}
\]

The edge measure

\[
d\Pi_{X,B}(s,o,e)=\frac2s\pi_s(o,e)\,ds
\]

is retained in the source audit. Its physical output is the zero packet because the two incidences carry the same `p_s`.

No bulk record has a rough owner or a causal child.

## 2. Anchored incidences and output

Let `mathscr L_(X,A)` be the literal terminal path set of `L-91881`. For each leaf define

\[
\Gamma_{\omega}^{\rm res}=\omega_X\,\operatorname{Place}_\omega(R(\nu_\omega)),
\]

\[
\Gamma_{\omega}^{\rm bon}=\omega_X\,\operatorname{Place}_\omega(B_\omega).
\]

The anchored coupling is

\[
\boxed{\Gamma_{X,A}=\tau_K\sum_{\omega\in\mathscr L_{X,A}}\left(\Gamma_\omega^{\rm res}+\Gamma_\omega^{\rm bon}\right).}
\tag{L-91882.3}
\]

The corresponding incidence measures `Pi_omega` satisfy the exact leaf marginals of (L-91881.3). The same path coefficient `omega_X` multiplies target, score, every row and both ordinary columns.

## 3. One physical target and one quantizer

Use the disjoint target

\[
\mathcal T_X=\mathcal T_{X,A}\dotplus\mathcal T_{X,B}
\]

and the sole quantizer

\[
\boxed{Q_X^{\rm nat}=I_A\oplus Q_X^B.}
\tag{L-91882.4}
\]

It depends only on the physical target point. Dependence on parity, Hall edge, Target-Lorenz cutoff, first owner, rough history or current/child label is forbidden.

The complete positive coupling is

\[
\boxed{\Gamma_X=\Gamma_{X,A}+\Gamma_{X,B}.}
\tag{L-91882.5}
\]

The finite row is its output marginal

\[
\boxed{d_X(j)=\Gamma_X(\mathcal Z_X\times\mathcal T_X\times\{j\}).}
\tag{L-91882.6}
\]

## 4. Explicit thinning discard

For each positive and negative native input marginal define the discard

\[
\Sigma_X^{\rm disc,\pm}=(1-\tau_K)\Sigma_X^\pm.
\]

The retained Hall/Lorenz incidences and residuals are multiplied by `tau_K`. For each sign,

\[
\boxed{\text{retained incidence marginal}+\text{discard marginal}=\text{native input marginal}.}
\tag{L-91882.7}
\]

## 5. One-use table

```text
bulk odd occurrence          one Hall edge incidence
bulk even occurrence         edge incidences plus one residual
anchored occurrence          one stopping-tree path distribution
rough monomial               one least rough owner
terminal even occurrence     Target-Lorenz used plus residual
terminal odd occurrence      one Target-Lorenz incidence
row bonus                    one current leaf owner
path coefficient             one application
physical packet              one placement
bulk endpoint                one tagged complete cell
all outputs                   one block-diagonal quantizer
```

The output marginal is not used to infer ownership; the incidence marginals prove ownership independently.
# L-18503 — Direct harmonic-Schur saturation by a sacrificial high subspace

Claim ID: `L-18503`  
Title: A one-end high-floor subspace closes the full low Schur operator without the certified-zero count  
Status: `PROPOSED`  
Authoring agent: `gpt56-02-p`  
Created: 2026-07-31  
Dependencies: Courant--Fischer; inverse Ritz; the harmonic lift; dimension-uniform local-Weyl boundary floor  
Scope: an alternative completion of the final gate in the harmonic three-block program  
Related candidates: none

## 1. Abstract theorem

Let `S` be Hermitian on an `n`-dimensional Hilbert space with positive metric
`G`. Let `R` be an `r`-dimensional subspace. After whitening by `G`, write

\[
 B=P_RSP_R|_R,
 \qquad
 X=P_{R^\perp}SP_R|_R.
 \tag{L-18503.1}
\]

Assume

\[
 \boxed{-\alpha I_R\preceq B\preceq\alpha I_R,}
 \tag{L-18503.2}
\]

\[
 \boxed{X^*X\preceq\beta^2 I_R.}
 \tag{L-18503.3}
\]

Suppose there exists a subspace `W` such that

\[
 \boxed{\operatorname{codim}W\le r,}
 \tag{L-18503.4}
\]

and

\[
 \boxed{S|_W\succeq\Gamma I_W.}
 \tag{L-18503.5}
\]

Choose any real `t` satisfying

\[
 \boxed{\alpha<t<\Gamma.}
 \tag{L-18503.6}
\]

Then

\[
 \boxed{
 \lambda_{\min}(S)
 \ge
 -\alpha-\frac{\beta^2}{t-\alpha}.}
 \tag{L-18503.7}
\]

No selected-zero Gram, omitted-zero budget, principal angle, or explicit
visible-space split is required.

## 2. Proof

### Exact low-index saturation

Equation (L-18503.5) and Courant--Fischer give

\[
 N_S(\Gamma)\le r.
 \tag{L-18503.8}
\]

Equation (L-18503.2) gives

\[
 \langle Su,u\rangle\le\alpha\|u\|^2<t\|u\|^2
 \qquad(0\ne u\in R),
\]

so

\[
 N_S(t)\ge r.
 \tag{L-18503.9}
\]

Since `t<Gamma`,

\[
 \boxed{N_S(t)=N_S(\Gamma)=r.}
 \tag{L-18503.10}
\]

Thus `R` accounts for the complete low spectral multiplicity even though no
angle between `R` and the actual low eigenspace was assumed.

### Inverse-Ritz floor

Put

\[
 D=tI_R-B.
\]

Then

\[
 (t-\alpha)I_R\preceq D\preceq(t+\alpha)I_R.
 \tag{L-18503.11}
\]

For the shifted operator `S-tI`, its compression and squared-residual forms on
`R` are

\[
 H=B-tI_R=-D,
 \tag{L-18503.12}
\]

\[
 K=(B-tI_R)^2+X^*X=D^2+X^*X.
 \tag{L-18503.13}
\]

Let

\[
 s=t+\alpha+\frac{\beta^2}{t-\alpha},
 \qquad q=-\frac1s<0.
 \tag{L-18503.14}
\]

Since

\[
 D^2\preceq(t+\alpha)D,
 \qquad
 X^*X\preceq\beta^2I_R
 \preceq\frac{\beta^2}{t-\alpha}D,
\]

we have

\[
 K\preceq sD.
\]

Equivalently,

\[
 \boxed{qK-H=D-K/s\succeq0.}
 \tag{L-18503.15}
\]

The shifted operator has exactly `r` negative eigenvalues by
(L-18503.10). On the `r`-dimensional space `(S-tI)R`, the Rayleigh quotient of
`(S-tI)^(-1)` is at most `q`. Min--max for the inverse therefore gives

\[
 \frac1{\lambda_{\min}(S)-t}\le q.
\]

Both sides are negative, so inversion gives

\[
 \lambda_{\min}(S)\ge t+\frac1q
 =-\alpha-\frac{\beta^2}{t-\alpha},
\]

proving (L-18503.7). If `t` belongs to the spectrum, replace it by a decreasing
nearby sequence and pass to the limit. QED.

## 3. Harmonic application

For the complete low packet `U_lambda`, let

\[
 S_{U,\lambda}
 =B_\lambda-L_\lambda^*C_\lambda^{-1}L_\lambda,
 \qquad
 G_{C,\lambda}=J_\lambda^*G_\lambda J_\lambda.
 \tag{L-18503.16}
\]

Whiten by `G_(C,lambda)` and take `R_lambda` to be the exact localized radical
packet. The Gaussian radical-tail theorem supplies (L-18503.2)--(L-18503.3)
with

\[
 \alpha_\lambda\to0,
 \qquad
 \beta_\lambda\to0
 \tag{L-18503.17}
\]

after the declared metric losses.

It remains only to exhibit `W_lambda subset U_lambda` with

\[
 \operatorname{codim}W_\lambda\le\dim R_\lambda
 \tag{L-18503.18}
\]

and a direct harmonic-Schur floor

\[
 S_{U,\lambda}|_{W_\lambda}
 \succeq\Gamma_\lambda
 G_{C,\lambda}|_{W_\lambda},
 \qquad
 \liminf\Gamma_\lambda>0.
 \tag{L-18503.19}
\]

Then choose one fixed `t>0` below `Gamma_lambda` eventually. Equation
(L-18503.7) gives

\[
 \boxed{
 \lambda_{\min}(S_{U,\lambda},G_{C,\lambda})
 \ge
 -\alpha_\lambda
 -\frac{\beta_\lambda^2}{t-\alpha_\lambda}
 \longrightarrow0^-.}
 \tag{L-18503.20}
\]

The directed assembly radius may be added afterward.

## 4. One-end local-Weyl witness

Suppose `U_lambda` has two endpoint-profile sectors and one endpoint sector
`W_lambda` satisfies the codimension gate (L-18503.18). Restricting the
quadratic form to `W_lambda` eliminates every opposite-end cross term. In
particular the centered terminal-prime Hankel matrix that couples the two ends
never enters the witness inequality.

If the harmonic lifts `J_lambda W_lambda` obey the graph/profile hypotheses of
the dimension-uniform local-Weyl theorem, that theorem gives

\[
 \boxed{
 S_{U,\lambda}|_{W_\lambda}
 \succeq
 \left[
 \log R_\lambda-O(1)-o(1)
 \right]
 G_{C,\lambda}|_{W_\lambda}.}
 \tag{L-18503.21}
\]

Thus `Gamma_lambda->infinity`, far stronger than needed. The full terminal-prime
operator norm, the selected-zero count, and the omitted-zero absolute budget are
all bypassed.

The load-bearing analytic statement is now only that the exact harmonic lift of
the one-end packet remains inside the local-Weyl graph class with a controlled
metric. This is a same-end profile theorem, not a global zeta-zero count.

## 5. Why this can succeed when the count route stalls

The selected-zero count asks for a lower frame of one positive *part* of the
zero expansion and must pay an absolute budget for every omitted zero. The
direct Schur form retains the cancellation and positivity already present in
the complete localized Weil operator. The local-Weyl theorem treats off-critical
horizontal displacement before taking absolute values, at cost `O(log R/R)`.

Therefore a one-end direct-form witness can have a growing floor even when no
finite selected-zero Gram has a useful cofinal omitted-zero moat.

## 6. Exact finite certificate

A finite proof object contains:

1. directed `G_C` and `S_U` matrices;
2. exact bases for `R` and `W`;
3. the codimension inequality;
4. an exact `LDL*` certificate for `S_W-Gamma G_W`;
5. exact compression bounds `+-alpha G_R`;
6. a complete cross-residual Gram bound `X^*G_(Rperp)^(-1)X<=beta^2G_R`;
7. a rational `t` with `alpha<t<Gamma`;
8. the final floor from (L-18503.7).

This can be added to the existing inverse-Ritz checker without an eigensolver.

## 7. Proof boundary

- The abstract theorem is exact.
- The same-end local-Weyl theorem currently applies to graph-bounded shrinking
  packets; its hypotheses must be verified for the **harmonic lifts**, not only
  the unlifted endpoint profiles.
- The codimension gate must be checked for the declared complete low packet.
- If the harmonic lift develops an uncontrolled opposite-end or high-frequency
  component, (L-18503.21) does not follow.
- No production harmonic one-end certificate has yet been generated, so RH is
  not claimed.

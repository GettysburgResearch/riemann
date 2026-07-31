# L-18504 — Schatten trace sieve for the harmonic correction

Claim ID: `L-18504`  
Title: Only the large singular directions of the ambient harmonic response need be sacrificed  
Status: `PROPOSED`  
Authoring agent: `gpt56-02-p`  
Created: 2026-07-31  
Dependencies: Ky Fan/Markov eigenvalue counting; harmonic Schur complement; one-end local-Weyl floor  
Scope: production of the high subspace required by `L-18503`  
Related candidates: none

## 1. Abstract trace sieve

Let `W_0` be a finite-dimensional metric space with `G_0>0`. Let

\[
 B_0\succeq gG_0,
 \qquad
 H_0\succeq0,
 \qquad
 S_0=B_0-H_0.
 \tag{L-18504.1}
\]

Whiten by `G_0` and put

\[
 \Delta=\operatorname{Tr}
 \left(G_0^{-1/2}H_0G_0^{-1/2}\right).
 \tag{L-18504.2}
\]

For any `kappa>0`, let `E_kappa` be the spectral subspace of the whitened
`H_0` corresponding to eigenvalues strictly greater than `kappa`. Then

\[
 \boxed{\dim E_\kappa\le\Delta/\kappa.}
 \tag{L-18504.3}
\]

On

\[
 W_\kappa=G_0^{-1/2}E_\kappa^\perp
 \tag{L-18504.4}
\]

one has

\[
 \boxed{S_0|_{W_\kappa}\succeq(g-\kappa)G_0|_{W_\kappa}.}
 \tag{L-18504.5}
\]

### Proof

The positive eigenvalues `mu_j` of the whitened correction satisfy

\[
 \sum_j\mu_j=\Delta.
\]

Every eigenvalue in `E_kappa` exceeds `kappa`, proving (L-18504.3). On its
orthogonal complement the correction is at most `kappa I`; subtract this from
the floor `gI`. QED.

## 2. Codimension budget

Let `W_0 subset U` have codimension `q_0`, and let the radical rank be `r>=q_0`.
Write the available sacrifice slack as

\[
 s=r-q_0.
 \tag{L-18504.6}
\]

If

\[
 \boxed{\Delta<(s+1)\kappa,}
 \tag{L-18504.7}
\]

then (L-18504.3) gives `dim E_kappa<=s`, and hence

\[
 \boxed{\operatorname{codim}_U W_\kappa\le r.}
 \tag{L-18504.8}
\]

Therefore, whenever `kappa<g`, `W_kappa` is a valid sacrificial high subspace for
`L-18503`.

A convenient nearly optimal choice is

\[
 \kappa=\frac{\Delta}{s+1}+\varepsilon
 \tag{L-18504.9}
\]

with any rational `epsilon>0`. The retained Schur floor is

\[
 \boxed{
 g-\frac{\Delta}{s+1}-\varepsilon.}
 \tag{L-18504.10}
\]

## 3. No-slack corollary

If `q_0=r`, no additional direction may be discarded. Since a positive
operator has norm at most its trace,

\[
 H_0\preceq\Delta G_0.
\]

Thus directly

\[
 \boxed{S_0\succeq(g-\Delta)G_0.}
 \tag{L-18504.11}
\]

In particular a same-end floor `g_lambda~log R_lambda` survives the exact
harmonic lift whenever

\[
 \boxed{\Delta_\lambda=o(\log R_\lambda).}
 \tag{L-18504.12}
\]

No harmonic-lift profile theorem is then needed.

## 4. Harmonic correction identity

For the low/ambient block

\[
 \mathcal H=
 \begin{pmatrix}B&L^*\\L&C\end{pmatrix},
 \qquad C\succ0,
\]

the exact harmonic Schur form is

\[
 S_U=B-L^*C^{-1}L.
 \tag{L-18504.13}
\]

On a supplied packet `W_0` with basis map `J_0`, define

\[
 G_0=J_0^*G_UJ_0,
 \qquad
 H_0=J_0^*L^*C^{-1}LJ_0.
 \tag{L-18504.14}
\]

Then

\[
 \boxed{
 \Delta
 =\left\|
 C^{-1/2}LJ_0G_0^{-1/2}
 \right\|_{\mathfrak S_2}^2.}
 \tag{L-18504.15}
\]

Thus the trace sieve needs a Hilbert--Schmidt cross bound, not the operator norm
of the complete terminal-prime or harmonic-response matrix.

If `C>=hM`, a sufficient bound is

\[
 \boxed{
 \Delta
 \le h^{-1}
 \left\|
 M^{-1/2}LJ_0G_0^{-1/2}
 \right\|_{\mathfrak S_2}^2.}
 \tag{L-18504.16}
\]

Every quantity is a positive trace and admits exact finite or directed replay.

## 5. Same-end local-Weyl composition

Let `W_0` be one endpoint sector of the complete low packet. Suppose the
unlifted same-end form has the dimension-uniform floor

\[
 B|_{W_0}
 \succeq
 \left[
 \log R-O(1)-o(1)
 \right]G_0.
 \tag{L-18504.17}
\]

Opposite-end terminal-prime coupling does not occur in `B|W_0`. If

\[
 \frac{\Delta_\lambda}{s_\lambda+1}
 =o(\log R_\lambda),
 \tag{L-18504.18}
\]

then choose `kappa_lambda` by (L-18504.9). The resulting subspace has codimension
at most the radical rank and harmonic Schur floor

\[
 \boxed{
 \Gamma_\lambda
 =\log R_\lambda-O(1)
 -\frac{\Delta_\lambda}{s_\lambda+1}
 -o(1)>0.}
 \tag{L-18504.19}
\]

Cofinally `Gamma_lambda` may even tend to infinity.

Combining with `L-18503` yields

\[
 \lambda_{\min}(S_U,G_C)
 \ge-\alpha_\lambda
 -\frac{\beta_\lambda^2}{t-\alpha_\lambda}
 \longrightarrow0^-
 \tag{L-18504.20}
\]

for one fixed `t>0`, once the Gaussian radical compression/cross rates hold.

## 6. Relationship to plunge and Schatten estimates

The trace in (L-18504.15) measures the total ambient energy removed by harmonic
minimization from the chosen same-end packet. It is naturally controlled by
Schatten estimates for commutators and off-diagonal blocks of localization
operators. A bound on the number of plunge modes alone is insufficient, but a
Hilbert--Schmidt estimate converts directly into (L-18504.18).

This is the appropriate place to use recent pre-plunge/Schatten results: not to
bound the terminal-prime matrix itself, but to show that harmonic minimization
can destroy the local-Weyl floor on only a few sacrificial directions.

## 7. Exact finite certificate

A proof object needs:

1. exact/directed matrices `G_0`, `B_0`, `L_0`, and `C`;
2. a lower floor `B_0>=gG_0`;
3. an upper rational trace for `G_0^-1/2 L_0^*C^-1L_0 G_0^-1/2`;
4. the packet codimension `q_0`, radical rank `r`, and slack `s`;
5. a rational `kappa` with `Delta<(s+1)kappa< (s+1)g`;
6. the resulting high-subspace rank or a spectral-projector enclosure.

For a purely scalar proof, one may bypass construction of `W_kappa`: the trace
count itself, combined with min--max, certifies that a subspace of the required
dimension exists. A directed finite implementation may nevertheless freeze a
rational basis for independent replay.

## 8. Proof boundary

- The trace sieve is exact.
- A production proof still needs a source-bound Hilbert--Schmidt estimate for the
  actual harmonic cross map on the same-end packet.
- A trace bound in an unrelated metric or on an unlifted surrogate is
  insufficient.
- The newest localization/Schatten estimates must be translated with their exact
  constants and geometry before use.
- No production cofinal trace estimate has yet been supplied, so RH is not
  claimed.

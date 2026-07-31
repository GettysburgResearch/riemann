# L-15111 — A relative Weil–prolate transfer theorem for the corrected ratio

Claim ID: `L-15111`  
Status: **PROVED ABSTRACT TRANSFER; arithmetic trace-form hypotheses open**  
Authoring agent: `gpt56-pro-10`  
Created: 2026-07-31  
Dependencies: `L-15110`, audited `L-14302`, the radical-cluster audit `L-15106`  
Scope: exact remaining bridge from information-theoretic prolate geometry to the localized Weil form  
Related counterexample candidates: none

## 1. Purpose

`L-15110` proves the desired relative separation in the compressed-Fourier
model:

\[
 \frac{\text{0/4 constrained residual}}
      {\text{mode-8 constrained gap}}
 =O(\lambda^{-7}).
\]

This lemma states precisely what must be proved about the localized Weil form to
transport that decay to

\[
 B_{\lambda,N,\tau}/h_{\lambda,N,\tau}.
\]

It deliberately does not assume that the one-dimensional target complement is
the whole low-energy space. Any localized radical-like cluster must first be
captured in a finite block or quotient, as required by `L-15106`, PR #152, PR
#155, and PR #157.

## 2. Abstract transfer data

For each `lambda`, let the prolate source data be

\[
 (\mathcal H_\lambda,D_\lambda,t_\lambda,S_\lambda,
  \mu_{t,\lambda},g_{\rm pro,\lambda},B_{\rm pro,\lambda})
\]

from `L-15110`, where

\[
 g_{\rm pro,\lambda}
 =d_8\frac{A^2}{2\lambda}-\mu_t,
 \qquad
 B_{\rm pro,\lambda}
 =\|P_S(D-\mu_tI)t\|.
\]

Let `J_lambda` map the source target and its constrained complement into a local
Weil Hilbert space. Let `R_lambda` be a finite radical-like packet that has been
separated from the target, and let `V_lambda` be the remaining
`evaluation-visible` finite low block. Let `C_lambda` be the complete residual
complement after removing

\[
 \operatorname{span}\{J_\lambda t_\lambda\}
 \oplus R_\lambda\oplus V_\lambda.
\]

The finite or continuum local Weil form is denoted `q_lambda`, its target
Rayleigh upper endpoint is `U_lambda`, and its Hardy metric is `M_lambda`.

Assume the following uniform inequalities.

### A. Hardy metric comparability on the transported prolate complement

There are positive `m_-(lambda),m_+(lambda)` such that

\[
 m_-\|x\|^2
 \le\|J_\lambda x\|_{M_\lambda}^2
 \le m_+\|x\|^2
 \qquad(x\in S_\lambda).
 \tag{L-15111.1}
\]

### B. Corrected residual transfer

The actual target residual, after projecting away all retained low blocks,
satisfies

\[
 \boxed{
 B_{\rm Weil,\lambda}
 \le C_B(\lambda)B_{\rm pro,\lambda}
     +\varepsilon_B(\lambda).}
 \tag{L-15111.2}
\]

This is where the correlated cancellation `A c_lambda-b_lambda` must be retained;
separate absolute estimates are not sufficient.

### C. Relative form lower comparison

For every `x in S_lambda`,

\[
 \boxed{
 q_\lambda(J_\lambda x,J_\lambda x)
 -U_\lambda\|J_\lambda x\|^2
 \ge C_H(\lambda)
       \langle(D_\lambda-\mu_{t,\lambda}I)x,x\rangle
      -\varepsilon_H(\lambda)\|x\|^2.}
 \tag{L-15111.3}
\]

### D. Remaining blocks

The directly certified visible block, the radical-like block after its internal
Schur correction, and the infinite complement `C_lambda` all have Hardy
coercivity at least the bound obtained below. Every cross map is included in one
block Temple--Schur correction rather than discarded.

## 3. Transferred coercivity and ratio

If

\[
 C_Hg_{\rm pro}>\varepsilon_H,
\]

then the complete actual complement coercivity may be taken as

\[
 \boxed{
 h_{\rm Weil,\lambda}
 \ge\frac{C_H(\lambda)g_{\rm pro,\lambda}
             -\varepsilon_H(\lambda)}
            {m_+(\lambda)}.}
 \tag{L-15111.4}
\]

Consequently

\[
 \boxed{
 \frac{B_{\rm Weil,\lambda}}
      {h_{\rm Weil,\lambda}}
 \le
 \frac{m_+(\lambda)
       [C_B(\lambda)B_{\rm pro,\lambda}
        +\varepsilon_B(\lambda)]}
      {C_H(\lambda)g_{\rm pro,\lambda}
        -\varepsilon_H(\lambda)}.}
 \tag{L-15111.5}
\]

### Proof

By `L-15110`, the centered prolate form on `S_lambda` is at least
`g_pro||x||^2`. Insert this in (L-15111.3), then use the upper metric comparison
in (L-15111.1):

\[
 q(Jx,Jx)-U\|Jx\|^2
 \ge(C_Hg_{\rm pro}-\varepsilon_H)\|x\|^2
 \ge\frac{C_Hg_{\rm pro}-\varepsilon_H}{m_+}
      \|Jx\|_M^2.
\]

Assumption D extends this floor to the complete complement after the exact
block Schur correction. This proves (L-15111.4). Combine with
(L-15111.2) to obtain (L-15111.5). QED.

## 4. Polynomial-budget corollary

Suppose

\[
 \frac{m_+(\lambda)C_B(\lambda)}{C_H(\lambda)}
 =O(\lambda^r),
 \qquad r<7,
 \tag{L-15111.6}
\]

and

\[
 \varepsilon_B
 =o\!\left(
   \frac{C_H}{m_+}g_{\rm pro}\right),
 \qquad
 \varepsilon_H=o(C_Hg_{\rm pro}).
 \tag{L-15111.7}
\]

Then `L-15110` gives

\[
 \boxed{
 \frac{B_{\rm Weil,\lambda}}
      {h_{\rm Weil,\lambda}}
 =O(\lambda^{r-7})+o(1)
 \longrightarrow0.}
 \tag{L-15111.8}
\]

The exact prolate theorem therefore supplies **seven powers of allowable
polynomial loss** in transferring to the Weil and Hardy geometries.

## 5. Strong operator form sufficient for A--C

A convenient, stronger but directly auditable hypothesis is a relative Loewner
comparison on `span{t_lambda} plus S_lambda`:

\[
 \left|
 q_\lambda(Jx,Jy)
 -\beta_\lambda\langle Jx,Jy\rangle
 -\kappa_\lambda\langle D_\lambda x,y\rangle
 \right|
 \le\delta_\lambda\|x\|\|y\|.
 \tag{L-15111.9}
\]

Together with a target-Rayleigh enclosure and the metric comparison, this gives

\[
 C_H=\kappa_\lambda,
 \qquad
 \varepsilon_H=O(\delta_\lambda),
 \qquad
 \varepsilon_B=O(\delta_\lambda/\sqrt{m_-}).
\]

Thus it is sufficient to prove

\[
 \boxed{
 \delta_\lambda=o(d_8(\lambda)/\lambda)}
 \tag{L-15111.10}
\]

on the correctly captured low packet and constrained complement, with
polynomially controlled metric constants.

This is the exact form of the missing relative trace theorem. The
Connes--Consani archimedean trace formula motivates such a comparison by
expressing a Weil/trace discrepancy through prolate functions. It does not, as
currently imported, supply the semilocal uniform estimate (L-15111.10).

## 6. Radical-cluster and evaluation-visible gates

The transfer fails if one simply declares mode `8` to be the next actual Weil
direction. The global Weil radical is infinite dimensional, and its localized
truncations produce an arbitrarily long near-zero Ritz cluster. In addition,
PR #157 proves that a generic evaluation-visible direction cannot be uniformly
approximated by small-tail radical truncations because every exact radical
transform vanishes at certified zeta zeros.

Therefore a valid production decomposition is

```text
complete low-symbol packet
  = radical-like zero-evaluation near-kernel R_lambda
    + evaluation-visible block V_lambda,
```

followed by:

1. exact radical-tail control on `R_lambda`;
2. direct finite lower certification on `V_lambda`;
3. packet-leverage control of the infinite complement;
4. one block Temple--Schur composition;
5. the prolate relative comparison only on the residual constrained packet.

## 7. Proof boundary

This lemma proves the transfer algebra. It does not establish:

- the relative Loewner comparison (L-15111.9);
- the error scale (L-15111.10);
- a production radical/visible packet decomposition;
- a cofinal finite lower certificate;
- RH.

It identifies the precise literature-level theorem now worth proving. More
finite eigenvalue matching, without a directed relative form envelope, does not
advance (L-15111.10).

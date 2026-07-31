# L-18501 — Sacrificial-subspace harmonic count

Claim ID: `L-18501`  
Title: A high-frame subspace of the right codimension proves the sharp harmonic evaluation count without an angle theorem  
Status: `PROPOSED`  
Authoring agent: `gpt56-02-p`  
Created: 2026-07-31  
Dependencies: Courant--Fischer; Sylvester inertia; the harmonic-lift metric and certified-zero Gram of the three-block program  
Scope: the final integer gate in Issue #156  
Related candidates: none

## 1. Abstract count theorem

Let `U` be an `n`-dimensional real or complex vector space. Let

\[
 G\succ0,
 \qquad K\succeq0
 \tag{L-18501.1}
\]

be Hermitian forms, and define

\[
 A=G^{-1/2}KG^{-1/2}.
 \tag{L-18501.2}
\]

For a real threshold `tau`, write

\[
 N_A(\tau)=\dim\operatorname{Ran}1_{(-\infty,\tau)}(A),
 \tag{L-18501.3}
\]

counting multiplicity. Let `r` be a nonnegative integer.

Suppose there exists a subspace `W subset U` such that

\[
 \boxed{\operatorname{codim}_U W\le r}
 \tag{L-18501.4}
\]

and

\[
 \boxed{K|_W\succeq\tau G|_W.}
 \tag{L-18501.5}
\]

Then

\[
 \boxed{N_A(\tau)\le r.}
 \tag{L-18501.6}
\]

The witness `W` need not be the metric orthogonal complement of the proposed
radical packet, and it need not have any controlled angle with that packet.

### Proof

Let `q=n-r`. Equation (L-18501.4) gives `dim W>=q`. Choose a
`q`-dimensional subspace `W_0 subset W`. Every nonzero vector of `W_0` has
generalized Rayleigh quotient at least `tau` by (L-18501.5). Courant--Fischer
therefore gives

\[
 \lambda_{r+1}(A)\ge\tau,
\]

where eigenvalues are listed increasingly. Hence fewer than `r+1` eigenvalues
lie below `tau`, proving (L-18501.6). QED.

## 2. Exact saturation and automatic principal-angle estimate

Let `R subset U` have dimension exactly `r`, and suppose

\[
 \boxed{K|_R\preceq\epsilon G|_R,
 \qquad 0\le\epsilon<\tau.}
 \tag{L-18501.7}
\]

Then min--max gives `N_A(tau)>=r`, while (L-18501.6) gives the reverse
inequality. Thus

\[
 \boxed{N_A(\tau)=r.}
 \tag{L-18501.8}
\]

Let

\[
 N=\operatorname{Ran}1_{[0,\tau)}(A).
\]

For `u in G^(1/2)R`, decompose `u=P_Nu+P_(N^perp)u`. Since `A>=tau` on
`N^perp`,

\[
 \tau\|P_{N^\perp}u\|^2
 \le\langle Au,u\rangle
 \le\epsilon\|u\|^2.
\]

Consequently

\[
 \boxed{
 \|P_{N^\perp}P_{G^{1/2}R}\|^2
 \le\frac\epsilon\tau.}
 \tag{L-18501.9}
\]

This is exactly the principal-angle conclusion needed by the counted harmonic
transfer. It follows after the count and is not an input.

## 3. Application to the harmonic lift

At support `lambda`, let

\[
 J_\lambda u=(u,-C_\lambda^{-1}L_\lambda u),
\]

and define

\[
 G_{C,\lambda}=J_\lambda^*G_\lambda J_\lambda,
 \qquad
 K_{T,\lambda}^C=J_\lambda^*K_{T,\lambda}J_\lambda.
 \tag{L-18501.10}
\]

Put

\[
 \tau_\lambda=B_{T,\lambda}+\beta_\lambda.
 \tag{L-18501.11}
\]

The sharp count

\[
 N_{G_{C,\lambda}^{-1/2}K_{T,\lambda}^C
      G_{C,\lambda}^{-1/2}}(\tau_\lambda)
 \le\dim R_\lambda
 \tag{L-18501.12}
\]

is proved as soon as one exhibits **any** subspace `W_lambda subset U_lambda`
with

\[
 \boxed{
 \operatorname{codim}_{U_\lambda}W_\lambda
 \le\dim R_\lambda}
 \tag{L-18501.13}
\]

and

\[
 \boxed{
 K_{T,\lambda}^C|_{W_\lambda}
 \succeq
 (B_{T,\lambda}+\beta_\lambda)
 G_{C,\lambda}|_{W_\lambda}.}
 \tag{L-18501.14}
\]

This is weaker than proving the visible floor directly on
`R_lambda^(perp_GC)`. Cross terms between `W_lambda` and its complement are
irrelevant to the count.

## 4. One-sided endpoint sacrifice

Suppose the complete harmonic low packet contains a one-end profile packet
`W_lambda` and that discarding the opposite-end/source block costs at most the
radical rank:

\[
 \operatorname{codim}_{U_\lambda}W_\lambda
 \le\dim R_\lambda.
 \tag{L-18501.15}
\]

Then only a same-end certified-zero frame is needed on `W_lambda`. The
opposite-end terminal-prime Hankel matrix, and every cross term between the two
ends, disappear from the min--max witness. They may still be present in the
operator, but cannot create more than the sacrificed codimension many low
harmonic-evaluation eigenvalues.

This is the main structural escape from the terminal-prime norm gate: the count
requires a large subspace with a frame floor, not a frame floor on the particular
orthogonal complement selected after the radical split.

## 5. Fixed-codimension source-corrector packet

Let a source packet `P` have dimension `d`, let

\[
 \ell:H_{src}\to\mathbb C^q
\]

be the exact source-constraint map, and let `Q:C^q->H_src` satisfy

\[
 \ell Q=I,
 \qquad \operatorname{Ran}Q\cap P=\{0\}.
 \tag{L-18501.16}
\]

Define

\[
 \mathcal R=(I-Q\ell)|_P,
 \qquad
 U^{src}=P\oplus\operatorname{Ran}Q,
 \qquad
 R^{src}=\mathcal R(P).
 \tag{L-18501.17}
\]

Then `mathcal R` is injective whenever `P intersect Ran Q={0}`, and

\[
 \dim R^{src}=d,
 \qquad
 \dim U^{src}=d+q.
 \tag{L-18501.18}
\]

The corrector space `Ran Q` has dimension `q=codim R^(src)`. After any
injective localized/harmonic map, it is therefore an admissible sacrificial
witness `W` for (L-18501.4). The entire growing count is reduced to a fixed
`q x q` generalized frame inequality on the external correctors.

For the self-dual Hermite repair

\[
 P_m=\operatorname{span}\{h_4,h_8,\ldots,h_{4m}\},
 \qquad
 Qc=c\,h_0/h_0(0),
 \tag{L-18501.19}
\]

there is one source constraint, so `q=1`. The repaired sources are

\[
 h_{4j}-\frac{h_{4j}(0)}{h_0(0)}h_0,
\]

and the harmonic count is reduced to one directed corrector Rayleigh quotient.

## 6. Exact finite certificate

Let `B_W` be a full-column-rank rational basis for `W`. A proof object checks

\[
 B_W^*(K-\tau G)B_W\succeq0
 \tag{L-18501.20}
\]

by exact or directed `LDL*`, together with

\[
 n-\operatorname{rank}B_W\le r.
 \tag{L-18501.21}
\]

If a radical basis `B_R` is supplied, the automatic-angle gate additionally
checks

\[
 B_R^*(\epsilon G-K)B_R\succeq0,
 \qquad \epsilon<\tau.
 \tag{L-18501.22}
\]

No eigensolver, SVD, or principal-angle computation is part of the proof.
`X-18501` implements this exact arithmetic.

## 7. Proof boundary

- The abstract theorem and source-corrector dimension algebra are exact.
- A one-end or external-corrector packet must actually lie inside the declared
  complete harmonic low packet.
- Its directed selected-zero frame floor must exceed the complete omitted-zero
  threshold.
- Ordinary packet dimension without (L-18501.5) remains insufficient, in
  agreement with `R-15601`.
- This lemma does not by itself prove the zeta-specific cofinal frame estimate or
  RH.

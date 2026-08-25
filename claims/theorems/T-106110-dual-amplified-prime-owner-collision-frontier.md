# T-106110 — Dual-amplified prime-owner collision frontier

Claim ID: `T-106110`  
Programme aliases: `LFAM1.DUAL_AMPLIFIED_REPAIR`, `LFAM2.PRIME_OWNER_COLLISION_FRONTIER`, `STRESS.BOOLEAN_ROUGH_TAIL_TRACE_FORM`  
Status: **MAJOR UNCONDITIONAL FULL REPAIR OF THE T-106090 NORMAL FORM; TWO HYBRID MOMENTS OPEN**  
Created: 2026-08-25  
Depends on: `R-106110`; `L-106110--L-106113`; retained `L-106090--L-106093`; parent PR #719 at `ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc`, especially `L-102951--L-102963`, `T-102990`  
Programme issues: #743, #736, #737  
RH status: **unproved**

The least-discrepancy programme has now passed two source-level audits.

1. The left anchor must be summed before the family square (`R-106090`).
2. The opposite semiprime-owner fibres must also be summed before the family
   square (`R-106110`).

This theorem records the fully repaired two-sided normal form.

## 1. Inherited Boolean incidence spine

At the locked parent head:

```text
critical Hodge class = native squarefree Boolean source      PROVED;
Boolean Type-I global transport                              PROVED;
equal/one-sided reduced cores and terminal sectors           CLOSED;
exceptional balanced-owner sector                            EMPTY COFINALLY;
literal-product phase packing with arbitrary masks           PROVED;
canonical equal-pair owner gauge                              PROVED;
owner and phase gauges                                        DECOUPLED;
BCI102990 coprime two-sided Boolean incidence                 OPEN.
```

The exact least-discrepancy partition of `L-106090` writes every live pair as

\[
 N=P g^2c^2,
 \qquad
 M=Q g^2d^2,
 \qquad
 (c,d)=1,
 \qquad
 \ell=P^-(c)<P^-(d),
\]

with one nonzero phase modulo `ell` and an `ell`-rough opposite core.

## 2. Binding correction to the first T-106090 moment

The Q-fixed moment of the first `T-106090` used external weight `g^2 ell Q`.
It remains a formally sufficient but unnecessarily strong condition if proved
in full.  `R-106110` shows that its claimed diagonal closure was false: the
factor `Q` cancels the literal `1/Q` owner energy and leaves the number of
opposite-owner fibres.

Therefore:

```text
first L-106094 same-anchor diagonal claim          WITHDRAWN;
first LDRPCX/LDRNEX distinct-anchor-only gates      SUPERSEDED;
Q-fixed fibre moment                                 NON-NORMATIVE OVERSTRONG ROUTE.
```

## 3. Complete dual amplification

For fixed `(g,ell,sigma,t)`, sum both the left anchors and all opposite-owner
fibres before squaring:

\[
 \mathcal Z_{g,\ell,\sigma,h}(t)
 =
 \sum_{\alpha,Q}
 \overline{A_\alpha(t)}
 B_{\alpha,Q,\sigma,h}(t).
\tag{T-106110.1}
\]

Here `sigma=kappa_ell(Q)` and every literal `Q^{-1/2}` coefficient remains
inside `B`.  `L-106110` proves the exact family identity

\[
\boxed{
\begin{aligned}
 \sum_{h=1}^{\ell-1}|\mathcal Z_h|^2
={}&{\ell+1\over\ell-1}|\mathcal Z_1|^2
 +{2\ell\over\ell-1}
 \sum_{\substack{\eta(-1)=1\\\eta\ne1}}|\mathcal Z_\eta|^2,
\end{aligned}
}
\tag{T-106110.2}
\]

and the principal recombination

\[
 \sum_{h=1}^{\ell-1}\mathcal Z_h=-\mathcal Z_0.
\tag{T-106110.3}
\]

## 4. Correct controlling moment

Define

\[
\boxed{
\begin{aligned}
 \mathfrak M_{\rm DA}(Y)
 ={1\over2\pi}
 \sum_{g,\ell}g^2\ell
 \sum_{\sigma=\pm1}
 \int |\widehat\kappa(t)|^2
 \Bigg[&{\ell+1\over\ell-1}|\mathcal Z_1(t)|^2\\
 &+{2\ell\over\ell-1}
 \sum_{\substack{\eta(-1)=1\\\eta\ne1}}
 |\mathcal Z_\eta(t)|^2\Bigg]dt.
\end{aligned}
}
\tag{T-106110.4}
\]

The source-dual weight is

\[
 \boxed{g^2\ell,}
\]

not `g^2 ell Q`.  Since

\[
 \sum_{g,\ell}{1\over g^2\ell}
 \ll\log\log(3Y),
\]

`L-106111` proves

\[
\boxed{
 \mathfrak M_{\rm DA}(Y)=Y^{o(1)}
 \Longrightarrow
 \mathrm{BCI}_{102990}
 \Longrightarrow
 \mathrm{RH}.
}
\tag{T-106110.5}
\]

The last implication is the frozen parent detector/Mellin consumer.

## 5. Diagonal and owner algebra

`L-106112` proves

\[
\boxed{
 \mathfrak M_{\rm DA}^{\rm atomic\ diagonal}(Y)=Y^{o(1)}.
}
\tag{T-106110.6}
\]

Only exact equality of the complete source atom is included in this diagonal.
All other correlations remain until independently removed.

In the canonical equal-pair gauge, the complete opposite semiprime-owner
amplifier has the exact Wick form

\[
\boxed{
 \sum_{p<q}{\chi(pq)\over(pq)^s}
 ={1\over2}
 \left[
  \left(\sum_p{\chi(p)\over p^s}\right)^2
  -\sum_p{\chi(p)^2\over p^{2s}}
 \right],
}
\tag{T-106110.7}
\]

with owner/core exclusions and shell projections retained linearly.  The
second term is in the closed repeated-prime ledger.  Thus the genuine owner
coherence is a fourth moment of one explicit prime Dirichlet polynomial.

## 6. Exact remaining gates

Because (T-106110.4) is positive, separate it into:

```text
DAPRO106110:
  after removal of the literal atomic/equal-product/repeated-prime diagonal,
  the complete dual-amplified principal/quadratic-root prime-Wick moment is
  Y^o(1);

DAKUM106110:
  the complete dual-amplified nonprincipal even-character prime-Wick moment,
  restricted to strict product congruences, is Y^o(1).
```

`L-106113` identifies the nonprincipal gate exactly with

\[
 p_1p_2\equiv\pm p_3p_4\pmod\ell,
 \qquad
 p_1p_2\ne p_3p_4,
\tag{T-106110.8}
\]

with all Boolean-core, roughness, least-discrepancy and physical-shell masks
retained.  The equal-product and repeated-prime components are already closed.

The conjunction is exact:

\[
\boxed{
 \mathrm{DAPRO}_{106110}
 \wedge
 \mathrm{DAKUM}_{106110}
 \Longrightarrow
 \mathfrak M_{\rm DA}(Y)=Y^{o(1)}
 \Longrightarrow
 \mathrm{BCI}_{102990}
 \Longrightarrow
 \mathrm{RH}.
}
\tag{T-106110.9}
\]

Neither first premise is proved.

## 7. Function-field and trace-formula target

Define

```text
FFDA106110:
  over F_q[T], construct the dual-amplified least-discrepancy family with the
  complete opposite-owner sum inside each Kummer/Artin--Schreier member;
  identify the prime-product collision sheaf;
  remove every geometrically constant, equal-product, quadratic-root and
  shared-incidence constituent;
  prove the remaining trace moment and export one explicit number-field
  exponential-sum or relative-trace-formula theorem.
```

Known function-field RH is not itself the transfer.  The desired output is the
geometry of the strict product-collision components and an individualization
mechanism for the principal channel.

## 8. Exact scientific boundary

```text
Boolean/Hodge source and Type-I                         INHERITED PROVED
cofinal equal-pair Boolean incidence normal form        INHERITED PROVED
least-discrepancy triangular partition                  PROVED EXACT
strict rough-tail family at fixed fibre                 PROVED EXACT
left-anchor amplification                               PROVED EXACT
Q-fixed diagonal closure                                REFUTED
complete opposite-owner amplification                   PROVED EXACT
dual-amplified family identity                          PROVED EXACT
correct source-dual weight g^2 ell                      PROVED EXACT
atomic diagonal                                         PROVED SUBPOWER
semiprime owner = prime Wick square minus diagonal      PROVED EXACT
nonprincipal fourth moment = strict product collisions  PROVED EXACT
DAPRO106110 / DAKUM106110                               OPEN
BCI102990                                               OPEN / RH-BEARING
Riemann Hypothesis                                      UNPROVED
```

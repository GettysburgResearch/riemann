# T-106120 — Bilateral Kummer prime-Wick tensor frontier

Claim ID: `T-106120`  
Programme aliases: `LFAM1.BILATERAL_FULL_REPAIR`, `LFAM2.DOUBLE_KUMMER_OWNER_TENSOR`, `STRESS.COPRIME_BOOLEAN_TRACE_FRONTIER`  
Status: **PREFERRED SOURCE-SYMMETRIC REPAIR OF BCI102990; THREE EXPLICIT MOMENTS OPEN**  
Created: 2026-08-25  
Depends on: `L-106120--L-106122`; `T-106110`; parent PR #719 at `ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc`, `T-102990`  
Programme issues: #743, #736, #737  
RH status: **unproved**

`T-106110` repairs the least-discrepancy programme by amplifying both source
dimensions before one family square.  It remains asymmetric: only the rough
tail receives a nonzero phase transform.

The coprime Boolean packet contains a second canonical internal prime.  This
theorem uses both and produces the source-symmetric preferred frontier.

## 1. Exact bilateral source coordinate

Every live pair has

\[
 N=P g^2c^2,
 \qquad
 M=Q g^2d^2,
 \qquad
 c,d>1,
 \qquad
 (c,d)=1.
\]

Put

\[
 \ell=P^-(c),
 \qquad
 \rho=P^-(d).
\]

Then `ell!=rho`, `ell` divides only `N`, and `rho` divides only `M`.  The exact
same-occurrence phase identity is

\[
\boxed{
 1=
 \sum_{h=1}^{\ell-1}
 \sum_{k=1}^{\rho-1}
 e_\ell(h(N-M))e_\rho(k(N-M)).
}
\tag{T-106120.1}
\]

Both complete semiprime-owner sums, both reduced-core sums and all source
incidence labels are assembled before squaring.

## 2. Exact tensor family

After splitting the two owner quadratic classes, the complete member is

\[
 \mathcal W_{g,\ell,\rho,\sigma,\tau,h,k}(t)
 =
 \sum_{P,Q,c,d}
 \overline{A_{P,c}(t)}B_{Q,d}(t)
 e_\ell(-hQd^2)e_\rho(kPc^2).
\]

For even characters `eta` modulo `ell` and `theta` modulo `rho`, define the
weights

\[
 w_q(1)={q+1\over q-1},
 \qquad
 w_q(\vartheta)={2q\over q-1}\quad(\vartheta\ne1).
\]

`L-106120` proves

\[
\boxed{
 \sum_{h\ne0}\sum_{k\ne0}|\mathcal W_{h,k}|^2
 =
 \sum_{\eta,\theta}
 w_\ell(\eta)w_\rho(\theta)
 |\mathcal W_{\eta,\theta}|^2
}
\tag{T-106120.2}
\]

and

\[
 \sum_{h\ne0}\sum_{k\ne0}\mathcal W_{h,k}
 =\mathcal W_{0,0}.
\tag{T-106120.3}
\]

Thus the native Boolean incidence current is exactly the
principal--principal member of the complete tensor family.

## 3. Correct source-dual moment

Define

\[
\boxed{
\begin{aligned}
 \mathfrak M_{\rm BT}(Y)
 ={1\over2\pi}
 \sum_g\sum_{\ell\ne\rho}g^2\ell\rho
 \sum_{\sigma,\tau}
 \int |\widehat\kappa(t)|^2
 \sum_{\eta,\theta}
 w_\ell(\eta)w_\rho(\theta)
 |\mathcal W_{\eta,\theta}(t)|^2dt.
\end{aligned}
}
\tag{T-106120.4}
\]

No owner product is placed outside the square.  The reciprocal source-dual
mass is

\[
 \sum_g{1\over g^2}
 \sum_{\ell\ne\rho}{1\over\ell\rho}
 \ll(\log\log(3Y))^2.
\]

Therefore

\[
\boxed{
 \mathfrak M_{\rm BT}(Y)=Y^{o(1)}
 \Longrightarrow
 \mathrm{BCI}_{102990}
 \Longrightarrow
 \mathrm{RH}.
}
\tag{T-106120.5}
\]

## 4. Paid diagonal and exact prime-owner algebra

`L-106121` proves

\[
\boxed{
 \mathfrak M_{\rm BT}^{\rm atomic\ diagonal}(Y)=Y^{o(1)}.
}
\tag{T-106120.6}
\]

In each source side, the canonical equal-pair semiprime owner field is

\[
 {1\over2}
 \left[
  \mathcal P_\chi(s)^2-\mathcal D_\chi(s)
 \right].
\]

Both diagonal polynomials `mathcal D` are in the inherited repeated-prime
ledger.  Modulo closed fields, one tensor member is therefore the product of
two one-prime Wick squares.

## 5. Exact remaining tensor channels

`L-106122` gives the positive split:

```text
BTPP106122:
  off-atomic principal--principal prime-Wick tensor moment;

BTPN106122:
  the two mixed principal/nonprincipal product-collision moments;

BTNN106122:
  the strict double nonprincipal product-collision moment.
```

The strict double collision is

\[
\begin{aligned}
&p_1p_2\equiv\pm p_3p_4\pmod\rho,
&&p_1p_2\ne p_3p_4,\\
&q_1q_2\equiv\pm q_3q_4\pmod\ell,
&&q_1q_2\ne q_3q_4,
\end{aligned}
\tag{T-106120.7}
\]

with every Boolean-core, least-prime, shell, marked-prime and clean-incidence
mask retained.

The exact conjunction is

\[
\boxed{
 \mathrm{BTPP}_{106122}
 \wedge
 \mathrm{BTPN}_{106122}
 \wedge
 \mathrm{BTNN}_{106122}
 \Longrightarrow
 \mathfrak M_{\rm BT}(Y)=Y^{o(1)}
 \Longrightarrow
 \mathrm{BCI}_{102990}
 \Longrightarrow
 \mathrm{RH}.
}
\tag{T-106120.8}

None of the three first premises is proved.

## 6. Relation to earlier frontiers

```text
HQORO106071:
  finite-residue owner crowding after a scale-matched auxiliary collapse;

MOBOSM106081:
  minimum-owner selector-tied phase moment;

T-106110:
  one-phase dual-amplified least-discrepancy family;

T-106120:
  two-phase, two-owner, source-symmetric tensor family before any auxiliary
  residue collapse.
```

`T-106120` is preferred because it transforms both reduced-core directions and
retains all owner coherence inside one positive family object.  It does not
claim the older frontiers are false; it supplies a cleaner equivalent
sufficient coordinate.

## 7. Function-field programme

Define

```text
FFBT106120:
  construct the two-sided Artin--Schreier/Kummer tensor over F_q[T];
  identify the two prime-product multiplication sheaves;
  remove equal-product, quadratic-root, repeated-label and shared-incidence
  constituents;
  prove the mixed and double-nonprincipal trace moments;
  determine what geometric or trace-formula mechanism can individualize the
  principal--principal member over the integers.
```

The family geometry, not function-field RH by itself, is the desired export.

## 8. Current boundary

```text
bilateral least-prime source partition                 PROVED EXACT
double nonzero same-occurrence phases                  PROVED EXACT
complete two-sided amplification                       PROVED EXACT
tensor Gauss/even-character identity                   PROVED EXACT
correct source-dual weight g^2 ell rho                 PROVED EXACT
atomic diagonal                                        PROVED SUBPOWER
both semiprime owners factor as prime Wick squares     PROVED EXACT
mixed/squared collision varieties                      PROVED EXACT
BTPP106122 / BTPN106122 / BTNN106122                  OPEN
BCI102990                                               OPEN / RH-BEARING
Riemann Hypothesis                                      UNPROVEN
```

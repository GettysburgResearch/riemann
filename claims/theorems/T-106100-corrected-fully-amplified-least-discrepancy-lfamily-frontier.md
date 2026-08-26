# T-106100 — Corrected fully amplified least-discrepancy L-family frontier

Claim ID: `T-106100`  
Programme aliases: `LFAM1.FULL_REPAIR_FRONTIER`, `LFAM2.ANCHOR_OWNER_ROUGH_TAIL_MOMENT`, `STRESS.CORRECTED_BOOLEAN_CORE_FAMILY`  
Status: **BINDING CORRECTED NORMAL FORM; OFF-DIAGONAL HYBRID MOMENTS OPEN**  
Created: 2026-08-25  
Depends on: `L-106090--L-106092`, `R-106090`, `R-106095`, `L-106095--L-106096`; parent PR #719 at `ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc`, `T-102990`  
Programme issues: #743, #736, #737  
RH status: **unproved**

`R-106095` corrects the first `T-106090` moment: the opposite owner product
\(Q\) must be aggregated inside the family amplitude, not separated and paid
by a scalar Cauchy weight.

All prior exact source reductions remain:

```text
Boolean Type-I and closed core sectors       inherited closed;
least-discrepancy orientation                proved exact;
opposite core strictly rough                 proved exact;
fixed-Q local even-character frame           proved exact;
fixed-Q local phase energy                    proved long-core.
```

## 1. Correct fully amplified family

For fixed \(g,\ell,\sigma\), `L-106095` defines

\[
\widetilde Z_{g,\ell,\sigma,h}(t)
=
\sum_{\alpha:g_\alpha=g,\ell_\alpha=\ell}
\overline{A_\alpha(t)}
\sum_{\substack{Q,d,\ldots\\
P^-(d)>\ell,\ (d,c_\alpha)=1\\
\kappa_\ell(Qg^2)=\sigma}}
b_{Q,d,\ldots}(t)e_\ell(-hQg^2d^2).
\tag{T-106100.1}
\]

Both coherent dimensions are inside the amplitude before squaring:

```text
left anchors (c,P,...);
opposite owner/core atoms (Q,d,...).
```

The exact even-character identity is

\[
\boxed{
\sum_{h\ne0}|\widetilde Z_{g,\ell,\sigma,h}|^2
=
{\ell+1\over\ell-1}
|\widetilde Z_{g,\ell,\sigma,1}|^2
+
{2\ell\over\ell-1}
\sum_{\substack{\eta(-1)=1\\\eta\ne1}}
|\widetilde Z_{g,\ell,\sigma,\eta}|^2.
}
\tag{T-106100.2}
\]

## 2. Correct moment and exact implication

Define

\[
\begin{aligned}
\widetilde{\mathfrak M}_{\rm LDRT}(Y)
={1\over2\pi}
\sum_{g,\ell}g^2\ell
\sum_{\sigma=\pm1}
\int |\widehat\kappa(t)|^2
\Bigg[
&{\ell+1\over\ell-1}
|\widetilde Z_{g,\ell,\sigma,1}(t)|^2\\
&+{2\ell\over\ell-1}
\sum_{\substack{\eta(-1)=1\\\eta\ne1}}
|\widetilde Z_{g,\ell,\sigma,\eta}(t)|^2
\Bigg]dt .
\end{aligned}
\tag{T-106100.3}
\]

The dual sum

\[
\sum_{g,\ell}(g^2\ell)^{-1}
\]

is polylogarithmic.  Thus

\[
\boxed{
\widetilde{\mathfrak M}_{\rm LDRT}(Y)=Y^{o(1)}
\Longrightarrow
\mathrm{LDART}_{106090}
\Longrightarrow
\mathrm{BCI}_{102990}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-106100.4}
\]

## 3. Atomic diagonal removed

`L-106096` proves

\[
\boxed{
\widetilde{\mathfrak M}_{\rm LDRT}^{\rm literal\ atomic\ diagonal}(Y)
=
Y^{o(1)}.
}
\tag{T-106100.5}
\]

Only genuine cross-incidence terms remain.

Define

```text
FAPCX106100:
  the off-atomic-diagonal principal part of the fully amplified moment is
  Y^o(1);

FANEX106100:
  the off-atomic-diagonal nonprincipal even-family part is Y^o(1).
```

Because the moment is positive,

\[
\boxed{
\mathrm{FAPCX}_{106100}
\wedge
\mathrm{FANEX}_{106100}
\Longrightarrow
\widetilde{\mathfrak M}_{\rm LDRT}=Y^{o(1)}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-106100.6}
\]

This is the corrected two-statement conjunction.

## 4. Function-field programme

The corrected mirror must sum both owner and core variables inside one trace
function before taking the family square:

```text
FFFA106100:
  prove the off-diagonal fully amplified Artin--Schreier/Kummer moment,
  with the common-core and least-discrepancy filtrations retained, classify
  constant/resonant constituents, and export the corresponding number-field
  trace or exponential-sum theorem.
```

A fixed-\(Q\) function-field estimate is only a local input and does not close
the corrected moment.

## 5. Binding status

```text
R-106095 opposite-owner dimension correction       BINDING
L-106095 fully amplified family normal form         PROVED EXACT
L-106096 literal atomic diagonal                    PROVED SUBPOWER
FAPCX106100 principal off-diagonal moment            OPEN
FANEX106100 nonprincipal off-diagonal moment         OPEN
BCI102990                                            OPEN / RH-BEARING
Riemann Hypothesis                                   UNPROVEN
```

The unresolved object is now strictly off-diagonal in the complete
anchor/opposite-owner incidence graph.  No local conductor, diagonal or
source-order ambiguity remains.

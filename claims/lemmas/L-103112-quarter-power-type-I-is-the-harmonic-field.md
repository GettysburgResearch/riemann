# L-103112 — The complete quarter-power Type-I lift is exactly the harmonic field

Claim ID: `L-103112`  
Status: **PROVED EXACT SOURCE EQUIVALENCE; ESTIMATE OPEN**  
Created: 2026-08-26  
Depends on: `L-103111`; Boolean Vaughan identity; canonical equal-pair functor  
RH status: **unproved**

Let `E_P` be the canonical equal-pair lift in one labelled owner fibre `P`, and
let `Pi_A` retain `A<=P<2A`. On the dyadic physical block choose

\[
V_A=\left\lfloor(2Y/A)^{1/4}\right\rfloor.
\]

The Boolean identity is

\[
\mu_{\rm sf}=\mathcal T_{V_A}+\mathcal B_{V_A}.
\]

Since `E_P` and `Pi_A` are linear source functors,

\[
\Pi_AE_P\mu_{\rm sf}
=
\Pi_AE_P\mathcal T_{V_A}
+
\Pi_AE_P\mathcal B_{V_A}.
\tag{L-103112.1}
\]

`L-103111` proves that the fixed physical observation of the last term is zero.
Thus

\[
\boxed{
\mathcal O_{K_L}[\Pi_AE_P\mu_{\rm sf}]
=
\mathcal O_{K_L}[\Pi_AE_P\mathcal T_{V_A}].
}
\tag{L-103112.2}
\]

Summing the disjoint owner-product blocks gives

\[
\boxed{
H_{\rm harm}^{\rm eq}(X)
=
\sum_A
\mathcal O_{K_L}[\Pi_AE\mathcal T_{V_A}](X)
+H_{\rm closed}(X),
}
\tag{L-103112.3}
\]

where `H_closed` is exactly the previously closed root, first-chaos,
repeated-label, squared-activity and terminal ledger.

Consequently the statement

```text
QPTI103112:
  the coherently collapsed sum of the block-dependent quarter-power Type-I
  lifts has subpower logarithmic negative mass
```

is equivalent, modulo the frozen closed field, to `HMO102940` and hence to the
canonical `BCI102990` frontier.

## Meaning

The quarter-power cutoff is a useful normal form: it makes the balanced source
vanish and places the entire difficulty in a Type-I-labelled field. It does not
make that field analytically easier without a theorem controlling the
cross-owner physical restriction.
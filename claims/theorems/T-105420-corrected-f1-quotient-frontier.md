# T-105420 — Corrected F1 Hodge frontier after the Wick quotient

Claim ID: `T-105420`

Status: **PROVED REPAIR AND CONDITIONAL CLOSURE; PHYSICAL RESTRICTION OPEN**

This forward checkpoint supersedes only the cofinal claim of
`L-105405/T-105410`. The finite native functor, toric Hodge index, primitive
ray realization and exact Gram identities remain valid.

## Binding correction

The later PR #719 prime-carrier theorem gives a first-chaos Hodge block of size

\[
\asymp e^T/T^2.
\]

Therefore `F1ATO105405` and `F1PE105403`, when read as subpower packing of the
unquotiented positive Hodge energy, are false and withdrawn.

## Corrected conclusion-facing theorem

Let `widetilde Q_tau` be the literal Wick-carrier-quotiented primitive energy of
`L-105412`. Define

```text
F1WNC105420:
  integral_(T to T+1) integral_(0 to 1)
  widetilde Q_tau(e^u) d tau du = e^o(T).
```

The quotient removes exactly the complete degree-one source before any square
or regional positive part. It is the F1 Hodge coordinate of PR #719
`WNC102743`, not a fitted subtraction and not a new independent RH assumption.

`L-105412` proves

\[
\boxed{
\mathrm{F1WNC105420}
\Longrightarrow
\int_T^{T+1}(\mathcal L_{\rm def}(e^u))_-du=e^{o(T)}.
}
\]

The frozen outer-ray/resolvent and Mellin--Landau consumers then give

\[
\boxed{
\mathrm{F1WNC105420}\Longrightarrow\mathrm{RH}.
}
\]

After the quotient, every source monomial has at least two labelled prime
occurrences. The diagonal, same-product, duplicate-owner, same-owner-core,
free labelled-energy and far-ratio costs are closed by the frozen PR #719
ledger. The sole remaining term is the degree-at-least-two,
distinct-product, different-owner physical restriction inside the ratio-eight
window.

```text
finite F1 source/Hodge geometry                       PROVED EXACT
unquotiented primitive-energy packing                 REFUTED
first-chaos Hodge direction                            PROVED EXACT
Wick/source-exact degree-at-least-two quotient         PROVED EXACT
favorable first-chaos one-sided transfer               PROVED EXACT
closed free/same-product/far-ratio sectors             RETAINED
F1WNC105420 = WNC102743 physical restriction           OPEN / RH-BEARING
Riemann Hypothesis                                     UNPROVED
```

# T-100140 — Terminal equivalence audit of the canonical scalar obstruction

Claim ID: `T-100140`
Status: **SUPPLEMENTAL BINDING STATUS THEOREM — RH UNPROVED**
Created: 2026-08-20
Base: PR #659 at `83c17b32a99ac9e1aa5aec3168535550eb286636`
Publication base: PR #671 at `2889071e9ebdc412b94cf2cfe74f1fd5142b2857`

PR #671 now independently preserves the positive-tail equivalence direction.
This supplement retains the signed phase identity and the frozen-orbit OCE
corollary that are absent there.

## 1. Exact result

`L-100140` converts the final positive Poisson norm into

\[
Q_L(y)=|f_L(y)|^2+2\tau_L\int_1^\infty
\left|\sum_{n\ge u}c_{L,y}(n)\right|^2u^{2\tau_L-1}\,du.
\]

Thus the unresolved off-diagonal owner packing is exactly a weighted
square-root-Mertens tail theorem for the complete compact filtered source.

`L-100141` proves that RH supplies all these tail estimates with the full
growing-moment and positive-inverse bookkeeping. Together with PR #659,

\[
\boxed{\mathrm{GPMOC99800}\iff\mathrm{RH}.}
\]

Likewise, on PR #660's proved energy inputs,

\[
\boxed{\mathrm{OCE67}\iff\mathrm{RH}.}
\]

## 2. What is and is not closed

```text
Cauchy–Poisson tail-square identity        PROVED EXACT
signed Poisson square identity             PROVED EXACT
RH => GPMOC                                PROVED
GPMOC => RH                                RETAINED / RECONSTRUCTED
RH <=> GPMOC                               PROVED
RH <=> OCE on native LP inputs             PROVED
diagonal/local-energy shortcut             REFUTED
unconditional GPMOC/OCE                    NOT PROVED
Riemann Hypothesis                         UNPROVED
```

## 3. Consequence for the project

The last estimate is no longer an unspecified technical embedding. It is an
exact equivalent formulation of RH. Renaming it as a Carleson theorem,
off-diagonal packing theorem, or physical-collapse lemma does not lower its
burden.

The strongest honest next attack is the coefficient-tail form

\[
2\tau_L\int_1^\infty
\left|\sum_{n\ge u}\frac{\beta(n)}{\sqrt n}
(\mathcal F_LT)(y/n)\right|^2u^{2\tau_L-1}\,du=2^{o(L)}
\]

after inverse-weighted block integration. It must exploit the actual
squarefree-core signs. Any proof of this display is already a complete RH
proof.

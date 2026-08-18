# T-98100 — The native scalar reduces to one rough prefix and logarithmic-four active children

Claim ID: `T-98100`  
Status: **UNCONDITIONAL REDUCTION; ONE-SIDED BOUNDARY ESTIMATE OPEN**  
Created: 2026-08-18  
Depends on: `L-98100--L-98102`, `R-98100`; PRs #590/#599  
RH status: **unproved**

Fix `epsilon>0`, let

\[
Z=(\log\log\log X)^2,
\qquad
Y_\epsilon=(\log X)^{4+\epsilon},
\]

and use the notation of `L-98100--L-98102`. Define the explicit absolute bulk
budget

\[
\mathcal B_\epsilon(X)
={C_bE_Z\over\sqrt{Y_\epsilon}}
\prod_{Z<p\le X/2}(1+1/p).
\tag{T-98100.1}
\]

Then

\[
\mathcal B_\epsilon(X)=o(1/\log X),
\tag{T-98100.2}
\]

and the exact source satisfies

\[
\boxed{
U_{\rm full}(X)
=
A_Z\mathcal M_Z(X/2)
+
\mathcal A_\epsilon(X)
+
\mathfrak E_{\rm bulk}(X),
\qquad
|\mathfrak E_{\rm bulk}(X)|\le\mathcal B_\epsilon(X).
}
\tag{T-98100.3}
\]

Here

\[
\mathcal M_Z(X/2)
=
\sum_{v<X/2\atop P^-(v)>Z}{\mu(v)\over v}
\tag{T-98100.4}
\]

is one rough reciprocal-Möbius prefix, while

\[
\mathcal A_\epsilon(X)
=
\sum_{X/Y_\epsilon<v<X/2\atop P^-(v)>Z}
{\mu(v)\over v}\varepsilon_Z(X/v)
\tag{T-98100.5}
\]

has only active children

\[
2<X/v<(\log X)^{4+\epsilon}.
\tag{T-98100.6}
\]

Define **Logarithmic-Four Product Boundary 67 (`L4PBR67`)** to be the one-sided
estimate

\[
\boxed{
A_Z\mathcal M_Z(X/2)+\mathcal A_\epsilon(X)
\ge\mathcal B_\epsilon(X)
}
\tag{T-98100.7}
\]

for one fixed `epsilon>0` and all sufficiently large real `X`.
Then

\[
\boxed{
\mathrm{L4PBR}_{67}
\Longrightarrow
U_{\rm full}(X)\ge0\text{ eventually}
\Longrightarrow
\mathrm{GPC}_{67}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-98100.8}
\]

The last implication is the frozen Mellin–Landau consumer.

## What has been removed

Compared with `AFPBR67` in PR #599, the open theorem no longer contains any
child of fixed-power scale `X^delta`. Compared with `BLPTE67` in PR #590, every
large-child Type-I sector has been absorbed before the remaining source is
observed. The surviving data are exactly:

```text
one Z-rough reciprocal-Mobius prefix;
one active correction with child <= log^(4+epsilon) X;
an explicit o(1/log X) debt.
```

The inactive Euler-product tail is not a separate reserve: `L-98102` proves it
combines exactly with the positive Euler main into the rough prefix.

## Exact frontier

```text
slow complete cube                       PROVED POSITIVE
all children above log^(4+epsilon) X    CLOSED
inactive Euler tail/main recombination   PROVED EXACT
logarithmic fourth-power method wall     PROVED AT SOURCE-BLIND SCOPE
L4PBR67                                  OPEN / RH-BEARING
GPC67                                    OPEN / IMPLIED BY L4PBR67
Riemann Hypothesis                       UNPROVEN
```

A proof must preserve the sign coupling between the rough prefix and active
child correction. Separate absolute estimates are not sufficient.
# R-91880 — The PR #503 infinitesimal causal generator is false and is excluded by type

Claim ID: `R-91880`  
Status: **PROVED EXACT COUNTEREXAMPLE AND SUCCESSOR FIREWALL**  
Created: 2026-08-16  
Review source: PR #503 at `db77e5792966edf080604fd4b69fb00f07739681`  
RH status: **unproved**

## 1. Exact witness

Let `p_s(j)` be the positive infinitesimal endpoint row from the Volterra disintegration. At

\[
p=67,\qquad y=15,\qquad s=py=1005,\qquad j=14,
\]

the proposed causal difference is

\[
D_{\rm inf}=p_{1005}(14)-67^{-1/2}p_{15}(14).
\]

The exact radical expression is

\[
\begin{aligned}
D_{\rm inf}
={}&4+\frac{15\sqrt{14}}{13}-\frac{15\sqrt{15}}7-\frac1{91\sqrt{1005}}\\
&-\frac{15\sqrt{14}-14\sqrt{15}}{13\sqrt{67}}.
\end{aligned}
\]

Directed rational square-root enclosures give

\[
\boxed{-\frac{184291}{10^9}<D_{\rm inf}<-\frac{184290}{10^9}<0.}
\tag{R-91880.1}
\]

Therefore the implication

```text
positive infinitesimal Volterra packet
    -> positive factor-67 causal difference
```

is false.

## 2. The successor split

The successor has two disjoint generator sorts.

### Volterra bulk

For a retained endpoint `s`, put `x=X/s`. The complete-cell support satisfies

\[
1<x<67.
\]

Every active Möbius colour `k<x` has all prime factors at most `61`. The bulk packet `p_s` is therefore declared **terminal current**. It is never assigned a rough first owner and the expression

\[
p_s-rp_{s/p}
\]

does not occur anywhere in the generator list.

### Anchored finite sector

Every rough first owner occurs only in the literal finite stopping-line sector. The physical leaf is the finite Target-Lorenz datum

\[
G_\omega=(\nu_\omega;B_\omega;\sigma_\omega)
\]

from `L-93783`, with actual path weight and same-index placement. It is not an infinitesimal packet and it is not obtained from `p_s-rp_{s/p}`.

For the witness `(67,15)`, the frozen directed AVLT applies to the finite leaf. A lightweight independent diagnostic finds Target-Lorenz cutoff `133`, positive score reserve greater than `2.88`, and minimum row reserve greater than `0.0095`. That diagnostic is not substituted for the frozen directed theorem; it confirms that the successor routes the witness to the intended finite leaf.

## 3. Mandatory validator rule

A live certificate is rejected if any node has

```text
generator_kind = infinitesimal_causal
```

or if any Volterra bulk occurrence carries a rough first-owner label.

```text
negative PR #503 witness                    exact
bulk infinitesimal causal generator         forbidden
bulk rough first owner                      forbidden
anchored finite Target-Lorenz replacement   explicit
RH                                           unproved
```
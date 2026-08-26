# L-102837 — Shared-largest-owner sectors form a polylogarithmic decreasing-prime renewal

Claim ID: `L-102837`  
Status: **PROVED EXACT SOURCE-RENEWAL REDUCTION**  
Created: 2026-08-24  
Depends on: `L-102830--L-102836`; `L-102733`  
RH status: **not assumed**

Work in the hard sector of distinct physical prime labels and use the Euler
gauge for the owner decomposition. Repeated prime powers and the joint two-
label `67` occurrence remain in the closed squared ledger.

For an ordered finite prime set put

\[
E_{<p}=\prod_{q<p}(I-x_q),
\qquad x_p=p^{-1/2}U_p.
\]

Modulo the closed repeated-`p` powers, the squarefree occurrences whose largest
prime is `p` and whose depth is at least two are exactly

\[
\boxed{
-x_p(E_{<p}-I).
}
\tag{L-102837.1}

Thus two occurrences whose largest-two owner pairs share the same greatest
prime `p` have a common factor `x_p` on both sides of the physical Gram form.
Translation invariance of the fixed log-kernel gives the exact energy weight

\[
\boxed{\|x_pF\|_2^2={1\over p}\|F\|_2^2.}
\tag{L-102837.2}

The lower field is the same carrier-recombined defect problem on the strictly
smaller prime set `{q:q<p}` and at physical scale divided by `p`.

## 1. Renewal inequality

Let `E(Y;P)` denote the endpoint centered radial cost of all cross-pair terms
from the ordered prime set `P`, after the exact carrier quotient and all closed
source regions. Let `D(Y;P)` denote only the terms whose two owner pairs are
disjoint. Positive homogeneity and subadditivity of the radial gauge give

\[
\boxed{
E(Y;P)
\le
D(Y;P)
+C\sum_{p\in P}{1\over p}
E(Y/p;P_{<p})
+Y^{o(1)}.
}
\tag{L-102837.3}

Here `C` is an absolute gauge-transfer constant and the last term contains
only the already-closed squared, repeated-label, same-product and finite
regions.

The strict order `P_{<p}` prevents a prime from being used twice along one
renewal history.

## 2. Polylogarithmic path mass

Iterating (L-102837.3) produces decreasing squarefree prime chains. Their total
weight is bounded by

\[
\sum_{S\subseteq P} {C^{|S|}\over\prod_{p\in S}p}
=
\prod_{p\in P}\left(1+{C\over p}\right)
\ll_C (\log(2Y))^C.
\tag{L-102837.4}

Therefore

\[
\boxed{
D(Y)=Y^{o(1)}
\Longrightarrow
E(Y)=Y^{o(1)}.
}
\tag{L-102837.5}

Shared-owner sectors require no independent conclusion-bearing estimate. They
are absorbed by a source-faithful decreasing-prime renewal.

## Exact remaining owner geometry

The direct dispersion theorem may now be restricted to owner pairs with four
distinct physical primes. This is frozen in `T-102850`.
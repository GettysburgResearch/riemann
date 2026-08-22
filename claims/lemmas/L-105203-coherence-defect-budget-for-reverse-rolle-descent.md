# L-105203 — Off-real zeros are bounded by a cumulative residue-coherence defect budget

Claim ID: `L-105203`  
Status: **PROVED EXACT FINITE THEOREM AND XI CONDITIONAL LEDGER**  
Created: 2026-08-23  
Depends on: PR #716 `L-104500--L-104501`; PR #720 `L-104522`  
RH status: **not assumed**

## 1. Finite polynomial theorem

Let `p` be a real polynomial. Fix an integer `r>=1` and assume that every real
critical point needed below is simple and no adjacent derivatives have a
common real zero. For `0<=j<r`, let

\[
R_j=N_\mathbb R(p^{(j+1)})
\]

and define the critical residues of `p^(j)` at the real zeros `c` of
`p^(j+1)` by

\[
\rho_{j,c}
={p^{(j)}(c)\over p^{(j+2)}(c)}.
\]

Put

\[
A_j=\left(-\sum_c\rho_{j,c}\right)_+,
\qquad
B_j=\sum_c\rho_{j,c}^2,
\]

and, when `R_jB_j>0`, define

\[
\mathfrak C_j={A_j^2\over R_jB_j};
\]

put `mathfrak C_j=0` in the degenerate case.

Let `E_j` be the number of wrong extrema of `p^(j)`. The proof of
`L-104522.3` gives

\[
R_j-E_j\ge R_j\mathfrak C_j.
\]

Hence

\[
\boxed{
E_j\le R_j(1-\mathfrak C_j).
}
\tag{L-105203.1}
\]

Combine this with the exact global conservation law

\[
N_{\rm nr}(p)
=N_{\rm nr}(p^{(r)})+2\sum_{j=0}^{r-1}E_j.
\]

One obtains

\[
\boxed{
N_{\rm nr}(p)
\le
N_{\rm nr}(p^{(r)})
+2\sum_{j=0}^{r-1}R_j(1-\mathfrak C_j).
}
\tag{L-105203.2}
\]

This is a genuine quantitative reverse-Rolle theorem. It does not require one
coherence constant to be uniformly positive: every derivative level pays only
its own measured coherence defect.

If `p^(r)` is real-rooted and

\[
\boxed{
\sum_{j=0}^{r-1}R_j(1-\mathfrak C_j)<1,
}
\tag{L-105203.3}
\]

then `N_nr(p)<2`. Since nonreal zeros occur in conjugate pairs,

\[
\boxed{p\text{ is real-rooted}.}
\tag{L-105203.4}
\]

Thus an all-or-nothing real-rootedness conclusion follows from a cumulative
**fractional** coherence budget.

## 2. Exact Xi rectangle ledger

Let `Omega` be a regular conjugation-symmetric rectangle for the derivative
ladder

\[
F_j=\Xi^{(j)}.
\]

Use the notation of `L-104501`:

```text
O_j       off-real zeros of F_j in Omega;
R_j       real zeros of F_(j+1) on the real slice;
B_j       two real endpoint defects;
W_j       boundary winding difference;
mathfrak C_j residue coherence of F_j at those real critical points.
```

The exact complex transport identity is

\[
O_0
=O_r+2\sum_{j=0}^{r-1}E_j
 +\sum_{j=0}^{r-1}(B_j+W_j-1).
\]

Substituting (L-105203.1) yields the deterministic upper ledger

\[
\boxed{
O_0
\le
O_r
+2\sum_{j=0}^{r-1}R_j(1-\mathfrak C_j)
+\sum_{j=0}^{r-1}(B_j+W_j-1).
}
\tag{L-105203.5}
\]

No boundary term is discarded. The winding charges may have either local sign;
the displayed sum is retained exactly.

Since `O_0` is a nonnegative even integer, the sufficient condition

\[
\boxed{
O_r
+2\sum_{j=0}^{r-1}R_j(1-\mathfrak C_j)
+\sum_{j=0}^{r-1}(B_j+W_j-1)
<2
}
\tag{L-105203.6}
\]

forces

\[
O_0=0.
\]

## 3. Natural-scale high-tail entry

Choose a height `T`, a fixed vertical margin `H>1/2`, and

\[
r\asymp T^2\log T.
\]

By `L-105201`, every derivative of order at least `r` has no off-real zero in
the rectangle for sufficiently large `T`; hence `O_r=0`. By `L-105202`, the
residue coherence is `1-o(1)` throughout every still-higher derivative level.
In fact, because all adjacent functions in that tail are real-rooted in the
common rectangle, their complete local reverse-Rolle charge vanishes exactly.

Therefore the Xi problem in a height-`T` rectangle is reduced to a finite
low-order ledger of length `O(T^2 log T)`:

\[
\boxed{
2\sum_{j<r}R_j(1-\mathfrak C_j)
+
\sum_{j<r}(B_j+W_j-1)<2.
}
\tag{L-105203.7}
\]

This is sharper than asking every step to satisfy a common transfer constant.
Large coherence losses are permitted at some levels if compensated by exact
zero boundary transport at the others.

## 4. Scope

The theorem does not prove (L-105203.7). It supplies the exact quantitative
quantity whose smallness would descend the unconditional high-derivative entry
to Xi. The residue part is measured by the first two moments already isolated
in PRs #720 and #723; the remaining boundary part is the explicit
Hermite--Biehler/Levinson flux of those branches.

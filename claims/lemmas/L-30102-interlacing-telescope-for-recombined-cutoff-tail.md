# L-30102 — Interlacing telescope for the recombined cutoff tail

Claim ID: `L-30102`  
Title: The ordinary recombined parity tail is one first-boundary atom minus an explicit positive interlacing reserve  
Status: **PROPOSED COMPLETE EXACT LEMMA — INDEPENDENT REVIEW REQUESTED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: elementary monotonicity and telescoping  
Scope: a corrected replacement for the invalid recombined alternating-Euler adapter; no RH conclusion

## 1. Interlaced sequences

Fix

\[
q\ge1,
\qquad
s>0,
\]

and define

\[
A_k=(2kq-1)^{-s},
\qquad
B_k=((2k+1)q)^{-s},
\qquad
D_k=A_k-B_k.
\tag{L-30102.1}
\]

Also put

\[
G_k=B_{k-1}-A_k
=((2k-1)q)^{-s}-(2kq-1)^{-s}.
\tag{L-30102.2}
\]

Because

\[
(2k-1)q\le2kq-1<(2k+1)q,
\]

one has

\[
\boxed{
D_k>0,
\qquad
G_k\ge0.
}
\tag{L-30102.3}
\]

Equality `G_k=0` occurs exactly when `q=1`.

## 2. One-step identity

The adjacent odd subsequence difference is

\[
B_{k-1}-B_k.
\]

Inserting `A_k` gives the exact positive decomposition

\[
\boxed{
B_{k-1}-B_k
=
G_k+D_k.
}
\tag{L-30102.4}
\]

Thus each common-tail pair is a portion of an ordinary telescoping boundary decrement; the remaining portion is the nonnegative interlacing gap `G_k`.

## 3. Finite and infinite telescopes

Summing (L-30102.4) for `K<=k<=L` gives

\[
\boxed{
\sum_{k=K}^{L}D_k
=
B_{K-1}-B_L
-
\sum_{k=K}^{L}G_k.
}
\tag{L-30102.5}
\]

Every term is exact. Since `B_L` tends to zero,

\[
\boxed{
Q_K:=\sum_{k\ge K}D_k
=
B_{K-1}-\sum_{k\ge K}G_k.
}
\tag{L-30102.6}
\]

Consequently

\[
\boxed{
0<Q_K\le B_{K-1}=((2K-1)q)^{-s}.
}
\tag{L-30102.7}
\]

For `q=1`, all gaps vanish and the common tail is exactly one boundary atom:

\[
\boxed{
\sum_{k\ge K}
\left[(2k-1)^{-s}-(2k+1)^{-s}ight]
=(2K-1)^{-s}.
}
\tag{L-30102.8}
\]

For `q>1`, the tail is the same first-boundary atom minus a positive reserve.

## 4. Hausdorff form

If

\[
D_k=\int_{[0,1]}y^k\,d\sigma(y)
\]

is the Hausdorff representation of `L-29808`, then the actual ordinary tail is

\[
\boxed{
Q_K
=
\int_{[0,1]}
\frac{y^K}{1-y}
\,d\sigma(y).
}
\tag{L-30102.9]

The closing bracket in the tag is typographical only.

Equation (L-30102.6) is a second, purely discrete representation of the same quantity. It identifies the correct finite boundary coordinate and the exact positive reserve hidden by the invalid alternating denominator `1+y`.

## 5. Cutoff interpretation

When the first omitted shifted-even and unshifted-odd indices agree at `K`, the complete common cutoff source is exactly `Q_K`.

When the odd index starts one step earlier, the cutoff source is

```text
one explicit unmatched odd collar term
+
Q_K.
```

By (L-30102.6), the latter can be rewritten as

```text
one explicit first odd boundary atom B_(K-1)
-
one positive interlacing-gap reservoir sum G_k.
```

Thus the infinite common tail introduces no independent arbitrary source family. It is controlled by one first-boundary coordinate together with a favorable signed reserve. This is the correct replacement geometry for the double-Euler step rejected in `R-30101`.

## 6. What this does and does not close

This lemma closes exactly:

1. absolute convergence of the recombined common tail;
2. its finite and infinite interlacing telescopes;
3. a one-boundary upper cap;
4. the positive reserve decomposition;
5. the exact `q=1` collapse.

It does **not** yet prove that the boundary atom and reserve map into PR #272's capacity-weighted Pascal flow with polylogarithmic debt. A valid continuation must emit that map explicitly; it may not restore the invalid alternating factor `2^{-M}`.

The strongest plausible repair direction is now source-specific and finite:

```text
first-boundary collar atom
-
positive interlacing reserve
-> exact adjacent/Pascal transport
-> half-scale Cycle-Debt recurrence.
```

No RH conclusion is claimed here.

# L-105542 — Horizontal Xi bank transfer closes BANKREAL105530

Claim ID: `L-105542`  
Status: **PROVED FROM PINNED SOURCE ESTIMATES**  
Created: 2026-08-24  
Depends on: `L-105323`, `L-105341`, `L-105342`, `L-105540`, `L-105541`; pinned one-sided Toeplitz--Hankel realization `L-105260` and strict-bandwidth source ledger `L-105262` at PR #731 head `26a4f398bae1f1a58174ebab9d79a5394227cf36`  
RH status: **not assumed**

Use the source-owned hard one-sided frame with any fixed strict bandwidth
`lambda<1`; in particular `lambda=999/1000`.  Let `d_T` be its dimension and
let the right safe-line reciprocal source be written as

\[
\frac{\xi}{\xi'}
=(L-A)^{-1}+E_{\rm arch}.
\tag{L-105542.1}
\]

The following inputs are already proved on their pinned scopes:

1. the left safe line folds to the right by the exact oriented-ratio
   functional equation (`L-105341`);
2. the omitted reciprocal coefficient tail is power-saving (`L-105342`);
3. entry-dependent freezing has `H1/H2/H3` norm `o(d_T)` after the positive
   Hardy division (`L-105323`);
4. the one-sided Paley--Wiener transform realizes the reflected and same-sign
   boundary products as the exact Toeplitz and Hankel shifts (`L-105260`);
5. at strict bandwidth the source tail, coefficient freezing, finite-degree
   conditioning, and hard-frame ledger are `o(d_T)` in the one-copy and
   two-copy statistics (`L-105262`).

Apply the fixed degree-two bank.  The norm bounds and Lipschitz estimate in
`L-105540` show that multiplying either the model source or any of the pinned
errors by the bank changes an `o(d_T)` trace/HS error by only a fixed factor.
The exact left inverse (L-105540.5) shows that the observation dimension is
still exactly `d_T`; `L-105541` shows that no bank partial index is introduced.
Finally, the normalized safe-line contraction is `O(1/log T)`, so the bank
anchor is

\[
G_T+E_{\rm cubic,T},
\qquad
\|G_T^{-1/2}E_{\rm cubic,T}G_T^{-1/2}\|=O(\log(T)^{-3}).
\tag{L-105542.2}
\]

Therefore the actual folded **horizontal** Xi compression has the form

\[
\boxed{
C_{\rm hor,T}=G_T+E_{\rm hor,T},
\qquad
\operatorname{tr}
\bigl((G_T^{-1/2}E_{\rm hor,T}G_T^{-1/2})_-\bigr)=o(d_T).
}
\tag{L-105542.3}
\]

The finite-window Xi partial-index ledger is retained in the complementary
vertical/companion field; it is not set to zero.  This proves the precise
horizontal realization statement named `BANKREAL105530` in `T-105530`.

```text
BANKREAL105530: PROVED
```

The closed-contour carrier cancellation remains binding: (L-105542.3) is the
horizontal anchor in a signed contour decomposition, not by itself a zero
count.

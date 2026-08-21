# L-103210 — Exact moving-cutoff source-transfer identity

Claim ID: `L-103210`  
Status: **PROVED EXACT SOURCE IDENTITY**  
Created: 2026-08-20  
Depends on: corrected PR #684; audited PR #695  
RH status: **unproved**

For a finite completion cutoff \(Z\), let

\[
\mathscr A_Z
=
\prod_{p\le Z}(I+p^{-1/2}S_p),
\]

with the two labelled copies of \(67\) kept separate.

When the cutoff crosses an ordinary prime \(p\),

\[
\boxed{
\mathscr A_pF-\mathscr A_{p^-}F
=
p^{-1/2}S_p\mathscr A_{p^-}F.
}
\tag{L-103210.1}
\]

This is a literal source transition.  It is not the scalar owner-budget jump
\(1/p\).

For a horizon-dependent cutoff \(Z(X)\), the distributional derivative of the
completed observation therefore has two sorts:

```text
continuous scale derivative at fixed source;
atomic source-transfer jumps at every X for which Z(X) crosses a prime.
```

The corrected PR #684 further shows that the critical kernel is noncompact.
The completion ledger includes an inactive prime tail

\[
R_m(X,Z)
\ll_m
\sqrt X\sum_{p>\max(X,Z)}p^{-3/2}.
\]

Thus a valid one-sided variation theorem must retain:

```text
active squared-core terms;
unsquared activated terms;
inactive continuation;
moving-cutoff source-transfer atoms.
```

No coefficient-only budget may replace this complete packet.

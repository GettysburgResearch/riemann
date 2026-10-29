# Review of the fixed-order conjugate conductor-sieve note

**Status:** The displayed exponent algebra and the reduction to the cited source's localized bound check after two corrections. This is not a full independent proof of the imported analytic lemmas or the proposed generalized theorem. The source-family and Poisson/root-number interfaces remain dependencies.

**Reviewed sources:** `research/exploratory/2026-10-29-conjugate-conductor-sieve/README.md` and De Faveri, [*Optimal large sieve for fixed order characters*](https://arxiv.org/abs/2610.04045v1), version 1, Theorem 1.1, Lemmas 3.1, 3.3, 6.1, and Proposition 8.1. The source is a recent preprint; this review does not certify its theorems.

The conjugate identity `chi_q(a b^(n-1))=chi_q(a) overline(chi_q(b))` includes coprimality zeros, so swapping A and B conjugates the sum after conjugating coefficients. With squarefree q, the source's common-factor split leaves squarefree coprime factors; in Lemma 3.3 their sharp parts are trivial, so the listed mixed root-number factors reduce to fixed ray-class phases. Generalizing the cited Poisson/Mellin/gcd chain still requires checking that each source weight and modulus normalization survives for arbitrary fixed n; the note explicitly imports this step.

Lemma 6.1's `R L1(X/R^n,Y)` combined with Theorem 1.1 gives the four terms of the note's `F_n`: the R exponents are `1-n`, `1`, `2-n`, `-1`, respectively, and the allowed maximum has `R<<X^(1/n)`. The subsequent substitution `X=AQ²R/(BD²)`, `Y=Q/D`, prefactor `BD/(QR)` yields exponents of `(A,B,Q,D,R)`:

```text
T1: (1, 0, 1, -1, 0)
T2: (1/n, 1-1/n, 2/n, -2/n, 1/n-1)
T3: (1-1/n, 1/n, 1, -1, -1/n)
T4: (2/n, 1-2/n, 3/n, -3/n, 2/n-1)
```

For `n>=3`, all D and R exponents are nonpositive. After dropping those factors, `T1 <= T3` for `A<=B`; and the global T4 is bounded by global T2 when `AQ<=B`, or global T3 when `AQ>=B`. The note originally omitted factors of D,R in two local ratios, used `D^(-1/n)` where exact substitution gives `D^(-2/n)` for T2, and compared local T1 and T3 before dropping R. The author corrected the display and now performs those comparisons only on the global terms. These errors did not by themselves invalidate the final majorant.

The replacement of column scale `Q/N(dg)` by `Q/D` is legitimate only after inserting a monotone explicit upper-bound polynomial, as stated; the dyadic operator norm itself need not be monotone. The remaining load-bearing step is the source-to-proof mapping through the generalized squarefree gcd and Mellin localization, including all zero masks, conductor/ray classes, coefficient weights, and the dyadic factor sums. This review has not rebuilt that analytic chain or checked a machine formalization. The note does not establish a zero-free region.

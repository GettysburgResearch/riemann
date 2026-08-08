# R-30502 — The paired odd-divisor commutator cannot be split and paid by atomic norm

Claim ID: `R-30502`  
Title: Separating the two divisor legs of the exact dyadic tail commutator produces an infinite square-root atomic charge  
Status: **EXACT SCOPE REFUTATION / AUTOMATIC REJECTION RULE**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Target: any continuation of PR #304 or `L-30504` that applies source total variation before all-scale commutator recombination

`L-30504` identifies the unresolved tail term as

\[
G_M
=\sum_{m\ge M}a_{2m+1}(E_{2m}-E_m),
\qquad
 a_n=\frac1{\sqrt n}-\frac1{\sqrt{n+1}}.
\tag{R-30502.1}

Its carry source is

\[
\sum_{m\ge M}a_{2m+1}
[\delta_{2m+1}-\delta_{m+1}]
\tag{R-30502.2}

in divisor coordinates.

If the two legs are separated before cancellation, their square-root atomic charge is at least

\[
\sum_{m\ge M}a_{2m+1}\sqrt{m+1}.
\tag{R-30502.3}

Now

\[
a_{2m+1}
=
\frac1{
\sqrt{2m+1}\sqrt{2m+2}
(\sqrt{2m+1}+\sqrt{2m+2})}.
\]

The denominator is at most

\[
2(2m+2)^{3/2}.
\]

Hence

\[
\boxed{
 a_{2m+1}\sqrt{m+1}
\ge
\frac1{2^{7/2}(m+1)}.
}
\tag{R-30502.4}

Therefore

\[
\boxed{
\sum_{m\ge M}a_{2m+1}\sqrt{m+1}=+\infty.
}
\tag{R-30502.5}

The same conclusion holds a fortiori after also charging the current-scale leg `2m+1`.

## Verdict

The following strategy is false as a finite-cost completion:

```text
exact paired odd commutator
-> split into current-scale and half-scale divisor sources
-> take square-root atomic total variation
-> apply adjacent-tree source bounds independently.
```

The divergence does not refute the paired commutator identity or a cancellation-sensitive all-scale estimate. It proves that such an estimate must retain

\[
\delta_{2m+1}-\delta_{m+1}
\]

as one signed transport atom, and must recombine the entire dyadic hierarchy before any absolute value.

## Automatic rejection rule

Reject a claimed repair if it contains either of the bounds

\[
\sum_m a_{2m+1}
(\sqrt{2m+1}+\sqrt{m+1})<\infty
\]

or an equivalent termwise adjacent-commutator charge. The exact lower bound (R-30502.4) contradicts it.

# R-93291 — The natural conjugated-prefix monotone cone is not prime-stable

Claim ID: `R-93291`  
Status: **EXACT REFUTATION**  
Created: 2026-08-18  
Refutes: closure of `LPTRP_23` by requiring `sqrt(N) A_P(N)` to be nondecreasing under every prime adjunction

For a finite prime state `P`, write

\[
 H_{j,P}(N)=\sqrt N\,A_{j,P}(N).
\tag{R-93291.1}
\]

The prime-adjoining recurrence suggests the cone `H(N)` nondecreasing in `N`.
It already fails after adjoining the first permitted prime `5`, even though the
prefix itself remains positive.

## Row two

Before the activation at ten,

\[
 A_{2,\{5\}}(9)
 =\frac3{\sqrt2}+\sum_{n=4}^9\frac1{\sqrt n}.
\tag{R-93291.2}
\]

The coefficient at ten is `1-3=-2`, so

\[
 H_{2,\{5\}}(10)-H_{2,\{5\}}(9)
 =(\sqrt{10}-3)A_{2,\{5\}}(9)-2.
\tag{R-93291.3}
\]

Now `sqrt(10)-3<1/6`, `3/sqrt2<9/4`, and the six remaining terms sum to at
most three. Hence

\[
\boxed{
 H_{2,\{5\}}(10)-H_{2,\{5\}}(9)<\frac78-2=-\frac98.
}
\tag{R-93291.4}
\]

## Row three

Use the integer-scaled row `q_3^sharp`. Before the activation at fifteen,

\[
 A_{3,\{5\}}^\sharp(14)
 =2\sqrt3-1+\sum_{n=5}^{14}\frac1{\sqrt n}<\frac{15}{2}.
\tag{R-93291.5}
\]

The coefficient at fifteen is `1-6=-5`, while
`sqrt(15)-sqrt(14)<1/7`. Therefore

\[
\boxed{
 H_{3,\{5\}}^\sharp(15)-H_{3,\{5\}}^\sharp(14)
 <\frac{15}{14}-5=-\frac{55}{14}.
}
\tag{R-93291.6}
\]

Thus the simplest finite-dimensional monotone cone is not invariant even under
the first large-prime activation. A valid global cone must retain additional
activation-boundary state; positivity alone cannot be upgraded through this
conjugation.

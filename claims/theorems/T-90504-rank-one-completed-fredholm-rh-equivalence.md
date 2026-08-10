# T-90504 — Rank-one completed Fredholm equivalences for RH

Claim ID: `T-90504`  
Status: **FULL EXACT EQUIVALENCE PROPOSAL — PRIME-SIDE SIGN THEOREM OPEN; INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Depends on: `L-90505`, `L-90509`; Xi-cardinal capture on PR #365; trace-class spectral calculus

Fix `1/2<a<c`, let `A_(a,c)` be the Cauchy–Sobolev trace-class Weil operator, and define

\[
 A_{a,c}^\sharp=A_{a,c}+r_-r_-^*,
 \qquad
 r_-g={\widehat{J_{a,c}g}(i/2)-\widehat{J_{a,c}g}(-i/2)\over\sqrt2}.
 \tag{T-90504.1}
\]

Then the prime-side pole term of `A^sharp` is the positive square

\[
 r_+r_+^*,
 \qquad
 r_+g={\widehat{J_{a,c}g}(i/2)+\widehat{J_{a,c}g}(-i/2)\over\sqrt2},
 \tag{T-90504.2}
\]

and

\[
 n_-(A_{a,c}^\sharp)
 =\#\{\text{distinct reflected off-line zero pairs}\}.
 \tag{T-90504.3}
\]

Consequently the following are equivalent:

\[
 \boxed{
 \begin{aligned}
 \mathrm{RH}
 &\iff A_{a,c}^\sharp\succeq0\\
 &\iff \det(I+tA_{a,c}^\sharp)>0\quad(t>0)\\
 &\iff \operatorname{tr}(e^{-\beta A_{a,c}^\sharp}-I)\le0
       \quad(\beta>0)\\
 &\iff \operatorname{tr}[A_{a,c}^\sharp e^{-\beta A_{a,c}^\sharp}]\ge0
       \quad(\beta>0)\\
 &\iff
 \bigl(\operatorname{tr}[(A_{a,c}^\sharp)^{i+j+1}]\bigr)_{0\le i,j\le d}
 \succeq0\quad(d\ge0).
 \end{aligned}}
 \tag{T-90504.4}
\]

This is the preferred unconstrained Fredholm target:

```text
zero side:
    complete Weil form + one positive square;

prime side:
    Lévy gamma operator - all prime adjacencies
    + one manifestly positive cosh-moment square;

negative index:
    exactly the off-line-pair count.
```

No unconditional closing sign theorem is claimed.

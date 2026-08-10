# T-90503 — Intrinsic Darboux–Fredholm equivalences for RH

Claim ID: `T-90503`  
Status: **FULL EXACT EQUIVALENCE PROPOSAL — PRIME-SIDE SIGN THEOREM OPEN; INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Depends on: `L-90508`; Xi-cardinal capture on PR #365; trace-class spectral calculus  
Scope: one explicit intrinsically pole-null trace-class completion

Fix `1/2<a<c` and define

\[
 J_{a,c}^{(0)}
 =\left(\partial_u^2-\frac14\right)
  (c^2-\partial_u^2)^{-2}M_{e^{-a|u|}}.
 \tag{T-90503.1}
\]

Let `A_(a,c)^(D)` represent the complete Weil form on the image of this map, and put

\[
 D_{a,c}^{(D)}(t)=\det(I+tA_{a,c}^{(D)}),
\]

\[
 \Theta_{a,c}^{(D)}(\beta)
 =\operatorname{tr}(e^{-\beta A_{a,c}^{(D)}}-I),
\]

\[
 H_d^{(D)}
 =\left(
 \operatorname{tr}[(A_{a,c}^{(D)})^{i+j+1}]
 \right)_{0\le i,j\le d}.
\]

Then

\[
 \boxed{
 \begin{aligned}
 \mathrm{RH}
 &\iff A_{a,c}^{(D)}\succeq0\\
 &\iff D_{a,c}^{(D)}(t)>0\quad(t>0)\\
 &\iff \Theta_{a,c}^{(D)}(\beta)\le0\quad(\beta>0)\\
 &\iff \operatorname{tr}
 [A_{a,c}^{(D)}e^{-\beta A_{a,c}^{(D)}}]\ge0
 \quad(\beta>0)\\
 &\iff H_d^{(D)}\succeq0\quad(d\ge0).
 \end{aligned}}
 \tag{T-90503.2}
\]

Moreover, the number of positive real zeros of `D_(a,c)^(D)`, counted with multiplicity, is exactly the number of distinct reflected off-line zero pairs.

The test map is intrinsically pole-null because its Fourier multiplier contains

\[
 z^2+\frac14=s(1-s).
\]

Thus there is no pole term and no external projection in the complete prime-side expansion.

Any one of the following proves RH:

```text
Darboux Lee–Yang:
    D_(a,c)^(D)(t)>0 for every t>0;

Darboux heat pressure:
    Theta_(a,c)^(D)(beta)<=0 for every beta>0;

Darboux all-word positivity:
    tr[A_D exp(-beta A_D)]>=0 for every beta>0;

Darboux Hankel hierarchy:
    every shifted moment Hankel matrix H_d^(D) is PSD.
```

No unconditional proof of any closing sign theorem is claimed.

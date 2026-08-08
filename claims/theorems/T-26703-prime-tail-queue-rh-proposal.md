# T-26703 — Prime-tail queue proposal, superseded after density-drift refutation

Claim ID: `T-26703`  
Title: The prime-tail queue implication to RH is correct conditionally, but its proposed subpower hypothesis is false  
Status: **SUPERSEDED / PROPOSED REJECTED AS A COMPLETION**  
Authoring agent: `gpt56-08`  
Created: 2026-08-08  
Corrected: 2026-08-08  
Dependencies: `L-26704`, `L-26705`; PR #274 `R-27302`  
Scope: preserves the finite queue algebra and conditional implication; withdraws `PTQ`

## 1. The finite queue remains exact

For the ordinary-prime residual of the parabolic seed,

\[
r_X(p)=v_p(b_X^{(0)})-p^{-1/2}\log(X/p),
\]

define

\[
\mathcal Q_X
=
\max_{P\le X}
\left(\sum_{P\le p\le X}r_X(p)\right)_+.
\]

`L-26704` gives an explicit nonnegative prime-to-prime interval transport whose sole exterior charge is exactly `mathcal Q_X`, and proves

\[
P_X\ge J_{\mathbb P,X}(b_X^{(0)})-\mathcal Q_X\log X.
\]

It also proves that `mathcal Q_X` is the minimum exterior charge among upward transports using only ordinary-prime endpoints. These finite statements are retained.

`L-26705` proves that every positive maximizing tail begins below every fixed output ratio. This fixed-ratio localization is also retained at its stated scope.

## 2. The former load-bearing assertion

The previous version proposed

\[
\boxed{\mathcal Q_X=X^{o(1)}}
\tag{PTQ}
\]

as the remaining theorem. Conditionally, `PTQ` would imply the sharp prime-ramp lower bound and RH.

That conditional implication remains correct. The hypothesis does not.

## 3. Density-drift obstruction

PR #274 `R-27302`, frozen for this correction at

```text
c2e1a978a0156944c26132943fa41bcf7c838fec
```

derives, subject to independent review of its uniform finite-difference and prime-sampling steps,

\[
\sum_{p\le X}r_X(p)
=
\left(4(1-\gamma)+o(1)\right)
\frac{\sqrt X}{\log^2X}.
\]

The complete suffix beginning at the first prime is one of the tails in the maximum. Therefore

\[
\boxed{
\mathcal Q_X
\ge
\left(4(1-\gamma)+o(1)\right)
\frac{\sqrt X}{\log^2X},
}
\]

which is incompatible with `PTQ`.

The mechanism is structural. The continuum defect has total mass zero, but prime sampling uses density `1/log(X\theta)`. Its first density correction is the nonzero logarithmic moment

\[
-\int_0^1E(\theta)\log\theta\,d\theta=4(1-\gamma)>0.
\]

Prime-to-prime blocks preserve total ordinary-prime incidence and must export this drift to the boundary.

## 4. Correct surviving scope

Retained:

```text
prime queue recurrence and max-tail formula       PROPOSED EXACT
nonnegative consecutive-prime transport            PROPOSED EXACT
minimum exterior charge in that restricted cone    PROPOSED EXACT
objective ledger                                    PROPOSED EXACT
fixed-ratio tail localization                       PROPOSED ASYMPTOTIC
```

Withdrawn:

```text
subpower prime-only queue PTQ                       PROPOSED FALSE
T-26703 as a route completing RH                    REJECTED
```

The density drift does not refute composite squarefree collectors, dyadic opposite-parity source contraction, or the parity/factor-five physical transition route. Those mechanisms recombine incidence before the prime-density correction is charged.

## 5. Correct frontier

The canonical source-specific endgame is now the parity/factor-five transition programme:

```text
correct two-frequency block
-> parity-paired finite source frame
-> omega_2 synthesis
-> factor-five localization to quotient cells 2,3,4
-> strict generalized-prime carry reserve
-> physical source-image domination
-> dyadic shell / bottom-charge consumer
-> RH.
```

The sole unresolved theorem in that chain is the physical source-image transition certificate recorded in the consolidated review spine `T-26704`.

## 6. Status boundary

```text
PTQ conditional implication to RH      correct but unusable
PTQ asymptotic hypothesis               proposed refuted
finite queue algebra                    retained
Riemann Hypothesis                      unproved
```

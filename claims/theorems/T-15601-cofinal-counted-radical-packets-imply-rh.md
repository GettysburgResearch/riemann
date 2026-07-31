# T-15601 — Cofinal counted radical packets imply RH

Claim ID: `T-15601`  
Title: Count caps plus inverse–Ritz near-radical floors complete the localized Weil chain  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-09-c`  
Created: 2026-07-31  
Dependencies: `T-14302`, `L-15601`, localized Weil support monotonicity  
Scope: positive sufficient criterion for the Riemann hypothesis

## Statement

Let `A_j=A_(a_j)` be localized Weil operators at a cofinal sequence

\[
 a_j\longrightarrow\infty.
\]

For every `j`, suppose the following finite, proof-producing data exist.

1. Rational thresholds
   \[
   0<t_j<\Gamma_j.
   \]
2. An integer `d_j>=1` and a rigorous ambient count certificate
   \[
   \dim 1_{(-\infty,\Gamma_j)}(A_j)\le d_j.
   \tag{T-15601.1}
   \]
3. A `d_j`-dimensional exact trial packet `L_j subset D(A_j)`.
4. Directed forms `H_j,K_j` enclosing
   \[
   \langle(A_j-t_j)u,v\rangle,
   \qquad
   \langle(A_j-t_j)u,(A_j-t_j)v\rangle
   \]
   on the complete packet.
5. A rational `q_j<0` for which the exact gates of `L-15601` certify
   \[
   H_j\prec0,
   \qquad
   q_jK_j-H_j\succeq0.
   \tag{T-15601.2}
   \]

Put

\[
 F_j=t_j+\frac1{q_j}.
 \tag{T-15601.3}
\]

If

\[
 \boxed{\liminf_{j\to\infty}F_j\ge0,}
 \tag{T-15601.4}
\]

then the Riemann hypothesis is true.

## Proof

`L-15601` gives the ambient lower bound

\[
 \inf\sigma(A_j)\ge F_j
\]

at every level. The cofinal lower-envelope theorem `T-14302` then applies and proves RH. QED.

## Closed scalar sufficient condition

It is sufficient to replace item 5 by the exact hypotheses of `L-15602`. Thus, if the count-matching packet has compression and cross-residual bounds

\[
 -\alpha_jG_j\preceq B_j\preceq\alpha_jG_j,
 \qquad
 \mathcal R_j\preceq\beta_j^2G_j,
 \qquad
 0\le\alpha_j<t_j,
\]

then one may take

\[
 \boxed{
 F_j=
 -\frac{3t_j\alpha_j+\alpha_j^2+\beta_j^2}
        {t_j-\alpha_j}.}
 \tag{T-15601.5}
\]

In particular, RH follows from the explicit cofinal conditions

\[
 \inf_j t_j>0,
 \qquad
 \alpha_j\to0,
 \qquad
 \beta_j\to0,
 \tag{T-15601.6}
\]

provided the packet rank equals the certified count cap at every level.

## How this completes the finite chain

The prior chain was

```text
complete directed symbol
 -> finite low-symbol set
 -> finite low-mode count
 -> complement floor
 -> finite low block and cross map
 -> cofinal lower envelope.
```

T-15601 supplies an alternative final finite adapter:

```text
complete directed symbol
 -> finite low-mode count d_j below Gamma_j
 -> d_j exact repaired radical trial vectors
 -> directed first/second shifted forms
 -> inverse-Ritz floor F_j.
```

The low-symbol packet is still needed to prove the count cap, but it need not be matched to the radical packet by an explicit principal-angle theorem. Count, rank, and complete residual replace that comparison.

## What remains open

The theorem is a genuine weakening, not an RH proof. The remaining analytic problem is the cofinal rank-capacity estimate

\[
 D(a_j,t_j,\Gamma_j)
 \le C(a_j,\varepsilon_j),
 \qquad \varepsilon_j\to0,
\]

with both sides referring to the same exact normalization. Existing work gives:

- finite count interfaces from `L-14310/L-14311`;
- exact repaired radical packets from `L-15301/L-15303`;
- fixed-rank tail decay.

No current theorem proves the required simultaneous growing-rank decay. A finite numerical trend is not a substitute for this symbolic comparison.

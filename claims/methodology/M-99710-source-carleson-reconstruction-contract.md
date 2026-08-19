# M-99710 — Source-Carleson reconstruction contract

Methodology ID: `M-99710`  
Status: **FAIL-CLOSED PROOF PROGRAM**  
Created: 2026-08-20

## Objective

Prove `APOC99710` from the literal native owner graph, not from an unsigned
prefix norm.  The target is

\[
\int_{e^e}^{X}\left(
 \int_{\mathbb R}P_{\tau_x}(\gamma)
 |\mathscr H_x(-\tau_x+i\gamma)|^2d\gamma
\right)^{1/2}{dx\over x}=X^{o(1)},
\qquad
\tau_x=(\log\log x)^{-1}.
\]

## Exact state

At a source index `n`, retain

```text
n;
67-adic depth e=0,1,2;
owner prime power q;
P_n(q);
a(n)=beta(n)/g(n);
activation x/n;
phase gamma;
Poisson width tau_x;
future-prime / first-owner label.
```

No coordinate may be marginalized before the owner square is formed.

## Required decomposition

A valid proof should have the following literal shape.

1. **Poisson point evaluation.** Use `L-99711` to replace the physical phase
   zero by the adaptive vertical square function.
2. **Owner disintegration.** Expand every coefficient through the exact
   logarithmic-owner law of PR #655.
3. **Quadratic-variation payment.** Use `L-99710` before any sum over `n`.
4. **Activation tents.** Group owner edges only after their complete SHARP
   activation intervals and RN endpoint labels agree.
5. **Carleson packing.** Prove that every logarithmic activation tent is paid a
   bounded number of times, up to `x^(o(1))` from the left strip.
6. **Negative-mass consumer.** Invoke only PR #653's subpower logarithmic debt
   theorem and the exact scalar Mellin transform.

## Immediate falsifiers

```text
replace P_n(q) by an arbitrary prime choice;
use V_0 instead of the phase-averaged square;
fix tau independently of x;
apply Cauchy-Schwarz after summing all source indices;
identify the contracted alpha-child tree with the native Euler operator;
drop the e=2 duplicated-67 owner transitions;
use L-99712's positive real-order completion as a pole-free witness;
claim RH from finite endpoint scans.
```

## Smallest useful computational campaign

For a segmented endpoint range, export exact sparse records

```text
(n,e,q,P_n(q),a(n),activation interval)
```

and assemble the Poisson-averaged edge Gram with the exact kernel
`q^(-tau)`.  Measure the maximal source-tent packing constant rather than only
sampling the final scalar sign.  Hostile mutations must include:

```text
removing the q=67^2 owner;
changing Lambda_g(67^k) from 2 log 67 to log 67;
using a raw endpoint cutoff instead of the RN ratio;
replacing tau_x by a fixed positive constant;
forcing the real-u completion into the Landau consumer.
```

A numerical bounded packing constant is reconnaissance only.  Promotion
requires a symbolic source-tent decomposition or a directed finite campaign
plus a separately proved analytic tail.

## Scientific boundary

The exact owner gap and adaptive analytic tradeoff are proved.  The only
conclusion-producing arithmetic statement is the source-tent Carleson packing
estimate `APOC99710`.  RH remains unproved.
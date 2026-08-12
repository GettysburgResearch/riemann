# Moving-node Clark-moat attack

Date: 2026-08-13  
Branch: `research/gpt56-pro/91720-moving-node-clark-moat`  
Parent: PR #422 at `4619269090043f0baef2aa13f5cc1184eed85ee2`

## Result

The fixed-node zero moat was optimized over the Cauchy node. For a depth box
`delta<=x<=b` and height `|y|<=Y`, the optimal node is

\[
\eta_*=\sqrt{b^2+Y^2}
\]

and the uniform charge is

\[
\frac{2\delta}{\sqrt{b^2+Y^2}+b}
\sim\frac{2\delta}{Y}.
\]

This improves the fixed-node `Y^-2` scale by one full power.

Consequently exact entropy exhaustion is not required: a canonical
source/model error `o(1/Y)` at the moving node excludes every fixed
hypothetical off-line zero.

## Remaining issue

The entropy error must be source identified. An arbitrary scalar upper bound
or a separately chosen model remainder is not sufficient.

## RH status

Unproved.

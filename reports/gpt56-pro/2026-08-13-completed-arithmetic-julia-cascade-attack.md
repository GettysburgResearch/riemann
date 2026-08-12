# Completed arithmetic Julia-cascade attack

Date: 2026-08-13  
Branch: `research/gpt56-pro/91730-completed-arithmetic-julia-cascade`  
Parent: PR #423 at `03a057c7bc18080bf89afaa436abf839d6d1c17f`

## Result

The paired-eta, compact dyadic/gamma bridge, and beta/gamma source channels
have been assembled into one exact ordered Julia cascade.

At the kernel level,

\[
K_{\rm arith}^-
=
K_{\rm arith}^+
+
D_\eta K_{\rm br}^-K_\Gamma^-
+
K_\eta^+D_{\rm br}K_\Gamma^-
+
K_\eta^+K_{\rm br}^+D_\Gamma.
\]

Every term is positive and fully polarized. The rational square is lossless.

This removes the remaining source-side assembly problem. The only open
component is canonical allocation of these returned/detail channels to the
critical and stable model outputs rather than the hyperbolic or auxiliary
ports.

## RH status

Unproved.

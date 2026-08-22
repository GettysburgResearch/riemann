# Paired residue-coherence boundary flux

## Executive result

L-105101 represented the second critical-residue moment on one finite
rectangle. L-105102 adds the matching first-moment contour and combines the
two into the exact coherence quotient.

For

\[
P_F=\frac{F}{F'},
\qquad
Q_F=\frac{F^2}{F'F''},
\]

let \(\Phi_{1,F}\) and \(B_F\) be their complete counterclockwise boundary
charges.
Then

\[
\mathcal M_{1,F}=-\Phi_{1,F}+C_{1,F},
\qquad
\mathcal M_{2,F}=B_F-C_{2,F}-D_{2,F},
\]

and, when \(R_F\mathcal M_{2,F}>0\), therefore

\[
\mathfrak C_F
=
\frac{(-\Phi_{1,F}+C_{1,F})_+^2}
{R_F(B_F-C_{2,F}-D_{2,F})}.
\]

The new \(C_{1,F}\) term is the sum of first residues at nonreal critical
points. The two second-moment corrections are the algebraic squared-residue
sum at nonreal critical points and the adjacent-derivative pole debt.

## Why it matters

At \(F=\Xi^{(k-1)}\), the formula is exactly the finite-window transfer-safe
coherence gate from draft PR #720, conditional on the regular-window
hypotheses. It turns the open input into one explicit inequality involving
two oriented boundary charges and three correction ledgers. The literal
RCMV104530 square agrees only after positivity of the signed first moment is
established.

The representation is not an estimate. Each correction is load bearing.
For

\[
p(x)=x^5-x^3+x,
\]

\(p'(x)>0\) on the real axis, so the real first moment is zero. Nevertheless,
the global first boundary charge is \(-2/25\). The nonreal correction is also
\(-2/25\), exactly canceling the apparent positive carrier \(2/25\).

At each fixed regular height, one may instead choose a sufficiently thin
strip so that both nonreal critical corrections vanish. That exact
simplification trades correction estimates for the unresolved problem of
controlling the two boundary charges along a potentially shrinking strip.

## Verification

The exact rational/Gaussian-rational replay checks:

- narrow, full, real, nonreal, and asymmetric windows;
- independent \(V_2\) and frozen \(V_2,V_4\) global ledgers;
- exact coherence \(4/5\) for \(x^3-3x+1\);
- exact coherence \(2/27\) for the quartic transfer firewall;
- integrated first- and second-edge orientation oracles;
- incomplete, duplicate, wrong-kind, and boundary-root rejection;
- authentication of the frozen L-105101 checkpoint;
- fail-closed asymptotic, RCMV, and RH scope.

No Xi evaluation, floating-point contour quadrature, or heavy campaign was
run.

## Remaining frontier

The five analytic tasks are a signed estimate for \(\Phi_{1,k}\), control of
\(C_{1,k}\), an upper estimate for \(B_k\), and control of \(C_{2,k}\) and
\(D_{2,k}\), all along a justified cofinal window sequence and with a strict
coherence margin. Multiple/common-zero events still need a separate
structural ledger before the simple-stratum transfer can be applied.

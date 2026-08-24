# L-105632 — Inner all-pass phases have no adverse signed complement under any source projection

Claim ID: `L-105632`  
Status: **PROVED EXACT HARDY/HANKEL SIGN THEOREM**  
Created: 2026-08-25  
Depends on: `L-105627`; sibling `L-106431`  
RH status: **not assumed**

## 1. Signed complement charge

Let `U` be unimodular on the boundary and suppose `H_U` and
`H_(bar U)` are Hilbert--Schmidt on the finite/regularized scope in use. For an
orthogonal source projection `P`, define

\[
\Delta_P(U)
=
\operatorname{tr}(P^\perp H_U^*H_UP^\perp)
-
\operatorname{tr}(P^\perp H_{\overline U}^*H_{\overline U}P^\perp).
\tag{L-105632.1}
\]

This is the signed unobserved index of sibling `L-106431`.

## 2. Inner phases

If `U` is inner in the upper half-plane, multiplication by `U` maps `H^2`
into `H^2`. Therefore

\[
\boxed{H_U=0.}
\tag{L-105632.2}
\]

Consequently, for every source projection `P`,

\[
\boxed{
\Delta_P(U)
=-\|H_{\overline U}P^\perp\|_{\mathcal S_2}^2
\le0.
}
\tag{L-105632.3}
\]

In particular,

\[
\boxed{(\Delta_P(U))_+=0.}
\tag{L-105632.4}
\]

No absolute model-space coverage estimate is needed to prove this sign.
Large unobserved inner model-space mass is favorable and must not be charged as
an error.

If `U` is anti-inner, the signs reverse. For a reduced quotient

\[
U=\omega B_+/B_-,
\]

the positive signed complement is carried entirely by the anti-causal
`B_-` component after the exact pole--zero overlap cancellation.

## 3. Xi safe-region consequence

For every total height

\[
H\ge\beta_1,
\]
`L-105627` proves that

\[
U_H(x)=\Xi'(x-iH)/\Xi'(x+iH)
\]

is inner. Hence every finite/source-regularized signed complement satisfies

\[
\boxed{(\Delta_P(U_H))_+=0}
\tag{L-105632.5}
\]

for every predeclared source bank `P`.

Thus the signed Paley--Wiener tail is already closed throughout the safe
Xi-prime region, independently of sampling coverage. A positive signed tail can
first appear only when a zero of the denominator crosses above the shifted
boundary and inserts an anti-inner factor.

## 4. Relation to raw shell energy

The real-rooted firewall `R-105620` has large `E_-` and equally large `E_+`.
Equation (L-105632.3) explains why the exact signed index remains harmless:
the favorable channel is not discarded. Requiring the absolute negative
energy to be small charges precisely the inner model-space mass which the
index subtracts.

## 5. Remaining boundary

At a descending base below `beta_1`, the phase need no longer be inner. The
positive signed complement is then a quantitative measure of the newly
anti-causal denominator divisor. Estimating or excluding that divisor is the
same pole/zero-height obstruction as `SAFEDESC105628`.

The theorem does not prove that the base can be descended to zero. It proves
that absolute coverage and the positive signed-tail estimate are not separate
gates in the safe region.

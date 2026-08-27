# L-105449 — Strict extremal-line Gauss–Lucas structure for Xi derivatives

Claim ID: `L-105449`  
Status: **PROVED EXACT EXTREMAL-BOUNDARY THEOREM**  
Created: 2026-08-24  
Depends on: `L-105062`, `L-105442`, `L-105447--L-105448`  
RH status: **not assumed**

## 1. General parity-symmetric setup

Let `F` be a real entire function of order at most one and definite parity.
Assume every zero `rho` of `F` satisfies

\[
\Im\rho\le\beta
\]

and at least one zero lies strictly below the line `Im z=beta`. Put

\[
g_\beta(w)
=-{F'(w+i\beta)\over F(w+i\beta)}.
\tag{L-105449.1}

Away from the top-edge zeros of `F`, the parity-paired Hadamard product gives

\[
{F'(z)\over F(z)}
=
\sum_{\rho}^{\rm sym}{1\over z-\rho},
\tag{L-105449.2}

with multiplicities and symmetric local convergence. Definite parity removes
the possible nonconstant exponential derivative.

## 2. Strict boundary orientation

For `z=x+i beta`, one zero `rho=u+iv` contributes

\[
\Im\left(-{1\over z-\rho}\right)
={\beta-v\over(x-u)^2+(\beta-v)^2}
\ge0.
\tag{L-105449.3}

A zero strictly below the extremal line contributes strictly positively for
every finite `x`. Therefore

\[
\boxed{
\Im g_\beta(x)>0
}
\tag{L-105449.4}

at every real `x` which is not a top-edge zero of `F`.

This is stronger than the abstract Pick conclusion: the continuous boundary
current created by the lower zeros is strictly positive on the complete
extremal line.

## 3. No new noncommon critical point on the top line

Suppose

\[
F'(c+i\beta)=0,
\qquad
F(c+i\beta)\ne0.
\]

Then `g_beta(c)=0`, contradicting (L-105449.4). Hence

\[
\boxed{
F'(c+i\beta)=0
\Longrightarrow
F(c+i\beta)=0.
}
\tag{L-105449.5}

Every derivative zero on the parent extremal line is therefore inherited from
a multiple parent zero. No noncommon critical point is created there.

If `rho=a+i beta` is a parent zero of multiplicity `n`, then it is a derivative
zero of multiplicity exactly `n-1`. Consequently the complete extremal-line
multiset satisfies

\[
\boxed{
\operatorname{ord}_\rho F'
=
\max(\operatorname{ord}_\rho F-1,0).
}
\tag{L-105449.6}

This is a strict boundary form of Gauss–Lucas for the parity-symmetric entire
class.

## 4. Xi derivative specialization

Take

\[
F=\Xi^{(r)},
\qquad
\beta=\beta_r.
\]

Every Xi derivative has real zeros: Hardy supplies infinitely many for `Xi`,
and the multiplicity-aware Rolle floor in `L-105062` propagates infinitely
many real zeros up the derivative ladder. Thus, whenever `beta_r>0`, the
hypothesis of at least one zero strictly below the extremal line is automatic.

Therefore

\[
\boxed{
\{z:\Xi^{(r+1)}(z)=0,\ \Im z=\beta_r\}
}
\]

consists only of common zeros inherited from multiple zeros of `Xi^(r)`, with
multiplicity reduced by one.

In particular, if every zero of `Xi^(r)` on an attained extremal line is
simple, then `Xi^(r+1)` has no zero on that line.

## 5. Exact line extinction, not a quantitative height gap

Suppose the multiplicities of all top-edge zeros are bounded by `M`. Repeated
differentiation and (L-105449.6) give the exact line statement

\[
\boxed{
F^{(M)}(z)\ne0
\qquad\text{whenever }\Im z=\beta.
}
\tag{L-105449.7}

This does **not** imply a bound of the form

\[
\beta(F^{(M)})\le\beta-\delta
\]

for a parent height gap `delta`. New derivative zeros can lie strictly below
but arbitrarily close to the parent extremal line, and an unbounded sequence
of such zeros can retain the same supremal height without attaining it.

Thus even a simple isolated top zero disappears from the exact line after one
derivative, but a quantitative drop of the global height supremum requires an
additional compactness or no-escape theorem.

## 6. What remains in the nonattained case

If the supremal height is approached by zeros with real parts tending to
infinity, the derivative may have the same supremum even though it has no zero
on the extremal line. This is exactly the spatial-escape alternative of
`T-105446`.

The attained-boundary content is therefore rigid but deliberately limited:

```text
new noncommon top critical point      IMPOSSIBLE;
multiple top zero                     loses one multiplicity per derivative;
simple top zero                       disappears from the exact line;
strict supremal-height descent        REQUIRES NO-ESCAPE INPUT;
unattained or spatially escaping top  REMAINS THE GENUINE MECHANISM.
```

## 7. Scope

The theorem does not bound how close derivative zeros may lie below `beta`,
and it does not exclude unbounded top-edge multiplicity. It removes new
critical-point creation on an attained extremal line; it does not prove strict
height descent or RH.
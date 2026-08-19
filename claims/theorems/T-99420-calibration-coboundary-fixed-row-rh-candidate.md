# T-99420 — Calibration-coboundary fixed-row RH candidate

Claim ID: `T-99420`
Status: **PROPOSED COMPLETE UNCONDITIONAL PROOF CANDIDATE — HOSTILE REVIEW REQUIRED**
Created: 2026-08-19
Base: PR #641 at `19cd3939a54ccea73b055b3952b5dd7ed638c4fb`
RH status: **not established by publication**

## 1. Canonical local decomposition

For the exact native equality frame \(E\), use `L-99421` to write

\[
E=P+A,
\tag{T-99420.1}
\]

where \(P\) is the positive absolutely continuous endpoint frame and \(A\) is
the complete signed compact calibration potential.

Compact Hall and the random-key common-parent construction act on \(P\) and
give

\[
P=J+PT,\qquad J\ge0,
\tag{T-99420.2}
\]

with one source-faithful, endpoint-decreasing child operator \(T\).

By `L-99420`,

\[
\boxed{
E=J+ET+(A-AT),
}
\tag{T-99420.3}
\]

and the finite nilpotent resolution is

\[
\boxed{
c_X(j)=D_X(j)+A_X(j),
\qquad
D_X(j)=\bigl[J(I-T)^{-1}\bigr]_X(j)\ge0.
}
\tag{T-99420.4}
\]

This reconstructs the actual signed identity left open in PR #641.  Every
descendant calibration cancels exactly.

## 2. Fixed-row analytic transfer

By `L-99422`,

\[
A_X(j)=O_j(1),
\tag{T-99420.5}
\]

so its Mellin transform is holomorphic in \(\Re s>0\).

The exact full-row transform is

\[
\int_1^\infty c_X(j)X^{-s-1}\,dX
=
\frac{C_j}{s^2}
+
\frac{P_j(s+\tfrac12)}
{s^2\zeta(s+\tfrac12)}.
\tag{T-99420.6}
\]

The elementary finite-row bounds give, for some fixed exponent depending only
on \(j\),

\[
D_X(j)+|A_X(j)|=O_j(\sqrt X\,\log^2(2X)),
\tag{T-99420.6a}
\]

so the defining Mellin integral of \(D_X(j)\) has a finite abscissa of
convergence.

Subtracting the holomorphic transform of \(A_X(j)\), the Mellin transform of
the nonnegative function \(D_X(j)\) has every nonremovable reciprocal-zeta pole
of (T-99420.6).

For every \(z\) in the open critical strip, the large-row asymptotic

\[
P_j(z)=
-\frac{z(z+1)}{1-z}j^{-z-1}
+o_z(j^{-\Re z-1})
\tag{T-99420.7}
\]

shows that \(P_j(z)\ne0\) for some fixed sufficiently large row \(j\).

The right side of (T-99420.6) is analytic at every positive real \(s\).
Landau's real-abscissa theorem applied to \(D_X(j)\ge0\) forces its defining
Mellin integral to be holomorphic throughout \(\Re s>0\).  An off-line zero
\(\rho\) would give a nonremovable pole at \(s=\rho-\tfrac12\), a
contradiction.  Functional-equation symmetry gives the proposed RH conclusion.

## 3. Why the known obstructions do not apply

```text
odd-history Target-Lorenz orientation       never used
branchwise positive oriented child          never used
generationwise calibration debt             telescopes exactly
positive knot atoms / positive anchors      not required
literal score 4sqrt(X)                      not used
ordinary/detail capacity                    not used
prime-square moat                           not used
scalar-to-two-row lift                      not used
```

## 4. Composition graph

```text
distributional exact endpoint frame              PR #638 + L-99421
positive factor-67 density                       frozen compact certificate
endpoint-nested canonical packet                 PR #636
compact Hall literal source partition            PR #636 / PR #620
random-key residual child partition               PR #636 / PR #632
primitive calibration coboundary                 L-99420
root-only fixed-row defect                        L-99422
fixed-row reciprocal-zeta transform               frozen / reconstructed
large-row noncancellation                         frozen / reconstructed
Landau + functional equation                      frozen / reconstructed
RH candidate
```

## 5. Exact scientific status

The packet is candidate-complete on the frozen compact Hall/profile and
endpoint-frame formulas.  Publication is not independent acceptance of those
inputs or of RH.

```text
calibration coboundary composition          PROVED EXACT
actual signed ledger identity               RECONSTRUCTED CANONICALLY
descendant defect cancellation              PROVED EXACT
root fixed-row boundedness                  PROVED ON FROZEN INPUTS
Mellin pole preservation                    PROVED
Riemann Hypothesis                          UNPROVED PENDING REVIEW
```

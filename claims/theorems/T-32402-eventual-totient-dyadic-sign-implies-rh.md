# T-32402 — Eventual one-sidedness of the dyadic totient defect implies RH

Claim ID: `T-32402`  
Title: If the explicit parity-filtered Euler-totient Riesz defect is eventually nonpositive, then every nontrivial zeta zero lies on the critical line  
Status: **PROPOSED COMPLETE CONDITIONAL THEOREM — EVENTUAL SIGN OPEN**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: `L-32406`; Landau's one-sign theorem for Mellin/Laplace transforms  
Scope: one-sided scalar RH implication; no proof of the eventual sign

## 1. Scalar

Retain

\[
 D_\varphi(X)
 =P(X)-2\sqrt2P(X/2),
\]

where

\[
 P(X)=\sum_{n\le X}{\varphi(n)\over\sqrt n}\log{X\over n}.
\]

`L-32406` proves

\[
\boxed{
 \int_1^\infty D_\varphi(X)X^{-z-1}dX
 ={\eta(z-1/2)\over z^2\zeta(z+1/2)}
}
\tag{T-32402.1}
\]

initially in the absolute-convergence half-plane, with meromorphic continuation thereafter.

## 2. No positive-real singularity

For real `z>0`, `zeta(z+1/2)` has no zero. At `z=1/2` its pole produces a zero of the reciprocal quotient rather than a singularity. The eta numerator is entire.

Thus the right side of (T-32402.1) has no singularity on the positive real axis.

At `z=0` it has the declared boundary pole from `z^-2`; that point is the boundary of the RH half-plane, not an obstruction to the argument below.

## 3. Off-line zeros are genuine nonreal poles

By `L-32406`, every nontrivial zero

\[
 \rho=\frac12+\delta+i\gamma,
 \qquad\delta>0,
\]

produces an uncancelled pole at

\[
 z_\rho=\delta+i\gamma.
\]

In particular any failure of RH produces at least one singularity with positive real part and nonzero imaginary part.

## 4. Landau argument

Assume there exists `X_0` such that

\[
\boxed{
 D_\varphi(X)\le0
 \qquad(X\ge X_0).
}
\tag{T-32402.2}
\]

Put

\[
 f(t)=-D_\varphi(e^t).
\]

After adding a compactly supported correction, one obtains a nonnegative locally integrable function on `[0,infinity)` whose Laplace transform differs from minus (T-32402.1) only by an entire function.

Suppose an off-line zero exists and let `a>0` be the abscissa of convergence of this nonnegative Laplace transform. The nonreal pole set in `Re z>0` makes `a>0`. Landau's one-sign theorem then forces a singularity at the **real** boundary point `z=a`.

But Section 2 shows that the meromorphic continuation has no positive-real singularity. This contradiction excludes every off-line zero to the right of the critical line.

Functional-equation symmetry excludes the reflected half. Hence

\[
\boxed{
 D_\varphi(X)\le0\text{ eventually}
 \Longrightarrow\mathrm{RH}.
}
\tag{T-32402.3}
\]

The same argument works if `D_phi` is eventually nonnegative.

## 5. Why this target is unusually concrete

The scalar contains no Möbius coefficients after the pole filter:

\[
 c(n)=\varphi(n)-4\mathbf1_{2\mid n}\varphi(n/2),
\]

with deterministic parity sign. Equivalently the desired inequality is simply

\[
\boxed{
 P(X)\le2\sqrt2P(X/2)
}
\tag{T-32402.4}
\]

cofinally.

Thus one possible full proof of RH has been reduced to a pure inequality for positive Euler-totient Riesz means at two dyadic scales.

No zero sum, prime packet, Type-II estimate, or carry-flow existence theorem appears in the statement.

## 6. Proof boundary

Closed here:

- the Mellin transform;
- absence of positive-real singularities;
- uncancelled off-line poles;
- the Landau implication from eventual one-sidedness to RH.

Open:

- proof of (T-32402.2) or its reverse sign;
- RH.

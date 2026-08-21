# T-94200 — Prime-sieved parabolic splines give a zero-deficit native proof candidate for RH

Claim ID: `T-94200`  
Status: **PROPOSED COMPLETE UNCONDITIONAL RH THEOREM — HOSTILE INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-16  
New producer: `L-94200--L-94202`  
Frozen endpoint sources reconstructed: PR #352 at `906b5a477a1ed7c88a40db7569924f15f3d54b72`; PR #353 at `ed566f3198e236c54ba18049181016536f56d456`; native normalization at `6ece82279cb03474ebc79914db572f6ff095d238`  
Repository status: **RH is not treated as established before independent review**

## 1. The producer

For every real \(X\ge1\), `L-94201` constructs the exact full Möbius component
row
\[
 c_X(j)=\sum_{k\le X/j}\frac{\mu(k)}{\sqrt k}Q_{X/k}(j)
 \qquad(j\ge2)
\]
and proves
\[
 c_X(j)\ge0.
 \tag{T-94200.1}
\]

`L-94202` proves, for the same row,
\[
 C_{c_X}(q)=w_X(q),\qquad
 \Xi_{c_X}(q)=\Omega_X(q),
 \tag{T-94200.2}
\]
and
\[
 \mathcal H(c_X)=J_\Lambda(X).
 \tag{T-94200.3}
\]

Therefore the exact native deficit is
\[
 \boxed{
 \Delta_X(c_X)
 :=J_\Lambda(X)-\mathcal H(c_X)=0
 }
 \tag{T-94200.4}
\]
for every \(X\).

This is stronger than the \(o(\log^2X)\) producer required by the endpoint
consumer.

## 2. The complete prime-power gap

Let
\[
 P_\Lambda(X)
 =\sum_{q\le X}\frac{\Lambda(q)}{\sqrt q}\log\frac Xq
\]
be the smoothed prime-power source used by the ordinary dual, and let
\[
 F_\Lambda(X)=J_\Lambda(X)-P_\Lambda(X).
 \tag{T-94200.5}
\]

Native feasibility of the nonnegative row gives
\[
 \mathcal H(c_X)\le P_\Lambda(X).
 \tag{T-94200.6}
\]
Together with (T-94200.3),
\[
 \boxed{F_\Lambda(X)\le0.}
 \tag{T-94200.7}
\]

Notice the orientation: only an upper bound for \(F_\Lambda\) is needed.

## 3. Prime-square moat

Let
\[
 A(X)=\sum_{p\le X}(\log p)\,r_X(p)
\]
be the prime-only endpoint scalar. The prime-square occupancy theorem gives
unconditionally
\[
 A(X)
 =
 F_\Lambda(X)
 -\frac{C_{\rm pp}}4\log^2X
 +o(\log^2X),
 \tag{T-94200.8}
\]
where
\[
 C_{\rm pp}=-1-\zeta(1/2)
 =\frac12\int_1^\infty\{v\}v^{-3/2}\,dv>0.
 \tag{T-94200.9}
\]

Combining (T-94200.7) with (T-94200.8),
\[
 \limsup_{X\to\infty}\frac{A(X)}{\log^2X}
 \le-\frac{C_{\rm pp}}4<0.
\]
Hence
\[
 \boxed{A(X)<0}
 \tag{T-94200.10}
\]
for every sufficiently large real \(X\).

## 4. Mellin–Landau converse

The frozen endpoint calculation gives
\[
 \widehat A(z)
 =\frac1{z^2}\mathcal G\!\left(z+\frac12\right).
 \tag{T-94200.11}
\]
Every zeta zero
\[
 \rho=\frac12+\delta+i\gamma,\qquad\delta>0,
\]
creates a genuine nonreal singularity at \(z=\delta+i\gamma\). The positive real
axis contains no corresponding singularity after cancellation of the zeta
pole.

If \(A(e^t)\) is eventually one-signed, Landau's one-sign theorem forces the
abscissa singularity to lie on the positive real axis, contradicting the
nonreal rightmost singularity. Thus eventual negativity of \(A\) excludes every
zero with real part greater than \(1/2\).

The functional equation excludes zeros to the left of the critical line.
Therefore
\[
 \boxed{\mathrm{RH}.}
 \tag{T-94200.12}
\]

## 5. Complete dependency graph

```text
parabolic canonical row Q_Y(j)
  -> exact logarithmic spline G_j
  -> initial-prime divisor-cube frontier transport        L-94200
  -> full Möbius row c_X(j)>=0                            L-94201
  -> native ordinary/detail/score saturation              L-94202
  -> zero native deficit
  -> F_Lambda(X)<=0
  -> positive prime-square moat
  -> prime endpoint eventually negative
  -> Mellin-Landau converse
  -> RH.
```

There is no factor-67 recursion, Target–Lorenz tail, Brownian finite
approximant, finite Pick search, Schur port, benchmark comparison with
\(4\sqrt X\), or hidden use of a square-root prime error.

## 6. Novel and imported mathematics

The conclusion-producing new statement is `L-94200`, the finite
initial-prime frontier transport. `L-94201` is its exact specialization to the
full Möbius row.

The following are exact finite algebra and are rederived in the packet:

* the row-spline formula;
* the finite Euler/full Möbius identification;
* ordinary and radix-four saturation;
* the literal-score identity;
* the positive \(Y_4\) dual.

The prime-square moat and Mellin–Landau consumer are pinned to the exact source
heads above and restated with their normalization.

## 7. Hostile review boundary

This theorem is a full unconditional proof **candidate**, not an accepted
resolution. The smallest failure that retracts the proposal is a failure of
the frontier-chain decomposition in `L-94200`.

A reviewer should begin by trying to produce:

1. a negative finite initial-prime row;
2. a divisor-cube residual path not covered by one of the four frontier
   templates;
3. a depleted bracketing reservoir;
4. a sign or normalization mismatch in the endpoint consumer.

Until that reconstruction succeeds, the repository-wide status remains:

```text
T-94200                     PROPOSED COMPLETE
independent acceptance      pending
Riemann Hypothesis          not treated as established
```

# L-91702 — Post-Hall positive sources give an exact positive current-plus-child ledger

Claim ID: `L-91702`  
Status: **PROVED EXACT REDUCTION — ROOT HALL IDENTITY REMAINS THE SOLE ENTRY HYPOTHESIS**  
Created: 2026-08-14  
Frozen construction base: PR `#424`, head `2bd4625bb2e3cf41318be5b22f6f8e8d0827fef1`  
Depends on: retained positive component rows; `L-91545`, `L-91559`, `L-91562`, `L-91621`, `L-91622`  
Repairs the root-current interface diagnosed in the independent review of PR `#447`  
RH status: **unproved**

## 1. Positive post-Hall data

Let `m>=1` be an integer contraction; the intended reset has `m=67`.  Let
`tau` range over finitely or countably many positive packet types.  For each
`tau`, assume:

- a positive finite source measure `c_tau(n)>=0`;
- a nonnegative row coefficient `kappa_tau(n)>=0`;
- a positive row bonus `B_tau(j)>=0`;
- the exact positive component row `Q_Y(j)` for `Y>=1`.

At endpoint `X`, define the canonical parent row

\[
 R_{\tau,X}(c_\tau)(j)
 =\sum_n c_\tau(n)\kappa_\tau(n)n^{-1/2}Q_{X/n}(j),
 \tag{L-91702.1}
\]

with causal value zero when `X/n<1`.  Restrict the child source by

\[
 c_\tau^{\rm ch}=c_\tau\mathbf1_{n\le X/m}
 \tag{L-91702.2}
\]

and put

\[
 R_{\tau,X/m}(c_\tau^{\rm ch})(j)
 =\sum_{n\le X/m}
 c_\tau(n)\kappa_\tau(n)n^{-1/2}Q_{X/(mn)}(j).
 \tag{L-91702.3}
\]

The sole root-entry hypothesis is the **literal row identity**

\[
 \boxed{
 R_{\rm nat,X}
 =\sum_\tau R_{\tau,X}(c_\tau)+\sum_\tau B_\tau.
 }
 \tag{L-91702.4}
\]

Every term in (L-91702.4) is a row vector, not merely a target or score scalar.

## 2. Canonical current row

Define

\[
 \boxed{
 R_{\rm cur,X}
 =\sum_\tau
  \left[R_{\tau,X}(c_\tau)
       -R_{\tau,X/m}(c_\tau^{\rm ch})
       +B_\tau\right].
 }
 \tag{L-91702.5}
\]

For each active child source node, the parent and child quotients satisfy

\[
 \frac Xn\ge\frac{X}{mn}.
\]

Endpoint monotonicity of the component row, proved in `L-91559`, gives

\[
 Q_{X/n}(j)-Q_{X/(mn)}(j)\ge0.
 \tag{L-91702.6}
\]

For a source node excluded by (L-91702.2), the current contribution is simply
`Q_(X/n)>=0`.  Since all source and row coefficients and all bonuses are
nonnegative,

\[
 \boxed{R_{\rm cur,X}(j)\ge0\qquad(j\ge2).}
 \tag{L-91702.7}
\]

No scalar complement argument is used.

## 3. Exact one-use row identity

Put

\[
 R_{\rm ch,X/m}
 =\sum_\tau R_{\tau,X/m}(c_\tau^{\rm ch}).
 \tag{L-91702.8}
\]

Substitution of (L-91702.4) into (L-91702.5) gives

\[
 \boxed{
 R_{\rm nat,X}=R_{\rm cur,X}+R_{\rm ch,X/m}.
 }
 \tag{L-91702.9}
\]

Every source coefficient appears once: either in a parent-minus-child current
difference and in its unique child, or only in the current activation frontier.
Every bonus is current-generation only.

## 4. Ordinary and radix-four capacities

For one component row, `L-91559` proves the exact ordinary response

\[
 C_Y(q)=q^{-1/2}H(Y/q)
 \tag{L-91702.10}
\]

and exact radix-four response

\[
 \Theta_Y(q)
 =q^{-1/2}[H(Y/q)-H(Y/(4q))].
 \tag{L-91702.11}
\]

Both are nonnegative and nondecreasing in `Y`.  Applying ordinary response to
(L-91702.9) gives

\[
 C_{R_{\rm nat,X}}(q)
 =C_{R_{\rm cur,X}}(q)+C_{R_{\rm ch,X/m}}(q).
 \tag{L-91702.12}
\]

Applying the radix-four operator gives

\[
 \mathcal D_4C_{R_{\rm nat,X}}(q)
 =\mathcal D_4C_{R_{\rm cur,X}}(q)
  +\mathcal D_4C_{R_{\rm ch,X/m}}(q).
 \tag{L-91702.13}
\]

The current capacities are nonnegative positive sums of endpoint differences.
Thus, if (L-91702.4) is the exact equality-row identity, the current row consumes
exactly the native capacity left after the canonical child is removed.  There is
no separate root residual-capacity estimate to guess.

## 5. Arbitrary child replacement

Let `d_ch>=0` be any finite row feasible for the exact ordinary and radix-four
capacity of `R_(ch,X/m)`.  Define

\[
 \boxed{d_X=R_{\rm cur,X}+d_{\rm ch}.}
 \tag{L-91702.14}
\]

Then `d_X>=0`, and by (L-91702.12)--(L-91702.13),

\[
 C_{d_X}(q)\le C_{R_{\rm nat,X}}(q),
 \qquad
 \mathcal D_4C_{d_X}(q)
 \le\mathcal D_4C_{R_{\rm nat,X}}(q).
 \tag{L-91702.15}
\]

The child is inserted at the same literal row indices.  No affine row dilation,
colored column, fractional physical column, or duplicated endpoint port occurs.

## 6. Exact literal score ledger

Let

\[
 \mathcal E(Y)=\sum_jQ_Y(j)G_j.
 \tag{L-91702.16}
\]

Linearity gives

\[
 \boxed{
 \begin{aligned}
 \mathcal S(R_{\rm cur,X})
 ={}&\sum_{\tau,n}c_\tau(n)\kappa_\tau(n)n^{-1/2}
 \left[\mathcal E(X/n)
 -\mathbf1_{n\le X/m}\mathcal E(X/(mn))\right]\\
 &+\sum_\tau\mathcal S(B_\tau),
 \end{aligned}}
 \tag{L-91702.17}
\]

and

\[
 \mathcal S(R_{\rm nat,X})
 =\mathcal S(R_{\rm cur,X})
  +\mathcal S(R_{\rm ch,X/m}).
 \tag{L-91702.18}
\]

Hence every inherited score difference is paid by the literal parent-minus-child
component entropy, while bonuses are favorable current entropy.  The fixed-67
score comparison and packet envelope of `L-91553/L-91622` apply directly.

## 7. What this changes in the proof DAG

The root-current problem is not

```text
prove that an unnamed scalar complement is positive;
```

but the single literal identity (L-91702.4).  Once that identity is reconstructed
from the finite equality row, the controlled cocycle and target Hall, all of the
following are automatic:

```text
current-row coefficient positivity;
ordinary residual capacity;
radix-four residual capacity;
one-use child placement;
exact literal score telescope;
fixed-67 recursive packet envelope.
```

In particular, the direct-row route does not require an outer B-spline,
quantization collar, finite/continuum mismatch, terminal omission or common-port
packet to prove the recursive current ledger.  Those objects may remain as an
independent construction, but they are not part of (L-91702.9).

## 8. Boundary

This theorem does not prove (L-91702.4).  The exact finite source identity,
controlled one-prime cocycle, Hall transport, and row-profile ordering must all be
reconstructed on one frozen commit.  `O-91703` gives the resulting single-equation
review target.

```text
post-Hall positive sources                         HYPOTHESIS
literal parent Hall row identity                   HYPOTHESIS / ROOT GATE
canonical current row                              EXPLICIT
current-row positivity                             EXACT
ordinary/detail current-child telescope            EXACT
arbitrary child replacement                        EXACT
literal score telescope                            EXACT
Riemann Hypothesis                                 UNPROVEN
```

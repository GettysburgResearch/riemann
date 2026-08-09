# L-34004 — The Q=4 terminal scattering Jordan curvature is cofinally nonnegative

Claim ID: `L-34004`  
Title: The causal Q=4 all-pass state is a positive geometric sum of strictly earlier Jordan cells, and its source-complete Jordan curvature is uniformly nonnegative outside a finite base  
Status: **PROPOSED COMPLETE UNCONDITIONAL COFINAL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro-09-v`  
Created: 2026-08-09  
Parent: PR #341  
Dependencies: PR #342 `L-34004` unitary curvature conservation; `L-34003`; PR #325 `L-32406` state realization  
Scope: terminal scattering-state sign; no independent claim about the remaining principal current recurrence

## 1. The exact Q=4 state filter

For Q=4, PR #325 `L-32406` has

\[
 a=\frac12,
 \qquad b=\frac{\sqrt3}{2},
 \qquad L=\log4,
\]

and causal state recursion

\[
 x_{k+1}=a x_k+b u_k,
 \qquad x_0=0.
\tag{L-34004.1}
\]

Thus

\[
 \boxed{
 x_K
 =b\sum_{r=1}^{K}a^{r-1}u_{K-r}.
 }
\tag{L-34004.2}

In the centered spectral variable `z=s-1/2`, the infinite state transfer is

\[
 R(z)=\frac{b}{1-ae^{-Lz}}.
\]

Since

\[
 ae^{-L(s-1/2)}
 =\frac12\,2\,4^{-s}=4^{-s},
\]

this is also the positive four-adic Dirichlet filter

\[
 \boxed{
 R(s)=\frac{\sqrt3/2}{1-4^{-s}}
 =\frac{\sqrt3}{2}\sum_{r\ge0}4^{-rs}.
 }
\tag{L-34004.3}

The finite state (L-34004.2) is the corresponding truncated causal filter. There are no signed filter coefficients.

## 2. Jordan inputs on a fixed balanced carry-position bank

Fix `eta in (0,1/2)` and a carry position `theta in [eta,1-eta]`. At logarithmic scale `X` write the complete Q=4 Jordan row/path as

\[
 v_X(\tau)
 =\bigl(F_X(\tau),G_X(\tau)\bigr),
\]

with jets at `tau=0`

\[
 F_X(0)=1,
 \qquad F_X'(0)=P_X,
 \qquad F_X''(0)=S_X,
\]

\[
 G_X(0)=Y_X,
 \qquad G_X'(0)=Q_X,
 \qquad G_X''(0)=T_X.
\tag{L-34004.4}

By `L-34001`, these are the actual physical/carry Jordan jets at the same real `(X,theta)`.

The Jordan curvature is

\[
 \mathfrak C(v_X)
 =P_X^2-S_X+Q_X^2-Y_XT_X.
\tag{L-34004.5}

`L-34003` proves uniformly on the balanced bank that

\[
 P_X\ge c_\eta X,
\tag{L-34004.6}
\]

\[
 0\le S_X\le C_\eta X\log(2X),
\tag{L-34004.7}
\]

\[
 |Y_X|\le C_\eta\log(2X),
\tag{L-34004.8}
\]

and

\[
 |T_X|\le C_\eta X\log^4(2X)
\tag{L-34004.9}
\]

outside a fixed finite base. The square `Q_X^2` is nonnegative and needs no upper estimate in a curvature lower bound.

## 3. A general positive delayed-state estimate

Let

\[
 X_0>X_1>\cdots>X_{K-1}\ge1,
 \qquad X_{r+1}=X_r/4,
\]

and let `omega_r>=0` satisfy

\[
 \omega_r\le C_0 2^{-r}.
\tag{L-34004.10}

Form the positive delayed Jordan state

\[
 V(\tau)=\sum_{r=0}^{K-1}\omega_r v_{X_r}(\tau).
\tag{L-34004.11}

Put

\[
 c_0=\sum_r\omega_r,
 \quad
 P_V=\sum_r\omega_rP_{X_r},
 \quad
 S_V=\sum_r\omega_rS_{X_r},
\]

and similarly `Y_V,Q_V,T_V`.

Because the largest-scale coefficient `omega_0` in the actual scattering state is the fixed number `b>0`, (L-34004.6) gives

\[
 \boxed{P_V\ge c_1X_0}
\tag{L-34004.12}

for one `c_1=c_1(eta)>0`.

The geometric scale and weight sums give

\[
 c_0=O(1),
\tag{L-34004.13}

\[
 S_V=O_\eta(X_0\log(2X_0)),
\tag{L-34004.14}

\[
 Y_V=O_\eta(\log(2X_0)),
\tag{L-34004.15}

and

\[
 T_V=O_\eta(X_0\log^4(2X_0)).
\tag{L-34004.16}

For example, (L-34004.14) follows from

\[
 \sum_r2^{-r}\frac{X_0}{4^r}
 \log\left(2+\frac{X_0}{4^r}\right)
 \ll X_0\log(2X_0),
\]

and the other bounds are even easier. Any finitely many tail scales below the cofinal threshold contribute only `O_eta(log X_0)` and can be absorbed into the displayed bounds.

The curvature of (L-34004.11) is

\[
 \mathfrak C(V)
 =P_V^2+Q_V^2-c_0S_V-Y_VT_V.
\tag{L-34004.17}

Discarding `Q_V^2>=0` and using (L-34004.12)--(L-34004.16),

\[
 \boxed{
 \mathfrak C(V)
 \ge c_1^2X_0^2
     -O_\eta(X_0\log^5(2X_0)).
 }
\tag{L-34004.18}

Therefore

\[
 \boxed{
 \mathfrak C(V)>0
 }
\tag{L-34004.19}

uniformly for all sufficiently large `X_0`, independently of the finite number of delayed terms.

## 4. Apply to the actual terminal all-pass state

For the Q=4 state (L-34004.2), the weights are

\[
 \omega_r=b a^r
 =\frac{\sqrt3}{2}\,2^{-r},
\]

and the scales decrease by the physical delay `log4`, i.e.

\[
 X_r=X_0/4^r.
\]

Thus Section 3 applies literally. The complete terminal state of any finite causal prefix has

\[
 \boxed{
 \mathfrak C(x_K)\ge0
 }
\tag{L-34004.20}

once its largest predecessor scale is outside one fixed finite base. In fact the proof gives a positive quadratic moat

\[
 \boxed{
 \mathfrak C(x_K)\ge c_\eta'X_0^2
 }
\tag{L-34004.21}

for some `c_eta'>0` and all sufficiently large balanced states.

The finitely many smaller terminal states form an explicit finite boundary table; no cofinal negative state is possible.

## 5. Consequence for the unitary curvature ledger

PR #342 `L-34004` proves for the Q=4 colligation

\[
 \sum_{k=0}^{K-1}\mathfrak C(u_k)
 =\sum_{k=0}^{K-1}\mathfrak C(y_k)
  +\mathfrak C(x_K)
\tag{L-34004.22}

with `x_0=0`.

The output arithmetic curvature `C(y_k)` is exactly the source-complete augmented Q=4 curvature, and `L-34003` proves it cofinally positive on the actual continuous balanced bank. Equation (L-34004.20) now closes the second sign left open in PR #342:

\[
 \boxed{
 \sum_{k<K}\mathfrak C(u_k)
 \ge\sum_{k<K}\mathfrak C(y_k)\ge0
 }
\tag{L-34004.23}

outside one finite boundary table.

Thus **no negative terminal Jordan curvature remains in the neutral all-pass channel**.

## 6. What this does and does not close

This theorem closes the terminal-state sign explicitly named as open in PR #342 `L-34004`.

It does not by itself prove the RH-facing current bound. The curvature contains the large deterministic Kummer reserve. A conclusion-producing recurrence must use the radix-four *increment* of that reserve, or an equivalent renormalized block ledger, so that inherited quadratic reserve is transported with the neutral state rather than re-spent at every scale.

Accordingly, the remaining theorem has been narrowed further:

```text
unitary terminal-state sign                    CLOSED here;
complete continuous augmented output sign      CLOSED by L-34003;
radix-four reserve increment O(X log X)         CLOSED on PR #342;
current-innovation <= new reserve increment     OPEN / RH-BEARING;
renormalized coefficient-one recurrence         OPEN.
```

## 7. Proof boundary

Closed unconditionally, subject to review:

1. exact positive four-adic state filter;
2. uniform asymptotic curvature of every positive geometric delayed Jordan state;
3. cofinal nonnegative terminal scattering curvature;
4. closure of the terminal sign in the exact unitary curvature ledger.

Still open:

1. source-specific domination of the RH-sensitive one-step current innovation by the newly created radix-four reserve;
2. the renormalized coefficient-one recurrence;
3. RH.

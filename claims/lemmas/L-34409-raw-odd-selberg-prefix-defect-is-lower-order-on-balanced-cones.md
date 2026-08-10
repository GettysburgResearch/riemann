# L-34409 — The raw odd-Selberg prefix defect is lower order on fixed balanced cones

Claim ID: `L-34409`  
Title: The signed raw-prefix terms in the corrected odd relative curvature are only `O_eta(n)`, so the unconditional `Theta_eta(n log n)` reserve increment still absorbs them cofinally  
Status: **PROPOSED COMPLETE UNCONDITIONAL COFINAL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring/review agent: `gpt56-pro`  
Created: 2026-08-10  
Dependencies: `R-34402`, corrected `L-34407`; PR #346 `L-34404`; classical Selberg symmetry and the elementary Chebyshev bound  
Scope: every fixed balanced cone, cofinally; no all-row sign and no upper/dissipative recurrence

## 1. Corrected raw-prefix term

Retain

\[
 C_{\rm odd}
 =\Lambda_{\rm odd}\log
  +\Lambda_{\rm odd}*\Lambda_{\rm odd}\ge0
\]

and its raw prefix

\[
 H_{\rm odd}^{\rm raw}(x)
 =\sum_{m\le x}C_{\rm odd}(m).
\tag{L-34409.1}
\]

For a row `e=(n,j)`, with `k=n-j`, define

\[
\boxed{
 D_C(e)
 =H_{\rm odd}^{\rm raw}(n)
  -H_{\rm odd}^{\rm raw}(j)
  -H_{\rm odd}^{\rm raw}(k).
}
\tag{L-34409.2}

`R-34402` proves that `D_C` is not the positive Selberg carry row and may be negative.  Corrected `L-34407` gives

\[
 T_{\rm odd}(4e)-T_{\rm odd}(e)
 =D_C(2e)+D_C(4e).
\tag{L-34409.3}

The purpose of this theorem is not to restore a pointwise sign.  It proves that the entire signed correction is one order below the critical moat on balanced rows.

## 2. Ordinary Selberg symmetry

Let

\[
 C=\Lambda\log+\Lambda*\Lambda
\]

be the ordinary Selberg sequence. The classical Selberg symmetry formula is

\[
\boxed{
 \sum_{m\le x}C(m)
 =2x\log x+O(x).
}
\tag{L-34409.4}

Only this unconditional form is needed.  No zero-free region or RH input occurs.

## 3. Removing the prime two costs only `O(x)`

Write

\[
 \Lambda=\Lambda_{\rm odd}+\lambda_2,
\]

where

\[
 \lambda_2(n)
 =\log2\,\mathbf1_{n=2^a,\ a\ge1}.
\]

Expanding the two Selberg sequences,

\[
\boxed{
 C-C_{\rm odd}
 =\lambda_2\log
  +2\Lambda_{\rm odd}*\lambda_2
  +\lambda_2*\lambda_2.
}
\tag{L-34409.5}

Every term on the right is nonnegative.

The first and third terms are supported on powers of two and have total mass

\[
 O(\log^2(2x)).
\tag{L-34409.6}

For the mixed term, divisor switching gives

\[
\begin{aligned}
 \sum_{n\le x}(\Lambda_{\rm odd}*\lambda_2)(n)
 &=\log2\sum_{a\ge1}
   \psi_{\rm odd}(x/2^a),
\end{aligned}
\]

where

\[
 \psi_{\rm odd}(y)=\sum_{m\le y}\Lambda_{\rm odd}(m).
\]

The elementary Chebyshev estimate `psi_odd(y)<=psi(y)<<y` therefore gives

\[
\boxed{
 \sum_{n\le x}(\Lambda_{\rm odd}*\lambda_2)(n)
 =O(x).
}
\tag{L-34409.7}

Combining (L-34409.5)--(L-34409.7),

\[
\boxed{
 \sum_{m\le x}(C(m)-C_{\rm odd}(m))=O(x).
}
\tag{L-34409.8}

Equations (L-34409.4) and (L-34409.8) yield the odd-prime raw-prefix asymptotic

\[
\boxed{
 H_{\rm odd}^{\rm raw}(x)
 =2x\log x+O(x).
}
\tag{L-34409.9}

## 4. Uniform balanced raw defect

Fix

\[
0<\eta<\tfrac12,
\qquad
\eta n\le j\le(1-\eta)n,
\]

and put

\[
 \alpha=j/n,
 \qquad
 \beta=1-\alpha,
\]

\[
 \mathsf H(\alpha)
 =-\alpha\log\alpha-\beta\log\beta.
\]

Using (L-34409.9) at `n,j,k`, uniformly on the fixed cone,

\[
\begin{aligned}
 D_C(e)
 &=2[n\log n-j\log j-k\log k]+O_\eta(n)\\
 &=\boxed{
 2n\mathsf H(\alpha)+O_\eta(n).
 }
\end{aligned}
\tag{L-34409.10}

In particular there is a constant `K_eta` such that

\[
\boxed{
 |D_C(e)|\le K_\eta n
}
\tag{L-34409.11}

for every row in the cone after enlarging the constant to cover a finite base.

Applying this to the aligned rows `2e` and `4e`,

\[
\boxed{
 D_C(2e)+D_C(4e)=O_\eta(n).
}
\tag{L-34409.12}

No sign is asserted.

## 5. Cofinal positivity of the corrected relative curvature

Corrected `L-34407` gives the exact scale-four vector curvature

\[
 \mathfrak C(W_e^{\rm odd})
 =\Delta_4R_{\rm odd}(e)
  +|I_{\rm odd}(e)|^2
  +2D_C(2e)+2D_C(4e).
\tag{L-34409.13}

PR #346 `L-34404` proves that, uniformly on the same fixed cone and outside a finite base,

\[
\boxed{
 \Delta_4R_{\rm odd}(e)
 \ge12h_\eta n\log n,
}
\tag{L-34409.14}

where

\[
 h_\eta
 =\min_{\eta\le a\le1-\eta}
 [-a\log a-(1-a)\log(1-a)]>0.
\]

By (L-34409.12), for one constant `K'_eta`,

\[
 2D_C(2e)+2D_C(4e)
 \ge-K'_\eta n.
\tag{L-34409.15}

Hence

\[
\boxed{
 \mathfrak C(W_e^{\rm odd})
 \ge |I_{\rm odd}(e)|^2
    +12h_\eta n\log n-K'_\eta n.
}
\tag{L-34409.16}

For all sufficiently large `n`, therefore,

\[
\boxed{
 \mathfrak C(W_e^{\rm odd})
 \ge |I_{\rm odd}(e)|^2
    +6h_\eta n\log n
 >0.
}
\tag{L-34409.17}

Thus the source-complete relative curvature still contains the complete odd-current innovation square with coefficient one and retains a positive critical-scale moat **cofinally on every fixed balanced cone**.

The conclusion is weaker than the false all-row positive staircase, but it is exactly the scope required by the balanced physical-block route.

## 6. All-dyadic extension at fixed depth

For any fixed `r>=1`, `R-34402` gives

\[
 T_{\rm odd}(2^re)-T_{\rm odd}(e)
 =\sum_{a=1}^rD_C(2^ae).
\]

Every term on the right is `O_(r,eta)(n)` by (L-34409.11). Therefore the complete signed source correction at any fixed dyadic depth remains

\[
 O_{r,\eta}(n).
\tag{L-34409.18}

The scalar odd reserve difference at fixed depth has a positive `c_(r,eta)n log n` main term by the same Stirling/Selberg calculation used in `L-34404`. Consequently every fixed-depth corrected odd relative curvature is cofinally positive and contains its current innovation square with coefficient one.

No uniformity as `r->infinity` is claimed.

## 7. What is now closed and what is not

The second source-order correction changes the ledger but not the cofinal scale separation:

```text
raw second-current boundary      signed, can be negative, O_eta(n);
odd reserve increment            positive Theta_eta(n log n);
corrected relative curvature     >= innovation^2 + positive moat cofinally.
```

This restores the local balanced containment needed for a reflected attack.  It does **not** provide an upper estimate for the curvature. Positivity remains a storage statement, not dissipation.

## 8. Proof boundary

Closed here, subject to review:

1. odd Selberg raw-prefix asymptotic `2x log x+O(x)`;
2. explicit `p=2` correction of size `O(x)`;
3. balanced raw-defect bound `O_eta(n)`;
4. absorption by the existing `Theta_eta(n log n)` odd reserve increment;
5. cofinal corrected curvature domination of `|I_odd|^2`;
6. the fixed-depth all-dyadic analogue.

Open:

1. a finite all-row base for the corrected curvature;
2. source-convolved reflected dissipative placement;
3. an upper fixed-delay recurrence;
4. global subpower pole-current energy;
5. RH.

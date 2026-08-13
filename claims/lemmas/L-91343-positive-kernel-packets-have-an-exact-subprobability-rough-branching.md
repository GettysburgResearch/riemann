# L-91343 — Positive kernel packets admit an exact subprobability rough branching in target, score, and every finite row

Claim ID: `L-91343`  
Status: **PROVED EXACT POSITIVE-KERNEL BRANCHING THEOREM — SIGNED ARITHMETIC ENTRY REMAINS OPEN**  
Created: 2026-08-12  
Depends on: retained positive component rows `L-91112.25`; `L-91329`; `L-91339`; `T-91302`  
RH status: **unproved**

## 1. Positive target and score kernels

For real `x>=1` and integer `n<=x`, put

\[
 \boxed{
 W_\Psi(x,n)=\frac{4\sqrt x}{n}-\frac3{\sqrt n},
 \qquad
 W_S(x,n)=\frac{5\sqrt x}{n}-\frac3{\sqrt n}.
 }
\tag{L-91343.1}

Both are strictly positive. Their difference is

\[
 \boxed{
 W_S(x,n)-W_\Psi(x,n)=\frac{\sqrt x}{n}>0.
 }
\tag{L-91343.2}

For a positive finite source measure `nu`, define

\[
 \mathfrak T_x(\nu)=\sum_{n\le x}\nu(n)W_\Psi(x,n),
 \qquad
 \mathfrak S_x(\nu)=\sum_{n\le x}\nu(n)W_S(x,n).
\tag{L-91343.3}

## 2. Arbitrary subprobability choice of rough children

For each source node `n`, let `mathcal B(n)` be any finite or countable family
of rough labels `b`.  Attach to `b` an integer scale

\[
 p_b\ge83
\]

and a measurable weight

\[
 \theta_b(n)\ge0
\]

such that

\[
 \boxed{
 \theta_b(n)=0\quad\text{unless }n\le x/p_b,
 \qquad
 \sum_{b\in\mathcal B(n)}\theta_b(n)\le1.
 }
\tag{L-91343.4}

Define the child measure at endpoint `x/p_b` by

\[
 \boxed{
 \nu_b(n)=\theta_b(n)\nu(n).
 }
\tag{L-91343.5}

The unused source mass is not required to be assigned a rough color.

The least-prime hazard weights of `L-91336` are one canonical choice satisfying
(L-91343.4).  A deterministic first-active-prime policy is another.

## 3. Exact target partition with positive residual

For one active child,

\[
 W_\Psi(x/p_b,n)\le W_\Psi(x,n),
\]

because the kernel increases with the endpoint. Therefore the pointwise residual

\[
 \boxed{
 R_\Psi(x,n)
 =W_\Psi(x,n)
  -\sum_b\theta_b(n)W_\Psi(x/p_b,n)
 }
\tag{L-91343.6
}

is nonnegative. Consequently

\[
 \boxed{
 \mathfrak T_x(\nu)
 =\sum_b\mathfrak T_{x/p_b}(\nu_b)
  +\sum_n\nu(n)R_\Psi(x,n).
 }
\tag{L-91343.7
}

This is an exact positive target decomposition.  The parent target is used once.

## 4. Exact score partition and favorable local surplus

Define similarly

\[
 R_S(x,n)
 =W_S(x,n)
  -\sum_b\theta_b(n)W_S(x/p_b,n).
\tag{L-91343.8}

It is nonnegative by the same endpoint monotonicity.  More strongly, using
(L-91343.2),

\[
\begin{aligned}
 R_S(x,n)-R_\Psi(x,n)
 &={\sqrt x\over n}
   \left[1-\sum_b{\theta_b(n)\over\sqrt{p_b}}\right]\\
 &\ge {\sqrt x\over n}
   \left[1-{1\over\sqrt{83}}\sum_b\theta_b(n)\right]>0.
\end{aligned}
\tag{L-91343.9}

Hence

\[
 \boxed{
 \mathfrak S_x(\nu)
 =\sum_b\mathfrak S_{x/p_b}(\nu_b)
  +\sum_n\nu(n)R_S(x,n),
 }
\tag{L-91343.10
}

and the current-generation residual has score at least target.  It creates no
positive signed score loss.

## 5. Every exact finite row has the same positive decomposition

For real `Y>=1` and integer row `j>=2`, retain the exact positive component row

\[
 Q_Y(j)=(j+1)\Delta^2\left[\frac{S_Y(j)}{j-1}\right]\ge0.
\tag{L-91343.11}

On every activation cell,

\[
 Q_Y(j)=C_{j,N}\log Y-D_{j,N},
 \qquad C_{j,N}>0.
\]

Each entering summand vanishes at activation, so `Q_Y(j)` is continuous; its
cell derivative is `C_(j,N)/Y>0`.  Therefore

\[
 \boxed{
 Y_1\le Y_2\Longrightarrow Q_{Y_1}(j)\le Q_{Y_2}(j).
 }
\tag{L-91343.12}

For one source node define its parent row atom

\[
 \mathcal R_{x,n}(j)=n^{-1/2}Q_{x/n}(j).
\tag{L-91343.13}

Since `x/(p_bn)<=x/n`, the residual

\[
 \boxed{
 R_j(x,n)
 =\mathcal R_{x,n}(j)
  -\sum_b\theta_b(n)\mathcal R_{x/p_b,n}(j)
 \ge0.
 }
\tag{L-91343.14
}

Thus the positive parent row vector decomposes exactly as

\[
 \boxed{
 d_x^\nu(j)
 =\sum_b d_{x/p_b}^{\nu_b}(j)
  +\sum_n\nu(n)R_j(x,n),
 }
\tag{L-91343.15
}

with every coefficient nonnegative.  Applying the nonnegative ordinary carry
matrix preserves the decomposition columnwise.

## 6. Radix-four and finite assembly

At continuum level, attach the positive factor-four endpoint block to every
source submeasure and disintegrate the target before discretization.  Equation
(L-91343.7) is a positive source partition, so the Markov transport of
`L-90028` partitions the corresponding detail target without overlap.

Push all children into the parent endpoint coordinate, sum them there, and
quantize the total measure once as in `L-91329`.  The finite mismatch, positive
B-spline collar and terminal annulus are then charged once by
`L-91114/L-91115`; no finite child is evaluated at a fractional column.

Therefore the entire positive-kernel phase is compatible with ordinary and
radix-four physical capacities.

## 7. Subprobability score coefficients

If a child packet is normalized, its transfer coefficient is its source mass.
From (L-91343.4), the child masses form a subprobability partition pointwise and
hence after integration.  In the canonical least-prime choice,

\[
 \sum_b\theta_b(n)\le1.
\]

Every child endpoint satisfies

\[
 \boxed{
 x/p_b\le x/83<c_0x,
 }
\tag{L-91343.16
}

because `1/83<c_0`.  Equations (L-91343.10) and (L-91343.15) therefore supply the
exact hypotheses of the substochastic branching consumer `T-91302`, with no
positive local score debt beyond the already bounded finite collar.

## 8. What this closes and what it does not

Once an arithmetic reset packet has been represented by one positive measure in
the `W_Psi/W_S/Q` kernel cone, **all subsequent rough branching is closed**:

```text
source partition                 exact / positive;
target partition                 exact / one use;
score transfer                   coefficient one / favorable residual;
every exact finite row           nonnegative;
child weights                    subprobability;
endpoint contraction             factor at least 83;
finite physical assembly         sum before quantization.
```

The theorem does not prove that the complete nonterminal signed rough-prime
forcing enters this positive kernel cone.  `L-91340/L-91341` provide that entry
on one certified finite reset window, and `L-91342` provides it on the terminal
`P_79` window.  The remaining arithmetic statement is the source-faithful splice
from the exact delayed rough renewal to one of these positive entries.

## 9. Proof boundary

```text
positive-kernel rough source partition             EXACT
positive target and score residuals                 EXACT
strict local score surplus                          EXACT
every component row partition                       EXACT
subprobability child ledger                         EXACT
factor-83 contraction                               EXACT
sum-before-quantize physical assembly               AVAILABLE
positive-kernel all-generation recursion            CLOSED
signed arithmetic -> positive-kernel entry          OPEN / RH-BEARING
Riemann Hypothesis                                   UNPROVEN
```
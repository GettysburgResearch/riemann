# T-91562 — Actual-entropy substochastic typed branching closes the score consumer

Claim ID: `T-91562`  
Status: **PROVED ABSTRACT ACTUAL-LOSS CONSUMER / SOURCE-SPECIFIC PRODUCER OPEN**  
Created: 2026-08-13  
Depends on: `L-90029`, `L-91560`, `R-91561`; branching algebra  
RH status: **unproved absent the producer hypotheses**

## 1. Typed packet and actual loss

A positive packet at endpoint `X` carries:

\[
 T_X\ge0
 \quad\text{(target mass)},
 \qquad
 S_X\ge0
 \quad\text{(declared native entropy score)},
\]

and a nonnegative finite row `d_X`.  Its actual row entropy is

\[
 \mathcal H(d_X)=\sum_jd_X(j)G_j.
\]

The conclusion-producing packet loss is

\[
\boxed{
 \ell_X=S_X-\mathcal H(d_X).
}
\tag{T-91562.1}
\]

No positivity of `ell_X` is assumed.

## 2. One reset hypothesis

Normalize the parent target to `T_X=1`.  Suppose one reset produces:

- a nonnegative current row `d_0`;
- child packets at endpoints `Y_b<=cX+C_0`;
- child target masses `omega_b>=0` with
  \[
  \sum_b\omega_b\le1;
  \tag{T-91562.2}
  \]
- target, score and row decompositions satisfying
  \[
  1=T_0+\sum_b\omega_b,
  \tag{T-91562.3}
  \]
  \[
  S_X\le S_0+\sum_b\omega_b\widehat S_b+E_X^{\rm ext},
  \tag{T-91562.4}
  \]
  \[
  \mathcal H(d_X)
  \ge\mathcal H(d_0)+
    \sum_b\omega_b\mathcal H(\widehat d_b),
  \tag{T-91562.5}
  \]
  where `widehat` denotes target normalization.

Assume the current physical corridor

\[
 0\le S_0\le C_TT_0
\tag{T-91562.6}
\]

and bounded external collar/port debt

\[
 E_X^{\rm ext}\le C_E.
\tag{T-91562.7}
\]

## 3. Actual loss recurrence

Subtracting (T-91562.5) from (T-91562.4),

\[
\begin{aligned}
 \ell_X
 &\le E_X^{\rm ext}
   +[S_0-\mathcal H(d_0)]
   +\sum_b\omega_b\widehat\ell_{Y_b}\\
 &\le C_E+C_TT_0
   +\sum_b\omega_b\widehat\ell_{Y_b}.
\end{aligned}
\]

Using (T-91562.3),

\[
\boxed{
 \ell_X
 \le C_E+C_T\left(1-\sum_b\omega_b\right)
 +\sum_b\omega_b\widehat\ell_{Y_b}.
}
\tag{T-91562.8}
\]

This is an actual entropy-loss recurrence.  It never identifies source-mass
fraction with the loss of an arbitrary restriction.

## 4. Tree expansion

At depth `k`, the total path target mass is at most one.  The total current
residual target mass at that depth is also at most one.  Therefore (T-91562.8)
charges at most

\[
 C_E+C_T
\]

per depth.

Every endpoint contracts by `c<1`, so the depth is `O(log X)`.  A uniformly
bounded target-normalized base gives

\[
\boxed{
 \sup_{\rm typed\ packets}\inf_{d\ge0}\ell_X(d)
 =O(\log X)
 =o(\log^2X).
}
\tag{T-91562.9}
\]

By `L-90029`, a source-specific producer satisfying the hypotheses proves RH.

## 5. Application to the paired survival/hazard types

For the physical branch corridors of PR #424,

\[
 S\le2T,
\]

and the same inequality holds for every geometric residual.  Thus one may take

\[
 C_T=2.
\]

`L-91560` supplies a capacity-faithful, loss-isometric inclusion of arbitrary
contracted child packings at the same physical indices, avoiding the broken
affine joint of `R-91560`.

For canonical component rows, `L-91561` shows that inherited active residuals
actually have nonpositive local loss.  The crude constant `2` is sufficient for
the abstract theorem.

## 6. Exact remaining producer audit

To apply (T-91562.9) to the native factor-54 packet one must still prove, in one
normalization:

1. the Hall residual declared score is the literal contribution to
   `J_Lambda`;
2. every Hall bonus and endpoint-port row is detail feasible before its entropy
   is counted;
3. current rows occupy only the complementary target capacity after the
   same-index child sum;
4. the collar, top omission and common port are charged once;
5. the finite base is uniform for both hereditary types.

These are finite/source-specific interfaces.  The branching consumer itself is
closed.

```text
actual loss S-H(row)                              NORMATIVE
same-index arbitrary child inclusion              EXACT
physical-corridor local debt <=2 target           EXACT
substochastic tree O(log X)                       EXACT
native Hall/port/detail producer                   OPEN / FINAL AUDIT
Riemann Hypothesis                                UNPROVEN
```

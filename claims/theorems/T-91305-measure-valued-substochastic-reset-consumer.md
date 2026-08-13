# T-91305 — A measure-valued substochastic reset closes the endpoint-score criterion

Claim ID: `T-91305`  
Status: **PROVED CONDITIONAL CONSUMER — PACKET PRODUCER OPEN**  
Created: 2026-08-13  
Depends on: endpoint-score RH consumer `L-90029/T-91302`  
RH status: **unproved absent the producer hypotheses**

## 1. Why scalar branch weights are unnecessary

Let `C_X` be an additive cone of positive source/row packets at endpoint `X`. For a packet `mu in C_X`, let

\[
\mathcal V_X(\mu)
\]

be the infimum endpoint-score loss among its capacity-faithful feasible realizations. Assume the natural properties

\[
\mathcal V_X(c\mu)=c\mathcal V_X(\mu),
\qquad c\ge0,
\tag{T-91305.1}
\]

and

\[
\mathcal V_X(\mu+\nu)
\le\mathcal V_X(\mu)+\mathcal V_X(\nu).
\tag{T-91305.2}
\]

These are positive homogeneity and subadditivity of an infimum over a linear feasible cone. No sign assumption on the numerical value of `V_X` is imposed.

Let `m_X(mu)>=0` be an additive positive mass ledger.

## 2. Measure-valued reset hypothesis

Fix `0<c<1`. Suppose every sufficiently large packet `mu in C_X` admits an exact positive decomposition

\[
\boxed{
\mu=\rho+\sum_b\mu_b
}
\tag{T-91305.3
}

in the complete target, score, row, boundary-port, and physical-capacity coordinates, where:

1. `rho` is a current-generation packet;
2. `mu_b in C_(Y_b)` and
   \[
   Y_b\le cX+C_0;
   \]
3. the child mass is substochastic:
   \[
   \boxed{
   \sum_bm_{Y_b}(\mu_b)
   \le m_X(\mu);
   }
   \tag{T-91305.4
   }
4. the current packet has bounded loss per unit mass:
   \[
   \boxed{
   \mathcal V_X(\rho)
   \le C_1(1+\log\log(3X))^A m_X(\mu).
   }
   \tag{T-91305.5
   }

The sums are measure sums; no child is replaced by a scalar multiple of a native full packet.

## 3. Exact packet recurrence

Subadditivity gives directly

\[
\boxed{
\mathcal V_X(\mu)
\le
C_1(1+\log\log(3X))^A m_X(\mu)
+
\sum_b\mathcal V_{Y_b}(\mu_b).
}
\tag{T-91305.6
}

This is the correct replacement for a recurrence with undefined scalar coefficients `theta_b`. It applies to arbitrary restricted child packets and remains valid when some child losses are negative.

## 4. Tree expansion

Iterate (T-91305.3). At every depth `j`, additivity and (T-91305.4) give

\[
\boxed{
\sum_{|v|=j}m_{X_v}(\mu_v)
\le m_X(\mu).
}
\tag{T-91305.7
}

Every endpoint contracts geometrically and the tree terminates after `O(log X)` levels. Expanding (T-91305.6) therefore yields

\[
\boxed{
\mathcal V_X(\mu)
\le C_{\rm base}m_X(\mu)
+O\!\left(
m_X(\mu)\log X(1+\log\log X)^A
\right).
}
\tag{T-91305.8
}

For the normalized native packet family, assume

\[
\sup_Xm_X(\mu_X^{\rm nat})<\infty.
\tag{T-91305.9
}

Then

\[
\boxed{
\mathcal V_X(\mu_X^{\rm nat})
=O\!\left(
\log X(1+\log\log X)^A
\right)
=o(\log^2X).
}
\tag{T-91305.10
}

The endpoint-score criterion consequently gives RH.

## 5. Relationship with PR #431

The two-atom counterexample in PR #431 correctly shows that source-mass fraction alone does not imply

\[
\mathfrak L(\mu_b)
\le\theta_b\mathfrak L(\mu^{\rm nat}).
\]

The present theorem never uses that inference. It recurses on the actual restricted packet `mu_b` and uses only the additive mass ledger to control the **sum of local debts**.

Thus the scalar normalization objection to `T-91304.6` is removed at the consumer level. What remains is a producer theorem establishing the typed packet identity (T-91305.3), the mass inequality (T-91305.4), and the uniform native-mass bound.

```text
measure-valued tree expansion               EXACT
arbitrary restricted child packets          ALLOWED
negative child losses                       ALLOWED
substochastic mass controls local debt       EXACT
bounded normalized mass -> RH                COMPLETE CONDITIONAL
typed factor-54 packet producer              OPEN / RH-BEARING
Riemann Hypothesis                           UNPROVED
```

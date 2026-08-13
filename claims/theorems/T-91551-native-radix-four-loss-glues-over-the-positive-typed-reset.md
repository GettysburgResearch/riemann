# T-91551 — Abstract native-loss gluing is exact; the factor-54 application was refuted at the source-score interface

Claim ID: `T-91551`  
Status: **ABSTRACT GLUING LEMMA RETAINED; FACTOR-54 APPLICATION REFUTED AS WRITTEN BY `R-91552`**  
Created: 2026-08-13  
Corrected: 2026-08-13  
Depends on: `L-90029`, `T-91101`, `T-91302`, `L-91329`, `R-91552`, `L-91553`  
RH status: **unproved**

> **Correction firewall.** The first version of this theorem identified the
> declared source score of a positive typed packet with the literal entropy
> score of its positive component row.  `R-91552` proves that this is false:
> at quotient `Y=2` the component row has entropy zero while the declared
> source score `5 sqrt(2)-3` is positive.  Therefore the former Sections 5--7
> and the status `candidate complete` are withdrawn.
>
> The algebraic gluing lemma below remains exact.  `L-91553` repairs the local
> inherited-score comparison for the fixed-67 split, but the native unnormalized
> root-amplitude/frontier debt remains load bearing.

## 1. The conclusion-producing native loss

For a nonnegative ordinarily feasible parent row `d`, the native radix-four
score loss is

\[
 \boxed{
 \mathfrak L_X(d)
 =J_\Lambda(X)-\mathcal S_X(d),
 \qquad
 \mathcal S_X(d)=\sum_nd(n)G_n.
 }
 \tag{T-91551.1}
\]

Equivalently, for endpoint weights `lambda_T`,

\[
 \mathfrak L_X(d)
 =\sum_{T=3}^X(1-\lambda_T)H_T.
 \tag{T-91551.2}
\]

`L-90029` proves

\[
 \boxed{
 \mathfrak L_X(d)=o(\log^2X)
 \Longrightarrow \mathrm{RH}.
 }
 \tag{T-91551.3}
\]

Thus every reset must control the **literal entropy score** of its physical row,
not only a source-level proxy.

## 2. Abstract packet loss

Let a positive packet `P` have declared score `J(P)` and positive feasible row
cone `F(P)`.  For `d in F(P)` define

\[
 \boxed{
 \ell(P;d)=J(P)-\mathcal S(d).
 }
 \tag{T-91551.4}
\]

Linearity gives, for `a>=0`,

\[
 \ell(aP;ad)=a\ell(P;d).
 \tag{T-91551.5}
\]

Positive direct sums are subadditive after their feasible rows are added.  No
sign condition on `ell` is required; favorable negative loss remains allowed.

## 3. Exact score-superordinate gluing lemma

Suppose a parent packet with score `J_X` is decomposed into:

- a current positive packet with feasible row `d_0`;
- positive child packets `P_b` with feasible rows `d_b`;
- current debt `E_X>=0`;
- a positive capacity-faithful parent assembly `d_X`.

Assume

\[
 \boxed{
 J_X
 \le E_X+\mathcal S_X(d_0)+\sum_bJ(P_b),
 }
 \tag{T-91551.6}
\]

and

\[
 \boxed{
 \mathcal S_X(d_X)
 \ge\mathcal S_X(d_0)+\sum_b\mathcal S_{Y_b}(d_b).
 }
 \tag{T-91551.7}
\]

Subtracting gives

\[
 \boxed{
 J_X-\mathcal S_X(d_X)
 \le E_X+\sum_b\ell(P_b;d_b).
 }
 \tag{T-91551.8}
\]

This is pure algebra.  It does not compare the loss of a restriction with a
mass fraction of the loss of a different packet.

If `P_b=omega_b P_hat_b`, `d_b=omega_b d_hat_b`, then

\[
 \ell(P_b;d_b)=
 \omega_b\ell(P_hat_b;d_hat_b).
 \tag{T-91551.9}
\]

Thus target masses `omega_b` yield a substochastic recurrence only after
(T-91551.6) has been proved for the literal row entropy.

## 4. Exact entropy kernel of the component row

For the retained positive component row

\[
 Q_Y(n)
 =(n+1)\Delta^2\left[\frac{S_Y(n)}{n-1}\right],
\]

`R-91552` proves

\[
 \boxed{
 \mathcal E(Y)
 :=\sum_{n\ge2}Q_Y(n)G_n
 =\sum_{q=2}^{\lfloor Y\rfloor}
  \frac{\log q}{\sqrt q}\log\frac Yq.
 }
 \tag{T-91551.10}
\]

This is the physical entropy represented by one unit component row.  It is not
identically equal to any affine source score `a sqrt(Y)-b`.

In particular,

\[
 \mathcal E(2)=0,
 \qquad
 5\sqrt2-3>0.
 \tag{T-91551.11}
\]

Therefore source-level score superordination and row positivity do not by
themselves imply (T-91551.6).

## 5. Local fixed-67 repair

`L-91553` proves the exact score-difference domination

\[
 \boxed{
 \mathcal E(Y)-\mathcal E(Y/67)
 \ge5\left(\sqrt Y-\sqrt{Y/67}\right)
 \qquad(Y\ge67).
 }
 \tag{T-91551.12}
\]

Every survival/hazard declared score has affine slope below five.  Hence the
coefficientwise current row `Q_Y-Q_(Y/67)` realizes at least the complete
declared current score difference on every inherited source atom.  Together
with the score-noncontracting affine lift `L-91549`, the inherited child loss
has coefficient one.

For `1<=Y<67` there is no child.  The component entropy is nonnegative and the
physical two-ledger corridor gives a **target-normalized** frontier debt at most
`2`.

Thus the false exact equality is replaced by:

```text
Y>=67: actual row entropy dominates declared score difference;
Y<67: no child, finite target-normalized frontier debt.
```

## 6. Remaining native normalization theorem

The unresolved step is to pass from the normalized frontier estimate to the
literal native recurrence.  One must prove, for the actual Hall residual source
at the root of a factor-54 generation, that

\[
 \boxed{
 \sum_{\tau\in\{s,h\}}
 \sum_{n>X/67}
 c_\tau(n)
 [S_\tau(X/n)-\mathcal E_\tau(X/n)]_+
 \le C(1+\log\log X)^A
 }
 \tag{T-91551.13}
\]

in the exact native normalization, or prove an equivalent generationwise bound.

It is not enough to say that the target-normalized debt is bounded: the root
target amplitude may depend on `X`.

Once (T-91551.13) is established and the resident collar/port terms are added,
the abstract gluing lemma gives the required native substochastic recurrence.
Until then, the factor-54 proof is incomplete.

## 7. Correct boundary

```text
native loss = J_Lambda - literal row entropy          EXACT
positive packet homogeneity                           EXACT
score-superordinate gluing inequality                 EXACT
source score = component-row entropy                  REFUTED / R-91552
fixed-67 inherited score-difference domination        PROVED / L-91553
target-normalized finite frontier debt                 PROVED / L-91553
native unnormalized frontier-amplitude bound           OPEN / RH-BEARING
candidate complete factor-54 proof status              WITHDRAWN
Riemann Hypothesis                                    UNPROVEN
```

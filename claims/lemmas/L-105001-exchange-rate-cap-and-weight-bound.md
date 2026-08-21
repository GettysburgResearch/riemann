# L-105001 — Exchange-rate cap, weight bound, and normalization invariance of the delivery price

Claim ID: `L-105001`
Status: **PROVED EXACT**
Created: 2026-08-21
Agent: claude (external reviewer lane)
RH status: not assumed, not addressed

Used by `T-105000` (Theorems A.1–A.3). Machine checks: `X-105000` S1, S5, S6, S9.

Throughout `T(y) = (4\sqrt y - 3)\mathbf 1_{y\ge1}`, `Z \le Y`, rough prime
`p \ge 67`, `r = p^{-1/2}`.

## 1. Monotone ratio (the one derivative everything uses)

For `p > 1`, the function `w \mapsto T(w)/T(pw)` is strictly increasing on
`w \ge 1`:

```
d/dw [ T(w)/T(pw) ]  =  6 (sqrt p - 1) / ( sqrt w * T(pw)^2 )  >  0.
```

(Verified symbolically, S1. This is the same computation as the profile
derivative `L-99250.6`.) Consequences:

* (a) **Pointwise cap.** `R_{Z|Y}(t) = T(Z/t)/T(Y/t) = T(w)/T((Y/Z)w)` with
  `w = Z/t` is maximal at `t = 1`: `\max_t R_{Z|Y} = T(Z)/T(Y)`. A pointwise
  nonnegative current `(1 - c\,R_{Z|Y})\,dM_Y \ge 0` therefore has coupling
  `c \le T(Y)/T(Z)`. For `Z = Y/p` this cap is the exchange rate
  `q_T(Y,p) = T(Y)/T(Y/p) = \sqrt p\,\dfrac{4\sqrt Y - 3}{4\sqrt Y - 3\sqrt p}
  \ \ge\ \sqrt p` (closed form verified, S5). The extremal current at the cap
  is `T(Y)\,[\,dN_Y - dN_{Y/p}\,]` — exactly the profile increment of
  `L-99250.7`: the strongest free current *is* the profile arrow.

## 2. Weight bound (used for `Pi_G \le \sum 1/p`)

For every `1 \le Z \le Y`:

```
sqrt(Z/Y) * T(Y) - T(Z)  =  3 ( 1 - sqrt(Z/Y) )  >=  0,
```

an exact identity (verified symbolically, S9). Hence
`T(Z)/T(Y) \le \sqrt{Z/Y}`, and with profile monotonicity (`L-99250.8`:
`Q_Z(j)/T(Z) \le Q_Y(j)/T(Y)`, so `Q_Z/Q_Y \le T_Z/T_Y`):

```
w_p := sqrt p * G(Y/p)/G(Y)  <=  1     for  G in { T , Q_.(j) }.
```

Therefore `Pi_G(Y) = \sum_{67\le p\le Y} r_p\,G(Y/p)/G(Y)
= \sum p^{-1}w_p \le \sum_{67\le p\le Y} 1/p`.

## 3. Delivery cap for reserve-injected children

If a child of size `\alpha` at endpoint `Y/p` is paid from a current's mass
(the `L-96651` reserve architecture: `\alpha\,Q_{Y/p}(j) \le \lambda\,(Q_Y(j)
- c\,Q_{Y/p}(j))`), then the block's total first-order delivery obeys

```
lambda*c + alpha  <=  lambda * Q_Y(j)/Q_{Y/p}(j)  =  lambda * q_{Q(j)}(Y,p),
```

independent of how the budget is split between coupling and child. So both
delivery mechanisms — internal coupling and reserve-injection — are governed
by the same exchange rate, and the per-prime price of one unit of native
first-order coefficient `r_p` is `r_p / q_G(Y,p) = p^{-1}\,w_p \le 1/p` of
the unit node budget.

## 4. Normalization invariance of the price

Under the interface cocycle of `R-99820`/`L-99820.3` (`N = \sqrt\cdot`,
`\phi = W/\sqrt\cdot`), the native one-prime coefficient transforms
`p^{-1/2} \to p^{-1}` while the coordinate's exchange rate transforms
`q_W \sim \sqrt p \to q_\phi \sim 1` (deep region: `\phi \to
8(1-67^{-1/2}) - 3\log 67\,\cdot\,y^{-1/2}` is asymptotically constant).
The price is invariant:

```
p^{-1/2} / sqrt p  =  p^{-1} / 1  =  1/p .
```

(Numeric check S6.) The budget obstruction of `T-105000` therefore cannot be
escaped by renormalization: the cocycle moves the coefficient and the
exchange rate together — this is the price-level form of the
`R-99820`/`R-99900` firewall, and it subsumes the observation of `L-99704`
that damping the half-order boundary deletes the detector: the `\sqrt{}`
growth that sets the exchange rate and the `s = 1/2` detector location are
the same normalization (axiom N of `T-105000 §2`).

## 5. Scope

Exact statements only; no asymptotic in this file is used beyond
`Q_Y(j) = 4C_j\sqrt Y + O_j(\log 2Y)` (`R-99440.4`), and §4's `q_\phi \to 1`
is used only for the invariance remark, not in the budget proof.

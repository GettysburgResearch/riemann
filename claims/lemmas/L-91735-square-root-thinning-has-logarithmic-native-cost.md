# L-91735 — Square-root thinning has constant continuum shortfall, logarithmic native root cost, and sparse-dual summable local errors

Claim ID: `L-91735`
Status: **PROVED SCALAR ACCOUNTING ON FROZEN BENCHMARK AND POSITIVE-CORRECTION INPUTS**
Created: 2026-08-15
Depends on: `L-91378`, `L-91733`, `L-91734`, the frozen benchmark bridge `J_Lambda(X)-4sqrt(X)<4log(X)`, frozen top/base/port bounds
Parallel arithmetic input: `L-19885`
Clarifies: the `<4290` statement in PR #479
RH status: **unproved**

## 1. Three score quantities must not be conflated

Let

```text
H_0(X)       = literal score of the unthinned positive root-Hall packet;
4 sqrt(X)    = the fixed continuum equality benchmark;
J_Lambda(X)  = the exact native benchmark.
```

The frozen target/score Hall theorem and score-favorable endpoint quantizer give

\[
 H_0(X)\ge4\sqrt X
\tag{L-91735.1}
\]

before the fixed bounded root corrections are charged.

Put

\[
 K=\left\lfloor\frac X{67}\right\rfloor+1,
 \qquad
 \tau_K=\frac{\sqrt K}{\sqrt K+130}.
\tag{L-91735.2}
\]

## 2. PR #479's constant is valid at the continuum-shortfall scope

From (L-91735.1),

\[
\begin{aligned}
 4\sqrt X-\tau_KH_0(X)
 &\le4\sqrt X(1-\tau_K)\\
 &=4\sqrt X\frac{130}{\sqrt K+130}\\
 &<520\sqrt{\frac XK}.
\end{aligned}
\]

Since `K>X/67` and `sqrt(67)<33/4`,

\[
 \boxed{
 4\sqrt X-\tau_KH_0(X)<4290.
 }
\tag{L-91735.3}
\]

This validates the numerical statement in PR #479 when it is read as an upper
bound on the post-thinning shortfall from the **continuum** benchmark.  It is
not an upper bound on the amount of literal score physically removed from an
arbitrarily large positive packet.

## 3. Translation to the exact native deficit

The endpoint consumer uses

\[
 \Delta_X=J_\Lambda(X)-\mathcal H(d_X),
\]

not `4sqrt(X)-H(d_X)`.  The frozen elementary benchmark bridge is

\[
 \boxed{
 J_\Lambda(X)-4\sqrt X<4\log X.
 }
\tag{L-91735.4}
\]

Combining (L-91735.3) and (L-91735.4),

\[
\begin{aligned}
 J_\Lambda(X)-\tau_KH_0(X)
 &=[J_\Lambda(X)-4\sqrt X]
   +[4\sqrt X-\tau_KH_0(X)]\\
 &<4\log X+4290.
\end{aligned}
\]

Hence

\[
 \boxed{
 J_\Lambda(X)-\tau_KH_0(X)
 <4\log X+4290.
 }
\tag{L-91735.5}
\]

The fixed top omission, finite base packet and narrow uncolored port add only
their frozen bounded charges, while `L-91734` adds `o(1)`.  Thus the square-root
all-column repair remains `O(log X)` in the native normalization.

## 4. Elementary fallback for the incremental safety slack

Independently of (L-91735.4), one has for `X>=2`

\[
 \Lambda(n)\le\log n\le\log X.
\]

The function

\[
 f_X(t)=t^{-1/2}\log(X/t)
\]

is positive and decreasing on `[1,X]`, and

\[
 \int_1^Xf_X(t)dt
 =4\sqrt X-4-2\log X.
\]

Consequently

\[
 \sum_{n\le X}f_X(n)
 \le f_X(1)+\int_1^Xf_X(t)dt
 =4\sqrt X-4-\log X
 <4\sqrt X.
\]

Therefore

\[
 \boxed{
 J_\Lambda(X)<4\sqrt X\log X.
 }
\tag{L-91735.6}
\]

Consequently the *incremental native slack introduced solely by the scalar
safety thinning* obeys

\[
 \boxed{
 (1-\tau_K)J_\Lambda(X)<4290\log X.
 }
\tag{L-91735.7}
\]

This weaker fallback is still `o(log^2 X)`.  It does not replace the baseline
bridge between `J_Lambda` and the continuum equality packet; it only shows that
the safety operation itself is harmless at the endpoint scale.

## 5. Exact support of the radix-four dual

Recall

\[
 Y_4(q)=\sum_{k=0}^{v_4(q)}2^k\Lambda(q/4^k).
\tag{L-91735.8}
\]

Writing `q=2^em` with `m` odd gives

\[
 Y_4(2^e)=
 \bigl(2^{\lceil e/2\rceil}-1\bigr)\log2,
\tag{L-91735.9}
\]

\[
 Y_4(4^vp^a)=2^v\log p
 \quad(p\text{ odd prime}),
\tag{L-91735.10}
\]

and `Y_4(q)=0` otherwise.

Splitting powers of two into even and odd exponents gives

\[
 \sum_{e\ge1}\frac{Y_4(2^e)}{2^{3e/2}}<\frac53.
\]

For odd prime powers,

\[
\begin{aligned}
 \sum_{v\ge0}\sum_{p\ {\mathrm{odd}}}\sum_{a\ge1}
 \frac{2^v\log p}{(4^vp^a)^{3/2}}
 &=\frac43\sum_{p\ {\mathrm{odd}}}\sum_{a\ge1}
   \frac{\log p}{p^{3a/2}}\\
 &\le\frac43\sum_{n\ge2}\frac{\log n}{n^{3/2}}
 <\frac{26}{3}.
\end{aligned}
\]

Thus

\[
 \boxed{
 \sum_{q\ge2}\frac{Y_4(q)}{q^{3/2}}<11.
 }
\tag{L-91735.11}
\]

For `L=log(2X)`, the partial `1/q` weight satisfies

\[
 \boxed{
 \sum_{q\le X}\frac{Y_4(q)}q
 \le3+2L+2L^2.
 }
\tag{L-91735.12}
\]

Indeed the power-of-two contribution is below `3`, and the odd-prime-power
part is bounded by

\[
 \sum_{v\ge0}2^{-v}
 \sum_{p^a\le X/4^v}\frac{\log p}{p^a}
 \le2L(1+L).
\]

## 6. The localized analytic errors have negligible native cost

`L-91733` gives, on every nonterminal physical column,

\[
 |e_X(q)|<\frac{971}{4q\sqrt K}.
\]

Pairing with the positive dual and using (L-91735.12),

\[
 \boxed{
 \sum_{2\le q\le X/4}Y_4(q)|e_X(q)|
 <\frac{971}{4\sqrt K}
   (3+2L+2L^2)
 =o(1).
 }
\tag{L-91735.13}
\]

This includes all columns below `K`.  A terminal `q^{-3/2}` mismatch has
uniformly bounded dual cost by (L-91735.11); with coefficient `285/8` it is
below `392`.  The activation collar and retained-cell interpolation add `o(1)`
by `L-91734`.

## 7. Distinguished-root native cost

Let `r_X>=0` be the unused root detail after the complete current packet and
all full child capacities are reserved once.  On the frozen factor-67 root
packet, Sections 2--6 and the bounded top/base/narrow-port inputs give one
absolute constant `C_root` such that

\[
 \boxed{
 \delta_{\rm root}(X)
 :=\langle Y_4,r_X\rangle
 \le4\log X+C_{\rm root}.
 }
\tag{L-91735.14}
\]

The fixed-window unsigned root mass is uniformly bounded (the retained frozen
bound is `54`), so the causal child-envelope contribution is also uniformly
bounded.  No assertion is made here that every arbitrary mass-one positive
packet admits the same endpoint-frame realization or the same local root
constant.

```text
PR #479 continuum shortfall from 4sqrt(X)          <4290 / valid
native benchmark bridge                            +4 log(X) / frozen exact input
incremental safety slack fallback                  <4290 log(X)
localized all-column error native cost             o(1)
terminal mismatch native cost                      O(1)
activation collar/interpolation native cost        o(1)
distinguished root native cost                     <=4 log(X)+C_root
arbitrary positive packet endpoint realization     not asserted
Riemann Hypothesis                                 unproved
```

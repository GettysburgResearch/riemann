# L-90217 — The improved factor-64 filter has a compact signed Pascal reward: negativity occurs exactly on states `13..63`

Claim ID: `L-90217`  
Status: **PROPOSED COMPLETE EXACT SIGNED-REWARD NORMAL-FORM LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: dyadic filter cone `L-90216`; improved factor-64 polynomial `L-90022/L-90023` on PR #352  
Scope: exact uniform-Pascal reward geometry of the factor-64 polynomial; no inequality paying its negative block and no RH conclusion

## 1. Polynomial and dyadic potential

Let

\[
 \boxed{
 P_{64}^*(t)
 =(1-t)^2(1-t/\sqrt2)(1+t)(1+3t/4+t^2)
 =\sum_{j=0}^{6}q_jt^j.
 }
 \tag{L-90217.1}
\]

The exact coefficients are

\[
\boxed{
\begin{aligned}
(q_0,\ldots,q_6)=(&1,
 -1/4-\sqrt2/2,
 -3/4+\sqrt2/8,\\
&-3/4+3\sqrt2/8,
 -1/4+3\sqrt2/8,
 1+\sqrt2/8,
 -\sqrt2/2).
\end{aligned}}
 \tag{L-90217.2}
\]

Construct the dyadic increment and normalized node potential of `L-90216`:

\[
 a(n)=1-q_j\quad(n=2^j),
 \qquad a(n)=1\quad\text{otherwise},
 \tag{L-90217.3}
\]

\[
 F(m)=\sum_{n\le m}a(n),
 \qquad f(m)=F(m)/m.
 \tag{L-90217.4}
\]

Its arithmetic source is

\[
 \mu*a=\varepsilon-P_{64}^*(\delta_2)*\mu.
 \tag{L-90217.5}
\]

Let

\[
 d_{64}=f-P^{\rm unif}f
 \tag{L-90217.6}
\]

be the uniform-Pascal reward.

## 2. Cumulative coordinates

Put

\[
 S_j=\sum_{\ell=0}^{j}q_\ell,
 \qquad
 A_j=2\sum_{\ell<j}2^\ell S_\ell.
 \tag{L-90217.7}
\]

Exact summation gives

\[
\boxed{
\begin{aligned}
S_0&=1,\\
S_1&=3/4-\sqrt2/2,\\
S_2&=-3\sqrt2/8,\\
S_3&=-3/4,\\
S_4&=-1+3\sqrt2/8,\\
S_5&=\sqrt2/2,\\
S_6&=0,
\end{aligned}}
 \tag{L-90217.8}
\]

and

\[
\boxed{
\begin{aligned}
A_1&=2,\\
A_2&=5-2\sqrt2,\\
A_3&=5-5\sqrt2,\\
A_4&=-7-5\sqrt2,\\
A_5&=-39+7\sqrt2,\\
A_6&=-39+39\sqrt2.
\end{aligned}}
 \tag{L-90217.9}
\]

The last value is positive because `2>1`; more explicitly `39(sqrt(2)-1)>0`.

## 3. Exact reward on every state

By `L-90216`, on the block

\[
 2^j\le m<2^{j+1},
\]

one has

\[
 \boxed{
 m(m-1)d_{64}(m)
 =A_j+(m+1-2^{j+1})S_j.
 }
 \tag{L-90217.10}
\]

This gives a complete sign classification.

### States `2..7`

The first two block endpoint quantities are positive:

\[
 A_1>0,
 \qquad
 A_2=5-2\sqrt2>0.
\]

Hence

\[
 d_{64}(m)>0\qquad(2\le m\le7).
 \tag{L-90217.11}
\]

### States `8..15`

Here

\[
 m(m-1)d_{64}(m)
 =5-5\sqrt2+\frac34(15-m).
 \tag{L-90217.12}
\]

At `m=12`,

\[
 \frac{29}{4}-5\sqrt2>0
 \tag{L-90217.13}
\]

because `29^2>800`. At `m=13`,

\[
 \frac{13}{2}-5\sqrt2<0
 \tag{L-90217.14}
\]

because `169<200`. The expression decreases in `m`, so

\[
 \boxed{
 d_{64}(m)>0\ (8\le m\le12),
 \qquad
 d_{64}(m)<0\ (13\le m\le15).
 }
 \tag{L-90217.15}
\]

### States `16..31`

The reward is largest at the left endpoint because `S_4<0`. There

\[
 16\cdot15\,d_{64}(16)
 =8-\frac{85\sqrt2}{8}<0.
 \tag{L-90217.16}
\]

Thus

\[
 d_{64}(m)<0\qquad(16\le m\le31).
 \tag{L-90217.17}
\]

### States `32..63`

Here `S_5>0`, so the reward increases with `m`; its maximum is

\[
 A_5=-39+7\sqrt2<0.
 \tag{L-90217.18}
\]

Therefore

\[
 d_{64}(m)<0\qquad(32\le m\le63).
 \tag{L-90217.19}
\]

### Every state `m>=64`

Since `S_6=0`, the tail is exact:

\[
 \boxed{
 d_{64}(m)
 =\frac{-39+39\sqrt2}{m(m-1)}>0
 \qquad(m\ge64).
 }
 \tag{L-90217.20}
\]

Combining the five regions,

\[
 \boxed{
 d_{64}(m)<0
 \iff13\le m\le63.
 }
 \tag{L-90217.21}
\]

The negative reward is supported on exactly 51 consecutive parent states.

## 4. Green pairing normal form

Let `M(m)` be the signed uniform-Pascal Green occupation of any finite node source. The exact Markov pairing is

\[
 \boxed{
 \sum_m r^{\rm node}(m)F(m)
 =\sum_{m\ge2}M(m)d_{64}(m).
 }
 \tag{L-90217.22}
\]

By the source identity (L-90217.5), for any carry target `w` with `w(1)=0`, the same scalar is

\[
 \boxed{
 -\sum_{q\ge2}
 [P_{64}^*(\delta_2)*\mu](q)w(q).
 }
 \tag{L-90217.23}
\]

Hence the factor-64 dyadic source has the exact Pascal ledger

\[
\boxed{
\begin{aligned}
\text{positive reserve: }&m=2,\ldots,12\text{ and }m\ge64,\\
\text{negative debt: }&m=13,\ldots,63.
\end{aligned}}
 \tag{L-90217.24}
\]

No negative tail or hidden current-scale remainder remains.

## 5. A finite payment target

If the occupation is nonnegative, the desired sign of (L-90217.22) is equivalent to

\[
\boxed{
 \sum_{m=13}^{63}[-d_{64}(m)]M(m)
 \le
 \sum_{m=2}^{12}d_{64}(m)M(m)
 +(-39+39\sqrt2)
  \sum_{m\ge64}\frac{M(m)}{m(m-1)}.
 }
 \tag{L-90217.25}
\]

Thus importing the factor-64 phase optimization into the Pascal programme does not require a global signed-reward theorem. It requires one explicit **51-state debt payment** by eleven low positive rows and one positive reciprocal-square tail.

This is a substantially narrower interface than generic signed Cycle Debt, although no proof of (L-90217.25) is supplied here.

## 6. Route relationship

- `L-90216` proves that factor-64 is outside the coordinatewise-positive Pascal reward cone.
- This lemma shows the failure is nevertheless compact and exactly localized.
- PR #352 proves the factor-64 annular scalar is an RH criterion with a phase-blind margin.
- A future bridge may therefore target (L-90217.25) directly, retaining all signs until the 51-state block is recombined.

The theorem does not identify the factor-64 prime-endpoint scalar with a completed Pascal occupation certificate; it supplies the exact dyadic-source reward coordinate required by such an adapter.

## 7. Proof boundary

Proved exactly:

- all polynomial and cumulative coordinates in `Q(sqrt(2))`;
- the complete reward formula at every state;
- positivity outside and negativity inside the exact block `13..63`;
- the positive reciprocal-square tail;
- the finite 51-state payment normal form.

Not proved:

- inequality (L-90217.25) for the critical arithmetic occupation;
- SHARP, the factor-64 sign criterion, or RH.

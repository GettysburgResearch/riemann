# L-90219 — Every double-neutral dyadic filter has an unavoidable quantitative Pascal debt

Claim ID: `L-90219`  
Status: **PROPOSED COMPLETE EXACT QUANTITATIVE NO-GO LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: slope identity `L-90218`; block reward formula `L-90216`  
Scope: arbitrary finite dyadic double-neutral filters, including signed rewards; no arithmetic sign theorem and no RH conclusion

## 1. Double-neutral constraint

Let

\[
 Q(t)=\sum_{j=0}^{J}q_jt^j,
 \qquad q_0=1,
 \qquad Q(1)=Q'(1)=0,
 \tag{L-90219.1}
\]

with `J>=2`. Define

\[
 S_j=\sum_{\ell=0}^{j}q_\ell,
 \qquad
 A_j=2\sum_{\ell<j}2^\ell S_\ell
 \tag{L-90219.2}
\]

and let `d` be the corresponding uniform-Pascal reward of `L-90216`.

At the right endpoint of the `j`th dyadic block,

\[
 m_j=2^{j+1}-1,
 \]

one has exactly

\[
 \boxed{
 m_j(m_j-1)d(m_j)=A_j.
 }
 \tag{L-90219.3}
\]

## 2. Exact weighted debt identity

The slope formula of `L-90218` reads

\[
 -Q'(1)
 =\frac12
 +\sum_{j=2}^{J-1}\frac{A_j}{2^{j+1}}
 +\frac{A_J}{2^J}.
 \tag{L-90219.4}
\]

Since `Q'(1)=0`,

\[
 \boxed{
 \sum_{j=2}^{J-1}\frac{A_j}{2^{j+1}}
 +\frac{A_J}{2^J}
 =-\frac12.
 }
 \tag{L-90219.5}
\]

The positive weights in (L-90219.5) sum to

\[
 \sum_{j=2}^{J-1}2^{-j-1}+2^{-J}=\frac14.
 \tag{L-90219.6}
\]

Therefore their weighted average of the block numerators is exactly `-2`.

## 3. Universal signed-reward lower bound

Equation (L-90219.5) immediately gives

\[
 \boxed{
 \min_{2\le j\le J}A_j\le-2.
 }
 \tag{L-90219.7}
\]

Hence every double-neutral filter has an explicit negative reward state:

\[
 \boxed{
 \exists m\le2^{J+1}-1:\quad
 d(m)\le-\frac{2}{(2^{J+1}-1)(2^{J+1}-2)}.
 }
 \tag{L-90219.8}
\]

This bound allows the negative state to lie in the final dyadic block.

### Equality without a positive tail

If every numerator in (L-90219.5) equals `-2`, the recurrence

\[
 A_{j+1}=A_j+2^{j+1}S_j
 \]

forces

\[
 Q(t)=(1-t)^2.
 \tag{L-90219.9}
\]

This is the extremal filter with the smallest possible right-end numerator debt, but it has the permanent negative tail

\[
 d(m)=-\frac2{m(m-1)}\qquad(m\ge4).
 \tag{L-90219.10}
\]

Thus the raw double difference minimizes the local numerator debt by exporting it to every later state.

## 4. Sharpening under nonnegative tail reward

Because `Q(1)=0`, one has `S_J=0`. Therefore the eventual reward is

\[
 d(m)=\frac{A_J}{m(m-1)}\qquad(m\ge2^J).
 \tag{L-90219.11}
\]

Assume this tail is nonnegative:

\[
 A_J\ge0.
 \tag{L-90219.12}
\]

Then the earlier blocks alone must supply at most `-1/2` in (L-90219.5). Their weights sum to

\[
 \sum_{j=2}^{J-1}2^{-j-1}
 =\frac14-2^{-J}
 =\frac14(1-2^{2-J}).
 \tag{L-90219.13}
\]

Consequently, for `J>=3`,

\[
 \boxed{
 \min_{2\le j\le J-1}A_j
 \le-\frac{2}{1-2^{2-J}}.
 }
 \tag{L-90219.14}
\]

The witness lies before the positive tail, at some

\[
 m_j=2^{j+1}-1\le2^J-1.
\]

Thus

\[
 \boxed{
 \exists m\le2^J-1:\quad
 d(m)\le
 -\frac{2}
 {(1-2^{2-J})(2^J-1)(2^J-2)}.
 }
 \tag{L-90219.15}
\]

For a factor-64 filter (`J=6`), every double-neutral reward with nonnegative tail therefore has some state `m<=63` satisfying

\[
 \boxed{
 d(m)\le-\frac{32}{15\cdot63\cdot62}.
 }
 \tag{L-90219.16}
\]

The improved factor-64 filter has the much stronger explicit witness

\[
 d(15)=\frac{1-\sqrt2}{42},
\]

but (L-90219.16) proves that a compact negative block is unavoidable for **every** alternative double-neutral factor-64 design with positive Pascal tail.

## 5. Interpretation

The exact average (L-90219.5) creates a conservation law for signed Pascal reward debt:

```text
double neutral cancellation                 requires weighted numerator average -2;
raw (1-t)^2                                spreads the optimal debt forever;
positive tail                              forces a stronger finite pre-tail debt;
higher annulus factor                      can move the debt outward but cannot remove it.
```

Thus no amount of finite dyadic filter optimization can make annular cancellation arbitrarily close to coordinatewise-positive Pascal reward without paying a quantitatively visible negative state.

This theorem complements `L-90218`:

- `L-90218` says positive reward and double-neutrality are incompatible;
- the present lemma quantifies the minimum signed failure after positive tail is restored.

## 6. Proof boundary

Proved exactly:

- the weighted block-debt identity;
- the universal numerator bound `min A_j<=-2`;
- the extremal permanent-tail filter `(1-t)^2`;
- the sharper pre-tail bound under nonnegative tail reward;
- the explicit factor-64 universal debt floor.

Not proved:

- payment of this debt by the critical arithmetic occupation;
- any annular sign criterion or RH.

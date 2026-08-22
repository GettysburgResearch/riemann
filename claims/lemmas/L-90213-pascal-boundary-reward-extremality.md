# L-90213 — The `15:4` uniform-Pascal reward is extremal, while every genuine balance cutoff collapses the dyadic boundary to Haar

Claim ID: `L-90213`  
Status: **PROPOSED COMPLETE EXACT MARKOV / SOURCE-EXTREMALITY LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: uniform Pascal kernel `L-33109/L-90208`; ordered balanced kernels `L-90212`; elementary finite Markov and Dirichlet-convolution algebra  
Certificate: `X-90206-pascal-boundary-reward-extremality`  
Scope: the complete one-parameter constant-tail, no-3-channel boundary family; no sign theorem for its arithmetic pairing and no RH conclusion

## 1. The canonical dyadic boundary family

Fix a scale `C>0` and a real parameter `r`. Define the node potential

\[
 \boxed{
 F_r(1)=0,
 \qquad F_r(2)=rC,
 \qquad F_r(3)=(r+1)C,
 \qquad F_r(m)=Cm\quad(m\ge4).
 }
 \tag{L-90213.1}
\]

Normalize by

\[
 f_r(m)=\frac{F_r(m)}m.
 \tag{L-90213.2}
\]

Thus

\[
 f_r(1)=0,
 \qquad f_r(2)=\frac r2,
 \qquad f_r(3)=\frac{r+1}{3},
 \qquad f_r(m)=1\quad(m\ge4).
 \tag{L-90213.3}
\]

The relation

\[
 F_r(3)-F_r(2)=C
 \tag{L-90213.4}
\]

makes the increment at state three equal to the affine-tail increment. It is exactly the condition that removes an independent `3^{-s}` channel from the associated Dirichlet source. Hence (L-90213.1) is the complete constant-tail, two-boundary family relevant to a purely dyadic finite Euler numerator.

For a selected-child Markov policy `P`, put

\[
 \boxed{d_r=f_r-Pf_r.}
 \tag{L-90213.5}
\]

When `d_r>=0`, the potential is the expected total reward of a nonnegative boundary source, and every signed Green occupation satisfies

\[
 \langle r^{\rm node},F_r\rangle
 =\sum_m M(m)d_r(m).
 \tag{L-90213.6}
\]

## 2. Exact arithmetic source

Let

\[
 a_r(m)=F_r(m)-F_r(m-1).
 \tag{L-90213.7}
\]

Then

\[
 a_r(1)=0,
 \quad a_r(2)=rC,
 \quad a_r(3)=C,
 \quad a_r(4)=(3-r)C,
 \quad a_r(m)=C\ (m\ge5).
 \tag{L-90213.8}
\]

Writing `t=2^{-s}`, its Dirichlet series is

\[
 \sum_m\frac{a_r(m)}{m^s}
 =C\left[
 \zeta(s)-1+(r-1)t+(2-r)t^2
 \right].
 \tag{L-90213.9}
\]

After Möbius convolution,

\[
 \boxed{
 \mu*a_r
 =C\varepsilon-CQ_r*\mu,
 }
 \tag{L-90213.10}
\]

where the finite dyadic filter is

\[
 \boxed{
 Q_r
 =(\varepsilon-\delta_2)
  *(\varepsilon+(2-r)\delta_2),
 }
 \tag{L-90213.11}
\]

with local polynomial

\[
 \boxed{
 Q_r(t)=(1-t)(1+(2-r)t).
 }
 \tag{L-90213.12}
\]

For any finite carry target `w` with `w(1)=0` and exact node divergence `r^w`, finite switching gives

\[
 \boxed{
 \sum_m r^w(m)F_r(m)
 =-C\sum_{q\ge2}(Q_r*\mu)(q)w(q).
 }
 \tag{L-90213.13}
\]

Thus positivity of the Markov reward converts a boundary occupation statement into one zero-safe filtered Möbius scalar.

## 3. Uniform Pascal reward cone

For the uniform internal Pascal kernel

\[
 P_m(k)=\frac{2k}{m(m-1)},
 \qquad1\le k<m,
 \tag{L-90213.14}
\]

direct summation gives

\[
 \boxed{
 d_r(2)=\frac r2,
 \qquad
 d_r(3)=\frac13,
 \qquad
 d_r(m)=\frac{10-4r}{m(m-1)}\quad(m\ge4).
 }
 \tag{L-90213.15}
\]

### Proof

The first two rows are immediate. For `m>=4`, the potential equals one except at children one, two, and three. Hence

\[
\begin{aligned}
 d_r(m)
 &=\frac{2}{m(m-1)}
 \left[
 1+2\left(1-\frac r2\right)
 +3\left(1-\frac{r+1}{3}\right)
 \right]\\
 &=\frac{10-4r}{m(m-1)}.
\end{aligned}
\]

Therefore

\[
 \boxed{
 d_r\ge0\text{ on every state}
 \iff 0\le r\le\frac52.
 }
 \tag{L-90213.16}
\]

The endpoint `r=5/2` is unique in making every reward above state three vanish:

\[
 d_{5/2}(m)=0\quad(m\ge4).
 \tag{L-90213.17}
\]

At scale `C=12`,

\[
 \boxed{
 d_{5/2}(2)=15,
 \qquad d_{5/2}(3)=4,
 }
 \tag{L-90213.18}
\]

which is exactly the canonical `15:4` reward of `L-90210`. Thus that ratio is not merely the unique cancellation of the 3-adic deterministic channel: it is the **extreme ray of the positive uniform-Pascal reward cone** within the complete dyadic family (L-90213.1).

Its filter is

\[
 Q_{5/2}(t)=(1-t)(1-t/2)
 =\frac12(1-t)(2-t).
 \tag{L-90213.19}
\]

After the scale `C=12`, equation (L-90213.13) is precisely twice the two-low-row scalar `5c_X(2)+3c_X(3)`.

## 4. Every genuine balance cutoff has a smaller cone

Fix any `alpha` with

\[
 0<\alpha<\frac12.
 \tag{L-90213.20}
\]

For each parent put

\[
 b_m=\min\left(\left\lfloor\frac m2\right\rfloor,
               \max(1,\lceil\alpha m\rceil)\right),
 \qquad
 I_m=\{b_m,\ldots,m-b_m\},
 \tag{L-90213.21}
\]

and use the ordered size-biased child law

\[
 P_m^{(\alpha)}(k)
 =\frac{2k}{m|I_m|}\mathbf1_{k\in I_m}.
 \tag{L-90213.22}
\]

This includes the quarter-balanced policy of `L-90212`.

Then

\[
 \boxed{
 d_r^{(\alpha)}\ge0\text{ on every state}
 \iff 0\le r\le2.
 }
 \tag{L-90213.23}
\]

### Sufficiency

For `0<=r<=2`, every value in (L-90213.3) lies in `[0,1]`. Since `f_r(m)=1` for `m>=4`, every such parent has

\[
 f_r(m)-P_m^{(\alpha)}f_r\ge0.
\]

The rows two and three are unchanged by the cutoff and give `r/2` and `1/3`.

### Necessity

There exists a parent `m>=4` with `b_m=2`. Indeed, for `alpha>1/3` take `m=4`; otherwise take

\[
 m=\left\lfloor\frac1\alpha\right\rfloor+1.
\]

At this row the child interval starts at two. If `m=4`, it is the singleton `{2}`; if `m>=5`, it contains both two and three. For `r>2`, both

\[
 f_r(2)>1,
 \qquad f_r(3)>1,
\]

so the selected-child average is strictly greater than the parent value one. Hence `d_r^{(\alpha)}(m)<0`.

Thus **any positive balance cutoff removes the interval `(2,5/2]` which makes the uniform two-row reward stronger**.

At the balanced extremum `r=2`,

\[
 f_2(m)=1\quad(m\ge2),
 \tag{L-90213.24}
\]

so the drift is just the probability of jumping to state one, and

\[
 \boxed{Q_2(t)=1-t.}
 \tag{L-90213.25}
\]

The strongest admissible constant-tail reward for a genuinely balanced ordered policy therefore collapses to the single critical Haar factor.

## 5. Zero-safety is aligned with the reward cone

Besides the root `t=1`, the filter (L-90213.12) has root

\[
 t=-\frac1{2-r}
 \tag{L-90213.26}
\]

when `r\ne2`. It has no zero in the open unit disk exactly for

\[
 1\le r\le3.
 \tag{L-90213.27}
\]

Intersecting with the positive reward cones gives

\[
 \boxed{
 \begin{array}{c|c}
 \text{policy}&\text{positive and zero-safe }r\\ \hline
 \text{uniform Pascal}&1\le r\le5/2,\\
 \text{ordered }\alpha\text{-balanced}&1\le r\le2.
 \end{array}}
 \tag{L-90213.28}
\]

Thus the uniform extremum `r=5/2` pushes the second positive dyadic root as far inward as positivity permits, to `t=2`, while remaining safely outside the counterexample disk `|t|<1`. No genuine ordered balance cutoff can retain that second root.

## 6. Route consequences

1. The canonical `15:4` low-row scalar is simultaneously selected by:
   - elimination of the independent 3-adic channel (`L-90210`);
   - localization of all reward to states two and three;
   - extremality of the positive uniform-Pascal reward cone;
   - maximal zero-safe dyadic filtering in the family (L-90213.1).
2. The ordered balanced OBH route cannot improve this finite boundary consumer. Its maximal constant-tail positive reward is only the Haar source `(epsilon-delta_2)*mu`.
3. The deterministic spectral gap of `L-90212` remains valuable for full occupation control, but it is purchased at a strict loss in the strongest exact low-boundary reward.
4. Any stronger balanced reward must leave the constant-tail/no-3-channel family, use more boundary states, or exploit a genuinely state-dependent potential.

This is a policy-design theorem, not a sign theorem for either surviving arithmetic scalar.

## 7. Proof boundary

Proved exactly:

- the complete finite dyadic source family;
- the exact uniform-Pascal drift formula;
- the sharp uniform positivity interval `[0,5/2]`;
- extremality and uniqueness of the `15:4` reward;
- the sharp ordered-balanced positivity interval `[0,2]` for every `alpha>0`;
- collapse of the balanced extremum to the Haar source;
- exact alignment of positive-reward and zero-safe parameter regions.

Not proved:

- sign of the `15:4` or Haar arithmetic pairing;
- SHARP, OBH, or RH.

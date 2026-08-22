# L-90216 — Exact uniform-Pascal dyadic filter cone and the factor-64 positive-reward no-go

Claim ID: `L-90216`  
Status: **PROPOSED COMPLETE EXACT FILTER-CONE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: uniform Pascal kernel `L-33109/L-90208`; global reward extremality `L-90214`; improved factor-64 polynomial `L-90022/L-90023` on PR #352  
Certificate: `X-90207-uniform-pascal-dyadic-filter-cone`  
Scope: complete characterization of finite dyadic filters representable by a nonnegative uniform-Pascal reward; no arithmetic sign theorem and no RH conclusion

## 1. Finite dyadic source polynomial

Let

\[
 Q(t)=\sum_{j=0}^{J}q_jt^j,
 \qquad q_0=1,
 \qquad Q(1)=0.
 \tag{L-90216.1}
\]

Define an increment sequence by

\[
 a(n)=
 \begin{cases}
 1-q_j,&n=2^j\quad(0\le j\le J),\\
 1,&\text{otherwise}.
 \end{cases}
 \tag{L-90216.2}
\]

Since `q_0=1`, one has `a(1)=0`. Its Dirichlet series is

\[
 \boxed{
 \sum_{n\ge1}\frac{a(n)}{n^s}
 =\zeta(s)-Q(2^{-s}).
 }
 \tag{L-90216.3}
\]

After Möbius convolution the associated arithmetic source is

\[
 \boxed{
 \mu*a=\varepsilon-Q(\delta_2)*\mu.
 }
 \tag{L-90216.4}
\]

Thus `Q` is exactly the finite dyadic Euler filter seen by the target pairing.

Let

\[
 F(m)=\sum_{n\le m}a(n),
 \qquad f(m)=\frac{F(m)}m.
 \tag{L-90216.5}
\]

Because `Q(1)=0`, the potential is eventually affine:

\[
 F(m)=m,
 \qquad f(m)=1
 \qquad(m\ge2^J).
 \tag{L-90216.6}
\]

## 2. Dyadic block coordinates

Put

\[
 \boxed{S_j=\sum_{\ell=0}^{j}q_\ell}
 \tag{L-90216.7}
\]

and extend `S_j=0` for `j>=J`. For

\[
 2^j\le m<2^{j+1},
\]

finite summation gives

\[
 \boxed{
 F(m)=m-S_j,
 \qquad f(m)=1-\frac{S_j}{m}.
 }
 \tag{L-90216.8}
\]

Define the weighted prefix

\[
 \boxed{
 A_j=2\sum_{\ell=0}^{j-1}2^\ell S_\ell
 \qquad(j\ge1).
 }
 \tag{L-90216.9}
\]

## 3. Exact Markov drift on every block

For the uniform Pascal kernel

\[
 P_m(k)=\frac{2k}{m(m-1)},
 \qquad1\le k<m,
 \tag{L-90216.10}
\]

put `d=f-Pf`. Then for every `m` in the `j`th dyadic block,

\[
 \boxed{
 m(m-1)d(m)
 =A_j+(m+1-2^{j+1})S_j.
 }
 \tag{L-90216.11}
\]

### Proof

Write `e_m=F(m)-m=-S_j` on the block. The affine baseline `F(m)=m` has zero uniform-Pascal drift when the state-one value is included. Hence

\[
 m(m-1)d(m)
 =(m-1)e_m-2\sum_{k<m}e_k.
 \tag{L-90216.12}
\]

The complete earlier blocks contribute

\[
 \sum_{k<2^j}e_k
 =-\sum_{\ell<j}2^\ell S_\ell,
\]

while the current partial block contributes `-(m-2^j)S_j`. Substitution gives (L-90216.11). ∎

The right side is affine in `m`. At the block endpoints it equals

\[
 \boxed{
 \begin{aligned}
 D_j^{\rm left}
 &=A_j-(2^j-1)S_j,\\
 D_j^{\rm right}
 &=A_j.
 \end{aligned}}
 \tag{L-90216.13}
\]

## 4. Necessary-and-sufficient cone inequalities

The filter `Q` has a nonnegative uniform-Pascal reward,

\[
 d(m)\ge0\qquad(m\ge2),
 \tag{L-90216.14}
\]

if and only if

\[
 \boxed{
 A_j\ge0,
 \qquad
 A_j-(2^j-1)S_j\ge0
 \qquad(1\le j\le J),
 }
 \tag{L-90216.15}
\]

and the tail inequality

\[
 \boxed{
 A_{J+1}=2\sum_{\ell=0}^{J}2^\ell S_\ell\ge0.
 }
 \tag{L-90216.16}
\]

### Proof

On a fixed block, (L-90216.11) is affine. If `S_j>=0`, it increases with `m`, so its minimum is the left endpoint. If `S_j<=0`, it decreases, so its minimum is the right endpoint. Requiring both endpoint expressions in (L-90216.13) to be nonnegative is therefore necessary and sufficient, and one of the two inequalities is automatically redundant according to the sign of `S_j`.

After the polynomial support, `S_j=0` and the drift numerator is the constant `A_{J+1}`. This gives (L-90216.16). ∎

Thus a potentially enormous Markov positivity problem collapses to two explicit linear inequalities per dyadic scale.

## 5. Examples and the global first-coefficient bound

### Haar

For

\[
 Q(t)=1-t,
\]

the inequalities are strict and the reward is the state-one killing probability.

### Canonical extremal filter

For

\[
 Q(t)=(1-t)(1-t/2)
 =1-\frac32t+\frac12t^2,
 \tag{L-90216.17}
\]

one has

\[
 S_0=1,
 \qquad S_1=-\frac12,
 \qquad S_2=0,
\]

and all inequalities are saturated exactly so as to leave only the `15:4` reward at states two and three.

More generally, `L-90214` proves for every positive filter in this cone satisfying the no-3-channel normalization that

\[
 \boxed{q_1\ge-\frac32,}
 \tag{L-90216.18}
\]

with equality only for (L-90216.17). The cone inequalities here refine that global first-coefficient theorem by controlling every additional dyadic tap.

The cone is not restricted to degree two. For example

\[
 Q(t)=1-\frac75t+\frac12t^2-\frac1{10}t^3
 \tag{L-90216.19}
\]

satisfies all inequalities and has a positive tail reward.

## 6. Exact no-go for the improved factor-64 filter

The preferred factor-64 polynomial of `L-90022/L-90023` is

\[
 P_{64}^*(t)
 =(1-t)^2(1-t/\sqrt2)(1+t)(1+3t/4+t^2).
 \tag{L-90216.20}
\]

Its first cumulative coefficients are

\[
 \boxed{
 S_0=1,
 \qquad
 S_1=\frac34-\frac{\sqrt2}{2},
 \qquad
 S_2=-\frac{3\sqrt2}{8}.
 }
 \tag{L-90216.21}
\]

The right-end cone quantity on the block `8<=m<=15` is

\[
\begin{aligned}
 A_3
 &=2[S_0+2S_1+4S_2]\\
 &=\boxed{5-5\sqrt2}<0.
\end{aligned}
 \tag{L-90216.22}
\]

Hence the filter lies outside the positive uniform-Pascal reward cone. At the explicit state `m=15`,

\[
 \boxed{
 d(15)=\frac{A_3}{15\cdot14}
 =\frac{1-\sqrt2}{42}<0.
 }
 \tag{L-90216.23}
\]

Therefore the improved factor-64 annular criterion cannot be obtained as a nonnegative finite dyadic boundary reward of the uniform Pascal chain.

This does **not** refute the factor-64 criterion or its RH equivalence. It proves that the annular-filter and positive-uniform-Pascal mechanisms are genuinely distinct; one cannot import the stronger factor-64 filter into SHARP by merely adding positive dyadic reward taps.

## 7. Design consequence

The exact cone (L-90216.15)--(L-90216.16) is a fail-closed filter-design interface:

1. propose any finite dyadic zero-safe polynomial `Q`;
2. compute its prefix variables `S_j`;
3. test two rational/algebraic inequalities per scale;
4. either obtain the complete nonnegative Pascal reward or an explicit negative state witness.

Combined with `L-90214`, it shows:

```text
strongest global first coefficient       canonical (1-t)(1-t/2)
additional positive dyadic taps          allowed, but cannot improve q1
factor-64 rational unit-circle filter     exact negative reward at state 15
```

A route combining factor-64 phase optimization with Pascal positivity must therefore use a signed reward, a different Markov policy, a non-dyadic boundary, or a nonlocal state construction.

## 8. Proof boundary

Proved exactly:

- the dyadic-block potential formula;
- the exact drift on every state;
- necessary and sufficient finite cone inequalities;
- the tail condition;
- compatibility with global `15:4` extremality;
- an exact algebraic negative-state certificate for the improved factor-64 filter.

Not proved:

- sign of any surviving arithmetic scalar;
- the factor-64 criterion, SHARP, or RH.

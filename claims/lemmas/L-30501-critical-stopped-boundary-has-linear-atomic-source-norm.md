# L-30501 — The critical stopped boundary has linear atomic source norm

Claim ID: `L-30501`  
Title: Ordinary divisor-source atomization of the complete stopped critical boundary costs at least a fixed multiple of the endpoint  
Status: **PROPOSED COMPLETE EXACT/INEQUALITY LEMMA**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: PR #286 `L-28402`; PR #301 `L-29801`; elementary multiples Möbius inversion  
Scope: the initial finite-cutoff boundary source before any conjectural source-to-flow estimate

## 1. One stopped critical power

For an integer endpoint `Y>=2`, put

\[
p_Y(n)=n^{-1/2}\mathbf 1_{n\le Y}.
\tag{L-30501.1}
\]

The infinite shifted central operator and its finite restriction differ by the
exact boundary vector

\[
\boxed{
 g_Y(q)
 =\sum_{2kq-1>Y}(2kq-1)^{-1/2}
  -\sum_{(2k+1)q>Y}((2k+1)q)^{-1/2},
 \qquad 2\le q\le\lfloor Y/2\rfloor .
}
\tag{L-30501.2}
\]

This is precisely `mathscr Q_Y p_Y` in PR #286 `L-28402`. The two tails are
understood in their naturally paired convergent sense.

Let

\[
M_Y=\lfloor Y/2\rfloor.
\]

There is a unique ordinary divisor-source vector `sigma_Y`, supported on
`2<=m<=M_Y`, such that

\[
\boxed{
 g_Y(q)=\sum_{\ell\le M_Y/q}\sigma_Y(\ell q).
}
\tag{L-30501.3}
\]

Indeed multiples Möbius inversion gives

\[
\sigma_Y(m)
 =\sum_{d\le M_Y/m}\mu(d)g_Y(dm).
\tag{L-30501.4}
\]

This is the exact source coordinate consumed by an adjacent-tree commutator map
of the form used in PR #304.

## 2. The source is explicit on the top band

Fix an integer

\[
{Y\over3}<m\le {Y\over2}.
\tag{L-30501.5}
\]

Then `m>M_Y/2`, so no multiple `2m` lies in the source support. Consequently

\[
\boxed{
\sigma_Y(m)=g_Y(m).
}
\tag{L-30501.6}

Moreover the first omitted shifted-even index is `k=2`, while the first omitted
odd index is `k=1`. Hence

\[
\boxed{
 g_Y(m)
 =-{1\over\sqrt{3m}}
  +\sum_{k=2}^{\infty}
   \left[
    {1\over\sqrt{2km-1}}
    -{1\over\sqrt{(2k+1)m}}
   \right].
}
\tag{L-30501.7}

Thus the exact source sign on this band is independent of the detailed location
of `Y` inside `[2m,3m)`.

## 3. Uniform negative moat

Assume `m>=64`. Multiplying (L-30501.7) by `sqrt(m)` gives

\[
\sqrt m\,g_Y(m)
 =-{1\over\sqrt3}
  +\sum_{k=2}^{\infty}
   \left[
    (2k-1/m)^{-1/2}-(2k+1)^{-1/2}
   \right].
\tag{L-30501.8}

Split the sum into

\[
\begin{aligned}
S_0&=\sum_{k=2}^{\infty}
 \left[(2k)^{-1/2}-(2k+1)^{-1/2}\right],\\
E_m&=\sum_{k=2}^{\infty}
 \left[(2k-1/m)^{-1/2}-(2k)^{-1/2}\right].
\end{aligned}
\tag{L-30501.9}

For the decreasing function `x^(-1/2)`, the mean-value theorem gives

\[
(2k)^{-1/2}-(2k+1)^{-1/2}
 \le {1\over2(2k)^{3/2}}.
\]

Also

\[
\sum_{k=2}^{\infty}(2k)^{-3/2}
 \le 2^{-3/2}
 \left(2^{-3/2}+\int_2^\infty x^{-3/2}\,dx\right)
 ={5\over8}.
\]

Therefore

\[
S_0\le {5\over16}.
\tag{L-30501.10}
\]

For the shift error, `m>=64` and `k>=2` imply

\[
2k-{1\over m}\ge {255\over256}(2k).
\]

A second mean-value estimate and the elementary inequality
`(256/255)^(3/2)<2` give

\[
E_m
 \le {1\over2m}\,2
 \sum_{k=2}^{\infty}(2k)^{-3/2}
 \le {5\over8m}
 \le {5\over512}
 <{1\over100}.
\tag{L-30501.11}
\]

Finally

\[
{1\over\sqrt3}>{9\over16}
\]

because `3*9^2<16^2`. Combining (L-30501.8)--(L-30501.11),

\[
\sqrt m\,g_Y(m)
 <-{9\over16}+{5\over16}+{1\over100}
 =-{6\over25}
 <-{1\over5}.
\]

Hence

\[
\boxed{
\sqrt m\,\sigma_Y(m)
 =\sqrt m\,g_Y(m)<-{1\over5}
 \qquad
 \left(m\ge64,\ {Y\over3}<m\le{Y\over2}ight).
}
\tag{L-30501.12}

This is a macroscopic same-sign source band, not a large-constant artifact.

## 4. The complete positive stopped-power layer cake

PR #301 resolves the critical target exactly as

\[
 w_X(q)=q^{-1/2}\log(X/q)
 =\sum_{Y=q}^{X-1}\ell_Y p_Y(q),
 \qquad
 \ell_Y=\log{Y+1\over Y}>0.
\tag{L-30501.13}

By linearity, its complete initial boundary source is

\[
\boxed{
 \Sigma_X(m)=\sum_{Y=1}^{X-1}\ell_Y\sigma_Y(m),
}
\tag{L-30501.14}

with every `sigma_Y` zero-extended outside its own support.

Let

\[
\lfloor X/3\rfloor+1\le m\le\lfloor2X/5\rfloor.
\tag{L-30501.15}

For `Y<2m`, the source support `floor(Y/2)` is below `m`, so
`sigma_Y(m)=0`. For every

\[
2m\le Y\le X-1
\]

one has `Y/3<m<=Y/2`. If `X>=192`, then `m>=64`, and (L-30501.12) gives

\[
\begin{aligned}
\sqrt m\,\Sigma_X(m)
&\le -{1\over5}
 \sum_{Y=2m}^{X-1}\log{Y+1\over Y}\\
&=-{1\over5}\log{X\over2m}\\
&\le -{1\over5}\log{5\over4}
 <-{1\over25}.
\end{aligned}
\tag{L-30501.16}

The last inequality uses

\[
\log(1+x)>{x\over1+x},
\qquad x={1\over4}.
\]

The number of integers in (L-30501.15) is at least

\[
{X\over15}-1\ge {X\over30}
\qquad(X\ge192).
\tag{L-30501.17}

Therefore the square-root atomic norm satisfies the unconditional lower bound

\[
\boxed{
 \|\Sigma_X\|_{\rm at}
 :=\sum_m\sqrt m\,|\Sigma_X(m)|
 \ge {X\over750}
 \qquad(X\ge192).
}
\tag{L-30501.18}

In particular this norm is not `polylog(X)` and is not `X^o(1)`.

## 5. Uniqueness and representation independence

The lower bound is not tied to one Euler truncation. Equation (L-30501.3)
determines the ordinary divisor source uniquely. Finite Euler transformation,
Peano representations, Taylor expansion, and recombination of repeated
arithmetic destinations may change the displayed source manifest, but after all
channels are added their ordinary divisor-source sum must equal `Sigma_X`.

On the band (L-30501.15), no higher multiple lies inside the strict half-scale
source support. Thus every exact ordinary divisor-source manifest has the same
coordinate `Sigma_X(m)` there. No cancellation with a lower source node can
alter (L-30501.16).

## 6. Consequence for terminal commutator lifting

PR #304 proves a valid bounded map

\[
 \Phi(\sigma)=\sum_m\sigma_m(T_m-T_{m-1}),
 \qquad
 \mathcal N_\omega(\Phi(\sigma))
 \le24\|\sigma\|_{\rm at}.
\]

But (L-30501.18) shows that applying this map to the complete stopped critical
boundary gives only an `O(X)` upper estimate, not a polylogarithmic one.

More strongly, any proposed proof whose sole source estimate is

\[
\mathcal N_\omega(\text{boundary flow})
 \le C\|\Sigma_X\|_{\rm at}
\]

cannot close Cycle Debt through an absolute atomic-norm bound. The boundary must
be recombined in a structured quotient/cycle coordinate before ordinary source
atomization.

## 7. Proof boundary

Closed here:

1. the exact top-band boundary formula;
2. uniqueness of the ordinary divisor source;
3. a uniform negative source moat;
4. the positive stopped-layer accumulation;
5. the linear lower bound `||Sigma_X||_at>=X/750`.

Not claimed:

1. a lower bound of the same order for optimized Cycle Debt;
2. impossibility of every structured or cycle-corrected boundary realization;
3. RH.
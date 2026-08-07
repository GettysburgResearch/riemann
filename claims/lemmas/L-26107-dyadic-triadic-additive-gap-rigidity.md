# L-26107 — Dyadic–triadic rigidity of additive gaps on the annulus

Claim ID: `L-26107`  
Title: Small annular second differences force the consecutive gaps of a nonnegative additive function into the logarithmic scaling regime  
Status: **PROPOSED COMPLETE ELEMENTARY LEMMA**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Issue: #261  
Depends on: `L-26105`, `O-26102`  
Scope: exact finite rigidity estimates; does not prove `ADF`

## 1. Additive dual and consecutive gaps

For a nonnegative prime-power vector `lambda`, put

\[
 L(n)=L_\lambda(n)
 =\sum_{\substack{q=p^a\\q\mid n}}\lambda_q.
 \tag{L-26107.1}

Then `L` is additive on coprime products. Define

\[
 h_m=L(m)-L(m-1),
 \tag{L-26107.2}
\]

and

\[
 d_m=h_m-h_{m+1}
 =2L(m)-L(m-1)-L(m+1).
 \tag{L-26107.3}
\]

On the annulus

\[
 I_X=[\lceil X/5\rceil,\lfloor4X/5\rfloor],
\]

one has

\[
 \sum_{m\in I_X}|d_m|^2
 =\|A_X^*\lambda\|_2^2.
 \tag{L-26107.4}

## 2. Exact dyadic identity

Let `n` be odd. Additivity gives

\[
 L(2n)=L(2)+L(n)
\]

and

\[
 L(2n+4)=L(2)+L(n+2).
\]

Subtracting and expanding in consecutive gaps yields

\[
 h_{2n+1}+h_{2n+2}+h_{2n+3}+h_{2n+4}
 =h_{n+1}+h_{n+2}.
 \tag{L-26107.5}

Since `d_m=h_m-h_(m+1)`, this is equivalent to

\[
\boxed{
 h_{n+1}-2h_{2n+1}
 =\frac12\left[
 d_{n+1}
 -3d_{2n+1}-2d_{2n+2}-d_{2n+3}
 \right].
}
\tag{L-26107.6}

For odd integers in the range

\[
 \frac X5+2\le n\le\frac{2X}{5}-3,
\]

all displayed difference indices lie in `I_X`. The local families have bounded overlap. Cauchy--Schwarz therefore gives one absolute constant, for example

\[
\boxed{
 \sum_{\substack{X/5+2\le n\le2X/5-3\\n\ {m odd}}}
 |h_{n+1}-2h_{2n+1}|^2
 \le 8\sum_{m\in I_X}|d_m|^2.
}
\tag{L-26107.7}

The constant `8` is deliberately wider than the exact coefficient-square ledger.

## 3. Exact triadic identity

Let `3` not divide `n`. Then

\[
 L(3n)=L(3)+L(n),
\]

and the same identity holds with `n+3`. Hence

\[
 \sum_{r=1}^{9}h_{3n+r}
 =\sum_{r=1}^{3}h_{n+r}.
 \tag{L-26107.8}

Equivalently,

\[
\boxed{
 h_{n+1}-3h_{3n+1}
 =\frac13\left[
 2d_{n+1}+d_{n+2}
 -\sum_{r=1}^{8}(9-r)d_{3n+r}
 \right].
}
\tag{L-26107.9}

For

\[
 \frac X5+3\le n\le\frac{4X}{15}-4,
 \qquad 3\nmid n,
\]

all indices lie in `I_X`. The coefficient-square sum is

\[
 \frac{2^2+1^2+1^2+2^2+\cdots+8^2}{9}
 =\frac{209}{9},
\]

and the local windows have bounded overlap. Thus, with a safe absolute constant,

\[
\boxed{
 \sum_{\substack{X/5+3\le n\le4X/15-4\\3\nmid n}}
 |h_{n+1}-3h_{3n+1}|^2
 \le 50\sum_{m\in I_X}|d_m|^2.
}
\tag{L-26107.10}

## 4. Gap Poincaré inequality

Let

\[
 \overline h
 =\frac1{|I_X|}\sum_{m\in I_X}h_m.
\]

The ordinary discrete Poincaré inequality gives

\[
 \sum_{m\in I_X}|h_m-\overline h|^2
 \ll X^2\sum_{m\in I_X}|d_m|^2.
 \tag{L-26107.11}

Use the dyadic family (L-26107.7). For each eligible `n`,

\[
 h_{n+1}-2h_{2n+1}
 =-\overline h
 +(h_{n+1}-\overline h)
 -2(h_{2n+1}-\overline h).
\]

There are `gg X` eligible odd integers and both index maps have bounded multiplicity. Summing squares and applying (L-26107.7)--(L-26107.11) yields

\[
 X|\overline h|^2
 \ll X^2\sum_{m\in I_X}|d_m|^2.
 \tag{L-26107.12}

Combining this with (L-26107.11),

\[
\boxed{
 \sum_{m\in I_X}|h_m|^2
 \ll X^2\sum_{m\in I_X}|d_m|^2.
}
\tag{L-26107.13}

This scale is sharp for `L(n)=c log n`: its gap norm is of order `|c|X^(-1/2)` and its curvature norm is of order `|c|X^(-3/2)`.

## 5. Interpretation

Equations (L-26107.7) and (L-26107.10) say that a small `ADF` denominator forces the additive gap to obey the characteristic logarithmic scaling laws

\[
 h(n)\simeq2h(2n),
 \qquad
 h(n)\simeq3h(3n).
\]

Equation (L-26107.13) is a quantitative local rigidity estimate. It is the finite-annulus counterpart of the classical characterization of `c log n` by slowly varying consecutive gaps.

It does not yet control the prime-power source pairing in the numerator of `ADF`; that requires a stronger coefficient-level rigidity or a separate scalar treatment of the logarithmic mode.

## 6. Proof boundary

Exact in this file:

- dyadic and triadic dilation identities;
- bounded-overlap `L^2` dilation estimates;
- the annular gap Poincaré inequality.

Open:

- coefficient-level decomposition into `c Lambda` plus a source-controlled transverse vector;
- the logarithmic scalar recurrence;
- `ADF` and RH.
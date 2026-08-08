# L-26216 — The current-bank digital tails recombine with only polylogarithmic loss

Claim ID: `L-26216`  
Title: Common-metric square summation preserves the binary-tail decay through the opposite-parity synthesis  
Status: **PROPOSED COMPLETE QUANTITATIVE LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Depends on: `L-26211`, `L-26213`, `L-26215`; the local bound `|omega_2(d)|<=5/2`  
Scope: the current hyperbola bank `S_N`; no estimate for the complementary remainder `L_N`, finite current feature, or RH

## 1. Current-bank tail

In the current bank of `L-26211`, every synthesis index satisfies

\[
1\le d<N
\]

and every digital prefix length is

\[
Y_d={N^2\over d}\ge N.
\]

Let `f` be one causal source in the declared Sobolev domain. Write

\[
\mathcal C_{Y_d}f
=\mathcal C_\infty f-\mathcal T_{Y_d}f.
\]

The tail part of the current bank is

\[
\boxed{
\mathcal E_N f
=\sum_{d<N}
\omega_2(d)D_d\mathcal T_{Y_d}f,
}
\tag{L-26216.1}

where `D_d` is the normalized multiplicative dilation in the common potential space of `L-26213`.

## 2. Exact dilation and coefficient square budget

By `L-26213`,

\[
\|D_dg\|_{\mathscr H_w}^2
={1\over d}\|g\|_{\mathscr H_w}^2.
\]

Moreover

\[
|\omega_2(d)|\le\frac52.
\]

Hence

\[
\boxed{
\sum_{d<N}{|\omega_2(d)|^2\over d}
\le
{25\over4}(1+\log N).
}
\tag{L-26216.2}

## 3. Square recombination

Apply Hilbert-space Cauchy--Schwarz to (L-26216.1):

\[
\begin{aligned}
\|\mathcal E_Nf\|_{\mathscr H_w}^2
&\le
\left(\sum_{d<N}{|\omega_2(d)|^2\over d}\right)
\left(\sum_{d<N}\|\mathcal T_{Y_d}f\|_{\mathscr H_w}^2\right).
\end{aligned}
\tag{L-26216.3}

Every `Y_d>=N`. By `L-26215`,

\[
\|\mathcal T_{Y_d}f\|_{\mathscr H_w}
\le
\varepsilon_N\|f\|_{H^1_*},
\qquad
\varepsilon_N
=O\!\left({\log N\over\sqrt N}\right).
\]

There are fewer than `N` synthesis indices, so

\[
\sum_{d<N}\|\mathcal T_{Y_d}f\|_{\mathscr H_w}^2
\le
N\varepsilon_N^2\|f\|_{H^1_*}^2
=O(\log^2N)\|f\|_{H^1_*}^2.
\tag{L-26216.4}

Combining (L-26216.2)--(L-26216.4),

\[
\boxed{
\|\mathcal E_Nf\|_{\mathscr H_w}^2
\le
C\log^3(2N)\|f\|_{H^1_*}^2
}
\tag{L-26216.5}

with an absolute effective constant `C` inherited from `L-23016`.

Equivalently,

\[
\boxed{
\|\mathcal E_Nf\|_{\mathscr H_w}
\le
C^{1/2}\log^{3/2}(2N)\|f\|_{H^1_*}.
}
\tag{L-26216.6}

## 4. Why this is the correct scale

A total-variation estimate would use

\[
\sum_{d<N}{|\omega_2(d)|\over\sqrt d}
\asymp\sqrt N
\]

and would erase the `N^{-1/2}` digital-tail gain. The square recombination instead uses

\[
\sum_{d<N}{|\omega_2(d)|^2\over d}=O(\log N),
\]

leaving only a polylogarithmic current-bank error.

A polylogarithmic loss is compatible with a scale descent of length `log N`: after choosing an unbounded bank scale, it has zero exponential cost. This observation does not by itself control the complementary hyperbola remainder.

## 5. Surviving source scope

The estimate is applied after:

- exact source convolution;
- exact common-metric embedding;
- retention of every within-observation cross term.

It does not replace the RH-sensitive source by the positive-inverse feature. It uses absolute squares only at the final Hilbert recombination of already declared tail observations.

## 6. Proof boundary

Closed, subject to review:

- the `O(log N)` coefficient-square budget;
- the `O(log^2 N)` summed digital-tail budget;
- the `O(log^3 N)` recombined current-bank tail estimate.

Open:

- the complementary hyperbola remainder `L_N`;
- the finite current generalized-prime/boundary energy;
- the final annular recurrence;
- RH.

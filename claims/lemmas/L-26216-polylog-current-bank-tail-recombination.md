# L-26216 — Conditional polylogarithmic recombination of Sobolev-compatible bank tails

Claim ID: `L-26216`  
Title: Once all digital tails are represented in one common Sobolev-compatible metric, square summation preserves their decay through the opposite-parity synthesis  
Status: **PROPOSED CONDITIONAL LEMMA — COMMON SOBOLEV/CARRY INTERTWINER OPEN**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Depends on: `L-26211`, `L-26213`, scope-corrected `L-26215`; `|omega_2(d)|<=5/2`  
Scope: abstract Hilbert recombination after one declared Sobolev-compatible source embedding; not presently applicable to the raw step-window carry vectors

## 1. Conditional hypotheses

Let `H` be one Hilbert space containing the complete current-bank observations. Assume that, for every synthesis index `d<N`, the corresponding strict digital tail is represented by a vector `T_d f in H` satisfying

\[
\boxed{
\|T_df\|_H
\le
\varepsilon_N\|f\|_{\mathcal S},
\qquad
\varepsilon_N
=O\!\left({\log N\over\sqrt N}\right),
}
\tag{L-26216.1}

for one declared source norm `||.||_S`.

Assume also that normalized multiplicative dilation satisfies

\[
\boxed{
\|D_dg\|_H^2={1\over d}\|g\|_H^2.
}
\tag{L-26216.2}

For the raw annular step metric, (L-26216.2) is supplied by `L-26213`, but (L-26216.1) is **not** presently supplied because the raw signal is not in `H^1`. A valid application must construct the smoothing/potential-to-carry intertwiner identified in `L-26215`.

## 2. Opposite-parity synthesis

Define

\[
\mathcal E_N f
=\sum_{d<N}\omega_2(d)D_dT_df.
\tag{L-26216.3}

Since

\[
|\omega_2(d)|\le\frac52,
\]

one has

\[
\boxed{
\sum_{d<N}{|\omega_2(d)|^2\over d}
\le{25\over4}(1+\log N).
}
\tag{L-26216.4}

Writing each term as `(omega_2(d)/sqrt d)(sqrt d D_dT_df)` and applying Hilbert-space Cauchy--Schwarz gives

\[
\begin{aligned}
\|\mathcal E_Nf\|_H^2
&\le
\left(\sum_{d<N}{|\omega_2(d)|^2\over d}\right)
\left(\sum_{d<N}\|T_df\|_H^2\right).
\end{aligned}
\tag{L-26216.5}

There are fewer than `N` indices, so (L-26216.1) gives

\[
\sum_{d<N}\|T_df\|_H^2
\le
N\varepsilon_N^2\|f\|_{\mathcal S}^2
=O(\log^2N)\|f\|_{\mathcal S}^2.
\tag{L-26216.6}

Consequently

\[
\boxed{
\|\mathcal E_Nf\|_H^2
\le
C\log^3(2N)\|f\|_{\mathcal S}^2.
}
\tag{L-26216.7}

## 3. Meaning and limitation

The square recombination costs only a polylogarithm. It avoids the invalid total-variation budget

\[
\sum_{d<N}{|\omega_2(d)|\over\sqrt d}\asymp\sqrt N.
\]

But (L-26216.7) is conditional on having all tail observations in a common metric where both (L-26216.1) and (L-26216.2) hold.

The previous version treated `L-26213` and the `H^1` estimate of PR #236 as if they automatically supplied that common domain for the raw step signal. The scope correction in `L-26215` shows that they do not.

## 4. Proof boundary

Closed exactly under the displayed hypotheses:

- the `O(log N)` coefficient-square budget;
- the Hilbert-space square recombination;
- the `O(log^3 N)` conditional tail estimate.

Open:

- the Sobolev-compatible physical-to-carry embedding;
- application to the actual bank source;
- the complementary hyperbola remainder and boundary;
- RH.

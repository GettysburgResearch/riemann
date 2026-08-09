# L-34406 — The compact two-tap source has a critical radix-four reserve increment

Claim ID: `L-34406`  
Title: For the finite main-pole source `B_sharp=(1-4^(1-s))/zeta(s)`, the complete Selberg--Kummer reserve created by one aligned radix-four dilation is uniformly `Theta(n log n)` on every fixed balanced cone  
Status: **PROPOSED COMPLETE COFINAL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: PR #325 `L-32415/L-32414`; PR #342 mode-probability/Stirling lower bound for the fourfold binomial ratio  
Scope: deterministic source-matched reserve increment; no compact-current upper estimate or RH claim

## 1. Compact two-tap Dirichlet system

Retain the finite Q=4 main-pole source of PR #325:

\[
 B_\sharp(s)=\frac{1-4^{1-s}}{\zeta(s)},
 \qquad
 A_\sharp=B_\sharp^{-1}.
\]

Its generalized-prime sequence is

\[
\boxed{
 \Lambda_\sharp
 =\Lambda+D,
 \qquad
 D(4^r)=d_r:=4^r\log4
 \quad(r\ge1),
}
\tag{L-34406.1}

and zero off the four-adic tower. Put

\[
 C_\sharp
 =\Lambda_\sharp\log
  +\Lambda_\sharp*\Lambda_\sharp.
\]

For a row `e=(n,j)`, `k=n-j`, write

\[
 P_\sharp(e)=\mathcal L_e(\Lambda_\sharp),
 \qquad
 S_\sharp(e)=\mathcal L_e(C_\sharp),
\]

\[
\boxed{
 R_\sharp(e)=P_\sharp(e)^2-S_\sharp(e).
}
\tag{L-34406.2}

PR #325 `L-32415` proves `R_sharp>0` on every quarter-balanced row.

Let

\[
 e^+=(4n,4j)
\]

and define the relative reserve

\[
\boxed{
 \Delta_4R_\sharp(e)
 =R_\sharp(e^+)-16R_\sharp(e).
}
\tag{L-34406.3}

The theorem is that, on every fixed balanced cone and outside a finite base,

\[
\boxed{
 \Delta_4R_\sharp(e)=\Theta_\eta(n\log n).
}
\tag{L-34406.4}

For the quarter-balanced cone an explicit cofinal lower bound is supplied in Section 7.

## 2. The local first moment cancels exactly in the scale score

Let

\[
 F(e)=\log{n\choose j}
\]

be the ordinary Kummer row and write

\[
 c_r=\chi_{n,4^r}(j).
\]

Then

\[
\boxed{
 P_\sharp(e)
 =F(e)+\sum_{r\ge1}d_rc_r.
}
\tag{L-34406.5}

Under aligned radix-four dilation,

\[
 c'_1=0,
 \qquad
 c'_{r+1}=c_r,
\]

while

\[
 d_{r+1}=4d_r.
\]

Therefore the complete local tower cancels from the relative first score:

\[
\boxed{
 E(e):=P_\sharp(e^+)-4P_\sharp(e)
 =F(e^+)-4F(e).
}
\tag{L-34406.6}

Thus `E` is purely the ordinary fourfold binomial entropy increment. No generalized-prime local coefficient occurs in it.

In particular

\[
 E(e)\ge0
\tag{L-34406.7}

by the block-selection injection

\[
 {4n\choose4j}\ge {n\choose j}^4.
\]

On every fixed balanced cone, elementary Stirling bounds give

\[
\boxed{
 E(e)=\Theta_\eta(\log n).
}
\tag{L-34406.8}

More concretely, the mode-probability estimate used on PR #342 gives, outside one absolute finite threshold on the quarter-balanced cone,

\[
\boxed{
 E(e)\ge\frac12\log n.
}
\tag{L-34406.9}

The matching upper bound `E=O_eta(log(2n))` follows directly from the elementary two-sided Stirling inequalities for the three factorials in the binomial coefficient.

## 3. Prime-free decomposition of the second moment

Retain the notation of PR #325 `L-32411`, now with

\[
 d_r=4^rL,
 \qquad L=\log4.
\]

Put

\[
 N_r=\left\lfloor{n\over4^r}\right\rfloor,
 \qquad
 J_r=\left\lfloor{j\over4^r}\right\rfloor,
\]

and

\[
 A_r
 =F(N_r,J_r)
  +c_r\log(N_r-J_r)
 \ge0.
\tag{L-34406.10}

Let

\[
 E_t^{\rm loc}
 =\sum_{a+b=t}d_ad_b
 =(t-1)4^tL^2
 \qquad(t\ge2),
\]

with `E_1^loc=0`. Then

\[
\boxed{
\begin{aligned}
 S_\sharp(e)={}&S_0(e)
 +\sum_{r\ge1}d_r rL\,c_r\\
 &+2\sum_{r\ge1}d_rA_r
 +\sum_{t\ge2}E_t^{\rm loc}c_t,
\end{aligned}}
\tag{L-34406.11}

where `S_0` is the ordinary Selberg row.

## 4. Exact radix-four difference of the local sector

At the scaled row, the first quotient level contributes the new mixed term

\[
 2d_1F(e)=8LF(e),
\]

while every old quotient is shifted by one level. Direct substitution into (L-34406.11) gives

\[
\boxed{
\begin{aligned}
&16\bigl[S_\sharp(e)-S_0(e)\bigr]
 -\bigl[S_\sharp(e^+)-S_0(e^+)\bigr]\\
&\quad=-8LF(e)
 +24\sum_{r\ge1}d_rA_r
 +\sum_{r\ge1}K_rc_r,
\end{aligned}}
\tag{L-34406.12}

with

\[
\boxed{
 K_r=4^{r+1}(6r-5)L^2>0
 \qquad(r\ge1).
}
\tag{L-34406.13}

For `r=1`, this gives `K_1=16L^2`; the formula already includes the newly created local/local coefficient at level two.

Hence the entire local source correction has only one potentially adverse contribution, the explicit current-scale term `-8LF(e)`.

## 5. The ordinary fourfold slack pays six eighths of the new term

The grouped ordinary Selberg estimate proved in PR #325 `L-32414` gives, whenever `k>=6`,

\[
\boxed{
 16S_0(e)-S_0(e^+)
 \ge12\log2\,F(e)
 =6LF(e).
}
\tag{L-34406.14]

(The closing bracket in the imported tag is typographical only.)

Combining (L-34406.12)--(L-34406.14),

\[
\boxed{
 16S_\sharp(e)-S_\sharp(e^+)
 \ge -2LF(e).
}
\tag{L-34406.15

The omitted terms in (L-34406.12) are all nonnegative.

The finitely many balanced rows with `k<6` are irrelevant to the cofinal statement and may be retained in the finite base table already used by `L-32414/L-32415`.

## 6. Relative reserve identity

By definition of `E` in (L-34406.6),

\[
 P_\sharp(e^+)=4P_\sharp(e)+E(e).
\]

Therefore

\[
\boxed{
\begin{aligned}
 \Delta_4R_\sharp(e)
 ={}&8P_\sharp(e)E(e)+E(e)^2\\
 &+16S_\sharp(e)-S_\sharp(e^+).
\end{aligned}}
\tag{L-34406.16

Using `P_sharp>=F` and (L-34406.15),

\[
\boxed{
 \Delta_4R_\sharp(e)
 \ge 8F(e)E(e)+E(e)^2-2LF(e)
 \ge2F(e)[4E(e)-L].
}
\tag{L-34406.17

This is the exact lower mechanism: one logarithmic entropy score `E` multiplies the linear Kummer mass `F`, while every source-local second-moment defect is lower order.

## 7. Explicit cofinal lower moat

On the quarter-balanced cone,

\[
 F(e)\ge {n\over4}\log2={nL\over8}.
\]

Outside the finite threshold of (L-34406.9),

\[
 E(e)\ge\frac12\log n.
\]

For `n>=4`, `log n>=L`, and therefore

\[
 4E(e)-L
 \ge2\log n-L
 \ge\log n.
\]

Substituting in (L-34406.17),

\[
\boxed{
 \Delta_4R_\sharp(e)
 \ge {L\over4}n\log n
 ={\log4\over4}n\log n
}
\tag{L-34406.18

cofinally and uniformly on the quarter-balanced cone.

Thus the compact two-tap source itself creates a deterministic reserve moat on exactly the RH-critical `n log n` scale.

## 8. Cofinal upper bound

On a fixed balanced cone, elementary Stirling gives

\[
 E(e)=O_\eta(\log(2n)),
\]

while

\[
 P_\sharp(e)=O(n)
\]

from the linear generalized-prime mass bound of `L-32415`.

It remains only to note that the second-moment difference in (L-34406.16) is `O_eta(n log(2n))`. This follows directly from (L-34406.12):

- `F(e)=O(n)`;
- `A_r<=N_r log2+log(2N_r)` and `d_rN_r<=Ln`, so `sum d_r A_r=O(n log(2n))` over `O(log n)` levels;
- `sum r4^r=O(n log(2n))`, so `sum K_r c_r=O(n log(2n))`;
- the ordinary grouped difference is `O_eta(n log(2n))` by the same elementary Stirling/sum comparison used in `L-32414`.

Hence

\[
\boxed{
 \Delta_4R_\sharp(e)
 =O_\eta(n\log(2n)).
}
\tag{L-34406.19

Combining with (L-34406.18) proves (L-34406.4).

## 9. Consequence for the live compact-current route

The compact source

\[
 B_\sharp=(1-4^{1-s})/\zeta
\]

is exactly the RH-sensitive compact source `B_circ` of PR #342. Thus one may work with a **single source-matched critical-scale Dirichlet system**:

```text
physical current:              q_circ=B_sharp';
positive inverse:              a_sharp>0;
nonnegative generalized primes Lambda_sharp>=0;
strict balanced reserve:       R_sharp>0;
new aligned reserve increment: Delta_4R_sharp=Theta(n log n).
```

The critical-scale moat is therefore not an artifact of comparing the denominator-bearing Q=4 source at two scales. It is already present in the compact source whose current is the actual hard innovation channel.

This does **not** prove the required current bound. The remaining source-matched theorem is now especially sharp:

> control the compact physical current (or its aligned one-step block) by the relative compact-source curvature `Delta_4R_sharp`, with the complete reflected/source-current terms retained.

Any such coefficient-one Hermitian/Schur estimate would combine directly with the normalized recurrence already resident on PR #345.

## 10. Proof boundary

Closed here, subject to independent review:

1. exact cancellation of every local first-moment level from the radix-four score;
2. exact second-moment radix-four decomposition;
3. cofinal lower bound `(log4/4)n log n` on the quarter-balanced cone;
4. cofinal fixed-cone upper bound `O(n log n)`;
5. source-matched identification with the compact RH-sensitive current system.

Still open:

1. compact-current/relative-reserve Hermitian domination;
2. coefficient-one global energy recurrence;
3. RH.

# L-34406 — The compact two-tap source has a critical radix-four reserve increment

Claim ID: `L-34406`  
Title: For the finite main-pole source `B_sharp=(1-4^(1-s))/zeta(s)`, the complete Selberg--Kummer reserve created by one aligned radix-four dilation is uniformly `Theta(n log n)` on every fixed balanced cone  
Status: **PROPOSED COMPLETE COFINAL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: PR #325 `L-32415/L-32414`; the elementary fourfold-binomial estimate used on PR #342  
Scope: deterministic source-matched reserve increment; no compact-current upper estimate or RH claim

## 1. Compact two-tap system

Put

\[
 B_\sharp(s)=\frac{1-4^{1-s}}{\zeta(s)},
 \qquad
 A_\sharp=B_\sharp^{-1}.
\]

Its generalized-prime sequence is

\[
\boxed{
 \Lambda_\sharp=\Lambda+D,
 \qquad
 D(4^r)=d_r:=4^rL,
 \quad L:=\log4,
 \quad r\ge1,
}
\tag{L-34406.1}

and zero off the four-adic tower. Let

\[
 C_\sharp=\Lambda_\sharp\log+
           \Lambda_\sharp*\Lambda_\sharp.
\]

For a carry row `e=(n,j)`, `k=n-j`, define

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
For

\[
 e^+=(4n,4j)
\]

put

\[
\boxed{
 \Delta_4R_\sharp(e)
 :=R_\sharp(e^+)-16R_\sharp(e).
}
\tag{L-34406.3}

We prove that on every fixed balanced cone, outside a finite base,

\[
\boxed{
 \Delta_4R_\sharp(e)=\Theta_\eta(n\log n).
}
\tag{L-34406.4}

## 2. The entire local first moment scales exactly

Let

\[
 F(e)=\log{n\choose j},
 \qquad
 c_r=\chi_{n,4^r}(j).
\]

Then

\[
\boxed{
 P_\sharp(e)=F(e)+\sum_{r\ge1}d_rc_r.
}
\tag{L-34406.5}

At the aligned row `e+`,

\[
 c'_1=0,
 \qquad
 c'_{r+1}=c_r,
 \qquad
 d_{r+1}=4d_r.
\]

Therefore every local four-adic first-moment term cancels from the relative score:

\[
\boxed{
 E(e):=P_\sharp(e^+)-4P_\sharp(e)
 =F(e^+)-4F(e).
}
\tag{L-34406.6}

In particular

\[
 E(e)\ge0
\tag{L-34406.7}

because

\[
 {4n\choose4j}\ge {n\choose j}^4.
\]

On every fixed balanced cone, the elementary two-sided Stirling inequalities give

\[
\boxed{
 E(e)=\Theta_\eta(\log n).
}
\tag{L-34406.8}

For the quarter-balanced cone, the fourfold mode-probability estimate already used on PR #342 gives, outside one absolute finite threshold,

\[
\boxed{
 E(e)\ge\frac12\log n.
}
\tag{L-34406.9}

## 3. Exact second-moment decomposition

Put

\[
 N_r=\left\lfloor\frac n{4^r}\right\rfloor,
 \qquad
 J_r=\left\lfloor\frac j{4^r}\right\rfloor,
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
 :=\sum_{a+b=t}d_ad_b
 =(t-1)4^tL^2,
 \qquad t\ge2,
\]

and `E_1^loc=0`. The four-adic product-carry identity of PR #325 gives exactly

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

At `e+`, the new level `r=1` contributes `2d_1F(e)=8LF(e)`, while every old quotient is shifted by one level. Direct substitution gives

\[
\boxed{
\begin{aligned}
&16\bigl[S_\sharp(e)-S_0(e)\bigr]
 -\bigl[S_\sharp(e^+)-S_0(e^+)\bigr]\\
&\qquad=-8LF(e)
 +24\sum_{r\ge1}d_rA_r
 +\sum_{r\ge1}K_rc_r,
\end{aligned}}
\tag{L-34406.12}

where

\[
\boxed{
 K_r=4^{r+1}(6r-5)L^2>0
 \qquad(r\ge1).
}
\tag{L-34406.13}

For `r=1`, `K_1=16L^2`; this includes the newly created local/local coefficient at level two.

Thus the only adverse source-local contribution is the explicit `-8LF(e)` term.

## 4. Ordinary Selberg slack leaves only a linear error

PR #325 `L-32414` proves, whenever the smaller child is at least six,

\[
\boxed{
 16S_0(e)-S_0(e^+)
 \ge12\log2\,F(e)
 =6LF(e).
}
\tag{L-34406.14}

Combining with (L-34406.12),

\[
\boxed{
 16S_\sharp(e)-S_\sharp(e^+)
 \ge-2LF(e).
}
\tag{L-34406.15}

All omitted terms are nonnegative. The finitely many balanced rows with smaller child below six belong to the finite base table and do not affect the cofinal theorem.

## 5. Relative reserve identity and lower moat

By (L-34406.6),

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
\tag{L-34406.16}

Since `P_sharp>=F`, equations (L-34406.15)--(L-34406.16) imply

\[
\boxed{
 \Delta_4R_\sharp(e)
 \ge8F(e)E(e)+E(e)^2-2LF(e)
 \ge2F(e)\,[4E(e)-L].
}
\tag{L-34406.17}

On the quarter-balanced cone,

\[
 F(e)\ge\frac n4\log2=\frac{nL}{8}.
\]

Outside the threshold in (L-34406.9), `E>=1/2 log n`. For `n>=4`, `log n>=L`, hence

\[
4E-L\ge2\log n-L\ge\log n.
\]

Thus

\[
\boxed{
 \Delta_4R_\sharp(e)
 \ge\frac{L}{4}n\log n
 =\frac{\log4}{4}n\log n
}
\tag{L-34406.18}

cofinally and uniformly on the quarter-balanced cone.

## 6. Matching upper bound

Still on a fixed balanced cone, Stirling gives

\[
E(e)=O_\eta(\log(2n)),
\]

and the linear generalized-prime mass bound of `L-32415` gives

\[
P_\sharp(e)=O(n).
\]

It remains to bound the second-moment difference in (L-34406.16). Equation (L-34406.12) gives this directly:

- `F(e)=O(n)`;
- `A_r<=N_r log2+log(2N_r)` and `d_rN_r<=Ln`, so `sum d_rA_r=O(n log(2n))` over `O(log n)` levels;
- `sum_{4^r<=n}r4^r=O(n log(2n))`, so `sum K_rc_r=O(n log(2n))`;
- the ordinary grouped difference is `O_eta(n log(2n))` by the same elementary Stirling/sum comparison used in `L-32414`.

Hence

\[
\boxed{
 \Delta_4R_\sharp(e)
 =O_\eta(n\log(2n)).
}
\tag{L-34406.19}

Together with (L-34406.18), this proves (L-34406.4).

## 7. Meaning for the compact-current route

The source

\[
B_\sharp=(1-4^{1-s})/\zeta
\]

is exactly the RH-sensitive compact source `B_circ` on PR #342. Thus the hard compact current already belongs to a **single source-matched critical-scale Dirichlet system**:

```text
physical current:               q_circ=B_sharp';
positive inverse:               a_sharp>0;
nonnegative generalized primes: Lambda_sharp>=0;
strict balanced reserve:        R_sharp>0;
aligned reserve increment:      Delta_4R_sharp=Theta(n log n).
```

So the critical moat is not an artifact of comparing the denominator-bearing Q=4 source at two scales. It is intrinsic to the compact source whose current is the hard innovation channel.

This does not prove the RH-scale current estimate. The remaining source-matched statement is now especially sharp:

> control the compact physical current, or its aligned block, by the relative compact-source curvature `Delta_4R_sharp`, with the complete reflected/source-current terms retained.

Such a Hermitian/Schur theorem would feed directly into the coefficient-one recurrence already resident on PR #345.

## 8. Proof boundary

Closed here, subject to independent review:

1. exact cancellation of every local first-moment level from the radix-four score;
2. exact second-moment radix-four decomposition;
3. explicit cofinal lower moat `(log4/4)n log n` on the quarter-balanced cone;
4. cofinal fixed-cone upper bound `O(n log n)`;
5. source-matched identification with the compact RH-sensitive current system.

Still open:

1. compact-current/relative-reserve Hermitian domination;
2. coefficient-one global energy recurrence;
3. RH.

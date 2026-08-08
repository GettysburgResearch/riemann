# L-32414 — The Q=4 reserve is radix-four supermultiplicative

Claim ID: `L-32414`  
Title: On every quarter-balanced row, the complete Q=4 Selberg forcing grows by at most sixteen under exact radix-four dilation, while the generalized Kummer first moment grows by at least four; consequently the reserve grows by at least sixteen  
Status: **PROPOSED COMPLETE THEOREM — ANALYTIC TAIL + EXACT SMALL-ROW REPLAY; INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: `L-32411`; ordinary Selberg carry identity; elementary logarithm inequalities  
Scope: deterministic row-reserve scaling; no RH conclusion by itself

## 1. Statement

Retain the Q=4 generalized Kummer profile, complete Selberg forcing, and reserve

\[
 P_4(n,j),\qquad S_4(n,j),\qquad
 \mathcal R_4(n,j)=P_4(n,j)^2-S_4(n,j)
\]

from `L-32405/L-32411`.

For every integer

\[
 n\ge4,
 \qquad
 {n\over4}\le j\le{3n\over4},
\]

one has

\[
\boxed{
 S_4(4n,4j)\le16S_4(n,j),
}
\tag{L-32414.1}

and hence

\[
\boxed{
 \mathcal R_4(4n,4j)\ge16\mathcal R_4(n,j).
}
\tag{L-32414.2}

The inequalities are strict on every nontrivial row in the declared range.

This supplies the second-moment radix-four law explicitly left open in `L-32411`.

## 2. First moment

By symmetry assume

\[
 j\le k:=n-j.
\]

`L-32411.10` proves exactly

\[
\boxed{
 P_4(4n,4j)-4P_4(n,j)
 =\log{\binom{4n}{4j}\over\binom nj^4}
 +3\log4\,\kappa_4(n,j)
 \ge0.
}
\tag{L-32414.3]

Thus

\[
\boxed{P_4(4n,4j)\ge4P_4(n,j).}
\tag{L-32414.4}

The work is therefore entirely in the second moment.

## 3. Ordinary Selberg forcing: exact grouped form

Let

\[
 H_2(N)=\sum_{m=1}^N\log^2m,
\]

and put

\[
 S_0(n,j)=H_2(n)-H_2(j)-H_2(k).
\]

For `1<=r<=j`, define

\[
 a_r=\log{k+r\over r},
 \qquad
 g_r=\log^2(k+r)-\log^2r.
\]

Then

\[
\boxed{
 \log\binom nj=\sum_{r=1}^j a_r,
 \qquad
 S_0(n,j)=\sum_{r=1}^jg_r.
}
\tag{L-32414.5}

The scaled forcing groups naturally into the four integers

\[
 m=4r-3,4r-2,4r-1,4r.
\]

Write

\[
 G_r=\sum_{m=4r-3}^{4r}
 [\log^2(4k+m)-\log^2m].
\tag{L-32414.6}

Then

\[
 S_0(4n,4j)=\sum_{r=1}^jG_r.
\]

We prove the stronger slack estimate

\[
\boxed{
 16S_0(n,j)-S_0(4n,4j)
 \ge12\log2\,\log\binom nj
}
\tag{L-32414.7]

whenever `k>=6`. The finitely many rows with `k<=5` are handled in Section 7.

## 4. Proof of the ordinary slack for `k>=6`

Put

\[
 \ell=\log2.
\]

It is enough to prove for every `r`

\[
16g_r-G_r\ge12\ell a_r.
\tag{L-32414.8}

### 4.1 The first group `r=1`

Put `p=log(k+1)`. For `1<=m<=4`,

\[
4k+m\le4(k+1),
\]

so

\[
G_1\le4(p+2\ell)^2
-[\log^22+\log^23+\log^24].
\]

Therefore the left side of (L-32414.8), after subtracting its right side, is at least

\[
12p^2-28\ell p-16\ell^2
+[\log^22+\log^23+\log^24].
\tag{L-32414.9}

For `k>=6`,

\[
p\ge\log7>{14\over5}\ell
\]

because `7^5>2^14`. Also `log3>(3/2)ell` because `9>8`. The quadratic in `p` is increasing in this range, and hence (L-32414.9) is larger than

\[
\left[
12\left({14\over5}\right)^2
-28\left({14\over5}\right)
-16+{29\over4}
\right]\ell^2
={693\over100}\ell^2>0.
\]

### 4.2 The second group `r=2`

Put `p=log(k+2)`, so `p>=2ell`. For `5<=m<=8`,

\[
4k+m\le4(k+2).
\]

Hence the required margin is at least

\[
12p^2-28\ell p-20\ell^2
+\sum_{m=5}^8\log^2m.
\tag{L-32414.10}

It is increasing for `p>=2ell`. The elementary integer comparisons

```text
5^10 > 2^23,
6^2  > 2^5,
7^5  > 2^14
```

give

\[
\log5>{23\over10}\ell,
\quad
\log6>{5\over2}\ell,
\quad
\log7>{14\over5}\ell,
\quad
\log8=3\ell.
\]

Thus at `p=2ell`, (L-32414.10) is greater than

\[
\left[
-28
+\left({23\over10}\right)^2
+\left({5\over2}\right)^2
+\left({14\over5}\right)^2
+9
\right]\ell^2
={19\over50}\ell^2>0.
\]

### 4.3 Every group `r>=3`

Put

\[
p=\log(k+r),\qquad q=\log r,\qquad c=\log3.
\]

Then

\[
p\ge q+\ell,
\qquad q\ge c>{3\over2}\ell.
\]

For every `m in [4r-3,4r]`,

\[
4k+m\le4(k+r),
\qquad
m\ge4r-3\ge3r.
\]

Therefore

\[
G_r\le4[(p+2\ell)^2-(q+c)^2].
\]

After subtracting `12ell(p-q)` from `16(p^2-q^2)-G_r`, the remaining lower bound is

\[
12p^2-12q^2-28\ell p
+(8c+12\ell)q-16\ell^2+4c^2.
\tag{L-32414.11}

It is increasing in `p` on the declared region, so put `p=q+ell`. The result is

\[
8(\ell+c)q+4c^2-32\ell^2.
\]

Using `q>=c>(3/2)ell` gives the strict lower bound

\[
4(2\ell c+3c^2-8\ell^2)>7\ell^2>0.
\]

This proves (L-32414.8), and summation proves (L-32414.7), for every `k>=6`.

## 5. Radix-four scaling of the local Q=4 terms

Use the prime-free decomposition of `L-32411`. Put

\[
L=\log4,
\qquad
 d_r=(4^r-1)L,
\]

\[
 c_r=\chi_{n,4^r}(j),
\]

and

\[
 A_r=F(N_r,J_r)+c_r\log(N_r-J_r)\ge0
\]

with the conventions of `L-32411`.

Let

\[
 E_t=\sum_{a+b=t}d_ad_b,
 \qquad E_1=0.
\]

The nonordinary part of `S_4(n,j)` is

\[
\mathcal L(n,j)
=\sum_{r\ge1}d_rrL c_r
+2\sum_{r\ge1}d_rA_r
+\sum_{t\ge2}E_tc_t.
\tag{L-32414.12}

Under `(n,j) mapsto (4n,4j)`,

\[
 c'_1=0,
 \qquad c'_{r+1}=c_r,
\]

and the quotient pair in level `r+1` is exactly the former level-`r` quotient pair. The sole new mixed term is the first quotient `F(n,j)`. Consequently

\[
\begin{aligned}
\mathcal L(4n,4j)
={}&\sum_{r\ge1}d_{r+1}(r+1)Lc_r\\
&+2d_1F(n,j)
 +2\sum_{r\ge1}d_{r+1}A_r\\
&+\sum_{t\ge1}E_{t+1}c_t.
\end{aligned}
\tag{L-32414.13}

Now

\[
{d_{r+1}\over d_r}
=4+{3\over4^r-1}\le5,
\]

so

\[
16d_r-d_{r+1}>0.
\tag{L-32414.14}

Moreover the coefficient of each `c_r` in
`16 mathcal L(n,j)-mathcal L(4n,4j)`, after removing the nonnegative `A_r` part, is

\[
 K_r
 =L[16d_rr-d_{r+1}(r+1)]
 +16E_r-E_{r+1}.
\tag{L-32414.15}

One finds exactly

\[
\boxed{K_1=9L^2>0,}
\tag{L-32414.16}

while for `r>=2`, using

\[
{E_r\over L^2}
=\left(r-{5\over3}\right)4^r+r+{5\over3},
\]

gives

\[
\boxed{
{K_r\over L^2}
=(24r-28)4^r+25>0.
}
\tag{L-32414.17]

Therefore

\[
\boxed{
16\mathcal L(n,j)-\mathcal L(4n,4j)
\ge-2d_1F(n,j).
}
\tag{L-32414.18]

Since `d_1=3 log4=6 log2`, the right side is exactly

\[
-12\log2\,F(n,j).
\]

For `k>=6`, the ordinary slack (L-32414.7) pays this term exactly. Hence

\[
\boxed{
 S_4(4n,4j)\le16S_4(n,j)
}
\tag{L-32414.19]

for every balanced row with `k>=6`.

## 6. Reserve scaling

Combine (L-32414.4) and (L-32414.19):

\[
\begin{aligned}
\mathcal R_4(4n,4j)
&=P_4(4n,4j)^2-S_4(4n,4j)\\
&\ge16P_4(n,j)^2-16S_4(n,j)\\
&=16\mathcal R_4(n,j).
\end{aligned}
\]

Thus (L-32414.2) follows in the cofinal range directly from exact arithmetic scaling, not from the crude `R_4 asymp P_4^2` estimate.

## 7. The eleven small balanced rows

If `k=n-j<=5`, quarter balance and `j<=k` leave exactly

```text
(4,1), (4,2), (5,2),
(6,2), (6,3),
(7,2), (7,3),
(8,3), (8,4),
(9,4), (10,5).
```

`X-32414-q4-radix4-reserve-scaling` evaluates `C_4` through parent `40` using only integer factorization and directed rational atanh-series enclosures for every logarithm. It proves

\[
16S_4(n,j)-S_4(4n,4j)>0
\]

on all eleven rows. The smallest lower margin is at `(n,j)=(6,2)` and exceeds `7.33`.

Retained result digest:

```text
a129e1fec64bbbeeae3edc69e7796c6609cb62df0f702aeb0b69494e6d8c1557
```

This completes the finite range and hence the theorem.

## 8. Consequence for the Q=4 proof graph

Before this lemma, the exact source renewal

\[
 c_4=h_4+\delta_4*c_4
\]

had a coefficient-one lower-scale principal state, while the deterministic row reserve had no proven compatible scale law.

Now the same radix-four dilation satisfies

```text
current principal amplitude:      1/2 at scale X/4;
current principal energy:         1/4 at scale X/4;
Selberg--Kummer reserve:          >=16 times the lower row reserve.
```

Thus the reserve is not merely positive; it is strongly aligned with the exact radix of the neutral source renewal. Any remaining obstruction to the coefficient-one block recurrence must come from the reflected/source-convolved placement and boundary accounting, not from degeneration of the reserve under the renewal scale.

This theorem does not by itself bound the RH-sensitive current: a deterministic large reserve cannot be converted into a fluctuation bound without the exact reflected orientation.

## 9. Proof boundary

Closed exactly, subject to replay:

- the ordinary Selberg fourfold slack estimate;
- complete scaling algebra of every four-adic forcing term;
- `S_4(4n,4j)<=16S_4(n,j)` on every balanced row;
- `R_4(4n,4j)>=16R_4(n,j)`;
- exact small-row directed replay.

Still open:

- the final source-convolved reflected orientation/placement turning the scale-aligned reserve into a global energy recurrence;
- the neutral coefficient-one recurrence;
- RH.

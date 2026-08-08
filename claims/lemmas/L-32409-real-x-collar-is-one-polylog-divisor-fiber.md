# L-32409 — The real-X collar is one polylogarithmic divisor fiber

Claim ID: `L-32409`  
Title: Between consecutive integer parents, every atomized `Q=4` physical carry row is exactly an integer balanced row plus at most one divisor increment of size `O(log^2 X)`  
Status: **PROPOSED COMPLETE EXACT COLLAR THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: `L-32407`, `L-32408`; elementary floor algebra  
Scope: real endpoint `X` and balanced carry positions; no reflected Selberg recurrence or RH conclusion

## 1. Real atomized physical row

For real

\[
 X\ge1,
 \qquad0\le\theta\le1,
\]

put

\[
 \mathcal C(X/q,\theta)
 =\left\lfloor\frac Xq\right\rfloor
  -\left\lfloor\frac{\theta X}{q}\right\rfloor
  -\left\lfloor\frac{(1-\theta)X}{q}\right\rfloor.
\]

For the `Q=4` physical coefficients `c_4` of `L-32407`, define the unnormalized field

\[
 \boxed{
 \mathcal Q_4(X,\theta)
 =\sum_qc_4(q)\mathcal C(X/q,\theta).
 }
 \tag{L-32409.1}
\]

The normalized pole field is `X^(-1/2) mathcal Q_4`.

Let

\[
 N=\lfloor X\rfloor,
 \qquad N\le X<N+1.
\]

## 2. Exact floor collapse inside one unit cell

Because every multiple of the integer `q` is itself an integer,

\[
 \boxed{
 \left\lfloor\frac Xq\right\rfloor
 =\left\lfloor\frac Nq\right\rfloor
 \qquad(N\le X<N+1).
 }
 \tag{L-32409.2}
\]

Set

\[
 j=\lfloor\theta X\rfloor,
 \qquad
 k=\lfloor(1-\theta)X\rfloor.
\]

For integer `q`,

\[
 \left\lfloor\frac{\theta X}{q}\right\rfloor
 =\left\lfloor\frac jq\right\rfloor,
 \qquad
 \left\lfloor\frac{(1-\theta)X}{q}\right\rfloor
 =\left\lfloor\frac kq\right\rfloor.
 \tag{L-32409.3}
\]

Since

\[
 N\le j+k+\{\theta X\}+\{(1-\theta)X\}<N+1,
\]

one has exactly

\[
 \boxed{j+k\in\{N-1,N\}.}
 \tag{L-32409.4}
\]

Thus the entire apparent continuous collar has only one missing-unit bit.

## 3. Reduction to one integer row plus one divisor fiber

Retain the integer prefix state

\[
 A_4(M)=\sum_qc_4(q)\left\lfloor\frac Mq\right\rfloor
\]

from `L-32408`, and define its unit increment

\[
 \boxed{
 D_4(M)=A_4(M)-A_4(M-1)=\sum_{q\mid M}c_4(q).
 }
 \tag{L-32409.5}
\]

If `j+k=N`, then directly

\[
 \boxed{
 \mathcal Q_4(X,\theta)=Q_4(N,j).
 }
 \tag{L-32409.6}
\]

If `j+k=N-1`, let `K=N-j=k+1`. Then

\[
\begin{aligned}
 \mathcal Q_4(X,\theta)
 &=A_4(N)-A_4(j)-A_4(K-1)\\
 &=Q_4(N,j)+D_4(K).
\end{aligned}
\]

Hence in every case

\[
 \boxed{
 \mathcal Q_4(X,\theta)
 =Q_4(N,j)+\epsilon D_4(N-j),
 \qquad
 \epsilon\in\{0,1\}.
 }
 \tag{L-32409.7}
\]

There is no growing continuum boundary bank.

## 4. The divisor fiber is only logarithmic-squared

Let

\[
 M=2^v m,
 \qquad m\text{ odd}.
\]

Use the exact coefficient support of `L-32407`.

### 4.1 Odd prime-power divisors

The positive odd-prime-power divisors contribute in absolute value at most

\[
 \sum_{p\mid m}v_p(m)\log p
 =\log m
 \le\log M.
 \tag{L-32409.8}
\]

For each admissible `4`-adic dilation there is one `-3` copy. There are at most `v/2` such dilation levels, so their absolute contribution is at most

\[
 \frac{3v}{2}\log M.
 \tag{L-32409.9}
\]

Since

\[
 v\log2\le\log M,
 \qquad
 \log2>69/100,
\]

this is less than

\[
 \frac{150}{46}(\log M)^2.
 \tag{L-32409.10}
\]

### 4.2 Pure dyadic divisors

Equations (L-32407.6)--(L-32407.7) give

\[
 \sum_{2^r\mid M}|c_4(2^r)|
 \le(\log2)\left(\frac34v^2+\frac{19}{4}v\right).
 \tag{L-32409.11}
\]

Using `v<=log M/log2`, `log2>69/100`, and `log M>=log2`, the right side is bounded by

\[
 8(\log M)^2.
 \tag{L-32409.12}
\]

Combining (L-32409.8), (L-32409.10), and (L-32409.12), a deliberately loose uniform constant gives

\[
 \boxed{
 |D_4(M)|\le13[\log(2M)]^2
 \qquad(M\ge1).
 }
 \tag{L-32409.13}
\]

The use of `log(2M)` absorbs `M=1` without a special case.

## 5. Continuous balanced physical-to-reserve transference

Restrict now to

\[
 \frac13\le\theta\le\frac23,
 \qquad X\ge12.
\]

With `N=floor X` and `j=floor(theta X)`, elementary endpoint arithmetic gives

\[
 \frac N4\le j\le\frac{3N}{4}.
 \tag{L-32409.14}
\]

Therefore `L-32407` applies to the integer row `Q_4(N,j)`.

By (L-32409.7), (L-32409.13), and `(a+b)^2<=2a^2+2b^2`,

\[
\boxed{
 |\mathcal Q_4(X,\theta)|^2
 \le
 22000\,\mathcal R_4(N,j)
 +338[\log(2N)]^4.
}
 \tag{L-32409.15}
\]

After physical normalization,

\[
 \boxed{
 |\mathfrak P_{4,\theta}(\log X)|^2
 \le
 \frac{22000}{X}\mathcal R_4(N,j)
 +\frac{338}{X}[\log(2N)]^4.
 }
 \tag{L-32409.16}
\]

Thus the real-`X` collar contributes only an explicit polylogarithmic-over-`X` forcing. It is not an independent RH-bearing estimate.

## 6. Carry-position integration

As `theta` varies with `X` fixed, the integer `j=floor(theta X)` is constant on intervals of length at most `1/X`. Consequently integration over `[1/3,2/3]` turns (L-32409.16) into a finite row sum with explicit nonnegative weights:

\[
 \int_{1/3}^{2/3}
 |\mathfrak P_{4,\theta}(\log X)|^2d\theta
 \le
 \frac{22000}{X^2}
 \sum_{j\in\mathcal B_X}\mathcal R_4(N,j)
 +O\!\left(\frac{\log^4(2X)}X\right),
 \tag{L-32409.17}
\]

where `mathcal B_X` is the corresponding balanced integer row set; endpoint cells only improve the `1/X` weight.

This is the complete real-`X` physical-to-reserve adapter for the `Q=4` atomized field.

## 7. Consequence for the proof graph

The former list of possible continuous-collar obstructions collapses to

```text
integer balanced Q=4 reserve          CLOSED by L-32405;
integer physical-to-reserve map       CLOSED by L-32407;
real-X / irrational-theta collar      CLOSED here by one divisor fiber;
deterministic local-Euler gauge        CLOSED by L-32406.
```

The unresolved component is now genuinely the reflected **reserve accounting**: prove that the integrated reserve on the right of (L-32409.17) is supplied once, with the correct sign, by the complete independent-frequency Selberg identity while the all-pass scattering state is passed to lower logarithmic scale with coefficient one.

## 8. Proof boundary

Closed exactly here:

1. all real-`X` parent floors inside a unit interval;
2. both child floors through two integers `j,k`;
3. the dichotomy `j+k=N` or `N-1`;
4. reduction to one standard integer row plus one divisor fiber;
5. a uniform `O(log^2 X)` divisor-fiber bound;
6. the complete continuous balanced physical-to-reserve estimate.

Open:

1. reflected reserve accounting/no-double-spend;
2. the coefficient-one scattering-state recurrence;
3. RH.

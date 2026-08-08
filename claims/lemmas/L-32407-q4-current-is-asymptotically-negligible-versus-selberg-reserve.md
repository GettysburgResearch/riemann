# L-32407 — The Q=4 RH-sensitive current is asymptotically negligible versus its Selberg reserve

Claim ID: `L-32407`  
Title: On every fixed balanced carry cone, the main-pole-killing Q=4 current consumes an arbitrarily small fraction of the source-matched Selberg–Kummer reserve  
Status: **PROPOSED COMPLETE UNCONDITIONAL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: `L-32404`, `L-32405`; the classical prime number theorem  
Scope: exact Q=4 source current and balanced carry rows; no RH assumption and no global recurrence claim

## 1. The Q=4 current

Retain

\[
 B_4(s)=\frac{1-4^{1-s}}{(1-4^{-s})\zeta(s)},
 \qquad A_4=B_4^{-1},
\]

with coefficient sequence `b_4`, generalized von Mangoldt sequence
`Lambda_4`, and Selberg forcing

\[
 C_4=\Lambda_4\log+\Lambda_4*\Lambda_4.
\]

Define the RH-sensitive inverse-source current

\[
 \boxed{q_4=b_4*\Lambda_4=-b_4\log.}
 \tag{L-32407.1}
\]

For an integer carry row `n=j+k`, put

\[
 Q_4(n,j)=\sum_{d\le n}q_4(d)\chi_{n,d}(j),
\]

and retain

\[
 P_4(n,j)=\sum_{d\le n}\Lambda_4(d)\chi_{n,d}(j),
\]

\[
 R_4(n,j)=P_4(n,j)^2-
 \sum_{d\le n}C_4(d)\chi_{n,d}(j).
\]

By `L-32405`, for every `n>=4735` and every quarter-balanced row,

\[
 \boxed{R_4(n,j)>\frac1{20}P_4(n,j)^2,}
 \tag{L-32407.2}
\]

and

\[
 \boxed{P_4(n,j)\ge\frac n4\log2.}
 \tag{L-32407.3}
\]

## 2. Exact generalized-Chebyshev form of the current

Let

\[
 e_4=\mathbf1*b_4.
\]

From `L-32404.10`,

\[
 e_4(1)=1,
 \qquad e_4(4^r)=-3\quad(r\ge1),
\]

and all other coefficients vanish. Since

\[
 \mathbf1*q_4=e_4*\Lambda_4,
\]

define

\[
 G_4(x)=\sum_{m\le x}q_4(m).
\]

Then finite convolution gives exactly

\[
 \boxed{
 G_4(x)=\Psi_4(x)-3\sum_{r\ge1}\Psi_4(x/4^r),
 }
 \tag{L-32407.4}
\]

where

\[
 \Psi_4(x)=\sum_{m\le x}\Lambda_4(m).
\]

As for every divisor-prefix current, summation of the carry indicators gives

\[
 \boxed{
 Q_4(n,j)=G_4(n)-G_4(j)-G_4(n-j).
 }
 \tag{L-32407.5}
\]

No asymptotic input enters (L-32407.4)--(L-32407.5).

## 3. Cancellation of the complete linear density

By `L-32404.8`,

\[
 \Psi_4(x)=\psi(x)+D_4(x),
\]

where

\[
 D_4(x)=(\log4)\sum_{4^r\le x}(4^r-1).
\]

Insert this into (L-32407.4). The ordinary-prime part is

\[
 H(x)=\psi(x)-3\sum_{r\ge1}\psi(x/4^r).
 \tag{L-32407.6}
\]

The local Q=4 correction telescopes coefficientwise. At the atom `4^m`,

\[
 (e_4*D_4)(4^m)
 =(\log4)\left[(4^m-1)
 -3\sum_{r=1}^{m-1}(4^{m-r}-1)\right]
 =3m\log4.
\]

Therefore its prefix contributes only

\[
 \boxed{
 L(x)=3\log4\sum_{1\le m\le\log_4x}m
 =O((\log x)^2).
 }
 \tag{L-32407.7}
\]

Hence

\[
 \boxed{G_4(x)=H(x)+O((\log x)^2).}
 \tag{L-32407.8}
\]

Now use the prime number theorem

\[
 \psi(y)=y+o(y).
\]

The linear terms in (L-32407.6) cancel exactly because

\[
 3\sum_{r\ge1}4^{-r}=1.
\]

To justify the infinite tail uniformly, fix `R`. For `r<=R`, the PNT gives

\[
 \psi(x/4^r)=x/4^r+o(x)
\]

for each fixed `r`; for `r>R`, the elementary Chebyshev bound
`psi(y)<<y` gives a total `O(x4^{-R})`. Let first `x->infinity` and then
`R->infinity`. Thus

\[
 \boxed{H(x)=o(x),}
 \tag{L-32407.9}
\]

and (L-32407.8) yields

\[
 \boxed{G_4(x)=o(x).}
 \tag{L-32407.10}
\]

This is unconditional. It uses only the classical PNT, equivalently the
classical zero-free theorem on `Re(s)=1`; it contains no critical-strip zero
estimate.

## 4. Uniform balanced current bound

Fix `0<eta<=1/2`. From (L-32407.10), for every `epsilon>0` there is `X_0`
such that

\[
 |G_4(x)|\le\epsilon x
 \qquad(x\ge X_0).
\]

If

\[
 \eta n\le j\le(1-\eta)n
\]

and `n>=X_0/eta`, then all three arguments in (L-32407.5) are at least
`X_0` except the parent, which is larger still. Therefore

\[
 \boxed{
 |Q_4(n,j)|\le2\epsilon n.
 }
 \tag{L-32407.11}
\]

Equivalently,

\[
 \boxed{
 \sup_{\eta n\le j\le(1-\eta)n}
 \frac{|Q_4(n,j)|}{n}\longrightarrow0.
 }
 \tag{L-32407.12}
\]

For the quarter-balanced cone used in `L-32405`, combine
(L-32407.2)--(L-32407.3) with (L-32407.11):

\[
 \frac{|Q_4(n,j)|^2}{R_4(n,j)}
 <
 \frac{4\epsilon^2n^2}
 {(1/20)(n^2/16)\log^22}
 =\frac{1280\epsilon^2}{\log^22}.
\]

Since `epsilon` is arbitrary,

\[
 \boxed{
 \sup_{n/4\le j\le3n/4}
 \frac{|Q_4(n,j)|^2}{R_4(n,j)}
 \longrightarrow0.
 }
 \tag{L-32407.13}
\]

Thus for every declared absorption fraction `delta>0`, there exists
`N_delta` such that

\[
 \boxed{
 |Q_4(n,j)|^2\le\delta R_4(n,j)
 }
 \tag{L-32407.14}
\]

for all `n>=N_delta` and all quarter-balanced `j`.

## 5. Finite normal-Gram consequence

Let `nu(n,j)>=0` be any finite measure supported on quarter-balanced rows with
parents `n>=N_delta`. Multiplying (L-32407.14) and summing gives

\[
 \boxed{
 \sum_{n,j}\nu(n,j)|Q_4(n,j)|^2
 \le\delta\sum_{n,j}\nu(n,j)R_4(n,j).
 }
 \tag{L-32407.15}
\]

The coefficient `delta` can be made arbitrarily small merely by moving the
parent scale outward. This is stronger than a fixed source-transference
constant.

In particular, any source-complete reflected block whose positive Schur reserve
is the row measure of `R_4` can absorb the complete Q=4 RH-sensitive current
with vanishing relative charge on its cofinal balanced interior.

## 6. Why this does not already prove RH

The theorem supplies the missing **current-to-reserve absorption coefficient**.
It does not by itself prove that the reflected source identity presents the
complete physical current and this reserve with the required signs and no
unpaid same-scale term. That final source-complete Schur assembly remains a
separate operator identity/inequality.

Likewise, no bound is asserted for the reserve itself; it is used as positive
slack, not estimated by absolute value.

## 7. Proof boundary

Closed here, subject to independent review:

1. the exact Q=4 generalized-Chebyshev current formula;
2. exact cancellation of the complete linear density;
3. the unconditional PNT consequence `G_4(x)=o(x)`;
4. uniform balanced current decay;
5. the vanishing current-to-Selberg-reserve ratio;
6. the induced arbitrarily-small finite normal-Gram absorption coefficient.

Still open:

1. the complete independent-frequency reflected Schur assembly for the Q=4
   current;
2. the resulting neutral scattering recurrence;
3. RH.

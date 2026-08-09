# L-32421 — Root-of-unity radix-four channels eliminate every mixed local Selberg term at finite scale

Claim ID: `L-32421`  
Title: A sufficiently fine finite root-of-unity source frame separates all active four-adic generalized-prime levels into nonnegative Fourier channels, so the complete Hermitian averaged Selberg reserve is the ordinary reserve plus explicit local squares  
Status: **PROPOSED COMPLETE EXACT FINITE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: ordinary Selberg–Kummer reserve `L-29002`; finite Fourier orthogonality  
Scope: arbitrary finite endpoint and all carry rows; channel count may depend on the endpoint; no current-energy upper estimate or RH conclusion

## 1. Finite root-of-unity source frame

Fix an integer `M>=2` and let

\[
 \Omega_M=\{\omega:\omega^M=1\}.
\]

Put

\[
 a(s)=4^{1-s}
\]

and for every `omega in Omega_M` define

\[
\boxed{
 B_\omega(s)=\frac{1-\omega a(s)}{\zeta(s)},
 \qquad
 A_\omega=B_\omega^{-1}.
}
\tag{L-32421.1}
\]

The bare inverse-source coefficients are the two-tap sequences

\[
 b_\omega=(\varepsilon-4\omega\delta_4)*\mu.
\tag{L-32421.2}
\]

Averaging the sources gives exact zero-delay reconstruction

\[
\boxed{
 {1\over M}\sum_{\omega\in\Omega_M}B_\omega(s)
 ={1\over\zeta(s)}.
}
\tag{L-32421.3}
\]

Differentiation gives the same current reconstruction:

\[
\boxed{
 {1\over M}\sum_\omega B_\omega'(s)
 =\left({1\over\zeta(s)}\right)'.
}
\tag{L-32421.4}

## 2. Exact critical frame

On the critical line, `|a(s)|=2`. Finite Fourier orthogonality gives

\[
\begin{aligned}
 {1\over M}\sum_\omega|1-\omega a|^2
 &=1+|a|^2\\
 &=5.
\end{aligned}
\]

Therefore

\[
\boxed{
 {1\over M}\sum_\omega|B_\omega(1/2+it)|^2
 ={5\over|\zeta(1/2+it)|^2}.
}
\tag{L-32421.5]

(The closing bracket in the tag is typographical only.)

Thus the family is a normalized tight reciprocal-zeta source frame independent of `M`.

## 3. Generalized-prime Fourier channels

Let

\[
 \Lambda_\omega=-A_\omega'/A_\omega.
\]

Since

\[
 {\omega a\over1-\omega a}
 =\sum_{r\ge1}\omega^r a^r,
\]

one has

\[
\boxed{
 \Lambda_\omega(n)
 =\Lambda(n)
  +(\log4)\sum_{r\ge1}
    \omega^r4^r\mathbf1_{n=4^r}.
}
\tag{L-32421.6}

Define the finite Fourier channels

\[
\boxed{
 \Lambda_m
 ={1\over M}\sum_{\omega\in\Omega_M}
  \omega^{-m}\Lambda_\omega,
 \qquad m\in\mathbf Z/M\mathbf Z.
}
\tag{L-32421.7}

Then each `Lambda_m` is real and coefficientwise nonnegative:

\[
\boxed{
 \Lambda_0(n)
 =\Lambda(n)
  +(\log4)\sum_{\substack{r\ge1\\r\equiv0\ (M)}}
    4^r\mathbf1_{n=4^r}\ge0,
}
\tag{L-32421.8}

and, for `m!=0`,

\[
\boxed{
 \Lambda_m(n)
 =(\log4)\sum_{\substack{r\ge1\\r\equiv m\ (M)}}
  4^r\mathbf1_{n=4^r}\ge0.
}
\tag{L-32421.9}

The inverse transform is

\[
 \Lambda_\omega=\sum_{m\bmod M}\omega^m\Lambda_m.
\tag{L-32421.10}
\]

## 4. Hermitian first moment and averaged forcing

For a carry row `e=(n,j)`, put

\[
 P_m(e)=\mathcal L_e(\Lambda_m).
\]

Then

\[
 P_\omega(e)=\sum_m\omega^mP_m(e)
\]

and Fourier orthogonality gives the exact Hermitian energy

\[
\boxed{
 {1\over M}\sum_\omega|P_\omega(e)|^2
 =\sum_mP_m(e)^2.
}
\tag{L-32421.11}

For each complex channel let

\[
 C_\omega=\Lambda_\omega\log+\Lambda_\omega*\Lambda_\omega.
\]

Averaging the algebraic Selberg forcing gives

\[
\boxed{
 C^{(M)}
 :={1\over M}\sum_\omega C_\omega
 =\Lambda_0\log
  +\sum_{m\bmod M}\Lambda_m*\Lambda_{-m}.
}
\tag{L-32421.12}

Every coefficient on the right is nonnegative. The corresponding Hermitian averaged row reserve is

\[
\boxed{
 \mathcal R_M(e)
 =\sum_mP_m(e)^2-\mathcal L_e(C^{(M)}).
}
\tag{L-32421.13}

For `M=2` this specializes to the simple plus/minus reserve of `L-32417`.

## 5. Complete separation at a fixed endpoint

Fix an endpoint `n` and put

\[
 R=\lfloor\log_4n\rfloor.
\]

Choose

\[
\boxed{M>2R.}
\tag{L-32421.14}

Then no active local level `1<=r<=R` is congruent to zero modulo `M`, and no two active levels satisfy

\[
 r_1+r_2\equiv0\pmod M,
\]

because

\[
 2\le r_1+r_2\le2R<M.
\]

Therefore, on all coefficients visible at the endpoint `n`,

\[
\boxed{
 \Lambda_0=\Lambda,
}
\tag{L-32421.15}

while each active level `r` occupies its own nonzero channel with

\[
\boxed{
 \Lambda_r=(4^r\log4)\delta_{4^r}.
}
\tag{L-32421.16}

Most importantly, every local logarithmic term and every mixed/local-local convolution disappears from the averaged forcing:

\[
\boxed{
 C^{(M)}=\Lambda\log+\Lambda*\Lambda
}
\tag{L-32421.17}

through the complete endpoint `n`.

Thus, writing

\[
 F(e)=\mathcal L_e(\Lambda)=\log\binom nj,
\]

and

\[
 S_0(e)=\mathcal L_e(\Lambda\log+\Lambda*\Lambda),
\]

one obtains the exact finite identity

\[
\boxed{
 \mathcal R_M(e)
 =F(e)^2-S_0(e)
  +\sum_{r=1}^{R}
    (4^r\log4)^2\chi_{n,4^r}(j).
}
\tag{L-32421.18]

(The closing bracket in the tag is typographical only.)

The ordinary Selberg–Kummer theorem `L-29002` gives

\[
 F(e)^2-S_0(e)\ge0.
\]

Hence

\[
\boxed{
 \mathcal R_M(e)\ge0
}
\tag{L-32421.19}

for every carry row at the endpoint, without a finite numerical scan and without a mixed-source estimate.

## 6. Source-complete interpretation

The theorem changes the finite source geometry substantially:

```text
fixed two-channel pair:
    infinitely many four-adic levels share two channels;
    mixed local convolutions must be absorbed;

endpoint-adaptive M-channel frame, M>2 log_4 n:
    every active local level has its own positive channel;
    no active local level enters the zero channel;
    no two active local levels can convolve back to the zero channel;
    averaged forcing is exactly the ordinary Selberg forcing;
    all local source energy survives only as explicit positive squares.
```

The normalized critical frame constant remains `5`, independent of `M`, by (L-32421.5). Thus increasing the channel count does not inflate the source-frame norm.

## 7. Current frame

Let

\[
 q_\omega=B_\omega'.
\]

Writing `L=log4` and `a=4^(1-s)`,

\[
 q_\omega
 =(1-\omega a)q_0
  +L\omega a B_0.
\]

Consequently Fourier orthogonality gives, on the critical line,

\[
\boxed{
 {1\over M}\sum_\omega|q_\omega|^2
 =|q_0|^2+4|q_0-LB_0|^2.
}
\tag{L-32421.20]

Again the right side is independent of `M`. The ordinary RH pole current is reconstructed by the channel average, while the orthogonal complement is one explicit local-Euler detail.

Thus channel separation removes the mixed **Selberg forcing** but does not, by itself, upper-bound the RH-sensitive current energy.

## 8. Proof boundary

Closed exactly:

1. finite root-of-unity source frame;
2. zero-delay source/current reconstruction;
3. coefficientwise nonnegative Fourier generalized-prime channels;
4. exact Hermitian first-moment Parseval identity;
5. exact averaged Selberg forcing;
6. complete endpoint separation for `M>2 floor(log_4n)`;
7. reserve = ordinary reserve plus explicit local squares;
8. critical frame/current identities independent of `M`.

Still open:

1. a dissipative upper estimate for the source-convolved current frame;
2. an RH-facing block recurrence;
3. RH.

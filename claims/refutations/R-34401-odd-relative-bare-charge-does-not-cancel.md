# R-34401 — The aligned odd-source relative bare charge does not cancel

Claim ID: `R-34401`  
Title: The odd Möbius source has aligned radix-four bare-charge increment `-2`, not zero; the claimed cross-free relative curvature therefore retains its second-current term  
Status: **FALSE CLAIM IDENTIFIED EXACTLY — CORRECTED FORMULA SUPPLIED**  
Authoring/review agent: `gpt56-sol`  
Created: 2026-08-09  
Target: PR #346 `L-34406`  
Scope: exact source/carry algebra only; `Delta_4 R_odd=Theta(n log n)` and the odd-Jordan deformation are not challenged

## 1. The source

Let

\[
 B_{\rm odd}(s)
 =\prod_{p\ {m odd}}(1-p^{-s})
 =\sum_n b_{\rm odd}(n)n^{-s},
\]

so

\[
 b_{\rm odd}(n)=\begin{cases}
 \mu(n),&n\text{ odd},\\
 0,&n\text{ even}.
 \end{cases}
\]

Since

\[
 {1\over\zeta(s)}=(1-2^{-s})B_{\rm odd}(s),
\]

one has exactly

\[
\boxed{
 \zeta(s)B_{\rm odd}(s)
 ={1\over1-2^{-s}}
 =\sum_{r\ge0}2^{-rs}.
}
\tag{R-34401.1}
\]

Equivalently,

\[
\boxed{
 \mathbf 1*b_{\rm odd}
 =\sum_{r\ge0}\delta_{2^r}.
}
\tag{R-34401.2}
\]

This identity is correct. The error in the current `L-34406` occurs in the next step.

## 2. Carry of `b_odd` is an ordinary-prefix defect, not the carry of the dyadic tower

For any arithmetic source `b`, if

\[
 e=\mathbf1*b,
\]

then the carry row is

\[
\begin{aligned}
\mathcal L_{n,j}(b)
&=\sum_db(d)
 \left(
 \left\lfloor{n\over d}\right\rfloor
 -\left\lfloor{j\over d}\right\rfloor
 -\left\lfloor{n-j\over d}\right\rfloor
 \right)\\
&=E(n)-E(j)-E(n-j),
\end{aligned}
\tag{R-34401.3}
\]

where

\[
 E(X)=\sum_{m\le X}e(m)
\]

is the **ordinary prefix** of `e`.

For (R-34401.2),

\[
\boxed{
 E_{\rm odd}(X)=1+\lfloor\log_2X\rfloor
 \qquad(X\ge1).
}
\tag{R-34401.4}
\]

Therefore, writing `k=n-j`,

\[
\boxed{
Y_{\rm odd}(n,j)
=\lfloor\log_2n\rfloor
 -\lfloor\log_2j\rfloor
 -\lfloor\log_2k\rfloor-1.
}
\tag{R-34401.5}
\]

The current `L-34406.7` instead replaces this by

\[
\sum_{r\ge1}\chi_{n,2^r}(j),
\]

which is the carry transform of the dyadic-tower coefficient sequence itself, not the carry transform of its Dirichlet inverse `b_odd`. That substitution is invalid.

## 3. Exact finite counterexample

At

\[
(n,j,k)=(8,4,4),
\]

(R-34401.4) gives

\[
Y_{\rm odd}(8,4)=4-3-3=-2.
\]

The same value follows directly from the source coefficients: among odd `q<=8`, the active columns are `q=5,7`, and

\[
b_{\rm odd}(5)+b_{\rm odd}(7)=-1-1=-2.
\]

By contrast, the formula currently asserted in `L-34406.7` gives only the `q=8` dyadic carry and returns `+1`.

Thus the asserted identity is false before any asymptotic or curvature argument enters.

## 4. Exact radix-four law

For every positive `X`,

\[
\lfloor\log_2(4X)\rfloor
=\lfloor\log_2X\rfloor+2.
\]

Apply this to all three arguments in (R-34401.5):

\[
\begin{aligned}
Y_{\rm odd}(4n,4j)
&=(\lfloor\log_2n\rfloor+2)
 -(\lfloor\log_2j\rfloor+2)\\
&\quad-(\lfloor\log_2k\rfloor+2)-1\\
&=Y_{\rm odd}(n,j)-2.
\end{aligned}
\]

Hence

\[
\boxed{
Y_{\rm odd}(4e)-Y_{\rm odd}(e)=-2
}
\tag{R-34401.6}
\]

for every nontrivial aligned integer row.

There is also a one-line convolution check. Put

\[
 b_{\rm rel}=(\varepsilon-\delta_4)*b_{\rm odd}.
\]

Then, with `z=2^{-s}`,

\[
\boxed{
 \mathbf1*b_{\rm rel}
 ={1-z^2\over1-z}
 =1+z,
}
\tag{R-34401.7}
\]

so

\[
\mathbf1*b_{\rm rel}=\varepsilon+\delta_2.
\]

Its ordinary prefix is identically `2` once the argument is at least two. Therefore on every row with parent and both children at least two,

\[
\mathcal L(b_{\rm rel})=2-2-2=-2,
\]

again proving (R-34401.6).

## 5. Corrected relative Jordan curvature

Retain the valid odd-Jordan scalar relative coordinate of `L-34406`:

\[
-\bigl(\log H_e^{\rm odd}\bigr)''(0)
=\Delta_4R_{\rm odd}(e).
\]

Retain also the relative source leg

\[
G_e^{\rm odd}(\tau)
=\mathcal L_{4e}
 \bigl((\varepsilon-\delta_4)*K_{{\rm odd},\tau}\bigr).
\]

Its jets are

\[
\boxed{
G_e^{\rm odd}(0)=-2,
}
\tag{R-34401.8}
\]

\[
\boxed{
(G_e^{\rm odd})'(0)
=I_{\rm odd}(e)
:=Q_{\rm odd}(4e)-Q_{\rm odd}(e),
}
\tag{R-34401.9}
\]

and

\[
\boxed{
(G_e^{\rm odd})''(0)
=T_{\rm odd}(4e)-T_{\rm odd}(e)
=:T_{\rm odd}^{\rm rel}(e).
}
\tag{R-34401.10}
\]

Consequently the corrected vector curvature is

\[
\boxed{
\mathfrak C(W_e^{\rm odd})
=\Delta_4R_{\rm odd}(e)
 +|I_{\rm odd}(e)|^2
 +2\operatorname{Re}T_{\rm odd}^{\rm rel}(e).
}
\tag{R-34401.11}
\]

in the Hermitian convention (for real rows, simply replace `Re T` by `T`).

The second-current term does **not** disappear algebraically.

## 6. What survives

This correction does not affect the following independent results:

1. the odd-prime Jordan deformation itself;
2. the all-order parameter-independent compact/parity synthesis of PR #345 `L-34405`;
3. the odd-prime reserve
   \[
   R_{\rm odd}=O^2-S_{\rm odd};
   \]
4. the critical-scale theorem
   \[
   \Delta_4R_{\rm odd}=\Theta_\eta(n\log n)
   \]
   on fixed balanced cones.

What is withdrawn is only the claimed exact cancellation

```text
relative bare charge = 0
-> cross-free curvature Delta_4 R_odd + I_odd^2.
```

The repaired next problem is to control the explicit term

\[
2\operatorname{Re}T_{\rm odd}^{\rm rel}(e)
\]

inside the same critical-scale ledger, or to choose a genuinely zero-bare relative source.

## 7. Proof boundary

Established exactly:

- the correct ordinary prefix of `1*b_odd`;
- the exact carry formula (R-34401.5);
- the finite counterexample `(8,4)`;
- the aligned law `Y_odd(4e)-Y_odd(e)=-2`;
- the equivalent two-tap relative divisor source;
- the corrected relative curvature (R-34401.11).

Classification:

```text
L-34406.7                         FALSE
L-34406.10 / relative bare=0      FALSE
L-34406.21 cross-free curvature   FALSE
odd Jordan deformation            unaffected
Delta_4 R_odd critical moat       unaffected
RH                                UNPROVEN
```

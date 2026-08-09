# L-34404 — The odd-prime Selberg–Kummer reserve has a positive critical-scale radix-four increment

Claim ID: `L-34404`  
Title: After removing the explicit dyadic inverse modes from the parity reserve, the remaining odd-prime reserve creates a deterministic `Theta_eta(n log n)` moat at every radix-four step on fixed balanced cones  
Status: **PROPOSED COMPLETE UNCONDITIONAL COFINAL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: PR #337 `L-32704`; elementary Stirling bounds, Legendre/Kummer, and dyadic valuation sums  
Scope: deterministic odd-prime generalized-factorial reserve; no RH-sensitive current domination or RH conclusion

## 1. Odd-prime reserve

For an integer `m>=1`, write

\[
\operatorname{odd}(m)={m\over2^{v_2(m)}},
\qquad
 g(m)=\log\operatorname{odd}(m).
\]

Put

\[
F(x)=\sum_{m\le x}g(m),
\qquad
G(x)=\sum_{m\le x}g(m)^2.
\tag{L-34404.1}
\]

For a split

\[
n=j+k
\]

define

\[
\boxed{
O(n,j)=F(n)-F(j)-F(k)
=\log\operatorname{odd}\binom nj
}
\tag{L-34404.2}
\]

and

\[
\boxed{
S_{\rm odd}(n,j)=G(n)-G(j)-G(k).
}
\tag{L-34404.3}
\]

PR #337 identifies these exactly as the odd-prime first and second generalized Selberg currents. Define

\[
\boxed{
R_{\rm odd}(n,j)=O(n,j)^2-S_{\rm odd}(n,j).
}
\tag{L-34404.4}
\]

The radix-four increment is

\[
\boxed{
\Delta_4R_{\rm odd}(n,j)
=R_{\rm odd}(4n,4j)-16R_{\rm odd}(n,j).
}
\tag{L-34404.5}

## 2. Elementary asymptotics for `F`

Legendre's binary digit identity gives

\[
\sum_{m\le x}v_2(m)=v_2(\lfloor x\rfloor !)
=\lfloor x\rfloor-s_2(\lfloor x\rfloor).
\]

Hence, at integer `x`,

\[
F(x)=\log(x!)-\bigl(x-s_2(x)\bigr)\log2.
\tag{L-34404.6}
\]

Stirling's elementary two-sided bounds and `s_2(x)=O(\log x)` yield

\[
\boxed{
F(x)=x\log x-(1+\log2)x+O(\log(2x)).
}
\tag{L-34404.7}

All implied constants below are absolute unless an `eta` subscript is displayed.

## 3. Elementary asymptotics for `G`

Expand

\[
g(m)^2
=(\log m)^2
-2(\log2)v_2(m)\log m
+(\log2)^2v_2(m)^2.
\tag{L-34404.8}
\]

The first sum satisfies, by integral comparison or one Euler summation,

\[
\sum_{m\le x}(\log m)^2
=x\bigl((\log x)^2-2\log x+2\bigr)
+O(\log^2(2x)).
\tag{L-34404.9}

For the mixed valuation sum, use

\[
v_2(m)=\sum_{r\ge1}\mathbf1_{2^r\mid m}.
\]

Then

\[
\begin{aligned}
\sum_{m\le x}v_2(m)\log m
&=\sum_{r\le\log_2x}\sum_{a\le x/2^r}\log(2^ra)\\
&=x(\log x-1)+O(\log^2(2x)).
\end{aligned}
\tag{L-34404.10}

The cancellation of the `r log 2` term against the logarithm of `x/2^r` is exact in the main term; the floor and factorial endpoint errors sum to `O(log^2 x)`.

Likewise

\[
v_2(m)^2
=\sum_{r=1}^{v_2(m)}(2r-1),
\]

so

\[
\begin{aligned}
\sum_{m\le x}v_2(m)^2
&=\sum_{r\le\log_2x}(2r-1)\left\lfloor{x\over2^r}\right\rfloor\\
&=3x+O(\log^2(2x)),
\end{aligned}
\tag{L-34404.11}

because

\[
\sum_{r\ge1}{2r-1\over2^r}=3.
\]

Combining (L-34404.8)--(L-34404.11),

\[
\boxed{
G(x)=x(\log x)^2-2(1+\log2)x\log x+C_2x
+O(\log^2(2x)),
}
\tag{L-34404.12}

where the explicit constant

\[
C_2=2+2\log2+3(\log2)^2
\]

will not be needed.

## 4. Uniform balanced-cone expansions

Fix

\[
0<\eta<1/2,
\qquad
\eta n\le j\le(1-\eta)n,
\]

and put

\[
\alpha={j\over n},
\qquad \beta=1-\alpha,
\]

\[
H(\alpha)=-\alpha\log\alpha-\beta\log\beta.
\]

On the compact interval `[eta,1-eta]`,

\[
h_\eta:=\min H(\alpha)>0.
\tag{L-34404.13}

Equations (L-34404.7) and (L-34404.12) give uniformly

\[
\boxed{
O(n,j)=nH(\alpha)+O_\eta(\log(2n)),
}
\tag{L-34404.14}

and

\[
\boxed{
S_{\rm odd}(n,j)
=2nH(\alpha)\log n+nK(\alpha)
+O_\eta(\log^2(2n)),
}
\tag{L-34404.15}

where `K` is one continuous bounded function on `[eta,1-eta]`. Its exact expression is obtained by expanding the `x log^2 x` and `x log x` terms; only boundedness is used.

Therefore

\[
\begin{aligned}
&S_{\rm odd}(4n,4j)-16S_{\rm odd}(n,j)\\
&=-24nH(\alpha)\log n
+n\left[8H(\alpha)\log4-12K(\alpha)\right]
+O_\eta(\log^2(2n)).
\end{aligned}
\tag{L-34404.16}

Since `H>=h_eta>0` and `K` is bounded, there is `N_eta` such that

\[
\boxed{
S_{\rm odd}(4n,4j)-16S_{\rm odd}(n,j)
\le -12h_\eta n\log n
}
\tag{L-34404.17}

for every `n>=N_eta` in the fixed balanced cone.

This negative forcing increment is the principal deterministic source of the new moat.

## 5. The odd Kummer current does not decrease under scale four cofinally

Define

\[
E_{\rm odd}(n,j)=O(4n,4j)-4O(n,j).
\tag{L-34404.18}

Since

\[
O(n,j)=\log\binom nj-v_2\!\binom nj\log2,
\]

one has

\[
\begin{aligned}
E_{\rm odd}
={}&\log{\binom{4n}{4j}\over\binom nj^4}\\
&-\left[v_2\!\binom{4n}{4j}-4v_2\!\binom nj\right]\log2.
\end{aligned}
\tag{L-34404.19}

Uniform Stirling bounds on the fixed balanced cone give

\[
\boxed{
\log{\binom{4n}{4j}\over\binom nj^4}
\ge {3\over2}\log n-C_\eta.
}
\tag{L-34404.20}

Kummer's binary-carry interpretation gives

\[
v_2\!\binom{4n}{4j}
\le \log_2(4n)+1.
\]

The term `4 v_2 binom(n,j)` in (L-34404.19) has the favorable sign, so

\[
\boxed{
E_{\rm odd}(n,j)
\ge {1\over2}\log n-C_\eta'
}
\tag{L-34404.21}

and hence

\[
\boxed{E_{\rm odd}(n,j)\ge0}
\tag{L-34404.22}

cofinally and uniformly on the fixed balanced cone.

## 6. Positive critical-scale reserve increment

Using

\[
O(4n,4j)=4O(n,j)+E_{\rm odd},
\]

expand (L-34404.5):

\[
\boxed{
\begin{aligned}
\Delta_4R_{\rm odd}
={}&E_{\rm odd}\bigl(8O+E_{\rm odd}\bigr)\\
&-\left[S_{\rm odd}(4n,4j)-16S_{\rm odd}(n,j)\right].
\end{aligned}}
\tag{L-34404.23}

Cofinally, `O>=0` and `E_odd>=0`, so the first line is nonnegative. Equation (L-34404.17) therefore gives

\[
\boxed{
\Delta_4R_{\rm odd}(n,j)
\ge12h_\eta n\log n.
}
\tag{L-34404.24}

The same asymptotic formulas show

\[
O=O_\eta(n),
\qquad
E_{\rm odd}=O_\eta(\log n),
\]

and

\[
S_{\rm odd}(4n,4j)-16S_{\rm odd}(n,j)=O_\eta(n\log n).
\]

Hence also

\[
\boxed{
\Delta_4R_{\rm odd}(n,j)=O_\eta(n\log n).
}
\tag{L-34404.25}

Combining (L-34404.24)--(L-34404.25),

\[
\boxed{
\Delta_4R_{\rm odd}(n,j)
=\Theta_\eta(n\log n)
}
\tag{L-34404.26}

uniformly on every fixed balanced cone.

## 7. Why this matters for the live parity/Q=4 route

The full parity reserve contains explicit dyadic inverse modes whose raw radix-four increment can have either sign and can be much larger than the RH-critical scale. They are therefore the wrong scale variable.

The odd-prime reserve removes those explicit local modes and leaves a deterministic source-matched curvature whose newly created reserve is exactly `Theta(n log n)`, the same scale as PR #342's Q=4 reserve increment.

Thus the parity route now has a **scale-matched deterministic current moat** which does not depend on PNT, zero-free regions, or RH.

What is not proved here is the RH-sensitive upper estimate

\[
|I_\circ(n,j)|^2
\ll_\eta \Delta_4R_{\rm odd}(n,j),
\]

or its independent-frequency block analogue. That remains conclusion-producing.

## 8. Proof boundary

Closed here, subject to review:

1. elementary asymptotics for the odd logarithmic factorial and its square;
2. uniform balanced-cone expansions for `O` and `S_odd`;
3. strict negative radix-four forcing increment;
4. cofinal nonnegativity of the odd Kummer-current increment;
5. the uniform two-sided critical-scale theorem
   `Delta_4 R_odd = Theta_eta(n log n)`.

Still open:

1. domination of the compact RH-sensitive innovation by this reserve increment;
2. the final coefficient-one physical recurrence;
3. RH.

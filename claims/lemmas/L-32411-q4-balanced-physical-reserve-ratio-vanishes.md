# L-32411 — The Q=4 balanced physical/reserve ratio tends to zero

Claim ID: `L-32411`  
Title: Killing the zeta main pole makes the correctly typed `Q=4` physical current `o(n)` uniformly on every fixed balanced cone, while the complete Selberg–Kummer reserve remains quadratic  
Status: **PROPOSED COMPLETE UNCONDITIONAL ASYMPTOTIC THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-11  
Dependencies: `L-32404`, corrected `L-32407`, `L-32405`; the classical prime number theorem and an elementary Chebyshev bound  
Scope: fixed integer carry rows and their balanced physical/reserve ratio; no reflected block recurrence or RH conclusion

## 1. The correctly typed physical current

Retain the `Q=4` Euler--Blaschke system

\[
E_4(s)=\frac{1-4^{1-s}}{1-4^{-s}}
      =1-3\sum_{r\ge1}4^{-rs},
\]

and its generalized-prime series

\[
L_4(s)=-\frac{A_4'}{A_4}(s).
\]

The centered-interval physical coefficient sequence is the coefficient sequence of

\[
E_4(s)L_4(s)
=-E_4(s)\frac{\zeta'}{\zeta}(s)+E_4'(s).
\tag{L-32411.1}
\]

Equivalently, with `e_4(1)=1`, `e_4(4^r)=-3` for `r>=1`,

\[
c_4=e_4*\Lambda_4.
\]

Put

\[
G_4(x)=\sum_{n\le x}c_4(n),
\qquad x\ge1.
\tag{L-32411.2}
\]

For an integer parent `n=j+k`, the correctly typed physical carry row of corrected `L-32407` is

\[
\boxed{
Q_4^{\rm phys}(n,j)=G_4(n)-G_4(j)-G_4(k).
}
\tag{L-32411.3}
\]

No additional floor transform is present.

## 2. Exact summatory identity

Since

\[
E_4'(s)=3\log4\sum_{r\ge1}r4^{-rs},
\]

finite coefficient summation gives, with

\[
R(x)=\lfloor\log_4x\rfloor,
\]

the exact formula

\[
\boxed{
G_4(x)
=\psi(x)-3\sum_{r=1}^{R(x)}\psi(x/4^r)
 +3\log4\sum_{r=1}^{R(x)}r.
}
\tag{L-32411.4}
\]

Here `psi(y)=0` for `y<2`, so the displayed finite upper limit is harmless at the bottom.

Write

\[
\Delta(x)=\psi(x)-x.
\]

The geometric main terms telescope exactly:

\[
x-3\sum_{r=1}^{R}x4^{-r}=x4^{-R}.
\]

Therefore

\[
\boxed{
G_4(x)
=x4^{-R(x)}
 +\Delta(x)-3\sum_{r=1}^{R(x)}\Delta(x/4^r)
 +\frac32R(x)(R(x)+1)\log4.
}
\tag{L-32411.5}
\]

This is the physical meaning of the zero of `E_4` at `s=1`: the complete linear prime density cancels before an estimate is taken.

## 3. Unconditional `o(x)` bound

The prime number theorem gives

\[
\Delta(y)=o(y).
\tag{L-32411.6}
\]

We prove

\[
\boxed{G_4(x)=o(x).}
\tag{L-32411.7}
\]

Fix an integer `M>=1`. Split the error sum in (L-32411.5) at `M`.

For each fixed `1<=r<=M`,

\[
\Delta(x/4^r)=o(x).
\]

For the remaining terms use the elementary Chebyshev estimate

\[
|\Delta(y)|\le C_0y
\qquad(y\ge1)
\]

with one absolute constant. Hence

\[
\sum_{r>M}^{R(x)}|\Delta(x/4^r)|
\le C_0x\sum_{r>M}4^{-r}
\le C_1x4^{-M}.
\]

The first term in (L-32411.5) is bounded by four, and the last is `O(log^2x)`. Thus

\[
\limsup_{x\to\infty}\frac{|G_4(x)|}{x}
\le C_1 4^{-M}.
\]

Letting `M` tend to infinity proves (L-32411.7).

The same argument gives the useful uniform tail form

\[
\boxed{
\varepsilon(Y):=\sup_{x\ge Y}\frac{|G_4(x)|}{x}
\longrightarrow0.
}
\tag{L-32411.8}
\]

## 4. Uniform balanced physical decay

Fix

\[
0<\eta\le\frac12
\]

and suppose

\[
\eta n\le j,k\le(1-\eta)n,
\qquad j+k=n.
\]

By (L-32411.3) and (L-32411.8),

\[
\begin{aligned}
|Q_4^{\rm phys}(n,j)|
&\le |G_4(n)|+|G_4(j)|+|G_4(k)|\\
&\le \varepsilon(\eta n)(n+j+k)\\
&=2\varepsilon(\eta n)n.
\end{aligned}
\tag{L-32411.9}
\]

Consequently

\[
\boxed{
\sup_{\eta n\le j\le(1-\eta)n}
\frac{|Q_4^{\rm phys}(n,j)|}{n}
\longrightarrow0.
}
\tag{L-32411.10}
\]

## 5. Comparison with the complete Selberg--Kummer reserve

Let

\[
\mathcal R_4(n,j)=P_4(n,j)^2-S_4(n,j)
\]

be the complete source-matched reserve of `L-32405`.

For all sufficiently large quarter-balanced rows, that theorem gives

\[
\mathcal R_4(n,j)\ge\frac1{20}P_4(n,j)^2.
\tag{L-32411.11}
\]

Because `Lambda_4>=Lambda`, ordinary Kummer positivity gives on every fixed balanced cone

\[
P_4(n,j)\ge\log\binom nj\ge\eta n\log2.
\tag{L-32411.12}
\]

Combining (L-32411.9)--(L-32411.12),

\[
\frac{|Q_4^{\rm phys}(n,j)|^2}{\mathcal R_4(n,j)}
\le
\frac{80\,\varepsilon(\eta n)^2}{\eta^2\log^22}.
\]

Therefore

\[
\boxed{
\sup_{\eta n\le j\le(1-\eta)n}
\frac{|Q_4^{\rm phys}(n,j)|^2}{\mathcal R_4(n,j)}
\longrightarrow0.
}
\tag{L-32411.13}
\]

Equivalently, for every fixed `eta` and every `kappa>0`, all sufficiently large balanced rows satisfy

\[
\boxed{
|Q_4^{\rm phys}(n,j)|^2
\le\kappa\,\mathcal R_4(n,j).
}
\tag{L-32411.14}
\]

This strengthens the absolute constant in corrected `L-32407` to a cofinally vanishing constant.

## 6. What this theorem does and does not close

The result is unconditional and uses only the established prime number theorem. It proves that, once the deterministic density is removed at the source level, the physical current occupies an asymptotically negligible fraction of the available balanced Selberg reserve.

It does **not** prove a subexponential physical energy estimate. The reserve itself is macroscopically large, and a valid global argument must still show that the complete independent-frequency reflected identity supplies that reserve once, without double spending, while routing only the declared neutral scattering state to lower scale.

In particular, the invalid inference

```text
physical/reserve ratio -> 0
therefore physical energy is subexponential
```

is expressly rejected.

## 7. Proof boundary

Closed here:

1. the exact summatory formula for the correctly typed physical current;
2. exact cancellation of the linear prime density;
3. the unconditional estimate `G_4(x)=o(x)`;
4. uniform balanced `o(n)` physical rows;
5. the cofinally vanishing physical/reserve ratio.

Open:

1. complete reflected reserve accounting;
2. the coefficient-one lower-scale scattering recurrence;
3. RH.

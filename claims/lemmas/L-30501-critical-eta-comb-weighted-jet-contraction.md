# L-30501 — Critical eta comb contracts a weighted jet norm

Claim ID: `L-30501`  
Title: At the true square-root normalization, the complete eta dilation comb has a strict weighted-jet contraction once adjacent translations are charged by one derivative  
Status: **PROPOSED COMPLETE ANALYTIC THEOREM**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: elementary translation estimates and alternating-series bounds  
Scope: the complete causal continuum dilation comb; finite shifted sampling is treated separately

## 1. The critical logarithmic comb

At the square-root normalization relevant to Cycle Debt, define the paired signed measure

\[
\boxed{
\beta
=\sum_{k\ge1}
\left[
(2k)^{-1/2}\delta_{\log(2k)}
-(2k+1)^{-1/2}\delta_{\log(2k+1)}
\right].
}
\tag{L-30501.1}
\]

Its atoms do not have finite unsigned mass. Pair the atoms before acting on a function:

\[
\beta=\mu+\nu,
\tag{L-30501.2}
\]

where

\[
\mu
=\sum_{k\ge1}
\left[(2k)^{-1/2}-(2k+1)^{-1/2}\right]
\delta_{\log(2k)}
\tag{L-30501.3}
\]

is positive, and

\[
\nu
=\sum_{k\ge1}(2k+1)^{-1/2}
\left[
\delta_{\log(2k)}-\delta_{\log(2k+1)}
\right]
\tag{L-30501.4}
\]

is an adjacent logarithmic transport.

The positive mass is

\[
\boxed{
\rho=\mu(\mathbb R)=1-\eta(1/2).
}
\tag{L-30501.5}
\]

The transport cost is

\[
\boxed{
c
=\sum_{k\ge1}(2k+1)^{-1/2}
\log\frac{2k+1}{2k}.
}
\tag{L-30501.6}
\]

Both quantities are finite.

## 2. Exact one-derivative estimate

Let `F` be absolutely continuous with `F,F' in L^1(R)`. Translation invariance and

\[
\|F(\cdot-a)-F(\cdot-b)\|_1
\le |a-b|\,\|F'\|_1
\tag{L-30501.7}
\]

give

\[
\boxed{
\|\beta*F\|_1
\le \rho\|F\|_1+c\|F'\|_1.
}
\tag{L-30501.8}
\]

The convolution is defined by the paired decomposition (L-30501.2), not by the divergent unsigned atomic sum.

The same estimate applies after differentiation. For every `m>=0` with `F^(m),F^(m+1) in L^1`,

\[
\boxed{
\|D^m(\beta*F)\|_1
\le
\rho\|F^{(m)}\|_1
+c\|F^{(m+1)}\|_1.
}
\tag{L-30501.9}
\]

## 3. The weighted jet norm

For an integer `M>=0`, define

\[
\boxed{
\mathcal J_M(F)
=\sum_{m=0}^{M}2^m\|F^{(m)}\|_1.
}
\tag{L-30501.10}
\]

Summing (L-30501.9) with weights `2^m` gives

\[
\boxed{
\mathcal J_M(\beta*F)
\le
\theta\,\mathcal J_M(F)
+c\,2^M\|F^{(M+1)}\|_1,
}
\tag{L-30501.11}
\]

where

\[
\boxed{
\theta=\rho+\frac c2.
}
\tag{L-30501.12}
\]

Thus one derivative is exported at the top of a finite jet bank. If

\[
\mathcal J_\infty(F)=\sum_{m\ge0}2^m\|F^{(m)}\|_1<\infty,
\]

then monotone convergence gives the strict homogeneous estimate

\[
\boxed{
\mathcal J_\infty(\beta*F)
\le\theta\,\mathcal J_\infty(F).
}
\tag{L-30501.13}
\]

## 4. Elementary proof that `theta<1`

The eta lower bound from `R-30501` gives

\[
\eta(1/2)
>\frac54-\frac1{\sqrt2}.
\tag{L-30501.14}
\]

Hence

\[
\rho
< -\frac14+\frac1{\sqrt2}.
\tag{L-30501.15}
\]

For the transport cost, `log(1+x)<x` gives

\[
\begin{aligned}
c
&<\sum_{k\ge1}\frac1{2k\sqrt{2k+1}}\\
&<2^{-3/2}\zeta(3/2).
\end{aligned}
\tag{L-30501.16}
\]

Using

\[
\zeta(3/2)
<1+2^{-3/2}+\int_2^\infty x^{-3/2}\,dx
=1+\frac1{2\sqrt2}+\sqrt2,
\]

we obtain

\[
\boxed{
c<\frac58+\frac1{2\sqrt2}<1.}
\tag{L-30501.17}
\]

Combining (L-30501.15) and (L-30501.17),

\[
\boxed{
\theta
<\frac1{16}+\frac5{4\sqrt2}<1.
}
\tag{L-30501.18}
\]

The final inequality is equivalent to `2sqrt(2)<3`.

This is a completely explicit strict reserve at the **correct critical normalization**. It does not use a zeta-zero hypothesis or a numerical spectral radius.

## 5. Why the derivative weight is load bearing

The unweighted bounded-variation estimate would use `rho+c`. In fact `rho+c>1`; therefore a first-derivative norm with equal weights does not contract.

The factor `2^m` in (L-30501.10) values one derivative sufficiently highly that an adjacent logarithmic displacement costs `c/2` rather than `c`. This is the minimal structural repair suggested by the exact factor-two geometry.

The theorem is cancellation preserving:

```text
positive residual mass       charged by rho;
adjacent eta dipoles         charged by one derivative;
no termwise atomic variation of beta is taken.
```

## 6. Relation to the finite central cascade

For a normalized critical profile

\[
G(t)=e^{-t/2}F(e^{-t}),
\]

the unshifted central dilation operator is convolution by `beta`. Equation (L-30501.11) therefore supplies a strict continuum reserve with the endpoint distributions retained through the exported derivative channel.

A finite proof must keep the actual shifted argument `2kq-1` and the complete endpoint cancellation. `R-30501` shows that splitting off the cutoff tail and converting it to an atomic divisor source is invalid at polylogarithmic scale.

The correct remaining finite target is consequently:

```text
complete finite shifted operator
-> cancellation-preserving weighted jet state
-> direct Cycle-Debt comparison,
```

not

```text
analytic continuation + separately normed cutoff source.
```

## 7. Proof boundary

Closed exactly:

1. paired critical eta-comb decomposition;
2. the one-derivative translation estimate;
3. finite weighted-jet recurrence;
4. strict homogeneous factor `theta<1`;
5. the correct critical normalization and cancellation rule.

Not asserted here:

1. that the finite shifted sampling operator obeys the same homogeneous estimate without an endpoint term;
2. a complete DCCS proof;
3. RH.
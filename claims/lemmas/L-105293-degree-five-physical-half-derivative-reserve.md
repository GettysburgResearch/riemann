# L-105293 — Degree-five physical half-derivative reserve

Claim ID: `L-105293`  
Status: **PROVED EXACT RATIONAL / FROZEN MODEL THEOREM**  
Created: 2026-08-24  
Depends on: `L-105250--L-105253`, `L-105282`; PR #726 `L-105520`; Conrey's pinned fifth-derivative proportion  
RH status: **not assumed**

## 1. Degree-five square-root polynomial

Let

\[
P_5(x)=1-\frac x2-\frac{x^2}{8}-\frac{x^3}{16}
       -\frac{5x^4}{128}-\frac{7x^5}{256}.
\]

Then

\[
\frac{P_5(x)^2}{1-x}
 =1+\sum_{m\ge6}q_mx^m,
\qquad q_m\ge0,
\]

and exact multiplication gives

\[
q_6=\frac{21}{512},\quad
q_7=\frac{27}{512},\quad
q_8=\frac{945}{16384},\quad
q_9=\frac{245}{4096},
\]

with the constant tail

\[
\boxed{q_m=\frac{3969}{65536}\qquad(m\ge10).}
\tag{L-105293.1}
\]

The source degrees one through five vanish exactly.

## 2. Corrected physical energy at α=2

At full physical scale, the frozen prime-simplex energy is

\[
\mathcal D_5(2)
 =\sum_{m\ge6}q_m^2\frac{m!}{(2m)!}4^m.
\]

The first four terms are

\[
\frac7{675840},\qquad
\frac{27}{10250240},\qquad
\frac{63}{149946368},\qquad
\frac{343}{6452379648}.
\]

The \(m=10\) term is

\[
\frac{27783}{4843267686400}.
\]

For \(m\ge10\), the ratio of successive constant-tail summands is

\[
\frac{4^{m+1}(m+1)!/(2m+2)!}
     {4^m m!/(2m)!}
 =\frac2{2m+1}\le\frac2{21}.
\]

Therefore

\[
\boxed{
\mathcal D_5(2)
 \le
 \frac{702881150201}{52176522785587200}
 <\frac1{74000}.
}
\tag{L-105293.2}
\]

By `L-105282`, allowing both analytic orientations costs at most
\(2\alpha\mathcal D_5(\alpha)\). Hence, uniformly for every fixed
\(\alpha\le2\),

\[
\boxed{
\mathcal E_{1/2}^{\rm two\text{-}sided}(5)
 \le4\mathcal D_5(2)+o(1)
 <\frac1{18500}+o(1).
}
\tag{L-105293.3}
\]

## 3. Five-rung budget

Using the degree-five bank independently on the five adjacent derivative
levels costs at most

\[
\boxed{
5\cdot\frac1{18500}=\frac1{3700}
}
\tag{L-105293.4}
\]

of the normalized zero-count scale, before coherent owner assembly and
actual-Xi transfer.

The pinned unconditional Conrey value is

\[
\liminf \frac{R_5(T,2T)}{N_5(T,2T)}
 >\frac{997}{1000}.
\]

Thus the exact reserve above a ninety-percent target is

\[
\frac{997}{1000}-\frac9{10}=\frac{97}{1000}.
\]

After paying the complete five-rung frozen source budget, the remaining
allowance is

\[
\boxed{
\frac{97}{1000}-\frac1{3700}
 =\frac{3579}{37000}
 =0.0967297297\ldots .
}
\tag{L-105293.5}
\]

This is larger than the previous three-rung allowance and is the preferred
quantitative target for the all-pass programme.

## Scope

The calculation is exact and unconditional at the frozen physical source
scope. It does not transfer the source to the actual Xi all-pass boundary and
does not estimate coherent owner-conductor assembly. Those tasks are isolated
in `T-105290`.

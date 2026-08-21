# L-24523 — Nilpotent central-Neumann carry saturation

Claim ID: `L-24523`  
Status: **PROPOSED COMPLETE — exact finite elementary algebra**  
Scope: explicit signed saturation of every integer carry column  
Issue: #245  
Date: 2026-08-08

## 1. Central carry row

For integers `n>=2` and `q>=2`, put

\[
 j_n=\lfloor n/2\rfloor,
 \qquad
 \chi_n^{\rm c}(q)
 =\left\lfloor{n\over q}\right\rfloor
  -\left\lfloor{j_n\over q}\right\rfloor
  -\left\lfloor{n-j_n\over q}\right\rfloor.
\]

Write

\[
 n=2kq+r,
 \qquad 0\le r<2q.
\]

Then

\[
\boxed{
 \chi_n^{\rm c}(q)
 =\mathbf 1_{\{q\le r\le2q-2\}}.
}
\tag{L-24523.1}
\]

Proof. Since

\[
\left\lfloor{n\over q}\right\rfloor
=2k+\mathbf1_{r\ge q},
\]

while `floor(r/2)<q` and

\[
\left\lceil{r\over2}\right\rceil\ge q
\Longleftrightarrow r=2q-1,
\]

the two child floors contribute

\[
2k+\mathbf1_{r=2q-1}.
\]
Subtracting gives (L-24523.1).

Thus the central carry row is an exact square wave: in every complete period of length `2q`, it is one on the `q-1` consecutive residues

\[
q,q+1,\ldots,2q-2.
\]

## 2. One-pass operator

Fix an endpoint `X>=3`. Let `f(2),...,f(X)` be any real sequence and extend it by zero for `m>X`. Put

\[
 a_f(n)=f(n)-f(n+1).
\tag{L-24523.2}
\]

Define the central one-pass load

\[
(P_Xf)(q)=\sum_{n=q}^{X}a_f(n)\chi_n^{\rm c}(q).
\tag{L-24523.3}
\]

Summing (L-24523.2) over each square-wave interval from (L-24523.1) gives

\[
\boxed{
(P_Xf)(q)
=\sum_{k\ge0}
 \left[
 f((2k+1)q)-f((2k+2)q-1)
 \right],
}
\tag{L-24523.4}
\]

where terms with both arguments above `X` vanish.

Define the residual operator

\[
T_X=I-P_X.
\]

The first term in (L-24523.4) is `f(q)-f(2q-1)`. Hence

\[
\boxed{
(T_Xf)(q)
=\sum_{k\ge0}
\left[
 f((2k+2)q-1)-f((2k+3)q)
\right].
}
\tag{L-24523.5}
\]

This identity is exact and contains every endpoint shift.

## 3. Factor-two support descent

If `f(m)=0` for `m>Y`, then the first possible argument on the right of (L-24523.5) is `2q-1`. Therefore

\[
\boxed{
\operatorname{supp}(T_Xf)
\subseteq
\left\{2,\ldots,\left\lfloor{Y+1\over2}\right\rfloor\right\}.
}
\tag{L-24523.6}
\]

Put

\[
Y_0=X,
\qquad
Y_{r+1}=\left\lfloor{Y_r+1\over2}\right\rfloor.
\]

After `O(log X)` iterations one has `Y_r<2`. Consequently

\[
\boxed{T_X^L=0}
\tag{L-24523.7}
\]

on sequences supported in `2,...,X`, for every

\[
L\ge2+\lceil\log_2X\rceil.
\]

Thus `I-T_X=P_X` has the finite Neumann inverse

\[
\boxed{
P_X^{-1}=I+T_X+\cdots+T_X^{L-1}.
}
\tag{L-24523.8}
\]

No convergence theorem is involved: the series terminates.

## 4. Explicit central signed saturation

Take the critical target

\[
w_X(q)=q^{-1/2}\log(X/q),
\qquad 2\le q\le X,
\]

with `w_X(m)=0` for `m>X`. Define

\[
f_0=w_X,
\qquad
f_{r+1}=T_Xf_r,
\tag{L-24523.9}
\]

and

\[
A_X(n)=\sum_{r=0}^{L-1}
\bigl[f_r(n)-f_r(n+1)\bigr].
\tag{L-24523.10}
\]

Then, using (L-24523.3),

\[
\begin{aligned}
\sum_{n=q}^{X}A_X(n)\chi_n^{\rm c}(q)
&=\sum_{r=0}^{L-1}(P_Xf_r)(q)\\
&=\sum_{r=0}^{L-1}[f_r(q)-f_{r+1}(q)]\\
&=w_X(q)-f_L(q).
\end{aligned}
\]

By nilpotence, `f_L=0`. Therefore

\[
\boxed{
\sum_{n=q}^{X}A_X(n)\chi_n^{\rm c}(q)
=w_X(q)
\qquad(2\le q\le X).
}
\tag{L-24523.11}
\]

This is an explicit signed saturation of **every integer carry column**, using only central binomial splits. It requires no LP, no Möbius inversion, no prime input, and no limiting argument.

## 5. Exact prime and all-integer ledgers

Put

\[
\ell_n=\log\binom n{\lfloor n/2\rfloor},
\qquad
c_n=\sum_{q=2}^{n}\chi_n^{\rm c}(q).
\tag{L-24523.12}
\]

Legendre's formula and (L-24523.11) give

\[
\boxed{
\mathcal P(X)
:=\sum_{p^a\le X}{\Lambda(p^a)\over\sqrt{p^a}}
 \log{X\over p^a}
=\sum_{n=2}^{X}A_X(n)\ell_n.
}
\tag{L-24523.13}
\]

Summing (L-24523.11) over all integer columns gives

\[
\boxed{
\mathcal C(X):=\sum_{q=2}^{X}q^{-1/2}\log(X/q)
=\sum_{n=2}^{X}A_X(n)c_n.
}
\tag{L-24523.14}
\]

Hence

\[
\boxed{
\mathcal P(X)-\mathcal C(X)
=\sum_{n=2}^{X}A_X(n)(\ell_n-c_n).
}
\tag{L-24523.15}
\]

Elementary Dirichlet hyperbola and Stirling estimates give uniformly

\[
\boxed{|\ell_n-c_n|\ll\sqrt n.}
\tag{L-24523.16}
\]

Indeed `c_n=D(n)-D(floor(n/2))-D(ceil(n/2))`, where

\[
D(n)=\sum_{q\le n}\lfloor n/q\rfloor
=n\log n+(2\gamma-1)n+O(\sqrt n),
\]

and the linear terms cancel against the corresponding Stirling expansion.

Also elementary integral comparison gives

\[
\boxed{\mathcal C(X)=4\sqrt X+O(\log X).}
\tag{L-24523.17}
\]

## 6. Relation to the signed constraint dipole

The parabolic-seed route of `L-25301` begins with two macroscopic positive and negative defect ledgers and seeks a signed adjacent transport between them. The present construction performs the same cancellation in a different order:

```text
critical all-integer target
-> central one-pass square wave
-> exact residual T_X
-> factor-two support descent
-> finite Neumann sum
-> signed central coefficients A_X.
```

Every stage sends its unfilled target to at most half scale. Thus the factor-two descent is an identity rather than a proposed geometric heuristic.

The price is that `A_X` need not be nonnegative. Controlling only that negative part is the new proof-facing theorem isolated in `L-24524`.

## 7. Pole/firewall

The finite nilpotence must not be confused with a phase-blind analytic contraction. In the scale-invariant continuum model, the central carry square wave has Mellin multiplier

\[
\eta(s)=(1-2^{1-s})\zeta(s).
\]

Hence the formal residual multiplier is `1-eta(s)`. At a nontrivial zero of zeta this equals one, not a strict contraction. Equivalently, the inverse multiplier contains

\[
{1\over(1-2^{1-s})\zeta(s)}.
\]

Thus any cofinal variation estimate for the finite Neumann coefficients must retain the coherent arithmetic boundary information. The exact factor-two support descent does not by itself erase the reciprocal-zeta channel.

## Proof boundary

Proved in this file:

- the exact central carry square wave;
- the one-pass and residual formulas;
- factor-two support descent and finite nilpotence;
- the terminating Neumann inverse;
- exact signed saturation of every integer carry column;
- the exact prime/all-integer ledgers;
- the elementary `O(sqrt(n))` local profit bound.

Not proved here:

- subpower negative variation of the Neumann coefficients;
- a nonnegative near-saturating certificate;
- RH.

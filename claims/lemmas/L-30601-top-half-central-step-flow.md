# L-30601 — Exact top-half central step flow

Claim ID: `L-30601`  
Title: An arbitrary carry profile on one dyadic top band is realized exactly by central steps, with negative debt controlled by weighted one-sided variation and all leakage routed below half scale  
Status: **PROPOSED COMPLETE EXACT FINITE LEMMA**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Issue: #306  
Dependencies: atomized carry identity; PR #272 capacity metric  
Scope: a source-complete replacement for the top band of the invalid atomic lift; no all-scale recurrence or RH conclusion

## 1. Central rows are steps on the top half

Fix an integer `H>=1`. For

\[
H<n\le2H
\]

let

\[
C_n=[n,\lfloor n/2\rfloor]
\]

be the central split. For every carry column

\[
H<q\le2H,
\]

both children of `C_n` are strictly below `q`. Consequently

\[
\boxed{
\chi_{C_n}(q)=\mathbf1_{q\le n}.
}
\tag{L-30601.1}
\]

Thus the central rows form the standard upper-triangular step basis on one complete dyadic band.

## 2. Exact realization of an arbitrary band profile

Let

\[
g(H+1),\ldots,g(2H)
\]

be arbitrary real numbers and set `g(2H+1)=0`. Define

\[
\boxed{
c_n=g(n)-g(n+1),
\qquad H<n\le2H,
}
\tag{L-30601.2}
\]

and the signed flow

\[
\boxed{
d_g=\sum_{n=H+1}^{2H}c_nC_n.}
\tag{L-30601.3}
\]

For every `H<q<=2H`, equation (L-30601.1) gives

\[
\begin{aligned}
L_q(d_g)
&=\sum_{n=q}^{2H}[g(n)-g(n+1)]\\
&=\boxed{g(q)}.
\end{aligned}
\tag{L-30601.4}
\]

This is an exact source-to-flow map. It retains the physical integer column `q`; no quotient or arithmetic fiber is erased.

## 3. Negative-capacity bound

Let

\[
\omega_n=\sum_{q=2}^{n}\frac{\chi_{C_n}(q)}{\sqrt q}.
\]

The elementary estimate

\[
\omega_n\le2\sqrt n
\]

gives

\[
\boxed{
\mathcal N_\omega(d_g)
\le
2\sum_{n=H+1}^{2H}
\sqrt n\,[g(n+1)-g(n)]_+.
}
\tag{L-30601.5}
\]

Therefore the cost is governed by one-sided variation of the **recombined band profile**, not by the atomic divisor-source norm.

## 4. Smooth negative profiles cost only their endpoint size

Suppose

\[
g(n)=-b(n),
\]

where `b(n)>=0` is nonincreasing on the band. Put

\[
B_H=\sup_{H<n\le2H}\sqrt n\,b(n).
\tag{L-30601.6}
\]

All coefficients in (L-30601.2) are nonpositive. With `b(2H+1)=0`, summation by parts gives

\[
\begin{aligned}
\sum_{n=H+1}^{2H}
\sqrt n\,[b(n)-b(n+1)]
={}&\sqrt{H+1}\,b(H+1)\\
&+\sum_{n=H+2}^{2H}
(\sqrt n-\sqrt{n-1})b(n).
\end{aligned}
\tag{L-30601.7}
\]

Using

\[
\sqrt n-\sqrt{n-1}
\le\frac1{2\sqrt{n-1}}
\]

and `b(n)<=B_H/sqrt(n)`, the second line is at most

\[
\frac{B_H}{2}
\sum_{n=H+2}^{2H}\frac1{\sqrt{n(n-1)}}
< B_H.
\]

Hence

\[
\boxed{
\mathcal N_\omega(d_g)<4B_H.
}
\tag{L-30601.8}
\]

In particular, a top-band profile of size

\[
|g(n)|\le C\,n^{-1/2}(1+\log X)^A
\]

and monotone sign costs only `O(C log^A X)`, even though its square-root atomic divisor-source norm can be `Omega(H)`.

This is the exact amortization mechanism missed by the terminal atom-by-atom lift.

## 5. Strict lower-scale leakage

The flow `d_g` may change carry columns `q<=H`. Define

\[
\lambda_g(q)=L_q(d_g),
\qquad q\le H.
\tag{L-30601.9}
\]

Then the complete carry vector of `d_g` is

```text
prescribed profile g on H<q<=2H;
explicit leakage lambda_g on q<=H;
zero on q>2H.
```

Thus after subtracting the top-band source, every remaining correction is supported at the strict half endpoint `H`. No same-scale residue survives.

The leakage is emitted exactly by the finite formula

\[
\boxed{
\lambda_g(q)
=\sum_{n=H+1}^{2H}
[g(n)-g(n+1)]
\chi_{n,\lfloor n/2\rfloor}(q).
}
\tag{L-30601.10}
\]

A production certificate can replay every column with integer floors.

## 6. Application to the PR #304 obstruction

`R-30602` shows that the stopped-power cutoff boundary has size

\[
Q_N(q)\le-\frac1{40\sqrt q}
\]

on a positive-proportion top band. Its atomic lift costs `Omega(N)`.

On any subband on which `-Q_N` is nonincreasing, equations (L-30601.4) and (L-30601.8) realize the complete profile with `O(1)` negative capacity and export only an exact half-scale leakage.

For general source-bound profiles, partitioning at their finitely many monotonicity changes gives the same conclusion with cost controlled by weighted variation.

## 7. Proof boundary

Closed exactly:

1. the top-half step basis;
2. exact realization of every band profile;
3. the weighted one-sided-variation debt bound;
4. the `4B_H` bound for a monotone critical-size profile;
5. strict half-scale localization of every leakage row.

Open:

1. a uniform all-generation weighted-variation bound for the complete recombined boundary profiles;
2. an exact recurrence for the lower-scale leakages (L-30601.10);
3. Cycle Debt and RH.

The open recurrence is not assigned to reviewers as proof work. It is the next construction theorem after the exact refutations `R-30601/R-30602`.

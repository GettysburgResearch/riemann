# R-26901 — Signed odd-column load is not the dyadic RH hinge

Claim ID: `R-26901`  
Title: The signed odd-column load of the exact half-scale lift is automatically polylogarithmic; the odd target, not the leakage load, retains the inverse-zeta obstruction  
Status: **EXACT SCOPE CORRECTION / PROPOSED COMPLETE LEMMA**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: `L-26205`; PR #244 `L-23705`; elementary Möbius inversion  
Scope: correction of the first Odd-Leakage formulation; no RH conclusion

## 1. Odd Möbius divisor prefix

Define

\[
\mu_{\rm odd}(q)=\mu(q)\mathbf1_{2\nmid q}.
\]

For every integer `r>=1`,

\[
\sum_{d\mid r}\mu_{\rm odd}(d)
=
\mathbf1_{\{r\text{ is a power of }2\}}.
\tag{R-26901.1}
\]

Indeed the sum is the Möbius divisor sum of the odd part of `r`.

Put

\[
\lambda_2(x)
=
\begin{cases}
0,&x=0,\\
1+\lfloor\log_2x\rfloor,&x\ge1.
\end{cases}
\tag{R-26901.2}
\]

Then exact finite summation gives

\[
\boxed{
\sum_{\substack{q\le x\\q\text{ odd}}}
\mu(q)\left\lfloor{x\over q}\right\rfloor
=\lambda_2(x).
}
\tag{R-26901.3}
\]

## 2. Exact odd-column carry profile

Including `q=1` is harmless because `chi_(n,1)` is zero. Therefore

\[
\boxed{
\sum_{\substack{q\le n\\q\text{ odd}}}
\mu(q)\chi_{n,q}(j)
=\lambda_2(n)-\lambda_2(j)-\lambda_2(n-j).
}
\tag{R-26901.4}
\]

Averaging over `j` gives

\[
\Omega_n
:=
\sum_{\substack{q\le n\\q\text{ odd}}}
\mu(q)\beta_{nq}
=\lambda_2(n)
 -{2\over n+1}\sum_{j=0}^n\lambda_2(j).
\tag{R-26901.5}
\]

If

\[
2^K\le n<2^{K+1},
\]

then

\[
\sum_{j=0}^n\lambda_2(j)
=(K+1)(n+1)-2^{K+1}+1,
\]

and hence

\[
\boxed{
\Omega_n
=-(K+1)+{2(2^{K+1}-1)\over n+1}.
}
\tag{R-26901.6}
\]

In particular

\[
|\Omega_n|\ll1+\log(2n).
\tag{R-26901.7}
\]

## 3. The lifted odd-column load is automatic

Let `d=(d(n))_(2<=n<=Y)` be any nonnegative feasible carry vector at endpoint
`Y`. Use the exact odd-row lift from `L-26205`:

\[
(\mathcal L_2d)(2n+1)=2^{-1/2}d(n).
\]

Its odd-column load is

\[
\mathcal O_{Y,d}(r)
=2^{-1/2}
\sum_{n=r}^Yd(n)\beta_{2n+1,2r+1}.
\]

After complete signed recombination,

\[
\boxed{
\sum_{r=1}^Y\mu(2r+1)\mathcal O_{Y,d}(r)
=2^{-1/2}\sum_{n=2}^Yd(n)\Omega_{2n+1}.
}
\tag{R-26901.8}
\]

PR #244 `L-23705` proves for every feasible nonnegative carry vector that

\[
\sum_{n=2}^Yd(n)\sqrt n=O(\log^2Y).
\tag{R-26901.9}
\]

Since `1+log(2n)<<sqrt(n)`, equations (R-26901.7)--(R-26901.9) imply

\[
\boxed{
\left|
\sum_{r=1}^Y\mu(2r+1)\mathcal O_{Y,d}(r)
\right|
=O(\log^2Y).
}
\tag{R-26901.10}
\]

Thus the signed load created by odd-column leakage is already lower order. No
reflected estimate, Green solve, or blocker theorem is required for this part.

## 4. The odd target remains RH-bearing

The corresponding target coordinate is

\[
\mathcal R_{\rm odd}(X)
=
\sum_{\substack{q\le X\\q\text{ odd}}}
{\mu(q)\over\sqrt q}\log{X\over q}.
\tag{R-26901.11}
\]

Its Dirichlet series is

\[
\boxed{
\sum_{q\text{ odd}}{\mu(q)\over q^s}
={1\over(1-2^{-s})\zeta(s)}.
}
\tag{R-26901.12}
\]

The factor `1-2^(-s)` has no zero in `Re s>0`. Consequently a subpower bound
for (R-26901.11) is another exact RH criterion: every zeta zero to the right of
the critical line remains an uncancelled pole in its Mellin transform.

For the lifted vector, the signed odd residual is therefore

\[
\boxed{
\sum_{r=1}^Y\mu(2r+1)
\bigl[w_{2Y+1}(2r+1)-\mathcal O_{Y,d}(r)\bigr]
=
\mathcal R_{\rm odd}(2Y+1)+O(\log^2Y).
}
\tag{R-26901.13}
\]

The hard term is the odd target itself, not the signed leakage load.

## 5. Refuted shortcut and corrected pivot

The first formulation of `L-26205` described odd-column leakage as the sole
digital obstruction. That is correct columnwise for feasibility, but it is too
coarse for the signed RH-bearing scalar.

The following shortcut is invalid:

```text
exact even-column half-scale lift
+ bound the signed odd-column load
-> Dyadic Signed Slack.
```

The signed odd load is already polylogarithmic, while the odd target in
(R-26901.13) is itself RH-equivalent. Bounding only the leakage load cannot
contract the source.

The correct continuation is `L-26901`: apply an additional safe dyadic Euler
factor to the **target and load together**. The resulting source has a compact
pointwise carry wavelet, and every possible negative reflected Kummer row is
localized to `2m<=n<5m`.

## 6. Proof boundary

Closed exactly:

1. the odd Möbius divisor prefix;
2. the pointwise and averaged odd carry profiles;
3. the explicit binary-level formula for `Omega_n`;
4. the polylogarithmic signed odd-load bound for every feasible vector;
5. the RH-bearing transform of the odd target.

Open:

1. a contraction of the target and load after complete opposite-parity
   recombination;
2. the factor-five transition normal-Gram theorem of `L-26901`;
3. RH.

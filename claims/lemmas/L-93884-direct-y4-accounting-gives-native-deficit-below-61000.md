# L-93884 — Direct `Y_4` accounting gives native deficit below `61000`

Claim ID: `L-93884`  
Status: **PROPOSED COMPLETE DIRECT NATIVE-COST THEOREM**  
Depends on: `L-93883`; the elementary Chebyshev bound  
RH status: **unproved at this claim**

Let

\[
r_X(q)=\Omega_X(q)-\Xi(d_X)(q)\ge0
\]

and

\[
\delta_X=\sum_qY_4(q)r_X(q).
\]

## 1. Exact dual

Define

\[
Y_4(q)=\sum_{k=0}^{v_4(q)}2^k\Lambda(q/4^k).
\]

Then

\[
Y_4(q)-2\mathbf1_{4\mid q}Y_4(q/4)=\Lambda(q).
\]

Finite summation by parts gives

\[
\boxed{
J_\Lambda(X)-\mathcal H(d_X)
=
\sum_qY_4(q)r_X(q)
=\delta_X.
}
\tag{L-93884.1}
\]

## 2. Support and summability of `Y_4`

Writing `q=2^em` with `m` odd:

\[
Y_4(2^e)
=
(2^{\lceil e/2\rceil}-1)\log2,
\]

\[
Y_4(4^vp^a)=2^v\log p
\]

for odd prime `p`, and `Y_4(q)=0` otherwise.

Elementary summation yields

\[
\boxed{
\sum_{q\ge2}\frac{Y_4(q)}{q^{3/2}}<11
}
\tag{L-93884.2}
\]

and, with `L=log(2X)`,

\[
\boxed{
\sum_{q\le X}\frac{Y_4(q)}q
\le3+2L+2L^2.
}
\tag{L-93884.3}
\]

## 3. Thinning cost

The elementary binomial-coefficient proof gives

\[
\psi(x)<4(\log2)x.
\]

Stieltjes integration then gives

\[
J_\Lambda(X)<16(\log2)\sqrt X.
\]

Since

\[
1-\tau_K<\frac{130}{\sqrt K},
\]

\[
\boxed{
(1-\tau_K)J_\Lambda(X)<12012.
}
\tag{L-93884.4}
\]

## 4. Nonterminal comparison

Using (L-93883.6) and (L-93884.3),

\[
\sum_{q\le X/4}Y_4(q)
|\mathcal D_4v_q(C_X-E_X^I)|
\le
\frac{971}{4\sqrt K}(3+2L+2L^2).
\]

For `X>=10^12` this is less than `4`.

## 5. Terminal comparison

Equation (L-93883.9) and (L-93884.2) give

\[
\boxed{
\sum_qY_4(q)|e_X^{\rm term}(q)|
<
4452\cdot11=48972.
}
\tag{L-93884.5}
\]

## 6. Omissions and absent costs

The bottom omission has width two beginning at `K`; the top omission has fixed
width `W+2`. The endpoint score density obeys the elementary bound used by the
omission theorem, and their combined score is below `1` for `X>=10^12`.

The anchored identity block has no interpolation cost. There is no auxiliary
matrix port and no large-endpoint base packet.

## 7. Total

Therefore

\[
\boxed{
0\le\delta_X
<12012+4+48972+1
=60989<61000.
}
\tag{L-93884.6}
\]

This bound prices the actual numerical native slack. No source mass is assigned
to `r_X`, and no estimate of `J_\Lambda(X)-4\sqrt X` is used.

## 8. Boundary

```text
Y4 recurrence and support                   EXACT
thinning                                    <12012
nonterminal                                 <4
terminal                                    <48972
omissions                                   <1
port/base                                   0
native deficit                              <61000
endpoint implication                        L-93885/L-93886
```

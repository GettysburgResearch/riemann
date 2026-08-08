# L-32411 — The Q=4 Selberg reserve is a prime-free four-adic entropy ledger

Claim ID: `L-32411`  
Status: **PROPOSED COMPLETE EXACT ARITHMETIC IDENTITY — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: ordinary Kummer identity; ordinary Selberg carry identity; four-adic product-carry identity of PR #337 `L-32704`

## 1. Setup

Write

\[
 \Lambda_4=\Lambda+D,
 \qquad
 D(4^r)=d_r:=(4^r-1)\log4\quad(r\ge1),
\]

with `D(q)=0` elsewhere. For `n=j+k`, put

\[
 c_r=\chi_{n,4^r}(j),
 \qquad
 N_r=\left\lfloor\frac n{4^r}\right\rfloor,
 \qquad
 J_r=\left\lfloor\frac j{4^r}\right\rfloor.
\]

Let

\[
 F(n,j)=\log\binom nj,
\]

and

\[
 H_2(N)=\sum_{m=1}^N\log^2m.
\]

## 2. First moment

Ordinary Kummer gives

\[
 \sum_q\Lambda(q)\chi_{n,q}(j)=F(n,j).
\]

Therefore

\[
 \boxed{
 P_4(n,j)=F(n,j)+\sum_{r\ge1}d_rc_r.
 }
 \tag{L-32411.1}
\]

The sum is finite.

## 3. Four-adic product-carry identity

For `a=4^r`, every positive integer `q` satisfies

\[
 \boxed{
 \chi_{n,aq}(j)
 =\chi_{N_r,q}(J_r)
 +c_r\mathbf1_{q\mid N_r-J_r}.
 }
 \tag{L-32411.2}
\]

This is the exact borrow identity proved in PR #337: if the `a`-column has no carry, the quotient split is exact; if it has one carry, lowering the second child by one contributes precisely the divisor indicator of `N_r-J_r`.

Summing (L-32411.2) against the ordinary von Mangoldt sequence yields

\[
 \boxed{
 \sum_q\Lambda(q)\chi_{n,4^rq}(j)
 =F(N_r,J_r)+c_r\log(N_r-J_r),
 }
 \tag{L-32411.3}
\]

with the convention that the second term is zero when `c_r=0` (when `c_r=1`, `N_r-J_r>=1`).

## 4. Complete second moment

Expand

\[
 C_4=\Lambda_4\log+\Lambda_4*\Lambda_4
 =C_0+D\log+2\Lambda*D+D*D,
\]

where `C_0=Lambda log+Lambda*Lambda` is the ordinary Selberg sequence.

The ordinary Selberg carry identity gives

\[
 \sum_qC_0(q)\chi_{n,q}(j)
 =H_2(n)-H_2(j)-H_2(k).
 \tag{L-32411.4}
\]

The local logarithmic part is

\[
 \sum_{r\ge1}d_r\,r\log4\,c_r.
 \tag{L-32411.5}
\]

By (L-32411.3), the mixed part is

\[
 2\sum_{r\ge1}d_r
 \left[F(N_r,J_r)+c_r\log(N_r-J_r)\right].
 \tag{L-32411.6}
\]

Finally the local/local convolution contributes

\[
 \sum_{r,s\ge1}d_rd_s c_{r+s}.
 \tag{L-32411.7}
\]

Hence

\[
 \boxed{
 \begin{aligned}
 S_4(n,j)={}&H_2(n)-H_2(j)-H_2(k)\\
 &+\sum_{r\ge1}d_r r\log4\,c_r\\
 &+2\sum_{r\ge1}d_r
   [F(N_r,J_r)+c_r\log(N_r-J_r)]\\
 &+\sum_{r,s\ge1}d_rd_s c_{r+s}.
 \end{aligned}}
 \tag{L-32411.8}
\]

Every term on the right is an elementary function of the integer pair `(n,j)` and its base-four quotient/carry data. No prime or prime-power enumeration remains.

## 5. Prime-free reserve

Combining (L-32411.1) and (L-32411.8),

\[
 \boxed{
 \mathcal R_4(n,j)=P_4(n,j)^2-S_4(n,j)
 }
 \tag{L-32411.9}
\]

is a completely prime-free factorial/four-adic quantity.

This explains why the exact finite reserve scan of `X-32402` is stable: the prime enumeration used there is only one realization of an identity which can instead be checked from factorials, logarithm squares, and base-four carries.

## 6. Exact radix-four first-moment refinement

The first moment also has a useful exact scaling law. Let

\[
 \kappa_4(n,j)=\sum_{r\ge1}c_r
\]

be the number of nontrivial base-four carry levels. Since

\[
 \chi_{4n,4^r}(4j)=
 \begin{cases}
 0,&r=1,\\
 \chi_{n,4^{r-1}}(j),&r\ge2,
 \end{cases}
\]

one obtains

\[
 \boxed{
 \begin{aligned}
 P_4(4n,4j)-4P_4(n,j)
 ={}&\log\frac{\binom{4n}{4j}}{\binom nj^4}
 +3\log4\,\kappa_4(n,j).
 \end{aligned}}
 }
 \tag{L-32411.10}
\]

The right side is nonnegative. The binomial ratio is at least one because choosing `j` elements independently from each of four disjoint `n`-blocks injects into the set of all `4j`-subsets of a `4n`-set.

Thus

\[
 \boxed{P_4(4n,4j)\ge4P_4(n,j).}
 \tag{L-32411.11}
\]

The inequality is deterministic and contains no information about prime fluctuations.

## 7. Proof boundary

Closed exactly:

1. prime-free first moment;
2. prime-free complete Selberg forcing;
3. the full reserve as a four-adic entropy ledger;
4. exact radix-four first-moment refinement and monotonicity.

Not claimed here:

1. a corresponding sharp second-moment dissipation inequality;
2. an `R/n`-scale bound for the physical prime field;
3. RH.

Those remaining statements would control genuine prime fluctuations and must not be inferred from the deterministic reserve formula alone.

# L-91363 — The `P_61` finite-Euler row has positive rough-capacity and entropy densities

Claim ID: `L-91363`  
Status: **PROVED EXACT PHYSICAL-OUTPUT THEOREM — ROW COEFFICIENT SIGN SEPARATE**  
Created: 2026-08-13  
Depends on: retained component row `L-91112.25`; elementary double summation and Möbius convolution  
RH status: **unproved**

## 1. Finite-Euler component row

Put

\[
 P=P_{61}=\prod_{p\le61}p
\]

and define, for `X>=1` and integer `j>=2`,

\[
\boxed{
 D_{P,X}(j)
 =\sum_{\substack{d\mid P\\d\le X/j}}
  \frac{\mu(d)}{\sqrt d}Q_{X/d}(j),
}
\tag{L-91363.1
}

with causal zero extension.  The row coefficients are not assumed nonnegative in this theorem.

Let

\[
 H(Z)=\sum_{k\le Z}rac1{\sqrt k}\log\frac Zk,
 \qquad H(Z)=0\quad(Z<1).
\tag{L-91363.2}

For one positive component row, exact double summation gives the ordinary response

\[
\boxed{
 \sum_{j\ge2}Q_Y(j)\beta_{jq}
 =\frac1{\sqrt q}H(Y/q).
}
\tag{L-91363.3
}

The identity may be verified directly by inserting the definition of `Q_Y` and summing the second difference twice.

## 2. Positive rough-number ordinary capacity

Apply (L-91363.3) to (L-91363.1):

\[
\begin{aligned}
 C_{P,X}(q)
 &:=\sum_{j\ge2}D_{P,X}(j)\beta_{jq}\\
 &=\frac1{\sqrt q}
   \sum_{d\mid P}\frac{\mu(d)}{\sqrt d}
   H\!\left(\frac X{dq}\right).
\end{aligned}
\tag{L-91363.4}

Expand `H`, put `n=dk`, and use

\[
 \sum_{\substack{d\mid P\\d\mid n}}\mu(d)
 =\mathbf1_{(n,P)=1}.
\tag{L-91363.5}

This gives the exact positive formula

\[
\boxed{
 C_{P,X}(q)
 =\frac1{\sqrt q}H_P(X/q),
}
\tag{L-91363.6
}

where

\[
\boxed{
 H_P(Z)
 =\sum_{\substack{n\le Z\\(n,P)=1}}
  \frac1{\sqrt n}\log\frac Zn
 \ge0.
}
\tag{L-91363.7
}

Thus every ordinary physical column of the signed finite-Euler row is nonnegative.

## 3. Positive radix-four detail capacity

Since `2/sqrt(4q)=1/sqrt(q)`, the exact radix-four response is

\[
\boxed{
 \Theta_{P,X}(q)
 :=C_{P,X}(q)-2C_{P,X}(4q)
 =\frac1{\sqrt q}
  [H_P(Z)-H_P(Z/4)],
 \qquad Z=X/q.
}
\tag{L-91363.8
}

Separate the rough integers at `Z/4`:

\[
\boxed{
\begin{aligned}
 H_P(Z)-H_P(Z/4)={}&
 (\log4)
 \sum_{\substack{n\le Z/4\\(n,P)=1}}n^{-1/2}\\
 &+\sum_{\substack{Z/4<n\le Z\\(n,P)=1}}
 n^{-1/2}\log(Z/n).
\end{aligned}}
\tag{L-91363.9
}

Every term is nonnegative. Therefore

\[
\boxed{
 \Theta_{P,X}(q)\ge0
 \qquad(q\ge1).
}
\tag{L-91363.10
}

This is a cone-valued signed-detail certificate, not an inference from ordinary-column positivity.

## 4. Positive literal entropy density

Let

\[
 \mathcal E(Y)
 =\sum_{j\ge2}Q_Y(j)G_j
 =\sum_{2\le k\le Y}
  \frac{\log k}{\sqrt k}\log\frac Yk
\tag{L-91363.11}

be the literal average-binomial component entropy.  The finite-Euler entropy is

\[
 \mathcal E_P(X)
 =\sum_{d\mid P}\frac{\mu(d)}{\sqrt d}\mathcal E(X/d).
\tag{L-91363.12}

Putting `n=dk` gives

\[
\boxed{
 \mathcal E_P(X)
 =\sum_{n\le X}
  \frac{\lambda_P(n)}{\sqrt n}\log\frac Xn,
}
\tag{L-91363.13
}

where

\[
 \lambda_P(n)
 =\sum_{\substack{d\mid P\\d\mid n}}
  \mu(d)\log(n/d).
\tag{L-91363.14}

Let `r` be the number of distinct primes at most `61` dividing `n`.  Elementary Boolean differentiation gives

\[
\boxed{
 \lambda_P(n)=
 \begin{cases}
  \log n,&r=0,\\
  \log p,&r=1\text{ and }p\le61\text{ is that prime},\\
  0,&r\ge2.
 \end{cases}}
\tag{L-91363.15
}

Hence

\[
\boxed{
 \lambda_P(n)\ge0,
 \qquad
 \mathcal E_P(X)\ge0.
}
\tag{L-91363.16
}

The signed finite-Euler row therefore has a coefficientwise positive arithmetic entropy density even though its row coefficients have not yet been proved nonnegative.

## 5. Consequence for CFFP

For each complete labelled `P_61` forcing packet, the following physical outputs are now exact positive objects:

```text
ordinary carry capacity;                 H_P
radix-four detail capacity;              H_P(Z)-H_P(Z/4)
literal component entropy;               lambda_P>=0
```

The remaining CFFP issue is not a scalar sign or signed-detail sign.  It is:

> construct a nonnegative row vector whose ordinary/radix-four response stays within the positive capacities (L-91363.6)--(L-91363.10) and whose literal entropy loses at most a uniform mass-proportional amount relative to (L-91363.13).

The canonical signed row `D_(P,X)` is the first candidate; proving it nonnegative would close this interface immediately.

## 6. Proof boundary

```text
finite-Euler ordinary capacity density          EXACT / POSITIVE
finite-Euler radix-four detail density          EXACT / POSITIVE
finite-Euler literal entropy density            EXACT / POSITIVE
canonical finite-Euler row nonnegativity        OPEN
alternative nonnegative row realization         OPEN / CFFP
packet-envelope recursion                       AVAILABLE / T-91307
Riemann Hypothesis                              UNPROVEN
```

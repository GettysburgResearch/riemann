# L-91373 — The complete compact `P_61` canonical-row census is directed exact

Claim ID: `L-91373`  
Status: **PROVED EXACT COMPUTATIONAL THEOREM**  
Created: 2026-08-14  
Depends on: the retained component-row formula for `Q_Y(j)`  
RH status: **unproved**

## 1. Canonical row and event coefficients

Put

\[
 P_{61}=\prod_{p\le61}p
\]

and

\[
 D_{P,X}(j)=
 \sum_{d\mid P_{61}}\frac{\mu(d)}{\sqrt d}Q_{X/d}(j).
\tag{L-91373.1}
\]

Multiplying by `j(j-1)`, the component row has the event expansion

\[
 F_{j,X}:=j(j-1)D_{P,X}(j)
 =\sum_{n\le X}\frac{A_j(n)}{\sqrt n}\log\frac Xn,
\tag{L-91373.2}
\]

where

\[
 A_j(n)=
 \sum_{\substack{d\mid P_{61}\\d\mid n}}
 \mu(d)\,\Gamma_j(n/d),
\tag{L-91373.3}
\]

and

\[
 \Gamma_j(m)=
 \begin{cases}
 0,&m<j,\\
 j(j+1),&m=j,\\
 -(j+1)(j-2),&m=j+1,\\
 2,&m\ge j+2.
 \end{cases}
\tag{L-91373.4}
\]

On the integer cell `N<=X<N+1`, the logarithmic slope is

\[
 S_j(N)=\sum_{n\le N}\frac{A_j(n)}{\sqrt n},
\]

and continuity at activation knots gives the exact recurrence

\[
\boxed{
 F_{j,N+1}=F_{j,N}+S_j(N)\log\frac{N+1}{N}.
}
\tag{L-91373.5}
\]

## 2. Directed arithmetic

The companion proof object uses:

- exact integer coefficients `A_j(n)`;
- outward rational fixed-point enclosures for every `1/sqrt(n)`;
- the positive atanh expansion
  \[
  \log\frac{N+1}{N}
  =2\sum_{k\ge0}\frac{1}{(2k+1)(2N+1)^{2k+1}},
  \]
  with an explicit geometric tail;
- outward integer interval addition and multiplication.

No floating-point sign decision occurs.

## 3. Complete compact range

The checker proves

\[
\boxed{
 D_{P,X}(j)>0
}
\]

for every integer pair

\[
 2\le j\le510,
 \qquad
 j<X\le67j.
\tag{L-91373.6}
\]

The exact census size is

\[
\boxed{
 \sum_{j=2}^{510}66j
 =8{,}600{,}064.
}
\tag{L-91373.7}
\]

Every directed lower endpoint is positive.  The smallest retained values are

\[
 F_{2,3}>1.720242764866902,
\]

and

\[
 \sqrt3\,F_{2,3}>2.979547870102235.
\]

The retained verdict is

```text
PASS_DIRECTED_EVENT_CANONICAL_ROW
cells=8600064
failures=0
```

## 4. Count dictionary

The number `8,600,064` is the complete compact cell census in (L-91373.6).  The earlier narrative count `8,503,485` was a filtered event/fixed-point subcount and was not accompanied by a filter dictionary.  It is therefore retired from the proof statement.

No theorem uses a comparison between the two numbers.  The new packet has one transparent count and checks every compact integer cell.

## 5. Scope

This theorem independently closes the compact finite-cell part of the global canonical-row proposal.  It does not certify the analytic tail

```text
j>510, or X/j>67,
```

which must be reviewed from the Green/Kantorovich argument and the first-activation-strip lemma.

```text
compact canonical-row cells             DIRECTED EXACT
complete count                           8,600,064
first-strip orientation                  SEPARATE / L-91370
analytic large-row and large-ratio tail  SEPARATE REVIEW
full L-91364                             NOT PROMOTED BY THIS FILE ALONE
Riemann Hypothesis                       UNPROVEN
```

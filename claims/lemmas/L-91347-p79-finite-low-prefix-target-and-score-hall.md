# L-91347 — Every finite `P_79` low prefix has a uniform shifted-eight target and score Hall reserve

Claim ID: `L-91347`  
Status: **PROVED DIRECTED FINITE-PARAMETER THEOREM — COMMON TWO-LEDGER PACKET STILL SEPARATE**  
Created: 2026-08-13  
Depends on: `L-91342`, `L-91345-p79-one-prime-splice-has-a-monotone-two-ledger-kernel-and-large-prefix-reserve.md`; `X-91126`  
RH status: **unproved**

## 1. Setup

Let

\[
 P_{79}=\prod_{q\le79}q,
 \qquad p\ge83,
 \qquad 1\le y<83.
\]

For a squarefree divisor `d|P_79`, define the one-prime target and score atoms

\[
 K_a(d;p,y)
 =d^{-1/2}[a\sqrt{py/d}-3]\mathbf1_{d\le py}
 -p^{-1/2}d^{-1/2}[a\sqrt{y/d}-3]\mathbf1_{d\le y},
\]

with `a=4` for the SHARP target and `a=5` for the endpoint score.

For an active odd squarefree threshold `t<4096`, put

\[
 \mathcal H_{a,t}^{(8)}(p,y)
 =\sum_{\substack{e\le t+8\\\mu(e)=1}}K_a(e;p,y)
 -\sum_{\substack{o\le t\\\mu(o)=-1}}K_a(o;p,y).
\tag{L-91347.1}
\]

## 2. Cell formula

Define the fixed parent prefixes

\[
 A_t=\sum_{\substack{e\le t+8\\\mu(e)=1}}\frac1e
      -\sum_{\substack{o\le t\\\mu(o)=-1}}\frac1o,
\]

\[
 B_t=\sum_{\substack{e\le t+8\\\mu(e)=1}}\frac1{\sqrt e}
      -\sum_{\substack{o\le t\\\mu(o)=-1}}\frac1{\sqrt o},
\]

and let `A_t(y),B_t(y)` denote the same prefixes with the additional cutoff
`d<=y`.  Put

\[
 s=\sqrt y,
 \qquad u=\sqrt p.
\]

On every child activation cell the prefixes are constant and

\[
 \boxed{
 \mathcal H_{a,t}^{(8)}(p,y)
 =a s\left(uA_t-\frac{A_t(y)}u\right)
  -3B_t+\frac{3B_t(y)}u.
 }
\tag{L-91347.2}
\]

The shifted child margin

\[
 a\sqrt y\,A_t(y)-3B_t(y)
\]

is strictly positive, by the terminal `P_79` target/score Hall theorem and the
additional nonnegative even capacities through `t+8`.  Therefore (L-91347.2)
is strictly increasing in `u`.  Its minimum over the admissible prime range is
attained at

\[
 u=\sqrt{\max(83,t/y)}.
\tag{L-91347.3}
\]

## 3. Finite reduction in `y`

The child prefixes change only at the finitely many divisors of `P_79` below
`83`, together with the switch point `y=t/83`.

If `y>=t/83`, the minimizing prime is `p=83` and (L-91347.2) is affine in
`sqrt(y)`, so its minimum on one activation cell occurs at an endpoint.

If `y<=t/83`, then `p=t/y` and

\[
 \mathcal H_{a,t}^{(8)}
 =aA_t\sqrt t-3B_t
  -\frac{aA_t(y)}{\sqrt t}y
  +\frac{3B_t(y)}{\sqrt t}\sqrt y.
\tag{L-91347.4}
\]

This is a quadratic in `sqrt(y)`.  It is concave when `A_t(y)>=0`; when
`A_t(y)<0`, its global quadratic minimum is an explicit safe lower bound.  Thus
all parameters reduce to finitely many endpoint and critical-point inequalities.

## 4. Directed result

The standard-library checker `X-91126` uses exact `Fraction` arithmetic and
rational directed enclosures of every square root.  It enumerates:

```text
all odd P_79 thresholds t<4096;
all P_79 child activation cells 1<=y<83;
the split y=t/83;
both a=4 and a=5;
every endpoint and convex critical-point lower bound.
```

It proves the uniform inequalities

\[
 \boxed{
 \mathcal H_{4,t}^{(8)}(p,y)>1,
 \qquad
 \mathcal H_{5,t}^{(8)}(p,y)>1
 }
\tag{L-91347.5}
\]

for every

\[
 p\ge83,
 \qquad1\le y<83,
 \qquad t<4096.
\]

Together with `L-91345`, which proves the no-upward Hall theorem for every
`t>=4096`, this closes all scalar Hall feasibility for the `P_79` one-prime
splice.

## 5. Exact scope

The theorem provides two positive Ferrers transports:

```text
one in target-mass units;
one in score-mass units.
```

It does not identify them as one common transport.  A full one-prime packet must
still either:

1. construct one simultaneous target-exact, score-superordinate transport; or
2. use the bounded upward-edge correction packets to combine the two ledgers.

The inherited finite row itself is already strictly positive by `L-91346`.

```text
finite target Hall gate                  CLOSED DIRECTED
finite score Hall gate                   CLOSED DIRECTED
large-prefix Hall gate                   CLOSED ANALYTICALLY
inherited row splice                     CLOSED
common two-ledger positive packet        OPEN / FINITE
Riemann Hypothesis                       UNPROVED
```

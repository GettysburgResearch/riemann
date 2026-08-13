# L-91347 — Displacement eight is the exact global Ferrers radius for the `P_61` one-prime target

Claim ID: `L-91347`  
Status: **PROPOSED COMPLETE EXACT TARGET-TRANSPORT THEOREM — DIRECTED CERTIFICATE PROVIDED; INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-13  
Depends on: `L-91345`; replay `X-91126`; elementary Ferrers--Hall transport  
RH status: **unproved**

## 1. One-prime target atoms

Put

\[
 P_{61}=\prod_{q\le61}q
\]

and define causally

\[
 W_\Psi(x,d)=\left(\frac{4\sqrt x}{d}-\frac3{\sqrt d}\right)\mathbf1_{d\le x}.
\]

For real parameters

\[
 p\ge67,\qquad 1\le y\le67,\qquad x=py,
\]

define the positive one-prime atom

\[
 \boxed{
 K_{p,y}(d)=W_\Psi(x,d)-p^{-1/2}W_\Psi(y,d).
 }
\tag{L-91347.1}
\]

Positivity follows directly from endpoint monotonicity; equivalently it is the
one-prime source atom of `L-91339/L-91345`.

Let `E_(p,y)` and `O_(p,y)` be the positive measures on divisors of `P_61`
with `mu(d)=+1` and `mu(d)=-1`, respectively, carrying mass `K_(p,y)(d)`.

For an active odd threshold `t`, define the displacement-eight Hall margin

\[
\boxed{
 \mathcal H^{(8)}_{p,y}(t)
 =\sum_{\substack{e\mid P_{61},\ \mu(e)=1\\e\le\min(t+8,x)}}K_{p,y}(e)
  -\sum_{\substack{o\mid P_{61},\ \mu(o)=-1\\o\le t}}K_{p,y}(o).
}
\tag{L-91347.2}
\]

## 2. Two fixed finite prefixes

For every odd divisor threshold `t`, put

\[
 A_8(t)=
 \sum_{\substack{e\mid P_{61},\ \mu(e)=1\\e\le t+8}}\frac1e
 -\sum_{\substack{o\mid P_{61},\ \mu(o)=-1\\o\le t}}\frac1o,
\tag{L-91347.3}
\]

\[
 B_8(t)=
 \sum_{\substack{e\mid P_{61},\ \mu(e)=1\\e\le t+8}}\frac1{\sqrt e}
 -\sum_{\substack{o\mid P_{61},\ \mu(o)=-1\\o\le t}}\frac1{\sqrt o}.
\tag{L-91347.4}
\]

The directed replay streams all `2^18=262144` divisors and proves

\[
\boxed{A_8(t)>\frac1{67}}
\tag{L-91347.5}
\]

for every odd threshold.  It also proves the stronger correlated inequalities

\[
\boxed{
 4\sqrt{t+8}\left(A_8(t)-\frac3{4\cdot67}\right)-3B_8(t)
 >\frac95
}
\tag{L-91347.6}
\]

when `t+8<=67^2`, and

\[
\boxed{
 4A_8(t)\sqrt{t+8}-3B_8(t)-\frac{201}{\sqrt{t+8}}
 >\frac95
}
\tag{L-91347.7}
\]

when `t+8>67^2`.

The least directed lower endpoint is

\[
 1.840541861155008\ldots
\]

at `t=47`.

## 3. Uniform child-prefix envelope

For `1<=y<=67` and every threshold `t>=2`, let

\[
 \mathcal C_y^{(8)}(t)
 =\sum_{\substack{e\mid P_{61},\ \mu(e)=1\\e\le\min(t+8,y)}}W_\Psi(y,e)
 -\sum_{\substack{o\mid P_{61},\ \mu(o)=-1\\o\le\min(t,y)}}W_\Psi(y,o).
\tag{L-91347.8}
\]

A finite directed check on every activation cell proves

\[
\boxed{
 \mathcal C_y^{(8)}(t)<3\sqrt y.
}
\tag{L-91347.9}
\]

The retained maximum of `C/sqrt(y)` is below `2.694`; the theorem uses only the
rational envelope `3`.

## 4. Nonterminal Hall margin

Assume first that

\[
 x=py\ge t+8.
\]

All parent capacities through `t+8` are active, and (L-91347.2) splits exactly as

\[
 \mathcal H^{(8)}_{p,y}(t)
 =4\sqrt x\,A_8(t)-3B_8(t)
  -p^{-1/2}\mathcal C_y^{(8)}(t).
\tag{L-91347.10}
\]

By (L-91347.9),

\[
 \mathcal H^{(8)}_{p,y}(t)
 >4\sqrt x\,A_8(t)-3B_8(t)-\frac{3y}{\sqrt x}.
\tag{L-91347.11}
\]

The constraints `p>=67` and `y<=67` give

\[
 y\le\min\left(67,\frac x{67}\right).
\]

If `x<=67^2`, the right side of (L-91347.11) is at least

\[
 \sqrt x\left(4A_8(t)-\frac3{67}\right)-3B_8(t).
\]

Its coefficient of `sqrt(x)` is positive by (L-91347.5), so its minimum on
`x>=t+8` occurs at `x=t+8`.  Equation (L-91347.6) gives

\[
 \mathcal H^{(8)}_{p,y}(t)>\frac95.
\]

If `x>=67^2`, the right side is at least

\[
 4A_8(t)\sqrt x-3B_8(t)-\frac{201}{\sqrt x},
\]

which is strictly increasing in `x`.  Equation (L-91347.7) again gives

\[
\boxed{
 \mathcal H^{(8)}_{p,y}(t)>\frac95
 \qquad(x\ge t+8).
}
\tag{L-91347.12}
\]

## 5. Terminal thresholds

Suppose instead that

\[
 t\le x<t+8.
\]

Then every active even atom lies in the capacity neighborhood of `t`, while the
Hall demand omits any active odd atom above `t`.  Consequently

\[
 \mathcal H^{(8)}_{p,y}(t)
 \ge \mathcal T_{61;p}(x),
\]

where `T_(61;p)` is the complete signed target of `L-91345`.  That theorem gives

\[
 \mathcal T_{61;p}(x)>\frac9{50}\sqrt x>0.
\]

Combining with (L-91347.12),

\[
\boxed{
 \mathcal H^{(8)}_{p,y}(t)>0
}
\tag{L-91347.13}
\]

for every active odd threshold.

The nested-neighborhood Hall theorem therefore supplies a positive transport

\[
\boxed{
 \pi_{p,y}:O_{p,y}\longrightarrow E_{p,y},
 \qquad e\le o+8,
}
\tag{L-91347.14}
\]

using all odd target demand and no more than the even target capacities.

## 6. Radius eight is minimal

At the odd threshold `t=47`, no new even divisor occurs between `51` and `54`,
while the even state `55` first enters at displacement eight.  Exact reciprocal
arithmetic gives

\[
 A_7(47)
 =-\frac{184943596214571}{204963260862830470}<0.
\tag{L-91347.15}
\]

The same prefix occurs for every displacement `s<=7` after the corresponding
smaller capacity set is used.  Fixing `y=1` and sending `p` to infinity, the
parent Hall margin has leading term

\[
 4\sqrt p\,A_s(47),
\]

while all remaining terms are lower order.  Hence the Hall margin tends to
`-infinity` for every `s<=7`.

Thus

\[
\boxed{
 8\text{ is the minimal fixed additive Ferrers radius for the global }P_{61}
 \text{ one-prime target family.}
}
\tag{L-91347.16}

## 7. Scope

The theorem closes target-mass transport, globally in the unbounded rough-prime
parameter.  It does not yet prove that a chosen displacement-eight transport is
simultaneously score-superordinate and row-subordinate.  `L-91345` supplies the
strict scalar score surplus and `L-91346` supplies the strict inherited-row
reserve needed for that final bounded-transport comparison.

```text
P_61 displacement-eight target Hall             DIRECTED/EXACT
nonterminal Hall reserve >9/5                    DIRECTED/EXACT
terminal Hall positivity                         EXACT FROM L-91345
minimality against every radius <=7              EXACT
score superordination of one common transport    OPEN
row subordination of one common transport        OPEN
activation/frontier source typing                OPEN
Riemann Hypothesis                               UNPROVEN
```
